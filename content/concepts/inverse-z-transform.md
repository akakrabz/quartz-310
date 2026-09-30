---
title: "Inverse z-transform"
description: "Getting x[n] back from X(z) and its ROC — by inspection for finite and table-shaped transforms, by partial fractions for rational ones — with the ROC deciding, pole by pole, whether each term is right- or left-sided."
tags: [concept, z-transform, roc]
aliases: ["inverse z-transform", "inverse z transform"]
---

> [!key] What determines the answer
> The formal inverse is a contour integral, $x[n] = \frac{1}{j2\pi}\oint_C X(z)\,z^{n-1}\,dz$, which this course never evaluates. Instead: **(1)** read finite sequences off their coefficients, **(2)** match [[concepts/z-transform-pairs|table rows]] (with [[concepts/z-transform-properties|properties]]), **(3)** use [[concepts/partial-fraction-expansion|partial fractions]] for rational $X(z)$. In every case the [[concepts/region-of-convergence|ROC]] picks the signal:
> $$
> \frac{A}{1-pz^{-1}} \;\longrightarrow\;
> \begin{cases} A\,p^n\,u[n], & \text{ROC outside the pole } (|z|>|p|),\\[2pt]
> -A\,p^n\,u[-n-1], & \text{ROC inside the pole } (|z|<|p|). \end{cases}
> $$

## By inspection

A polynomial in $z^{-1}$ (and $z$) is a finite sequence: the coefficient of $z^{-k}$ is $x[k]$ ([[2-z-transform/08-inverse-z-transform|Lecture 8]]).

> [!example] Lecture 8 slides, Example 1 — and one exam item
> - (a) $X(z) = 1-\frac14 z^{-1}+\frac{1}{16}z^{-2}$: $\ x[n] = \delta[n]-\frac14\delta[n-1]+\frac{1}{16}\delta[n-2] = \{\underset{\uparrow}{1},\ -\tfrac14,\ \tfrac{1}{16}\}$.
> - (b) $X(z) = \dfrac{1}{1+\frac13 z^{-1}}$, $|z|<\frac13$: pole $-\frac13$, ROC inside it, so $x[n] = -\left(-\frac13\right)^n u[-n-1]$.
> - (c) $X(z) = \dfrac{1}{1-\frac12 z^{-1}} - \dfrac{3z^{-1}}{1+\frac15 z^{-1}}$, $|z|>\frac12$: both right-sided; the $z^{-1}$ is a one-step delay, so $x[n] = \left(\frac12\right)^n u[n] - 3\left(-\frac15\right)^{n-1}u[n-1]$.
> - FA2019 #6: $Y(z) = 1 + z^{-100} + \dfrac{1}{1-5z^{-1}}$, $|z|>5$: $\ y[n] = \delta[n]+\delta[n-100]+5^n u[n]$.

## By partial fractions

> [!recipe] Inverting a rational $X(z)$
> 1. Write $X(z)$ in powers of $z^{-1}$ and **cancel** common factors ([[concepts/pole-zero-cancellation|pole-zero cancellation]]).
> 2. **Improper?** (numerator degree $\ge$ denominator degree in $z^{-1}$) Long-divide; the quotient $\sum C_k z^{-k}$ becomes $\sum C_k\delta[n-k]$. A pure delay factor $z^{-k}$ can instead be pulled out and applied at the end.
> 3. **PFE** the proper part: $\sum_k \frac{A_k}{1-p_k z^{-1}}$.
> 4. **Each pole's side from the ROC**: pole inside the ROC's inner edge → $A_k p_k^n u[n]$; pole outside its outer edge → $-A_k p_k^n u[-n-1]$.
> 5. Re-apply delays ($z^{-k}\cdot\frac{A}{1-pz^{-1}} \to A\,p^{n-k}u[n-k]$), combine conjugate pairs into cosines, and **state the result with its $u[\cdot]$ factors**.

> [!example] Lecture 8 slides, Example 3: all ROCs of $X(z) = \dfrac{1}{\left(1-\frac43 z^{-1}\right)\left(1-\frac23 z^{-1}\right)}$
> PFE: $A_1 = \left[\frac{1}{1-\frac23 z^{-1}}\right]_{z=4/3} = \frac{1}{1-\frac12} = 2$ and $A_2 = \left[\frac{1}{1-\frac43 z^{-1}}\right]_{z=2/3} = \frac{1}{1-2} = -1$:
> $$
> X(z) = \frac{2}{1-\frac43 z^{-1}} - \frac{1}{1-\frac23 z^{-1}} .
> $$

