# Section 6: Benchmark Datasets & Accessibility Audit (RQ3)

## 6.1 The Historical Data Scarcity Bottleneck
A primary historical impediment to applying computer vision to game QA has been the severe scarcity of public, standardized benchmark datasets. Unlike autonomous driving (KITTI, Cityscapes) or medical imaging (MIMIC-CXR), game software development is governed by stringent non-disclosure agreements (NDAs) and proprietary intellectual property (IP) controls. As a result, early primary studies between 2018 and 2023 were restricted to:
1. **Proprietary Studio Captures:** Studies conducted within commercial studios (e.g., Rahman at Microsoft Xbox [P07], Bergdahl at EA Frostbite [P14], Ling at EA SEED [P31]) utilized internal playtest archives that could not be legally open-sourced to the research community.
2. **Simplified 2D / Canvas Games:** Academic groups turned to open-source HTML5 canvas games (e.g., *CanvasBug-Bench* [P08]) or retro emulators, which failed to reproduce the visual complexity of modern 3D physically based rendering (PBR) pipelines.
3. **Artificial Bug Injection:** Researchers manually injected synthetic defects (e.g., deleting texture assets or displacing collision meshes in Unity) rather than harvesting organic glitches encountered during unstructured human playtesting.

---

## 6.2 The 2024–2026 Open-Science Watershed
Between 2024 and 2026, the domain reached a decisive turning point with the coordinated release of large-scale, multi-game open benchmarks spanning commercial-grade 3D, stylized, and 2D environments. Table 1 provides an exhaustive comparative audit of these landmark datasets:

