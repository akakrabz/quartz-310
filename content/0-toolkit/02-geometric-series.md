---
title: "Geometric series"
description: "Finite and infinite geometric sums, sums that start at k0, left-sided and two-sided sums, and the sum of k a^k — and how each one's convergence condition becomes a z-transform ROC. Every exam z-transform is one of these sums."
tags: [toolkit, z-transform, roc]
---

*Toolkit · reference page · the algebra behind [[2-z-transform/06-the-z-transform|Lecture 6]], [[2-z-transform/07-z-transform-properties|Lecture 7]] and the infinite-length convolutions of [[1-signals-and-systems/04-impulse-response-and-convolution|Lecture 4]]*

A z-transform $X(z) = \sum_n x[n]z^{-n}$ of an exponential signal *is* a geometric series in the ratio $\alpha z^{-1}$ (or $z/\alpha$). So: sum it with the formulas below, and read the ROC off the convergence condition. Nothing else is needed for [[problems/z-transform-with-roc|z-transform-with-ROC]] problems.

## The formulas

> [!key] Geometric sums
> $$
> \begin{aligned}
> \sum_{k=0}^{N-1} a^k &= \frac{1-a^N}{1-a}\quad (a\neq1;\ \text{equals } N \text{ if } a=1) \\
> \sum_{k=k_1}^{k_2} a^k &= \frac{a^{k_1}-a^{k_2+1}}{1-a} \qquad \text{("first term minus first omitted term, over one minus ratio")} \\
> \sum_{k=0}^{\infty} a^k &= \frac{1}{1-a}\quad\text{iff } \lvert a\rvert<1, \qquad \sum_{k=k_0}^{\infty} a^k = \frac{a^{k_0}}{1-a}\quad\text{iff } \lvert a\rvert<1 \\
> \sum_{k=0}^{\infty} k\,a^k &= \frac{a}{(1-a)^2}\quad\text{iff } \lvert a\rvert<1 \qquad \Big(\text{finite: } \sum_{k=0}^{N-1} k\,a^k = \frac{a\big(1-Na^{N-1}+(N-1)a^N\big)}{(1-a)^2}\Big)
> \end{aligned}
> $$
> An infinite geometric series with $\lvert a\rvert\ge1$ diverges — its terms do not even go to zero. That single fact is where every ROC comes from.

Quick check: $\sum_{k=2}^{6}2^k = \dfrac{2^2-2^7}{1-2} = 124$. The $\sum k\,a^k$ formula is $a\,\tfrac{d}{da}$ of $\sum a^k$ — the same move as the "multiply by $n$" property $n\,x[n] \leftrightarrow -z\,\tfrac{dX}{dz}$.

## Finite sums → finite-length signals

A finite-length signal gives a finite sum: it converges for every $z$ except possibly $z=0$ (if some $x[n]\neq0$ with $n>0$) and $z=\infty$ (if some $x[n]\neq0$ with $n<0$).

> [!exam] FA2025 #5(b): $x[n] = u[n]-u[n-8]$
> Eight ones, $n = 0,\dots,7$ (not nine — $u[n]-u[n-N]$ has $N$ samples). $X(z) = \sum_{k=0}^{7} z^{-k} = \dfrac{1-z^{-8}}{1-z^{-1}}$, ROC: all $z$ except $z=0$. The apparent pole at $z=1$ is cancelled by a zero of $1-z^{-8}$ ($X(1) = 8$), so it does not restrict the ROC. See [[0-midterm-1/past-exams/fall-2025|FA2025]].

> [!exam] FA2019 #5(a): $x[n] = 3^{-n}\big(u[n-5]-u[n-100]\big)$
> Nonzero for $5\le n\le 99$ (95 terms): $X(z) = \sum_{k=5}^{99}\big(\tfrac13\big)^k z^{-k} = \dfrac{(\tfrac13)^5 z^{-5}\big(1-(\tfrac13)^{95}z^{-95}\big)}{1-\tfrac13 z^{-1}}$, ROC $z\neq0$. The key boxes the sum form; the closed form is the "first minus first-omitted" rule. See [[0-midterm-1/past-exams/fall-2019|FA2019]].

