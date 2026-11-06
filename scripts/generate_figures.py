#!/usr/bin/env python3
"""
Generate publication-quality figures for the Systematic Mapping Study:
- Figure 1: PRISMA-S Study Selection Flowchart
- Figure 2: Publication Trends by Year and Venue Type
- Figure 3: Bubble Map: Algorithmic Paradigm vs. Visual Testing Task
- Figure 4: Visual Defect Subtype Distribution (VGVD-Taxonomy)
- Figure 5: Modality Distribution and Cross-Game Transfer Evaluation
"""

import os
from pathlib import Path
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
import pandas as pd

# Set global style
plt.rcParams['font.sans-serif'] = 'DejaVu Sans'
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.size'] = 10
plt.rcParams['axes.labelsize'] = 11
plt.rcParams['axes.titlesize'] = 12
plt.rcParams['xtick.labelsize'] = 9
plt.rcParams['ytick.labelsize'] = 9
plt.rcParams['legend.fontsize'] = 9
plt.rcParams['figure.titlesize'] = 14

OUT_DIR = Path("manuscript/figures")
OUT_DIR.mkdir(parents=True, exist_ok=True)


def generate_figure1_prisma():
    """Figure 1: PRISMA-S 2020 Flow Diagram."""
    fig, ax = plt.subplots(figsize=(10, 8), dpi=300)
    ax.axis('off')

    # Styles
    box_blue = dict(boxstyle="round,pad=0.5", fc="#E3F2FD", ec="#1976D2", lw=1.8)
    box_orange = dict(boxstyle="round,pad=0.5", fc="#FFF3E0", ec="#F57C00", lw=1.8)
    box_green = dict(boxstyle="round,pad=0.5", fc="#E8F5E9", ec="#388E3C", lw=2.0)
    box_grey = dict(boxstyle="round,pad=0.4", fc="#F5F5F5", ec="#757575", lw=1.2)

    # Stages boxes
    # Stage 1: Identification
    ax.text(0.32, 0.90, "Databases Searched (N = 692)\n• IEEE Xplore: 142\n• ACM Digital Library: 118\n• Scopus: 184\n• Web of Science: 96\n• arXiv (cs.CV, cs.SE): 152", 
            ha='center', va='center', bbox=box_blue)
    ax.text(0.78, 0.90, "Duplicates Removed\n(n = 188 duplicates)\nVia Title/DOI/Hash match", 
            ha='center', va='center', bbox=box_grey)

    # Arrow 1
    ax.annotate('', xy=(0.58, 0.90), xytext=(0.50, 0.90),
                arrowprops=dict(arrowstyle="->", lw=1.5, color="#1976D2"))

    # Stage 2: Screening
    ax.text(0.32, 0.68, "Records Screened\nby Title & Abstract\n(N = 504 records)", 
            ha='center', va='center', bbox=box_blue)
    ax.text(0.78, 0.68, "Records Excluded (n = 416)\n• Non-visual / RL gameplay: 182\n• Pure functional logic tests: 134\n• Non-game UI tests: 68\n• Short papers / tutorials: 32", 
            ha='center', va='center', bbox=box_orange)

    ax.annotate('', xy=(0.32, 0.76), xytext=(0.32, 0.81),
                arrowprops=dict(arrowstyle="->", lw=1.5, color="#1976D2"))
    ax.annotate('', xy=(0.58, 0.68), xytext=(0.46, 0.68),
                arrowprops=dict(arrowstyle="->", lw=1.5, color="#F57C00"))

    # Stage 3: Eligibility
    ax.text(0.32, 0.44, "Full-Text Articles Assessed\nfor Eligibility\n(N = 88 articles)", 
            ha='center', va='center', bbox=box_blue)
    ax.text(0.78, 0.44, "Full-Text Excluded (n = 47)\n• Headless logic/functional: 18\n• Bot gameplay / no QA: 12\n• Non-game visual diff: 9\n• Lacking empirical metrics: 8", 
            ha='center', va='center', bbox=box_orange)

    ax.annotate('', xy=(0.32, 0.52), xytext=(0.32, 0.60),
                arrowprops=dict(arrowstyle="->", lw=1.5, color="#1976D2"))
    ax.annotate('', xy=(0.58, 0.44), xytext=(0.48, 0.44),
                arrowprops=dict(arrowstyle="->", lw=1.5, color="#F57C00"))

    # Stage 4: Snowballing & Inclusion
    ax.text(0.32, 0.22, "Eligible Studies from\nDatabase Search\n(n = 41 studies)", 
            ha='center', va='center', bbox=box_blue)
    ax.text(0.78, 0.22, "Snowballing Identification\n• Backward citation chaining: 2\n• Forward citation chaining: 2\n(n = 4 additional studies)", 
            ha='center', va='center', bbox=box_grey)

    ax.annotate('', xy=(0.32, 0.30), xytext=(0.32, 0.36),
                arrowprops=dict(arrowstyle="->", lw=1.5, color="#1976D2"))
    ax.annotate('', xy=(0.48, 0.22), xytext=(0.58, 0.22),
                arrowprops=dict(arrowstyle="<-", lw=1.5, color="#1976D2"))

    # Final Included Box
    ax.text(0.32, 0.05, "Total Included Primary Studies (N = 45)\n• Cluster 1: VLMs & Multimodal QA (10)\n• Cluster 2: Anomaly Detection & Self-Supervision (9)\n• Cluster 3: State-Aware & Telemetry Fusion (7)\n• Cluster 4: Spatio-Temporal Video Analysis (7)\n• Cluster 5: GUI, HUD & Visual Regression (6)\n• Cluster 6: Taxonomies & Systematic Reviews (6)", 
            ha='center', va='center', bbox=box_green, fontsize=9.5)

    ax.annotate('', xy=(0.32, 0.12), xytext=(0.32, 0.16),
                arrowprops=dict(arrowstyle="->", lw=2.0, color="#388E3C"))

    # Stage labels on the left margin
    stages = [
        ("IDENTIFICATION", 0.90),
        ("SCREENING", 0.68),
        ("ELIGIBILITY", 0.44),
        ("INCLUSION", 0.13),
    ]
    for label, y in stages:
        ax.text(0.04, y, label, rotation=90, ha='center', va='center', 
                fontsize=11, fontweight='bold', color="#455A64",
                bbox=dict(boxstyle="square,pad=0.3", fc="#ECEFF1", ec="#90A4AE", lw=1))

    plt.title("Figure 1: PRISMA-S 2020 Literature Selection Flow Diagram (N = 45 Included Primary Studies)", 
              fontsize=12, pad=15, fontweight='bold')
    plt.tight_layout()
    fig.savefig(OUT_DIR / "figure1_prisma_flow.png", dpi=300)
    fig.savefig(OUT_DIR / "figure1_prisma_flow.svg")
    plt.close()
    print("Saved Figure 1: PRISMA-S Flow Diagram.")


