# Related Work: Typed Dependency Graph

```
[Taesiri 2025 (NeurIPS)] <---extends--- [Yu 2026 (RefGlitch)]
         ^                                    ^
         | imports                            | bounds
         |                                    |
[Lu 2026 (FSE EA)]                     [Muller 2026 (TempGlitch)]
         ^                                    ^
         | refutes (Image RAG)                | extends
         |                                    |
[Rahman 2023 (BMVC)] <---bounds--- [Kovacs 2026 (ESWA)]
```

---

## RW01: VideoGameQA-Bench (Taesiri et al., NeurIPS 2025)
* **DOI/URL:** `https://arxiv.org/abs/2505.15952`
* **Type:** `baseline` / `imports`
* **Delta:** Establishes the first standardized 9-task multimodal game QA benchmark across >800 games; defines the temporal Needle-in-a-Haystack (NIAH) and parametric clipping detection protocols.
* **Claims Affected:** [C01](../logic/claims.md#c01-static-vlm-triage-vs-temporal-needle-in-a-haystack-collapse).

---

## RW02: RefGlitch-Bench (Yu et al., 2026)
* **DOI/URL:** `https://arxiv.org/abs/2604.11082`
* **Type:** `extends` / `bounds`
* **Delta:** Resolves the ambiguity of unguided single-frame bug detection on stylized art by formulating reference-guided sequential prompting and evaluating the `LastCleanFrame` policy against oracle reference bounds.
* **Claims Affected:** [C02](../logic/claims.md#c02-reference-guided-lastcleanframe-performance-recovery).

---

## RW03: Industrial VLM Gameplay Study (Lu et al., ACM/IEEE FSE 2026)
* **DOI/URL:** `https://arxiv.org/abs/2603.22706`
* **Type:** `extends` / `refutes`
* **Delta:** Evaluates production triage on 41 hours / 19,738 keyframes at Electronic Arts; proves that Image RAG degrades precision (0.50 $\rightarrow$ 0.37) while VLM-as-a-judge (`gpt-5-mini` as critic) improves precision to 0.55.
* **Claims Affected:** [C01](../logic/claims.md#c01-static-vlm-triage-vs-temporal-needle-in-a-haystack-collapse), [C02](../logic/claims.md#c02-reference-guided-lastcleanframe-performance-recovery).

---

## RW04: Weak Supervision on Xbox QuAIL (Rahman, BMVC 2023)
* **DOI/URL:** `https://arxiv.org/abs/2309.11077`
* **Type:** `extends`
* **Delta:** Solves extreme defect scarcity (<0.01 prevalence) by combining zero-shot SAM segmentation with canonical egocentric viewport priors, achieving 95.2% accuracy on clipping from 15 samples.
* **Claims Affected:** [C05](../logic/claims.md#c05-negative-space-weak-supervision-achieves-extreme-label-efficiency).

---

## RW05: State-Aware Glitch Net (Kovacs et al., ESWA 2026)
* **DOI/URL:** `https://doi.org/10.1016/j.eswa.2025.124500`
* **Type:** `bounds` / `extends`
* **Delta:** Fuses RGB screen pixels with engine depth buffers, surface normals, and collision hulls, eliminating 42% of false positives caused by stylistic weather and particle effects.
* **Claims Affected:** [C03](../logic/claims.md#c03-engine-state-telemetry-fusion-eliminates-stylistic-false-alarms).

---

## RW06: Hybrid Co-Finetuning (Yi et al., AAAI AIIDE 2025)
* **DOI/URL:** `https://arxiv.org/abs/2510.03591`
* **Type:** `extends`
* **Delta:** Introduces multi-title co-supervised detection combined with latent masked autoencoder distillation (I-JEPA inspired) to mitigate cross-game domain transfer drop.
* **Claims Affected:** [C04](../logic/claims.md#c04-cross-game-art-style-domain-degradation).

---

## RW07: TempGlitch Spatio-Temporal Video Anomaly (Muller et al., 2026)
* **DOI/URL:** `https://arxiv.org/abs/2605.21443`
* **Type:** `extends`
* **Delta:** Demonstrates that single-frame static detectors miss >65% of animation and rendering glitches; proposes 16-frame sliding temporal window Video Transformers.
* **Claims Affected:** [C01](../logic/claims.md#c01-static-vlm-triage-vs-temporal-needle-in-a-haystack-collapse).
