---
title: "Lecture 10 — Improper transfer functions and system algebra"
description: "When the numerator reaches the denominator's degree (more input taps than feedback taps): long division then PFE, or PFE of 1/A(z) plus time shifts; and system algebra — series = product, parallel = sum — with what happens to ROCs, stability and pole-zero cancellations when LTI systems are combined."
tags: [lecture, midterm-1, z-transform, lccde, systems]
lecture: 10
---

*Lecture 10 · Wed Sep 16, 2026 · notes + slides "Transfer functions and LTI system response: Part 2" · prev: [[2-z-transform/09-transfer-functions|Lecture 9]] · next: [[2-z-transform/11-bibo-stability-and-causality|Lecture 11]]*

> [!abstract] In one breath
> Partial fractions only work on **proper** rational functions (numerator degree < denominator degree, counted in powers of $z^{-1}$). An LCCDE whose input taps reach as far back as its feedback taps gives an **improper** $H(z)$; then either **long-divide first** — the quotient $C_0 + C_1z^{-1} + \dots$ becomes a few impulses $C_k\delta[n-k]$, the remainder gets the usual PFE — or expand $1/A(z)$ and add up shifted copies. The second half is **system algebra**: LTI systems in **series** multiply ($h_1 * h_2 \leftrightarrow H_1H_2$), in **parallel** add ($h_1 + h_2 \leftrightarrow H_1 + H_2$), so any diagram collapses to one $H(z)$. The combined ROC contains the intersection of the individual ROCs, and a zero of one system can cancel a pole of the other — which is how two unstable systems can make a stable one, a favourite True/False topic.

## 1. Proper and improper transfer functions

Lecture 9's transfer functions were **proper**:
$$
H(z) = \frac{\sum_{k=0}^{M-1} b_k z^{-k}}{1 + \sum_{k=1}^{N} a_k z^{-k}}, \qquad M \le N ,
$$
i.e. the numerator's highest power $z^{-(M-1)}$ is lower than the denominator's $z^{-N}$. If $M > N$ the expression is **improper**. In LCCDE terms: *some input term is delayed at least as far as the most-delayed feedback term* — e.g. $x[n-3]$ against $y[n-2]$ below. Long division splits an improper $H$ into a polynomial part and a proper part:

> [!key] Improper = impulses + exponentials
> $$
> H(z) = \sum_{k=0}^{M-N-1} C_k z^{-k} + \frac{\sum_{k=0}^{N-1} d_k z^{-k}}{1 + \sum_{k=1}^{N} a_k z^{-k}}
> = \sum_{k=0}^{M-N-1} C_k z^{-k} + \sum_{k=1}^{N}\frac{A_k}{1 - p_k z^{-1}}
> $$
> $$
> \Longrightarrow\quad h[n] = \sum_{k} C_k\,\delta[n-k] + \sum_k A_k\,p_k^n\,u[n] \qquad(\text{causal}).
> $$
> The $C_k$ come from long division, the $A_k$ from a PFE of the **remainder** over the denominator.

> [!trap] Count degrees in $z^{-1}$ — and "equal" already counts as improper
> HW4 #3(a) gives $H(z) = \dfrac{z(z-4)}{z^2-5z+6}$, which *looks* improper in $z$ (the official solution long-divides in $z$). In powers of $z^{-1}$ it is $\dfrac{1-4z^{-1}}{(1-2z^{-1})(1-3z^{-1})}$ — **proper**, so the PFE is immediate: $A = 2$ at $z = 2$, $A = -1$ at $z = 3$, $h[n] = (2^{n+1} - 3^n)u[n]$ (the same sequence as the key's $\delta[n] + 4(2)^{n-1}u[n-1] - 3^n u[n-1]$). Conversely, **equal** degrees in $z^{-1}$ are improper: FA2025 #6's $\dfrac{1-z^{-2}}{(1-2z^{-1})(1+\frac23 z^{-1})}$ hides a constant $C_0 = \tfrac34$, and without it the cover-up coefficients are wrong.

## 2. Exercise 1 — the same $h[n]$ two ways

> [!question] Exercise 1 (notes and slides 4–8)
> Compute the impulse response of the causal LCCDE
> $$
> y[n] = 2y[n-1] + 3y[n-2] + x[n] - 3x[n-1] + x[n-2] + 4x[n-3] .
> $$

