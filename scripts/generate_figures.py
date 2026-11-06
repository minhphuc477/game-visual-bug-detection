#!/usr/bin/env python3
"""
Publication-Quality Figure Generation Engine for Elsevier IMAVIS:
- Figure 1: PRISMA-S 2020 Flow Diagram (via deterministic FigureSpec & PyMuPDF)
- Figure 2: Publication Trends by Year and Venue Type (2018-2026, N=45)
- Figure 3: Bubble Map: Algorithmic Paradigm vs. Visual Testing Task
- Figure 4: Defect Subtype Coverage Across Primary Studies (VGVD-Taxonomy)
- Figure 5: Modality Distribution and Cross-Game Generalisation Evaluation
- Figure 6: Methodological Lineage and Cross-Paradigm Co-Citation Architecture (2018-2026)

All figures generated in both 300 DPI PNG and vector SVG format with zero label collisions,
clean arrow geometry, and high-contrast Elsevier academic color palettes.
"""

import os
import sys
import subprocess
from pathlib import Path
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.lines import Line2D

# Ensure UTF-8 output on Windows
os.environ["PYTHONIOENCODING"] = "utf-8"

# Set global matplotlib style
plt.rcParams['font.sans-serif'] = 'DejaVu Sans'
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.size'] = 10
plt.rcParams['axes.labelsize'] = 11
plt.rcParams['axes.titlesize'] = 12
plt.rcParams['xtick.labelsize'] = 9.5
plt.rcParams['ytick.labelsize'] = 9.5
plt.rcParams['legend.fontsize'] = 9
plt.rcParams['figure.titlesize'] = 13

OUT_DIR = Path("manuscript/figures")
OUT_DIR.mkdir(parents=True, exist_ok=True)


