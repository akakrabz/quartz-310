---
title: "All possible ROCs (inverse z by partial fractions)"
description: "Recipe for the inverse z-transform when no ROC is given: cancel, factor, partial fractions, list every annulus between the pole magnitudes, match each term to right- or left-sided, and pick the stable or causal one. Three fresh practice problems."
tags: [problem-family, problem, midterm-1, z-transform, roc, stability]
family_frequency: "7 of 7 exams"
typical_points: "15–20"
lectures: [7, 8, 10, 11]
---

*Problem family · on 7 of 7 past midterms · typically 15–20 pts · uses [[2-z-transform/07-z-transform-properties|Lecture 7]], [[2-z-transform/08-inverse-z-transform|Lecture 8]], [[2-z-transform/10-improper-transfer-functions-and-system-algebra|Lecture 10]], [[2-z-transform/11-bibo-stability-and-causality|Lecture 11]] · concepts: [[concepts/partial-fraction-expansion]], [[concepts/region-of-convergence]], [[concepts/sided-sequences]], [[concepts/pole-zero-cancellation]]*

> [!abstract] In one breath
> A rational $X(z)$ **without** an ROC is not one signal but several: one for each annulus between consecutive pole magnitudes. Factor, do the partial fractions once, then for each annulus make every pole *inside* it a right-sided term $A\,p^n u[n]$ and every pole *outside* it a left-sided term $-A\,p^n u[-n-1]$. "BIBO stable" picks the annulus containing $\lvert z\rvert = 1$; "causal" picks the outermost one.

## What it looks like on the exam

You get $X(z)$ or $H(z)$ as a ratio of polynomials, usually with two poles (sometimes written in positive powers of $z$), and one of these questions:

