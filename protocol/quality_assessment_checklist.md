# Quality Assessment Checklist for Primary Studies

Adapted from Dybå & Dingsøyr (2008) and Kitchenham et al. for empirical evaluations of machine learning in software engineering and game quality assurance.

Scoring:
- **Yes (1.0)**: Criterion is explicitly and thoroughly addressed.
- **Partially (0.5)**: Criterion is mentioned or partially satisfied, but lacks full experimental rigour or details.
- **No (0.0)**: Criterion is not addressed or completely absent.

---

## Evaluation Criteria

| ID | Quality Question | Target Dimension |
|---|---|---|
| **QA1** | Are the research aims, visual bug targets, and context clearly stated? | Study Rigour |
| **QA2** | Is the proposed computer vision / deep learning architecture described in adequate technical detail for replication? | Reproducibility |
| **QA3** | Is the dataset described clearly (number of games, total frames, resolution, capture setup, balance of clean vs. buggy states)? | Dataset Validity |
| **QA4** | Are the ground-truth annotations and labelling processes clearly defined and verified (e.g., inter-rater reliability, automated synthetic injection)? | Ground Truth Integrity |
| **QA5** | Are baselines or standard benchmark models included for comparison (e.g., standard object detectors, classic anomaly detectors, off-the-shelf VLMs)? | Comparative Rigour |
| **QA6** | Are standard evaluation metrics reported (Precision, Recall, F1, AUROC, False Positive Rate)? | Metric Validity |
| **QA7** | Did the study evaluate cross-game generalization (testing on games or assets not seen during model training)? | Generalisability |
| **QA8** | Did the authors report computational complexity, inference time, or frame-rate (FPS) constraints for real-time QA? | Practical Viability |
| **QA9** | Are limitations, failure cases, and false positives critically analyzed and discussed? | Critical Appraisal |
| **QA10** | Are code, models, or datasets publicly accessible for research verification? | Open Science |

---

## Quality Threshold
- **High Quality (QA Score >= 7.5)**: Included in deep comparative synthesis and quantitative benchmark mapping.
- **Moderate Quality (5.0 <= QA Score < 7.5)**: Included in general taxonomy mapping and qualitative discussion.
- **Low Quality (QA Score < 5.0)**: Excluded from main synthesis; retained only as contextual or preliminary grey literature if unique insights exist.
