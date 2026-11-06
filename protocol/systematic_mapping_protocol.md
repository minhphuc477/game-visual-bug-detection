# Research Protocol

## 1. Proposed Title

**Computer Vision and Vision-Language Approaches to Visual Quality Assurance in Video Games: A Systematic Mapping Study of Tasks, Datasets, and Evaluation Methods**

### Study type

Systematic Mapping Study (SMS).

### Research domain

Computer Science, Software Engineering, Computer Vision, Artificial Intelligence, and Game Development.

### Methodological foundation

The study will follow the systematic mapping guidelines proposed by Petersen et al. (2015), supplemented by relevant systematic search and reporting practices from PRISMA-S. The ROSES systematic map reporting checklist may also be used as a supplementary reporting resource.

### Protocol version

Version 1.0 — 6 November 2026.

---

# 2. Background and Rationale

Video games are increasingly complex software systems involving real-time rendering, interactive environments, animation, graphical interfaces, and dynamic visual content.

Ensuring visual quality is an important part of game development and software quality assurance. Visual defects can include missing textures, rendering errors, graphical glitches, incorrect object placement, broken animations, unexpected visual artefacts, and inconsistencies between expected and actual game output.

Traditional game testing approaches often focus on gameplay functionality, software logic, performance, and functional correctness. However, these approaches do not necessarily identify visual defects that occur during gameplay.

Recent developments in computer vision, deep learning, anomaly detection, and vision-language models have created opportunities for automating visual quality assurance in video games.

Research in this area includes several related activities:

- Computer vision-based visual defect detection.

- Automated visual regression testing.

- Visual anomaly and glitch detection.

- Image-based and video-based game analysis.

- Visual interface and object verification.

- Temporal detection and localization of visual defects.

- Vision-language-based game testing and bug reporting.

Despite the growing research activity, relevant contributions are distributed across different research communities, including software engineering, computer vision, artificial intelligence, and game development.

Consequently, the terminology, testing tasks, datasets, experimental methods, and evaluation metrics may differ between studies.

A systematic mapping study is appropriate because its primary purpose is to organize and classify the available research, identify research concentrations, and expose areas where evidence remains limited.

This study will develop a structured classification of computer vision and vision-language approaches to visual quality assurance in video games.

The study will not assume that a research gap exists before the literature has been examined. Instead, potential gaps and research opportunities will be identified through the systematic mapping process.

---

# 3. Aim and Objectives

## 3.1 Overall aim

To systematically identify, classify, and analyze existing research on computer vision and vision-language approaches to visual quality assurance in video games, focusing on testing tasks, detection techniques, datasets, evaluation methods, and research trends.

## 3.2 Research objectives

The study has six objectives:

1. Identify computer vision and vision-language techniques applied to visual testing and visual defect detection in video games.

2. Classify the visual testing tasks investigated in existing research.

3. Identify the datasets, benchmarks, and data-generation approaches used.

4. Examine the evaluation metrics and experimental methodologies employed.

5. Map research trends across publication years, venues, game genres, and platforms.

6. Identify limitations and research opportunities based on the distribution and characteristics of existing studies.

---

# 4. Research Questions

The research questions are designed to be descriptive and classificatory, consistent with the objectives of a systematic mapping study.

## RQ1 — Techniques and Methods

What computer vision, deep learning, and vision-language techniques have been investigated for visual quality assurance in video games?

Subcategories:

- Traditional image processing.

- Image comparison and similarity techniques.

- Convolutional neural networks.

- Object detection and image classification.

- Deep learning-based anomaly detection.

- Video understanding and temporal analysis.

- Vision-language models.

- Hybrid and agent-based approaches.

Purpose:

To identify the methodological landscape and determine which technique families have received the most research attention.

## RQ2 — Visual Testing Tasks

What types of visual testing and defect-detection tasks have been investigated in video games?

Subcategories:

- Visual unit testing.

- Visual regression testing.

- Visual glitch and anomaly detection.

- Visual defect localization.

- Temporal glitch detection.

- Graphical user interface verification.

- Object and scene verification.

- Automated visual bug report generation.

Purpose:

