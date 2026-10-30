---
title: "Frequency response"
description: "H_d(ω), the DTFT of h[n]: equals H(z) on the unit circle for stable systems; e^{jω₀n} in, H_d(ω₀)e^{jω₀n} out; real h turns cosines into scaled, shifted cosines; Y_d = X_dH_d for any input."
tags: [concept, frequency-response, dtft, midterm-2]
aliases: ["frequency response", "sinusoidal response", "response to sinusoids", "steady-state response", "cosine rule"]
---

*Lecture 15 (Fri Oct 2) · [[homework/hw6|HW6]] #5–#7, HW7 #2, #4 ([[exams/quiz-2|Quiz 2 page]]) · family: [[problems/lti-response-to-sinusoids|LTI response to sinusoids]]*

> [!abstract] In one breath
> - Frequency response $H_d(\omega)$ = DTFT of $h[n]$ = $H(z)$ on the unit circle when the system is stable.
> - Any LTI system: $Ae^{j\omega_0 n}\to H_d(\omega_0)\,Ae^{j\omega_0 n}$.
> - Real $h$: $A\cos(\omega_0 n+\theta)\to A|H_d(\omega_0)|\cos(\omega_0 n+\theta+\angle H_d(\omega_0))$. Any input: $Y_d=X_dH_d$.

## 1. Definition

