---
title: "Discrete-time Fourier transform (DTFT)"
description: "X_d(ω) = Σ x[n]e^{−jωn}: definition, inverse, 2π-periodicity, existence (ROC contains the unit circle ⇒ X_d(ω) = X(e^{jω})), the pulse and DTFS link, short-sequence DTFTs, free values, traps."
tags: [concept, dtft, fourier-analysis, midterm-2]
aliases: ["DTFT", "discrete-time Fourier transform", "inverse DTFT", "spectrum", "frequency spectrum", "magnitude spectrum", "phase spectrum"]
---

*Lectures 13 (Wed Sep 23) §4 and 14 (Fri Sep 25) §1 · [[homework/hw5|HW5]] #1, [[homework/hw6|HW6]] #1 · family: [[problems/dtft-and-inverse-dtft|DTFT and inverse DTFT]]*

> [!abstract] In one breath
> - $X_d(\omega)=\sum_nx[n]e^{-j\omega n}$ scores $x$ against every $e^{j\omega n}$; it is $2\pi$-periodic, so $[-\pi,\pi]$ says everything.
> - Exists if $\sum_n|x[n]|<\infty$, i.e. the ROC of $X(z)$ contains $|z|=1$; then $X_d(\omega)=X(e^{j\omega})$.
> - Short sequences: write the sum out; symmetric ones factor into $e^{-jM\omega}\times$ real.

## 1. Definition, inverse, existence

Let $N_0\to\infty$ in the [[concepts/fourier-series|DTFS]]: the harmonic frequencies $\frac{2\pi k}{N_0}$ fill a continuum $\omega$.

> [!key] The DTFT and its inverse (Lecture 13, eqs. 41–42)
> $$
> X_d(\omega)=\sum_{n=-\infty}^{\infty}x[n]\,e^{-j\omega n}\qquad\qquad x[n]=\frac{1}{2\pi}\int_{-\pi}^{\pi}X_d(\omega)\,e^{j\omega n}\,d\omega
> $$
> $\omega$ in radians per sample. $\lvert X_d(\omega)\rvert$: **magnitude spectrum**; $\angle X_d(\omega)$: **phase spectrum**. The inverse may use any interval of length $2\pi$. Manolakis and Ingle write $X(e^{j\omega})$.

> [!key] Existence and uniqueness (Lecture 13, eq. 43)
> If $\sum_n|x[n]|<\infty$, the sum converges for every $\omega$:
> $$
> |X_d(\omega)|\le\sum_{n=-\infty}^{\infty}|x[n]|<\infty .
> $$
> Sufficient, not necessary. If the DTFT exists, it is unique; then $X_d$ is bounded and continuous. Everlasting sinusoids and $u[n]$ need impulses ([[concepts/dtft-pairs|DTFT pairs]]); growing sequences have no DTFT.

- Like the CTFT: complex-valued, continuous in $\omega$, says how much of each frequency is in $x[n]$.
- Unlike the CTFT: **$2\pi$-periodic**, so one period ($[-\pi,\pi]$) says everything; $\omega\approx0$ low, $\omega\approx\pm\pi$ high frequency:

$$
X_d(\omega+2\pi)=\sum_n x[n]\,e^{-j\omega n}\,e^{-j2\pi n}=X_d(\omega).
$$

- **Free values:** $X_d(0)=\sum_nx[n]$; $X_d(\pi)=\sum_n(-1)^nx[n]$; $\int_{-\pi}^{\pi}X_d(\omega)\,d\omega=2\pi\,x[0]$. Parseval: $\int_{-\pi}^{\pi}|X_d(\omega)|^2d\omega=2\pi\sum_n|x[n]|^2$ ([[concepts/dtft-properties|properties]]).

## 2. The rectangular pulse and the DTFS link

> [!question] Exercise 2 (Lecture 13, eqs. 44–48): the pulse $x[n]=1$ for $0\le n<L$, $0$ otherwise
> Find $X_d(\omega)$ and compare with the DTFS of its period-$N_0$ version ([[concepts/fourier-series|Fourier series]] Exercise 1).

