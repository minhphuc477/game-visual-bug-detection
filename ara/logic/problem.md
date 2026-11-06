# Problem Definition: Visual Bug Detection in Video Games

## 1. Observations

- **O01 (Industrial QA Bottleneck):** In modern commercial game studios (AAA to AA), functional testing is rapidly automating via unit tests and headless bot scripts, yet **visual testing remains over 80% manual** (Svensson & Lindqvist, 2025). Human testers spend thousands of hours manually reviewing build footage for visual defects.
- **O02 (Underutilized Video Corpora):** Automated overnight soak testing generates hundreds of hours of gameplay video (e.g., 41 hours / 4.3 million frames per build at Electronic Arts), but less than 0.05% of this footage is ever reviewed unless a fatal engine crash occurs (Lu et al., FSE 2026).
- **O03 (Temporal Defect Invisibility):** Single-frame static anomaly detectors miss **over 65% of animation and rendering glitches** (e.g., T-pose freezes, ragdoll physics explosions, texture flickering, LOD popping) because individual frames appear plausible in isolation; the bug only manifests across temporal delta sequences (Muller et al., *TempGlitch* 2026).
- **O04 (Foundation Model Performance Cliff):** While state-of-the-art vision-language models (GPT-4o, Gemini 2.5 Pro) achieve up to 82.8% accuracy on static image glitch detection, their accuracy collapses to **10% to 19% on temporal Needle-in-a-Haystack (NIAH)** video localization tasks (Taesiri et al., *VideoGameQA-Bench* NeurIPS 2025).

---

## 2. Gaps in the Literature

- **G01 (The Cross-Game Generalisation Penalty):** Existing computer vision detectors overfit severely to specific game titles, rendering engines, and art styles. Transferring a model trained on photorealistic Unreal Engine 5 to stylized cel-shaded or voxel titles results in **>35% mAP drop** and massive false alarm rates (Yi et al., AIIDE 2025).
- **G02 (Temporal Inference Latency vs. 60 FPS CI Playtesting):** Heavy 3D-CNNs and Spatio-Temporal Video Transformers capture motion anomalies effectively but introduce 1.5s+ per-frame latency, making live real-time 60 FPS continuous integration (CI) playtesting computationally impossible without severe frame dropping.
- **G03 (The Black-Box Oracle Dilemma):** Pure RGB vision models struggle to distinguish intentional artistic styling (e.g., dense fog, surreal geometry, chromatic aberration) from true rendering errors. While engine-telemetry hooks (depth, collision bounding boxes) reduce false positives by 42%, they destroy black-box testing capability on compiled commercial release builds (Kovacs et al., 2026).
- **G04 (Lack of Standardized Multi-Game Reference Baselines):** Prior datasets lack paired clean/glitched references within the same viewpoint, forcing models to infer correctness from vague prior training distributions rather than explicit visual contrast (Yu et al., *RefGlitch-Bench* 2026).

---

## 3. Key Insights

1. **Temporal Reference Guidance:** Providing an explicit **LastCleanFrame** reference from earlier in the gameplay stream transforms open-ended visual anomaly detection into a localized contrastive verification problem, eliminating artistic ambiguity and raising F1 scores by up to +0.27.
2. **Weak Supervision via Negative-Space Domain Priors:** In 3D games, egocentric camera viewports feature invariant structural anchors (such as first-person player weapons or HUD zones). Leveraging promptable segmentation (SAM) to paste game semantics into these anchor zones synthesizes highly accurate pseudo-glitches from as few as 5 human-annotated exemplar frames.
3. **Decoupled Visual vs. Textual Anomaly Triage:** Off-the-shelf VLMs spend token bandwidth reading on-screen error logs (46.8% of flagged bugs at EA). Decoupling optical character recognition (OCR) from visual feature anomaly detection prevents prompt degradation and reduces inference compute costs.

---

## 4. Fundamental Assumptions

- **A01 (Visual Observability):** We focus exclusively on player-visible graphical defects that manifest in the rendered RGB framebuffer or camera viewport; non-visual game logic states that cause no visual discrepancy are out of scope.
- **A02 (Temporal Frame Order):** Automated playtesting streams are ingested in chronological temporal order ($t_1, t_2, \dots, t_T$), enabling caching and retrieval of historical reference states.
- **A03 (Downstream Engine Diversity):** A production visual testing pipeline must operate without requiring manual retraining of neural network weights from scratch whenever a game level or asset changes.
