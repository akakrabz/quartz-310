---
title: "Complex exponential"
description: "x[n] = B aⁿ with complex a = r e^{jω}: complex numbers in brief (rectangular, polar, quadrant rule, Euler), growth vs. decay set by r, and how every exponential becomes a pole."
tags: [concept, signals, complex-numbers, midterm-1]
aliases: ["complex exponential", "Euler's formula", "Euler's identities", "complex sinusoid", "exponential signal", "polar form", "complex number", "sinusoid", "principal angle", "magnitude and phase"]
---

*Lecture 2 (Wed Aug 26) §1–2 · [[homework/hw1|HW1]] #4 · [[homework/hw4|HW4]] #3d · families: [[problems/z-transform-with-roc|z-transform with ROC]], [[problems/unbounded-outputs-and-pole-matching|Unbounded outputs and pole matching]] · long version of the arithmetic: [[0-toolkit/01-complex-numbers|toolkit]]*

> [!abstract] In one breath
> - $x = a + jb = Re^{j\theta}$: add in rectangular form, multiply and divide in polar; Euler converts. Phase needs the quadrant rule; angles repeat every $2\pi$.
> - Exponential signal $Ba^n$ with $a = re^{j\omega}$: $r$ sets growth or decay, $\omega$ the radians per sample.
> - Every exponential becomes a pole at $z = a$; a real sinusoid is two exponentials.

## 1. Complex numbers in brief

> [!key] Rectangular and polar form (Lecture 2, eqs. 1–2, 6–10)
> $$
> \begin{gathered}
> x = a + jb = R\,e^{j\theta}, \qquad a = \operatorname{Re}\{x\},\ b = \operatorname{Im}\{x\},\ j = \sqrt{-1};\\
> x^* = a - jb = R\,e^{-j\theta}.
> \end{gathered}
> $$
> $x^*x = R^2$ is always real. Add and subtract part by part; multiply by expanding, $j^2 = -1$; divide by the conjugate of the bottom (eqs. 3–5): $\dfrac{1 + j2}{3 - j} = \dfrac{(1+j2)(3+j)}{(3-j)(3+j)} = \dfrac{1 + j7}{10}$. In polar form, with $y = Se^{j\phi}$: $xy = RS\,e^{j(\theta+\phi)}$, $x/y = \dfrac{R}{S}\,e^{j(\theta-\phi)}$.

> [!key] Magnitude and phase (Lecture 2, eqs. 11–12)
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
> Real numbers have phase $0$ (positive) or $\pm\pi$ (negative). Complex plane: real part horizontal, imaginary vertical; $x^*$ mirrors $x$ across the real axis (notes Fig. 1).

