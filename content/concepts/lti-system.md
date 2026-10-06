---
title: "LTI system"
description: "Linear + time-invariant: the only systems completely described by one sequence h[n]. Output = convolution, Y(z) = H(z)X(z); the equivalent descriptions (h, H(z) with ROC, LCCDE, block diagram) and the traps about non-LTI systems."
tags: [concept, systems, convolution, midterm-1]
aliases: ["LTI system", "LSI system", "linear shift-invariant", "linear time-invariant", "LTI", "LSI"]
---

> [!key] Why LTI systems are special (Lecture 4)
> Write any input as shifted impulses, $x[n]=\sum_k x[k]\,\delta[n-k]$. **Time-invariance** sends each $\delta[n-k]$ to $h[n-k]$; **linearity** sends the weighted sum to the same weighted sum:
> $$
> y[n]=\sum_{k=-\infty}^{\infty}x[k]\,h[n-k]=(x*h)[n],\qquad Y(z)=H(z)\,X(z).
> $$
> "$T$ is LTI", "$T$'s output is a convolution" and "$T$ is fully described by its impulse response" are equivalent statements (Lecture 4, Fig. 1). **LSI** (linear shift-invariant, older exams) is the same thing, and the **unit pulse response** is the impulse response.

One LTI system, five equivalent descriptions (here the first-order system of Lectures 5 and 9):

| description | what it is | example |
|---|---|---|
| [[concepts/impulse-response\|impulse response]] | output for the input $\delta[n]$ | $h[n]=(\frac12)^nu[n]$ |
| [[concepts/transfer-function\|transfer function]] + ROC | $Y(z)/X(z)=\mathcal{Z}\{h\}$ | $H(z)=\frac{1}{1-\frac12z^{-1}}$, $\lvert z\rvert>\frac12$ |
| [[concepts/lccde\|LCCDE]] + causality (initial rest) | the recursion you run | $y[n]=\frac12y[n-1]+x[n]$ |
| [[concepts/block-diagram\|block diagram]] | delays, gains, adders | one delay, feedback gain $\frac12$ |
| [[concepts/eigenfunctions-of-lti-systems\|eigenvalues]] | response to $z_0^n$ (all $n$) | $H(z_0)\,z_0^n$ |

**Properties read off $h$:** [[concepts/causality|causal]] $\iff h[n]=0$ for $n<0$; [[concepts/bibo-stability|BIBO stable]] $\iff\sum\lvert h[n]\rvert<\infty\iff$ ROC $\ni$ unit circle; [[concepts/fir-and-iir|FIR]] $\iff$ finitely many nonzero samples. **Interconnections** ([[concepts/system-algebra|system algebra]]): series $h_1*h_2$ ($H_1H_2$, order irrelevant), parallel $h_1+h_2$ ($H_1+H_2$).

**Worked example (Lecture 4).** The difference system $y[n]=x[n]-x[n-1]$ is LTI with $h[n]=\delta[n]-\delta[n-1]$, and $x*h$ reproduces it for every input. The three-point median filter $y[n]=\operatorname{median}\{x[n],x[n-1],x[n-2]\}$ has $h[n]=0$ (a single nonzero sample is never the middle value), yet it maps $u[n]$ to $u[n-1]$: it is nonlinear, so its $h$ says nothing.

> [!trap]
> - **"The output is always determined by $h$" is False unless the system is LTI**: [[exams/midterm-1/past-exams/fall-2024|FA2024 #1a]], [[exams/midterm-1/past-exams/fall-2023|FA2023 #1d]], [[exams/midterm-1/past-exams/fall-2019|FA2019 #1b]] (all F). The converse is True: a system whose every response is fully described by $h$ must be LTI ([[exams/midterm-1/past-exams/spring-2023|SP2023 #1a]]).
> - **$h=0$ does not mean "zero system"** for non-LTI systems: the median filter above; $y=n\,x[n]$ answers $\delta[n]$ with $n\,\delta[n]=0$.
> - **Swapping blocks in a cascade is safe only for LTI blocks** ([[exams/midterm-1/past-exams/fall-2023|FA2023 #1e]] T). A time-varying block does not commute: "$n\,x[n]$, then delay" gives $(n-1)x[n-1]$, "delay, then $n\,x[n]$" gives $n\,x[n-1]$.
> - An LCCDE describes an LTI system only **at initial rest** (zero initial conditions).
> - To **prove** a convolution system is LTI, show superposition and shift-invariance of the sum ([[homework/hw2|HW2]] #2).

**Where it appears.** [[1-signals-and-systems/04-impulse-response-and-convolution|Lecture 4]] §1.2, [[1-signals-and-systems/05-difference-equations-and-block-diagrams|Lecture 5]], [[2-z-transform/06-the-z-transform|Lecture 6]] §1, [[2-z-transform/09-transfer-functions|Lecture 9]] §1, [[2-z-transform/10-improper-transfer-functions-and-system-algebra|Lecture 10]] (series/parallel); [[homework/hw2|HW2]] #2–#4. Problem family: [[problems/finding-h-from-input-output-pairs]] (7/7 exams), e.g. the interconnections in [[exams/midterm-1/past-exams/fall-2024|FA2024 #3]] and [[exams/midterm-1/past-exams/spring-2025|SP2025 #3]]; T/F: [[exams/midterm-1/true-false-bank]].

**Related.** [[concepts/linearity|linearity]] · [[concepts/time-invariance|time-invariance]] · [[concepts/convolution|convolution]] · [[concepts/impulse-response|impulse response]] · [[concepts/transfer-function|transfer function]] · [[concepts/system-algebra|system algebra]] · [[concepts/eigenfunctions-of-lti-systems|eigenfunctions]]

### Sources for this page
Lecture 4 §1.2 and Fig. 1 (median-filter and difference-system examples); Lecture 5 Eq. 6; Lecture 9 Eqs. 2 and 8–12; Lecture 10 Table 1; HW2 #2 solution; T/F items FA2024 #1a, FA2023 #1d–e, SP2023 #1a, FA2019 #1b. Median-filter and non-commuting cascade checks in `verify/concepts/verify_glossary_time.py`.
