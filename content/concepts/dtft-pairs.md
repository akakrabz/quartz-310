---
title: "DTFT pairs"
description: "The DTFT pairs this course uses — finite sequences, exponentials, pulses, sinc and sinc², and the impulse pairs for periodic signals and the step — each with the condition under which it holds, where it comes from, and a numerical check."
tags: [concept, dtft, midterm-2]
aliases: ["DTFT pairs", "DTFT table", "common DTFT pairs"]
---

> [!key] Ordinary pairs: the DTFT sum converges absolutely
> | $x[n]$ | $X_d(\omega)$, one period $-\pi\le\omega\le\pi$ | holds when | route |
> |---|---|---|---|
> | $\delta[n]$ | $1$ | always | definition |
> | $\delta[n-k]$ | $e^{-j\omega k}$ | $k$ an integer | definition |
> | $a^n u[n]$ | $\dfrac{1}{1-ae^{-j\omega}}$ | $\lvert a\rvert\lt1$ | geometric series; $\frac{1}{1-az^{-1}}$, ROC $\lvert z\rvert>\lvert a\rvert$ |
> | $-a^n u[-n-1]$ | $\dfrac{1}{1-ae^{-j\omega}}$ | $\lvert a\rvert>1$ | $\frac{1}{1-az^{-1}}$, ROC $\lvert z\rvert\lt\lvert a\rvert$ |
> | $n\,a^n u[n]$ | $\dfrac{ae^{-j\omega}}{(1-ae^{-j\omega})^2}$ | $\lvert a\rvert\lt1$ | $+j\,\frac{d}{d\omega}$ of the $a^nu[n]$ row |
> | $(n+1)\,a^n u[n]$ | $\dfrac{1}{(1-ae^{-j\omega})^2}$ | $\lvert a\rvert\lt1$ | sum of the two rows above |
> | $a^{\lvert n\rvert}$ | $\dfrac{1-a^2}{1-2a\cos\omega+a^2}$ | $\lvert a\rvert\lt1$ | ring $\lvert a\rvert\lt\lvert z\rvert\lt1/\lvert a\rvert$ |
> | $1$ for $0\le n\le L-1$ | $e^{-j\omega(L-1)/2}\,\dfrac{\sin(L\omega/2)}{\sin(\omega/2)}$ | — | finite geometric sum (Lecture 13) |
> | $\mathrm{rect}\!\left(\frac{n-k}{L}\right)$: $L$ ones centred at $k$ | $\dfrac{\sin(L\omega/2)}{\sin(\omega/2)}\,e^{-j\omega k}$ | $L$ odd | the pulse, shifted |
> | $\mathrm{sinc}^2(Ln)$ | $\dfrac{\pi}{L}\left(1-\dfrac{\lvert\omega\rvert}{2L}\right)$ for $\lvert\omega\rvert\le2L$, else $0$ | $0\lt L\le\frac{\pi}{2}$ | windowing of the sinc row |
>
> The course writes $\mathrm{sinc}(x)=\dfrac{\sin x}{x}$ and $\Delta(\frac{\omega}{2L})$ for the triangle. Every pair is periodic: the formula describes one period and repeats every $2\pi$.

> [!key] A pair that converges only in energy
> | $x[n]$ | $X_d(\omega)$ on $-\pi\le\omega\le\pi$ | holds when |
> |---|---|---|
> | $\dfrac{\sin(Wn)}{\pi n}=\dfrac{W}{\pi}\,\mathrm{sinc}(Wn)$ | $1$ for $\lvert\omega\rvert\le W$, $0$ for $W\lt\lvert\omega\rvert\le\pi$ | $0\lt W\lt\pi$ |
> | $\mathrm{sinc}(Ln)$ | $\dfrac{\pi}{L}\,\mathrm{rect}\!\left(\frac{\omega}{2L}\right)$: $\dfrac{\pi}{L}$ for $\lvert\omega\rvert\lt L$ | $0\lt L\lt\pi$ |
>
> The same pair written twice. It decays only like $1/n$, so it is **not** absolutely summable and its DTFT has jumps. It is the impulse response of the ideal low-pass filter, which is why that filter is not BIBO stable.

