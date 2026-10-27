---
title: "z-transform pairs"
description: "The Lecture 6 table of z-transform pairs plus the derived pairs past exams keep using (shifted exponentials, (n+1)aⁿ, pulses, a^|n|, left-sided shifts, cos²) — every row checked numerically."
tags: [concept, z-transform, roc]
aliases: ["z-transform table", "transform pairs", "table of z-transform pairs"]
---

*Lecture 6 (Fri Sep 4) Table 1 · Lecture 7 §2 (rows from properties) · Lecture 8 §2 (read backwards) · [[homework/hw3|HW3]] #1–#3 · family: [[problems/z-transform-with-roc|z-transform with ROC]]*

> [!abstract] In one breath
> - Two pairs generate the table: $a^nu[n]\leftrightarrow\frac{1}{1-az^{-1}}$ ($\lvert z\rvert>\lvert a\rvert$) and $-a^nu[-n-1]\leftrightarrow$ the same formula ($\lvert z\rvert<\lvert a\rvert$).
> - $n\,a^n$ rows come from the differentiation property, cosine/sine rows from Euler + $a^nu[n]$, shifted rows from $z^{-k}$.
> - Every row carries its ROC; a finite sequence has none of the poles its formula suggests.

## 1. The two pairs everything else is built from

> [!key] Lecture 6, Exercise 2 and the left-sided twin
> $$
> \begin{gathered}
> a^n u[n] \;\longleftrightarrow\; \frac{1}{1-az^{-1}},\ \ |z|>|a|
> \\[4pt]
> -a^n u[-n-1] \;\longleftrightarrow\; \frac{1}{1-az^{-1}},\ \ |z|<|a|
> \end{gathered}
> $$
> Same formula, opposite ROCs. Both are one [[0-toolkit/02-geometric-series|geometric series]]; $a$ may be complex (e.g. $a = e^{j\omega_0}$ gives $e^{j\omega_0 n}u[n] \leftrightarrow \frac{1}{1-e^{j\omega_0}z^{-1}}$, $|z|>1$).

## 2. The Lecture 6 table (Table 1, after Manolakis and Ingle Table 3.1)

| $x[n]$ | $X(z)$ | ROC |
|---|---|---|
| $\delta[n]$ | $1$ | all $z$ |
| $\delta[n-m]$ | $z^{-m}$ | all $z$ except $0$ ($m>0$) or $\infty$ ($m<0$) |
| $u[n]$ | $\frac{1}{1-z^{-1}}$ | $\lvert z\rvert > 1$ |
| $-u[-n-1]$ | $\frac{1}{1-z^{-1}}$ | $\lvert z\rvert < 1$ |
| $a^n u[n]$ | $\frac{1}{1-az^{-1}}$ | $\lvert z\rvert > \lvert a\rvert$ |
| $-a^n u[-n-1]$ | $\frac{1}{1-az^{-1}}$ | $\lvert z\rvert < \lvert a\rvert$ |
| $n a^n u[n]$ | $\frac{az^{-1}}{(1-az^{-1})^2}$ | $\lvert z\rvert > \lvert a\rvert$ |
| $-n a^n u[-n-1]$ | $\frac{az^{-1}}{(1-az^{-1})^2}$ | $\lvert z\rvert < \lvert a\rvert$ |
| $\cos(\omega_0 n)u[n]$ | $\frac{1-\cos(\omega_0)z^{-1}}{1-2\cos(\omega_0)z^{-1}+z^{-2}}$ | $\lvert z\rvert > 1$ |
| $\sin(\omega_0 n)u[n]$ | $\frac{\sin(\omega_0)z^{-1}}{1-2\cos(\omega_0)z^{-1}+z^{-2}}$ | $\lvert z\rvert > 1$ |
| $a^n\cos(\omega_0 n)u[n]$ | $\frac{1-a\cos(\omega_0)z^{-1}}{1-2a\cos(\omega_0)z^{-1}+a^2z^{-2}}$ | $\lvert z\rvert > \lvert a\rvert$ |
| $a^n\sin(\omega_0 n)u[n]$ | $\frac{a\sin(\omega_0)z^{-1}}{1-2a\cos(\omega_0)z^{-1}+a^2z^{-2}}$ | $\lvert z\rvert > \lvert a\rvert$ |

