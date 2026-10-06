---
title: "DTFT properties"
description: "What shifting, modulating, reversing, conjugating, differentiating, convolving and windowing a sequence do to its DTFT; 2π-periodicity, Hermitian and other symmetries, Parseval; the four numbers you can read off without computing X_d(ω); and the sign erratum in the lecture's differentiation row."
tags: [concept, dtft, midterm-2]
aliases: ["DTFT properties", "properties of the DTFT", "DTFT property table"]
---

> [!key] The property table (Lecture 14, Table 2 — differentiation sign corrected)
> Let $x[n]\leftrightarrow X_d(\omega)$, $h[n]\leftrightarrow H_d(\omega)$, $w[n]\leftrightarrow W_d(\omega)$.
>
> | property | signal | DTFT | use it when |
> |---|---|---|---|
> | linearity | $a\,x_1[n]+b\,x_2[n]$ | $aX_1(\omega)+bX_2(\omega)$ | splitting a signal into table rows |
> | periodicity | any $x[n]$ | $X_d(\omega+2\pi k)=X_d(\omega)$ | values outside $[-\pi,\pi]$ |
> | time shift | $x[n-k]$ ($k\in\mathbb{Z}$) | $e^{-j\omega k}X_d(\omega)$ | delays; the midpoint trick; linear phase |
> | frequency shift | $e^{j\omega_0 n}x[n]$ | $X_d(\omega-\omega_0)$ | complex exponential factors |
> | modulation | $x[n]\cos(\omega_0 n)$ | $\tfrac12X_d(\omega-\omega_0)+\tfrac12X_d(\omega+\omega_0)$ | cosine factors; band-pass from low-pass |
> | time reversal | $x[-n]$ | $X_d(-\omega)$ | flipped sequences |
> | conjugation | $x^*[n]$ | $X_d^*(-\omega)$ | complex sequences; symmetry tests |
> | differentiation | $n\,x[n]$ | $+j\,\dfrac{dX_d(\omega)}{d\omega}$ | factors of $n$ |
> | convolution | $x[n]*h[n]$ | $X_d(\omega)H_d(\omega)$ | LTI outputs ([[concepts/frequency-response\|frequency response]]) |
> | windowing | $x[n]\,w[n]$ | $\dfrac{1}{2\pi}\displaystyle\int_{-\pi}^{\pi}X_d(\theta)\,W_d(\omega-\theta)\,d\theta$ | products of signals (not LTI!) |
> | Hermitian symmetry | $x[n]$ real | $X_d^*(\omega)=X_d(-\omega)$ | deciding whether a signal or system is real |
> | Parseval | $\sum_n\lvert x[n]\rvert^2$ | $\dfrac{1}{2\pi}\displaystyle\int_{-\pi}^{\pi}\lvert X_d(\omega)\rvert^2d\omega$ | energy; $\int\lvert X_d\rvert^2$ questions |
>
> The first block is the [[concepts/z-transform-properties|z-transform table]] at $z=e^{j\omega}$ (shift: $z^{-k}$; frequency shift: $a^nx[n]\leftrightarrow X(z/a)$ with $a=e^{j\omega_0}$; reversal: $X(1/z)$; conjugation: $X^*(z^*)$; differentiation: $-z\frac{dX}{dz}$; convolution: $XH$). Windowing and Parseval only make sense in frequency.

> [!warning] Erratum: $n\,x[n]\leftrightarrow+j\,\frac{dX_d}{d\omega}$, not $-j$
> The Lecture 14 notes (Table 2) and slides (slide 15) print $-j\,\frac{dX_d(\omega)}{d\omega}$. Differentiating $X_d(\omega)=\sum_n x[n]e^{-j\omega n}$ term by term gives $\frac{dX_d}{d\omega}=-j\sum_n n\,x[n]e^{-j\omega n}$, hence $\sum_n n\,x[n]e^{-j\omega n}=+j\frac{dX_d}{d\omega}$. Test: $n\,a^nu[n]$ must give $\frac{ae^{-j\omega}}{(1-ae^{-j\omega})^2}$ (the z-pair on the unit circle), and only $+j$ does. The official `transform_tables.pdf` (Table 5) has $+j$. See [[0-toolkit/05-errata|errata]].