def generate_figure2_publications_by_year():
    """Figure 2: Publication Trends by Year and Venue Type."""
    df = pd.read_csv("literature/evidence_table.csv")
    
    # Cross-tabulate Year and Venue Type
    ct = pd.crosstab(df['year'], df['venue_type'])
    years = ct.index.tolist()
    
    fig, ax = plt.subplots(figsize=(9, 5.2), dpi=300)
    
    colors = {"Conference": "#1976D2", "Journal": "#388E3C", "Preprint": "#F57C00"}
    
    bottom = np.zeros(len(years))
    for vtype in ["Conference", "Journal", "Preprint"]:
        if vtype in ct.columns:
            values = ct[vtype].values
            ax.bar(years, values, bottom=bottom, label=vtype, color=colors[vtype], width=0.6, edgecolor='white', linewidth=1)
            bottom += values

    # Annotate total counts on top of bars
    for i, (yr, total) in enumerate(zip(years, bottom)):
        ax.text(yr, total + 0.2, f"{int(total)}", ha='center', va='bottom', fontweight='bold', fontsize=9.5)

    ax.set_xlabel("Publication Year", fontweight='bold', labelpad=8)
    ax.set_ylabel("Number of Primary Studies", fontweight='bold', labelpad=8)
    ax.set_title("Figure 2: Publication Trajectory and Venue Distribution (2018 – 2026, N = 45)", fontweight='bold', pad=12)
    ax.set_ylim(0, max(bottom) + 1.5)
    ax.grid(axis='y', linestyle='--', alpha=0.5)
    ax.set_axisbelow(True)
    ax.legend(title="Publication Venue Type", frameon=True, facecolor='white', framealpha=0.9)

    plt.tight_layout()
    fig.savefig(OUT_DIR / "figure2_publications_by_year.png", dpi=300)
    fig.savefig(OUT_DIR / "figure2_publications_by_year.svg")
    plt.close()
    print("Saved Figure 2: Publication Trends by Year.")


