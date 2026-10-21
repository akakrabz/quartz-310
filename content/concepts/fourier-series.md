---
title: "Fourier series"
description: "A periodic signal as a sum of harmonics: CTFS and DTFS, coefficients by orthogonality, Dirichlet and Gibbs, DTFS = DTFT samples / N₀. Background for Midterm 2, not computed on it."
tags: [concept, fourier-series, fourier-analysis, unit-3]
aliases: ["Fourier series", "CTFS", "DTFS", "continuous-time Fourier series", "discrete-time Fourier series", "Fourier coefficients", "harmonics"]
---

> [!key] Continuous time, period $T_0=2\pi/\Omega_0$ (Lecture 13, eqs. 19, 23)
> $$
> x(t)=\sum_{k=-\infty}^{\infty}c_k\,e^{jk\Omega_0t}\qquad\qquad c_k=\frac{1}{T_0}\int_{T_0}x(t)\,e^{-jk\Omega_0t}\,dt
> $$

> [!key] Discrete time, period $N_0$ (Lecture 13, eqs. 32–33)
> $$
> x[n]=\sum_{k=0}^{N_0-1}c_k\,e^{j\frac{2\pi k}{N_0}n}\qquad\qquad c_k=\frac{1}{N_0}\sum_{n=0}^{N_0-1}x[n]\,e^{-j\frac{2\pi k}{N_0}n}
> $$
> Only $N_0$ distinct harmonics; $c_{k+N_0}=c_k$.

- **Orthogonality:** harmonics are orthogonal over a period, so only $c_l$ survives the analysis integral.
- **Existence:** CTFS under the Dirichlet conditions (midpoint at jumps); DTFS always.
- **Link to the DTFT:**

$$
c_k=\frac{1}{N_0}X_d\!\left(\frac{2\pi k}{N_0}\right),\qquad X_d \text{ the DTFT of one period.}
$$

- **Periodic CT signal:** $X_c(\Omega)=2\pi\sum_kc_k\,\delta(\Omega-k\Omega_0)$ ([[homework/hw6|HW6]] #1(b)).

> [!example] Lecture 13
> - Sawtooth $x(t)=t$ on $[0,1)$: $c_0=\frac12$, $c_k=\frac{j}{2\pi k}$ (the notes' caption prints $\frac{j}{\pi k}$). Partial sums overshoot near jumps (Gibbs, about $9\%$ in the limit).
> - Periodic pulse, $N_0=12$, $L=4$: $\lvert c_k\rvert=0.333,0.279,0.144,0,0.083,0.075,0$ for $k=0,\dots,6$.

> [!trap]
> - DTFS coefficients carry $\frac{1}{N_0}$; DTFT values do not.
> - $\angle c_k=-\frac{\pi k}{N_0}(L-1)$ needs $\pm\pi$ where the sine ratio is negative.
> - Gibbs overshoot does not shrink with more terms.

**Where it appears:** [[3-fourier-analysis/13-fourier-analysis-and-the-dtft|Lecture 13]], [[3-fourier-analysis/12-convolution-as-template-matching|Lecture 12]]; [[homework/hw6|HW6]] #1; returns with the DFT ([[exams/midterm-2/past-exams/fall-2024|FA2024 MT2]] #7, [[exams/midterm-2/past-exams/fall-2023|FA2023 MT2]] #1(h)).

## Related
[[concepts/dtft|DTFT]] · [[concepts/complex-exponential|complex exponential]] · [[concepts/template-matching|template matching]] · [[supplements/singer-munson-notes|Singer–Munson notes]]

### Sources for this page
Lecture 13 notes §1.1–4 (eqs. 6–49, Figs. 1–2), slides 8–9; Singer–Munson §2.1, §2.3; HW6; FA2024, FA2023 MT2 keys.
