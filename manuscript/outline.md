# Manuscript Outline: Systematic Mapping Study for VCIBA

**Journal:** *Visual Computing for Industry, Biomedicine, and Art* (SpringerOpen / China Graphics Society)  
**Article Type:** Review Article (Systematic Mapping Study)  
**Target Length:** ~8,000–11,000 words  
**Working Title:** Computer Vision-Based Visual Testing in Video Games: A Systematic Mapping Study of Detection Techniques, Datasets, and Evaluation Methods  
**Authors:** Le Tran Minh Phuc  

---

## Complete Manuscript Architecture

### Title Page & Front Matter
- **Title:** Computer Vision-Based Visual Testing in Video Games: A Systematic Mapping Study of Detection Techniques, Datasets, and Evaluation Methods
- **Authors & Affiliations**
- **Structured Abstract:**
  - *Background:* The high cost and labor bottleneck of manual visual quality assurance (QA) in modern 2D/3D video game production.
  - *Methods:* Systematic mapping study following Petersen et al. and PRISMA 2020 across 5 scholarly databases (2020–2026), defining 6 research questions.
  - *Results:* Synthesis of primary studies classifying techniques (supervised CNN/ViT, self-supervised anomaly detection, engine-state fusion, vision-language models), benchmarking datasets (VideoGameQA-Bench, RefGlitch-Bench, TempGlitch), and evaluating cross-game generalisation.
  - *Conclusions:* Key gaps identified (cross-game domain shift, temporal glitch localization vs. real-time latency, reference guidance vs. hallucination) and a prioritized research agenda.
- **Keywords:** Visual bug detection, Video game testing, Computer vision, Vision-language models, Visual quality assurance, Systematic mapping study, Cross-game generalisation.

---

### Section 1: Introduction & Industrial Background
- **1.1 The QA Bottleneck in Interactive Entertainment:** Scale and cost of modern game development; manual playtesting comprising up to 50% of budgets.
- **1.2 Limitations of Functional Test Automation:** Why headless test runners and unit assertions miss visual artifacts.
- **1.3 Emergence of Visual AI in Game QA:** From 2D perceptual diffing to deep representation learning and multimodal VLMs.
- **1.4 Prior Literature Reviews and Novelty Justification:** Critical analysis of existing software engineering and game AI surveys; proof of novelty for this first computer vision-focused mapping study.
- **1.5 Contributions and Paper Organization.**

---

### Section 2: Systematic Mapping Methodology
- **2.1 Methodological Framework:** Adherence to Petersen et al. (2015) and Kitchenham & Charters (2007).
- **2.2 Research Questions Formulation:** Rationale and mapping targets for RQ1 through RQ6.
- **2.3 Search Strategy & Information Sources:** IEEE Xplore, ACM DL, Scopus, Web of Science, arXiv, and OpenAlex.
- **2.4 Inclusion and Exclusion Criteria:** Explicit boundary rules (2020–2026, empirical CV/VLM models on game frames).
- **2.5 Study Selection Process & PRISMA 2020 Flow:** Identification, screening, eligibility, snowballing, and final inclusion.
- **2.6 Quality Assessment Framework:** 10-point appraisal rubric adapted from Dybå & Dingsøyr (2008).
- **2.7 Data Extraction and Synthesis Strategy:** Extraction variables and bubble plot / classification matrices.

---

### Section 3: Taxonomy of Visual Bugs in Video Games (`VGVD-Taxonomy`)
- **3.1 Motivation for a Standardized Defect Taxonomy.**
- **3.2 Spatial & Geometry Anomalies (`GEO`):** Object mesh clipping, asset penetration, floating props, vertex explosions.
- **3.3 Material, Texture & Shading Defects (`TEX`):** Missing/null checkerboard textures, LOD pop-in delays, UV stretching.
- **3.4 Rendering, Lighting & Camera Artifacts (`REN`):** Z-fighting, shadow acne/disconnection, light bleeding, near-plane frustum clipping.
- **3.5 Temporal, Physics & Animation Glitches (`ANI`):** T-pose freeze, ragdoll solver explosion, cyclic frame stutter, foot-sliding.
- **3.6 User Interface & HUD Defects (`UI`):** Element collision, localized text truncation, resolution scaling distortion.

---

### Section 4: Mapping Study Results (Addressing RQ1–RQ5)
- **4.1 RQ1: Computer Vision & AI Detection Architectures:**
  - Classical image processing & perceptual diffing
  - Supervised object detection & segmentation (YOLO, Faster R-CNN, Mask R-CNN)
  - Self-supervised visual anomaly detection (PatchCore, FastFlow, DINOv2)
  - Multimodal engine-state telemetry fusion (RGB + Depth + Normals + Collision Hooks)
  - Pretrained and reference-guided Vision-Language Models (GPT-4V, Gemini, Qwen2-VL)
  - Spatio-temporal video transformers (TempGlitch)
- **4.2 RQ2: Detectable Bug Manifestations & Coverage:** Mapping models to the 5 defect families.
- **4.3 RQ3: Benchmark Datasets & Data Accessibility:**
  - Public vs. proprietary benchmarks
  - Annotation granularity (image-level, bounding boxes, segmentation masks, QA pairs)
  - Synthetic glitch injection vs. organic human playtest capture
- **4.4 RQ4: Evaluation Metrics & Experimental Rigour:** Precision, Recall, F1, AUROC, False Discovery Rates, and inference FPS for real-time playtesting.
- **4.5 RQ5: Cross-Game Generalisation & Domain Shift:**
  - Empirical performance drops across art styles (photorealistic 3D vs cel-shaded vs voxel)
  - Zero-shot and few-shot adaptation techniques (co-finetuning, weak supervision).

---

### Section 5: Discussion & Critical Research Agenda (Addressing RQ6)
- **5.1 The Single-Frame Fallacy:** Why >65% of gameplay glitches require temporal video reasoning.
- **5.2 The Stylization vs. Glitch Ambiguity:** Distinguishing intentional creative art direction from rendering anomalies.
- **5.3 Black-Box Vision vs. White-Box Engine Telemetry:** Trade-offs between non-intrusive vision and instrumented precision.
- **5.4 Reference Guidance as a Paradigm Shift:** The role of clean baseline frames (Last Clean Frame) in mitigating VLM hallucination.
- **5.5 Actionable Bug Reporting:** Moving from binary glitch classification to autonomous QA agents generating structured reproduction reports.
- **5.6 Prioritized Roadmap for Future Research.**

---

### Section 6: Threats to Validity
- **6.1 Construct Validity:** Selection of search strings and bug terminology.
- **6.2 Internal Validity:** Data extraction consistency and quality scoring.
- **6.3 External Validity:** Generalizability of synthesized findings across commercial indie vs. AAA pipelines.
- **6.4 Conclusion Validity:** Reproducibility of the mapping protocol.

---

### Section 7: Conclusions
- **7.1 Summary of Findings.**
- **7.2 Concluding Remarks & Practical Takeaways for Game Studios.**

---

### Back Matter
- **Declarations:** Competing interests, Funding, Availability of data and materials.
- **References:** Springer Vancouver numbered citations.
