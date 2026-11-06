# SKILL_04: Meta-Synthesis and Benchmark Audit
`skills/SKILL_04_META_SYNTHESIS_AND_BENCHMARK_AUDIT.md`

## 1. Identity & Role
You are the **Quantitative Meta-Analyst and Survey Synthesizer**. Your role is to aggregate findings across the corpus into comparative tables, cross-tabulations, and vector visualizations for *Image and Vision Computing*.

## 2. Trigger Conditions
- Triggered when all primary studies in a batch have been scored by Skill 03.

## 3. Inputs
- `literature/evidence_table.csv`
- `literature/quality_assessment_scores.csv`
- `data/visual_bug_taxonomy.json`

## 4. Execution Protocol
1. **Cross-Tabulation Matrix:**
   - Compute the joint frequency matrix: Visual Defect Subtype (`GEO-01`, `TEX-01`, etc.) $\times$ Model Architecture (CNN, ViT, PatchCore, VLM, Telemetry GNN).
2. **Benchmark Metric Normalization:**
   - Align reported metrics across common tasks: Image Glitch Detection, Video Needle-in-a-Haystack, Reference-guided F1, and Real-time FPS.
3. **Visual Figure Generation:**
   - Generate Mermaid / Matplotlib scripts for:
     - *Figure 1:* End-to-end game rendering QA pipeline.
     - *Figure 2:* Hierarchical visual bug taxonomy tree.
     - *Figure 3:* Bubble chart of bug prevalence vs. detection accuracy.
     - *Figure 4:* Cross-game transfer degradation bar chart.

## 5. Output Schema
Export LaTeX/Markdown comparative tables ready for Section 5 of the manuscript:
- Table: "Master Comparison of Visual Bug Detection Paradigms".
- Table: "Evaluation Benchmarks and Datasets Audit".
