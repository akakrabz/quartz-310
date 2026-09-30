---
title: "Partial fraction expansion (PFE)"
description: "Split a rational X(z) into first-order terms A_k/(1 − p_k z⁻¹) — factor, write the sum, set z = p_k — so each term inverts by table lookup; plus long division for improper X(z), conjugate poles and repeated poles."
tags: [concept, z-transform, roc]
aliases: ["PFE", "partial fractions", "partial fraction decomposition"]
---

> [!key] The form (proper $X(z)$, distinct poles)
> $$
> \begin{gathered}
> X(z) = \frac{\sum_{k=0}^{M-1} b_k z^{-k}}{\prod_{k=1}^{N}\left(1-p_k z^{-1}\right)} = \sum_{k=1}^{N} \frac{A_k}{1-p_k z^{-1}},
> \\[4pt]
> A_k = \Big[\left(1-p_k z^{-1}\right)X(z)\Big]_{z=p_k}
> \end{gathered}
> $$
> "Proper" here means the numerator's highest power of $z^{-1}$ is **lower** than the denominator's. Each term then inverts by the [[concepts/z-transform-pairs|table]]: $A_k p_k^n u[n]$ if the ROC lies outside $|p_k|$, $-A_k p_k^n u[-n-1]$ if it lies inside.

> [!recipe] The three steps (Lecture 8)
> 1. **Factor** the denominator into $\prod_k (1-p_k z^{-1})$ and write $X(z) = \sum_k \frac{A_k}{1-p_k z^{-1}}$.
> 2. **Multiply** both sides by the common denominator.
> 3. **Set $z = p_k$** (that is, $z^{-1} = 1/p_k$): every term but one vanishes and gives $A_k$. This is the "cover-up" rule in the box above.
>
> Then invert term by term, choosing each term's side from the [[concepts/region-of-convergence|ROC]].

> [!example] Lecture 8, Exercise 1: $H(z) = \dfrac{2-z^{-1}}{1-\frac73 z^{-1}+\frac23 z^{-2}}$
> Factor: $1-\frac73 z^{-1}+\frac23 z^{-2} = \left(1-\frac13 z^{-1}\right)\left(1-2z^{-1}\right)$. Then $2-z^{-1} = A_1(1-2z^{-1}) + A_2(1-\frac13 z^{-1})$.
> - $z=\frac13$ ($z^{-1}=3$): $\;2-3 = A_1(1-6) \Rightarrow A_1 = \frac15$.
> - $z=2$ ($z^{-1}=\frac12$): $\;2-\frac12 = A_2(1-\frac16) \Rightarrow A_2 = \frac95$.
>
> Sanity check: with no direct terms, $\sum_k A_k = H(\infty) = b_0$: $\frac15+\frac95 = 2$. ✓

> [!success]- The three possible $h[n]$
> - $|z|>2$ (causal): $h[n] = \frac15\left(\frac13\right)^n u[n] + \frac95\, 2^n u[n]$.
> - $|z|<\frac13$ (anti-causal): $h[n] = -\frac15\left(\frac13\right)^n u[-n-1] - \frac95\, 2^n u[-n-1]$.
> - $\frac13<|z|<2$ (two-sided, stable): $h[n] = \frac15\left(\frac13\right)^n u[n] - \frac95\, 2^n u[-n-1]$.

## Complex-conjugate poles → a cosine

A real $X(z)$ with complex poles has them in conjugate pairs $re^{\pm j\omega_0}$, and the two residues are conjugates too, so the pair combines into one real sinusoid:
$$
A p^n + A^{*}(p^{*})^n = 2|A|\,r^n\cos\!\left(\omega_0 n + \angle A\right).
$$

> [!example]- Lecture 8, Exercise 2: $H(z) = \dfrac{3-\frac32 z^{-1}}{1-z^{-1}+z^{-2}}$, causal
> Poles: $p = \frac12 \pm j\frac{\sqrt3}{2} = e^{\pm j\pi/3}$. Setting $z = e^{j\pi/3}$ in $3-\frac32 z^{-1} = A_1\left(1-e^{-j\pi/3}z^{-1}\right) + A_2\left(1-e^{j\pi/3}z^{-1}\right)$ gives $A_1 = \frac32$, and likewise $A_2 = \frac32$. So
> $$
> h[n] = \tfrac32\left(e^{j\pi n/3} + e^{-j\pi n/3}\right)u[n] = 3\cos\!\left(\tfrac{\pi}{3}n\right)u[n].
> $$
> Shortcut: match the table row $\frac{1-\cos(\omega_0)z^{-1}}{1-2\cos(\omega_0)z^{-1}+z^{-2}}$ with $\omega_0 = \pi/3$: $H(z)$ is exactly 3 times it. SP2021 #5 works the same way: $\frac{3z^{-1}}{1+z^{-2}}$ is 3 times the $\sin(\frac{\pi}{2}n)u[n]$ row.

