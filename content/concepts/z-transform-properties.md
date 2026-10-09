---
title: "z-transform properties"
description: "Shift, linearity, convolution, differentiation, conjugation, time reversal, scaling and Re/Im — what each does to X(z) and to the ROC, when to reach for it, and worked examples from HW3."
tags: [concept, z-transform, roc]
aliases: ["z-transform properties", "properties of the z-transform"]
---

> [!key] The Lecture 7 table (with ROC rules)
> Let $x[n] \leftrightarrow X(z)$ with ROC $R_x$.
>
> | property | signal | z-transform | ROC | use it when |
> |---|---|---|---|---|
> | time shift | $x[n-k]$ | $z^{-k}X(z)$ | $R_x$, except possibly $z=0$ or $\infty$ | delays in an LCCDE; shifted exponentials; finite sequences |
> | linearity | $a x_1[n] + b x_2[n]$ | $aX_1(z)+bX_2(z)$ | at least $R_1\cap R_2$ | splitting a signal into table rows |
> | convolution | $x_1[n]*x_2[n]$ | $X_1(z)X_2(z)$ | at least $R_1\cap R_2$ | LTI outputs $Y=HX$; cascades; $H = Y/X$ |
> | differentiation | $n\,x[n]$ | $-z\,\dfrac{dX(z)}{dz}$ | $R_x$ | factors of $n$, $n^2$; double poles |
> | conjugation | $x^*[n]$ | $X^*(z^*)$ | $R_x$ | complex-valued signals |
> | time reversal | $x[-n]$ | $X(z^{-1})$ | $1/R_x$ | $x[-n]$, $u[-n]$: right-sided ↔ left-sided |
> | scaling | $a^n x[n]$ | $X(z/a)$ | $\lvert a\rvert R_x$ | $a^n$ factors; $e^{j\omega_0 n}x[n]$, $\cos(\omega_0 n)x[n]$ |
> | real part | $\mathrm{Re}\{x[n]\}$ | $\tfrac12\left[X(z)+X^*(z^*)\right]$ | at least $R_x$ | real part of a complex signal |
> | imaginary part | $\mathrm{Im}\{x[n]\}$ | $\tfrac{1}{2j}\left[X(z)-X^*(z^*)\right]$ | at least $R_x$ | imaginary part |
>
> "$1/R_x$": $|z|>a$ becomes $|z|<1/a$. "$|a|R_x$": every pole $p$ moves to $a\,p$, so $|z|>r$ becomes $|z|>|a|r$.

**The two proofs worth knowing** ([[2-z-transform/07-z-transform-properties|Lecture 7]]). Shift: substitute $m = n-k$ in $\sum_n x[n-k]z^{-n}$ to pull out $z^{-k}$. Convolution: write $y[n] = \sum_k x_1[k]x_2[n-k]$, split $z^{-n} = z^{-k}z^{-(n-k)}$, and the double sum factors into $X_1(z)X_2(z)$. Convolution → multiplication is what makes [[concepts/transfer-function|transfer functions]] work.

## Worked example: differentiation (HW3 #2d)

> [!example] $x[n] = \left(\tfrac13\right)^n u[n] \leftrightarrow X(z) = \dfrac{1}{1-\frac13 z^{-1}}$, $|z|>\tfrac13$. Find the transform of $n(n-2)\,x[n-1]$.
> Let $g[n] = x[n-1] \leftrightarrow G(z) = z^{-1}X(z) = \dfrac{1}{z-\frac13}$. Differentiating once and twice,
> $$
> n\,g[n] \leftrightarrow -zG'(z), \qquad n^2 g[n] \leftrightarrow -z\frac{d}{dz}\big(-zG'(z)\big) = zG'(z) + z^2G''(z),
> $$
> with $G'(z) = -\dfrac{1}{(z-\frac13)^2}$ and $G''(z) = \dfrac{2}{(z-\frac13)^3}$. Since $n(n-2)g[n] = n^2g[n] - 2n\,g[n]$:
> $$
> \begin{aligned}
> X_4(z) &= 3zG'(z) + z^2G''(z) = \frac{-3z}{(z-\frac13)^2} + \frac{2z^2}{(z-\frac13)^3}\\[4pt]
> &= \frac{z-z^2}{(z-\frac13)^3} = \frac{z^{-2}-z^{-1}}{\left(1-\frac13 z^{-1}\right)^3}, \qquad |z|>\tfrac13 .
> \end{aligned}
> $$
> A triple pole at $\frac13$: each factor of $n$ raises the pole order by one. Check the first samples: $y[1] = 1\cdot(-1)\,x[0] = -1$, and the series of $\frac{z^{-2}-z^{-1}}{(1-\frac13 z^{-1})^3}$ starts $-z^{-1}+\dots$ ✓.

> [!tip] A shortcut for the same problem
> Substitute $m = n-1$: $n(n-2) = (m+1)(m-1) = m^2-1$, so $n(n-2)x[n-1]$ is $v[n-1]$ with $v[m] = m^2x[m]-x[m]$. Differentiate $X$ twice for $m^2x[m]$, subtract $X$, multiply by $z^{-1}$ — same answer (both routes checked numerically).

## Worked example: time reversal