To distinguish the different problems addressed by existing approaches rather than treating all visual testing activities as equivalent.

## RQ3 — Datasets and Benchmarks

What datasets and benchmarks are used to develop and evaluate computer vision-based visual testing approaches in video games?

Subcategories:

- Real gameplay data.

- Synthetic or artificially generated defects.

- Manually annotated datasets.

- Automatically annotated datasets.

- Image-based datasets.

- Video-based datasets.

- Publicly available benchmarks.

- Private or unreleased datasets.

Additional characteristics:

- Number of games.

- Number of images or video clips.

- Defect categories.

- Annotation method.

- Dataset availability.

- Licensing and accessibility.

- Single-game or multi-game coverage.

Purpose:

To establish the availability, characteristics, and limitations of research data and evaluation benchmarks.

## RQ4 — Evaluation Methodologies

How are computer vision-based visual testing approaches evaluated in video games?

Subcategories:

- Accuracy.

- Precision.

- Recall.

- F1-score.

- Intersection over Union (IoU).

- Average Precision (AP).

- Temporal Intersection over Union.

- False-positive and false-negative rates.

- Detection latency.

- Human evaluation.

- Model-based or LLM-as-judge evaluation.

Additional considerations:

- Training and testing procedures.

- Baseline comparisons.

- Cross-game evaluation.

- Cross-platform evaluation.

- Reproducibility.

- Statistical reporting.

Purpose:

To identify the evaluation practices used and determine whether the field has developed consistent approaches to measuring visual testing performance.

## RQ5 — Research Trends and Gaps

What research trends, limitations, and future research opportunities can be identified in computer vision-based visual quality assurance for video games?

Subcategories:

- Publication trends.

- Research communities and publication venues.

- Game genres and platforms.

- Dataset availability.

- Temporal reasoning.

- Cross-game generalization.

- Rare defect detection.

- Explainability.

- Reproducibility.

- Real-world deployment.

Purpose:

To develop an evidence-based research agenda grounded in the findings of the mapping study.

---

# 5. Research Scope

## 5.1 Included research domain

The study will focus on research involving computer vision, image processing, deep learning, anomaly detection, or vision-language approaches applied to visual quality assurance in video games.

The term video games includes:

- PC games.

- Console games.

- Mobile games.

- Browser-based games.

- Games developed using commercial or open-source game engines.

- Research prototypes and experimental game environments.

## 5.2 Definition of visual quality assurance

For this study, visual quality assurance refers to the automated or semi-automated identification, verification, comparison, localization, or reporting of visual properties and defects in video game environments.

A study must have a clear connection to visual testing, visual defect identification, or visual verification.

General game-playing agents, game understanding, and image recognition will not automatically qualify unless their methods are explicitly applied to a visual testing or quality-assurance task.

## 5.3 Publication period

The search will cover publications from database inception to the final search date.

No arbitrary starting year will be imposed during the initial search.

The final search date will be recorded, and the analysis will report publication trends by year.

A supplementary analysis may emphasize developments from 2020 onward to examine recent advances in deep learning and vision-language models.

---

# 6. Search Strategy

## 6.1 Information sources

The following databases will be searched:

| Database | Reason for inclusion |

|---|---|

| Scopus | Broad multidisciplinary research coverage |

| Web of Science | Cross-disciplinary research coverage |

| IEEE Xplore | Computer vision, AI, and software testing |

| ACM Digital Library | Software engineering and game research |

| ScienceDirect | Software engineering and computer science |

| SpringerLink | Computer vision, AI, and software engineering |

ArXiv will be searched separately as a supplementary source for recent preprints.

Google Scholar will be used for supplementary discovery and citation searching, not as a substitute for the main database searches.

OpenAlex may be used to identify additional publications and metadata.

Conference proceedings will be included because they are important publication outlets in Computer Science.

## 6.2 Search concepts

The search strategy will combine three main concepts:

**Concept A — Video games**

- Video game

- Video games

- Videogame

- Gameplay

- Game engine

- Game testing

- Game quality assurance

**Concept B — Visual testing**

- Visual testing

- Visual bug

- Visual glitch