## Improper $X(z)$ → long division first

If the numerator's degree in $z^{-1}$ is at least the denominator's (an input term $x[n-k]$ delayed at least as much as the last feedback term $y[n-N]$), divide first ([[2-z-transform/10-improper-transfer-functions-and-system-algebra|Lecture 10]], [[0-toolkit/04-factoring-and-long-division|long division]]):
$$
X(z) = \underbrace{\sum_{k=0}^{M-N-1} C_k z^{-k}}_{\text{impulses } C_k\delta[n-k]} \;+\; \sum_{k=1}^{N}\frac{A_k}{1-p_k z^{-1}} .
$$

> [!example]- Lecture 10, Exercise 1: $H(z) = \dfrac{1-3z^{-1}+z^{-2}+4z^{-3}}{1-2z^{-1}-3z^{-2}}$, causal
> Dividing (as polynomials in $z^{-1}$) gives $C_0 = \frac59$, $C_1 = -\frac43$ and remainder $\frac49-\frac59 z^{-1}$:
> $$
> H(z) = \frac59 - \frac43 z^{-1} + \frac{\frac49-\frac59 z^{-1}}{(1-3z^{-1})(1+z^{-1})}
> = \frac59 - \frac43 z^{-1} + \frac{\frac{7}{36}}{1-3z^{-1}} + \frac{\frac14}{1+z^{-1}},
> $$
> $$
> h[n] = \tfrac59\,\delta[n] - \tfrac43\,\delta[n-1] + \tfrac{7}{36}\,3^n u[n] + \tfrac14(-1)^n u[n].
> $$
> Lecture 10's alternative: expand only $\frac{1}{1-2z^{-1}-3z^{-2}} = \frac{3/4}{1-3z^{-1}} + \frac{1/4}{1+z^{-1}}$ and add four shifted, scaled copies of its inverse (one per numerator term). Same $h[n]$, messier to write.

Equal degrees count as improper too: FA2025 #6's $H(z) = \frac{1-z^{-2}}{(1-2z^{-1})(1+\frac23 z^{-1})} = \frac34 + \frac{9/16}{1-2z^{-1}} - \frac{5/16}{1+\frac23 z^{-1}}$ (one constant $C_0 = \frac34$).

