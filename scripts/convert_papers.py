#!/usr/bin/env python3
"""
Automated Literature Ingestion Pipeline for Video Game Visual Testing Research
Converts raw academic PDF papers into structured, provenance-rich Markdown using academic-pdf2md (PyMuPDF4LLM + RapidOCR / Marker).

Usage:
    # Convert all PDFs in papers/ directory:
    python scripts/convert_papers.py

    # Using uv:
    uv run scripts/convert_papers.py

    # Convert a specific PDF:
    python scripts/convert_papers.py --file papers/04_benchmarks_and_datasets/Taesiri_2025_VideoGameQA_Bench.pdf

    # Choose engine (fast or marker):
    python scripts/convert_papers.py --engine fast
"""

from __future__ import annotations

import argparse
import json
import logging
import os
import re
import shutil
import subprocess
import sys
from dataclasses import dataclass
from datetime import datetime, timezone
from hashlib import sha256
from pathlib import Path
from typing import Optional

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s] [%(levelname)s] %(message)s",
    datefmt="%H:%M:%S",
)
logger = logging.getLogger("convert_papers")

FILENAME_PATTERN = re.compile(
    r"^(?P<author>[^_]+)_(?P<year>(?:19|20)\d{2})_(?P<title>.+)$"
)


@dataclass
class PaperMetadata:
    source_path: str
    output_path: str
    title: str
    author: Optional[str]
    year: Optional[str]
    sha256_hash: str
    converted_at: str
    converter_engine: str
    char_count: int
    figures_count: int
    status: str = "success"
    error_message: Optional[str] = None


def sanitize_filename_text(value: str) -> str:
    """Turn underscore-delimited filename into human-readable text."""
    return re.sub(r"\s+", " ", value.replace("_", " ")).strip()


def infer_metadata_from_path(path: Path) -> tuple[Optional[str], Optional[str], str]:
    """Extract (author, year, title) from Author_Year_Title.pdf naming scheme."""
    match = FILENAME_PATTERN.fullmatch(path.stem)
    if match:
        author = sanitize_filename_text(match.group("author"))
        year = match.group("year")
        title = sanitize_filename_text(match.group("title"))
        return author, year, title
    return None, None, sanitize_filename_text(path.stem)


def compute_sha256(path: Path) -> str:
    """Compute SHA-256 hash in streaming chunks."""
    hasher = sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            hasher.update(chunk)
    return hasher.hexdigest()


def convert_with_academic_pdf2md(
    pdf_path: Path,
    output_folder: Path,
    engine: str = "fast",
) -> tuple[Path, int]:
    """
    Invoke academic-pdf2md to convert PDF to Markdown.
    Returns (md_file_path, extracted_images_count).
    """
    cmd = [
        "academic-pdf2md",
        str(pdf_path.resolve()),
        "-o",
        str(output_folder.resolve()),
        "-e",
        engine,
    ]
    logger.info(f"Invoking: {' '.join(cmd)}")
    result = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", errors="replace")
    if result.returncode != 0:
        raise RuntimeError(f"academic-pdf2md failed (code {result.returncode}): {result.stderr or result.stdout}")

    paper_stem = pdf_path.stem
    paper_dir = output_folder / paper_stem
    md_file = paper_dir / f"{paper_stem}.md"
    images_dir = paper_dir / "images"

    if not md_file.exists():
        # Fallback check directly under output_folder
        alt_md = output_folder / f"{paper_stem}.md"
        if alt_md.exists():
            md_file = alt_md

    img_count = len(list(images_dir.glob("*.png"))) if images_dir.exists() else 0

    # Ensure all image links in markdown are normalized to relative 'images/...'
    if md_file.exists():
        content = md_file.read_text(encoding="utf-8", errors="replace")
        norm_content = re.sub(r'!\[(.*?)\]\([^)]*?/images/([^)]+)\)', r'![\1](images/\2)', content)
        if norm_content != content:
            md_file.write_text(norm_content, encoding="utf-8")

    return md_file, img_count


