---
title: "Factoring and long division"
description: "Factoring 1 + a z^-1 + b z^-2 into first-order terms, reading poles and zeros correctly from z^-1 form (including those at 0 and infinity), the cover-up rule for partial fractions, and polynomial long division in z^-1 for improper transfer functions (Lecture 10), with the scipy residuez / tf2zpk equivalents."
tags: [toolkit, z-transform, lccde]
---

*Toolkit · reference page · the algebra of [[2-z-transform/08-inverse-z-transform|Lecture 8]] (PFE), [[2-z-transform/09-transfer-functions|Lecture 9]] (poles and zeros) and [[2-z-transform/10-improper-transfer-functions-and-system-algebra|Lecture 10]] (long division)*

Every LCCDE, PFE and stability problem on the exam passes through the same three moves: factor the denominator, split into first-order terms, and — if the numerator is too long — divide first.

## Factoring $1 + a z^{-1} + b z^{-2}$

$$
1 + a z^{-1} + b z^{-2} = (1 - p_1 z^{-1})(1 - p_2 z^{-1}),\qquad p_1 + p_2 = -a,\quad p_1 p_2 = b .
$$

The $p_i$ are the roots of $z^2 + az + b = 0$ (multiply through by $z^2$). Guess from sum and product, or use the quadratic formula.

