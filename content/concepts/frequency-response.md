---
title: "Frequency response"
description: "H_d(ω), the DTFT of h[n]: equals H(z) on the unit circle for stable systems, gives the response to every sinusoid (real-h condition for cosines), common FIR examples, traps."
tags: [concept, frequency-response, dtft, midterm-2]
aliases: ["frequency response", "sinusoidal response", "response to sinusoids"]
---

> [!key] Definition (Lecture 15)
> $$
> H_d(\omega)=\sum_{n=-\infty}^{\infty}h[n]\,e^{-j\omega n}=|H_d(\omega)|\,e^{j\angle H_d(\omega)}
> $$
> $2\pi$-periodic; **magnitude response** $|H_d(\omega)|\ge0$, **phase response** $\angle H_d(\omega)$. If the ROC of $H(z)$ contains $|z|=1$: $H_d(\omega)=H(z)\big|_{z=e^{j\omega}}$.

> [!key] Response to sinusoids
> | input (all $n$) | output | needs |
> |---|---|---|
> | $A\,e^{j\omega_0 n}$ | $A\,H_d(\omega_0)\,e^{j\omega_0 n}$ | any LTI |
> | $A\cos(\omega_0 n+\theta)$ | $A\lvert H_d(\omega_0)\rvert\cos(\omega_0 n+\theta+\angle H_d(\omega_0))$ | $h$ real |
> | constant $c$ | $H_d(0)\,c$ | |
> | $(-1)^n$ | $H_d(\pi)\,(-1)^n$ | |
> | $x$ with a DTFT | $Y_d(\omega)=X_d(\omega)H_d(\omega)$ | |
>
> No new frequencies are created.

- **Real $h$** $\iff$ $H_d(-\omega)=H_d^*(\omega)$ (even magnitude, odd phase). Complex $h$: split cosines into $e^{\pm j\omega_0n}$ and treat each half separately.
- **Stability:** stable ⇒ ordinary $H_d=H(e^{j\omega})$; pole on $|z|=1$ ⇒ impulses (accumulator: $\frac{1}{1-e^{-j\omega}}+\pi\delta(\omega)$, [[homework/hw6|HW6]] #5); unstable causal ⇒ none.
- **Zeros notch, poles peak:** $1+z^{-4}$ removes $\frac{\pi}{4}$ and $\frac{3\pi}{4}$; $\frac{1}{1-0.9z^{-1}}$ has gain $10$ at $\omega=0$.

| system | $H_d(\omega)$ | where |
|---|---|---|
| $h=\delta[n+2]+\delta[n]+\delta[n-2]$ | $1+2\cos(2\omega)$ | [[exams/midterm-2/past-exams/fall-2024\|FA2024 MT2]] #3 |
| $h=\delta[n]+\delta[n-6]$ | $2\cos(3\omega)\,e^{-j3\omega}$ | [[exams/midterm-2/past-exams/spring-2023\|SP2023 MT2]] #5 |
| $y[n]=x[n]+2x[n-3]+x[n-6]$ | $\left(2+2\cos3\omega\right)e^{-j3\omega}$ | [[exams/midterm-2/past-exams/spring-2025\|SP2025 MT2]] #3 |
| $y[n]=x[n]+x[n-10]$ | $2\cos(5\omega)\,e^{-j5\omega}$ | [[homework/hw6\|HW6]] #6 |

> [!trap]
> - Cosine formula needs real $h$ ([[exams/midterm-2/past-exams/spring-2023|SP2023 MT2]] #6, [[exams/midterm-2/past-exams/fall-2023|FA2023 MT2]] #4 have complex $h$).
> - A cosine is not an eigenfunction; only $e^{j\omega_0 n}$ is ([[exams/midterm-2/past-exams/fall-2021|FA2021 MT2]] 1(a)).
> - Magnitude never negative: $H_d(\frac{\pi}{2})=-1$ is gain $1$, phase $\pi$.
> - $H_d(\pm\pi)$ of a real system is real; a formula giving different values at $\pm\pi$ jumps there ([[exams/midterm-2/past-exams/spring-2025|SP2025 MT2]] #4).

**Where it appears:** [[3-fourier-analysis/15-frequency-response|L15]], [[3-fourier-analysis/16-magnitude-and-phase-response|L16]]; [[problems/lti-response-to-sinusoids|LTI response to sinusoids]]; [[homework/hw6|HW6]] #5–#7; [[demos/frequency-response-explorer|frequency response explorer]].

## Related
[[concepts/eigenfunctions-of-lti-systems|eigenfunctions]] · [[concepts/transfer-function|transfer function]] · [[concepts/dtft|DTFT]] · [[concepts/magnitude-and-phase-response|magnitude and phase response]] · [[concepts/group-delay|group delay]]

### Sources for this page
Lecture 15 notes §1 (eqs. 1–22), slides 3–11; Lecture 14 §1; HW6 #5–#7; Midterm 2 keys cited.
