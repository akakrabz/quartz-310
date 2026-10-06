---
title: "Lecture 15 — Frequency response"
description: "H_d(ω) as the DTFT of h[n] and H(z) on the unit circle; complex exponentials as eigenfunctions, e^{jω₀n} → H_d(ω₀)e^{jω₀n}; A cos(ω₀n+θ) → A|H_d(ω₀)|cos(ω₀n+θ+∠H_d(ω₀)) for real h, and what goes wrong when h is complex; sums of sinusoids, constants and (−1)ⁿ; inferring a response from one input–output pair; aperiodic inputs via Y_d = X_dH_d; the z-domain vs frequency-domain summary."
tags: [lecture, midterm-2, frequency-response, dtft]
lecture: 15
---

*Lecture 15 · Fri Oct 2, 2026 · notes + slides "Frequency response" · prev: [[3-fourier-analysis/14-dtft-properties|Lecture 14]] · next: [[3-fourier-analysis/16-magnitude-and-phase-response|Lecture 16]]*

> [!abstract] In one breath
> The DTFT of the impulse response is the system's **frequency response**, $H_d(\omega)=\sum_n h[n]e^{-j\omega n}$: the transfer function on the unit circle whenever the system is stable. Because $e^{j\omega_0 n}$ is an eigenfunction of every LTI system, that one function answers every sinusoidal question: $e^{j\omega_0 n}$ leaves as $H_d(\omega_0)\,e^{j\omega_0 n}$, its amplitude multiplied by $|H_d(\omega_0)|$ and its phase shifted by $\angle H_d(\omega_0)$. A real cosine is two exponentials, at $+\omega_0$ and $-\omega_0$. If $h$ is **real**, Hermitian symmetry makes their two eigenvalues conjugates and they recombine into one cosine, $A\cos(\omega_0 n+\theta)\to A|H_d(\omega_0)|\cos(\omega_0 n+\theta+\angle H_d(\omega_0))$; if $h$ is complex there is no such shortcut, and a real input can even produce a complex output. Sums go through term by term (a constant is frequency $0$, $(-1)^n$ is frequency $\pi$), and any input with a DTFT goes through $Y_d(\omega)=X_d(\omega)H_d(\omega)$.

## 1. Transfer function and frequency response

[[2-z-transform/09-transfer-functions|Lecture 9]] named the z-transform of the impulse response the **transfer function**. Its DTFT gets a name too.

> [!key] Frequency response
> $$
> h[n]\ \overset{\mathcal{Z}}{\longleftrightarrow}\ H(z)\ \ \text{(transfer function)}\qquad\qquad h[n]\ \overset{\mathcal{F}}{\longleftrightarrow}\ H_d(\omega)=\sum_{n=-\infty}^{\infty}h[n]\,e^{-j\omega n}\ \ \text{(frequency response)}
> $$
> When the ROC of $H(z)$ contains the unit circle, which for an LTI system means **BIBO stable**, $H_d(\omega)=H(z)\big|_{z=e^{j\omega}}$ ([[3-fourier-analysis/14-dtft-properties|Lecture 14]]). It is $2\pi$-periodic and complex at each $\omega$:
> $$
> H_d(\omega)=|H_d(\omega)|\,e^{j\angle H_d(\omega)},
> $$
> with the **magnitude response** $|H_d(\omega)|\ge0$ and the **phase response** $\angle H_d(\omega)$, a principal angle in $[-\pi,\pi]$. Computing and plotting the two is [[3-fourier-analysis/16-magnitude-and-phase-response|Lecture 16]] ([[concepts/magnitude-and-phase-response|magnitude and phase response]]).

Stability decides what kind of object $H_d$ is. A stable system has an ordinary, continuous $H_d(\omega)$. A marginally stable one (a pole *on* the unit circle) has a frequency response only with an impulse at the pole's frequency, and an input at that frequency resonates ([[2-z-transform/11-bibo-stability-and-causality|Lecture 11]]): the accumulator $y[n]=y[n-1]+x[n]$ has $h=u[n]$ and $H_d(\omega)=\frac{1}{1-e^{-j\omega}}+\pi\delta(\omega)\neq H(e^{j\omega})$%%hw6:IChbW2hvbWV3b3JrL2h3NnxIVzZdXSAjNSk=%%%%/hw6%%. A causal system with a pole outside the unit circle has no frequency response at all.

> [!question] FA2024 MT2 #3(a) — a three-tap system
> $h[n]=\delta[n+2]+\delta[n]+\delta[n-2]$. Find $H_d(\omega)$ and its values at $\omega=0,\ \frac{\pi}{2},\ \pi$.