> [!example] Same $x[n] = \left(\tfrac13\right)^nu[n]$. Find the transform of $x[-n]$.
> $x[-n] = \left(\tfrac13\right)^{-n}u[-n] = 3^n u[-n]$, and
> $$
> X(z^{-1}) = \frac{1}{1-\frac13 z}, \qquad \text{ROC: } |z^{-1}|>\tfrac13 \iff |z|<3 .
> $$
> The pole moved from $\frac13$ to $3$ (reciprocal), and the right-sided ROC became a left-sided one. This agrees with the [[concepts/z-transform-pairs|derived pair]] $a^nu[-n] \leftrightarrow \frac{1}{1-a^{-1}z}$ with $a=3$ (HW3 #1c uses exactly this piece).

> [!success]- All of HW3 #2 (with $X(z) = \frac{1}{1-\frac13 z^{-1}}$, $|z|>\frac13$)
> - (a) $x[n+3] \leftrightarrow \dfrac{z^3}{1-\frac13 z^{-1}}$, $\ \frac13<|z|<\infty$ (the advance loses $z=\infty$).
> - (b) $2^n x[n] = \left(\frac23\right)^n u[n] \leftrightarrow \dfrac{1}{1-\frac23 z^{-1}}$, $|z|>\frac23$ (scaling: the pole moves to $\frac23$).
> - (c) $\cos(\frac{\pi}{4}n)x[n] \leftrightarrow \frac12\left[\dfrac{1}{1-\frac13 e^{j\pi/4}z^{-1}} + \dfrac{1}{1-\frac13 e^{-j\pi/4}z^{-1}}\right] = \dfrac{1-\frac13\cos(\frac{\pi}{4})z^{-1}}{1-\frac23\cos(\frac{\pi}{4})z^{-1}+\frac19 z^{-2}}$, $|z|>\frac13$.
> - (d) $n(n-2)x[n-1] \leftrightarrow \dfrac{z-z^2}{(z-\frac13)^3}$, $|z|>\frac13$ (above).
> - (e) $\left(\frac15\right)^nu[n]*x[n] \leftrightarrow \dfrac{1}{(1-\frac15 z^{-1})(1-\frac13 z^{-1})}$, $|z|>\frac13$.

More from the Lecture 7 slides: $2^n\,n\,(\frac13)^nu[n] = n(\frac23)^nu[n] \leftrightarrow \dfrac{\frac23 z^{-1}}{(1-\frac23 z^{-1})^2}$, $|z|>\frac23$ (scaling, then differentiation); and SP2021 #4 asks for $(n+1)x[n]$ with $X = \frac{1}{1-\frac12 z^{-1}}$: $-zX'(z) + X(z) = \dfrac{\frac12 z^{-1}}{(1-\frac12 z^{-1})^2} + \dfrac{1}{1-\frac12 z^{-1}}$, $|z|>\frac12$.

> [!trap]
> - **Shift changes the ROC only at $0$ and $\infty$**: a delay can add $z^{-k}$ (loses $z=0$), an advance adds $z^{k}$ (loses $z=\infty$).
> - **Scaling moves the poles** ($p \to ap$) and scales the ROC by $|a|$ — it does not scale $X$ itself. $e^{j\omega_0 n}x[n]$ rotates the pole-zero plot by $\omega_0$ and keeps the ROC.
> - **Time reversal inverts the ROC**: $|z|>\frac13$ becomes $|z|<3$, not $|z|<\frac13$.
> - **Differentiation**: it is $-z\,\frac{d}{dz}$ — keep the $-z$, and apply the product rule when differentiating twice. Differentiating in $z^{-1}$ instead of $z$ flips signs and powers.
> - **Linearity and convolution give "at least" the intersection**: a [[concepts/pole-zero-cancellation|cancellation]] can enlarge the ROC (Lecture 7 slide Example 2 with $c=-1$).
> - The Lecture 7 table prints the imaginary-part row as $\frac12[X(z)-X^*(z^*)]$; the factor must be $\frac{1}{2j}$ (checked numerically — see [[0-toolkit/05-errata|errata]]).

**Where it appears.**
- Lectures: [[2-z-transform/07-z-transform-properties|L7]] (table, proofs, slide Examples 2–3), [[2-z-transform/09-transfer-functions|L9]] (shift + linearity turn an LCCDE into $H(z)$), [[2-z-transform/10-improper-transfer-functions-and-system-algebra|L10]] (convolution → system algebra).
- Problem families: [[problems/z-transform-with-roc]], [[problems/infinite-length-convolution]] (convolution property), [[problems/lccde-to-transfer-function-and-response]], [[problems/finding-h-from-input-output-pairs]] ($H = Y/X$).
- Homework: [[homework/hw3|HW3]] #1–#2.
- Past exams: [[exams/midterm-1/past-exams/spring-2021|SP2021 #4]] (differentiation), [[exams/midterm-1/past-exams/fall-2024|FA2024 #5a]] ($(n+1)u[n-1]$), [[exams/midterm-1/past-exams/fall-2023|FA2023 #5]] ($n\,u[n+1]$), [[exams/midterm-1/past-exams/spring-2025|SP2025 #5]] (shift, time reversal), [[exams/midterm-1/past-exams/fall-2025|FA2025 #5]] (shift, Euler + linearity), [[exams/midterm-1/past-exams/fall-2019|FA2019 #5]].

Related: [[concepts/z-transform]] · [[concepts/z-transform-pairs]] · [[concepts/region-of-convergence]] · [[concepts/convolution]] · [[concepts/transfer-function]] · [[concepts/pole-zero-cancellation]]

### Sources for this page
Lecture 7 notes §2 (properties, proofs, Table 1) and slides (Examples 2–3, summary table); HW3 #2 and its solution (the $G(z) = \frac{1}{z-\frac13}$ route); SP2021 #4 key; `review.pdf` property table; `transform_tables.pdf` Table 9. Verification: `verify/concepts/verify_properties.py` (16/16, including the $\frac{1}{2j}$ check) and `verify_zdomain_extra.py`.
