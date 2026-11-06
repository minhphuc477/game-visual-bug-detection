# Section 3: Systematic Mapping Methodology

## 3.1 Methodological Framework & Reporting Standards
This systematic mapping study adheres strictly to the guidelines for Software Engineering Systematic Mapping Studies formulated by **Petersen et al. (2015)** [20] and the methodological recommendations of **Kitchenham and Charters (2007)** [21]. While a systematic literature review (SLR) synthesizes empirical evidence around narrow, highly homogeneous outcomes, a Systematic Mapping Study (SMS) is designed to provide a broad, structured overview of an emerging research area, establishing taxonomies, quantifying publication distributions, identifying clusters of high activity, and charting unexplored research gaps [20].

Reporting transparency is maintained in compliance with the **PRISMA 2020 (Preferred Reporting Items for Systematic Reviews and Meta-Analyses)** statement [22], the **PRISMA-S search reporting extension** [23], and relevant evidence synthesis guidance from the **ROSES (RepOrting standards for Systematic Evidence Syntheses)** protocol [24]. The complete mapping protocol was registered *a priori* in the study's open-science repository [25].

---

## 3.2 Formulation of Research Questions
In accordance with the Goal-Question-Metric (GQM) perspective [20], each Research Question investigates a distinct structural dimension of the literature landscape:

* **RQ1 (Techniques & Methods):** *What computer vision, deep learning, and vision-language techniques have been investigated for visual quality assurance in video games?*  
  *Rationale:* Catalog algorithmic paradigms, contrasting classical perceptual diffing, supervised CNN/ViT detectors, self-supervised anomaly detectors, engine-state multimodal fusion, foundation vision-language models, and spatio-temporal video transformers.
* **RQ2 (Visual Testing Tasks):** *What types of visual testing and defect-detection tasks have been investigated across video games?*  
  *Rationale:* Classify the spectrum of graphical anomalies addressed in primary literature and identify which defect categories (e.g., spatial mesh clipping, texture streaming pop-in, Z-fighting, foot-sliding) remain under-addressed.
* **RQ3 (Datasets & Benchmarks):** *What datasets and benchmarks are used to develop and evaluate visual testing approaches, and how accessible are they?*  
  *Rationale:* Audit data availability, annotation granularity, commercial vs. open-source titles, synthetic vs. organic capture protocols, and open-science reproducibility.
* **RQ4 (Evaluation Methodologies):** *How are computer vision-based visual testing approaches evaluated in video games?*  
  *Rationale:* Examine empirical evaluation practices, analyzing precision, recall, F1, AUROC, false positive rates, and real-time inference latency (FPS) required for production playtesting.
* **RQ5 (Research Trends & Gaps):** *What research trends, cross-game generalization limitations, and future research opportunities can be identified?*  
  *Rationale:* Assess domain transfer across distinct artistic styles and rendering engines, synthesizing explicit failure modes into a prioritized research agenda.

---

## 3.3 Search Strategy & Information Sources
The literature search strategy was executed across five authoritative electronic bibliographic databases spanning Computer Science, Software Engineering, and Visual Computing:
1. **IEEE Xplore Digital Library**
2. **ACM Digital Library**
3. **Scopus**
4. **Web of Science (Core Collection)**
5. **arXiv e-Print Archive** (categories: `cs.CV`, `cs.SE`, `cs.AI`, `cs.GR`)

Supplementary searches and forward/backward citation chaining were conducted using **OpenAlex** and **Semantic Scholar**.

### Search Query Design
The search strategy combined three major concept clusters using Boolean operators (`AND` across facets, `OR` within facets):
1. **Technique Facet:** Computer Vision, Deep Learning, Vision-Language Model, Visual Anomaly Detection, Image Recognition, Visual Regression.
2. **Domain Facet:** Video Game, Game Testing, Game Quality Assurance, Gameplay Video, Game Engine.
3. **Problem Facet:** Visual Bug, Visual Glitch, Rendering Defect, Clipping Detection, Graphical Anomaly, Visual Defect.

The canonical search query is formulated as:
```text
( "computer vision" OR "deep learning" OR "vision-language model" OR "visual anomaly detection" OR "image recognition" OR "visual regression" )
AND
( "video game" OR "game testing" OR "game quality assurance" OR "gameplay video" OR "game engine" )
AND
( "visual bug" OR "visual glitch" OR "rendering defect" OR "clipping detection" OR "graphical anomaly" OR "visual defect" )
```
Search queries were adapted to the syntax and field tags of each respective database. Searches spanned literature published between **January 2018 and November 2026**.

---

## 3.4 Inclusion & Exclusion Criteria
To ensure high scientific rigour and empirical relevance, candidate papers were screened against explicit Inclusion Criteria (IC) and Exclusion Criteria (EC):

### Inclusion Criteria (IC):
- **IC1:** Published between **January 1, 2018 and November 2026**.
- **IC2:** Proposes, evaluates, or empirically benchmarks a computer vision, deep learning, or vision-language technique for detecting visual defects, graphical glitches, or visual regressions in video games.
- **IC3:** Employs empirical evaluation using gameplay screenshots, video frame sequences, or rendering engine buffers.
- **IC4:** Published as a peer-reviewed journal article, conference proceeding, workshop paper, or authoritative technical benchmark preprint.
- **IC5:** Written in English with full text accessible.