## The proofs worth knowing

- **Periodicity:** $e^{-j(\omega+2\pi k)n}=e^{-j\omega n}$ because $e^{-j2\pi kn}=1$ for integer $n$, $k$.
- **Time shift:** substitute $m=n-k$; out comes $e^{-j\omega k}$. The magnitude is unchanged; the phase gains the line $-\omega k$, the origin of [[concepts/group-delay|group delay]].
- **Frequency shift:** $x[n]e^{j\omega_0 n}e^{-j\omega n}=x[n]e^{-j(\omega-\omega_0)n}$. Modulation is Euler's formula plus this, twice.
- **Windowing:** replace $x[n]$ by its inverse DTFT and swap sum and integral; the inner sum is $W_d(\omega-\theta)$ (notes eqs. 47–51).
- **Parseval** is windowing with $w=x^*$ read at $\omega=0$: $\sum_n x[n]x^*[n]=\frac{1}{2\pi}\int X_d(\theta)X_d^*(\theta)\,d\theta$.

## Symmetry

> [!key] Symmetries of $x[n]$ and of $X_d(\omega)$
> | $x[n]$ | $X_d(\omega)$ |
> |---|---|
> | real | Hermitian, $X_d(-\omega)=X_d^*(\omega)$: $\lvert X_d\rvert$ and $\mathrm{Re}\,X_d$ even, $\angle X_d$ and $\mathrm{Im}\,X_d$ odd; $X_d(0)$, $X_d(\pi)$ real |
> | real and even | real and even |
> | real and odd | purely imaginary and odd |
> | purely imaginary | anti-Hermitian, $X_d(-\omega)=-X_d^*(\omega)$ |
> | even, $x[-n]=x[n]$ (possibly complex) | even, $X_d(-\omega)=X_d(\omega)$ |
> | conjugate-symmetric, $x[-n]=x^*[n]$ | real |
>
> Each line is "if and only if" (slide 11 stresses it for the first). All follow from the reversal and conjugation rows: $x^*[-n]\leftrightarrow X_d^*(\omega)$%%hw6:IChbW2hvbWV3b3JrL2h3NnxIVzZdXSAjMik=%%%%/hw6%%.

> [!recipe] Is $x[n]$ (or $h[n]$) real? Read it off $X_d(\omega)$
> 1. Use the formula on the whole period $-\pi\le\omega\le\pi$.
> 2. Compare $X_d(-\omega)$ with $X_d^*(\omega)$: equal everywhere ⇒ real.
> 3. In polar form with a nonnegative magnitude: real ⇔ magnitude even and phase odd (mod $2\pi$). A sign is phase: $\omega=|\omega|e^{j\pi}$ for $\omega\lt0$.
> 4. Quick checks: $X_d(0)$ and $X_d(\pi)$ real; the formula must agree with itself at $\omega=\pm\pi$.
>
> Lecture 14 slide 12 ($\omega^2e^{j\cos\omega}$: phase even ⇒ not real), [[exams/midterm-2/past-exams/fall-2019|FA2019 MT2]] #6 ($e^{-j\omega^2/3}$ ⇒ not real), [[exams/midterm-2/past-exams/fall-2024|FA2024 MT2]] #4(a) ($|\omega|e^{-j\pi\sin\omega}$ ⇒ real)%%hw6:LCBbW2hvbWV3b3JrL2h3NnxIVzZdXSAjNyAoJFxvbWVnYSBlXntqXHNpblxvbWVnYX0kIOKHkiBhbnRpLUhlcm1pdGlhbiwgcHVyZWx5IGltYWdpbmFyeSAkaCQp%%%%/hw6%%.

## Four numbers without computing $X_d(\omega)$

> [!recipe] Evaluate the definitions instead
> $$
> X_d(0)=\sum_n x[n],\qquad X_d(\pi)=\sum_n(-1)^n x[n],\qquad \int_{-\pi}^{\pi}X_d(\omega)\,d\omega=2\pi\,x[0],\qquad \int_{-\pi}^{\pi}\lvert X_d(\omega)\rvert^2d\omega=2\pi\sum_n\lvert x[n]\rvert^2 .
> $$