| denominator | poles | where |
|---|---|---|
| $1 - 2z^{-1} - 3z^{-2} = (1-3z^{-1})(1+z^{-1})$ | $3,\ -1$ | Lecture 10, Exercise 1 |
| $1 - \tfrac43 z^{-1} - \tfrac43 z^{-2} = (1-2z^{-1})(1+\tfrac23 z^{-1})$ | $2,\ -\tfrac23$ | [[0-midterm-1/past-exams/fall-2025\|FA2025 #6]] |
| $1 - \tfrac34 z^{-1} + \tfrac18 z^{-2} = (1-\tfrac12 z^{-1})(1-\tfrac14 z^{-1})$ | $\tfrac12,\ \tfrac14$ | [[0-midterm-1/past-exams/spring-2023\|SP2023 #6]], FA2019 #10 |
| $1 + z^{-1} - \tfrac34 z^{-2} = (1-\tfrac12 z^{-1})(1+\tfrac32 z^{-1})$ | $\tfrac12,\ -\tfrac32$ | [[0-midterm-1/past-exams/spring-2025\|SP2025 #8]] |
| $1 + \tfrac16 z^{-1} - \tfrac13 z^{-2} = (1+\tfrac23 z^{-1})(1-\tfrac12 z^{-1})$ | $-\tfrac23,\ \tfrac12$ | [[homework/hw3\|HW3 #4]] |
| $1 + z^{-2} = (1-jz^{-1})(1+jz^{-1})$ | $\pm j$ | SP2021 #5 |
| $1 - 2r\cos\omega_0\,z^{-1} + r^2 z^{-2} = (1-re^{j\omega_0}z^{-1})(1-re^{-j\omega_0}z^{-1})$ | $re^{\pm j\omega_0}$ | table pairs 11–12 |

> [!trap] $(1 - p\,z^{-1})$ has its pole at $z = +p$
> $1 + 2z^{-1}$ is a pole at $z=-2$, not $+2$. Check each factor by setting it to zero: $1 + 2z^{-1} = 0 \iff z = -2$.

## Reading poles and zeros from $z^{-1}$ form

Poles and zeros are values of $z$, so rewrite in positive powers first: multiply numerator **and** denominator by $z^{\max(M,N)}$, where $M$, $N$ are the highest powers of $z^{-1}$ in the numerator and denominator.

- $\dfrac{1-z^{-2}}{(1-2z^{-1})(1+\tfrac23 z^{-1})} = \dfrac{z^2-1}{(z-2)(z+\tfrac23)}$: zeros $\pm1$, poles $2, -\tfrac23$; nothing at $0$ or $\infty$ (FA2025 #6).
- $\dfrac{z^{-1}}{1-\tfrac12 z^{-1}} = \dfrac{1}{z-\tfrac12}$: pole $\tfrac12$, **no** zero at $0$ — the zero is at $z=\infty$.
- $\dfrac{3z^{-1}}{1+z^{-2}} = \dfrac{3z}{z^2+1}$: zero at $z=0$, poles $\pm j$, one more zero at $\infty$ (SP2021 #5).
- $\dfrac{1-3z^{-1}+z^{-2}+4z^{-3}}{1-2z^{-1}-3z^{-2}} = \dfrac{z^3-3z^2+z+4}{z\,(z^2-2z-3)}$: poles $3, -1$ **and $0$** — an improper $H$ has poles at the origin (Lecture 10's example).

> [!key] Counting rule
> With the points $z=0$ and $z=\infty$ included, a rational $H(z)$ has as many poles as zeros. Extra powers of $z^{-1}$ in the numerator ($M>N$) put $M-N$ poles at $z=0$; extra powers in the denominator put zeros at $0$; positive powers of $z$ (e.g. the $z^4$ of [[0-midterm-1/past-exams/fall-2025|FA2025 #5a]]) put poles at $\infty$ — which is why that ROC excludes $\infty$ and the signal is not causal. See [[concepts/poles-and-zeros|poles and zeros]].

## The cover-up rule (partial fractions)

For a **proper** $X(z)$ (numerator degree in $z^{-1}$ less than the denominator's) with distinct poles:

$$
X(z) = \sum_k \frac{A_k}{1 - p_k z^{-1}},\qquad A_k = \Big[(1 - p_k z^{-1})\,X(z)\Big]_{z = p_k}.
$$

> [!example] FA2025 #7: $H(z) = \dfrac{1-z^{-1}}{(1+2z^{-1})(1+\tfrac23 z^{-1})}$
> Cover up $(1+2z^{-1})$ and set $z=-2$ (so $z^{-1} = -\tfrac12$): $A_1 = \dfrac{1+\tfrac12}{1-\tfrac13} = \dfrac94$. Cover up $(1+\tfrac23 z^{-1})$ and set $z = -\tfrac23$ ($z^{-1} = -\tfrac32$): $A_2 = \dfrac{1+\tfrac32}{1-3} = -\dfrac54$.
> Check at $z=\infty$ ($z^{-1}=0$): $A_1 + A_2 = 1 = H(\infty)$. ✓ Which term becomes left- or right-sided is then decided by the ROC — for the stable choice $\tfrac23<\lvert z\rvert<2$, $h[n] = -\tfrac94(-2)^n u[-n-1] - \tfrac54(-\tfrac23)^n u[n]$ ([[problems/all-possible-rocs|all possible ROCs]]).

**Repeated pole:** a factor $(1-pz^{-1})^2$ needs both $\dfrac{A}{1-pz^{-1}}$ and $\dfrac{B}{(1-pz^{-1})^2}$; cover-up gives $B$, and one more point (e.g. $z^{-1} = 0$) gives $A$. The pair to invert with is $(n+1)p^n u[n] \leftrightarrow \dfrac{1}{(1-pz^{-1})^2}$ (see [[0-toolkit/02-geometric-series|geometric series]]).

## Long division for improper transfer functions (Lecture 10)

If the numerator's highest power of $z^{-1}$ is **at least** the denominator's, the cover-up rule does not apply yet. Divide first:

$$
H(z) = \underbrace{\sum_{k=0}^{M-N} C_k z^{-k}}_{\text{quotient} \;\to\; C_k\,\delta[n-k]} + \underbrace{\sum_{k=1}^{N}\frac{A_k}{1-p_k z^{-1}}}_{\text{PFE of remainder / denominator}}
$$

(here $M$ and $N$ are the highest powers of $z^{-1}$ in the numerator and denominator).

> [!recipe] Long division in $z^{-1}$
> 1. Write both polynomials in **descending** powers of $z^{-1}$ (highest power first) — treat $w = z^{-1}$ as the variable.
> 2. Divide leading term by leading term, multiply the whole denominator by that quotient term, subtract.
> 3. Repeat until the remainder's degree is below the denominator's. Quotient terms are the $C_k z^{-k}$.
> 4. PFE the remainder over the factored denominator with the cover-up rule.
> 5. Check: $C_0 + \sum_k A_k = H(\infty) = b_0/a_0$.

> [!example] Lecture 10, Exercise 1: $y[n] = 2y[n-1] + 3y[n-2] + x[n] - 3x[n-1] + x[n-2] + 4x[n-3]$, causal
> $H(z) = \dfrac{1-3z^{-1}+z^{-2}+4z^{-3}}{1-2z^{-1}-3z^{-2}}$ — numerator degree 3, denominator degree 2, so two quotient terms $C_0 + C_1 z^{-1}$.
> $$
> \begin{aligned}
> &\text{step 1: } \frac{4z^{-3}}{-3z^{-2}} = -\tfrac43 z^{-1},\\
> &\quad (1-3z^{-1}+z^{-2}+4z^{-3}) - \big(-\tfrac43 z^{-1}\big)(1-2z^{-1}-3z^{-2})\\
> &\qquad = 1 - \tfrac53 z^{-1} - \tfrac53 z^{-2};\\[4pt]
> &\text{step 2: } \frac{-\tfrac53 z^{-2}}{-3z^{-2}} = \tfrac59,\\
> &\quad \big(1 - \tfrac53 z^{-1} - \tfrac53 z^{-2}\big) - \tfrac59\,(1-2z^{-1}-3z^{-2}) = \tfrac49 - \tfrac59 z^{-1}.
> \end{aligned}
> $$
> So $C_1 = -\tfrac43$, $C_0 = \tfrac59$, remainder $\tfrac49 - \tfrac59 z^{-1}$. Cover-up on $\dfrac{\tfrac49 - \tfrac59 z^{-1}}{(1-3z^{-1})(1+z^{-1})}$: at $z=3$, $A_1 = \dfrac{\tfrac49 - \tfrac{5}{27}}{1+\tfrac13} = \dfrac{7}{36}$; at $z=-1$, $A_2 = \dfrac{\tfrac49 + \tfrac59}{1+3} = \dfrac14$. Check: $\tfrac59 + \tfrac{7}{36} + \tfrac14 = 1 = b_0/a_0$. ✓
> $$
> h[n] = \tfrac59\,\delta[n] - \tfrac43\,\delta[n-1] + \tfrac{7}{36}\,3^n u[n] + \tfrac14(-1)^n u[n].
> $$
> (The notes' second subtraction line has a sign and an exponent slip; their final numbers are right — [[0-toolkit/05-errata|errata]].)

> [!tip] Two cheaper alternatives, both in Lecture 10
> - **PFE of $1/A(z)$, then shift:** $\dfrac{1}{1-2z^{-1}-3z^{-2}} = \dfrac{3/4}{1-3z^{-1}} + \dfrac{1/4}{1+z^{-1}}$, so $h[n] = g[n] - 3g[n-1] + g[n-2] + 4g[n-3]$ with $g[n] = \big(\tfrac34 3^n + \tfrac14(-1)^n\big)u[n]$. Same $h$, uglier form.
> - **Divide in ascending powers** (constant term first) and you get the power series of the causal $h[n]$ directly: $1, -1, 2, 5, 16, 47, \dots$ — a quick numerical check of any closed form.

## Python: `residuez` and `tf2zpk`

`residuez(b, a)` returns exactly the course's PFE form: `R` = $A_k$, `P` = $p_k$, `K` = $C_k$ (in powers of $z^{-1}$). `tf2zpk` reads `b` and `a` as polynomials in **positive** powers of $z$, which matches $z^{-1}$ form only when both arrays have the same length — pad with zeros first.

```python
import numpy as np
from scipy.signal import residuez, tf2zpk
b = [1, -3, 1, 4]                 # 1 - 3z^-1 + z^-2 + 4z^-3
a = [1, -2, -3]                   # 1 - 2z^-1 - 3z^-2
R, P, K = residuez(b, a)          # A_k, p_k, C_k
print("R =", np.round(R.real, 4), " P =", P.real, " K =", np.round(K.real, 4))
print("poles, unpadded:", tf2zpk(b, a)[1].real)        # misses z = 0 !
print("poles, padded:  ", tf2zpk(b, a + [0])[1].real)  # equal lengths first
```

```text
R = [0.25   0.1944]  P = [-1.  3.]  K = [ 0.5556 -1.3333]
poles, unpadded: [ 3. -1.]
poles, padded:   [ 3. -1.  0.]
```

$0.1944 = \tfrac{7}{36}$, $0.5556 = \tfrac59$, $-1.3333 = -\tfrac43$. More in [[demos/python-demos|Python demos]].

## Related

[[concepts/partial-fraction-expansion|partial fraction expansion]] · [[concepts/inverse-z-transform|inverse z-transform]] · [[concepts/transfer-function|transfer function]] · [[concepts/poles-and-zeros|poles and zeros]] · [[concepts/pole-zero-cancellation|pole-zero cancellation]] · [[problems/lccde-to-transfer-function-and-response|LCCDE → transfer function → response]] · [[0-toolkit/01-complex-numbers|complex numbers]] (complex-conjugate poles).

### Sources for this page

Lecture 8 notes (PFE, cover-up); Lecture 9 notes (transfer functions, poles and zeros); Lecture 10 notes §1.1–1.2 (Exercise 1, long division, the $1/A(z)$ alternative; PDF p. 2 rendered to read the division); FA2025 #5(a), #6, #7; SP2025 #8; SP2023 #6; SP2021 #5; HW3 #4. Checked in `verify/hub/toolkit_factoring.py` (34 checks) with `scipy.signal.residuez`, `tf2zpk` and `lfilter`.