<figure class="ece-fig"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 640 300" width="640" height="300" role="img" aria-label="Complex plane: x = -4 + j3 with magnitude and phase, its conjugate, and the 8th roots of unity" style="font-family:'Source Sans 3','Source Sans Pro',system-ui,sans-serif;font-size:13px"><line x1="40.0" y1="150.0" x2="338.0" y2="150.0" stroke="currentColor" stroke-width="1.1" stroke-linecap="round"/><polygon points="344.0,150.0 338.0,146.7 338.0,153.3" fill="currentColor"/><line x1="190.0" y1="270.0" x2="190.0" y2="32.0" stroke="currentColor" stroke-width="1.1" stroke-linecap="round"/><polygon points="190.0,26.0 186.7,32.0 193.3,32.0" fill="currentColor"/><text x="342.0" y="168.0" text-anchor="end" fill="currentColor" style="font-size:12px;">Re</text><text x="198.0" y="36.0" text-anchor="start" fill="currentColor" style="font-size:12px;">Im</text><line x1="86.0" y1="147.0" x2="86.0" y2="153.0" stroke="currentColor" stroke-width="1" stroke-linecap="round"/><text x="86.0" y="166.0" text-anchor="middle" fill="currentColor" style="font-size:11px;" opacity="0.8">−4</text><line x1="138.0" y1="147.0" x2="138.0" y2="153.0" stroke="currentColor" stroke-width="1" stroke-linecap="round"/><text x="138.0" y="166.0" text-anchor="middle" fill="currentColor" style="font-size:11px;" opacity="0.8">−2</text><line x1="242.0" y1="147.0" x2="242.0" y2="153.0" stroke="currentColor" stroke-width="1" stroke-linecap="round"/><text x="242.0" y="166.0" text-anchor="middle" fill="currentColor" style="font-size:11px;" opacity="0.8">2</text><line x1="294.0" y1="147.0" x2="294.0" y2="153.0" stroke="currentColor" stroke-width="1" stroke-linecap="round"/><text x="294.0" y="166.0" text-anchor="middle" fill="currentColor" style="font-size:11px;" opacity="0.8">4</text><line x1="187.0" y1="228.0" x2="193.0" y2="228.0" stroke="currentColor" stroke-width="1" stroke-linecap="round"/><text x="198.0" y="232.0" text-anchor="start" fill="currentColor" style="font-size:11px;" opacity="0.8">−3j</text><line x1="187.0" y1="72.0" x2="193.0" y2="72.0" stroke="currentColor" stroke-width="1" stroke-linecap="round"/><text x="198.0" y="76.0" text-anchor="start" fill="currentColor" style="font-size:11px;" opacity="0.8">3j</text><line x1="86.0" y1="72.0" x2="86.0" y2="150.0" stroke="currentColor" stroke-width="1" stroke-dasharray="3 3" opacity="0.6" stroke-linecap="round"/><line x1="86.0" y1="72.0" x2="190.0" y2="72.0" stroke="currentColor" stroke-width="1" stroke-dasharray="3 3" opacity="0.6" stroke-linecap="round"/><line x1="190.0" y1="150.0" x2="86.0" y2="72.0" stroke="var(--accent)" stroke-width="2.4" stroke-linecap="round"/><circle cx="86.0" cy="72.0" r="5.0" fill="var(--accent)" stroke="none" stroke-width="1.4"/><line x1="190.0" y1="150.0" x2="86.0" y2="228.0" stroke="var(--accent2)" stroke-width="1.6" stroke-dasharray="6 4" stroke-linecap="round"/><circle cx="86.0" cy="228.0" r="4.6" fill="none" stroke="var(--accent2)" stroke-width="1.8"/><text x="78.0" y="62.0" text-anchor="middle" fill="var(--accent)" style="font-size:13.5px;font-weight:600;">x = −4 + j3</text><text x="80.0" y="248.0" text-anchor="middle" fill="var(--accent2)" style="font-size:13px;font-weight:600;">x* = −4 − j3</text><text x="152.0" y="103.0" text-anchor="start" fill="var(--accent)" style="font-size:13px;">R = 5</text><path d="M220,150 A30,30 0 0 0 166.0,132.0" fill="none" stroke="currentColor" stroke-width="1.3"/><text x="220.0" y="116.0" text-anchor="start" fill="currentColor" style="font-size:12px;">θ ≈ 2.50 rad (143°)</text><text x="40.0" y="22" text-anchor="start" fill="currentColor" style="font-size:13px;font-weight:600">rectangular a + jb  ↔  polar Re<tspan dy="-6" style="font-size:10px">jθ</tspan></text><line x1="382.0" y1="156.0" x2="616.0" y2="156.0" stroke="currentColor" stroke-width="1.1" stroke-linecap="round"/><polygon points="622.0,156.0 616.0,152.7 616.0,159.3" fill="currentColor"/><line x1="500.0" y1="272.0" x2="500.0" y2="42.0" stroke="currentColor" stroke-width="1.1" stroke-linecap="round"/><polygon points="500.0,36.0 496.7,42.0 503.3,42.0" fill="currentColor"/><text x="620.0" y="174.0" text-anchor="end" fill="currentColor" style="font-size:12px;">Re</text><text x="508.0" y="46.0" text-anchor="start" fill="currentColor" style="font-size:12px;">Im</text><circle cx="500.0" cy="156.0" r="86.0" fill="none" stroke="currentColor" stroke-width="1.2" stroke-dasharray="4 4" opacity="0.7"/><circle cx="586.0" cy="156.0" r="6.0" fill="var(--accent)" stroke="none" stroke-width="1.4"/><line x1="500.0" y1="156.0" x2="560.8" y2="95.2" stroke="var(--accent2)" stroke-width="1" stroke-dasharray="3 3" opacity="0.7" stroke-linecap="round"/><circle cx="560.8" cy="95.2" r="5.5" fill="none" stroke="var(--accent2)" stroke-width="2"/><circle cx="500.0" cy="70.0" r="6.0" fill="var(--accent)" stroke="none" stroke-width="1.4"/><line x1="500.0" y1="156.0" x2="439.2" y2="95.2" stroke="var(--accent2)" stroke-width="1" stroke-dasharray="3 3" opacity="0.7" stroke-linecap="round"/><circle cx="439.2" cy="95.2" r="5.5" fill="none" stroke="var(--accent2)" stroke-width="2"/><circle cx="414.0" cy="156.0" r="6.0" fill="var(--accent)" stroke="none" stroke-width="1.4"/><line x1="500.0" y1="156.0" x2="439.2" y2="216.8" stroke="var(--accent2)" stroke-width="1" stroke-dasharray="3 3" opacity="0.7" stroke-linecap="round"/><circle cx="439.2" cy="216.8" r="5.5" fill="none" stroke="var(--accent2)" stroke-width="2"/><circle cx="500.0" cy="242.0" r="6.0" fill="var(--accent)" stroke="none" stroke-width="1.4"/><line x1="500.0" y1="156.0" x2="560.8" y2="216.8" stroke="var(--accent2)" stroke-width="1" stroke-dasharray="3 3" opacity="0.7" stroke-linecap="round"/><circle cx="560.8" cy="216.8" r="5.5" fill="none" stroke="var(--accent2)" stroke-width="2"/><text x="596.0" y="148.0" text-anchor="start" fill="currentColor" style="font-size:14px;font-family:'STIX Two Math','Latin Modern Math','Cambria Math','Times New Roman',serif;font-style:italic;font-weight:600;">1</text><text x="510.0" y="66.0" text-anchor="start" fill="currentColor" style="font-size:14px;font-family:'STIX Two Math','Latin Modern Math','Cambria Math','Times New Roman',serif;font-style:italic;font-weight:600;">j</text><text x="402.0" y="148.0" text-anchor="end" fill="currentColor" style="font-size:14px;font-family:'STIX Two Math','Latin Modern Math','Cambria Math','Times New Roman',serif;font-style:italic;font-weight:600;">−1</text><text x="510.0" y="258.0" text-anchor="start" fill="currentColor" style="font-size:14px;font-family:'STIX Two Math','Latin Modern Math','Cambria Math','Times New Roman',serif;font-style:italic;font-weight:600;">−j</text><path d="M534,156 A34,34 0 0 0 524.0,132.0" fill="none" stroke="currentColor" stroke-width="1.2"/><text x="540.0" y="146.0" text-anchor="start" fill="currentColor" style="font-size:11.5px;font-family:'STIX Two Math','Latin Modern Math','Cambria Math','Times New Roman',serif;font-style:italic;">π/4</text><text x="382.0" y="22" text-anchor="start" fill="currentColor" style="font-size:13px;font-weight:600">8th roots of unity e<tspan dy="-6" style="font-size:10px">j2πk/8</tspan></text><circle cx="388.0" cy="280.0" r="5.5" fill="var(--accent)" stroke="none" stroke-width="1.4"/><text x="398.0" y="284.0" text-anchor="start" fill="currentColor" style="font-size:12.5px;">z⁴ = 1</text><circle cx="506.0" cy="280.0" r="5.0" fill="none" stroke="var(--accent2)" stroke-width="2"/><text x="516.0" y="284.0" text-anchor="start" fill="currentColor" style="font-size:12.5px;">z⁴ = −1  (HW1 #4)</text></svg><figcaption><strong>Left: x = −4 + j3 = 5e<sup>jθ</sup> with θ ≈ 2.50 rad (second quadrant); x* is its mirror image.</strong> Right: the 8th roots of unity; filled dots solve z⁴ = 1, open dots solve z⁴ = −1 (HW1 #4).</figcaption></figure>

