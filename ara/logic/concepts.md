# Formal Concepts and Definitions

## Concept 1: Video Game Visual Defect (VGVD)
* **Notation:** $D = \langle \tau, \mathbf{b}, t_{\text{start}}, t_{\text{end}}, s \rangle$
* **Definition:** A player-visible graphical aberration occurring in the rendered output buffer of a video game engine that violates either physical plausibility, intended asset design, rendering pipeline integrity, or user interface legibility. Here $\tau \in \mathcal{T}$ represents the defect taxonomy category, $\mathbf{b} \in \mathbb{R}^4$ is the normalized spatial bounding box $[x_{\min}, y_{\min}, x_{\max}, y_{\max}]$, $[t_{\text{start}}, t_{\text{end}}]$ denotes the temporal interval of manifestation, and $s \in [0, 1]$ represents the perceived severity.
* **Boundary Conditions:** Pure game-logic errors (such as an incorrect mathematical score calculation in the background) that do not alter the rendered pixels in the camera viewport are excluded. Transient sub-pixel rasterization antialiasing fluctuations are excluded unless perceptible to human visual contrast filters.
* **Related Concepts:** `VGVD-Taxonomy`, `Rendering Artifact`, `G-Buffer`.

---

## Concept 2: LastCleanFrame Reference Oracle
* **Notation:** $R_t = \arg\max_{k < t} \{ k \mid \hat{y}_k = 0 \land \text{Sim}(I_k, I_t) \ge \theta_{\text{scene}} \}$
* **Definition:** A verified or high-confidence glitch-free video keyframe sampled from an earlier point in the identical gameplay video stream, displaying the same local scene geometry, lighting environment, and camera perspective as the test frame $I_t$.
* **Boundary Conditions:** If the gameplay camera transitions across an instantaneous cutscene cut or level teleportation boundary where $\text{Sim}(I_{t-1}, I_t) < \theta_{\text{scene}}$, the reference pool resets to empty ($R_t = \emptyset$) to prevent misleading cross-scene comparisons.
* **Related Concepts:** `Reference-Guided Sequential Prompting`, `Temporal Drift`, `Scene Cut`.

---

## Concept 3: Temporal Needle-in-a-Haystack (NIAH)
* **Notation:** $\text{NIAH}(V) \to \langle \hat{y}, \hat{f}_{\text{glitch}} \rangle$
* **Definition:** A long-context video evaluation task in which a model ingests an extended sequence of gameplay video frames $V = (I_1, I_2, \dots, I_T)$ containing predominantly normal gameplay frames ("haystack"), and must output both a binary detection decision $\hat{y} \in \{0, 1\}$ and the exact frame index $\hat{f}_{\text{glitch}} \in [1, T]$ where an injected or natural visual glitch first manifests ("needle").
* **Boundary Conditions:** The evaluation requires temporal localization precision; predicting $\hat{y} = 1$ without identifying the correct timestamp window $|\hat{f} - f^*| \le \delta$ is penalized as a localization failure.
* **Related Concepts:** `Video Transformer`, `Frame Sampling Rate`, `Sliding Window`.

---

## Concept 4: Multimodal Engine-State Fusion
* **Notation:** $\Phi(I_t, \mathbf{G}_t) = \mathbf{z}_t \in \mathbb{R}^d$ where $\mathbf{G}_t = \{ \mathbf{D}_t, \mathbf{N}_t, \mathbf{C}_t, \mathbf{M}_t \}$
* **Definition:** A neural representation combining the rendered three-channel RGB color frame $I_t \in \mathbb{R}^{H \times W \times 3}$ with internal game engine G-buffer geometry representations, where $\mathbf{D}_t$ is the metric depth buffer, $\mathbf{N}_t$ is the screen-space surface normal tensor, $\mathbf{C}_t$ is the collision hull mesh projection, and $\mathbf{M}_t$ represents camera transform matrices.
* **Boundary Conditions:** Requires engine-instrumentation hooks or native graphics API interception (DirectX, Vulkan, RenderDoc); cannot be extracted from post-compression H.264/HEVC video streams.
* **Related Concepts:** `Black-Box Testing`, `G-Buffer`, `False Positive Discovery Rate`.

---

## Concept 5: Negative-Space Domain-Prior Augmentation
* **Notation:** $I_{\text{aug}} = M_{\text{anchor}} \odot I_{\text{target}} + (1 - M_{\text{anchor}}) \odot \mathcal{A}(M_{\text{source}}, I_{\text{source}})$
* **Definition:** A data synthesis technique for visual defects in first-person viewports where invariant foreground occlusion regions (e.g., character arms or weapons identified by mask $M_{\text{anchor}}$) serve as a spatial oracle: pasting segmented scene objects over $M_{\text{anchor}}$ generates synthetic positive penetration instances ("pseudo-clipping"), while pasting beneath $M_{\text{anchor}}$ generates negative clean samples.
* **Boundary Conditions:** Relies on the spatial permanence of the egocentric viewpoint invariant; inapplicable to dynamic third-person free-floating cinematic cameras.
* **Related Concepts:** `Weak Supervision`, `Segment Anything Model (SAM)`, `First-Person Player Clipping (FPPC)`.

---

## Concept 6: Cross-Game Generalisation Penalty
* **Notation:** $\Delta_{\text{OOD}} = \frac{\text{mAP}_{\text{ID}} - \text{mAP}_{\text{OOD}}}{\text{mAP}_{\text{ID}}} \times 100\%$
* **Definition:** The percentage reduction in detection performance when an object detection or glitch segmentation model trained on game distribution $\mathcal{D}_{\text{source}}$ is evaluated without parameter adaptation on an out-of-distribution game $\mathcal{D}_{\text{target}}$ featuring distinct shaders, polygon density, lighting models, and artistic stylization.
* **Boundary Conditions:** Assesses zero-shot or frozen backbone performance; fine-tuning or domain-adversarial retraining on $\mathcal{D}_{\text{target}}$ transitions the evaluation to transfer learning.
* **Related Concepts:** `Domain Adaptation`, `Co-Finetuning`, `Style Shift`.
