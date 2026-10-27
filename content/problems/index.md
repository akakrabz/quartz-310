---
title: "Problem families"
description: "Exam problem types distilled from past ECE 310 exams and homework, each with recipe, traps, past instances and practice: ten for Midterm 1 (plus T/F and property banks), eight for Midterm 2 (Units 3, 4 and 5)."
tags: [problem, exam]
---

*Problem families · 18 in all: 10 from past Midterm 1 exams (Units 1–2); 8 from past Midterm 2 exams: 3 (Unit 3), 2 (Unit 4), 3 (Unit 5)*

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
| [[problems/digital-filtering-of-analog-signals\|Digital filtering of analog signals: A/D → filter → D/A]] | $X_d$, $Y_d=H_dX_d$, $Y_a(\Omega)=T\,Y_d(\Omega T)$ at two $T$; $H_a(\Omega)=H_d(\Omega T)$; largest $T$, cutoff $\omega_c$ | 17, 18, 19 |

## Unit 5: the DFT

| family | what the exam asks | lectures |
|---|---|---|
| [[problems/dft-values-and-zero-padding\|DFT values and zero padding]] | $X[0]$, $X[N/2]$, one bin; $X[k]=X_d(\frac{2\pi k}{N})$; which padded bin equals $X[k]$; smallest $N$; inverse DFT; bins in hertz | 20 |
| [[problems/circular-convolution-and-dft-properties\|Circular convolution and DFT properties]] | $y[n]$ from a phase ramp or a rearranged $X[k]$; $Y[k]$ of a reversed, shifted $x$; linear vs circular convolution, $N\ge N_1+N_2-1$; conjugation, symmetry, Parseval | 21 |
| [[problems/dft-spectral-analysis\|DFT spectral analysis]] | DFT of a finite cosine (clean or leaky); amplitudes and frequencies from a plot; zero padding; lobe separation $N\gt\frac{4\pi}{\Delta\omega}$; rectangular vs Hamming | 22, 23 |

Per exam: [[exams/midterm-2/index|overview]] · [[exams/midterm-2/past-exams/index|past-exams map]] · [[exams/midterm-2/true-false-bank|T/F bank]].

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
Seven past Midterm 1 exams (FA2019–FA2025) and seven past Midterm 2 exams (FA2019–SP2025) with keys; Lectures 1–23 notes; Midterm 1 review lecture (Sep 28, 2026).