> [!key] Impulse pairs: periodic signals and the step (one period shown)
> | $x[n]$ | $X_d(\omega)$ on $-\pi\le\omega\le\pi$ |
> |---|---|
> | $1$ (all $n$) | $2\pi\,\delta(\omega)$ |
> | $e^{j\omega_0 n}$ | $2\pi\,\delta(\omega-\omega_0)$ |
> | $\cos(\omega_0 n)$ | $\pi\left[\delta(\omega-\omega_0)+\delta(\omega+\omega_0)\right]$ |
> | $\sin(\omega_0 n)$ | $-j\pi\left[\delta(\omega-\omega_0)-\delta(\omega+\omega_0)\right]$ |
> | $\cos(\omega_0 n+\theta)$ | $\pi\left[e^{j\theta}\delta(\omega-\omega_0)+e^{-j\theta}\delta(\omega+\omega_0)\right]$ |
> | $u[n]$ | $\dfrac{1}{1-e^{-j\omega}}+\pi\,\delta(\omega)$ |
> | $e^{j\omega_0 n}u[n]$ | $\dfrac{1}{1-e^{-j(\omega-\omega_0)}}+\pi\,\delta(\omega-\omega_0)$ |
> | $(-1)^n u[n]$ | $\dfrac{1}{1+e^{-j\omega}}+\pi\,\delta(\omega-\pi)$ |
>
> $\delta(\omega)$ is the Dirac delta (unit area, sifting), not the Kronecker $\delta[n]$; an arrow's height in a sketch shows its area. A periodic signal with Fourier-series coefficients $c_k$ has $X_d(\omega)=2\pi\sum_k c_k\,\delta\!\left(\omega-\frac{2\pi k}{N}\right)$ ([[concepts/fourier-series|Fourier series]]).

**No DTFT at all:** $a^n u[n]$ with $|a|>1$ (e.g. $2^n u[n]$), $-a^nu[-n-1]$ with $|a|\lt1$, and anything else whose ROC misses the unit circle without touching it — the samples grow without bound.

## Where the pairs come from

Three routes cover every row ([[3-fourier-analysis/14-dtft-properties|Lecture 14]]):

1. **The geometric series** for finite and exponential sequences: $\sum_{n\ge0}(ae^{-j\omega})^n=\frac{1}{1-ae^{-j\omega}}$ needs $|ae^{-j\omega}|=|a|\lt1$ ([[0-toolkit/02-geometric-series|geometric series]]).
2. **The z-transform on the unit circle**, $X_d(\omega)=X(z)\big|_{z=e^{j\omega}}$, whenever the ROC contains $|z|=1$. Every ordinary row is a [[concepts/z-transform-pairs|z-transform pair]] with this substitution; that is why $-a^nu[-n-1]$ needs $|a|>1$ (its ROC is $|z|\lt|a|$).
3. **Properties applied to a known pair** ([[concepts/dtft-properties|DTFT properties]]): a shift multiplies by $e^{-j\omega k}$; $e^{j\omega_0 n}$ slides the spectrum ($e^{j\omega_0 n}u[n]$ from $u[n]$); $n\,x[n]\leftrightarrow+j\frac{dX_d}{d\omega}$ gives the $n\,a^nu[n]$ row; multiplying two sincs convolves two rectangles into the triangle of the $\mathrm{sinc}^2$ row.

The impulse rows come from inverting a guess: $\frac{1}{2\pi}\int_{-\pi}^{\pi}c\,\delta(\omega-\omega_0)e^{j\omega n}d\omega=\frac{c}{2\pi}e^{j\omega_0 n}$ forces $c=2\pi$. The step's $\pi\delta(\omega)$ is its average value $\frac12$ times $2\pi$; the rest, $u[n]-\frac12$, has first difference $\delta[n]$ and so transforms to $\frac{1}{1-e^{-j\omega}}$.