- Visual anomaly

- Visual regression

- Rendering error

- Graphical defect

- Visual quality assurance

**Concept C — Computer vision and AI**

- Computer vision

- Image processing

- Deep learning

- Convolutional neural network

- Object detection

- Anomaly detection

- Vision-language model

- Multimodal model

## 6.3 Primary search string

The following search string will be used as the starting point and adapted to each database's syntax:

```text

(

  "video game*" OR videogame* OR gameplay OR

  "game engine*" OR "game testing" OR

  "game quality assurance"

)

AND

(

  "visual testing" OR "visual bug*" OR

  "visual glitch*" OR "visual anomaly" OR

  "visual regression" OR "rendering error*" OR

  "graphical defect*" OR "visual quality assurance"

)

```

The primary search intentionally does not require computer vision terminology.

This is important because relevant studies may describe their methods using task-specific terminology without explicitly using the phrase "computer vision."

## 6.4 Supplementary method-focused search

A second search will identify studies that may not use the visual-testing terminology above:

```text

(

  "video game*" OR videogame* OR gameplay OR

  "game engine*"

)

AND

(

  "computer vision" OR "image processing" OR

  "deep learning" OR CNN OR

  "object detection" OR "anomaly detection" OR

  "vision-language model*" OR

  "multimodal model*"

)

AND

(

  detection OR testing OR benchmark OR

  evaluation OR verification

)

```

Results from this supplementary search must still satisfy the inclusion criteria.

## 6.5 Search validation

Before conducting the final searches, the search strings will be tested against a set of known relevant publications.

The validation set will include studies on:

- Automated visual bug detection in games.

- Game visual glitch benchmarks.

- Visual regression testing in games.

- Vision-language approaches to game testing.

- Video-based visual defect detection.

The search strategy will be refined if known relevant studies are not retrieved.

The final search strings, database names, search dates, filters, and result counts will be recorded.

## 6.6 Citation searching

Backward and forward citation searching will be conducted on the included studies and relevant review papers.

Backward snowballing will identify relevant publications cited by included studies.

Forward snowballing will identify publications that cite the included studies.

Additional papers discovered through snowballing will undergo the same eligibility screening as database results.

---

# 7. Eligibility Criteria

## 7.1 Inclusion criteria

A publication will be included when it satisfies all applicable criteria:

**IC1:** It investigates video games, game environments, or game-engine-based environments.

**IC2:** It addresses a visual testing, visual verification, visual anomaly detection, visual defect detection, visual regression, or closely related quality-assurance task.

**IC3:** It proposes, applies, evaluates, or benchmarks a computer vision, image processing, deep learning, or vision-language approach.

**IC4:** It provides sufficient methodological information to identify its research contribution.

**IC5:** It is an accessible full-text publication or an accessible manuscript containing sufficient information for screening and data extraction.

Eligible publication types:

- Peer-reviewed journal articles.

- Peer-reviewed conference papers.

- Peer-reviewed workshop papers, where they contain sufficient methodological detail.

- Preprints, including arXiv papers, reported separately from peer-reviewed publications.

## 7.2 Exclusion criteria

A publication will be excluded when:

**EC1:** It investigates game-playing agents or gameplay strategy without a visual testing or quality-assurance component.

**EC2:** It focuses exclusively on functional testing, gameplay logic, performance testing, or software correctness without visual testing.

**EC3:** It investigates visual testing of non-game software without evaluating or explicitly adapting the approach to video games.

**EC4:** It focuses on generating game graphics, textures, or environments without evaluating visual quality assurance.

**EC5:** It is an editorial, opinion article, abstract-only publication, tutorial, or non-research article without sufficient methodological information.

**EC6:** It is a duplicate publication of an already included study without a distinct contribution.

**EC7:** Its full text cannot be obtained after reasonable attempts through legal open-access sources, author repositories, or author contact.

## 7.3 Treatment of preprints

Preprints will not automatically be treated as equivalent to peer-reviewed publications.

Each study will be assigned a publication-status category:

- Peer-reviewed journal article.

- Peer-reviewed conference paper.

- Peer-reviewed workshop paper.

