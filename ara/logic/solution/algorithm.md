# Mathematical Formulations and Algorithm Blueprints

## 1. Co-Supervised and Latent Distillation Objective (Yi et al., 2025)

The visual bug detector balances object detection across multiple game titles while leveraging unlabeled gameplay video through a self-supervised latent masked autoencoder objective:

$$\mathcal{L}_{\text{total}} = \mathcal{L}_{\text{co\_sup}} + \beta \mathcal{L}_{\text{ssl}}$$

Where the co-supervised loss combines target game annotations with auxiliary co-domain titles:

$$\mathcal{L}_{\text{co\_sup}} = \mathcal{L}_{\text{od}}^{\text{downstream}} + \alpha \mathcal{L}_{\text{od}}^{\text{co-title}}$$

$$\mathcal{L}_{\text{od}} = \frac{1}{N_{\text{cls}}} \sum_{i} \mathcal{L}_{\text{cls}}(p_i, p_i^*) + \frac{\lambda}{N_{\text{loc}}} \sum_{i} p_i^* \mathcal{L}_{\text{smooth\_L1}}(t_i, t_i^*)$$

The self-supervised target distillation loss ($\mathcal{L}_{\text{ssl}}$) measures the Mean Squared Error between the reconstructed latent representation from the student encoder and the frozen target encoder on masked patch indices $\mathcal{M}$:

$$\mathcal{L}_{\text{ssl}} = \frac{1}{|\mathcal{M}|} \sum_{j \in \mathcal{M}} \left\| \mathbf{z}_{\text{student}}^{(j)} - \mathbf{z}_{\text{target}}^{(j)} \right\|_2^2$$

---

## 2. Reference-Guided Sequential Prompting Algorithm (Yu et al., 2026)

```python
from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass

@dataclass
class KeyframeRecord:
    frame_id: int
    timestamp_sec: float
    image_tensor: object
    predicted_glitch: bool
    confidence: float
    rationale: str

class ReferenceGuidedDetector:
    def __init__(self, vlm_client, similarity_threshold: float = 0.65):
        self.vlm = vlm_client
        self.sim_threshold = similarity_threshold
        self.reference_pool: List[KeyframeRecord] = []

    def select_reference(self, current_frame) -> Optional[KeyframeRecord]:
        """
        Implements LastCleanFrame policy:
        Traverses pool in reverse chronological order to find the latest verified clean frame.
        """
        for record in reversed(self.reference_pool):
            if not record.predicted_glitch:
                return record
        return None  # Pool has no clean frame; fallback to single-frame prompt

    def evaluate_video_stream(self, keyframes: List[Tuple[int, float, object]]) -> List[KeyframeRecord]:
        results: List[KeyframeRecord] = []
        
        for frame_id, t_sec, img in keyframes:
            ref_record = self.select_reference(img)
            
            if ref_record is None:
                # Cold start: Frame 1 or no clean reference found
                prompt = self.construct_single_frame_prompt(img)
                response = self.vlm.generate(prompt, image=img)
            else:
                # Reference-guided paired prompt
                prompt = self.construct_paired_prompt(
                    test_image=img,
                    ref_image=ref_record.image_tensor,
                    ref_is_clean=not ref_record.predicted_glitch
                )
                response = self.vlm.generate(prompt, images=[ref_record.image_tensor, img])
            
            record = KeyframeRecord(
                frame_id=frame_id,
                timestamp_sec=t_sec,
                image_tensor=img,
                predicted_glitch=response["is_glitch"],
                confidence=response.get("confidence", 1.0),
                rationale=response.get("reasoning", "")
            )
            
            self.reference_pool.append(record)
            results.append(record)
            
        return results
```

---

## 3. Computational Complexity Analysis

- **Keyframe Downsampling:** Downsampling 60 FPS video to I-frames ($\sim 1$ FPS) reduces frame volume by a factor of 60 ($O(T) \to O(T/60)$).
- **Reference Selection:** Linear backward search over sliding pool $\mathcal{P}$ of size $K \le 50$ requires $O(K)$ time, which is negligible ($< 1$ ms) compared to model inference.
- **VLM Inference:** Bound by vision tokenizer and transformer forward pass: $O(N_{\text{patches}}^2 + L \cdot d)$, requiring approximately 250–800 ms per frame on modern GPU hardware (NVIDIA L40S / RTX 4090).