> [!success]- Answer
> $$
> \begin{aligned}
> X_d(\omega)&=\sum_{n=0}^{L-1}e^{-j\omega n}=\frac{1-e^{-j\omega L}}{1-e^{-j\omega}}
> =\frac{e^{-j\omega L/2}}{e^{-j\omega/2}}\cdot\frac{e^{j\omega L/2}-e^{-j\omega L/2}}{e^{j\omega/2}-e^{-j\omega/2}}\\
> &=e^{-j\omega(L-1)/2}\,\frac{\sin(\omega L/2)}{\sin(\omega/2)},\qquad X_d(0)=L .
> \end{aligned}
> $$
> (Notes eq. 47 prints the numerator as $e^{j\omega L/2}-e^{j\omega L/2}$; the second exponent needs a minus sign.) At $\omega_k=\frac{2\pi k}{N_0}$ this is $N_0\,c_k$ (notes eq. 49): **DTFS coefficients are DTFT samples divided by $N_0$**.

<figure class="ece-fig"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 680 370" width="680" height="370" role="img" aria-label="periodic DTFT magnitude of a 4-sample pulse with DTFS samples, and periodic impulses for a cosine" style="font-family:'Source Sans 3','Source Sans Pro',system-ui,sans-serif;font-size:13px"><text x="353.0" y="22.0" text-anchor="middle" fill="currentColor" style="font-size:13px;font-weight:600">(a) |X<tspan baseline-shift="sub" style="font-size:75%">d</tspan>(ω)| for x[n] = u[n] − u[n−4], with 12·|c<tspan baseline-shift="sub" style="font-size:75%">k</tspan>| of its period-12 version</text><rect x="251.3" y="28.0" width="203.3" height="120.0" fill="var(--accent)" fill-opacity="0.1" stroke="none"/><line x1="48.0" y1="96.9" x2="658.0" y2="96.9" stroke="var(--muted)" stroke-width="0.6" stroke-dasharray="3 3" opacity="0.6"/><line x1="48.0" y1="45.9" x2="658.0" y2="45.9" stroke="var(--muted)" stroke-width="0.6" stroke-dasharray="3 3" opacity="0.6"/><line x1="48.0" y1="148.0" x2="658.0" y2="148.0" stroke="currentColor" stroke-width="1" opacity="0.75"/><line x1="353.0" y1="28.0" x2="353.0" y2="148.0" stroke="currentColor" stroke-width="1" opacity="0.75"/><line x1="48.0" y1="145.0" x2="48.0" y2="151.0" stroke="currentColor" stroke-width="1"/><text x="48.0" y="162.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">−3π</text><line x1="149.7" y1="145.0" x2="149.7" y2="151.0" stroke="currentColor" stroke-width="1"/><text x="149.7" y="162.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">−2π</text><line x1="251.3" y1="145.0" x2="251.3" y2="151.0" stroke="currentColor" stroke-width="1"/><text x="251.3" y="162.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">−π</text><line x1="353.0" y1="145.0" x2="353.0" y2="151.0" stroke="currentColor" stroke-width="1"/><text x="353.0" y="162.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">0</text><line x1="454.7" y1="145.0" x2="454.7" y2="151.0" stroke="currentColor" stroke-width="1"/><text x="454.7" y="162.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">π</text><line x1="556.3" y1="145.0" x2="556.3" y2="151.0" stroke="currentColor" stroke-width="1"/><text x="556.3" y="162.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">2π</text><line x1="658.0" y1="145.0" x2="658.0" y2="151.0" stroke="currentColor" stroke-width="1"/><text x="658.0" y="162.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">3π</text><line x1="350.0" y1="148.0" x2="356.0" y2="148.0" stroke="currentColor" stroke-width="1"/><text x="44.0" y="152.0" text-anchor="end" fill="var(--muted)" style="font-size:11px">0</text><line x1="350.0" y1="96.9" x2="356.0" y2="96.9" stroke="currentColor" stroke-width="1"/><text x="44.0" y="100.9" text-anchor="end" fill="var(--muted)" style="font-size:11px">2</text><line x1="350.0" y1="45.9" x2="356.0" y2="45.9" stroke="currentColor" stroke-width="1"/><text x="44.0" y="49.9" text-anchor="end" fill="var(--muted)" style="font-size:11px">4</text><text x="658.0" y="142.0" text-anchor="end" fill="var(--muted)" style="font-size:12px">ω</text><polyline points="48.0,148.0 55.6,136.3 62.2,127.8 67.8,122.8 71.9,120.7 74.4,120.2 76.0,120.2 79.5,121.1 82.1,122.6 85.6,125.7 88.7,129.4 91.2,133.2 94.8,139.5 98.8,148.0 106.5,129.3 123.2,83.8 129.8,68.3 135.4,57.8 140.5,50.9 144.6,47.4 146.6,46.4 148.7,45.9 152.7,46.4 156.8,48.9 161.9,54.7 167.0,63.2 174.6,80.0 194.4,133.3 200.5,148.0 207.1,134.9 211.7,128.1 215.2,124.2 217.8,122.2 220.8,120.7 223.4,120.2 224.9,120.2 229.0,121.3 232.5,123.5 235.1,125.7 240.7,132.1 251.3,148.0 262.0,132.1 265.6,127.8 269.6,123.9 275.2,120.7 277.8,120.2 281.8,120.7 284.9,122.2 287.4,124.2 292.0,129.4 297.1,137.6 302.2,148.0 308.3,133.3 325.0,87.8 330.1,75.1 334.2,66.2 338.8,57.8 343.3,51.5 347.9,47.4 352.0,45.9 356.1,46.4 360.1,48.9 362.2,50.9 365.2,54.7 370.3,63.2 374.9,72.8 380.5,86.4 397.7,133.3 403.8,148.0 410.4,134.9 415.0,128.1 418.6,124.2 421.1,122.2 424.2,120.7 426.7,120.2 429.8,120.5 432.3,121.3 435.9,123.5 438.4,125.7 444.0,132.1 454.7,148.0 465.3,132.1 470.9,125.7 474.5,122.8 478.6,120.7 481.1,120.2 485.2,120.7 488.2,122.2 490.8,124.2 495.3,129.4 500.4,137.6 505.5,148.0 514.7,125.2 529.9,83.8 537.5,66.2 543.1,56.2 547.2,50.9 551.2,47.4 555.3,45.9 557.4,45.9 559.9,46.6 562.4,48.1 565.5,50.9 570.6,57.8 575.7,67.3 582.8,83.8 599.5,129.3 607.2,148.0 611.2,139.5 617.3,129.4 620.4,125.7 623.9,122.6 627.5,120.7 630.0,120.2 631.6,120.2 635.6,121.3 639.2,123.5 641.7,125.7 648.9,134.2 658.0,148.0" fill="none" stroke="var(--accent)" stroke-width="1.8" stroke-linejoin="round" stroke-linecap="round" opacity="1.0"/><circle cx="48.0" cy="148.0" r="2.8" fill="var(--hi)" stroke="var(--hi)" stroke-width="1.5"/><circle cx="64.9" cy="125.1" r="2.8" fill="var(--hi)" stroke="var(--hi)" stroke-width="1.5"/><circle cx="81.9" cy="122.5" r="2.8" fill="var(--hi)" stroke="var(--hi)" stroke-width="1.5"/><circle cx="98.8" cy="148.0" r="2.8" fill="var(--hi)" stroke="var(--hi)" stroke-width="1.5"/><circle cx="115.8" cy="103.8" r="2.8" fill="var(--hi)" stroke="var(--hi)" stroke-width="1.5"/><circle cx="132.7" cy="62.6" r="2.8" fill="var(--hi)" stroke="var(--hi)" stroke-width="1.5"/><circle cx="149.7" cy="45.9" r="2.8" fill="var(--hi)" stroke="var(--hi)" stroke-width="1.5"/><circle cx="166.6" cy="62.6" r="2.8" fill="var(--hi)" stroke="var(--hi)" stroke-width="1.5"/><circle cx="183.6" cy="103.8" r="2.8" fill="var(--hi)" stroke="var(--hi)" stroke-width="1.5"/><circle cx="200.5" cy="148.0" r="2.8" fill="var(--hi)" stroke="var(--hi)" stroke-width="1.5"/><circle cx="217.4" cy="122.5" r="2.8" fill="var(--hi)" stroke="var(--hi)" stroke-width="1.5"/><circle cx="234.4" cy="125.1" r="2.8" fill="var(--hi)" stroke="var(--hi)" stroke-width="1.5"/><circle cx="251.3" cy="148.0" r="2.8" fill="var(--hi)" stroke="var(--hi)" stroke-width="1.5"/><circle cx="268.3" cy="125.1" r="2.8" fill="var(--hi)" stroke="var(--hi)" stroke-width="1.5"/><circle cx="285.2" cy="122.5" r="2.8" fill="var(--hi)" stroke="var(--hi)" stroke-width="1.5"/><circle cx="302.2" cy="148.0" r="2.8" fill="var(--hi)" stroke="var(--hi)" stroke-width="1.5"/><circle cx="319.1" cy="103.8" r="2.8" fill="var(--hi)" stroke="var(--hi)" stroke-width="1.5"/><circle cx="336.1" cy="62.6" r="2.8" fill="var(--hi)" stroke="var(--hi)" stroke-width="1.5"/><circle cx="353.0" cy="45.9" r="2.8" fill="var(--hi)" stroke="var(--hi)" stroke-width="1.5"/><circle cx="369.9" cy="62.6" r="2.8" fill="var(--hi)" stroke="var(--hi)" stroke-width="1.5"/><circle cx="386.9" cy="103.8" r="2.8" fill="var(--hi)" stroke="var(--hi)" stroke-width="1.5"/><circle cx="403.8" cy="148.0" r="2.8" fill="var(--hi)" stroke="var(--hi)" stroke-width="1.5"/><circle cx="420.8" cy="122.5" r="2.8" fill="var(--hi)" stroke="var(--hi)" stroke-width="1.5"/><circle cx="437.7" cy="125.1" r="2.8" fill="var(--hi)" stroke="var(--hi)" stroke-width="1.5"/><circle cx="454.7" cy="148.0" r="2.8" fill="var(--hi)" stroke="var(--hi)" stroke-width="1.5"/><circle cx="471.6" cy="125.1" r="2.8" fill="var(--hi)" stroke="var(--hi)" stroke-width="1.5"/><circle cx="488.6" cy="122.5" r="2.8" fill="var(--hi)" stroke="var(--hi)" stroke-width="1.5"/><circle cx="505.5" cy="148.0" r="2.8" fill="var(--hi)" stroke="var(--hi)" stroke-width="1.5"/><circle cx="522.4" cy="103.8" r="2.8" fill="var(--hi)" stroke="var(--hi)" stroke-width="1.5"/><circle cx="539.4" cy="62.6" r="2.8" fill="var(--hi)" stroke="var(--hi)" stroke-width="1.5"/><circle cx="556.3" cy="45.9" r="2.8" fill="var(--hi)" stroke="var(--hi)" stroke-width="1.5"/><circle cx="573.3" cy="62.6" r="2.8" fill="var(--hi)" stroke="var(--hi)" stroke-width="1.5"/><circle cx="590.2" cy="103.8" r="2.8" fill="var(--hi)" stroke="var(--hi)" stroke-width="1.5"/><circle cx="607.2" cy="148.0" r="2.8" fill="var(--hi)" stroke="var(--hi)" stroke-width="1.5"/><circle cx="624.1" cy="122.5" r="2.8" fill="var(--hi)" stroke="var(--hi)" stroke-width="1.5"/><circle cx="641.1" cy="125.1" r="2.8" fill="var(--hi)" stroke="var(--hi)" stroke-width="1.5"/><circle cx="658.0" cy="148.0" r="2.8" fill="var(--hi)" stroke="var(--hi)" stroke-width="1.5"/><text x="383.0" y="49.9" text-anchor="start" fill="var(--accent)" style="font-size:11px">one period</text><text x="353.0" y="208.0" text-anchor="middle" fill="currentColor" style="font-size:13px;font-weight:600">(b) X<tspan baseline-shift="sub" style="font-size:75%">d</tspan>(ω) for cos(πn/3): impulses of area π at ±π/3, repeated every 2π</text><rect x="251.3" y="214.0" width="203.3" height="120.0" fill="var(--accent)" fill-opacity="0.1" stroke="none"/><line x1="48.0" y1="334.0" x2="658.0" y2="334.0" stroke="currentColor" stroke-width="1" opacity="0.75"/><line x1="353.0" y1="214.0" x2="353.0" y2="334.0" stroke="currentColor" stroke-width="1" opacity="0.75"/><line x1="48.0" y1="331.0" x2="48.0" y2="337.0" stroke="currentColor" stroke-width="1"/><text x="48.0" y="348.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">−3π</text><line x1="149.7" y1="331.0" x2="149.7" y2="337.0" stroke="currentColor" stroke-width="1"/><text x="149.7" y="348.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">−2π</text><line x1="251.3" y1="331.0" x2="251.3" y2="337.0" stroke="currentColor" stroke-width="1"/><text x="251.3" y="348.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">−π</text><line x1="353.0" y1="331.0" x2="353.0" y2="337.0" stroke="currentColor" stroke-width="1"/><text x="353.0" y="348.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">0</text><line x1="454.7" y1="331.0" x2="454.7" y2="337.0" stroke="currentColor" stroke-width="1"/><text x="454.7" y="348.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">π</text><line x1="556.3" y1="331.0" x2="556.3" y2="337.0" stroke="currentColor" stroke-width="1"/><text x="556.3" y="348.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">2π</text><line x1="658.0" y1="331.0" x2="658.0" y2="337.0" stroke="currentColor" stroke-width="1"/><text x="658.0" y="348.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">3π</text><text x="658.0" y="328.0" text-anchor="end" fill="var(--muted)" style="font-size:12px">ω</text><line x1="115.8" y1="334.0" x2="115.8" y2="258.3" stroke="var(--muted)" stroke-width="2"/><path d="M110.8,260.3 L115.8,252.3 L120.8,260.3 Z" fill="var(--muted)"/><line x1="183.6" y1="334.0" x2="183.6" y2="258.3" stroke="var(--muted)" stroke-width="2"/><path d="M178.6,260.3 L183.6,252.3 L188.6,260.3 Z" fill="var(--muted)"/><line x1="319.1" y1="334.0" x2="319.1" y2="258.3" stroke="var(--hi)" stroke-width="2"/><path d="M314.1,260.3 L319.1,252.3 L324.1,260.3 Z" fill="var(--hi)"/><text x="325.1" y="256.3" text-anchor="start" fill="var(--hi)" style="font-size:11px">π</text><line x1="386.9" y1="334.0" x2="386.9" y2="258.3" stroke="var(--hi)" stroke-width="2"/><path d="M381.9,260.3 L386.9,252.3 L391.9,260.3 Z" fill="var(--hi)"/><text x="392.9" y="256.3" text-anchor="start" fill="var(--hi)" style="font-size:11px">π</text><line x1="522.4" y1="334.0" x2="522.4" y2="258.3" stroke="var(--muted)" stroke-width="2"/><path d="M517.4,260.3 L522.4,252.3 L527.4,260.3 Z" fill="var(--muted)"/><line x1="590.2" y1="334.0" x2="590.2" y2="258.3" stroke="var(--muted)" stroke-width="2"/><path d="M585.2,260.3 L590.2,252.3 L595.2,260.3 Z" fill="var(--muted)"/><text x="386.9" y="360.0" text-anchor="middle" fill="var(--muted)" style="font-size:10px">π/3</text><text x="319.1" y="360.0" text-anchor="middle" fill="var(--muted)" style="font-size:10px">−π/3</text></svg><figcaption><strong>DTFS coefficients sample the DTFT (cf. notes Fig. 2).</strong> (a) |X<sub>d</sub>(ω)| = |sin(2ω)/sin(ω/2)| of the 4-sample pulse repeats every 2π, and the dots are 12·|c<sub>k</sub>| of its period-12 version at ω<sub>k</sub> = 2πk/12; (b) cos(πn/3) is not absolutely summable, and its DTFT is impulses of area π at ±π/3, repeated every 2π (Lecture 14).</figcaption></figure>

