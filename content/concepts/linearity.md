---
title: "Linearity"
description: "Linear iff superposition holds, T{a x1 + b x2} = a T{x1} + b T{x2}: the formal test, the zero-in/zero-out shortcut, Lecture 3's exercises, linear and nonlinear systems from past exams."
tags: [concept, systems, midterm-1]
aliases: ["linear", "linear system", "superposition", "homogeneity", "additivity", "nonlinear", "non-linear"]
---

*Lecture 3 (Fri Aug 28) §2.1 · [[homework/hw1|HW1]] #5–#6 · [[homework/hw2|HW2]] #1–#2 · family: [[problems/classifying-system-properties|Classifying system properties]]*

> [!abstract] In one breath
> - Linear ⇔ superposition: scale and add inputs ⇒ outputs scale and add the same way.
> - Prove for *every* input by regrouping the formula; disprove with *one* counterexample ($x = 0$, $a = -1$, $a = 2$).
> - Coefficients that depend on $n$ keep a system linear; functions of the input's value do not.

## 1. Definition

> [!key] Linearity (Lecture 3, eqs. 5–7)
> $T$ is **linear** if and only if
> $$
> \begin{aligned}
> T(a\,x[n]) &= a\,T(x[n]) &&\text{(homogeneity)}\\
> T(x_1[n] + x_2[n]) &= T(x_1[n]) + T(x_2[n]) &&\text{(additivity)}
> \end{aligned}
> $$
> or, equivalently, **superposition**: $T(a\,x_1[n] + b\,x_2[n]) = a\,T(x_1[n]) + b\,T(x_2[n])$ for all inputs and all $a, b$.
> Consequence: a linear system maps the zero input to the zero output, $T\{0\}=0$.

## 2. Proving or disproving it

> [!recipe] Proving or disproving linearity
> 1. **Prove:** name $v[n] = a\,x_1[n] + b\,x_2[n]$, write $T(v[n])$ from the formula, regroup into $a\,T(x_1[n]) + b\,T(x_2[n])$ for every $a, b, x_1, x_2$.
> 2. **Disprove:** break homogeneity or additivity with one concrete input. Fastest tries: $x = 0$ (catches offsets), $a = -1$ (catches $\lvert x\rvert$, $\max\{0,x\}$), $a = 2$ (catches $x^2$, $e^x$, products of samples).

> [!question] Notes Exercises 1–2 and slide 5: linear?
> (E1) $y[n] = x[n] - x[n-1]$ (E2) $y[n] = (x[n])^p$, $p > 0$ (S1) $y[n] = \tfrac12 x[n] + \tfrac12 x[n-1]$ (S2) $y[n] = x[n] + 1$

> [!success]- Answers
> **E1, linear.** With $v[n] = a\,x_1[n] + b\,x_2[n]$:
> $$
> \begin{aligned}
> T(v[n]) &= v[n] - v[n-1] = \big(a\,x_1[n] + b\,x_2[n]\big) - \big(a\,x_1[n-1] + b\,x_2[n-1]\big)\\
> &= a\big(x_1[n] - x_1[n-1]\big) + b\big(x_2[n] - x_2[n-1]\big)\\
> &= a\,T(x_1[n]) + b\,T(x_2[n]). \ \checkmark
> \end{aligned}
> $$
> **E2, nonlinear.** $T(a\,x[n]) = a^p (x[n])^p = a^p\,T(x[n]) \neq a\,T(x[n])$ for $p \neq 1$.
> **S1, linear** (as E1). **S2, nonlinear:** $T(a\,x[n]) = a\,x[n] + 1 \ne a\,x[n] + a$; $x = 0$ gives $y = 1$ (affine).

> [!question] Extra practice (slide 6): linear?
> (1) $y[n] = \lvert x[n]\rvert$ (2) $y[n] = n\,(x[n] - x[n-1])$ (3) $y[n] = e^{x[n]}$ (4) $y[n] = \max\{0, x[n]\}$ (posted deck) or $x[n]\,x[0]$ (annotated deck) (5) the running median $\operatorname{median}\{x[n], x[n-1], x[n-2]\}$

> [!success]- Answers
> 1. Nonlinear: $T(a\,x) = \lvert a\rvert\,\lvert x[n]\rvert \neq a\,\lvert x[n]\rvert$ for $a < 0$.
> 2. **Linear**: the factor $n$ is the same for every input.
> 3. Nonlinear: $e^{a\,x[n]} \neq a\,e^{x[n]}$.
> 4. Nonlinear: $\max\{0, -x\} \neq -\max\{0, x\}$; $T(a\,x) = a^2\,x[n]\,x[0]$.
> 5. Nonlinear: windows $(1, 0, 0)$ and $(0, 1, 0)$ have median $0$, their sum $(1, 1, 0)$ median $1$.

