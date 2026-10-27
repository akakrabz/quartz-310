---
title: "Marginal stability"
description: "Simple poles on the unit circle: h[n] bounded but not absolutely summable, so unstable; only inputs with a matching unit-circle pole (double pole, resonance) give unbounded outputs."
tags: [concept, stability, z-transform, roc]
aliases: ["marginally stable", "marginal stability", "pole matching", "resonance"]
---

*Lecture 11 (Fri Sep 18) §1.2–1.2.1 · [[homework/hw4|HW4]] #3(c)–(d) · family: [[problems/unbounded-outputs-and-pole-matching|unbounded outputs and pole matching]]*

> [!abstract] In one breath
> - A pole outside the unit circle: $h$ unbounded, almost every bounded input gives an unbounded output; only an input zero on that pole helps.
> - A simple pole on the unit circle (ROC open on $\lvert z\rvert=1$): still unstable, but $h$ bounded; only inputs that **resonate** blow up.
> - Unbounded iff an input pole lands exactly on an uncancelled unit-circle pole of $H$: double pole, $y\sim n\,e^{j\omega_0n}$.

## 1. Unstable inputs (Lecture 11 §1.2)

**Pole outside the unit circle** (slides 12–13): $h[n] = 3^n u[n]$, $H(z) = \dfrac{1}{1-3z^{-1}}$, $\lvert z\rvert > 3$. $\delta[n]$, $u[n]$, $(\tfrac13)^n u[n]$ — almost any bounded input — give unbounded outputs. Only a zero of $X(z)$ at $3$ helps ([[concepts/pole-zero-cancellation|pole-zero cancellation]]):
$$
\begin{aligned}
X(z) &= 1 - 3z^{-1} \;\leftrightarrow\; x[n] = \delta[n] - 3\delta[n-1] \\
\quad\Longrightarrow\quad Y(z) &= \frac{1-3z^{-1}}{1-3z^{-1}} = 1,\qquad y[n] = \delta[n]
\end{aligned}
$$
(and any scaled or shifted copy).

**Pole on the unit circle** (slide 14): $h[n] = (-1)^n u[n]$, $H(z) = \dfrac{1}{1+z^{-1}}$, $\lvert z\rvert > 1$: unstable but $h$ bounded. $\delta[n] \to (-1)^n u[n]$ and $u[n] \to \tfrac12(1 + (-1)^n)u[n]$ are bounded; $x[n] = (-1)^n u[n]$ gives $y[n] = (n+1)(-1)^n u[n]$.

## 2. Marginal stability (Lecture 11 §1.2.1)

> [!key] Marginal stability (slide 15)
> ROC of $H(z)$ **open on the unit circle** (touches $\lvert z\rvert = 1$ without containing it, e.g. $\lvert z\rvert > 1$ causal); causal: no poles outside, at least one **simple** pole **on** $\lvert z\rvert=1$.
> - **Not BIBO stable:** $h$ bounded (undamped $e^{j\omega n}u[n]$ terms, cosines/sines for conjugate pairs), $\sum_n \lvert h[n]\rvert = \infty$ ($h=u[n]$).
> - Only inputs that **resonate** give unbounded outputs: $Y$ gets a double pole,
> $$
> \frac{1}{(1-e^{j\omega}z^{-1})^2} \leftrightarrow (n+1)e^{j\omega n}u[n],\quad \lvert z\rvert>1 .
> $$

Slides 16–17 (eqs. 21–23): $h[n] = a^n u[n]$, $\lvert a\rvert = 1$; input $x[n] = b^n u[n]$:

