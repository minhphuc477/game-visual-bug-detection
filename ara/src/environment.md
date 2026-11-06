# Environment Specification

## System & Software Dependencies
* **Python Runtime:** Python 3.12.x or 3.13.x
* **PyTorch Version:** `torch >= 2.5.0`, `torchvision >= 0.20.0`
* **VLM Inference Framework:** `vllm >= 0.6.3` / `unsloth >= 2025.2` (for open-weight Qwen3-VL and Llama-Vision models)
* **Computer Vision & Video:** `opencv-python-headless >= 4.10.0`, `ffmpeg-python >= 0.2.0`, `PyMuPDF >= 1.25.0`
* **Segmentation & Embeddings:** `segment-anything >= 1.0`, `transformers >= 4.48.0`, `sentence-transformers >= 3.3.0`
* **Vector Store & Indexing:** `elasticsearch >= 8.16.0`

## Hardware Infrastructure
* **GPU Compute:** 4 $\times$ NVIDIA L40S (48GB VRAM per GPU) or 2 $\times$ NVIDIA RTX 4090 (24GB VRAM)
* **CUDA Driver:** CUDA 12.4 / cuDNN 9.1
* **Host CPU:** 32 cores, 128 GB System RAM
* **Storage:** 2 TB NVMe SSD (for streaming video frame caching)

## Determinism & Random Seeds
* `torch.manual_seed(42)`
* `numpy.random.seed(42)`
* `random.seed(42)`
* `PYTHONHASHSEED=42`
* `torch.backends.cudnn.deterministic = True`