- Preprint.

- Other research report.

If a preprint is later published in a peer-reviewed venue, the published version will be used as the primary record, while the relationship between versions will be documented.

Results will distinguish peer-reviewed evidence from preprint evidence.

---

# 8. Study Selection Process

The selection process will consist of four stages.

## Stage 1 — Identification

All database search results will be exported with available bibliographic information.

The records will be imported into Zotero or another reference-management tool.

Duplicate records will be identified and removed.

## Stage 2 — Title and abstract screening

Titles and abstracts will be assessed against the eligibility criteria.

Clearly irrelevant studies will be excluded.

Uncertain records will be retained for full-text screening.

## Stage 3 — Full-text screening

Full texts will be examined to determine whether the studies satisfy the inclusion criteria.

The reason for each full-text exclusion will be recorded using predefined categories.

## Stage 4 — Final inclusion

The final set of eligible studies will form the primary study corpus.

A flow diagram will report:

- Records identified.

- Duplicates removed.

- Records screened.

- Records excluded.

- Full texts assessed.

- Full texts excluded with reasons.

- Studies included.

The selection process will be documented using a PRISMA-style flow diagram, adapted for the systematic mapping study.

## Reviewer arrangements

Ideally, two reviewers will independently screen the records.

Disagreements will be resolved through discussion or a third reviewer.

If the study is conducted by a single researcher, the researcher will screen all records and a second person will independently check a predefined sample and disputed cases.

The actual reviewer arrangement will be reported transparently.

---

# 9. Data Extraction

A structured extraction form will be developed and piloted on a small sample of eligible studies before full extraction begins.

The following information will be collected.

## 9.1 Bibliographic information

- Study identification number.

- Title.

- Authors.

- Publication year.

- Journal or conference.

- Publisher.

- DOI or permanent identifier.

- Publication status.

- Country or research affiliation, where reported.

## 9.2 Research characteristics

- Research objective.

- Research problem.

- Main contribution.

- Research methodology.

- Research community.

- Game or game environment investigated.

## 9.3 Visual testing task

Each study will be classified according to its primary task:

1. Visual unit testing.

2. Visual regression testing.

3. Visual glitch or anomaly detection.

4. Visual defect localization.

5. Temporal glitch detection.

6. Graphical user interface verification.

7. Object or scene verification.

8. Automated visual bug reporting.

9. Other visual quality-assurance tasks.

Multiple categories may be assigned when a study addresses more than one task.

## 9.4 Technical approach

- Traditional image processing.

- Image comparison.

- CNN-based methods.

- Object detection.

- Image classification.

- Anomaly detection.

- Video analysis.

- Vision-language models.

- Multimodal models.

- Hybrid approaches.

- Other methods.

The actual model or algorithm name will also be recorded.

## 9.5 Dataset and benchmark characteristics

- Dataset or benchmark name.

- Number of games.

- Game titles, where disclosed.

- Game genres.

- Number of screenshots.

- Number of video clips or frames.

- Visual defect categories.

- Real or synthetic data.

- Annotation method.

- Public or private availability.

- Licensing information, where available.

## 9.6 Modality and temporal characteristics

- Screenshot-based.

- Video-based.

- Image and video combined.

- Frame-level detection.

- Temporal detection.

- Timestamp localization.

- Single-game evaluation.

- Multi-game evaluation.

- Cross-game evaluation.

## 9.7 Evaluation methodology

- Accuracy.

- Precision.

- Recall.

- F1-score.

- Average Precision.

- Intersection over Union.

- Temporal Intersection over Union.

- False-positive rate.

- False-negative rate.

- Detection latency.

- Human evaluation.

- LLM-as-judge evaluation.

- Other evaluation methods.

The original metric names and definitions will be recorded to avoid treating different measurements as interchangeable.

## 9.8 Study limitations

- Limitations reported by the authors.

- Dataset limitations.

- Methodological limitations.

- Generalization limitations.

- Computational limitations.

- Reproducibility limitations.

- Identified future research directions.

---

# 10. Classification Framework

The extracted studies will be organized using a multidimensional classification framework.