- $\lvert b\rvert > 1$: input unbounded; not a BIBO test input.
- $\lvert b\rvert < 1$: $Y(z) = \dfrac{1}{(1-bz^{-1})(1-az^{-1})} = \dfrac{A_1}{1-bz^{-1}} + \dfrac{A_2}{1-az^{-1}}$, $y[n] = A_1 b^n u[n] + A_2 a^n u[n]$: **bounded**.
- $\lvert b\rvert = 1$, $a = e^{j\theta}$, $b = e^{j\phi}$:
$$
\begin{aligned}
y[n] &= \sum_{k=0}^{n} e^{j\theta k}e^{j\phi(n-k)} \\
&= e^{j\phi n}\sum_{k=0}^{n} e^{j(\theta-\phi)k} \\
&= \begin{cases} e^{j\phi n}\,(n+1)\,u[n], & \theta = \phi \quad\text{(unbounded)}\\[4pt]
e^{j\phi n}\,\dfrac{1-e^{j(\theta-\phi)(n+1)}}{1-e^{j(\theta-\phi)}}\,u[n], & \theta \ne \phi \quad\text{(bounded by } \tfrac{2}{\lvert 1-e^{j(\theta-\phi)}\rvert}\text{)} \end{cases}
\end{aligned}
$$

Notes example ($a = b = 1$, the accumulator $H(z)=\frac{1}{1-z^{-1}}$): $h = u[n]$, $x = u[n]$ gives $y = (n+1)u[n]$, unbounded; $x = c^n u[n]$, $\lvert c\rvert < 1$, gives the bounded $\sum_{k=0}^n c^k$. $x=(-1)^nu[n]$ or $(\frac12)^nu[n]$: bounded. $x=\delta[n]-\delta[n-1]$: $y=\delta[n]$.

> [!derivation]- Lecture exercise: a double pole on the unit circle is an unbounded output (eqs. 24–28)
> From $n\,a^n u[n] \leftrightarrow \dfrac{a z^{-1}}{(1-az^{-1})^2}$:
> $$
> \frac{1}{(1-az^{-1})^2} = \sum_{n=0}^{\infty}(n+1)\,a^n z^{-n} \;\leftrightarrow\; (n+1)\,a^n u[n], \qquad \lvert z\rvert > \lvert a\rvert .
> $$
> $\lvert a\rvert = 1$: $\lvert y[n]\rvert = n+1 \to \infty$. $\lvert a\rvert < 1$: $(n+1)a^n \to 0$. Matching is dangerous **only on the unit circle**.

## 3. Pole matching

> [!key] Pole matching
> A marginally stable system gives an unbounded output **iff the input's z-transform has a pole exactly on one of the system's uncancelled unit-circle poles**: $Y = HX$ then has a double pole on $\lvert z\rvert = 1$ and $y[n]$ contains $n\,e^{j\omega_0 n}$.

> [!recipe] Which bounded inputs give unbounded outputs?
> 1. Factor $H$, cancel, list poles **with angles**. Causal with an uncancelled $\lvert p\rvert > 1$: $h$ unbounded, almost every input fails.
> 2. Input poles: $a^n u[n] \to a$; $u[n] \to 1$; $(-1)^n u[n] \to -1$; $j^n u[n] \to j$; $\cos(\omega_0 n)u[n]$, $\sin(\omega_0 n)u[n] \to e^{\pm j\omega_0}$. Finite-length inputs: no finite poles, never match.
> 3. Cancel input zeros against system poles. **Unbounded iff an input pole sits on a unit-circle pole of $H$** (not cancelled). One of $e^{\pm j\omega_0}$ is enough.
> 4. Compare angles exactly: $e^{j2/3}$ ($\tfrac23$ rad) is not $e^{j2\pi/3}$.

> [!question] Lecture 11, slide 18 — which inputs give an unbounded output?
> Causal $H(z) = \dfrac{1}{(1-jz^{-1})(1+z^{-1})(1-\frac23 z^{-1})}$, $\lvert z\rvert > 1$. (1) $(-1)^n u[n]$ (2) $u[n]$ (3) $e^{j\frac{\pi}{2}n}u[n]$ (4) $e^{-j\frac{\pi}{2}n}u[n]$ (5) $(\tfrac23)^n u[n]$ (6) $\sin(-\tfrac{\pi}{2}n)u[n]$ (7) $\cos(\tfrac{\pi}{2}n)u[n]$ (8) $\sin(\tfrac{2\pi}{3}n)u[n]$