**Pure delays: pull them out.** For $Y(z) = \frac{\frac18 z^{-3}}{(1+\frac13 z^{-1})(1-\frac12 z^{-1})}$ (SP2025 #4b), expand $\frac{1}{(1+\frac13 z^{-1})(1-\frac12 z^{-1})} = \frac{2/5}{1+\frac13 z^{-1}} + \frac{3/5}{1-\frac12 z^{-1}}$, invert, then shift by 3 and scale by $\frac18$: $y[n] = \frac{1}{20}\left(-\frac13\right)^{n-3}u[n-3] + \frac{3}{40}\left(\frac12\right)^{n-3}u[n-3]$.

## Repeated poles

A double pole at $p$ needs two terms:
$$
\frac{A}{1-pz^{-1}} + \frac{B}{(1-pz^{-1})^2}
\;\longleftrightarrow\;
A\,p^n u[n] + B\,(n+1)p^n u[n] \quad (\text{causal}).
$$
Get $B$ by cover-up with the squared factor, then $A$ by comparing one coefficient. Example: $\frac{1+z^{-1}}{(1-\frac12 z^{-1})^2}$: $1+z^{-1} = A(1-\frac12 z^{-1}) + B$; $z^{-1}=2$ gives $B=3$, the $z^{-1}$ coefficient gives $A=-2$, so $x[n] = (3n+1)\left(\frac12\right)^n u[n]$. The course mostly avoids these in PFE problems; they show up through the $(n+1)a^n$ and $na^n$ [[concepts/z-transform-pairs|pairs]] (SP2021 #4, FA2024 #7d) and as the double poles that make [[concepts/marginal-stability|marginally stable]] systems blow up.

## Checking with Python

`scipy.signal.residuez(b, a)` does the whole expansion in the course's $z^{-1}$ form: `r` are the $A_k$, `p` the $p_k$, `k` the direct terms $C_k$ (for a repeated pole, `r` lists the $\frac{1}{1-pz^{-1}}$ coefficient first, then the squared one).

```python
from scipy.signal import residuez
# L8 Ex. 1: H(z) = (2 - z^-1) / (1 - 7/3 z^-1 + 2/3 z^-2)
r, p, k = residuez([2, -1], [1, -7/3, 2/3])
print(r, p, k)      # residues A_k, poles p_k, direct terms C_k
# L10 Ex. 1 (improper): (1 - 3z^-1 + z^-2 + 4z^-3) / (1 - 2z^-1 - 3z^-2)
r, p, k = residuez([1, -3, 1, 4], [1, -2, -3])
print(r, p, k)
```

```text
[0.2 1.8] [0.33333333 2.        ] []
[0.25       0.19444444] [-1.  3.] [ 0.55555556 -1.33333333]
```

($0.2 = \frac15$, $1.8 = \frac95$; $0.1944 = \frac{7}{36}$, $0.5556 = \frac59$, $-1.3333 = -\frac43$.)

> [!trap]
> - **Plug in $z = p_k$, i.e. $z^{-1} = 1/p_k$.** Substituting $p_k$ for $z^{-1}$ is the most common slip.
> - **Divide first** when the numerator degree (in $z^{-1}$) is $\ge$ the denominator's; otherwise the $A_k$ come out wrong and $\delta$ terms go missing.
> - Stay in **one form**: factors $(1-pz^{-1})$ with the table in $z^{-1}$. A PFE of $X(z)$ in powers of $z$ (the "$X(z)/z$" method) gives different constants; don't mix the two.
> - The PFE does not depend on the ROC — **the ROC only picks each term's side**. Two terms can go opposite ways (two-sided ROC).
> - A pole cancelled by a zero has **no term** (its $A_k$ would be 0): cancel common factors first ([[concepts/pole-zero-cancellation|pole-zero cancellation]]).
> - Conjugate poles give conjugate $A_k$; for a real signal, combine them into $2|A|r^n\cos(\omega_0 n+\angle A)$.
> - Quick checks: $\sum_k A_k + C_0 = X(\infty)$, and for a causal $h$, $h[0] = H(\infty)$.

**Where it appears.**
- Lectures: [[2-z-transform/08-inverse-z-transform|L8]] (procedure, Exercises 1–2), [[2-z-transform/09-transfer-functions|L9]] (impulse responses of LCCDEs), [[2-z-transform/10-improper-transfer-functions-and-system-algebra|L10]] (improper case).
- Problem families: [[problems/all-possible-rocs]], [[problems/lccde-to-transfer-function-and-response]], [[problems/infinite-length-convolution]] (via $Y = HX$), [[problems/two-sided-systems-as-recursions]] (splitting $H = H_1 + H_2$).
- Homework: [[homework/hw3|HW3]] #3, #4; [[homework/hw4|HW4]] #1, #4, #5, #6.
- Past exams: [[0-midterm-1/past-exams/fall-2025|FA2025]] #6, #7; [[0-midterm-1/past-exams/spring-2025|SP2025]] #4b, #8; [[0-midterm-1/past-exams/fall-2024|FA2024]] #7; [[0-midterm-1/past-exams/fall-2023|FA2023]] #6, #7; [[0-midterm-1/past-exams/spring-2023|SP2023]] #6; [[0-midterm-1/past-exams/spring-2021|SP2021]] #5, #7; [[0-midterm-1/past-exams/fall-2019|FA2019]] #10. Some PFE appears on every exam.

Related: [[concepts/inverse-z-transform]] · [[concepts/region-of-convergence]] · [[concepts/z-transform-pairs]] · [[concepts/poles-and-zeros]] · [[concepts/transfer-function]] · [[demos/python-demos]]

### Sources for this page
Lecture 8 notes §2.2 (procedure, Exercises 1–2) and slides (Examples 2–3); Lecture 10 notes §1.1–1.2 and annotated slides 7–8 (long division, $C_0=\frac59$, $C_1=-\frac43$); exam keys FA2025 #6, SP2025 #4b, SP2021 #4–#5. Verification: `verify/concepts/verify_pfe.py` (39/39, including the repeated-pole case) and `verify_zdomain_extra.py`; the Python output above is pasted from a real run.
