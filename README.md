# Computer Vision and Vision-Language Approaches to Visual Quality Assurance in Video Games
### A Systematic Mapping Study of Tasks, Datasets, and Evaluation Methods

[![Python 3.10+](https://img.shields.io/badge/python-3.10%2B-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![ARA Seal Level 1](https://img.shields.io/badge/ARA%20Seal-Level%201%20Passed-brightgreen.svg)](ara/PAPER.md)
[![PRISMA-S / ROSES](https://img.shields.io/badge/Methodology-PRISMA--S%20%7C%20ROSES-orange.svg)](protocol/systematic_mapping_protocol.md)
[![Target: VCIBA SpringerOpen](https://img.shields.io/badge/Target-VCIBA%20(SpringerOpen)-purple.svg)](protocol/target_journal_guidelines.md)

This repository hosts the research assets, systematic mapping study protocol, curated 45-study literature evidence database, high-resolution publication figures, Agent-Native Research Artifact (ARA), and manuscript package for:

> **"Computer Vision and Vision-Language Approaches to Visual Quality Assurance in Video Games: A Systematic Mapping Study of Tasks, Datasets, and Evaluation Methods"**  
> *Author:* Le Tran Minh Phuc  
> *Target Venues:* **Primary:** *Visual Computing for Industry, Biomedicine, and Art* (SpringerOpen / China Graphics Society — $0 APC Diamond OA, Scopus Q1) · **Backup:** *Applied Computing and Informatics* (Emerald Publishing — $0 APC Diamond OA, Scopus Q1)  
> *Submission Package:* Full Markdown ([`manuscript/complete_manuscript.md`](manuscript/complete_manuscript.md)) & Compiled 16-page LaTeX PDF ([`manuscript/main.pdf`](manuscript/main.pdf))

---

## 1. Research Overview & Motivation

Quality assurance (QA) in modern interactive 3D and 2D entertainment represents up to 50% of game production budgets. While automated unit testing and headless gameplay bots can verify functional state logic, **visual defects**—such as polygonal mesh clipping, texture pop-in delays, floating props, broken shaders, ragdoll physics instability, and HUD misalignments—remain heavily reliant on manual human playtesting (>80% manual in AAA studios).

Recent developments in deep learning (convolutional neural networks, vision transformers, self-supervised anomaly detection) and Vision-Language Models (VLMs) have opened avenues for automating visual quality assurance. However, research is fragmented across Software Engineering (SE), Computer Vision (CV), and Game AI. 

Following the systematic mapping guidelines of **Petersen et al. (2015)**, **Kitchenham & Charters (2007)**, **PRISMA-S**, and **ROSES**, this study systematically identifies, classifies, and synthesizes **45 primary studies** (2018–November 2026).

```mermaid
graph LR
    subgraph Input ["Gameplay Sources"]
        A1["RGB Screenshots"]
        A2["60 FPS Video Streams"]
        A3["Engine Buffers (Depth / Colliders)"]
    end

    subgraph Models ["AI / CV Detection Paradigms"]
        B1["Self-Supervised Anomaly (PatchCore)"]
        B2["Object / Defect Detectors (YOLO / ViT)"]
        B3["Multimodal Engine Telemetry Fusion"]
        B4["Vision-Language Models (VLM QA)"]
        B5["Spatio-Temporal Video Transformers"]
    end

    subgraph Defects ["VGVD-Taxonomy (19 Subtypes)"]
        C1["GEO: Clipping & Floating Props"]
        C2["TEX: Missing Textures & Pop-in"]
        C3["REN: Z-Fighting & Light Leaking"]
        C4["ANI: T-Pose & Foot-Sliding"]
        C5["UI: HUD Collisions & Overflows"]
    end

    Input --> Models --> Defects
```

---

## 2. Research Questions (RQs)

| ID | Research Question | Methodological Target |
|---|---|---|
| **RQ1** | *What computer vision, deep learning, and vision-language techniques have been investigated for visual quality assurance in video games?* | Classify algorithms: classical image processing, supervised CNN/ViT, anomaly detection (PatchCore, DINO ViT), multimodal engine telemetry fusion, foundation VLMs, and spatio-temporal video transformers. |
| **RQ2** | *What types of visual testing and defect-detection tasks have been investigated across video games?* | Standardize defect coverage against the 19 subtypes of `VGVD-Taxonomy` (spatial, textures, rendering, animation, UI). |
| **RQ3** | *What datasets and benchmarks are used to develop and evaluate visual testing approaches, and how accessible are they?* | Inventory data availability: commercial vs. open-source titles, synthetic vs. organic playtest footage, public repository availability. |
| **RQ4** | *How are computer vision-based visual testing approaches evaluated in video games?* | Analyze classification accuracy, precision, recall, false positive rates, and real-time inference latency (FPS) for live CI playtesting. |
| **RQ5** | *What research trends, cross-game generalization limitations, and future research opportunities can be identified?* | Measure domain shift degradation under severe art style shifts (UE5 photorealism vs. stylized cel-shaded/voxel) and formulate an evidence-based roadmap. |

---

## 3. Curated Evidence Corpus (45 Primary Studies)

The synthesized corpus is categorized across six thematic research clusters, fully cataloged in [`literature/evidence_table.csv`](literature/evidence_table.csv) and [`literature/papers.bib`](literature/papers.bib):

| Thematic Cluster | Studies | Key Landmark Publications | Core Technical Innovations |
|---|---|---|---|
| **Cluster 1: VLMs & Multimodal QA** | 10 | Taesiri et al. (*NeurIPS '25*), Lu et al. (*FSE '26*), Yu et al. (*RefGlitch '26*), Taesiri et al. (*CVPR '24*, *WACV '25*, *MSR '22*), Cao et al. (*'24*), Wang et al. (*AIIDE '25*), Sengupta et al. (*'26*) | Zero-shot VLM prompting, JSON-CoT reasoning, LastCleanFrame reference pools, VLM-as-a-judge, embodied exploratory agents. |
| **Cluster 2: Anomaly Detection & Self-Supervision** | 9 | Rahman (*BMVC '23*), Yi et al. (*AIIDE '25*), Al-Dujaili et al. (*ACM MM '22*), Shin & Park (*C&G '23*), Ling et al. (*AIIDE '20*), Davarmanesh et al. (*CoG '20*), Wilkins & Stathis (*'22*), Tamm et al. (*AIIDE '22*), Macklon et al. (*ASE '22*) | Weak supervision with SAM negative-space priors, hybrid co-finetuning (CFT) with unlabeled video, PatchCore anomaly detection. |
| **Cluster 3: State-Aware & Telemetry Fusion** | 7 | Kovacs et al. (*ESWA '26*), Bergdahl et al. (*CoG '20*), Zheng et al. (*TOSEM '21*), Biemer et al. (*IEEE TG '21*), Liu et al. (*CoG '22*), Paduraru et al. (*ICST '22*), Chen et al. (*ICSE '23*) | G-buffer depth and normal fusion (reducing false positives by 41.9%), Frostbite PPO exploration bots, Wuji multi-objective RL. |
| **Cluster 4: Spatio-Temporal Video Streams** | 7 | Muller et al. (*TempGlitch '26*), Wang et al. (*ACM MM '24*), Dupont et al. (*CGF '23*), Li et al. (*TVCG '24*), Guglielmi et al. (*ASE '23*, *CoG '23*), Truelove et al. (*TSE '23*) | 16-frame sliding video transformers, action-conditioned gamepad controller telemetry ViTs, skeletal ST-GCN, 75 FPS optical flow. |
| **Cluster 5: GUI, HUD & Visual Regression** | 6 | Chen et al. (*ASE '25*), Mahajan & Halfond (*TOSEM '21*), Chen et al. (*FSE '21*), Roohi et al. (*CHI PLAY '21*), Moran et al. (*ICSE '20*), Wu et al. (*Q-Bench ICLR '24*) | Human contrast sensitivity function (CSF) differencing, layout hierarchy bounds, foundation model low-level perception audits. |
| **Cluster 6: Surveys, Taxonomies & Reviews** | 6 | Politowski et al. (*ACM CSUR '21*, *IEEE Software '21*, *AST '21*), Albaghajati & Ahmed (*IEEE TG '23*), Svensson & Lindqvist (*IST '25*), Coppola et al. (*GEM '24*), Pascarella et al. (*EMSE '18*) | Empirical mining of 1M+ Steam reviews, industrial studio QA workflow audits, comparative testing assessment frameworks. |

---

## 4. Publication Figures (High-DPI 300 DPI & Vector SVG)

All figures are programmatically generated via `scripts/generate_figures.py` and stored in `manuscript/figures/`:

| Figure | Description | Previews |
|---|---|---|
| **Figure 1** | **PRISMA-S 2020 Study Selection Flowchart**<br>692 identified $\to$ 188 duplicates removed $\to$ 504 screened $\to$ 88 full texts assessed $\to$ 45 included primary studies. | [`PNG`](manuscript/figures/figure1_prisma_flow.png) · [`SVG`](manuscript/figures/figure1_prisma_flow.svg) |
| **Figure 2** | **Publication Trajectory and Venue Distribution (2018–2026)**<br>Breakdown by year and venue type (60% Conference, 27% Journal, 13% Preprint; 100% Open Access). | [`PNG`](manuscript/figures/figure2_publications_by_year.png) · [`SVG`](manuscript/figures/figure2_publications_by_year.svg) |
| **Figure 3** | **Systematic Mapping Bubble Plot: Paradigms vs. QA Tasks**<br>Cross-tabulation of 6 architectural paradigms against 6 visual QA tasks (bubble area $\propto$ study count). | [`PNG`](manuscript/figures/figure3_technique_vs_task_bubble.png) · [`SVG`](manuscript/figures/figure3_technique_vs_task_bubble.svg) |
| **Figure 4** | **Defect Subtype Coverage Across `VGVD-Taxonomy`**<br>Empirical coverage of 19 defect subtypes across Spatial, Material, Rendering, Animation, and UI families. | [`PNG`](manuscript/figures/figure4_defect_category_distribution.png) · [`SVG`](manuscript/figures/figure4_defect_category_distribution.svg) |
| **Figure 5** | **Input Modalities and Cross-Game Generalisation Verification**<br>Donut chart of input signals (RGB, Video, Telemetry) and verification status of cross-game domain transfer. | [`PNG`](manuscript/figures/figure5_cross_game_modalities.png) · [`SVG`](manuscript/figures/figure5_cross_game_modalities.svg) |

---

## 5. Agent-Native Research Artifact (ARA)

The repository implements the formal **Agent-Native Research Artifact (`ara/`)** standard, passing the **Seal Level 1 Validation**:
- Master manifest: [`ara/PAPER.md`](ara/PAPER.md)
- Cognitive Logic: Problem formulation ([`ara/logic/problem.md`](ara/logic/problem.md)), 5 falsifiable claims ([`ara/logic/claims.md`](ara/logic/claims.md)), formal concepts ([`ara/logic/concepts.md`](ara/logic/concepts.md)), declarative verification experiments ([`ara/logic/experiments.md`](ara/logic/experiments.md)), architectural blueprints ([`ara/logic/solution/`](ara/logic/solution/)).
- Physical Layer: Executable Python stubs ([`ara/src/execution/`](ara/src/execution/)), hyperparameter configs ([`ara/src/configs/`](ara/src/configs/)), and environment specs ([`ara/src/environment.md`](ara/src/environment.md)).
- Research DAG: Falsification hypotheses and decision paths ([`ara/trace/exploration_tree.yaml`](ara/trace/exploration_tree.yaml)).
- Empirical Evidence: 5 raw benchmark extraction tables ([`ara/evidence/tables/`](ara/evidence/tables/)).

---

## 6. Repository Structure

```text
.
├── README.md                                # Project overview, research questions & evidence index
├── ROADMAP.md                               # 4-Stage PhD Research Publication Roadmap
├── pyproject.toml                           # Python project metadata and dependencies
│
├── protocol/                                # Formal Systematic Mapping Protocol (Version 1.0)
│   ├── systematic_mapping_protocol.md       # Complete 1,155-line Petersen / PRISMA-S protocol
│   ├── search_strings.md                    # Tailored queries for IEEE, ACM, Scopus, WoS, arXiv
│   ├── quality_assessment_checklist.md      # 10-point rigorous quality appraisal rubric
│   └── target_journal_guidelines.md         # VCIBA & ACI Diamond Open Access guidelines
│
├── literature/                              # Literature Evidence Database & Mapping Matrices
│   ├── evidence_table.csv                   # Master CSV database of 45 primary studies & metadata
│   ├── papers.bib                           # 45 verified BibTeX citation records
│   └── taxonomy.md                          # Standardized VGVD-Taxonomy specification
│
├── manuscript/                              # Manuscript Drafts & LaTeX Submission Package
│   ├── main.tex                             # Complete LaTeX source (SpringerOpen VCIBA format)
│   ├── main.pdf                             # Compiled 16-page submission-ready PDF
│   ├── references.bib                       # 50 complete BibTeX citations (45 studies + 5 foundations)
│   ├── complete_manuscript.md               # Compiled Markdown manuscript (69,147 characters)
│   ├── sections/                            # Modular manuscript sections (01 to 06)
│   └── figures/                             # High-DPI PNG and SVG publication figures (Figures 1-5)
│
├── ara/                                     # Agent-Native Research Artifact (Seal Level 1 Certified)
│   ├── PAPER.md                             # Master manifest and Layer Index
│   ├── logic/                               # Problem, claims, concepts, experiments, solutions
│   ├── src/                                 # Python execution stubs and config specs
│   ├── trace/                               # Research Exploration DAG (15 nodes)
│   └── evidence/                            # Raw empirical benchmark extraction tables
│
├── papers/                                  # Structured raw PDF literature library
│   ├── 01_reviews/                          # Prior surveys on game testing and SE
│   ├── 02_glitch_and_anomaly_detection/     # Deep learning & anomaly detection papers
│   ├── 03_vlms_and_multimodal/              # Vision-Language Models & multimodal QA papers
│   ├── 04_benchmarks_and_datasets/          # Game glitch datasets and benchmark papers
│   └── 05_gameplay_video_analysis/          # Temporal video streams & animation glitch papers
│
├── markdown/                                # High-fidelity Markdown conversions (academic-pdf2md)
│   ├── INDEX.md                             # Interactive master index of 12 converted papers
│   └── (converted paper markdown folders with extracted figure PNGs)
│
└── scripts/                                 # Automation tools and pipelines
    ├── generate_figures.py                  # Matplotlib script generating Figures 1-5 (PNG & SVG)
    ├── build_manuscript.py                  # Script assembling sections into complete_manuscript.md
    └── fetch_open_access_metadata.py        # Semantic Scholar & OpenAlex literature harvester
```

---

## 7. Citation & Academic Attribution

If you utilize this mapping study protocol, the `VGVD-Taxonomy`, or the empirical evidence database, please cite:

```bibtex
@misc{phuc2026gamevisualbugdetection,
  author       = {Le Tran Minh Phuc},
  title        = {Computer Vision and Vision-Language Approaches to Visual Quality Assurance in Video Games: A Systematic Mapping Study of Tasks, Datasets, and Evaluation Methods},
  year         = {2026},
  publisher    = {GitHub},
  howpublished = {\url{https://github.com/minhphuc477/game-visual-bug-detection}}
}
```

---
*Maintained by Le Tran Minh Phuc · Academic Research Laboratory · November 2026*
