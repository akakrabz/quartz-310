---
title: "Transfer function H(z)"
description: "H(z) = Z{h[n]} = Y(z)/X(z): read it off an LCCDE and back, factor for poles and zeros, attach the ROC causality or stability demands, invert for h[n] and y[n]."
tags: [concept, z-transform, lccde, systems, stability]
aliases: ["system function", "H(z)", "transfer function"]
---

*Lecture 9 (Mon Sep 14) §1–1.1 · [[homework/hw3|HW3]] #4, [[homework/hw4|HW4]] #3–#6 · family: [[problems/lccde-to-transfer-function-and-response|LCCDE → transfer function → response]]*

> [!abstract] In one breath
> - Convolution becomes multiplication: $Y(z) = H(z)X(z)$, with transfer function $H(z) = Y(z)/X(z) = \mathcal{Z}\{h[n]\}$.
> - z-transform an LCCDE: each delay becomes $z^{-k}$, giving $H(z)$ in one line; read it backwards for the LCCDE.
> - The words "causal", "stable", "initially at rest" fix the ROC; the LCCDE alone does not.

## 1. LTI system response with the z-transform

> [!key] Transfer function (Lecture 9, eqs. 1–3)
> $$
> \begin{aligned}
> Y(z) &= H(z)\,X(z), \qquad \text{ROC at least } R_x \cap R_h, \qquad\qquad \\
> H(z) &= \frac{Y(z)}{X(z)} = \mathcal{Z}\{h[n]\} .
> \end{aligned}
> $$
> Two routes to any output: the [[concepts/convolution|convolution sum]], or multiply in $z$ and invert ([[concepts/inverse-z-transform|inverse z-transform]]). Same `b, a` as `scipy.signal.lfilter`.

"At least": a zero of one factor can cancel a pole of the other and enlarge the ROC of $Y$ ([[concepts/pole-zero-cancellation|pole-zero cancellation]]).

