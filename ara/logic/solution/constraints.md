# Operational Constraints and Environmental Boundaries

## 1. Latency & Playtesting Throughput Limits
* **Interactive 60 FPS Target:** Commercial interactive playtesting runs at 60 to 120 FPS ($16.6\text{ ms} - 8.3\text{ ms}$ per frame). Current foundation VLMs (GPT-4o, Claude 3.5 Sonnet, Gemini 2.5 Pro) exhibit inference latencies between 1,200 ms and 3,500 ms per request. Consequently, real-time in-loop VLM playtesting is strictly infeasible without temporal downsampling or asynchronous batching.
* **Overnight Soak Batch Limit:** A standard nightly CI build produces between 40 and 200 hours of gameplay video across testing rigs. Total keyframe processing must complete within a 6-hour overnight window ($\le 108,000$ seconds), requiring effective inference throughput of at least 5 frames per second across distributed worker nodes.

---

## 2. Hardware & Memory Footprint
* **VRAM Boundaries:** On-premise industrial QA clusters typically utilize consumer or enterprise GPUs with 24GB to 48GB VRAM (NVIDIA RTX 4090, A5000, L40S). Loading 70B+ parameter vision-language models (e.g., Llama-3.2-90B-Vision, Qwen-2.5-VL-72B) requires 4-bit/8-bit AWQ/GPTQ quantization or multi-GPU tensor parallelism.
* **Video Transformer Context Limits:** Ingesting dense 60 FPS continuous clips into spatio-temporal video transformers exceeds GPU memory beyond 64 consecutive frames, necessitating sliding-window temporal pooling.

---

## 3. Black-Box vs. White-Box Accessibility
* **Compiled Release Builds:** Release candidate and security-locked builds disable debug console commands, G-buffer readback hooks, and internal telemetry APIs. Algorithms relying strictly on post-render RGB screen pixels are universally deployable across all build targets (PC, console, mobile).
* **Engine Instrumentation Constraints:** Accessing depth and collision buffers introduces memory copy overhead from GPU render targets to CPU memory, causing potential micro-stutters during active gameplay benchmarking.
