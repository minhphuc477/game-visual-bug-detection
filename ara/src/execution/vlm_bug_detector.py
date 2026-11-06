#!/usr/bin/env python3
"""
vlm_bug_detector.py: Zero-shot VLM Bug Triage & LLM-as-a-Judge Pipeline
Implements the methodology of Taesiri et al. (NeurIPS 2025) and Lu et al. (FSE 2026).
"""

from __future__ import annotations

import json
import logging
from dataclasses import dataclass
from typing import Any, Dict, Optional, Tuple

logger = logging.getLogger("vlm_detector")


@dataclass
class DetectionResult:
    is_glitch: bool
    reasoning: str
    glitch_description: str
    confidence: float
    raw_response: str
    judge_confirmed: Optional[bool] = None


class VLMBugDetector:
    def __init__(self, client: Any, detector_model: str = "gpt-4.1-mini", judge_model: str = "gpt-5-mini"):
        self.client = client
        self.detector_model = detector_model
        self.judge_model = judge_model

    @staticmethod
    def construct_system_prompt() -> str:
        return (
            "You are a senior video game Quality Assurance (QA) engineer specializing in automated visual bug triage.\n"
            "Your task is to analyze the provided gameplay keyframe and determine whether it exhibits a visible defect.\n"
            "Defect categories include: mesh clipping, missing textures (magenta nulls), broken UI overlaps, T-pose animation freezes, "
            "and abnormal shadow detachment.\n\n"
            "CRITICAL: You must reason thoroughly in the 'reasoning' field BEFORE setting the boolean 'glitch_detected'.\n"
            "Respond in valid JSON only conforming to this schema:\n"
            "{\n"
            '  "reasoning": "Step-by-step observation of scene geometry, shaders, lighting, and HUD",\n'
            '  "glitch_detected": true or false,\n'
            '  "description_of_glitch": "Concise bug report description if detected, else empty string",\n'
            '  "confidence": 0.0 to 1.0\n'
            "}"
        )

    def analyze_frame(self, image_data: Any) -> DetectionResult:
        """Execute primary baseline VLM inference."""
        prompt = self.construct_system_prompt()
        # Simulated or actual client API invocation
        response = self.client.chat.completions.create(
            model=self.detector_model,
            messages=[
                {"role": "system", "content": prompt},
                {"role": "user", "content": [{"type": "image_url", "image_url": {"url": image_data}}]},
            ],
            temperature=0.0,
            response_format={"type": "json_object"},
        )
        payload = json.loads(response.choices[0].message.content)
        return DetectionResult(
            is_glitch=payload.get("glitch_detected", False),
            reasoning=payload.get("reasoning", ""),
            glitch_description=payload.get("description_of_glitch", ""),
            confidence=payload.get("confidence", 1.0),
            raw_response=response.choices[0].message.content,
        )

    def verify_with_judge(self, image_data: Any, primary_result: DetectionResult) -> DetectionResult:
        """Execute secondary Judge VLM to arbitrate and filter false positives."""
        if not primary_result.is_glitch:
            primary_result.judge_confirmed = False
            return primary_result

        judge_prompt = (
            "You are an arbitration judge in a game studio QA pipeline.\n"
            f"The primary detector flagged this frame as a bug with rationale:\n'{primary_result.reasoning}'\n"
            f"Proposed defect: '{primary_result.glitch_description}'.\n\n"
            "Verify whether this is a bona fide bug or an intentional artistic/gameplay element (fog, stylistic shader, character customization).\n"
            "Respond strictly in JSON:\n"
            '{"confirm_bug": true or false, "arbitration_rationale": "..."}'
        )

        response = self.client.chat.completions.create(
            model=self.judge_model,
            messages=[
                {"role": "system", "content": judge_prompt},
                {"role": "user", "content": [{"type": "image_url", "image_url": {"url": image_data}}]},
            ],
            temperature=0.0,
            response_format={"type": "json_object"},
        )
        payload = json.loads(response.choices[0].message.content)
        primary_result.judge_confirmed = payload.get("confirm_bug", False)
        return primary_result
