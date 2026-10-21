---
title: "Lecture 2 — Complex numbers and elementary signals"
description: "Rectangular and polar form, conjugate, magnitude and phase with the quadrant rule, principal angle, Euler's formula and identities; the n = 0 marker, Kronecker delta, unit step, sinusoids and exponentials."
tags: [lecture, midterm-1, complex-numbers, signals]
lecture: 2
---

*Lecture 2 · Wed Aug 26, 2026 · notes + slides "Math preliminaries, complex numbers" · prev: [[1-signals-and-systems/01-digital-signals|Lecture 1]] · next: [[1-signals-and-systems/03-system-properties|Lecture 3]]*

> [!abstract] In one breath
> - $x = a + jb = Re^{j\theta}$: add in rectangular form, multiply and divide in polar; Euler converts.
> - Phase needs the quadrant rule; angles repeat every $2\pi$.
> - Building blocks: $\delta[n]$, $u[n]$, $A\sin(\omega_0 n + \theta)$, $Ba^n$.

## 1. Complex numbers

### 1.1 Rectangular form

> [!key] Rectangular form and conjugate (eqs. 1–2)
> $$
> x = a + jb, \qquad a = \operatorname{Re}\{x\},\quad b = \operatorname{Im}\{x\},\quad j = \sqrt{-1}; \qquad x^* = a - jb .
> $$
> $x^*x$ is always real.

- Add, subtract: real and imaginary parts separately.
- Multiply: expand every pair, $j^2 = -1$.
- Divide: multiply top and bottom by the denominator's conjugate (eqs. 3–5):
$$
\frac{1 + j2}{3 - j} = \frac{(1+j2)(3+j)}{(3-j)(3+j)} = \frac{1 + j7}{10}.
$$
- Complex plane: real part horizontal, imaginary part vertical; $x^*$ mirrors $x$ across the real axis (notes Fig. 1).

### 1.2 Polar form

> [!key] Polar form (eqs. 6–10)
> $$
> x = R\,e^{j\theta}, \quad x^* = R\,e^{-j\theta}; \qquad y = Se^{j\phi}: \quad xy = RS\,e^{j(\theta+\phi)}, \quad \frac{x}{y} = \frac{R}{S}\,e^{j(\theta-\phi)} .
> $$

### 1.3 Magnitude and phase of complex numbers

> [!key] Magnitude and phase of $x = a + jb = Re^{j\theta}$ (eqs. 11–12)
> $$
> \begin{gathered}
> \lvert x\rvert = \sqrt{a^2 + b^2} = \sqrt{x\,x^*} = R \ge 0, \\[4pt]
> \angle x = \theta =
> \begin{cases}
> \tan^{-1}\!\left(\frac{b}{a}\right), & a \ge 0\\[4pt]
> \tan^{-1}\!\left(\frac{b}{a}\right) + \pi, & a < 0,\ b \ge 0\\[4pt]
> \tan^{-1}\!\left(\frac{b}{a}\right) - \pi, & a < 0,\ b < 0
> \end{cases}
> \quad \in [-\pi, \pi].
> \end{gathered}
> $$
> Real numbers have phase $0$ (positive) or $\pm\pi$ (negative).