> [!success]- Answer
> Poles $j$, $-1$ on the unit circle, $\tfrac23$ inside: marginally stable.
> **Unbounded: (1), (3), (6), (7).** (1) pole $-1$; (3) pole $j$; (6) $\sin(-\tfrac{\pi}{2}n) = -\tfrac{1}{2j}\bigl(e^{j\frac{\pi}{2}n} - e^{-j\frac{\pi}{2}n}\bigr)$ and (7) contain $e^{j\frac{\pi}{2}n}$.
> **Bounded: (2), (4), (5), (8).** Poles $1$ and $e^{\pm j2\pi/3}$ are not system poles; $-j$ is not a pole of this $H$ (complex coefficients: no conjugate pairs needed); (5) double pole at $\tfrac23$ gives a decaying $n(\tfrac23)^n u[n]$.

<figure class="ece-fig"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 680 372" width="680" height="372" role="img" style="font-family:'Source Sans 3','Source Sans Pro',system-ui,sans-serif;font-size:14px;max-width:100%;height:auto"><text x="340.0" y="22.0" text-anchor="middle" fill="currentColor" style="font-size:14px;font-weight:600;">Causal H(z) = 1 / [(1 − jz⁻¹)(1 + z⁻¹)(1 − ⅔z⁻¹)],  ROC |z| &gt; 1  (marginally stable)</text><path d="M287.00,200.00 A112.00,112.00 0 1,0 63.00,200.00 A112.00,112.00 0 1,0 287.00,200.00 Z" fill="none" stroke="currentColor" stroke-width="1.8" stroke-dasharray="6 4"/><line x1="27.0" y1="200.0" x2="323.0" y2="200.0" stroke="currentColor" stroke-width="1.0" opacity="0.7" stroke-linecap="round"/><line x1="175.0" y1="52.0" x2="175.0" y2="348.0" stroke="currentColor" stroke-width="1.0" opacity="0.7" stroke-linecap="round"/><text x="321.0" y="215.0" text-anchor="end" fill="var(--muted)" style="font-size:11px;">Re</text><text x="181.0" y="64.0" text-anchor="start" fill="var(--muted)" style="font-size:11px;">Im</text><text x="263.9" y="296.9" text-anchor="start" fill="currentColor" style="font-size:12px;">|z| = 1</text><circle cx="63.0" cy="200.0" r="7.0" fill="none" stroke="var(--accent)" stroke-width="2.0"/><text x="50.0" y="188.0" text-anchor="end" fill="var(--accent)" style="font-size:13px;font-weight:600;">1</text><circle cx="287.0" cy="200.0" r="7.0" fill="none" stroke="var(--accent)" stroke-width="2.0"/><text x="300.0" y="188.0" text-anchor="start" fill="var(--accent)" style="font-size:13px;font-weight:600;">2</text><circle cx="175.0" cy="88.0" r="7.0" fill="none" stroke="var(--accent)" stroke-width="2.0"/><text x="190.0" y="76.0" text-anchor="start" fill="var(--accent)" style="font-size:13px;font-weight:600;">3, 6, 7</text><circle cx="175.0" cy="312.0" r="7.0" fill="none" stroke="var(--accent)" stroke-width="2.0"/><text x="190.0" y="332.0" text-anchor="start" fill="var(--accent)" style="font-size:13px;font-weight:600;">4, 6, 7</text><circle cx="249.7" cy="200.0" r="7.0" fill="none" stroke="var(--accent)" stroke-width="2.0"/><text x="249.7" y="226.0" text-anchor="middle" fill="var(--accent)" style="font-size:13px;font-weight:600;">5</text><circle cx="119.0" cy="103.0" r="7.0" fill="none" stroke="var(--accent)" stroke-width="2.0"/><text x="106.0" y="93.0" text-anchor="end" fill="var(--accent)" style="font-size:13px;font-weight:600;">8</text><circle cx="119.0" cy="297.0" r="7.0" fill="none" stroke="var(--accent)" stroke-width="2.0"/><text x="106.0" y="317.0" text-anchor="end" fill="var(--accent)" style="font-size:13px;font-weight:600;">8</text><line x1="168.0" y1="81.0" x2="182.0" y2="95.0" stroke="var(--hi)" stroke-width="2.4" stroke-linecap="round"/><line x1="168.0" y1="95.0" x2="182.0" y2="81.0" stroke="var(--hi)" stroke-width="2.4" stroke-linecap="round"/><line x1="56.0" y1="193.0" x2="70.0" y2="207.0" stroke="var(--hi)" stroke-width="2.4" stroke-linecap="round"/><line x1="56.0" y1="207.0" x2="70.0" y2="193.0" stroke="var(--hi)" stroke-width="2.4" stroke-linecap="round"/><line x1="242.7" y1="193.0" x2="256.7" y2="207.0" stroke="var(--hi)" stroke-width="2.4" stroke-linecap="round"/><line x1="242.7" y1="207.0" x2="256.7" y2="193.0" stroke="var(--hi)" stroke-width="2.4" stroke-linecap="round"/><circle cx="175.0" cy="88.0" r="15.0" fill="none" stroke="var(--hi)" stroke-width="2.2" stroke-dasharray="3 3"/><circle cx="63.0" cy="200.0" r="15.0" fill="none" stroke="var(--hi)" stroke-width="2.2" stroke-dasharray="3 3"/><line x1="372.0" y1="52.0" x2="384.0" y2="64.0" stroke="var(--hi)" stroke-width="2.4" stroke-linecap="round"/><line x1="372.0" y1="64.0" x2="384.0" y2="52.0" stroke="var(--hi)" stroke-width="2.4" stroke-linecap="round"/><text x="392.0" y="63.0" text-anchor="start" fill="currentColor" style="font-size:13px;">system pole</text><circle cx="522.0" cy="58.0" r="7.0" fill="none" stroke="var(--accent)" stroke-width="2.0"/><text x="536.0" y="63.0" text-anchor="start" fill="currentColor" style="font-size:13px;">input pole (input #)</text><text x="372.0" y="98.0" text-anchor="start" fill="var(--hi)" style="font-size:12.5px;font-weight:700;">unbounded</text><text x="454.0" y="98.0" text-anchor="start" fill="currentColor" style="font-size:13px;">#1  (−1)<tspan baseline-shift="super" font-size="10">n</tspan>u[n]</text><text x="454.0" y="114.0" text-anchor="start" fill="var(--muted)" style="font-size:11.5px;">pole −1: a system pole on |z| = 1</text><text x="372.0" y="136.0" text-anchor="start" fill="var(--hi)" style="font-size:12.5px;font-weight:700;">unbounded</text><text x="454.0" y="136.0" text-anchor="start" fill="currentColor" style="font-size:13px;">#3  e<tspan baseline-shift="super" font-size="10">jπn/2</tspan>u[n]</text><text x="454.0" y="152.0" text-anchor="start" fill="var(--muted)" style="font-size:11.5px;">pole j: a system pole on |z| = 1</text><text x="372.0" y="174.0" text-anchor="start" fill="var(--hi)" style="font-size:12.5px;font-weight:700;">unbounded</text><text x="454.0" y="174.0" text-anchor="start" fill="currentColor" style="font-size:13px;">#6, 7  sin(−πn/2), cos(πn/2)</text><text x="454.0" y="190.0" text-anchor="start" fill="var(--muted)" style="font-size:11.5px;">poles ±j: the j half matches</text><text x="372.0" y="212.0" text-anchor="start" fill="var(--muted)" style="font-size:12.5px;font-weight:700;">bounded</text><text x="454.0" y="212.0" text-anchor="start" fill="currentColor" style="font-size:13px;">#2  u[n]</text><text x="454.0" y="228.0" text-anchor="start" fill="var(--muted)" style="font-size:11.5px;">pole 1: no system pole there</text><text x="372.0" y="250.0" text-anchor="start" fill="var(--muted)" style="font-size:12.5px;font-weight:700;">bounded</text><text x="454.0" y="250.0" text-anchor="start" fill="currentColor" style="font-size:13px;">#4  e<tspan baseline-shift="super" font-size="10">−jπn/2</tspan>u[n]</text><text x="454.0" y="266.0" text-anchor="start" fill="var(--muted)" style="font-size:11.5px;">pole −j: not a system pole</text><text x="372.0" y="288.0" text-anchor="start" fill="var(--muted)" style="font-size:12.5px;font-weight:700;">bounded</text><text x="454.0" y="288.0" text-anchor="start" fill="currentColor" style="font-size:13px;">#8  sin(2πn/3)u[n]</text><text x="454.0" y="304.0" text-anchor="start" fill="var(--muted)" style="font-size:11.5px;">poles e<tspan baseline-shift="super" font-size="10">±j2π/3</tspan>: no match</text><text x="372.0" y="326.0" text-anchor="start" fill="var(--muted)" style="font-size:12.5px;font-weight:700;">bounded</text><text x="454.0" y="326.0" text-anchor="start" fill="currentColor" style="font-size:13px;">#5  (⅔)<tspan baseline-shift="super" font-size="10">n</tspan>u[n]</text><text x="454.0" y="342.0" text-anchor="start" fill="var(--muted)" style="font-size:11.5px;">matches ⅔, but inside: n(⅔)<tspan baseline-shift="super" font-size="10">n</tspan> → 0</text></svg><figcaption><strong>Pole matching (slide 18).</strong> An input gives an unbounded output exactly when one of its poles (circles, labelled by input number) lands on a system pole on the unit circle.</figcaption></figure>

