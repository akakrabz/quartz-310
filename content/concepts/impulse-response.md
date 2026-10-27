---
title: "Impulse response"
description: "h[n] = T{δ[n]}: the whole LTI system in one sequence. Lecture 4's two examples, four ways to get h (formula, LCCDE, input–output pair, differenced step response) and what it tells you."
tags: [concept, systems, convolution, midterm-1]
aliases: ["impulse response", "unit pulse response", "unit-pulse response", "unit impulse response", "UPR", "h[n]"]
---

*Lectures 4 (Mon Aug 31) §1 and 5 (Wed Sep 2) §1.2 · [[homework/hw2|HW2]] #4 · [[homework/hw3|HW3]] #3–#4 · [[homework/hw4|HW4]] #4–#6 · family: [[problems/finding-h-from-input-output-pairs|Finding h from input–output pairs]]*

> [!abstract] In one breath
> - $h[n] = T(\delta[n])$: feed one unit impulse, record the output.
> - For an LTI system $h$ is everything: $y = x * h$, $H(z) = \mathcal{Z}\{h\}$, causality and stability read off $h$.
> - Every system has an $h$; only LTI systems are described by it.

## 1. Definition

> [!key] Impulse response (Lecture 4, eq. 1)
> $$
> h[n]=T(\delta[n]).
> $$
> Older exams: *unit pulse response*.

Lecture 4's two examples (eqs. 2–4):
- Difference system $y_1[n] = x[n] - x[n-1]$ (Lecture 3): $h_1[n] = \delta[n] - \delta[n-1]$.
- Width-3 median $y_2[n] = \operatorname{median}\{x[n], x[n-1], x[n-2]\}$: $h_2[n] = 0$ (every window holds one $1$, two $0$s). The difference system is LTI, so $x * h_1$ reproduces it; the median is nonlinear, so $h_2 = 0$ says nothing about other inputs ([[concepts/lti-system|LTI system]]).

## 2. What h tells you

For an [[concepts/lti-system|LTI system]]: $y=x*h$ for every input ([[concepts/convolution|convolution]]), and $H(z)=\mathcal{Z}\{h[n]\}$ is the [[concepts/transfer-function|transfer function]]. Read off $h$: **causal** $\iff h[n]=0$ for $n<0$; **stable** $\iff\sum\lvert h[n]\rvert<\infty$; **FIR** $\iff$ finitely many nonzero samples ([[concepts/fir-and-iir|FIR and IIR]]); start, end and length of $y$ from those of $x$ and $h$.

## 3. Finding h[n]

