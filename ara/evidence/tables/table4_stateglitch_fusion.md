# Table 4: StateGlitch-3D Multimodal Telemetry Fusion Benchmark

* **Source:** Kovacs et al., *State-aware visual glitch detection in complex 3D video games using deep multimodal representations*, Expert Systems with Applications, Vol. 268, 2026, Table 4.
* **Corresponds to:** Claim [C03](../../logic/claims.md#c03-engine-state-telemetry-fusion-eliminates-stylistic-false-alarms).

| Model Configuration | Input Modalities | Precision (%) | Recall (%) | AUROC (%) | False Positive Rate (FPR %) | False Discovery Reduction |
|---|---|---|---|---|---|---|
| **ResNet-50 (Baseline)** | RGB Only | 74.5 | 82.1 | 81.3 | 28.4 | Baseline (0%) |
| **ViT-Base / PatchCore** | RGB Only | 78.2 | 84.6 | 85.0 | 24.1 | -15.1% |
| **RGB + Depth ($\mathbf{D}$)** | RGB + Linear Depth Buffer | 84.6 | 88.0 | 89.2 | 19.8 | -30.3% |
| **RGB + Depth + Normals ($\mathbf{N}$)**| Visual-Geometric Tensor (7-ch) | 88.1 | 90.4 | 91.8 | 17.6 | -38.0% |
| **StateGlitch Net (Full Fusion)** | **RGB + $\mathbf{D}$ + $\mathbf{N}$ + Physics Colliders ($\mathbf{C}$)** | **91.2** | **92.8** | **93.5** | **16.5** | **-41.9% Reduction** |

*Note: Incorporating internal engine telemetry reduces spurious glitch alarms caused by dynamic weather particles and fog shaders from 28.4% to 16.5%.*
