---
title: "Lecture 14 — DTFT properties"
description: "The DTFT as the z-transform on the unit circle (ROC must contain |z| = 1); impulse DTFTs of periodic signals; common pairs; Hermitian symmetry, 2π-periodicity, modulation, Parseval, convolution, windowing; the n·x[n] sign erratum."
tags: [lecture, midterm-2, dtft]
lecture: 14
---

*Lecture 14 · Fri Sep 25, 2026 · notes + slides "Discrete-time Fourier transform properties" · prev: [[3-fourier-analysis/13-fourier-analysis-and-the-dtft|Lecture 13]] · next: [[3-fourier-analysis/15-frequency-response|Lecture 15]]*

> [!abstract] In one breath
> - $X_d(\omega)=X(z)\big|_{z=e^{j\omega}}$ when the ROC contains $|z|=1$. Periodic signals get Dirac impulses: $e^{j\omega_0n}\leftrightarrow2\pi\delta(\omega-\omega_0)$.
> - Real $x[n]$ $\iff$ Hermitian $X_d$: even magnitude, odd phase. Every DTFT is $2\pi$-periodic.
> - Properties: the z-transform's with $z=e^{j\omega}$, plus modulation, windowing and Parseval.

## 1. DTFT and the z-transform

- z-transform: how much of each $z^n$, $z\in\mathbb{C}$, is in a signal ([[2-z-transform/06-the-z-transform|Lecture 6]]). DTFT: how much of each $e^{j\omega n}$.
- Signals that are both: $z^n$ with $z=e^{j\omega}$, the unit circle.

> [!key] The DTFT is the z-transform on the unit circle (notes eqs. 1–2)
> $$
> X(z)\Big|_{z=e^{j\omega}}=\sum_{n=-\infty}^{\infty}x[n]\,e^{-j\omega n}=X_d(\omega)\qquad\text{if the ROC of } X(z) \text{ contains } |z|=1 .
> $$
> Hence the textbook's $X(e^{j\omega})$.

- Why keep the z-transform: it covers every $z$. $x[n]=2^nu[n]$ has $X(z)=\frac{1}{1-2z^{-1}}$, $|z|>2$, but $\sum_n|x[n]|=\infty$: no DTFT (notes eqs. 3–5).
- Stability ([[2-z-transform/11-bibo-stability-and-causality|Lecture 11]]): BIBO stable $\iff\sum_n|h[n]|<\infty\iff$ ROC of $H(z)$ contains $|z|=1\iff$ the DTFT sum of $h$ converges absolutely (notes eq. 6).
- *Absolutely* matters: the ideal low-pass $h[n]=\frac{\sin(Wn)}{\pi n}$ has a DTFT (a rectangle, §2) but is not stable.

### 1.1 Linear algebra intuition (optional)

$X_d(\omega)=\mathbf{v}^*\mathbf{u}$ with $\mathbf{u}=x[n]$, $\mathbf{v}=e^{j\omega n}$: how similar $x$ is to frequency $\omega$ (notes eqs. 10–12).

> [!question] Slide 4: compute the DTFT
> (a) $x[n]=\{1,\underset{\uparrow}{0},0,-1\}$ $\qquad$ (b) $x[n]=a^n u[n]$, $a\in\mathbb{C}$, $|a|\lt1$ $\qquad$ (c) $x[n]=\{\underset{\uparrow}{1},2,3\}$

> [!success]- Answers
> **(a)** $x[-1]=1$, $x[2]=-1$; factor out the midpoint $n=\tfrac12$:
> $$
> X_d(\omega)=e^{j\omega}-e^{-j2\omega}=e^{-j\omega/2}\left(e^{j3\omega/2}-e^{-j3\omega/2}\right)=2j\,e^{-j\omega/2}\sin\!\left(\tfrac{3}{2}\omega\right).
> $$
> **(b)** Geometric series, $|ae^{-j\omega}|=|a|\lt1$:
> $$
> X_d(\omega)=\sum_{n=0}^{\infty}\left(ae^{-j\omega}\right)^n=\frac{1}{1-ae^{-j\omega}} ,
> $$
> the same as $X(z)=\frac{1}{1-az^{-1}}$ (ROC $|z|>|a|$ contains the unit circle) at $z=e^{j\omega}$.
>
> **(c)** $X_d(\omega)=1+2e^{-j\omega}+3e^{-j2\omega}$.

> [!question] Slide 6: do these DTFTs exist?
> $$
> X_1(z)=\frac{1-z^{-1}}{1-\frac12 z^{-1}},\ |z|>\tfrac12 \qquad\qquad X_2(z)=\frac{1+z^{-1}}{1-2z^{-1}-3z^{-2}},\ |z|>2
> $$
> For each: (a) does not exist; (b) replace $z^{-1}$ by $e^{-j\omega}$; (c) replace $z^{-1}$ by $j\omega$.

