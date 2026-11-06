# Declarative Verification Experiments

## E01: VLM Static vs. Temporal NIAH Benchmark
* **Verifies:** Claim [C01](claims.md#c01-static-vlm-triage-vs-temporal-needle-in-a-haystack-collapse).
* **Setup:** Ingest benchmark datasets comprising static standalone screenshots ($N = 1,000$ from 507 games) and continuous 50-second gameplay video streams ($N = 100$ clips at 1 FPS downsampling). Evaluate across 16 VLM backbones (GPT-4.1, GPT-4o, o3, Gemini 2.5 Pro, Sonnet-3.7, Qwen-2.5-VL-72B, Llama-4).
* **Procedure:**
  1. For image tasks (IGD), supply single frame $I$ with structured JSON template requesting `glitch_detected: bool` and `reasoning: str`.
  2. For video tasks (NIAH), supply the 50-frame sequence with prompt requesting `glitch_detected: bool`, `frame_number: int`, and `reasoning: str`.
  3. Validate JSON formatting; compute binary accuracy for IGD and joint detection + temporal localization accuracy for NIAH.
* **Metrics:** Accuracy (%), Precision, Recall, Temporal Localization Error $|\hat{f} - f^*|$.
* **Expected Outcome (Directional):** All top proprietary models exceed 75% accuracy on static IGD, while collapsing below 20% on temporal NIAH (with models predicting $\hat{f}$ nearly at random across the 50 frames).
* **Baselines:** Uniform random guessing (2% accuracy on NIAH), middle-frame heuristic.
* **Dependencies:** None.

---

## E02: Reference Frame Selection Policy Evaluation
* **Verifies:** Claim [C02](claims.md#c02-reference-guided-lastcleanframe-performance-recovery).
* **Setup:** Evaluated on *RefGlitch-Bench* (1,000 synthetic paired frames across 5 glitch types in Godot TPS) and real-world gameplay video benchmarks (1,000 frames from PhysGame & VideoGameQA-Bench). Backbones: Qwen3-VL-8B, GPT-5, Gemini 3 Flash.
* **Procedure:**
  1. Extract I-frame keyframes using FFmpeg from video streams.
  2. Implement sequential prompting loop maintaining a reference pool $\mathcal{P} = \{ (I_k, \hat{y}_k) \}_{k < t}$.
  3. Test 5 reference policies: `NoRef` (single frame baseline), `PreviousFrame` ($I_{t-1}$), `MostSimilarFrame` (highest CLIP cosine similarity in pool), `LastCleanFrame` (most recent frame where $\hat{y} = 0$), and `OracleRef` (human-verified clean frame).
  4. Compare $(R_t, I_t)$ with conditioned prompt; compute frame-level predictions.
* **Metrics:** Accuracy, F1-score, Precision, Recall, False Positive Rate (FPR).
* **Expected Outcome (Directional):** `LastCleanFrame` consistently outperforms `NoRef`, `PreviousFrame`, and `MostSimilarFrame` across all models. `PreviousFrame` improves recall but degrades precision when the preceding frame is also glitched.
* **Baselines:** `NoRef` unguided single-frame prompt.
* **Dependencies:** E01.

---

## E03: Multimodal Engine-Telemetry Ablation
* **Verifies:** Claim [C03](claims.md#c03-engine-state-telemetry-fusion-eliminates-stylistic-false-alarms).
* **Setup:** Evaluated on *StateGlitch-3D* across 3 commercial-grade Unreal Engine 5 projects. Dataset contains 45,000 frames featuring both standard geometry glitches (mesh penetration, floating assets) and challenging stylistic effects (volumetric fog, particle sparks, dynamic translucency).
* **Procedure:**
  1. Extract synchronized RGB buffers, metric depth buffers ($\mathbf{D}$), surface normal buffers ($\mathbf{N}$), and collision query results ($\mathbf{C}$).
  2. Train baseline CNN/ViT on pure RGB frames.
  3. Train multimodal fusion architecture combining RGB with depth channels and spatial normal embeddings.
  4. Evaluate false positive rates specifically on non-glitched frames containing heavy stylistic particle/fog effects.
* **Metrics:** False Positive Rate (FPR), Precision, AUROC, False Discovery Rate (FDR).
* **Expected Outcome (Directional):** Multimodal telemetry fusion reduces false positive detections on artistic scenes by $\ge 40\%$ relative to pure RGB detectors, achieving near-perfect separation between mesh penetration and translucent particle overlapping.
* **Baselines:** ResNet-50 RGB-only, ViT-Base RGB-only.
* **Dependencies:** None.

---

## E04: Cross-Game Domain Transfer Benchmark
* **Verifies:** Claim [C04](claims.md#c04-cross-game-art-style-domain-degradation).
* **Setup:** Train object detection and glitch localization models on source game $\mathcal{D}_S$ (*GiantMap* - realistic park environment in Unreal Engine 5). Test on target titles $\mathcal{D}_T$: *HighRise* (indoor sci-fi shooter), *CombatGame* (AAA military combat), and stylized indie titles.
* **Procedure:**
  1. Measure in-distribution detection mAP on held-out test frames of $\mathcal{D}_S$.
  2. Deploy trained model zero-shot on $\mathcal{D}_T$ without updating weights; record cross-domain mAP.
  3. Apply co-finetuning with varying levels of unlabeled stream data and co-domain supervised batches.
* **Metrics:** mean Average Precision (mAP@0.5:0.95), cross-domain retention ratio $\Delta_{\text{OOD}}$, Class-wise Recall.
* **Expected Outcome (Directional):** Zero-shot transfer causes $\ge 35\%$ degradation in mAP; models fail to localize bounding boxes around clipping limbs when character clothing shaders and lighting diverge significantly from training assets.
* **Baselines:** Faster R-CNN with ResNet-50, ViT-Base supervised fine-tuning.
* **Dependencies:** E01, E03.

---

## E05: Weak Supervision Label Efficiency
* **Verifies:** Claim [C05](claims.md#c05-negative-space-weak-supervision-achieves-extreme-label-efficiency).
* **Setup:** Egocentric 3D gameplay dataset (*GiantMap-4* and *GM50* in Unreal Engine). Training set restricted to low-data regimes: $N = 15$ samples (GM4-Tiny) and $N = 156$ samples (GM4-Base); evaluated on a low-prevalence (0.007) video deployment stream with 46 out-of-distribution objects.
* **Procedure:**
  1. Extract masks from unlabeled gameplay using Segment Anything Model (SAM) guided by geometric prompts excluding the lower-right weapon region.
  2. Filter and cluster mask embeddings using CLIP + Hierarchical Agglomerative Clustering (HAC, $k=50$) to rebalance the distribution.
  3. Synthesize augmented pairs: paste source masks *over* weapon masks in 5 human-annotated target frames (positives) and *behind* weapon masks (negatives).
  4. Fine-tune ViT-Base backbones (supervised, DINOv1, CLIP) with a weapon-crop spatial prior.
* **Metrics:** Balanced Accuracy (%), F1-Score in low-prevalence stream, Area Under Precision-Recall Curve (AUPRC).
* **Expected Outcome (Directional):** ViT-Base pretrained on DINOv1 achieves $>95\%$ balanced test accuracy using only 15 training frames, dramatically outperforming ResNet-18/50 baselines.
* **Baselines:** Fully supervised ResNet-50 trained from scratch, full-frame uncropped ViT.
* **Dependencies:** None.
