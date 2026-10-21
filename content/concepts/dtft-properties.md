---
title: "DTFT properties"
description: "Shift, modulation, reversal, conjugation, differentiation, convolution, windowing; periodicity, symmetries, Parseval; four free numbers; the sign erratum in Lecture 14's differentiation row."
tags: [concept, dtft, midterm-2]
aliases: ["DTFT properties", "properties of the DTFT", "DTFT property table"]
---

> [!key] Property table (Lecture 14, Table 2 — differentiation sign corrected)
> | property | signal | DTFT |
> |---|---|---|
> | linearity | $a\,x_1[n]+b\,x_2[n]$ | $aX_1(\omega)+bX_2(\omega)$ |
> | periodicity | any $x[n]$ | $X_d(\omega+2\pi k)=X_d(\omega)$ |
> | time shift | $x[n-k]$ ($k\in\mathbb{Z}$) | $e^{-j\omega k}X_d(\omega)$ |
> | frequency shift | $e^{j\omega_0 n}x[n]$ | $X_d(\omega-\omega_0)$ |
> | modulation | $x[n]\cos(\omega_0 n)$ | $\tfrac12X_d(\omega-\omega_0)+\tfrac12X_d(\omega+\omega_0)$ |
> | time reversal | $x[-n]$ | $X_d(-\omega)$ |
> | conjugation | $x^*[n]$ | $X_d^*(-\omega)$ |
> | differentiation | $n\,x[n]$ | $+j\,\dfrac{dX_d(\omega)}{d\omega}$ |
> | convolution | $x[n]*h[n]$ | $X_d(\omega)H_d(\omega)$ |
> | windowing | $x[n]\,w[n]$ | $\dfrac{1}{2\pi}\displaystyle\int_{-\pi}^{\pi}X_d(\theta)\,W_d(\omega-\theta)\,d\theta$ |
> | Hermitian symmetry | $x[n]$ real | $X_d^*(\omega)=X_d(-\omega)$ |
> | Parseval | $\sum_n\lvert x[n]\rvert^2$ | $\dfrac{1}{2\pi}\displaystyle\int_{-\pi}^{\pi}\lvert X_d(\omega)\rvert^2d\omega$ |

> [!warning] Erratum: $n\,x[n]\leftrightarrow+j\,\frac{dX_d}{d\omega}$, not $-j$
> Lecture 14 Table 2 and slide 15 print $-j$. $\frac{dX_d}{d\omega}=-j\sum_n n\,x[n]e^{-j\omega n}$, so the sign is $+j$ (transform tables Table 5 agree). See [[0-toolkit/05-errata|errata]].

| $x[n]$ | $X_d(\omega)$ |
|---|---|
| real | Hermitian: $\lvert X_d\rvert$ even, $\angle X_d$ odd; $X_d(0)$, $X_d(\pi)$ real |
| real and even | real and even |
| real and odd | purely imaginary and odd |
| conjugate-symmetric, $x[-n]=x^*[n]$ | real |

> [!recipe] Four numbers without computing $X_d(\omega)$
> $$
> \begin{gathered}
> X_d(0)=\sum_n x[n],\qquad X_d(\pi)=\sum_n(-1)^n x[n],\\
> \int_{-\pi}^{\pi}X_d(\omega)\,d\omega=2\pi\,x[0],\qquad \int_{-\pi}^{\pi}\lvert X_d(\omega)\rvert^2d\omega=2\pi\sum_n\lvert x[n]\rvert^2 .
> \end{gathered}
> $$
> [[homework/hw5|HW5]] #2: $x=\{2,-1,\underset{\uparrow}{1},-1,2\}$ gives $3$, $7$, $2\pi$, $22\pi$.

> [!trap]
> - Integer shifts only; $e^{-j\omega k}$ with non-integer $k$ is a shifted sinc.
> - Conjugation flips $\omega$ too: $x^*[n]\leftrightarrow X_d^*(-\omega)$.
> - Modulation halves heights; copies past $\pm\pi$ wrap and can overlap ([[exams/midterm-2/past-exams/spring-2025|SP2025 MT2]] #2(b)).
> - Real test: magnitude even and phase odd on the whole period ([[exams/midterm-2/past-exams/fall-2024|FA2024 MT2]] #4(a), [[homework/hw6|HW6]] #7).

**Where it appears:** [[3-fourier-analysis/14-dtft-properties|L14]], [[3-fourier-analysis/15-frequency-response|L15]], [[3-fourier-analysis/16-magnitude-and-phase-response|L16]]; [[problems/dtft-and-inverse-dtft|DTFT family]]; [[homework/hw5|HW5]] #1–#2, [[homework/hw6|HW6]] #2, #7.

## Related
[[concepts/dtft|DTFT]] · [[concepts/dtft-pairs|DTFT pairs]] · [[concepts/z-transform-properties|z-transform properties]] · [[concepts/frequency-response|frequency response]]

### Sources for this page
Lecture 14 notes §3 (eqs. 26–51), Table 2, slides 10–15; transform tables Table 5; HW5 #1–#2 solutions; Midterm 2 keys cited.
