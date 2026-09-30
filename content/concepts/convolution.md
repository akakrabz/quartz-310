---
title: "Convolution"
description: "y[n] = Σ x[k] h[n−k], the output of every LTI system: properties, the start/end/length rules, the three hand methods on one example, and np.convolve with n = 0 bookkeeping."
tags: [concept, convolution, systems, midterm-1]
aliases: ["convolution", "convolution sum", "discrete convolution", "linear convolution", "x*h", "(x*h)[n]"]
---

> [!key] Definition (Lecture 4)
> $$
> y[n]=(x*h)[n]=\sum_{k=-\infty}^{\infty}x[k]\,h[n-k]=\sum_{k=-\infty}^{\infty}h[k]\,x[n-k]
> $$
> The response of an [[concepts/lti-system|LTI system]] with [[concepts/impulse-response|impulse response]] $h$ to the input $x$. Procedure: **flip** one signal ($h[-k]$), **shift** it by $n$ ($h[n-k]$), **multiply** sample by sample with $x[k]$, **sum** over $k$; repeat for every $n$.

| property | statement | why you care |
|---|---|---|
| commutative | $x*h=h*x$ | flip the shorter one; cascade order is irrelevant |
| associative | $(x*h_1)*h_2=x*(h_1*h_2)$ | series connection has $h=h_1*h_2$ |
| distributive | $x*(h_1+h_2)=x*h_1+x*h_2$ | parallel connection has $h=h_1+h_2$ |
| identity | $x*\delta=x$ | $\delta[n]$ is the "do nothing" system |
| shift | $x*\delta[n-k]=x[n-k]$; $x[n-a]*h[n-b]=y[n-a-b]$ | shifts just add |
| z-domain | $Y(z)=X(z)H(z)$, ROC at least $R_x\cap R_h$ | [[concepts/z-transform-properties\|convolution property]] |

> [!key] Start, end, length (finite sequences)
> $x$ nonzero on $[n_s,n_e]$ (length $N$), $h$ on $[m_s,m_e]$ (length $M$) $\Rightarrow$ $y$ lives on $[\,n_s+m_s,\ n_e+m_e\,]$ and has length $N+M-1$.

**One example, three methods.** $x[n]=\{\underset{\uparrow}{1},\ 2,\ 3\}$ and $h[n]=\{1,\ \underset{\uparrow}{0},\ -1\}$ (so $h[-1]=1$, $h[1]=-1$). Start $0+(-1)=-1$, end $2+1=3$, length $3+3-1=5$.

*1. Flip-and-shift table.* Row $n$ holds $h[n-k]$ (the flipped $h$ slid to position $n$); multiply by the $x[k]$ row and add:

| | $k=-2$ | $-1$ | $0$ | $1$ | $2$ | $3$ | $4$ | sum of products |
|---|---|---|---|---|---|---|---|---|
| $x[k]$ | | | $1$ | $2$ | $3$ | | | |
| $h[-1-k]$ | $-1$ | $0$ | $1$ | | | | | $y[-1]=1$ |
| $h[-k]$ | | $-1$ | $0$ | $1$ | | | | $y[0]=2$ |
| $h[1-k]$ | | | $-1$ | $0$ | $1$ | | | $y[1]=-1+3=2$ |
| $h[2-k]$ | | | | $-1$ | $0$ | $1$ | | $y[2]=-2$ |
| $h[3-k]$ | | | | | $-1$ | $0$ | $1$ | $y[3]=-3$ |

*2. Toeplitz matrix.* The columns of $\mathbf H$ are copies of $h$, each shifted down one row; the first row is $n=n_s+m_s=-1$:
$$
\begin{bmatrix}y[-1]\\ y[0]\\ y[1]\\ y[2]\\ y[3]\end{bmatrix}=
\begin{bmatrix}1&0&0\\ 0&1&0\\ -1&0&1\\ 0&-1&0\\ 0&0&-1\end{bmatrix}
\begin{bmatrix}1\\ 2\\ 3\end{bmatrix}=
\begin{bmatrix}1\\ 2\\ 2\\ -2\\ -3\end{bmatrix}
$$

*3. Superposition of shifted copies.* $h[n]=\delta[n+1]-\delta[n-1]$, so $y[n]=x[n+1]-x[n-1]$: the copy of $x$ advanced by one minus the copy delayed by one. (Equivalently $x=\delta[n]+2\delta[n-1]+3\delta[n-2]$ gives $y=h[n]+2h[n-1]+3h[n-2]$.) All three give
$$
y[n]=\{1,\ \underset{\uparrow}{2},\ 2,\ -2,\ -3\}.
$$