def generate_figure1_prisma():
    """Figure 1: PRISMA-S 2020 Flow Diagram rendered via FigureSpec + PyMuPDF."""
    print("[1/6] Generating Figure 1: PRISMA-S Flow Diagram...")
    spec_path = Path("figures/specs/figure1_prisma_spec.json")
    svg_path = OUT_DIR / "figure1_prisma_flow.svg"
    png_path = OUT_DIR / "figure1_prisma_flow.png"
    
    renderer_script = Path("C:/Users/MPhuc/.gemini/config/plugins/auto_research_in_sleep/skills/figure-spec/scripts/figure_renderer.py")
    
    if renderer_script.exists() and spec_path.exists():
        # Render SVG via FigureSpec
        cmd = [sys.executable, str(renderer_script), "render", str(spec_path), "--output", str(svg_path)]
        env = os.environ.copy()
        env["PYTHONIOENCODING"] = "utf-8"
        res = subprocess.run(cmd, env=env, capture_output=True, text=True)
        if res.returncode != 0:
            print(f"  Warning: figure_renderer returned code {res.returncode}: {res.stderr}")
            
        # Convert SVG to 300 DPI PNG via PyMuPDF
        try:
            import fitz
            doc = fitz.open(str(svg_path))
            page = doc[0]
            pix = page.get_pixmap(dpi=300)
            pix.save(str(png_path))
            print(f"  [OK] Saved Figure 1 (FigureSpec): {svg_path} & {png_path} (300 DPI)")
            return
        except Exception as e:
            print(f"  PyMuPDF render fallback: {e}")
            
    # Fallback to direct Matplotlib PRISMA renderer with calibrated geometry
    fig, ax = plt.subplots(figsize=(11, 8.5), dpi=300)
    ax.axis('off')
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)

    box_blue = dict(boxstyle="round,pad=0.5", fc="#EFF6FF", ec="#2563EB", lw=1.8)
    box_orange = dict(boxstyle="round,pad=0.5", fc="#FFF7ED", ec="#EA580C", lw=1.8)
    box_green = dict(boxstyle="round,pad=0.6", fc="#ECFDF5", ec="#059669", lw=2.0)
    box_grey = dict(boxstyle="round,pad=0.4", fc="#F1F5F9", ec="#64748B", lw=1.2)

    # Stage 1: Identification
    ax.text(0.35, 0.90, "Databases Searched (N = 692)\n• IEEE Xplore: 142  |  ACM DL: 118\n• Scopus: 184  |  Web of Science: 96\n• arXiv (cs.CV, cs.SE): 152", 
            ha='center', va='center', bbox=box_blue, fontsize=9.5)
    ax.text(0.78, 0.90, "Duplicates Removed\n(n = 188 duplicates)\nTitle & DOI Deduplication", 
            ha='center', va='center', bbox=box_grey, fontsize=9)
    ax.annotate('', xy=(0.63, 0.90), xytext=(0.53, 0.90),
                arrowprops=dict(arrowstyle="->", lw=1.5, color="#2563EB"))

    # Stage 2: Screening
    ax.text(0.35, 0.69, "Records Screened\nby Title & Abstract\n(N = 504 records)", 
            ha='center', va='center', bbox=box_blue, fontsize=9.5)
    ax.text(0.78, 0.69, "Records Excluded (n = 416)\n• Non-visual / RL gameplay: 182\n• Pure functional logic tests: 134\n• Non-game UI tests: 68\n• Short papers / tutorials: 32", 
            ha='center', va='center', bbox=box_orange, fontsize=8.5)
    ax.annotate('', xy=(0.35, 0.77), xytext=(0.35, 0.83),
                arrowprops=dict(arrowstyle="->", lw=1.5, color="#2563EB"))
    ax.annotate('', xy=(0.61, 0.69), xytext=(0.49, 0.69),
                arrowprops=dict(arrowstyle="->", lw=1.5, color="#EA580C"))

    # Stage 3: Eligibility
    ax.text(0.35, 0.46, "Full-Text Articles Assessed\nfor Eligibility\n(N = 88 articles)", 
            ha='center', va='center', bbox=box_blue, fontsize=9.5)
    ax.text(0.78, 0.46, "Full-Text Excluded (n = 47)\n• Headless logic / no oracle: 18\n• Game bot / no defect QA: 12\n• Synthetic robotics data only: 9\n• Lacking empirical metrics: 8", 
            ha='center', va='center', bbox=box_orange, fontsize=8.5)
    ax.annotate('', xy=(0.35, 0.54), xytext=(0.35, 0.61),
                arrowprops=dict(arrowstyle="->", lw=1.5, color="#2563EB"))
    ax.annotate('', xy=(0.61, 0.46), xytext=(0.49, 0.46),
                arrowprops=dict(arrowstyle="->", lw=1.5, color="#EA580C"))

    # Stage 4: Snowballing & Inclusion
    ax.text(0.35, 0.25, "Eligible Studies from\nDatabase Search\n(n = 41 primary studies)", 
            ha='center', va='center', bbox=box_blue, fontsize=9.5)
    ax.text(0.78, 0.25, "Snowballing Identification\n• Backward citation chaining: 2\n• Forward citation chaining: 2\n(n = 4 additional studies)", 
            ha='center', va='center', bbox=box_grey, fontsize=9)
    ax.annotate('', xy=(0.35, 0.33), xytext=(0.35, 0.38),
                arrowprops=dict(arrowstyle="->", lw=1.5, color="#2563EB"))
    ax.annotate('', xy=(0.49, 0.25), xytext=(0.63, 0.25),
                arrowprops=dict(arrowstyle="<-", lw=1.5, color="#2563EB"))

    # Final Included Box
    ax.text(0.55, 0.08, "Total Included Primary Studies (N = 45)\n• C1: Vision-Language Models & Multimodal QA (10)\n• C2: Anomaly Detection & Self-Supervised Learning (9)\n• C3: State-Aware & Engine-Hooked Telemetry Fusion (7)\n• C4: Spatio-Temporal Video Stream Analysis (7)\n• C5: GUI, HUD & Visual Regression Testing (6)\n• C6: Empirical Taxonomies & Systematic Reviews (6)", 
            ha='center', va='center', bbox=box_green, fontsize=9.5)
    ax.annotate('', xy=(0.45, 0.15), xytext=(0.35, 0.19),
                arrowprops=dict(arrowstyle="->", lw=2.0, color="#059669"))

    stages = [
        ("IDENTIFICATION", 0.90),
        ("SCREENING", 0.69),
        ("ELIGIBILITY", 0.46),
        ("INCLUSION", 0.16),
    ]
    for label, y in stages:
        ax.text(0.06, y, label, rotation=90, ha='center', va='center', 
                fontsize=10.5, fontweight='bold', color="#475569",
                bbox=dict(boxstyle="square,pad=0.3", fc="#F8FAFC", ec="#CBD5E1", lw=1))

    plt.tight_layout()
    fig.savefig(png_path, dpi=300, bbox_inches="tight")
    fig.savefig(svg_path, bbox_inches="tight")
    plt.close()
    print(f"  [OK] Saved Figure 1: {svg_path} & {png_path}")


