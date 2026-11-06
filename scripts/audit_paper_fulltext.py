#!/usr/bin/env python3
"""
Full-Text Paper and Markdown Audit:
Checks all 51 references in manuscript/references.bib:
- Checks if local PDF exists in papers/
- Checks if Markdown full-text exists in markdown/
- Extracts verified arXiv IDs, DOIs, and direct download links for missing papers
"""

import re
import csv
from pathlib import Path

def audit_fulltext():
    bib_text = Path("manuscript/references.bib").read_text(encoding="utf-8")
    entries = re.findall(r'@\w+\s*\{\s*([^,]+),([^@]*?)(?=\n@|\Z)', bib_text, re.DOTALL)
    
    local_pdfs = list(Path("papers").rglob("*.pdf"))
    local_mds = list(Path("markdown").rglob("*.md"))
    
    # Exclude meta markdown files
    content_mds = [p for p in local_mds if p.name not in ["README.md", "INDEX.md"]]
    
    print(f"Total Reference Entries in references.bib: {len(entries)}")
    print(f"Total Local PDFs: {len(local_pdfs)}")
    print(f"Total Local Full-Text Markdown Conversions: {len(content_mds)}")
    print("=" * 80)
    
    results = []
    
    for key, body in entries:
        title_m = re.search(r'title\s*=\s*[\{"](.*?)[}"]', body, re.I | re.DOTALL)
        year_m = re.search(r'year\s*=\s*[\{"]?(\d+)[\}"]?', body, re.I)
        doi_m = re.search(r'doi\s*=\s*[\{"](.*?)[}"]', body, re.I)
        url_m = re.search(r'url\s*=\s*[\{"](.*?)[}"]', body, re.I)
        eprint_m = re.search(r'eprint\s*=\s*[\{"](.*?)[}"]', body, re.I)
        
        title = clean_text(title_m.group(1)) if title_m else ""
        year = year_m.group(1) if year_m else ""
        doi = doi_m.group(1) if doi_m else ""
        url = url_m.group(1) if url_m else ""
        eprint = eprint_m.group(1) if eprint_m else ""
        
        # Check matching PDF
        found_pdf = None
        key_stem = key.lower()
        title_keywords = [w.lower() for w in re.findall(r'\b[a-zA-Z]{4,}\b', title)[:4]]
        
        for pdf in local_pdfs:
            pdf_name = pdf.name.lower()
            if any(k in pdf_name for k in title_keywords if len(k) > 4):
                found_pdf = pdf
                break
                
        # Check matching Markdown
        found_md = None
        for md in content_mds:
            md_name = md.name.lower()
            if any(k in md_name for k in title_keywords if len(k) > 4):
                found_md = md
                break
                
        results.append({
            "key": key,
            "title": title,
            "year": year,
            "doi": doi,
            "url": url,
            "eprint": eprint,
            "pdf": str(found_pdf) if found_pdf else None,
            "md": str(found_md) if found_md else None
        })
        
    have_pdf = [r for r in results if r["pdf"]]
    missing_pdf = [r for r in results if not r["pdf"]]
    have_md = [r for r in results if r["md"]]
    missing_md = [r for r in results if not r["md"]]
    
    print(f"Papers WITH local PDF: {len(have_pdf)} / {len(results)}")
    print(f"Papers WITH Markdown full-text: {len(have_md)} / {len(results)}")
    print(f"Papers MISSING PDF & Markdown: {len(missing_pdf)} / {len(results)}")
    print("=" * 80)
    
    print("\nSample of Papers with Markdown Full-Text ready for deep reading:")
    for r in have_md[:8]:
        print(f"  [OK] {r['key']:<28} -> {Path(r['md']).name}")
        
    print("\nSample of Missing Papers to Harvest, Download & Convert:")
    for r in missing_pdf[:15]:
        link = r['doi'] or r['url'] or r['eprint']
        print(f"  [NEED] {r['key']:<26} ({r['year']}) : {r['title'][:40]}... -> Link: {link}")
        
    return results

def clean_text(text):
    text = re.sub(r'\s+', ' ', text)
    text = text.replace('{', '').replace('}', '').replace('\\&', '&').strip()
    return text

if __name__ == "__main__":
    audit_fulltext()
