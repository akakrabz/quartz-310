---
title: "Discrete-time Fourier transform (DTFT)"
description: "X_d(ω) = Σ x[n]e^{−jωn}: definition, inverse, 2π-periodicity, existence (ROC contains the unit circle ⇒ X_d(ω) = X(e^{jω})), core pairs, free values, traps."
tags: [concept, dtft, fourier-analysis, midterm-2]
aliases: ["DTFT", "discrete-time Fourier transform", "inverse DTFT", "spectrum", "frequency spectrum"]
---

> [!key] Definition and inverse (Lecture 13, eqs. 41–42)
> $$
> X_d(\omega)=\sum_{n=-\infty}^{\infty}x[n]\,e^{-j\omega n}\qquad\qquad x[n]=\frac{1}{2\pi}\int_{-\pi}^{\pi}X_d(\omega)\,e^{j\omega n}\,d\omega
> $$
> $\omega$ in radians per sample. **Magnitude spectrum** $\lvert X_d(\omega)\rvert$, **phase spectrum** $\angle X_d(\omega)$. Textbooks write $X(e^{j\omega})$.

- **Periodic:** $X_d(\omega+2\pi)=X_d(\omega)$. One period $[-\pi,\pi]$ says everything; $\omega\approx0$ low, $\omega\approx\pm\pi$ high frequency.
- **Exists if $\sum_n|x[n]|<\infty$** (sufficient, not necessary); then $X_d$ is bounded, continuous, unique. Everlasting sinusoids and $u[n]$ need impulses; growing sequences have no DTFT.
- **Bridge:** $\sum|x[n]|<\infty$ $\iff$ ROC of $X(z)$ contains $|z|=1$; then $X_d(\omega)=X(z)\big|_{z=e^{j\omega}}$ (only then). Example: $(\tfrac12)^nu[n]$ gives $X_d(\omega)=\frac{1}{1-\frac12e^{-j\omega}}$, $X_d(0)=2$, $X_d(\pi)=\frac23$.
- **Free values:** $X_d(0)=\sum_nx[n]$; $X_d(\pi)=\sum_n(-1)^nx[n]$; $\int_{-\pi}^{\pi}X_d(\omega)\,d\omega=2\pi\,x[0]$. Parseval: $\int_{-\pi}^{\pi}|X_d(\omega)|^2d\omega=2\pi\sum_n|x[n]|^2$.

| $x[n]$ | $X_d(\omega)$ on $-\pi\le\omega\le\pi$ |
|---|---|
| $\delta[n-n_0]$ | $e^{-j\omega n_0}$ |
| $u[n]-u[n-L]$ | $e^{-j\omega(L-1)/2}\,\dfrac{\sin(\omega L/2)}{\sin(\omega/2)}$ |
| $a^nu[n]$, $\lvert a\rvert<1$ | $\dfrac{1}{1-ae^{-j\omega}}$ |
| $\dfrac{\sin(\omega_cn)}{\pi n}$ | $1$ for $\lvert\omega\rvert\le\omega_c$, $0$ for $\omega_c<\lvert\omega\rvert\le\pi$ |
| $e^{j\omega_0n}$ (all $n$) | $2\pi\,\delta(\omega-\omega_0)$ |
| $\cos(\omega_0n)$ | $\pi\big[\delta(\omega-\omega_0)+\delta(\omega+\omega_0)\big]$ |
| $u[n]$ | $\dfrac{1}{1-e^{-j\omega}}+\pi\,\delta(\omega)$ |

More: [[concepts/dtft-pairs|DTFT pairs]], [[concepts/dtft-properties|DTFT properties]] (note $n\,x[n]\leftrightarrow+j\,\frac{dX_d(\omega)}{d\omega}$; Lecture 14's table prints $-j$).

> [!trap]
> - $2^nu[n]$ has no DTFT although $\frac{1}{1-2e^{-j\omega}}$ evaluates fine; "$X_d=X(e^{j\omega})$ always" is False ([[exams/midterm-2/past-exams/fall-2024|FA2024 MT2]] #1(a), [[exams/midterm-1/past-exams/spring-2023|SP2023 MT1]] #1(d)).
> - Every DTFT repeats every $2\pi$; "bandlimited to $\frac{\pi}{4}$" means zero on $\frac{\pi}{4}<|\omega|\le\pi$ only ([[exams/midterm-2/past-exams/fall-2019|FA2019 MT2]] #1(b)).
> - Impulses need all $n$: a finite piece of a cosine has an ordinary DTFT. Zero-padding changes nothing.
> - $e^{-j\omega/2}$ is not $\delta[n-\frac12]$; its inverse is $\frac{\sin(\pi(n-\frac12))}{\pi(n-\frac12)}$ ([[exams/midterm-2/past-exams/fall-2023|FA2023 MT2]] #1(b)).
> - A real $X_d$ can be negative; a magnitude cannot: $1+2\cos(2\omega)=-1$ at $\omega=\frac{\pi}{2}$ means magnitude $1$, phase $\pi$.

**Where it appears:** [[3-fourier-analysis/13-fourier-analysis-and-the-dtft|L13]]–[[3-fourier-analysis/16-magnitude-and-phase-response|L16]], [[problems/dtft-and-inverse-dtft|DTFT family]], [[homework/hw5|HW5]], [[homework/hw6|HW6]], all seven past Midterm 2 exams.

## Related
[[concepts/dtft-pairs|DTFT pairs]] · [[concepts/dtft-properties|DTFT properties]] · [[concepts/frequency-response|frequency response]] · [[concepts/magnitude-and-phase-response|magnitude and phase]] · [[concepts/region-of-convergence|ROC]] · [[concepts/fourier-series|Fourier series]]

### Sources for this page
Lecture 13 notes §4; Lecture 14 notes §1–3 (Table 1, $n\,x[n]$ sign corrected); HW5–HW6; Midterm 2 keys FA2019–SP2025.
