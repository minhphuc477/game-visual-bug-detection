# Falsifiable Research Claims

## C01: Static VLM Triage vs. Temporal Needle-in-a-Haystack Collapse
* **Statement:** General-purpose Vision-Language Models (VLMs) demonstrate viable zero-shot glitch detection accuracy ($\ge 75\%$) on static standalone screenshots across diverse game genres, but experience a catastrophic performance collapse ($<20\%$ accuracy) when tasked with temporal timestamp localization in continuous gameplay video streams (Needle-in-a-Haystack).
* **Status:** Verified empirically across 16 VLM backbones.
* **Falsification Criteria:** Any commercial or open-weight VLM achieving $\ge 50\%$ accuracy on the 50-second NIAH task in *VideoGameQA-Bench* under 1 FPS uniform sampling without specialized video temporal fine-tuning would refute this claim.
* **Proof Pointer:** [Experiment E01](experiments.md#e01-vlm-static-vs-temporal-niah-benchmark) $\rightarrow$ [Table 1](../evidence/tables/table1_videogameqa_bench.md).
* **Evidence Basis:** GPT-4.1 scores 81.3% on Image Glitch Detection (IGD) but only 19.0% on NIAH; GPT-4.1-mini achieves 76.8% on IGD and 10.0% on NIAH; GPT-4o scores 82.8% on IGD and collapses to 1.0% on NIAH (*VideoGameQA-Bench*, NeurIPS 2025).
* **Interpretation:** Static image glitch detection relies on recognizing texture or geometry corruption patterns (e.g., magenta null textures, stretched polygons), which are represented in internet-scale VLM pretraining. Video NIAH requires continuous spatio-temporal tracking, frame-difference memory, and temporal grounding, which current frame-by-frame VLM tokenizers cannot perform natively.
* **Dependencies:** None.
* **Tags:** `VLM`, `benchmark`, `temporal-defect`, `NIAH`.

---

## C02: Reference-Guided LastCleanFrame Performance Recovery
* **Statement:** Conditioning VLM glitch predictions on a dynamic within-video reference frame (*LastCleanFrame*) recovers significant detection performance, improving F1 score by up to +0.27 over unguided single-frame inference (*NoRef*) by transforming open-ended anomaly detection into a localized contrastive comparison.
* **Status:** Verified empirically across 5 VLM backbones.
* **Falsification Criteria:** If *LastCleanFrame* achieves an F1 score equal to or lower than *NoRef* on *RefGlitch-Bench* or real-world gameplay video benchmarks, this claim is falsified.
* **Proof Pointer:** [Experiment E02](experiments.md#e02-reference-frame-selection-policy-evaluation) $\rightarrow$ [Table 3](../evidence/tables/table3_refglitch_baselines.md).
* **Evidence Basis:** On *RefGlitch-Bench* with Qwen3-VL-8B, *NoRef* achieves F1 = 0.42 (Precision 0.88, Recall 0.28). Supplying *LastCleanFrame* elevates F1 to 0.69 (Precision 0.70, Recall 0.69) and accuracy to 0.70 (+0.08 over baseline). The oracle reference frame achieves F1 = 0.74 (*RefGlitch-Bench*, 2026).
* **Interpretation:** In artistic virtual worlds, an unfamiliar asset layout or unusual shading cannot be verified as correct without context. A clean temporal reference from the same scene anchors the model's visual expectation, dramatically reducing false alarms and boosting sensitivity to sudden missing objects and texture corruptions.
* **Dependencies:** C01.
* **Tags:** `reference-guidance`, `prompt-engineering`, `oracle`, `F1-score`.

---

## C03: Engine-State Telemetry Fusion Eliminates Stylistic False Alarms
* **Statement:** Multimodal fusion combining raw viewport RGB pixels with engine-internal G-buffer telemetry (depth buffers, surface normal vectors, and collision hull bounding queries) eliminates $\ge 40\%$ of false alarms caused by stylized visual effects (fog, particle systems, semi-transparent materials) compared to RGB-only detectors.
* **Status:** Verified on commercial Unreal Engine 5 environments.
* **Falsification Criteria:** If an RGB-only detector demonstrates equivalent or lower false discovery rate ($FDR$) than an engine-telemetry fused network across stylized weather and atmospheric scenes, this claim is refuted.
* **Proof Pointer:** [Experiment E03](experiments.md#e03-multimodal-engine-telemetry-ablation) $\rightarrow$ [Table 4](../evidence/tables/table4_stateglitch_fusion.md).
* **Evidence Basis:** Kovacs et al. (ESWA 2026) show that incorporating depth maps and collision queries reduces false positive rate from 28.4% (RGB-only ResNet) to 16.5% (multimodal fusion), eliminating 41.9% of spurious glitch flags in *StateGlitch-3D*.
* **Interpretation:** RGB pixels do not convey whether two overlapping visual surfaces correspond to a valid physical collision or an illegal mesh penetration. Engine G-buffers provide exact metric depth and transform matrices, allowing the model to distinguish volumetric atmospheric fog from rendering corruption.
* **Dependencies:** None.
* **Tags:** `multimodal`, `telemetry`, `G-buffer`, `false-positives`.

---

## C04: Cross-Game Art-Style Domain Degradation
* **Statement:** Supervised and semi-supervised visual defect detectors suffer a catastrophic performance degradation ($\ge 35\%$ reduction in mean Average Precision, mAP) when evaluated cross-game on target titles with divergent visual rendering aesthetics (photorealistic vs. cel-shaded vs. voxel).
* **Status:** Verified across 5 commercial and experimental titles.
* **Falsification Criteria:** Any vision model trained on a single source game title that achieves $\ge 85\%$ of its in-distribution mAP when transferred zero-shot to a divergent art style without fine-tuning falsifies this claim.
* **Proof Pointer:** [Experiment E04](experiments.md#e04-cross-game-domain-transfer-benchmark).
* **Evidence Basis:** Yi et al. (AIIDE 2025) demonstrate that transferring an object detection model trained on realistic Unreal demo *GiantMap* to distinct gameplay titles suffers substantial recall and mAP drops; hybrid co-finetuning with co-domain data recovers +18.4% mAP but cannot eliminate the cross-style gap.
* **Interpretation:** Deep convolutional and transformer backbones bind glitch features to texture statistics and edge distributions. When shaders, polygon budgets, and lighting models change completely, learned representation weights fail to activate.
* **Dependencies:** C01, C03.
* **Tags:** `domain-transfer`, `generalisation`, `cross-game`, `mAP`.

---

## C05: Negative-Space Weak Supervision Achieves Extreme Label Efficiency
* **Statement:** In egocentric 3D gameplay viewports, weakly supervised domain-specific augmentation leveraging zero-shot foundation segmentation (SAM) and canonical viewport priors achieves $\ge 90\%$ glitch classification accuracy using $\le 15$ human-annotated exemplar frames.
* **Status:** Verified on Xbox QuAIL GiantMap-4/GM50 benchmarks.
* **Falsification Criteria:** Requiring more than 50 human-labeled glitch frames to exceed 85% balanced accuracy on first-person player clipping would refute this claim.
* **Proof Pointer:** [Experiment E05](experiments.md#e05-weak-supervision-label-efficiency) $\rightarrow$ [Table 5](../evidence/tables/table5_xbox_weak_supervision.md).
* **Evidence Basis:** Rahman (BMVC 2023) demonstrates that a Vision Transformer (ViT-Base-16) pretrained on DINOv1 with a crop prior achieves 95.2% accuracy on GM4-Tiny using only 15 total training samples, and achieves 97.9% accuracy with CLIP pretraining on 156 samples.
* **Interpretation:** Ground-truth visual bug annotations are scarce in early game production. By recognizing that weapon clipping always intersects the egocentric view invariant, pasting segmented game assets over vs. under weapon masks synthesizes realistic training distributions with zero human manual glitch drawing.
* **Dependencies:** None.
* **Tags:** `weak-supervision`, `SAM`, `DINO`, `label-efficiency`.