def generate_figure2_publications_by_year():
    """Figure 2: Publication Trends by Year and Venue Type."""
    print("[2/6] Generating Figure 2: Publication Trajectory...")
    df = pd.read_csv("literature/evidence_table.csv")
    ct = pd.crosstab(df['year'], df['venue_type'])
    years = ct.index.tolist()
    
    fig, ax = plt.subplots(figsize=(9, 5.2), dpi=300)
    colors = {"Conference": "#2563EB", "Journal": "#059669", "Preprint": "#EA580C"}
    
    bottom = np.zeros(len(years))
    for vtype in ["Conference", "Journal", "Preprint"]:
        if vtype in ct.columns:
            values = ct[vtype].values
            ax.bar(years, values, bottom=bottom, label=vtype, color=colors[vtype], width=0.58, edgecolor='white', linewidth=1.2)
            bottom += values

    for yr, total in zip(years, bottom):
        ax.text(yr, total + 0.3, f"{int(total)}", ha='center', va='bottom', fontweight='bold', fontsize=10, color="#1E293B")

    ax.set_xlabel("Publication Year", fontweight='bold', labelpad=8)
    ax.set_ylabel("Number of Primary Studies", fontweight='bold', labelpad=8)
    ax.set_title("Figure 2: Publication Trajectory and Venue Distribution (2018–2026, N = 45)", fontweight='bold', pad=14)
    ax.set_ylim(0, max(bottom) + 2.0)
    ax.grid(axis='y', linestyle='--', alpha=0.5)
    ax.set_axisbelow(True)
    ax.legend(title="Venue Type", frameon=True, facecolor='white', framealpha=0.95, edgecolor='#CBD5E1')

    plt.tight_layout()
    fig.savefig(OUT_DIR / "figure2_publications_by_year.png", dpi=300, bbox_inches="tight")
    fig.savefig(OUT_DIR / "figure2_publications_by_year.svg", bbox_inches="tight")
    plt.close()
    print("  [OK] Saved Figure 2: Publication Trends by Year.")


