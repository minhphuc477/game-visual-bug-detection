# Section 2: Formal Problem Definition & Mathematical Foundations

## 2.1 Video Game Rendering Pipeline and Defect Space
Modern real-time video games generate visual content through complex rendering pipelines operating at 30 to 120 frames per second (FPS). Let a continuous gameplay session be represented as an ordered sequence of discrete time steps $t \in \{1, 2, \dots, T\}$. At each time step $t$, the graphics subsystem transforms a dynamic 3D scene graph $\mathcal{G}_t = (\mathcal{V}_t, \mathcal{E}_t)$—comprising geometric vertex buffers, skeletal rigs, material shaders, physical colliders, and lighting parameters—into a rendered screen-space frame buffer:
\begin{equation}
I_t = \mathcal{R}(\mathcal{G}_t, \mathbf{C}_t, \mathbf{\Theta}_{\text{render}}) \in \mathbb{R}^{H \times W \times 3}
\end{equation}
where $\mathbf{C}_t \in SE(3)$ denotes the 6-DoF virtual camera pose (position $\mathbf{p} \in \mathbb{R}^3$ and orientation quaternion $\mathbf{q} \in \mathbb{H}$), $\mathbf{\Theta}_{\text{render}}$ encompasses the rasterization/ray-tracing pipeline configurations, and $H \times W$ represents the display resolution.

A **visual defect** (or graphical glitch) occurs when the projected image $I_t$ manifests visual artifacts that violate either physical realism, engine design constraints, or intended artistic specifications, formally defined as:
\begin{equation}
\mathcal{D}_t = \mathbb{I}\left( d_{\text{perceptual}}(I_t, I_t^*) > \tau_{\text{glitch}} \right)
\end{equation}
where $I_t^*$ is the latent, unobservable "ideal" clean rendering under identical game logic, $d_{\text{perceptual}}$ is a visual difference metric, and $\tau_{\text{glitch}}$ is an imperceptibility threshold. Because $I_t^*$ cannot be generated in real time without duplicating rendering overhead, automated visual QA must infer defect states directly from observable gameplay data.

---

## 2.2 Formulation 1: Single-Frame Visual Bug Detection and Localization
In its simplest formulation, visual quality assurance is framed as an image-level classification or object detection problem operating on an isolated gameplay screenshot $I \in \mathbb{R}^{H \times W \times 3}$.

### 2.2.1 Binary and Multi-Class Glitch Classification
A feature extractor $\phi_{\theta}: \mathbb{R}^{H \times W \times 3} \rightarrow \mathbb{R}^D$ maps the screenshot to a latent embedding, followed by a classification head:
\begin{equation}
\hat{y} = \sigma\left(\mathbf{w}^T \phi_{\theta}(I) + b\right) \in [0, 1]
\end{equation}
where $\hat{y} \ge 0.5$ signals the presence of a visual glitch. In multi-class settings, the output space expands to $\mathcal{Y} = \{c_1, c_2, \dots, c_K, \text{clean}\}$, categorizing the defect into specific taxonomy subtypes (e.g., missing textures, floating assets).

### 2.2.2 Spatial Defect Localization
For localized defects (e.g., mesh clipping, UI overlaps), the model outputs a set of bounding boxes $\mathcal{B} = \{(\mathbf{b}_k, c_k, s_k)\}_{k=1}^K$, where $\mathbf{b}_k = (x_k, y_k, w_k, h_k) \in [0, 1]^4$ parameterizes the bounding box coordinates, $c_k \in \mathcal{C}$ denotes the defect class, and $s_k \in [0, 1]$ represents detection confidence. The detection objective optimizes a multi-task loss combining cross-entropy classification and bounding box regression (e.g., Complete IoU loss):
\begin{equation}
\mathcal{L}_{\text{det}} = \mathcal{L}_{\text{cls}}(c_k, \hat{c}_k) + \lambda_{\text{box}} \mathcal{L}_{\text{CIoU}}(\mathbf{b}_k, \hat{\mathbf{b}}_k)
\end{equation}

### 2.2.3 Self-Supervised Anomaly Formulation (PatchCore / DINO)
To bypass the prohibitive cost of collecting exhaustive defect annotations, anomaly detection formulations learn exclusively from clean gameplay footage. Let $\mathcal{M}_{\text{clean}} = \{\mathbf{m}_j\}_{j=1}^M \subset \mathbb{R}^D$ be a coreset memory bank of locally aggregated patch features extracted from defect-free frames. For an evaluation frame $I$, the pixel-level anomaly score at coordinate $(u, v)$ is defined by the nearest-neighbor Euclidean distance to the memory bank:
\begin{equation}
\mathcal{A}(u, v) = \min_{\mathbf{m} \in \mathcal{M}_{\text{clean}}} \left\| \phi_{\theta}(p_{u,v}) - \mathbf{m} \right\|_2
\end{equation}
An image-level anomaly score is derived via greedy maximum pooling: $\mathcal{A}_{\text{frame}}(I) = \max_{u, v} \mathcal{A}(u, v)$.

---

## 2.3 Formulation 2: Reference-Guided Pairwise Visual Diffing
In complex virtual worlds, distinguishing intentional artistic stylization (e.g., translucent ghosts, cel-shaded outlines) from genuine rendering bugs is ill-posed in isolation. Reference-guided approaches condition the defect inference on a verified baseline frame $R_t \in \mathbb{R}^{H \times W \times 3}$ (e.g., the *Last Clean Frame* from the same camera trajectory or an authoritative asset render):
\begin{equation}
f_{\theta}: (R_t, I_t) \rightarrow \{0, 1\} \times \mathcal{B}_{\text{defect}}
\end{equation}

