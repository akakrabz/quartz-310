---
title: "Frequency response"
description: "H_d(ω), the DTFT of the impulse response: when it equals H(z) on the unit circle (stability), why it alone determines the response to every sinusoid (eigenfunctions), the recipe for sums of sinusoids with its real-h condition, common FIR examples from the exams, and where magnitude, phase and group delay take over."
tags: [concept, frequency-response, dtft, midterm-2]
aliases: ["frequency response", "sinusoidal response", "response to sinusoids"]
---

> [!key] Definition (Lecture 15)
> The frequency response of an LTI system is the DTFT of its impulse response:
> $$
> H_d(\omega)=\sum_{n=-\infty}^{\infty}h[n]\,e^{-j\omega n}=|H_d(\omega)|\,e^{j\angle H_d(\omega)},
> $$
> $2\pi$-periodic, plotted on $-\pi\le\omega\le\pi$, with **magnitude response** $|H_d(\omega)|\ge0$ and **phase response** $\angle H_d(\omega)$ (a principal angle). If the ROC of the [[concepts/transfer-function|transfer function]] contains the unit circle, $H_d(\omega)=H(z)\big|_{z=e^{j\omega}}$.

Three ways to read the same function:

| view | statement | from |
|---|---|---|
| a DTFT | $H_d$ is the spectrum of $h[n]$ | [[3-fourier-analysis/14-dtft-properties\|Lecture 14]] |
| a transfer function on the unit circle | $H_d(\omega)=H(e^{j\omega})$ for stable systems | [[3-fourier-analysis/14-dtft-properties\|Lecture 14]] |
| an eigenvalue | $e^{j\omega n}\mapsto H_d(\omega)\,e^{j\omega n}$ | [[concepts/eigenfunctions-of-lti-systems\|eigenfunctions]], [[3-fourier-analysis/15-frequency-response\|Lecture 15]] |

## The response recipe

> [!key] What an LTI system does to sinusoids
> | input (all $n$) | output | needs |
> |---|---|---|
> | $A\,e^{j\omega_0 n}$ | $A\,H_d(\omega_0)\,e^{j\omega_0 n}=A\lvert H_d(\omega_0)\rvert e^{j(\omega_0 n+\angle H_d(\omega_0))}$ | any LTI system |
> | $A\cos(\omega_0 n+\theta)$ | $A\lvert H_d(\omega_0)\rvert\cos(\omega_0 n+\theta+\angle H_d(\omega_0))$ | $h$ real |
> | constant $c$ | $H_d(0)\,c$ | ($H_d(0)$ real if $h$ is) |
> | $(-1)^n=e^{j\pi n}$ | $H_d(\pi)\,(-1)^n$ | ($H_d(\pi)$ real if $h$ is) |
> | any $x$ with a DTFT | $Y_d(\omega)=X_d(\omega)H_d(\omega)$ | convolution property |
>
> Same frequencies out as in: an LTI system rescales and phase-shifts each frequency and creates none.

