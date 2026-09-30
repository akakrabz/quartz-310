---
title: "Finding h (or H) from input–output pairs"
description: "Recover an LTI system from what it did: deconvolve short sequences by inspection, build δ out of the given inputs, use h = g[n] − g[n−1] for a step response, or divide H = Y/X in the z-domain and pick the ROC. On every past Midterm 1."
tags: [problem-family, problem, systems, convolution, z-transform, midterm-1]
family_frequency: "7 of 7 exams"
typical_points: "5–15"
lectures: [4, 8, 9]
---

*Problem family · on all seven past exams (twice on FA2024 and SP2023) · 5–10 points in the time domain, 15–21 when it grows into a full transfer-function problem · uses [[1-signals-and-systems/04-impulse-response-and-convolution|Lecture 4]], [[2-z-transform/08-inverse-z-transform|Lecture 8]], [[2-z-transform/09-transfer-functions|Lecture 9]] · concepts: [[concepts/impulse-response]], [[concepts/step-response]], [[concepts/transfer-function]], [[concepts/system-algebra]]*

## What it looks like on the exam

"Here is what the system did — what is the system?" The data come in four shapes, and each has its own move. Linearity and time invariance are the whole toolkit: whatever combination of shifted inputs you form, the same combination of shifted outputs comes out.

**1. Short sequences — deconvolve by inspection** (often with one branch of a series/parallel connection known):