| Classification dimension | Main categories |

|---|---|

| Visual testing task | Unit testing, regression testing, glitch detection, localization, bug reporting |

| Technical approach | Traditional CV, deep learning, anomaly detection, VLM, hybrid |

| Data modality | Image, video, image and video |

| Dataset provenance | Real, synthetic, mixed |

| Annotation approach | Manual, automatic, weak supervision, mixed |

| Evaluation | Classification, localization, temporal, human, model-based |

| Game coverage | Single-game, multi-game, cross-game |

| Publication type | Journal, conference, workshop, preprint |

| Research maturity | Conceptual, prototype, experimental, benchmark-based, deployed |

Categories will be refined during pilot extraction.

The classification scheme will be documented with operational definitions and examples.

A study may belong to multiple categories where appropriate.

---

# 11. Data Analysis and Synthesis

The study will primarily use descriptive quantitative analysis and structured qualitative classification.

It will not attempt to combine model performance results into a single pooled effect estimate because the research tasks, datasets, and evaluation conditions may differ substantially.

## 11.1 Descriptive analysis

The following distributions will be calculated:

- Number of publications per year.

- Number of publications by venue.

- Number of publications by research community.

- Frequency of visual testing tasks.

- Frequency of technical approaches.

- Frequency of dataset types.

- Frequency of evaluation metrics.

- Distribution of game genres and platforms.

Counts and percentages will be reported with clearly stated denominators.

## 11.2 Cross-dimensional analysis

The study will examine relationships between classification dimensions.

Examples:

- Technique type versus visual testing task.

- Dataset provenance versus detection approach.

- Image-based versus video-based methods.

- Evaluation metrics versus testing task.

- Single-game versus cross-game evaluation.

- Publication year versus technique family.

## 11.3 Planned visualizations

The following figures and tables are proposed:

**Figure 1:** Study selection flow diagram.

**Figure 2:** Publications by year and research community.

**Figure 3:** Bubble map of technical approaches versus visual testing tasks.

**Figure 4:** Dataset characteristics and provenance matrix.

**Figure 5:** Image-based and video-based research distribution.

**Figure 6:** Evaluation metrics used across research tasks.

**Figure 7:** Cross-game evaluation coverage.

**Table 1:** Included study characteristics.

**Table 2:** Technical approaches and algorithms.

**Table 3:** Datasets and benchmarks.

**Table 4:** Evaluation methodologies.

**Table 5:** Research limitations and opportunities.

Empty or sparsely populated categories will be examined as potential research gaps, but their significance will be interpreted in the context of search coverage and publication maturity.

---

# 12. Quality and Reproducibility Assessment

Although the primary purpose of an SMS is mapping rather than ranking the strength of evidence, basic methodological characteristics will be recorded.

Each study will be examined for:

- Clarity of research objectives.

- Description of the proposed method.

- Description of the experimental environment.

- Dataset transparency.

- Evaluation procedure transparency.

- Availability of code or implementation.

- Availability of datasets.

- Reproducibility information.

These characteristics will be reported descriptively.

Studies will not automatically be excluded merely because their code or datasets are unavailable. Such limitations will be recorded and discussed.

No unsupported overall quality score will be created.

---

# 13. Reporting and Research Transparency

The final study will report its methodology in sufficient detail to permit replication.

The following supplementary materials will be prepared:

1. Complete search strings for each database.

2. Search dates and database result counts.

3. Inclusion and exclusion criteria.

4. Study selection records.

5. Full-text exclusion reasons.

6. Data extraction form.

7. Final classification scheme.

8. List of included studies.

9. Analysis data and visualization scripts, where possible.

The protocol and supplementary materials may be deposited in the Open Science Framework (OSF).

The final report will use the Petersen et al. (2015) mapping-study guidance as its principal methodological foundation, with PRISMA-S search-reporting practices and relevant ROSES reporting elements used where appropriate.

---

# 14. Threats to Validity

Four principal threats will be considered.

## 14.1 Construct validity

Search terms may fail to capture studies using different terminology.

Mitigation:

- Use multiple search strings.

- Validate searches against known relevant studies.

