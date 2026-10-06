---
title: "Problem families"
description: "Each problem family is one kind of problem distilled from the past ECE 310 exams and the homework — how to recognise it, a recipe, the traps, every past instance and fresh practice problems: ten families (plus the True/False and property banks) for Units 1–2 and Midterm 1, three for Unit 3 from the past Midterm 2 exams."
tags: [problem, exam]
---

*Problem families · each one kind of problem distilled from the past exams and the homework · ten from the seven past Midterm 1 exams (Units 1–2), three from the past Midterm 2 exams (Unit 3) · each page: every past instance, a recipe, the traps, and 2–3 new practice problems with folded, Python-verified solutions*

The same few kinds of problem come back in the homework and on every exam, with new numbers. A **problem family** is one of those kinds, distilled from all its past instances: what it looks like, the method a strong student uses (a `recipe` box ending with the checks), the specific mistakes that cost points (a `trap` box), every past instance with its answer folded, and fresh practice problems. Learn a family after the lectures it rests on, as the bridge from understanding an idea to using it under time pressure. The numbers in the practice problems are new, so they are practice, not answer keys; the real exam problems are linked from each family page and worked in full on the exam pages.

Every past Midterm 1 is assembled from the same short list: True/False, the Linear / Time-invariant / Causal / Stable table, a convolution, z-transforms with ROC, an LCCDE / transfer-function problem, partial fractions with the right ROC, and a stability or unbounded-output question.

## Units 1–2: the Midterm 1 families

| family | what the exam asks | on past Midterm 1 exams | typical points | lectures |
|---|---|---|---|---|
| [[exams/midterm-1/true-false-bank\|True/False bank]] | 5–10 statements across the whole course (SP2023 and SP2025: −1 for a wrong answer) | 7 of 7 | 10–12 | 3, 4, 9, 10, 11 |
| [[problems/classifying-system-properties\|Classifying system properties]] | yes/no for L, TI, C, S on three systems, no proofs | 7 of 7 | 12 | 3, 4 |
| [[exams/midterm-1/system-property-bank\|System-property bank]] | every system ever asked in that table, with a reason per cell | 7 of 7 | 12 | 3, 4 |
| [[problems/finite-length-convolution\|Finite-length convolution]] | $x*h$ for two short lists with $n=0$ marked | 7 of 7 | 5–10 | 4 |
| [[problems/infinite-length-convolution\|Infinite-length convolution]] | exponential * exponential, or finite * infinite | 5 of 7 | 5–8 | 4, 7 |
| [[problems/finding-h-from-input-output-pairs\|Finding h (or H) from input–output pairs]] | deconvolve, build $\delta$ from inputs, step response, $H=Y/X$ | 7 of 7 | 5–15 | 4, 8, 9 |
| [[problems/z-transform-with-roc\|z-transform with ROC]] | $X(z)$ and ROC for three awkward signals | 6 of 7 | 9–18 | 6, 7 |
| [[problems/all-possible-rocs\|All possible ROCs (inverse z by PFE)]] | every ROC and its $h[n]$; pick the causal or stable one | 7 of 7 | 15–20 | 7, 8, 10, 11 |
| [[problems/lccde-to-transfer-function-and-response\|LCCDE ⇄ transfer function ⇄ response]] | LCCDE ↔ $H(z)$, poles/zeros, ROC, output for a given input | 7 of 7 | 15–20 | 5, 9, 10, 11 |
| [[problems/unbounded-outputs-and-pole-matching\|Unbounded outputs and pole matching]] | which bounded inputs give unbounded outputs; cancellation | 7 of 7 | 6–10 | 4, 9, 10, 11 |
| [[problems/parameters-for-stability\|Parameters for stability]] | values of a parameter that make a system stable | 3 of 7 | 6–10 | 9, 11 |
| [[problems/two-sided-systems-as-recursions\|Two-sided systems as recursions]] | run a non-causal part of a stable system backwards | 2 of 7 | 5–8 | 5, 9, 10, 11 |

Where each family appeared, exam by exam, is tabulated on the [[exams/midterm-1/index|Midterm 1 review guide]] and problem by problem on the [[exams/midterm-1/past-exams/index|past-exams map]]. The typical Midterm 1: two hours, about 8 problems, 100 points, one handwritten two-sided sheet, no calculator.

## Unit 3: the DTFT and frequency-response families

Three families come from the past Midterm 2 exams and cover [[3-fourier-analysis/index|Unit 3]]; where each appeared is listed on its own page and on the [[exams/midterm-2/past-exams/index|past Midterm 2 exams]] map.