> [!question] FA2025 #8(b): causal $H$ with poles $\tfrac34$, $j$, $e^{j2/3}$. Which of $j^nu[n]$, $\sin(\tfrac{\pi}{2}n)u[n]$, $\cos(\tfrac{2\pi}{3}n)u[n]$, $\delta[n]-\tfrac34\delta[n-1]$, $(\tfrac23)^nu[n]$ give unbounded outputs?

> [!success]- Answer
> $j^nu[n]$ and $\sin(\tfrac{\pi}{2}n)u[n]$ (pole $j$ doubled). $\cos(\tfrac{2\pi}{3}n)u[n]$ has poles $e^{\pm j2\pi/3}$ at $\pm120°$, not at $\tfrac23$ rad $\approx 38.2°$: bounded. $\delta[n]-\tfrac34\delta[n-1]$ cancels $\tfrac34$; $(\tfrac23)^nu[n]$ adds a pole inside: both bounded.

<figure class="ece-fig"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 760 330" width="760" height="330" role="img" style="font-family:'Source Sans 3','Source Sans Pro',system-ui,sans-serif;font-size:14px"><defs><marker id="ahpm" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="context-stroke"/></marker></defs><line x1="50.0" y1="165.0" x2="350.0" y2="165.0" stroke="currentColor" stroke-width="1.1" opacity="0.8" stroke-linecap="round"/><line x1="200.0" y1="15.0" x2="200.0" y2="315.0" stroke="currentColor" stroke-width="1.1" opacity="0.8" stroke-linecap="round"/><circle cx="200.0" cy="165.0" r="120.0" fill="none" stroke="currentColor" stroke-width="1.3" stroke-dasharray="5 4"/><text x="350.0" y="159.0" text-anchor="end" fill="var(--muted)" style="font-size:12px;">Re</text><text x="206.0" y="27.0" text-anchor="start" fill="var(--muted)" style="font-size:12px;">Im</text><line x1="283.0" y1="158.0" x2="297.0" y2="172.0" stroke="var(--hi)" stroke-width="2.4" stroke-linecap="round"/><line x1="283.0" y1="172.0" x2="297.0" y2="158.0" stroke="var(--hi)" stroke-width="2.4" stroke-linecap="round"/><line x1="193.0" y1="38.0" x2="207.0" y2="52.0" stroke="var(--hi)" stroke-width="2.4" stroke-linecap="round"/><line x1="193.0" y1="52.0" x2="207.0" y2="38.0" stroke="var(--hi)" stroke-width="2.4" stroke-linecap="round"/><line x1="287.3" y1="83.8" x2="301.3" y2="97.8" stroke="var(--hi)" stroke-width="2.4" stroke-linecap="round"/><line x1="287.3" y1="97.8" x2="301.3" y2="83.8" stroke="var(--hi)" stroke-width="2.4" stroke-linecap="round"/><rect x="134.0" y="55.1" width="12" height="12" fill="none" stroke="var(--accent2)" stroke-width="2"/><rect x="134.0" y="262.9" width="12" height="12" fill="none" stroke="var(--accent2)" stroke-width="2"/><circle cx="200.0" cy="45.0" r="12.0" fill="none" stroke="var(--accent)" stroke-width="2"/><path d="M242.0,165.0 A42,42 0 0,0 233.0,139.0" fill="none" stroke="var(--hi)" stroke-width="1.4"/><text x="250.0" y="154.0" text-anchor="start" fill="var(--hi)" style="font-size:12px;">2/3 rad</text><path d="M226.0,165.0 A26,26 0 0,0 187.0,142.5" fill="none" stroke="var(--accent2)" stroke-width="1.4"/><text x="170.0" y="135.0" text-anchor="end" fill="var(--accent2)" style="font-size:12px;">2π/3</text><text x="306.3" y="82.8" text-anchor="start" fill="var(--hi)" style="font-size:14px;font-family:'STIX Two Math','Latin Modern Math','Cambria Math','Times New Roman',serif;font-style:italic;">e<tspan dy="-6" font-size="10">j2/3</tspan></text><text x="218.0" y="33.0" text-anchor="start" fill="var(--hi)" style="font-size:15px;font-family:'STIX Two Math','Latin Modern Math','Cambria Math','Times New Roman',serif;font-style:italic;">j</text><text x="290.0" y="187.0" text-anchor="middle" fill="var(--hi)" style="font-size:14px;">¾</text><text x="128.0" y="51.1" text-anchor="end" fill="var(--accent2)" style="font-size:14px;font-family:'STIX Two Math','Latin Modern Math','Cambria Math','Times New Roman',serif;font-style:italic;">e<tspan dy="-6" font-size="10">j2π/3</tspan></text><text x="128.0" y="290.9" text-anchor="end" fill="var(--accent2)" style="font-size:14px;font-family:'STIX Two Math','Latin Modern Math','Cambria Math','Times New Roman',serif;font-style:italic;">e<tspan dy="-6" font-size="10">−j2π/3</tspan></text><line x1="382.0" y1="54.0" x2="394.0" y2="66.0" stroke="var(--hi)" stroke-width="2.4" stroke-linecap="round"/><line x1="382.0" y1="66.0" x2="394.0" y2="54.0" stroke="var(--hi)" stroke-width="2.4" stroke-linecap="round"/><text x="406.0" y="65.0" text-anchor="start" fill="currentColor" style="font-size:13px;">poles of H(z): ¾, j, e<tspan dy="-6" font-size="10">j2/3</tspan></text><circle cx="388.0" cy="94.0" r="10.0" fill="none" stroke="var(--accent)" stroke-width="2"/><text x="406.0" y="99.0" text-anchor="start" fill="currentColor" style="font-size:13px;">j<tspan dy="-6" font-size="10">n</tspan><tspan dy="6">u[n], sin(πn/2)u[n] hit j</tspan></text><text x="406.0" y="117.0" text-anchor="start" fill="var(--accent)" style="font-size:13px;">→ double pole on |z| = 1 → unbounded</text><rect x="382.0" y="140.0" width="12" height="12" fill="none" stroke="var(--accent2)" stroke-width="2"/><text x="406.0" y="151.0" text-anchor="start" fill="currentColor" style="font-size:13px;">cos(2πn/3)u[n]: poles e<tspan dy="-6" font-size="10">±j2π/3</tspan></text><text x="406.0" y="169.0" text-anchor="start" fill="var(--accent2)" style="font-size:13px;">→ no match (120° ≠ 38.2°) → bounded</text><text x="406.0" y="205.0" text-anchor="start" fill="var(--muted)" style="font-size:13px;">δ[n] − ¾δ[n−1] cancels ¾ → bounded;</text><text x="406.0" y="223.0" text-anchor="start" fill="var(--muted)" style="font-size:13px;">(⅔)ⁿu[n] adds a pole inside → bounded</text></svg><figcaption><strong>FA2025 #8(b).</strong> The pole e<sup>j2/3</sup> sits at 2/3 rad ≈ 38.2°, not at the ±120° poles of cos(2πn/3)u[n], so that output stays bounded; jⁿu[n] and sin(πn/2)u[n] double the pole at j and grow like n.</figcaption></figure>

