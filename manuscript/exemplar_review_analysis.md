# Structural Anatomy & Publication Strategies of Exemplary Systematic Reviews and Mapping Studies

**Purpose:** Comprehensive comparative analysis of published Systematic Literature Reviews (SLRs) and Systematic Mapping Studies (SMS) in *Visual Computing for Industry, Biomedicine, and Art* (SpringerOpen), *Applied Computing and Informatics* (Emerald), *ACM Computing Surveys* (ACM CSUR), and *Information and Software Technology* (Elsevier IST) to benchmark and elevate our manuscript for publication.

---

## 1. Inventory of Analyzed Reference Reviews (Downloaded & Converted to Markdown)

All reference reviews are archived in `papers/reference_reviews/` and converted into full-text Markdown in `markdown/reference_reviews/`:

1. **VCIBA Exemplar:**  
   *Systematic review and meta-analysis of augmented reality in medicine, retail, and games*  
   - **Journal:** *Visual Computing for Industry, Biomedicine, and Art* (SpringerOpen, 2020)  
   - **DOI:** [10.1186/s42492-020-00057-7](https://doi.org/10.1186/s42492-020-00057-7)  
   - **Full-Text Markdown:** [`markdown/reference_reviews/Xiong_2020_VCIBA_Systematic_Review_and_Meta_Analysis_AR_Games.md`](file:///f:/PhD/markdown/reference_reviews/Xiong_2020_VCIBA_Systematic_Review_and_Meta_Analysis_AR_Games.md) (50,772 characters)
2. **ACM CSUR Game Testing Exemplar:**  
   *A Survey of Video Game Testing* (Politowski et al., ACM CSUR 2021)  
   - **Journal:** *ACM Computing Surveys* (Vol. 54, No. 6, 2021)  
   - **DOI:** [10.1145/3466822](https://doi.org/10.1145/3466822)  
   - **Full-Text Markdown:** [`markdown/reference_reviews/Politowski_2021_Survey_of_Video_Game_Testing_ACM_CSUR.md`](file:///f:/PhD/markdown/reference_reviews/Politowski_2021_Survey_of_Video_Game_Testing_ACM_CSUR.md) (94,980 characters)
3. **ACM CSUR Machine Learning Testing Exemplar:**  
   *Machine Learning Testing: Survey, Landscapes and Horizons* (Zhang, Harman, Ma, Liu, ACM CSUR 2020)  
   - **Journal:** *ACM Computing Surveys* (Vol. 53, No. 1, 2020)  
   - **DOI:** [10.1145/3363562](https://doi.org/10.1145/3363562)  
   - **Full-Text Markdown:** [`markdown/reference_reviews/Zhang_2020_Machine_Learning_Testing_Survey_CSUR.md`](file:///f:/PhD/markdown/reference_reviews/Zhang_2020_Machine_Learning_Testing_Survey_CSUR.md) (332,483 characters)

---

## 2. Comparative Matrix: How Top Venues Structure and Publish Reviews

| Dimension | SpringerOpen (*VCIBA*) | Emerald (*ACI*) | Elsevier (*IST*) | ACM (*CSUR*) |
|---|---|---|---|---|
| **Editorial Appetite** | Visual computing intersection (graphics, vision, HCI, gaming) | Applied computing, enterprise software architectures | Empirical SE, software testing, mapping guidelines | Broad horizons, comprehensive ML/SE surveys |
| **Abstract Format** | 4-part structured (*Background, Methods, Results, Conclusions*) | Mandatory 6-part structured (*Purpose, Design, Findings, Limitations, Practical Impl, Value*) | 5-part structured (*Context, Objective, Method, Results, Conclusion*) | Narrative continuous abstract (250–300 words) + ACM CCS concepts |
| **Methodological Foundation** | PRISMA 2020 / Meta-analysis | Petersen et al. (2015) SMS Guidelines | Petersen et al. (2015) + Kitchenham & Charters | Systematic Survey & Conceptual Taxonomy |
| **Opening Hook / Narrative Style** | Industrial necessity, visual technology convergence across sectors | Practical challenges in complex system architectures | Empirical data gaps, software quality assurance crises | High-impact industry failures (*Cyberpunk 2077*, Tesla crashes) |
| **Taxonomy Structure** | Technical pipeline $\to$ Domain applications | Faceted classification (Design $\times$ Evaluation) | 3-Facet schema (Topic, Contribution, Research type) | Mathematical properties $\to$ Components $\to$ Horizons |
| **Visual Mapping Artifacts** | Hardware/pipeline diagrams, PRISMA flow, Forest plots | 2D Bubble plots (Faceted crossing), Bar charts | Petersen Facet Bubble plots, Venn diagrams, PRISMA trees | Large workflow schematics, hierarchical tree maps |
| **Primary Study Citation** | Numbered sequentially in main references | Dedicated appendix with `[S1]`, `[S2]` IDs | Separate Appendix table / Supplementary data | Comprehensive integrated bibliography (>150 refs) |
| **Open Access & Data Policy** | Gold OA under CC BY 4.0; Data Availability statement mandatory | Diamond OA ($0 APC); Replication statement | Mandatory Data Availability Statement & Zenodo DOI | Open replication package / GitHub repository |

---

## 3. Seven Key Writing Strategies Learned from the Exemplars

### Strategy 1: The "High-Impact Hook" Introduction (Learned from ACM CSUR & VCIBA)
- **The Pattern:** Successful surveys do not open with dry definitions; they open with the economic magnitude of the industry and high-profile production failures.
- **Example in Politowski et al. (2021):** Opens with the catastrophic December 2020 launch of *Cyberpunk 2077*—a \$300M+ game pulled from the PlayStation Store due to visual bugs and day-one glitches, proving that massive budgets and manual testers cannot guarantee quality.
- **Application in Our Paper:** In [`01_introduction.md`](file:///f:/PhD/manuscript/sections/01_introduction.md), we open by contextualizing the \$250B+ interactive media industry, the economic crisis of manual QA consuming 50% of budgets, and the architectural blind spot where headless test runners pass logical tests while leaving broken visuals on screen.

### Strategy 2: Explicit Goal-Question-Metric (GQM) Formulation (Learned from Petersen / IST)
- **The Pattern:** Research questions must not be arbitrary; each must map to an explicit operational need and measurable synthesis output.
- **Application in Our Paper:** In [`02_methodology.md`](file:///f:/PhD/manuscript/sections/02_methodology.md), every RQ (RQ1 to RQ6) includes an explicit **Rationale and Methodological Target**, ensuring reviewers can verify exactly how the extraction variables answer each question.

### Strategy 3: Grounded Multi-Tier Taxonomy (Learned from VCIBA & Zhang et al.)
- **The Pattern:** In visual computing reviews, taxonomies must bridge the *rendering pipeline origin* with the *perceptual manifestation*.
- **Application in Our Paper:** In [`03_taxonomy.md`](file:///f:/PhD/manuscript/sections/03_taxonomy.md), our `VGVD-Taxonomy` classifies defects across 5 families and 19 subtypes, explicitly categorizing each by:
  1. *Temporal Nature:* Static single-frame vs. dynamic temporal multi-frame.
  2. *Visual Subtlety:* Macro obvious vs. micro subtle.
  3. *Pipeline Origin:* Transformation/Collision, Shading, Depth buffer, Physics solver, UI Compositor.

### Strategy 4: The 2D Bubble Plot & Mapping Matrix (Learned from Emerald ACI & Petersen)
- **The Pattern:** Systematic mapping studies are distinguished from standard surveys by crossing two orthogonal classification facets on a 2D grid, with bubble size indicating study density.
- **Application in Our Paper:** In [`04_results_mapping.md`](file:///f:/PhD/manuscript/sections/04_results_mapping.md), we cross **Model Architectural Paradigm** (X-axis: Classical Diffing, Supervised CNN/ViT, Anomaly Detection, Engine-State Fusion, VLMs, Video Transformers) against **Defect Family** (Y-axis: `GEO`, `TEX`, `REN`, `ANI`, `UI`). This visually exposes the dense cluster around static mesh clipping and the severe void around temporal glitches.

### Strategy 5: Contrasting Operational Trade-Offs (Learned from VCIBA)
- **The Pattern:** VCIBA papers emphasize industrial utility and deployment constraints. Reviews must evaluate runtime throughput and hardware latency.
- **Application in Our Paper:** In Section 4.4, we benchmark inference throughput:
  - Lightweight CNNs/YOLO: **45–60 FPS** (viable for real-time live engine assertions).
  - Anomaly Detectors (PatchCore): **15–25 FPS** (viable for near-real-time playtesting).
  - Foundation VLMs (GPT-4V, Gemini): **1.2–2.8 seconds/frame** (restricted to post-session offline video triage).

### Strategy 6: The "Threats to Validity" Quadriad (Learned from Software Engineering Reviews)
- **The Pattern:** Rigorous SMS manuscripts conclude with a systematic 4-part validity threat discussion:
  1. *Construct Validity:* Search query synonyms and terminology coverage.
  2. *Internal Validity:* Extraction consistency and inter-annotator agreement.
  3. *External Validity:* Generalizability across indie vs. AAA game engines.
  4. *Conclusion Validity:* Reproducibility of the mapping protocol.
- **Application in Our Paper:** Fully articulated in [`06_conclusion.md`](file:///f:/PhD/manuscript/sections/06_conclusion.md#61-threats-to-validity).

### Strategy 7: Diamond Open Science & Complete Artifact Transparency
- **The Pattern:** Leading journals require complete data availability statements, open repositories, and replication packages (e.g. Zenodo or GitHub).
- **Application in Our Paper:** All raw search queries, extracted CSV databases (`literature/evidence_table.csv`), converted Markdown texts, BibTeX citations, and compilation scripts are version-controlled and publicly archived at `https://github.com/minhphuc477/game-visual-bug-detection`.

---

## 4. Alignment Verification for Target Submission: VCIBA

Reviewing VCIBA's publication criteria against our compiled manuscript ([`manuscript/complete_manuscript.md`](file:///f:/PhD/manuscript/complete_manuscript.md)):

| VCIBA Submission Requirement | Our Manuscript Status |
|---|---|
| **Interdisciplinary Scope** (Visual Computing + Industry + Games) | **100% Aligned:** Directly addresses industrial game quality assurance, rendering pipelines, and computer vision models. |
| **Systematic Methodology & PRISMA Compliance** | **100% Aligned:** Follows PRISMA 2020 flow, Petersen et al. SMS guidelines, and explicit Boolean search protocols. |
| **Word Count & Structure** (6,000–12,000 words) | **100% Aligned:** Manuscript contains ~10,200 words across Sections 1 to 6. |
| **Abstract Structure** (Background, Methods, Results, Conclusions $\le$ 350 words) | **100% Aligned:** Fully formatted in abstract block of `main.tex` and `complete_manuscript.md`. |
| **Mandatory Back Matter Declarations** | **100% Aligned:** Declarations include Availability of Data, Competing Interests, Funding, and Authors' Contributions. |
| **Numbered Vancouver Citation Style** | **100% Aligned:** Maintained in `references.bib` and sequential numeric citations throughout text. |
| **Zero Author Fees ($0 APC)** | **Confirmed:** Fully sponsored by China Graphics Society. |
