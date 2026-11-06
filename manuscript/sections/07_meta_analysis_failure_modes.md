# Section 7: Empirical Meta-Analysis, Cross-Game Generalisation & Failure Modes

## 7.1 Quantitative Meta-Analysis of Evaluated Systems
Synthesizing experimental findings across the 45 primary studies reveals clear operational divisions in performance, input modalities, and detection throughput.

![Figure 5: Empirical Modality Breakdown and Cross-Game Generalisation Verification](figures/figure5_cross_game_modalities.png)

### 7.1.1 Input Modality Distribution (Figure 5A)
- **Single Static Frame (RGB Only): 51.1% (n = 23).** Over half of the published literature operates strictly on isolated screenshots. While computationally expedient, static analysis remains fundamentally blind to temporal defects.
- **Spatio-Temporal Video Streams: 31.1% (n = 14).** Processing multi-frame buffers (sliding windows of 8 to 32 frames) to capture dynamic animation physics and rendering oscillations.
- **Multimodal Engine Telemetry Fusion: 17.8% (n = 8).** Synchronizing screen-space pixels with internal engine buffers (depth maps, surface normals, collision bounding boxes).

### 7.1.2 Operational Inference Latency & The Pareto Frontier (RQ4)
Operational throughput dictates where an AI detector can be deployed in the game production lifecycle:
1. **Real-Time Inline Assertion (45–60 FPS):** Lightweight supervised detectors (e.g., ShuffleNetV2, YOLOv8-Nano) achieve inference times of $8\text{--}16.6\text{ ms}$, operating directly within continuous integration (CI) automated playtests without throttling game engine execution.
2. **Near-Real-Time Playtest Inspection (15–25 FPS):** Patch-based anomaly detectors (PatchCore, FastFlow) and multi-modal state-aware fusion engines require $35\text{--}95\text{ ms}$ per frame, viable for dedicated headless QA server clusters.
3. **Asynchronous Post-Session Video Triage (<1 FPS):** Frontier multimodal Vision-Language Models (GPT-4o, Gemini 1.5 Pro, Claude 3.5 Sonnet) require **$1.8\text{ to }4.5\text{ seconds per frame/window}$**. This high latency prevents live deployment, restricting VLMs to asynchronous batch processing of recorded playtest sessions.

To visualize these critical engineering trade-offs, Figure 9 plots the **Operational Latency vs. Detection Accuracy Pareto Frontier** across all primary algorithmic paradigms:

![Figure 9: Operational Latency vs. Detection Accuracy Pareto Frontier](figures/figure9_latency_pareto_frontier.png)

The empirical Pareto envelope illustrates that high-speed inline assertions (Zone 1: $\le 16.6$ ms, $\ge 60$ FPS) achieve high accuracy on specialized structural domains (e.g., Macklon et al.'s 95% on 2D HTML5 canvas ASTs, Ling et al.'s 86.8% accuracy with ShuffleNetV2). In Zone 2 ($16.6$--$150$ ms), Kovacs et al.'s G-buffer fusion achieves a benchmark-leading 91.2% precision by synchronizing geometry telemetry, and Rifaat et al.'s ResNet18-BiLSTM achieves an 85.8% micro F1 score on multi-label video clips at 52 ms latency. In Zone 3 ($>1.0$ s), foundation VLMs provide open-ended natural-language bug reporting and pairwise reference diffing (Yu et al., F1: 0.69 at 1,850 ms; Taesiri et al., 78.2% coarse accuracy at 3,200 ms), but incur a $100\times$ to $300\times$ latency penalty that confines them to asynchronous offline triage.

---

## 7.2 The Cross-Game Domain Shift Penalty (RQ5)
A critical evaluation dimension audited in this mapping study is **cross-game generalisation**—the ability of an algorithm trained on Game $A$ to detect visual defects in Game $B$ without exhaustive title-specific fine-tuning.

As shown in **Figure 5B**:
- **55.6% (n = 25)** of primary studies evaluated their methods across multiple game environments.
- **37.8% (n = 17)** evaluated exclusively within a single game title or closed asset repository.
- **6.7% (n = 3)** evaluated across games sharing identical rendering engines and art styles (partial transfer).

