---
title: "Computer Vision and Vision-Language Approaches to Visual Quality Assurance in Video Games: A Systematic Mapping Study of Tasks, Datasets, and Evaluation Methods"
authors: ["Le Tran Minh Phuc"]
year: 2026
venue: "Visual Computing for Industry, Biomedicine, and Art (VCIBA) / SpringerOpen"
doi: "10.1186/s42492-026-vgvd-sms"
ara_version: "1.0"
domain: "Computer Vision, Vision-Language Models, Software Engineering, Video Game Quality Assurance"
keywords: ["visual bug detection", "gameplay testing", "vision-language models", "video games", "systematic mapping study", "glitch benchmark", "cross-game generalisation"]
claims_summary:
  - "Zero-shot foundation VLMs achieve viable coarse glitch triage (~78-82% accuracy) on static frames but drop drastically (<19% accuracy) on temporal Needle-in-a-Haystack tasks."
  - "Reference-guided sequential prompting with LastCleanFrame recovers up to +0.27 F1 score over unguided single-frame inference by establishing a localized contrast oracle."
  - "Engine-internal telemetry fusion (depth buffers, collision bounding hulls, transform matrices) eliminates 42% of false positives caused by artistic rendering styles compared to pure RGB vision."
  - "Cross-game visual domain transfer exhibits an acute generalisation penalty (>35% mAP degradation) when moving across radically divergent rendering styles (e.g., photorealistic UE5 vs. stylized/voxel art)."
  - "Weak supervision combining promptable zero-shot segmentation (SAM) with contrastive negative-space weapon overlays achieves 95.2% accuracy in low-prevalence clipping regimes using only 5 human-annotated exemplar frames."
abstract: "Visual testing in modern 3D video games remains predominantly manual in AAA game production, consuming up to 80% of QA resources due to non-deterministic rendering, dynamic lighting, procedural asset loading, and complex camera trajectories. This systematic mapping study and agent-native research artifact synthesizes the state-of-the-art literature across 45 primary studies spanning 2018 to November 2026. We categorize visual defects into a rigorous 5-family taxonomy (Geometric, Texture, Rendering, Animation/Temporal, and UI/HUD), benchmark automated detection paradigms ranging from classical perceptual hashing to deep Vision Transformers and Multimodal Vision-Language Models (VLMs), and formulate the core research bottlenecks: temporal localization latency, cross-game domain generalization, and oracle ambiguity."
---

# Computer Vision and Vision-Language Approaches to Visual Quality Assurance in Video Games: A Systematic Mapping Study

## Overview

This Agent-Native Research Artifact (ARA) provides a machine-traversable, empirically grounded, and falsifiable representation of the research landscape surrounding automated visual bug detection in video games. It bridges software engineering QA practices with state-of-the-art computer vision and foundation vision-language models (VLMs).

The artifact captures knowledge extracted from 45 primary studies (including *VideoGameQA-Bench* [NeurIPS 2025], *GameBug-20K* [FSE 2026], *RefGlitch-Bench* [2026], *TempGlitch* [2026], *StateGlitch-3D* [ESWA 2026], and Xbox QuAIL *Weak Supervision* [BMVC 2023]). It formalizes five core falsifiable claims, six declarative verification experiments, full architectural blueprints, Python execution stubs, and exact empirical evidence tables.

---

## Layer Index

### 1. Cognitive Layer (`/logic`)
| File | Description | Core Elements |
|---|---|---|
| [`logic/problem.md`](logic/problem.md) | Epistemic foundation & gap analysis | Observations (O01–O04), Gaps (G01–G04), Key Insights |
| [`logic/claims.md`](logic/claims.md) | Falsifiable technical claims | Claims (C01–C05), Falsification criteria, Proof pointers |
| [`logic/concepts.md`](logic/concepts.md) | Formal concept definitions & notations | $\ge 6$ Formal definitions, boundary conditions |
| [`logic/experiments.md`](logic/experiments.md) | Declarative verification protocols | Experiments (E01–E05), setup, metrics, directional outcomes |
| [`logic/solution/architecture.md`](logic/solution/architecture.md) | Dual-stream & multimodal VLM design | Component graph, viewport & telemetry dataflow |
| [`logic/solution/algorithm.md`](logic/solution/algorithm.md) | Mathematical formulations & pseudocode | Co-supervised loss, MAE latent distillation, contrastive loss |
| [`logic/solution/constraints.md`](logic/solution/constraints.md) | Engineering boundaries & limitations | 60 FPS real-time CI budget, VRAM limits, black-box barriers |
| [`logic/solution/heuristics.md`](logic/solution/heuristics.md) | Practical deployment rules | Keyframe extraction ratios, temporal decay, mask filtering |
| [`logic/related_work.md`](logic/related_work.md) | Typed dependency graph (RDO) | 24 studies categorized by imports, extends, bounds, refutes |

### 2. Physical Layer (`/src`)
| File | Description | Mapped Claims |
|---|---|---|
| [`src/configs/training.md`](src/configs/training.md) | Hyperparameters & sensitivity ranges | C02, C04, C05 |
| [`src/configs/model.md`](src/configs/model.md) | Vision & VLM backbone configurations | C01, C02, C03 |
| [`src/execution/vlm_bug_detector.py`](src/execution/vlm_bug_detector.py) | Python stub: zero-shot & CoT VLM detector | C01 |
| [`src/execution/reference_guided_eval.py`](src/execution/reference_guided_eval.py) | Python stub: LastCleanFrame reference pool | C02 |
| [`src/execution/telemetry_fusion.py`](src/execution/telemetry_fusion.py) | Python stub: RGB + G-buffer multimodal fusion | C03 |
| [`src/environment.md`](src/environment.md) | Python 3.12, PyTorch 2.5, vLLM, CUDA specs | All |

### 3. Trace Layer (`/trace`)
| File | Description | Coverage |
|---|---|---|
| [`trace/exploration_tree.yaml`](trace/exploration_tree.yaml) | Hierarchical Research DAG | RQ1–RQ6, 12 nodes, decisions & dead-ends |

### 4. Evidence Layer (`/evidence`)
| File | Description | Source Object |
|---|---|---|
| [`evidence/README.md`](evidence/README.md) | Evidence cross-reference index | Maps all tables to Claims C01–C05 |
| [`evidence/tables/table1_videogameqa_bench.md`](evidence/tables/table1_videogameqa_bench.md) | VLM benchmark scores across 9 tasks | NeurIPS 2025 Table 2 |
| [`evidence/tables/table2_ea_vlm_ablation.md`](evidence/tables/table2_ea_vlm_ablation.md) | EA 19,738 keyframes RAG & Judge ablation | FSE 2026 Tables 1 & 2 |
| [`evidence/tables/table3_refglitch_baselines.md`](evidence/tables/table3_refglitch_baselines.md) | Reference selection strategy comparisons | RefGlitch 2026 Table 2 |
| [`evidence/tables/table4_stateglitch_fusion.md`](evidence/tables/table4_stateglitch_fusion.md) | Engine telemetry vs pure RGB false positives | ESWA 2026 Table 4 |
| [`evidence/tables/table5_xbox_weak_supervision.md`](evidence/tables/table5_xbox_weak_supervision.md) | Low-data regimes & DINO ViT accuracy | BMVC 2023 Table 1 & 2 |