<figure class="ece-fig"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 640 300" width="640" height="300" role="img" aria-label="Complex plane: x = -4 + j3 with magnitude and phase, its conjugate, and the 8th roots of unity" style="font-family:'Source Sans 3','Source Sans Pro',system-ui,sans-serif;font-size:13px"><line x1="40.0" y1="150.0" x2="338.0" y2="150.0" stroke="currentColor" stroke-width="1.1" stroke-linecap="round"/><polygon points="344.0,150.0 338.0,146.7 338.0,153.3" fill="currentColor"/><line x1="190.0" y1="270.0" x2="190.0" y2="32.0" stroke="currentColor" stroke-width="1.1" stroke-linecap="round"/><polygon points="190.0,26.0 186.7,32.0 193.3,32.0" fill="currentColor"/><text x="342.0" y="168.0" text-anchor="end" fill="currentColor" style="font-size:12px;">Re</text><text x="198.0" y="36.0" text-anchor="start" fill="currentColor" style="font-size:12px;">Im</text><line x1="86.0" y1="147.0" x2="86.0" y2="153.0" stroke="currentColor" stroke-width="1" stroke-linecap="round"/><text x="86.0" y="166.0" text-anchor="middle" fill="currentColor" style="font-size:11px;" opacity="0.8">−4</text><line x1="138.0" y1="147.0" x2="138.0" y2="153.0" stroke="currentColor" stroke-width="1" stroke-linecap="round"/><text x="138.0" y="166.0" text-anchor="middle" fill="currentColor" style="font-size:11px;" opacity="0.8">−2</text><line x1="242.0" y1="147.0" x2="242.0" y2="153.0" stroke="currentColor" stroke-width="1" stroke-linecap="round"/><text x="242.0" y="166.0" text-anchor="middle" fill="currentColor" style="font-size:11px;" opacity="0.8">2</text><line x1="294.0" y1="147.0" x2="294.0" y2="153.0" stroke="currentColor" stroke-width="1" stroke-linecap="round"/><text x="294.0" y="166.0" text-anchor="middle" fill="currentColor" style="font-size:11px;" opacity="0.8">4</text><line x1="187.0" y1="228.0" x2="193.0" y2="228.0" stroke="currentColor" stroke-width="1" stroke-linecap="round"/><text x="198.0" y="232.0" text-anchor="start" fill="currentColor" style="font-size:11px;" opacity="0.8">−3j</text><line x1="187.0" y1="72.0" x2="193.0" y2="72.0" stroke="currentColor" stroke-width="1" stroke-linecap="round"/><text x="198.0" y="76.0" text-anchor="start" fill="currentColor" style="font-size:11px;" opacity="0.8">3j</text><line x1="86.0" y1="72.0" x2="86.0" y2="150.0" stroke="currentColor" stroke-width="1" stroke-dasharray="3 3" opacity="0.6" stroke-linecap="round"/><line x1="86.0" y1="72.0" x2="190.0" y2="72.0" stroke="currentColor" stroke-width="1" stroke-dasharray="3 3" opacity="0.6" stroke-linecap="round"/><line x1="190.0" y1="150.0" x2="86.0" y2="72.0" stroke="var(--accent)" stroke-width="2.4" stroke-linecap="round"/><circle cx="86.0" cy="72.0" r="5.0" fill="var(--accent)" stroke="none" stroke-width="1.4"/><line x1="190.0" y1="150.0" x2="86.0" y2="228.0" stroke="var(--accent2)" stroke-width="1.6" stroke-dasharray="6 4" stroke-linecap="round"/><circle cx="86.0" cy="228.0" r="4.6" fill="none" stroke="var(--accent2)" stroke-width="1.8"/><text x="78.0" y="62.0" text-anchor="middle" fill="var(--accent)" style="font-size:13.5px;font-weight:600;">x = −4 + j3</text><text x="80.0" y="248.0" text-anchor="middle" fill="var(--accent2)" style="font-size:13px;font-weight:600;">x* = −4 − j3</text><text x="152.0" y="103.0" text-anchor="start" fill="var(--accent)" style="font-size:13px;">R = 5</text><path d="M220,150 A30,30 0 0 0 166.0,132.0" fill="none" stroke="currentColor" stroke-width="1.3"/><text x="220.0" y="116.0" text-anchor="start" fill="currentColor" style="font-size:12px;">θ ≈ 2.50 rad (143°)</text><text x="40.0" y="22" text-anchor="start" fill="currentColor" style="font-size:13px;font-weight:600">rectangular a + jb  ↔  polar Re<tspan dy="-6" style="font-size:10px">jθ</tspan></text><line x1="382.0" y1="156.0" x2="616.0" y2="156.0" stroke="currentColor" stroke-width="1.1" stroke-linecap="round"/><polygon points="622.0,156.0 616.0,152.7 616.0,159.3" fill="currentColor"/><line x1="500.0" y1="272.0" x2="500.0" y2="42.0" stroke="currentColor" stroke-width="1.1" stroke-linecap="round"/><polygon points="500.0,36.0 496.7,42.0 503.3,42.0" fill="currentColor"/><text x="620.0" y="174.0" text-anchor="end" fill="currentColor" style="font-size:12px;">Re</text><text x="508.0" y="46.0" text-anchor="start" fill="currentColor" style="font-size:12px;">Im</text><circle cx="500.0" cy="156.0" r="86.0" fill="none" stroke="currentColor" stroke-width="1.2" stroke-dasharray="4 4" opacity="0.7"/><circle cx="586.0" cy="156.0" r="6.0" fill="var(--accent)" stroke="none" stroke-width="1.4"/><line x1="500.0" y1="156.0" x2="560.8" y2="95.2" stroke="var(--accent2)" stroke-width="1" stroke-dasharray="3 3" opacity="0.7" stroke-linecap="round"/><circle cx="560.8" cy="95.2" r="5.5" fill="none" stroke="var(--accent2)" stroke-width="2"/><circle cx="500.0" cy="70.0" r="6.0" fill="var(--accent)" stroke="none" stroke-width="1.4"/><line x1="500.0" y1="156.0" x2="439.2" y2="95.2" stroke="var(--accent2)" stroke-width="1" stroke-dasharray="3 3" opacity="0.7" stroke-linecap="round"/><circle cx="439.2" cy="95.2" r="5.5" fill="none" stroke="var(--accent2)" stroke-width="2"/><circle cx="414.0" cy="156.0" r="6.0" fill="var(--accent)" stroke="none" stroke-width="1.4"/><line x1="500.0" y1="156.0" x2="439.2" y2="216.8" stroke="var(--accent2)" stroke-width="1" stroke-dasharray="3 3" opacity="0.7" stroke-linecap="round"/><circle cx="439.2" cy="216.8" r="5.5" fill="none" stroke="var(--accent2)" stroke-width="2"/><circle cx="500.0" cy="242.0" r="6.0" fill="var(--accent)" stroke="none" stroke-width="1.4"/><line x1="500.0" y1="156.0" x2="560.8" y2="216.8" stroke="var(--accent2)" stroke-width="1" stroke-dasharray="3 3" opacity="0.7" stroke-linecap="round"/><circle cx="560.8" cy="216.8" r="5.5" fill="none" stroke="var(--accent2)" stroke-width="2"/><text x="596.0" y="148.0" text-anchor="start" fill="currentColor" style="font-size:14px;font-family:'STIX Two Math','Latin Modern Math','Cambria Math','Times New Roman',serif;font-style:italic;font-weight:600;">1</text><text x="510.0" y="66.0" text-anchor="start" fill="currentColor" style="font-size:14px;font-family:'STIX Two Math','Latin Modern Math','Cambria Math','Times New Roman',serif;font-style:italic;font-weight:600;">j</text><text x="402.0" y="148.0" text-anchor="end" fill="currentColor" style="font-size:14px;font-family:'STIX Two Math','Latin Modern Math','Cambria Math','Times New Roman',serif;font-style:italic;font-weight:600;">−1</text><text x="510.0" y="258.0" text-anchor="start" fill="currentColor" style="font-size:14px;font-family:'STIX Two Math','Latin Modern Math','Cambria Math','Times New Roman',serif;font-style:italic;font-weight:600;">−j</text><path d="M534,156 A34,34 0 0 0 524.0,132.0" fill="none" stroke="currentColor" stroke-width="1.2"/><text x="540.0" y="146.0" text-anchor="start" fill="currentColor" style="font-size:11.5px;font-family:'STIX Two Math','Latin Modern Math','Cambria Math','Times New Roman',serif;font-style:italic;">π/4</text><text x="382.0" y="22" text-anchor="start" fill="currentColor" style="font-size:13px;font-weight:600">8th roots of unity e<tspan dy="-6" style="font-size:10px">j2πk/8</tspan></text><circle cx="388.0" cy="280.0" r="5.5" fill="var(--accent)" stroke="none" stroke-width="1.4"/><text x="398.0" y="284.0" text-anchor="start" fill="currentColor" style="font-size:12.5px;">z⁴ = 1</text><circle cx="506.0" cy="280.0" r="5.0" fill="none" stroke="var(--accent2)" stroke-width="2"/><text x="516.0" y="284.0" text-anchor="start" fill="currentColor" style="font-size:12.5px;">z⁴ = −1  (HW1 #4)</text></svg><figcaption><strong>Left: x = −4 + j3 = 5e<sup>jθ</sup> with θ ≈ 2.50 rad (second quadrant); x* is its mirror image.</strong> Right: the 8th roots of unity; filled dots solve z⁴ = 1, open dots solve z⁴ = −1 (HW1 #4).</figcaption></figure>

