---
title: "ECE 310 · Digital Signal Processing"
description: "Study notes for ECE 310 (DSP, UIUC Fall 2026): lecture pages following Prof. Snyder's notes, concept glossary, problem families, homework walkthroughs, demos and drills, past exams with folded solutions."
---

Notes for **ECE 310 — Digital Signal Processing** (UIUC, Fall 2026, Profs. Snyder and Kamalabadi), from Prof. Snyder's lecture notes and slides, the homework and past exams.

## How to learn with this site

> [!tip] A path through each topic
> 1. **Lecture page**, following the notes.
> 2. **Concept pages**, one idea each.
> 3. **Folded questions**: answer first.
> 4. **Problem families**, one exam problem type each.
> 5. **Do the homework**, then compare with its walkthrough: the statement, a folded solution, and the traps.
> 6. **Drills and demos.**
> 7. **Past exams**, timed; repair misses by family.

## Course map

### [[0-toolkit/index|Toolkit]] — assumed mathematics
[[0-toolkit/01-complex-numbers|Complex numbers]] · [[0-toolkit/02-geometric-series|Geometric series]] · [[0-toolkit/03-sketching-and-transforming-signals|Sketching and transforming signals]] · [[0-toolkit/04-factoring-and-long-division|Factoring and long division]] · [[0-toolkit/05-errata|Errata]]

### [[1-signals-and-systems/index|Unit 1 · Signals and systems]] — Lectures 1–5
1. [[1-signals-and-systems/01-digital-signals|Introduction to digital signals]]
2. [[1-signals-and-systems/02-complex-numbers-and-elementary-signals|Complex numbers and elementary signals]]
3. [[1-signals-and-systems/03-system-properties|System properties]]
4. [[1-signals-and-systems/04-impulse-response-and-convolution|Impulse response and convolution]]
5. [[1-signals-and-systems/05-difference-equations-and-block-diagrams|Difference equations and block diagrams]]

### [[2-z-transform/index|Unit 2 · The z-transform and LTI systems]] — Lectures 6–11
6. [[2-z-transform/06-the-z-transform|The z-transform]]
7. [[2-z-transform/07-z-transform-properties|Properties of the z-transform]]
8. [[2-z-transform/08-inverse-z-transform|The inverse z-transform]]
9. [[2-z-transform/09-transfer-functions|Transfer functions and LTI system response]]
10. [[2-z-transform/10-improper-transfer-functions-and-system-algebra|Improper transfer functions and system algebra]]
11. [[2-z-transform/11-bibo-stability-and-causality|BIBO stability and causality]]

### [[3-fourier-analysis/index|Unit 3 · Fourier analysis and frequency response]] — Lectures 12–16
12. [[3-fourier-analysis/12-convolution-as-template-matching|Convolution as template matching]] (not tested)
13. [[3-fourier-analysis/13-fourier-analysis-and-the-dtft|From Fourier series to the DTFT]]
14. [[3-fourier-analysis/14-dtft-properties|DTFT properties]]
15. [[3-fourier-analysis/15-frequency-response|Frequency response]]
16. [[3-fourier-analysis/16-magnitude-and-phase-response|Magnitude and phase response, group delay]]

### [[4-sampling-and-reconstruction/index|Unit 4 · Sampling and reconstruction]] — Lectures 17–19
17. [[4-sampling-and-reconstruction/17-ideal-analog-to-digital-conversion|Ideal analog-to-digital conversion]]
18. [[4-sampling-and-reconstruction/18-ideal-digital-to-analog-conversion|Ideal digital-to-analog conversion]]
19. [[4-sampling-and-reconstruction/19-aliasing|The aliasing effect]]

### [[5-dft-and-fft/index|Unit 5 · The DFT and FFT]] — Lecture 20 onward
20. [[5-dft-and-fft/20-discrete-fourier-transform|The discrete Fourier transform]] (computing the DTFT, $X[k] = X_d(2\pi k/N)$, $N$-periodicity, zero padding)
21. [[5-dft-and-fft/21-dft-properties|DFT properties]] (modulo/circular reversal, circular convolution, properties table)