def generate_figure3_bubble_map():
    """Figure 3: Bubble Map: Algorithmic Paradigm vs. Visual Testing Task."""
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

    # Frequency matrix based on primary studies evidence mapping
    matrix = np.array([
        [4, 1, 3, 0, 4, 0],  # Classical Diffing
        [2, 7, 5, 2, 3, 0],  # Supervised Object Detection
        [1, 8, 4, 2, 1, 0],  # Anomaly Detection & Self-Supervision
        [2, 6, 2, 4, 1, 1],  # Multimodal Engine-State Fusion
        [3, 6, 5, 3, 4, 8],  # Vision-Language Models
        [1, 3, 3, 7, 1, 2],  # Spatio-Temporal Video Transformers
    ])

    fig, ax = plt.subplots(figsize=(10, 6.5), dpi=300)

    for i in range(len(paradigms)):
        for j in range(len(tasks)):
            val = matrix[i, j]
            if val > 0:
                # bubble size proportional to study count
                size = val * 85
                color = "#1565C0" if val >= 5 else "#42A5F5" if val >= 3 else "#90CAF9"
                ax.scatter(j, i, s=size, color=color, alpha=0.75, edgecolors="#0D47A1", linewidth=1.5)
                ax.text(j, i, str(val), ha='center', va='center', fontsize=9.5, fontweight='bold', color='black')

    ax.set_xticks(range(len(tasks)))
    ax.set_xticklabels(tasks, rotation=25, ha='right', fontweight='medium')
    ax.set_yticks(range(len(paradigms)))
    ax.set_yticklabels(paradigms, fontweight='medium')

    ax.set_xlabel("Visual Quality Assurance Task", fontweight='bold', labelpad=10)
    ax.set_ylabel("Technical & Algorithmic Paradigm", fontweight='bold', labelpad=10)
    ax.set_title("Figure 3: Systematic Mapping Bubble Plot: Algorithmic Paradigm vs. Visual QA Task", fontweight='bold', pad=14)
    ax.grid(True, linestyle=':', alpha=0.5)
    ax.set_axisbelow(True)

    # Size legend
    for sample_val in [2, 5, 8]:
        ax.scatter([], [], s=sample_val * 85, color="#1565C0", alpha=0.6, edgecolors="#0D47A1",
                   label=f"{sample_val} studies")
    ax.legend(title="Study Count", loc="upper left", bbox_to_anchor=(1.02, 1.0), frameon=True)

    plt.tight_layout()
    fig.savefig(OUT_DIR / "figure3_technique_vs_task_bubble.png", dpi=300)
    fig.savefig(OUT_DIR / "figure3_technique_vs_task_bubble.svg")
    plt.close()
    print("Saved Figure 3: Bubble Map.")


def generate_figure4_defect_distribution():
    """Figure 4: Distribution of the 19 VGVD-Taxonomy Defect Subtypes."""
    subtypes = [
        ("GEO-01: Mesh Clipping", 20, "#1976D2", "Spatial & Geometry"),
        ("GEO-02: Floating Asset", 7, "#1976D2", "Spatial & Geometry"),
        ("GEO-03: Vertex Distortion", 3, "#1976D2", "Spatial & Geometry"),
        ("GEO-04: Collision Mismatch", 2, "#1976D2", "Spatial & Geometry"),
        ("TEX-01: Missing Texture", 9, "#388E3C", "Material & Texture"),
        ("TEX-02: LOD Pop-In Delay", 3, "#388E3C", "Material & Texture"),
        ("TEX-03: UV Seam Tearing", 2, "#388E3C", "Material & Texture"),
        ("TEX-04: Broken Shaders", 2, "#388E3C", "Material & Texture"),
        ("REN-01: Coplanar Z-Fighting", 10, "#F57C00", "Rendering & Lighting"),
        ("REN-02: Shadow Detached", 2, "#F57C00", "Rendering & Lighting"),
        ("REN-03: Light Leaking", 2, "#F57C00", "Rendering & Lighting"),
        ("REN-04: Near-Plane Frustum", 1, "#F57C00", "Rendering & Lighting"),
        ("ANI-01: T-Pose Freeze", 6, "#7B1FA2", "Animation & Physics"),
        ("ANI-02: Ragdoll Chaos", 3, "#7B1FA2", "Animation & Physics"),
        ("ANI-03: Foot-Sliding Drift", 1, "#7B1FA2", "Animation & Physics"),
        ("ANI-04: Frame Stuttering", 2, "#7B1FA2", "Animation & Physics"),
        ("UI-01: Element Collision", 11, "#C2185B", "User Interface"),
        ("UI-02: Text Truncation", 3, "#C2185B", "User Interface"),
        ("UI-03: Aspect Ratio Stretch", 2, "#C2185B", "User Interface"),
    ]

    labels = [s[0] for s in subtypes]
    counts = [s[1] for s in subtypes]
    colors = [s[2] for s in subtypes]

    fig, ax = plt.subplots(figsize=(10, 7), dpi=300)
    bars = ax.barh(labels[::-1], counts[::-1], color=colors[::-1], edgecolor='white', height=0.65)

    for bar in bars:
        w = bar.get_width()
        ax.text(w + 0.3, bar.get_y() + bar.get_height()/2, f"{int(w)} ({w/45*100:.1f}%)", 
                va='center', ha='left', fontsize=8.5, fontweight='bold')

    ax.set_xlabel("Number of Studies Investigating Defect (and % of N = 45 Corpus)", fontweight='bold', labelpad=8)
    ax.set_title("Figure 4: Defect Subtype Coverage Across Primary Studies (VGVD-Taxonomy)", fontweight='bold', pad=12)
    ax.set_xlim(0, 24)
    ax.grid(axis='x', linestyle='--', alpha=0.5)
    ax.set_axisbelow(True)

    # Category legend
    from matplotlib.lines import Line2D
    custom_lines = [
        Line2D([0], [0], color="#1976D2", lw=6),
        Line2D([0], [0], color="#388E3C", lw=6),
        Line2D([0], [0], color="#F57C00", lw=6),
        Line2D([0], [0], color="#7B1FA2", lw=6),
        Line2D([0], [0], color="#C2185B", lw=6),
    ]
    ax.legend(custom_lines, [
        "Spatial & Geometry (GEO)",
        "Material & Texture (TEX)",
        "Rendering & Lighting (REN)",
        "Animation & Physics (ANI)",
        "User Interface & HUD (UI)"
    ], loc='lower right', frameon=True, facecolor='white', framealpha=0.9)

    plt.tight_layout()
    fig.savefig(OUT_DIR / "figure4_defect_category_distribution.png", dpi=300)
    fig.savefig(OUT_DIR / "figure4_defect_category_distribution.svg")
    plt.close()
    print("Saved Figure 4: Defect Subtype Distribution.")


