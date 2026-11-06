#!/usr/bin/env python3
"""
Open Access Literature Discovery Script
Queries Semantic Scholar and OpenAlex APIs for open-access research papers
on Computer Vision and Vision-Language Models in Video Game Visual Testing.

Usage:
    python scripts/fetch_open_access_metadata.py
    uv run scripts/fetch_open_access_metadata.py --limit 20
"""

from __future__ import annotations

import argparse
import json
import logging
from pathlib import Path
import urllib.parse
import urllib.request

logging.basicConfig(level=logging.INFO, format="[%(asctime)s] %(levelname)s: %(message)s")
logger = logging.getLogger("fetch_oa")

SEARCH_QUERIES = [
    '"visual bug detection" "video games"',
    '"visual glitch detection" "video games"',
    '"visual regression testing" "video games"',
    '"visual anomaly detection" "gameplay"',
    'VideoGameQA-Bench',
    'TempGlitch gameplay video',
]


def search_semantic_scholar(query: str, limit: int = 10) -> list[dict]:
    """Search Semantic Scholar Graph API for academic publications."""
    base_url = "https://api.semanticscholar.org/graph/v1/paper/search"
    fields = "paperId,title,authors,year,venue,openAccessPdf,citationCount,abstract"
    params = {
        "query": query,
        "limit": limit,
        "fields": fields,
    }
    encoded_url = f"{base_url}?{urllib.parse.urlencode(params)}"
    logger.info(f"Querying Semantic Scholar for: {query}")
    req = urllib.request.Request(
        encoded_url,
        headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AcademicResearchBot/1.0"},
    )
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            return data.get("data", [])
    except Exception as exc:
        logger.warning(f"Error querying Semantic Scholar: {exc}")
        return []


def main() -> None:
    parser = argparse.ArgumentParser(description="Fetch open access paper metadata.")
    parser.add_argument("--limit", type=int, default=10, help="Max results per search query")
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("literature/discovered_open_access_papers.json"),
        help="Path to save discovered paper metadata",
    )
    args = parser.parse_args()

    discovered: dict[str, dict] = {}

    for q in SEARCH_QUERIES:
        results = search_semantic_scholar(q, limit=args.limit)
        for p in results:
            pid = p.get("paperId")
            if pid and pid not in discovered:
                discovered[pid] = p

    logger.info(f"Retrieved {len(discovered)} unique candidate papers.")
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(list(discovered.values()), indent=2, ensure_ascii=False), encoding="utf-8")
    logger.info(f"Saved candidate metadata to: {args.output}")


if __name__ == "__main__":
    main()