> [!question] Slides 7–8: magnitude and phase of (a) $x = -4 + j3$, (b) $y = j2$, and the special case $x = -3.10$.

> [!success]- Answers
> (a) $\lvert x\rvert = \sqrt{16 + 9} = 5$; $a < 0$, $b \ge 0$: $\angle x = \tan^{-1}\!\big(\tfrac{3}{-4}\big) + \pi \approx 2.50$ rad $\approx 143.1°$, so $x = 5e^{j2.50}$.
> (b) $\lvert y\rvert = 2$, $\angle y = \tfrac{\pi}{2}$: $y = 2e^{j\pi/2}$.
> Special case: $-3.10 = 3.10\,e^{\pm j\pi}$: magnitude $3.10$, phase $\pm\pi$.

> [!key] Principal angle (eq. 13)
> $$
> Re^{j\theta} = Re^{j(\theta_p + 2\pi k)}, \qquad k \in \mathbb{Z},
> $$
> $\theta_p \in [-\pi, \pi]$ (or $[0, 2\pi]$; conventions vary). $e^{j\pi/3}$ and $e^{j7\pi/3}$ are the same point, $\theta_p = \pi/3$.

> [!trap] Angle traps
> - $\tan^{-1}(b/a)$ alone loses the quadrant: $-4 + j3$ and $4 - j3$ share $b/a = -\tfrac34$, phases $2.50$ and $-0.64$ rad. Sketch the point first.
> - Magnitude is never negative: $-3.10$ has $R = 3.10$, phase $\pm\pi$.
> - $e^{j2/3}$ has angle $2/3$ rad $\approx 38°$, not $2\pi/3$.