Transforming both sides as in Lecture 9, $Y(z)\bigl(1 - 2z^{-1} - 3z^{-2}\bigr) = X(z)\bigl(1 - 3z^{-1} + z^{-2} + 4z^{-3}\bigr)$, so
$$
H(z) = \frac{1 - 3z^{-1} + z^{-2} + 4z^{-3}}{1 - 2z^{-1} - 3z^{-2}} = \frac{1 - 3z^{-1} + z^{-2} + 4z^{-3}}{(1-3z^{-1})(1+z^{-1})}, \qquad |z| > 3 ,
$$
with $M = 4$ input terms and $N = 2$ feedback terms: improper, with $M - N = 2$ quotient terms $C_0 + C_1 z^{-1}$.

**Approach #2 — long division, then PFE.** Divide starting from the **highest** power of $z^{-1}$:
$$
\begin{aligned}
&4z^{-3} \div (-3z^{-2}) = -\tfrac43 z^{-1}: && \bigl(1 - 3z^{-1} + z^{-2} + 4z^{-3}\bigr) - \left(-\tfrac43 z^{-1}\right)\bigl(1 - 2z^{-1} - 3z^{-2}\bigr) = 1 - \tfrac53 z^{-1} - \tfrac53 z^{-2}\\
&-\tfrac53 z^{-2} \div (-3z^{-2}) = \tfrac59: && \bigl(1 - \tfrac53 z^{-1} - \tfrac53 z^{-2}\bigr) - \tfrac59\bigl(1 - 2z^{-1} - 3z^{-2}\bigr) = \tfrac49 - \tfrac59 z^{-1}
\end{aligned}
$$
So $C_0 = \tfrac59$, $C_1 = -\tfrac43$ and
$$
H(z) = \frac59 - \frac43 z^{-1} + \frac{\frac49 - \frac59 z^{-1}}{(1-3z^{-1})(1+z^{-1})} = \frac59 - \frac43 z^{-1} + \frac{A_1}{1-3z^{-1}} + \frac{A_2}{1+z^{-1}} .
$$
Cover-up on the **remainder**: $A_1 = \dfrac{\frac49 - \frac59\cdot\frac13}{1 + \frac13} = \dfrac{7}{36}$ (at $z = 3$) and $A_2 = \dfrac{\frac49 + \frac59}{1 + 3} = \dfrac14$ (at $z = -1$). The system is causal, so every term inverts by inspection — assemble $h[n]$ yourself, then check:

> [!success]- Answer (exact rational check of 40 samples; $h = \{\underset{\uparrow}{1}, -1, 2, 5, 16, 47, \dots\}$)
> $$
> h[n] = \tfrac59\,\delta[n] - \tfrac43\,\delta[n-1] + \tfrac{7}{36}\,3^n u[n] + \tfrac14\,(-1)^n u[n] .
> $$
> Sanity check at $n = 0$: $\tfrac59 + \tfrac{7}{36} + \tfrac14 = 1 = b_0$, as the recursion demands.

**Approach #1 — numerator 1 first, then shift.** Factor out the numerator:
$$
H(z) = \bigl(1 - 3z^{-1} + z^{-2} + 4z^{-3}\bigr)\,G(z), \qquad G(z) = \frac{1}{(1-3z^{-1})(1+z^{-1})} = \frac{\frac34}{1-3z^{-1}} + \frac{\frac14}{1+z^{-1}} ,
$$
so $g[n] = \tfrac34\,3^n u[n] + \tfrac14(-1)^n u[n]$ and, by linearity and time shifting,
$$
h[n] = g[n] - 3g[n-1] + g[n-2] + 4g[n-3] .
$$
"Unseemly", as the notes say, but identical sample for sample (checked exactly). Use it when the division looks messy; use Approach #2 when you want a clean closed form.

