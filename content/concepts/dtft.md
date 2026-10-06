---
title: "Discrete-time Fourier transform (DTFT)"
description: "X_d(ω) = Σ x[n]e^{−jωn}, the spectrum of a sequence: definition and inverse, 2π-periodicity, existence (absolute summability ⇔ ROC contains the unit circle, and then X_d(ω) = X(z) at z = e^{jω}), uniqueness, the handful of pairs everyone needs, three values for free, magnitude and phase — with every lecture, problem family, homework and Midterm 2 exam that uses it."
tags: [concept, dtft, fourier-analysis, midterm-2]
aliases: ["DTFT", "discrete-time Fourier transform", "inverse DTFT", "spectrum", "frequency spectrum"]
---

> [!key] Definition and inverse (Lecture 13, eqs. 41–42)
> $$
> X_d(\omega)=\sum_{n=-\infty}^{\infty}x[n]\,e^{-j\omega n}\qquad\qquad x[n]=\frac{1}{2\pi}\int_{-\pi}^{\pi}X_d(\omega)\,e^{j\omega n}\,d\omega
> $$
> $\omega$ in radians per sample; $X_d(\omega)$ is complex, with **magnitude spectrum** $\lvert X_d(\omega)\rvert$ and **phase spectrum** $\angle X_d(\omega)$. $X_d(\omega)$ says how much of the frequency $\omega$ is in $x[n]$: it is the inner product of $x$ with $e^{j\omega n}$. Textbooks write $X(e^{j\omega})$.

## Four facts that answer most questions

1. **Periodic.** $X_d(\omega+2\pi)=X_d(\omega)$, because $e^{-j2\pi n}=1$. One period, $[-\pi,\pi]$, says everything; $\omega\approx0$ is low frequency, $\omega\approx\pm\pi$ high frequency. (The CTFT $X_c(\Omega)$ is not periodic.)
2. **Exists if $\sum_n|x[n]|<\infty$.** Then $|X_d(\omega)|\le\sum_n|x[n]|$, $X_d$ is bounded and continuous, and it is **unique**. This is sufficient, not necessary: everlasting sinusoids and $u[n]$ get DTFTs with impulses, and $\frac{\sin(\omega_cn)}{\pi n}$ (finite energy) has a rectangle for a DTFT. Growing sequences have none.
3. **Bridge to the z-transform.** $\sum|x[n]|<\infty$ is the statement "the ROC of $X(z)$ contains the unit circle", and then $X_d(\omega)=X(z)\big|_{z=e^{j\omega}}$ (**only** when the ROC contains $|z|=1$). For an impulse response this is the [[concepts/frequency-response|frequency response]] $H_d(\omega)=H(e^{j\omega})$, whose defining sum converges absolutely exactly for BIBO-stable systems ([[concepts/bibo-stability|BIBO stability]], [[concepts/region-of-convergence|ROC]]). Example: $(\tfrac12)^nu[n]\leftrightarrow\frac{1}{1-\frac12z^{-1}}$, $|z|>\frac12$, so $X_d(\omega)=\frac{1}{1-\frac12e^{-j\omega}}$, with $X_d(0)=2$ and $X_d(\pi)=\frac23$.
4. **Three values for free.** $X_d(0)=\sum_nx[n]$; $X_d(\pi)=\sum_n(-1)^nx[n]$; $\int_{-\pi}^{\pi}X_d(\omega)\,d\omega=2\pi\,x[0]$. And Parseval: $\int_{-\pi}^{\pi}|X_d(\omega)|^2d\omega=2\pi\sum_n|x[n]|^2$.

## The pairs everyone needs