> [!question] Slides 7–8: magnitude and phase of (a) $x = -4 + j3$, (b) $y = j2$, and the special case $x = -3.10$.

> [!success]- Answers
> (a) $\lvert x\rvert = \sqrt{16 + 9} = 5$; $a < 0$, $b \ge 0$: $\angle x = \tan^{-1}\!\big(\tfrac{3}{-4}\big) + \pi \approx 2.50$ rad $\approx 143.1°$, so $x = 5e^{j2.50}$.
> (b) $\lvert y\rvert = 2$, $\angle y = \tfrac{\pi}{2}$: $y = 2e^{j\pi/2}$.
> Special case: $-3.10 = 3.10\,e^{\pm j\pi}$: magnitude $3.10$, phase $\pm\pi$.

> [!key] Principal angle (Lecture 2, eq. 13)
> $$
> Re^{j\theta} = Re^{j(\theta_p + 2\pi k)}, \qquad k \in \mathbb{Z},
> $$
> $\theta_p \in [-\pi, \pi]$ (or $[0, 2\pi]$; conventions vary). $e^{j\pi/3}$ and $e^{j7\pi/3}$ are the same point, $\theta_p = \pi/3$; frequencies $\omega$ and $\omega+2\pi$ give identical sequences, and a sampled sinusoid is periodic only for rational $\omega_0/2\pi$ ([[concepts/periodic-signals|periodic signals]]).