**Infinite-length signals** need the sum itself (Lecture 4 §2.2.3): the steps in $a^ku[k]\,b^{n-k}u[n-k]$ restrict $k$ to $0\le k\le n$, and a finite geometric sum finishes it:
$$
a^nu[n]*b^nu[n]=\frac{a^{n+1}-b^{n+1}}{a-b}\,u[n]\ (a\ne b),\qquad a^nu[n]*a^nu[n]=(n+1)\,a^nu[n].
$$
Lecture 4's example: $u[n]*(-\tfrac34)^nu[n]=\tfrac47\big(1-(-\tfrac34)^{n+1}\big)u[n]$. A short sequence against a long one is fastest by superposition ([[0-midterm-1/past-exams/fall-2025|FA2025 #3b]]: $x=-\delta[n+1]+\delta[n-1]$ gives $y=-h[n+1]+h[n-1]$).

```python
import numpy as np
x, nx0 = np.array([1, 2, 3]), 0      # x[0] = 1
h, nh0 = np.array([1, 0, -1]), -1    # h[-1] = 1, h[0] = 0, h[1] = -1
y = np.convolve(x, h)                # values only: numpy knows nothing about n = 0
ny0 = nx0 + nh0                      # start of y = start of x + start of h
for n, v in zip(range(ny0, ny0 + len(y)), y):
    print(f"y[{n}] = {v}")
```

```text
y[-1] = 1
y[0] = 2
y[1] = 2
y[2] = -2
y[3] = -3
```

> [!trap]
> - **The $n=0$ arrow.** `np.convolve` and the matrix method return values only; the start index is $n_s+m_s$. Even two official keys mislabel the rows ([[0-toolkit/05-errata|errata]]).
> - **Length counts interior zeros**: $\{1,2,3,0,-1,-2,-3\}$ has length 7, so with a length-3 $h$ the answer has 9 samples ([[0-midterm-1/past-exams/fall-2025|FA2025 #3a]]).
> - **Flip one signal, not both**, and sum products (not a product of sums).
> - **$*$ is not $\times$**: $x[n]*\delta[n-k]=x[n-k]$ (the whole signal shifts) but $x[n]\,\delta[n-k]=x[k]\,\delta[n-k]$ (one sample survives).
> - **Keep the $u[n]$** in infinite-length answers: $y=0$ for $n<0$ came from the limits.
> - **Two-sided sums can diverge**: $(\tfrac12)^nu[n]*2^{-n}u[-n]$ has infinitely many equal terms at every $n$ ([[homework/hw2|HW2]] #5e).
> - Causal $*$ causal is causal (start index $0+0$): [[0-midterm-1/past-exams/fall-2025|FA2025 #1b]] is True.

**Where it appears.** [[1-signals-and-systems/04-impulse-response-and-convolution|Lecture 4]] (all of it), [[2-z-transform/09-transfer-functions|Lecture 9]] ($Y=HX$), [[2-z-transform/10-improper-transfer-functions-and-system-algebra|Lecture 10]] (series and parallel); [[homework/hw2|HW2]] #3–#5. Problem families: [[problems/finite-length-convolution]] (7/7 exams: [[0-midterm-1/past-exams/fall-2025|FA2025 #3a]], [[0-midterm-1/past-exams/spring-2025|SP2025 #4a]], [[0-midterm-1/past-exams/fall-2024|FA2024 #4a]], [[0-midterm-1/past-exams/fall-2023|FA2023 #3a]], [[0-midterm-1/past-exams/spring-2023|SP2023 #3a]], [[0-midterm-1/past-exams/spring-2021|SP2021 #2]], [[0-midterm-1/past-exams/fall-2019|FA2019 #4]]) and [[problems/infinite-length-convolution]] (5/7). Try it: [[demos/convolution-explorer]].

**Related.** [[concepts/lti-system|LTI system]] · [[concepts/impulse-response|impulse response]] · [[concepts/kronecker-delta|Kronecker delta]] · [[concepts/step-response|step response]] · [[concepts/system-algebra|system algebra]] · [[concepts/z-transform-properties|z-transform properties]] · [[concepts/bibo-stability|BIBO stability]]

### Sources for this page
Lecture 4 §2 (definition, properties, start/end/length rules, table, matrix and direct-sum methods, §2.3 finite-by-infinite case); Lecture 4 slides 6–11; HW2 #5; the convolution problems of the seven past exams. Every number checked in `verify/concepts/verify_glossary_time.py` and `verify_systems.py`; the snippet was run as shown.