> [!recipe] Improper $H(z) \to h[n]$
> 1. Write $H$ in powers of $z^{-1}$ and compare degrees; numerator degree $\ge$ denominator degree ⇒ improper.
> 2. Long-divide from the **highest** power of $z^{-1}$ down, until the remainder's degree is below the denominator's. The quotient is $C_0 + C_1 z^{-1} + \dots$
> 3. PFE of remainder ÷ denominator by cover-up (the numerator is the *remainder*, not the original numerator).
> 4. Invert: $C_k z^{-k} \to C_k\,\delta[n-k]$; $\dfrac{A_k}{1-p_kz^{-1}} \to A_k p_k^n u[n]$ (or $-A_k p_k^n u[-n-1]$ for the left-sided choice).
> 5. Check $h[0]$ against the LCCDE ($h[0] = b_0$ for a causal system).

> [!trap] Dividing from the wrong end
> Ordinary long division starts from the constant term; done that way here it never terminates — it produces the power series of $H$ (which is just $h[0], h[1], \dots$ again). For a finite quotient, start from the highest power of $z^{-1}$, as above.

In Python, `residuez` does both steps at once: its third output `k` is the list of $C_k$.

```python
import numpy as np
from scipy.signal import residuez, lfilter

# Exercise 1: y[n] = 2y[n-1] + 3y[n-2] + x[n] - 3x[n-1] + x[n-2] + 4x[n-3]
b = [1, -3, 1, 4]          # numerator, powers of z^-1 (degree 3)
a = [1, -2, -3]            # denominator 1 - 2z^-1 - 3z^-2 (degree 2) -> improper
r, p, k = residuez(b, a)   # H = sum r_i/(1 - p_i z^-1) + sum_j k_j z^-j
print("A_k:", np.round(r.real, 4), " p_k:", np.round(p.real, 4))
print("C_k:", np.round(k.real, 4))          # the long-division quotient C_0, C_1
print("h[0..5]:", lfilter(b, a, [1., 0, 0, 0, 0, 0]))   # 1, -1, 2, 5, 16, ...: 3^n takes over
```

```text
A_k: [0.25   0.1944]  p_k: [-1.  3.]
C_k: [ 0.5556 -1.3333]
h[0..5]: [ 1. -1.  2.  5. 16. 47.]
```

$0.1944 = \tfrac{7}{36}$, $0.5556 = \tfrac59$, $-1.3333 = -\tfrac43$.

> [!example] An exam key that needed this lecture — SP2021 #6
> $y[n] = 2y[n-3] - x[n] + x[n-3]$ (causal, at rest) gives $H(z) = \dfrac{-1 + z^{-3}}{1 - 2z^{-3}}$ — equal degrees, so improper. One division step: $H = -\tfrac12 - \dfrac{\frac12}{1-2z^{-3}}$, and $\dfrac{1}{1-2z^{-3}} = \sum_{k\ge0} 2^k z^{-3k}$, so $h[n] = -\tfrac12\delta[n] - \tfrac12\sum_{k\ge 0}2^k\delta[n-3k]$: $h[0] = -1$, $h[1] = h[2] = 0$, $h[3] = -1$, $h[4] = 0$, $h[6] = -2$. The official key reports $h[0] = 1$, $h[3] = 3$ — a sign slip (those are the values for $+x[n]$); see [[0-toolkit/05-errata|errata]].

## 3. System algebra: series multiplies, parallel adds

Two LTI systems **in parallel** see the same input and their outputs are added:
$$
y[n] = x[n]*h_1[n] + x[n]*h_2[n] = x[n]*\bigl(h_1[n] + h_2[n]\bigr) \quad(\text{distributivity}) \;\Longrightarrow\; H(z) = H_1(z) + H_2(z).
$$
**In series** (cascade) the output of one is the input of the next:
$$
y[n] = \bigl(x[n]*h_1[n]\bigr)*h_2[n] = x[n]*\bigl(h_1[n]*h_2[n]\bigr) \quad(\text{associativity}) \;\Longrightarrow\; H(z) = H_1(z)\,H_2(z).
$$