The cosine row needs a real $h$ because a cosine is the two exponentials $e^{\pm j\omega_0 n}$, which meet the two eigenvalues $H_d(\pm\omega_0)$; only Hermitian symmetry, $H_d(-\omega_0)=H_d^*(\omega_0)$, makes them recombine into one real cosine. With a complex $h$, split every sinusoid and treat the halves separately; a real input can then give a complex output (Lecture 15's $h=\frac12(\delta[n]+j\delta[n-1])$ maps $\cos(\frac{\pi}{2}n)$ to $\frac12e^{j\pi n/2}$; [[exams/midterm-2/past-exams/spring-2023|SP2023 MT2]] #6 maps a sine to an imaginary cosine).

> [!recipe] Response to a sum of sinusoids
> 1. **Is $h$ real?** Magnitude even and phase odd on $-\pi\le\omega\le\pi$ ⇔ $H_d(-\omega)=H_d^*(\omega)$ ⇔ real ([[concepts/dtft-properties|DTFT properties]]).
> 2. **Frequencies:** constant → $0$, $(-1)^n$ → $\pi$, $j^n$ → $\frac{\pi}{2}$ (a single exponential); degrees → radians.
> 3. **Evaluate** $H_d$ at each frequency in polar form; a zero deletes the term.
> 4. **Apply** the rows above and add.
>
> Worked in [[3-fourier-analysis/15-frequency-response|Lecture 15]] (slides 6, 10, 11) and drilled in [[problems/lti-response-to-sinusoids|LTI response to sinusoids]].

## Frequency response, $H(z)$ and stability

| system | ROC of $H(z)$ | frequency response |
|---|---|---|
| BIBO stable | contains $\lvert z\rvert=1$ | ordinary, continuous: $H_d(\omega)=H(e^{j\omega})$ |
| marginally stable (pole on $\lvert z\rvert=1$) | touches $\lvert z\rvert=1$ | only with impulses; $\neq H(e^{j\omega})$. Accumulator: $\frac{1}{1-e^{-j\omega}}+\pi\delta(\omega)$%%hw6:IChbW2hvbWV3b3JrL2h3Nlx8SFc2XV0gIzUp%%%%/hw6%%; $h=(-1)^nu[n]$: impulse at $\pi$ ([[exams/midterm-2/past-exams/fall-2021\|FA2021 MT2]] #2c) |
| unstable, causal | misses $\lvert z\rvert=1$ | none |

(The ideal filters of later lectures sit outside this table: their sinc-shaped $h[n]$ has a DTFT but no z-transform, and is not stable.) The poles and zeros shape $|H_d|$. A zero on the unit circle at $e^{j\omega_0}$ is a notch, $H_d(\omega_0)=0$: $1-2\cos(\omega_0)z^{-1}+z^{-2}$ removes $\omega_0$ exactly, and $1+z^{-4}$ removes $\frac{\pi}{4}$ and $\frac{3\pi}{4}$ ([[exams/midterm-2/past-exams/fall-2019|FA2019 MT2]] #7). A pole close to the unit circle makes a peak: $\frac{1}{1-0.9z^{-1}}$ has gain $10$ at $\omega=0$ and $\frac{1}{1.9}\approx0.53$ at $\omega=\pi$, a low-pass. ([[concepts/eigenfunctions-of-lti-systems|Eigenfunctions]]: "a zero blocks, a pole resonates", now read on the unit circle.)

## Frequency responses you will meet

Symmetric FIR filters from the exams and homework all factor as a real amplitude times $e^{-j\omega c}$, with $c$ the centre of symmetry (all checked numerically):

| system | $H_d(\omega)$ | where |
|---|---|---|
| $h=\delta[n+2]+\delta[n]+\delta[n-2]$ | $1+2\cos(2\omega)$ | [[exams/midterm-2/past-exams/fall-2024\|FA2024 MT2]] #3 |
| $H(z)=1+z^{-4}$ | $2\cos(2\omega)\,e^{-j2\omega}$ | [[exams/midterm-2/past-exams/fall-2019\|FA2019 MT2]] #7 |
| $h=\delta[n]+\delta[n-6]$ | $2\cos(3\omega)\,e^{-j3\omega}$ | [[exams/midterm-2/past-exams/spring-2023\|SP2023 MT2]] #5 |
| $y[n]=x[n]+2x[n-3]+x[n-6]$ | $\left(2+2\cos3\omega\right)e^{-j3\omega}$ | [[exams/midterm-2/past-exams/spring-2025\|SP2025 MT2]] #3 |
| $y[n]=x[n]+x[n-10]$ | $2\cos(5\omega)\,e^{-j5\omega}$ | %%hw6:W1tob21ld29yay9odzZcfEhXNl1dICM2%%—%%/hw6%% |

Where the real amplitude goes negative, the magnitude response is its absolute value and the phase picks up a jump of $\pi$; the straight-line phase $-c\,\omega$ is a constant delay of $c$ samples. Plotting magnitude and phase, principal angles, $\pi$ jumps and the group delay $-\frac{d\angle H_d}{d\omega}$ are the subject of [[3-fourier-analysis/16-magnitude-and-phase-response|Lecture 16]]: see [[concepts/magnitude-and-phase-response|magnitude and phase response]] and [[concepts/group-delay|group delay]].

> [!trap]
> - **The cosine formula needs real $h$** — check Hermitian symmetry first ([[exams/midterm-2/past-exams/fall-2019|FA2019 MT2]] 1(d); [[exams/midterm-2/past-exams/spring-2023|SP2023 MT2]] #6 and [[exams/midterm-2/past-exams/fall-2023|FA2023 MT2]] #4 have complex $h$).
> - **A cosine is not an eigenfunction** ([[exams/midterm-2/past-exams/fall-2021|FA2021 MT2]] 1(a), False); only $e^{j\omega_0 n}$ is.
> - **Magnitude is never negative.** $H_d(\frac{\pi}{2})=-1$ is gain $1$, phase $\pi$.
> - **Phase in radians:** $\angle H_d=\sin\omega$ at $\frac{\pi}{3}$ is $\frac{\sqrt3}{2}\approx0.87$ rad.
> - **$H_d(\pm\pi)$ of a real system is real.** A formula that gives different values at $\omega=\pi$ and $\omega=-\pi$ jumps there; do not trust its value at $\pi$ ([[exams/midterm-2/past-exams/spring-2025|SP2025 MT2]] #4, discussed in [[3-fourier-analysis/15-frequency-response|Lecture 15]]).
> - **$H_d\neq H(e^{j\omega})$ for marginally stable systems:** the impulse is missing.
> - **One input–output pair reveals $H_d$ only at the input's frequencies** (Lecture 15, slide 11).

**Where it appears.**
- Lectures: [[3-fourier-analysis/15-frequency-response|L15]] (definition, eigenfunctions, sinusoids, $Y_d=X_dH_d$), [[3-fourier-analysis/14-dtft-properties|L14]] (the DTFT–z-transform link, Hermitian symmetry), [[3-fourier-analysis/16-magnitude-and-phase-response|L16]] (magnitude, phase, group delay), [[2-z-transform/06-the-z-transform|L6]] and [[2-z-transform/11-bibo-stability-and-causality|L11]] (eigenfunctions, stability).
- Problem families: [[problems/lti-response-to-sinusoids|LTI response to sinusoids]], [[problems/magnitude-phase-and-group-delay|magnitude, phase and group delay]].
- Homework: %%hw6:W1tob21ld29yay9odzZ8SFc2XV0=%%HW6%%/hw6%% #5–#7.
- Past exams: [[exams/midterm-2/past-exams/fall-2024|FA2024 MT2]] #3, #4; [[exams/midterm-2/past-exams/spring-2025|SP2025 MT2]] #3, #4; [[exams/midterm-2/past-exams/spring-2023|SP2023 MT2]] #5, #6; [[exams/midterm-2/past-exams/fall-2023|FA2023 MT2]] #4; [[exams/midterm-2/past-exams/fall-2021|FA2021 MT2]] 1(a), #2; [[exams/midterm-2/past-exams/fall-2019|FA2019 MT2]] 1(d), #6, #7.
- Try it live: [[demos/frequency-response-explorer|frequency response explorer]].

Related: [[concepts/eigenfunctions-of-lti-systems|eigenfunctions of LTI systems]] · [[concepts/transfer-function|transfer function]] · [[concepts/dtft|DTFT]] · [[concepts/dtft-properties|DTFT properties]] · [[concepts/magnitude-and-phase-response|magnitude and phase response]] · [[concepts/group-delay|group delay]] · [[concepts/bibo-stability|BIBO stability]] · [[concepts/poles-and-zeros|poles and zeros]]

### Sources for this page
Lecture 15 notes §1 (eqs. 1–22, Figure 1) and slides 3–11; Lecture 14 notes §1; HW6 #5–#7; past-exam keys cited above. The sinusoidal responses are verified in `verify/LB_l15.py` by building systems with the stated $H_d$ values and convolving; the FIR frequency responses, gains and notch in `verify/LB_concepts.py`.