## 3. The DTFT is the z-transform on the unit circle

- z-transform: how much of each $z^n$, $z\in\mathbb{C}$, is in a signal ([[concepts/z-transform|z-transform]]). DTFT: how much of each $e^{j\omega n}$. Signals that are both: $z^n$ with $z=e^{j\omega}$, the unit circle.

> [!key] Bridge (Lecture 14, eqs. 1–2)
> $$
> X(z)\Big|_{z=e^{j\omega}}=\sum_{n=-\infty}^{\infty}x[n]\,e^{-j\omega n}=X_d(\omega)\qquad\text{if the ROC of } X(z) \text{ contains } |z|=1 .
> $$
> Hence the textbook's $X(e^{j\omega})$. $\sum|x[n]|<\infty$ $\iff$ the ROC contains $|z|=1$, and only then may $z^{-1}$ be replaced by $e^{-j\omega}$.

- Why keep the z-transform: it covers every $z$. $x[n]=2^nu[n]$ has $X(z)=\frac{1}{1-2z^{-1}}$, $|z|>2$, but $\sum_n|x[n]|=\infty$: no DTFT (eqs. 3–5). Example that works: $(\tfrac12)^nu[n]$ gives $X_d(\omega)=\frac{1}{1-\frac12e^{-j\omega}}$, $X_d(0)=2$, $X_d(\pi)=\frac23$.
- Stability ([[concepts/bibo-stability|BIBO]]): BIBO stable $\iff\sum_n|h[n]|<\infty\iff$ ROC of $H(z)$ contains $|z|=1\iff$ the DTFT sum of $h$ converges absolutely (eq. 6). So the [[concepts/frequency-response|frequency response]] of a stable system is $H(e^{j\omega})$.
- *Absolutely* matters: the ideal low-pass $h[n]=\frac{\sin(Wn)}{\pi n}$ has a DTFT (a rectangle) but is not stable.
- **Linear-algebra view** (eqs. 10–12, optional): $X_d(\omega)=\mathbf{v}^*\mathbf{u}$ with $\mathbf{u}=x[n]$, $\mathbf{v}=e^{j\omega n}$: how similar $x$ is to frequency $\omega$ ([[concepts/template-matching|template matching]]).