> [!success]- The three signals (and the one that does not exist)
> - $|z|>\frac43$ (both right-sided): $x[n] = 2\left(\frac43\right)^n u[n] - \left(\frac23\right)^n u[n]$.
> - $\frac23<|z|<\frac43$ (pole $\frac43$ left, pole $\frac23$ right): $x[n] = -2\left(\frac43\right)^n u[-n-1] - \left(\frac23\right)^n u[n]$ — the only stable one.
> - $|z|<\frac23$ (both left-sided): $x[n] = -2\left(\frac43\right)^n u[-n-1] + \left(\frac23\right)^n u[-n-1]$.
> - Pole $\frac43$ right-sided with pole $\frac23$ left-sided would need $|z|>\frac43$ and $|z|<\frac23$: empty, no such z-transform (the signal grows in both directions).

> [!example]- HW3 #3(b)–(c): a delay and a two-sided ROC
> - $H_2(z) = \dfrac{3z^{-2}}{1+2z^{-1}}$, $|z|>2$: delay by 2 of $3(-2)^nu[n]$, so $h_2[n] = 3(-2)^{n-2}u[n-2]$.
> - $H_3(z) = \dfrac{1}{1-\frac14 z^{-1}} + \dfrac{1}{1-\frac32 z^{-1}}$, $\frac14<|z|<\frac32$: $h_3[n] = \left(\frac14\right)^nu[n] - \left(\frac32\right)^nu[-n-1]$.

**Systems given as two-sided $H(z)$.** When the stable ROC is an annulus, $h[n]$ splits into a causal part (poles inside) and an anti-causal part (poles outside). FA2025 #7 does exactly this and then asks for each part as a recursion: the causal part runs forward in $n$, the anti-causal part backward ([[problems/two-sided-systems-as-recursions]]).

> [!trap]
> - The left-sided term is $-A\,p^n u[-n-1]$: **both** the minus sign and the $-n-1$ matter.
> - Choose the side **per pole**, from the ROC — never "the whole answer is causal" unless the ROC is $|z|>|p_{\max}|$.
> - A delayed term shifts the **exponent too**: $\frac{z^{-1}}{1-az^{-1}} \to a^{n-1}u[n-1]$, not $a^n u[n-1]$.
> - "Causal" in the problem means every term is right-sided; "stable" means the ROC contains $|z|=1$; with neither, list every ROC ([[problems/all-possible-rocs]]).
> - For a causal answer, check $h[0] = H(\infty)$ (the ratio of the constant terms).

**Where it appears.**
- Lectures: [[2-z-transform/08-inverse-z-transform|L8]] (methods, Exercises 1–2), [[2-z-transform/09-transfer-functions|L9]] (impulse responses of LCCDEs), [[2-z-transform/10-improper-transfer-functions-and-system-algebra|L10]] (improper $H$), [[2-z-transform/11-bibo-stability-and-causality|L11]] (stable/causal choices).
- Problem families: [[problems/all-possible-rocs]], [[problems/lccde-to-transfer-function-and-response]], [[problems/two-sided-systems-as-recursions]], [[problems/infinite-length-convolution]].
- Homework: [[homework/hw3|HW3]] #3, #4c; [[homework/hw4|HW4]] #1, #4, #5b, #6.
- Past exams: [[0-midterm-1/past-exams/fall-2025|FA2025]] #6, #7; [[0-midterm-1/past-exams/spring-2025|SP2025 #8]]; [[0-midterm-1/past-exams/fall-2024|FA2024 #7]]; [[0-midterm-1/past-exams/fall-2023|FA2023 #6]]; [[0-midterm-1/past-exams/spring-2023|SP2023 #6]]; [[0-midterm-1/past-exams/spring-2021|SP2021]] #5, #7; [[0-midterm-1/past-exams/fall-2019|FA2019]] #6, #7, #10.

Related: [[concepts/partial-fraction-expansion]] · [[concepts/region-of-convergence]] · [[concepts/z-transform-pairs]] · [[concepts/sided-sequences]] · [[concepts/z-transform]] · [[concepts/transfer-function]]

### Sources for this page
Lecture 8 notes §1–2 (forms, the contour integral, Exercises 1–2) and annotated slides (Examples 1–3, including the empty fourth ROC); HW3 #3 solutions; exam keys FA2019 #6, FA2025 #7. Verification: `verify/concepts/verify_pfe.py` and `verify_zdomain_extra.py` (every sequence on this page summed numerically at a point inside its ROC).