- Conduct backward and forward snowballing.

- Document search limitations.

## 14.2 Selection validity

Study selection may be influenced by subjective interpretation.

Mitigation:

- Use predefined eligibility criteria.

- Pilot the screening procedure.

- Use independent screening where feasible.

- Record exclusion reasons.

## 14.3 Classification reliability

Different researchers may classify the same study differently.

Mitigation:

- Define categories operationally.

- Pilot the extraction form.

- Document ambiguous cases.

- Review and refine classification decisions.

## 14.4 External validity

The findings may not represent every game genre, platform, or industrial testing environment.

Mitigation:

- Include multiple game platforms.

- Include different research communities.

- Report coverage limitations.

- Avoid generalizing beyond the included evidence.

---

# 15. Expected Contributions

The study is expected to provide five contributions.

**Contribution 1 — Research taxonomy**

A structured classification of computer vision and vision-language approaches to visual quality assurance in video games.

**Contribution 2 — Task landscape**

An overview distinguishing visual regression, glitch detection, visual verification, temporal detection, and related testing tasks.

**Contribution 3 — Dataset and benchmark landscape**

A consolidated inventory of available datasets, benchmarks, data-generation strategies, annotation approaches, and accessibility.

**Contribution 4 — Evaluation landscape**

A systematic overview of evaluation metrics and experimental protocols.

**Contribution 5 — Evidence-based research agenda**

A set of research opportunities supported by observed limitations and underrepresented areas in the mapped literature.

Potential research opportunities to investigate include:

- Cross-game generalization.

- Temporal visual defect detection.

- Publicly available real-world defect datasets.

- Rare and previously unseen defect detection.

- Standardized evaluation benchmarks.

- Explainable visual defect detection.

- Reproducible experimental frameworks.

- Efficient deployment in game development pipelines.

These are candidate areas for investigation, not predetermined findings.

---

# 16. Proposed Manuscript Structure

The final paper will follow this structure:

1. Introduction

2. Background and Related Work

3. Research Methodology

4. Results

5. Discussion

6. Research Implications and Future Directions

7. Threats to Validity

8. Conclusion

9. References

10. Supplementary Materials

The Introduction will explain the research problem and establish the need for the study.

The Related Work section will compare the proposed mapping study with existing surveys and reviews.

The Methodology section will describe the complete protocol and its implementation.

The Results section will answer the research questions using descriptive statistics, classification tables, and visual maps.

The Discussion will interpret the mapped evidence and identify implications for researchers and game developers.

The Threats to Validity section will discuss limitations of the search, selection, classification, and analysis.

The Conclusion will summarize the findings and identify future research directions.

---

# 17. Methodological References

The following publications will provide the methodological foundation:

1. Petersen, K., Vakkalanka, S., & Kuzniarz, L. (2015). Guidelines for conducting systematic mapping studies in software engineering: An update. *Information and Software Technology, 64*, 1–18. https://doi.org/10.1016/j.infsof.2015.03.007

2. Petersen, K., Feldt, R., Mujtaba, S., & Mattsson, M. (2008). Systematic mapping studies in software engineering. In *Proceedings of the 12th International Conference on Evaluation and Assessment in Software Engineering*.

3. Rethlefsen, M. L., et al. (2021). PRISMA-S: An extension to the PRISMA Statement for Reporting Literature Searches in Systematic Reviews. *Systematic Reviews, 10*, 39. https://doi.org/10.1186/s13643-020-01542-z

4. Haddaway, N. R., et al. (2018). ROSES for systematic review reports. *Environmental Evidence*. The ROSES reporting resources will be consulted as supplementary guidance.

---

# 18. Final Research Position

This study will investigate how computer vision and vision-language approaches are being used to support visual quality assurance in video games.

Its primary purpose is to map the research landscape rather than compare the performance of individual algorithms.

The study will connect research from software engineering, computer vision, artificial intelligence, and game development through a unified classification framework.

The final novelty claim will be established only after a systematic comparison with existing reviews and surveys.

The study will prioritize transparent methodology, reproducibility, comprehensive search coverage, and evidence-based research recommendations.

**End of Protocol.**
