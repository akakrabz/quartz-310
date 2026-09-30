---
title: "Official transform tables"
description: "The course's z-transform properties and pairs tables (transform_tables.pdf, Tables 9 and 10) typed out and checked numerically — including the missing minus sign in pair 3 — with the DTFT tables folded away as after-Midterm-1 material."
tags: [supplement, z-transform, roc, midterm-1]
---

*Supplement · `suppliment/transform_tables.pdf` (10 pages) · used by [[2-z-transform/06-the-z-transform|Lecture 6]], [[2-z-transform/07-z-transform-properties|Lecture 7]] and [[2-z-transform/08-inverse-z-transform|Lecture 8]]*

The course's reference sheet is the standard set of ten tables from Oppenheim & Willsky, *Signals and Systems*: Fourier series (Tables 1–2), CT Fourier transform (3–4), **DTFT (5–6)**, Laplace (7–8) and **z-transform (9–10)**. For Midterm 1 only Tables 9 and 10 matter; the DTFT tables become relevant after the midterm, and Tables 1–4 and 7–8 are continuous-time background from earlier courses.

Every z-transform pair below was checked by summing the series directly at three test points inside the ROC, and every property on test signals (`verify/hub/supp_tables.py`, 45 checks).

## Table 10 — common z-transform pairs (PDF p. 10)

| # | signal | transform | ROC |
|---|---|---|---|
| 1 | $\delta[n]$ | $1$ | all $z$ |
| 2 | $u[n]$ | $\dfrac{1}{1-z^{-1}}$ | $\lvert z\rvert>1$ |
| 3 | $-u[-n-1]$ ⚠ | $\dfrac{1}{1-z^{-1}}$ | $\lvert z\rvert<1$ |
| 4 | $\delta[n-m]$ | $z^{-m}$ | all $z$ except $0$ (if $m>0$) or $\infty$ (if $m<0$) |
| 5 | $\alpha^n u[n]$ | $\dfrac{1}{1-\alpha z^{-1}}$ | $\lvert z\rvert>\lvert\alpha\rvert$ |
| 6 | $-\alpha^n u[-n-1]$ | $\dfrac{1}{1-\alpha z^{-1}}$ | $\lvert z\rvert<\lvert\alpha\rvert$ |
| 7 | $n\alpha^n u[n]$ | $\dfrac{\alpha z^{-1}}{(1-\alpha z^{-1})^2}$ | $\lvert z\rvert>\lvert\alpha\rvert$ |
| 8 | $-n\alpha^n u[-n-1]$ | $\dfrac{\alpha z^{-1}}{(1-\alpha z^{-1})^2}$ | $\lvert z\rvert<\lvert\alpha\rvert$ |
| 9 | $[\cos\omega_0 n]\,u[n]$ | $\dfrac{1-[\cos\omega_0]z^{-1}}{1-[2\cos\omega_0]z^{-1}+z^{-2}}$ | $\lvert z\rvert>1$ |
| 10 | $[\sin\omega_0 n]\,u[n]$ | $\dfrac{[\sin\omega_0]z^{-1}}{1-[2\cos\omega_0]z^{-1}+z^{-2}}$ | $\lvert z\rvert>1$ |
| 11 | $[r^n\cos\omega_0 n]\,u[n]$ | $\dfrac{1-[r\cos\omega_0]z^{-1}}{1-[2r\cos\omega_0]z^{-1}+r^2z^{-2}}$ | $\lvert z\rvert>r$ |
| 12 | $[r^n\sin\omega_0 n]\,u[n]$ | $\dfrac{[r\sin\omega_0]z^{-1}}{1-[2r\cos\omega_0]z^{-1}+r^2z^{-2}}$ | $\lvert z\rvert>r$ |

