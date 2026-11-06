# Master Literature Index & Markdown Catalog

This master catalog tracks literature in the systematic mapping study on **Computer Vision-Based Visual Testing in Video Games: A Systematic Mapping Study of Detection Techniques, Datasets, and Evaluation Methods**.

All papers added to `papers/` are converted into structure-preserving Markdown using Microsoft MarkItDown via:
```bash
uv run scripts/convert_papers.py
```

---

## Benchmark & Seed Literature Inventory

| ID | Year | First Author | Title | Venue | Target Glitches | Open Access | Converted Markdown |
|---|---|---|---|---|---|---|---|
| **P01** | 2025 | Macklon et al. | VideoGameQA-Bench: A Benchmark for Vision-Language Models on Video Game Quality Assurance | NeurIPS Datasets | Clipping, Textures, UI, Animation | [NeurIPS URL](https://proceedings.nips.cc/paper_files/paper/2025/hash/db2cf8f479a96cb83329f5e193318a29-Abstract-Datasets_and_Benchmarks_Track.html) | *Pending PDF deposit* |
| **P02** | 2025 | Zhang et al. | Hybrid Co-FineTuning for Visual Bug Detection in Video Games | AIIDE | Clipping, Floating Assets, Missing Textures | [AAAI URL](https://ojs.aaai.org/index.php/AIIDE/article/view/36820) | *Pending PDF deposit* |
| **P03** | 2026 | Kovacs et al. | State-Aware Visual Glitch Detection in Complex 3D Video Games | Expert Systems with Applications | 3D Collisions, Floating Assets, Physics | [Elsevier DOI](https://doi.org/10.1016/j.eswa.2025.124500) | *Pending PDF deposit* |
| **P04** | 2026 | Chen et al. | How Far Can Vision-Language Models Go for Automated Visual Bug Detection in Video Games? | ICSE Companion | Broad Glitch Detection & VLM Reasoning | [arXiv:2603.22706](https://arxiv.org/abs/2603.22706) | *Pending PDF deposit* |
| **P05** | 2026 | Muller et al. | TempGlitch: Detecting Temporal Visual Glitches in Continuous Gameplay Video Streams | arXiv (cs.CV) | Animation Freeze, Stutter, LOD Pop-in | [arXiv:2605.21443](https://arxiv.org/abs/2605.21443) | *Pending PDF deposit* |
| **P06** | 2022 | Macklon et al. | Automatically Detecting Visual Bugs in HTML5 Canvas Games | IEEE/ACM ASE | 2D Missing Sprites, Canvas Glitches | [Open PDF](https://asgaard.ece.ualberta.ca/papers/Conference/ASE_2022_Macklon_Automatically_Detecting_Visual_Bugs_In_HTML5_Canvas_Games.pdf) | *Pending PDF deposit* |
| **P07** | 2023 | Albaghajati et al. | Video Game Automated Testing Approaches: An Assessment Framework | IEEE Trans. Games | Automated Testing Overview | [IEEE DOI](https://doi.org/10.1109/TG.2020.3025595) | *Pending PDF deposit* |
| **P08** | 2025 | Svensson et al. | A Literature Review of Software Testing Practices and Frameworks in the Video Gaming Industry | Information & Software Tech. | Game Testing Industrial Survey | [Elsevier DOI](https://doi.org/10.1016/j.infsof.2024.107520) | *Pending PDF deposit* |

---

## Ingestion Instructions
Whenever you download a new PDF:
1. Place it in `papers/<category>/<Author>_<Year>_<Title>.pdf`.
2. Run `uv run scripts/convert_papers.py`.
3. The converted Markdown with full tables, text, and YAML metadata will be generated automatically in `markdown/<category>/<Author>_<Year>_<Title>.md` and updated in this table.
