---
title: "Marginal stability"
description: "Poles on the unit circle: the impulse response stays bounded but is not absolutely summable, so the system is unstable — yet only inputs with a matching unit-circle pole (a double pole, resonance) drive the output to infinity."
tags: [concept, stability, z-transform, roc]
aliases: ["marginally stable"]
---

> [!key] Definition (Lecture 11)
> An LTI system is **marginally stable** when the ROC of $H(z)$ is bounded by the unit circle without containing it ($|z|>1$ or $|z|<1$). For a causal system: no poles outside $|z|=1$, at least one **simple** pole **on** it. (A repeated pole on the circle makes $h$ itself unbounded: $\frac{1}{(1-z^{-1})^2} \leftrightarrow (n+1)u[n]$.)
> - It is **not BIBO stable**: $h[n]$ is bounded but $\sum_n |h[n]| = \infty$ (think $h = u[n]$ or $\cos(\omega_0 n)u[n]$).
> - A bounded input gives an unbounded output **only if it has a pole at the same unit-circle location** as a pole of $H(z)$: $Y(z)=H(z)X(z)$ then has a **double pole** on $|z|=1$, i.e. a term $(n+1)e^{j\omega n}u[n]$.

**Why only matching inputs.** Take $h[n] = e^{j\omega_1 n}u[n]$ and $x[n] = e^{j\omega_2 n}u[n]$:
$$
y[n] = \sum_{k=0}^{n} e^{j\omega_1 k}e^{j\omega_2(n-k)} = e^{j\omega_2 n}\sum_{k=0}^{n} e^{j(\omega_1-\omega_2)k}
= \begin{cases} (n+1)\,e^{j\omega_2 n}, & \omega_1 = \omega_2 \ \ (\text{unbounded})\\[4pt]
e^{j\omega_2 n}\,\dfrac{1-e^{j(\omega_1-\omega_2)(n+1)}}{1-e^{j(\omega_1-\omega_2)}}, & \omega_1\neq\omega_2 \ \ (\text{bounded, oscillates}) \end{cases}
$$
The input "resonates" with the system. In the z-domain, $\frac{1}{(1-e^{j\omega}z^{-1})^2} \leftrightarrow (n+1)e^{j\omega n}u[n]$, $|z|>1$ — the [[concepts/z-transform-pairs|derived pair]] $(n+1)a^nu[n]$ with $|a|=1$.

> [!example] The accumulator $h[n] = u[n]$, $H(z) = \frac{1}{1-z^{-1}}$ (pole at $z=1$)
> - $x = u[n]$ (pole at 1, matches): $y = u[n]*u[n] = (n+1)u[n]$ — **unbounded**.
> - $x = (-1)^n u[n]$ (pole at $-1$): bounded. $x = \left(\frac12\right)^n u[n]$ (pole inside): bounded.
> - $x = \delta[n]-\delta[n-1]$ (a zero at 1): $y = \delta[n]$ — the pole is cancelled.

## Pole matching with sines and cosines

Split real sinusoids with Euler before matching ([[0-toolkit/01-complex-numbers|complex numbers]]):
$$
\cos(\omega_0 n)u[n] = \tfrac12 e^{j\omega_0 n}u[n] + \tfrac12 e^{-j\omega_0 n}u[n]
\quad\Longrightarrow\quad \text{poles at } e^{+j\omega_0} \text{ and } e^{-j\omega_0}
$$
(same for $\sin$). A cosine therefore resonates with a system pole at **either** $e^{j\omega_0}$ or $e^{-j\omega_0}$. SP2025 #6: $H = \frac{1}{1-e^{j\pi/4}z^{-1}}$ is driven unbounded by $e^{j\pi n/4}u[n]$ and by $\cos(\frac{\pi}{4}n)u[n]$, but **not** by $e^{-j\pi n/4}u[n]$ alone.