> [!key] Transfer function and frequency response (Lecture 15, eqs. 1–2)
> $$
> \begin{gathered}
> h[n]\ \overset{\mathcal{Z}}{\longleftrightarrow}\ H(z)\ \ \text{(transfer function)}\\
> h[n]\ \overset{\mathcal{F}}{\longleftrightarrow}\ H_d(\omega)=\sum_{n=-\infty}^{\infty}h[n]\,e^{-j\omega n}=|H_d(\omega)|\,e^{j\angle H_d(\omega)}\ \ \text{(frequency response)}
> \end{gathered}
> $$
> - $H_d(\omega)=H(z)\big|_{z=e^{j\omega}}$ when the ROC contains $|z|=1$, i.e. BIBO stable ([[concepts/dtft|DTFT]] §3). Pole on the unit circle: $H_d$ has impulses and differs from $H(e^{j\omega})$ (accumulator: $\frac{1}{1-e^{-j\omega}}+\pi\delta(\omega)$, [[homework/hw6|HW6]] #5); unstable causal: none.
> - Complex at each $\omega$ (slide 4), $2\pi$-periodic: **magnitude response** $|H_d(\omega)|\ge0$, **phase response** $\angle H_d(\omega)$ ([[concepts/magnitude-and-phase-response|magnitude and phase]]).

## 2. Eigenfunctions in frequency

> [!key] Complex exponentials are eigenfunctions (Lecture 15, eqs. 3–8)
> $$
> x[n]=Az^n\ \Longrightarrow\ y[n]=H(z)\,Az^n\qquad(A,\,z\in\mathbb{C})
> $$
> $$
> x[n]=A\,e^{j\omega_0 n}\ \ (\text{all } n)\quad\Longrightarrow\quad y[n]=H_d(\omega_0)\,A\,e^{j\omega_0 n}=|H_d(\omega_0)|\,A\,e^{j\left(\omega_0 n+\angle H_d(\omega_0)\right)} .
> $$
> Same frequency, amplitude scaled by $|H_d(\omega_0)|$, phase shifted by $\angle H_d(\omega_0)$. Any LTI system, real or complex $h$ ([[concepts/eigenfunctions-of-lti-systems|eigenfunctions]]). A one-sided $e^{j\omega_0 n}u[n]$ adds a transient.

> [!question] Slide 6
> $|H_d(\omega)|=|\omega|$ and $\angle H_d(\omega)=-\frac{\omega}{2}$ for $-\pi\le\omega\le\pi$.
> (a) Write $H_d(\omega)$. (b) Find $y[n]$ for $x[n]=2e^{j\frac{\pi}{3}n}+e^{j\left(\frac{\pi}{2}n+\frac{\pi}{4}\right)}$.

> [!success]- Answer
> **(a)** $H_d(\omega)=|\omega|\,e^{-j\omega/2}$ for $-\pi\le\omega\le\pi$, repeated every $2\pi$.
>
> **(b)** $H_d(\frac{\pi}{3})=\frac{\pi}{3}e^{-j\pi/6}$, $H_d(\frac{\pi}{2})=\frac{\pi}{2}e^{-j\pi/4}$. Multiply magnitudes, add phases:
> $$
> y[n]=2\cdot\tfrac{\pi}{3}\,e^{j\left(\frac{\pi}{3}n-\frac{\pi}{6}\right)}+\tfrac{\pi}{2}\,e^{j\left(\frac{\pi}{2}n+\frac{\pi}{4}-\frac{\pi}{4}\right)}=\tfrac{2\pi}{3}\,e^{j\left(\frac{\pi}{3}n-\frac{\pi}{6}\right)}+\tfrac{\pi}{2}\,e^{j\frac{\pi}{2}n}.
> $$

## 3. Sinusoids and the cosine rule

A cosine is two eigenfunctions, at $\pm\omega_0$ (eqs. 9–11, slide 8):

$$
\begin{aligned}
x[n]&=A\cos(\omega_0 n+\theta)=\tfrac{A}{2}e^{j(\omega_0 n+\theta)}+\tfrac{A}{2}e^{-j(\omega_0 n+\theta)}\\
y[n]&=\tfrac{A}{2}H_d(\omega_0)\,e^{j(\omega_0 n+\theta)}+\tfrac{A}{2}H_d(-\omega_0)\,e^{-j(\omega_0 n+\theta)}\\
&=\tfrac{A}{2}|H_d(\omega_0)|\,e^{j(\omega_0 n+\theta+\angle H_d(\omega_0))}+\tfrac{A}{2}|H_d(-\omega_0)|\,e^{-j(\omega_0 n+\theta-\angle H_d(-\omega_0))}.
\end{aligned}
$$

Real $h$ ⇒ Hermitian $H_d$ (eqs. 12–13): $H_d^*(\omega)=H_d(-\omega)$, so $|H_d(\omega)|=|H_d(-\omega)|$ and $\angle H_d(\omega)=-\angle H_d(-\omega)$. The two terms become conjugates and sum to one cosine.

> [!key] Sinusoidal response of a real LTI system (Lecture 15, eq. 15)
> | input (all $n$) | output | needs |
> |---|---|---|
> | $A\,e^{j\omega_0 n}$ | $A\,H_d(\omega_0)\,e^{j\omega_0 n}$ | any LTI |
> | $A\cos(\omega_0 n+\theta)$, same with $\sin$ | $A\lvert H_d(\omega_0)\rvert\cos(\omega_0 n+\theta+\angle H_d(\omega_0))$ | $h$ real |
> | constant $c=c\,e^{j0n}$ | $H_d(0)\,c$ | real $h$: real gain |
> | $(-1)^n=e^{j\pi n}$ | $H_d(\pi)\,(-1)^n$ | real $h$: real gain |
> | $x$ with a DTFT | $Y_d(\omega)=X_d(\omega)H_d(\omega)$ | both exist |
>
> No new frequencies are created. Complex $h$: no shortcut; use the two-term line above with $H_d(\omega_0)$ and $H_d(-\omega_0)$ separately. Test for real $h$: $|H_d|$ even and $\angle H_d$ odd.

Why real $h$ is needed (slide 8 asks): $h[n]=\frac12\big(\delta[n]+j\,\delta[n-1]\big)$ has $H_d(\frac{\pi}{2})=1$ but $H_d(-\frac{\pi}{2})=0$, so $\cos(\frac{\pi}{2}n)\to\frac12\,e^{j\frac{\pi}{2}n}$, a complex output.

> [!recipe] Response to a sum of sinusoids
> 1. Decide whether $h$ is real.
> 2. List each term's frequency in $[-\pi,\pi]$; evaluate $H_d$ there in polar form. Gain $0$ deletes the term.
> 3. Single exponentials: eigenfunction rule. Real sinusoids: cosine rule (real $h$) or split into $e^{\pm j\omega_0 n}$ (complex $h$). Add.

> [!question] Slide 10 (concept check)
> $|H_d(\omega)|=\cos^2\omega$ and $\angle H_d(\omega)=\sin\omega$ for $-\pi\le\omega\le\pi$.
> (a) Is the system real-valued (is $h[n]$ real)? (b) Find $y[n]$ for $x[n]=\sin\!\left(\frac{\pi}{3}n\right)+\cos\!\left(\frac{\pi}{2}n+\frac{3\pi}{10}\right)+(-1)^n$.

> [!success]- Answer
> **(a) Yes.** $\cos^2\omega$ even, $\sin\omega$ odd: $H_d(-\omega)=\cos^2\omega\,e^{-j\sin\omega}=H_d^*(\omega)$.
>
> **(b)**
> - $\omega=\frac{\pi}{3}$: gain $\cos^2\frac{\pi}{3}=\frac14$, phase $\sin\frac{\pi}{3}=\frac{\sqrt3}{2}$ rad.
> - $\omega=\frac{\pi}{2}$: gain $\cos^2\frac{\pi}{2}=0$: cosine removed.
> - $\omega=\pi$: $H_d(\pi)=\cos^2\pi\,e^{j\sin\pi}=1$.
> $$
> y[n]=\tfrac14\sin\!\left(\tfrac{\pi}{3}n+\tfrac{\sqrt3}{2}\right)+(-1)^n .
> $$
>
> <figure class="ece-fig"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 640 250" width="640" height="250" role="img" aria-label="cos squared omega and sin omega with markers at pi/3, pi/2 and pi" style="font-family:'Source Sans 3','Source Sans Pro',system-ui,sans-serif;font-size:13px"><text x="169.0" y="24.0" text-anchor="middle" fill="currentColor" style="font-size:13px;font-weight:600">|H<tspan baseline-shift="sub" style="font-size:75%">d</tspan>(ω)| = cos²ω</text><line x1="34.0" y1="170.9" x2="304.0" y2="170.9" stroke="var(--muted)" stroke-width="0.6" stroke-dasharray="3 3" opacity="0.6"/><line x1="34.0" y1="131.7" x2="304.0" y2="131.7" stroke="var(--muted)" stroke-width="0.6" stroke-dasharray="3 3" opacity="0.6"/><line x1="34.0" y1="53.5" x2="304.0" y2="53.5" stroke="var(--muted)" stroke-width="0.6" stroke-dasharray="3 3" opacity="0.6"/><line x1="34.0" y1="210.0" x2="304.0" y2="210.0" stroke="currentColor" stroke-width="1" opacity="0.75"/><line x1="169.0" y1="30.0" x2="169.0" y2="210.0" stroke="currentColor" stroke-width="1" opacity="0.75"/><line x1="34.0" y1="207.0" x2="34.0" y2="213.0" stroke="currentColor" stroke-width="1"/><text x="34.0" y="224.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">−π</text><line x1="101.5" y1="207.0" x2="101.5" y2="213.0" stroke="currentColor" stroke-width="1"/><text x="101.5" y="224.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">−π/2</text><line x1="169.0" y1="207.0" x2="169.0" y2="213.0" stroke="currentColor" stroke-width="1"/><text x="169.0" y="224.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">0</text><line x1="236.5" y1="207.0" x2="236.5" y2="213.0" stroke="currentColor" stroke-width="1"/><text x="236.5" y="224.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">π/2</text><line x1="304.0" y1="207.0" x2="304.0" y2="213.0" stroke="currentColor" stroke-width="1"/><text x="304.0" y="224.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">π</text><line x1="166.0" y1="170.9" x2="172.0" y2="170.9" stroke="currentColor" stroke-width="1"/><text x="30.0" y="174.9" text-anchor="end" fill="var(--muted)" style="font-size:11px">¼</text><line x1="166.0" y1="131.7" x2="172.0" y2="131.7" stroke="currentColor" stroke-width="1"/><text x="30.0" y="135.7" text-anchor="end" fill="var(--muted)" style="font-size:11px">½</text><line x1="166.0" y1="53.5" x2="172.0" y2="53.5" stroke="currentColor" stroke-width="1"/><text x="30.0" y="57.5" text-anchor="end" fill="var(--muted)" style="font-size:11px">1</text><text x="304.0" y="204.0" text-anchor="end" fill="var(--muted)" style="font-size:12px">ω</text><polyline points="34.0,53.5 37.4,54.4 39.1,55.6 41.8,58.5 45.5,64.4 49.2,72.2 52.6,80.9 57.0,94.0 74.8,157.1 82.9,182.6 88.3,195.8 92.7,203.6 97.1,208.4 100.8,210.0 104.2,209.4 105.9,208.4 108.6,205.8 112.0,200.9 116.4,192.0 120.1,182.6 125.5,166.2 142.3,106.4 147.7,88.8 151.4,78.2 155.8,67.7 160.2,59.9 163.9,55.6 165.6,54.4 168.3,53.5 170.3,53.6 172.4,54.4 174.1,55.6 176.8,58.5 179.5,62.6 182.2,67.7 186.6,78.2 194.7,102.9 212.5,166.2 217.9,182.6 223.3,195.8 227.7,203.6 232.1,208.4 235.8,210.0 238.2,209.8 240.9,208.4 245.3,203.6 248.0,199.1 251.4,192.0 255.1,182.6 263.2,157.1 280.0,97.3 285.4,80.9 289.1,71.4 292.5,64.4 296.2,58.5 298.9,55.6 300.6,54.4 302.6,53.6 304.0,53.5" fill="none" stroke="var(--accent)" stroke-width="1.8" stroke-linejoin="round" stroke-linecap="round" opacity="1.0"/><text x="498.0" y="24.0" text-anchor="middle" fill="currentColor" style="font-size:13px;font-weight:600">∠H<tspan baseline-shift="sub" style="font-size:75%">d</tspan>(ω) = sin ω  (radians)</text><line x1="366.0" y1="198.3" x2="630.0" y2="198.3" stroke="var(--muted)" stroke-width="0.6" stroke-dasharray="3 3" opacity="0.6"/><line x1="366.0" y1="41.7" x2="630.0" y2="41.7" stroke="var(--muted)" stroke-width="0.6" stroke-dasharray="3 3" opacity="0.6"/><line x1="366.0" y1="120.0" x2="630.0" y2="120.0" stroke="currentColor" stroke-width="1" opacity="0.75"/><line x1="498.0" y1="30.0" x2="498.0" y2="210.0" stroke="currentColor" stroke-width="1" opacity="0.75"/><line x1="366.0" y1="117.0" x2="366.0" y2="123.0" stroke="currentColor" stroke-width="1"/><text x="366.0" y="224.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">−π</text><line x1="432.0" y1="117.0" x2="432.0" y2="123.0" stroke="currentColor" stroke-width="1"/><text x="432.0" y="224.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">−π/2</text><line x1="498.0" y1="117.0" x2="498.0" y2="123.0" stroke="currentColor" stroke-width="1"/><text x="498.0" y="224.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">0</text><line x1="564.0" y1="117.0" x2="564.0" y2="123.0" stroke="currentColor" stroke-width="1"/><text x="564.0" y="224.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">π/2</text><line x1="630.0" y1="117.0" x2="630.0" y2="123.0" stroke="currentColor" stroke-width="1"/><text x="630.0" y="224.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">π</text><line x1="495.0" y1="198.3" x2="501.0" y2="198.3" stroke="currentColor" stroke-width="1"/><text x="362.0" y="202.3" text-anchor="end" fill="var(--muted)" style="font-size:11px">−1</text><line x1="495.0" y1="41.7" x2="501.0" y2="41.7" stroke="currentColor" stroke-width="1"/><text x="362.0" y="45.7" text-anchor="end" fill="var(--muted)" style="font-size:11px">1</text><polyline points="366.0,120.0 377.2,140.7 386.1,156.1 395.0,169.9 403.9,181.5 411.5,189.2 417.1,193.4 423.8,196.8 427.7,197.9 431.3,198.3 435.0,198.1 439.3,197.1 443.9,195.2 446.9,193.4 452.5,189.2 455.8,186.1 463.4,177.5 470.0,168.5 479.9,152.8 489.8,135.3 511.5,95.2 518.1,83.9 526.0,71.5 533.6,61.3 542.5,51.7 548.8,46.8 552.1,44.8 555.8,43.2 559.7,42.1 563.3,41.7 568.3,42.1 572.2,43.2 575.9,44.8 580.8,47.9 584.5,50.8 588.8,54.9 597.7,65.5 605.6,77.0 615.2,92.9 630.0,120.0" fill="none" stroke="var(--accent)" stroke-width="1.8" stroke-linejoin="round" stroke-linecap="round" opacity="1.0"/><text x="536.0" y="56.2" text-anchor="end" fill="var(--hi)" style="font-size:11px">√3/2</text><text x="623.0" y="113.0" text-anchor="end" fill="var(--hi)" style="font-size:11px">0</text><text x="220.0" y="166.9" text-anchor="start" fill="var(--hi)" style="font-size:11px">¼</text><text x="242.5" y="204.0" text-anchor="start" fill="var(--hi)" style="font-size:11px">0</text><text x="297.0" y="57.5" text-anchor="end" fill="var(--hi)" style="font-size:11px">1</text><line x1="214.0" y1="30.0" x2="214.0" y2="210.0" stroke="var(--hi)" stroke-width="0.9" stroke-dasharray="2 3"/><line x1="542.0" y1="30.0" x2="542.0" y2="210.0" stroke="var(--hi)" stroke-width="0.9" stroke-dasharray="2 3"/><circle cx="214.0" cy="170.9" r="3.5" fill="var(--hi)" stroke="var(--hi)" stroke-width="1.5"/><circle cx="542.0" cy="52.2" r="3.5" fill="var(--hi)" stroke="var(--hi)" stroke-width="1.5"/><line x1="236.5" y1="30.0" x2="236.5" y2="210.0" stroke="var(--hi)" stroke-width="0.9" stroke-dasharray="2 3"/><line x1="564.0" y1="30.0" x2="564.0" y2="210.0" stroke="var(--hi)" stroke-width="0.9" stroke-dasharray="2 3"/><circle cx="236.5" cy="210.0" r="3.5" fill="var(--hi)" stroke="var(--hi)" stroke-width="1.5"/><circle cx="564.0" cy="41.7" r="3.5" fill="var(--hi)" stroke="var(--hi)" stroke-width="1.5"/><line x1="304.0" y1="30.0" x2="304.0" y2="210.0" stroke="var(--hi)" stroke-width="0.9" stroke-dasharray="2 3"/><line x1="630.0" y1="30.0" x2="630.0" y2="210.0" stroke="var(--hi)" stroke-width="0.9" stroke-dasharray="2 3"/><circle cx="304.0" cy="53.5" r="3.5" fill="var(--hi)" stroke="var(--hi)" stroke-width="1.5"/><circle cx="630.0" cy="120.0" r="3.5" fill="var(--hi)" stroke="var(--hi)" stroke-width="1.5"/><circle cx="124.0" cy="170.9" r="3.5" fill="none" stroke="var(--muted)" stroke-width="1.5"/><circle cx="454.0" cy="187.8" r="3.5" fill="none" stroke="var(--muted)" stroke-width="1.5"/><circle cx="101.5" cy="210.0" r="3.5" fill="none" stroke="var(--muted)" stroke-width="1.5"/><circle cx="432.0" cy="198.3" r="3.5" fill="none" stroke="var(--muted)" stroke-width="1.5"/></svg><figcaption><strong>Slide 10 read off the plots:</strong> red dots mark the input frequencies π/3 (gain ¼, phase √3/2 rad), π/2 (gain 0) and π (gain 1, phase 0). Hollow dots are their mirror images at −π/3 and −π/2 (same magnitude, opposite phase).</figcaption></figure>

> [!question] Slide 11: one input–output pair, then a new input
> A real LTI system maps $x[n]=5+\cos\!\left(\frac{\pi}{4}n-\frac{\pi}{3}\right)+\sin\!\left(-\frac{2\pi}{3}n\right)$ to $y[n]=-10+\cos\!\left(-\frac{2\pi}{3}n\right)$. Find its response to $v[n]=-1+\sin\!\left(-\frac{\pi}{4}n\right)+2\cos\!\left(\frac{2\pi}{3}n\right)$.

> [!success]- Answer
> Read $H_d$ off at the frequencies in $x$:
> - $\omega=0$: $5\to-10$, so $H_d(0)=-2$.
> - $\omega=\frac{\pi}{4}$: no output term, so $H_d(\frac{\pi}{4})=0$.
> - $\omega=\frac{2\pi}{3}$: $-\sin(\frac{2\pi}{3}n)\to\cos(\frac{2\pi}{3}n)$. With $\theta=\frac{2\pi}{3}n$, $-\sin(\theta-\frac{\pi}{2})=\cos\theta$, so $|H_d(\frac{2\pi}{3})|=1$, $\angle H_d(\frac{2\pi}{3})=-\frac{\pi}{2}$.
>
> $v[n]$ uses only these frequencies:
> $$
> \begin{gathered}
> -1\to(-2)(-1)=2,\qquad \sin\!\left(-\tfrac{\pi}{4}n\right)\to0,\\
> 2\cos\!\left(\tfrac{2\pi}{3}n\right)\to2\cos\!\left(\tfrac{2\pi}{3}n-\tfrac{\pi}{2}\right)=2\sin\!\left(\tfrac{2\pi}{3}n\right),
> \end{gathered}
> $$
> $$
> \text{response to } v:\quad 2+2\sin\!\left(\tfrac{2\pi}{3}n\right).
> $$

## 4. Aperiodic inputs and the summary

> [!key] Convolution property (Lecture 15, eq. 16)
> $$
> y[n]=x[n]*h[n]\quad\Longleftrightarrow\quad Y_d(\omega)=X_d(\omega)\,H_d(\omega)
> $$
> Multiply the DTFTs (when both exist), then invert. Two uses: the response to any signal with a DTFT; the design of systems that pass or stop chosen bands (filters).

> [!derivation]- Eq. 6 again from eq. 16 (eqs. 17–22)
> $X_d(\omega)=2\pi A\,\delta(\omega-\omega_0)$, so $Y_d(\omega)=2\pi A\,H_d(\omega_0)\,\delta(\omega-\omega_0)$ and
> $$
> y[n]=\frac{1}{2\pi}\int_{-\pi}^{\pi}2\pi A\,H_d(\omega_0)\,\delta(\omega-\omega_0)\,e^{j\omega n}\,d\omega=H_d(\omega_0)\,A\,e^{j\omega_0 n}.
> $$

| | z-domain: transfer function $H(z)$ | frequency domain: frequency response $H_d(\omega)$ |
|---|---|---|
| any input | $X(z)\ \to\ X(z)H(z)$ | $X_d(\omega)\ \to\ X_d(\omega)H_d(\omega)$ |
| eigenfunction | $Az^n\ \to\ H(z)\,Az^n$ ($z$ in the ROC of $H$) | $Ae^{j\omega_0 n}\ \to\ H_d(\omega_0)\,Ae^{j\omega_0 n}$ |
| real sinusoid | — | $A\cos(\omega_0 n+\theta)\ \to\ \lvert H_d(\omega_0)\rvert A\cos(\omega_0 n+\theta+\angle H_d(\omega_0))$, $h$ real |

Notes Figure 1. **Zeros notch, poles peak:** $1+z^{-4}$ removes $\frac{\pi}{4}$ and $\frac{3\pi}{4}$; $\frac{1}{1-0.9z^{-1}}$ has gain $10$ at $\omega=0$.

| system | $H_d(\omega)$ | where |
|---|---|---|
| $h=\delta[n+2]+\delta[n]+\delta[n-2]$ | $1+2\cos(2\omega)$ | [[exams/midterm-2/past-exams/fall-2024\|FA2024 MT2]] #3 |
| $h=\delta[n]+\delta[n-6]$ | $2\cos(3\omega)\,e^{-j3\omega}$ | [[exams/midterm-2/past-exams/spring-2023\|SP2023 MT2]] #5 |
| $y[n]=x[n]+2x[n-3]+x[n-6]$ | $\left(2+2\cos3\omega\right)e^{-j3\omega}$ | [[exams/midterm-2/past-exams/spring-2025\|SP2025 MT2]] #3 |
| $y[n]=x[n]+x[n-10]$ | $2\cos(5\omega)\,e^{-j5\omega}$ | [[homework/hw6\|HW6]] #6 |

## 5. Midterm 2 quick check

> [!question] Q1 · Sines through a first difference
> $y[n]=x[n]-x[n-1]$. Find $y[n]$ for $x[n]=5+4\sin(\frac{\pi}{3}n-\frac{\pi}{4})+2\cos(\pi n)$, all $n$.

> [!success]- Answer
> $H_d(\omega)=1-e^{-j\omega}=e^{-j\omega/2}\,2j\sin\frac{\omega}{2}=2\sin\frac{\omega}{2}\,e^{j(\frac{\pi}{2}-\frac{\omega}{2})}$; $h$ real.
> - $\omega=0$: $H_d(0)=0$; the $5$ disappears.
> - $\omega=\frac{\pi}{3}$: gain $2\sin\frac{\pi}{6}=1$, phase $\frac{\pi}{2}-\frac{\pi}{6}=\frac{\pi}{3}$; the sine stays a sine: $4\sin(\frac{\pi}{3}n-\frac{\pi}{4}+\frac{\pi}{3})$.
> - $\omega=\pi$: $H_d(\pi)=2$, so $2\cos(\pi n)\to4(-1)^n$.
>
> $y[n]=4\sin(\frac{\pi}{3}n+\frac{\pi}{12})+4(-1)^n$.

> [!question] Q2 · True or False
> (a) For real $h$, $A\sin(\omega_0n)\to A|H_d(\omega_0)|\sin(\omega_0n+\angle H_d(\omega_0))$. (b) In Q1's system, $x[n]=\cos(\frac{\pi}{3}n)u[n]$ gives $y[n]=\cos(\frac{\pi}{3}n+\frac{\pi}{3})$ for all $n\ge0$.

> [!success]- Answer
> (a) **True.** Eq. 15 holds for sine as for cosine.
> (b) **False.** The rule needs the input for all $n$. $y[0]=x[0]-x[-1]=1$, not $\cos\frac{\pi}{3}=\frac12$; from $n=1$ on, $y[n]=\cos(\frac{\pi}{3}n+\frac{\pi}{3})$: a one-sample transient.

> [!trap]
> - $\cos(\omega_0 n)$ is not an eigenfunction; only $e^{j\omega_0 n}$ is ([[exams/midterm-2/past-exams/fall-2021|FA2021 MT2]] 1(a)).
> - Cosine rule ⇔ Hermitian $H_d$ ⇔ real $h$; check $H_d(-\omega)=H_d^*(\omega)$ first ([[exams/midterm-2/past-exams/spring-2023|SP2023 MT2]] #6, [[exams/midterm-2/past-exams/fall-2023|FA2023 MT2]] #4 have complex $h$).
> - Phase is in radians: $\angle H_d=\sin\omega$ at $\frac{\pi}{3}$ is $\frac{\sqrt3}{2}$ rad, not $\frac{\sqrt3}{2}\pi$.
> - $j^n=e^{j\pi n/2}$ is one exponential, with no partner at $-\frac{\pi}{2}$.
> - Magnitude never negative: $H_d(\frac{\pi}{2})=-1$ is gain $1$, phase $\pi$.
> - Real $h$ ⇒ $H_d(\pm\pi)$ real; a formula giving different values at $\pm\pi$ jumps there ([[exams/midterm-2/past-exams/spring-2025|SP2025 MT2]] #4).

> [!exam] Exam
> Fall 2026 MT2 (Wed Nov 4) covers this topic. Sinusoid response from a given $H_d$ or $H(z)$: 5 of 7 past exams, 8–18 points. First decide whether $h$ is real. Family: [[problems/lti-response-to-sinusoids|LTI response to sinusoids]].
> - [[exams/midterm-2/past-exams/fall-2024|FA2024 MT2]] #3, #4 · [[exams/midterm-2/past-exams/spring-2025|SP2025 MT2]] #3, #4 · [[exams/midterm-2/past-exams/spring-2023|SP2023 MT2]] #5, #6 · [[exams/midterm-2/past-exams/fall-2023|FA2023 MT2]] #4 · [[exams/midterm-2/past-exams/fall-2021|FA2021 MT2]] #1(a), #2(c) · [[exams/midterm-2/past-exams/fall-2019|FA2019 MT2]] #1(d), #6, #7 · [[homework/hw6|HW6]] #5–#7 · HW7 #2, #4 ([[exams/quiz-2|Quiz 2 page]])

**Where it appears:** [[3-fourier-analysis/15-frequency-response|L15]] (slides 4–11), [[3-fourier-analysis/16-magnitude-and-phase-response|L16]]; [[problems/lti-response-to-sinusoids|LTI response to sinusoids]]; [[homework/hw6|HW6]] #5–#7; HW7 #2, #4 on [[exams/quiz-2|Quiz 2]]; [[demos/frequency-response-explorer|frequency response explorer]].

## Related
[[concepts/eigenfunctions-of-lti-systems|eigenfunctions]] · [[concepts/transfer-function|transfer function]] · [[concepts/dtft|DTFT]] · [[concepts/dtft-properties|DTFT properties]] · [[concepts/magnitude-and-phase-response|magnitude and phase response]] · [[concepts/group-delay|group delay]] · [[concepts/bibo-stability|BIBO stability]] · [[concepts/periodic-signals|periodic signals]]

### Sources for this page
Lecture 15 notes §1–1.3 (eqs. 1–22, Figure 1), slides 4–11 (unannotated; answers worked here); Lecture 14 §1; HW6 #5–#7, HW7 #2; Midterm 2 keys cited.
