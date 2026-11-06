#!/usr/bin/env python3
"""Download exemplar systematic reviews and mapping studies into papers/reference_reviews/."""

import time
import urllib.request
from pathlib import Path

TARGETS = [
    {
        "url": "https://vciba.springeropen.com/track/pdf/10.1186/s42492-020-00057-7",
        "filename": "Xiong_2020_VCIBA_Systematic_Review_and_Meta_Analysis_AR_Games.pdf",
        "description": "VCIBA SpringerOpen: Systematic Review and Meta-Analysis of AR in Medicine, Retail, and Games (2020)",
    },
    {
        "url": "https://arxiv.org/pdf/2103.06431.pdf",
        "filename": "Politowski_2021_Survey_of_Video_Game_Testing_ACM_CSUR.pdf",
        "description": "ACM Computing Surveys: A Survey of Video Game Testing (Politowski et al., 2021)",
    },
    {
        "url": "https://arxiv.org/pdf/2301.03608.pdf",
        "filename": "Junior_2023_Automated_Testing_Video_Games_Systematic_Mapping.pdf",
        "description": "Systematic Mapping Study: Automated Testing of Video Games (Junior et al., 2023)",
    },
    {
        "url": "https://arxiv.org/pdf/2311.16439.pdf",
        "filename": "Ahmad_2023_Visual_Testing_of_Graphical_User_Interfaces_Survey.pdf",
        "description": "Survey: Visual Testing of Graphical User Interfaces with Computer Vision and Deep Learning (2023)",
    },
]

USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
OUTPUT_DIR = Path("papers/reference_reviews")


def download_target(target: dict):
    dest = OUTPUT_DIR / target["filename"]
    if dest.exists() and dest.stat().st_size > 10000:
        print(f"[EXISTS] {dest.name}")
        return

    print(f"[DOWNLOADING] {target['description']}")
    print(f"  URL: {target['url']}")
    dest.parent.mkdir(parents=True, exist_ok=True)

    req = urllib.request.Request(target["url"], headers={"User-Agent": USER_AGENT})
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            data = resp.read()
        with open(dest, "wb") as f:
            f.write(data)
        print(f"  [SUCCESS] Saved {dest.name} ({len(data)} bytes)\n")
    except Exception as exc:
        print(f"  [ERROR] Failed to download {target['filename']}: {exc}\n")
        if dest.exists():
            dest.unlink()


def main():
    for t in TARGETS:
        download_target(t)
        time.sleep(2.0)


if __name__ == "__main__":
    main()