| $x[n]$ | $X_d(\omega)$ on $-\pi\le\omega\le\pi$ (repeat every $2\pi$) | where from |
|---|---|---|
| $\delta[n]$ | $1$ | definition |
| $\delta[n-n_0]$ | $e^{-j\omega n_0}$ | definition |
| $u[n]-u[n-L]$ | $e^{-j\omega(L-1)/2}\,\dfrac{\sin(\omega L/2)}{\sin(\omega/2)}$ | finite geometric sum (L13, Ex. 2) |
| $a^nu[n]$, $\lvert a\rvert<1$ | $\dfrac{1}{1-ae^{-j\omega}}$ | geometric series |
| $\dfrac{\sin(\omega_cn)}{\pi n}$ | $1$ for $\lvert\omega\rvert\le\omega_c$, $0$ for $\omega_c<\lvert\omega\rvert\le\pi$ | inverse DTFT of a rectangle |
| $e^{j\omega_0n}$ (all $n$) | $2\pi\,\delta(\omega-\omega_0)$ | inverse DTFT of an impulse |
| $\cos(\omega_0n)$ | $\pi\big[\delta(\omega-\omega_0)+\delta(\omega+\omega_0)\big]$ | Euler + the line above |
| $\sin(\omega_0n)$ | $-j\pi\big[\delta(\omega-\omega_0)-\delta(\omega+\omega_0)\big]$ | Euler + the line above |
| $1$ (all $n$) | $2\pi\,\delta(\omega)$ | $\omega_0=0$ |
| $u[n]$ | $\dfrac{1}{1-e^{-j\omega}}+\pi\,\delta(\omega)$ | Lecture 14 |

More pairs (Lecture 14's Table 1) are on [[concepts/dtft-pairs|DTFT pairs]]; Tables 5–6 of the course's [[supplements/transform-tables|transform tables]] write the same pairs as $X(e^{j\omega})$. The course defines $\mathrm{sinc}(\theta)=\frac{\sin\theta}{\theta}$, so the rectangle's sequence is $\frac{\omega_c}{\pi}\mathrm{sinc}(\omega_cn)$; numpy's `np.sinc(v)` means $\frac{\sin(\pi v)}{\pi v}$.

## Properties, magnitude and phase

The properties mirror the z-transform's on the unit circle: linearity; $x[n-n_0]\leftrightarrow e^{-j\omega n_0}X_d(\omega)$; $e^{j\omega_0n}x[n]\leftrightarrow X_d(\omega-\omega_0)$; convolution $\leftrightarrow$ product; product $\leftrightarrow$ periodic convolution divided by $2\pi$; for real $x$, $X_d(-\omega)=X_d^*(\omega)$ (even magnitude, odd phase); $n\,x[n]\leftrightarrow+j\,\frac{dX_d(\omega)}{d\omega}$ (Lecture 14's table prints $-j$; the sign is $+j$, since $\frac{dX_d}{d\omega}=-j\sum_nn\,x[n]e^{-j\omega n}$). Proofs and examples: [[concepts/dtft-properties|DTFT properties]] and [[3-fourier-analysis/14-dtft-properties|Lecture 14]].

For an LTI system, $e^{j\omega_0n}\mapsto H_d(\omega_0)\,e^{j\omega_0n}$ and, for real $h$, $\cos(\omega_0n+\phi)\mapsto\lvert H_d(\omega_0)\rvert\cos\big(\omega_0n+\phi+\angle H_d(\omega_0)\big)$: see [[concepts/frequency-response|frequency response]]. Plots of $\lvert H_d\rvert$ and $\angle H_d$ follow two rules, magnitude never negative and phase as a principal angle: see [[concepts/magnitude-and-phase-response|magnitude and phase response]] and [[concepts/group-delay|group delay]].

> [!recipe] Computing a DTFT or an inverse DTFT
> - **Finite sequence**: read it off, one term $x[k]e^{-j\omega k}$ per sample; factor out the midpoint exponential $e^{-j\omega M}$; pair terms with Euler ($2\cos$, $2j\sin$); for a run of equal samples use the geometric sum and the half-angle trick. Check $X_d(0)$ and $X_d(\pi)$.
> - **Infinite sequence**: geometric series, or the z-transform evaluated at $z=e^{j\omega}$ if (and only if) its ROC contains the unit circle; impulses for everlasting sinusoids.
> - **Inverse of a polynomial in $e^{\pm j\omega}$**: by uniqueness, the coefficient of $e^{-j\omega n}$ is $x[n]$ (expand $\cos$ and $\sin$ with Euler first).
> - **Inverse of a sketch**: split one period into rectangles; each centred rectangle of height $A$ and half-width $W$ gives $A\frac{\sin(Wn)}{\pi n}$. Impulses: sift, $\frac{1}{2\pi}\int2\pi\delta(\omega-\omega_0)e^{j\omega n}d\omega=e^{j\omega_0n}$.

