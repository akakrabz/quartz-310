---
title: "Homework"
description: "The four Midterm 1 homework sets (HW1–HW4) with due dates, lectures, topics and the exam skills each one trains, linked to verified walkthroughs; HW5 (DTFT) is outside the Midterm 1 scope."
tags: [homework, midterm-1]
---

*Homework · HW1–HW4 cover exactly the Midterm 1 scope ([[1-signals-and-systems/index|Unit 1]] and [[2-z-transform/index|Unit 2]], Lectures 1–11) · each walkthrough has the statement, a folded worked solution, traps, the official rubric's lessons, and the past-exam problems that reuse each idea · back to the [[0-midterm-1/index|Midterm 1 survival guide]]*

> [!abstract] How to use these pages
> Treat every problem as practice: read the statement, solve it on paper, then open the folded solution. Every answer was re-derived and checked numerically in Python; where an official solution slips, the page says so in a warning box and gives the corrected result. The **On the exam** line under each problem names the past midterm problems that reuse the idea, so a homework problem doubles as a pointer into the [[0-midterm-1/past-exams/index|past exams]].

## The four sets

| Set | Due (2026) | Lectures | Topics | Exam skills it trains | Walkthrough |
|---|---|---|---|---|---|
| HW1 | Fri Sep 4 | [[1-signals-and-systems/01-digital-signals\|L1]]–[[1-signals-and-systems/03-system-properties\|L3]] | stem plots of δ/u combinations; time reversal, shift and decimation; δ- and step-expressions of plotted signals; roots of $z^4 = \pm 1$; clipping and windowing systems | index bookkeeping (the flip-and-shift of convolution); complex roots, i.e. poles on the unit circle; property-table arguments | [[homework/hw1\|HW1 · signals, sketching, and system properties]] |
| HW2 | Fri Sep 11 | [[1-signals-and-systems/03-system-properties\|L3]]–[[1-signals-and-systems/05-difference-equations-and-block-diagrams\|L5]] | linearity and time invariance of recursions and time-varying gains; convolution ⇒ LSI; output from the step response; $h[n]$ from one input–output pair; five convolutions (one divergent) | property table; finding $h$; finite and infinite convolution; the sum check | [[homework/hw2\|HW2 · system properties, convolution, and the impulse response]] |
| HW3 | Fri Sep 18 | [[2-z-transform/06-the-z-transform\|L6]]–[[2-z-transform/09-transfer-functions\|L9]] | z-transforms with ROC (impulses, a shifted exponential, a two-sided sum, $(1/4)^{\lvert n\rvert}$, a finite-length sequence); transform properties (shift, scaling by $a^n$, modulation by a cosine, multiplication by $n$, convolution); inverse transforms for a given ROC; poles, zeros, ROC and $h[n]$ of a right-sided $H(z)$ | z-transform with ROC; inverse z-transform and PFE; pole-zero plots | [[homework/hw3\|HW3 · the z-transform, its properties, and its inverse]] |
| HW4 | Fri Sep 25 | [[2-z-transform/08-inverse-z-transform\|L8]]–[[2-z-transform/11-bibo-stability-and-causality\|L11]] | all possible ROCs and their inverses; proof that BIBO stability ⇔ absolutely summable $h$; stability of causal systems and bounded inputs with unbounded outputs; causal $h[n]$ from an input–output pair; stability of a cascade; LCCDE → $H(z)$, $h[n]$ and an output | all possible ROCs; stability tests; pole matching and cancellation; finding $h$; LCCDE ↔ $H(z)$ | [[homework/hw4\|HW4 · all possible ROCs, BIBO stability, and system algebra]] |

> [!note] HW5 is not on Midterm 1
> HW5 (due Sun Oct 4) is on the DTFT (Lectures 13–14), which is outside the Midterm 1 scope, as is Lecture 12 (template matching). A short outline of that material is in [[3-beyond-midterm-1/index|beyond Midterm 1]].

## Which homework problems practise which exam family

The exam counts are out of the seven past Midterm 1 exams (FA2025 back to FA2019); the family pages have the recipes.

| Exam problem family | On past exams | Homework practice |
|---|---|---|
| [[0-midterm-1/true-false-bank\|True/False]] | 7/7 | HW1 #4 (poles on the unit circle); HW2 #2 (only LTI systems are described by $h$); HW2 #3 ($\delta[n] = u[n] - u[n-1]$); HW4 #2 (stability ⇔ absolutely summable $h$) |
| [[problems/classifying-system-properties\|System-property table]] | 7/7 | HW1 #5, #6; HW2 #1, #2 |
| [[problems/finite-length-convolution\|Finite-length convolution]] | 7/7 | HW1 #2 (flip and shift); HW2 #5(a)–(c) |
| [[problems/infinite-length-convolution\|Infinite / mixed convolution]] | 5/7 | HW2 #5(b), (d), (e) |
| [[problems/finding-h-from-input-output-pairs\|Finding h from input–output data]] | 7/7 | HW2 #3, #4; HW4 #4 |
| [[problems/z-transform-with-roc\|z-transform with ROC]] | 6/7 | HW1 #3 (step forms); HW3 #1, #2 |
| [[problems/all-possible-rocs\|Inverse z / PFE / all possible ROCs]] | 7/7 | HW3 #3; HW4 #1 |
| [[problems/lccde-to-transfer-function-and-response\|LCCDE ↔ H(z) ↔ response]] | 7/7 | HW3 #4; HW4 #6 |
| [[problems/unbounded-outputs-and-pole-matching\|Unbounded outputs, pole matching, cancellation]] | 7/7 | HW4 #3, #5 |
| [[problems/parameters-for-stability\|Parameters for stability]] | 3/7 | no homework analogue (closest: HW4 #3) — practise on the past exams |
| [[problems/two-sided-systems-as-recursions\|Two-sided systems as recursions]] | 2/7 | no homework analogue — practise on the past exams |

## What the official rubrics reward

- **Plots** are graded on the values and the axis labeling: always mark where $n = 0$ is. A minor slip costs one point.
- **Property questions**: the verdict carries most of the points on the homework, and on the midterm's property table *only* the Y/N boxes are graded ([[0-midterm-1/past-exams/fall-2023|FA2023 #2]] says so), so learn the fast tests in [[problems/classifying-system-properties|classifying system properties]].
- **Proofs and derivations** (HW2 #1–#4) earn their points only with a proper justification; for "find $h$", the LTI reasoning is worth most of the credit even when the algebra slips.
- **Computations** lose one point per minor math mistake: do the bookkeeping (start index, length, ROC) before the arithmetic, and use a check (the sum rule for convolutions, a few samples of $h$ for closed forms).

### Sources for this page

- ECE 310 Fall 2026 assignments HW1–HW5 and the official solutions to HW1–HW4 (including their grading rubrics).
- Lecture dates from the slide decks: L1 Aug 24, L2 Aug 26, L3 Aug 28, L4 Aug 31, L5 Sep 2, L6 Sep 4, …, L11 Sep 18.
- Problem-family counts from the shared map of the seven past Midterm 1 exams ([[0-midterm-1/past-exams/index|past exams]]).