> [!success]- Answer (checked numerically)
> $H_d(\omega)=e^{j2\omega}+1+e^{-j2\omega}=1+2\cos(2\omega)$, so $H_d(0)=3$, $H_d(\frac{\pi}{2})=-1$, $H_d(\pi)=3$. The value $-1$ is magnitude $1$ and phase $\pi$: a real, even $h$ has a real $H_d$, but a magnitude response is never negative, so the plot asked for in part (b) is $|1+2\cos 2\omega|$ ([[exams/midterm-2/past-exams/fall-2024|FA2024 MT2]] #3).

> [!intuition] Zeros on the unit circle are notches
> "A zero blocks an exponential" ([[concepts/eigenfunctions-of-lti-systems|eigenfunctions]]) becomes, on the unit circle, "a zero at $e^{j\omega_0}$ removes the frequency $\omega_0$". $H(z)=1+z^{-4}$ has zeros at $e^{\pm j\pi/4}$ and $e^{\pm j3\pi/4}$, so $H_d(\frac{\pi}{4})=0$: in [[exams/midterm-2/past-exams/fall-2019|FA2019 MT2]] #7 the input $3+4\cos(\frac{\pi}{4}n)+e^{j\pi n/2}$ comes out as $6+2e^{j\pi n/2}$, the cosine gone.

## 2. Complex exponentials are eigenfunctions

[[2-z-transform/06-the-z-transform|Lecture 6]] showed that $z_0^{\,n}$ passes through any LTI system as $H(z_0)\,z_0^{\,n}$ ([[concepts/eigenfunctions-of-lti-systems|eigenfunctions of LTI systems]]). The DTFT is the z-transform on the unit circle, so take $z_0=e^{j\omega_0}$:

> [!key] Response to a complex exponential
> $$
> x[n]=A\,e^{j\omega_0 n}\ \ (\text{all } n)\quad\Longrightarrow\quad y[n]=H_d(\omega_0)\,A\,e^{j\omega_0 n}=|H_d(\omega_0)|\,A\,e^{j\left(\omega_0 n+\angle H_d(\omega_0)\right)} .
> $$
> Same frequency; amplitude scaled by $|H_d(\omega_0)|$; phase shifted by $\angle H_d(\omega_0)$ ($A$ may be complex). This holds for **any** LTI system, real or complex $h$, as long as $H_d(\omega_0)$ is finite. The input must last for all $n$; a one-sided $e^{j\omega_0 n}u[n]$ adds a transient.

> [!derivation]- The same result from $Y_d=X_dH_d$ (notes eqs. 17–22)
> $X_d(\omega)=2\pi A\,\delta(\omega-\omega_0)$, so $Y_d(\omega)=2\pi A\,\delta(\omega-\omega_0)H_d(\omega)=2\pi A\,H_d(\omega_0)\,\delta(\omega-\omega_0)$ (an impulse only samples $H_d$ where it sits). Invert:
> $$
> y[n]=\frac{1}{2\pi}\int_{-\pi}^{\pi}2\pi A\,H_d(\omega_0)\,\delta(\omega-\omega_0)\,e^{j\omega n}\,d\omega=H_d(\omega_0)\,A\,e^{j\omega_0 n}.
> $$

<figure class="ece-fig"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 640 250" width="640" height="250" role="img" aria-label="Magnitude |omega| and phase -omega/2 with markers at pi/3 and pi/2" style="font-family:'Source Sans 3','Source Sans Pro',system-ui,sans-serif;font-size:13px"><text x="169.0" y="24.0" text-anchor="middle" fill="currentColor" style="font-size:13px;font-weight:600">|H<tspan baseline-shift="sub" style="font-size:75%">d</tspan>(ω)| = |ω|</text><line x1="34.0" y1="158.6" x2="304.0" y2="158.6" stroke="var(--muted)" stroke-width="0.6" stroke-dasharray="3 3" opacity="0.6"/><line x1="34.0" y1="107.1" x2="304.0" y2="107.1" stroke="var(--muted)" stroke-width="0.6" stroke-dasharray="3 3" opacity="0.6"/><line x1="34.0" y1="55.7" x2="304.0" y2="55.7" stroke="var(--muted)" stroke-width="0.6" stroke-dasharray="3 3" opacity="0.6"/><line x1="34.0" y1="210.0" x2="304.0" y2="210.0" stroke="currentColor" stroke-width="1" opacity="0.75"/><line x1="169.0" y1="30.0" x2="169.0" y2="210.0" stroke="currentColor" stroke-width="1" opacity="0.75"/><line x1="34.0" y1="207.0" x2="34.0" y2="213.0" stroke="currentColor" stroke-width="1"/><text x="34.0" y="224.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">−π</text><line x1="101.5" y1="207.0" x2="101.5" y2="213.0" stroke="currentColor" stroke-width="1"/><text x="101.5" y="224.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">−π/2</text><line x1="169.0" y1="207.0" x2="169.0" y2="213.0" stroke="currentColor" stroke-width="1"/><text x="169.0" y="224.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">0</text><line x1="236.5" y1="207.0" x2="236.5" y2="213.0" stroke="currentColor" stroke-width="1"/><text x="236.5" y="224.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">π/2</text><line x1="304.0" y1="207.0" x2="304.0" y2="213.0" stroke="currentColor" stroke-width="1"/><text x="304.0" y="224.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">π</text><line x1="166.0" y1="158.6" x2="172.0" y2="158.6" stroke="currentColor" stroke-width="1"/><text x="30.0" y="162.6" text-anchor="end" fill="var(--muted)" style="font-size:11px">1</text><line x1="166.0" y1="107.1" x2="172.0" y2="107.1" stroke="currentColor" stroke-width="1"/><text x="30.0" y="111.1" text-anchor="end" fill="var(--muted)" style="font-size:11px">2</text><line x1="166.0" y1="55.7" x2="172.0" y2="55.7" stroke="currentColor" stroke-width="1"/><text x="30.0" y="59.7" text-anchor="end" fill="var(--muted)" style="font-size:11px">3</text><text x="304.0" y="204.0" text-anchor="end" fill="var(--muted)" style="font-size:12px">ω</text><polyline points="34.0,48.4 169.0,210.0 304.0,48.4" fill="none" stroke="var(--accent)" stroke-width="1.8" stroke-linejoin="round" stroke-linecap="round" opacity="1.0"/><text x="498.0" y="24.0" text-anchor="middle" fill="currentColor" style="font-size:13px;font-weight:600">∠H<tspan baseline-shift="sub" style="font-size:75%">d</tspan>(ω) = −ω/2</text><line x1="366.0" y1="197.6" x2="630.0" y2="197.6" stroke="var(--muted)" stroke-width="0.6" stroke-dasharray="3 3" opacity="0.6"/><line x1="366.0" y1="158.8" x2="630.0" y2="158.8" stroke="var(--muted)" stroke-width="0.6" stroke-dasharray="3 3" opacity="0.6"/><line x1="366.0" y1="81.2" x2="630.0" y2="81.2" stroke="var(--muted)" stroke-width="0.6" stroke-dasharray="3 3" opacity="0.6"/><line x1="366.0" y1="42.4" x2="630.0" y2="42.4" stroke="var(--muted)" stroke-width="0.6" stroke-dasharray="3 3" opacity="0.6"/><line x1="366.0" y1="120.0" x2="630.0" y2="120.0" stroke="currentColor" stroke-width="1" opacity="0.75"/><line x1="498.0" y1="30.0" x2="498.0" y2="210.0" stroke="currentColor" stroke-width="1" opacity="0.75"/><line x1="366.0" y1="117.0" x2="366.0" y2="123.0" stroke="currentColor" stroke-width="1"/><text x="366.0" y="224.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">−π</text><line x1="432.0" y1="117.0" x2="432.0" y2="123.0" stroke="currentColor" stroke-width="1"/><text x="432.0" y="224.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">−π/2</text><line x1="498.0" y1="117.0" x2="498.0" y2="123.0" stroke="currentColor" stroke-width="1"/><text x="498.0" y="224.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">0</text><line x1="564.0" y1="117.0" x2="564.0" y2="123.0" stroke="currentColor" stroke-width="1"/><text x="564.0" y="224.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">π/2</text><line x1="630.0" y1="117.0" x2="630.0" y2="123.0" stroke="currentColor" stroke-width="1"/><text x="630.0" y="224.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">π</text><line x1="495.0" y1="197.6" x2="501.0" y2="197.6" stroke="currentColor" stroke-width="1"/><text x="362.0" y="201.6" text-anchor="end" fill="var(--muted)" style="font-size:11px">−π/2</text><line x1="495.0" y1="158.8" x2="501.0" y2="158.8" stroke="currentColor" stroke-width="1"/><text x="362.0" y="162.8" text-anchor="end" fill="var(--muted)" style="font-size:11px">−π/4</text><line x1="495.0" y1="81.2" x2="501.0" y2="81.2" stroke="currentColor" stroke-width="1"/><text x="362.0" y="85.2" text-anchor="end" fill="var(--muted)" style="font-size:11px">π/4</text><line x1="495.0" y1="42.4" x2="501.0" y2="42.4" stroke="currentColor" stroke-width="1"/><text x="362.0" y="46.4" text-anchor="end" fill="var(--muted)" style="font-size:11px">π/2</text><text x="630.0" y="114.0" text-anchor="end" fill="var(--muted)" style="font-size:12px">ω</text><polyline points="366.0,42.4 630.0,197.6" fill="none" stroke="var(--accent)" stroke-width="1.8" stroke-linejoin="round" stroke-linecap="round" opacity="1.0"/><line x1="214.0" y1="30.0" x2="214.0" y2="210.0" stroke="var(--hi)" stroke-width="0.9" stroke-dasharray="2 3"/><line x1="542.0" y1="30.0" x2="542.0" y2="210.0" stroke="var(--hi)" stroke-width="0.9" stroke-dasharray="2 3"/><circle cx="214.0" cy="156.1" r="3.5" fill="var(--hi)" stroke="var(--hi)" stroke-width="1.5"/><circle cx="542.0" cy="145.9" r="3.5" fill="var(--hi)" stroke="var(--hi)" stroke-width="1.5"/><line x1="236.5" y1="30.0" x2="236.5" y2="210.0" stroke="var(--hi)" stroke-width="0.9" stroke-dasharray="2 3"/><line x1="564.0" y1="30.0" x2="564.0" y2="210.0" stroke="var(--hi)" stroke-width="0.9" stroke-dasharray="2 3"/><circle cx="236.5" cy="129.2" r="3.5" fill="var(--hi)" stroke="var(--hi)" stroke-width="1.5"/><circle cx="564.0" cy="158.8" r="3.5" fill="var(--hi)" stroke="var(--hi)" stroke-width="1.5"/><text x="206.0" y="40.3" text-anchor="middle" fill="var(--hi)" style="font-size:10px">π/3</text><text x="246.5" y="40.3" text-anchor="middle" fill="var(--hi)" style="font-size:10px">π/2</text><circle cx="630.0" cy="197.6" r="3.5" fill="none" stroke="var(--muted)" stroke-width="1.5"/><circle cx="366.0" cy="42.4" r="3.5" fill="none" stroke="var(--muted)" stroke-width="1.5"/></svg><figcaption><strong>The system of slide 6, and where the input lives.</strong> The input 2e<sup>jπn/3</sup> + e<sup>j(πn/2 + π/4)</sup> contains only the frequencies π/3 and π/2 (red), so only the two values H<sub>d</sub>(π/3) and H<sub>d</sub>(π/2) matter: read the magnitude on the left and the phase on the right. The phase −ω/2 runs from π/2 at ω = −π down to −π/2 at ω = π, so the 2π-periodic extension jumps at ω = ±π (hollow dots) — harmless here, because no input sits there.</figcaption></figure>

> [!question] Slide 6 — a system given by its magnitude and phase
> $|H_d(\omega)|=|\omega|$ and $\angle H_d(\omega)=-\frac{\omega}{2}$ for $-\pi\le\omega\le\pi$.
> (a) Write $H_d(\omega)$. (b) Find $y[n]$ for $x[n]=2e^{j\frac{\pi}{3}n}+e^{j\left(\frac{\pi}{2}n+\frac{\pi}{4}\right)}$.

> [!success]- Answer (no annotated slides exist for this lecture; checked by building a real FIR filter with the same two values of $H_d$ and convolving)
> **(a)** $H_d(\omega)=|\omega|\,e^{-j\omega/2}$ for $-\pi\le\omega\le\pi$, repeated every $2\pi$.
>
> **(b)** Two eigenfunctions, two eigenvalues: $H_d(\frac{\pi}{3})=\frac{\pi}{3}e^{-j\pi/6}$ and $H_d(\frac{\pi}{2})=\frac{\pi}{2}e^{-j\pi/4}$. Multiply magnitudes, add phases:
> $$
> y[n]=2\cdot\tfrac{\pi}{3}\,e^{j\left(\frac{\pi}{3}n-\frac{\pi}{6}\right)}+\tfrac{\pi}{2}\,e^{j\left(\frac{\pi}{2}n+\frac{\pi}{4}-\frac{\pi}{4}\right)}=\tfrac{2\pi}{3}\,e^{j\left(\frac{\pi}{3}n-\frac{\pi}{6}\right)}+\tfrac{\pi}{2}\,e^{j\frac{\pi}{2}n}.
> $$
> The second term's phase offset $\frac{\pi}{4}$ is exactly cancelled by the system's $-\frac{\pi}{4}$. No realness was needed: each input term is a single exponential.

## 3. Real sinusoids, and why $h$ must be real

A cosine is not an eigenfunction: it is the sum of two, at $+\omega_0$ and $-\omega_0$. Push each half through separately (slide 8, notes eqs. 9–15):

$$
\begin{aligned}
x[n]&=A\cos(\omega_0 n+\theta)=\tfrac{A}{2}e^{j(\omega_0 n+\theta)}+\tfrac{A}{2}e^{-j(\omega_0 n+\theta)}\\
y[n]&=\tfrac{A}{2}H_d(\omega_0)\,e^{j(\omega_0 n+\theta)}+\tfrac{A}{2}H_d(-\omega_0)\,e^{-j(\omega_0 n+\theta)}\\
&=\tfrac{A}{2}|H_d(\omega_0)|\,e^{j(\omega_0 n+\theta+\angle H_d(\omega_0))}+\tfrac{A}{2}|H_d(-\omega_0)|\,e^{-j(\omega_0 n+\theta-\angle H_d(-\omega_0))}.
\end{aligned}
$$

Nothing yet forces the two terms to be conjugates. That is what a **real** $h$ supplies: its frequency response is Hermitian ([[3-fourier-analysis/14-dtft-properties|Lecture 14]]), $|H_d(-\omega_0)|=|H_d(\omega_0)|$ and $\angle H_d(-\omega_0)=-\angle H_d(\omega_0)$. The second term becomes the conjugate of the first, and the sum is twice its real part.

> [!key] Sinusoidal response of a real LTI system
> $$
> h[n]\ \text{real}:\qquad A\cos(\omega_0 n+\theta)\ \longrightarrow\ A\,|H_d(\omega_0)|\cos\!\big(\omega_0 n+\theta+\angle H_d(\omega_0)\big),
> $$
> and the same with $\sin$ in place of $\cos$. Same frequency; gain $|H_d(\omega_0)|$; phase shift $\angle H_d(\omega_0)$. An LTI system never creates a frequency that is not in its input.

**What happens when $h$ is complex.** Then $H_d(-\omega_0)$ is unrelated to $H_d(\omega_0)$, and only the two-term line above is valid. The smallest example: $h[n]=\frac12\big(\delta[n]+j\,\delta[n-1]\big)$ has $H_d(\omega)=\frac12(1+je^{-j\omega})$, so $H_d(\frac{\pi}{2})=1$ but $H_d(-\frac{\pi}{2})=0$. The input $\cos(\frac{\pi}{2}n)$ keeps its $e^{j\pi n/2}$ half and loses the other:

$$
y[n]=\tfrac12\cos\!\left(\tfrac{\pi}{2}n\right)+\tfrac{j}{2}\cos\!\left(\tfrac{\pi}{2}(n-1)\right)=\tfrac12\cos\!\left(\tfrac{\pi}{2}n\right)+\tfrac{j}{2}\sin\!\left(\tfrac{\pi}{2}n\right)=\tfrac12\,e^{j\frac{\pi}{2}n},
$$

a complex exponential, while the real-$h$ formula would have predicted $|H_d(\frac{\pi}{2})|\cos(\frac{\pi}{2}n+0)=\cos(\frac{\pi}{2}n)$ (checked with `lfilter`).

> [!recipe] Before using the cosine formula: is $h$ real?
> 1. Write $H_d=|H_d|e^{j\angle H_d}$ on the whole period $-\pi\le\omega\le\pi$ (a sign in front is part of the phase).
> 2. Real $h$ $\iff$ $H_d(-\omega)=H_d^*(\omega)$ $\iff$ $|H_d|$ even and $\angle H_d$ odd. Quick necessary checks: $H_d(0)$ and $H_d(\pi)$ are real.
> 3. Real: use the cosine formula for every sinusoid. Not real: split every $\cos$ and $\sin$ into $e^{\pm j\omega_0 n}$ and use $H_d(\omega_0)$ and $H_d(-\omega_0)$ separately.

> [!question] An exam item to try (SP2023 MT2 #6)
> $H_d(\omega)=\omega\,e^{j\pi\cos\omega}$ for $|\omega|\le\pi$. Find the response to $x[n]=3+e^{j\frac{\pi}{3}n}+\sin\!\left(\frac{\pi}{2}n+\frac{\pi}{4}\right)$.

> [!success]- Answer (matches the key; checked with a complex FIR filter having the same four values of $H_d$)
> **Is $h$ real?** $H_d(-\omega)=-\omega\,e^{j\pi\cos\omega}$ but $H_d^*(\omega)=\omega\,e^{-j\pi\cos\omega}$: not equal, so $h$ is complex and the sine must be split. The values needed: $H_d(0)=0$, $H_d(\frac{\pi}{3})=\frac{\pi}{3}e^{j\pi/2}=j\frac{\pi}{3}$, $H_d(\frac{\pi}{2})=\frac{\pi}{2}e^{j0}=\frac{\pi}{2}$, $H_d(-\frac{\pi}{2})=-\frac{\pi}{2}$. With $\phi=\frac{\pi}{2}n+\frac{\pi}{4}$,
> $$
> \sin\phi=\frac{e^{j\phi}-e^{-j\phi}}{2j}\ \longrightarrow\ \frac{\frac{\pi}{2}e^{j\phi}-\left(-\frac{\pi}{2}\right)e^{-j\phi}}{2j}=\frac{\pi}{2}\cdot\frac{2\cos\phi}{2j}=-j\,\frac{\pi}{2}\cos\phi .
> $$
> $$
> y[n]=\frac{\pi}{3}\,e^{j\left(\frac{\pi}{3}n+\frac{\pi}{2}\right)}-j\,\frac{\pi}{2}\cos\!\left(\frac{\pi}{2}n+\frac{\pi}{4}\right).
> $$
> A real sine in, an imaginary cosine out. Using the real-$h$ formula would give $\frac{\pi}{2}\sin(\frac{\pi}{2}n+\frac{\pi}{4})$, which is wrong. [[exams/midterm-2/past-exams/fall-2023|FA2023 MT2]] #4 is built the same way: $H_d=(\frac12+\cos\omega)e^{j|\omega|}$ has an even phase, $H_d(\pm\frac{3\pi}{4})$ are equal rather than conjugate, and $3\sin(\frac{3\pi}{4}n)$ leaves as $\frac{3(\sqrt2-1)}{2}e^{-j\pi/4}\sin(\frac{3\pi}{4}n)$, a sine times a complex constant.

> [!trap] A cosine is not an eigenfunction
> "$\cos(\omega_0 n)$ is an eigenfunction of a stable LTI system" is **False** ([[exams/midterm-2/past-exams/fall-2021|FA2021 MT2]] 1(a)): even for real $h$ the output $|H_d|\cos(\omega_0 n+\angle H_d)$ is a shifted cosine, a multiple of the input only when $\angle H_d(\omega_0)$ is $0$ or $\pi$. And "the cosine formula holds for every $\omega_0$ and $\phi$, so $h$ can be real or complex" is **False** ([[exams/midterm-2/past-exams/fall-2019|FA2019 MT2]] 1(d)): the formula holding for all inputs forces Hermitian symmetry, so $h$ must be real.

## 4. Sums of sinusoids, constants and $(-1)^n$

Linearity does the rest. Two special frequencies deserve names: a **constant** $c=c\,e^{j0n}$ lives at $\omega=0$ and leaves as $H_d(0)\,c$; the alternating sequence $(-1)^n=e^{j\pi n}=\cos(\pi n)$ lives at $\omega=\pi$ and leaves as $H_d(\pi)(-1)^n$. For a real system both gains are **real** numbers, possibly negative (a sign flip is phase $\pi$).

> [!recipe] Response to a sum of sinusoids (FA2024 MT2 #4, SP2025 MT2 #4, SP2023 MT2 #6, FA2019 MT2 #7)
> 1. **Decide whether $h$ is real** (§3). Convert any degrees to radians (HW6 #7 writes $45^\circ$).
> 2. **List the frequencies** of the input terms, each in $[-\pi,\pi]$: constant → $0$; $(-1)^n$ → $\pi$; $j^n=e^{j\pi n/2}$ → $\frac{\pi}{2}$ (a single exponential: no partner at $-\frac{\pi}{2}$).
> 3. **Evaluate $H_d$** at each frequency, in polar form. A gain of $0$ deletes the term.
> 4. **Apply** the exponential rule to single exponentials and the cosine rule to real sinusoids (real $h$ only), then add. The phase response is in radians: $\angle H_d=\sin\omega$ at $\omega=\frac{\pi}{3}$ is $\frac{\sqrt3}{2}\approx0.866$ rad, not $\frac{\sqrt3}{2}\pi$.

> [!question] Slide 10 (concept check)
> $|H_d(\omega)|=\cos^2\omega$ and $\angle H_d(\omega)=\sin\omega$ for $-\pi\le\omega\le\pi$.
> (a) Is the system real-valued (is $h[n]$ real)? (b) Find $y[n]$ for $x[n]=\sin\!\left(\frac{\pi}{3}n\right)+\cos\!\left(\frac{\pi}{2}n+\frac{3\pi}{10}\right)+(-1)^n$.

> [!success]- Answer (checked: $h[n]$ computed from $H_d$ by an inverse FFT is real, and convolving it with $x$ reproduces $y$ — see the Python below)
> **(a) Yes.** $\cos^2\omega$ is even and $\sin\omega$ is odd, so $H_d(-\omega)=\cos^2\omega\,e^{-j\sin\omega}=H_d^*(\omega)$: Hermitian, hence $h$ real. The endpoint values agree, $H_d(\pi)=H_d(-\pi)=1$. ($h$ is two-sided: $h[0]\approx0.440$, $h[\pm1]\approx\mp0.115$, $h[\pm2]\approx0.249$, …)
>
> **(b)** Evaluate at the three input frequencies:
> - $\omega=\frac{\pi}{3}$: gain $\cos^2\frac{\pi}{3}=\frac14$, phase $\sin\frac{\pi}{3}=\frac{\sqrt3}{2}$ rad, so $\sin(\frac{\pi}{3}n)\to\frac14\sin\!\left(\frac{\pi}{3}n+\frac{\sqrt3}{2}\right)$.
> - $\omega=\frac{\pi}{2}$: gain $\cos^2\frac{\pi}{2}=0$: the cosine is removed, whatever its phase $\frac{3\pi}{10}$.
> - $\omega=\pi$: $H_d(\pi)=\cos^2\pi\,e^{j\sin\pi}=1$, so $(-1)^n$ passes unchanged.
> $$
> y[n]=\tfrac14\sin\!\left(\tfrac{\pi}{3}n+\tfrac{\sqrt3}{2}\right)+(-1)^n .
> $$
>
> <figure class="ece-fig"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 640 250" width="640" height="250" role="img" aria-label="cos squared omega and sin omega with markers at pi/3, pi/2 and pi" style="font-family:'Source Sans 3','Source Sans Pro',system-ui,sans-serif;font-size:13px"><text x="169.0" y="24.0" text-anchor="middle" fill="currentColor" style="font-size:13px;font-weight:600">|H<tspan baseline-shift="sub" style="font-size:75%">d</tspan>(ω)| = cos²ω</text><line x1="34.0" y1="170.9" x2="304.0" y2="170.9" stroke="var(--muted)" stroke-width="0.6" stroke-dasharray="3 3" opacity="0.6"/><line x1="34.0" y1="131.7" x2="304.0" y2="131.7" stroke="var(--muted)" stroke-width="0.6" stroke-dasharray="3 3" opacity="0.6"/><line x1="34.0" y1="53.5" x2="304.0" y2="53.5" stroke="var(--muted)" stroke-width="0.6" stroke-dasharray="3 3" opacity="0.6"/><line x1="34.0" y1="210.0" x2="304.0" y2="210.0" stroke="currentColor" stroke-width="1" opacity="0.75"/><line x1="169.0" y1="30.0" x2="169.0" y2="210.0" stroke="currentColor" stroke-width="1" opacity="0.75"/><line x1="34.0" y1="207.0" x2="34.0" y2="213.0" stroke="currentColor" stroke-width="1"/><text x="34.0" y="224.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">−π</text><line x1="101.5" y1="207.0" x2="101.5" y2="213.0" stroke="currentColor" stroke-width="1"/><text x="101.5" y="224.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">−π/2</text><line x1="169.0" y1="207.0" x2="169.0" y2="213.0" stroke="currentColor" stroke-width="1"/><text x="169.0" y="224.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">0</text><line x1="236.5" y1="207.0" x2="236.5" y2="213.0" stroke="currentColor" stroke-width="1"/><text x="236.5" y="224.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">π/2</text><line x1="304.0" y1="207.0" x2="304.0" y2="213.0" stroke="currentColor" stroke-width="1"/><text x="304.0" y="224.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">π</text><line x1="166.0" y1="170.9" x2="172.0" y2="170.9" stroke="currentColor" stroke-width="1"/><text x="30.0" y="174.9" text-anchor="end" fill="var(--muted)" style="font-size:11px">¼</text><line x1="166.0" y1="131.7" x2="172.0" y2="131.7" stroke="currentColor" stroke-width="1"/><text x="30.0" y="135.7" text-anchor="end" fill="var(--muted)" style="font-size:11px">½</text><line x1="166.0" y1="53.5" x2="172.0" y2="53.5" stroke="currentColor" stroke-width="1"/><text x="30.0" y="57.5" text-anchor="end" fill="var(--muted)" style="font-size:11px">1</text><text x="304.0" y="204.0" text-anchor="end" fill="var(--muted)" style="font-size:12px">ω</text><polyline points="34.0,53.5 37.4,54.4 39.1,55.6 41.8,58.5 45.5,64.4 49.2,72.2 52.6,80.9 57.0,94.0 74.8,157.1 82.9,182.6 88.3,195.8 92.7,203.6 97.1,208.4 100.8,210.0 104.2,209.4 105.9,208.4 108.6,205.8 112.0,200.9 116.4,192.0 120.1,182.6 125.5,166.2 142.3,106.4 147.7,88.8 151.4,78.2 155.8,67.7 160.2,59.9 163.9,55.6 165.6,54.4 168.3,53.5 170.3,53.6 172.4,54.4 174.1,55.6 176.8,58.5 179.5,62.6 182.2,67.7 186.6,78.2 194.7,102.9 212.5,166.2 217.9,182.6 223.3,195.8 227.7,203.6 232.1,208.4 235.8,210.0 238.2,209.8 240.9,208.4 245.3,203.6 248.0,199.1 251.4,192.0 255.1,182.6 263.2,157.1 280.0,97.3 285.4,80.9 289.1,71.4 292.5,64.4 296.2,58.5 298.9,55.6 300.6,54.4 302.6,53.6 304.0,53.5" fill="none" stroke="var(--accent)" stroke-width="1.8" stroke-linejoin="round" stroke-linecap="round" opacity="1.0"/><text x="498.0" y="24.0" text-anchor="middle" fill="currentColor" style="font-size:13px;font-weight:600">∠H<tspan baseline-shift="sub" style="font-size:75%">d</tspan>(ω) = sin ω  (radians)</text><line x1="366.0" y1="198.3" x2="630.0" y2="198.3" stroke="var(--muted)" stroke-width="0.6" stroke-dasharray="3 3" opacity="0.6"/><line x1="366.0" y1="41.7" x2="630.0" y2="41.7" stroke="var(--muted)" stroke-width="0.6" stroke-dasharray="3 3" opacity="0.6"/><line x1="366.0" y1="120.0" x2="630.0" y2="120.0" stroke="currentColor" stroke-width="1" opacity="0.75"/><line x1="498.0" y1="30.0" x2="498.0" y2="210.0" stroke="currentColor" stroke-width="1" opacity="0.75"/><line x1="366.0" y1="117.0" x2="366.0" y2="123.0" stroke="currentColor" stroke-width="1"/><text x="366.0" y="224.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">−π</text><line x1="432.0" y1="117.0" x2="432.0" y2="123.0" stroke="currentColor" stroke-width="1"/><text x="432.0" y="224.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">−π/2</text><line x1="498.0" y1="117.0" x2="498.0" y2="123.0" stroke="currentColor" stroke-width="1"/><text x="498.0" y="224.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">0</text><line x1="564.0" y1="117.0" x2="564.0" y2="123.0" stroke="currentColor" stroke-width="1"/><text x="564.0" y="224.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">π/2</text><line x1="630.0" y1="117.0" x2="630.0" y2="123.0" stroke="currentColor" stroke-width="1"/><text x="630.0" y="224.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">π</text><line x1="495.0" y1="198.3" x2="501.0" y2="198.3" stroke="currentColor" stroke-width="1"/><text x="362.0" y="202.3" text-anchor="end" fill="var(--muted)" style="font-size:11px">−1</text><line x1="495.0" y1="41.7" x2="501.0" y2="41.7" stroke="currentColor" stroke-width="1"/><text x="362.0" y="45.7" text-anchor="end" fill="var(--muted)" style="font-size:11px">1</text><polyline points="366.0,120.0 377.2,140.7 386.1,156.1 395.0,169.9 403.9,181.5 411.5,189.2 417.1,193.4 423.8,196.8 427.7,197.9 431.3,198.3 435.0,198.1 439.3,197.1 443.9,195.2 446.9,193.4 452.5,189.2 455.8,186.1 463.4,177.5 470.0,168.5 479.9,152.8 489.8,135.3 511.5,95.2 518.1,83.9 526.0,71.5 533.6,61.3 542.5,51.7 548.8,46.8 552.1,44.8 555.8,43.2 559.7,42.1 563.3,41.7 568.3,42.1 572.2,43.2 575.9,44.8 580.8,47.9 584.5,50.8 588.8,54.9 597.7,65.5 605.6,77.0 615.2,92.9 630.0,120.0" fill="none" stroke="var(--accent)" stroke-width="1.8" stroke-linejoin="round" stroke-linecap="round" opacity="1.0"/><text x="536.0" y="56.2" text-anchor="end" fill="var(--hi)" style="font-size:11px">√3/2</text><text x="623.0" y="113.0" text-anchor="end" fill="var(--hi)" style="font-size:11px">0</text><text x="220.0" y="166.9" text-anchor="start" fill="var(--hi)" style="font-size:11px">¼</text><text x="242.5" y="204.0" text-anchor="start" fill="var(--hi)" style="font-size:11px">0</text><text x="297.0" y="57.5" text-anchor="end" fill="var(--hi)" style="font-size:11px">1</text><line x1="214.0" y1="30.0" x2="214.0" y2="210.0" stroke="var(--hi)" stroke-width="0.9" stroke-dasharray="2 3"/><line x1="542.0" y1="30.0" x2="542.0" y2="210.0" stroke="var(--hi)" stroke-width="0.9" stroke-dasharray="2 3"/><circle cx="214.0" cy="170.9" r="3.5" fill="var(--hi)" stroke="var(--hi)" stroke-width="1.5"/><circle cx="542.0" cy="52.2" r="3.5" fill="var(--hi)" stroke="var(--hi)" stroke-width="1.5"/><line x1="236.5" y1="30.0" x2="236.5" y2="210.0" stroke="var(--hi)" stroke-width="0.9" stroke-dasharray="2 3"/><line x1="564.0" y1="30.0" x2="564.0" y2="210.0" stroke="var(--hi)" stroke-width="0.9" stroke-dasharray="2 3"/><circle cx="236.5" cy="210.0" r="3.5" fill="var(--hi)" stroke="var(--hi)" stroke-width="1.5"/><circle cx="564.0" cy="41.7" r="3.5" fill="var(--hi)" stroke="var(--hi)" stroke-width="1.5"/><line x1="304.0" y1="30.0" x2="304.0" y2="210.0" stroke="var(--hi)" stroke-width="0.9" stroke-dasharray="2 3"/><line x1="630.0" y1="30.0" x2="630.0" y2="210.0" stroke="var(--hi)" stroke-width="0.9" stroke-dasharray="2 3"/><circle cx="304.0" cy="53.5" r="3.5" fill="var(--hi)" stroke="var(--hi)" stroke-width="1.5"/><circle cx="630.0" cy="120.0" r="3.5" fill="var(--hi)" stroke="var(--hi)" stroke-width="1.5"/><circle cx="124.0" cy="170.9" r="3.5" fill="none" stroke="var(--muted)" stroke-width="1.5"/><circle cx="454.0" cy="187.8" r="3.5" fill="none" stroke="var(--muted)" stroke-width="1.5"/><circle cx="101.5" cy="210.0" r="3.5" fill="none" stroke="var(--muted)" stroke-width="1.5"/><circle cx="432.0" cy="198.3" r="3.5" fill="none" stroke="var(--muted)" stroke-width="1.5"/></svg><figcaption><strong>Reading the concept check off the plots.</strong> Red dots at the three input frequencies: at π/3 the gain is ¼ and the phase √3/2 rad; at π/2 the gain is 0 (the cosine is removed); at π the gain is 1 and the phase 0. The hollow dots at −π/3 and −π/2 are the mirror images that Hermitian symmetry guarantees (same magnitude, opposite phase) — the reason a real system returns a real sinusoid.</figcaption></figure>

> [!question] Slide 11 — one input–output pair, then a new input
> A real LTI system maps $x[n]=5+\cos\!\left(\frac{\pi}{4}n-\frac{\pi}{3}\right)+\sin\!\left(-\frac{2\pi}{3}n\right)$ to $y[n]=-10+\cos\!\left(-\frac{2\pi}{3}n\right)$. Find its response to $v[n]=-1+\sin\!\left(-\frac{\pi}{4}n\right)+2\cos\!\left(\frac{2\pi}{3}n\right)$.

> [!success]- Answer (checked: two different real FIR filters with these three values of $H_d$ both reproduce the given pair and give this response)
> One pair reveals $H_d$ only at the frequencies present in $x$: $0$, $\frac{\pi}{4}$, $\frac{2\pi}{3}$ (and, because $h$ is real, at their negatives). Read them off term by term:
> - $\omega=0$: $5\to-10$, so $H_d(0)=-2$ (gain $2$, phase $\pi$).
> - $\omega=\frac{\pi}{4}$: nothing at $\frac{\pi}{4}$ survives in $y$, so $H_d(\frac{\pi}{4})=0$.
> - $\omega=\frac{2\pi}{3}$: the input term is $\sin(-\frac{2\pi}{3}n)=-\sin(\frac{2\pi}{3}n)$ and the output term is $\cos(-\frac{2\pi}{3}n)=\cos(\frac{2\pi}{3}n)$. We need $-|H_d|\sin(\theta+\angle H_d)=\cos\theta$ with $\theta=\frac{2\pi}{3}n$: $|H_d(\frac{2\pi}{3})|=1$ and $\angle H_d(\frac{2\pi}{3})=-\frac{\pi}{2}$, because $-\sin(\theta-\frac{\pi}{2})=\cos\theta$.
>
> $v[n]$ uses only these frequencies, so its response is determined:
> $$
> -1\to(-2)(-1)=2,\qquad \sin\!\left(-\tfrac{\pi}{4}n\right)\to0,\qquad 2\cos\!\left(\tfrac{2\pi}{3}n\right)\to2\cos\!\left(\tfrac{2\pi}{3}n-\tfrac{\pi}{2}\right)=2\sin\!\left(\tfrac{2\pi}{3}n\right),
> $$
> $$
> \text{response to } v:\quad 2+2\sin\!\left(\tfrac{2\pi}{3}n\right).
> $$
> Had $v$ contained any other frequency, the pair would not have been enough.

> [!question] An exam item to try (FA2024 MT2 #4)
> $H_d(\omega)=|\omega|\,e^{-j\pi\sin\omega}$ for $|\omega|\le\pi$. (a) Is $h[n]$ real? (b) Find the output for $x[n]=3+\cos\!\left(\frac{\pi}{6}n\right)+j^n$.

> [!success]- Answer (matches the key; checked with a real FIR filter having the same values of $H_d$)
> **(a)** $H_d(-\omega)=|\omega|e^{j\pi\sin\omega}=H_d^*(\omega)$: Hermitian, so $h$ is real.
>
> **(b)** $H_d(0)=0$ removes the $3$. $H_d(\frac{\pi}{6})=\frac{\pi}{6}e^{-j\pi/2}$, so $\cos(\frac{\pi}{6}n)\to\frac{\pi}{6}\cos(\frac{\pi}{6}n-\frac{\pi}{2})=\frac{\pi}{6}\sin(\frac{\pi}{6}n)$. $j^n=e^{j\pi n/2}$ is one exponential, and $H_d(\frac{\pi}{2})=\frac{\pi}{2}e^{-j\pi}=-\frac{\pi}{2}$:
> $$
> y[n]=\frac{\pi}{6}\sin\!\left(\frac{\pi}{6}n\right)-\frac{\pi}{2}\,j^n .
> $$

> [!warning] $\omega=\pi$ in a real system, and a slip in the SP2025 key
> For real $h$, $H_d(\pi)=H_d(-\pi)=H_d^*(\pi)$ is real, so a real system maps $(-1)^n$ to a real multiple of $(-1)^n$. [[exams/midterm-2/past-exams/spring-2025|SP2025 MT2]] #4 gives $H_d(\omega)=j\omega\,e^{j\pi\sin\omega}$ on $|\omega|\le\pi$; the key correctly shows $h$ is real, then plugs in $\omega=\pi$, gets $H_d(\pi)=j\pi$ and answers $j\pi(-1)^n$ for the $(-1)^n$ term — an imaginary output from a real input to a real system, which cannot happen. The formula itself is the problem: it gives $j\pi$ at $\omega=\pi$ but $-j\pi$ at $\omega=-\pi$, so its periodic extension jumps there, $h[n]$ decays only like $1/n$, and the sums $\sum_{|k|\le M}(-1)^k h[k]$ are real and tend to $0$, the midpoint of the jump (checked numerically up to $M=2000$). The rest of that key ($0$ for the constant, $\frac{\pi}{2}e^{j(\frac{\pi}{4}n+\frac{\pi}{2}(1+\sqrt2))}$ and $\frac{\pi}{2}\sin(\frac{\pi}{2}n-\frac{\pi}{4})$) is right. Before plugging in $\omega=\pm\pi$, check that the formula agrees with itself there.

## 5. Aperiodic inputs: $Y_d=X_dH_d$

For an input that is not a sum of sinusoids, use the convolution property of [[3-fourier-analysis/14-dtft-properties|Lecture 14]]:

$$
y[n]=x[n]*h[n]\quad\Longleftrightarrow\quad Y_d(\omega)=X_d(\omega)\,H_d(\omega),
$$

valid whenever both DTFTs exist. The system reweights every frequency of the input by $H_d$. To get $y[n]$ back, invert $Y_d$; for rational transforms the fastest route is partial fractions in $e^{-j\omega}$, exactly as in the z-domain.

> [!example] $x[n]=(\frac12)^n u[n]$ into $h[n]=(\frac13)^n u[n]$
> $$
> Y_d(\omega)=\frac{1}{\left(1-\frac12e^{-j\omega}\right)\left(1-\frac13e^{-j\omega}\right)}=\frac{3}{1-\frac12e^{-j\omega}}-\frac{2}{1-\frac13e^{-j\omega}}\quad\Longrightarrow\quad y[n]=\left[3\left(\tfrac12\right)^n-2\left(\tfrac13\right)^n\right]u[n].
> $$
> The same computation as with $Y(z)=X(z)H(z)$, because both ROCs contain the unit circle (checked with `lfilter`). The frequency view adds the reading: $h$ is a low-pass ($|H_d(0)|=\frac32$, $|H_d(\pi)|=\frac34$), so the fast-changing part of $x$ gets half the gain of the slow part.

The notes close with the two uses of $H_d$: computing the response to any input with a DTFT, and **designing** systems that pass or stop chosen frequency bands, the ideal filters of the next lectures.

Here is the slide 10 concept check done by brute force: build $h[n]$ from samples of $H_d(\omega)$ (an inverse DTFT by inverse FFT, accurate here because this $h$ decays extremely fast), convolve, and compare with the answer.

```python
import numpy as np

# Slide 10: H_d(w) = cos^2(w) e^{j sin w}. Get h[n] from samples of H_d (inverse DTFT via the inverse FFT).
N = 256
w = 2 * np.pi * np.arange(N) / N
h = np.roll(np.fft.ifft(np.cos(w) ** 2 * np.exp(1j * np.sin(w))), N // 2)   # h[n] for n = -128..127
print("max |Im h[n]|  :", np.abs(h.imag).max())
print("h[-3..3]       :", np.round(h.real[N // 2 - 3:N // 2 + 4], 4))

n = np.arange(-300, 300)
x = np.sin(np.pi * n / 3) + np.cos(np.pi * n / 2 + 3 * np.pi / 10) + (-1.0) ** n
y = np.convolve(x, h.real)                        # y[k] belongs to time n = k - 300 - 128
ny = np.arange(len(y)) - 428
keep = np.abs(ny) <= 100                          # away from the edges of the finite input
pred = 0.25 * np.sin(np.pi * ny[keep] / 3 + np.sqrt(3) / 2) + (-1.0) ** ny[keep]
print("max |y - prediction|:", np.abs(y[keep] - pred).max())
```

```text
max |Im h[n]|  : 7.279466256070008e-17
h[-3..3]       : [ 0.1199  0.2494  0.1149  0.4401 -0.1149  0.2494 -0.1199]
max |y - prediction|: 1.176836406102666e-14
```

$h$ is real (Hermitian symmetry at work), two-sided and non-causal, and the convolution agrees with $\frac14\sin(\frac{\pi}{3}n+\frac{\sqrt3}{2})+(-1)^n$ to rounding error: the $\cos(\frac{\pi}{2}n+\frac{3\pi}{10})$ term really is gone.

## 6. Summary: the z-domain and the frequency domain

Figure 1 of the notes, as a table:

| | z-domain: transfer function $H(z)$ | frequency domain: frequency response $H_d(\omega)$ |
|---|---|---|
| any input | $X(z)\ \to\ X(z)H(z)$ | $X_d(\omega)\ \to\ X_d(\omega)H_d(\omega)$ |
| eigenfunction | $Az^n\ \to\ H(z)\,Az^n$ ($z$ in the ROC of $H$) | $Ae^{j\omega_0 n}\ \to\ H_d(\omega_0)\,Ae^{j\omega_0 n}$ |
| real sinusoid | — | $A\cos(\omega_0 n+\theta)\ \to\ \lvert H_d(\omega_0)\rvert A\cos(\omega_0 n+\theta+\angle H_d(\omega_0))$, **$h$ real** |
| exists when | the system has a z-transform (some ROC) | the ROC contains $\lvert z\rvert=1$ (stable); impulses if a pole sits on it |

## 7. How this lecture is tested

> [!exam] How Lecture 15 is tested (Midterm 2)
> - **Response to a sum of sinusoids from a given $H_d(\omega)$ or $H(z)$** — on 5 of the 7 past exams, 8–18 points: [[exams/midterm-2/past-exams/fall-2024|FA2024 MT2]] #4 ($|\omega|e^{-j\pi\sin\omega}$, above), [[exams/midterm-2/past-exams/spring-2025|SP2025 MT2]] #4 ($j\omega e^{j\pi\sin\omega}$, with the $\omega=\pi$ slip above), [[exams/midterm-2/past-exams/spring-2023|SP2023 MT2]] #6 ($\omega e^{j\pi\cos\omega}$: complex $h$), [[exams/midterm-2/past-exams/fall-2023|FA2023 MT2]] #4 ($(\frac12+\cos\omega)e^{j|\omega|}$: complex $h$), [[exams/midterm-2/past-exams/fall-2019|FA2019 MT2]] #7 ($1+z^{-4}$). The first question is always whether $h$ is real.
> - **Real or not, and what that implies:** [[exams/midterm-2/past-exams/fall-2024|FA2024 MT2]] #4(a), [[exams/midterm-2/past-exams/fall-2019|FA2019 MT2]] 1(d) (F) and #6 (can $y$ be real?), [[exams/midterm-2/past-exams/fall-2021|FA2021 MT2]] 1(a) (F: a cosine is not an eigenfunction).
> - **$H_d$ versus $H(e^{j\omega})$:** [[exams/midterm-2/past-exams/fall-2021|FA2021 MT2]] #2(c) ($y[n]=y[n-2]+x[n]-x[n-1]$, so $h=(-1)^nu[n]$ and $H_d$ has an impulse at $\pi$).
> - **Computing $H_d$ from $h$ or an LCCDE** (then plotting it, Lecture 16): [[exams/midterm-2/past-exams/fall-2024|FA2024 MT2]] #3, [[exams/midterm-2/past-exams/spring-2023|SP2023 MT2]] #5, [[exams/midterm-2/past-exams/spring-2025|SP2025 MT2]] #3.
> - **Homework:** %%hw6:W1tob21ld29yay9odzZ8SFc2XV0=%%HW6%%/hw6%% #5 (the accumulator: is $H_d=H(e^{j\omega})$?), #6 ($y[n]=x[n]+x[n-10]$ and two sinusoidal inputs), #7 ($H_d=\omega e^{j\sin\omega}$: test the symmetry first%%hw6:IOKAlCAkSF9kKC1cb21lZ2EpPS1IX2ReKihcb21lZ2EpJCwgc28gJGgkIGlzIHB1cmVseSBpbWFnaW5hcnkgYW5kIGV2ZXJ5IHNpbnVzb2lkIG11c3QgYmUgc3BsaXQgaW50byBleHBvbmVudGlhbHM=%%%%/hw6%%).
>
> Recipe, traps and fresh practice: [[problems/lti-response-to-sinusoids|LTI response to sinusoids]].

## Related

- Concepts: [[concepts/frequency-response|frequency response]] · [[concepts/eigenfunctions-of-lti-systems|eigenfunctions of LTI systems]] · [[concepts/dtft-properties|DTFT properties]] (Hermitian symmetry, convolution) · [[concepts/magnitude-and-phase-response|magnitude and phase response]] · [[concepts/transfer-function|transfer function]] · [[concepts/bibo-stability|BIBO stability]] · [[concepts/complex-exponential|complex exponential]]
- Lectures: [[3-fourier-analysis/14-dtft-properties|Lecture 14]] · [[3-fourier-analysis/16-magnitude-and-phase-response|Lecture 16]] · [[2-z-transform/06-the-z-transform|Lecture 6]] (eigenfunctions) · [[3-fourier-analysis/index|Unit 3]]
- Practice: [[problems/lti-response-to-sinusoids|LTI response to sinusoids]] · %%hw6:W1tob21ld29yay9odzZ8SFc2XV0=%%HW6%%/hw6%% · [[demos/frequency-response-explorer|frequency response explorer]]

### Sources for this page

Snyder, ECE 310 Lecture 15 notes ("Frequency response": §1, §1.1 periodic exponentials, §1.2 sinusoids, §1.3 aperiodic inputs, Figure 1) and slides of Oct 2, 2026 (slides 3–11). **There are no annotated slides for Lecture 15**: the answers to slides 6, 10 and 11 are worked out here and each was verified numerically by constructing an actual system (a real FIR filter with the required values of $H_d$, or $h[n]$ from the inverse DTFT) and convolving. HW6 #5–#7 (no official solutions yet). Past exams FA2024 MT2 #3–#4, SP2025 MT2 #3–#4, SP2023 MT2 #5–#6, FA2023 MT2 #4, FA2021 MT2 #1–#2, FA2019 MT2 #1, #6, #7, with their keys. Checks: `verify/LB_l15.py` (54 checks, including the SP2025 #4 partial sums); figures from `verify/LB_figs.py`.
