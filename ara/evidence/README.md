# Grounded Evidence Index

This directory archives empirical result tables extracted directly from the primary benchmarked studies. All numerical entries reproduce the source publications' exact unrounded findings.

| Evidence File | Source Study | Venue & Year | Primary Metrics Captured | Mapped Claims |
|---|---|---|---|---|
| [`tables/table1_videogameqa_bench.md`](tables/table1_videogameqa_bench.md) | Taesiri et al. (*VideoGameQA-Bench*) | NeurIPS 2025 | Image Glitch Acc (82.8%), Video Glitch Acc (78.1%), NIAH Acc (1.0%–36.0%) | [C01](../logic/claims.md#c01-static-vlm-triage-vs-temporal-needle-in-a-haystack-collapse) |
| [`tables/table2_ea_vlm_ablation.md`](tables/table2_ea_vlm_ablation.md) | Lu et al. (Electronic Arts Case Study) | ACM/IEEE FSE 2026 | Baseline Precision (0.50), Judge Precision (0.55), Image RAG (0.37), Text RAG (0.57) | [C01](../logic/claims.md#c01-static-vlm-triage-vs-temporal-needle-in-a-haystack-collapse), [C02](../logic/claims.md#c02-reference-guided-lastcleanframe-performance-recovery) |
| [`tables/table3_refglitch_baselines.md`](tables/table3_refglitch_baselines.md) | Yu et al. (*RefGlitch-Bench*) | SIE / arXiv 2026 | NoRef F1 (0.42), LastCleanFrame F1 (0.69), PreviousFrame F1 (0.57), Oracle Ref F1 (0.74) | [C02](../logic/claims.md#c02-reference-guided-lastcleanframe-performance-recovery) |
| [`tables/table4_stateglitch_fusion.md`](tables/table4_stateglitch_fusion.md) | Kovacs et al. (*StateGlitch-3D*) | ESWA 2026 | False Positive Reduction (41.9%), Precision (91.2%), AUROC (93.5%) | [C03](../logic/claims.md#c03-engine-state-telemetry-fusion-eliminates-stylistic-false-alarms) |
| [`tables/table5_xbox_weak_supervision.md`](tables/table5_xbox_weak_supervision.md) | Rahman (*Weak Supervision / Xbox QuAIL*) | BMVC 2023 | 15-sample DINO ViT Acc (95.2%), 156-sample CLIP Acc (97.9%), SFT F1 (0.336 $\to$ 0.550) | [C05](../logic/claims.md#c05-negative-space-weak-supervision-achieves-extreme-label-efficiency) |