> [!success]- Answer: $X_1$ (b), $X_2$ (a)
> $X_1$: ROC contains the unit circle, $X_1(\omega)=\dfrac{1-e^{-j\omega}}{1-\frac12 e^{-j\omega}}$.
>
> $X_2$: $1-2z^{-1}-3z^{-2}=(1-3z^{-1})(1+z^{-1})$; the zero at $-1$ cancels the pole at $-1$, leaving $\frac{1}{1-3z^{-1}}$: right-sided $3^nu[n]$, ROC $|z|>3$, no DTFT. (The slide's "$|z|>2$" contains the pole $z=3$, so it cannot be an ROC; the unit circle is outside either way.)
>
> (c) is never right: $s=j\Omega$ is the Laplace habit.

## 2. DTFT of periodic signals

- Periodic signals are not absolutely summable. Exception made: impulses.
- $e^{j\omega_0n}$ holds one frequency, so $X_d(\omega)\neq0$ only at $\omega=\omega_0+2\pi k$ (notes eq. 13).
- **Dirac delta** $\delta(\omega)$: zero except at $0$, unit area, sifting $\int f(\omega)\,\delta(\omega-a)\,d\omega=f(a)$. Parentheses, continuous argument: not the Kronecker $\delta[n]$.

> [!key] Impulse pairs (notes eqs. 16–22; every one repeats at $\omega+2\pi k$)
> Guess $X_d(\omega)=c\,\delta(\omega-\omega_0)$ and invert:
> $$
> \frac{1}{2\pi}\int_{-\pi}^{\pi}c\,\delta(\omega-\omega_0)\,e^{j\omega n}\,d\omega=\frac{c}{2\pi}\,e^{j\omega_0 n}\stackrel{!}{=}e^{j\omega_0 n}\quad\Longrightarrow\quad c=2\pi .
> $$
> $$
> \begin{aligned}
> e^{j\omega_0 n}&\ \longleftrightarrow\ 2\pi\,\delta(\omega-\omega_0)\\
> \cos(\omega_0 n)&\ \longleftrightarrow\ \pi\left[\delta(\omega-\omega_0)+\delta(\omega+\omega_0)\right]\\
> \sin(\omega_0 n)&\ \longleftrightarrow\ -j\pi\left[\delta(\omega-\omega_0)-\delta(\omega+\omega_0)\right]
> \end{aligned}
> $$
> Cosine and sine: Euler on the first pair.

<figure class="ece-fig"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 640 215" width="640" height="215" role="img" aria-label="Impulses of area pi at plus and minus pi/3 and at their 2 pi periodic copies" style="font-family:'Source Sans 3','Source Sans Pro',system-ui,sans-serif;font-size:13px"><text x="322.0" y="24.0" text-anchor="middle" fill="currentColor" style="font-size:13px;font-weight:600">X<tspan baseline-shift="sub" style="font-size:75%">d</tspan>(ω) for x[n] = cos(πn/3)</text><rect x="222.7" y="30.0" width="198.7" height="140.0" fill="var(--accent)" fill-opacity="0.1" stroke="none"/><line x1="24.0" y1="170.0" x2="620.0" y2="170.0" stroke="currentColor" stroke-width="1" opacity="0.75"/><line x1="322.0" y1="30.0" x2="322.0" y2="170.0" stroke="currentColor" stroke-width="1" opacity="0.75"/><line x1="24.0" y1="167.0" x2="24.0" y2="173.0" stroke="currentColor" stroke-width="1"/><text x="24.0" y="184.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">−3π</text><line x1="123.3" y1="167.0" x2="123.3" y2="173.0" stroke="currentColor" stroke-width="1"/><text x="123.3" y="184.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">−2π</text><line x1="222.7" y1="167.0" x2="222.7" y2="173.0" stroke="currentColor" stroke-width="1"/><text x="222.7" y="184.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">−π</text><line x1="288.9" y1="167.0" x2="288.9" y2="173.0" stroke="currentColor" stroke-width="1"/><text x="288.9" y="184.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">−π/3</text><line x1="355.1" y1="167.0" x2="355.1" y2="173.0" stroke="currentColor" stroke-width="1"/><text x="355.1" y="184.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">π/3</text><line x1="421.3" y1="167.0" x2="421.3" y2="173.0" stroke="currentColor" stroke-width="1"/><text x="421.3" y="184.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">π</text><line x1="520.7" y1="167.0" x2="520.7" y2="173.0" stroke="currentColor" stroke-width="1"/><text x="520.7" y="184.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">2π</text><line x1="620.0" y1="167.0" x2="620.0" y2="173.0" stroke="currentColor" stroke-width="1"/><text x="620.0" y="184.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">3π</text><text x="620.0" y="164.0" text-anchor="end" fill="var(--muted)" style="font-size:12px">ω</text><line x1="90.2" y1="170.0" x2="90.2" y2="73.7" stroke="var(--muted)" stroke-width="2"/><path d="M85.2,75.7 L90.2,67.7 L95.2,75.7 Z" fill="var(--muted)"/><text x="96.2" y="71.7" text-anchor="start" fill="var(--muted)" style="font-size:11px">π</text><line x1="156.4" y1="170.0" x2="156.4" y2="73.7" stroke="var(--muted)" stroke-width="2"/><path d="M151.4,75.7 L156.4,67.7 L161.4,75.7 Z" fill="var(--muted)"/><text x="162.4" y="71.7" text-anchor="start" fill="var(--muted)" style="font-size:11px">π</text><line x1="288.9" y1="170.0" x2="288.9" y2="73.7" stroke="var(--accent)" stroke-width="2"/><path d="M283.9,75.7 L288.9,67.7 L293.9,75.7 Z" fill="var(--accent)"/><text x="294.9" y="71.7" text-anchor="start" fill="var(--accent)" style="font-size:11px">π</text><line x1="355.1" y1="170.0" x2="355.1" y2="73.7" stroke="var(--accent)" stroke-width="2"/><path d="M350.1,75.7 L355.1,67.7 L360.1,75.7 Z" fill="var(--accent)"/><text x="361.1" y="71.7" text-anchor="start" fill="var(--accent)" style="font-size:11px">π</text><line x1="487.6" y1="170.0" x2="487.6" y2="73.7" stroke="var(--muted)" stroke-width="2"/><path d="M482.6,75.7 L487.6,67.7 L492.6,75.7 Z" fill="var(--muted)"/><text x="493.6" y="71.7" text-anchor="start" fill="var(--muted)" style="font-size:11px">π</text><line x1="553.8" y1="170.0" x2="553.8" y2="73.7" stroke="var(--muted)" stroke-width="2"/><path d="M548.8,75.7 L553.8,67.7 L558.8,75.7 Z" fill="var(--muted)"/><text x="559.8" y="71.7" text-anchor="start" fill="var(--muted)" style="font-size:11px">π</text><text x="226.5" y="41.4" text-anchor="start" fill="var(--accent)" style="font-size:11px">one period</text><text x="226.5" y="52.8" text-anchor="start" fill="var(--accent)" style="font-size:11px">−π ≤ ω ≤ π</text><text x="123.3" y="41.4" text-anchor="middle" fill="var(--muted)" style="font-size:11px">copy (k = −1)</text><text x="520.7" y="41.4" text-anchor="middle" fill="var(--muted)" style="font-size:11px">copy (k = 1)</text></svg><figcaption><strong>cos(πn/3) ⟷ impulses of area π at ±π/3 on the shaded period, repeated every 2π (grey).</strong> An arrow's height marks the impulse's area, not a function value.</figcaption></figure>

> [!key] Table 1: common DTFT pairs, with the conditions under which each holds
> | $x[n]$ | $X_d(\omega)$ on $-\pi\le\omega\le\pi$ | holds when |
> |---|---|---|
> | $\delta[n]$ | $1$ | always |
> | $u[n]$ | $\dfrac{1}{1-e^{-j\omega}}+\pi\delta(\omega)$ | (pole on $\lvert z\rvert=1$: impulse) |
> | $a^n u[n]$ | $\dfrac{1}{1-ae^{-j\omega}}$ | $\lvert a\rvert\lt1$; none for $\lvert a\rvert>1$ |
> | $e^{j\omega_0 n}$ | $2\pi\delta(\omega-\omega_0)$ | (periodic: impulse) |
> | $\cos(\omega_0 n)$ | $\pi\left[\delta(\omega-\omega_0)+\delta(\omega+\omega_0)\right]$ | (impulses) |
> | $\sin(\omega_0 n)$ | $-j\pi\left[\delta(\omega-\omega_0)-\delta(\omega+\omega_0)\right]$ | (impulses) |
> | $\mathrm{rect}\!\left(\frac{n-k}{L}\right)$ ($L$ ones centred at $k$) | $\dfrac{\sin(L\omega/2)}{\sin(\omega/2)}\,e^{-j\omega k}$ | $L$ odd |
> | $\mathrm{sinc}(Ln)=\dfrac{\sin(Ln)}{Ln}$ | $\dfrac{\pi}{L}\,\mathrm{rect}\!\left(\frac{\omega}{2L}\right)$: $\dfrac{\pi}{L}$ for $\lvert\omega\rvert\lt L$, else $0$ | $0\lt L\lt\pi$ |
> | $\mathrm{sinc}^2(Ln)$ | $\dfrac{\pi}{L}\,\Delta\!\left(\frac{\omega}{2L}\right)=\dfrac{\pi}{L}\left(1-\dfrac{\lvert\omega\rvert}{2L}\right)$ for $\lvert\omega\rvert\le2L$ | $0\lt L\le\pi/2$ |
>
> Notes' definitions (eqs. 23–25): $\mathrm{rect}\!\left(\frac{n-k}{L}\right)=1$ for $k-\frac L2\lt n\le k+\frac L2$; $\Delta\!\left(\frac nL\right)=1-\left|\frac nL\right|$ for $|n|\le L$. Every entry repeats every $2\pi$. The sinc decays like $1/n$: not absolutely summable, converges in energy. $\mathrm{sinc}^2$ is absolutely summable.

- Even $L$: the rect's ones run from $k-\frac L2+1$ to $k+\frac L2$, centred at $k+\frac12$, so the DTFT gains $e^{-j\omega/2}$.
- $\mathrm{sinc}^2$ with $2L>\pi$: the triangle's $2\pi$-periodic copies overlap; the DTFT is their sum.
- Sketched piecewise-constant spectrum: a centred rectangle of height $A$ and half-width $W$ gives $A\,\dfrac{\sin(Wn)}{\pi n}$; a band $\omega_a\le|\omega|\le\omega_b$ is the rectangle of half-width $\omega_b$ minus the one of half-width $\omega_a$.

<figure class="ece-fig"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 680 250" width="680" height="250" role="img" aria-label="rectangular spectrum and its sinc sequence" style="font-family:'Source Sans 3','Source Sans Pro',system-ui,sans-serif;font-size:13px"><text x="175.0" y="28.0" text-anchor="middle" fill="currentColor" style="font-size:13px;font-weight:600">X<tspan baseline-shift="sub" style="font-size:75%">d</tspan>(ω) = 1 for |ω| ≤ π/4 (one period)</text><line x1="40.0" y1="69.2" x2="310.0" y2="69.2" stroke="var(--muted)" stroke-width="0.6" stroke-dasharray="3 3" opacity="0.6"/><line x1="40.0" y1="186.4" x2="310.0" y2="186.4" stroke="currentColor" stroke-width="1" opacity="0.75"/><line x1="175.0" y1="34.0" x2="175.0" y2="204.0" stroke="currentColor" stroke-width="1" opacity="0.75"/><line x1="40.0" y1="183.4" x2="40.0" y2="189.4" stroke="currentColor" stroke-width="1"/><text x="40.0" y="218.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">−π</text><line x1="141.2" y1="183.4" x2="141.2" y2="189.4" stroke="currentColor" stroke-width="1"/><text x="141.2" y="218.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">−π/4</text><line x1="208.8" y1="183.4" x2="208.8" y2="189.4" stroke="currentColor" stroke-width="1"/><text x="208.8" y="218.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">π/4</text><line x1="310.0" y1="183.4" x2="310.0" y2="189.4" stroke="currentColor" stroke-width="1"/><text x="310.0" y="218.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">π</text><line x1="172.0" y1="186.4" x2="178.0" y2="186.4" stroke="currentColor" stroke-width="1"/><text x="36.0" y="190.4" text-anchor="end" fill="var(--muted)" style="font-size:11px">0</text><line x1="172.0" y1="69.2" x2="178.0" y2="69.2" stroke="currentColor" stroke-width="1"/><text x="36.0" y="73.2" text-anchor="end" fill="var(--muted)" style="font-size:11px">1</text><text x="310.0" y="180.4" text-anchor="end" fill="var(--muted)" style="font-size:12px">ω</text><polyline points="40.0,186.4 141.2,186.4 141.2,69.2 208.8,69.2 208.8,186.4 310.0,186.4" fill="none" stroke="var(--accent)" stroke-width="2.2" stroke-linejoin="round" stroke-linecap="round" opacity="1.0"/><text x="515.0" y="28.0" text-anchor="middle" fill="currentColor" style="font-size:13px;font-weight:600">x[n] = sin(πn/4)/(πn)</text><line x1="370.0" y1="55.8" x2="660.0" y2="55.8" stroke="var(--muted)" stroke-width="0.6" stroke-dasharray="3 3" opacity="0.6"/><line x1="370.0" y1="164.8" x2="660.0" y2="164.8" stroke="currentColor" stroke-width="1" opacity="0.75"/><line x1="515.0" y1="34.0" x2="515.0" y2="204.0" stroke="currentColor" stroke-width="1" opacity="0.75"/><line x1="376.9" y1="161.8" x2="376.9" y2="167.8" stroke="currentColor" stroke-width="1"/><text x="376.9" y="218.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">−16</text><line x1="446.0" y1="161.8" x2="446.0" y2="167.8" stroke="currentColor" stroke-width="1"/><text x="446.0" y="218.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">−8</text><line x1="480.5" y1="161.8" x2="480.5" y2="167.8" stroke="currentColor" stroke-width="1"/><text x="480.5" y="218.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">−4</text><line x1="515.0" y1="161.8" x2="515.0" y2="167.8" stroke="currentColor" stroke-width="1"/><text x="515.0" y="218.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">0</text><line x1="549.5" y1="161.8" x2="549.5" y2="167.8" stroke="currentColor" stroke-width="1"/><text x="549.5" y="218.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">4</text><line x1="584.0" y1="161.8" x2="584.0" y2="167.8" stroke="currentColor" stroke-width="1"/><text x="584.0" y="218.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">8</text><line x1="653.1" y1="161.8" x2="653.1" y2="167.8" stroke="currentColor" stroke-width="1"/><text x="653.1" y="218.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">16</text><line x1="512.0" y1="164.8" x2="518.0" y2="164.8" stroke="currentColor" stroke-width="1"/><text x="366.0" y="168.8" text-anchor="end" fill="var(--muted)" style="font-size:11px">0</text><line x1="512.0" y1="55.8" x2="518.0" y2="55.8" stroke="currentColor" stroke-width="1"/><text x="366.0" y="59.8" text-anchor="end" fill="var(--muted)" style="font-size:11px">¼</text><text x="660.0" y="158.8" text-anchor="end" fill="var(--muted)" style="font-size:12px">n</text><line x1="376.9" y1="164.8" x2="376.9" y2="164.8" stroke="var(--accent)" stroke-width="1.6"/><circle cx="376.9" cy="164.8" r="2.4" fill="var(--accent)"/><line x1="385.5" y1="164.8" x2="385.5" y2="171.3" stroke="var(--accent)" stroke-width="1.6"/><circle cx="385.5" cy="171.3" r="2.4" fill="var(--accent)"/><line x1="394.2" y1="164.8" x2="394.2" y2="174.7" stroke="var(--accent)" stroke-width="1.6"/><circle cx="394.2" cy="174.7" r="2.4" fill="var(--accent)"/><line x1="402.8" y1="164.8" x2="402.8" y2="172.3" stroke="var(--accent)" stroke-width="1.6"/><circle cx="402.8" cy="172.3" r="2.4" fill="var(--accent)"/><line x1="411.4" y1="164.8" x2="411.4" y2="164.8" stroke="var(--accent)" stroke-width="1.6"/><circle cx="411.4" cy="164.8" r="2.4" fill="var(--accent)"/><line x1="420.1" y1="164.8" x2="420.1" y2="155.9" stroke="var(--accent)" stroke-width="1.6"/><circle cx="420.1" cy="155.9" r="2.4" fill="var(--accent)"/><line x1="428.7" y1="164.8" x2="428.7" y2="150.9" stroke="var(--accent)" stroke-width="1.6"/><circle cx="428.7" cy="150.9" r="2.4" fill="var(--accent)"/><line x1="437.3" y1="164.8" x2="437.3" y2="153.9" stroke="var(--accent)" stroke-width="1.6"/><circle cx="437.3" cy="153.9" r="2.4" fill="var(--accent)"/><line x1="446.0" y1="164.8" x2="446.0" y2="164.8" stroke="var(--accent)" stroke-width="1.6"/><circle cx="446.0" cy="164.8" r="2.4" fill="var(--accent)"/><line x1="454.6" y1="164.8" x2="454.6" y2="178.8" stroke="var(--accent)" stroke-width="1.6"/><circle cx="454.6" cy="178.8" r="2.4" fill="var(--accent)"/><line x1="463.2" y1="164.8" x2="463.2" y2="187.9" stroke="var(--accent)" stroke-width="1.6"/><circle cx="463.2" cy="187.9" r="2.4" fill="var(--accent)"/><line x1="471.8" y1="164.8" x2="471.8" y2="184.4" stroke="var(--accent)" stroke-width="1.6"/><circle cx="471.8" cy="184.4" r="2.4" fill="var(--accent)"/><line x1="480.5" y1="164.8" x2="480.5" y2="164.8" stroke="var(--accent)" stroke-width="1.6"/><circle cx="480.5" cy="164.8" r="2.4" fill="var(--accent)"/><line x1="489.1" y1="164.8" x2="489.1" y2="132.1" stroke="var(--accent)" stroke-width="1.6"/><circle cx="489.1" cy="132.1" r="2.4" fill="var(--accent)"/><line x1="497.7" y1="164.8" x2="497.7" y2="95.4" stroke="var(--accent)" stroke-width="1.6"/><circle cx="497.7" cy="95.4" r="2.4" fill="var(--accent)"/><line x1="506.4" y1="164.8" x2="506.4" y2="66.7" stroke="var(--accent)" stroke-width="1.6"/><circle cx="506.4" cy="66.7" r="2.4" fill="var(--accent)"/><line x1="515.0" y1="164.8" x2="515.0" y2="55.8" stroke="var(--accent)" stroke-width="1.6"/><circle cx="515.0" cy="55.8" r="2.4" fill="var(--accent)"/><line x1="523.6" y1="164.8" x2="523.6" y2="66.7" stroke="var(--accent)" stroke-width="1.6"/><circle cx="523.6" cy="66.7" r="2.4" fill="var(--accent)"/><line x1="532.3" y1="164.8" x2="532.3" y2="95.4" stroke="var(--accent)" stroke-width="1.6"/><circle cx="532.3" cy="95.4" r="2.4" fill="var(--accent)"/><line x1="540.9" y1="164.8" x2="540.9" y2="132.1" stroke="var(--accent)" stroke-width="1.6"/><circle cx="540.9" cy="132.1" r="2.4" fill="var(--accent)"/><line x1="549.5" y1="164.8" x2="549.5" y2="164.8" stroke="var(--accent)" stroke-width="1.6"/><circle cx="549.5" cy="164.8" r="2.4" fill="var(--accent)"/><line x1="558.2" y1="164.8" x2="558.2" y2="184.4" stroke="var(--accent)" stroke-width="1.6"/><circle cx="558.2" cy="184.4" r="2.4" fill="var(--accent)"/><line x1="566.8" y1="164.8" x2="566.8" y2="187.9" stroke="var(--accent)" stroke-width="1.6"/><circle cx="566.8" cy="187.9" r="2.4" fill="var(--accent)"/><line x1="575.4" y1="164.8" x2="575.4" y2="178.8" stroke="var(--accent)" stroke-width="1.6"/><circle cx="575.4" cy="178.8" r="2.4" fill="var(--accent)"/><line x1="584.0" y1="164.8" x2="584.0" y2="164.8" stroke="var(--accent)" stroke-width="1.6"/><circle cx="584.0" cy="164.8" r="2.4" fill="var(--accent)"/><line x1="592.7" y1="164.8" x2="592.7" y2="153.9" stroke="var(--accent)" stroke-width="1.6"/><circle cx="592.7" cy="153.9" r="2.4" fill="var(--accent)"/><line x1="601.3" y1="164.8" x2="601.3" y2="150.9" stroke="var(--accent)" stroke-width="1.6"/><circle cx="601.3" cy="150.9" r="2.4" fill="var(--accent)"/><line x1="609.9" y1="164.8" x2="609.9" y2="155.9" stroke="var(--accent)" stroke-width="1.6"/><circle cx="609.9" cy="155.9" r="2.4" fill="var(--accent)"/><line x1="618.6" y1="164.8" x2="618.6" y2="164.8" stroke="var(--accent)" stroke-width="1.6"/><circle cx="618.6" cy="164.8" r="2.4" fill="var(--accent)"/><line x1="627.2" y1="164.8" x2="627.2" y2="172.3" stroke="var(--accent)" stroke-width="1.6"/><circle cx="627.2" cy="172.3" r="2.4" fill="var(--accent)"/><line x1="635.8" y1="164.8" x2="635.8" y2="174.7" stroke="var(--accent)" stroke-width="1.6"/><circle cx="635.8" cy="174.7" r="2.4" fill="var(--accent)"/><line x1="644.5" y1="164.8" x2="644.5" y2="171.3" stroke="var(--accent)" stroke-width="1.6"/><circle cx="644.5" cy="171.3" r="2.4" fill="var(--accent)"/><line x1="653.1" y1="164.8" x2="653.1" y2="164.8" stroke="var(--accent)" stroke-width="1.6"/><circle cx="653.1" cy="164.8" r="2.4" fill="var(--accent)"/></svg><figcaption><strong>Rectangle in frequency ⟷ sinc in time.</strong> The inverse DTFT of 1 on |ω| ≤ π/4 is sin(πn/4)/(πn): height ω<sub>c</sub>/π = ¼ at n = 0, zeros at n = ±4, ±8, …, and a 1/n tail, so not absolutely summable, though its energy is finite (¼).</figcaption></figure>

## 3. Properties of the DTFT

Several properties carry over from the z-transform with $z=e^{j\omega}$ (last column).

> [!key] DTFT properties (Table 2 of the notes, sign corrected)
> | property | signal | DTFT | inherited from the z-transform? |
> |---|---|---|---|
> | linearity | $a\,x_1[n]+b\,x_2[n]$ | $aX_1(\omega)+bX_2(\omega)$ | yes |
> | time shift | $x[n-k]$, $k\in\mathbb{Z}$ | $e^{-j\omega k}X_d(\omega)$ | $z^{-k}X(z)$ |
> | frequency shift | $e^{j\omega_0 n}x[n]$ | $X_d(\omega-\omega_0)$ | $a^n x[n]\leftrightarrow X(z/a)$, $a=e^{j\omega_0}$ |
> | modulation | $x[n]\cos(\omega_0 n)$ | $\tfrac12X_d(\omega-\omega_0)+\tfrac12X_d(\omega+\omega_0)$ | Euler + frequency shift |
> | time reversal | $x[-n]$ | $X_d(-\omega)$ | $X(1/z)$ |
> | conjugation | $x^*[n]$ | $X_d^*(-\omega)$ | $X^*(z^*)$ |
> | differentiation | $n\,x[n]$ | $+j\,\dfrac{dX_d(\omega)}{d\omega}$ ⚠ | $-z\,\dfrac{dX}{dz}$ |
> | convolution | $x[n]*h[n]$ | $X_d(\omega)H_d(\omega)$ | $X(z)H(z)$ |
> | windowing | $x[n]\,w[n]$ | $\dfrac{1}{2\pi}\displaystyle\int_{-\pi}^{\pi}X_d(\theta)W_d(\omega-\theta)\,d\theta$ | DTFT only |
> | Hermitian symmetry | $x[n]$ real | $X_d^*(\omega)=X_d(-\omega)$ | — |
> | Parseval | $\sum_n\lvert x[n]\rvert^2$ | $\dfrac{1}{2\pi}\displaystyle\int_{-\pi}^{\pi}\lvert X_d(\omega)\rvert^2d\omega$ | DTFT only |

⚠ **Erratum:** the notes' Table 2 and slide 15 print $n\,x[n]\leftrightarrow-j\,\frac{dX_d}{d\omega}$; differentiating the definition term by term gives $+j\,\frac{dX_d}{d\omega}$ (as in the official transform tables; [[0-toolkit/05-errata|errata]]).

### Hermitian symmetry

> [!key] Real signal $\iff$ Hermitian DTFT (notes eqs. 31–33)
> $$
> \begin{aligned}
> x[n]\ \text{real}\quad&\Longleftrightarrow\quad X_d(-\omega)=X_d^*(\omega)\\
> &\Longleftrightarrow\quad |X_d(-\omega)|=|X_d(\omega)|\ \text{and}\ \angle X_d(-\omega)=-\angle X_d(\omega).
> \end{aligned}
> $$
> Magnitude even, phase odd. "If and only if" (slide 11). For real $x$: $X_d(0)$ and $X_d(\pi)$ are real; real and even $x$ ⇒ $X_d$ real and even; real and odd $x$ ⇒ $X_d$ imaginary and odd.

> [!derivation]- Real and imaginary parts (notes eqs. 26–30)
> With $e^{-j\omega n}=\cos(\omega n)-j\sin(\omega n)$:
> $$
> \begin{aligned}
> \mathrm{Re}\{X_d(\omega)\}&=\sum_n \mathrm{Re}\{x[n]\}\cos(\omega n)+\mathrm{Im}\{x[n]\}\sin(\omega n),\\
> \mathrm{Im}\{X_d(\omega)\}&=\sum_n \mathrm{Im}\{x[n]\}\cos(\omega n)-\mathrm{Re}\{x[n]\}\sin(\omega n).
> \end{aligned}
> $$
> With $\mathrm{Im}\{x[n]\}=0$ the first line is even in $\omega$ and the second odd, so $X_d(-\omega)=X_d^*(\omega)$. (Notes eq. 27's lower limit "$n=\infty$" should read $-\infty$.)

<figure class="ece-fig"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 640 262" width="640" height="262" role="img" aria-label="Magnitude and phase of the DTFT of 0.8^n u[n] and of its frequency-shifted complex version" style="font-family:'Source Sans 3','Source Sans Pro',system-ui,sans-serif;font-size:13px"><text x="174.0" y="24.0" text-anchor="middle" fill="currentColor" style="font-size:13px;font-weight:600">|X<tspan baseline-shift="sub" style="font-size:75%">d</tspan>(ω)|</text><line x1="34.0" y1="186.1" x2="314.0" y2="186.1" stroke="var(--muted)" stroke-width="0.6" stroke-dasharray="3 3" opacity="0.6"/><line x1="34.0" y1="152.1" x2="314.0" y2="152.1" stroke="var(--muted)" stroke-width="0.6" stroke-dasharray="3 3" opacity="0.6"/><line x1="34.0" y1="118.2" x2="314.0" y2="118.2" stroke="var(--muted)" stroke-width="0.6" stroke-dasharray="3 3" opacity="0.6"/><line x1="34.0" y1="84.3" x2="314.0" y2="84.3" stroke="var(--muted)" stroke-width="0.6" stroke-dasharray="3 3" opacity="0.6"/><line x1="34.0" y1="50.4" x2="314.0" y2="50.4" stroke="var(--muted)" stroke-width="0.6" stroke-dasharray="3 3" opacity="0.6"/><line x1="34.0" y1="220.0" x2="314.0" y2="220.0" stroke="currentColor" stroke-width="1" opacity="0.75"/><line x1="174.0" y1="30.0" x2="174.0" y2="220.0" stroke="currentColor" stroke-width="1" opacity="0.75"/><line x1="34.0" y1="217.0" x2="34.0" y2="223.0" stroke="currentColor" stroke-width="1"/><text x="34.0" y="234.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">−π</text><line x1="104.0" y1="217.0" x2="104.0" y2="223.0" stroke="currentColor" stroke-width="1"/><text x="104.0" y="234.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">−π/2</text><line x1="174.0" y1="217.0" x2="174.0" y2="223.0" stroke="currentColor" stroke-width="1"/><text x="174.0" y="234.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">0</text><line x1="244.0" y1="217.0" x2="244.0" y2="223.0" stroke="currentColor" stroke-width="1"/><text x="244.0" y="234.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">π/2</text><line x1="314.0" y1="217.0" x2="314.0" y2="223.0" stroke="currentColor" stroke-width="1"/><text x="314.0" y="234.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">π</text><line x1="171.0" y1="186.1" x2="177.0" y2="186.1" stroke="currentColor" stroke-width="1"/><text x="30.0" y="190.1" text-anchor="end" fill="var(--muted)" style="font-size:11px">1</text><line x1="171.0" y1="152.1" x2="177.0" y2="152.1" stroke="currentColor" stroke-width="1"/><text x="30.0" y="156.1" text-anchor="end" fill="var(--muted)" style="font-size:11px">2</text><line x1="171.0" y1="118.2" x2="177.0" y2="118.2" stroke="currentColor" stroke-width="1"/><text x="30.0" y="122.2" text-anchor="end" fill="var(--muted)" style="font-size:11px">3</text><line x1="171.0" y1="84.3" x2="177.0" y2="84.3" stroke="currentColor" stroke-width="1"/><text x="30.0" y="88.3" text-anchor="end" fill="var(--muted)" style="font-size:11px">4</text><line x1="171.0" y1="50.4" x2="177.0" y2="50.4" stroke="currentColor" stroke-width="1"/><text x="30.0" y="54.4" text-anchor="end" fill="var(--muted)" style="font-size:11px">5</text><text x="314.0" y="214.0" text-anchor="end" fill="var(--muted)" style="font-size:12px">ω</text><polyline points="34.0,199.6 53.1,200.9 78.1,201.1 98.9,200.1 119.9,197.7 132.7,195.2 145.1,191.6 156.3,186.7 165.4,180.8 170.3,176.5 174.5,171.9 180.1,163.9 185.0,154.4 189.9,141.2 193.4,128.5 196.9,112.1 205.7,58.8 207.1,53.3 207.8,51.5 208.8,50.4 209.5,50.5 210.2,51.5 212.3,58.8 220.4,108.4 223.2,122.4 226.7,136.5 230.2,147.4 233.0,154.4 237.2,162.7 241.4,169.2 247.0,175.8 252.6,180.8 260.1,185.8 268.0,189.7 276.2,192.7 286.2,195.4 298.1,197.7 314.0,199.6" fill="none" stroke="var(--accent2)" stroke-width="1.8" stroke-dasharray="5 4" stroke-linejoin="round" stroke-linecap="round" opacity="1.0"/><polyline points="34.0,201.2 52.2,200.8 69.7,199.6 87.9,197.2 101.7,194.2 111.7,191.0 121.3,186.7 130.4,180.8 137.4,174.3 143.0,167.2 147.2,160.2 151.4,151.0 155.6,138.9 159.1,125.5 162.6,108.4 170.7,58.8 172.1,53.3 172.8,51.5 173.8,50.4 174.5,50.5 175.2,51.5 177.3,58.8 185.4,108.4 188.9,125.5 192.4,138.9 196.6,151.0 200.8,160.2 205.0,167.2 210.6,174.3 217.6,180.8 226.7,186.7 236.3,191.0 246.3,194.2 260.1,197.2 278.3,199.6 295.8,200.8 314.0,201.2" fill="none" stroke="var(--accent)" stroke-width="1.8" stroke-linejoin="round" stroke-linecap="round" opacity="1.0"/><line x1="209.0" y1="30.0" x2="209.0" y2="220.0" stroke="var(--accent2)" stroke-width="0.8" stroke-dasharray="2 3"/><text x="500.0" y="24.0" text-anchor="middle" fill="currentColor" style="font-size:13px;font-weight:600">∠X<tspan baseline-shift="sub" style="font-size:75%">d</tspan>(ω)</text><line x1="370.0" y1="220.0" x2="630.0" y2="220.0" stroke="var(--muted)" stroke-width="0.6" stroke-dasharray="3 3" opacity="0.6"/><line x1="370.0" y1="172.5" x2="630.0" y2="172.5" stroke="var(--muted)" stroke-width="0.6" stroke-dasharray="3 3" opacity="0.6"/><line x1="370.0" y1="77.5" x2="630.0" y2="77.5" stroke="var(--muted)" stroke-width="0.6" stroke-dasharray="3 3" opacity="0.6"/><line x1="370.0" y1="30.0" x2="630.0" y2="30.0" stroke="var(--muted)" stroke-width="0.6" stroke-dasharray="3 3" opacity="0.6"/><line x1="370.0" y1="125.0" x2="630.0" y2="125.0" stroke="currentColor" stroke-width="1" opacity="0.75"/><line x1="500.0" y1="30.0" x2="500.0" y2="220.0" stroke="currentColor" stroke-width="1" opacity="0.75"/><line x1="370.0" y1="122.0" x2="370.0" y2="128.0" stroke="currentColor" stroke-width="1"/><text x="370.0" y="234.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">−π</text><line x1="435.0" y1="122.0" x2="435.0" y2="128.0" stroke="currentColor" stroke-width="1"/><text x="435.0" y="234.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">−π/2</text><line x1="500.0" y1="122.0" x2="500.0" y2="128.0" stroke="currentColor" stroke-width="1"/><text x="500.0" y="234.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">0</text><line x1="565.0" y1="122.0" x2="565.0" y2="128.0" stroke="currentColor" stroke-width="1"/><text x="565.0" y="234.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">π/2</text><line x1="630.0" y1="122.0" x2="630.0" y2="128.0" stroke="currentColor" stroke-width="1"/><text x="630.0" y="234.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">π</text><line x1="497.0" y1="220.0" x2="503.0" y2="220.0" stroke="currentColor" stroke-width="1"/><text x="366.0" y="224.0" text-anchor="end" fill="var(--muted)" style="font-size:11px">−π/2</text><line x1="497.0" y1="172.5" x2="503.0" y2="172.5" stroke="currentColor" stroke-width="1"/><text x="366.0" y="176.5" text-anchor="end" fill="var(--muted)" style="font-size:11px">−π/4</text><line x1="497.0" y1="77.5" x2="503.0" y2="77.5" stroke="currentColor" stroke-width="1"/><text x="366.0" y="81.5" text-anchor="end" fill="var(--muted)" style="font-size:11px">π/4</text><line x1="497.0" y1="30.0" x2="503.0" y2="30.0" stroke="currentColor" stroke-width="1"/><text x="366.0" y="34.0" text-anchor="end" fill="var(--muted)" style="font-size:11px">π/2</text><text x="630.0" y="119.0" text-anchor="end" fill="var(--muted)" style="font-size:12px">ω</text><polyline points="370.0,146.0 439.5,101.1 467.9,83.9 477.2,78.8 488.7,73.3 497.4,70.2 504.8,68.9 510.6,69.5 515.0,71.6 519.1,75.9 522.8,82.7 525.6,90.9 528.0,100.5 535.5,142.1 539.6,159.8 542.2,167.3 544.6,172.1 547.2,175.8 551.1,179.1 555.7,180.8 561.5,181.0 567.6,179.8 576.3,176.7 587.8,171.2 597.1,166.1 630.0,146.0" fill="none" stroke="var(--accent2)" stroke-width="1.8" stroke-dasharray="5 4" stroke-linejoin="round" stroke-linecap="round" opacity="1.0"/><polyline points="370.0,125.0 409.4,99.6 439.5,81.6 449.9,76.2 458.2,72.5 466.4,69.8 472.3,68.9 475.5,69.0 478.8,69.7 483.1,72.1 486.6,75.9 490.5,83.2 493.1,90.9 495.7,101.5 503.2,143.2 507.1,159.8 509.5,166.8 513.6,174.4 517.5,178.4 521.2,180.3 524.5,181.0 527.7,181.1 533.6,180.2 543.8,176.7 553.5,172.1 567.2,164.6 586.9,152.7 630.0,125.0" fill="none" stroke="var(--accent)" stroke-width="1.8" stroke-linejoin="round" stroke-linecap="round" opacity="1.0"/><text x="40" y="250" fill="var(--accent)" style="font-size:12px">━ real: 0.8ⁿu[n]</text><text x="250" y="250" fill="var(--accent2)" style="font-size:12px">╌ complex: e<tspan baseline-shift="super" style="font-size:75%">jπn/4</tspan>·0.8ⁿu[n]</text></svg><figcaption><strong>Real signal ⇒ even magnitude, odd phase.</strong> Solid: x[n] = 0.8ⁿu[n], X<sub>d</sub>(ω) = 1/(1 − 0.8e<sup>−jω</sup>); dashed: e<sup>jπn/4</sup>·0.8ⁿu[n], the same spectrum shifted right by π/4 (frequency shift), with neither symmetry.</figcaption></figure>

Plot and compute on $\omega\in[-\pi,\pi]$, where the symmetry is easiest to see.

> [!question] Slide 12: $X_d(\omega)=\omega^2 e^{j\cos\omega}$ (on $-\pi\le\omega\le\pi$). Is $x[n]$ real-valued?

> [!success]- Answer: no
> Magnitude $\omega^2$ is even, but the phase $\cos\omega$ is **even**, not odd:
> $$
> X_d(-\omega)=\omega^2e^{j\cos\omega}\qquad\text{but}\qquad X_d^*(\omega)=\omega^2e^{-j\cos\omega},
> $$
> different wherever $\cos\omega\neq0$. So $x[n]$ is complex (and even: $x[0]\approx2.403-1.752j$, $x[\pm1]\approx-1.276+1.656j$).

> [!question] Slide 13: $x[n]$ is real. Which are true?
> (a) $X_d(0)=X_d(2\pi)$ $\quad$ (b) $X_d(\frac{\pi}{3})=X_d(-\frac{\pi}{3})$ $\quad$ (c) $X_d(\frac{\pi}{3})=X_d^*(-\frac{\pi}{3})$ $\quad$ (d) $X_d(\pi)=X_d(7\pi)$ $\quad$ (e) $X_d(\frac{2\pi}{3})=X_d^*(\frac{4\pi}{3})$

> [!success]- Answer: (a), (c), (d), (e)
> (a) periodicity. (b) not in general: the values at $\pm\frac{\pi}{3}$ are conjugates; only the magnitudes are equal. (c) Hermitian symmetry. (d) $7\pi=\pi+3\cdot2\pi$. (e) $\frac{4\pi}{3}=-\frac{2\pi}{3}+2\pi$, so $X_d(\frac{4\pi}{3})=X_d(-\frac{2\pi}{3})=X_d^*(\frac{2\pi}{3})$.

### 2π periodicity

$$
X_d(\omega+2\pi k)=\sum_n x[n]\,e^{-j\omega n}\underbrace{e^{-j2\pi kn}}_{=1}=X_d(\omega),\qquad k\in\mathbb{Z}.
$$

### Frequency shifting and modulation

- $e^{j\omega_0n}x[n]\leftrightarrow X_d(\omega-\omega_0)$: $\sum_n x[n]e^{j\omega_0 n}e^{-j\omega n}=\sum_n x[n]e^{-j(\omega-\omega_0)n}$ (notes eqs. 39–42).
- Euler gives modulation: $x[n]\cos(\omega_0n)\leftrightarrow\frac12X_d(\omega-\omega_0)+\frac12X_d(\omega+\omega_0)$, two half-height copies (notes eq. 43). Key in digital and wireless communications.
- Copies that run past $\pm\pi$ re-enter from the other side (periodicity).

### Parseval's relation

$$
\sum_{n=-\infty}^{\infty}|x[n]|^2=\frac{1}{2\pi}\int_{-\pi}^{\pi}|X_d(\omega)|^2\,d\omega .
$$

Companions from the definitions: $X_d(0)=\sum_n x[n]$, $X_d(\pi)=\sum_n(-1)^n x[n]$, $\int_{-\pi}^{\pi}X_d(\omega)\,d\omega=2\pi\,x[0]$. [[homework/hw5|HW5]] #2 ($x=\{2,-1,\underset{\uparrow}{1},-1,2\}$): $3$, $7$, $2\pi$, and $\int|X_d|^2=22\pi$.

### Convolution

$x[n]*h[n]\leftrightarrow X_d(\omega)H_d(\omega)$ ($z=e^{j\omega}$ in the z-transform property). With $h$ an impulse response, $H_d(\omega)$ is the **frequency response** ([[3-fourier-analysis/15-frequency-response|Lecture 15]]).

### Multiplication in time (windowing)

$$
x[n]\,w[n]\ \longleftrightarrow\ \frac{1}{2\pi}X_d(\omega)*W_d(\omega)=\frac{1}{2\pi}\int_{2\pi}X_d(\phi)\,W_d(\omega-\phi)\,d\phi .
$$

- Continuous (periodic) convolution in frequency. Proof: substitute the inverse DTFT of $X_d$ and swap sum and integral (notes eqs. 47–51).
- Multiplying by a fixed $w[n]$ is **not** LTI.

> [!trap] Traps
> - Substitute $z=e^{j\omega}$ only if the ROC contains $|z|=1$; a pole on $|z|=1$ ($u[n]$) needs an extra impulse.
> - Two sincs: course $\mathrm{sinc}(x)=\frac{\sin x}{x}$; `np.sinc` and the [[supplements/transform-tables|transform tables]] use $\frac{\sin(\pi x)}{\pi x}$.
> - Time shift needs an integer $k$: $e^{-j\omega/2}$ is a valid DTFT, but not $\delta[n-\frac12]$.
> - Real $x$: $X_d(\omega)$ and $X_d(-\omega)$ are conjugates, not equal.

> [!exam] Exam
> Midterm 2: existence via the ROC, symmetry and periodicity true/false, values without $X_d$, sinc and impulse pairs, modulation sketches. Family: [[problems/dtft-and-inverse-dtft|DTFT and inverse DTFT]].
> - MT2: [[exams/midterm-2/past-exams/fall-2024|FA2024]] #1(a), (b), #2 · [[exams/midterm-2/past-exams/fall-2023|FA2023]] #1(a)–(c), #2 · [[exams/midterm-2/past-exams/spring-2023|SP2023]] #2–#4 · [[exams/midterm-2/past-exams/spring-2025|SP2025]] #2 · [[exams/midterm-2/past-exams/spring-2021|SP2021]] #6, #7 · [[exams/midterm-2/past-exams/fall-2021|FA2021]] #2(c) · [[exams/midterm-2/past-exams/fall-2019|FA2019]] #1(b), (e), #3, #5, #6
> - MT1: [[exams/midterm-1/past-exams/spring-2023|SP2023]] #1(d), (e), #9 · homework: [[homework/hw5|HW5]] #1–#2, [[homework/hw6|HW6]] #2–#5

## Related

[[concepts/dtft-pairs|DTFT pairs]] · [[concepts/dtft-properties|DTFT properties]] · [[concepts/region-of-convergence|ROC]] · [[concepts/bibo-stability|BIBO stability]] · [[3-fourier-analysis/13-fourier-analysis-and-the-dtft|Lecture 13]] · [[3-fourier-analysis/15-frequency-response|Lecture 15]] · [[3-fourier-analysis/index|Unit 3]]

### Sources for this page

Snyder, ECE 310 Lecture 14 notes (§§1–3, Tables 1–2) and slides of Sep 25, 2026 (annotated slides 4–5); HW5–HW6; past Midterm 1–2 exams; course transform tables (the $+j$ sign).