| family | what the exam asks | lectures |
|---|---|---|
| [[problems/dtft-and-inverse-dtft\|Computing DTFTs and inverse DTFTs]] | a DTFT from the definition or the pairs; an inverse DTFT from a formula or a sketch; values such as $X_d(0)$, $X_d(\pi)$ or $\int\lvert X_d\rvert^2\,d\omega$ without computing the transform | 13, 14 |
| [[problems/lti-response-to-sinusoids\|LTI response to sinusoids and periodic inputs]] | the output of a system given by $h[n]$, an LCCDE or $H_d(\omega)$ for sums of sinusoids and complex exponentials, one frequency at a time | 15 |
| [[problems/magnitude-phase-and-group-delay\|Magnitude, phase and group delay]] | $H_d(\omega)$ as a real amplitude times a linear phase; sketches of $\lvert H_d\rvert$ and $\angle H_d$ with their jumps; the group delay | 16 |

The past Midterm 2 exams also test topics that come after Lecture 16 (ideal filters, sampling and reconstruction, the DFT and FFT). Those problems are typed with solutions on the exam pages; families for them will follow the lectures.

## A review order for the Midterm 1 families

For a review of Units 1–2 before an exam, ordered by points per minute of practice: quick, certain points first, then the long z-domain problems that carry the most weight, then the families that do not appear every time. Times are for reading the recipe and trap boxes and doing one practice problem without peeking.

1. **[[problems/classifying-system-properties|Property table]]** (15 min) — memorize the fast-rules table; do Practice 1. Twelve points you can bank in five minutes on the exam.
2. **[[problems/finite-length-convolution|Finite-length convolution]]** (10 min) — one problem, then both checks ($\sum y=\sum x\sum h$ and the alternating sum). Never lose the arrow.
3. **[[problems/z-transform-with-roc|z-transform with ROC]]** (20 min) — the shift factor, the left-sided sign, the finite-sequence $0/\infty$ rule. Write the ROC next to every transform.
4. **[[problems/all-possible-rocs|All possible ROCs]]** (25 min) — cover-up PFE and the ring-by-ring table of right/left-sided terms.
5. **[[problems/lccde-to-transfer-function-and-response|LCCDE ⇄ H(z) ⇄ response]]** (25 min) — the biggest single problem on most exams; watch pole–zero cancellations.
6. **[[problems/unbounded-outputs-and-pole-matching|Unbounded outputs and pole matching]]** (15 min) — list the poles of $Y=HX$; a unit-circle pole of $H$ is hit only by an input with the *same* pole.
7. **[[problems/finding-h-from-input-output-pairs|Finding h]]** (15 min) — the four moves: deconvolve, build $\delta$, difference a step response, divide $Y/X$.
8. **[[problems/infinite-length-convolution|Infinite-length convolution]]** (15 min) — step limits → geometric sum → keep the step factor; or unmask a finite sequence.
9. **[[problems/parameters-for-stability|Parameters for stability]]** and **[[problems/two-sided-systems-as-recursions|two-sided recursions]]** (10 min each) — only if time remains; both reuse steps 4–5.
10. **Last, as flashcards:** the [[exams/midterm-1/true-false-bank|True/False bank]] (10 min). The statements recycle every topic above, so this doubles as a final review; the [[exams/midterm-1/cheat-sheet|cheat sheet]] page says what to copy onto your sheet.

If you have less than two hours: steps 1, 2, 3, 5 and 10. For randomized, auto-graded versions of steps 1–4 use the [[demos/practice-drills|practice drills]]; for seeing the ideas move, the [[demos/convolution-explorer|convolution explorer]], [[demos/pole-zero-and-roc-explorer|pole–zero and ROC explorer]] and [[demos/difference-equation-simulator|difference-equation simulator]].

## Browse the families (Bases table)

The same list as a live table, generated from each page's properties (`family_frequency`, `typical_points`, `lectures`); switch to the *By lecture* view to see which families a lecture feeds.

![[problems/exam-problem-families.base]]

## How the family pages are built

Every page follows the same layout: **What it looks like on the exam** (the pattern and every past instance, linked, with folded answers) → a `recipe` box (the method a strong student uses, ending with the checks) → a `trap` box (the specific point-losers) → **Practice problems** (new numbers, exam difficulty, statement in a question box, full solution folded) → **Related** (lectures, concepts, demos). Every number was checked in Python (`np.convolve`, `scipy.signal.lfilter`, `residuez`, direct partial sums of $\sum x[n]z^{-n}$ inside the claimed ROC); where an official key is wrong, the page says so and the fix is listed on the [[0-toolkit/05-errata|errata]] page.

### Sources for this page

Problem-type counts and point values from the seven past Midterm 1 exams with solutions (FA2025, SP2025, FA2024, FA2023, SP2023, SP2021, FA2019); the Unit 3 families from the seven past Midterm 2 exams with keys (FA2019–SP2025); lecture mapping from the Lecture 1–16 notes; the review order follows the Midterm 1 review lecture (Sep 28, 2026), which walked through T/F, the property table, convolution, z-transforms, a transfer-function response and a stability problem in that order.
