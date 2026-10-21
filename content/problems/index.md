---
title: "Problem families"
description: "Exam problem types distilled from past ECE 310 exams and homework, each with recipe, traps, past instances and practice: ten for Midterm 1 (plus T/F and property banks), three for Unit 3, two for Unit 4."
tags: [problem, exam]
---

*Problem families · 10 from past Midterm 1 exams (Units 1–2), 3 (Unit 3) and 2 (Unit 4) from past Midterm 2 exams*

Each page: **what it looks like on the exam** (every past instance, folded answers) → `recipe` (method, ending with checks) → `trap` → **practice problems** (new numbers, folded solutions) → related pages. Learn a family after its lectures.

## Units 1–2: Midterm 1

| family | what the exam asks | past MT1 | points | lectures |
|---|---|---|---|---|
| [[exams/midterm-1/true-false-bank\|True/False bank]] | 5–10 statements (SP2023, SP2025: −1 if wrong) | 7/7 | 10–12 | 3, 4, 9, 10, 11 |
| [[problems/classifying-system-properties\|Classifying system properties]] | L, TI, C, S for three systems | 7/7 | 12 | 3, 4 |
| [[exams/midterm-1/system-property-bank\|System-property bank]] | every past table system, reason per cell | 7/7 | 12 | 3, 4 |
| [[problems/finite-length-convolution\|Finite-length convolution]] | $x*h$ of two short lists, $n=0$ marked | 7/7 | 5–10 | 4 |
| [[problems/infinite-length-convolution\|Infinite-length convolution]] | exponential * exponential, finite * infinite | 5/7 | 5–8 | 4, 7 |
| [[problems/finding-h-from-input-output-pairs\|Finding h (or H) from input–output pairs]] | deconvolve, build $\delta$, step response, $H=Y/X$ | 7/7 | 5–15 | 4, 8, 9 |
| [[problems/z-transform-with-roc\|z-transform with ROC]] | $X(z)$ and ROC of three signals | 6/7 | 9–18 | 6, 7 |
| [[problems/all-possible-rocs\|All possible ROCs (inverse z by PFE)]] | every ROC and its $h[n]$; causal or stable one | 7/7 | 15–20 | 7, 8, 10, 11 |
| [[problems/lccde-to-transfer-function-and-response\|LCCDE ⇄ transfer function ⇄ response]] | LCCDE ↔ $H(z)$, poles, zeros, ROC, output | 7/7 | 15–20 | 5, 9, 10, 11 |
| [[problems/unbounded-outputs-and-pole-matching\|Unbounded outputs and pole matching]] | bounded inputs with unbounded outputs; cancellation | 7/7 | 6–10 | 4, 9, 10, 11 |
| [[problems/parameters-for-stability\|Parameters for stability]] | parameter values for stability | 3/7 | 6–10 | 9, 11 |
| [[problems/two-sided-systems-as-recursions\|Two-sided systems as recursions]] | run a non-causal part backwards | 2/7 | 5–8 | 5, 9, 10, 11 |

Per exam: [[exams/midterm-1/index|review guide]] · [[exams/midterm-1/past-exams/index|past-exams map]].

## Unit 3: DTFT and frequency response

| family | what the exam asks | lectures |
|---|---|---|
| [[problems/dtft-and-inverse-dtft\|Computing DTFTs and inverse DTFTs]] | DTFT from definition or pairs; inverse from a formula or sketch; $X_d(0)$, $X_d(\pi)$, $\int\lvert X_d\rvert^2\,d\omega$ without the transform | 13, 14 |
| [[problems/lti-response-to-sinusoids\|LTI response to sinusoids and periodic inputs]] | output of $h[n]$, an LCCDE or $H_d(\omega)$ for sums of sinusoids, one frequency at a time | 15 |
| [[problems/magnitude-phase-and-group-delay\|Magnitude, phase and group delay]] | real amplitude × linear phase; sketches with jumps; group delay | 16 |

## Unit 4: sampling

| family | what the exam asks | lectures |
|---|---|---|
| [[problems/sampling-and-the-nyquist-rate\|Sampling and the Nyquist rate]] | Nyquist rate or period; sketch $X_d(\omega)$ at a given $T$; consistent sampling periods; ideal D/A output | 17, 18, 19 |
| [[problems/digital-filtering-of-analog-signals\|Digital filtering of analog signals: A/D → H_d → D/A]] | $X_d$, $Y_d=H_dX_d$, $Y_a(\Omega)=T\,Y_d(\Omega T)$ at two $T$; $H_a(\Omega)=H_d(\Omega T)$; largest $T$, cutoff $\omega_c$ | 17, 18, 19 |

Unit 5 ([[5-dft-and-fft/index|DFT]]): no family yet; DFT problems are on the [[exams/midterm-2/past-exams/index|past Midterm 2 exams]].

## Review order (Midterm 1 families)

Quick, certain points first; times = recipe + traps + one practice problem.
1. [[problems/classifying-system-properties|Property table]] (15 min)
2. [[problems/finite-length-convolution|Finite convolution]] (10) — both checks; keep the arrow.
3. [[problems/z-transform-with-roc|z-transform with ROC]] (20) — shift factor, left-sided sign, $0/\infty$.
4. [[problems/all-possible-rocs|All possible ROCs]] (25) — cover-up, ring-by-ring table.
5. [[problems/lccde-to-transfer-function-and-response|LCCDE ⇄ H(z)]] (25) — watch cancellations.
6. [[problems/unbounded-outputs-and-pole-matching|Pole matching]] (15) — poles of $Y=HX$.
7. [[problems/finding-h-from-input-output-pairs|Finding h]] (15) — five data shapes, one move each.
8. [[problems/infinite-length-convolution|Infinite convolution]] (15)
9. [[problems/parameters-for-stability|Parameters for stability]], [[problems/two-sided-systems-as-recursions|two-sided recursions]] (10 each)
10. [[exams/midterm-1/true-false-bank|T/F bank]] (10); [[exams/midterm-1/cheat-sheet|cheat sheet]].

Under two hours: 1, 2, 3, 5, 10. Drills: [[demos/practice-drills|practice drills]]; demos: [[demos/convolution-explorer|convolution]] · [[demos/pole-zero-and-roc-explorer|pole-zero and ROC]] · [[demos/difference-equation-simulator|difference equations]].

## Table view

Live table from each page's `family_frequency`, `typical_points`, `lectures` (*By lecture* view available).

![[problems/exam-problem-families.base]]

Key errors: [[0-toolkit/05-errata|errata]].

### Sources for this page
Seven past Midterm 1 exams (FA2019–FA2025) and seven past Midterm 2 exams (FA2019–SP2025) with keys; Lectures 1–19 notes; Midterm 1 review lecture (Sep 28, 2026).
