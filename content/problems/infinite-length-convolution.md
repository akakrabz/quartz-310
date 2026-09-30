---
title: "Infinite-length convolution"
description: "Convolutions where at least one sequence never ends: the convolution sum with u[k]u[n−k] limits and a geometric sum, the finite-times-infinite shortcut (a sum of shifted copies), when the sum diverges, and the z-domain route Y = XH as a check."
tags: [problem-family, problem, convolution, z-transform, midterm-1]
family_frequency: "5 of 7 exams"
typical_points: "5–8"
lectures: [4, 7]
---

*Problem family · part (b) of the convolution problem on the five most recent exams · 5–8 points · uses [[1-signals-and-systems/04-impulse-response-and-convolution|Lecture 4]] (convolution sum) and [[2-z-transform/07-z-transform-properties|Lecture 7]] (convolution property, for the check) · toolkit: [[0-toolkit/02-geometric-series|geometric series]] · concepts: [[concepts/convolution]], [[concepts/unit-step]], [[concepts/z-transform-properties]]*

## What it looks like on the exam

One sequence (or both) is infinitely long: an exponential times a shifted step, against either another exponential or a short sequence *disguised* as steps. There are only two kinds, and recognizing which one you have is half the problem.

**Kind 1 — exponential * exponential** (a convolution sum and a geometric series):

