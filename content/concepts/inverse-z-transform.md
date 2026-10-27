---
title: "Inverse z-transform"
description: "x[n] from X(z) and its ROC without the contour integral: by inspection for finite and table-shaped transforms, by partial fractions for rational ones; the ROC decides each term's side."
tags: [concept, z-transform, roc]
aliases: ["inverse z-transform", "inverse z transform", "inverse z"]
---

*Lecture 8 (Fri Sep 11) §1–2 · [[homework/hw3|HW3]] #3, [[homework/hw4|HW4]] #1 · family: [[problems/all-possible-rocs|all possible ROCs]]*

> [!abstract] In one breath
> - Reshape $X(z)$ into table entries: polynomial → impulses; proper rational → partial fractions $\sum_k \frac{A_k}{1-p_kz^{-1}}$.
> - The ROC picks each term's side: poles inside the inner circle → right-sided, outside the outer circle → left-sided.
> - Conjugate pole pair → one real (decaying, steady or growing) sinusoid.

## 1. Common forms of the z-transform (Lecture 8 §1)

**Finite-length signals** (eqs. 1–5): $x[n]=\sum_{k=n_s}^{n_e}x[k]\,\delta[n-k]\ \leftrightarrow\ X(z)=\sum_{k=n_s}^{n_e}x[k]\,z^{-k}$ (impulse decomposition of Lecture 4, then the shift property).

**Infinite-length signals** (eqs. 6–7). Table transforms are **rational**: a ratio of polynomials in $z^{-1}$. **Proper**: numerator degree < denominator degree ($N-1<M$).

$$
\begin{gathered}
\underbrace{X(z)=\frac{\sum_{k=0}^{N-1}b_kz^{-k}}{1+\sum_{k=1}^{M}a_kz^{-k}}}_{(1)\ \text{polynomials}}
\qquad
\underbrace{X(z)=\frac{\prod_{k=1}^{N-1}\left(1-q_kz^{-1}\right)}{\prod_{k=1}^{M}\left(1-p_kz^{-1}\right)}}_{(2)\ \text{factored: zeros } q_k,\ \text{poles } p_k}
\\[8pt]
\underbrace{X(z)=\sum_{k=1}^{M}\frac{A_k}{1-p_kz^{-1}}}_{(3)\ \text{partial fractions}}
\end{gathered}
$$

- $N$ input terms, $M$ feedback terms; form (2) as drawn has $b_0=1$ (else a constant $b_0$ multiplies it).
- Form (3) is the goal: every term is a table entry.

## 2. The inverse z-transform (Lecture 8 §2)

Formal definition (eq. 8): $x[n]=\frac{1}{j2\pi}\oint_C X(z)\,z^{n-1}\,dz$. Never used in the course ("Don't worry, we won't use this formula!").

> [!key] Everything is built from three facts (Lecture 8 §2)
> $$
> \begin{gathered}
> \delta[n-k]\ \leftrightarrow\ z^{-k},\qquad
> a^nu[n]\ \leftrightarrow\ \frac{1}{1-az^{-1}}\ \ (\lvert z\rvert>\lvert a\rvert),\\[4pt]
> -a^nu[-n-1]\ \leftrightarrow\ \frac{1}{1-az^{-1}}\ \ (\lvert z\rvert<\lvert a\rvert),
> \end{gathered}
> $$
> plus the time shift $x[n-k]\leftrightarrow z^{-k}X(z)$ ([[concepts/z-transform-properties|properties]]): a factor $z^{-k}$ delays its term by $k$. The [[concepts/region-of-convergence|ROC]] picks each term:
> $$
> \frac{A}{1-pz^{-1}} \;\longrightarrow\;
> \begin{cases} A\,p^n\,u[n], & \lvert z\rvert>\lvert p\rvert,\\[2pt]
> -A\,p^n\,u[-n-1], & \lvert z\rvert<\lvert p\rvert. \end{cases}
> $$

**Finite-length signals** (§2.1, eq. 9): the pair of §1 is the inverse; read the coefficients of $z^{-k}$.

**Infinite-length signals** (§2.2): by inspection when $X(z)$ already has table shape; otherwise [[concepts/partial-fraction-expansion|PFE]].

> [!question] Example 1(a)–(c) (Lecture 8 slides) — by inspection
> (a) $X(z)=1-\tfrac14z^{-1}+\tfrac1{16}z^{-2}$ (b) $X(z)=\dfrac{1}{1+\frac13z^{-1}}$, $\lvert z\rvert<\tfrac13$ (c) $X(z)=\dfrac{1}{1-\frac12z^{-1}}-\dfrac{3z^{-1}}{1+\frac15z^{-1}}$, $\lvert z\rvert>\tfrac12$