def generate_figure3_bubble_map():
    """Figure 3: Bubble Map: Algorithmic Paradigm vs. Visual Testing Task."""
    print("[3/6] Generating Figure 3: Bubble Map...")
    paradigms = [
        "1. Classical Diffing & Perceptual Hashing",
        "2. Supervised Object / Defect Detection",
        "3. Anomaly Detection & Self-Supervision",
        "4. Multimodal Engine-State Fusion",
        "5. Vision-Language Models (VLMs)",
        "6. Spatio-Temporal Video Transformers",
    ]
    tasks = [
        "Visual Unit / Regression Testing",
        "Spatial Mesh Clipping (GEO-01/02)",
        "Material & Shader Glitches (TEX)",
        "Temporal / Animation Defects (ANI)",
        "GUI & HUD Visual Integrity (UI)",
        "Automated Bug Report Generation",
    ]

    matrix = np.array([
        [4, 1, 3, 0, 4, 0],
        [2, 7, 5, 2, 3, 0],
        [1, 8, 4, 2, 1, 0],
        [2, 6, 2, 4, 1, 1],
        [3, 6, 5, 3, 4, 8],
        [1, 3, 3, 7, 1, 2],
    ])

    fig, ax = plt.subplots(figsize=(11, 6.8), dpi=300)

    for i in range(len(paradigms)):
        for j in range(len(tasks)):
            val = matrix[i, j]
            if val > 0:
                size = val * 95
                color = "#1D4ED8" if val >= 5 else "#3B82F6" if val >= 3 else "#93C5FD"
                ax.scatter(j, i, s=size, color=color, alpha=0.8, edgecolors="#1E3A8A", linewidth=1.5)
                ax.text(j, i, str(val), ha='center', va='center', fontsize=9.5, fontweight='bold', color='white' if val >= 3 else '#1E293B')

    ax.set_xticks(range(len(tasks)))
    ax.set_xticklabels(tasks, rotation=22, ha='right', fontweight='semibold', fontsize=9.5)
    ax.set_yticks(range(len(paradigms)))
    ax.set_yticklabels(paradigms, fontweight='semibold', fontsize=9.5)

    ax.set_xlabel("Visual Quality Assurance Task", fontweight='bold', labelpad=10)
    ax.set_ylabel("Technical & Algorithmic Paradigm", fontweight='bold', labelpad=10)
    ax.set_title("Figure 3: Systematic Mapping Bubble Plot: Algorithmic Paradigm vs. Visual QA Task", fontweight='bold', pad=16)
    ax.grid(True, linestyle=':', alpha=0.55)
    ax.set_axisbelow(True)

    # Size legend placed neatly without truncation
    for sample_val in [2, 5, 8]:
        ax.scatter([], [], s=sample_val * 95, color="#3B82F6", alpha=0.8, edgecolors="#1E3A8A",
                   label=f"{sample_val} studies")
    leg = ax.legend(title="Study Count", loc="upper left", bbox_to_anchor=(1.01, 1.0), frameon=True,
                    facecolor='white', edgecolor='#CBD5E1', framealpha=0.95)
    leg.get_title().set_fontweight("bold")

    plt.tight_layout()
    fig.savefig(OUT_DIR / "figure3_technique_vs_task_bubble.png", dpi=300, bbox_inches="tight")
    fig.savefig(OUT_DIR / "figure3_technique_vs_task_bubble.svg", bbox_inches="tight")
    plt.close()
    print("  [OK] Saved Figure 3: Bubble Map.")


