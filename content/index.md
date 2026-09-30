---
title: "ECE 310 · Digital Signal Processing"
description: "Teaching notes for ECE 310 (Digital Signal Processing, UIUC Fall 2026): lectures rewritten as narratives, a concept glossary that links everything, exam problem families with recipes, past exams and homework with folded solutions, and interactive demos — built for Midterm 1."
---

Notes for **ECE 310 — Digital Signal Processing** (University of Illinois, Fall 2026, Profs. Snyder and Kamalabadi), written to *teach* the material rather than to summarize it. The source material is the course itself — Prof. Snyder's lecture notes, the lecture slides with their in-class annotations, the homework and the past exams — digested and rewritten in one consistent notation, with the connections made explicit and every number checked.

> [!exam] Midterm 1 is today — Wednesday, September 30, 7:00–9:00 pm
> Lectures 1–11 and HW1–HW4 (no DTFT). Start here:
> - [[0-midterm-1/index|Survival guide]] — scope, format, how often each problem type appears, a plan for today, the fifteen traps, and the review lecture's problems with solutions
> - [[0-midterm-1/cheat-sheet|Cheat sheet]] — what to put on your one handwritten two-sided sheet
> - [[0-midterm-1/practice-drills|Practice drills]] — randomized, autograded convolution / z-transform / PFE drills
> - [[0-midterm-1/true-false-bank|True/False bank]] and [[0-midterm-1/system-property-bank|system-property bank]] — every T/F statement and every property-table system from seven past exams
> - [[0-midterm-1/past-exams/index|Past exams]] — FA2025, SP2025, FA2024, FA2023, SP2023, SP2021, FA2019, with folded solutions

> [!tip] How this site is organized — layers, one graph
> - **Lectures** (the spine, in course order) tell the story: motivation → definition → worked example → what goes wrong → what the exam does with it.
> - **Concepts** are the glossary hubs: one short page per idea (convolution, ROC, BIBO stability, …) with the key formula, the traps, and links to every lecture and problem that uses it.
> - **Problem families** are the exam recipes: each page is one kind of exam problem — how to recognise it, the procedure, the traps, and every past-exam instance.
> - **Past exams and homework** are the practice: every problem with its solution folded, so you can try first.
> - **Demos** are interactive: drag signals, poles and zeros, and watch convolutions, ROCs and difference equations respond.
>
> Hover any link for a preview; open the **graph view** (top right of every page) to see what connects to what; use **search** for any term. The [[0-midterm-1/concept-map.canvas|concept map]] lays the whole Midterm 1 story out on one canvas, and the problem-family table on [[problems/index|problem families]] maps every past-exam problem to its recipe.

## Course map

### [[0-toolkit/index|Toolkit]] — the mathematics assumed
[[0-toolkit/01-complex-numbers|Complex numbers]] · [[0-toolkit/02-geometric-series|Geometric series]] · [[0-toolkit/03-sketching-and-transforming-signals|Sketching and transforming signals]] · [[0-toolkit/04-factoring-and-long-division|Factoring and long division]] · [[0-toolkit/05-errata|Errata in the course materials]]

### [[1-signals-and-systems/index|Unit 1 · Signals and systems]] — Lectures 1–5 (Midterm 1)
1. [[1-signals-and-systems/01-digital-signals|Introduction to digital signals]]
2. [[1-signals-and-systems/02-complex-numbers-and-elementary-signals|Math preliminaries: complex numbers and elementary signals]]
3. [[1-signals-and-systems/03-system-properties|Discrete-time systems: linearity, time-invariance, causality, stability]]
4. [[1-signals-and-systems/04-impulse-response-and-convolution|The impulse response and convolution]]
5. [[1-signals-and-systems/05-difference-equations-and-block-diagrams|Difference equations and block diagrams]]

### [[2-z-transform/index|Unit 2 · The z-transform and LTI systems]] — Lectures 6–11 (Midterm 1)
6. [[2-z-transform/06-the-z-transform|The z-transform]]
7. [[2-z-transform/07-z-transform-properties|Properties of the z-transform]]
8. [[2-z-transform/08-inverse-z-transform|The inverse z-transform]]
9. [[2-z-transform/09-transfer-functions|Transfer functions and LTI system response, part 1]]
10. [[2-z-transform/10-improper-transfer-functions-and-system-algebra|Improper transfer functions and system algebra, part 2]]
11. [[2-z-transform/11-bibo-stability-and-causality|BIBO stability and causality]]