## Infinite sums → right-sided signals

$$
x[n] = \alpha^n u[n]:\qquad X(z) = \sum_{n=0}^{\infty}(\alpha z^{-1})^n = \frac{1}{1-\alpha z^{-1}}\quad\text{iff } \lvert\alpha z^{-1}\rvert<1 \iff \lvert z\rvert>\lvert\alpha\rvert .
$$

**Starting later:** pull out the first term. [[homework/hw3|HW3 #1(b)]]: $x[n] = (\tfrac34)^{n+3}u[n-2]$, so with $k = n-2$,

$$
X(z) = \sum_{n=2}^{\infty}\Big(\tfrac34\Big)^{n+3}z^{-n} = \Big(\tfrac34\Big)^{5}z^{-2}\sum_{k=0}^{\infty}\Big(\tfrac34 z^{-1}\Big)^k = \frac{(3/4)^5\,z^{-2}}{1-\tfrac34 z^{-1}},\qquad \lvert z\rvert>\tfrac34 .
$$

(One line of the official solution writes $(3/4)^3$ — see [[0-toolkit/05-errata|errata]].)

**Convolving two causal exponentials** is a finite geometric sum in $k$: for $a\neq b$,

$$
\big(a^n u[n]\big)*\big(b^n u[n]\big) = \sum_{k=0}^{n}a^k b^{n-k} = b^n\sum_{k=0}^{n}\Big(\frac{a}{b}\Big)^k = \frac{a^{n+1}-b^{n+1}}{a-b}\,u[n],
$$

and $(n+1)a^n u[n]$ when $a=b$. This is the time-domain route of [[problems/infinite-length-convolution|infinite-length convolution]].

## Left-sided and two-sided sums

Substitute $m = -n$ so the sum runs over positive powers of $z/\alpha$:

$$
-\alpha^n u[-n-1]:\qquad X(z) = -\sum_{n=-\infty}^{-1}\alpha^n z^{-n} = -\sum_{m=1}^{\infty}\Big(\frac{z}{\alpha}\Big)^m = -\frac{z/\alpha}{1-z/\alpha} = \frac{1}{1-\alpha z^{-1}}\quad\text{iff } \lvert z\rvert<\lvert\alpha\rvert .
$$

> [!trap] Same formula, different signal
> $\alpha^n u[n]$ and $-\alpha^n u[-n-1]$ have the **same** algebraic $X(z)$; only the ROC tells them apart. Drop the minus sign on the left-sided one and every anti-causal term in a PFE comes out with the wrong sign (the printed official table does exactly this for $\alpha=1$ — [[0-toolkit/05-errata|errata]]).

> [!exam] SP2025 #5(b): $x[n] = 3^n u[-n+2]$
> Nonzero for $n\le2$. With $m = 2-n\ge0$: $X(z) = \sum_{m=0}^{\infty}3^{2-m}z^{m-2} = 9z^{-2}\sum_{m=0}^{\infty}\big(\tfrac{z}{3}\big)^m = \dfrac{9z^{-2}}{1-z/3} = \dfrac{-27z^{-3}}{1-3z^{-1}}$. Converges iff $\lvert z\rvert<3$, and the $z^{-2}$ (samples at $n=1,2$) removes $z=0$: ROC $0<\lvert z\rvert<3$. See [[0-midterm-1/past-exams/spring-2025|SP2025]].

**Two-sided** signals split into a right-sided and a left-sided sum; $X(z)$ exists only where **both** converge, i.e. on the intersection — an annulus, possibly empty. [[homework/hw3|HW3 #1(d)]]: $(\tfrac14)^{\lvert n\rvert} = (\tfrac14)^n u[n] + 4^n u[-n-1]$ gives

$$
X(z) = \frac{1}{1-\tfrac14 z^{-1}} - \frac{1}{1-4z^{-1}},\qquad \tfrac14<\lvert z\rvert<4 .
$$

By contrast $x[n] = 1$ for all $n$ needs $\lvert z\rvert>1$ (right half) and $\lvert z\rvert<1$ (left half): no z-transform at all. The same emptiness kills one of the four ROC combinations in [[0-midterm-1/past-exams/fall-2019|FA2019 #7]] — see [[problems/all-possible-rocs|all possible ROCs]].

## Weighted by $k$: repeated poles

$\sum k\,a^k$ gives $n\alpha^n u[n] \leftrightarrow \dfrac{\alpha z^{-1}}{(1-\alpha z^{-1})^2}$, $\lvert z\rvert>\lvert\alpha\rvert$. [[0-midterm-1/past-exams/spring-2021|SP2021 #4]]: $(n+1)x[n]$ with $x[n] = (\tfrac12)^n u[n]$ is

$$
\frac{\tfrac12 z^{-1}}{(1-\tfrac12 z^{-1})^2} + \frac{1}{1-\tfrac12 z^{-1}} = \frac{1}{(1-\tfrac12 z^{-1})^2},\qquad \lvert z\rvert>\tfrac12 .
$$

## Convergence ⇔ ROC at a glance

| signal type | the series | converges iff | ROC shape |
|---|---|---|---|
| finite length | finite sum | always (except $z=0$ / $z=\infty$ for positive / negative indices) | all $z$, maybe minus $0$ and/or $\infty$ |
| right-sided $\alpha^n u[n]$ | $\sum_{n\ge0}(\alpha z^{-1})^n$ | $\lvert z\rvert>\lvert\alpha\rvert$ | outside a circle |
| left-sided $-\alpha^n u[-n-1]$ | $\sum_{m\ge1}(z/\alpha)^m$ | $\lvert z\rvert<\lvert\alpha\rvert$ | inside a circle |
| two-sided | both | both conditions | annulus (possibly empty) |
| sum of several | each term | all conditions | intersection (at least — a cancelled pole can widen it) |

The same test decides **stability**: a causal $h[n] = \alpha^n u[n]$ has $\sum_n\lvert h[n]\rvert = \sum_n\lvert\alpha\rvert^n<\infty$ iff $\lvert\alpha\rvert<1$, i.e. iff the ROC $\lvert z\rvert>\lvert\alpha\rvert$ contains the unit circle. See [[concepts/bibo-stability|BIBO stability]] and [[concepts/region-of-convergence|ROC]].

## Python check: a z-transform as a truncated sum

Pick a test point inside the ROC and compare the partial sum with the closed form — how every transform on this site was verified.

```python
import numpy as np
z0 = 1.5 * np.exp(0.4j)                      # test point with |z0| > 3/4
n = np.arange(0, 200)
x = 0.75 ** (n + 3) * (n >= 2)               # (3/4)^(n+3) u[n-2]  (HW3 #1b)
partial = np.sum(x * z0 ** (-n))             # truncated z-transform sum
closed = 0.75**5 * z0**-2 / (1 - 0.75 / z0)  # (3/4)^5 z^-2 / (1 - (3/4) z^-1)
print(np.round(partial, 12), np.round(closed, 12))
print(abs(partial - closed))
```

```text
(0.07572592317-0.167577928771j) (0.07572592317-0.167577928771j)
5.721958498152797e-17
```

Pick $z_0$ *outside* the ROC and the partial sums blow up instead of settling — the ROC made visible.

## Related

[[concepts/z-transform|z-transform]] · [[concepts/region-of-convergence|region of convergence]] · [[concepts/sided-sequences|sided sequences]] · [[concepts/z-transform-pairs|z-transform pairs]] · [[supplements/transform-tables|official transform tables]] · [[0-toolkit/01-complex-numbers|complex numbers]] · [[0-toolkit/04-factoring-and-long-division|factoring and long division]].

### Sources for this page

Lecture 6 notes (definition, ROC from convergence) and Lecture 7 notes (multiplication by $n$); HW3 #1(b), #1(d) and solutions; FA2025 #5(b); FA2019 #5(a), #7; SP2025 #5(b); SP2021 #4. Every sum and transform checked in `verify/hub/toolkit_geometric.py` (46 checks).