### 1.4 Euler's identities

> [!key] Euler (eqs. 14–20)
> $$
> e^{j\theta} = \cos\theta + j\sin\theta, \qquad Re^{j\theta} = R\cos\theta + jR\sin\theta \quad(\text{polar} \to \text{rectangular}).
> $$
> $$
> e^{\pm j\pi} = -1, \qquad \cos\theta = \frac{e^{j\theta} + e^{-j\theta}}{2}, \qquad \sin\theta = \frac{e^{j\theta} - e^{-j\theta}}{2j}.
> $$

> [!derivation]- Where the identities come from
> Add and subtract Euler at $\pm\theta$; $\cos$ is even, $\sin$ odd:
> $$
> e^{j\theta} + e^{-j\theta} = 2\cos\theta, \qquad e^{j\theta} - e^{-j\theta} = 2j\sin\theta .
> $$

> [!question] Slide 12: simplify into rectangular and polar form (a) $j2 + \sqrt2\,e^{-j\pi/4}$, (b) $\dfrac{j3}{1-j}$.

> [!success]- Answers
> (a) $\sqrt2\,e^{-j\pi/4} = \sqrt2\big(\tfrac{\sqrt2}{2} - j\tfrac{\sqrt2}{2}\big) = 1 - j$; sum $1 + j = \sqrt2\,e^{j\pi/4}$.
> (b) $\lvert j3\rvert / \lvert 1-j\rvert = 3/\sqrt2$, $\angle = \tfrac{\pi}{2} - \big(-\tfrac{\pi}{4}\big) = \tfrac{3\pi}{4}$: $\dfrac{j3}{1-j} = \dfrac{3}{\sqrt2}\,e^{j3\pi/4} = -\dfrac32 + j\dfrac32$. Check: $\dfrac{j3(1+j)}{2} = \dfrac{-3 + j3}{2}$ ✓.

