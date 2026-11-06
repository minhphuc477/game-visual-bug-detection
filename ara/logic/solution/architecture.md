# System Architecture: Agent-Native Visual Bug Detection

```mermaid
graph TD
    subgraph Capture["1. Ingestion & Preprocessing"]
        Stream["60 FPS Gameplay Video / Engine Viewport"] --> FFmpeg["FFmpeg Keyframe Extractor<br/>(I-Frames: ~1 FPS)"]
        Stream -. Telemetry Hook .-> GBuffer["G-Buffer Capture<br/>(Depth, Normals, Colliders)"]
    end

    subgraph Memory["2. Temporal Reference Pool"]
        FFmpeg --> CurrFrame["Candidate Test Frame (I_t)"]
        Pool[("Reference Pool P<br/>{(I_k, y_k)} for k < t")]
        Policy{"Reference Selection Policy<br/>(LastCleanFrame)"}
        Pool --> Policy
        Policy --> RefFrame["Selected Reference (R_t)"]
    end

    subgraph Reasoning["3. Multimodal Cognitive Core"]
        CurrFrame --> PromptEngine["Conditioned Prompt Constructor<br/>JSON Schema + Reasoning CoT"]
        RefFrame --> PromptEngine
        GBuffer -. Fusion Embedder .-> PromptEngine
        PromptEngine --> VLM["Vision-Language Model Backbone<br/>(GPT-4o / Qwen-2.5-VL / Gemini)"]
    end

    subgraph Verification["4. Triage & Arbitration"]
        VLM --> RawPred["Prediction & Rationale<br/>(y_t, Glitch Rationale)"]
        RawPred --> Judge{"Judge / OCR Filter<br/>(Separates Log Overlays)"}
        Judge --> CleanQueue["Verified Visual Bug Queue"]
        RawPred --> Deposit["Deposit (I_t, y_t) into Reference Pool"]
        Deposit --> Pool
    end
```

## Component Graph

1. **Ingestion & Keyframe Extraction Layer:**
   - Ingests raw 60 FPS gameplay video streams or continuous playtesting runs.
   - Extracts sparse I-frames via FFmpeg to reduce temporal redundancy by ~98.8% while retaining full defect visibility.
   - Optionally captures synchronized engine telemetry G-buffers (depth, normal vectors, collision bounding hulls) where engine hooks are permissible.

2. **Temporal Reference Pool & Selection Policy:**
   - Maintains an in-memory sliding buffer of previously evaluated keyframes and their predicted defect states: $\mathcal{P}_t = \{ (I_k, \hat{y}_k) \}_{k=1}^{t-1}$.
   - Executes the `LastCleanFrame` policy: selects the most temporally recent frame certified as glitch-free ($\hat{y} = 0$).
   - Dynamically adapts comparison logic based on reference status (clean comparison vs. persistent bug warning).

3. **Multimodal Cognitive Core:**
   - Assembles structured multi-image prompts combining candidate frame $I_t$, reference frame $R_t$, and strict JSON output schemas.
   - Enforces intermediate Chain-of-Thought reasoning tokens in a dedicated `"reasoning"` JSON field prior to committing to binary output flags.

4. **Triage, Arbitration & Memory Deposit:**
   - Separates text-based engine log overlays (using fast OCR preprocessing) from visual asset/rendering defects.
   - Deposits newly evaluated test frames back into the reference pool to support downstream comparisons.
   - Generates structured bug triage reports for QA engineering queues.
