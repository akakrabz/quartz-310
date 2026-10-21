---
title: "All possible ROCs (inverse z by partial fractions)"
description: "Inverse z-transform without a given ROC: cancel, factor, partial fractions, one ROC per annulus between pole magnitudes, each term right- or left-sided; then pick the stable or causal one."
tags: [problem-family, problem, midterm-1, z-transform, roc, stability]
family_frequency: "7 of 7 exams"
typical_points: "15–20"
lectures: [7, 8, 10, 11]
---

*Problem family · 7 of 7 past midterms · 15–20 points · [[2-z-transform/07-z-transform-properties|Lecture 7]], [[2-z-transform/08-inverse-z-transform|Lecture 8]], [[2-z-transform/10-improper-transfer-functions-and-system-algebra|Lecture 10]], [[2-z-transform/11-bibo-stability-and-causality|Lecture 11]]*

## What it looks like on the exam

Rational $X(z)$ or $H(z)$, usually two poles, often in positive powers of $z$. Three asks, often part (a) of a longer problem:

1. **All possible ROCs and $x[n]$** (FA2023, FA2019, HW4).
2. **BIBO stable, find $h[n]$:** the annulus containing $\lvert z\rvert=1$, often two-sided (FA2025, SP2025).
3. **Causal:** outside the largest pole (FA2024, SP2023, HW3 #4).

| where | asked | poles | result |
|---|---|---|---|
| [[exams/midterm-1/past-exams/fall-2025\|FA2025 #7a]] | stable $h$ of $\dfrac{1-z^{-1}}{(1+2z^{-1})(1+\frac23z^{-1})}$ | $-2,\ -\tfrac23$ | ROC $\tfrac23<\lvert z\rvert<2$, $h=-\tfrac94(-2)^nu[-n-1]-\tfrac54(-\tfrac23)^nu[n]$ |
| [[exams/midterm-1/past-exams/spring-2025\|SP2025 #8b,c]] | all outputs; stable $h$ | $\tfrac12,\ -\tfrac32$ | two outputs; ROC $\tfrac12<\lvert z\rvert<\tfrac32$, $h=-(\tfrac12)^nu[n]-3(-\tfrac32)^nu[-n-1]$ |
| [[exams/midterm-1/past-exams/fall-2024\|FA2024 #7a,b]] | causal: ROC, $h$ | $\tfrac12,\ 2$ | $\lvert z\rvert>2$, $h=-\tfrac13(\tfrac12)^nu[n]+\tfrac43\,2^nu[n]$ |
| [[exams/midterm-1/past-exams/fall-2023\|FA2023 #6a]] | all ROCs of $\dfrac{1-z^{-1}}{(1-\frac12z^{-1})(1-2z^{-1})}$ | $\tfrac12,\ 2$ | $A_1=\tfrac13$, $A_2=\tfrac23$; three ROCs, the fourth combination empty |
| [[exams/midterm-1/past-exams/spring-2023\|SP2023 #6a,b]] | $H=Y/X$, causal and stable | $\tfrac12,\ \tfrac14$ | $\lvert z\rvert>\tfrac12$, $h=-6(\tfrac12)^nu[n]+7(\tfrac14)^nu[n]$ |
| [[exams/midterm-1/past-exams/spring-2021\|SP2021 #5a]] | $h$ of $\dfrac{3z^{-1}}{1+z^{-2}}$, $\lvert z\rvert>1$ | $\pm j$ | $h=3\sin(\tfrac{\pi}{2}n)u[n]$ |
| SP2021 #7 | $X$, $H=Y/X$, ROC of $Y$, $h$ | $\tfrac12,\ 1$ ($4$ cancels) | ROC$_Y$ $\lvert z\rvert>1$, $h=7(\tfrac12)^nu[n]-6u[n]$ |
| [[exams/midterm-1/past-exams/fall-2019\|FA2019 #6]] | inverse of $1+z^{-100}+\dfrac{1}{1-5z^{-1}}$, $\lvert z\rvert>5$ | $5$ | $\delta[n]+\delta[n-100]+5^nu[n]$ |
| FA2019 #7 | all ROCs of $\dfrac{z}{z-e^{j\pi/3}}+\dfrac{z}{z-0.5}$ | $e^{j\pi/3},\ \tfrac12$ | $\lvert z\rvert>1$, $\lvert z\rvert<\tfrac12$, $\tfrac12<\lvert z\rvert<1$ |
| [[homework/hw4\|HW4 #1]] | all ROCs, three transforms | (b): $(z+1)$ cancels | (a), (c): three ROCs each; (b): two, improper |
| [[homework/hw3\|HW3 #3c, #4]] | $h$ for a given ROC; right-sided $H$ | | two-sided $h_3$ on $\tfrac14<\lvert z\rvert<\tfrac32$; $\lvert z\rvert>\tfrac23$ |
| Lecture 8 | Exercise 1; slides Example 3 | $\tfrac13,2$; $\tfrac43,\tfrac23$ | $A=\tfrac15,\tfrac95$; $A=2,-1$ |
| Lecture 11 | slide 10: stable $h$ of two $H$ | $\tfrac12,-\tfrac43$; $\tfrac15,\tfrac45$ | two-sided; causal |

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
<figcaption><strong>Two pole magnitudes, three ROCs.</strong> Poles (×) at radii a &lt; 1 &lt; b, dashed |z| = 1; the fourth sign pattern (a right-sided, b left-sided) would need |z| &gt; b and |z| &lt; a at once: empty.</figcaption>
</figure>

## The recipe

> [!recipe] All possible ROCs
> 1. **Clean up.** Powers of $z^{-1}$; cancel common factors (a cancelled pole is no ROC boundary).
> 2. **Proper?** If not, long-divide ([[2-z-transform/10-improper-transfer-functions-and-system-algebra|Lecture 10]]) or split off $z^k$; $C_kz^{-k}\to C_k\delta[n-k]$ in every ROC.
> 3. **Expand:** $X(z)=\sum_k\dfrac{A_k}{1-p_kz^{-1}}$, $A_k=\Big[(1-p_kz^{-1})X(z)\Big]_{z=p_k}$. Distinct magnitudes $r_1<\dots<r_m$ (conjugates and $\pm p$ share one).
> 4. **List $m+1$ ROCs:** $\lvert z\rvert<r_1$, $r_1<\lvert z\rvert<r_2$, …, $\lvert z\rvert>r_m$.
> 5. **Invert per ROC:** pole inside the ROC's inner circle → $A_kp_k^nu[n]$; outside its outer circle → $-A_kp_k^nu[-n-1]$.
> 6. **Name them:** contains $\lvert z\rvert=1$ → stable (none if a pole is on it); outermost → causal (if no $z^k$ left); innermost → anti-causal. Check: recombine at $z=1$; $\sum_kA_k=b_0$ for a proper $X$.

> [!trap] Where the points go
> - **Cancel first.** HW4 #1(b): $\dfrac{z^3-z}{z^2+3z+2}$, $(z+1)$ cancels: two ROCs, not three.
> - **Improper:** cover-up misses the $C_kz^{-k}$ terms; divide first.
> - **Left-sided pair:** $-p^nu[-n-1]$, minus sign and $u[-n-1]$.
> - **Empty pattern.** Outer pole right-sided with inner left-sided converges nowhere (FA2023 key); poles on one circle move together.
> - **Stable ≠ middle.** Both poles inside the unit circle: the outer ROC is stable (SP2023 #6); a pole on $\lvert z\rvert=1$: none (FA2019 #7). A leftover $z$ gives $\delta[n+1]$: not causal.

## Practice problems

> [!question] Practice 1 — factor first, then three ROCs
> $$
> X(z) = \frac{3-\frac43 z^{-1}}{1-\frac53 z^{-1}-\frac23 z^{-2}}
> $$
> (a) Poles and all ROCs. (b) $x[n]$ for each. (c) Which is absolutely summable, which causal?

> [!success]- Solution
> **(a)** $z^2-\frac53z-\frac23=\frac13(3z+1)(z-2)$: poles $-\frac13$, $2$; zero $\frac49$, no cancellation. ROCs $\lvert z\rvert<\frac13$, $\frac13<\lvert z\rvert<2$, $\lvert z\rvert>2$. Cover-up:
> $$
> A = \frac{3-\frac43(-3)}{1-2(-3)} = 1,\qquad B = \frac{3-\frac43\cdot\frac12}{1+\frac13\cdot\frac12} = 2 .
> $$
> **(b)**
> $$
> \begin{aligned}
> \lvert z\rvert>2:&\quad x[n] = \left(-\tfrac13\right)^n u[n] + 2\,(2)^n u[n] \\
> \tfrac13<\lvert z\rvert<2:&\quad x[n] = \left(-\tfrac13\right)^n u[n] - 2\,(2)^n u[-n-1] \\
> \lvert z\rvert<\tfrac13:&\quad x[n] = -\left(-\tfrac13\right)^n u[-n-1] - 2\,(2)^n u[-n-1]
> \end{aligned}
> $$
> **(c)** Summable: $\frac13<\lvert z\rvert<2$ ($\sum\lvert x\rvert=\frac72$). Causal: $\lvert z\rvert>2$.

> [!question] Practice 2 — a cancelled pole and an improper fraction
> $$
> X(z) = \frac{z^3-4z}{z^2-\frac32 z-1}
> $$
> All ROCs and $x[n]$. Stable? Causal?

> [!success]- Solution
> $z(z-2)(z+2)$ over $(z-2)(z+\frac12)$; $(z-2)$ cancels:
> $$
> X(z) = z\cdot\frac{1+2z^{-1}}{1+\frac12 z^{-1}} = 4z - \frac{3z}{1+\frac12 z^{-1}} .
> $$
> One finite pole: two ROCs. The leftover $z$ excludes $\infty$.
> $$
> \begin{aligned}
> \tfrac12<\lvert z\rvert<\infty:&\quad x[n] = 4\delta[n+1] - 3\left(-\tfrac12\right)^{n+1}u[n+1] \\
> \lvert z\rvert<\tfrac12:&\quad x[n] = 4\delta[n+1] + 3\left(-\tfrac12\right)^{n+1}u[-n-2]
> \end{aligned}
> $$
> First: stable, right-sided, not causal ($x[-1]=1$). Second: neither.

> [!question] Practice 3 — stable choice, then all possible outputs
> $$
> H(z) = \frac{2-\frac52 z^{-1}}{1-\frac52 z^{-1}-\frac32 z^{-2}} .
> $$
> (a) All ROCs; which is stable, which causal? (b) Stable $h[n]$. (c) All outputs for $x[n]=\delta[n]-3\delta[n-1]$, and which system gives each.

> [!success]- Solution
> **(a)** Poles $-\frac12$, $3$. $\lvert z\rvert<\frac12$ anti-causal; $\frac12<\lvert z\rvert<3$ stable; $\lvert z\rvert>3$ causal. None both.
> **(b)** $A=1$, $B=1$:
> $$
> h[n] = \left(-\tfrac12\right)^n u[n] - 3^n u[-n-1] .
> $$
> **(c)** The zero of $X$ at 3 cancels the pole at 3:
> $$
> Y(z) = \frac{2-\frac52 z^{-1}}{1+\frac12 z^{-1}} = -5 + \frac{7}{1+\frac12 z^{-1}}
> $$
> $$
> \begin{aligned}
> y_1[n] &= -5\delta[n] + 7\left(-\tfrac12\right)^n u[n]\ \ (\lvert z\rvert>\tfrac12),\\
> y_2[n] &= -5\delta[n] - 7\left(-\tfrac12\right)^n u[-n-1]\ \ (\lvert z\rvert<\tfrac12).
> \end{aligned}
> $$
> Causal and stable systems both give $y_1$; the anti-causal one gives $y_2$.

## Related

[[concepts/partial-fraction-expansion|PFE]] · [[concepts/region-of-convergence|ROC]] · [[concepts/sided-sequences|sided sequences]] · [[concepts/pole-zero-cancellation|pole–zero cancellation]] · [[problems/two-sided-systems-as-recursions|two-sided recursions]] · [[problems/lccde-to-transfer-function-and-response|LCCDE ⇄ H(z)]] · [[demos/pole-zero-and-roc-explorer|ROC explorer]]

### Sources for this page

Lecture 8, 10, 11 notes and slides; HW3 #3–4, HW4 #1 with solutions; past Midterm 1 exams FA2019–FA2025 with keys. Practice problems are new.