1. **"Determine all possible ROCs and the corresponding $x[n]$ for each."** The pure version (FA2023, FA2019, HW4).
2. **"The system is BIBO stable. Find $h[n]$."** The ROC is not given but is fixed by the word *stable*: it is the annulus that contains the unit circle, which often makes $h[n]$ two-sided (FA2025, SP2025).
3. **"The system is causal"** (or "right-sided"): the ROC is outside the largest pole (FA2024, SP2023, HW3 #4).

Every past midterm has at least one of the three, usually worth 15–20 points, and it is often part (a) of a longer problem whose later parts use the $h[n]$ you found ([[problems/two-sided-systems-as-recursions|two-sided recursions]], [[problems/lccde-to-transfer-function-and-response|LCCDE and response]]).

| where | what is asked | poles | result |
|---|---|---|---|
| [[0-midterm-1/past-exams/fall-2025\|FA2025 #7a]] | stable $h$ of $\dfrac{1-z^{-1}}{(1+2z^{-1})(1+\frac23z^{-1})}$ | $-2,\ -\tfrac23$ | ROC $\tfrac23<\lvert z\rvert<2$, $h=-\tfrac94(-2)^nu[-n-1]-\tfrac54(-\tfrac23)^nu[n]$ |
| [[0-midterm-1/past-exams/spring-2025\|SP2025 #8b,c]] | all possible outputs; stable $h$ | $\tfrac12,\ -\tfrac32$ | two outputs; ROC $\tfrac12<\lvert z\rvert<\tfrac32$, $h=-(\tfrac12)^nu[n]-3(-\tfrac32)^nu[-n-1]$ |
| [[0-midterm-1/past-exams/fall-2024\|FA2024 #7a,b]] | causal: sketch ROC, find $h$ | $\tfrac12,\ 2$ | $\lvert z\rvert>2$, $h=-\tfrac13(\tfrac12)^nu[n]+\tfrac43\,2^nu[n]$ |
| [[0-midterm-1/past-exams/fall-2023\|FA2023 #6a]] | all possible ROCs of $\dfrac{1-z^{-1}}{(1-\frac12z^{-1})(1-2z^{-1})}$ | $\tfrac12,\ 2$ | $A_1=\tfrac13$, $A_2=\tfrac23$; three ROCs, the fourth combination is empty |
| [[0-midterm-1/past-exams/spring-2023\|SP2023 #6a,b]] | $H=Y/X$, causal and stable, find $h$ | $\tfrac12,\ \tfrac14$ | $\lvert z\rvert>\tfrac12$, $h=-6(\tfrac12)^nu[n]+7(\tfrac14)^nu[n]$ |
| [[0-midterm-1/past-exams/spring-2021\|SP2021 #5a]] | $h$ of $\dfrac{3z^{-1}}{1+z^{-2}}$, $\lvert z\rvert>1$ | $\pm j$ | $h=3\sin(\tfrac{\pi}{2}n)u[n]$ |
| [[0-midterm-1/past-exams/spring-2021\|SP2021 #7]] | $X$, $H=Y/X$, ROC of $Y$, $h$ | $\tfrac12,\ 1$ ($4$ cancels) | ROC$_Y$ $\lvert z\rvert>1$, $h=7(\tfrac12)^nu[n]-6u[n]$ |
| [[0-midterm-1/past-exams/fall-2019\|FA2019 #6]] | inverse of $1+z^{-100}+\dfrac{1}{1-5z^{-1}}$, $\lvert z\rvert>5$ | $5$ | $\delta[n]+\delta[n-100]+5^nu[n]$ |
| [[0-midterm-1/past-exams/fall-2019\|FA2019 #7]] | all valid ROCs of $\dfrac{z}{z-e^{j\pi/3}}+\dfrac{z}{z-0.5}$ | $e^{j\pi/3},\ \tfrac12$ | $\lvert z\rvert>1$, $\lvert z\rvert<\tfrac12$, $\tfrac12<\lvert z\rvert<1$ (fourth is empty) |
| [[homework/hw4\|HW4 #1]] | all possible ROCs, three transforms | (b): $(z+1)$ cancels | (a), (c): three ROCs each; (b): two ROCs, improper |
| [[homework/hw3\|HW3 #3c, #4]] | $h$ for a given ROC; right-sided $H$ | | two-sided $h_3$ on $\tfrac14<\lvert z\rvert<\tfrac32$; $\lvert z\rvert>\tfrac23$ |
| [[2-z-transform/08-inverse-z-transform\|Lecture 8]] | Exercise 1; slides Example 3 | $\tfrac13,2$; $\tfrac43,\tfrac23$ | $A=\tfrac15,\tfrac95$; $A=2,-1$ |
| [[2-z-transform/11-bibo-stability-and-causality\|Lecture 11]] | slide 10: the stable $h$ of two given $H$ | $\tfrac12,-\tfrac43$; $\tfrac15,\tfrac45$ | two-sided (non-causal); causal |

All exam answers above are checked against the keys on the past-exam pages.

<figure class="ece-fig">
<svg viewBox="0 0 600 232" width="100%" style="max-width:620px" role="img" aria-label="Three z-plane panels with two poles at radii a and b: the ROC inside a, between a and b, and outside b">
<g transform="translate(10,8)">
<circle cx="90" cy="90" r="25" fill="var(--accent)" fill-opacity="0.22"/>
<line x1="0" y1="90" x2="180" y2="90" stroke="currentColor" stroke-opacity="0.35"/><line x1="90" y1="0" x2="90" y2="180" stroke="currentColor" stroke-opacity="0.35"/>
<circle cx="90" cy="90" r="50" fill="none" stroke="currentColor" stroke-opacity="0.6" stroke-dasharray="4 3"/>
<circle cx="90" cy="90" r="25" fill="none" stroke="var(--accent)" stroke-width="1.4"/><circle cx="90" cy="90" r="72" fill="none" stroke="var(--accent)" stroke-width="1.4"/>
<path d="M60,85 l10,10 M70,85 l-10,10 M157,85 l10,10 M167,85 l-10,10" stroke="var(--hi)" stroke-width="2.2"/>
<text x="90" y="200" text-anchor="middle" font-size="13" fill="currentColor">|z| &lt; a : both left-sided</text>
</g>
<g transform="translate(210,8)">
<path d="M18,90 a72,72 0 1,0 144,0 a72,72 0 1,0 -144,0 Z M65,90 a25,25 0 1,0 50,0 a25,25 0 1,0 -50,0 Z" fill="var(--accent)" fill-opacity="0.22" fill-rule="evenodd"/>
<line x1="0" y1="90" x2="180" y2="90" stroke="currentColor" stroke-opacity="0.35"/><line x1="90" y1="0" x2="90" y2="180" stroke="currentColor" stroke-opacity="0.35"/>
<circle cx="90" cy="90" r="50" fill="none" stroke="currentColor" stroke-opacity="0.6" stroke-dasharray="4 3"/>
<circle cx="90" cy="90" r="25" fill="none" stroke="var(--accent)" stroke-width="1.4"/><circle cx="90" cy="90" r="72" fill="none" stroke="var(--accent)" stroke-width="1.4"/>
<path d="M60,85 l10,10 M70,85 l-10,10 M157,85 l10,10 M167,85 l-10,10" stroke="var(--hi)" stroke-width="2.2"/>
<text x="90" y="200" text-anchor="middle" font-size="13" fill="currentColor">a &lt; |z| &lt; b : two-sided</text>
<text x="90" y="218" text-anchor="middle" font-size="12" fill="var(--accent2)">contains |z| = 1 → stable</text>
</g>
<g transform="translate(410,8)">
<path d="M0,0 H180 V180 H0 Z M18,90 a72,72 0 1,0 144,0 a72,72 0 1,0 -144,0 Z" fill="var(--accent)" fill-opacity="0.22" fill-rule="evenodd"/>
<line x1="0" y1="90" x2="180" y2="90" stroke="currentColor" stroke-opacity="0.35"/><line x1="90" y1="0" x2="90" y2="180" stroke="currentColor" stroke-opacity="0.35"/>
<circle cx="90" cy="90" r="50" fill="none" stroke="currentColor" stroke-opacity="0.6" stroke-dasharray="4 3"/>
<circle cx="90" cy="90" r="25" fill="none" stroke="var(--accent)" stroke-width="1.4"/><circle cx="90" cy="90" r="72" fill="none" stroke="var(--accent)" stroke-width="1.4"/>
<path d="M60,85 l10,10 M70,85 l-10,10 M157,85 l10,10 M167,85 l-10,10" stroke="var(--hi)" stroke-width="2.2"/>
<text x="90" y="200" text-anchor="middle" font-size="13" fill="currentColor">|z| &gt; b : both right-sided</text>
<text x="90" y="218" text-anchor="middle" font-size="12" fill="var(--muted)">causal (if no positive powers of z)</text>
</g>
</svg>
<figcaption><strong>Two pole magnitudes, three ROCs.</strong> Poles (×) at radii a &lt; 1 &lt; b; the dashed circle is |z| = 1. The ROC never contains a pole, so it is a disc, an annulus or an exterior bounded by pole circles. The fourth sign pattern (the pole at a right-sided, the pole at b left-sided) would need |z| &gt; b and |z| &lt; a at once: empty, not an answer.</figcaption>
</figure>

## The recipe

> [!recipe] All possible ROCs, step by step
> 1. **Clean up $X(z)$.** Rewrite in powers of $z^{-1}$ (divide numerator and denominator by the highest power of $z$ in the denominator). **Cancel common factors** of numerator and denominator; a cancelled pole is not a pole and does not create an ROC boundary.
> 2. **Proper?** If the numerator degree in $z^{-1}$ is $\geq$ the denominator degree, do long division first ([[2-z-transform/10-improper-transfer-functions-and-system-algebra|Lecture 10]]), or pull out a pure shift $z^{k}$ and use the shift property. Leftover terms $C_k z^{-k}$ invert to $C_k\,\delta[n-k]$ in every ROC.
> 3. **Factor the denominator**, $\prod_k (1-p_kz^{-1})$, and list the **distinct pole magnitudes** $r_1<r_2<\dots<r_m$ (a conjugate pair, or $p$ and $-p$, share one magnitude).
> 4. **Partial fractions once:** $X(z)=\sum_k \dfrac{A_k}{1-p_kz^{-1}}$ with the cover-up rule $A_k = \Big[(1-p_kz^{-1})X(z)\Big]_{z=p_k}$.
> 5. **List the ROCs:** $\lvert z\rvert<r_1$, $\ r_1<\lvert z\rvert<r_2$, …, $\lvert z\rvert>r_m$. That is $m+1$ ROCs, not $2^{\#\text{poles}}$.
> 6. **For each ROC, invert term by term:** pole inside the ROC's inner circle ($\lvert p_k\rvert\le$ inner radius) → right-sided $A_k\,p_k^n\,u[n]$; pole outside ($\lvert p_k\rvert\ge$ outer radius) → left-sided $-A_k\,p_k^n\,u[-n-1]$.
> 7. **Name them:** the ROC containing $\lvert z\rvert=1$ is the **BIBO stable** one (if a pole sits on the unit circle, there is none); the outermost $\lvert z\rvert>r_m$ is the **causal** one (provided there are no positive powers $z^{k}$ left, which exclude $\infty$); the innermost is **anti-causal** (left-sided).
>
> **Checks.** (i) Recombine: $\sum_k A_k/(1-p_kz^{-1})$ at one convenient $z$ (e.g. $z=1$) must equal $X(z)$ there. (ii) For a proper $X$, $\sum_k A_k = X(\infty) = b_0$, which is also $x[0]$ of the causal answer. (iii) Every ROC excludes all poles, and the stable one contains the unit circle.

> [!trap] Where the points go
> - **A zero cancels a pole.** HW4 #1(b): $\dfrac{z^3-z}{z^2+3z+2}=\dfrac{z(z-1)(z+1)}{(z+1)(z+2)}$. Not cancelling $(z+1)$ gives three ROCs; the right answer has two. Always factor the numerator too.
> - **Improper fraction.** Cover-up on an improper fraction gives wrong $A_k$ and loses the $\delta$ terms. Divide first, or split off $z^k$ (HW4 #1b, [[2-z-transform/10-improper-transfer-functions-and-system-algebra|Lecture 10]]).
> - **The left-sided pair has a minus sign and $u[-n-1]$:** $\dfrac{1}{1-pz^{-1}},\ \lvert z\rvert<\lvert p\rvert \ \longleftrightarrow\ -p^n u[-n-1]$. Writing $+p^nu[-n-1]$ or $u[-n]$ are the two most common deductions.
> - **"All possible" means the non-empty ones.** With poles at $a<b$ there are three ROCs. The pattern "outer pole right-sided, inner pole left-sided" converges nowhere; the FA2023 key notes it only to say it is *not* an answer.
> - **Equal magnitudes move together.** Complex-conjugate poles (or $\pm p$) are on the same circle, so they are always on the same side. Two poles on one circle give two ROCs, not four.
> - **Stability means the unit circle, not "the middle one".** If both poles are inside the unit circle, the stable ROC is the *outer* one (SP2023 #6); if a pole is on $\lvert z\rvert=1$ (FA2019 #7: $e^{j\pi/3}$), no ROC is stable.
> - **Positive powers of $z$.** $\dfrac{z}{z-p} = \dfrac{1}{1-pz^{-1}}$, but $\dfrac{1}{z-p} = \dfrac{z^{-1}}{1-pz^{-1}}$ gives $p^{n-1}u[n-1]$. A leftover factor $z$ gives $\delta[n+1]$: right-sided, stable perhaps, but **not causal**.

## Practice problems

> [!question] Practice 1 — factor first, then three ROCs
> $$
> X(z) = \frac{3-\frac43 z^{-1}}{1-\frac53 z^{-1}-\frac23 z^{-2}}
> $$
> (a) Find the poles and all possible ROCs. (b) Find $x[n]$ for each ROC. (c) Which ROC gives an absolutely summable $x[n]$, and which one a causal $x[n]$?

> [!success]- Solution
> **(a) Poles.** In positive powers of $z$ the denominator is $z^2-\frac53z-\frac23 = \frac13(3z+1)(z-2)$, so
> $$
> X(z) = \frac{3-\frac43 z^{-1}}{(1+\frac13 z^{-1})(1-2z^{-1})},\qquad p_1=-\tfrac13,\quad p_2 = 2 .
> $$
> The numerator's zero is at $z=\frac49$: no cancellation. Two distinct magnitudes, so three ROCs: $\lvert z\rvert<\frac13$, $\ \frac13<\lvert z\rvert<2$, $\ \lvert z\rvert>2$.
>
> **Partial fractions.** $X = \dfrac{A}{1+\frac13z^{-1}}+\dfrac{B}{1-2z^{-1}}$, cover-up with $z^{-1}=-3$ and $z^{-1}=\frac12$:
> $$
> A = \frac{3-\frac43(-3)}{1-2(-3)} = \frac{7}{7}=1,\qquad B = \frac{3-\frac43\cdot\frac12}{1+\frac13\cdot\frac12} = \frac{7/3}{7/6} = 2 .
> $$
> Check: $A+B = 3 = b_0$ ✓, and at $z=1$: $\frac{3-4/3}{1-5/3-2/3} = -\frac54 = \frac{1}{4/3}+\frac{2}{-1}$ ✓.
>
> **(b)**
> $$
> \begin{aligned}
> \lvert z\rvert>2:&\quad x[n] = \left(-\tfrac13\right)^n u[n] + 2\,(2)^n u[n] \\
> \tfrac13<\lvert z\rvert<2:&\quad x[n] = \left(-\tfrac13\right)^n u[n] - 2\,(2)^n u[-n-1] \\
> \lvert z\rvert<\tfrac13:&\quad x[n] = -\left(-\tfrac13\right)^n u[-n-1] - 2\,(2)^n u[-n-1]
> \end{aligned}
> $$
> ($-\frac13$ right-sided with $2$ left-sided is the middle case; the reverse would need $\lvert z\rvert>2$ and $\lvert z\rvert<\frac13$: empty.)
>
> **(c)** Only $\frac13<\lvert z\rvert<2$ contains the unit circle, so the two-sided $x[n]$ is the absolutely summable one ($\sum\lvert x\rvert = \frac32 + 2 = \frac72$). The causal one is $\lvert z\rvert>2$; it grows like $2^n$.

> [!question] Practice 2 — a cancelled pole and an improper fraction
> $$
> X(z) = \frac{z^3-4z}{z^2-\frac32 z-1}
> $$
> Find all possible ROCs and the corresponding $x[n]$. Is any of them stable? Causal?

> [!success]- Solution
> **Factor everything.** $z^3-4z = z(z-2)(z+2)$ and $z^2-\frac32z-1 = (z-2)(z+\frac12)$. The factor $(z-2)$ cancels:
> $$
> X(z) = \frac{z(z+2)}{z+\frac12} = z\cdot\frac{1+2z^{-1}}{1+\frac12 z^{-1}} .
> $$
> One finite pole, $z=-\frac12$, so only **two** ROCs (not three): $\frac12<\lvert z\rvert<\infty$ and $\lvert z\rvert<\frac12$. The leftover $z$ (degree 2 over degree 1 in $z$) also puts a pole at $\infty$, which is why the first ROC stops short of $\infty$.
>
> **Divide.** With $w=z^{-1}$: $\dfrac{1+2w}{1+\frac12w} = 4-\dfrac{3}{1+\frac12 w}$ (check: $4(1+\frac12w)-3 = 1+2w$ ✓), so
> $$
> X(z) = 4z - \frac{3z}{1+\frac12 z^{-1}} .
> $$
> $4z\leftrightarrow 4\delta[n+1]$ in both ROCs; the second term is the shifted pair $z\cdot\frac{1}{1+\frac12z^{-1}}$.
> $$
> \begin{aligned}
> \tfrac12<\lvert z\rvert<\infty:&\quad x[n] = 4\delta[n+1] - 3\left(-\tfrac12\right)^{n+1}u[n+1] \\
> \lvert z\rvert<\tfrac12:&\quad x[n] = 4\delta[n+1] + 3\left(-\tfrac12\right)^{n+1}u[-n-2]
> \end{aligned}
> $$
> Values: the first gives $x[-1]=1$, $x[0]=\frac32$, $x[1]=-\frac34,\dots$; the second gives $x[-1]=4$, $x[-2]=-6$, $x[-3]=12,\dots$
>
> **Stable?** The first ROC contains $\lvert z\rvert=1$: stable. **Causal?** Neither. The first is right-sided but $x[-1]\neq0$ (the ROC excludes $\infty$), the "right-sided but non-causal" row of the [[2-z-transform/11-bibo-stability-and-causality|Lecture 11]] table. Forgetting to cancel $(z-2)$ would have produced a bogus pole at 2 and a wrong "stable" answer on $\frac12<\lvert z\rvert<2$.

> [!question] Practice 3 — stable choice, then "all possible outputs"
> An LTI system has
> $$
> H(z) = \frac{2-\frac52 z^{-1}}{1-\frac52 z^{-1}-\frac32 z^{-2}} .
> $$
> (a) List all possible ROCs and say which is BIBO stable and which is causal. (b) Find $h[n]$ for the stable system. (c) The input is $x[n]=\delta[n]-3\delta[n-1]$. Find all possible outputs, and say which of the three systems produces each.

> [!success]- Solution
> **(a)** $1-\frac52z^{-1}-\frac32z^{-2} = (1+\frac12z^{-1})(1-3z^{-1})$: poles $-\frac12$ and $3$. ROCs: $\lvert z\rvert<\frac12$ (anti-causal, unstable), $\ \frac12<\lvert z\rvert<3$ (two-sided, **stable**), $\ \lvert z\rvert>3$ (**causal**, unstable). No ROC is both.
>
> **(b)** Cover-up: $A = \dfrac{2-\frac52(-2)}{1-3(-2)} = 1$ at $p=-\frac12$, $\ B = \dfrac{2-\frac52\cdot\frac13}{1+\frac12\cdot\frac13} = 1$ at $p=3$. On $\frac12<\lvert z\rvert<3$ the pole $-\frac12$ is inside (right-sided), the pole $3$ outside (left-sided):
> $$
> h[n] = \left(-\tfrac12\right)^n u[n] - 3^n u[-n-1] .
> $$
>
> **(c)** $X(z) = 1-3z^{-1}$ has a zero at $z=3$ that **cancels** the pole at 3:
> $$
> Y(z) = H(z)X(z) = \frac{2-\frac52 z^{-1}}{1+\frac12 z^{-1}} = -5 + \frac{7}{1+\frac12 z^{-1}}
> $$
> (improper, so divide: $-5(1+\frac12z^{-1})+7 = 2-\frac52z^{-1}$ ✓). One pole left, so two possible outputs:
> $$
> y_1[n] = -5\delta[n] + 7\left(-\tfrac12\right)^n u[n]\ \ (\lvert z\rvert>\tfrac12),\qquad y_2[n] = -5\delta[n] - 7\left(-\tfrac12\right)^n u[-n-1]\ \ (\lvert z\rvert<\tfrac12).
> $$
> ROC$_Y$ must contain ROC$_H\cap$ROC$_X$ (and ROC$_X$ is $z\neq0$). For the causal system ($\lvert z\rvert>3$) and the stable one ($\frac12<\lvert z\rvert<3$) the only pole-bounded region containing that is $\lvert z\rvert>\frac12$, so **both give $y_1$**: the input removed the one pole in which they differ. The anti-causal system gives $y_2$. Check: $y_1[0] = 2 = Y(\infty)$ and $y_1[1]=-\frac72$, matching the recursion $y[n]=\frac52y[n-1]+\frac32y[n-2]+2x[n]-\frac52x[n-1]$ run forward.

## The Python side

`scipy.signal.residuez` does step 4 for you (it returns $A_k$ as `r`, $p_k$ as `p`, and the long-division terms as `k`); `lfilter` gives the causal choice. On the exam you do it by hand, but this is how to check a practice answer:

```python
import numpy as np
from scipy.signal import residuez, lfilter

b, a = [3, -4/3], [1, -5/3, -2/3]       # X(z) of Practice 1, coefficients of z^0, z^-1, z^-2
r, p, k = residuez(b, a)                # X = sum r_k / (1 - p_k z^-1) + direct terms k
print("A_k =", np.round(r.real, 6), " p_k =", np.round(p.real, 6), " k =", k)

n = np.arange(6)                        # causal choice |z| > 2: both terms right-sided
x = lfilter(b, a, (n == 0).astype(float))
print(np.allclose(x, (-1/3)**n + 2 * 2.0**n), x[:4])
```

```text
A_k = [1. 2.]  p_k = [-0.333333  2.      ]  k = []
True [ 3.          3.66666667  8.11111111 15.96296296]
```

`residuez` knows nothing about ROCs: the sidedness of each term is your decision, made with step 6.

## Where to go next

- Concepts: [[concepts/partial-fraction-expansion|partial-fraction expansion]], [[concepts/region-of-convergence|region of convergence]], [[concepts/sided-sequences|right-, left- and two-sided sequences]], [[concepts/z-transform-pairs|z-transform pairs]], [[concepts/pole-zero-cancellation|pole–zero cancellation]], [[concepts/bibo-stability|BIBO stability]], [[concepts/causality|causality]].
- Lectures: [[2-z-transform/08-inverse-z-transform|Lecture 8]] (PFE), [[2-z-transform/10-improper-transfer-functions-and-system-algebra|Lecture 10]] (long division), [[2-z-transform/11-bibo-stability-and-causality|Lecture 11]] (ROC shape ↔ causality and stability table).
- Next family: [[problems/two-sided-systems-as-recursions|two-sided systems as recursions]] (what to do with the stable two-sided $h$), [[problems/lccde-to-transfer-function-and-response|LCCDE ↔ H(z) ↔ response]].
- Try it: [[demos/pole-zero-and-roc-explorer|pole–zero and ROC explorer]] (place the poles, click through the ROCs), [[0-midterm-1/practice-drills|practice drills]] (randomized PFE and ROC questions), [[0-midterm-1/cheat-sheet|cheat sheet]] (the pair table).

### Sources for this page

Lecture 8 notes (PFE procedure, Exercises 1–2) and slides (Example 3); Lecture 10 notes (improper rational functions); Lecture 11 notes and slides (ROC shape ↔ causality/stability table, slide 10); HW3 #3–4 and HW4 #1 with solutions; past midterms FA2025 #7a, SP2025 #8, FA2024 #7, FA2023 #6, SP2023 #6, SP2021 #5, #7, FA2019 #6, #7. Practice problems are new; every number on this page is checked in `verify/problems/rocs_practice.py`.