def convert_single_pdf(
    pdf_path: Path,
    papers_dir: Path,
    output_dir: Path,
    engine: str = "fast",
    overwrite: bool = False,
) -> PaperMetadata:
    """Convert one PDF file to Markdown preserving category directory hierarchy."""
    rel_path = pdf_path.relative_to(papers_dir)
    category_dir = output_dir / rel_path.parent
    paper_dir = category_dir / pdf_path.stem
    target_md_path = paper_dir / f"{pdf_path.stem}.md"

    author, year, title = infer_metadata_from_path(pdf_path)
    file_hash = compute_sha256(pdf_path)
    timestamp = datetime.now(timezone.utc).isoformat()

    if target_md_path.exists() and not overwrite:
        logger.info(f"Skipping existing: {target_md_path}")
        existing_text = target_md_path.read_text(encoding="utf-8", errors="ignore")
        images_dir = paper_dir / "images"
        img_count = len(list(images_dir.glob("*.png"))) if images_dir.exists() else 0
        return PaperMetadata(
            source_path=rel_path.as_posix(),
            output_path=target_md_path.relative_to(output_dir).as_posix(),
            title=title,
            author=author,
            year=year,
            sha256_hash=file_hash,
            converted_at=timestamp,
            converter_engine=f"academic-pdf2md ({engine})",
            char_count=len(existing_text),
            figures_count=img_count,
            status="skipped",
        )

    logger.info(f"Converting: {rel_path.as_posix()} via academic-pdf2md...")
    try:
        md_file, img_count = convert_with_academic_pdf2md(pdf_path, category_dir, engine=engine)
        char_count = len(md_file.read_text(encoding="utf-8", errors="ignore")) if md_file.exists() else 0

        return PaperMetadata(
            source_path=rel_path.as_posix(),
            output_path=md_file.relative_to(output_dir).as_posix(),
            title=title,
            author=author,
            year=year,
            sha256_hash=file_hash,
            converted_at=timestamp,
            converter_engine=f"academic-pdf2md ({engine})",
            char_count=char_count,
            figures_count=img_count,
            status="success",
        )
    except Exception as exc:
        logger.error(f"Failed to convert {pdf_path}: {exc}")
        return PaperMetadata(
            source_path=rel_path.as_posix(),
            output_path="",
            title=title,
            author=author,
            year=year,
            sha256_hash=file_hash,
            converted_at=timestamp,
            converter_engine=f"academic-pdf2md ({engine})",
            char_count=0,
            figures_count=0,
            status="error",
            error_message=str(exc),
        )


def generate_index_markdown(records: list[PaperMetadata], output_dir: Path) -> None:
    """Generate or update markdown/INDEX.md with all converted papers."""
    index_file = output_dir / "INDEX.md"
    logger.info(f"Generating master index at: {index_file}")

    total = len(records)
    successful = sum(1 for r in records if r.status in ("success", "skipped"))
    failed = total - successful
    total_figs = sum(r.figures_count for r in records if r.status in ("success", "skipped"))

    lines = [
        "# Research Paper Academic Markdown Index",
        "",
        "This repository contains full-text academic papers converted from PDF to high-fidelity Markdown using **`academic-pdf2md`** (PyMuPDF4LLM + RapidOCR layout analysis) for the systematic mapping study on **AI-Based Visual Bug Detection in Video Games**.",
        "",
        f"- **Total tracked papers:** {total}",
        f"- **Successfully processed:** {successful}",
        f"- **Total extracted figure assets:** {total_figs}",
        f"- **Failed:** {failed}",
        f"- **Last Index Update:** {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')}",
        "",
        "## Papers Catalog",
        "",
        "| Year | First Author / Group | Title | Converted Markdown | Figures | Engine | Status |",
        "|---|---|---|---|---|---|---|",
    ]

    sorted_records = sorted(
        records,
        key=lambda r: (r.year or "0000", r.title.lower()),
        reverse=True,
    )

    for r in sorted_records:
        year_str = r.year or "Unknown"
        author_str = r.author or "N/A"
        title_str = r.title
        md_link = f"[{Path(r.output_path).name}]({r.output_path})" if r.output_path else "Failed"
        lines.append(
            f"| {year_str} | {author_str} | {title_str} | {md_link} | {r.figures_count} imgs | {r.converter_engine} | {r.status} |"
        )

    lines.append("")
    lines.append("---")
    lines.append("*Generated automatically by `scripts/convert_papers.py` using `academic-pdf2md`.*")

    index_file.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Convert research PDFs into clean Markdown using academic-pdf2md."
    )
    parser.add_argument(
        "--papers-dir",
        type=Path,
        default=Path("papers"),
        help="Root directory containing raw PDF papers (default: papers/)",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=Path("markdown"),
        help="Directory to save converted Markdown files (default: markdown/)",
    )
    parser.add_argument(
        "--engine",
        type=str,
        choices=["fast", "marker"],
        default="fast",
        help="academic-pdf2md engine (fast or marker, default: fast)",
    )
    parser.add_argument(
        "--file",
        type=Path,
        default=None,
        help="Path to a single PDF to convert",
    )
    parser.add_argument(
        "--overwrite",
        action="store_true",
        help="Force re-conversion and overwrite existing markdown files",
    )
    parser.add_argument(
        "--no-index",
        action="store_true",
        help="Skip updating markdown/INDEX.md",
    )
    args = parser.parse_args()

    args.output_dir.mkdir(parents=True, exist_ok=True)
    records: list[PaperMetadata] = []

    if args.file:
        if not args.file.exists():
            logger.error(f"Specified file not found: {args.file}")
            sys.exit(1)
        res = convert_single_pdf(
            args.file,
            args.papers_dir if args.file.is_relative_to(args.papers_dir) else args.file.parent,
            args.output_dir,
            engine=args.engine,
            overwrite=args.overwrite,
        )
        records.append(res)
    else:
        pdf_files = sorted(args.papers_dir.rglob("*.pdf"))
        logger.info(f"Found {len(pdf_files)} PDF files in {args.papers_dir}")

        for pdf_path in pdf_files:
            res = convert_single_pdf(
                pdf_path,
                args.papers_dir,
                args.output_dir,
                engine=args.engine,
                overwrite=args.overwrite,
            )
            records.append(res)

    if not args.no_index and records:
        generate_index_markdown(records, args.output_dir)

    logger.info("academic-pdf2md batch pipeline execution completed.")


if __name__ == "__main__":
    main()