Beyond the notes: roots of $z^N = c$ and geometric sums are in the toolkit ([[0-toolkit/01-complex-numbers|complex numbers]], [[0-toolkit/02-geometric-series|geometric series]]). HW1 #4: $z^4 = 1$ gives $1, j, -1, -j$; $z^4 = -1$ gives $\dfrac{\pm1 \pm j}{\sqrt2}$.

## 2. Common discrete-time signal representations

Mark the $n = 0$ sample (arrow, bold or underline). Slide 13: $x[n] = \{1, \underset{\uparrow}{4}, -2, 0, 3, 1, 2\} = \{x[n]\}_{n=-1}^{5}$, so $x[-1] = 1$, $x[0] = 4$, $x[5] = 2$.

> [!key] Kronecker delta and unit step (eqs. 21–22)
> $$
> \delta[n] = \begin{cases} 1, & n = 0\\ 0, & n \ne 0\end{cases} \qquad\qquad
> u[n] = \begin{cases} 1, & n \ge 0\\ 0, & n < 0\end{cases}
> $$
> $\delta[n]$: unit impulse, unit pulse; **not** the Dirac delta. Any signal is a sum of scaled, shifted deltas.

Scale, shift, flip: $3\delta[n-10]$ is $3$ at $n = 10$ only; $4u[3-n]$ is $4$ for $n \le 3$, $0$ for $n > 3$.

> [!question] Slides 14–15: sketch $x[n] = -2\delta[n+3]$ and $u[3-n]$; write $x[n] = \{2, 0, \underset{\uparrow}{3}, -1, -4\}$ in terms of $\delta[n]$.

> [!success]- Answers
> $-2\delta[n+3]$: $-2$ at $n = -3$, zero elsewhere. $u[3-n]$: $1$ for $n \le 3$, a step running left. $x[n] = 2\delta[n+2] + 3\delta[n] - \delta[n-1] - 4\delta[n-2]$.

> [!key] Sinusoids and exponentials (eqs. 23–24)
> $$
> x[n] = A\sin(\omega_0 n + \theta), \quad A, \omega_0, \theta \in \mathbb{R}; \qquad x[n] = B\,a^n, \quad B, a \in \mathbb{C}.
> $$
> $\omega_0$ in radians per sample. Notes Fig. 2: $2\delta[n+3] - 3\delta[n-1]$, $5u[2-n]$, $\cos(\frac{\pi}{10}n - \frac{\pi}{3})$, $2(-\tfrac34)^n$.

With $a = re^{j\omega_0}$: $a^n = r^n\big(\cos(\omega_0 n) + j\sin(\omega_0 n)\big)$; $r < 1$ decays, $r = 1$ stays on the unit circle, $r > 1$ grows.

> [!exam] Where Lecture 2 shows up
> No calculator: know $e^{j\pi/4} = \frac{1+j}{\sqrt2}$, $e^{j\pi/3} = \frac12 + j\frac{\sqrt3}{2}$, $e^{j2\pi/3} = -\frac12 + j\frac{\sqrt3}{2}$. Tested via sifting T/F items, Euler inside z-transforms, poles on the unit circle.
> [[exams/midterm-1/past-exams/spring-2021|SP2021 #1(e), #5]] · [[exams/midterm-1/past-exams/fall-2019|FA2019 #1(g)]] · [[exams/midterm-1/past-exams/fall-2025|FA2025 #5(a), #5(c), #8(b)]] · [[exams/midterm-1/past-exams/fall-2024|FA2024 #1(e)]] · [[exams/midterm-1/past-exams/spring-2025|SP2025 #6]] · [[homework/hw1|HW1]] #1, #3, #4

## Related

[[concepts/complex-exponential|complex exponential]] · [[concepts/kronecker-delta|Kronecker delta]] · [[concepts/unit-step|unit step]] · [[concepts/discrete-time-signal|discrete-time signal]] · [[0-toolkit/01-complex-numbers|complex numbers]] · [[0-toolkit/03-sketching-and-transforming-signals|sketching signals]] · unit: [[1-signals-and-systems/index|Unit 1]]

### Sources for this page

Snyder, Lecture 2 notes (§1.1–1.4, §2, Figs. 1–2) and slides with in-class annotations (Aug 26, 2026); HW1 #1, #3–4; past exams above.