## 4. Short sequences by hand

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

> [!question] Lecture 13 slide 15: DTFT of $x[n]=\{\underset{\uparrow}{1},0,1,0,1\}$

> [!success]- Answer
> $x[n]=\delta[n]+\delta[n-2]+\delta[n-4]$:
> $$
> X_d(\omega)=1+e^{-j2\omega}+e^{-j4\omega}=e^{-j2\omega}\big(e^{j2\omega}+1+e^{-j2\omega}\big)=e^{-j2\omega}\big(1+2\cos(2\omega)\big).
> $$
> $X_d(0)=3$, $X_d(\frac{\pi}{2})=e^{-j\pi}(1-2)=1$, $X_d(\pi)=3$.

> [!question] Lecture 13 slide 16: $X_d(\omega)=2j\sin\omega$. Which sequence is $x[n]$?
> (a) $\{\underset{\uparrow}{1},0,-1\}$ $\quad$ (b) $\{1,\underset{\uparrow}{0},-1\}$ $\quad$ (c) $\{\underset{\uparrow}{2},0,-2\}$ $\quad$ (d) $\{2,\underset{\uparrow}{0},-2\}$

> [!success]- Answer: (b)
> $2j\sin\omega=e^{j\omega}-e^{-j\omega}$: $x[-1]=1$, $x[1]=-1$. Others: (a) $1-e^{-j2\omega}$, (c) $2-2e^{-j2\omega}$, (d) $2e^{j\omega}-2e^{-j\omega}=4j\sin\omega$.

