---
title: "z-transform with ROC"
description: "Find X(z) and its region of convergence for the signals Midterm 1 likes: shifted exponentials (with the shift factor), finite sequences (the 0/∞ rule), two-sided sums, n·x[n], and cos² expansions. Six of seven past exams, 9–18 points."
tags: [problem-family, problem, z-transform, roc, midterm-1]
family_frequency: "6 of 7 exams"
typical_points: "9–18"
lectures: [6, 7]
---

*Problem family · on six of the seven past exams, three parts of 5–6 points each on recent ones · 9–18 points · uses [[2-z-transform/06-the-z-transform|Lecture 6]] and [[2-z-transform/07-z-transform-properties|Lecture 7]] · concepts: [[concepts/z-transform]], [[concepts/region-of-convergence]], [[concepts/z-transform-pairs]], [[concepts/z-transform-properties]], [[concepts/sided-sequences]] · see it: [[demos/pole-zero-and-roc-explorer|pole–zero and ROC explorer]]*

## What it looks like on the exam

"For each signal, find $X(z)$ and its ROC." Three signals, each built so that the table pair does not apply directly: a step that starts at the wrong index, a finite window written with steps, a two-sided sum, a factor $n$, or a squared cosine. Credit is split between the transform and the ROC: the [[homework/hw3|HW3 #1]] rubric gives 3 of 6 points for a correct $X(z)$ whose ROC is missing or wrong.

| instance | signals |
|---|---|
| [[0-midterm-1/past-exams/fall-2025\|FA2025 #5]] (15) | (a) $e^{j\pi n/3}u[n+4]$ (b) $u[n]-u[n-8]$ (c) $\cos^2\!\left(\tfrac{\pi}{4}n\right)u[n]$ |
| [[0-midterm-1/past-exams/spring-2025\|SP2025 #5]] (18) | (a) $\sum_{k=0}^{2}\left(\tfrac12\right)^k u[n-k]$ (b) $3^n u[-n+2]$ (c) $\left(\tfrac14\right)^n\left(\tfrac23\right)^{n-2}u[n-1]+\left(\tfrac43\right)^n u[-n-1]$ |
| [[0-midterm-1/past-exams/fall-2024\|FA2024 #5]] (15) | (a) $(n+1)u[n-1]$ (b) $u[n-1]\,u[3-n]$ (c) $3^{-n}u[n]+3^n u[-n]$ |
| [[0-midterm-1/past-exams/fall-2023\|FA2023 #5]] (9) | $n\,u[n+1]$ |
| [[0-midterm-1/past-exams/spring-2021\|SP2021 #4]] (10) | $(n+1)x[n]$, given $x[n]\leftrightarrow\dfrac{1}{1-0.5z^{-1}}$, $\lvert z\rvert>0.5$ |
| [[0-midterm-1/past-exams/fall-2019\|FA2019 #5]] (10) | (a) $3^{-n}\left(u[n-5]-u[n-100]\right)$ (b) $e^{-n^2}u[n-8]\,u[-n+10]$ |
| [[homework/hw3\|HW3 #1]] | (a) $\delta[n+3]+4\delta[n]-\delta[n-2]$ (b) $\left(\tfrac34\right)^{n+3}u[n-2]$ (c) $3^n u[-n]+2^{-n}u[n]$ (d) $\left(\tfrac14\right)^{\lvert n\rvert}$ (e) $n\left(\tfrac12\right)^n\left(u[n]-u[n-5]\right)$ |
| [[homework/hw3\|HW3 #2]] | properties applied to $x[n]\leftrightarrow\dfrac{1}{1-\frac13z^{-1}}$: $x[n+3]$, $2^n x[n]$, $\cos\!\left(\tfrac{\pi}{4}n\right)x[n]$, $n(n-2)x[n-1]$, $\left(\tfrac15\right)^n u[n]*x[n]$ |
| [[2-z-transform/06-the-z-transform\|Lecture 6]] | exercises: $u[n]$, $a^n u[n]$; [[2-z-transform/07-z-transform-properties\|Lecture 7]]: why $X(\tfrac14)$ is meaningless for $\left(\tfrac12\right)^n u[n]$ |

> [!success]- Answers to the exam and HW3 #1 instances
> | instance | $X(z)$ | ROC |
> |---|---|---|
> | FA2025 #5a | $\dfrac{e^{-j4\pi/3}z^{4}}{1-e^{j\pi/3}z^{-1}}$ (key's handwritten denominator has a stray $n$) | $1<\lvert z\rvert<\infty$ |
> | FA2025 #5b | $\sum_{k=0}^{7}z^{-k}=\dfrac{1-z^{-8}}{1-z^{-1}}$ | $z\neq0$ |
> | FA2025 #5c | $\dfrac{1/2}{1-z^{-1}}+\dfrac{1/4}{1-jz^{-1}}+\dfrac{1/4}{1+jz^{-1}}$ | $\lvert z\rvert>1$ |
> | SP2025 #5a | $\dfrac{1+\frac12z^{-1}+\frac14z^{-2}}{1-z^{-1}}$ | $\lvert z\rvert>1$ |
> | SP2025 #5b | $\dfrac{-27z^{-3}}{1-3z^{-1}}=\dfrac{9z^{-2}}{1-\frac13z}$ | $0<\lvert z\rvert<3$ |
> | SP2025 #5c | $\dfrac{\frac38z^{-1}}{1-\frac16z^{-1}}-\dfrac{1}{1-\frac43z^{-1}}$ | $\tfrac16<\lvert z\rvert<\tfrac43$ |
> | FA2024 #5a | $\dfrac{z^{-2}}{(1-z^{-1})^2}+\dfrac{2z^{-1}}{1-z^{-1}}$ | $\lvert z\rvert>1$ |
> | FA2024 #5b | $z^{-1}+z^{-2}+z^{-3}$ | $z\neq0$ |
> | FA2024 #5c | $\dfrac{1}{1-\frac13z^{-1}}-\dfrac{3z^{-1}}{1-3z^{-1}}$ | $\tfrac13<\lvert z\rvert<3$ |
> | FA2023 #5 | $\dfrac{z^{-1}}{(1-z^{-1})^2}-z$ (key: $\dfrac{1}{(1-z^{-1})^2}-\dfrac{z}{1-z^{-1}}$, same function) | $1<\lvert z\rvert<\infty$ |
> | SP2021 #4 | $\dfrac{\frac12z^{-1}}{(1-\frac12z^{-1})^2}+\dfrac{1}{1-\frac12z^{-1}}$ | $\lvert z\rvert>\tfrac12$ |
> | FA2019 #5a | $\sum_{k=5}^{99}\left(\tfrac13\right)^k z^{-k}=\dfrac{\left(\frac13\right)^5z^{-5}\left(1-\left(\frac13\right)^{95}z^{-95}\right)}{1-\frac13z^{-1}}$ | $z\neq0$ |
> | FA2019 #5b | $e^{-64}z^{-8}+e^{-81}z^{-9}+e^{-100}z^{-10}$ (key: $e^{-91}$, a typo) | $z\neq0$ |
> | HW3 #1a | $z^{3}+4-z^{-2}$ | $0<\lvert z\rvert<\infty$ |
> | HW3 #1b | $\dfrac{\left(\frac34\right)^5z^{-2}}{1-\frac34z^{-1}}$ | $\lvert z\rvert>\tfrac34$ |
> | HW3 #1c | $\dfrac{1}{1-\frac13z}+\dfrac{1}{1-\frac12z^{-1}}$ | $\tfrac12<\lvert z\rvert<3$ |
> | HW3 #1d | $\dfrac{1}{1-\frac14z^{-1}}-\dfrac{1}{1-4z^{-1}}$ | $\tfrac14<\lvert z\rvert<4$ |
> | HW3 #1e | $\tfrac12z^{-1}+\tfrac12z^{-2}+\tfrac38z^{-3}+\tfrac14z^{-4}$ | $z\neq0$ |
>
> Every row is checked against a direct partial sum $\sum_n x[n]z^{-n}$ at several points inside the stated ROC (`verify/problems/z_transform_roc.py`).

## The method

The pairs and properties you need (all from [[2-z-transform/06-the-z-transform|Lecture 6]]–[[2-z-transform/07-z-transform-properties|7]]):

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

> [!recipe] X(z) and its ROC in five steps
> 1. **Split** the signal into pieces that each look like one table entry: expand products of steps into a window or a single step ($u[n-1]u[3-n]=\delta[n-1]+\delta[n-2]+\delta[n-3]$), split two-sided signals at $n=0$ ($a^{\lvert n\rvert}=a^n u[n]+a^{-n}u[-n-1]$), and turn $\cos$, $\cos^2$, $\sin^2$ into complex exponentials ($\cos^2\theta=\tfrac12+\tfrac14e^{j2\theta}+\tfrac14e^{-j2\theta}$).
> 2. **Match the exponent to the step (the shift factor).** Make the exponent read $n-n_0$ exactly when the step reads $u[n-n_0]$, paying for it with a constant:
> $$
> a^n u[n-n_0]=a^{n_0}\cdot a^{\,n-n_0}u[n-n_0]\ \longleftrightarrow\ \frac{a^{n_0}z^{-n_0}}{1-az^{-1}} .
> $$
> Same for left-sided pieces: $3^n u[-n+2]=9\cdot3^{\,n-2}u[-(n-2)]$.
> 3. **Transform each piece** with the table and the properties ($n\,x[n]$: differentiate; a finite piece: read the coefficients off as a polynomial in $z$ and $z^{-1}$).
> 4. **ROC of each piece, then intersect.** Right-sided infinite piece: outside its pole. Left-sided: inside its pole. Finite piece: everything, except $z=0$ if it has samples at $n>0$ and $z=\infty$ if it has samples at $n<0$ — the same exclusions apply to an infinite right-sided piece that starts at a negative index ($e^{j\pi n/3}u[n+4]$: $1<\lvert z\rvert<\infty$) and to a left-sided piece that ends at a positive index ($3^n u[-n+2]$: $0<\lvert z\rvert<3$). An empty intersection means the z-transform does not exist.
> 5. **Check:** no pole inside the ROC; poles of right-sided pieces inside the inner boundary, of left-sided pieces outside the outer one; if $z=1$ is in the ROC, $X(1)$ must equal $\sum_n x[n]$ (a 20-second check).

> [!example] Python: an ROC claim is a convergence claim — test it
> ```python
> import numpy as np
>
> # SP2025 #5(c): x[n] = (1/4)^n (2/3)^(n-2) u[n-1] + (4/3)^n u[-n-1], claimed ROC 1/6 < |z| < 4/3
> X = lambda z: (3/8) * z**-1 / (1 - z**-1 / 6) - 1 / (1 - (4/3) * z**-1)
> def partial_sum(z, N):
>     nr, nl = np.arange(1, N + 1), np.arange(-N, 0)
>     return (np.sum(0.25**nr * (2/3)**(nr - 2.0) * z**(-nr.astype(float)))
>             + np.sum((4/3)**nl * z**(-nl.astype(float))))
> z_in = 0.9 * np.exp(0.7j)                        # inside the ROC
> print("inside :", abs(partial_sum(z_in, 400) - X(z_in)))
> z_out = 1.5                                      # outside: |z| > 4/3
> print("outside:", [round(abs(partial_sum(z_out, N))) for N in (20, 40, 80)])
> ```
> ```text
> inside : 1.1102230246251565e-16
> outside: [86, 992, 111278]
> ```
> Inside the ROC the partial sums settle on the closed form; at $\lvert z\rvert=1.5$ the left-sided part grows without bound — even though the formula $X(1.5)$ returns a perfectly finite number. That is Lecture 7's warning: $X(z)$ means nothing outside its ROC.

> [!trap] Where the points go
> - **The shift factor.** $\left(\tfrac34\right)^{n+3}u[n-2]$ is $\left(\tfrac34\right)^5\left(\tfrac34\right)^{n-2}u[n-2]$, so $X=\dfrac{(3/4)^5z^{-2}}{1-\frac34z^{-1}}$ — not $\dfrac{z^{-2}}{1-\frac34z^{-1}}$, and not $(3/4)^3$.
> - **The left-sided sign.** $a^n u[-n-1]\leftrightarrow\dfrac{-1}{1-az^{-1}}$ (minus!), ROC $\lvert z\rvert<\lvert a\rvert$. And $a^n u[-n]$ includes $n=0$: $\sum_{n\le0}a^nz^{-n}=\dfrac{1}{1-a^{-1}z}=\dfrac{-az^{-1}}{1-az^{-1}}$, ROC $\lvert z\rvert<\lvert a\rvert$ (FA2024 #5c writes the second form). If unsure which form you have, check it at one test point.
> - **Forgetting the ROC**, or writing "$\lvert z\rvert>\lvert a\rvert$" for every piece by reflex.
> - **Finite sequences get a "pole" ROC.** $u[n]-u[n-8]$ has $X=\dfrac{1-z^{-8}}{1-z^{-1}}$, whose apparent pole at $z=1$ is cancelled by a zero; the ROC is $z\neq0$, not $\lvert z\rvert>1$.
> - **Missing the $\infty$ exclusion** when a right-sided signal starts at a negative index ($n\,u[n+1]$, $e^{j\pi n/3}u[n+4]$): the ROC is $1<\lvert z\rvert<\infty$.
> - **Complex exponentials have magnitude-1 poles:** $e^{j\omega_0n}u[n]$ has its pole at $e^{j\omega_0}$, so the ROC is $\lvert z\rvert>1$, not $\lvert z\rvert>\omega_0$.
> - **Differentiation property:** $n\,x[n]\leftrightarrow-z\,\frac{dX}{dz}$ — both the minus sign and the factor $z$. For $(n+1)x[n]$ add $X(z)$ back (SP2021 #4).
> - **Two-sided sums that do not converge:** $b^{\lvert n\rvert}$ with $\lvert b\rvert\ge1$ has no z-transform at all.

## Practice problems

> [!question] Practice 1 — shifts, windows, and a two-sided sum
> Find $X(z)$ and the ROC: (a) $\left(\tfrac12\right)^{n+1}u[n-3]$ (b) $(-1)^n\left(u[n+2]-u[n-3]\right)$ (c) $2^n u[-n+1]+\left(\tfrac13\right)^n u[n]$.

> [!success]- Solution
> **(a)** Shift factor: $\left(\tfrac12\right)^{n+1}=\left(\tfrac12\right)^4\left(\tfrac12\right)^{n-3}$, so
> $$
> X(z)=\frac{\frac1{16}z^{-3}}{1-\frac12z^{-1}},\qquad \lvert z\rvert>\tfrac12 .
> $$
> **(b)** A window: samples at $n=-2,\dots,2$ equal to $1,-1,1,-1,1$:
> $$
> X(z)=z^{2}-z+1-z^{-1}+z^{-2},\qquad 0<\lvert z\rvert<\infty
> $$
> (samples at $n<0$ exclude $\infty$, samples at $n>0$ exclude $0$).
>
> **(c)** Left piece: $2^n u[-n+1]=4\cdot2^{\,n-2}u[-(n-2)-1]$, and $2^n u[-n-1]\leftrightarrow\dfrac{-1}{1-2z^{-1}}$ on $\lvert z\rvert<2$, so this piece is $\dfrac{-4z^{-2}}{1-2z^{-1}}$ on $0<\lvert z\rvert<2$. Right piece: $\dfrac{1}{1-\frac13z^{-1}}$ on $\lvert z\rvert>\tfrac13$.
> $$
> X(z)=\frac{1}{1-\frac13z^{-1}}-\frac{4z^{-2}}{1-2z^{-1}},\qquad \tfrac13<\lvert z\rvert<2 .
> $$
> Check at $z=1$ (inside the ROC): $\tfrac32+4=\tfrac{11}{2}$, and directly $\sum_{n\le1}2^n+\sum_{n\ge0}3^{-n}=4+\tfrac32$ ✓.

> [!question] Practice 2 — n·x[n], a damped cosine, and sin²
> (a) $n\left(\tfrac12\right)^n u[n-1]$ (b) $\left(\tfrac12\right)^n\cos\!\left(\tfrac{\pi}{3}n\right)u[n]$ (c) $\sin^2\!\left(\tfrac{\pi}{2}n\right)u[n]$.

> [!success]- Solution
> **(a)** The $n=0$ term is zero anyway, so this is $n\left(\tfrac12\right)^n u[n]$:
> $$
> X(z)=\frac{\frac12z^{-1}}{\left(1-\frac12z^{-1}\right)^2},\qquad \lvert z\rvert>\tfrac12 .
> $$
> **(b)** Euler: $\tfrac12\left(\tfrac12e^{j\pi/3}\right)^n u[n]+\tfrac12\left(\tfrac12e^{-j\pi/3}\right)^n u[n]$; over a common denominator ($2\cdot\tfrac12\cos\tfrac{\pi}{3}=\tfrac12$):
> $$
> X(z)=\frac{1/2}{1-\frac12e^{j\pi/3}z^{-1}}+\frac{1/2}{1-\frac12e^{-j\pi/3}z^{-1}}=\frac{1-\frac14z^{-1}}{1-\frac12z^{-1}+\frac14z^{-2}},\qquad \lvert z\rvert>\tfrac12 .
> $$
> **(c)** $\sin^2\theta=\tfrac12-\tfrac12\cos2\theta$ and $\cos(\pi n)=(-1)^n$:
> $$
> X(z)=\frac{1/2}{1-z^{-1}}-\frac{1/2}{1+z^{-1}}=\frac{z^{-1}}{1-z^{-2}},\qquad \lvert z\rvert>1 .
> $$
> (The sequence is $0,1,0,1,\dots$, i.e. $z^{-1}+z^{-3}+z^{-5}+\cdots$ ✓.)

> [!question] Practice 3 — two-sided exponentials
> (a) $x[n]=\left(\tfrac45\right)^{\lvert n-2\rvert}$ (b) $x[n]=2^{\lvert n\rvert}$.

> [!success]- Solution
> **(a)** First $v[m]=\left(\tfrac45\right)^{\lvert m\rvert}=\left(\tfrac45\right)^m u[m]+\left(\tfrac54\right)^m u[-m-1]$, so $V(z)=\dfrac{1}{1-\frac45z^{-1}}-\dfrac{1}{1-\frac54z^{-1}}$ on $\tfrac45<\lvert z\rvert<\tfrac54$. Then $x[n]=v[n-2]$:
> $$
> X(z)=z^{-2}\left[\frac{1}{1-0.8z^{-1}}-\frac{1}{1-1.25z^{-1}}\right]=\frac{-0.45\,z^{-3}}{\left(1-0.8z^{-1}\right)\left(1-1.25z^{-1}\right)},\qquad 0.8<\lvert z\rvert<1.25 .
> $$
> Check at $z=1$: $5-(-4)=9$, and $\sum_n(0.8)^{\lvert n-2\rvert}=1+2\cdot\frac{0.8}{0.2}=9$ ✓.
>
> **(b)** The right half $2^n u[n]$ needs $\lvert z\rvert>2$; the left half $2^{-n}u[-n-1]=\left(\tfrac12\right)^n u[-n-1]$ needs $\lvert z\rvert<\tfrac12$. The intersection is empty: **no z-transform** (numerically, one of the two partial sums explodes at every radius tried).

All three are verified by partial sums in `verify/problems/z_transform_roc.py`; the snippet is `verify/problems/snippets/z_roc_snippet.py`.

## Related

- [[demos/pole-zero-and-roc-explorer|Pole–zero and ROC explorer]] — place poles, pick a ring, see which sequence you get; [[0-midterm-1/practice-drills|practice drills]] for randomized transform/ROC questions.
- Next step on the exam: [[problems/all-possible-rocs|inverse z / PFE / all possible ROCs]] (the same pairs, read backwards).
- Lectures: [[2-z-transform/06-the-z-transform|Lecture 6]] (definition, ROC, basic pairs), [[2-z-transform/07-z-transform-properties|Lecture 7]] (properties table, ROC rules for sided and finite sequences), [[2-z-transform/08-inverse-z-transform|Lecture 8]] (going back).
- Concepts: [[concepts/z-transform]], [[concepts/region-of-convergence]], [[concepts/z-transform-pairs]], [[concepts/z-transform-properties]], [[concepts/sided-sequences]], [[concepts/poles-and-zeros]]; toolkit: [[0-toolkit/02-geometric-series|geometric series]], [[0-toolkit/01-complex-numbers|complex numbers]]; tables: [[supplements/transform-tables|transform tables]]; all families: [[problems/index|exam problem families]].

### Sources for this page

Lecture 6 notes (exercises 1–2, ROC examples) and Lecture 7 notes (properties table, ROC rules, the $X(\tfrac14)$ warning) and slides; HW3 #1–2 and solutions; FA2025 #5, SP2025 #5, FA2024 #5, FA2023 #5, SP2021 #4, FA2019 #5 with keys (FA2025 #5a denominator and FA2019 #5b exponent corrected, see [[0-toolkit/05-errata|errata]]); Midterm 1 review slides (FA2024 #5); transform tables supplement. Verification: `verify/problems/z_transform_roc.py`.
