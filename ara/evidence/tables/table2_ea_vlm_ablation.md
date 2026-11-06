# Table 2: Electronic Arts 41-Hour Gameplay Keyframe QA Ablation

* **Source:** Lu et al., *How Far Can VLMs Go for Visual Bug Detection? Studying 19,738 Keyframes from 41 Hours of Gameplay Videos*, ACM/IEEE FSE Companion 2026, Tables 1 & 2.
* **Corresponds to:** Claims [C01](../../logic/claims.md#c01-static-vlm-triage-vs-temporal-needle-in-a-haystack-collapse) and [C02](../../logic/claims.md#c02-reference-guided-lastcleanframe-performance-recovery).

## Section A: Precision and Accuracy Across Judge & RAG Variants

| Pipeline Variant | Evaluator / Judge Model | Precision | Accuracy |
|---|---|---|---|
| **4.1-mini (Baseline)** | None (Single Prompt) | **0.50** | **0.72** |
| **5-mini (Baseline)** | None (Single Prompt) | 0.35 | 0.57 |
| **+ Judge Model** | 4.1-mini | 0.47 | 0.72 |
| **+ Judge Model** | 4o-mini | 0.48 | 0.71 |
| **+ Judge Model** | **5-mini** | **0.55** | **0.74** |
| **+ Image RAG (CLIP)** | 4.1-mini | 0.37 | 0.67 |
| **+ Image RAG (CLIP)** | 4o-mini | 0.35 | 0.67 |
| **+ Image RAG (CLIP)** | 5-mini | 0.46 | 0.71 |
| **+ Text RAG (Image Desc)** | 4.1-mini | 0.45 | 0.70 |
| **+ Text RAG (Image Desc)** | 4o-mini | 0.45 | 0.70 |
| **+ Text RAG (Image Desc)** | 5-mini | 0.54 | 0.74 |
| **+ Text RAG (Bug Desc)** | 4.1-mini | 0.47 | 0.71 |
| **+ Text RAG (Bug Desc)** | 4o-mini | 0.47 | 0.71 |
| **+ Text RAG (Bug Desc)** | **5-mini** | **0.57** | **0.75** |

---

## Section B: Distribution of Primary Bug Categories (Sample of 1,000 Detected Frames)

| Defect Category | Sub-Category | Share (%) | Nature of Anomaly |
|---|---|---|---|
| **Log Message(s)** | On-screen debug exception text | **46.80%** | Textual / Non-visual HUD overlay |
| **Other Visual Anomalies** | Total True Visual Defects | **53.20%** | Rendering, asset, and animation defects |
| | - Rendering & Texture | 18.60% | Missing textures, shader drops, z-fighting |
| | - UI & HUD | 18.10% | Minimap overlap, health meter clipping |
| | - Animation & VFX | 6.10% | Character t-pose, broken ragdoll bones |
| | - Lighting & Shadow | 5.90% | Detached shadow maps, inverted normals |
| | - Physics & Collision | 3.10% | Level voids, player mesh penetration |
| | - Game Crash & Logic | 0.70% | Frozen state, non-responsive scripts |
| | - Performance | 0.60% | Severe micro-stutter / dropped frame |
| | - Other | 0.10% | Unclassified visual defects |