In the last two rows $a>0$ is the pole **radius**: the poles are $a e^{\pm j\omega_0}$. The cos/sin rows are the $a=1$ case — poles $e^{\pm j\omega_0}$ **on the unit circle**, which is why their ROC is $|z|>1$ and why they matter for [[concepts/marginal-stability|marginal stability]]. $n\,a^n$ rows: [[concepts/z-transform-properties|differentiation property]]; cosine/sine rows: Euler + $a^n u[n]$ (Lecture 7).

Lecture 8 builds every inverse from three rows plus the shift: $\delta[n-k]\leftrightarrow z^{-k}$, $a^nu[n]\leftrightarrow\frac{1}{1-az^{-1}}$ ($|z|>|a|$), $-a^nu[-n-1]\leftrightarrow\frac{1}{1-az^{-1}}$ ($|z|<|a|$); a factor $z^{-k}$ delays its term by $k$ ([[concepts/inverse-z-transform|inverse z-transform]]).

## 3. Derived pairs that past exams use

Each follows from the table plus one [[concepts/z-transform-properties|property]] (linearity, shift, time reversal).

| $x[n]$ | $X(z)$ | ROC | how / where |
|---|---|---|---|
| $(n+1)a^n u[n]$ | $\frac{1}{(1-az^{-1})^2}$ | $\lvert z\rvert > \lvert a\rvert$ | $na^nu[n] + a^nu[n]$; SP2021 #4; $u*u=(n+1)u[n]$ |
| $a^n u[n-k]$ | $\frac{a^k z^{-k}}{1-az^{-1}}$ | $\lvert z\rvert > \lvert a\rvert$ (and $<\infty$ if $k<0$) | $a^n u[n-k] = a^k\,a^{n-k}u[n-k]$; HW3 #1b, FA2025 #5a, SP2025 #5c |
| $u[n]-u[n-N]$ | $\frac{1-z^{-N}}{1-z^{-1}} = \sum_{k=0}^{N-1} z^{-k}$ | $z \neq 0$ | finite pulse: the pole at 1 cancels; FA2025 #5b ($N=8$) |
| $a^{\lvert n\rvert}$, $\ \lvert a\rvert<1$ | $\frac{1}{1-az^{-1}} - \frac{1}{1-a^{-1}z^{-1}} = \frac{1-a^2}{(1-az^{-1})(1-az)}$ | $\lvert a\rvert < \lvert z\rvert < \frac{1}{\lvert a\rvert}$ | $a^nu[n] + (1/a)^n u[-n-1]$; HW3 #1d |
| $a^n u[-n]$ | $\frac{1}{1-a^{-1}z} = \frac{-az^{-1}}{1-az^{-1}}$ | $\lvert z\rvert < \lvert a\rvert$ | $\delta[n] + a^n u[-n-1]$; HW3 #1c, FA2024 #5c |
| $a^n u[-n+k]$, $k>0$ | $\frac{a^k z^{-k}}{1-a^{-1}z} = \frac{-a^{k+1}z^{-(k+1)}}{1-az^{-1}}$ | $0 < \lvert z\rvert < \lvert a\rvert$ | shift of the row above; SP2025 #5b ($a=3$, $k=2$) |
| $\cos^2(\omega_0 n)u[n]$ | $\frac{1/2}{1-z^{-1}} + \frac12\,\frac{1-\cos(2\omega_0)z^{-1}}{1-2\cos(2\omega_0)z^{-1}+z^{-2}}$ | $\lvert z\rvert > 1$ | $\cos^2\theta = \frac12 + \frac12\cos 2\theta$; FA2025 #5c |
| $\sum_{k=k_s}^{k_e} x[k]\,\delta[n-k]$ | $\sum_{k=k_s}^{k_e} x[k]\,z^{-k}$ | all $z$ except $0$ (if $k_e>0$), $\infty$ (if $k_s<0$) | any finite sequence; HW3 #1a, FA2024 #5b, FA2019 #5 |

