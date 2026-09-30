---
title: "Linearity"
description: "A system is linear iff it obeys superposition, T{a x1 + b x2} = a T{x1} + b T{x2}. The formal test, the zero-in/zero-out shortcut, and a library of linear and nonlinear systems from the past-exam tables."
tags: [concept, systems, midterm-1]
aliases: ["linear", "linear system", "superposition", "homogeneity", "additivity", "nonlinear", "non-linear"]
---

> [!key] Definition (Lecture 3)
> $T$ is **linear** iff for all inputs $x_1,x_2$ and all scalars $a,b$
> $$
> T\{a\,x_1[n]+b\,x_2[n]\}=a\,T\{x_1[n]\}+b\,T\{x_2[n]\}\qquad\text{(superposition)},
> $$
> equivalently **homogeneity** $T\{ax\}=aT\{x\}$ plus **additivity** $T\{x_1+x_2\}=T\{x_1\}+T\{x_2\}$.
> Consequence: a linear system maps the zero input to the zero output, $T\{0\}=0$.

> [!recipe] Proving or disproving it
> 1. Name the combined input $x_3=a\,x_1+b\,x_2$ and push it through the formula: $y_3=T\{x_3\}$.
> 2. Expand and try to regroup as $a\,y_1+b\,y_2$. If you can for every $a,b,x_1,x_2$: linear.
> 3. To disprove, one concrete counterexample is enough. Fastest tries: $x=0$ (catches offsets), $a=-1$ (catches $\lvert x\rvert$, $\max\{0,x\}$), $a=2$ (catches $x^2$, $e^x$, products of samples).

**Worked examples (from the tables).** $y=\lvert n\rvert x[n]$ ([[0-midterm-1/past-exams/fall-2025|FA2025 #2]]): $T\{ax_1+bx_2\}=\lvert n\rvert(ax_1[n]+bx_2[n])=a\lvert n\rvert x_1[n]+b\lvert n\rvert x_2[n]=ay_1+by_2$, **linear** (the gain may depend on $n$). $y=x[3]\,x[n]$ ([[0-midterm-1/past-exams/spring-2021|SP2021 #3]]): the input $2x$ gives $2x[3]\cdot2x[n]=4y\neq2y$, **nonlinear**. Lecture 3: $y=x^p[n]$ gives $T\{ax\}=a^pT\{x\}\neq aT\{x\}$ for $p\neq1$.

| form of the system | linear? | examples from exams and homework |
|---|---|---|
| gain depending on $n$ times $x[n]$ | yes | $\lvert n\rvert x[n]$, $\log(\lvert n\rvert+1)\,x[n]$, $(0.8+0.8j)^nx[n]$, $\cos^2(\frac{\pi}{2}n)\,x[n]$, window (HW1 #6) |
| index map only | yes | $x[\lvert n\rvert]$, $x[2n]$, $x[\lvert n\rvert+n]$ |
| convolution with any fixed $h$ | yes | $x*2^nu[-n]$, $x*j^nu[n]$, $x*u[n+1]$ |
| LCCDE at initial rest | yes | $y[n]=y[n-5]+x[n]+10x[n-1]$ (HW2 #1a) |
| constant offset | no | $x[n]+3$, $2x[\lvert n\rvert]+10$ ($T\{0\}\neq0$) |
| nonlinear function of the input | no | $\lvert x[n]-x[n-1]\rvert$, $e^{x[n]+1}$, $\sin(x[n])+x[0]$, $(0.2)^{\lvert n\rvert}\log x[n]$, clipping, median |
| product or ratio of input samples | no | $x[n]x[n+1]$, $x[3]x[n]$, $x[n]/x[2]$ |

> [!trap]
> - **Affine is not linear.** $y=x[n]+3$ ([[0-midterm-1/past-exams/fall-2023|FA2023 #2]]) is a straight line in $x$ but fails $T\{0\}=0$.
> - **$n$-dependent coefficients do not break linearity**; they break [[concepts/time-invariance|time-invariance]]. $\lvert n\rvert x[n]$ is linear.
> - **Products of samples are nonlinear** even when each factor is "first power": $x[3]x[n]$, $x[n]x[n+1]$, $x[n]/x[2]$.
> - **Test a negative scale too**: $\lvert x[n]\rvert$ and $\max\{0,x[n]\}$ pass $a=2$ and fail $a=-1$.
> - **A nonlinear system's impulse response describes nothing**: the median filter has $h[n]=0$ yet is not the zero system ([[concepts/lti-system|LTI system]]).
> - An LCCDE is linear only **at initial rest** (zero initial conditions, as the course assumes).

**Where it appears.** [[1-signals-and-systems/03-system-properties|Lecture 3]] §2.1; [[homework/hw1|HW1]] #5(b) (clipping: nonlinear) and #6(b) (window: linear), [[homework/hw2|HW2]] #1, #2. The Linear column of every property table (7/7 exams, [[0-midterm-1/past-exams/fall-2025|FA2025 #2]] … [[0-midterm-1/past-exams/fall-2019|FA2019 #2]]) and [[0-midterm-1/past-exams/fall-2025|FA2025 #4a]]. Drill: [[problems/classifying-system-properties]], [[0-midterm-1/system-property-bank]].

**Related.** [[concepts/time-invariance|time-invariance]] · [[concepts/causality|causality]] · [[concepts/bibo-stability|BIBO stability]] · [[concepts/lti-system|LTI system]] · [[concepts/impulse-response|impulse response]]

### Sources for this page
Lecture 3 §2.1 (Exercises 1–2) and slides 4–6; HW1 #5–#6 and HW2 #1–#2 with solutions; the property tables of the seven past exams (answers cross-checked numerically in `verify/exams/property_bank.py`, 45/45).
