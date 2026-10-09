---
title: "Fourier series"
description: "A periodic signal as a sum of harmonics: the continuous-time series with c_k found by an inner product (orthogonality), the Dirichlet conditions and the Gibbs overshoot, the N₀-term discrete-time series (DTFS) whose coefficients are DTFT samples divided by N₀, and the road from series to the Fourier transform and the DTFT. Background for Midterm 2, not computed on it."
tags: [concept, fourier-series, fourier-analysis, unit-3]
aliases: ["Fourier series", "CTFS", "DTFS", "continuous-time Fourier series", "discrete-time Fourier series", "Fourier coefficients", "harmonics"]
---

> [!key] Continuous time: period $T_0=2\pi/\Omega_0$ (Lecture 13, eqs. 19 and 23)
> $$
> x(t)=\sum_{k=-\infty}^{\infty}c_k\,e^{jk\Omega_0t}\qquad\qquad c_k=\frac{1}{T_0}\int_{T_0}x(t)\,e^{-jk\Omega_0t}\,dt
> $$
> Synthesis (left) builds $x$ from harmonics of the fundamental frequency $\Omega_0$; analysis (right) measures how much of the frequency $k\Omega_0$ is in $x(t)$.

> [!key] Discrete time: period $N_0$ (Lecture 13, eqs. 32–33)
> $$
> x[n]=\sum_{k=0}^{N_0-1}c_k\,e^{j\frac{2\pi k}{N_0}n}\qquad\qquad c_k=\frac{1}{N_0}\sum_{n=0}^{N_0-1}x[n]\,e^{-j\frac{2\pi k}{N_0}n}
> $$
> Only $N_0$ harmonics are distinct ($k$ and $k+N_0$ give the same sequence), both sums are finite, and $c_{k+N_0}=c_k$.

**Why the analysis formula works: orthogonality.** Harmonics are orthogonal over one period, $\int_{T_0}e^{jk\Omega_0t}e^{-jl\Omega_0t}dt=T_0$ if $k=l$ and $0$ otherwise (in discrete time the sum of $N_0$ roots of unity: $N_0$ or $0$). Multiply the synthesis equation by $e^{-jl\Omega_0t}$, integrate over a period, and only $c_lT_0$ survives. In the language of [[concepts/template-matching|template matching]], each $c_k$ is the score of $x$ against the harmonic $e^{jk\Omega_0t}$, and the harmonics do not respond to one another.

**When does it exist?** Continuous time: the **Dirichlet conditions** (absolutely integrable over a period; finitely many extrema and finite jumps per period) guarantee convergence to $x(t)$ where $x$ is continuous and to the midpoint of each jump; finite energy per period gives convergence in energy. Discrete time: always, for any periodic sequence (finite sums), and the synthesis is exact. Either way the coefficients are unique. A discrete-time sinusoid with irrational $\omega_0/2\pi$ is not periodic at all, so it has no Fourier series.

> [!example] Two examples from Lecture 13
> **Sawtooth** $x(t)=t$ on $[0,1)$, period $1$: $c_0=\frac12$, $c_k=\frac{j}{2\pi k}$, so $x(t)=\frac12-\sum_{k\ge1}\frac{\sin(2\pi kt)}{\pi k}$. The partial sum with $|k|\le50$ is within $0.01$ of $x$ away from the jumps, but overshoots by $8\%$ of the jump next to each one (the **Gibbs phenomenon**: with more terms the overshoot moves closer to the jump, but its height does not shrink; it tends to about $9\%$ of the jump). The notes' caption prints $\frac{j}{\pi k}$, twice the correct value.
>
> **Periodic pulse** ($1$ for $0\le n<L$, $0$ for $L\le n<N_0$): $c_k=\frac{1}{N_0}e^{-j\pi k(L-1)/N_0}\frac{\sin(\pi kL/N_0)}{\sin(\pi k/N_0)}$, $c_0=\frac{L}{N_0}$. For $N_0=12$, $L=4$: $\lvert c_k\rvert=0.333,0.279,0.144,0,0.083,0.075,0$ for $k=0,\dots,6$.