> [!key] Euler (Lecture 2, eqs. 14–20)
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

Beyond the notes: roots of $z^N = c$ and geometric sums are in the toolkit ([[0-toolkit/01-complex-numbers|complex numbers]], [[0-toolkit/02-geometric-series|geometric series]]). [[homework/hw1|HW1]] #4: $z^4 = 1$ gives $1, j, -1, -j$; $z^4 = -1$ gives $\dfrac{\pm1 \pm j}{\sqrt2}$ (figure, right).

## 2. Sinusoids and exponential signals

> [!key] Sinusoids and exponentials (Lecture 2, eqs. 23–24)
> $$
> x[n] = A\sin(\omega_0 n + \theta), \quad A, \omega_0, \theta \in \mathbb{R}; \qquad x[n] = B\,a^n, \quad B, a \in \mathbb{C}.
> $$
> $\omega_0$ in radians per sample. Writing $a=r\,e^{j\omega}$,
> $$
> x[n]=B\,r^n\,e^{j\omega n} = B\,r^n\big(\cos(\omega n) + j\sin(\omega n)\big):\qquad \lvert x[n]\rvert=\lvert B\rvert\,r^n
> $$
> decays if $r<1$, stays on the unit circle if $r=1$, grows if $r>1$, while the angle advances $\omega$ radians per sample. Notes Fig. 2: $\cos(\frac{\pi}{10}n - \frac{\pi}{3})$, $2(-\tfrac34)^n$.

## 3. Why it matters for the z-transform

$a^nu[n]\leftrightarrow\dfrac{1}{1-a\,z^{-1}}$, ROC $\lvert z\rvert>\lvert a\rvert$: each exponential becomes **a pole at $z=a$**; its radius $r$ is the growth or decay rate and its angle is the frequency. A real sinusoid is two exponentials, so $\cos(\omega_0n)u[n]$ has two poles $e^{\pm j\omega_0}$. Exponentials are also the [[concepts/eigenfunctions-of-lti-systems|eigenfunctions of LTI systems]].

