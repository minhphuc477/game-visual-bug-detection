#!/usr/bin/env python3
"""
Systematic arXiv Search and Download Utility for Video Game Visual Testing Literature.
Adheres to arXiv API Rate Limits (1 request every 3 seconds).
"""

import os
import re
import time
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from pathlib import Path

QUERIES = [
    'all:"visual bug" AND (all:game OR all:"video game")',
    'all:"visual glitch" AND (all:game OR all:"video game")',
    'all:"visual regression" AND (all:game OR all:"video game")',
    'all:"visual testing" AND (all:game OR all:"video game")',
    'ti:"game testing" AND all:"computer vision"',
    'all:"gameplay" AND all:"anomaly detection"',
    'all:"VideoGameQA"',
]

USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AcademicResearchBot/1.0"
BASE_URL = "http://export.arxiv.org/api/query"
PAPERS_DIR = Path("papers")


def clean_title(title: str) -> str:
    """Normalize whitespace and remove invalid filename characters."""
    t = re.sub(r"\s+", " ", title).strip()
    return re.sub(r'[\\/*?:"<>|]', "", t)


def query_arxiv(query_str: str, max_results: int = 5) -> list[dict]:
    params = {
        "search_query": query_str,
        "start": 0,
        "max_results": max_results,
        "sortBy": "relevance",
        "sortOrder": "descending",
    }
    url = f"{BASE_URL}?{urllib.parse.urlencode(params)}"
    print(f"[SEARCH] Querying arXiv: {query_str}")
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})

    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            content = resp.read().decode("utf-8")
        
        root = ET.fromstring(content)
        ns = {"atom": "http://www.w3.org/2005/Atom"}
        papers = []

        for entry in root.findall("atom:entry", ns):
            arxiv_id = entry.find("atom:id", ns).text.strip()
            title = entry.find("atom:title", ns).text.strip()
            summary = entry.find("atom:summary", ns).text.strip()
            published = entry.find("atom:published", ns).text.strip()
            
            authors = []
            for author_node in entry.findall("atom:author", ns):
                name = author_node.find("atom:name", ns).text.strip()
                authors.append(name)
            
            pdf_url = None
            for link in entry.findall("atom:link", ns):
                if link.get("title") == "pdf" or link.get("type") == "application/pdf":
                    pdf_url = link.get("href")
            
            if not pdf_url and "abs" in arxiv_id:
                pdf_url = arxiv_id.replace("abs", "pdf") + ".pdf"

            papers.append({
                "id": arxiv_id.split("/abs/")[-1],
                "title": clean_title(title),
                "summary": re.sub(r"\s+", " ", summary),
                "year": published[:4],
                "authors": authors,
                "first_author": authors[0].split()[-1] if authors else "Unknown",
                "pdf_url": pdf_url,
            })

        return papers
    except Exception as exc:
        print(f"[ERROR] Failed searching query '{query_str}': {exc}")
        return []


def download_pdf(pdf_url: str, dest_path: Path) -> bool:
    if dest_path.exists():
        print(f"[EXISTS] {dest_path.name}")
        return True

    print(f"[DOWNLOAD] {pdf_url} -> {dest_path.name}")
    dest_path.parent.mkdir(parents=True, exist_ok=True)
    req = urllib.request.Request(pdf_url, headers={"User-Agent": USER_AGENT})
    try:
        with urllib.request.urlopen(req, timeout=30) as resp, open(dest_path, "wb") as out:
            out.write(resp.read())
        print(f"[SUCCESS] Downloaded: {dest_path.name}")
        return True
    except Exception as exc:
        print(f"[ERROR] Download failed: {exc}")
        if dest_path.exists():
            dest_path.unlink()
        return False


def main():
    seen_ids = set()
    all_papers = []

    for q in QUERIES:
        papers = query_arxiv(q, max_results=5)
        for p in papers:
            if p["id"] not in seen_ids:
                seen_ids.add(p["id"])
                all_papers.append(p)
        time.sleep(3.2)  # Respect arXiv 3-second rate limit

    print(f"\nDiscovered {len(all_papers)} unique papers from arXiv.")

    for p in all_papers:
        title_summary = (p["title"] + " " + p["summary"]).lower()
        if not ("game" in title_summary or "play" in title_summary or "graphic" in title_summary or "canvas" in title_summary):
            continue

        # Route to appropriate category folder
        if "benchmark" in title_summary or "dataset" in title_summary:
            folder = PAPERS_DIR / "04_benchmarks_and_datasets"
        elif "video" in title_summary or "temporal" in title_summary or "frame" in title_summary:
            folder = PAPERS_DIR / "05_gameplay_video_analysis"
        elif "language" in title_summary or "vlm" in title_summary or "multimodal" in title_summary:
            folder = PAPERS_DIR / "03_vlms_and_multimodal"
        elif "review" in title_summary or "survey" in title_summary or "mapping" in title_summary:
            folder = PAPERS_DIR / "01_reviews"
        else:
            folder = PAPERS_DIR / "02_glitch_and_anomaly_detection"

        safe_title = re.sub(r"[^A-Za-z0-9]+", "_", p["title"])[:50].strip("_")
        dest_filename = f"{p['first_author']}_{p['year']}_{safe_title}.pdf"
        dest_path = folder / dest_filename

        if p.get("pdf_url"):
            download_pdf(p["pdf_url"], dest_path)
            time.sleep(3.2)


if __name__ == "__main__":
    main()
