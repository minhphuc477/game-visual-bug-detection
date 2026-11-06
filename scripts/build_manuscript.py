#!/usr/bin/env python3
"""Concatenate individual manuscript sections into a unified manuscript document."""

from pathlib import Path

SECTIONS = [
    "01_introduction.md",
    "02_methodology.md",
    "03_taxonomy.md",
    "04_results_mapping.md",
    "05_discussion_gaps.md",
    "06_conclusion.md",
]

HEADER = """# Computer Vision and Vision-Language Approaches to Visual Quality Assurance in Video Games: A Systematic Mapping Study of Tasks, Datasets, and Evaluation Methods

**Author:** Le Tran Minh Phuc  
**Target Journal:** *Visual Computing for Industry, Biomedicine, and Art* (SpringerOpen / China Graphics Society)  
**Backup Journal:** *Applied Computing and Informatics* (Emerald Publishing)  
**Publication Model:** Diamond Open Access ($0 APC)  
**Methodological Guidelines:** Petersen et al. (2015), PRISMA-S, and ROSES  
**Date:** November 2026  

---

"""

def main():
    sections_dir = Path("manuscript/sections")
    output_path = Path("manuscript/complete_manuscript.md")
    
    parts = [HEADER]
    for sec_file in SECTIONS:
        fpath = sections_dir / sec_file
        if fpath.exists():
            parts.append(fpath.read_text(encoding="utf-8"))
            parts.append("\n\n---\n\n")
        else:
            print(f"[WARN] Missing section: {fpath}")

    output_path.write_text("".join(parts), encoding="utf-8")
    print(f"[SUCCESS] Compiled complete manuscript -> {output_path} ({len(output_path.read_text(encoding='utf-8'))} characters)")

if __name__ == "__main__":
    main()