> [!recipe] "Which bounded inputs give an unbounded output?"
> 1. Factor $H(z)$; list the poles **on** the unit circle (a pole outside with a causal ROC means an ordinary unstable system: almost any input blows up).
> 2. Write each input's poles: $e^{j\omega n}u[n] \to e^{j\omega}$; $\cos/\sin(\omega n)u[n] \to e^{\pm j\omega}$; $u[n] \to 1$; $(-1)^nu[n] \to -1$; $j^nu[n] \to j$; finite inputs have no poles.
> 3. Cancel any input zero against a system pole (and any system zero against an input pole) — see [[concepts/pole-zero-cancellation|pole-zero cancellation]].
> 4. **Unbounded** iff a surviving input pole lands **exactly** on a surviving unit-circle pole of $H$ (a double pole on $|z|=1$). A shared pole **inside** the circle is harmless: it gives $n\,p^n u[n]$, which decays.

<figure class="ece-fig"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 760 330" width="760" height="330" role="img" style="font-family:'Source Sans 3','Source Sans Pro',system-ui,sans-serif;font-size:14px"><defs><marker id="ahpm" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="context-stroke"/></marker></defs><line x1="50.0" y1="165.0" x2="350.0" y2="165.0" stroke="currentColor" stroke-width="1.1" opacity="0.8" stroke-linecap="round"/><line x1="200.0" y1="15.0" x2="200.0" y2="315.0" stroke="currentColor" stroke-width="1.1" opacity="0.8" stroke-linecap="round"/><circle cx="200.0" cy="165.0" r="120.0" fill="none" stroke="currentColor" stroke-width="1.3" stroke-dasharray="5 4"/><text x="350.0" y="159.0" text-anchor="end" fill="var(--muted)" style="font-size:12px;">Re</text><text x="206.0" y="27.0" text-anchor="start" fill="var(--muted)" style="font-size:12px;">Im</text><line x1="283.0" y1="158.0" x2="297.0" y2="172.0" stroke="var(--hi)" stroke-width="2.4" stroke-linecap="round"/><line x1="283.0" y1="172.0" x2="297.0" y2="158.0" stroke="var(--hi)" stroke-width="2.4" stroke-linecap="round"/><line x1="193.0" y1="38.0" x2="207.0" y2="52.0" stroke="var(--hi)" stroke-width="2.4" stroke-linecap="round"/><line x1="193.0" y1="52.0" x2="207.0" y2="38.0" stroke="var(--hi)" stroke-width="2.4" stroke-linecap="round"/><line x1="287.3" y1="83.8" x2="301.3" y2="97.8" stroke="var(--hi)" stroke-width="2.4" stroke-linecap="round"/><line x1="287.3" y1="97.8" x2="301.3" y2="83.8" stroke="var(--hi)" stroke-width="2.4" stroke-linecap="round"/><rect x="134.0" y="55.1" width="12" height="12" fill="none" stroke="var(--accent2)" stroke-width="2"/><rect x="134.0" y="262.9" width="12" height="12" fill="none" stroke="var(--accent2)" stroke-width="2"/><circle cx="200.0" cy="45.0" r="12.0" fill="none" stroke="var(--accent)" stroke-width="2"/><path d="M242.0,165.0 A42,42 0 0,0 233.0,139.0" fill="none" stroke="var(--hi)" stroke-width="1.4"/><text x="250.0" y="154.0" text-anchor="start" fill="var(--hi)" style="font-size:12px;">2/3 rad</text><path d="M226.0,165.0 A26,26 0 0,0 187.0,142.5" fill="none" stroke="var(--accent2)" stroke-width="1.4"/><text x="170.0" y="135.0" text-anchor="end" fill="var(--accent2)" style="font-size:12px;">2π/3</text><text x="306.3" y="82.8" text-anchor="start" fill="var(--hi)" style="font-size:14px;font-family:'STIX Two Math','Latin Modern Math','Cambria Math','Times New Roman',serif;font-style:italic;">e<tspan dy="-6" font-size="10">j2/3</tspan></text><text x="218.0" y="33.0" text-anchor="start" fill="var(--hi)" style="font-size:15px;font-family:'STIX Two Math','Latin Modern Math','Cambria Math','Times New Roman',serif;font-style:italic;">j</text><text x="290.0" y="187.0" text-anchor="middle" fill="var(--hi)" style="font-size:14px;">¾</text><text x="128.0" y="51.1" text-anchor="end" fill="var(--accent2)" style="font-size:14px;font-family:'STIX Two Math','Latin Modern Math','Cambria Math','Times New Roman',serif;font-style:italic;">e<tspan dy="-6" font-size="10">j2π/3</tspan></text><text x="128.0" y="290.9" text-anchor="end" fill="var(--accent2)" style="font-size:14px;font-family:'STIX Two Math','Latin Modern Math','Cambria Math','Times New Roman',serif;font-style:italic;">e<tspan dy="-6" font-size="10">−j2π/3</tspan></text><line x1="382.0" y1="54.0" x2="394.0" y2="66.0" stroke="var(--hi)" stroke-width="2.4" stroke-linecap="round"/><line x1="382.0" y1="66.0" x2="394.0" y2="54.0" stroke="var(--hi)" stroke-width="2.4" stroke-linecap="round"/><text x="406.0" y="65.0" text-anchor="start" fill="currentColor" style="font-size:13px;">poles of H(z): ¾, j, e<tspan dy="-6" font-size="10">j2/3</tspan></text><circle cx="388.0" cy="94.0" r="10.0" fill="none" stroke="var(--accent)" stroke-width="2"/><text x="406.0" y="99.0" text-anchor="start" fill="currentColor" style="font-size:13px;">j<tspan dy="-6" font-size="10">n</tspan><tspan dy="6">u[n], sin(πn/2)u[n] hit j</tspan></text><text x="406.0" y="117.0" text-anchor="start" fill="var(--accent)" style="font-size:13px;">→ double pole on |z| = 1 → unbounded</text><rect x="382.0" y="140.0" width="12" height="12" fill="none" stroke="var(--accent2)" stroke-width="2"/><text x="406.0" y="151.0" text-anchor="start" fill="currentColor" style="font-size:13px;">cos(2πn/3)u[n]: poles e<tspan dy="-6" font-size="10">±j2π/3</tspan></text><text x="406.0" y="169.0" text-anchor="start" fill="var(--accent2)" style="font-size:13px;">→ no match (120° ≠ 38.2°) → bounded</text><text x="406.0" y="205.0" text-anchor="start" fill="var(--muted)" style="font-size:13px;">δ[n] − ¾δ[n−1] cancels ¾ → bounded;</text><text x="406.0" y="223.0" text-anchor="start" fill="var(--muted)" style="font-size:13px;">(⅔)ⁿu[n] adds a pole inside → bounded</text></svg><figcaption><strong>FA2025 #8(b): only an input pole that lands exactly on a unit-circle pole of H(z) makes the output blow up.</strong> H(z) = 1/((1 − ¾z⁻¹)(1 − jz⁻¹)(1 − e<sup>j2/3</sup>z⁻¹)), |z| &gt; 1. The pole e<sup>j2/3</sup> sits at 2/3 rad ≈ 38.2°, while cos(2πn/3)u[n] has its poles at ±120°: no double pole, bounded output (key: False). jⁿu[n] and sin(πn/2)u[n] put a second pole on top of j: output grows like n (key: True).</figcaption></figure>

