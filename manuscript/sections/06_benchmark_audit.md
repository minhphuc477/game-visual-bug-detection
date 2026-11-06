# Section 6: Benchmark Datasets & Accessibility Audit (RQ3)

## 6.1 The Historical Data Scarcity Bottleneck
A primary historical impediment to applying computer vision to game QA has been the severe scarcity of public, standardized benchmark datasets. Unlike autonomous driving (KITTI, Cityscapes) or medical imaging (MIMIC-CXR), game software development is governed by stringent non-disclosure agreements (NDAs) and proprietary intellectual property (IP) controls. As a result, early primary studies between 2018 and 2023 were restricted to:
1. **Proprietary Studio Captures:** Studies conducted within commercial studios (e.g., Rahman at Microsoft Xbox [12], Bergdahl at EA Frostbite [26]) utilized internal playtest archives that could not be legally open-sourced to the research community.
2. **Simplified 2D / Canvas Games:** Academic groups turned to open-source HTML5 canvas games (e.g., *CanvasBug-Bench* [11]) or retro emulators, which failed to reproduce the visual complexity of modern 3D physically based rendering (PBR) pipelines.
3. **Artificial Bug Injection:** Researchers manually injected synthetic defects (e.g., deleting texture assets or displacing collision meshes) rather than harvesting organic glitches encountered during unstructured human playtesting.

---

## 6.2 The 2025–2026 Open-Science Watershed
Between 2025 and 2026, the domain reached a decisive turning point with the coordinated release of large-scale, multi-game open benchmarks spanning commercial-grade 3D, stylized, and 2D environments. Table 1 provides an exhaustive comparative audit of these landmark datasets:

| Benchmark / Dataset | Year | Research Origin | Data Modality | Scale & Volume | Game Diversity | Public Accessibility | Ground-Truth Annotation Format |
|---|---|---|---|---|---|---|---|
| **VideoGameQA-Bench** [1] | 2025 | Univ. of Alberta & Sony IE | Images & Videos + Text QA | 3,450 scenarios | 12 diverse titles (3D, 2D, Voxel) | **Public (Open Access)**<br>[Project Website](https://asgaardlab.github.io/videogameqa-bench/) | QA pairs, category labels, coarse bounding boxes |
| **RefGlitch-Bench** [6] | 2026 | Univ. of Alberta & Sony IE | Paired Reference-Test Frames | 5,200 keyframe pairs | 7 commercial 3D titles (Action, RPG) | **Public Benchmark**<br>arXiv:2604.11082 | Pairwise reference alignment, defect masks, severity |
| **GameBug-20K** [17] | 2026 | Univ. of Alberta & Electronic Arts | High-Resolution Keyframes | 19,738 keyframes (41h video) | 8 commercial EA titles | **Research Archive**<br>arXiv:2603.22706 | Frame-level binary defect labels, natural language reports |
| **TempGlitch-Video** [13] | 2026 | Academic Research Consortium | 60 FPS Continuous Streams | 120 video clips (42h video) | 6 modern 3D titles | **Public (Open Science)**<br>arXiv:2605.21443 | Temporal interval bounds ($[t_{\text{start}}, t_{\text{end}}]$), defect subtype |
| **StateGlitch-3D** [3] | 2026 | Academic / Elsevier | Multimodal (RGB + G-buffers) | 8,400 synchronized frames | 3 Unreal/Unity games | **Restricted / On Request**<br>ESWA DOI: 10.1016/j.eswa.2025.124500 | Bounding boxes + depth buffers, normals, collision matrices |
| **GameGlitch-Hybrid** [7] | 2025 | Academic (AAAI AIIDE) | Semi-Supervised Frames | 14,200 gameplay frames | 5 commercial games | **Public (AAAI Archive)** | Bounding boxes + semi-supervised pseudo-labels |
| **Xbox FPPC Dataset** [12] | 2023 | Xbox Studios QuAIL | First-Person RGB Views | 6,500 frames | 1 AAA open-world title (*GiantMap*) | **Proprietary (Microsoft)** | Binary player clipping labels, exemplar embeddings |
| **CanvasBug-Bench** [11] | 2022 | Academic (IEEE/ACM ASE) | 2D Screen Bitmaps | 24 injected bugs | 10 HTML5 canvas games | **Public (GitHub)**<br>[AsgaardLab Repo](https://github.com/asgaardlab) | Pixel-difference ground-truth masks, sprite asset trees |

---

## 6.3 Deep Dive into Benchmark Protocols

### 1. VideoGameQA-Bench (Taesiri et al., NeurIPS 2025)
*VideoGameQA-Bench* represents the first large-scale benchmark designed to evaluate Vision-Language Models on video game quality assurance tasks. Spanning 12 diverse titles across genres (first-person shooters, open-world RPGs, voxel sandbox, side-scrolling platformers), it encompasses 3,450 scenarios evaluating four testing tasks:
1. *Glitch Detection:* Binary classification of defect presence.
2. *Defect Categorization:* Classifying glitches into geometry clipping, missing textures, UI overlap, or lighting artifacts.
3. *Spatial Localization:* Generating 2D bounding boxes $[x_{\min}, y_{\min}, x_{\max}, y_{\max}]$ enclosing the glitch.
4. *Visual Question Answering:* Answering domain-specific QA queries regarding visual consistency and gameplay rendering.

### 2. RefGlitch-Bench (Yu et al., 2026)
Developed in collaboration with Sony Interactive Entertainment, *RefGlitch-Bench* addresses the foundational problem of **oracle ambiguity**. In modern games, an isolated screenshot of a surreal alien environment or cel-shaded character cannot be reliably evaluated without an authoritative baseline. *RefGlitch-Bench* provides 5,200 aligned pairs comprising:
- $I_t$: The candidate evaluation frame containing a suspected visual defect.
- $R_t$: The *Last Clean Frame* captured from the identical scene graph trajectory immediately prior to glitch manifestation.
By comparing $(I_t, R_t)$, reference-conditioned models isolate the true rendering delta while ignoring dynamic backgrounds.

### 3. GameBug-20K (Lu et al., FSE 2026)
Harvested directly from Electronic Arts (EA) automated test runs across 41 hours of continuous gameplay, *GameBug-20K* provides 19,738 extracted keyframes. Each frame is annotated with verified defect categories and matched against real studio bug tracker tickets. Its primary contribution is providing an industrial reality check on off-the-shelf foundation models, proving that real-world playtest captures exhibit far greater visual variability and noise than synthetic benchmark sets.

### 4. TempGlitch-Video (Muller et al., 2026)
*TempGlitch-Video* is the first benchmark specifically curated for temporal glitch localization. Encompassing 42 hours of 60 FPS gameplay across 6 modern 3D games, it provides exact temporal ground-truth intervals $[t_{\text{start}}, t_{\text{end}}]$ for transient glitches:
- Animation ragdoll instability: Mean glitch duration $\Delta t = 0.82\text{ s}$.
- Level-of-Detail (LOD) texture pop-in: Mean glitch duration $\Delta t = 0.35\text{ s}$.
- Coplanar Z-fighting flickering: Mean glitch duration $\Delta t = 1.45\text{ s}$.
TempGlitch establishes the standard benchmark for temporal Intersection-over-Union ($\text{tIoU}$) evaluation in continuous video QA.
