---
title: "Partial fraction expansion (PFE)"
description: "Split a rational X(z) into first-order terms A_k/(1 − p_k z⁻¹) by cover-up so each term inverts by table lookup; conjugate and repeated poles; improper X(z) by long division or the numerator-1 trick."
tags: [concept, z-transform, roc]
aliases: ["PFE", "partial fractions", "partial fraction decomposition", "cover-up", "improper transfer function", "long division"]
---

*Lectures 8 (Fri Sep 11) §2.2 and 10 (Wed Sep 16) §1 · [[homework/hw3|HW3]] #3–#4, [[homework/hw4|HW4]] #1, #3 · families: [[problems/all-possible-rocs|all possible ROCs]], [[problems/lccde-to-transfer-function-and-response|LCCDE → H(z) → response]]*

> [!abstract] In one breath
> - Proper rational $X(z)$ with distinct poles: $X(z)=\sum_k \frac{A_k}{1-p_kz^{-1}}$, each $A_k$ by cover-up; check $\sum_k A_k=b_0$.
> - Conjugate pole pair → one real sinusoid $2\lvert A\rvert r^n\cos(\omega_0n+\angle A)$.
> - Improper (numerator degree in $z^{-1}$ ≥ denominator's): long-divide first; quotient → impulses, remainder → PFE.

## 1. Cover-up for proper X(z) with distinct poles (Lecture 8 §2.2)

> [!key] Proper $X(z)$, distinct poles (Lecture 8 §2.2)
> $$
> \begin{gathered}
> X(z) = \frac{\sum_{k=0}^{M-1} b_k z^{-k}}{\prod_{k=1}^{N}\left(1-p_k z^{-1}\right)} = \sum_{k=1}^{N} \frac{A_k}{1-p_k z^{-1}},
> \\[4pt]
> A_k = \Big[\left(1-p_k z^{-1}\right)X(z)\Big]_{z=p_k}
> \end{gathered}
> $$
> Proper: numerator degree in $z^{-1}$ lower than denominator's. Each term inverts to $A_k p_k^n u[n]$ (ROC outside $\lvert p_k\rvert$) or $-A_k p_k^n u[-n-1]$ (inside) ([[concepts/inverse-z-transform|inverse z-transform]]).

> [!recipe] Partial fraction expansion, cover-up
> 1. **Factor the denominator** into $\prod_k(1-p_kz^{-1})$ (multiply by $z^M$, find roots in $z$; [[0-toolkit/04-factoring-and-long-division|toolkit]]). Write $X(z)=\sum_k\frac{A_k}{1-p_kz^{-1}}$.
> 2. **Multiply both sides** by the full denominator: numerator $=\sum_k A_k\prod_{j\ne k}(1-p_jz^{-1})$.
> 3. **Set $z=p_k$** ($z^{-1}=1/p_k$): all products but the $k$-th vanish. Shortcut (**cover-up**): delete $(1-p_kz^{-1})$ from $X(z)$, evaluate the rest at $z=p_k$.
> 4. **Check**: $\sum_kA_k=b_0$ (set $z^{-1}=0$).

> [!question] Exercise 1 (Lecture 8 notes): $H(z)=\dfrac{2-z^{-1}}{1-\frac73z^{-1}+\frac23z^{-2}}$ — find $h[n]$
> ROC not given (so the factorization does not reveal the poles): give every case.

> [!success]- Answer (eqs. 15–20)
> $1-\tfrac73z^{-1}+\tfrac23z^{-2}=\left(1-\tfrac13z^{-1}\right)\left(1-2z^{-1}\right)$. Cover-up: $A_1=\left.\dfrac{2-z^{-1}}{1-2z^{-1}}\right|_{z^{-1}=3}=\dfrac{-1}{-5}=\dfrac15$ (pole $\tfrac13$), $A_2=\left.\dfrac{2-z^{-1}}{1-\frac13z^{-1}}\right|_{z^{-1}=1/2}=\dfrac{3/2}{5/6}=\dfrac95$ (pole $2$). Check: $\tfrac15+\tfrac95=2=b_0$ ✓.
> - $\lvert z\rvert>2$ (right-sided): $h[n]=\tfrac15\left(\tfrac13\right)^nu[n]+\tfrac95\,2^nu[n]$
> - $\lvert z\rvert<\tfrac13$ (left-sided): $h[n]=-\tfrac15\left(\tfrac13\right)^nu[-n-1]-\tfrac95\,2^nu[-n-1]$
> - $\tfrac13<\lvert z\rvert<2$ (two-sided, stable): $h[n]=\tfrac15\left(\tfrac13\right)^nu[n]-\tfrac95\,2^nu[-n-1]$

> [!question] Example 2 (Lecture 8 slides): $X(z)=\dfrac{2-z^{-1}}{1+\frac23z^{-1}-\frac13z^{-2}}$, $x[n]$ right-sided

> [!success]- Answer
> Roots of $z^2+\tfrac23z-\tfrac13$: $z=\dfrac{-\frac23\pm\sqrt{\frac49+\frac43}}{2}=\dfrac{-\frac23\pm\frac43}{2}=\tfrac13,\ -1$.
> $$
> X(z)=\frac{2-z^{-1}}{\left(1+z^{-1}\right)\left(1-\frac13z^{-1}\right)}=\frac{A_1}{1+z^{-1}}+\frac{A_2}{1-\frac13z^{-1}}.
> $$
> $2-z^{-1}=A_1\left(1-\tfrac13z^{-1}\right)+A_2\left(1+z^{-1}\right)$. $z^{-1}=-1$: $3=\tfrac43A_1$, $A_1=\tfrac94$. $z^{-1}=3$: $-1=4A_2$, $A_2=-\tfrac14$. Check: $\tfrac94-\tfrac14=2=b_0$ ✓.
> $$
> x[n]=\tfrac94(-1)^nu[n]-\tfrac14\left(\tfrac13\right)^nu[n].
> $$

> [!question] Example 1(d) (Lecture 8 slides): $X(z)=\dfrac{1-2z^{-1}+3z^{-2}}{\left(1-z^{-1}\right)\left(1+\frac23z^{-1}\right)\left(1-2z^{-1}\right)}$, $\lvert z\rvert>2$

> [!success]- Answer
> Poles $1,\ -\tfrac23,\ 2$; numerator degree $2<3$: proper. Cover-up with $w=z^{-1}$:
> - pole $1$ ($w=1$): $A_1=\dfrac{1-2+3}{\left(1+\frac23\right)(1-2)}=\dfrac{2}{-5/3}=-\dfrac65$
> - pole $-\tfrac23$ ($w=-\tfrac32$): $A_2=\dfrac{1+3+\frac{27}{4}}{\left(1+\frac32\right)(1+3)}=\dfrac{43/4}{10}=\dfrac{43}{40}$
> - pole $2$ ($w=\tfrac12$): $A_3=\dfrac{1-1+\frac34}{\left(1-\frac12\right)\left(1+\frac13\right)}=\dfrac{3/4}{2/3}=\dfrac98$
>
> Check: $-\tfrac65+\tfrac{43}{40}+\tfrac98=\tfrac{-48+43+45}{40}=1=b_0$ ✓. $\lvert z\rvert>2$: all right-sided:
> $$
> x[n]=\left[-\tfrac65+\tfrac{43}{40}\left(-\tfrac23\right)^n+\tfrac98\,2^n\right]u[n].
> $$

## 2. Conjugate and repeated poles

> [!question] Exercise 2 (Lecture 8 notes): $H(z)=\dfrac{3-\frac32z^{-1}}{1-z^{-1}+z^{-2}}$, causal

> [!success]- Answer (eqs. 21–31)
> Negative discriminant: $p=\dfrac{1\pm\sqrt{1-4}}{2}=\tfrac12\pm j\tfrac{\sqrt3}{2}=e^{\pm j\pi/3}$. Multiply out:
> $$
> 3-\tfrac32z^{-1}=A_1\left(1-e^{-j\pi/3}z^{-1}\right)+A_2\left(1-e^{j\pi/3}z^{-1}\right).
> $$
> $z=e^{j\pi/3}$: $\tfrac94+j\tfrac{3\sqrt3}{4}=A_1\left(\tfrac32+j\tfrac{\sqrt3}{2}\right)$, so $A_1=\tfrac32$ (multiply by the conjugate $\tfrac32-j\tfrac{\sqrt3}2$, divide by $3$). Likewise $A_2=\tfrac32$:
> $$
> h[n]=\tfrac32\left(e^{j\frac{\pi}{3}n}+e^{-j\frac{\pi}{3}n}\right)u[n]=3\cos\left(\tfrac{\pi}{3}n\right)u[n].
> $$

> [!key] Conjugate pole pair $\Rightarrow$ one real sinusoid
> Poles $p=re^{\pm j\omega_0}$, coefficients $A$, $A^*$ (right-sided):
> $$
> A\,p^n+A^*(p^*)^n=2\,\mathrm{Re}\{A\,p^n\}=2\lvert A\rvert\,r^n\cos\left(\omega_0n+\angle A\right)u[n].
> $$
> $r=1$: on the unit circle, periodic ([[concepts/marginal-stability|marginal stability]]); $r<1$: decaying; $r>1$: growing. One coefficient per pair (real $x$: $X(z)=X^*(z^*)$, [[concepts/z-transform-properties|conjugation property]]).

- **Repeated pole:** $\frac{A}{1-pz^{-1}} + \frac{B}{(1-pz^{-1})^2}\leftrightarrow A\,p^n u[n] + B\,(n+1)p^n u[n]$ (causal), from $n\,a^nu[n]\leftrightarrow\frac{az^{-1}}{(1-az^{-1})^2}$ ([[concepts/z-transform-pairs|pairs]]).
- **Pure delay:** pull $z^{-k}$ out, expand the rest, shift at the end.

## 3. Improper rational expressions (Lecture 10 §1)

Proper (Lecture 9): $H(z) = \dfrac{\sum_{k=0}^{M-1} b_k z^{-k}}{1 + \sum_{k=1}^{N} a_k z^{-k}}$ with $M \le N$. $M > N$: **improper**. In LCCDE terms: some input term is delayed at least as far as the most-delayed feedback term ($x[n-3]$ against $y[n-2]$ in Exercise 1 below).

> [!key] Improper = impulses + exponentials (Lecture 10, eqs. 2–3)
> $$
> H(z) = \sum_{k=0}^{M-N-1} C_k z^{-k} + \frac{\sum_{k=0}^{N-1} d_k z^{-k}}{1 + \sum_{k=1}^{N} a_k z^{-k}}
> = \sum_{k=0}^{M-N-1} C_k z^{-k} + \sum_{k=1}^{N}\frac{A_k}{1 - p_k z^{-1}}
> $$
> $$
> \Longrightarrow\quad h[n] = \sum_{k} C_k\,\delta[n-k] + \sum_k A_k\,p_k^n\,u[n] \qquad(\text{causal}).
> $$
> $C_k$: long division. $A_k$: PFE of the **remainder** over the denominator.

> [!question] Exercise 1 (Lecture 10 notes §1.1, slides 4–8): $h[n]$ of the causal LCCDE $y[n] = 2y[n-1] + 3y[n-2] + x[n] - 3x[n-1] + x[n-2] + 4x[n-3]$

> [!success]- Answer (eqs. 4–11)
> $Y(z)\bigl(1 - 2z^{-1} - 3z^{-2}\bigr) = X(z)\bigl(1 - 3z^{-1} + z^{-2} + 4z^{-3}\bigr)$:
> $$
> H(z) = \frac{1 - 3z^{-1} + z^{-2} + 4z^{-3}}{1 - 2z^{-1} - 3z^{-2}} = \frac{1 - 3z^{-1} + z^{-2} + 4z^{-3}}{(1-3z^{-1})(1+z^{-1})}, \qquad \lvert z\rvert > 3 ,
> $$
> $M = 4$, $N = 2$: improper, quotient $C_0 + C_1 z^{-1}$. Divide from the highest power:
> $$
> \begin{aligned}
> &4z^{-3} \div (-3z^{-2}) = -\tfrac43 z^{-1}: \\
> &\bigl(1 - 3z^{-1} + z^{-2} + 4z^{-3}\bigr) - \left(-\tfrac43 z^{-1}\right)\bigl(1 - 2z^{-1} - 3z^{-2}\bigr) = 1 - \tfrac53 z^{-1} - \tfrac53 z^{-2}\\
> &-\tfrac53 z^{-2} \div (-3z^{-2}) = \tfrac59: \\
> &\bigl(1 - \tfrac53 z^{-1} - \tfrac53 z^{-2}\bigr) - \tfrac59\bigl(1 - 2z^{-1} - 3z^{-2}\bigr) = \tfrac49 - \tfrac59 z^{-1}
> \end{aligned}
> $$
> $C_0 = \tfrac59$, $C_1 = -\tfrac43$:
> $$
> H(z) = \frac59 - \frac43 z^{-1} + \frac{\frac49 - \frac59 z^{-1}}{(1-3z^{-1})(1+z^{-1})} = \frac59 - \frac43 z^{-1} + \frac{A_1}{1-3z^{-1}} + \frac{A_2}{1+z^{-1}} .
> $$
> Cover-up on the remainder: $A_1 = \dfrac{\frac49 - \frac59\cdot\frac13}{1 + \frac13} = \dfrac{7}{36}$ ($z = 3$), $A_2 = \dfrac{\frac49 + \frac59}{1 + 3} = \dfrac14$ ($z = -1$). Causal:
> $$
> h[n] = \tfrac59\,\delta[n] - \tfrac43\,\delta[n-1] + \tfrac{7}{36}\,3^n u[n] + \tfrac14\,(-1)^n u[n] .
> $$
> $h = \{\underset{\uparrow}{1}, -1, 2, 5, 16, 47, \dots\}$; $h[0] = \tfrac59 + \tfrac{7}{36} + \tfrac14 = 1 = b_0$.

**A simpler approach** (Lecture 10 §1.2, eqs. 12–14). Factor out the numerator; PFE with numerator 1:
$$
\begin{aligned}
H(z) &= \bigl(1 - 3z^{-1} + z^{-2} + 4z^{-3}\bigr)\,G(z), \qquad \\
G(z) &= \frac{1}{(1-3z^{-1})(1+z^{-1})} = \frac{\frac34}{1-3z^{-1}} + \frac{\frac14}{1+z^{-1}} ,
\end{aligned}
$$
so $g[n] = \tfrac34\,3^n u[n] + \tfrac14(-1)^n u[n]$ and, by linearity and time shifting,
$$
h[n] = g[n] - 3g[n-1] + g[n-2] + 4g[n-3] .
$$
"Unseemly" (notes), but identical sample for sample.

> [!recipe] Improper $H(z) \to h[n]$
> 1. Powers of $z^{-1}$; numerator degree $\ge$ denominator degree ⇒ improper.
> 2. Long-divide from the highest power of $z^{-1}$ until the remainder's degree is below the denominator's: quotient $C_0 + C_1 z^{-1} + \dots$ (drill: [[0-toolkit/04-factoring-and-long-division|toolkit]]).
> 3. Cover-up PFE of remainder ÷ denominator (the original numerator gives the same $A_k$; only division gives the $C_k$).
> 4. $C_k z^{-k} \to C_k\,\delta[n-k]$; $\dfrac{A_k}{1-p_kz^{-1}} \to A_k p_k^n u[n]$ (or $-A_k p_k^n u[-n-1]$).
> 5. Check $h[0] = b_0$ (causal).

> [!trap] Improper or not; cover-up slips
> - Count degrees in $z^{-1}$: $\dfrac{z(z-4)}{z^2-5z+6} = \dfrac{1-4z^{-1}}{(1-2z^{-1})(1-3z^{-1})}$ is **proper** ([[homework/hw4|HW4]] #3(a)).
> - **Equal** degrees in $z^{-1}$ are improper: a constant $C_0$ hides. Cover-up still gives the right $A_k$; without $C_0$, $h[0]$ is wrong.
> - Divide from the **highest** power of $z^{-1}$; from the constant end the division never terminates (it produces $h[0], h[1], \dots$).
> - Plug in $z=p_k$ ($z^{-1}=1/p_k$), not $z^{-1}=p_k$. Stay in the $z^{-1}$ form; the "$X(z)/z$" method gives different constants.
> - The ROC only picks each term's side; cancel common factors first.

> [!exam] Every past Midterm 1
> PFE inside every inverse-z and LCCDE problem; improper $H(z)$ inside LCCDE problems. Show the cover-up arithmetic.
> [[exams/midterm-1/past-exams/fall-2025|FA2025 #6, #7]] · [[exams/midterm-1/past-exams/spring-2025|SP2025 #4b, #8]] · [[exams/midterm-1/past-exams/fall-2024|FA2024 #7]] · [[exams/midterm-1/past-exams/fall-2023|FA2023 #6]] · [[exams/midterm-1/past-exams/spring-2023|SP2023 #6]] · [[exams/midterm-1/past-exams/spring-2021|SP2021 #4–#5]] · [[exams/midterm-1/past-exams/fall-2019|FA2019 #6, #7]] · families: [[problems/all-possible-rocs|all possible ROCs]], [[problems/lccde-to-transfer-function-and-response|LCCDE → H(z) → response]]

**Where it appears:** [[2-z-transform/08-inverse-z-transform|L8]] §2.2 (eqs. 15–31, Exercises 1–2), [[2-z-transform/09-transfer-functions|L9]], [[2-z-transform/10-improper-transfer-functions-and-system-algebra|L10]] §1 (eqs. 1–14, Exercise 1); [[problems/all-possible-rocs|All possible ROCs (inverse z by partial fractions)]], [[problems/lccde-to-transfer-function-and-response|LCCDE ⇄ transfer function ⇄ response]]; [[homework/hw3|HW3]] #3–#4, [[homework/hw4|HW4]] #1, #3; [[demos/python-demos|Python demos]].

## Related
[[concepts/inverse-z-transform]] · [[concepts/region-of-convergence]] · [[concepts/z-transform-pairs]] · [[concepts/poles-and-zeros]] · [[concepts/transfer-function]] · [[0-toolkit/04-factoring-and-long-division|factoring and long division]] · [[0-toolkit/01-complex-numbers|complex numbers]] · [[demos/python-demos]]

### Sources for this page
Lecture 8 notes §2.2 (eqs. 15–31, Exercises 1–2) and slides (Examples 1(d), 2); Lecture 10 notes §1–1.2 (eqs. 1–14, Exercise 1), slides 4–8; HW4 #3(a); FA2025 #6, SP2025 #4b, SP2021 #4–#5 keys.