> [!recipe] Convert to exponentials first
> Before transforming or pole-matching a sinusoid, rewrite it with Euler. [[exams/midterm-1/past-exams/fall-2025|FA2025 #5c]]:
> $$
> \cos^2\!\big(\tfrac{\pi}{4}n\big)=\tfrac12+\tfrac12\cos\big(\tfrac{\pi}{2}n\big)=\tfrac12+\tfrac14e^{j\pi n/2}+\tfrac14e^{-j\pi n/2},
> $$
> so $\cos^2(\frac{\pi}{4}n)\,u[n]$ has poles at $1,\ j,\ -j$ and ROC $\lvert z\rvert>1$. Other conversions to know: $j^n=e^{j\pi n/2}$, $(-1)^n=e^{j\pi n}=\cos(\pi n)$, and ([[homework/hw1|HW1]] #4) $z^4=1\Rightarrow z=e^{j\pi k/2}=1,j,-1,-j$ while $z^4=-1=e^{j\pi}\Rightarrow z=e^{j(\pi/4+k\pi/2)}$.

## 4. In Unit 3

The everlasting $e^{j\omega_0n}$ has no z-transform, but it has a DTFT once Dirac impulses are allowed: $e^{j\omega_0n}\leftrightarrow2\pi\delta(\omega-\omega_0)$ on each period, i.e. $2\pi\sum_k\delta(\omega-\omega_0-2\pi k)$, and by Euler $\cos(\omega_0n)\leftrightarrow\pi\big[\delta(\omega-\omega_0)+\delta(\omega+\omega_0)\big]$ ([[3-fourier-analysis/14-dtft-properties|Lecture 14]], [[concepts/dtft-pairs|DTFT pairs]]). One frequency is one spike per period; a real sinusoid is two. Because $\omega$ and $\omega+2\pi$ give the same samples, every DTFT is $2\pi$-periodic and is drawn on $[-\pi,\pi]$ ([[concepts/dtft|DTFT]]).

> [!trap]
> - **Mind the quadrant and the sign**: $-4 + j3$ and $4 - j3$ share $b/a = -\tfrac34$ (phases $2.50$ and $-0.64$ rad); $\angle(-1-j)=-\frac{3\pi}{4}$ although $\tan^{-1}(\frac{-1}{-1})=\frac{\pi}{4}$; a magnitude is never negative, $-3.10 = 3.10\,e^{\pm j\pi}$. Sketch the point first.
> - **Read the exponent literally.** In [[exams/midterm-1/past-exams/fall-2025|FA2025 #8b]] the pole $e^{j2/3}$ sits at $2/3$ rad $\approx38.2^\circ$, not at $2\pi/3=120^\circ$; that is why $\cos(\frac{2\pi}{3}n)u[n]$ gives a *bounded* output there (key: False).
> - **Only $r$ sets the size**: $\lvert e^{j\theta}\rvert=1$ for every real $\theta$, but $\lvert0.8+0.8j\rvert=0.8\sqrt2\approx1.13>1$, so the gain $(0.8+0.8j)^n$ grows and $y=(0.8+0.8j)^nx[n]$ is unstable ([[exams/midterm-1/past-exams/spring-2021|SP2021 #3]]).
> - **Sine needs the $2j$**: $\sin\theta=(e^{j\theta}-e^{-j\theta})/(2j)$; dropping the $j$ flips signs and phases.
> - **A real cosine carries both frequencies**: $\cos(\frac{\pi}{4}n)u[n]$ blows up a system with a unit-circle pole at $e^{j\pi/4}$ (True), while $e^{-j\pi n/4}u[n]$ alone does not (False) ([[exams/midterm-1/past-exams/spring-2025|SP2025 #6]]).
> - $e^{j\omega n}$ **for all $n$** has no z-transform: its ROC is empty ([[exams/midterm-1/past-exams/spring-2025|SP2025 #1c]] T).

> [!exam] No calculator
> Know $e^{j\pi/4} = \frac{1+j}{\sqrt2}$, $e^{j\pi/3} = \frac12 + j\frac{\sqrt3}{2}$, $e^{j2\pi/3} = -\frac12 + j\frac{\sqrt3}{2}$. Tested via Euler inside z-transforms and poles on the unit circle.
> [[exams/midterm-1/past-exams/fall-2025|FA2025 #5a, #5c, #8b]] · [[exams/midterm-1/past-exams/spring-2025|SP2025 #1c, #6]] · [[exams/midterm-1/past-exams/spring-2021|SP2021 #3, #5]] · [[exams/midterm-1/past-exams/fall-2024|FA2024 #1e]] · [[homework/hw1|HW1]] #1, #3, #4

**Where it appears:** [[1-signals-and-systems/02-complex-numbers-and-elementary-signals|Lecture 2]] §1–2, [[2-z-transform/06-the-z-transform|Lecture 6]] §1 (eigenfunctions), [[2-z-transform/11-bibo-stability-and-causality|Lecture 11]] §1.2.1 (unit-circle poles); [[homework/hw1|HW1]] #4, [[homework/hw4|HW4]] #3d (poles $e^{-j\pi/4}$, $e^{j3\pi/4}$); [[0-toolkit/01-complex-numbers|toolkit]]; families [[problems/z-transform-with-roc|z-transform with ROC]] and [[problems/unbounded-outputs-and-pole-matching|unbounded outputs and pole matching]].

## Related
[[concepts/eigenfunctions-of-lti-systems|eigenfunctions]] · [[concepts/poles-and-zeros|poles and zeros]] · [[concepts/periodic-signals|periodic signals]] · [[concepts/z-transform-pairs|z-transform pairs]] · [[concepts/marginal-stability|marginal stability]] · [[concepts/discrete-time-signal|discrete-time signal]] · [[0-toolkit/01-complex-numbers|complex numbers (toolkit)]]

### Sources for this page
Lecture 2 §1.1–1.4 (eqs. 1–20, Fig. 1) and §2 (eqs. 23–24, Fig. 2), slides 7–8 and 12 with in-class annotations; Lecture 6 §1; HW1 #4; FA2025 #5c and #8b, SP2025 #6 and #1c, SP2021 #3 (annotated "1.13 e^{jπ/4}").