> [!warning] ⚠ Pair 3 is misprinted in the PDF
> The official table prints "$u[-n-1] \leftrightarrow \dfrac{1}{1-z^{-1}}$, $\lvert z\rvert<1$". The correct pair has a minus sign: $-u[-n-1] \leftrightarrow \dfrac{1}{1-z^{-1}}$ (it is pair 6 with $\alpha = 1$). Direct check at $z = \tfrac12$: $\sum_{n\le-1}(-1)\,z^{-n} = -\sum_{m\ge1}(\tfrac12)^m = -1 = \dfrac{1}{1-2}$. Lecture 6's table and the [[supplements/course-summary|course summary]] have it right. Listed with the other slips in [[0-toolkit/05-errata|errata]].

```python
import numpy as np
z = 0.5                                    # inside the ROC |z| < 1
n = np.arange(-200, 0)                     # u[-n-1] is 1 for n <= -1
print(np.sum(-1.0 * z ** (-n.astype(float))))   # Z{-u[-n-1]} by direct summation
print(1 / (1 - 1 / z))                     # table formula 1/(1 - z^-1)
```

```text
-1.0
-1.0
```

**Reading the table like the exam does:** pairs 5/6 and 7/8 have identical formulas — the ROC alone picks the signal. Pairs 9–12 are pairs 5–6 with complex-conjugate $\alpha = re^{\pm j\omega_0}$ combined over a common denominator ([[0-toolkit/01-complex-numbers|complex numbers]]); on the exam it is often faster to split $\cos$ into two exponentials than to match pair 9. The transforms are all written in powers of $z^{-1}$, which is the form the [[concepts/partial-fraction-expansion|PFE]] cover-up rule wants. See [[concepts/z-transform-pairs|z-transform pairs]].

## Table 9 — properties of the z-transform (PDF p. 9)

Signals $x[n]\leftrightarrow X(z)$ with ROC $R$, $x_1[n]\leftrightarrow X_1(z)$ with $R_1$, $x_2[n]\leftrightarrow X_2(z)$ with $R_2$.

| property | sequence | transform | ROC |
|---|---|---|---|
| linearity | $a x_1[n] + b x_2[n]$ | $aX_1(z) + bX_2(z)$ | at least $R_1\cap R_2$ |
| time shifting | $x[n-n_0]$ | $z^{-n_0}X(z)$ | $R$, except for the possible addition or deletion of the origin (and, for an advance $n_0<0$, of $\infty$ — Lecture 7 says "except $z=0$ or $z=\infty$") |
| scaling in the z-domain | $e^{j\omega_0 n}x[n]$ | $X(e^{-j\omega_0}z)$ | $R$ |
| | $z_0^n x[n]$ | $X(z/z_0)$ | $\lvert z_0\rvert R$ |
| | $a^n x[n]$ | $X(a^{-1}z)$ | scaled version of $R$: $\lvert a\rvert R$ |
| time reversal | $x[-n]$ | $X(z^{-1})$ | inverted $R$: the points $1/z$ for $z$ in $R$ |
| time expansion | $x_{(k)}[n] = x[r]$ if $n = rk$, $0$ otherwise | $X(z^k)$ | $R^{1/k}$ |
| conjugation | $x^*[n]$ | $X^*(z^*)$ | $R$ |
| convolution | $x_1[n] * x_2[n]$ | $X_1(z)X_2(z)$ | at least $R_1\cap R_2$ |
| first difference | $x[n] - x[n-1]$ | $(1-z^{-1})X(z)$ | at least $R\cap\{\lvert z\rvert>0\}$ |
| accumulation | $\sum_{k=-\infty}^{n}x[k]$ | $\dfrac{1}{1-z^{-1}}X(z)$ | at least $R\cap\{\lvert z\rvert>1\}$ |
| differentiation in the z-domain | $n\,x[n]$ | $-z\dfrac{dX(z)}{dz}$ | $R$ |

**Initial value theorem:** if $x[n] = 0$ for $n<0$, then $x[0] = \lim_{z\to\infty}X(z)$ — a free check on every causal answer (e.g. $h[0] = C_0 + \sum A_k$ after a PFE; see [[0-toolkit/04-factoring-and-long-division|long division]]).