### Practice
- [[problems/index|Problem families]]
- [[homework/index|Homework]] — [[homework/hw1|HW1]] · [[homework/hw2|HW2]] · [[homework/hw3|HW3]] · [[homework/hw4|HW4]] · [[homework/hw5|HW5]] · [[homework/hw6|HW6]]
- [[demos/practice-drills|Practice drills]] (autograded)
- [[demos/index|Demos]] — [[demos/convolution-explorer|convolution]] · [[demos/difference-equation-simulator|difference equations]] · [[demos/pole-zero-and-roc-explorer|pole-zero and ROC]] · [[demos/frequency-response-explorer|frequency response]] · [[demos/sampling-explorer|sampling]] · [[demos/python-demos|Python]]

### Exams
[[exams/index|Exams hub]]
- **Midterm 1** (L1–11, held Sep 30): [[exams/midterm-1/index|review guide]] · [[exams/midterm-1/cheat-sheet|cheat sheet]] · [[exams/midterm-1/true-false-bank|T/F bank]] · [[exams/midterm-1/system-property-bank|system-property bank]] · [[exams/midterm-1/past-exams/index|past exams]]
- **Quiz 2** (HW5–HW7, L13–18): [[exams/quiz-2|review page]]
- **Midterm 2** (Units 3–5): [[exams/midterm-2/index|overview]] · [[exams/midterm-2/true-false-bank|T/F bank]] · [[exams/midterm-2/past-exams/index|past exams]]

### Reference
[[concepts/index|Concepts]] ([[concepts/concept-map.canvas|concept map]], Units 1–2) · [[supplements/index|Supplements]] (summary, transform tables, notation, notebooks)

## Conventions

| | this site | also seen |
|---|---|---|
| signals | $x[n]$, $h[n]$, $y[n]$; integer $n$ | $x(t)$ = continuous time |
| elementary | $\delta[n]$ (Kronecker), $u[n]$ | "unit pulse response" = $h[n]$ |
| $n = 0$ | arrow: $\{1,\ \underset{\uparrow}{2},\ 3\}$ ⇒ $x[0] = 2$ | bold or underlined sample |
| convolution | $x[n]*h[n]$ | $(x*h)[n]$ |
| system class | LTI | LSI (older exams) |
| z-transforms | powers of $z^{-1}$: $\dfrac{1}{1-az^{-1}}$ | $\dfrac{z}{z-a}$ |
| ROC | always stated: $\lvert z\rvert>a$ | |
| LCCDE (L9) | $y[n]+\sum_k a_k\,y[n-k] = \sum_k b_k\,x[n-k]$, $\;H(z) = \dfrac{\sum_k b_kz^{-k}}{1+\sum_k a_kz^{-k}}$ (`lfilter(b, a)`) | L5: $y[n] = \sum_i b_i\,y[n-i]+\sum_j c_j\,x[n-j]$, feedback signs flipped |
| partial fractions | $\sum_k \dfrac{A_k}{1-p_kz^{-1}}$, $A_k$ by cover-up | `residuez` |
| DTFT | $X_d(\omega) = \sum_n x[n]e^{-j\omega n}$, on $[-\pi,\pi]$, rad/sample | $X(e^{j\omega})$ — equal when the ROC contains the unit circle |
| frequency response | $H_d(\omega)$; $\lvert H_d\rvert\ge0$; $\angle H_d\in[-\pi,\pi]$ | $H(e^{j\omega})$; a sign-changing real amplitude is not the magnitude |
| impulses | $\delta[n]$: one sample of height 1; $\delta(\omega)$, $\delta(t)$: Dirac, area 1 | |
| continuous time | $x_a(t)$, $X_c(\Omega)$ or $X_a(\Omega)$, rad/s; $\omega=\Omega T$; $\mathrm{sinc}(t)=\frac{\sin t}{t}$ | $X(\Omega)$ in L13; tables: $\frac{\sin\pi x}{\pi x}$ |
| exam citations | FA2024 MT2 #4 = Fall 2024, Midterm 2, problem 4 | FA2024 #4 on Midterm 1 pages |

## Callouts

> [!key] Key
> Result to remember.

> [!recipe] Recipe
> Step-by-step procedure.

> [!trap] Trap
> Point-losing mistake.

> [!exam] Exam
> Past-exam appearances (term, exam, problem).

> [!intuition] Intuition
> The picture behind it.

> [!derivation]- Derivation
> Folded derivation.

> [!question] Question
> Try before opening the answer.

> [!success]- Answer
> Folded solution.

*Status (Oct 20, 2026): Lectures 1–21. Walkthroughs HW1–HW6 (HW7 on the Quiz 2 page).*

### Sources for this page
Snyder, ECE 310 notes and slides L1–21 (Fall 2026); course notation supplement; past midterm cover pages.
