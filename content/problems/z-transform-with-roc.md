---
title: "z-transform with ROC"
description: "X(z) and its ROC for the signals Midterm 1 likes: shifted exponentials (shift factor), finite sequences (the 0/∞ rule), two-sided sums, n·x[n], cos² expansions. Six of seven past exams, 9–18 points."
tags: [problem-family, problem, z-transform, roc, midterm-1]
family_frequency: "6 of 7 exams"
typical_points: "9–18"
lectures: [6, 7]
---

*Problem family · six of seven past exams, three parts of 5–6 points on recent ones · 9–18 points · [[2-z-transform/06-the-z-transform|Lecture 6]], [[2-z-transform/07-z-transform-properties|Lecture 7]] · [[demos/pole-zero-and-roc-explorer|pole–zero and ROC explorer]]*

## What it looks like on the exam

"For each signal, find $X(z)$ and its ROC." Each signal dodges the table: a step at the wrong index, a window, a two-sided sum, a factor $n$, a squared cosine. The [[homework/hw3|HW3 #1]] rubric gives 3 of 6 points for $X(z)$ without a correct ROC.

| instance | signals |
|---|---|
| [[exams/midterm-1/past-exams/fall-2025\|FA2025 #5]] (15) | (a) $e^{j\pi n/3}u[n+4]$ (b) $u[n]-u[n-8]$ (c) $\cos^2\!\left(\tfrac{\pi}{4}n\right)u[n]$ |
| [[exams/midterm-1/past-exams/spring-2025\|SP2025 #5]] (18) | (a) $\sum_{k=0}^{2}\left(\tfrac12\right)^k u[n-k]$ (b) $3^n u[-n+2]$ (c) $\left(\tfrac14\right)^n\left(\tfrac23\right)^{n-2}u[n-1]+\left(\tfrac43\right)^n u[-n-1]$ |
| [[exams/midterm-1/past-exams/fall-2024\|FA2024 #5]] (15) | (a) $(n+1)u[n-1]$ (b) $u[n-1]\,u[3-n]$ (c) $3^{-n}u[n]+3^n u[-n]$ |
| [[exams/midterm-1/past-exams/fall-2023\|FA2023 #5]] (9) | $n\,u[n+1]$ |
| [[exams/midterm-1/past-exams/spring-2021\|SP2021 #4]] (10) | $(n+1)x[n]$, $x[n]\leftrightarrow\dfrac{1}{1-0.5z^{-1}}$, $\lvert z\rvert>0.5$ |
| [[exams/midterm-1/past-exams/fall-2019\|FA2019 #5]] (10) | (a) $3^{-n}\left(u[n-5]-u[n-100]\right)$ (b) $e^{-n^2}u[n-8]\,u[-n+10]$ |
| HW3 #1 | (a) $\delta[n+3]+4\delta[n]-\delta[n-2]$ (b) $\left(\tfrac34\right)^{n+3}u[n-2]$ (c) $3^n u[-n]+2^{-n}u[n]$ (d) $\left(\tfrac14\right)^{\lvert n\rvert}$ (e) $n\left(\tfrac12\right)^n\left(u[n]-u[n-5]\right)$ |
| HW3 #2 | properties on $x[n]\leftrightarrow\dfrac{1}{1-\frac13z^{-1}}$: $x[n+3]$, $2^n x[n]$, $\cos\!\left(\tfrac{\pi}{4}n\right)x[n]$, $n(n-2)x[n-1]$, $\left(\tfrac15\right)^n u[n]*x[n]$ |
| Lectures 6–7 | $u[n]$, $a^n u[n]$; why $X(\tfrac14)$ is meaningless for $\left(\tfrac12\right)^n u[n]$ |

> [!success]- Answers
> | instance | $X(z)$ | ROC |
> |---|---|---|
> | FA2025 #5a | $\dfrac{e^{-j4\pi/3}z^{4}}{1-e^{j\pi/3}z^{-1}}$ (key's denominator has a stray $n$) | $1<\lvert z\rvert<\infty$ |
> | FA2025 #5b | $\dfrac{1-z^{-8}}{1-z^{-1}}$ | $z\neq0$ |
> | FA2025 #5c | $\dfrac{1/2}{1-z^{-1}}+\dfrac{1/4}{1-jz^{-1}}+\dfrac{1/4}{1+jz^{-1}}$ | $\lvert z\rvert>1$ |
> | SP2025 #5a | $\dfrac{1+\frac12z^{-1}+\frac14z^{-2}}{1-z^{-1}}$ | $\lvert z\rvert>1$ |
> | SP2025 #5b | $\dfrac{-27z^{-3}}{1-3z^{-1}}=\dfrac{9z^{-2}}{1-\frac13z}$ | $0<\lvert z\rvert<3$ |
> | SP2025 #5c | $\dfrac{\frac38z^{-1}}{1-\frac16z^{-1}}-\dfrac{1}{1-\frac43z^{-1}}$ | $\tfrac16<\lvert z\rvert<\tfrac43$ |
> | FA2024 #5a | $\dfrac{z^{-2}}{(1-z^{-1})^2}+\dfrac{2z^{-1}}{1-z^{-1}}$ | $\lvert z\rvert>1$ |
> | FA2024 #5b | $z^{-1}+z^{-2}+z^{-3}$ | $z\neq0$ |
> | FA2024 #5c | $\dfrac{1}{1-\frac13z^{-1}}-\dfrac{3z^{-1}}{1-3z^{-1}}$ | $\tfrac13<\lvert z\rvert<3$ |
> | FA2023 #5 | $\dfrac{z^{-1}}{(1-z^{-1})^2}-z$ (key: $\dfrac{1}{(1-z^{-1})^2}-\dfrac{z}{1-z^{-1}}$, same) | $1<\lvert z\rvert<\infty$ |
> | SP2021 #4 | $\dfrac{\frac12z^{-1}}{(1-\frac12z^{-1})^2}+\dfrac{1}{1-\frac12z^{-1}}$ | $\lvert z\rvert>\tfrac12$ |
> | FA2019 #5a | $\dfrac{\left(\frac13\right)^5z^{-5}\left(1-\left(\frac13\right)^{95}z^{-95}\right)}{1-\frac13z^{-1}}$ | $z\neq0$ |
> | FA2019 #5b | $e^{-64}z^{-8}+e^{-81}z^{-9}+e^{-100}z^{-10}$ (key: $e^{-91}$, a typo) | $z\neq0$ |
> | HW3 #1a | $z^{3}+4-z^{-2}$ | $0<\lvert z\rvert<\infty$ |
> | HW3 #1b | $\dfrac{\left(\frac34\right)^5z^{-2}}{1-\frac34z^{-1}}$ | $\lvert z\rvert>\tfrac34$ |
> | HW3 #1c | $\dfrac{1}{1-\frac13z}+\dfrac{1}{1-\frac12z^{-1}}$ | $\tfrac12<\lvert z\rvert<3$ |
> | HW3 #1d | $\dfrac{1}{1-\frac14z^{-1}}-\dfrac{1}{1-4z^{-1}}$ | $\tfrac14<\lvert z\rvert<4$ |
> | HW3 #1e | $\tfrac12z^{-1}+\tfrac12z^{-2}+\tfrac38z^{-3}+\tfrac14z^{-4}$ | $z\neq0$ |

## The recipe

| $x[n]$ | $X(z)$ | ROC |
|---|---|---|
| $\delta[n-k]$ | $z^{-k}$ | all $z$, except $0$ if $k>0$, $\infty$ if $k<0$ |
| $a^n u[n]$ | $\dfrac{1}{1-az^{-1}}$ | $\lvert z\rvert>\lvert a\rvert$ |
| $-a^n u[-n-1]$ | $\dfrac{1}{1-az^{-1}}$ | $\lvert z\rvert<\lvert a\rvert$ |
| $n\,a^n u[n]$ | $\dfrac{az^{-1}}{(1-az^{-1})^2}$ | $\lvert z\rvert>\lvert a\rvert$ |
| $r^n\cos(\omega_0n)\,u[n]$ | $\dfrac{1-r\cos\omega_0\,z^{-1}}{1-2r\cos\omega_0\,z^{-1}+r^2z^{-2}}$ | $\lvert z\rvert>r$ |
| $x[n-k]$ | $z^{-k}X(z)$ | $R_x$, except possibly $0$ or $\infty$ |
| $a^n x[n]$ | $X(z/a)$ | $\lvert a\rvert R_x$ |
| $n\,x[n]$ | $-z\,\dfrac{dX}{dz}$ | $R_x$ |
| $x[-n]$ | $X(1/z)$ | $1/R_x$ |

> [!recipe] $X(z)$ and its ROC
> 1. **Split** into table pieces: products of steps → windows; two-sided at $n=0$ ($a^{\lvert n\rvert}=a^n u[n]+a^{-n}u[-n-1]$); $\cos^2\theta=\tfrac12+\tfrac14e^{j2\theta}+\tfrac14e^{-j2\theta}$.
> 2. **Shift factor:** match exponent to step,
> $$
> a^n u[n-n_0]=a^{n_0}\cdot a^{\,n-n_0}u[n-n_0]\ \longleftrightarrow\ \frac{a^{n_0}z^{-n_0}}{1-az^{-1}} ;
> $$
> left-sided too: $3^n u[-n+2]=9\cdot3^{\,n-2}u[-(n-2)]$.
> 3. **Transform** each piece; finite pieces: read the polynomial.
> 4. **ROC per piece, intersect.** Right-sided: outside the pole; left-sided: inside. Samples at $n>0$ exclude $0$, at $n<0$ exclude $\infty$ ($e^{j\pi n/3}u[n+4]$: $1<\lvert z\rvert<\infty$). Empty: no transform.
> 5. **Check:** no pole in the ROC; $X(1)=\sum x$ if $z=1$ is inside.

> [!trap] Where the points go
> - **Shift factor:** $\left(\tfrac34\right)^{n+3}u[n-2]$ gives $(3/4)^5$, not 1 or $(3/4)^3$.
> - **Left-sided sign:** $a^n u[-n-1]\leftrightarrow\dfrac{-1}{1-az^{-1}}$; $a^nu[-n]$ includes $n=0$: $\dfrac{-az^{-1}}{1-az^{-1}}$ (FA2024 #5c).
> - **Finite sequences:** $\dfrac{1-z^{-8}}{1-z^{-1}}$ has ROC $z\neq0$, not $\lvert z\rvert>1$; mind the $\infty$ exclusion ($n\,u[n+1]$).
> - **$e^{j\omega_0n}u[n]$:** pole on $\lvert z\rvert=1$, ROC $\lvert z\rvert>1$.
> - **$n\,x[n]\leftrightarrow-z\,\frac{dX}{dz}$:** minus and $z$; $(n+1)x[n]$ adds $X$ (SP2021 #4).

## Practice problems

> [!question] Practice 1 — shifts, windows, and a two-sided sum
> $X(z)$ and ROC: (a) $\left(\tfrac12\right)^{n+1}u[n-3]$ (b) $(-1)^n\left(u[n+2]-u[n-3]\right)$ (c) $2^n u[-n+1]+\left(\tfrac13\right)^n u[n]$.

> [!success]- Solution
> **(a)**
> $$
> X(z)=\frac{\frac1{16}z^{-3}}{1-\frac12z^{-1}},\qquad \lvert z\rvert>\tfrac12 .
> $$
> **(b)**
> $$
> X(z)=z^{2}-z+1-z^{-1}+z^{-2},\qquad 0<\lvert z\rvert<\infty .
> $$
> **(c)** $2^n u[-n+1]=4\cdot2^{\,n-2}u[-(n-2)-1]$:
> $$
> X(z)=\frac{1}{1-\frac13z^{-1}}-\frac{4z^{-2}}{1-2z^{-1}},\qquad \tfrac13<\lvert z\rvert<2 .
> $$
> Check $z=1$: $\tfrac32+4=\tfrac{11}{2}$ ✓.

> [!question] Practice 2 — n·x[n], a damped cosine, and sin²
> (a) $n\left(\tfrac12\right)^n u[n-1]$ (b) $\left(\tfrac12\right)^n\cos\!\left(\tfrac{\pi}{3}n\right)u[n]$ (c) $\sin^2\!\left(\tfrac{\pi}{2}n\right)u[n]$.

> [!success]- Solution
> $$
> \begin{gathered}
> \text{(a)}\ \frac{\frac12z^{-1}}{\left(1-\frac12z^{-1}\right)^2},\ \lvert z\rvert>\tfrac12;\qquad\text{(b)}\ \frac{1-\frac14z^{-1}}{1-\frac12z^{-1}+\frac14z^{-2}},\ \lvert z\rvert>\tfrac12;\\
> \text{(c)}\ \frac{z^{-1}}{1-z^{-2}},\ \lvert z\rvert>1 .
> \end{gathered}
> $$

> [!question] Practice 3 — two-sided exponentials
> (a) $\left(\tfrac45\right)^{\lvert n-2\rvert}$ (b) $2^{\lvert n\rvert}$.

> [!success]- Solution
> **(a)**
> $$
> \begin{aligned}
> X(z)&=z^{-2}\left[\frac{1}{1-0.8z^{-1}}-\frac{1}{1-1.25z^{-1}}\right]\\
> &=\frac{-0.45\,z^{-3}}{\left(1-0.8z^{-1}\right)\left(1-1.25z^{-1}\right)},\qquad 0.8<\lvert z\rvert<1.25 .
> \end{aligned}
> $$
> **(b)** $\lvert z\rvert>2$ and $\lvert z\rvert<\tfrac12$: empty, no z-transform.

## Related

[[concepts/region-of-convergence|ROC]] · [[concepts/z-transform-pairs|z-transform pairs]] · [[supplements/transform-tables|transform tables]] · [[problems/all-possible-rocs|all possible ROCs]] · [[0-toolkit/05-errata|errata]]

### Sources for this page

Lectures 6–7 notes and slides; HW3 #1–2 with solutions; past Midterm 1 exams FA2019–FA2025 with keys; Midterm 1 review slides.