**From series to transforms.** Let the period grow without bound and the harmonic spacing shrinks to zero: the continuous-time series becomes the Fourier transform $X_c(\Omega)=\int x(t)e^{-j\Omega t}dt$, the DTFS becomes the [[concepts/dtft|DTFT]] $X_d(\omega)=\sum_nx[n]e^{-j\omega n}$. The two are tied together exactly: **the DTFS coefficients of a periodic sequence are samples of the DTFT of one period, divided by $N_0$**,
$$
c_k=\frac{1}{N_0}X_d\!\left(\frac{2\pi k}{N_0}\right),\qquad X_d \text{ the DTFT of one period.}
$$
Going the other way, a periodic continuous-time signal has a Fourier transform made of impulses at its harmonics, $X_c(\Omega)=2\pi\sum_kc_k\,\delta(\Omega-k\Omega_0)$; $\cos(\Omega_0t+\phi_0)$, with $c_{\pm1}=\frac12e^{\pm j\phi_0}$, gives $\pi e^{j\phi_0}\delta(\Omega-\Omega_0)+\pi e^{-j\phi_0}\delta(\Omega+\Omega_0)$ ([[homework/hw6|HW6]] #1(b)).

> [!note] Not computed on exams in this course, but not gone either
> The notes star the Fourier-series objectives: you will not be asked to compute series. The idea returns later in the course as the DFT, which computes $N_0\,c_k$ from one period (`np.fft.fft` of one period of the pulse equals $12\,c_k$), and Midterm 2 asks DFT questions that rest on "the DFT samples the DTFT at $\frac{2\pi k}{N}$": smallest $N$ that captures $X_d(\frac{2\pi}{5})$ and $X_d(\frac{\pi}{3})$ is $30$ ([[exams/midterm-2/past-exams/fall-2024|FA2024 MT2]] #7); $X[11]=X_d(-\frac{3\pi}{7})$ for a length-14 DFT, by $2\pi$-periodicity ([[exams/midterm-2/past-exams/fall-2023|FA2023 MT2]] #1(h), True).

> [!trap]
> - **Scale factor.** DTFS coefficients carry $\frac{1}{N_0}$; DTFT values do not. $c_k$ equals a DTFT sample divided by $N_0$.
> - **Phase.** $\angle c_k=-\frac{\pi k}{N_0}(L-1)$ (the notes' eq. 40) is only the exponential's angle: wherever the real sine ratio is negative, add $\pm\pi$ ($N_0=12$, $L=4$: $c_4=+\frac{1}{12}$ has phase $0$, not $-\pi$). Magnitudes are never negative.
> - **Only $N_0$ distinct coefficients** in discrete time; listing $c_{N_0}$ as new information double-counts $c_0$.
> - **At a jump** the series converges to the midpoint, and the Gibbs overshoot next to it does not go away with more terms.

**Where it appears.**
- Lectures: [[3-fourier-analysis/13-fourier-analysis-and-the-dtft|Lecture 13]] §2–5 (orthogonality, CTFS, CTFT, DTFS, DTFS-samples-DTFT); [[3-fourier-analysis/12-convolution-as-template-matching|Lecture 12]] §6 (coefficients as inner products).
- Homework: [[homework/hw6|HW6]] #1 (Fourier transforms; #1(b) is a periodic signal whose only nonzero coefficients are $c_{\pm1}$).
- Exams: not computed directly; the sampling relation returns with the DFT ([[exams/midterm-2/past-exams/fall-2024|FA2024 MT2]] #7, [[exams/midterm-2/past-exams/fall-2023|FA2023 MT2]] #1(h)). Family: [[problems/dtft-and-inverse-dtft|computing DTFTs and inverse DTFTs]].

Related: [[concepts/dtft|DTFT]] · [[concepts/complex-exponential|complex exponential]] · [[concepts/template-matching|template matching]] · [[concepts/dtft-pairs|DTFT pairs]] · [[supplements/singer-munson-notes|Singer–Munson notes]] (Ch. 2: series and transforms in continuous and discrete time)

### Sources for this page
Lecture 13 notes §1.1 (orthogonality, eqs. 6–11), §2 (CTFS, eqs. 19–25, Fig. 1), §2.1 (CTFT), §3 (DTFS, Exercise 1, eqs. 29–40), §4 (eq. 49, Fig. 2) and annotated slides 8–9; Singer and Munson (2019) §2.1 and §2.3; HW6; FA2024 and FA2023 Midterm 2 keys. Checked in `verify/LA_l13.py` (coefficients, Gibbs overshoot, DTFS values and phases) and `verify/LA_concepts.py` (DFT relation, CTFT of a periodic cosine, FA2024 #7).