<figure class="ece-fig"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 680 300" width="680" height="300" role="img" style="font-family:'Source Sans 3','Source Sans Pro',system-ui,sans-serif;font-size:14px;max-width:100%;height:auto"><defs><marker id="l10ah" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="context-stroke"/></marker></defs><text x="170.0" y="24.0" text-anchor="middle" fill="currentColor" style="font-size:14px;font-weight:600;">series (cascade)</text><text x="22.0" y="65.0" text-anchor="start" fill="currentColor" style="font-size:13px;font-family:'STIX Two Math','Latin Modern Math','Cambria Math','Times New Roman',serif;font-style:italic;">x[n]</text><path d="M55.0,60.0 L88.0,60.0" fill="none" stroke="currentColor" stroke-width="1.6" marker-end="url(#l10ah)" stroke-linejoin="round"/><rect x="88.0" y="42.0" width="74" height="36" rx="4" fill="var(--accent)" fill-opacity="0.16" stroke="currentColor" stroke-width="1.5"/><text x="125.0" y="65.0" text-anchor="middle" fill="currentColor" style="font-size:14px;">H₁(z)</text><path d="M162.0,60.0 L196.0,60.0" fill="none" stroke="currentColor" stroke-width="1.6" marker-end="url(#l10ah)" stroke-linejoin="round"/><rect x="196.0" y="42.0" width="74" height="36" rx="4" fill="var(--accent)" fill-opacity="0.16" stroke="currentColor" stroke-width="1.5"/><text x="233.0" y="65.0" text-anchor="middle" fill="currentColor" style="font-size:14px;">H₂(z)</text><path d="M270.0,60.0 L300.0,60.0" fill="none" stroke="currentColor" stroke-width="1.6" marker-end="url(#l10ah)" stroke-linejoin="round"/><text x="305.0" y="65.0" text-anchor="start" fill="currentColor" style="font-size:13px;font-family:'STIX Two Math','Latin Modern Math','Cambria Math','Times New Roman',serif;font-style:italic;">y[n]</text><text x="170.0" y="104.0" text-anchor="middle" fill="currentColor" style="font-size:20px;">≡</text><text x="22.0" y="147.0" text-anchor="start" fill="currentColor" style="font-size:13px;font-family:'STIX Two Math','Latin Modern Math','Cambria Math','Times New Roman',serif;font-style:italic;">x[n]</text><path d="M55.0,142.0 L110.0,142.0" fill="none" stroke="currentColor" stroke-width="1.6" marker-end="url(#l10ah)" stroke-linejoin="round"/><rect x="112.0" y="124.0" width="134" height="36" rx="4" fill="var(--accent2)" fill-opacity="0.16" stroke="currentColor" stroke-width="1.5"/><text x="179.0" y="147.0" text-anchor="middle" fill="currentColor" style="font-size:14px;">H₁(z) H₂(z)</text><path d="M246.0,142.0 L300.0,142.0" fill="none" stroke="currentColor" stroke-width="1.6" marker-end="url(#l10ah)" stroke-linejoin="round"/><text x="305.0" y="147.0" text-anchor="start" fill="currentColor" style="font-size:13px;font-family:'STIX Two Math','Latin Modern Math','Cambria Math','Times New Roman',serif;font-style:italic;">y[n]</text><text x="170.0" y="190.0" text-anchor="middle" fill="currentColor" style="font-size:13.5px;">h[n] = h₁[n] ∗ h₂[n]</text><text x="170.0" y="210.0" text-anchor="middle" fill="var(--muted)" style="font-size:12.5px;">ROC ⊇ ROC₁ ∩ ROC₂</text><text x="170.0" y="228.0" text-anchor="middle" fill="var(--muted)" style="font-size:12.5px;">order does not matter (commutative)</text><text x="510.0" y="24.0" text-anchor="middle" fill="currentColor" style="font-size:14px;font-weight:600;">parallel</text><text x="368.0" y="85.0" text-anchor="start" fill="currentColor" style="font-size:13px;font-family:'STIX Two Math','Latin Modern Math','Cambria Math','Times New Roman',serif;font-style:italic;">x[n]</text><path d="M400.0,80.0 L420.0,80.0" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linejoin="round"/><circle cx="420" cy="80" r="3" fill="currentColor"/><path d="M420.0,48.0 L420.0,112.0" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linejoin="round"/><path d="M420.0,48.0 L466.0,48.0" fill="none" stroke="currentColor" stroke-width="1.6" marker-end="url(#l10ah)" stroke-linejoin="round"/><rect x="466.0" y="30.0" width="74" height="36" rx="4" fill="var(--accent)" fill-opacity="0.16" stroke="currentColor" stroke-width="1.5"/><text x="503.0" y="53.0" text-anchor="middle" fill="currentColor" style="font-size:14px;">H₁(z)</text><path d="M540.0,48.0 L590.0,48.0" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linejoin="round"/><path d="M590.0,48.0 L590.0,68.0" fill="none" stroke="currentColor" stroke-width="1.6" marker-end="url(#l10ah)" stroke-linejoin="round"/><path d="M420.0,112.0 L466.0,112.0" fill="none" stroke="currentColor" stroke-width="1.6" marker-end="url(#l10ah)" stroke-linejoin="round"/><rect x="466.0" y="94.0" width="74" height="36" rx="4" fill="var(--accent)" fill-opacity="0.16" stroke="currentColor" stroke-width="1.5"/><text x="503.0" y="117.0" text-anchor="middle" fill="currentColor" style="font-size:14px;">H₂(z)</text><path d="M540.0,112.0 L590.0,112.0" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linejoin="round"/><path d="M590.0,112.0 L590.0,92.0" fill="none" stroke="currentColor" stroke-width="1.6" marker-end="url(#l10ah)" stroke-linejoin="round"/><circle cx="590" cy="80" r="11" fill="none" stroke="currentColor" stroke-width="1.5"/><path d="M584.0,80.0 L596.0,80.0" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linejoin="round"/><path d="M590.0,74.0 L590.0,86.0" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linejoin="round"/><path d="M601.0,80.0 L632.0,80.0" fill="none" stroke="currentColor" stroke-width="1.6" marker-end="url(#l10ah)" stroke-linejoin="round"/><text x="636.0" y="85.0" text-anchor="start" fill="currentColor" style="font-size:13px;font-family:'STIX Two Math','Latin Modern Math','Cambria Math','Times New Roman',serif;font-style:italic;">y[n]</text><text x="510.0" y="158.0" text-anchor="middle" fill="currentColor" style="font-size:20px;">≡</text><text x="368.0" y="195.0" text-anchor="start" fill="currentColor" style="font-size:13px;font-family:'STIX Two Math','Latin Modern Math','Cambria Math','Times New Roman',serif;font-style:italic;">x[n]</text><path d="M400.0,190.0 L448.0,190.0" fill="none" stroke="currentColor" stroke-width="1.6" marker-end="url(#l10ah)" stroke-linejoin="round"/><rect x="448.0" y="172.0" width="140" height="36" rx="4" fill="var(--accent2)" fill-opacity="0.16" stroke="currentColor" stroke-width="1.5"/><text x="518.0" y="195.0" text-anchor="middle" fill="currentColor" style="font-size:14px;">H₁(z) + H₂(z)</text><path d="M588.0,190.0 L632.0,190.0" fill="none" stroke="currentColor" stroke-width="1.6" marker-end="url(#l10ah)" stroke-linejoin="round"/><text x="636.0" y="195.0" text-anchor="start" fill="currentColor" style="font-size:13px;font-family:'STIX Two Math','Latin Modern Math','Cambria Math','Times New Roman',serif;font-style:italic;">y[n]</text><text x="510.0" y="238.0" text-anchor="middle" fill="currentColor" style="font-size:13.5px;">h[n] = h₁[n] + h₂[n]</text><text x="510.0" y="258.0" text-anchor="middle" fill="var(--muted)" style="font-size:12.5px;">ROC ⊇ ROC₁ ∩ ROC₂</text><path d="M340.0,20.0 L340.0,280.0" fill="none" stroke="var(--muted)" stroke-width="1" stroke-linejoin="round"/></svg><figcaption><strong>System algebra (notes Table 1, slides 9–10).</strong> Two LTI systems in series collapse to one LTI system with h = h₁ ∗ h₂ and H = H₁H₂ (associativity of convolution); in parallel to h = h₁ + h₂ and H = H₁ + H₂ (distributivity). The combined ROC contains the intersection of the two ROCs, and can be larger when a pole of one factor is cancelled by a zero of the other.</figcaption></figure>

> [!key] Table 1 of the notes
> | connection | impulse response $h[n]$ | transfer function $H(z)$ |
> |---|---|---|
> | parallel | $h_1[n] + h_2[n]$ | $H_1(z) + H_2(z)$ |
> | series | $h_1[n] * h_2[n]$ | $H_1(z)\,H_2(z)$ |
>
> Any network of LTI systems built from series and parallel connections "collapses" into **one** LTI system, and the order of a cascade does not matter (convolution commutes — FA2023 1(e), True).

> [!question] Slide 11 — find the overall $H(z)$ in terms of $H_1,\dots,H_5$

<figure class="ece-fig"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 680 250" width="680" height="250" role="img" style="font-family:'Source Sans 3','Source Sans Pro',system-ui,sans-serif;font-size:14px;max-width:100%;height:auto"><defs><marker id="l10bh" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="context-stroke"/></marker></defs><text x="20.0" y="125.0" text-anchor="start" fill="currentColor" style="font-size:13px;font-family:'STIX Two Math','Latin Modern Math','Cambria Math','Times New Roman',serif;font-style:italic;">x[n]</text><path d="M52.0,120.0 L92.0,120.0" fill="none" stroke="currentColor" stroke-width="1.6" marker-end="url(#l10bh)" stroke-linejoin="round"/><rect x="93.0" y="102.0" width="74" height="36" rx="4" fill="var(--accent)" fill-opacity="0.16" stroke="currentColor" stroke-width="1.5"/><text x="130.0" y="125.0" text-anchor="middle" fill="currentColor" style="font-size:14px;">H₁(z)</text><path d="M167.0,120.0 L200.0,120.0" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linejoin="round"/><circle cx="200" cy="120" r="3" fill="currentColor"/><path d="M200.0,40.0 L200.0,181.0" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linejoin="round"/><path d="M200.0,40.0 L395.0,40.0" fill="none" stroke="currentColor" stroke-width="1.6" marker-end="url(#l10bh)" stroke-linejoin="round"/><rect x="395.0" y="22.0" width="74" height="36" rx="4" fill="var(--accent)" fill-opacity="0.16" stroke="currentColor" stroke-width="1.5"/><text x="432.0" y="45.0" text-anchor="middle" fill="currentColor" style="font-size:14px;">H₅(z)</text><path d="M200.0,181.0 L246.0,181.0" fill="none" stroke="currentColor" stroke-width="1.6" marker-end="url(#l10bh)" stroke-linejoin="round"/><rect x="246.0" y="163.0" width="74" height="36" rx="4" fill="var(--accent)" fill-opacity="0.16" stroke="currentColor" stroke-width="1.5"/><text x="283.0" y="186.0" text-anchor="middle" fill="currentColor" style="font-size:14px;">H₂(z)</text><path d="M320.0,181.0 L345.0,181.0" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linejoin="round"/><circle cx="345" cy="181" r="3" fill="currentColor"/><path d="M345.0,150.0 L345.0,212.0" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linejoin="round"/><path d="M345.0,150.0 L395.0,150.0" fill="none" stroke="currentColor" stroke-width="1.6" marker-end="url(#l10bh)" stroke-linejoin="round"/><rect x="395.0" y="132.0" width="74" height="36" rx="4" fill="var(--accent)" fill-opacity="0.16" stroke="currentColor" stroke-width="1.5"/><text x="432.0" y="155.0" text-anchor="middle" fill="currentColor" style="font-size:14px;">H₃(z)</text><path d="M345.0,212.0 L395.0,212.0" fill="none" stroke="currentColor" stroke-width="1.6" marker-end="url(#l10bh)" stroke-linejoin="round"/><rect x="395.0" y="194.0" width="74" height="36" rx="4" fill="var(--accent)" fill-opacity="0.16" stroke="currentColor" stroke-width="1.5"/><text x="432.0" y="217.0" text-anchor="middle" fill="currentColor" style="font-size:14px;">H₄(z)</text><path d="M469.0,40.0 L540.0,40.0 L540.0,107.0" fill="none" stroke="currentColor" stroke-width="1.6" marker-end="url(#l10bh)" stroke-linejoin="round"/><path d="M469.0,150.0 L534.0,150.0 L534.0,131.5" fill="none" stroke="currentColor" stroke-width="1.6" marker-end="url(#l10bh)" stroke-linejoin="round"/><path d="M469.0,212.0 L546.0,212.0 L546.0,131.5" fill="none" stroke="currentColor" stroke-width="1.6" marker-end="url(#l10bh)" stroke-linejoin="round"/><circle cx="540" cy="120" r="13" fill="none" stroke="currentColor" stroke-width="1.5"/><path d="M534.0,120.0 L546.0,120.0" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linejoin="round"/><path d="M540.0,114.0 L540.0,126.0" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linejoin="round"/><path d="M553.0,120.0 L590.0,120.0" fill="none" stroke="currentColor" stroke-width="1.6" marker-end="url(#l10bh)" stroke-linejoin="round"/><text x="596.0" y="125.0" text-anchor="start" fill="currentColor" style="font-size:13px;font-family:'STIX Two Math','Latin Modern Math','Cambria Math','Times New Roman',serif;font-style:italic;">y[n]</text><text x="300.0" y="30.0" text-anchor="middle" fill="var(--accent)" style="font-size:12px;">X H₁</text><text x="345.0" y="138.0" text-anchor="end" fill="var(--accent)" style="font-size:12px;">X H₁H₂</text><text x="500.0" y="32.0" text-anchor="start" fill="var(--accent)" style="font-size:12px;">X H₁H₅</text><text x="472.0" y="167.0" text-anchor="start" fill="var(--accent)" style="font-size:11px;">X H₁H₂H₃</text><text x="472.0" y="204.0" text-anchor="start" fill="var(--accent)" style="font-size:11px;">X H₁H₂H₄</text></svg><figcaption><strong>Slide 11: collapse the diagram by tracking signals.</strong> Label every wire with its z-transform (teal labels): the three paths into the adder carry XH₁H₅, XH₁H₂H₃ and XH₁H₂H₄. Adding them and dividing by X gives H(z) = H₁(z)[H₅(z) + H₂(z)(H₃(z) + H₄(z))].</figcaption></figure>

> [!success]- Answer (checked by simulating the diagram with random stable blocks)
> Track the z-transform on every wire: after $H_1$ the signal is $XH_1$; after $H_2$ it is $XH_1H_2$; the three wires into the adder carry $XH_1H_5$, $XH_1H_2H_3$, $XH_1H_2H_4$. So
> $$
> Y = X\,H_1\bigl(H_5 + H_2(H_3 + H_4)\bigr) \quad\Longrightarrow\quad H(z) = H_1(z)\Bigl[H_5(z) + H_2(z)\bigl(H_3(z) + H_4(z)\bigr)\Bigr].
> $$

> [!note]- Feedback loops (not in the Lecture 10 notes — for completeness)
> If the output is fed back through $F(z)$ and subtracted from the input before $G(z)$, then $E = X - FY$ and $Y = GE$, so $Y = G(X - FY)$ and
> $$
> H(z) = \frac{G(z)}{1 + G(z)F(z)} .
> $$
> The feedback part of every LCCDE is such a loop: $y[n] = x[n] - \sum_k a_k y[n-k]$ is $G = 1$, $F = \sum_k a_k z^{-k}$, which gives $H = \dfrac{1}{1 + \sum_k a_k z^{-k}}$ — Lecture 9's denominator; the input taps $\sum_k b_k z^{-k}$ then act in series with it (checked by simulating the loop sample by sample). No past Midterm 1 asks about feedback loops.

## 4. ROCs, stability and cancellation in combined systems

For $H_1 + H_2$ and for $H_1H_2$ the ROC is **at least** $\text{ROC}_1 \cap \text{ROC}_2$, and exactly that unless a zero of one factor cancels a pole that bounded the ROC. Consequences the exams love:

- **Stable + stable is stable**, in parallel and in series: both ROCs contain $|z| = 1$, so their intersection does (in time: $\sum|h_1 + h_2| \le \sum|h_1| + \sum|h_2|$ and $\sum|h_1 * h_2| \le \sum|h_1|\cdot\sum|h_2|$). FA2023 1(c), FA2024 1(c), SP2025 1(d): all **True**.
- **Unstable + unstable can be stable**, but only through cancellation. Parallel: $u[n]$ and $\delta[n] - u[n]$ are both unstable, their sum is $\delta[n]$ (FA2025 1(f), "always unstable": **False**). Series: $\dfrac{1-2z^{-1}}{1-3z^{-1}}\cdot\dfrac{1-3z^{-1}}{1-2z^{-1}} = 1$ (SP2021 1(c): **False**).
- **Unstable in series with stable can be stable**: $u[n] * (\delta[n] - \delta[n-1]) = \delta[n]$ (FA2019 1(d): **False**). HW4 #5 is the graded version: $h_1 = 2u[n] - 2(\tfrac12)^n u[n] \leftrightarrow \dfrac{z^{-1}}{(1-z^{-1})(1-\frac12 z^{-1})}$ has a pole at $1$ (unstable), $h_2 = \delta[n] - 3(\tfrac14)^n u[n-1] \leftrightarrow \dfrac{1-z^{-1}}{1-\frac14 z^{-1}}$ has a zero there, so
$$
H_1H_2 = \frac{z^{-1}}{(1-\frac12 z^{-1})(1-\frac14 z^{-1})}, \quad |z| > \tfrac12, \qquad h[n] = 4\Bigl[\left(\tfrac12\right)^n - \left(\tfrac14\right)^n\Bigr]u[n] \quad(\text{stable}).
$$
FA2019 #10(d) is the same idea: the zero of $H$ at $2$ cancels the pole of the unstable $2^n u[n]$ it is cascaded with, so "the overall system is unstable" is **False**.

> [!warning] Cancelled on paper, still there inside
> In HW4 #5 with $x = u[n]$ and $h_1$ first, the signal *between* the two blocks grows like $2n$ while the final output settles at $\tfrac83$ (checked numerically). The input–output system is stable; a real implementation of the first block would still overflow. Exams only ask about the input–output $H(z)$.

> [!exam] Where Lecture 10 shows up
> - **Improper $H(z)$ inside LCCDE problems** (family: [[problems/lccde-to-transfer-function-and-response|LCCDE ↔ H(z) ↔ response]], 7/7 exams): any numerator whose delays reach the denominator's — [[0-midterm-1/past-exams/fall-2025|FA2025 #6]] (equal degrees, $C_0 = \tfrac34$ if you invert $H$), [[0-midterm-1/past-exams/spring-2021|SP2021 #6]] (above). In [[homework/hw4|HW4]], #1(b) is improper and #3(a) only *looks* improper.
> - **System algebra with sequences**: [[0-midterm-1/past-exams/fall-2024|FA2024 #3]] (series: $x = \{\underset{\uparrow}{1}, -1\}$, $h_2 = \{\underset{\uparrow}{2}, 1\}$, $y = \{4, \underset{\uparrow}{-2}, -2\}$ ⇒ $h_1 = 2\delta[n+1]$, overall $h = \{4, \underset{\uparrow}{2}\}$, non-causal); [[0-midterm-1/past-exams/spring-2025|SP2025 #3]] (parallel: $h_1 = \delta[n-1]$ and the data force $h_2 = \delta[n+1]$, overall $h = \{1, \underset{\uparrow}{0}, 1\}$, non-causal). Family: [[problems/finding-h-from-input-output-pairs|finding h from input–output pairs]].
> - **Cascades and cancellation**: [[0-midterm-1/past-exams/fall-2019|FA2019 #10(d)]], HW4 #5, and the T/F items above — collected in the [[0-midterm-1/true-false-bank|T/F bank]].

## Related

[[concepts/system-algebra|system algebra]] · [[concepts/pole-zero-cancellation|pole-zero cancellation]] · [[concepts/partial-fraction-expansion|partial-fraction expansion]] · [[concepts/inverse-z-transform|inverse z-transform]] · [[concepts/transfer-function|transfer function]] · [[concepts/block-diagram|block diagram]] · [[concepts/bibo-stability|BIBO stability]] · [[0-toolkit/04-factoring-and-long-division|factoring and long division]] · [[homework/hw4|HW4]] · unit: [[2-z-transform/index|Unit 2]]

### Sources for this page

Snyder, *ECE 310 Lecture 10* notes (§1 improper rational expressions, §1.1 Exercise 1 with long division, §1.2 the numerator-equals-1 approach, §2 system algebra, Table 1, Fig. 1) and slides 1–11 with the annotated in-class work (slides 5–8 both approaches, 9–10 series/parallel, 11 system-algebra example). HW4 #1, #3(a), #5. Past exams FA2025 #1(f), #6; SP2025 #1(d), #3; FA2024 #1(c), #3; FA2023 #1(c), #1(e); SP2021 #1(c), #6; FA2019 #1(d), #10(d). Every number is checked in `verify/lectures/l10_verify.py`.
