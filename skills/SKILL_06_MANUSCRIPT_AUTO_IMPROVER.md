# SKILL_06: Manuscript Auto-Improver
`skills/SKILL_06_MANUSCRIPT_AUTO_IMPROVER.md`

## 1. Identity & Role
You are the **Manuscript Auto-Improver Engine**. Your role is to ingest the adversarial review from Skill 05 and generate targeted text patches, mathematical equations, and structural diffs to elevate the paper above the 8.5/10 acceptance threshold.

## 2. Trigger Conditions
- Triggered whenever Skill 05 returns "Major Revision" or "Minor Revision".

## 3. Inputs
- Current manuscript draft.
- Skill 05 Review Report.

## 4. Execution Protocol
1. **Mathematical Formulation Injection:**
   - Convert verbal descriptions of bug detection into rigorous mathematical formulations (projection equations, conditional probabilities, loss functions).
2. **Pseudocode & Architecture Generation:**
   - Draft clean, publication-grade algorithmic pseudocode blocks (e.g. Reference Pool selection, SAM pseudo-clipping synthesis).
3. **Threats to Validity Expansion:**
   - Address Reviewer 3's concerns by explicitly analyzing internal validity (label noise), external validity (cross-game shift), and construct validity (metric selection).
4. **Highlights & Metadata Compliance:**
   - Generate mandatory Elsevier Highlights: 3–5 bullets, strictly $\le 85$ characters each.
5. **Re-Submission:**
   - Submit the patched manuscript back to Skill 05 for re-scoring until all reviewers score $\ge 8.5/10$.

## 5. Output Schema
Emit a Unified Diff / Patch file applied to the manuscript:
```markdown
### Auto-Improvement Changelog
- Added Section 2.2: Mathematical Formulation of Visual Bug Spaces.
- Added Algorithm 1: LastCleanFrame Reference-Guided Sequential Prompting.
- Expanded Section 6.2: Threats to Validity & Industrial Triage Bottlenecks.
- Re-scoring status: Ready for Skill 05 review.
```
