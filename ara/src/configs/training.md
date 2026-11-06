# Training Configuration & Hyperparameters

| Hyperparameter | Value | Search Range | Rationale | Sensitivity | Source |
|---|---|---|---|---|---|
| `batch_size` | 16 | [8, 32] | Balances gradient variance with VRAM limits across multi-title batches. | Medium | Yi et al. (2025) |
| `learning_rate` | $1 \times 10^{-4}$ | [$5 \times 10^{-5}$, $2 \times 10^{-4}$] | AdamW optimizer with cosine learning rate decay schedule. | High | Rahman (2023) |
| `weight_decay` | $0.05$ | [0.01, 0.1] | Prevents overfitting on low-data regimes ($\le 150$ samples). | Low | Rahman (2023) |
| `co_title_weight_alpha` | $0.5$ | [0.2, 0.8] | Weights supervised loss of auxiliary co-domain titles against target title. | High | Yi et al. (2025) |
| `ssl_latent_weight_beta` | $0.1$ | [0.01, 0.5] | Balances latent masked autoencoder reconstruction against object detection. | Medium | Yi et al. (2025) |
| `masking_ratio` | $0.75$ | [0.60, 0.85] | Patch-wise random masking ratio for student latent encoder. | Medium | Yi et al. (2025) |
| `hac_clusters_k` | 50 | [30, 100] | Hierarchical Agglomerative Clustering clusters for SAM mask deduplication. | Medium | Rahman (2023) |
| `clip_filter_threshold` | $0.28$ | [0.20, 0.35] | Cosine similarity threshold for filtering out environmental masks (trees, sky). | High | Rahman (2023) |
| `vlm_temperature` | $0.0$ | [0.0, 0.2] | Deterministic greedy decoding for reproducible JSON output schema. | High | Taesiri et al. (2025) |