### [[3-beyond-midterm-1/index|Beyond Midterm 1]] — Lectures 12–14 (not on Midterm 1)
Convolution as template matching (not tested) · Fourier analysis: from Fourier series to the DTFT · DTFT properties — *outlined*

### Cross-cutting
[[concepts/index|Concept glossary]] · [[problems/index|Exam problem families]] · [[homework/index|Homework]] ([[homework/hw1|HW1]] · [[homework/hw2|HW2]] · [[homework/hw3|HW3]] · [[homework/hw4|HW4]]) · [[demos/index|Interactive demos]] · [[supplements/index|Supplements]] (course summary, transform tables, Singer & Munson notes, notation, demo notebooks)

## Conventions used throughout

| | this site writes | you may also see |
|---|---|---|
| signals | input $x[n]$, impulse response $h[n]$, output $y[n]$ — square brackets, integer $n$ | $\{x[n]\}$ for the whole sequence; $x(t)$ is continuous time |
| elementary signals | $\delta[n]$ (Kronecker delta, unit impulse), $u[n]$ (unit step) | "unit pulse response" for $h[n]$ on older exams |
| where $n = 0$ is | an up-arrow under that sample: $\{1,\ \underset{\uparrow}{2},\ 3\}$ means $x[0] = 2$ | a bold or underlined sample |
| convolution | $x[n]*h[n]$ | $(x*h)[n]$ on the exams and in the course summary |
| system class | LTI (linear time-invariant) | LSI (linear shift-invariant) on older exams — the same thing |
| z-transforms | in powers of $z^{-1}$: $\dfrac{1}{1-az^{-1}}$ | $\dfrac{z}{z-a}$ — the same function |
| region of convergence | always stated: "ROC: $\lvert z\rvert>a$" | |
| LCCDE (Lecture 9 form) | $y[n]+\sum_k a_k\,y[n-k] = \sum_k b_k\,x[n-k]$, $\;H(z) = \dfrac{\sum_k b_kz^{-k}}{1+\sum_k a_kz^{-k}}$ (= `lfilter(b, a)`) | Lecture 5: $y[n] = \sum_i b_i\,y[n-i]+\sum_j c_j\,x[n-j]$ — the feedback signs are flipped |
| partial fractions | $X(z) = \sum_k \dfrac{A_k}{1-p_kz^{-1}}$, $A_k$ by cover-up ($z = p_k$) | `residuez` returns the same $A_k$, $p_k$ |
| DTFT (after Midterm 1) | $X_d(\omega)$ | $X(e^{j\omega})$ in the textbook |

## Callouts

The notes use a few recurring boxes, so you can skim for what you need:

> [!key] Key
> The result to remember — e.g. an LTI system is BIBO stable if and only if the ROC of $H(z)$ contains the unit circle.

> [!recipe] Recipe
> A procedure, step by step — e.g. inverse z: factor, long-divide if improper, cover-up for each $A_k$, choose each term's direction from the ROC.

> [!trap] Trap
> A mistake that costs points — e.g. the left-sided pair is $-a^nu[-n-1] \leftrightarrow \dfrac{1}{1-az^{-1}}$, $\lvert z\rvert<\lvert a\rvert$, minus sign included. Several traps come from real exam keys.

> [!exam] Exam
> How the idea shows up on exams, citing term and problem — e.g. FA2025 #8b hides a pole at $e^{j2/3}$, not $e^{j2\pi/3}$.

> [!intuition] Intuition
> The picture behind the mathematics — e.g. convolution is a sum of shifted, scaled copies of $h[n]$, one per input sample.

> [!derivation]- Derivation (click to expand)
> Longer derivations are folded so the narrative stays readable. Expand when you want the details.

> [!question] Question
> A problem statement, taken from a past exam or homework — try it before opening the answer below it.

> [!success]- Answer (click to expand)
> Solutions are folded, so you can test yourself first. Every number in them was checked numerically.

*Status (September 30, 2026): everything in the Midterm 1 scope — Lectures 1–11, HW1–HW4 and seven past exams — is covered; Lectures 12–14 are outlined. Sources: C. Snyder, ECE 310 lecture notes and slides, Fall 2026 (with the annotated in-class slides and the Midterm 1 Review); homework HW1–HW4 with official solutions; past Midterm 1 exams FA2019–FA2025 with keys; the ECE 310 course summary and transform tables; A. C. Singer and D. C. Munson, ECE 310 course notes (2019).*

### Sources for this page

The course calendar and titles on the Fall 2026 lecture slides (Lectures 1–11, Aug 24 – Sep 18), the Midterm 1 exam instructions, and the notation supplement of the course (class vs. textbook notation).