> [!trap]
> - Marginally stable = unstable on T/F.
> - $e^{j2/3}$ is not $e^{j2\pi/3}$ ([[exams/midterm-1/past-exams/fall-2025|FA2025 #8b]]); angles in radians vs. multiples of $\pi$.
> - A cosine resonates with a pole at **either** $e^{\pm j\omega_0}$; $e^{-j\pi n/4}u[n]$ alone does not match $e^{j\pi/4}$ ([[exams/midterm-1/past-exams/spring-2025|SP2025 #6]]).
> - A double pole **inside** the circle is harmless: $n(\frac23)^n u[n]$.
> - $\delta[n]$ breaks a system only if $h$ itself is unbounded; for poles on $\lvert z\rvert=1$ use a matching input.

> [!exam] Unbounded outputs and pole matching — 7 of 7 past exams
> Which bounded inputs give unbounded outputs; T/F on marginal stability.
> [[exams/midterm-1/past-exams/fall-2025|FA2025 #8]] · [[exams/midterm-1/past-exams/spring-2025|SP2025 #6]] · [[exams/midterm-1/past-exams/fall-2024|FA2024 #8]] · [[exams/midterm-1/past-exams/fall-2023|FA2023 #7, #8]] · [[exams/midterm-1/past-exams/spring-2023|SP2023 #7]] · [[exams/midterm-1/past-exams/spring-2021|SP2021 #5]] · [[exams/midterm-1/past-exams/fall-2019|FA2019 #10(d)]] · family: [[problems/unbounded-outputs-and-pole-matching|unbounded outputs and pole matching]] · [[exams/midterm-1/true-false-bank|T/F bank]]

**Where it appears:** [[2-z-transform/11-bibo-stability-and-causality|L11]] §1.2–1.2.1 (eqs. 19–28, slides 12–18); [[problems/unbounded-outputs-and-pole-matching|Unbounded outputs and pole matching]] (7/7 exams); [[homework/hw4|HW4]] #3(c)–(d); [[exams/midterm-1/true-false-bank|T/F bank]].

## Related
[[concepts/bibo-stability]] · [[concepts/region-of-convergence]] · [[concepts/poles-and-zeros]] · [[concepts/pole-zero-cancellation]] · [[concepts/complex-exponential]] · [[concepts/eigenfunctions-of-lti-systems]] · [[concepts/z-transform-pairs]]

### Sources for this page
Lecture 11 notes §1.2–1.2.1 (eqs. 19–28, lecture exercise), slides 12–18; FA2025 #8b, SP2025 #6, FA2023 #7, SP2021 #5 keys; HW4 #3 solutions.
