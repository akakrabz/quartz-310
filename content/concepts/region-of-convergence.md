---
title: "Region of convergence (ROC)"
description: "The set of z where the z-transform sum converges — a ring bounded by pole radii that makes X(z) unique and tells you, at a glance, whether a system is causal and whether it is BIBO stable."
tags: [concept, z-transform, roc, stability]
aliases: ["ROC", "region of convergence"]
---

> [!key] Definition
> The ROC of $X(z) = \sum_{n=-\infty}^{\infty} x[n]\,z^{-n}$ is the set of $z$ for which this sum converges. Convergence depends only on $|z|$, so the ROC is always a **ring** centred at the origin:
> $$
> r_1 < |z| < r_2, \qquad 0 \le r_1 < r_2 \le \infty ,
> $$
> possibly together with the point $z=0$ (when $r_1=0$) or $z=\infty$ (when $r_2=\infty$).
> A formula for $X(z)$ **plus** its ROC is one signal; the formula alone is not an answer. Outside the ROC, $X(z)$ is simply undefined, even where the formula returns a number.

**Why the ROC is part of the answer.** $u[n]$ and $-u[-n-1]$ have the same formula $\dfrac{1}{1-z^{-1}}$; only the ROCs differ ($|z|>1$ versus $|z|<1$) ([[2-z-transform/06-the-z-transform|Lecture 6]]). And $(\tfrac12)^n u[n] \leftrightarrow \dfrac{1}{1-\frac12 z^{-1}}$, $|z|>\tfrac12$, "evaluates" to $-1$ at $z=\tfrac14$, but the sum there is $\sum_n 2^n = \infty$ ([[2-z-transform/07-z-transform-properties|Lecture 7]]).

## The rules

> [!key] ROC rules (Lecture 7)
> 1. The ROC contains **no poles**; zeros are allowed anywhere.
> 2. The ROC is **connected**: one ring, never two pieces.
> 3. **Right-sided** ($x[n]=0$ for $n<n_0$): outside the largest pole, $|z| > |p_{\max}|$.
> 4. **Left-sided** ($x[n]=0$ for $n>n_0$): inside the smallest pole, $|z| < |p_{\min}|$.
> 5. **Two-sided**: an annulus $a<|z|<b$ between two consecutive pole radii.
> 6. **Finite-length**: the whole plane, except $z=0$ if some $x[n]\neq 0$ with $n>0$, and $z=\infty$ if some $x[n]\neq0$ with $n<0$.
>
> The edges $0$ and $\infty$ follow the same logic for infinite sequences: a right-sided sequence that starts at $n_0<0$ has ROC $|p_{\max}|<|z|<\infty$; a left-sided one that ends at $n_0>0$ has $0<|z|<|p_{\min}|$ (see [[concepts/sided-sequences|sided sequences]]).

