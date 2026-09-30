---
title: "Poles and zeros"
description: "Where X(z) blows up and where it vanishes: how to find them from the z⁻¹ form, how to draw the pole-zero plot, and what each pole means in time — the mode pⁿ that decays, oscillates or grows."
tags: [concept, z-transform, roc, stability]
aliases: ["poles", "zeros", "pole-zero plot"]
---

> [!key] Definition (Lecture 6)
> **Zeros**: values of $z$ with $X(z) = 0$. **Poles**: values of $z$ with $X(z)\to\infty$. For a rational transform in factored form
> $$
> X(z) = b_0\,\frac{\prod_{k}\left(1-q_k z^{-1}\right)}{\prod_{k}\left(1-p_k z^{-1}\right)}
> \qquad\Longrightarrow\qquad \text{zeros at } q_k,\ \ \text{poles at } p_k .
> $$
> A **pole-zero plot** marks poles with ×, zeros with ○, shades the ROC and draws the unit circle dashed. Multiply through by the highest power of $z$ to see any extra poles or zeros at $z=0$.

**How to find them.** Set the numerator and the denominator to zero. It is easiest in $w = z^{-1}$: $1+\frac16 z^{-1}-\frac13 z^{-2} = 0$ becomes $-\frac13 w^2+\frac16 w+1 = 0$, i.e. $(-2w-3)(w-2)=0$, so $w = 2, -\frac32$ and the poles are $z = 1/w = \frac12, -\frac23$ (HW3 #4 solution). Quadratics with a negative discriminant give a conjugate pair $re^{\pm j\omega_0}$ ([[0-toolkit/04-factoring-and-long-division|factoring]], [[0-toolkit/01-complex-numbers|complex numbers]]).

> [!example] HW3 #4: $H(z) = \dfrac{1-3z^{-1}}{1+\frac16 z^{-1}-\frac13 z^{-2}}$, right-sided
> In positive powers, $H(z) = \dfrac{z(z-3)}{(z-\frac12)(z+\frac23)}$: **zeros** $3$ and $0$, **poles** $\frac12$ and $-\frac23$. Right-sided ⇒ ROC $|z|>\frac23$; it contains the unit circle, so the system is stable. PFE then gives $h[n] = \frac{22}{7}\left(-\frac23\right)^n u[n] - \frac{15}{7}\left(\frac12\right)^n u[n]$. (The official solution lists only the zero at $3$ — the zero at the origin is harmless and usually omitted.)

<figure class="ece-fig"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 420 330" width="420" height="330" role="img" style="font-family:'Source Sans 3','Source Sans Pro',system-ui,sans-serif;font-size:14px"><defs><marker id="ahpz" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="context-stroke"/></marker></defs><clipPath id="pzclip"><rect x="15.0" y="10.0" width="400.0" height="300.0"/></clipPath><path d="M15.0,10.0 h400.0 v300.0 h-400.0 Z M228.67,160.00 A38.67,38.67 0 1,0 151.33,160.00 A38.67,38.67 0 1,0 228.67,160.00 Z" fill="var(--accent)" fill-opacity="0.16" fill-rule="evenodd" stroke="none" clip-path="url(#pzclip)"/><circle cx="190.0" cy="160.0" r="38.7" fill="none" stroke="var(--accent)" stroke-width="1.4"/><line x1="15.0" y1="160.0" x2="412.0" y2="160.0" stroke="currentColor" stroke-width="1.1" opacity="0.8" stroke-linecap="round"/><line x1="190.0" y1="10.0" x2="190.0" y2="310.0" stroke="currentColor" stroke-width="1.1" opacity="0.8" stroke-linecap="round"/><circle cx="190.0" cy="160.0" r="58.0" fill="none" stroke="currentColor" stroke-width="1.3" stroke-dasharray="5 4"/><circle cx="190.0" cy="160.0" r="6.5" fill="none" stroke="var(--accent2)" stroke-width="2.2"/><circle cx="364.0" cy="160.0" r="6.5" fill="none" stroke="var(--accent2)" stroke-width="2.2"/><line x1="213.0" y1="154.0" x2="225.0" y2="166.0" stroke="var(--hi)" stroke-width="2.4" stroke-linecap="round"/><line x1="213.0" y1="166.0" x2="225.0" y2="154.0" stroke="var(--hi)" stroke-width="2.4" stroke-linecap="round"/><line x1="145.3" y1="154.0" x2="157.3" y2="166.0" stroke="var(--hi)" stroke-width="2.4" stroke-linecap="round"/><line x1="145.3" y1="166.0" x2="157.3" y2="154.0" stroke="var(--hi)" stroke-width="2.4" stroke-linecap="round"/><text x="364.0" y="184.0" text-anchor="middle" fill="var(--accent2)" style="font-size:14px;font-weight:600;">3</text><text x="199.0" y="182.0" text-anchor="start" fill="var(--accent2)" style="font-size:13px;">0</text><text x="221.0" y="148.0" text-anchor="middle" fill="var(--hi)" style="font-size:14px;font-weight:600;">½</text><text x="147.3" y="148.0" text-anchor="end" fill="var(--hi)" style="font-size:14px;font-weight:600;">−⅔</text><text x="192.0" y="94.0" text-anchor="start" fill="var(--muted)" style="font-size:12px;">|z| = 1</text><text x="412.0" y="154.0" text-anchor="end" fill="var(--muted)" style="font-size:12px;">Re</text><text x="196.0" y="23.0" text-anchor="start" fill="var(--muted)" style="font-size:12px;">Im</text><text x="25.0" y="26.0" text-anchor="start" fill="var(--accent)" style="font-size:13px;">ROC: |z| &gt; ⅔ (shaded)</text></svg><figcaption><strong>Pole-zero plot of HW3 #4: H(z) = (1 − 3z⁻¹)/(1 + ⅙z⁻¹ − ⅓z⁻²), right-sided.</strong> Poles × at ½ and −⅔, zeros ○ at 3 and at 0 (H = z(z − 3)/((z − ½)(z + ⅔)) in positive powers). Right-sided ⇒ ROC outside the largest pole, |z| &gt; ⅔; it contains the dashed unit circle, so the system is stable. The zero at 3 lies inside the ROC — zeros are allowed there.</figcaption></figure>

## What a pole means in time

Each simple pole $p$ contributes a **mode** $p^n$ to the signal (right-sided: $A p^n u[n]$; left-sided: $-A p^n u[-n-1]$):

| pole location | right-sided mode $p^n u[n]$ |
|---|---|
| $0<p<1$ | decays monotonically |
| $-1<p<0$ | decays, alternating sign |
| $\lvert p\rvert = 1$ ($p = e^{j\omega_0}$) | never decays: $e^{j\omega_0 n}$ ([[concepts/marginal-stability\|marginal]]) |
| $\lvert p\rvert > 1$ | grows (unstable if causal) |
| pair $re^{\pm j\omega_0}$ | $r^n\cos(\omega_0 n+\theta)$: radius sets the envelope, angle the frequency |
| $z = 0$ (causal FIR) | no mode — just delays |

**Zeros block exponentials.** If $H(z_0) = 0$, the input $z_0^n$ (all $n$) produces zero output. Example: $y[n] = x[n]-x[n-1]$ has $H(z) = 1-z^{-1}$, a zero at $1$, so a constant input gives $y=0$. A zero on top of a pole cancels it ([[concepts/pole-zero-cancellation|pole-zero cancellation]]).

**Poles and the ROC.** The ROC never contains a pole, so the pole radii are its possible edges ([[concepts/region-of-convergence|ROC]]); for a causal system, stability means **every pole strictly inside** $|z|=1$. An FIR system's poles are all at $z=0$ (causal) or $z=\infty$ — always stable ([[concepts/fir-and-iir|FIR and IIR]]).

> [!example]- The three pole-zero plots of Lecture 6, Fig. 1
> - $u[n] \leftrightarrow \frac{1}{1-z^{-1}} = \frac{z}{z-1}$: pole $1$, zero $0$, ROC $|z|>1$.
> - $\left(-\frac13\right)^n u[n] \leftrightarrow \frac{1}{1+\frac13 z^{-1}}$: pole $-\frac13$, zero $0$, ROC $|z|>\frac13$.
> - $\cos(\frac{2\pi}{3}n)u[n] \leftrightarrow \frac{1+\frac12 z^{-1}}{1+z^{-1}+z^{-2}}$: poles $e^{\pm j2\pi/3}$ on the unit circle, zeros $-\frac12$ and $0$, ROC $|z|>1$.

**In Python.** `np.roots` on each coefficient list, or `scipy.signal.tf2zpk` — pad `b` and `a` to the **same length** so both are read as polynomials in $z^{-1}$; otherwise zeros or poles at the origin silently disappear:

```python
import numpy as np
from scipy.signal import tf2zpk
# HW3 #4: H(z) = (1 - 3z^-1) / (1 + 1/6 z^-1 - 1/3 z^-2); pad b with a 0 so both
# lists have the same length (tf2zpk then reads them as polynomials in z^-1)
z, p, k = tf2zpk([1, -3, 0], [1, 1/6, -1/3])
print("zeros", z, " poles", p)
print("right-sided ROC: |z| >", round(np.abs(p).max(), 4), " stable:", np.all(np.abs(p) < 1))
```

```text
zeros [3. 0.]  poles [-0.66666667  0.5       ]
right-sided ROC: |z| > 0.6667  stable: True
```

> [!trap]
> - **Poles are values of $z$, not of $z^{-1}$.** $(1-2z^{-1})$ is a pole at $z=2$; $(1+\frac23 z^{-1})$ at $z=-\frac23$.
> - **Zeros may lie in the ROC**; poles may not (FA2023 T/F (b), False).
> - Equal-magnitude poles lie on one circle and bound the ROC together (conjugate pairs, $\pm j$).
> - Count the **distinct** poles carefully: $y[n] = y[n-3]+x[n]$ has $H = \frac{1}{1-z^{-3}}$ with three distinct poles, the cube roots of unity (FA2024 T/F (e), True); an LCCDE has finitely many poles (FA2024 T/F (d), True).
> - The angle is the exponent: $e^{j2/3}$ sits at $\frac23$ rad $\approx 38^\circ$, not at $120^\circ$ (FA2025 #8b — see [[concepts/marginal-stability|marginal stability]]).

**Where it appears.**
- Lectures: [[2-z-transform/06-the-z-transform|L6]] (definition, pole-zero plots), [[2-z-transform/07-z-transform-properties|L7]] (no poles in the ROC), [[2-z-transform/08-inverse-z-transform|L8]] (product form), [[2-z-transform/09-transfer-functions|L9]] §1.2 ($N$ poles, $M$ zeros, FIR vs IIR), [[2-z-transform/11-bibo-stability-and-causality|L11]] (pole locations ⇒ stability).
- Problem families: [[problems/all-possible-rocs]], [[problems/lccde-to-transfer-function-and-response]], [[problems/unbounded-outputs-and-pole-matching]], [[problems/parameters-for-stability]].
- Homework: [[homework/hw3|HW3]] #4; [[homework/hw4|HW4]] #3.
- Past exams: [[0-midterm-1/past-exams/fall-2025|FA2025]] #6 (poles $2, -\frac23$; zeros $\pm1$), #8; [[0-midterm-1/past-exams/spring-2025|SP2025 #7]] (poles $-2, \frac12$); [[0-midterm-1/past-exams/fall-2024|FA2024]] #8, T/F (d), (e); [[0-midterm-1/past-exams/fall-2023|FA2023]] #8, T/F (b); [[0-midterm-1/past-exams/spring-2023|SP2023 #5a]] (zeros $\pm2$, poles $\frac32, -\frac12$). Move poles and zeros yourself in the [[demos/pole-zero-and-roc-explorer|pole-zero and ROC explorer]].

Related: [[concepts/region-of-convergence]] · [[concepts/transfer-function]] · [[concepts/pole-zero-cancellation]] · [[concepts/marginal-stability]] · [[concepts/partial-fraction-expansion]] · [[concepts/bibo-stability]]

### Sources for this page
Lecture 6 notes §2 (definitions, Fig. 1) and slides; Lecture 8 notes §1.2 (product form); Lecture 9 notes §1.2; Lecture 11 notes §1.1; HW3 #4 solution (factoring in $z^{-1}$); exam keys cited above. Verification: `verify/concepts/verify_zdomain_extra.py` (pole-zero data for HW3 #4, L6 Fig. 1), `verify_pfe.py` (HW3 #4 $h[n]$); output above pasted from a real run.
