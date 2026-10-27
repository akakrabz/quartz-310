---
title: "FIR and IIR systems"
description: "Finite vs. infinite impulse response: FIR from no feedback, Lecture 5's recursions worked by superposition, the Lecture 9 test on H(z), why every FIR system is BIBO stable, and the recursive moving average."
tags: [concept, lccde, stability, systems, midterm-1]
aliases: ["FIR", "IIR", "finite impulse response", "infinite impulse response", "moving average", "FIR filter", "IIR filter", "recursive moving average"]
---

*Lectures 5 (Wed Sep 2) §1.1–1.2 and 9 (Mon Sep 14) §1.2 · [[homework/hw3|HW3]] #3a · [[homework/hw4|HW4]] #6 · family: [[problems/lccde-to-transfer-function-and-response|LCCDE → transfer function → response]] · demo: [[demos/difference-equation-simulator|simulator]]*

> [!abstract] In one breath
> - No feedback ($K = 0$): $h[n]$ is the list of input coefficients, finite (FIR), always BIBO stable.
> - Feedback ($K > 0$): the output keeps going after the input stops; $h[n]$ is infinite (IIR) unless a zero cancels every finite pole.
> - First-order recursions with several input terms: find $\hat h$ for one input term, then superpose shifted copies.

## 1. Definitions and the test

> [!key] FIR, IIR and the Lecture 9 test
> - **FIR:** $h[n]$ has finitely many nonzero samples. An [[concepts/lccde|LCCDE]] without feedback, $y[n]=\sum_j c_j\,x[n-j]$, has $h[n]=\sum_j c_j\,\delta[n-j]$: the coefficients *are* the impulse response. $H(z)$ is a polynomial in $z^{-1}$ (and $z$), so its only poles sit at $z=0$ (causal) or $z=\infty$ (non-causal).
> - **IIR:** infinitely many nonzero samples. That requires at least one **finite, nonzero pole that no zero cancels**.
> - **Test (Lecture 9, Fig. 1):** write $H(z)$, cancel common factors, and look for a remaining pole with $0<\lvert p\rvert<\infty$. One exists: IIR. None: FIR.
> - **FIR $\Rightarrow$ BIBO stable, always:** $\sum\lvert h[n]\rvert$ is a finite sum of finite numbers. Flowchart and the feedback-yet-FIR example (Lecture 9, Fig. 1): [[concepts/poles-and-zeros|poles and zeros]] §2.

## 2. Finite impulse response systems (Lecture 5 §1.1)

$K = 0$ in the LCCDE ⇒ **FIR** (eq. 2):
$$
h[n] = \sum_{j=0}^{M-1} c_j\,\delta[n-j] = \{\underset{\uparrow}{c_0},\ c_1,\ \dots,\ c_{M-1}\}.
$$
Finite length; usable directly in the convolution sum ([[concepts/convolution|convolution]]).

**Moving average (eqs. 3–4).** Length-$L$: $y[n]=\frac1L\sum_{i=0}^{L-1}x[n-i]$ has $h[n]=\frac1L\big(u[n]-u[n-L]\big)$. Recursive form, reusing the sum at $n-1$: two additions per sample instead of $L$,
$$
y[n]=y[n-1]+\frac1L\big(x[n]-x[n-L]\big).
$$
It is **still FIR**: in
$$
H(z)=\frac{1-z^{-L}}{L\,(1-z^{-1})}=\frac1L\sum_{k=0}^{L-1}z^{-k}
$$
the zero of $1-z^{-L}$ at $z=1$ cancels the pole ([[concepts/pole-zero-cancellation|pole-zero cancellation]]).