<figure class="ece-fig"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 660 270" width="660" height="270" role="img" style="font-family:'Source Sans 3','Source Sans Pro',system-ui,sans-serif;font-size:14px"><defs><marker id="ahroc" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="context-stroke"/></marker></defs><clipPath id="rocout"><rect x="23.0" y="18.0" width="184.0" height="184.0"/></clipPath><path d="M23.0,18.0 h184.0 v184.0 h-184.0 Z M141.00,110.00 A26.00,26.00 0 1,0 89.00,110.00 A26.00,26.00 0 1,0 141.00,110.00 Z" fill="var(--accent)" fill-opacity="0.22" fill-rule="evenodd" stroke="none" clip-path="url(#rocout)"/><circle cx="115.0" cy="110.0" r="26.0" fill="none" stroke="var(--accent)" stroke-width="1.4"/><line x1="23.0" y1="110.0" x2="207.0" y2="110.0" stroke="currentColor" stroke-width="1.1" opacity="0.8" stroke-linecap="round"/><line x1="115.0" y1="18.0" x2="115.0" y2="202.0" stroke="currentColor" stroke-width="1.1" opacity="0.8" stroke-linecap="round"/><circle cx="115.0" cy="110.0" r="52.0" fill="none" stroke="currentColor" stroke-width="1.3" stroke-dasharray="5 4"/><line x1="109.0" y1="78.0" x2="121.0" y2="90.0" stroke="var(--hi)" stroke-width="2.4" stroke-linecap="round"/><line x1="109.0" y1="90.0" x2="121.0" y2="78.0" stroke="var(--hi)" stroke-width="2.4" stroke-linecap="round"/><line x1="109.0" y1="130.0" x2="121.0" y2="142.0" stroke="var(--hi)" stroke-width="2.4" stroke-linecap="round"/><line x1="109.0" y1="142.0" x2="121.0" y2="130.0" stroke="var(--hi)" stroke-width="2.4" stroke-linecap="round"/><text x="205.0" y="135.0" text-anchor="end" fill="var(--muted)" style="font-size:12px;">Re</text><text x="121.0" y="31.0" text-anchor="start" fill="var(--muted)" style="font-size:12px;">Im</text><text x="115.0" y="224.0" text-anchor="middle" fill="currentColor" style="font-size:14px;font-weight:600;">(a) causal: |z| &gt; ½</text><text x="115.0" y="242.0" text-anchor="middle" fill="var(--muted)" style="font-size:13px;">h = (½)ⁿ cos(πn/2) u[n]</text><clipPath id="rocin"><rect x="238.0" y="18.0" width="184.0" height="184.0"/></clipPath><path d="M408.00,110.00 A78.00,78.00 0 1,0 252.00,110.00 A78.00,78.00 0 1,0 408.00,110.00 Z" fill="var(--accent)" fill-opacity="0.22" fill-rule="evenodd" stroke="none" clip-path="url(#rocin)"/><circle cx="330.0" cy="110.0" r="78.0" fill="none" stroke="var(--accent)" stroke-width="1.4"/><line x1="238.0" y1="110.0" x2="422.0" y2="110.0" stroke="currentColor" stroke-width="1.1" opacity="0.8" stroke-linecap="round"/><line x1="330.0" y1="18.0" x2="330.0" y2="202.0" stroke="currentColor" stroke-width="1.1" opacity="0.8" stroke-linecap="round"/><circle cx="330.0" cy="110.0" r="52.0" fill="none" stroke="currentColor" stroke-width="1.3" stroke-dasharray="5 4"/><line x1="402.0" y1="104.0" x2="414.0" y2="116.0" stroke="var(--hi)" stroke-width="2.4" stroke-linecap="round"/><line x1="402.0" y1="116.0" x2="414.0" y2="104.0" stroke="var(--hi)" stroke-width="2.4" stroke-linecap="round"/><text x="420.0" y="135.0" text-anchor="end" fill="var(--muted)" style="font-size:12px;">Re</text><text x="336.0" y="31.0" text-anchor="start" fill="var(--muted)" style="font-size:12px;">Im</text><text x="330.0" y="224.0" text-anchor="middle" fill="currentColor" style="font-size:14px;font-weight:600;">(b) left-sided: |z| &lt; 3/2</text><text x="330.0" y="242.0" text-anchor="middle" fill="var(--muted)" style="font-size:13px;">h = −(3/2)ⁿ u[−n−1]</text><clipPath id="rocann"><rect x="453.0" y="18.0" width="184.0" height="184.0"/></clipPath><path d="M623.00,110.00 A78.00,78.00 0 1,0 467.00,110.00 A78.00,78.00 0 1,0 623.00,110.00 Z M571.00,110.00 A26.00,26.00 0 1,0 519.00,110.00 A26.00,26.00 0 1,0 571.00,110.00 Z" fill="var(--accent)" fill-opacity="0.22" fill-rule="evenodd" stroke="none" clip-path="url(#rocann)"/><circle cx="545.0" cy="110.0" r="26.0" fill="none" stroke="var(--accent)" stroke-width="1.4"/><circle cx="545.0" cy="110.0" r="78.0" fill="none" stroke="var(--accent)" stroke-width="1.4"/><line x1="453.0" y1="110.0" x2="637.0" y2="110.0" stroke="currentColor" stroke-width="1.1" opacity="0.8" stroke-linecap="round"/><line x1="545.0" y1="18.0" x2="545.0" y2="202.0" stroke="currentColor" stroke-width="1.1" opacity="0.8" stroke-linecap="round"/><circle cx="545.0" cy="110.0" r="52.0" fill="none" stroke="currentColor" stroke-width="1.3" stroke-dasharray="5 4"/><line x1="539.0" y1="78.0" x2="551.0" y2="90.0" stroke="var(--hi)" stroke-width="2.4" stroke-linecap="round"/><line x1="539.0" y1="90.0" x2="551.0" y2="78.0" stroke="var(--hi)" stroke-width="2.4" stroke-linecap="round"/><line x1="539.0" y1="130.0" x2="551.0" y2="142.0" stroke="var(--hi)" stroke-width="2.4" stroke-linecap="round"/><line x1="539.0" y1="142.0" x2="551.0" y2="130.0" stroke="var(--hi)" stroke-width="2.4" stroke-linecap="round"/><line x1="617.0" y1="104.0" x2="629.0" y2="116.0" stroke="var(--hi)" stroke-width="2.4" stroke-linecap="round"/><line x1="617.0" y1="116.0" x2="629.0" y2="104.0" stroke="var(--hi)" stroke-width="2.4" stroke-linecap="round"/><text x="635.0" y="135.0" text-anchor="end" fill="var(--muted)" style="font-size:12px;">Re</text><text x="551.0" y="31.0" text-anchor="start" fill="var(--muted)" style="font-size:12px;">Im</text><text x="545.0" y="224.0" text-anchor="middle" fill="currentColor" style="font-size:14px;font-weight:600;">(c) two-sided: ½ &lt; |z| &lt; 3/2</text><text x="545.0" y="242.0" text-anchor="middle" fill="var(--muted)" style="font-size:13px;">sum of (a) and (b)</text></svg><figcaption><strong>The three ROC shapes (Lecture 11, Fig. 2).</strong> Poles × in red, ROC shaded, unit circle dashed. (a) A causal sequence converges <em>outside</em> its largest pole (poles ±j/2). (b) A left-sided sequence converges <em>inside</em> its smallest pole (3/2). (c) Their sum converges only where both do: the annulus between the poles. Here the annulus contains the unit circle, so this two-sided h[n] is BIBO stable.</figcaption></figure>

## What the ROC says about the system

For an LTI system, the ROC of $H(z)$ encodes both [[concepts/causality|causality]] and [[concepts/bibo-stability|BIBO stability]] ([[2-z-transform/11-bibo-stability-and-causality|Lecture 11]]):

> [!key] Stable $\iff$ the ROC of $H(z)$ contains the unit circle $|z|=1$. Causal $\iff$ the ROC is the outside of a circle **and includes** $z=\infty$.

| ROC of $H(z)$ | causality type | right-sided | left-sided | stable iff |
|---|---|---|---|---|
| $\lvert z\rvert > \lvert p_{\max}\rvert$ | causal | ✓ | ✗ | $\lvert p_{\max}\rvert < 1$ |
| $\lvert z\rvert < \lvert p_{\min}\rvert$ | anti-causal | ✗ | ✓ | $\lvert p_{\min}\rvert > 1$ |
| $\lvert p_{\max}\rvert < \lvert z\rvert < \infty$ | non-causal | ✓ | ✗ | $\lvert p_{\max}\rvert < 1$ |
| $0 < \lvert z\rvert < \lvert p_{\min}\rvert$ | non-causal | ✗ | ✓ | $\lvert p_{\min}\rvert > 1$ |
| $a < \lvert z\rvert < b$ | non-causal (two-sided) | ✓ | ✓ | $a < 1 < b$ |

So "causal **and** stable" means every pole strictly inside the unit circle; "stable" alone means: choose the ring that contains $|z|=1$ (if no pole sits on the unit circle, exactly one ring does).

## All possible ROCs

> [!recipe] Listing every ROC of a rational $X(z)$
> 1. Factor the denominator; list the **distinct pole radii** $r_1 < r_2 < \dots < r_K$.
> 2. The candidates are $|z|<r_1$, $\;r_1<|z|<r_2,\ \dots,\ \;|z|>r_K$: that is $K+1$ rings. Poles of equal magnitude (a conjugate pair, $\pm j/2$) share one boundary circle.
> 3. For each ring, every [[concepts/partial-fraction-expansion|PFE]] term with its pole **inside** the ring's inner edge is right-sided, $A\,p^n u[n]$; every term with its pole **outside** the outer edge is left-sided, $-A\,p^n u[-n-1]$.
> 4. Pick the one the problem wants: causal → outermost; stable → the ring containing $|z|=1$; "two-sided" → a middle ring.

> [!example] Lecture 7, Example 1: $X(z) = \dfrac{1+3z^{-1}}{1+\frac74 z^{-1}-\frac12 z^{-2}}$
> Factor: $1+\frac74 z^{-1}-\frac12 z^{-2} = (1+2z^{-1})(1-\frac14 z^{-1})$, so poles at $-2$ and $\tfrac14$ (zero at $-3$). Radii $\tfrac14 < 2$ → three ROCs. PFE (cover-up):
> $$
> X(z) = \frac{-\frac49}{1+2z^{-1}} + \frac{\frac{13}{9}}{1-\frac14 z^{-1}} .
> $$

> [!success]- The three signals
> - $|z|>2$ (right-sided, causal, unstable): $x[n] = -\tfrac49(-2)^n u[n] + \tfrac{13}{9}\left(\tfrac14\right)^n u[n]$.
> - $|z|<\tfrac14$ (left-sided, anti-causal, unstable): $x[n] = \tfrac49(-2)^n u[-n-1] - \tfrac{13}{9}\left(\tfrac14\right)^n u[-n-1]$.
> - $\tfrac14<|z|<2$ (two-sided, the only **stable** choice): $x[n] = \tfrac{13}{9}\left(\tfrac14\right)^n u[n] + \tfrac49(-2)^n u[-n-1]$.
>
> Each was checked by summing $\sum x[n]z^{-n}$ numerically at a point inside its ROC.

A combination can also be **empty**: in [[2-z-transform/08-inverse-z-transform|Lecture 8]] Example 3 (poles $\tfrac43$, $\tfrac23$), taking the $\tfrac43$ term right-sided and the $\tfrac23$ term left-sided needs $|z|>\tfrac43$ and $|z|<\tfrac23$ at once — no such $z$, so that "signal" has no z-transform. FA2019 #7 has the same fourth, empty case.

> [!trap]
> - **No ROC, no credit.** Every z-transform answer needs "ROC: …"; every inverse needs the ROC to decide each term's side.
> - The ROC is a **ring in $|z|$**, never a half-plane (that is the Laplace transform).
> - Poles on the **same circle** cannot be split between sides: $\pm j/2$ or $e^{\pm j\omega_0}$ are both right-sided or both left-sided.
> - **Zeros are allowed in the ROC** — FA2023 T/F (b) ("the ROC cannot contain any poles or zeros") is False.
> - **Right-sided is not causal.** $\delta[n+1]+\delta[n] \leftrightarrow z+1$ has ROC $|z|<\infty$: right-sided, non-causal (SP2023 T/F (c) is False for this reason).
> - After a [[concepts/pole-zero-cancellation|pole-zero cancellation]], the ROC is set by the poles that **remain**, so it can be larger than $R_1\cap R_2$ (SP2021 #7, HW4 #5).
> - An everlasting two-sided signal like $e^{j\pi n/4}$ (all $n$) needs $|z|>1$ and $|z|<1$ at once: **empty ROC**, no z-transform (SP2025 T/F (c), True).

**Where it appears.**
- Lectures: [[2-z-transform/06-the-z-transform|L6]] (definition), [[2-z-transform/07-z-transform-properties|L7]] (rules), [[2-z-transform/08-inverse-z-transform|L8]] (all ROCs), [[2-z-transform/11-bibo-stability-and-causality|L11]] (causality/stability table).
- Problem families: [[problems/z-transform-with-roc]], [[problems/all-possible-rocs]], [[problems/parameters-for-stability]], [[problems/two-sided-systems-as-recursions]].
- Homework: [[homework/hw3|HW3]] #1, #3, #4; [[homework/hw4|HW4]] #1, #3.
- Past exams: [[0-midterm-1/past-exams/fall-2025|FA2025]] #5, #7, T/F (c); [[0-midterm-1/past-exams/spring-2025|SP2025]] #5, #8, T/F (c), (e), (f); [[0-midterm-1/past-exams/fall-2024|FA2024]] #5, #8a, T/F (f); [[0-midterm-1/past-exams/fall-2023|FA2023]] #5, #6, T/F (b), (f); [[0-midterm-1/past-exams/spring-2021|SP2021]] #7, T/F (a); [[0-midterm-1/past-exams/fall-2019|FA2019]] #5, #7. Explore it live in the [[demos/pole-zero-and-roc-explorer|pole-zero and ROC explorer]].

Related: [[concepts/z-transform]] · [[concepts/poles-and-zeros]] · [[concepts/sided-sequences]] · [[concepts/bibo-stability]] · [[concepts/causality]] · [[concepts/inverse-z-transform]] · [[concepts/marginal-stability]] · [[concepts/pole-zero-cancellation]]

### Sources for this page
Lecture 6 notes §2 (ROC definition, $u[n]$ vs $-u[-n-1]$); Lecture 7 notes §1 (ROC rules, the $X(\tfrac14)=-1$ remark) and slides (Example 1); Lecture 8 slides (Example 3, all possible ROCs); Lecture 11 notes §1.1 (Table 1, Fig. 2) and slides; past-exam keys cited above. All sequences on this page were checked numerically (`verify/concepts/verify_zdomain_extra.py`, `verify_pfe.py`).