> [!trap]
> - **$X_d(\omega)=X(e^{j\omega})$ needs the ROC to contain $|z|=1$.** $2^nu[n]$ has no DTFT although $\frac{1}{1-2e^{-j\omega}}$ evaluates fine ([[exams/midterm-2/past-exams/fall-2024|FA2024 MT2]] #1(a), False); "always" is False ([[exams/midterm-2/past-exams/fall-2023|FA2023 MT2]] #1(a), [[exams/midterm-1/past-exams/spring-2023|SP2023 MT1]] #1(d)). For $(-1)^nu[n]$, ROC $|z|>1$, the DTFT exists only with an impulse at $\omega=\pi$ ([[exams/midterm-2/past-exams/fall-2021|FA2021 MT2]] #2(c)).
> - **Periodicity is not optional.** Every DTFT repeats every $2\pi$ ([[exams/midterm-2/past-exams/fall-2024|FA2024 MT2]] #1(b), True; [[exams/midterm-2/past-exams/fall-2019|FA2019 MT2]] #1(e), False for "only infinite-length signals"); "bandlimited to $\frac{\pi}{4}$" means zero on $\frac{\pi}{4}<|\omega|\le\pi$, not for all $|\omega|>\frac{\pi}{4}$ ([[exams/midterm-2/past-exams/fall-2019|FA2019 MT2]] #1(b), False); $X_d=j\omega$ on $[0,\pi]$ means $j(\omega-2\pi)$ on $[2\pi,3\pi]$ ([[exams/midterm-2/past-exams/spring-2023|SP2023 MT2]] #3).
> - **Impulses need all $n$.** A finite piece of a cosine has an ordinary DTFT ([[exams/midterm-2/past-exams/fall-2019|FA2019 MT2]] #1(c), False), and $u[n]$'s DTFT has the extra $\pi\delta(\omega)$.
> - **Sequences live on integers.** $e^{-j\omega/2}$ is not $\delta[n-\frac12]$; its inverse DTFT is the sinc $\frac{\sin(\pi(n-\frac12))}{\pi(n-\frac12)}$ ([[exams/midterm-2/past-exams/fall-2023|FA2023 MT2]] #1(b), False).
> - **Zero-padding changes nothing**: appended zeros add zero terms ([[exams/midterm-2/past-exams/fall-2023|FA2023 MT2]] #1(f), [[exams/midterm-2/past-exams/spring-2023|SP2023 MT2]] #1(c), [[exams/midterm-2/past-exams/fall-2024|FA2024 MT2]] #1(d) True; [[exams/midterm-2/past-exams/fall-2019|FA2019 MT2]] #1(a), [[exams/midterm-2/past-exams/spring-2025|SP2025 MT2]] #1(d) False).
> - **A real-valued $X_d$ can be negative; a magnitude cannot.** $1+2\cos(2\omega)$ is $-1$ at $\omega=\frac{\pi}{2}$: magnitude $1$, phase $\pi$ (or $-\pi$; say which end of the principal interval you use) ([[exams/midterm-2/past-exams/fall-2024|FA2024 MT2]] #3).
> - **Dirac $\delta(\omega)$ is not Kronecker $\delta[n]$**: continuous argument, infinite height, unit area.

## Where it appears

- **Lectures**: [[3-fourier-analysis/12-convolution-as-template-matching|L12]] §6 (the DTFT as a template score) · [[3-fourier-analysis/13-fourier-analysis-and-the-dtft|L13]] (definition, inverse, periodicity, existence, examples, impulses, rect ↔ sinc) · [[3-fourier-analysis/14-dtft-properties|L14]] (z-transform bridge, pairs, properties) · [[3-fourier-analysis/15-frequency-response|L15]] (frequency response, sinusoidal inputs) · [[3-fourier-analysis/16-magnitude-and-phase-response|L16]] (magnitude, phase, group delay) · unit: [[3-fourier-analysis/index|Unit 3]].
- **Problem families**: [[problems/dtft-and-inverse-dtft|computing DTFTs and inverse DTFTs]] · [[problems/lti-response-to-sinusoids|LTI response to sinusoids]] · [[problems/magnitude-phase-and-group-delay|magnitude, phase and group delay]].
- **Homework**: [[homework/hw5|HW5]] #1 (DTFTs from the definition), #2 (values, Parseval) · %%hw6:W1tob21ld29yay9odzZ8SFc2XV0=%%HW6%%/hw6%% #2 (conjugation), #3 (inverse DTFTs), #4 (DTFT vs z-transform), #5 (frequency response of an accumulator), #6–7 (magnitude, phase, sinusoidal response).
- **Past Midterm 2 exams** (all seven use it):
  - definition level (Lecture 13): [[exams/midterm-2/past-exams/fall-2024|FA2024]] #1(a), (b), #2, #3(a) · [[exams/midterm-2/past-exams/spring-2025|SP2025]] #1(a) · [[exams/midterm-2/past-exams/fall-2023|FA2023]] #1(a), (b), #2 · [[exams/midterm-2/past-exams/spring-2023|SP2023]] #3, #4 · [[exams/midterm-2/past-exams/spring-2021|SP2021]] #3, #6, #7 · [[exams/midterm-2/past-exams/fall-2019|FA2019]] #1(a)–(c), (e), #3; also [[exams/midterm-1/past-exams/spring-2023|SP2023 MT1]] #8, #9;
  - properties (Lecture 14): [[exams/midterm-2/past-exams/spring-2025|SP2025]] #2 (modulation) · [[exams/midterm-2/past-exams/fall-2023|FA2023]] #1(c) and [[exams/midterm-2/past-exams/spring-2023|SP2023]] #2 (conjugate symmetry) · [[exams/midterm-2/past-exams/fall-2024|FA2024]] #4(a) (real $h$?) · [[exams/midterm-2/past-exams/fall-2021|FA2021]] #2(c) (DTFT vs z-transform), #6(a) (convolution ↔ product);
  - frequency response, magnitude and phase (Lectures 15–16): [[exams/midterm-2/past-exams/fall-2024|FA2024]] #3(b), #4(b) · [[exams/midterm-2/past-exams/spring-2025|SP2025]] #3, #4 · [[exams/midterm-2/past-exams/fall-2023|FA2023]] #4 · [[exams/midterm-2/past-exams/spring-2023|SP2023]] #5, #6 · [[exams/midterm-2/past-exams/fall-2021|FA2021]] #1(a) · [[exams/midterm-2/past-exams/spring-2021|SP2021]] #2 · [[exams/midterm-2/past-exams/fall-2019|FA2019]] #1(d).
- **Later in the course** (also on Midterm 2): sampling and reconstruction, and the DFT, which samples the DTFT at $\omega_k=\frac{2\pi k}{N}$ ([[concepts/fourier-series|Fourier series]]).

Related: [[concepts/fourier-series|Fourier series]] · [[concepts/dtft-pairs|DTFT pairs]] · [[concepts/dtft-properties|DTFT properties]] · [[concepts/frequency-response|frequency response]] · [[concepts/magnitude-and-phase-response|magnitude and phase response]] · [[concepts/group-delay|group delay]] · [[concepts/z-transform|z-transform]] · [[concepts/region-of-convergence|region of convergence]] · [[concepts/eigenfunctions-of-lti-systems|eigenfunctions of LTI systems]] · [[concepts/template-matching|template matching]]

### Sources for this page
Lecture 13 notes §4 (definition, inverse, existence, uniqueness, Exercise 2) and annotated slides 15–16; Lecture 14 notes §1 (relation to the z-transform), §2 (impulse pairs, Table 1) and §3 (properties; the $n\,x[n]$ sign is corrected); the course transform tables; HW5 (with official solutions) and HW6; the seven Midterm 2 keys (FA2019, SP2021, FA2021, SP2023, FA2023, FA2024, SP2025) and the SP2023 Midterm 1 key. Every pair, value and property on this page is checked numerically in `verify/LA_concepts.py` (including the $u[n]$ pair through a principal-value inverse DTFT) and `verify/LA_l13.py`.