def generate_figure5_modalities_and_generalisation():
    """Figure 5: Input Modality Distribution and Cross-Game Generalization."""
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11, 4.8), dpi=300)

    # Subplot 1: Modality Pie/Donut Chart
    modalities = ["Single Static Frame (RGB)", "Spatio-Temporal Video Stream", "Engine Telemetry Fused (RGB+Depth+Physics)"]
    mod_counts = [23, 14, 8]
    mod_colors = ["#42A5F5", "#66BB6A", "#FFA726"]
    
    wedges, texts, autotexts = ax1.pie(mod_counts, labels=None, autopct='%1.1f%%',
                                       startangle=140, colors=mod_colors,
                                       wedgeprops=dict(width=0.4, edgecolor='white', linewidth=2),
                                       pctdistance=0.75)
    for at in autotexts:
        at.set_fontweight('bold')
        at.set_fontsize(9.5)
    ax1.set_title("A) Input Data Modality Distribution", fontweight='bold', pad=10)
    ax1.legend(wedges, [f"{m} (n={c})" for m, c in zip(modalities, mod_counts)], 
               loc="lower center", bbox_to_anchor=(0.5, -0.22), frameon=False, fontsize=8.5)

    # Subplot 2: Cross-Game Evaluation Status
    df = pd.read_csv("literature/evidence_table.csv")
    cg_counts = df['cross_game_evaluated'].value_counts()
    categories = ["Evaluated Across Games (Yes)", "Single Game Only (No)", "Partial / Same Engine Only"]
    vals = [cg_counts.get('Yes', 0), cg_counts.get('No', 0), cg_counts.get('Partial', 0)]
    bar_colors = ["#2E7D32", "#C62828", "#EF6C00"]

    bars = ax2.bar(categories, vals, color=bar_colors, width=0.55, edgecolor='white', linewidth=1.5)
    for b in bars:
        h = b.get_height()
        ax2.text(b.get_x() + b.get_width()/2, h + 0.5, f"{int(h)} ({h/45*100:.1f}%)", 
                 ha='center', va='bottom', fontweight='bold', fontsize=9.5)

    ax2.set_ylabel("Number of Studies", fontweight='bold', labelpad=8)
    ax2.set_title("B) Cross-Game Generalisation Evaluation", fontweight='bold', pad=10)
    ax2.set_ylim(0, 30)
    ax2.grid(axis='y', linestyle='--', alpha=0.5)
    ax2.set_axisbelow(True)
    ax2.set_xticks(range(len(categories)))
    ax2.set_xticklabels(["Yes (Cross-Game)", "No (Single-Game)", "Partial (Same Engine)"], rotation=15, ha='right')

    plt.suptitle("Figure 5: Empirical Modality Breakdown and Cross-Game Generalisation Verification", 
                 fontweight='bold', fontsize=12, y=1.02)
    plt.tight_layout()
    fig.savefig(OUT_DIR / "figure5_cross_game_modalities.png", dpi=300)
    fig.savefig(OUT_DIR / "figure5_cross_game_modalities.svg")
    plt.close()
    print("Saved Figure 5: Modality and Cross-Game Breakdown.")


def main():
    print("Generating publication-ready figures for SMS...")
    generate_figure1_prisma()
    generate_figure2_publications_by_year()
    generate_figure3_bubble_map()
    generate_figure4_defect_distribution()
    generate_figure5_modalities_and_generalisation()
    print("All 5 figures successfully created in manuscript/figures/")


if __name__ == "__main__":
    main()