> [!example]- Worked instances (all verified)
> - FA2025 #5c, $\omega_0 = \pi/4$: $\cos(2\omega_0) = 0$, so $\cos^2(\tfrac{\pi}{4}n)u[n] \leftrightarrow \dfrac{1/2}{1-z^{-1}} + \dfrac{1/2}{1+z^{-2}}$, $|z|>1$. Equivalently $\tfrac12\cdot\frac{1}{1-z^{-1}} + \tfrac14\cdot\frac{1}{1-jz^{-1}} + \tfrac14\cdot\frac{1}{1+jz^{-1}}$.
> - HW3 #1b: $\left(\tfrac34\right)^{n+3}u[n-2] = \left(\tfrac34\right)^5\left(\tfrac34\right)^{n-2}u[n-2] \leftrightarrow \dfrac{(3/4)^5 z^{-2}}{1-\frac34 z^{-1}}$, $|z|>\tfrac34$.
> - SP2025 #5b: $3^n u[-n+2] \leftrightarrow \dfrac{9z^{-2}}{1-\frac13 z} = \dfrac{-27z^{-3}}{1-3z^{-1}}$, $0<|z|<3$ (left-sided but ends at $n=2>0$, so $z=0$ is excluded).
> - HW3 #1a: $\delta[n+3]+4\delta[n]-\delta[n-2] \leftrightarrow z^3+4-z^{-2}$, $0<|z|<\infty$.
> - FA2023 #5: $n\,u[n+1] = -\delta[n+1] + n u[n] \leftrightarrow -z + \dfrac{z^{-1}}{(1-z^{-1})^2}$, $1<|z|<\infty$.

> [!trap]
> - **The left-sided pair carries a minus sign**: $-a^n u[-n-1] \leftrightarrow \frac{1}{1-az^{-1}}$, so $a^n u[-n-1] \leftrightarrow \frac{-1}{1-az^{-1}}$. The course handout `transform_tables.pdf` (Table 10, row 3) prints "$u[-n-1] \leftrightarrow \frac{1}{1-z^{-1}}$" — the minus is missing; the Lecture 6 table is right (see [[0-toolkit/05-errata|errata]]).
> - **Shifted exponentials need the constant.** $a^n u[n-k] \neq \frac{z^{-k}}{1-az^{-1}}$; first rewrite $a^n = a^k a^{n-k}$.
> - **$u[-n]$ includes $n=0$**, $u[-n-1]$ does not. Mixing them up drops or adds a $\delta[n]$.
> - The cos/sin rows have ROC $|z|>1$ — the poles sit on the unit circle, not at $\cos\omega_0$.
> - $na^nu[n]$ has an $az^{-1}$ in the numerator; $(n+1)a^nu[n]$ does not. Double poles come from these rows ([[concepts/partial-fraction-expansion|PFE]] with repeated poles).
> - The rectangular pulse $u[n]-u[n-N]$ has **no pole at $z=1$** (it cancels): ROC $z\neq0$, not $|z|>1$.

**Checking a pair yourself.** Sum $\sum_n x[n]z^{-n}$ at a point inside the ROC and compare with the closed form.

> [!exam] The z-transform problem appears on 6 of 7 exams
> Forward (with ROC) and backwards after PFE. Put this table on your [[exams/midterm-1/cheat-sheet|cheat sheet]].
> [[exams/midterm-1/past-exams/fall-2025|FA2025 #5]] · [[exams/midterm-1/past-exams/spring-2025|SP2025 #5]] · [[exams/midterm-1/past-exams/fall-2024|FA2024 #5]] · [[exams/midterm-1/past-exams/fall-2023|FA2023 #5]] · [[exams/midterm-1/past-exams/spring-2021|SP2021 #4]] · [[exams/midterm-1/past-exams/fall-2019|FA2019 #5]]

**Where it appears:** [[2-z-transform/06-the-z-transform|L6]] (Table 1), [[2-z-transform/07-z-transform-properties|L7]] (properties that generate new rows), [[2-z-transform/08-inverse-z-transform|L8]] (read backwards for the inverse); [[problems/z-transform-with-roc|z-transform with ROC]] (forward), [[problems/all-possible-rocs|All possible ROCs (inverse z by partial fractions)]] and [[problems/lccde-to-transfer-function-and-response|LCCDE ⇄ transfer function ⇄ response]] (backwards, after PFE); [[homework/hw3|HW3]] #1–#3.

## Related
[[concepts/z-transform]] · [[concepts/z-transform-properties]] · [[concepts/region-of-convergence]] · [[concepts/inverse-z-transform]] · [[concepts/sided-sequences]] · [[supplements/transform-tables]]

### Sources for this page
Lecture 6 notes (Table 1, Exercises 1–2) and slides; Lecture 8 notes §1.1 (finite-length form); `transform_tables.pdf` Table 10 (sign erratum in row 3 confirmed on the rendered PDF); HW3 and its solutions; exam keys FA2025, SP2025, FA2024, FA2023, SP2021, FA2019.
