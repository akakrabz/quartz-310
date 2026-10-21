---
title: "Partial fraction expansion (PFE)"
description: "Split a rational X(z) into first-order terms A_k/(1 − p_k z⁻¹) by cover-up so each term inverts by table lookup; long division for improper X(z), conjugate and repeated poles."
tags: [concept, z-transform, roc]
aliases: ["PFE", "partial fractions", "partial fraction decomposition"]
---

> [!key] Proper $X(z)$, distinct poles
> $$
> \begin{gathered}
> X(z) = \frac{\sum_{k=0}^{M-1} b_k z^{-k}}{\prod_{k=1}^{N}\left(1-p_k z^{-1}\right)} = \sum_{k=1}^{N} \frac{A_k}{1-p_k z^{-1}},
> \\[4pt]
> A_k = \Big[\left(1-p_k z^{-1}\right)X(z)\Big]_{z=p_k}
> \end{gathered}
> $$
> Proper: numerator degree in $z^{-1}$ lower than denominator's. Each term inverts to $A_k p_k^n u[n]$ (ROC outside $|p_k|$) or $-A_k p_k^n u[-n-1]$ (inside).

> [!example] Lecture 8, Exercise 1: $H(z) = \dfrac{2-z^{-1}}{\left(1-\frac13 z^{-1}\right)\left(1-2z^{-1}\right)}$
> $z=\frac13$: $A_1=\frac15$; $z=2$: $A_2=\frac95$. Check $\sum A_k=H(\infty)=2$.

> [!success]- The three possible $h[n]$
> - $|z|>2$: $h[n] = \frac15\left(\frac13\right)^n u[n] + \frac95\, 2^n u[n]$.
> - $|z|<\frac13$: $h[n] = -\frac15\left(\frac13\right)^n u[-n-1] - \frac95\, 2^n u[-n-1]$.
> - $\frac13<|z|<2$ (stable): $h[n] = \frac15\left(\frac13\right)^n u[n] - \frac95\, 2^n u[-n-1]$.

- **Conjugate poles** $re^{\pm j\omega_0}$: $A p^n + A^{*}(p^{*})^n = 2|A|\,r^n\cos\!\left(\omega_0 n + \angle A\right)$. Lecture 8, Exercise 2: $\frac{3-\frac32 z^{-1}}{1-z^{-1}+z^{-2}}$, causal, gives $3\cos\!\left(\tfrac{\pi}{3}n\right)u[n]$.
- **Improper** (numerator degree ≥ denominator's): long division first ([[0-toolkit/04-factoring-and-long-division|long division]]):

$$
X(z) = \sum_{k=0}^{M-N-1} C_k z^{-k} \;+\; \sum_{k=1}^{N}\frac{A_k}{1-p_k z^{-1}} .
$$

Lecture 10, Exercise 1: $h[n] = \tfrac59\,\delta[n] - \tfrac43\,\delta[n-1] + \tfrac{7}{36}\,3^n u[n] + \tfrac14(-1)^n u[n]$.
- **Repeated pole:** $\frac{A}{1-pz^{-1}} + \frac{B}{(1-pz^{-1})^2}\leftrightarrow A\,p^n u[n] + B\,(n+1)p^n u[n]$ (causal).
- **Pure delay:** pull $z^{-k}$ out, expand the rest, shift at the end.

> [!trap]
> - Plug in $z=p_k$ ($z^{-1}=1/p_k$), not $z^{-1}=p_k$.
> - Divide first when improper, else $\delta$ terms go missing.
> - Stay in the $z^{-1}$ form; the "$X(z)/z$" method gives different constants.
> - The ROC only picks each term's side; cancel common factors first.

**Where it appears:** [[2-z-transform/08-inverse-z-transform|L8]], [[2-z-transform/09-transfer-functions|L9]], [[2-z-transform/10-improper-transfer-functions-and-system-algebra|L10]]; [[problems/all-possible-rocs]], [[problems/lccde-to-transfer-function-and-response]]; [[homework/hw3|HW3]] #3–#4, [[homework/hw4|HW4]]; every past Midterm 1.

## Related
[[concepts/inverse-z-transform]] · [[concepts/region-of-convergence]] · [[concepts/z-transform-pairs]] · [[concepts/poles-and-zeros]] · [[demos/python-demos]]

### Sources for this page
Lecture 8 notes §2.2 (Exercises 1–2); Lecture 10 notes §1.1–1.2, slides 7–8; FA2025 #6, SP2025 #4b, SP2021 #4–#5 keys.