- [[0-midterm-1/past-exams/spring-2025|SP2025 #4b]]: $x[n]=\left(-\tfrac13\right)^n u[n]$, $h[n]=\left(\tfrac12\right)^n u[n-3]$.
- [[0-midterm-1/past-exams/spring-2023|SP2023 #3b]]: $x[n]=\left(-\tfrac12\right)^n u[n]$, $h[n]=\left(\tfrac23\right)^n u[n-1]$.
- [[homework/hw2|HW2 #5(d)]]: $(-1)^n u[n] * e^{-n}u[n]$; [[homework/hw2|HW2 #5(e)]]: $0.5^n u[n] * 2^{-n}u[-n]$ — **does not exist** (see below).
- [[1-signals-and-systems/04-impulse-response-and-convolution|Lecture 4 §2.2.3]]: $u[n]*\left(-\tfrac34\right)^n u[n]$.

**Kind 2 — finite * infinite** (write the finite one as deltas; the answer is a sum of shifted copies):

- [[0-midterm-1/past-exams/fall-2025|FA2025 #3b]]: $x[n]=n\,u[n+1]\,u[-n+1]$, $h[n]=n\left(\tfrac13\right)^n\cos(n)$.
- [[0-midterm-1/past-exams/fall-2024|FA2024 #4b]]: $x[n]=e^{-n}u[n]$, $h[n]=(n+1)(u[n]-u[n-3])$.
- [[0-midterm-1/past-exams/fall-2023|FA2023 #3b]]: $x[n]=\left(\tfrac34\right)^n u[n]$, $h[n]=2u[n]-u[n-1]-u[n-2]$.
- [[0-midterm-1/past-exams/spring-2023|SP2023 #3c]]: $x[n]=\log(\lvert n\rvert+1)$, $h[n]=u[n+1]-u[n-2]$.
- [[homework/hw2|HW2 #5(b)]]: $3^{-n}u[n]*\{\underset{\uparrow}{0},1,2\}$; [[homework/hw2|HW2 #5(c)]]: $u[n]*n(u[n]-u[n-4])$; [[1-signals-and-systems/04-impulse-response-and-convolution|Lecture 4 §2.3]]: $\{\underset{\uparrow}{1},0,2,0,-3\}$ against a sinusoidal $h[n]$.

> [!success]- Answers to the exam and homework instances
> | instance | $y[n]$ |
> |---|---|
> | SP2025 #4b | $\tfrac1{20}\left(-\tfrac13\right)^{n-3}u[n-3]+\tfrac{3}{40}\left(\tfrac12\right)^{n-3}u[n-3]$ |
> | SP2023 #3b | $\tfrac47\left[\left(\tfrac23\right)^n-\left(-\tfrac12\right)^n\right]u[n-1]$ |
> | FA2025 #3b | $x=\{-1,\underset{\uparrow}{0},1\}$, so $y[n]=-h[n+1]+h[n-1]$ |
> | FA2024 #4b | $h=\{\underset{\uparrow}{1},2,3\}$: $e^{-n}u[n]+2e^{-(n-1)}u[n-1]+3e^{-(n-2)}u[n-2]$ |
> | FA2023 #3b | $h=2\delta[n]+\delta[n-1]$: $2\left(\tfrac34\right)^n u[n]+\left(\tfrac34\right)^{n-1}u[n-1]$ |
> | SP2023 #3c | $h=\{1,\underset{\uparrow}{1},1\}$: $\log(\lvert n+1\rvert+1)+\log(\lvert n\rvert+1)+\log(\lvert n-1\rvert+1)$ |
> | HW2 #5(b) | $3^{-(n-1)}u[n-1]+2\cdot3^{-(n-2)}u[n-2]$ |
> | HW2 #5(c) | $u[n-1]+2u[n-2]+3u[n-3]$ |
> | HW2 #5(d) | $\dfrac{e^{-n}+(-1)^n e}{1+e}\,u[n]$ |
> | HW2 #5(e) | diverges for every $n$: each term of the sum equals $0.5^n$ and there are infinitely many |
> | Lecture 4 | $\tfrac47\left[1-\left(-\tfrac34\right)^{n+1}\right]u[n]$ |
>
> Each is compared sample-by-sample with a long truncated convolution sum in `verify/problems/infinite_convolution.py`.

## The method

> [!recipe] Route 1 — the convolution sum (exponential * exponential)
> 1. **Write the sum with the steps kept:** $y[n]=\sum_{k}x[k]\,h[n-k]$, e.g. $\sum_k \left(-\tfrac12\right)^k u[k]\,\left(\tfrac23\right)^{n-k}u[n-k-1]$.
> 2. **Turn each step into an inequality on $k$:** $u[k-a]$ means $k\ge a$; $u[n-k-b]$ means $k\le n-b$. The sum runs over $\max(\text{lower bounds})\le k\le\min(\text{upper bounds})$.
> 3. **Read off where $y$ lives:** the range is non-empty only when lower $\le$ upper, e.g. $0\le n-1 \iff n\ge1$. That condition *is* the step factor of the answer ($u[n-1]$ here). The first sample is $x[\text{first}]\,h[\text{first}]$, at (start of $x$) + (start of $h$).
> 4. **Pull the $n$-only factors out and sum the geometric series:**
> $$
> \sum_{k=K_1}^{K_2} r^k=\frac{r^{K_1}-r^{K_2+1}}{1-r}\quad(r\neq1),\qquad \sum_{k=K_1}^{K_2}1 = K_2-K_1+1 .
> $$
> 5. **Simplify** to $A\,a^n+B\,b^n$ times the step from step 3.
> 6. **Check:** evaluate your formula at the first index (must equal $x[\text{first}]h[\text{first}]$) and at the next one; then, if time allows, the z-domain route below.

Two identities cover most exam cases (both right-sided, starting at 0); shifted versions follow by pulling the shift out *with its constant* — $\left(\tfrac12\right)^n u[n-3] = \tfrac18\left(\tfrac12\right)^{n-3}u[n-3]$:

$$
a^n u[n] * b^n u[n]=\frac{a^{n+1}-b^{n+1}}{a-b}\,u[n]\ \ (a\neq b),\qquad a^n u[n]*a^n u[n]=(n+1)\,a^n u[n].
$$

For SP2025 #4b this gives, with $g[n]=\left(-\tfrac13\right)^n u[n]*\left(\tfrac12\right)^n u[n]=\left[\tfrac35\left(\tfrac12\right)^n+\tfrac25\left(-\tfrac13\right)^n\right]u[n]$, the answer $y[n]=\tfrac18\,g[n-3]$ — the key's result above, with first sample $y[3]=\tfrac18=x[0]\,h[3]$ ✓.

> [!recipe] Route 2 — finite * infinite: a sum of shifted copies
> 1. **Unmask the finite sequence.** Differences of steps and "polynomial × window" are short lists: $2u[n]-u[n-1]-u[n-2]=2\delta[n]+\delta[n-1]$; $(n+1)(u[n]-u[n-3])=\{\underset{\uparrow}{1},2,3\}$; $n\,u[n+1]u[-n+1]=\{-1,\underset{\uparrow}{0},1\}$; $u[n+1]-u[n-2]=\{1,\underset{\uparrow}{1},1\}$. Tabulate a few values of $n$ if unsure.
> 2. **Write it as deltas**, $x[n]=\sum_k c_k\,\delta[n-k]$.
> 3. **Answer** $y[n]=\sum_k c_k\,h[n-k]$ — each copy with its argument shifted *everywhere*, step included: $h[n-1]=\left(\tfrac34\right)^{n-1}u[n-1]$, not $\left(\tfrac34\right)^{n-1}u[n]$.
> 4. Leave it as a sum of shifted terms unless asked to combine; if you combine, split by ranges of $n$.

> [!recipe] Route 3 — the z-domain check (and when a convolution does not exist)
> $Y(z)=X(z)H(z)$ with ROC at least $\text{ROC}_x\cap\text{ROC}_h$; partial fractions give $y[n]$ back ([[2-z-transform/08-inverse-z-transform|Lecture 8]]). This is the fastest way to confirm the constants $A$, $B$ from route 1 (cover-up). **If the two ROCs do not overlap, the convolution sum diverges** — e.g. HW2 #5(e): $0.5^n u[n]$ needs $\lvert z\rvert>0.5$ while $2^{-n}u[-n]$ needs $\lvert z\rvert<0.5$; in the time domain every term of $\sum_k x[k]h[n-k]$ equals $0.5^n$, and there are infinitely many of them. When a sum has infinitely many terms, check that they shrink before summing.

> [!example] Python: check a closed form against `np.convolve`
> For right-sided sequences that start at $n=0$, the first $N$ output samples need only the first $N$ samples of each input, so a truncated `np.convolve` is *exact* on $0\le n<N$.
> ```python
> import numpy as np
>
> n = np.arange(25)
> x = (-1/3) ** n                          # SP2025 #4(b): x[n] = (-1/3)^n u[n]
> h = 0.5 ** n * (n >= 3)                  #               h[n] = (1/2)^n u[n-3]
> y = np.convolve(x, h)[:25]               # exact for n = 0..24: both start at n = 0
> closed = ((1/20) * (-1/3) ** (n - 3.0) + (3/40) * 0.5 ** (n - 3.0)) * (n >= 3)
> print(np.round(y[:6], 5))
> print("max |numeric - closed form| =", np.max(np.abs(y - closed)))
> ```
> ```text
> [0.      0.      0.      0.125   0.02083 0.02431]
> max |numeric - closed form| = 3.469446951953614e-18
> ```

> [!trap] Where the points go
> - **Dropping the step factor.** The formula from the geometric sum is valid only where the $k$-range is non-empty; without $u[n-1]$ (or $u[n-3]$) the answer claims nonzero output before the input arrives.
> - **Limits from habit.** "$\sum_{k=0}^{n}$" is right only when both sequences start at 0. With $u[n-k-1]$ the upper limit is $n-1$; with $u[k+1]$ the lower limit is $-1$.
> - **Off-by-one in the geometric sum:** $\sum_{k=0}^{n}r^k$ has $n+1$ terms, $\frac{1-r^{n+1}}{1-r}$.
> - **Losing the shift constant:** $\left(\tfrac12\right)^n u[n-3]$ is $\tfrac18\left(\tfrac12\right)^{n-3}u[n-3]$, not $\left(\tfrac12\right)^{n-3}u[n-3]$.
> - **Shifting only half of a copy:** $h[n-2]$ shifts the exponent *and* the step.
> - **"Simplifying" a divergent sum into a formula** — or declaring divergence without looking at the terms. Right-sided * right-sided with decaying tails always converges; mixed-sided pairs need the ROC-overlap test.
> - **$a=b$:** the identity's denominator is zero; the answer is $(n+1)a^n u[n]$.

## Practice problems

> [!question] Practice 1 — both steps shifted
> Compute $y[n]=x[n]*h[n]$ for $x[n]=\left(\tfrac13\right)^n u[n+1]$ and $h[n]=\left(\tfrac12\right)^n u[n-1]$, and confirm with the z-transform.

> [!success]- Solution
> **Limits.** $y[n]=\sum_k \left(\tfrac13\right)^k u[k+1]\,\left(\tfrac12\right)^{n-k}u[n-k-1]$: need $k\ge-1$ and $k\le n-1$, non-empty iff $n\ge0$. So $y$ starts at $n=0$ ($=-1+1$), with $y[0]=x[-1]h[1]=3\cdot\tfrac12=\tfrac32$.
>
> **Sum.** For $n\ge0$, with $r=\tfrac{1/3}{1/2}=\tfrac23$:
> $$
> y[n]=\left(\tfrac12\right)^n\sum_{k=-1}^{n-1}\left(\tfrac23\right)^k
> =\left(\tfrac12\right)^n\cdot\frac{\left(\tfrac23\right)^{-1}-\left(\tfrac23\right)^{n}}{1-\tfrac23}
> =\left(\tfrac12\right)^n\left[\tfrac92-3\left(\tfrac23\right)^n\right].
> $$
> $$
> \boxed{\,y[n]=\left[\tfrac92\left(\tfrac12\right)^n-3\left(\tfrac13\right)^n\right]u[n]\,}\qquad y[0]=\tfrac92-3=\tfrac32\ \checkmark
> $$
> **z-domain.** $X(z)=\sum_{n\ge-1}\left(\tfrac13\right)^n z^{-n}=\dfrac{3z}{1-\frac13z^{-1}}$ ($\tfrac13<\lvert z\rvert<\infty$), $H(z)=\dfrac{\frac12z^{-1}}{1-\frac12z^{-1}}$ ($\lvert z\rvert>\tfrac12$), so
> $$
> Y(z)=\frac{3/2}{\left(1-\frac13z^{-1}\right)\left(1-\frac12z^{-1}\right)},\quad \lvert z\rvert>\tfrac12;\qquad
> A_{1/2}=\frac{3/2}{1-\frac13\cdot2}=\tfrac92,\quad A_{1/3}=\frac{3/2}{1-\frac12\cdot3}=-3\ \checkmark
> $$

> [!question] Practice 2 — a finite sequence in disguise
> $x[n]=2u[n]-3u[n-1]+u[n-2]$ and $h[n]=n\left(\tfrac12\right)^n u[n]$. Find $y=x*h$ in the simplest form.

> [!success]- Solution
> Tabulate $x$: $x[0]=2$, $x[1]=2-3=-1$, $x[n]=2-3+1=0$ for $n\ge2$. So $x=2\delta[n]-\delta[n-1]$ and
> $$
> y[n]=2h[n]-h[n-1]=2n\left(\tfrac12\right)^n u[n]-(n-1)\left(\tfrac12\right)^{n-1}u[n-1].
> $$
> For $n\ge1$ both terms are present: $\left(\tfrac12\right)^{n-1}\left[n-(n-1)\right]=\left(\tfrac12\right)^{n-1}$; at $n=0$ both vanish. Hence
> $$
> \boxed{\,y[n]=\left(\tfrac12\right)^{n-1}u[n-1]\,}
> $$
> z-check: $X(z)=2-z^{-1}=2\left(1-\tfrac12z^{-1}\right)$ cancels one of the double poles of $H(z)=\dfrac{\frac12z^{-1}}{\left(1-\frac12z^{-1}\right)^2}$, leaving $Y(z)=\dfrac{z^{-1}}{1-\frac12z^{-1}}$ ✓.

> [!question] Practice 3 — mixed sides
> (a) Compute $2^n u[-n-1] * \left(\tfrac13\right)^n u[n]$. (b) Does $u[n]*\left(\tfrac12\right)^n u[-n]$ exist?

> [!success]- Solution
> **(a)** $y[n]=\sum_{k\le-1,\ k\le n}2^k\left(\tfrac13\right)^{n-k}=\left(\tfrac13\right)^n\sum_{k\le\min(n,-1)}6^k$. Two regimes:
> - $n\le-1$: $\sum_{k\le n}6^k=\dfrac{6^n}{1-\frac16}=\tfrac65\,6^n$, so $y[n]=\tfrac65\,2^n$;
> - $n\ge0$: $\sum_{k\le-1}6^k=\dfrac{1/6}{1-1/6}=\tfrac15$, so $y[n]=\tfrac15\left(\tfrac13\right)^n$.
> $$
> \boxed{\,y[n]=\tfrac65\,2^n u[-n-1]+\tfrac15\left(\tfrac13\right)^n u[n]\,}\qquad y[-1]=\tfrac35 .
> $$
> z-check: $Y(z)=\dfrac{-1}{\left(1-2z^{-1}\right)\left(1-\frac13z^{-1}\right)}$ on $\tfrac13<\lvert z\rvert<2$; cover-up gives $-\tfrac65$ at the pole $2$ (left-sided term $+\tfrac65 2^n u[-n-1]$) and $\tfrac15$ at the pole $\tfrac13$ ✓.
>
> **(b)** No. $\left(\tfrac12\right)^n u[-n]=2^{-n}$ for $n\le0$ *grows* toward $-\infty$. At any $n$, $y[n]=\sum_{k\ge\max(0,n)}2^{k-n}$ has infinitely many growing terms (partial sums at $n=0$, summing $k=0$ up to $10$, $20$, $40$: about $2\times10^3$, $2\times10^6$, $2\times10^{12}$). In the z-domain: $\lvert z\rvert>1$ and $\lvert z\rvert<\tfrac12$ do not overlap.

All three are verified in `verify/problems/infinite_convolution.py` (closed forms against truncated sums for $-15\le n<40$, the cover-up constants, and the divergence); the snippet is `verify/problems/snippets/infinite_conv_snippet.py`.

## Related

- [[problems/finite-length-convolution|Finite-length convolution]] — part (a) of the same exam problem; [[demos/convolution-explorer|convolution explorer]] shows the flip-and-slide for exponentials too.
- [[1-signals-and-systems/04-impulse-response-and-convolution|Lecture 4]] (the convolution sum, the three cases), [[2-z-transform/07-z-transform-properties|Lecture 7]] (convolution ↔ multiplication), [[2-z-transform/08-inverse-z-transform|Lecture 8]] (PFE for the check).
- Concepts: [[concepts/convolution]], [[concepts/unit-step]], [[concepts/sided-sequences]], [[concepts/region-of-convergence]], [[concepts/partial-fraction-expansion]]; toolkit: [[0-toolkit/02-geometric-series|geometric series]].
- [[0-midterm-1/practice-drills|Practice drills]]; all families: [[problems/index|exam problem families]].

### Sources for this page

Lecture 4 notes §2.2.3–2.3 ($u[n]*(-\tfrac34)^n u[n]$, finite * infinite by deltas) and slides; Lecture 7 notes (convolution property); HW2 #5(b)–(e) and solutions; FA2025 #3b, SP2025 #4b, FA2024 #4b, FA2023 #3b, SP2023 #3b–c with keys; Midterm 1 review slides (FA2023 #3). Verification: `verify/problems/infinite_convolution.py`, `verify/exams/*.py`.
