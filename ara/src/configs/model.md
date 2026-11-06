# Model Architectures and Component Configurations

| Component | Architecture / Spec | Weights / Checkpoint | Input Dimensions | Purpose |
|---|---|---|---|---|
| **Primary VLM Detector** | GPT-4.1-mini / Qwen-2.5-VL-72B | Pretrained API / HuggingFace | $1024 \times 1024$ RGB | Zero-shot bug triage & rationale generation |
| **Judge VLM Critic** | GPT-5-mini / OpenAI o3 | Pretrained API | $1024 \times 1024$ RGB | Re-evaluates baseline predictions to eliminate false positives |
| **Weak Supervision ViT** | Vision Transformer (`vit-base-16`) | `dinov1-vitb16` (ImageNet-1k) | $224 \times 224 \times 3$ | Label-efficient player clipping detection (Rahman 2023) |
| **Segmentation Oracle** | Segment Anything Model (SAM) | `sam_vit_h_4b8939.pth` | Dynamic Viewport | Autonomous extraction of environmental object masks |
| **Mask Filter Embedder** | CLIP ViT Image/Text Encoder | `openai/clip-vit-base-patch32` | $224 \times 224$ (Patch 32) | Semantic deduplication and environmental mask filtering |
| **Bug Ticket Embedder** | GTE-Qwen2-1.5B | `Alibaba-NLP/gte-Qwen2-1.5B-instruct` | Sequence length 512 | Dense text vectorization for JIRA bug report RAG |
| **G-Buffer Fusion Head** | Dual-Stream ResNet-50 + GNN | Multi-Task Supervised | 7 Channels ($RGB + D + N$) | Fuses telemetry G-buffers to filter stylistic false alarms |