> [!example] HW5 #2 and FA2023 MT2 #2
> $x=\{2,-1,\underset{\uparrow}{1},-1,2\}$: $X_d(0)=3$, $X_d(\pi)=2+1+1+1+2=7$, $\int X_d=2\pi$, $\int|X_d|^2=2\pi\cdot11=22\pi$ ([[homework/hw5|HW5]] #2). $u[n+2]-u[n-3]$ is five ones: $X_d(0)=5$, $X_d(\pi)=1$ ([[exams/midterm-2/past-exams/fall-2023|FA2023 MT2]] #2). All checked numerically.

> [!trap]
> - **The sign of the differentiation row** (above).
> - **Integer shifts only.** $e^{-j\omega k}$ with non-integer $k$ is not a delay but a shifted sinc ([[exams/midterm-2/past-exams/fall-2023|FA2023 MT2]] 1(b)).
> - **Conjugation flips $\omega$ too:** $x^*[n]\leftrightarrow X_d^*(-\omega)$, not $X_d^*(\omega)$ (that one belongs to $x^*[-n]$).
> - **Modulation halves.** $x[n]\cos(\omega_0 n)$ has two copies of *half* height; copies that run past $\pm\pi$ wrap around and can overlap ([[exams/midterm-2/past-exams/spring-2025|SP2025 MT2]] #2(b)).
> - **Windowing divides by $2\pi$** and convolves over one period; it is not an LTI operation.
> - **Parseval's $\frac{1}{2\pi}$**: $\int_{-\pi}^{\pi}|X_d|^2d\omega$ is $2\pi$ times the energy.
> - **Hermitian is about $\pm\omega$, periodicity about $\omega+2\pi$.** For an arbitrary $x$ only periodicity applies ([[exams/midterm-2/past-exams/spring-2023|SP2023 MT2]] #3); for real $x$ both do (#2).

**Where it appears.**
- Lectures: [[3-fourier-analysis/14-dtft-properties|L14]] (all of it), [[3-fourier-analysis/15-frequency-response|L15]] (convolution → $Y_d=X_dH_d$; Hermitian symmetry → the cosine formula), [[3-fourier-analysis/16-magnitude-and-phase-response|L16]] (time shift → linear phase).
- Problem families: [[problems/dtft-and-inverse-dtft|DTFT and inverse DTFT]], [[problems/lti-response-to-sinusoids|LTI response to sinusoids]].
- Homework: [[homework/hw5|HW5]] #1(d) (windowing / frequency shift), #2 (the four numbers); %%hw6:W1tob21ld29yay9odzZ8SFc2XV0=%%HW6%%/hw6%% #2 (conjugation and reversal), #7 (symmetry test).
- Past exams: [[exams/midterm-2/past-exams/fall-2019|FA2019 MT2]] 1(b), 1(e), #3, #6; [[exams/midterm-2/past-exams/spring-2023|SP2023 MT2]] #2, #3; [[exams/midterm-2/past-exams/fall-2023|FA2023 MT2]] 1(c), #2; [[exams/midterm-2/past-exams/fall-2024|FA2024 MT2]] 1(b), #2, #4(a); [[exams/midterm-2/past-exams/spring-2025|SP2025 MT2]] #2, #4; [[exams/midterm-1/past-exams/spring-2023|SP2023 MT1]] 1(e), #9.

Related: [[concepts/dtft|DTFT]] · [[concepts/dtft-pairs|DTFT pairs]] · [[concepts/z-transform-properties|z-transform properties]] · [[concepts/frequency-response|frequency response]] · [[concepts/convolution|convolution]] · [[0-toolkit/01-complex-numbers|complex numbers]]

### Sources for this page
Lecture 14 notes §3 (Hermitian symmetry eqs. 26–33, periodicity, frequency shift and modulation, Parseval, convolution, windowing eqs. 46–51) and Table 2; slides 10–15; `transform_tables.pdf` Table 5 (symmetry rows, $+j$ sign); HW5 #1–#2 solutions; past-exam keys cited above. Every row was checked on random complex sequences (`verify/LB_l14.py`), the extra symmetry rows and Parseval-as-windowing in `verify/LB_concepts.py`.
