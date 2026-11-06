#!/usr/bin/env python3
"""
reference_guided_eval.py: Reference-Guided Sequential Prompting (RefGlitch-Bench)
Implements the methodology of Yu et al. (Sony Interactive Entertainment / UAlberta 2026).
"""

from __future__ import annotations

import json
from dataclasses import dataclass
from typing import Any, List, Optional, Tuple


@dataclass
class FrameEvaluation:
    frame_index: int
    timestamp_sec: float
    is_glitch: bool
    reference_frame_index: Optional[int]
    reference_was_clean: Optional[bool]
    reasoning: str


class ReferencePoolManager:
    def __init__(self, policy: str = "LastCleanFrame", max_history: int = 50):
        self.policy = policy
        self.max_history = max_history
        self.pool: List[Tuple[int, Any, bool]] = []  # (index, image_tensor, is_glitch)

    def deposit(self, frame_index: int, image_data: Any, is_glitch: bool) -> None:
        self.pool.append((frame_index, image_data, is_glitch))
        if len(self.pool) > self.max_history:
            self.pool.pop(0)

    def select_reference(self) -> Optional[Tuple[int, Any, bool]]:
        if not self.pool:
            return None

        if self.policy == "LastCleanFrame":
            for idx, img, is_glitch in reversed(self.pool):
                if not is_glitch:
                    return idx, img, False
            # Fallback to earliest frame if no clean frame is in pool
            return self.pool[0]

        elif self.policy == "PreviousFrame":
            return self.pool[-1]

        raise ValueError(f"Unsupported reference policy: {self.policy}")


class ReferenceGuidedEvaluator:
    def __init__(self, vlm_client, model_name: str = "qwen3-vl-8b", policy: str = "LastCleanFrame"):
        self.client = vlm_client
        self.model_name = model_name
        self.pool_manager = ReferencePoolManager(policy=policy)

    def evaluate_frame(self, frame_index: int, timestamp: float, image_data: Any) -> FrameEvaluation:
        ref_selection = self.pool_manager.select_reference()

        if ref_selection is None:
            # Cold-start: Single-frame evaluation
            prompt = (
                "Determine if this game screenshot contains any visible visual defect or rendering bug.\n"
                "Respond in JSON: {'reasoning': str, 'glitch_detected': bool}"
            )
            images_payload = [image_data]
            ref_idx, ref_clean = None, None
        else:
            ref_idx, ref_img, ref_is_glitch = ref_selection
            ref_clean = not ref_is_glitch

            if ref_clean:
                prompt = (
                    "Image 1 is a verified NORMAL reference baseline from earlier in the same scene.\n"
                    "Image 2 is the test frame under review.\n"
                    "Compare Image 2 against Image 1. Flag noticeable visual discrepancies (missing objects, clipping, broken textures) as bugs.\n"
                    "Respond in JSON: {'reasoning': str, 'glitch_detected': bool}"
                )
            else:
                prompt = (
                    "WARNING: Image 1 is an earlier frame that was flagged as GLITCHY.\n"
                    "Image 2 is the test frame under review.\n"
                    "Evaluate whether Image 2 also contains evidence of a bug.\n"
                    "Respond in JSON: {'reasoning': str, 'glitch_detected': bool}"
                )
            images_payload = [ref_img, image_data]

        response = self.client.generate(prompt=prompt, images=images_payload)
        parsed = json.loads(response)
        is_glitch = parsed.get("glitch_detected", False)
        reasoning = parsed.get("reasoning", "")

        # Deposit result into temporal reference pool
        self.pool_manager.deposit(frame_index, image_data, is_glitch)

        return FrameEvaluation(
            frame_index=frame_index,
            timestamp_sec=timestamp,
            is_glitch=is_glitch,
            reference_frame_index=ref_idx,
            reference_was_clean=ref_clean,
            reasoning=reasoning,
        )
