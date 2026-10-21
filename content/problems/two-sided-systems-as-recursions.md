---
title: "Two-sided systems as recursions"
description: "Computing a stable non-causal H(z): split it by partial fractions into a causal part run forward and an anti-causal part run backward; what a \"non-causal LCCDE\" means. FA2025 #7b, FA2024 #8a."
tags: [problem-family, problem, midterm-1, lccde, stability, roc, z-transform]
family_frequency: "2 of 7 exams"
typical_points: "5–8"
lectures: [5, 9, 10, 11]
---

*Problem family · 2 of 7 past midterms (FA2025, FA2024) · 5–8 points, second half of a 10–15 point problem · [[1-signals-and-systems/05-difference-equations-and-block-diagrams|Lecture 5]], [[2-z-transform/09-transfer-functions|Lecture 9]], [[2-z-transform/10-improper-transfer-functions-and-system-algebra|Lecture 10]], [[2-z-transform/11-bibo-stability-and-causality|Lecture 11]]*

## What it looks like on the exam

Follows an [[problems/all-possible-rocs|all-possible-ROCs]] part that produced a stable two-sided $h[n]$.

- [[exams/midterm-1/past-exams/fall-2025|FA2025 #7b]]: implement $H=H_1+H_2$ with "BIBO stable difference equations"; "specify the directions of recursive computation".
- [[exams/midterm-1/past-exams/fall-2024|FA2024 #8a]]: "a **non-causal** LTI system described by $y[n]+\alpha y[n-1]=x[n]+3x[n-1]$. For what $\alpha$ is it BIBO stable?"
- Relatives: [[exams/midterm-1/past-exams/fall-2023|FA2023 #8b]] (two-sided: stable for every $\alpha$), [[exams/midterm-1/past-exams/spring-2025|SP2025 #8c]], the $h=h_l+h_r$ split in Lecture 11.

> [!success]- FA2025 #7, answered
> $H(z) = \dfrac{1-z^{-1}}{(1+2z^{-1})(1+\frac23z^{-1})} = \dfrac{9/4}{1+2z^{-1}} + \dfrac{-5/4}{1+\frac23z^{-1}}$, ROC $\tfrac23<\lvert z\rvert<2$.
> - $H_1 = \dfrac{9/4}{1+2z^{-1}}$, $\lvert z\rvert<2$, anti-causal, backward: $y_1[n-1] = -\tfrac12\,y_1[n] + \tfrac98\,x[n]$.
> - $H_2 = \dfrac{-5/4}{1+\frac23z^{-1}}$, $\lvert z\rvert>\tfrac23$, causal, forward: $y_2[n] = -\tfrac23\,y_2[n-1] - \tfrac54\,x[n]$.
> - $y=y_1+y_2$; feedback magnitudes $\tfrac12$, $\tfrac23$ in their directions: stable.

## The recipe

> [!recipe] A stable two-sided $H(z)$ as recursions
> 1. **PFE:** $H(z) = \sum_k \dfrac{A_k}{1-p_kz^{-1}}$; stable ROC contains $\lvert z\rvert=1$.
> 2. **Split:** poles inside the unit circle (and any $C_kz^{-k}$) → $H_c$; outside → $H_a$. Conjugate pairs stay together.
> 3. **Causal part, forward** (at rest before the input):
> $$
> y_c[n] = p\,y_c[n-1] + A\,x[n].
> $$
> 4. **Anti-causal part, backward** (at rest after the input), from the same $y_a[n]-p\,y_a[n-1] = A\,x[n]$:
> $$
> y_a[n-1] = \frac1p\,y_a[n] - \frac{A}{p}\,x[n].
> $$
> 5. **Add:** $y=y_c+y_a$. Check: feedback magnitude $\lt1$ in each direction.
> 6. **"Non-causal LCCDE"** means ROC inside the pole, run backward: FA2024 #8a gives $y[n-1] = \frac{1}{\alpha}\big(x[n]+3x[n-1]-y[n]\big)$, stable iff $\lvert\alpha\rvert>1$.

> [!trap] Where the points go
> - **Anti-causal part run forward:** $y_1[n] = -2y_1[n-1]+\tfrac94x[n]$ blows up.
> - **Dividing half the equation:** $\tfrac98$, not $\tfrac94$.
> - **Pole sign:** $\dfrac{A}{1+2z^{-1}}$ has $p=-2$.
> - **Say the direction** next to each recursion (FA2025 #7b asks).
> - **Non-causal is not unstable** (FA2024 #8a, FA2023 #8b).

## Practice problems

> [!question] Practice 1 — split and run
> Stable $H(z) = \dfrac{3-4z^{-1}}{(1-\frac12z^{-1})(1-3z^{-1})}$. (a) $h[n]$. (b) Stable recursions for $H_1$, $H_2$ with directions. (c) $x=\delta[n]$: $y_2[-1], y_2[-2], y_2[-3]$ from the backward recursion vs $h$.

> [!success]- Solution
> **(a)** $A=1$, $B=2$:
> $$
> h[n] = \left(\tfrac12\right)^n u[n] - 2\,(3)^n u[-n-1] .
> $$
> **(b)** Causal, forward: $y_1[n] = \tfrac12\,y_1[n-1] + x[n]$. Anti-causal, backward: $y_2[n-1] = \tfrac13\,y_2[n] - \tfrac23\,x[n]$.
> **(c)** $-\tfrac23$, $-\tfrac29$, $-\tfrac{2}{27}$, matching $-2\cdot3^{n}$ ✓.

> [!question] Practice 2 — one LCCDE, three systems
> $y[n] = \tfrac{10}{3}\,y[n-1] - y[n-2] + x[n]$. (a) $H(z)$ and every system it describes. (b) Recursions for the causal and anti-causal ones. (c) The stable one as two first-order recursions.

> [!success]- Solution
> **(a)** $H(z) = \dfrac{9/8}{1-3z^{-1}} + \dfrac{-1/8}{1-\frac13z^{-1}}$.
>
> | ROC | $h[n]$ | stable? |
> |---|---|---|
> | $\lvert z\rvert>3$ | $\tfrac98\,3^nu[n]-\tfrac18(\tfrac13)^nu[n]$ | no |
> | $\tfrac13<\lvert z\rvert<3$ | $-\tfrac18(\tfrac13)^nu[n]-\tfrac98\,3^nu[-n-1]$ | **yes** |
> | $\lvert z\rvert<\tfrac13$ | $-\tfrac98\,3^nu[-n-1]+\tfrac18(\tfrac13)^nu[-n-1]$ | no |
>
> **(b)** Forward: as given. Backward: $y[n-2] = \tfrac{10}{3}y[n-1]-y[n]+x[n]$. Both unstable.
> **(c)**
> $$
> \begin{gathered}
> y_c[n] = \tfrac13\,y_c[n-1] - \tfrac18\,x[n]\ \ \text{(forward)},\\
> y_a[n-1] = \tfrac13\,y_a[n] - \tfrac38\,x[n]\ \ \text{(backward)}.
> \end{gathered}
> $$

## Related

[[concepts/sided-sequences|Sided sequences]] · [[concepts/system-algebra|system algebra]] · [[problems/all-possible-rocs|all possible ROCs]] · [[problems/parameters-for-stability|parameters for stability]] · [[demos/difference-equation-simulator|difference-equation simulator]]

### Sources for this page

Lectures 5, 10, 11 notes; past Midterm 1 exams FA2025 #7 (handwritten key), FA2024 #8a, FA2023 #8b, SP2025 #8c. Practice problems are new.