- [[0-midterm-1/past-exams/spring-2025|SP2025 #3]]: parallel $h_1=\delta[n-1]$ and unknown $h_2$; $x=\{\underset{\uparrow}{1},2,1\}\mapsto y=\{1,\underset{\uparrow}{2},2,2,1\}$. Find $h_2$, the overall $h$, causal?
- [[0-midterm-1/past-exams/fall-2024|FA2024 #3]]: series, $h_2=\{\underset{\uparrow}{2},1\}$ known; $x=\{\underset{\uparrow}{1},-1\}\mapsto y=\{4,\underset{\uparrow}{-2},-2\}$. Find $h_1$, the overall $h$, causal?
- [[0-midterm-1/past-exams/fall-2019|FA2019 #3]]: $x=2\delta[n-2]\mapsto y=\delta[n-1]+2\delta[n-2]+\delta[n-3]$ (as stem plots). Find $h$, the step response, causal?

**2. Several inputs — build $\delta$ out of them:**

- [[0-midterm-1/past-exams/spring-2023|SP2023 #4]]: $x_1=\{\underset{\uparrow}{1},3,6,-3\}$, $x_2=\{\underset{\uparrow}{1},2,-1,0\}$; express $h$ through $y_1$, $y_2$.
- [[homework/hw2|HW2 #4]]: $x=3^{-n}u[n]\mapsto y=5^{-n}u[n-1]$ (one input, shifted copies of itself).

**3. A step response — difference it:**

- [[homework/hw2|HW2 #3]]: express $y$ through the step response $g=h*u$ and $x$.
- [[0-midterm-1/past-exams/fall-2023|FA2023 #4]] (multiple choice): $u[n]\mapsto\delta[n]+\delta[n-1]$; which $h$?

**4. Infinite sequences or transforms — divide, $H=Y/X$:**

- [[0-midterm-1/past-exams/fall-2024|FA2024 #6]]: causal; $\{\underset{\uparrow}{1},\tfrac13,0,\dots\}\mapsto\{\underset{\uparrow}{1},\tfrac12,0,\dots\}$. $H(z)$, $h[n]$, LCCDE.
- [[0-midterm-1/past-exams/spring-2023|SP2023 #6]] (20 pts, in the Midterm 1 review): causal and stable; $X=\dfrac{1}{(1-2z^{-1})(1-z^{-1})}$, $Y=\dfrac{1}{(1-\frac12z^{-1})(1-z^{-1})(1-\frac14z^{-1})}$. $H$ and ROC, $h$, LCCDE.
- [[0-midterm-1/past-exams/spring-2021|SP2021 #7]] (21 pts): causal; $x=\tfrac14\left(-\tfrac13\right)^n u[n]-3\cdot4^n u[-n-1]$ and $Y(z)=\dfrac{13/4}{(1-\frac12z^{-1})(1-z^{-1})(1+\frac13z^{-1})}$.
- [[homework/hw4|HW4 #4]]: causal; $x=2^n(u[n]-3u[n-1])\mapsto y=(3^n-2^n)u[n]$. $h$, stable?

**5. A system described in words or by a formula — feed it $\delta$:** [[0-midterm-1/past-exams/fall-2025|FA2025 #4(b)]]: the modified moving average $y[n]=\frac1L\sum_{k=0}^{L-1}x[n-Sk]$ with $L=3$, $S=4$.

> [!success]- Answers to every instance
> | instance | answer |
> |---|---|
> | SP2025 #3 | $h_2=\delta[n+1]$; $h=h_1+h_2=\{1,\underset{\uparrow}{0},1\}$; not causal |
> | FA2024 #3 | $x*h_2=\{\underset{\uparrow}{2},-1,-1\}$ so $h_1=2\delta[n+1]$; $h=h_1*h_2=\{4,\underset{\uparrow}{2}\}$; not causal |
> | FA2019 #3 | $h=\tfrac12\delta[n+1]+\delta[n]+\tfrac12\delta[n-1]$; step response $\tfrac12u[n+1]+u[n]+\tfrac12u[n-1]$; not causal |
> | SP2023 #4 | $x_1[n]-3x_2[n-1]=\delta[n]$, so $h[n]=y_1[n]-3y_2[n-1]$ |
> | HW2 #4 | $x[n]-\tfrac13x[n-1]=\delta[n]$, so $h[n]=\left(\tfrac15\right)^n u[n-1]-\tfrac13\left(\tfrac15\right)^{n-1}u[n-2]$ |
> | HW2 #3 | $h=g[n]-g[n-1]$, so $y[n]=\big(x[n]-x[n-1]\big)*g[n]$ |
> | FA2023 #4 | $h=g[n]-g[n-1]=\delta[n]-\delta[n-2]=\{\underset{\uparrow}{1},0,-1\}$, choice (b) |
> | FA2024 #6 | $H=\dfrac{1+\frac12z^{-1}}{1+\frac13z^{-1}}$, $\lvert z\rvert>\tfrac13$; $h=\tfrac32\delta[n]-\tfrac12\left(-\tfrac13\right)^n u[n]$; $y[n]=-\tfrac13y[n-1]+x[n]+\tfrac12x[n-1]$ |
> | SP2023 #6 | $H=\dfrac{1-2z^{-1}}{(1-\frac12z^{-1})(1-\frac14z^{-1})}$, $\lvert z\rvert>\tfrac12$; $h=-6\left(\tfrac12\right)^n u[n]+7\left(\tfrac14\right)^n u[n]$; $y[n]=\tfrac34y[n-1]-\tfrac18y[n-2]+x[n]-2x[n-1]$ (the key's LCCDE has a typo) |
> | SP2021 #7 | $X=\dfrac{13/4}{(1+\frac13z^{-1})(1-4z^{-1})}$ on $\tfrac13<\lvert z\rvert<4$; $H=\dfrac{1-4z^{-1}}{(1-\frac12z^{-1})(1-z^{-1})}$, $\lvert z\rvert>1$; $h=7\left(\tfrac12\right)^n u[n]-6u[n]$; not stable |
> | HW4 #4 | $H=\dfrac{z^{-1}}{(1-3z^{-1})(1-6z^{-1})}$, $\lvert z\rvert>6$; $h=\tfrac13\left(6^n-3^n\right)u[n]$; not stable |
> | FA2025 #4(b) | $h=\tfrac13\left(\delta[n]+\delta[n-4]+\delta[n-8]\right)$ (FIR, so always BIBO stable) |
>
> All checked by convolving back or filtering (`verify/problems/finding_h.py`, `verify/exams/*.py`).

## The method

> [!recipe] Pick the move from the shape of the data
> 1. **Series or parallel with a known branch? Remove it first.** Parallel: $y=x*h_1+x*h_2$, so work with $y-x*h_1=x*h_2$. Series: $y=(x*h_2)*h_1$, so convolve $x$ with the known branch and compare that with $y$. Overall: parallel $h=h_1+h_2$, series $h=h_1*h_2$.
> 2. **Short sequences: deconvolve.** $h$ starts at (start of $y$) − (start of $x$) and has length $L_y-L_x+1$. Either spot $y$ as scaled, shifted copies of $x$ (usually one or two), or peel samples off: $h[\text{first}]=y[\text{first}]/x[\text{first}]$, subtract that copy, repeat — this is long division of the polynomials in $z^{-1}$.
> 3. **Several inputs (or one infinite one): make a delta.** Find constants and shifts with $\sum_i c_i\,x_i[n-k_i]=\delta[n]$; then $h[n]=\sum_i c_i\,y_i[n-k_i]$. Line the sequences up and cancel from the second sample on. For a geometric input $a^n u[n]$, the combination is always $x[n]-a\,x[n-1]=\delta[n]$.
> 4. **Step response given: difference it.** $\delta[n]=u[n]-u[n-1]$, so $h[n]=g[n]-g[n-1]$.
> 5. **Exponentials or transforms: divide.** $H(z)=Y(z)/X(z)$; cancel common factors; choose the ROC from what the problem says (causal → outside the outermost pole; stable → contains $\lvert z\rvert=1$) — never from the ROC of $X$ alone. Then PFE (with long division first if the numerator degree in $z^{-1}$ is not smaller) and, if asked, the LCCDE by cross-multiplying.
> 6. **Check:** convolve your $h$ with $x$ and compare with $y$ (sum check $\sum y=\sum x\sum h$ for finite data); read causality ($h[n]=0$ for $n<0$?) and stability ($\sum\lvert h\rvert<\infty$, or poles inside the unit circle for causal $h$) from the answer.

> [!example] Python: finite deconvolution with index bookkeeping (SP2025 #3)
> ```python
> import numpy as np
> from scipy import signal
>
> # SP2025 #3: parallel branches, h1 = delta[n-1] known, h2 unknown
> x, nx = np.array([1., 2, 1]), 0              # x = {[1], 2, 1}
> y, ny = np.array([1., 2, 2, 2, 1]), -1       # y = {1, [2], 2, 2, 1}
> r = y.copy()
> r[2:5] -= x                                  # remove the known branch x*h1 = x[n-1] (n = 1..3)
> print("y - x*h1 =", r, "starting at n =", ny)
> q, rem = signal.deconvolve(np.trim_zeros(r, "b"), x)   # long division in powers of z^-1
> print("h2 =", q, "starting at n =", ny - nx, "| remainder", rem)
> ```
> ```text
> y - x*h1 = [1. 2. 1. 0. 0.] starting at n = -1
> h2 = [1.] starting at n = -1 | remainder [0. 0. 0.]
> ```
> So $h_2=\delta[n+1]$ and $h=\delta[n+1]+\delta[n-1]$. A nonzero remainder would mean the data are not consistent with any finite $h$ — recheck the arithmetic.

> [!trap] Where the points go
> - **Parallel vs series:** $h_1+h_2$ vs $h_1*h_2$. And in a parallel problem, forgetting to subtract the known branch before deconvolving.
> - **The start index of $h$:** start of $y$ minus start of $x$. FA2024 #3's $h=\{4,\underset{\uparrow}{2}\}$ has a sample at $n=-1$, so the system is *not* causal — a one-sample index slip flips that answer too.
> - **Step trick direction:** $h[n]=g[n]-g[n-1]$ (current minus previous), not $g[n+1]-g[n]$.
> - **$H=Y/X$ inherits the ROC of neither.** The ROC of $H$ comes from "causal"/"stable" in the statement; $\text{ROC}_Y\supseteq\text{ROC}_X\cap\text{ROC}_H$ is only a consistency check (SP2021 #7: $X$ is two-sided, $H$ is causal, and the pole of $X$ at 4 is cancelled, so $y$ is right-sided).
> - **Cancelling carelessly.** In SP2023 #6 the common factor $1-z^{-1}$ cancels and the zero $1-2z^{-1}$ of $H$ comes from the *denominator* of $X$. In FA2024 #6 the numerator and denominator have equal degree, so $h$ has a $\delta[n]$ term — long division (or "$h[0]$ from the leading coefficients") before PFE.
> - **Claiming $\delta[n]$ can be built** from inputs that cannot produce it — check the combination sample by sample to the end of the sequence.

## Practice problems

> [!question] Practice 1 — parallel connection with one known branch
> Two LTI systems are connected in parallel; $h_1[n]=2\delta[n-2]$. The input $x[n]=\{\underset{\uparrow}{1},-1,2\}$ produces $y[n]=\{1,\underset{\uparrow}{0},1,4,-2,4\}$. Find $h_2[n]$ and the overall $h[n]$. Is the overall system causal?

> [!success]- Solution
> **Remove the known branch.** $x*h_1=2x[n-2]=\{2,-2,4\}$ at $n=2,3,4$. Subtracting from $y$ (which starts at $n=-1$):
> $$
> y-x*h_1=\{1,\underset{\uparrow}{0},1,4-2,-2+2,4-4\}=\{1,\underset{\uparrow}{0},1,2\}\ (\text{starts at } -1).
> $$
> **Deconvolve.** $h_2$ starts at $-1-0=-1$ and has length $4-3+1=2$. $h_2[-1]=\tfrac{1}{x[0]}=1$; then $0=x[0]h_2[0]+x[1]h_2[-1]=h_2[0]-1$, so $h_2[0]=1$. Check: $\{1,-1,2\}*\{1,1\}=\{1,0,1,2\}$ ✓.
> $$
> h_2[n]=\delta[n+1]+\delta[n],\qquad h[n]=h_1+h_2=\{1,\underset{\uparrow}{1},0,2\}.
> $$
> **Not causal:** $h[-1]=1\neq0$. (Stable: finitely many samples.)

> [!question] Practice 2 — two ways to get δ
> (a) An LTI system maps $x_1=\{\underset{\uparrow}{1},2,-2,6\}$ to $y_1=\{\underset{\uparrow}{2},3,-5,16,-8,6\}$ and $x_2=\{\underset{\uparrow}{1},-1,3\}$ to $y_2=\{\underset{\uparrow}{2},-3,8,-4,3\}$. Find $h[n]$.
> (b) Another LTI system has step response $g[n]=\delta[n+1]+3u[n]-2u[n-2]$. Find $h[n]$. Causal? Stable?

> [!success]- Solution
> **(a)** Line up $x_1$ with a shifted $x_2$ to cancel everything after $n=0$:
> $$
> x_1[n]-2x_2[n-1]=\{1,\ 2-2,\ -2+2,\ 6-6\}=\delta[n].
> $$
> Apply the same combination to the outputs:
> $$
> h[n]=y_1[n]-2y_2[n-1]=\{2,\ 3-4,\ -5+6,\ 16-16,\ -8+8,\ 6-6\}=\{\underset{\uparrow}{2},-1,1\}.
> $$
> **(b)** $h[n]=g[n]-g[n-1]=\big(\delta[n+1]-\delta[n]\big)+3\big(u[n]-u[n-1]\big)-2\big(u[n-2]-u[n-3]\big)$:
> $$
> h[n]=\delta[n+1]+2\delta[n]-2\delta[n-2]=\{1,\underset{\uparrow}{2},0,-2\}.
> $$
> Not causal ($h[-1]=1$); stable (FIR). Check: the running sum of $h$ is $1,3,3,1,1,\dots$ from $n=-1$, which is $g$ ✓.

> [!question] Practice 3 — H = Y/X, then everything else
> A causal LTI system responds to $x[n]=\left(\tfrac12\right)^n u[n]$ with $y[n]=\left[10\left(\tfrac13\right)^n-9\left(\tfrac12\right)^n\right]u[n]$. Find $H(z)$ with its ROC, $h[n]$, the LCCDE, and decide stability.

> [!success]- Solution
> $$
> Y(z)=\frac{10}{1-\frac13z^{-1}}-\frac{9}{1-\frac12z^{-1}}=\frac{10\left(1-\frac12z^{-1}\right)-9\left(1-\frac13z^{-1}\right)}{\left(1-\frac13z^{-1}\right)\left(1-\frac12z^{-1}\right)}=\frac{1-2z^{-1}}{\left(1-\frac13z^{-1}\right)\left(1-\frac12z^{-1}\right)},\qquad X(z)=\frac{1}{1-\frac12z^{-1}} .
> $$
> $$
> H(z)=\frac{Y(z)}{X(z)}=\frac{1-2z^{-1}}{1-\frac13z^{-1}},\qquad \text{ROC } \lvert z\rvert>\tfrac13\ \text{(causal)}.
> $$
> Equal degrees in $z^{-1}$, so divide first: $1-2z^{-1}=6\left(1-\tfrac13z^{-1}\right)-5$, giving $H(z)=6-\dfrac{5}{1-\frac13z^{-1}}$ and
> $$
> h[n]=6\,\delta[n]-5\left(\tfrac13\right)^n u[n]=\delta[n]-5\left(\tfrac13\right)^n u[n-1].
> $$
> ($h[0]=1$, the ratio of the leading coefficients ✓.) **LCCDE:** $y[n]-\tfrac13y[n-1]=x[n]-2x[n-1]$. **Stable:** the only pole, $\tfrac13$, is inside the unit circle and the system is causal.
>
> **Time-domain cross-check** (move 3): $x[n]-\tfrac12x[n-1]=\delta[n]$, so $h[n]=y[n]-\tfrac12y[n-1]$; at $n=0,1$: $h[0]=1$, $h[1]=\left(\tfrac{10}{3}-\tfrac92\right)-\tfrac12=-\tfrac53=-5\cdot\tfrac13$ ✓.

All three are verified in `verify/problems/finding_h.py` (convolving back, `scipy.signal.lfilter` on the LCCDE, the time-domain route); the snippet is `verify/problems/snippets/finding_h_snippet.py`.

## Related

- [[problems/finite-length-convolution|Finite-length convolution]] (this family runs it backwards), [[problems/lccde-to-transfer-function-and-response|LCCDE ↔ H(z) ↔ response]] (where move 5 continues), [[problems/all-possible-rocs|inverse z / PFE / all possible ROCs]] (choosing the ROC).
- Lectures: [[1-signals-and-systems/04-impulse-response-and-convolution|Lecture 4]] (LTI ⇒ $y=x*h$), [[2-z-transform/08-inverse-z-transform|Lecture 8]] (PFE), [[2-z-transform/09-transfer-functions|Lecture 9]] ($H=Y/X$, LCCDE ↔ $H$), [[2-z-transform/10-improper-transfer-functions-and-system-algebra|Lecture 10]] (long division; series and parallel connections).
- Concepts: [[concepts/impulse-response]], [[concepts/step-response]], [[concepts/transfer-function]], [[concepts/system-algebra]], [[concepts/pole-zero-cancellation]].
- Demos: [[demos/convolution-explorer|convolution explorer]] (check a deconvolution by convolving back), [[demos/difference-equation-simulator|difference-equation simulator]] (check an LCCDE's impulse response), [[0-midterm-1/practice-drills|practice drills]]; all families: [[problems/index|exam problem families]].

### Sources for this page

Lecture 4 notes (LTI systems and convolution), Lecture 9 notes and slides (transfer functions), Lecture 10 notes (system algebra); HW2 #3–4, HW4 #4 and solutions; SP2025 #3, FA2024 #3 and #6, FA2023 #4, SP2023 #4 and #6, SP2021 #7, FA2019 #3, FA2025 #4(b) with keys (SP2023 #6(c) typo, see [[0-toolkit/05-errata|errata]]); Midterm 1 review slides (SP2023 #6). Verification: `verify/problems/finding_h.py`, `verify/exams/*.py`.
