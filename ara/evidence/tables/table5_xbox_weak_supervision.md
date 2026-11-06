# Table 5: Xbox QuAIL Weak Supervision and Low-Data Clipping Regimes

* **Source:** Rahman, *Weak Supervision for Label Efficient Visual Bug Detection in Video Games*, British Machine Vision Conference (BMVC 2023), Tables 1 & 2.
* **Corresponds to:** Claim [C05](../../logic/claims.md#c05-negative-space-weak-supervision-achieves-extreme-label-efficiency).

## Section A: In-Distribution Performance on GM4-Tiny Dataset (15 Total Samples)

| Architecture | Pretraining Method | Spatial Prior | Test Accuracy |
|---|---|---|---|
| **ResNet-18** | ImageNet-1k Supervised | Weapon Crop | 0.753 $\pm$ 0.04 |
| **ResNet-50** | ImageNet-1k Supervised | Full Frame | 0.733 $\pm$ 0.05 |
| **ResNet-50** | ImageNet-1k Supervised | Weapon Crop | 0.811 $\pm$ 0.06 |
| **ViT-Base-16** | ImageNet-1k Supervised | Full Frame | 0.738 $\pm$ 0.02 |
| **ViT-Base-16** | ImageNet-1k Supervised | Weapon Crop | 0.913 $\pm$ 0.03 |
| **ViT-Base-16** | CLIP Image Encoder | Weapon Crop | 0.949 $\pm$ 0.03 |
| **ViT-Base-16** | **DINOv1 (Self-Supervised)** | **Weapon Crop** | **0.952 $\pm$ 0.03** |

---

## Section B: In-Distribution Performance on GM5-Base Dataset (156 Total Samples)

| Architecture | Pretraining Method | Spatial Prior | Test Accuracy |
|---|---|---|---|
| **ResNet-50** | ImageNet-1k Supervised | Weapon Crop | 0.958 $\pm$ 0.02 |
| **ViT-Base-16** | ImageNet-1k Supervised | Weapon Crop | 0.965 $\pm$ 0.02 |
| **ViT-Base-16** | DINOv1 | Weapon Crop | 0.976 $\pm$ 0.02 |
| **ViT-Base-16** | **CLIP Image Encoder** | **Weapon Crop** | **0.979 $\pm$ 0.02** |

---

## Section C: Low-Prevalence Video Deployment (Prevalence = 0.007, 46 OOD Objects)

| Training Methodology | Labeled Training Images | F1 Score on Video Stream |
|---|---|---|
| **Supervised Fine-Tuning (SFT Baseline)** | 156 samples | 0.336 |
| **Weak Supervision Alone (Zero Bug Labels)** | 5 clean exemplar frames | **0.529** (+57.4% relative gain) |
| **Weak Supervision + SFT Multi-Tasking** | 5 exemplars + 156 samples | **0.550** (+63.7% relative gain) |
