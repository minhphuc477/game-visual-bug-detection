#!/usr/bin/env python3
"""
Automated Literature Ingestion Pipeline for Video Game Visual Testing Research
Converts raw academic PDF papers into structured, provenance-rich Markdown using Microsoft MarkItDown.

Usage:
    # Convert all PDFs in papers/ directory:
    python scripts/convert_papers.py

    # Using uv (no prior environment setup needed):
    uv run scripts/convert_papers.py

    # Convert a specific PDF:
    python scripts/convert_papers.py --file papers/04_benchmarks_and_datasets/VideoGameQA_Bench_2025.pdf

    # Overwrite existing markdown files:
    python scripts/convert_papers.py --overwrite
"""

from __future__ import annotations

import argparse
import json
import logging
import re
import sys
from dataclasses import asdict, dataclass
from datetime import datetime, timezone
from hashlib import sha256
from pathlib import Path
from typing import Optional

try:
    from markitdown import MarkItDown
    import importlib.metadata
    MARKITDOWN_VERSION = importlib.metadata.version("markitdown")
except ImportError:
    print("[ERROR] 'markitdown' is not installed.")
    print("Install via: pip install 'markitdown[pdf]>=0.1.6' or run using: uv run scripts/convert_papers.py")
    sys.exit(1)

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
    markitdown_version: str
    char_count: int
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
    
    # Fallback to cleaning stem
    return None, None, sanitize_filename_text(path.stem)


def compute_sha256(path: Path) -> str:
    """Compute SHA-256 hash in streaming chunks."""
    hasher = sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            hasher.update(chunk)
    return hasher.hexdigest()


def render_markdown_with_frontmatter(metadata: PaperMetadata, content: str) -> str:
    """Wrap converted text with standard YAML frontmatter."""
    header_dict = {
        "title": metadata.title,
        "author": metadata.author,
        "year": metadata.year,
        "source_file": metadata.source_path,
        "source_sha256": metadata.sha256_hash,
        "converted_at": metadata.converted_at,
        "markitdown_version": metadata.markitdown_version,
        "char_count": metadata.char_count,
    }
    
    lines = ["---"]
    for k, v in header_dict.items():
        if v is not None:
            lines.append(f"{k}: {json.dumps(v, ensure_ascii=False)}")
    lines.append("---\n")
    return "\n".join(lines) + content


def convert_single_pdf(
    pdf_path: Path,
    papers_dir: Path,
    output_dir: Path,
    converter: MarkItDown,
    overwrite: bool = False,
) -> PaperMetadata:
    """Convert one PDF file to Markdown using MarkItDown."""
    rel_path = pdf_path.relative_to(papers_dir)
    target_md_path = output_dir / rel_path.with_suffix(".md")
    target_md_path.parent.mkdir(parents=True, exist_ok=True)

    author, year, title = infer_metadata_from_path(pdf_path)
    file_hash = compute_sha256(pdf_path)
    timestamp = datetime.now(timezone.utc).isoformat()

    if target_md_path.exists() and not overwrite:
        logger.info(f"Skipping existing: {target_md_path.name}")
        existing_text = target_md_path.read_text(encoding="utf-8", errors="ignore")
        return PaperMetadata(
            source_path=rel_path.as_posix(),
            output_path=target_md_path.relative_to(output_dir).as_posix(),
            title=title,
            author=author,
            year=year,
            sha256_hash=file_hash,
            converted_at=timestamp,
            markitdown_version=MARKITDOWN_VERSION,
            char_count=len(existing_text),
            status="skipped",
        )

    logger.info(f"Converting: {rel_path.as_posix()} -> {target_md_path.name}")
    try:
        conversion_result = converter.convert_local(pdf_path)
        markdown_text = conversion_result.markdown

        metadata = PaperMetadata(
            source_path=rel_path.as_posix(),
            output_path=target_md_path.relative_to(output_dir).as_posix(),
            title=title,
            author=author,
            year=year,
            sha256_hash=file_hash,
            converted_at=timestamp,
            markitdown_version=MARKITDOWN_VERSION,
            char_count=len(markdown_text),
            status="success",
        )

        full_document = render_markdown_with_frontmatter(metadata, markdown_text)
        target_md_path.write_text(full_document, encoding="utf-8")
        return metadata

    except Exception as exc:
        logger.error(f"Failed to convert {pdf_path}: {exc}")
        return PaperMetadata(
            source_path=rel_path.as_posix(),
            output_path=target_md_path.relative_to(output_dir).as_posix(),
            title=title,
            author=author,
            year=year,
            sha256_hash=file_hash,
            converted_at=timestamp,
            markitdown_version=MARKITDOWN_VERSION,
            char_count=0,
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

    lines = [
        "# Research Paper Markdown Index",
        "",
        "This directory contains full-text academic papers converted from PDF to Markdown using Microsoft MarkItDown for the systematic mapping study on **AI-Based Visual Bug Detection in Video Games**.",
        "",
        f"- **Total tracked papers:** {total}",
        f"- **Successfully processed:** {successful}",
        f"- **Failed:** {failed}",
        f"- **Last Index Update:** {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')}",
        "",
        "## Papers Catalog",
        "",
        "| Year | First Author / Group | Title | Markdown Link | Source PDF | Status |",
        "|---|---|---|---|---|---|",
    ]

    # Sort primarily by year descending, then title
    sorted_records = sorted(
        records,
        key=lambda r: (r.year or "0000", r.title.lower()),
        reverse=True,
    )

    for r in sorted_records:
        year_str = r.year or "Unknown"
        author_str = r.author or "N/A"
        title_str = r.title
        md_link = f"[{r.output_path}]({r.output_path})" if r.status != "error" else "Failed"
        source_link = f"`{r.source_path}`"
        lines.append(
            f"| {year_str} | {author_str} | {title_str} | {md_link} | {source_link} | {r.status} |"
        )

    lines.append("")
    lines.append("---")
    lines.append("*Generated automatically by `scripts/convert_papers.py`.*")

    index_file.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Convert research PDFs into Markdown using Microsoft MarkItDown."
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

    converter = MarkItDown()
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
            converter,
            overwrite=args.overwrite,
        )
        records.append(res)
    else:
        # Batch convert all PDFs in papers_dir
        if not args.papers_dir.exists():
            logger.warning(f"Papers directory does not exist: {args.papers_dir}")
            args.papers_dir.mkdir(parents=True, exist_ok=True)

        pdf_files = sorted(args.papers_dir.rglob("*.pdf"))
        logger.info(f"Found {len(pdf_files)} PDF files in {args.papers_dir}")

        for pdf_path in pdf_files:
            res = convert_single_pdf(
                pdf_path,
                args.papers_dir,
                args.output_dir,
                converter,
                overwrite=args.overwrite,
            )
            records.append(res)

    if not args.no_index and records:
        generate_index_markdown(records, args.output_dir)

    logger.info("Batch conversion finished.")


if __name__ == "__main__":
    main()