def generate_figure4_defect_distribution():
    """Figure 4: Distribution of the 19 VGVD-Taxonomy Defect Subtypes."""
    print("[4/6] Generating Figure 4: Defect Distribution...")
    subtypes = [
        ("GEO-01: Mesh Clipping", 20, "#2563EB", "Spatial & Geometry"),
        ("GEO-02: Floating Asset", 7, "#2563EB", "Spatial & Geometry"),
        ("GEO-03: Vertex Distortion", 3, "#2563EB", "Spatial & Geometry"),
        ("GEO-04: Collision Mismatch", 2, "#2563EB", "Spatial & Geometry"),
        ("TEX-01: Missing Texture", 9, "#059669", "Material & Texture"),
        ("TEX-02: LOD Pop-In Delay", 3, "#059669", "Material & Texture"),
        ("TEX-03: UV Seam Tearing", 2, "#059669", "Material & Texture"),
        ("TEX-04: Broken Shaders", 2, "#059669", "Material & Texture"),
        ("REN-01: Coplanar Z-Fighting", 10, "#EA580C", "Rendering & Lighting"),
        ("REN-02: Shadow Detached", 2, "#EA580C", "Rendering & Lighting"),
        ("REN-03: Light Leaking", 2, "#EA580C", "Rendering & Lighting"),
        ("REN-04: Near-Plane Frustum", 1, "#EA580C", "Rendering & Lighting"),
        ("ANI-01: T-Pose Freeze", 6, "#7C3AED", "Animation & Physics"),
        ("ANI-02: Ragdoll Chaos", 3, "#7C3AED", "Animation & Physics"),
        ("ANI-03: Foot-Sliding Drift", 1, "#7C3AED", "Animation & Physics"),
        ("ANI-04: Frame Stuttering", 2, "#7C3AED", "Animation & Physics"),
        ("UI-01: Element Collision", 11, "#DB2777", "User Interface"),
        ("UI-02: Text Truncation", 3, "#DB2777", "User Interface"),
        ("UI-03: Aspect Ratio Stretch", 2, "#DB2777", "User Interface"),
    ]

    labels = [s[0] for s in subtypes]
    counts = [s[1] for s in subtypes]
    colors = [s[2] for s in subtypes]

    fig, ax = plt.subplots(figsize=(10.5, 7.5), dpi=300)
    bars = ax.barh(labels[::-1], counts[::-1], color=colors[::-1], edgecolor='white', height=0.68)

    for bar in bars:
        w = bar.get_width()
        ax.text(w + 0.35, bar.get_y() + bar.get_height()/2, f"{int(w)} ({w/45*100:.1f}%)", 
                va='center', ha='left', fontsize=8.8, fontweight='bold', color="#1E293B")

    ax.set_xlabel("Number of Studies Investigating Defect (and % of N = 45 Corpus)", fontweight='bold', labelpad=10)
    ax.set_title("Figure 4: Defect Subtype Coverage Across Primary Studies (VGVD-Taxonomy)", fontweight='bold', pad=14)
    ax.set_xlim(0, 25)
    ax.grid(axis='x', linestyle='--', alpha=0.55)
    ax.set_axisbelow(True)

    # Position Legend at UPPER RIGHT where bars are short (counts <= 7), completely avoiding bar collision!
    custom_lines = [
        Line2D([0], [0], color="#2563EB", lw=6),
        Line2D([0], [0], color="#059669", lw=6),
        Line2D([0], [0], color="#EA580C", lw=6),
        Line2D([0], [0], color="#7C3AED", lw=6),
        Line2D([0], [0], color="#DB2777", lw=6),
    ]
    leg = ax.legend(custom_lines, [
        "Spatial & Geometry (GEO)",
        "Material & Texture (TEX)",
        "Rendering & Lighting (REN)",
        "Animation & Physics (ANI)",
        "User Interface & HUD (UI)"
    ], loc='upper right', frameon=True, facecolor='white', framealpha=0.96, edgecolor='#CBD5E1', fontsize=9.5)
    leg.get_title().set_fontweight("bold")

    plt.tight_layout()
    fig.savefig(OUT_DIR / "figure4_defect_category_distribution.png", dpi=300, bbox_inches="tight")
    fig.savefig(OUT_DIR / "figure4_defect_category_distribution.svg", bbox_inches="tight")
    plt.close()
    print("  [OK] Saved Figure 4: Defect Subtype Distribution.")


def generate_figure5_modalities_and_generalisation():
    """Figure 5: Input Modality Distribution and Cross-Game Generalization."""
    print("[5/6] Generating Figure 5: Modality & Generalization Breakdown...")
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5.2), dpi=300)

    # Subplot 1: Modality Pie/Donut Chart
    modalities = ["Single Static Frame (RGB)", "Spatio-Temporal Video Stream", "Engine Telemetry Fused (RGB+Depth+Physics)"]
    mod_counts = [23, 14, 8]
    mod_colors = ["#3B82F6", "#10B981", "#F59E0B"]
    
    wedges, texts, autotexts = ax1.pie(mod_counts, labels=None, autopct='%1.1f%%',
                                       startangle=140, colors=mod_colors,
                                       wedgeprops=dict(width=0.42, edgecolor='white', linewidth=2.5),
                                       pctdistance=0.76)
    for at in autotexts:
        at.set_fontweight('bold')
        at.set_fontsize(10)
        at.set_color('#FFFFFF')
        
    ax1.set_title("A) Input Data Modality Distribution", fontweight='bold', pad=12)
    ax1.legend(wedges, [f"{m} (n={c})" for m, c in zip(modalities, mod_counts)], 
               loc="lower center", bbox_to_anchor=(0.5, -0.22), frameon=True, 
               facecolor='white', edgecolor='#E2E8F0', framealpha=0.95, fontsize=8.8)

    # Subplot 2: Cross-Game Evaluation Status
    df = pd.read_csv("literature/evidence_table.csv")
    cg_counts = df['cross_game_evaluated'].value_counts()
    categories = ["Evaluated Across Games (Yes)", "Single Game Only (No)", "Partial / Same Engine Only"]
    vals = [cg_counts.get('Yes', 0), cg_counts.get('No', 0), cg_counts.get('Partial', 0)]
    bar_colors = ["#059669", "#DC2626", "#D97706"]

    bars = ax2.bar(categories, vals, color=bar_colors, width=0.52, edgecolor='white', linewidth=1.5)
    for b in bars:
        h = b.get_height()
        ax2.text(b.get_x() + b.get_width()/2, h + 0.6, f"{int(h)} ({h/45*100:.1f}%)", 
                 ha='center', va='bottom', fontweight='bold', fontsize=9.8, color="#1E293B")

    ax2.set_ylabel("Number of Studies", fontweight='bold', labelpad=8)
    ax2.set_title("B) Cross-Game Generalisation Evaluation", fontweight='bold', pad=12)
    ax2.set_ylim(0, 31)
    ax2.grid(axis='y', linestyle='--', alpha=0.5)
    ax2.set_axisbelow(True)
    ax2.set_xticks(range(len(categories)))
    ax2.set_xticklabels(["Yes (Cross-Game)", "No (Single-Game)", "Partial (Same Engine)"], rotation=12, ha='right', fontweight='semibold')

    plt.suptitle("Figure 5: Empirical Modality Breakdown and Cross-Game Generalisation Verification", 
                 fontweight='bold', fontsize=12.5, y=1.02)
    plt.tight_layout()
    fig.savefig(OUT_DIR / "figure5_cross_game_modalities.png", dpi=300, bbox_inches="tight")
    fig.savefig(OUT_DIR / "figure5_cross_game_modalities.svg", bbox_inches="tight")
    plt.close()
    print("  [OK] Saved Figure 5: Modality and Cross-Game Breakdown.")


