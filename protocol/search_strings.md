# Tailored Database Search Strings

This document lists the exact syntax-adapted search queries for primary academic databases and indexing platforms.

---

## 1. IEEE Xplore
```text
(
  ("Document Title":"visual bug" OR "Document Title":"visual glitch" OR "Document Title":"visual defect" OR "Document Title":"visual anomaly" OR "Document Title":"visual regression" OR "Abstract":"visual bug" OR "Abstract":"visual glitch" OR "Abstract":"visual regression" OR "Abstract":"clipping detection")
  AND
  ("Document Title":"video game" OR "Document Title":"game testing" OR "Document Title":"gameplay" OR "Abstract":"video game" OR "Abstract":"game testing" OR "Abstract":"game quality assurance" OR "Abstract":"gameplay video")
  AND
  ("Abstract":"computer vision" OR "Abstract":"deep learning" OR "Abstract":"vision-language" OR "Abstract":"anomaly detection" OR "Abstract":"image processing")
)
```
*Filters: Conferences & Journals, Year Range: 2020 – 2026, Language: English.*

---

## 2. ACM Digital Library
```text
(Title:("visual bug" OR "visual glitch" OR "visual defect" OR "visual regression" OR "graphical anomaly") OR Abstract:("visual bug" OR "visual glitch" OR "visual defect" OR "visual regression" OR "clipping"))
AND
(Title:("video game" OR "game testing" OR "gameplay") OR Abstract:("video game" OR "game testing" OR "game quality assurance" OR "game engine"))
AND
Abstract:("computer vision" OR "deep learning" OR "vision-language" OR "convolutional" OR "transformer")
```
*Filters: ACM Conferences & Periodicals, Published: 01/01/2020 - 11/01/2026.*

---

## 3. Scopus
```text
TITLE-ABS-KEY (
  ( "visual bug*" OR "visual glitch*" OR "visual regression" OR "graphical anomal*" OR "rendering defect*" OR "clipping glitch*" )
  AND
  ( "video game*" OR "game testing" OR "game quality assurance" OR "gameplay video*" )
  AND
  ( "computer vision" OR "deep learning" OR "vision-language model*" OR "anomaly detection" OR "convolutional" OR "transformer" )
)
AND PUBYEAR > 2019
AND LANGUAGE ( english )
```

---

## 4. Web of Science (Core Collection)
```text
TS=(
  ("visual bug*" OR "visual glitch*" OR "visual regression" OR "graphical anomaly" OR "rendering defect*")
  AND
  ("video game*" OR "game testing" OR "game QA" OR "gameplay video*")
  AND
  ("computer vision" OR "deep learning" OR "vision-language" OR "anomaly detection")
)
Timespan: 2020-01-01 to 2026-11-01. Indexes: SCI-EXPANDED, SSCI, A&HCI, CPCI-S, ESCI.
```

---

## 5. arXiv (Search Query on API / OAI-PMH)
```text
cat:cs.CV OR cat:cs.SE OR cat:cs.AI
AND
all:("visual bug" OR "visual glitch" OR "game visual testing" OR "VideoGameQA" OR "TempGlitch")
AND submittedDate:[20200101 TO 20261106]
```

---

## 6. OpenAlex / Semantic Scholar API
- Semantic Scholar Keyword Endpoint:
  `https://api.semanticscholar.org/graph/v1/paper/search?query="visual+bug+detection"+game&year=2020-2026&fields=title,authors,year,venue,openAccessPdf`
- OpenAlex Concept Filter:
  `filter=concepts.id:C154945302(Computer science),concepts.id:C107457646(Video game),from_publication_date:2020-01-01`