## 3. Reading linearity off a formula

**From the exam tables.** $y=\lvert n\rvert x[n]$ ([[exams/midterm-1/past-exams/fall-2025|FA2025 #2]]): $T\{ax_1+bx_2\}=\lvert n\rvert(ax_1[n]+bx_2[n])=a\lvert n\rvert x_1[n]+b\lvert n\rvert x_2[n]=ay_1+by_2$, **linear** (the gain may depend on $n$). $y=x[3]\,x[n]$ ([[exams/midterm-1/past-exams/spring-2021|SP2021 #3]]): the input $2x$ gives $2x[3]\cdot2x[n]=4y\neq2y$, **nonlinear**.

| form of the system | linear? | examples from exams and homework |
|---|---|---|
| gain depending on $n$ times $x[n]$ | yes | $\lvert n\rvert x[n]$, $\log(\lvert n\rvert+1)\,x[n]$, $(0.8+0.8j)^nx[n]$, $\cos^2(\frac{\pi}{2}n)\,x[n]$, window (HW1 #6) |
| index map only | yes | $x[\lvert n\rvert]$, $x[2n]$, $x[\lvert n\rvert+n]$ |
| convolution with any fixed $h$ | yes | $x*2^nu[-n]$, $x*j^nu[n]$, $x*u[n+1]$ |
| LCCDE at initial rest | yes | $y[n]=y[n-5]+x[n]+10x[n-1]$ (HW2 #1a) |
| constant offset | no | $x[n]+3$, $2x[\lvert n\rvert]+10$ ($T\{0\}\neq0$) |
| nonlinear function of the input | no | $\lvert x[n]-x[n-1]\rvert$, $e^{x[n]+1}$, $\sin(x[n])+x[0]$, $(0.2)^{\lvert n\rvert}\log x[n]$, clipping, median |
| product or ratio of input samples | no | $x[n]x[n+1]$, $x[3]x[n]$, $x[n]/x[2]$ |

All four properties in one table: [[concepts/lti-system|LTI system]] §3.

> [!trap]
> - **Affine is not linear.** $y=x[n]+3$ ([[exams/midterm-1/past-exams/fall-2023|FA2023 #2]]) is a straight line in $x$ but fails $T\{0\}=0$.
> - **$n$-dependent coefficients do not break linearity**; they break [[concepts/time-invariance|time-invariance]]. $\lvert n\rvert x[n]$ and $(0.8+0.8j)^n\,x[n]$ are linear.
> - **Products of samples are nonlinear** even when each factor is "first power": $x[3]x[n]$, $x[n]x[n+1]$, $x[n]/x[2]$.
> - **Test a negative scale too**: $\lvert x[n]\rvert$ and $\max\{0,x[n]\}$ pass $a=2$ and fail $a=-1$.
> - **A nonlinear system's impulse response describes nothing**: the median filter has $h[n]=0$ yet is not the zero system ([[concepts/lti-system|LTI system]]).
> - An LCCDE is linear only **at initial rest** (zero initial conditions, as the course assumes).

> [!exam] The Linear column of the property table, 7 of 7 exams
> Three systems × four yes/no boxes, graded on the boxes; plus T/F on the properties' independence.
> [[exams/midterm-1/past-exams/fall-2025|FA2025 #2, #4a]] · [[exams/midterm-1/past-exams/spring-2025|SP2025 #2]] · [[exams/midterm-1/past-exams/fall-2024|FA2024 #2]] · [[exams/midterm-1/past-exams/fall-2023|FA2023 #2]] · [[exams/midterm-1/past-exams/spring-2023|SP2023 #2]] · [[exams/midterm-1/past-exams/spring-2021|SP2021 #3]] · [[exams/midterm-1/past-exams/fall-2019|FA2019 #2]] · [[exams/midterm-1/system-property-bank|system-property bank]] · [[exams/midterm-1/true-false-bank|T/F bank]]

**Where it appears:** [[1-signals-and-systems/03-system-properties|Lecture 3]] §2.1 (Exercises 1–2, slides 5–6); [[homework/hw1|HW1]] #5(b) (clipping: nonlinear) and #6(b) (window: linear), [[homework/hw2|HW2]] #1, #2; [[problems/classifying-system-properties|classifying system properties]], [[demos/practice-drills|practice drills]].

## Related
[[concepts/time-invariance|time-invariance]] · [[concepts/causality|causality]] · [[concepts/bibo-stability|BIBO stability]] · [[concepts/lti-system|LTI system]] · [[concepts/impulse-response|impulse response]]

### Sources for this page
Lecture 3 §2.1 (eqs. 5–7, Exercises 1–2) and slides 4–6 with the annotated in-class deck; HW1 #5–#6 and HW2 #1–#2 with solutions; the property tables of the seven past exams.
