---
title: "Parameters for stability"
description: "\"For what α is the system BIBO stable?\": find the bad poles for the stated causality, then cancel them with an α-dependent zero or put the α-dependent pole on the right side of the unit circle."
tags: [problem-family, problem, midterm-1, stability, lccde, roc, z-transform]
family_frequency: "3 of 7 exams"
typical_points: "6–10"
lectures: [9, 11]
---

*Problem family · 3 of 7 past midterms (SP2025, FA2024, FA2023) · 6–10 points · [[2-z-transform/09-transfer-functions|Lecture 9]], [[2-z-transform/11-bibo-stability-and-causality|Lecture 11]]*

## What it looks like on the exam

An LCCDE with one unknown $\alpha$ (or $\beta$), real or complex, and a causality sentence ("causal", "non-causal", "non-causal and two-sided"). Open question or a True/False list of candidates.

| where | system | causality | answer |
|---|---|---|---|
| [[exams/midterm-1/past-exams/spring-2025\|SP2025 #7]] (6 pts) | $y[n]=-\tfrac32y[n-1]+y[n-2]+x[n]-\alpha^2x[n-2]$, $\alpha\in\mathbb{C}$ | causal | poles $-2,\ \tfrac12$; zeros $\pm\alpha$; stable iff $\alpha=\pm2$: $2$ T, $-2$ T, $j2$ F, $-j2$ F, $\tfrac{\sqrt2}{2}$ F, $\tfrac12$ F |
| [[exams/midterm-1/past-exams/fall-2024\|FA2024 #8a]] | $y[n]+\alpha y[n-1]=x[n]+3x[n-1]$, $\alpha$ real | non-causal | ROC $\lvert z\rvert<\lvert\alpha\rvert$: stable iff $\lvert\alpha\rvert>1$ (key writes $\lvert a\rvert$) |
| FA2024 #8b | $y[n]-\tfrac52y[n-1]+y[n-2]=x[n]+\beta x[n-1]$ | causal | poles $2,\ \tfrac12$: $\beta=-2$ cancels 2 |
| [[exams/midterm-1/past-exams/fall-2023\|FA2023 #8a]] | $y[n]-\tfrac23y[n-1]-\tfrac89y[n-2]=3x[n]+\alpha x[n-1]$ | causal | poles $\tfrac43,\ -\tfrac23$: $\alpha=-4$ cancels $\tfrac43$ |
| FA2023 #8b | same | two-sided | ROC $\tfrac23<\lvert z\rvert<\tfrac43$: stable for every $\alpha$ |

## The recipe

> [!recipe] Stability as a function of a parameter
> 1. **$H(z)$** from the LCCDE; note whether $\alpha$ moves a zero (numerator) or a pole.
> 2. **Factor** the parameter-free polynomial: fixed poles.
> 3. **Bad poles:** causal: $\lvert p\rvert\ge1$; left-sided: $\lvert p\rvert\le1$; two-sided with $\lvert z\rvert=1$ in the annulus: none, stable for every $\alpha$.
> 4. **$\alpha$ in the numerator:** each bad pole must be a zero; substitute $z^{-1}=1/p_{\text{bad}}$, solve. Two bad poles: usually "no value".
> 5. **$\alpha$ in the denominator:** condition on $\lvert\alpha\rvert$ (causal $\lt1$, left-sided $\gt1$), plus any value that lands the pole on a zero.
> 6. **Complex $\alpha$ or $\alpha^2$:** solve for the zero location, then $\alpha$, all roots. Check: show the common factor and the new $H$, ROC.

> [!trap] Where the points go
> - **Sign of the cancelling value.** FA2023 #8a: $3+\tfrac34\alpha=0$, $\alpha=-4$, not $+4$.
> - **Wrong pole cancelled.** SP2025 #7, $\alpha=\tfrac12$ cancels the stable $\tfrac12$; $-2$ remains.
> - **Magnitude is not enough.** $\alpha=\pm j2$ gives zeros $\pm j2$: False.
> - **Left-sided flips the inequality** (FA2024 #8a: $\lvert\alpha\rvert>1$).
> - **New ROC after cancelling.** FA2024 #8b, $\beta=-2$: $H=\dfrac{1}{1-\frac12z^{-1}}$, $\lvert z\rvert>\tfrac12$.

## Practice problems

> [!question] Practice 1 — one LCCDE, three causality assumptions
> $$
> y[n] + \tfrac76\,y[n-1] - \tfrac12\,y[n-2] = 2x[n] + \alpha\,x[n-1],\qquad \alpha\in\mathbb{R}.
> $$
> Stable for which $\alpha$ if (a) causal, (b) anti-causal, (c) two-sided? $h[n]$ in (a), (b).

> [!success]- Solution
> $$
> H(z) = \frac{2+\alpha z^{-1}}{(1+\frac32z^{-1})(1-\frac13z^{-1})},\qquad\text{poles } -\tfrac32,\ \tfrac13;\ \text{zero } -\tfrac{\alpha}{2}.
> $$
> **(a)** Bad pole $-\tfrac32$: $\alpha=3$; $h[n]=2(\tfrac13)^nu[n]$.
> **(b)** Bad pole $\tfrac13$: $\alpha=-\tfrac23$; $h[n] = -2\left(-\tfrac32\right)^nu[-n-1]$.
> **(c)** $\tfrac13<\lvert z\rvert<\tfrac32$: every $\alpha$.

> [!question] Practice 2 — the parameter is a pole
> Causal $y[n] = a\,y[n-1] + x[n] - 2x[n-1]$, $a$ real. Stable for which $a$? $h[n]$ for $a=2$ and $a=1$?

> [!success]- Solution
> $H(z) = \dfrac{1-2z^{-1}}{1-az^{-1}}$. Answer: $\lvert a\rvert<1$ or $a=2$ ($H=1$, $h=\delta[n]$). $a=1$: $h[n]=\delta[n]-u[n-1]$, bounded but not summable: not BIBO stable.

> [!question] Practice 3 — complex $\alpha$, true or false
> Causal $y[n] = -\tfrac{11}{4}y[n-1] + \tfrac34y[n-2] + x[n] + \alpha^2x[n-2]$, $\alpha\in\mathbb{C}$. Stable for (a) $3$ (b) $-3$ (c) $3j$ (d) $-3j$ (e) $\tfrac{j}{4}$ (f) $\tfrac14$?

> [!success]- Solution
> Poles $-3$ (bad), $\tfrac14$; zeros $\pm j\alpha$. Need $\alpha^2=-9$: (c), (d) True, $H = \dfrac{1-3z^{-1}}{1-\frac14z^{-1}}$. (a), (b): zeros $\pm3j$, False. (e): cancels the harmless $\frac14$, False. (f): False.

## Related

[[concepts/bibo-stability|BIBO stability]] · [[concepts/pole-zero-cancellation|pole–zero cancellation]] · [[problems/unbounded-outputs-and-pole-matching|pole matching]] · [[problems/two-sided-systems-as-recursions|two-sided recursions]] · [[demos/pole-zero-and-roc-explorer|ROC explorer]]

### Sources for this page

Lecture 9 and 11 notes; past Midterm 1 exams SP2025, FA2024, FA2023 with keys. Practice problems are new.