Two more rows appear in Lecture 7's table and are used for complex signals: $\mathrm{Re}\{x[n]\}\leftrightarrow\tfrac12\big[X(z)+X^*(z^*)\big]$ and $\mathrm{Im}\{x[n]\}\leftrightarrow\tfrac{1}{2j}\big[X(z)-X^*(z^*)\big]$, ROC at least $R$ (the notes print $\tfrac12$ for the second — the $j$ is needed).

> [!trap] "At least" matters
> Linearity and convolution give *at least* the intersection: a pole can be cancelled by a zero and the ROC grows. That is exactly the mechanism of [[concepts/pole-zero-cancellation|pole-zero cancellation]] problems (FA2025 #6, SP2025 #8, SP2021 #7, FA2019 #10). And the accumulator adds a pole at $z=1$, so $\lvert z\rvert>1$ is imposed.

## After Midterm 1: the DTFT tables

The course writes the DTFT as $X_d(\omega)$; the tables write $X(e^{j\omega})$ — the same function, $X_d(\omega) = X(z)\big|_{z=e^{j\omega}}$ when the ROC contains the unit circle ([[supplements/notation-translation|notation translation]]). **Not on Midterm 1.**

> [!note]- Table 5 — properties of the DTFT (PDF p. 5)
> $x[n] = \dfrac{1}{2\pi}\displaystyle\int_{2\pi}X(e^{j\omega})e^{j\omega n}\,d\omega$, $\quad X(e^{j\omega}) = \displaystyle\sum_{n=-\infty}^{\infty}x[n]e^{-j\omega n}$ (periodic with period $2\pi$).
>
> | property | signal | DTFT |
> |---|---|---|
> | linearity | $ax[n] + by[n]$ | $aX(e^{j\omega}) + bY(e^{j\omega})$ |
> | time shifting | $x[n-n_0]$ | $e^{-j\omega n_0}X(e^{j\omega})$ |
> | frequency shifting | $e^{j\omega_0 n}x[n]$ | $X(e^{j(\omega-\omega_0)})$ |
> | conjugation | $x^*[n]$ | $X^*(e^{-j\omega})$ |
> | time reversal | $x[-n]$ | $X(e^{-j\omega})$ |
> | time expansion | $x_{(k)}[n] = x[n/k]$ if $k$ divides $n$, else $0$ | $X(e^{jk\omega})$ |
> | convolution | $x[n]*y[n]$ | $X(e^{j\omega})Y(e^{j\omega})$ |
> | multiplication | $x[n]y[n]$ | $\dfrac{1}{2\pi}\displaystyle\int_{2\pi}X(e^{j\theta})Y(e^{j(\omega-\theta)})\,d\theta$ |
> | differencing in time | $x[n]-x[n-1]$ | $(1-e^{-j\omega})X(e^{j\omega})$ |
> | accumulation | $\sum_{k=-\infty}^{n}x[k]$ | $\dfrac{X(e^{j\omega})}{1-e^{-j\omega}} + \pi X(e^{j0})\displaystyle\sum_{k}\delta(\omega-2\pi k)$ |
> | differentiation in frequency | $n\,x[n]$ | $j\dfrac{dX(e^{j\omega})}{d\omega}$ |
> | conjugate symmetry, $x$ real | | $X(e^{j\omega}) = X^*(e^{-j\omega})$: $\mathrm{Re}$ and $\lvert X\rvert$ even, $\mathrm{Im}$ and $\angle X$ odd |
> | $x$ real and even | | $X(e^{j\omega})$ real and even |
> | $x$ real and odd | | $X(e^{j\omega})$ purely imaginary and odd |
> | even–odd parts, $x$ real | $x_e[n]$, $x_o[n]$ | $\mathrm{Re}\{X(e^{j\omega})\}$, $j\,\mathrm{Im}\{X(e^{j\omega})\}$ |
>
> Parseval: $\displaystyle\sum_{n=-\infty}^{\infty}\lvert x[n]\rvert^2 = \frac{1}{2\pi}\int_{2\pi}\lvert X(e^{j\omega})\rvert^2\,d\omega$.

> [!note]- Table 6 — basic DTFT pairs (PDF p. 6)
> | signal | DTFT |
> |---|---|
> | $\delta[n]$ | $1$ |
> | $\delta[n-n_0]$ | $e^{-j\omega n_0}$ |
> | $a^n u[n]$, $\lvert a\rvert<1$ | $\dfrac{1}{1-ae^{-j\omega}}$ |
> | $(n+1)a^n u[n]$, $\lvert a\rvert<1$ | $\dfrac{1}{(1-ae^{-j\omega})^2}$ |
> | $\dfrac{(n+r-1)!}{n!\,(r-1)!}a^n u[n]$, $\lvert a\rvert<1$ | $\dfrac{1}{(1-ae^{-j\omega})^r}$ |
> | $x[n] = 1$ for $\lvert n\rvert\le N_1$, $0$ otherwise | $\dfrac{\sin[\omega(N_1+\frac12)]}{\sin(\omega/2)}$ |
> | $\dfrac{\sin Wn}{\pi n} = \dfrac{W}{\pi}\,\mathrm{sinc}\Big(\dfrac{Wn}{\pi}\Big)$, $0<W<\pi$ | $1$ for $0\le\lvert\omega\rvert\le W$, $0$ for $W<\lvert\omega\rvert\le\pi$, periodic with period $2\pi$ |
> | $u[n]$ | $\dfrac{1}{1-e^{-j\omega}} + \displaystyle\sum_{k}\pi\,\delta(\omega-2\pi k)$ |
> | $x[n] = 1$ (all $n$) | $2\pi\displaystyle\sum_{l}\delta(\omega-2\pi l)$ |
> | $e^{j\omega_0 n}$ | $2\pi\displaystyle\sum_{l}\delta(\omega-\omega_0-2\pi l)$ |
> | $\cos\omega_0 n$ | $\pi\displaystyle\sum_{l}\big[\delta(\omega-\omega_0-2\pi l)+\delta(\omega+\omega_0-2\pi l)\big]$ |
> | $\sin\omega_0 n$ | $\dfrac{\pi}{j}\displaystyle\sum_{l}\big[\delta(\omega-\omega_0-2\pi l)-\delta(\omega+\omega_0-2\pi l)\big]$ |
> | $\sum_{k}\delta[n-kN]$ | $\dfrac{2\pi}{N}\displaystyle\sum_{k}\delta\Big(\omega-\dfrac{2\pi k}{N}\Big)$ |
> | periodic $\sum_{k=\langle N\rangle}a_k e^{jk(2\pi/N)n}$ | $2\pi\displaystyle\sum_{k}a_k\,\delta\Big(\omega-\dfrac{2\pi k}{N}\Big)$ |
>
> The PDF's third column (Fourier-series coefficients of the periodic signals, including the periodic square wave) is DTFS material and is not repeated here. The aperiodic pairs and all Table 5 properties were checked numerically in `verify/hub/supp_tables.py`.

## Related

[[concepts/z-transform|z-transform]] · [[concepts/z-transform-properties|z-transform properties]] · [[concepts/region-of-convergence|ROC]] · [[concepts/inverse-z-transform|inverse z-transform]] · [[problems/z-transform-with-roc|z-transform with ROC]] · [[0-toolkit/02-geometric-series|geometric series]] (where every pair comes from) · [[3-beyond-midterm-1/index|beyond Midterm 1]] (DTFT).

### Sources for this page

`suppliment/transform_tables.pdf` Tables 5, 6, 9, 10 (pages 5, 6, 9, 10; page 10 rendered to confirm pair 3); Lecture 6 notes Table 1 and Lecture 7 notes Table 1; `suppliment/review.pdf` p. 3. Checked in `verify/hub/supp_tables.py`.
