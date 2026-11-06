# Section 6: Threats to Validity & Conclusions

## 6.1 Threats to Validity

### 6.1.1 Construct Validity
Construct validity concerns the degree to which our search queries and taxonomy accurately capture the intended concepts of visual testing and graphical glitches. To mitigate terminology bias, our search string incorporated broad synonyms across both software engineering ("visual regression", "automated testing") and visual computing ("rendering defect", "clipping detection", "visual anomaly"). Furthermore, our 5-family taxonomy (`VGVD-Taxonomy`) was iteratively validated against defect categories documented in industrial game studio reports (Electronic Arts, Sony Interactive Entertainment, Xbox Studios) [1, 3, 6, 12, 17].

### 6.1.2 Internal Validity
Internal validity relates to potential researcher bias during study screening, selection, and data extraction. To ensure consistency, all screening decisions were governed by explicit, pre-registered inclusion and exclusion criteria (IC1–IC5, EC1–EC5). Full texts were converted into searchable, provenance-verified Markdown via Microsoft MarkItDown, and quality assessment was conducted using a 10-point appraisal rubric adapted from Dybå & Dingsøyr (2008) [24].

### 6.1.3 External Validity & Generalisability
External validity concerns the extent to which our synthesized findings apply across diverse game genres, budgets, and game engines. Modern video games span immense variance, from indie 2D web games to AAA 3D open worlds built on proprietary engines. While early literature focused on constrained 2D environments [11], recent benchmarks (2025–2026) synthesize empirical evidence across commercial Unreal Engine 5, Unity, and custom commercial engines [1, 6, 17]. Consequently, our findings reflect industrial state-of-the-art production environments.

### 6.1.4 Conclusion Validity
Conclusion validity addresses the reproducibility of the mapping study. All bibliographic queries, extracted evidence tables (`literature/evidence_table.csv`), taxonomy definitions, and conversion scripts are version-controlled and publicly archived in the study's open-science repository [23].

---

## 6.2 Conclusions
Visual quality assurance in modern video game development represents a critical industrial challenge, historically constrained by an overwhelming reliance on labor-intensive manual playtesting. This paper presents the **first systematic mapping study** investigating the convergence of **Computer Vision (CV)** and **Vision-Language Models (VLMs)** for automated visual bug detection and regression testing in video games.

Synthesizing evidence across primary literature from 2020 to 2026, this study provides five principal contributions:
1. **Algorithmic Classification (RQ1):** Categorized detection methods into six paradigms, tracing the evolution from rigid 2D perceptual diffing to self-supervised anomaly detection, multimodal engine-state telemetry fusion, reference-guided VLMs, and spatio-temporal video transformers.
2. **Defect Taxonomy (RQ2):** Established the `VGVD-Taxonomy`, standardizing 19 defect subtypes across five core families: Spatial & Geometry (`GEO`), Material & Texture (`TEX`), Rendering & Lighting (`REN`), Animation & Physics (`ANI`), and User Interface (`UI`).
3. **Benchmark Audit (RQ3):** Provided the first comparative analysis of cutting-edge open benchmarks (*VideoGameQA-Bench*, *RefGlitch-Bench*, *TempGlitch-Video*, *GameBug-20K*), highlighting a dramatic shift toward reproducible open science.
4. **Generalisation & Latency Analysis (RQ4 & RQ5):** Identified the cross-game art style domain shift as the primary performance bottleneck, and contrasted the real-time throughput of lightweight CNNs (45–60 FPS) with the high semantic reasoning but latency-heavy footprint of foundation VLMs (1.2–2.8s per frame).
5. **Future Research Agenda (RQ6):** Outlined five prioritized research directions, emphasizing continuous spatio-temporal video attention, style-invariant pretraining, automated reference frame guidance, and autonomous bug reporting agents.

As interactive entertainment continues to scale toward photorealistic, procedurally infinite virtual worlds, computer vision and multimodal foundation models will become indispensable pillars of the modern game production pipeline. We anticipate that the taxonomy, benchmark audit, and research agenda established in this mapping study will serve as a foundational roadmap for researchers and game engineering practitioners worldwide.

---

## Declarations

### Availability of Data and Materials
The systematic mapping study protocol, tailored search strings, extracted literature evidence database (`evidence_table.csv`), machine-readable visual bug taxonomy (`visual_bug_taxonomy.json`), and automated PDF-to-Markdown ingestion scripts are publicly available in the study's official GitHub repository:  
[https://github.com/minhphuc477/game-visual-bug-detection](https://github.com/minhphuc477/game-visual-bug-detection)

### Competing Interests
The authors declare that they have no competing interests.

### Funding
This research received no external grant funding. All computational and literature ingestion pipelines were developed using open-source tools.

### Authors' Contributions
L.T.M.P. conceived the study, formulated the systematic mapping study protocol, designed the search strategy, extracted and synthesized the literature evidence, developed the `VGVD-Taxonomy`, and wrote the manuscript.
