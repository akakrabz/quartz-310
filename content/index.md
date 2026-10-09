---
title: "ECE 310 · Digital Signal Processing"
description: "Teaching notes for ECE 310 (Digital Signal Processing, UIUC Fall 2026): every lecture rewritten as a narrative, a concept glossary that links everything, problem families with recipes, homework walkthroughs, interactive demos and autograded drills, and past exams with folded solutions to test yourself."
---

Notes for **ECE 310 — Digital Signal Processing** (University of Illinois, Fall 2026, Profs. Snyder and Kamalabadi), written to *teach* the material rather than to summarize it. The source material is the course itself — Prof. Snyder's lecture notes, the lecture slides with their in-class annotations, the homework and the past exams — digested and rewritten in one consistent notation, with the connections made explicit and every number checked.

## How to learn with this site

> [!tip] A path through each topic
> 1. **Read the lecture.** Lecture pages are the spine, in course order: motivation → definition → worked example → what goes wrong. Each opens with an *In one breath* summary.
> 2. **Open the concept hubs** it links to: one short page per idea (convolution, ROC, DTFT, frequency response, …) with the key formula, the traps, and links to every lecture, homework and problem that uses it.
> 3. **Try the folded questions** before opening their answers. Every worked answer on the site is folded, so any page doubles as a self-test.
> 4. **Work through the problem families.** Each is one kind of problem distilled from the past exams and the homework: how to recognise it, a recipe, the traps, and fresh practice problems.
> 5. **Do the homework**, then compare with its walkthrough: the statement, a folded solution, the traps, and what the official rubric rewards.
> 6. **Drill and play.** The autograded drills generate fresh variants with hints and worked solutions; the demos let you drag signals, poles and zeros and watch the mathematics respond.
> 7. **Test yourself with past exams** at the end of a unit, timed and closed-book, then repair every miss with its problem family.
>
> Hover any link for a preview, open the **graph view** (top right of every page) to see what connects to what, and use **search** for any term.

## Course map

### [[0-toolkit/index|Toolkit]] — the mathematics assumed
[[0-toolkit/01-complex-numbers|Complex numbers]] · [[0-toolkit/02-geometric-series|Geometric series]] · [[0-toolkit/03-sketching-and-transforming-signals|Sketching and transforming signals]] · [[0-toolkit/04-factoring-and-long-division|Factoring and long division]] · [[0-toolkit/05-errata|Errata in the course materials]]

### [[1-signals-and-systems/index|Unit 1 · Signals and systems]] — Lectures 1–5
1. [[1-signals-and-systems/01-digital-signals|Introduction to digital signals]]
2. [[1-signals-and-systems/02-complex-numbers-and-elementary-signals|Math preliminaries: complex numbers and elementary signals]]
3. [[1-signals-and-systems/03-system-properties|Discrete-time systems: linearity, time-invariance, causality, stability]]
4. [[1-signals-and-systems/04-impulse-response-and-convolution|The impulse response and convolution]]
5. [[1-signals-and-systems/05-difference-equations-and-block-diagrams|Difference equations and block diagrams]]

### [[2-z-transform/index|Unit 2 · The z-transform and LTI systems]] — Lectures 6–11
6. [[2-z-transform/06-the-z-transform|The z-transform]]
7. [[2-z-transform/07-z-transform-properties|Properties of the z-transform]]
8. [[2-z-transform/08-inverse-z-transform|The inverse z-transform]]
9. [[2-z-transform/09-transfer-functions|Transfer functions and LTI system response, part 1]]
10. [[2-z-transform/10-improper-transfer-functions-and-system-algebra|Improper transfer functions and system algebra, part 2]]
11. [[2-z-transform/11-bibo-stability-and-causality|BIBO stability and causality]]

### [[3-fourier-analysis/index|Unit 3 · Fourier analysis and frequency response]] — Lectures 12–16
12. [[3-fourier-analysis/12-convolution-as-template-matching|Convolution as template matching]] (not tested)
13. [[3-fourier-analysis/13-fourier-analysis-and-the-dtft|Fourier analysis: from Fourier series to the DTFT]]
14. [[3-fourier-analysis/14-dtft-properties|DTFT properties and the link to the z-transform]]
15. [[3-fourier-analysis/15-frequency-response|Frequency response]]
16. [[3-fourier-analysis/16-magnitude-and-phase-response|Magnitude and phase response, group delay]]

More lectures to come: ideal filters, sampling and reconstruction, the DFT and FFT.

### Practice
- [[problems/index|Problem families]] — every kind of problem the past exams and the homework keep setting, each with a recipe, traps, all past instances and fresh practice problems.
- [[homework/index|Homework]] — walkthroughs of [[homework/hw1|HW1]] · [[homework/hw2|HW2]] · [[homework/hw3|HW3]] · [[homework/hw4|HW4]] · [[homework/hw5|HW5]] · [[homework/hw6|HW6]].
- [[demos/practice-drills|Practice drills]] — randomized, autograded drills with hints and worked solutions.
- [[demos/index|Interactive demos]] — [[demos/convolution-explorer|convolution explorer]] · [[demos/difference-equation-simulator|difference-equation simulator]] · [[demos/pole-zero-and-roc-explorer|pole-zero and ROC explorer]] · [[demos/frequency-response-explorer|frequency-response explorer]] · [[demos/python-demos|Python demos]].

