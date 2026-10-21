---
title: "z-transform properties"
description: "Shift, linearity, convolution, differentiation, conjugation, time reversal, scaling, Re/Im: what each does to X(z) and the ROC, with HW3 #2 worked."
tags: [concept, z-transform, roc]
aliases: ["z-transform properties", "properties of the z-transform"]
---

> [!key] Lecture 7 table ($x[n] \leftrightarrow X(z)$, ROC $R_x$)
> | property | signal | z-transform | ROC |
> |---|---|---|---|
> | time shift | $x[n-k]$ | $z^{-k}X(z)$ | $R_x$, except possibly $z=0$ or $\infty$ |
> | linearity | $a x_1[n] + b x_2[n]$ | $aX_1(z)+bX_2(z)$ | at least $R_1\cap R_2$ |
> | convolution | $x_1[n]*x_2[n]$ | $X_1(z)X_2(z)$ | at least $R_1\cap R_2$ |
> | differentiation | $n\,x[n]$ | $-z\,\dfrac{dX(z)}{dz}$ | $R_x$ |
> | conjugation | $x^*[n]$ | $X^*(z^*)$ | $R_x$ |
> | time reversal | $x[-n]$ | $X(z^{-1})$ | $1/R_x$ |
> | scaling | $a^n x[n]$ | $X(z/a)$ | $\lvert a\rvert R_x$ |
> | real part | $\mathrm{Re}\{x[n]\}$ | $\tfrac12\left[X(z)+X^*(z^*)\right]$ | at least $R_x$ |
> | imaginary part | $\mathrm{Im}\{x[n]\}$ | $\tfrac{1}{2j}\left[X(z)-X^*(z^*)\right]$ | at least $R_x$ |
>
> The Lecture 7 table prints $\frac12$ in the imaginary-part row; the factor is $\frac{1}{2j}$ ([[0-toolkit/05-errata|errata]]).

> [!example] HW3 #2: $X(z) = \frac{1}{1-\frac13 z^{-1}}$, $|z|>\frac13$
> Transform (a) $x[n+3]$, (b) $2^n x[n]$, (c) $\cos(\frac{\pi}{4}n)x[n]$, (d) $n(n-2)x[n-1]$, (e) $\left(\frac15\right)^nu[n]*x[n]$; also $x[-n]$.

> [!success]- Answers
> - (a) $\dfrac{z^3}{1-\frac13 z^{-1}}$, $\ \frac13<|z|<\infty$.
> - (b) $\dfrac{1}{1-\frac23 z^{-1}}$, $|z|>\frac23$.
> - (c) $\dfrac{1-\frac13\cos(\frac{\pi}{4})z^{-1}}{1-\frac23\cos(\frac{\pi}{4})z^{-1}+\frac19 z^{-2}}$, $|z|>\frac13$.
> - (d) $G(z)=z^{-1}X(z)=\frac{1}{z-\frac13}$; $n(n-2)g[n]\leftrightarrow 3zG'(z) + z^2G''(z)$:
> $$
> \frac{z-z^2}{(z-\frac13)^3} = \frac{z^{-2}-z^{-1}}{\left(1-\frac13 z^{-1}\right)^3}, \qquad |z|>\tfrac13 .
> $$
> - (e) $\dfrac{1}{(1-\frac15 z^{-1})(1-\frac13 z^{-1})}$, $|z|>\frac13$.
> - $x[-n]=3^nu[-n]\leftrightarrow\dfrac{1}{1-\frac13 z}$, $|z|<3$.

> [!trap]
> - Shift changes the ROC only at $0$ and $\infty$.
> - Scaling moves poles $p\to ap$; $e^{j\omega_0 n}x[n]$ rotates the pole-zero plot.
> - Time reversal inverts the ROC: $|z|>\frac13$ becomes $|z|<3$.
> - Differentiation is $-z\,\frac{d}{dz}$ in $z$, not $z^{-1}$; product rule when applied twice.

**Where it appears:** [[2-z-transform/07-z-transform-properties|L7]], [[2-z-transform/09-transfer-functions|L9]], [[2-z-transform/10-improper-transfer-functions-and-system-algebra|L10]]; [[problems/z-transform-with-roc]], [[problems/infinite-length-convolution]]; [[homework/hw3|HW3]] #1–#2; [[exams/midterm-1/past-exams/spring-2021|SP2021 #4]], [[exams/midterm-1/past-exams/fall-2023|FA2023 #5]].

## Related
[[concepts/z-transform]] · [[concepts/z-transform-pairs]] · [[concepts/region-of-convergence]] · [[concepts/convolution]] · [[concepts/pole-zero-cancellation]]

### Sources for this page
Lecture 7 notes §2 (Table 1), slides (Examples 2–3); HW3 #2 solution; SP2021 #4 key; transform tables Table 9.
