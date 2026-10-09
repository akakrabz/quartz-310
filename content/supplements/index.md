---
title: "Supplements"
description: "The course's own reference material, organised: a reading guide to the Singer & Munson notes, the notation translation table, the course summary sheet, the official transform tables (checked, with one misprint flagged) and a catalog of the Python demo notebooks."
tags: [supplement]
---

Reference material the course hands out alongside the lectures. None of it is required reading — the lecture pages are — but each page below says which parts matter for which lectures and links them to the lectures they support.

- [[supplements/singer-munson-notes|Singer & Munson notes — reading guide]] — the 321-page older course notes mapped section by section (with PDF page numbers) to Lectures 1–11; notation differences (LSI, unit pulse response, one-sided z-transform first) and what to skip. For Unit 3, its Chapter 2 (Fourier series, CTFT, DTFT) and Chapter 5 (frequency response) are the matching reading.
- [[supplements/notation-translation|Notation translation]] — the official table (lectures vs Singer & Munson vs four textbooks and the Kamalabadi videos) plus the Midterm 1 conventions that differ between lectures, exam keys and scipy.
- [[supplements/course-summary|Course summary sheet]] — the instructors' "ECE 310: Summary", with the parts for Units 1–2 (system properties, LSI and convolution, LCCDE, z-transform, stability, the pairs table) transcribed in full and the later parts (DTFT, frequency response, sampling, DFT) outlined.
- [[supplements/transform-tables|Official transform tables]] — Tables 9 and 10 (z-transform properties and pairs) typed and numerically verified — pair 3 is misprinted in the PDF — with the DTFT tables (Tables 5 and 6) folded below them for Unit 3.
- [[supplements/demo-notebooks|Course demo notebooks]] — what each of the eleven Jupyter notebooks shows, which lecture it belongs to (`demo_DTFT` and part of `demo_filtering` go with Unit 3), and how to run them.

> [!tip] Where to start
> For Units 1–2, read the [[supplements/course-summary|summary sheet]]'s pages 1–3 section and the corrected [[supplements/transform-tables|pairs table]]: together they are the course's own one-page view of that material, and a model for an exam sheet (check yours against the [[0-toolkit/05-errata|errata]] list). For [[3-fourier-analysis/index|Unit 3]], the DTFT tables on the transform-tables page pair with [[concepts/dtft-pairs|DTFT pairs]] and [[concepts/dtft-properties|DTFT properties]]; the course writes $X_d(\omega)$ where the tables write $X(e^{j\omega})$.

### Sources for this page

`suppliment/ECE310_notes_2019.pdf`, `suppliment/ece310_notation.pdf`, `suppliment/review.pdf`, `suppliment/transform_tables.pdf`, `ece310-demos-main/`.
