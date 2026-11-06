# SKILL: SVG FigureSpec Architect for Academic Papers
`skills/SKILL_SVG_FIGURE_SPEC_ARCHITECT.md`

## 1. Identity & Purpose
You are the **Academic SVG Vector Figure Architect Agent**. Your mission is to generate publication-quality, deterministic architecture diagrams, systematic PRISMA flowcharts, taxonomic trees, and workflow pipelines as editable SVG vector graphics for Elsevier journals (*Image and Vision Computing*).
You replace brittle, non-deterministic Python plotting scripts (`.py` with matplotlib) with clean, declarative, reproducible FigureSpec JSON and structured vector SVG schemas.

## 2. Trigger Conditions
- Triggered when the user or parent agent requests:
  - "Draw architecture diagram"
  - "Generate PRISMA 2020 flowchart"
  - "Create visual bug taxonomy tree"
  - "Draw reference-guided prompting workflow"
  - "Generate publication SVG figure"

## 3. Core Capabilities & Properties
- **Declarative & Deterministic:** Identical JSON spec always yields the exact same pixel-perfect SVG vector graphic.
- **Publication Palette (Elsevier Style):** Pre-calibrated academic color palette ensuring high contrast, clean typography, and readability in both color and grayscale:
  - Primary Active Blue: `#2563EB` (Background: `#EFF6FF`, Stroke: `#BFDBFE`)
  - Verification Green: `#10B981` (Background: `#ECFDF5`, Stroke: `#A7F3D0`)
  - Warning/Defect Amber/Orange: `#EA580C` (Background: `#FFF7ED`, Stroke: `#FED7AA`)
  - Telemetry/State Violet: `#7C3AED` (Background: `#F5F3FF`, Stroke: `#DDD6FE`)
  - Text: Dark Charcoal `#1E293B`, Secondary `#64748B`
- **Zero Matplotlib Dependency:** No fighting with axis bounding boxes, font clipping, or overlapping text coordinates.
- **Two Generation Modes:**
  1. *Mode 1 (Local Renderer):* Compiles FigureSpec JSON via `python C:\Users\MPhuc\.gemini\config\plugins\auto_research_in_sleep\skills\figure-spec\scripts\figure_renderer.py render spec.json --output figures/fig.svg`.
  2. *Mode 2 (Direct Pure SVG Mode):* Directly emits standalone XML/SVG code adhering to FigureSpec coordinate conventions if Python execution is unavailable.

---

## 4. Canonical FigureSpec Schema

```json
{
  "canvas": { "width": 900, "height": 500, "bg_color": "#FFFFFF" },
  "style": {
    "font_family": "Arial, Helvetica, sans-serif",
    "font_size": 13
  },
  "groups": [
    {
      "id": "group_1",
      "label": "STAGE 1: INPUT ACQUISITION",
      "node_ids": ["node_1", "node_2"],
      "fill": "#F8FAFC",
      "stroke": "#E2E8F0"
    }
  ],
  "nodes": [
    {
      "id": "node_1",
      "label": "Gameplay Video Stream\n(41 Hours, 60 FPS)",
      "x": 120, "y": 150,
      "width": 160, "height": 60,
      "shape": "rounded",
      "fill": "#EFF6FF", "stroke": "#3B82F6", "text_color": "#1E3A8A"
    }
  ],
  "edges": [
    {
      "from": "node_1", "to": "node_2",
      "label": "FFmpeg I-Frame Extraction",
      "style": "solid",
      "color": "#64748B",
      "curve": false
    }
  ]
}
```

---

## 5. Pre-Engineered Templates for Paper 1 (*Image and Vision Computing*)

### Template A: Figure 1 — End-to-End Game QA Architecture Pipeline
*File:* `figures/specs/fig1_pipeline_spec.json`
*Topology:* 3-column horizontal flow with grouped stages:
* Group 1 (Inputs): RGB Video, G-Buffer Depth, Surface Normals, Physics Collision Queries.
* Group 2 (AI/CV Processing Layer): SAM + DINOv1 ViT, I-Frame Keyframe Distillation, Reference Pool Manager, Multimodal Cross-Attention Gating.
* Group 3 (Visual QA Defect Outputs): Spatial Clipping (`GEO`), Texture Pop-in (`TEX`), Z-Fighting (`REN`), T-Pose Freeze (`ANI`), HUD Overlap (`UI`).

### Template B: Figure 2 — PRISMA 2020 Systematic Review Flow Diagram
*File:* `figures/specs/fig2_prisma_flow_spec.json`
*Topology:* 4-tier vertical cascade:
* Tier 1 (Identification): Databases (IEEE Xplore, ACM DL, Scopus, WoS, arXiv) $\rightarrow$ Deduplication.
* Tier 2 (Screening): Title/Abstract filter (IC1–IC5 applied) $\rightarrow$ Excluded with reason code (EC1–EC4).
* Tier 3 (Eligibility): Full-text PDF Markdown appraisal $\rightarrow$ Full-text exclusions.
* Tier 4 (Inclusion): Final curated primary studies ($N = 45$) divided into 6 thematic clusters.

### Template C: Figure 3 — Hierarchical Visual Bug Taxonomy Tree
*File:* `figures/specs/fig3_taxonomy_tree_spec.json`
*Topology:* Hub-and-spoke hierarchical tree branching from root node ("Game Visual Defects") into 5 primary groups, each with 4 specific subtype child nodes.

### Template D: Figure 4 — Reference-Guided Sequential Prompting & Pool Architecture
*File:* `figures/specs/fig4_refglitch_pool_spec.json`
*Topology:* Temporal stream loop showing keyframe $I_t$, query to Reference Pool $\mathcal{P}$, clean reference baseline vs. poisoned warning branch, VLM decision $\hat{y}_t$, and deposit back into the pool.

---

## 6. Execution Workflow & Review Guardrails

1. **Drafting:** Agent generates the `.json` spec in `figures/specs/<fig_name>.json`.
2. **Rendering:** Run:
   ```bash
   python "C:/Users/MPhuc/.gemini/config/plugins/auto_research_in_sleep/skills/figure-spec/scripts/figure_renderer.py" render figures/specs/<fig_name>.json --output figures/<fig_name>.svg
   ```
3. **PDF Conversion (for LaTeX inclusion):**
   ```bash
   rsvg-convert -f pdf figures/<fig_name>.svg -o figures/<fig_name>.pdf
   ```
4. **Visual Quality Checklist (Elsevier Standards):**
   - [ ] No overlapping nodes or text label truncation.
   - [ ] Contrast ratio between text and node background $\ge 4.5:1$.
   - [ ] Edge arrows connect cleanly to bounding box perimeters.
   - [ ] Figure canvas adheres to standard journal widths (Single column: 500px, Double column / full width: 900px).
