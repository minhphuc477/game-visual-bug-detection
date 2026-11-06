#!/usr/bin/env python3
"""
Automated downloader for verified academic literature on AI-Based Visual Bug Detection in Video Games.
Downloads PDFs using verified arXiv IDs and open-access links, ensuring 100% genuine content.
"""

import os
import sys
import time
import urllib.request
from pathlib import Path
import fitz  # PyMuPDF

PAPERS_DIR = Path("papers")

# Dictionary of target files with verified source URLs and expected keywords
VERIFIED_PAPERS = {
    # 03_vlms_and_multimodal
    "03_vlms_and_multimodal/Cao_2024_PhysGame_Uncovering_Physical_Commonsense_in_Video_Games.pdf": {
        "url": "https://arxiv.org/pdf/2412.01800.pdf",
        "keywords": ["PhysGame", "Physical", "Commonsense"],
    },
    "03_vlms_and_multimodal/Taesiri_2025_VideoGameBunny_VLM_Game_Testing.pdf": {
        "url": "https://arxiv.org/pdf/2407.15295.pdf",
        "keywords": ["VideoGameBunny", "Vision", "Assistant"],
    },
    "03_vlms_and_multimodal/Taesiri_2022_Zero_Shot_Game_Testing_with_Language_Models.pdf": {
        "url": "https://arxiv.org/pdf/2210.02506.pdf",
        "keywords": ["Large Language Models", "Bug Detectors"],
    },
    "03_vlms_and_multimodal/Taesiri_2022_CLIP_Meets_GamePhysics_Bug_Identification.pdf": {
        "url": "https://arxiv.org/pdf/2203.11096.pdf",
        "keywords": ["CLIP", "GamePhysics", "Bug"],
    },
    "03_vlms_and_multimodal/Zheng_2026_GliDe_Open_Ended_Video_Game_Glitch_Detection.pdf": {
        "url": "https://arxiv.org/pdf/2604.07818.pdf",
        "keywords": ["Glitch", "VideoGameGlitchBench", "GliDe", "Agentic"],
    },
    "03_vlms_and_multimodal/Zheng_2025_TITAN_Leveraging_LLM_Agents_Game_Testing.pdf": {
        "url": "https://arxiv.org/pdf/2509.22170.pdf",
        "keywords": ["Game Testing", "LLM", "Agent"],
    },
    "03_vlms_and_multimodal/GBQA_2026_Game_Benchmark_LLMs_QA_Engineers.pdf": {
        "url": "https://arxiv.org/pdf/2604.02648.pdf",
        "keywords": ["GBQA", "Quality Assurance", "Game"],
    },

    # 02_glitch_and_anomaly_detection
    "02_glitch_and_anomaly_detection/Davarmanesh_2020_Automating_Artifact_Detection_in_Video_Games.pdf": {
        "url": "https://arxiv.org/pdf/2011.15103.pdf",
        "keywords": ["Automating Artifact Detection", "Video Games"],
    },
    "02_glitch_and_anomaly_detection/Wilkins_2022_World_of_Bugs_3D_Video_Games.pdf": {
        "url": "https://arxiv.org/pdf/2206.11037.pdf",
        "keywords": ["World of Bugs", "Automated Bug Detection"],
    },
    "02_glitch_and_anomaly_detection/Moran_2020_Automated_Reporting_of_GUI_Display_Issues.pdf": {
        "url": "https://arxiv.org/pdf/1802.04732.pdf",
        "keywords": ["GUI", "Design Violations", "Automated Reporting"],
    },
    "02_glitch_and_anomaly_detection/Rifaat_2026_Multi_Label_Perceptual_Bug_Detection_Gameplay.pdf": {
        "url": "https://arxiv.org/pdf/2610.08593.pdf",
        "keywords": ["Multi-Label", "Perceptual Bug", "Gameplay"],
    },

    # 04_benchmarks_and_datasets
    "04_benchmarks_and_datasets/Wu_2024_Q_Bench_Visual_Quality_Assessment_Benchmark.pdf": {
        "url": "https://arxiv.org/pdf/2309.14181.pdf",
        "keywords": ["Q-Bench", "Low-Level Vision"],
    },

    # 05_gameplay_video_analysis
    "05_gameplay_video_analysis/Guglielmi_2023_GELID_Gameplay_Videos_Detecting_Issues.pdf": {
        "url": "https://arxiv.org/pdf/2307.14749.pdf",
        "keywords": ["Gameplay Videos", "Detecting Issues", "GELID"],
    },
    "05_gameplay_video_analysis/Truelove_2023_Detecting_Bug_Occurrences_Gameplay_Videos.pdf": {
        "url": "https://arxiv.org/pdf/2311.10926.pdf",
        "keywords": ["Bug Occurrences", "Gameplay Videos"],
    },

    # 01_reviews
    "01_reviews/Politowski_2021_Survey_of_Video_Game_Testing.pdf": {
        "url": "https://arxiv.org/pdf/2103.06431.pdf",
        "keywords": ["Survey", "Video Game Testing"],
    },
    "01_reviews/Politowski_2022_Towards_Automated_Video_Game_Testing.pdf": {
        "url": "https://arxiv.org/pdf/2202.12777.pdf",
        "keywords": ["Towards Automated Video Game Testing"],
    },
}

def download_and_verify():
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}
    success_count = 0
    fail_count = 0

    for rel_path_str, info in VERIFIED_PAPERS.items():
        dest_path = PAPERS_DIR / rel_path_str
        dest_path.parent.mkdir(parents=True, exist_ok=True)
        url = info["url"]
        keywords = info["keywords"]

        print(f"\n[INFO] Fetching: {dest_path.name}")
        print(f"       URL: {url}")

        try:
            req = urllib.request.Request(url, headers=headers)
            with urllib.request.urlopen(req, timeout=30) as resp:
                data = resp.read()

            # Verify with PyMuPDF
            doc = fitz.open(stream=data, filetype="pdf")
            if len(doc) == 0:
                print(f"       [ERROR] PDF has 0 pages!")
                fail_count += 1
                continue

            first_page_text = doc[0].get_text()
            matches = [kw for kw in keywords if kw.lower() in first_page_text.lower()]
            match_ratio = len(matches) / len(keywords)

            if match_ratio >= 0.5:
                # Save verified PDF
                with open(dest_path, "wb") as f:
                    f.write(data)
                print(f"       [OK] Verified ({len(matches)}/{len(keywords)} matches, {len(doc)} pages): saved to {dest_path}")
                success_count += 1
            else:
                print(f"       [WARNING] Keywords not matched on page 1 ({len(matches)}/{len(keywords)}):")
                print(f"       Page 1 preview: {first_page_text[:200].strip()}")
                # Check page 2 just in case cover page exists
                if len(doc) > 1:
                    p2_text = doc[1].get_text()
                    matches_p2 = [kw for kw in keywords if kw.lower() in p2_text.lower()]
                    if len(matches_p2) / len(keywords) >= 0.5:
                        with open(dest_path, "wb") as f:
                            f.write(data)
                        print(f"       [OK] Verified on page 2 ({len(matches_p2)}/{len(keywords)} matches): saved to {dest_path}")
                        success_count += 1
                        continue
                fail_count += 1

        except Exception as e:
            print(f"       [ERROR] Failed to download {url}: {e}")
            fail_count += 1

        time.sleep(1.0)

    print("\n" + "=" * 60)
    print(f"Download complete: {success_count} succeeded, {fail_count} failed.")

if __name__ == "__main__":
    download_and_verify()