> [!trap] $e^{j2/3}$ is not $e^{j2\pi/3}$ (FA2025 #8b)
> The pole $e^{j2/3}$ sits at an angle of $\frac23$ rad $\approx 38.2^\circ$. The input $\cos(\frac{2\pi}{3}n)u[n]$ has poles at $\pm\frac{2\pi}{3}$ rad $= \pm120^\circ$. No match, so the output stays **bounded** — the key's answer to "unbounded?" is False. Read the exponent before you match.

A quick simulation of FA2025 #8(b) shows the difference:

```python
import numpy as np
from scipy.signal import lfilter
# FA2025 #8(b): H(z) = 1/((1 - 3/4 z^-1)(1 - j z^-1)(1 - e^{j2/3} z^-1)), causal
a = np.convolve(np.convolve([1, -0.75], [1, -1j]), [1, -np.exp(2j/3)])
n = np.arange(2000)
for name, x in [("j^n u[n]", 1j**n), ("cos(2pi n/3) u[n]", np.cos(2*np.pi*n/3))]:
    y = lfilter([1], a, x)
    print(f"{name:18s} max|y| up to n=99: {abs(y[:100]).max():7.2f}   up to n=1999: {abs(y).max():8.2f}")
```

```text
j^n u[n]           max|y| up to n=99:   92.34   up to n=1999:  1833.46
cos(2pi n/3) u[n]  max|y| up to n=99:    2.63   up to n=1999:     2.63
```

The matched input grows linearly (about $0.92\,n$); the unmatched one never exceeds 2.63.

> [!trap]
> - **Marginally stable = unstable.** It is not a third category for T/F purposes: "BIBO stable" is False.
> - "Unstable ⇒ every input gives an unbounded output" is False (FA2019 T/F (j)); so is "unstable ⇒ $h$ unbounded" (FA2025 T/F (a), FA2024 (b), FA2019 (c)) — $h = u[n]$ is bounded.
> - $u[n]$ has its pole at $1$, $(-1)^nu[n]$ at $-1$, $j^nu[n]$ and $\sin(\frac{\pi}{2}n)u[n]$ at $j$ (and $-j$ for the sine). $\sin(-\frac{\pi}{2}n)u[n] = -\sin(\frac{\pi}{2}n)u[n]$: same poles.
> - A double pole **inside** the unit circle is fine: in the Lecture 11 slide example, $(\frac23)^nu[n]$ into a system with a pole at $\frac23$ gives $n(\frac23)^n u[n]$, bounded.
> - Inputs like $4^nu[n]$ or $(-3)^nu[n]$ are themselves unbounded; they do not test stability, but exam questions may still ask whether the *output* is bounded (FA2025 #8a iii: no).

**Where it appears.**
- Lectures: [[2-z-transform/11-bibo-stability-and-causality|L11]] §1.2.1 and slides 15–18 (pole matching, the eight-input example).
- Problem family: [[problems/unbounded-outputs-and-pole-matching]] (7/7 exams).
- Homework: [[homework/hw4|HW4]] #3(c) ($\frac{z+1}{z-1}$, $x=u[n]$ gives $(2n+1)u[n]$) and #3(d) ($\frac{z-1}{z^2+j}$, poles $e^{-j\pi/4}, e^{j3\pi/4}$; $\cos(\frac{\pi}{4}n)u[n]$ resonates).
- Past exams: [[0-midterm-1/past-exams/fall-2025|FA2025 #8b]], [[0-midterm-1/past-exams/spring-2025|SP2025 #6]], [[0-midterm-1/past-exams/fall-2023|FA2023 #7c]] (pole at $-1$, input $(-1)^nu[n]$), [[0-midterm-1/past-exams/spring-2021|SP2021 #5]] ($\frac{3z^{-1}}{1+z^{-2}}$: $j^n$, $\cos(\frac{\pi}{2}n)$, $\sin(\frac{\pi}{2}n)$ all resonate) and T/F (d) ($\frac{z^{-1}}{1-z^{-1}}$ with $u[n]$ gives $n\,u[n]$: True); [[0-midterm-1/true-false-bank|T/F bank]].

Related: [[concepts/bibo-stability]] · [[concepts/region-of-convergence]] · [[concepts/poles-and-zeros]] · [[concepts/pole-zero-cancellation]] · [[concepts/complex-exponential]] · [[concepts/eigenfunctions-of-lti-systems]]

### Sources for this page
Lecture 11 notes §1.2–1.2.1 (definition, $u[n]*u[n]$, the $e^{j\omega_1 n}$ vs $e^{j\omega_2 n}$ derivation) and annotated slides 14–18 (pole-matching example: inputs 1, 3, 6, 7 unbounded); exam keys FA2025 #8b, SP2025 #6, FA2023 #7, SP2021 #5; HW4 #3 solutions. Verification: `verify/concepts/verify_stability.py` (55/55: every case by pole bookkeeping **and** simulation) and `verify_zdomain_extra.py` (double-pole pair); output above pasted from a real run.