**On the exam ([[exams/midterm-1/past-exams/fall-2025|FA2025 #4]]).** The modified moving average $y[n]=\frac1L\sum_{k=0}^{L-1}x[n-Sk]$ with $L=3$, $S=4$ has $h[n]=\frac13\big(\delta[n]+\delta[n-4]+\delta[n-8]\big)$, and for every $L$, $S$ it is FIR, hence BIBO stable ($\sum\lvert h\rvert=1$): part (c) is True.

## 3. Infinite impulse response systems (Lecture 5 §1.2)

$K > 0$ ⇒ **IIR**: feedback keeps the output going after the input stops. $y[n] = \tfrac12 y[n-1] + x[n]$, $x[n] = \delta[n]$, at rest (eqs. 5–7):

| $n$ | 0 | 1 | 2 | 3 | 4 |
|---|---|---|---|---|---|
| $y[n] = \tfrac12 y[n-1] + x[n]$ | 1 | $\tfrac12$ | $\tfrac14$ | $\tfrac18$ | $\tfrac1{16}$ |

$$
h[n] = \Big\{\underset{\uparrow}{1},\ \tfrac12,\ \tfrac14,\ \tfrac18,\ \tfrac1{16},\ \dots\Big\} = \left(\tfrac12\right)^n u[n].
$$

Infinite $h$: no convolution sum in practice, but the recursion runs easily in code or hardware.

> [!question] Slides Example 1: $h[n]$ of $y[n] = \tfrac13 y[n-1] + x[n]$

> [!success]- Answer
> $h[0] = \tfrac13 h[-1] + \delta[0] = 1$, $h[1] = \tfrac13$, $h[2] = \tfrac19$, … so $h[n] = (\tfrac13)^n u[n]$. In general $y[n] = a\,y[n-1] + x[n]$ has $h[n] = a^n u[n]$.

> [!recipe] Impulse response of a first-order recursion with several input terms (linearity + time-invariance)
> 1. **Feedback part:** replace the input terms by one input $z[n]$: $\hat y[n] = b_1\,\hat y[n-1] + z[n]$, so $\hat h[n] = b_1^{\,n}\,u[n]$.
> 2. **Input part:** with $x[n] = \delta[n]$, $z[n] = \sum_j c_j\,\delta[n-j]$.
> 3. **Superpose:** $h[n] = z[n] * \hat h[n] = \sum_j c_j\,\hat h[n-j]$; shift the step with the exponential.

> [!question] Exercise 1 (notes): $h[n]$ of $y[n] = \tfrac14 y[n-1] - x[n] + \tfrac12 x[n-2]$

> [!success]- Answer
> $\hat h[n] = (\tfrac14)^n u[n]$; $z[n] = -\delta[n] + \tfrac12\delta[n-2]$ (eqs. 8–11):
> $$
> h[n] = -\hat h[n] + \tfrac12\hat h[n-2] = -\left(\tfrac14\right)^n u[n] + \tfrac12\left(\tfrac14\right)^{n-2} u[n-2].
> $$
> First samples: $-1,\ -\tfrac14,\ \tfrac{7}{16},\ \tfrac{7}{64},\ \dots$

> [!question] Slides Example 2: $h[n]$ of $y[n] = \tfrac13 y[n-1] + x[n] - 3x[n-1] + x[n-2]$

> [!success]- Answer
> $\hat h[n] = (\tfrac13)^n u[n]$, $z[n] = \delta[n] - 3\delta[n-1] + \delta[n-2]$:
> $$
> h[n] = \left(\tfrac13\right)^n u[n] - 3\left(\tfrac13\right)^{n-1}u[n-1] + \left(\tfrac13\right)^{n-2}u[n-2].
> $$
> $h[0] = 1$, $h[1] = \tfrac13 - 3 = -\tfrac83$; for $n \ge 2$: $(\tfrac13)^n(1 - 9 + 9) = (\tfrac13)^n$, so $h[2] = \tfrac19$, $h[3] = \tfrac1{27}$, …

Second-order feedback needs the z-transform and partial fractions ([[concepts/transfer-function|transfer function]], [[concepts/partial-fraction-expansion|PFE]]); until then, iterate by hand.

> [!trap]
> - **Feedback does not guarantee IIR**: the recursive moving average above is FIR. Always cancel first.
> - **Cancellation does not guarantee FIR either**: [[homework/hw4|HW4]] #6 has $H=\frac{1+0.5z^{-1}}{(1+0.5z^{-1})^2}=\frac{1}{1+0.5z^{-1}}$, still IIR with $h=(-\frac12)^nu[n]$.
> - "An LSI system with a finite-length impulse response can be BIBO stable or unstable" is **False** ([[exams/midterm-1/past-exams/fall-2019|FA2019 #1e]]): FIR is always stable.
> - **FIR is not the same as causal**: $h=\frac12\delta[n+1]+\delta[n]+\frac12\delta[n-1]$ ([[exams/midterm-1/past-exams/fall-2019|FA2019 #3]]) is FIR and non-causal (pole at $\infty$, ROC $0<\lvert z\rvert<\infty$).
> - **Poles at $z=0$ do not make a system IIR**: $z^{-3}=1/z^3$ is just $\delta[n-3]$.
> - **IIR is not the same as unstable**: $(\frac12)^nu[n]$ is IIR and stable.

> [!exam] FIR ⇒ stable; impulse responses of recursions
> [[exams/midterm-1/past-exams/fall-2025|FA2025 #4]] · [[exams/midterm-1/past-exams/fall-2019|FA2019 #1e, #3]] · [[exams/midterm-1/past-exams/spring-2021|SP2021 #6]] · [[homework/hw3|HW3]] #3a · [[homework/hw4|HW4]] #6 · family: [[problems/lccde-to-transfer-function-and-response|LCCDE → transfer function → response]]

**Where it appears:** [[1-signals-and-systems/05-difference-equations-and-block-diagrams|Lecture 5]] §1.1–1.2 (eqs. 2–11, Exercise 1, slides Examples 1–2), [[2-z-transform/09-transfer-functions|Lecture 9]] §1.2 (Fig. 1); [[homework/hw3|HW3]] #3a (an FIR $H_1(z)$ with ROC $z\neq0$), [[homework/hw4|HW4]] #6; [[problems/lccde-to-transfer-function-and-response|LCCDE → transfer function → response]]; [[demos/difference-equation-simulator|difference-equation simulator]].

## Related
[[concepts/lccde|LCCDE]] · [[concepts/impulse-response|impulse response]] · [[concepts/bibo-stability|BIBO stability]] · [[concepts/poles-and-zeros|poles and zeros]] · [[concepts/pole-zero-cancellation|pole-zero cancellation]] · [[concepts/block-diagram|block diagram]] · [[concepts/transfer-function|transfer function]]

### Sources for this page
Lecture 5 §1.1–1.2 (eqs. 2–11, Exercise 1) and slides (Examples 1–2); Lecture 9 §1.2 and Fig. 1; HW3 #3a, HW4 #6; FA2025 #4, FA2019 #1e and #3.