### Exclusion Criteria (EC):
- **EC1:** Papers addressing purely non-visual game testing (e.g., functional code unit testing, network packet fuzzing, server load testing, or headless memory profiling without visual inspection).
- **EC2:** Papers focusing exclusively on reinforcement learning (RL) game-playing agents or procedural level generation without visual anomaly detection or visual QA capabilities.
- **EC3:** Studies using video games purely as a synthetic image generation simulator for external real-world applications (e.g., autonomous driving, drone navigation) without investigating game visual bugs.
- **EC4:** Short extended abstracts, posters, tutorial descriptions, keynote summaries, or non-technical editorials (< 4 pages).
- **EC5:** Duplicate publications of the same study (the most complete peer-reviewed version is retained).

---

## 3.5 Study Selection & Screening Execution
The study selection process followed the four-phase PRISMA-S funnel depicted in **Figure 1**:

![Figure 1: PRISMA-S 2020 Literature Selection Flow Diagram](figures/figure1_prisma_flow.png)

1. **Automated Search & Ingestion:** Executing queries across five electronic bibliographic databases (IEEE Xplore: 142, ACM DL: 118, Scopus: 184, Web of Science: 96, arXiv: 152) yielded **692 raw bibliographic records**.
2. **Deduplication:** Matching DOIs, normalized titles, and author signatures eliminated **188 duplicate records**, leaving **504 unique publications** for title and abstract screening.
3. **Title and Abstract Screening:** Screening against IC1–IC5 and EC1–EC5 eliminated **416 records** unrelated to visual game testing (primarily non-visual RL gameplay agents, general software unit testing, and non-game visual diffing).
4. **Full-Text Retrieval & Conversion:** Full texts of the remaining **88 candidate manuscripts** were retrieved. Unstructured PDFs and publisher XMLs were converted into structured Markdown and extracted figure assets using `academic-pdf2md` (PyMuPDF4LLM + RapidOCR) to enable full-text indexing, regex searching, and in-depth qualitative analysis.
5. **Full-Text Eligibility Appraisal:** Detailed review of full-text manuscripts eliminated **47 studies** with recorded reasons: 18 headless logic/functional tests without visual rendering, 12 bot gameplay implementations lacking visual QA metrics, 9 non-game UI regression studies, and 8 studies lacking empirical evaluations or reporting metrics.
6. **Snowball Chaining:** Backward reference harvesting and forward citation tracking on landmark benchmarks (e.g., *VideoGameQA-Bench*, *RefGlitch-Bench*, *TempGlitch*) identified **4 additional eligible primary studies**, yielding a final corpus of **45 included primary studies**.

---

## 3.6 Quality Assessment (QA) Framework
To evaluate methodological robustness, primary studies were appraised using a 10-point Quality Assessment checklist adapted from **Dybå and Dingsøyr (2008)** [24] and **Kitchenham et al.** [21]:

| QA Item | Criterion Description | Evaluation Focus |
|---|---|---|
| **QA1** | Are research objectives, target visual bugs, and operational contexts explicitly defined? | Research Rigour |
| **QA2** | Is the computer vision / VLM architecture described with sufficient technical detail for replication? | Reproducibility |
| **QA3** | Is the dataset described adequately (number of games, total frames, resolution, capture setup, clean vs. buggy distribution)? | Dataset Validity |
| **QA4** | Are ground-truth annotations and verification procedures clearly documented (e.g., inter-annotator agreement, synthetic injection)? | Annotation Reliability |
| **QA5** | Are baselines or standard benchmark models included for comparative evaluation? | Comparative Validity |
| **QA6** | Are standard evaluation metrics reported (Precision, Recall, F1, AUROC, False Positive Rate)? | Metric Validity |
| **QA7** | Did the study investigate cross-game generalisation (testing on games or assets unseen during training)? | Generalisability |
| **QA8** | Did the authors report computational complexity, inference time, or frame rates (FPS) relevant to real-time QA? | Industrial Applicability |
| **QA9** | Are limitations, failure cases, and false positive triggers critically discussed? | Critical Appraisal |
| **QA10** | Are code repositories, pretrained model weights, or dataset archives publicly accessible? | Open Science |

Each item is scored on a 3-point scale: **Yes (1.0)**, **Partially (0.5)**, or **No (0.0)**, yielding an aggregate Quality Score between 0.0 and 10.0. Studies scoring $\ge 7.5$ are designated *High Quality*, forming the core of our quantitative synthesis.

---

## 3.7 Data Extraction and Evidence Base
Data extraction was executed using a standardized schema populated into the study's evidence database (`literature/evidence_table.csv`) [25]. Variables include: bibliographic metadata, algorithmic paradigms, backbone architectures, input modalities (RGB, optical flow, depth maps, collision matrices), addressed bug categories from `VGVD-Taxonomy`, dataset provenance, empirical metrics, and explicit limitations reported by authors.
