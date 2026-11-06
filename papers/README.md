# Raw Academic Papers Library

Store raw research PDF files in the structured subdirectories below. When naming PDF files, please use the standardized naming convention:
```text
<FirstAuthor>_<Year>_<ShortTitle>.pdf
```
*Example:* `Macklon_2025_VideoGameQA_Bench.pdf`

---

## Folder Organization

1. `01_reviews/`: Prior surveys on video game testing, automated quality assurance, and software engineering in gaming.
2. `02_glitch_and_anomaly_detection/`: Primary technical papers applying computer vision, anomaly detection (Autoencoders, PatchCore), and CNNs for bug detection.
3. `03_vlms_and_multimodal/`: Vision-Language Models (GPT-4V, Gemini, Qwen-VL, LLaVA) applied to visual bug reporting and multimodal game QA.
4. `04_benchmarks_and_datasets/`: Benchmark papers introducing annotated gameplay datasets, synthetic rendering datasets, or visual regression baselines.
5. `05_gameplay_video_analysis/`: Papers focusing on temporal video sequences, dynamic gameplay stream inspection, and multi-frame glitch tracking.

---

## Automated Ingestion to Markdown
To convert all newly added PDFs into Markdown using Microsoft MarkItDown:
```bash
uv run scripts/convert_papers.py
```
The converted Markdown documents will automatically appear in `markdown/` and be indexed in `markdown/INDEX.md`.
