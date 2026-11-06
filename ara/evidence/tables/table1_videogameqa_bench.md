# Table 1: VideoGameQA-Bench Full Model Benchmark Accuracy (%)

* **Source:** Taesiri et al., *VideoGameQA-Bench: Evaluating Vision-Language Models for Video Game Quality Assurance*, NeurIPS 2025 Datasets and Benchmarks Track, Table 2.
* **Corresponds to:** Claim [C01](../../logic/claims.md#c01-static-vlm-triage-vs-temporal-needle-in-a-haystack-collapse).
* **Task Legend:**
  * **VU:** Visual Unit Testing (100 samples)
  * **UI:** UI Unit Testing (100 samples)
  * **VR:** Visual Regression Testing (250 samples)
  * **IGD:** Image-based Glitch Detection (1,000 samples)
  * **PCD:** Parametric Clipping Detection (686 samples)
  * **IBR:** Image-based Bug Report Generation (100 samples)
  * **VGD:** Video-based Glitch Detection (1,000 samples)
  * **NIAH:** Needle-in-a-Haystack Temporal Localization (100 samples)
  * **VBR:** Video-based Bug Report Generation (100 samples)

| Model Architecture | VU | UI | VR | IGD | PCD | IBR | VGD | NIAH | VBR | Image Mean | Video Mean | Total Score |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **GPT-4.1** | 43.0 | 28.0 | 28.8 | 81.3 | **87.8** | 51.0 | 75.8 | 19.0 | 51.0 | **53.3** | 48.6 | **51.0** |
| **GPT-4.1-mini** | 42.0 | 30.0 | 20.4 | 76.8 | 66.9 | 46.0 | 71.8 | 10.0 | 26.0 | 47.0 | 35.9 | 41.5 |
| **GPT-4.1-nano** | 9.0 | 14.0 | 19.2 | 57.0 | 66.9 | 16.0 | 49.1 | 4.0 | 14.0 | 30.4 | 22.4 | 26.4 |
| **GPT-4o** | 39.0 | 23.0 | 31.6 | **82.8** | 82.5 | **54.0** | 57.0 | 1.0 | **52.0** | 52.2 | 36.7 | 44.4 |
| **o4-mini** | 50.0 | 35.0 | **45.2** | 76.4 | 65.0 | 38.0 | 70.0 | 18.0 | 28.0 | 51.6 | 38.7 | 45.1 |
| **o3** | 43.0 | 28.0 | 39.6 | 73.7 | 80.5 | 53.0 | 76.8 | 13.0 | 45.0 | 53.0 | 44.9 | 48.9 |
| **Gemini-2.5-Pro** | **53.0** | **40.0** | 30.8 | 75.4 | 72.2 | 33.0 | **78.1** | 34.0 | 36.0 | 50.7 | **49.4** | 50.0 |
| **Gemini-2.5-Flash** | 47.0 | 24.0 | 26.4 | 66.3 | 72.2 | 24.0 | 64.7 | 35.0 | 23.0 | 43.3 | 40.9 | 42.1 |
| **Gemini-2.0-Flash** | 44.0 | 28.0 | 12.0 | 68.1 | 78.0 | 20.0 | 54.5 | **36.0** | 26.0 | 41.7 | 38.8 | 40.3 |
| **Sonnet-3.7** | 23.0 | 22.0 | 24.0 | 65.1 | 76.4 | 29.0 | 66.9 | 31.0 | 22.0 | 39.9 | 40.0 | 39.9 |
| **Sonnet-3.5** | 23.0 | 29.0 | 14.0 | 70.1 | 72.9 | 33.0 | 61.2 | 27.0 | 26.0 | 40.3 | 38.1 | 39.2 |
| **Qwen-2.5-VL (72B)** | 38.0 | 27.0 | 21.2 | 70.0 | 76.0 | 19.0 | 47.9 | -- | 17.0 | 41.9 | 21.6 | 31.7 |
| **Mistral-Small-3.1 (24B)**| 15.0 | 17.0 | 25.6 | 59.7 | 62.5 | 9.0 | 61.4 | -- | 14.0 | 31.5 | 25.1 | 28.3 |
| **Gemma-3 (27B)** | 12.0 | 12.0 | 12.8 | 46.7 | 69.7 | 10.0 | 51.3 | -- | 9.0 | 27.2 | 20.1 | 23.6 |
| **Llama-4-Scout** | 32.0 | 23.0 | 13.6 | 55.8 | 71.6 | 8.0 | 58.6 | -- | 5.0 | 34.0 | 21.2 | 27.6 |
| **Llama-4-Maverick** | 21.0 | 22.0 | 18.4 | 53.2 | 65.7 | 7.0 | 56.6 | -- | 15.0 | 31.2 | 23.9 | 27.5 |