- **Stable:** $H_d(\omega)=H(e^{j\omega})$ ([[concepts/frequency-response|frequency response]]). Not for unstable $H$: the accumulator $\frac{1}{1-z^{-1}}$ has $H_d(\omega)=\frac{1}{1-e^{-j\omega}}+\pi\delta(\omega)$ (HW6 #5).

> [!recipe] Output of an LTI system via the z-transform
> 1. $H(z)$ with its ROC (LCCDE + "causal"/"stable"); $X(z)$ with its ROC.
> 2. $Y = HX$; **cancel common factors first**: an input zero can remove a system pole, a system zero an input pole.
> 3. ROC of $Y$: at least $R_x \cap R_h$; causal system + right-sided input → outside the largest *remaining* pole.
> 4. [[concepts/partial-fraction-expansion|PFE]] (cover-up $A_k = (1-p_k z^{-1})Y(z)\big|_{z=p_k}$); long-divide first if improper. Invert term by term.

## 2. Transfer functions and LCCDEs (Lecture 9 §1.1)

Causal LCCDE, $N$ feedback terms, $M$ input terms (eq. 4):
$$
y[n] + \sum_{k=1}^{N} a_k\, y[n-k] = \sum_{k=0}^{M-1} b_k\, x[n-k].
$$
z-transform both sides (linearity, time shift $x[n-k] \leftrightarrow z^{-k}X(z)$; eqs. 5–6):
$$
\begin{aligned}
Y(z) + \sum_{k=1}^{N} a_k z^{-k}\,Y(z) &= \sum_{k=0}^{M-1} b_k z^{-k}\,X(z)\\
Y(z)\Bigl(1 + \sum_{k=1}^{N} a_k z^{-k}\Bigr) &= X(z)\sum_{k=0}^{M-1} b_k z^{-k} .
\end{aligned}
$$

> [!key] LCCDE ⇄ transfer function (Lecture 9, eq. 7)
> $$
> \begin{aligned}
> &H(z) = \frac{Y(z)}{X(z)} = \frac{\displaystyle\sum_{k=0}^{M-1} b_k z^{-k}}{\displaystyle 1 + \sum_{k=1}^{N} a_k z^{-k}} \\
> \qquad\Longleftrightarrow\qquad
> &y[n] + \sum_{k=1}^{N} a_k\,y[n-k] = \sum_{k=0}^{M-1} b_k\,x[n-k] .
> \end{aligned}
> $$
> Numerator ↔ input taps, denominator ↔ feedback taps, $z^{-k}$ ↔ delay by $k$.

Uses: impulse response of any [[concepts/lccde|LCCDE]] (compute $H$, invert); response to any input without the convolution sum.

> [!recipe] LCCDE → $H(z)$ → LCCDE
> - **Forward.** All $y$ terms left; $y[n-k] \to z^{-k}Y(z)$, $x[n-k] \to z^{-k}X(z)$; $H = Y/X$. Factor (zeros, poles); ROC from the words: **causal → outside the largest pole**, stable → ring containing $\lvert z\rvert = 1$ ([[concepts/bibo-stability|BIBO stability]]).
> - **Backward.** Multiply out the denominator, cross-multiply $Y(z)\cdot\text{den} = X(z)\cdot\text{num}$, read $z^{-k}$ as delay by $k$.

> [!question] Exercise 1 (Lecture 9 notes) — impulse response of the causal $y[n] = \tfrac12 y[n-1] + x[n]$
> Slides Exercise 1: the same with $\tfrac13$.

> [!success]- Answer (eqs. 8–12)
> $Y(z)\bigl(1 - \tfrac12 z^{-1}\bigr) = X(z)$, so $H(z) = \dfrac{1}{1-\frac12 z^{-1}}$, $\lvert z\rvert > \tfrac12$ (causal), and $h[n] = (\tfrac12)^n u[n]$ by inspection (Lecture 5's answer). Slides: $h[n] = (\tfrac13)^n u[n]$.

> [!question] Slides, Exercises 2 and 3 — impulse responses of causal LCCDEs
> (2) $y[n] = \tfrac13 y[n-1] + x[n] - 3x[n-1] + x[n-2]$  (3) $y[n] = \tfrac12 y[n-1] + \tfrac{3}{16} y[n-2] + x[n] - 3x[n-1]$

> [!success]- Answers
> **(2)** $H(z) = \dfrac{1-3z^{-1}+z^{-2}}{1-\frac13 z^{-1}} = \dfrac{1}{1-\frac13 z^{-1}} - \dfrac{3z^{-1}}{1-\frac13 z^{-1}} + \dfrac{z^{-2}}{1-\frac13 z^{-1}}$, $\lvert z\rvert > \tfrac13$:
> $$
> \begin{aligned}
> h[n] &= \left(\tfrac13\right)^n u[n] - 3\left(\tfrac13\right)^{n-1} u[n-1] + \left(\tfrac13\right)^{n-2} u[n-2] \\
> &= \left(\tfrac13\right)^n u[n] - 3\,\delta[n-1],
> \end{aligned}
> $$
> ($h = \{\underset{\uparrow}{1}, -\tfrac83, \tfrac19, \tfrac1{27}, \dots\}$). Long division gives the short form directly: $H = -3z^{-1} + \dfrac{1}{1-\frac13 z^{-1}}$; this $H$ is *improper* ([[concepts/partial-fraction-expansion|PFE]] §3).
> **(3)** $H(z) = \dfrac{1-3z^{-1}}{1-\frac12 z^{-1}-\frac{3}{16}z^{-2}} = \dfrac{1-3z^{-1}}{(1+\frac14 z^{-1})(1-\frac34 z^{-1})} = \dfrac{A_1}{1+\frac14 z^{-1}} + \dfrac{A_2}{1-\frac34 z^{-1}}$. Cover-up: $A_1 = \dfrac{1-3z^{-1}}{1-\frac34 z^{-1}}\Big|_{z=-1/4} = \dfrac{1+12}{1+3} = \dfrac{13}{4}$, $A_2 = \dfrac{1-3z^{-1}}{1+\frac14 z^{-1}}\Big|_{z=3/4} = \dfrac{1-4}{1+\frac13} = -\dfrac94$. Causal:
> $$
> h[n] = \tfrac{13}{4}\left(-\tfrac14\right)^n u[n] - \tfrac94\left(\tfrac34\right)^n u[n] .
> $$
> ROC $\lvert z\rvert>\frac34$: stable. Check $h[0]=1=H(\infty)$.

## 3. Characterizing H(z)

- **Poles/zeros** give order, FIR vs IIR (after cancellation): [[concepts/poles-and-zeros|poles and zeros]], [[concepts/fir-and-iir|FIR and IIR]].
- **ROC:** causal ⇔ $\lvert z\rvert>\lvert p_{\max}\rvert$ incl. $\infty$; stable ⇔ contains $\lvert z\rvert=1$ ([[concepts/region-of-convergence|ROC]] §4).
- Series/parallel combinations: [[concepts/system-algebra|system algebra]].

> [!trap] Signs and ROC
> - [[1-signals-and-systems/05-difference-equations-and-block-diagrams|Lecture 5]] writes $y[n] = \sum_{i=1}^{K} b_i\, y[n-i] + \sum_{j=0}^{M-1} c_j\, x[n-j]$: feedback on the **right**, $b_i$ = feedback. Lecture 9: $a_k = -b_k^{(\text{L5})}$ and $b_k^{(\text{L9})} = c_k^{(\text{L5})}$.
> - $y[n] = \tfrac12 y[n-1] + \tfrac{3}{16}y[n-2] + \dots$ has denominator $1 - \tfrac12 z^{-1} - \tfrac{3}{16}z^{-2}$; $1 + \dots$ puts every pole in the wrong place. SP2021 #6 key slips ($h[0]=-1$, $h[3]=-1$ is correct; [[0-toolkit/05-errata|errata]]).
> - The LCCDE alone does not fix the ROC: $y[n] - \tfrac12 y[n-1] = x[n]$ fits $(\tfrac12)^n u[n]$ and $-(\tfrac12)^n u[-n-1]$. "Causal", "stable" or "initially at rest" picks it.
> - Improper $H$ gives $\delta$ terms: divide first. Cancel before calling a system IIR or unstable (HW4 #6).

> [!exam] LCCDE ↔ $H(z)$ ↔ response — every past exam, 15–20 points
> LCCDE → $H$, poles, zeros, ROC → output for a short input whose zero often cancels a pole.
> [[exams/midterm-1/past-exams/fall-2025|FA2025 #6]] · [[exams/midterm-1/past-exams/spring-2025|SP2025 #8]] · [[exams/midterm-1/past-exams/fall-2024|FA2024 #1(d)–(e), #6]] · [[exams/midterm-1/past-exams/fall-2023|FA2023 #6(b), #7]] · [[exams/midterm-1/past-exams/spring-2023|SP2023 #5, #6]] · [[exams/midterm-1/past-exams/spring-2021|SP2021 #6, #7]] · [[exams/midterm-1/past-exams/fall-2019|FA2019 #1(a), #10]] · family: [[problems/lccde-to-transfer-function-and-response|LCCDE → transfer function → response]]

**Where it appears:** [[2-z-transform/09-transfer-functions|L9]] §1–1.1 (eqs. 1–12, Exercise 1), [[2-z-transform/10-improper-transfer-functions-and-system-algebra|L10]], [[2-z-transform/11-bibo-stability-and-causality|L11]], [[3-fourier-analysis/15-frequency-response|L15]]; [[problems/lccde-to-transfer-function-and-response|LCCDE ⇄ transfer function ⇄ response]], [[problems/finding-h-from-input-output-pairs|Finding h (or H) from input–output pairs]]; [[homework/hw3|HW3]] #4, [[homework/hw4|HW4]] #3–#6; [[demos/difference-equation-simulator|difference-equation simulator]].

## Related
[[concepts/lccde]] · [[concepts/poles-and-zeros]] · [[concepts/region-of-convergence]] · [[concepts/fir-and-iir]] · [[concepts/system-algebra]] · [[concepts/bibo-stability]] · [[concepts/pole-zero-cancellation]] · [[concepts/partial-fraction-expansion]] · [[concepts/inverse-z-transform]] · [[concepts/z-transform-properties]] · [[concepts/eigenfunctions-of-lti-systems]]

### Sources for this page
Lecture 9 notes §1–1.1 (eqs. 1–12, Exercise 1) and slides 1–8 (Exercises 1–3); Lecture 5 notes eq. (1); Lecture 10 §1; Lecture 11 Table 1; Lecture 15 §1; SP2021 #6, FA2019 T/F (a) keys; past exams above.