| Benchmark / Dataset | Year | Research Origin | Data Modality | Scale & Volume | Game Diversity | Public Accessibility | Ground-Truth Annotation Format |
|---|---|---|---|---|---|---|---|
| **VideoGlitchBench** [P14] | 2026 | UC Davis & Virginia Tech | Raw Continuous Gameplay Videos | 5,238 videos | 120 games | **Public Benchmark**<br>ACM MM '26 / arXiv:2604.07818 | Precise temporal start/end timestamps $[t_{\text{start}}, t_{\text{end}}]$ + detailed natural language glitch descriptions |
| **Multi-Label Perceptual Bug Dataset** [P13] | 2026 | Ontario Tech Univ. & Univ. Osnabrück | 2-Second Video Clips (8 FPS) | 77,969 clips (~1.25M frames) | 3 Unity 3D games (Horror, Racing, FPS) | **Public Benchmark**<br>IEEE '26 / arXiv:2610.08593 | Multi-label JSON annotations (up to 3 concurrent bugs across 5 perceptual classes: Boundary Hole, Texture, Geometry, Z-Clipping, Z-Fighting) |
| **VideoGameQA-Bench** [P01] | 2025 | Univ. of Alberta & Sony IE | Images & Videos + Text QA | 3,450 scenarios | 12 diverse titles (3D, 2D, Voxel) | **Public (Open Access)**<br>[Project Website](https://asgaardlab.github.io/videogameqa-bench/) | QA pairs, defect category labels, coarse bounding boxes |
| **RefGlitch-Bench** [P05] | 2026 | Univ. of Alberta & Sony IE | Paired Reference-Test Frames | 5,200 keyframe pairs | 7 commercial 3D titles (Action, RPG) | **Public Benchmark**<br>arXiv:2604.11082 | Pairwise reference alignment (Last Clean Frame), defect masks, severity |
| **GameBug-20K** [P04] | 2026 | Univ. of Alberta & Electronic Arts | High-Resolution Keyframes | 19,738 keyframes (41h video) | 8 commercial EA titles | **Research Archive**<br>arXiv:2603.22706 | Frame-level binary defect labels, natural language reports |
| **TempGlitch-Video** [P06] | 2026 | Academic Research Consortium | 60 FPS Continuous Streams | 120 video clips (42h video) | 6 modern 3D titles | **Public (Open Science)**<br>arXiv:2605.21443 | Temporal interval bounds ($[t_{\text{start}}, t_{\text{end}}]$), defect subtype |
| **PhysGame & PhysInstruct** [P27] | 2024 | MBZUAI, PKU & Alibaba | Glitch Gameplay Videos (2.6s–239.6s) | 880 videos + 140,057 QA pairs | 300+ commercial titles | **Public (Open Science)**<br>arXiv:2412.01800 | Multiple-choice physical QA pairs spanning 4 domains (mechanics, kinematics, optics, materials) and 12 categories |
| **GlitchBench** [P25] | 2024 | Univ. of Alberta | Single Game Screenshots | 923 images (593 glitch, 330 clean) | 205 commercial games | **Public (CVPR '24)**<br>arXiv:2405.02298 | Binary glitch labels, natural language glitch descriptions |
| **VideoGameBunny** [P26] | 2025 | Univ. of Alberta | Screenshots & Instruction Pairs | 185,259 images | 413 diverse titles | **Public (WACV '25)**<br>arXiv:2407.15295 | Image captions, image-to-JSON state trees, 389,565 QA pairs |
| **GamePhysics** [P28] | 2022 | Univ. of Alberta | Gameplay Glitch Videos | 26,954 videos | 1,873 games | **Public (MSR '22)**<br>arXiv:2203.11096 | Community game titles, player commentary, weak metadata |
| **StateGlitch-3D** [P03] | 2026 | Academic / Elsevier | Multimodal (RGB + G-buffers) | 8,400 synchronized frames | 3 Unreal/Unity games | **Restricted / On Request**<br>ESWA DOI: 10.1016/j.eswa.2025.124500 | Bounding boxes + depth buffers, normals, collision matrices |
| **GameGlitch-Hybrid** [P02] | 2025 | Academic (AAAI AIIDE) | Semi-Supervised Frames | 14,200 gameplay frames | 5 commercial games | **Public (AAAI Archive)** | Bounding boxes + semi-supervised pseudo-labels |
| **World of Bugs (WOB)** [P35] | 2021 | Royal Holloway Univ. London | Synthetic 3D Renderings | Procedural testbed | Unity ML-Agents 3D | **Public (IEEE CoG '21)**<br>arXiv:2206.11037 | 10 perceptual bug classes, pixel-level ground truth segmentation masks |
| **Glitchify / AMD Corpus** [P32] | 2020 | AMD Research & Universities | Synthetic Corrupted Frames | 50,000 images | 10 commercial titles | **Public (CoG '20)**<br>arXiv:2011.15103 | 10 synthetic screen artifact types (line artifacts, color shifts, tiling, triangle displacement) |
| **GBQA** [P28] | 2026 | HKU & Westlake Univ. | Interactive Game Code & Runtime | 30 interactive games | 30 game projects | **Public (ICLR '26 Workshop)**<br>arXiv:2604.02648 | 124 human-verified bugs across 3 difficulty levels for autonomous LLM QA testing |
| **Xbox FPPC Dataset** [P07] | 2023 | Xbox Studios QuAIL | First-Person RGB Views | 6,500 frames | 1 AAA open-world title (*GiantMap*) | **Proprietary (Microsoft)** | Binary player clipping labels, exemplar embeddings |
| **CanvasBug-Bench** [P08] | 2022 | Academic (IEEE/ACM ASE) | 2D Screen Bitmaps | 24 injected bugs | 10 HTML5 canvas games | **Public (GitHub)**<br>[AsgaardLab Repo](https://github.com/asgaardlab) | Pixel-difference ground-truth masks, sprite asset trees |

---

## 6.3 Deep Dive into Landmark Benchmark Protocols

### 1. VideoGlitchBench (Zheng et al., ACM MM 2026)
*VideoGlitchBench* represents the first benchmark dedicated to **open-ended video game glitch detection with temporal localization**. While previous benchmarks restricted models to static image inspection or multiple-choice QA, VideoGlitchBench evaluates whether an AI system can ingest raw continuous gameplay video, determine whether an abnormal event violates game world logic, describe the defect in natural language, and output exact temporal boundaries $[t_{\text{start}}, t_{\text{end}}]$. Derived from community-reported glitch captures across 120 titles, it encompasses:
- Single-glitch episodes within isolated temporal bounds.
- Intermittently recurring occurrences of the same underlying defect.
- Cascading concurrent glitches occurring simultaneously or across overlapping time windows.
Evaluating proprietary and open-source foundation models reveals a severe performance bottleneck: vanilla open-source models achieve an average F1 of only 14.47% and 0.28 mIoU, while the agentic *GliDe* framework achieves **36.05% F1 and 0.51 mIoU**, establishing the state of the art.

### 2. Multi-Label Perceptual Bug Dataset (Rifaat et al., IEEE 2026)
Curated across 11 human players and three distinct open-source 3D Unity games (*Open Nights*, *Mario Kart*, and *FPS Microgame*), this benchmark provides **77,969 two-second video clips (~1.25 million frames at 8 FPS)**. Unlike single-label classification datasets, each video clip contains up to three simultaneous perceptual bugs from five fundamental defect categories:
- **Boundary Hole:** Player breaks through collision boundaries into void geometry.
- **Texture Corruption:** Broken surface texture maps and UV coordinate drift.
- **Geometry Corruption:** Stretched, inverted, or distorted polygon vertices.
- **Z-Clipping:** Near-plane frustum camera clipping through scene props.
- **Z-Fighting:** Rapid temporal flickering caused by coplanar polygon depth contention.
The dataset preserves a realistic defect distribution (65.55% clean clips, 17.97% single bug, 9.15% two bugs, 7.33% three concurrent bugs). ResNet-18 + BiLSTM models achieve an **85.78% micro F1 score**, proving that multi-defect temporal modeling is tractable.

### 3. VideoGameQA-Bench & RefGlitch-Bench (Taesiri et al., NeurIPS 2025; Yu et al., 2026)
Developed in collaboration with Sony Interactive Entertainment:
- *VideoGameQA-Bench* evaluates Vision-Language Models across 12 diverse titles spanning 3D realistic, voxel, and 2D pixel-art styles. It encompasses 3,450 scenarios testing glitch detection, categorization, spatial localization, and question answering.
- *RefGlitch-Bench* resolves the **oracle ambiguity problem** in visual testing. In dynamic or surreal game worlds, single screenshots cannot be verified without an authoritative baseline. RefGlitch-Bench pairs candidate glitch frames ($I_t$) with the immediate prior *Last Clean Frame* ($R_t$) along the identical camera trajectory, allowing reference-conditioned VLMs to achieve an F1 score of **0.69** (approaching the oracle upper bound of 0.74).

### 4. PhysGame & PhysInstruct (Cao et al., 2024)
Curated to assess whether Multimodal LLMs comprehend intuitive physical dynamics in video games, *PhysGame* features 880 gameplay clips (ranging from 2.6 seconds to 239.6 seconds) depicting physical commonsense violations across four domains:
- **Mechanics:** Gravity violations, extreme impact momentum inversion, object penetration.
- **Kinematics:** Unrealistic velocities, sudden infinite acceleration, locked rotational axes.
- **Optics:** Light passing through solid walls, detached shadow projections, mirror reflection anomalies.
- **Material Properties:** Rigid bodies deforming elastically, fluids behaving as solids.
Supported by **PhysInstruct (140,057 QA pairs)** and **PhysDPO (34,358 preference pairs)**, this benchmark provides the foundational dataset for training physical commonsense in game testing agents.

### 5. World of Bugs (Wilkins & Stathis, IEEE CoG 2021) & Glitchify (Davarmanesh et al., 2020)
Early foundational benchmarks established standardized procedural glitch synthesis:
- *World of Bugs (WOB)* deployed Unity ML-Agents to simulate autonomous playtesting agents while programmatically injecting 10 distinct perceptual defects with pixel-level ground truth masks.
- *Glitchify* generated 50,000 synthetic images across 10 common rendering corruptions, demonstrating that while machine learning ensembles achieve 84% accuracy on known game styles, domain transfer across divergent art styles incurs a 15% performance penalty.