The reference difference representation is computed through cross-attention between test features $\mathbf{Z}_I = \phi_{\theta}(I_t)$ and reference features $\mathbf{Z}_R = \phi_{\theta}(R_t)$:
\begin{equation}
\mathbf{Z}_{\text{diff}} = \text{Softmax}\left(\frac{(\mathbf{Z}_I \mathbf{W}_Q)(\mathbf{Z}_R \mathbf{W}_K)^T}{\sqrt{d_k}}\right) (\mathbf{Z}_R \mathbf{W}_V) - \mathbf{Z}_I
\end{equation}
Conditioning on $R_t$ cancels static environmental clutter and isolates localized rendering discrepancies, boosting F1 scores by up to $+0.27$ over single-frame inference.

---

## 2.4 Formulation 3: Multimodal Engine-State Telemetry Fusion
Pure RGB vision suffers high false positive rates ($25\%-45\%$) when inspecting complex particle systems, dynamic lighting, and volumetric smoke. White-box testing overcomes this by fusing screen-space pixels with synchronized internal game-engine telemetry buffers:
\begin{equation}
\mathcal{T}_t = \{I_t^{\text{RGB}}, D_t, N_t, C_t, M_t\}
\end{equation}
where:
- $D_t \in \mathbb{R}^{H \times W}$ is the 32-bit floating-point linear depth buffer (Z-buffer).
- $N_t \in \mathbb{R}^{H \times W \times 3}$ represents the screen-space surface normal G-buffer.
- $C_t \in \mathbb{R}^{P \times 6}$ encodes 3D physics collision bounding volume query matrices (AABBs/OBBs).
- $M_t = \mathbf{P} \cdot \mathbf{V} \in \mathbb{R}^{4 \times 4}$ is the camera view-projection matrix.

The multimodal defect probability fuses visual embeddings $\phi_v(I_t^{\text{RGB}})$ with geometric telemetry embeddings $\phi_g(D_t, N_t, C_t)$ through cross-modal gating:
\begin{equation}
P(\text{defect} \mid \mathcal{T}_t) = \sigma\left( \mathbf{W}_{\text{fuse}} \left[ \phi_v(I_t^{\text{RGB}}) \odot \sigma(\mathbf{W}_g \phi_g(D_t, N_t, C_t)) \right] + b \right)
\end{equation}
By cross-referencing visual polygon intersections with physical collision queries, engine telemetry fusion eliminates $41.9\%$ of false alarms caused by non-colliding visual effects (e.g., foliage sway, particle embers).

---

## 2.5 Formulation 4: Spatio-Temporal Video Stream Attention
Over $65\%$ of gameplay defects—such as character foot-sliding, ragdoll constraint explosion, texture mipmap pop-in, and coplanar Z-fighting—are temporal frequencies that do not exist within an isolated static image.

Let a continuous gameplay stream buffer spanning a temporal window of $L$ frames at 60 FPS be defined as:
\begin{equation}
\mathcal{S}_t = \{I_{t - L + 1}, I_{t - L + 2}, \dots, I_t\} \in \mathbb{R}^{L \times H \times W \times 3}
\end{equation}
A spatio-temporal video transformer partitions the video tensor into 3D tubelet tokens $\mathbf{E} \in \mathbb{R}^{T' \times H' \times W' \times d}$. Temporal self-attention models cross-frame dynamics:
\begin{equation}
\mathbf{A}_{\text{temporal}} = \text{Softmax}\left(\frac{\mathbf{Q}_t \mathbf{K}_t^T}{\sqrt{d}} + \mathbf{B}_{\text{rel}}\right) \mathbf{V}_t
\end{equation}
where $\mathbf{B}_{\text{rel}} \in \mathbb{R}^{L \times L}$ encodes relative temporal positional bias. The model outputs temporal glitch intervals and defect classifications:
\begin{equation}
\hat{\mathcal{T}}_{\text{glitch}} = \left\{ (t_{\text{start}}^{(k)}, t_{\text{end}}^{(k)}, c_k, s_k) \right\}_{k=1}^K
\end{equation}
where $[t_{\text{start}}^{(k)}, t_{\text{end}}^{(k)}]$ denotes the precise temporal boundaries during which the glitch manifests in gameplay.

---

## 2.6 Operational Latency Constraints in Game Production
For automated visual quality assurance to be viable in continuous integration (CI) and automated playtest pipelines, detection algorithms must satisfy strict operational latency thresholds:
\begin{equation}
T_{\text{inference}} + T_{\text{capture}} \le \frac{1}{\text{Target FPS}}
\end{equation}
1. **Inline Real-Time Assertion (60 FPS):** Requires $T_{\text{inference}} \le 16.6\text{ ms}$, achievable only by lightweight convolutional detectors (e.g., YOLOv8-Nano) or optimized TensorRT engines.
2. **Near-Real-Time Automated Playtest Bots (15–30 FPS):** Requires $T_{\text{inference}} \le 33.3\text{--}66.7\text{ ms}$, compatible with patch-based anomaly detectors (PatchCore) and distilled vision transformers.
3. **Offline Post-Session Video Triage:** $T_{\text{inference}} \ge 1.0\text{ s per frame}$, characteristic of large multimodal vision-language models (GPT-4o, Gemini 1.5 Pro), restricting their operational deployment to asynchronous bug report synthesis from recorded gameplay sessions.