> [!question] Lecture 14 slide 4: compute the DTFT
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

> [!question] Lecture 14 slide 6: do these DTFTs exist?
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

> [!trap]
> - $2^nu[n]$ has no DTFT although $\frac{1}{1-2e^{-j\omega}}$ evaluates fine; "$X_d=X(e^{j\omega})$ always" is False ([[exams/midterm-2/past-exams/fall-2024|FA2024 MT2]] #1(a), [[exams/midterm-1/past-exams/spring-2023|SP2023 MT1]] #1(d)). A pole on $|z|=1$ ($u[n]$) needs an extra impulse.
> - Every DTFT repeats every $2\pi$; "bandlimited to $\frac{\pi}{4}$" means zero on $\frac{\pi}{4}<|\omega|\le\pi$ only ([[exams/midterm-2/past-exams/fall-2019|FA2019 MT2]] #1(b)).
> - Impulses need all $n$: a finite piece of a cosine has an ordinary DTFT. Zero-padding changes nothing.
> - $e^{-j\omega/2}$ is not $\delta[n-\frac12]$; its inverse is $\frac{\sin(\pi(n-\frac12))}{\pi(n-\frac12)}$ ([[exams/midterm-2/past-exams/fall-2023|FA2023 MT2]] #1(b)).
> - A real $X_d$ can be negative; a magnitude cannot: $1+2\cos(2\omega)=-1$ at $\omega=\frac{\pi}{2}$ means magnitude $1$, phase $\pi$ (the centred $\delta[n+2]+\delta[n]+\delta[n-2]$, [[exams/midterm-2/past-exams/fall-2024|FA2024 MT2]] #3; slide 15's causal version adds $e^{-j2\omega}$).

> [!exam] Exam
> DTFTs of short sequences from the definition; existence via the ROC; true/false on uniqueness, $2\pi$-periodicity and zero-padding. Family: [[problems/dtft-and-inverse-dtft|DTFT and inverse DTFT]].
> - MT2: [[exams/midterm-2/past-exams/fall-2024|FA2024]] #1(a), (b), (d), #3(a) · [[exams/midterm-2/past-exams/fall-2023|FA2023]] #1(a), (b), (f) · [[exams/midterm-2/past-exams/spring-2023|SP2023]] #1(c), #3 · [[exams/midterm-2/past-exams/spring-2025|SP2025]] #1(a), (d) · [[exams/midterm-2/past-exams/spring-2021|SP2021]] #3 · [[exams/midterm-2/past-exams/fall-2019|FA2019]] #1(a)–(c), (e)
> - MT1: [[exams/midterm-1/past-exams/spring-2023|SP2023]] #1(d), #8 · homework: [[homework/hw5|HW5]] #1, [[homework/hw6|HW6]] #1

**Where it appears:** [[3-fourier-analysis/13-fourier-analysis-and-the-dtft|L13]] §4 (slides 14–16), [[3-fourier-analysis/14-dtft-properties|L14]] §1 (slides 3–6), [[3-fourier-analysis/15-frequency-response|L15]]–[[3-fourier-analysis/16-magnitude-and-phase-response|L16]]; [[problems/dtft-and-inverse-dtft|DTFT family]]; [[homework/hw5|HW5]], [[homework/hw6|HW6]]; [[exams/quiz-2|Quiz 2]]; all seven past Midterm 2 exams.

## Related
[[concepts/dtft-pairs|DTFT pairs]] · [[concepts/dtft-properties|DTFT properties]] · [[concepts/fourier-series|Fourier series]] · [[concepts/periodic-signals|periodic signals]] · [[concepts/frequency-response|frequency response]] · [[concepts/magnitude-and-phase-response|magnitude and phase]] · [[concepts/region-of-convergence|ROC]] · [[concepts/z-transform|z-transform]] · [[supplements/transform-tables|transform tables]]

### Sources for this page
Lecture 13 notes §4 (eqs. 41–49, Exercise 2, Fig. 2), slides 14–16; Lecture 14 notes §1–1.1 (eqs. 1–12), slides 3–6; HW5–HW6; Midterm 2 keys FA2019–SP2025.
