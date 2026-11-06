# Engineering Heuristics and Practical Rules

## H01: I-Frame Keyframe Sampling Ratio
* **Rule:** Extract only intra-coded frames (I-frames) via `ffmpeg -select_streams v -skip_frame nokey -i input.mp4` rather than uniform 60 FPS sampling.
* **Rationale:** Consecutive gameplay frames share $>95\%$ pixel redundancy. I-frames capture major camera and scene transitions while reducing frame evaluation volume by $\approx 98.8\%$, preserving 98.79% of player-visible visual defects (Lu et al., 2026).
* **Sensitivity:** High sensitivity to fast camera whip pans; if a player spins rapidly, keyframe frequency spikes. Set maximum keyframe rate cap to 2 FPS.
* **Bounds:** $0.5 \le \text{FPS}_{\text{key}} \le 2.0$.
* **Source:** Lu et al. (FSE 2026), Section 3.1.

---

## H02: LastCleanFrame Temporal Decay & Cut Boundary Reset
* **Rule:** Restrict reference frame lookup to within a maximum sliding window of 60 seconds of preceding gameplay. If camera cosine similarity falls below $\theta = 0.40$ (indicating an instantaneous level teleport or cutscene jump), reset the reference pool to empty.
* **Rationale:** Referencing a frame from 10 minutes prior often introduces irrelevant lighting and environmental drift (e.g., dynamic day/night cycles), misleading the VLM into flagging normal environmental changes as glitches.
* **Sensitivity:** Medium; dynamic time-of-day games require tighter windows (30s).
* **Bounds:** $15\text{s} \le \Delta t_{\text{max}} \le 60\text{s}$.
* **Source:** Yu et al. (RefGlitch-Bench 2026), Section 4.

---

## H03: Canonical Viewport Negative-Space Exclusion
* **Rule:** When applying zero-shot promptable segmentation (SAM) to first-person gameplay viewports, exclude the lower-right $25\% \times 25\%$ quadrant from the automatic point-grid prompt.
* **Rationale:** The lower-right corner is predominantly occupied by the player's weapon and hands. Without exclusion, $>40\%$ of generated masks cluster on weapon geometry, saturating downstream augmentation data with trivial weapon artifacts (Rahman, 2023).
* **Sensitivity:** Low; robust across modern first-person shooters.
* **Bounds:** Normalized viewport coordinates $[0.75, 1.0] \times [0.75, 1.0]$.
* **Source:** Rahman (BMVC 2023), Section 2.2.

---

## H04: Structured JSON Chain-of-Thought Enclosure
* **Rule:** Never ask a VLM for a direct raw boolean output (`"is_glitch: true"`) without providing an explicit intermediate `"reasoning"` or `"thought_trace"` field in the JSON schema.
* **Rationale:** Direct boolean generation suppresses internal reasoning tokens, causing severe hallucination and false positives on stylized art. Forcing 50–150 tokens of visual description before outputting the boolean flag increases glitch classification accuracy by $+8.4\%$ (Taesiri et al., 2025).
* **Sensitivity:** Very high; removing the reasoning field severely degrades small/mini VLM variants (e.g., GPT-4.1-mini, Qwen3-VL-8B).
* **Bounds:** Enforce schema: `{"reasoning": str, "visual_elements": list, "is_glitch": bool}`.
* **Source:** Taesiri et al. (NeurIPS 2025), Section 3.3.
