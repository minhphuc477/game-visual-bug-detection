#!/usr/bin/env python3
"""Concatenate individual manuscript sections into a unified manuscript document following the 8-Pillar IMAVIS framework."""

from pathlib import Path

SECTIONS = [
    "01_introduction.md",
    "02_problem_formulation.md",
    "03_methodology.md",
    "04_taxonomy.md",
    "05_results_mapping.md",
    "06_benchmark_audit.md",
    "07_meta_analysis_failure_modes.md",
    "08_open_challenges_conclusion.md",
]

HEADER = """# Computer Vision and Vision-Language Approaches to Visual Quality Assurance in Video Games: A Systematic Mapping Study of Tasks, Datasets, and Evaluation Methods

**Author:** Le Tran Minh Phuc  
**Target Journal:** *Image and Vision Computing* (Elsevier, ScienceDirect)  
**Backup Journal:** *Pattern Recognition* / *Expert Systems with Applications* (Elsevier)  
**Publishing Model:** Standard Elsevier Hybrid ($0 APC for authors)  
**Indexing:** SCIE, Scopus Q1, CiteScore 8.5–9.0, CORE Rank B  
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
    char_count = len(output_path.read_text(encoding="utf-8"))
    word_count = len(output_path.read_text(encoding="utf-8").split())
    print(f"[SUCCESS] Compiled 8-Pillar IMAVIS manuscript -> {output_path}")
    print(f"  Length: {char_count:,} characters | ~{word_count:,} words")

if __name__ == "__main__":
    main()
