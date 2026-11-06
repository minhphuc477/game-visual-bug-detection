# Literature Repository & Evidence Database

This directory manages all systematic mapping data, extracted evidence matrices, and bibliography files for the research project:
**"AI-Based Visual Bug Detection in Video Games: A Systematic Mapping Study"**

---

## Directory Structure
- `evidence_table.csv`: Structured master database recording bibliographic metadata, models, glitch types, benchmark datasets, cross-game capability, and quality scores for all screened primary papers.
- `papers.bib`: Master BibTeX citations for LaTeX drafting and reference management.
- `taxonomy.md`: Detailed visual glitch taxonomy (Geometry, Textures, Rendering/Lighting, Physics/Animation, UI/HUD).
- `review_matrices/`: Focused breakdown files mapping primary studies against research questions (RQ1 to RQ5).

---

## Literature Tracking Fields in `evidence_table.csv`

| Column | Description |
|---|---|
| `paper_id` | Unique identifier (e.g. `P01`, `P02`) |
| `year` | Year of publication (2020–2026) |
| `title` | Full title of the paper |
| `authors` | Authors list or first author et al. |
| `venue` | Conference, journal, or preprint repository |
| `venue_type` | `Conference`, `Journal`, or `Preprint` |
| `open_access` | `Yes` / `No` / `Accepted Manuscript` |
| `doi_url` | Direct DOI link or open access URL |
| `bug_categories_targeted` | Codes from `data/visual_bug_taxonomy.json` (e.g. `GEO-01`, `TEX-01`) |
| `model_family` | Model class (e.g., VLM, Anomaly Detection, Hybrid CNN+Engine, Classic CV) |
| `dataset_name` | Public or proprietary benchmark name |
| `num_games` | Number of distinct video game titles tested |
| `cross_game_evaluated` | `Yes`, `Partial`, or `No` |
| `qa_score` | Quality assessment score out of 10.0 (based on `protocol/quality_assessment_checklist.md`) |
| `key_findings` | Empirical conclusions and contributions |
| `primary_limitations` | Gaps, computational bottlenecks, or failure modes identified |

---

## How to Add New Papers
1. Place downloaded PDF in `papers/<category>/` using standard naming: `Author_Year_Title.pdf`.
2. Run MarkItDown ingestion:
   ```bash
   uv run scripts/convert_papers.py
   ```
3. Append study details and coding into `literature/evidence_table.csv`.
4. Append BibTeX entry into `literature/papers.bib`.
