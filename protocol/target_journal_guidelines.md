# Target Journal Submission Guidelines & Manuscript Structure

## 1. Primary Target: *Visual Computing for Industry, Biomedicine, and Art* (VCIBA)
- **Publisher:** SpringerOpen / Springer Nature
- **Sponsoring Society:** China Graphics Society (fully covers Article Processing Charges — $0 APC)
- **ISSN:** 2096-496X
- **Indexing:** Scopus (Q1 in Computer Science / Visual Computing), ESCI / Web of Science
- **Article Type:** **Review Article / Systematic Review**
- **Official URL:** [link.springer.com/journal/42492](https://link.springer.com/journal/42492)
- **Review Guidelines:** [link.springer.com/journal/42492/submission-guidelines/review](https://link.springer.com/journal/42492/submission-guidelines/review)

### VCIBA Review Article Formatting Requirements
- **Length:** Typically 6,000–12,000 words (excluding references, abstract, and tables).
- **Abstract:** Unstructured or structured (Background, Main body / Methods, Conclusions), maximum 350 words.
- **Keywords:** 4–6 keywords (e.g. *Visual bug detection, Video game testing, Computer vision, Vision-language models, Systematic mapping study, Visual quality assurance*).
- **Structure:**
  1. **Title Page:** Title, Author list, Affiliations, Corresponding author email.
  2. **Abstract & Keywords**
  3. **Introduction:** Industrial background of game QA, motivation for CV/VLM testing, limitations of prior reviews, research objectives.
  4. **Systematic Review Methodology:** Protocol definition, Research questions (RQ1–RQ6), Search strings, Inclusion/exclusion criteria, PRISMA 2020 flow diagram, Quality assessment.
  5. **Taxonomy of Visual Bugs in Video Games:** Structural definition of 5 glitch families (`GEO`, `TEX`, `REN`, `ANI`, `UI`).
  6. **Mapping Findings (Answers to RQs):**
     - RQ1: Computer Vision & VLM Architectures
     - RQ2: Detectable Bug Manifestations & Severities
     - RQ3: Benchmark Datasets & Annotation Protocols
     - RQ4: Evaluation Metrics & Experimental Rigour
     - RQ5: Cross-Game Generalisation & Domain Shift
  7. **Discussion & Thematic Synthesis:** The single-frame vs temporal gap, black-box vs white-box engine hooks, art style transferability.
  8. **Open Challenges & Future Research Agenda:** Concrete roadmap for subsequent empirical research.
  9. **Conclusions**
  10. **Declarations:** Competing interests, Funding, Authors' contributions, Acknowledgements.
  11. **References:** Springer Vancouver / Basic numbering format.

---

## 2. Backup Target: *Applied Computing and Informatics* (ACI)
- **Publisher:** Emerald Publishing
- **Publishing Model:** Diamond Open Access ($0 APC, hosted by Emerald)
- **ISSN:** 2210-8327
- **Indexing:** Scopus (Q1 in Computer Science Applications / Software), ESCI
- **Article Type:** Systematic Mapping Study / Review Paper
- **Precedent:** Published *Design and Evaluation of Software Reference Architecture: A Systematic Mapping Study* (2026).
- **Official URL:** [emeraldgrouppublishing.com/journal/aci](https://www.emeraldgrouppublishing.com/journal/aci)

---

## 3. Manuscript Preparation Checklist
- [x] Protocol formalized following Petersen et al. (2015) & Kitchenham & Charters (2007).
- [x] PRISMA 2020 flow diagram tracking identification, screening, eligibility, and inclusion counts.
- [x] Primary literature database structured in `literature/evidence_table.csv`.
- [x] Verified BibTeX citations maintained in `literature/papers.bib`.
- [x] Full-text PDFs ingested and converted to Markdown via Microsoft MarkItDown (`scripts/convert_papers.py`).
- [x] All citations verified against original PDF full-text manuscripts.
- [x] Zero-cost publication verified (No author-facing fees).