> [!recipe] Four ways to find $h[n]$
> 1. **Formula $y[n]=\sum_k c_k\,x[n-k]$:** the coefficients *are* $h$: $h[n]=\sum_k c_k\,\delta[n-k]$. ([[exams/midterm-1/past-exams/fall-2025|FA2025 #4b]]: $L=3$, $S=4$ gives $h=\frac13(\delta[n]+\delta[n-4]+\delta[n-8])$.)
> 2. **LCCDE:** run the recursion with $x=\delta$ at initial rest (Lecture 5), or find $H(z)$ and invert it (Lecture 9). With several input terms, find $\hat h$ for the input $\delta[n]$ alone and superpose shifted copies (Lecture 5, Exercise 1; worked in [[concepts/fir-and-iir|FIR and IIR]] §2).
> 3. **An input–output pair of an LTI system:** combine shifted copies of $x$ into $\delta[n]$; the same combination of shifted copies of $y$ is $h$ (HW2 #4, FA2019 #3, SP2023 #4). Or divide: $H(z)=Y(z)/X(z)$ (FA2024 #6, HW4 #4).
> 4. **The step response:** $h[n]=g[n]-g[n-1]$ ([[concepts/step-response|step response]]; FA2023 #4).

**Worked example ([[homework/hw2|HW2]] #4).** An LTI system maps $x[n]=3^{-n}u[n]$ to $y[n]=5^{-n}u[n-1]$. Because
$$
x[n]-\tfrac13x[n-1]=3^{-n}\big(u[n]-u[n-1]\big)=\delta[n],
$$
linearity and time-invariance give $h[n]=y[n]-\tfrac13y[n-1]=5^{-n}u[n-1]-\tfrac13\,5^{-(n-1)}u[n-2]=5^{-n}\big(u[n-1]-\tfrac53u[n-2]\big)$.

**From an LCCDE** (Lecture 5, Exercise 1): $y[n]=\frac14y[n-1]-x[n]+\frac12x[n-2]$ has $h[n]=-(\frac14)^nu[n]+\frac12(\frac14)^{n-2}u[n-2]$. Running the recursion in code: [[demos/python-demos|Python demos]].

> [!trap]
> - **Only LTI systems are described by $h$** ([[exams/midterm-1/past-exams/fall-2024|FA2024 #1a]] F, [[exams/midterm-1/past-exams/fall-2019|FA2019 #1b]] F): the median filter and $y=n\,x[n]$ both have $h=0$.
> - **Bounded $h$ is not stable $h$**: $h=u[n]$ ([[concepts/bibo-stability|BIBO stability]]); finite-length $h$ is always stable.
> - **With feedback, $h$ is not the coefficient list**: $y[n]=\frac12y[n-1]+x[n]$ has $h=(\frac12)^nu[n]$, infinitely long ([[concepts/fir-and-iir|FIR and IIR]]).
> - **Undo shifts as well as scales**: if the input was $2\delta[n-2]$, then $h[n]=\frac12\,y[n+2]$ ([[exams/midterm-1/past-exams/fall-2019|FA2019 #3]]: $h=\frac12\delta[n+1]+\delta[n]+\frac12\delta[n-1]$, not causal).
> - **Keep the unit steps** in pieces like $5^{-(n-1)}u[n-2]$: they say where each term starts.

> [!exam] Finding $h$ from input–output pairs: 7 of 7 exams
> [[exams/midterm-1/past-exams/fall-2025|FA2025 #4]] · [[exams/midterm-1/past-exams/spring-2025|SP2025 #3]] · [[exams/midterm-1/past-exams/fall-2024|FA2024 #3, #6]] · [[exams/midterm-1/past-exams/fall-2023|FA2023 #4]] · [[exams/midterm-1/past-exams/spring-2023|SP2023 #4, #6]] · [[exams/midterm-1/past-exams/spring-2021|SP2021 #7]] · [[exams/midterm-1/past-exams/fall-2019|FA2019 #3]] · recipe: [[problems/finding-h-from-input-output-pairs|finding h]]

**Where it appears:** [[1-signals-and-systems/04-impulse-response-and-convolution|Lecture 4]] §1, [[1-signals-and-systems/05-difference-equations-and-block-diagrams|Lecture 5]] §1, [[2-z-transform/09-transfer-functions|Lecture 9]] §1.1; [[homework/hw2|HW2]] #4, [[homework/hw3|HW3]] #3–#4, [[homework/hw4|HW4]] #4–#6; [[problems/finding-h-from-input-output-pairs|finding h]], [[problems/lccde-to-transfer-function-and-response|LCCDE → transfer function → response]].

## Related
[[concepts/kronecker-delta|Kronecker delta]] · [[concepts/lti-system|LTI system]] · [[concepts/convolution|convolution]] · [[concepts/step-response|step response]] · [[concepts/lccde|LCCDE]] · [[concepts/fir-and-iir|FIR and IIR]] · [[concepts/transfer-function|transfer function]] · [[concepts/inverse-z-transform|inverse z-transform]]

### Sources for this page
Lecture 4 §1 (eqs. 1–4, difference and median examples); Lecture 5 §1.2 and Exercise 1; Lecture 9 §1.1; HW2 #4 (official solution), HW4 #4; FA2019 #3, FA2025 #4.