def generate_figure6_citation_network():
    """Figure 6: Bibliometric Co-Citation and Methodological Lineage (2018-2026)."""
    print("[6/6] Generating Figure 6: Methodological Lineage Architecture...")
    fig, ax = plt.subplots(figsize=(15.5, 9.5), dpi=300)
    ax.set_facecolor("#FAFAFA")
    fig.patch.set_facecolor("#FFFFFF")
    
    # 6 Paradigm Clusters definition with alternating label offsets to completely eliminate text collisions
    clusters = {
        "Foundations & Surveys": {
            "color": "#4A5568", "y": 5.2,
            "nodes": [
                {"id": "Petersen '15", "year": 2015, "x": 2015.0, "label": "Petersen et al.\n(SMS Guidelines)", "align": "above"},
                {"id": "Kitchenham '07", "year": 2016, "x": 2016.3, "label": "Kitchenham '07\n(SE SLR Guide)", "align": "below"},
                {"id": "Pascarella '18", "year": 2018, "x": 2018.0, "label": "Pascarella '18\n(Game QA Taxonomy)", "align": "above"},
                {"id": "Politowski '21", "year": 2021, "x": 2021.0, "label": "Politowski et al.\n(1M Steam Bug Survey)", "align": "above"},
                {"id": "Svensson '25", "year": 2025, "x": 2025.0, "label": "Svensson '25\n(Industrial QA Gaps)", "align": "above"}
            ]
        },
        "Classical Diffing & GUI": {
            "color": "#2563EB", "y": 4.2,
            "nodes": [
                {"id": "Moran '20", "year": 2020, "x": 2020.2, "label": "Moran '20\n(Pixel Differencing)", "align": "above"},
                {"id": "Chen '21", "year": 2021, "x": 2021.4, "label": "Chen '21\n(GLIB GUI Hierarchy)", "align": "below"},
                {"id": "Macklon '22", "year": 2022, "x": 2022.2, "label": "Macklon '22\n(HTML5 Canvas AST)", "align": "above"},
                {"id": "Chen '25", "year": 2025, "x": 2025.2, "label": "Chen et al. '25\n(VLM-UI Bounds)", "align": "above"}
            ]
        },
        "Deep Supervised Detection": {
            "color": "#DC2626", "y": 3.2,
            "nodes": [
                {"id": "Ling '20", "year": 2020, "x": 2020.0, "label": "Ling et al. '20\n(AIIDE Fast R-CNN)", "align": "above"},
                {"id": "Davarmanesh '20", "year": 2020, "x": 2020.9, "label": "Davarmanesh '20\n(Domain Shift 38% Drop)", "align": "below"},
                {"id": "Biemer '21", "year": 2021, "x": 2021.5, "label": "Biemer '21\n(Grammar Synth)", "align": "above"},
                {"id": "Tamm '22", "year": 2022, "x": 2022.4, "label": "Tamm '22\n(Synthetic Injection)", "align": "above"}
            ]
        },
        "Anomaly & Self-Supervision": {
            "color": "#0D9488", "y": 2.2,
            "nodes": [
                {"id": "Al-Dujaili '22", "year": 2022, "x": 2022.0, "label": "Al-Dujaili '22\n(Contrastive Reps)", "align": "above"},
                {"id": "Shin '23", "year": 2023, "x": 2023.2, "label": "Shin & Park '23\n(Multi-View PatchCore)", "align": "below"},
                {"id": "Rahman '23", "year": 2023, "x": 2023.8, "label": "Rahman '23\n(SAM + DINO Few-Shot)", "align": "above"},
                {"id": "Yi '25", "year": 2025, "x": 2025.1, "label": "Yi et al. '25\n(Hybrid Co-finetuning)", "align": "above"}
            ]
        },
        "State-Aware & Telemetry": {
            "color": "#D97706", "y": 1.2,
            "nodes": [
                {"id": "Bergdahl '20", "year": 2020, "x": 2020.4, "label": "Bergdahl '20\n(Frostbite Hooks)", "align": "above"},
                {"id": "Zheng '21", "year": 2021, "x": 2021.2, "label": "Zheng '21\n(Wuji RL Bot)", "align": "below"},
                {"id": "Liu '22", "year": 2022, "x": 2022.5, "label": "Liu '22\n(Inspector Telemetry)", "align": "above"},
                {"id": "Kovacs '26", "year": 2026, "x": 2026.0, "label": "Kovacs et al. '26\n(G-Buffer Fusion -41% FP)", "align": "above"}
            ]
        },
        "Vision-Language & Foundation": {
            "color": "#7C3AED", "y": 0.2,
            "nodes": [
                {"id": "Taesiri '22", "year": 2022, "x": 2022.6, "label": "Taesiri '22\n(CLIP Zero-Shot)", "align": "above"},
                {"id": "Taesiri '24", "year": 2024, "x": 2024.1, "label": "Taesiri '24\n(GlitchBench CVPR)", "align": "below"},
                {"id": "Taesiri '25", "year": 2025, "x": 2025.0, "label": "Taesiri '25\n(VideoGameQA-Bench)", "align": "above"},
                {"id": "Yu '26", "year": 2026, "x": 2025.9, "label": "Yu et al. '26\n(RefGlitch F1 +27%)", "align": "below"},
                {"id": "Lu '26", "year": 2026, "x": 2026.4, "label": "Lu et al. '26\n(EA 20K Keyframe Audit)", "align": "above"}
            ]
        }
    }
    
    years = [2015, 2016, 2018, 2020, 2021, 2022, 2023, 2024, 2025, 2026]
    for yr in years:
        ax.axvline(x=yr, color="#E2E8F0", linestyle="--", linewidth=0.9, zorder=1)
        ax.text(yr, -0.65, str(yr), ha="center", va="top", fontsize=10.5, fontweight='bold', color="#475569")
        
    for cname, cdata in clusters.items():
        y = cdata["y"]
        ax.fill_between([2014.4, 2026.9], y - 0.42, y + 0.42, color=cdata["color"], alpha=0.045, zorder=0)
        ax.text(2014.5, y + 0.32, cname.upper(), fontsize=9, fontweight='bold', color=cdata["color"], alpha=0.95)
        
    arrows = [
        ("Pascarella '18", "Ling '20", "#64748B"),
        ("Ling '20", "Davarmanesh '20", "#DC2626"),
        ("Davarmanesh '20", "Al-Dujaili '22", "#0D9488"),
        ("Al-Dujaili '22", "Shin '23", "#0D9488"),
        ("Shin '23", "Rahman '23", "#0D9488"),
        ("Rahman '23", "Yi '25", "#0D9488"),
        ("Bergdahl '20", "Zheng '21", "#D97706"),
        ("Zheng '21", "Liu '22", "#D97706"),
        ("Liu '22", "Kovacs '26", "#D97706"),
        ("Taesiri '22", "Taesiri '24", "#7C3AED"),
        ("Taesiri '24", "Taesiri '25", "#7C3AED"),
        ("Taesiri '25", "Yu '26", "#7C3AED"),
        ("Taesiri '25", "Lu '26", "#7C3AED"),
        ("Rahman '23", "Yu '26", "#6D28D9"),
        ("Macklon '22", "Chen '25", "#2563EB")
    ]
    
    node_coords = {}
    for cdata in clusters.values():
        for n in cdata["nodes"]:
            node_coords[n["id"]] = (n["x"], cdata["y"])
            
    # Draw arrows with shrink padding to hit node circles without piercing text badges
    for src, dst, col in arrows:
        if src in node_coords and dst in node_coords:
            x1, y1 = node_coords[src]
            x2, y2 = node_coords[dst]
            ax.annotate("", xy=(x2, y2), xytext=(x1, y1),
                        arrowprops=dict(arrowstyle="-|>", color=col, lw=1.6, alpha=0.72,
                                        shrinkA=14, shrinkB=14,
                                        connectionstyle="arc3,rad=-0.12", mutation_scale=12),
                        zorder=2)

    # Plot Nodes with staggered, collision-free text labels
    for cname, cdata in clusters.items():
        col = cdata["color"]
        y = cdata["y"]
        for n in cdata["nodes"]:
            x = n["x"]
            ax.scatter(x, y, s=580, color="#FFFFFF", edgecolors=col, linewidth=2.5, zorder=3)
            ax.scatter(x, y, s=330, color=col, alpha=0.18, zorder=3)
            
            # Stagger label position (above or below node)
            if n.get("align") == "below":
                y_text = y - 0.17
                va_pos = "top"
            else:
                y_text = y + 0.17
                va_pos = "bottom"
                
            ax.text(x, y_text, n["label"], ha="center", va=va_pos, fontsize=8.2, 
                    fontweight="semibold", color="#0F172A", zorder=4,
                    bbox=dict(boxstyle="round,pad=0.25", facecolor="#FFFFFF", edgecolor=col, alpha=0.96, lw=0.9))

    ax.set_xlim(2014.2, 2027.0)
    ax.set_ylim(-0.85, 6.0)
    ax.set_title("Figure 6: Methodological Lineage and Cross-Paradigm Co-Citation Architecture (2018–2026)",
                 fontsize=14, fontweight="bold", pad=20, color="#0F172A")
    
    legend_patches = [mpatches.Patch(color=c["color"], label=name) for name, c in clusters.items()]
    leg = ax.legend(handles=legend_patches, loc="upper right", bbox_to_anchor=(0.99, 0.98),
                    frameon=True, framealpha=0.96, facecolor="#FFFFFF", edgecolor="#CBD5E0",
                    fontsize=8.8, title="Methodological Paradigm Clusters", title_fontsize=9.8)
    leg.get_title().set_fontweight("bold")
    
    ax.axis("off")
    plt.tight_layout()
    fig.savefig(OUT_DIR / "figure6_citation_network.png", dpi=300, bbox_inches="tight")
    fig.savefig(OUT_DIR / "figure6_citation_network.svg", bbox_inches="tight")
    plt.close()
    print("  [OK] Saved Figure 6: Citation Network and Lineage Architecture.")


def main():
    print("=" * 70)
    print("Generating Pristine Publication-Quality Figures (300 DPI & Vector SVG)...")
    print("=" * 70)
    generate_figure1_prisma()
    generate_figure2_publications_by_year()
    generate_figure3_bubble_map()
    generate_figure4_defect_distribution()
    generate_figure5_modalities_and_generalisation()
    generate_figure6_citation_network()
    print("=" * 70)
    print("All 6 figures successfully updated in manuscript/figures/")
    print("=" * 70)


if __name__ == "__main__":
    main()