> [!success]- Answers
> (a) $x[n]=\delta[n]-\tfrac14\delta[n-1]+\tfrac1{16}\delta[n-2]=\{\underset{\uparrow}{1},-\tfrac14,\tfrac1{16}\}$.
> (b) Left-sided pair, $a=-\tfrac13$: $x[n]=-\left(-\tfrac13\right)^nu[-n-1]$.
> (c) Poles $\tfrac12$, $-\tfrac15$ both inside $\lvert z\rvert=\tfrac12$: both right-sided; $z^{-1}$ delays the second term:
> $$
> x[n]=\left(\tfrac12\right)^nu[n]-3\left(-\tfrac15\right)^{n-1}u[n-1].
> $$

Why form (3) (eqs. 10–14): with $A_1=3,\ p_1=\tfrac12,\ A_2=-1,\ p_2=-2$, causal, each term is one lookup:

$$
\frac{3}{1-\frac12z^{-1}}-\frac{1}{1+2z^{-1}}\ \longmapsto\ 3\left(\tfrac12\right)^nu[n]-(-2)^nu[n].
$$

> [!recipe] Rational $X(z)$
> 1. Powers of $z^{-1}$; cancel common factors ([[concepts/pole-zero-cancellation|pole-zero cancellation]]).
> 2. Improper: long division ($C_k\delta[n-k]$) or pull out $z^{-k}$ ([[concepts/partial-fraction-expansion|PFE]] §3).
> 3. PFE by cover-up; check $\sum_k A_k = b_0$.
> 4. Each pole's side from the ROC; all possible ROCs: [[concepts/region-of-convergence|ROC]] §3.
> 5. Re-apply delays; state $u[\cdot]$ factors.

Worked PFE examples (Lecture 8 Exercises 1–2, slides Examples 1(d) and 2, the conjugate-pole rule): [[concepts/partial-fraction-expansion|partial fraction expansion]]. All possible ROCs (slides Example 3): [[concepts/region-of-convergence|region of convergence]] §3.

> [!trap] Points lost on inverse z
> - Substituting $z^{-1}=p_k$ instead of $z^{-1}=1/p_k$.
> - Mixing forms: $\frac{C}{z-p}=\frac{Cz^{-1}}{1-pz^{-1}}$ is $C\,p^{n-1}u[n-1]$, not $C\,p^nu[n]$. Stay in $z^{-1}$.
> - Cover-up needs a proper $X(z)$ with distinct poles. Improper: divide first. Repeated pole: $n\,a^nu[n]\leftrightarrow\frac{az^{-1}}{(1-az^{-1})^2}$.
> - Listing $2^M$ sign patterns: only $M+1$ rings exist; outer pole right + inner pole left is empty.
> - Dropping the minus on left-sided terms: $-A\,p^nu[-n-1]$; both the minus and the $-n-1$.
> - Causal check: $h[0] = H(\infty)$.

> [!exam] Inverse z / PFE / all possible ROCs — 7 of 7 past exams, 15–20 points
> All ROCs and signals, or "stable/causal — find $h[n]$" (one ring). Show the cover-up arithmetic; write $u[n]$ / $u[-n-1]$.
> [[exams/midterm-1/past-exams/fall-2025|FA2025 #7]] · [[exams/midterm-1/past-exams/spring-2025|SP2025 #8]] · [[exams/midterm-1/past-exams/fall-2024|FA2024 #7]] · [[exams/midterm-1/past-exams/fall-2023|FA2023 #6]] · [[exams/midterm-1/past-exams/spring-2023|SP2023 #6]] · [[exams/midterm-1/past-exams/spring-2021|SP2021 #5, #7]] · [[exams/midterm-1/past-exams/fall-2019|FA2019 #6, #7]] · family: [[problems/all-possible-rocs|all possible ROCs]]

**Where it appears:** [[2-z-transform/08-inverse-z-transform|L8]] §1–2 (eqs. 1–14, Example 1)–[[2-z-transform/11-bibo-stability-and-causality|L11]]; [[problems/all-possible-rocs|All possible ROCs (inverse z by partial fractions)]], [[problems/two-sided-systems-as-recursions|Two-sided systems as recursions]]; [[homework/hw3|HW3]] #3, [[homework/hw4|HW4]] #1; [[demos/pole-zero-and-roc-explorer|pole-zero and ROC explorer]], [[demos/python-demos|Python demos]].

## Related
[[concepts/partial-fraction-expansion]] · [[concepts/region-of-convergence]] · [[concepts/z-transform-pairs]] · [[concepts/sided-sequences]] · [[concepts/z-transform]] · [[concepts/poles-and-zeros]] · [[0-toolkit/04-factoring-and-long-division|factoring and long division]] · [[0-toolkit/01-complex-numbers|complex numbers]]

### Sources for this page
Lecture 8 notes §1–2 (eqs. 1–14) and slides (Example 1); HW3 #3 solutions; FA2019 #6, FA2025 #7 keys; past exams above.