Where cross-game domain transfer was quantitatively reported, models exhibited sharp performance penalties:
1. **Convolutional Overfitting to Background Textures:** Davarmanesh et al. [35] and Yi et al. [7] demonstrated that standard supervised object detectors (Faster R-CNN, YOLO) suffer a **$32\%\text{ to }46\%$ drop in mean Average Precision (mAP)** when evaluated on unseen game environments. The convolutional kernels learn to correlate defect presence with specific level background textures rather than learning intrinsic geometric defect properties.
2. **Artistic Style Shift Degradation:** Transferring models trained on photorealistic 3D engines (e.g., Unreal Engine 5 Nanite/Lumen) to stylized environments (cel-shaded, hand-painted, or low-poly voxel titles) triggered severe false alarm cascades. Zero-shot foundation VLMs exhibited a **$+28\%$ spike in false positives**, misinterpreting black cel-shaded character outlines and non-photorealistic lighting ramps as polygon clipping and shadow acne [1, 17].
3. **Reference Guidance as a Domain Transfer Anchor:** Yu et al. [6] (*RefGlitch-Bench*) proved that pairwise reference guidance effectively neutralizes style shift. By supplying the model with a same-game baseline frame ($R_t$), the VLM's cross-game F1 score recovered from $0.42$ to $0.69$, proving that reference conditioning allows models to separate artistic style from structural defects.

---

## 7.3 Forensic Diagnostic of Core Algorithmic Failure Modes

By cross-referencing qualitative failure cases and empirical error logs across the 45 primary studies, we diagnose four systemic algorithmic failure modes. Figure 8 provides a comprehensive **Forensic Visual Autopsy** illustrating the failure mechanisms across four distinct visual diagnostic panels:

![Figure 8: Forensic Visual Autopsy of Four Systemic Algorithmic Failure Modes](figures/figure8_failure_mode_autopsy.png)

### 1. Panel A: Spatial Blindness of Foundation VLMs on Micro-Clipping
Modern Vision-Language Models tokenize input images via coarse patch projection (e.g., $14 \times 14$ or $16 \times 16$ pixel patches in ViT backbones). In video games, severe geometric clipping frequently occupies sub-pixel or narrow screen regions—such as a character's sword hilt penetrating hand armor, or a shoe sole sinking 2 inches into stone pavement (`GEO-01`). As visualized in Figure 8A, when a sub-pixel polygonal interpenetration falls within a single coarse ViT patch, spatial self-attention layers smooth out localized high-frequency boundary gradients against the surrounding nominal environment pixels. Consequently, the local anomaly is completely diluted into the dominant background token embedding, resulting in **false negative rates exceeding 70%** on subtle clipping (Taesiri et al., 2025; Lu et al., 2026).

### 2. Panel B: Catastrophic Temporal Needle-in-a-Haystack (NIAH) Collapse
When evaluated on isolated, cherry-picked static screenshots, frontier VLMs achieve respectable bug detection accuracy ($\sim 78\%\text{--}82\%$). However, when deployed on long-horizon continuous gameplay videos (5 to 30 minutes of 60 FPS recording, totaling 18,000 to 108,000 frames), performance collapses catastrophically. As shown in Figure 8B, in temporal Needle-in-a-Haystack (NIAH) evaluations—where the model must identify the exact onset and termination of a transient 1-second animation glitch (e.g., a T-pose snap or z-fighting flicker) within continuous footage—**VLM localization accuracy collapsed to $1\%\text{ to }19\%$** (Zheng et al., 2026; Muller et al., 2026). Standard uniform frame subsampling (e.g., 1 FPS) frequently skips the transient glitch window entirely, while temporal self-attention across video frames suffers severe weight dilution over long sequences of nominal gameplay.

### 3. Panel C: Context Poisoning in Sequential Reference Pools
In reference-guided frameworks, maintaining an uncorrupted reference buffer $\mathcal{R}_{\text{clean}}$ is vital. Yu et al. (*RefGlitch-Bench*, 2026) discovered that if an undetected visual defect accidentally leaks into the clean reference pool (Figure 8C)—such as a prop that failed to stream its high-resolution texture or a character whose foot remains clipped into terrain—the reference baseline itself becomes compromised. When subsequent test frames exhibiting the identical persistent defect are evaluated against the poisoned reference $R_{\text{poisoned}}$, the calculated visual anomaly delta $\Delta(I_t, R_{\text{poisoned}}) \approx 0$ with high cosine similarity ($\ge 0.95$). This context poisoning triggers **false negative suppression rates exceeding $80\%$**, permanently masking persistent streaming and level-geometry bugs from the QA pipeline.

### 4. Panel D: Multimodal RAG Confirmation Bias via CLIP Image Embeddings
To assist VLMs in evaluating novel game environments without manual reference pairing, Lu et al. (2026) integrated Retrieval-Augmented Generation (RAG) by retrieving top-$k$ visually similar frames using standard CLIP embeddings. Surprisingly, **image RAG degraded detection precision from $0.50$ to $0.37$** (+26% false positive spike). As depicted in Figure 8D, global CLIP visual representations are overwhelmingly dominated by macro-scale environmental background semantics (e.g., broad desert sand dunes, sky lighting gradients, distant mountain foliage) rather than localized geometric defect tokens. Consequently, the retrieval pipeline fetches clean environmental frames captured from irrelevantly rotated viewpoints, misleading the downstream VLM into flagging viewpoint discrepancies as visual rendering defects.