> [!example] Using the table backwards (SP2021 MT2 #7)
> $x[n]=A_1\frac{\sin(\omega_0 n)}{\omega_0 n}+A_2\frac{\sin(2\omega_0 n)}{2\omega_0 n}$ has a staircase DTFT: height $2$ for $|\omega|\le\frac{\pi}{3}$ and $1$ for $\frac{\pi}{3}\lt|\omega|\le\frac{2\pi}{3}$. Each term is a sinc row: $A\,\mathrm{sinc}(Ln)\leftrightarrow\frac{A\pi}{L}$ on $|\omega|\lt L$. The outer edge gives $2\omega_0=\frac{2\pi}{3}$, so $\omega_0=\frac{\pi}{3}$; the outer step gives $\frac{A_2\pi}{2\omega_0}=1$, so $A_2=\frac23$; the inner step gives $\frac{A_1\pi}{\omega_0}+1=2$, so $A_1=\frac13$ (checked).

> [!trap]
> - **$|a|\lt1$ is part of the pair.** $\frac{1}{1-2e^{-j\omega}}$ is *not* the DTFT of $2^nu[n]$ ([[exams/midterm-2/past-exams/fall-2024|FA2024 MT2]] 1(a), False).
> - **Impulses repeat.** $\cos(\omega_0 n)$ has impulses at $\pm\omega_0+2\pi k$ for every $k$; the table shows one period.
> - **Finite length means no impulses.** $\cos(\frac{\pi}{32}n)$ for $0\le n\le15$ has an ordinary DTFT (two shifted copies of the pulse transform), not $\pi[\delta(\omega-\frac{\pi}{32})+\delta(\omega+\frac{\pi}{32})]$ ([[exams/midterm-2/past-exams/fall-2019|FA2019 MT2]] 1(c), False).
> - **Two sincs.** NumPy's `np.sinc(x)` and the official [[supplements/transform-tables|transform tables]] mean $\frac{\sin\pi x}{\pi x}$; the course and its exam keys mean $\frac{\sin x}{x}$.
> - **Even $L$.** The notes define $\mathrm{rect}(\frac{n-k}{L})=1$ for $k-\frac L2\lt n\le k+\frac L2$; for even $L$ that block is centred at $k+\frac12$ and its DTFT carries an extra $e^{-j\omega/2}$.
> - **$\mathrm{sinc}^2$ needs $L\le\frac{\pi}{2}$**, or the triangles of neighbouring periods overlap and add.
> - **Non-integer "delays" are sincs.** $e^{-j\omega/2}$ on $|\omega|\le\pi$ inverts to $\frac{\sin(\pi(n-\frac12))}{\pi(n-\frac12)}$, not $\delta[n-\frac12]$ ([[exams/midterm-2/past-exams/fall-2023|FA2023 MT2]] 1(b), False; [[exams/midterm-2/past-exams/fall-2019|FA2019 MT2]] #5; %%hw6:W1tob21ld29yay9odzZ8SFc2XV0=%%HW6%%/hw6%% #3b).

**Where it appears.**
- Lectures: [[3-fourier-analysis/13-fourier-analysis-and-the-dtft|L13]] (the pulse, Exercise 2), [[3-fourier-analysis/14-dtft-properties|L14]] (Table 1, impulse pairs), [[3-fourier-analysis/15-frequency-response|L15]] ($e^{j\omega_0 n}\leftrightarrow2\pi\delta(\omega-\omega_0)$ gives the eigenfunction response).
- Problem family: [[problems/dtft-and-inverse-dtft|DTFT and inverse DTFT]].
- Homework: [[homework/hw5|HW5]] #1 (from the definition, with the impulse pair allowed in (c)–(d)); %%hw6:W1tob21ld29yay9odzZ8SFc2XV0=%%HW6%%/hw6%% #3–#5.
- Past exams: [[exams/midterm-2/past-exams/spring-2021|SP2021 MT2]] #3, #7; [[exams/midterm-1/past-exams/spring-2023|SP2023 MT1]] #8; [[exams/midterm-2/past-exams/fall-2024|FA2024 MT2]] 1(a), #2; [[exams/midterm-2/past-exams/spring-2025|SP2025 MT2]] #2; [[exams/midterm-2/past-exams/spring-2023|SP2023 MT2]] #4; [[exams/midterm-2/past-exams/fall-2023|FA2023 MT2]] 1(b); [[exams/midterm-2/past-exams/fall-2021|FA2021 MT2]] #2(c); [[exams/midterm-2/past-exams/fall-2019|FA2019 MT2]] 1(c), #5.

Related: [[concepts/dtft|DTFT]] · [[concepts/dtft-properties|DTFT properties]] · [[concepts/z-transform-pairs|z-transform pairs]] · [[concepts/region-of-convergence|region of convergence]] · [[concepts/frequency-response|frequency response]] · [[supplements/transform-tables|transform tables]]

### Sources for this page
Lecture 14 notes §2 and Table 1 (with its rect, sinc and $\mathrm{sinc}^2$ definitions) and slides 7–9; Lecture 13 notes Exercise 2; `transform_tables.pdf` Table 6; HW5 solutions #1; past-exam keys cited above. Checks: ordinary rows by truncated sums at many $\omega$, the sinc rows by numerical inverse DTFT (and the $L\le\frac{\pi}{2}$ limit by showing the formula fails at $L=\frac{3\pi}{4}$), the step and $e^{j\omega_0n}u[n]$ rows by Abel summation, the impulse rows by Fejér-windowed spectra whose area near $\pm\omega_0$ tends to $\pi$ — `verify/LB_l14.py` and `verify/LB_concepts.py`.
