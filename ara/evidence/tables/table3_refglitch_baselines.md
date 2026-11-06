# Table 3: RefGlitch-Bench Reference Selection Policies and Ablation

* **Source:** Yu et al., *RefGlitch-Bench: A Benchmark for Reference-based Gameplay Glitch Detection with Vision-Language Models*, Sony Interactive Entertainment / UAlberta 2026, Tables 2, 3 & 4.
* **Corresponds to:** Claim [C02](../../logic/claims.md#c02-reference-guided-lastcleanframe-performance-recovery).

## Section A: Reference Selection Strategy Performance (Qwen3-VL-8B Backbone)

| Strategy | Accuracy | F1 Score | Precision | Recall | Qualitative Behavior |
|---|---|---|---|---|---|
| **Oracle Reference ($Ref$)** | **0.73** | **0.74** | 0.72 | **0.76** | Human-selected verified clean frame (Upper Bound) |
| **LastCleanFrame (LCF)** | **0.70** | **0.69** | 0.70 | **0.69** | Most recent predicted clean frame; high contrast |
| **RandomFrame** | 0.67 | 0.66 | 0.68 | 0.63 | Arbitrary previous frame; stochastic quality |
| **PreviousFrame ($t-1$)** | 0.61 | 0.57 | 0.64 | 0.51 | Lacks contrast when bug persists across frames |
| **MostSimilarFrame (CLIP)** | 0.60 | 0.54 | 0.64 | 0.47 | Often retrieves buggy frame with same background |
| **NoRef (Single Frame Baseline)**| 0.62 | 0.42 | **0.88** | 0.28 | Conservative; misses subtle rendering defects |

---

## Section B: Real-World Benchmark Transfer (1,000 Frames from PhysGame & VideoGameQA-Bench)

| Condition | Strategy | Accuracy | F1 Score | Precision | Recall |
|---|---|---|---|---|---|
| **Real-World Gameplay Evaluation** | **LastCleanFrame** | **0.60** | **0.70** | **0.56** | 0.91 |
| **Real-World Gameplay Evaluation** | **NoRef Baseline** | 0.54 | 0.67 | 0.52 | **0.92** |

---

## Section C: Reference Contamination Analysis (Impact of Mispredicted References)

| Reference Status Condition | # Evaluated Frames | Ground Truth Glitch (GT=1) | Ground Truth Clean (GT=0) | True Positive Rate (TPR) | False Positive Rate (FPR) |
|---|---|---|---|---|---|
| **Truly Glitch-Free Reference** | 367 | 156 | 211 | **0.94** | **0.58** |
| **Contaminated / Glitchy Reference** | 184 | 147 | 37 | 0.82 | **0.84** (Catastrophic Error Spike) |
| **Has No Reference Available** | 449 | 197 | 252 | 0.94 | 0.78 |
