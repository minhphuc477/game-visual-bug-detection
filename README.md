# AI-Based Visual Bug Detection in Video Games
### A Systematic Mapping Study & Research Hub for Intelligent Game Visual Quality Assurance

[![Python 3.10+](https://img.shields.io/badge/python-3.10%2B-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![MarkItDown](https://img.shields.io/badge/MarkItDown-0.1.6-brightgreen.svg)](https://github.com/microsoft/markitdown)
[![PRISMA 2020](https://img.shields.io/badge/Reporting-PRISMA%202020-orange.svg)](http://www.prisma-statement.org/)

This repository hosts the research assets, systematic mapping study protocol, curated literature evidence database, and automated PDF-to-Markdown document ingestion pipeline for:

> **"Computer Vision-Based Visual Testing in Video Games: A Systematic Mapping Study of Detection Techniques, Datasets, and Evaluation Methods"**

---

## 1. Research Motivation & Scope
Quality assurance in modern interactive entertainment is one of the most cost-intensive phases of software development, frequently consuming over 50% of production budgets. While functional and gameplay logic tests can be automated via headless test runners, **visual defects**—such as object clipping, floating meshes, texture popping, missing materials, T-pose freezes, shadow tearing, and UI overlaps—remain predominantly reliant on manual human playtesting.

Recent advances in deep learning (convolutional neural networks, vision transformers, patch-based anomaly detection) and Vision-Language Models (VLMs) present transformative opportunities to automate visual regression testing and glitch detection directly from gameplay screenshots and video streams. 

However, existing literature is fragmented across software engineering, computer vision, and game AI. This research establishes the foundational taxonomy, benchmark audit, and critical research agenda for intelligent visual QA.

```mermaid
graph LR
    subgraph Input ["Gameplay Sources"]
        A1["RGB Screenshots"]
        A2["Video Streams"]
        A3["Engine Buffers (Depth / Normals)"]
    end

    subgraph Models ["AI / CV Detection Layer"]
        B1["Self-Supervised Anomaly (PatchCore)"]
        B2["Object / UI Detectors (YOLO / ViT)"]
        B3["Vision-Language Models (VLM QA)"]
    end

    subgraph Defects ["Visual Bug Taxonomy"]
        C1["Spatial: Clipping & Floating"]
        C2["Textures: Missing / Pop-in"]
        C3["Temporal: Animation & Stutter"]
        C4["Interface: HUD / Text Overlap"]
    end

    Input --> Models --> Defects
```

---

## 2. Research Questions (RQs)

- **RQ1 (Techniques):** What computer vision and AI techniques are currently employed for visual testing and glitch detection in video games?
- **RQ2 (Taxonomy):** What categories, severities, and manifestations of visual bugs can existing methods detect?
- **RQ3 (Benchmarks):** What datasets and benchmarks are utilized in primary studies, and how accessible/reproducible are they?
- **RQ4 (Evaluation):** What evaluation metrics and experimental protocols are applied to measure detection accuracy and real-time inference?
- **RQ5 (Generalisation):** To what extent do existing detection models generalise across diverse games, art styles, and rendering engines without re-training?
- **RQ6 (Research Agenda):** What are the principal limitations, open challenges, and high-impact opportunities for future research?

---

## 3. PhD Research Roadmap (4-Stage Programme)

| Stage | Manuscript Title | Core Contribution | Target Venues |
|---|---|---|---|
| **Stage 1** | *Computer Vision-Based Visual Testing in Video Games: A Systematic Mapping Study* | Taxonomy, benchmark audit, evaluation gap mapping (2020–2026) | JSS, EMSE, IEEE Trans. Games |
| **Stage 2** | *Cross-Game Generalisation of Visual Anomaly Detection Models* | Empirical multi-game benchmark assessing zero-shot domain transfer | ICSE, FSE, AIIDE |
| **Stage 3** | *State-Aware Contrastive Learning for Object Clipping & Geometry Glitch Detection* | Novel architecture fusing rendering buffers with visual representations | CVPR, ECCV, NeurIPS D&B |
| **Stage 4** | *Temporal Vision-Language Models for Gameplay Bug Localization & Reporting* | Multi-frame VLM agent generating automated natural language bug reports | ACL, NeurIPS, IEEE Trans. Games |

*For complete details, see [ROADMAP.md](ROADMAP.md).*

---

## 4. Repository Structure

```text
.
├── README.md                                # Project overview, research questions & guide
├── ROADMAP.md                               # 4-Stage PhD Research Publication Roadmap
├── pyproject.toml                           # Python project metadata and dependencies
├── .gitignore                               # Git ignore configuration
│
├── protocol/                                # Systematic Mapping Study Protocol
│   ├── systematic_mapping_protocol.md       # Full SMS protocol (Kitchenham / Petersen guidelines)
│   ├── search_strings.md                    # Tailored queries for IEEE, ACM, Scopus, WoS, arXiv
│   └── quality_assessment_checklist.md      # 10-point rigorous quality appraisal rubric
│
├── literature/                              # Literature Evidence Database & Mapping Matrices
│   ├── README.md                            # Guide to literature data fields
│   ├── evidence_table.csv                   # Master CSV database of primary studies & metadata
│   ├── papers.bib                           # BibTeX citations for all tracked literature
│   ├── taxonomy.md                          # Detailed visual bug taxonomy specification
│   └── discovered_open_access_papers.json   # Output from automated open-access harvester
│
├── papers/                                  # Structured raw PDF literature library
│   ├── README.md                            # PDF naming conventions and guide
│   ├── 01_reviews/                          # Prior surveys on game testing and SE
│   ├── 02_glitch_and_anomaly_detection/     # Deep learning & anomaly detection papers
│   ├── 03_vlms_and_multimodal/              # Vision-Language Models & multimodal QA papers
│   ├── 04_benchmarks_and_datasets/          # Game glitch datasets and benchmark papers
│   └── 05_gameplay_video_analysis/          # Temporal video streams & animation glitch papers
│
├── markdown/                                # Converted full-text Markdown papers
│   ├── README.md                            # MarkItDown output documentation
│   ├── INDEX.md                             # Interactive master index of all converted papers
│   └── (converted paper markdown files)
│
├── scripts/                                 # Automation tools and pipelines
│   ├── convert_papers.py                    # PDF-to-Markdown batch converter using MarkItDown
│   └── fetch_open_access_metadata.py        # Semantic Scholar & OpenAlex literature harvester
│
└── data/                                    # Machine-readable schemas & taxonomies
    └── visual_bug_taxonomy.json             # JSON Schema taxonomy for benchmark evaluation
```

---

## 5. Automated PDF-to-Markdown Pipeline (MarkItDown)

This repository includes a production-grade ingestion tool powered by [Microsoft MarkItDown](https://github.com/microsoft/markitdown) (`markitdown>=0.1.6`). It extracts structure-preserving Markdown from raw academic PDFs, adds provenance YAML frontmatter, and auto-generates `markdown/INDEX.md`.

### Quickstart with `uv` (Recommended)
No manual virtual environment setup required—`uv` handles isolated dependencies automatically:

```bash
# Convert all PDFs in papers/ directory to markdown/
uv run scripts/convert_papers.py

# Convert a single paper
uv run scripts/convert_papers.py --file papers/04_benchmarks_and_datasets/Macklon_2025_VideoGameQA.pdf

# Force re-conversion and overwrite existing files
uv run scripts/convert_papers.py --overwrite
```

### Standard Python Usage
```bash
# Install dependencies
pip install -e .

# Run batch conversion
python scripts/convert_papers.py
```

Each generated Markdown file contains structured provenance headers:
```yaml
---
title: "VideoGameQA-Bench: A Benchmark for Vision-Language Models on Video Game Quality Assurance"
author: "Macklon et al."
year: "2025"
source_file: "04_benchmarks_and_datasets/Macklon_2025_VideoGameQA.pdf"
source_sha256: "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"
converted_at: "2026-11-06T14:25:00Z"
markitdown_version: "0.1.6"
char_count: 48920
---
```

---

## 6. Seed Benchmark & Dataset Overview

| Benchmark / Study | Year | Venue | Modality | Bug Categories | Open Access |
|---|---|---|---|---|---|
| **VideoGameQA-Bench** | 2025 | NeurIPS Datasets | RGB + Text VLM | Clipping, Missing Textures, UI, Animation | [Link](https://proceedings.nips.cc/paper_files/paper/2025/hash/db2cf8f479a96cb83329f5e193318a29-Abstract-Datasets_and_Benchmarks_Track.html) |
| **Hybrid Co-FineTuning** | 2025 | AIIDE | Semi-Supervised ViT | Mesh Clipping, Texture Pop-in | [Link](https://ojs.aaai.org/index.php/AIIDE/article/view/36820) |
| **State-Aware Glitch Net** | 2026 | ESWA (Elsevier) | Multimodal (Vision+State) | 3D Geometry Collisions, Floating Meshes | [Link](https://doi.org/10.1016/j.eswa.2025.124500) |
| **How Far Can VLMs Go?** | 2026 | ICSE Companion | Pretrained VLMs (20K frames) | Broad Glitch Detection & QA | [Link](https://arxiv.org/abs/2603.22706) |
| **TempGlitch** | 2026 | arXiv (cs.CV) | Gameplay Video Streams | Temporal Animation Glitches, LOD Pop-in | [Link](https://arxiv.org/abs/2605.21443) |
| **HTML5 Canvas Glitch** | 2022 | ASE | Classical CV / Feature Matching | 2D Missing Sprites, Render Difference | [Link](https://asgaard.ece.ualberta.ca/papers/Conference/ASE_2022_Macklon_Automatically_Detecting_Visual_Bugs_In_HTML5_Canvas_Games.pdf) |

---

## 7. How to Contribute & Literature Screening Protocol

1. **Add Papers:** Drop candidate PDFs into the appropriate subfolder in `papers/`.
2. **Convert to Markdown:** Execute `uv run scripts/convert_papers.py`.
3. **Record Findings:** Add study row into `literature/evidence_table.csv` and citation to `literature/papers.bib`.
4. **Follow Quality Checklist:** Score the study using `protocol/quality_assessment_checklist.md`.

---

## 8. Citation & Academic Attribution
If you utilize this mapping framework, taxonomy, or dataset matrix in your academic research, please cite:

```bibtex
@misc{phuc2026gamevisualbugdetection,
  author       = {Le Tran Minh Phuc},
  title        = {Computer Vision-Based Visual Testing in Video Games: A Systematic Mapping Study of Detection Techniques, Datasets, and Evaluation Methods},
  year         = {2026},
  publisher    = {GitHub},
  howpublished = {\url{https://github.com/minhphuc477/game-visual-bug-detection}}
}
```

---
*Maintained by Le Tran Minh Phuc · PhD Research Hub*