### Exams
[[exams/index|Exams]] — how to use past exams to test yourself, and everything for each midterm:

- **Midterm 1** (Lectures 1–11, held Sep 30): [[exams/midterm-1/index|review guide]] · [[exams/midterm-1/cheat-sheet|cheat sheet]] · [[exams/midterm-1/true-false-bank|T/F bank]] · [[exams/midterm-1/system-property-bank|system-property bank]] · [[exams/midterm-1/past-exams/index|seven past exams]]
- **Midterm 2** (Unit 3 and the lectures after it): [[exams/midterm-2/index|overview]] · [[exams/midterm-2/past-exams/index|seven past exams]]

### Reference
[[concepts/index|Concept glossary]] (with the [[concepts/concept-map.canvas|concept map]] of Units 1–2) · [[0-toolkit/index|Toolkit]] · [[0-toolkit/05-errata|Errata in the course materials]] · [[supplements/index|Supplements]] (course summary, transform tables, Singer & Munson notes, notation, demo notebooks)

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
| DTFT | $X_d(\omega) = \sum_n x[n]e^{-j\omega n}$, $2\pi$-periodic, plotted on $[-\pi,\pi]$, $\omega$ in radians per sample | $X(e^{j\omega})$ in the textbook and the course tables — the same function when the ROC of $X(z)$ contains the unit circle |
| frequency response | $H_d(\omega)$, the DTFT of $h[n]$; magnitude $\lvert H_d(\omega)\rvert\ge0$ always; phase $\angle H_d(\omega)$ as a principal angle in $[-\pi,\pi]$ | $H(e^{j\omega})$; a real amplitude that changes sign, as in $2e^{j(\pi/2-\omega)}\sin\omega$ (Lecture 16), is a step on the way, not the magnitude |
| impulses | $\delta[n]$ is the Kronecker delta, one sample of height 1; $\delta(\omega)$ and $\delta(t)$ are Dirac impulses of area 1, used in spectra | |
| continuous time | $x(t)$, its Fourier transform $X_c(\Omega)$ or $X_a(\Omega)$ as the exams write it, $\Omega$ in radians per second | $X(\Omega)$ in Lecture 13 |
| exam citations | FA2024 MT2 #4 = Fall 2024, Midterm 2, problem 4 | the Midterm 1 pages write FA2024 #4 for Midterm 1 problems |

## Callouts

The notes use a few recurring boxes, so you can skim for what you need:

> [!key] Key
> The result to remember — e.g. an LTI system is BIBO stable if and only if the ROC of $H(z)$ contains the unit circle, and then its frequency response is $H_d(\omega) = H(e^{j\omega})$.

> [!recipe] Recipe
> A procedure, step by step — e.g. inverse z: factor, long-divide if improper, cover-up for each $A_k$, choose each term's direction from the ROC.

> [!trap] Trap
> A mistake that costs points — e.g. the left-sided pair is $-a^nu[-n-1] \leftrightarrow \dfrac{1}{1-az^{-1}}$, $\lvert z\rvert<\lvert a\rvert$, minus sign included. Several traps come from real exam keys.

> [!exam] Exam
> How the idea shows up on past exams, citing term, exam and problem — e.g. FA2025 MT1 #8b hides a pole at $e^{j2/3}$, not $e^{j2\pi/3}$. These boxes are the exam layer: usually one per lecture, near the end.

> [!intuition] Intuition
> The picture behind the mathematics — e.g. convolution is a sum of shifted, scaled copies of $h[n]$, one per input sample.

> [!derivation]- Derivation (click to expand)
> Longer derivations are folded so the narrative stays readable. Expand when you want the details.

> [!question] Question
> A problem statement, taken from a lecture, the homework or a past exam — try it before opening the answer below it.

> [!success]- Answer (click to expand)
> Solutions are folded, so you can test yourself first. Every number in them was checked numerically.

*Status (October 2026): Units 1–2 — Lectures 1–11, HW1–HW4 and the seven past Midterm 1 exams — are complete. Unit 3 covers Lectures 12–16 and HW5–HW6, and the seven past Midterm 2 exams are typed with folded solutions. Lectures 17 onward are to come. Sources: C. Snyder, ECE 310 lecture notes and slides, Fall 2026 (with the annotated in-class slides and the Midterm 1 Review); homework HW1–HW6 with the official solutions to HW1–HW5; past Midterm 1 exams FA2019–FA2025 and past Midterm 2 exams FA2019–SP2025, with keys; the ECE 310 course summary and transform tables; A. C. Singer and D. C. Munson, ECE 310 course notes (2019).*

### Sources for this page

The course calendar and titles on the Fall 2026 lecture slides (Lectures 1–16, Aug 24 – Oct 5), the exam instructions on the past midterms, the notation supplement of the course (class vs. textbook notation), and Lectures 13–16 for the DTFT and frequency-response notation.
