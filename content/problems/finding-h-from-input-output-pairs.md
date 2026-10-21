---
title: "Finding h (or H) from input–output pairs"
description: "Recover an LTI system from what it did: deconvolve short sequences, build δ from the given inputs, difference a step response, or divide H = Y/X and pick the ROC. On every past Midterm 1."
tags: [problem-family, problem, systems, convolution, z-transform, midterm-1]
family_frequency: "7 of 7 exams"
typical_points: "5–15"
lectures: [4, 8, 9]
---

*Problem family · all seven past exams (twice on FA2024 and SP2023) · 5–10 points in the time domain, 15–21 as a full transfer-function problem · [[1-signals-and-systems/04-impulse-response-and-convolution|Lecture 4]], [[2-z-transform/08-inverse-z-transform|Lecture 8]], [[2-z-transform/09-transfer-functions|Lecture 9]]*

## What it looks like on the exam

"Here is what the system did; what is the system?" Five data shapes, one move each:

1. **Short sequences: deconvolve**, often with one series/parallel branch known.
   - [[exams/midterm-1/past-exams/spring-2025|SP2025 #3]]: parallel $h_1=\delta[n-1]$, unknown $h_2$; $x=\{\underset{\uparrow}{1},2,1\}\mapsto y=\{1,\underset{\uparrow}{2},2,2,1\}$. $h_2$, $h$, causal?
   - [[exams/midterm-1/past-exams/fall-2024|FA2024 #3]]: series, $h_2=\{\underset{\uparrow}{2},1\}$; $x=\{\underset{\uparrow}{1},-1\}\mapsto y=\{4,\underset{\uparrow}{-2},-2\}$. $h_1$, $h$, causal?
   - [[exams/midterm-1/past-exams/fall-2019|FA2019 #3]]: $2\delta[n-2]\mapsto\delta[n-1]+2\delta[n-2]+\delta[n-3]$. $h$, step response, causal?
2. **Several inputs: build $\delta$.**
   - [[exams/midterm-1/past-exams/spring-2023|SP2023 #4]]: $x_1=\{\underset{\uparrow}{1},3,6,-3\}$, $x_2=\{\underset{\uparrow}{1},2,-1,0\}$; $h$ through $y_1$, $y_2$.
   - [[homework/hw2|HW2 #4]]: $3^{-n}u[n]\mapsto5^{-n}u[n-1]$.
3. **Step response: difference it.** HW2 #3; [[exams/midterm-1/past-exams/fall-2023|FA2023 #4]]: $u[n]\mapsto\delta[n]+\delta[n-1]$, which $h$?
4. **Infinite sequences or transforms: $H=Y/X$.**
   - FA2024 #6: causal; $\{\underset{\uparrow}{1},\tfrac13,0,\dots\}\mapsto\{\underset{\uparrow}{1},\tfrac12,0,\dots\}$. $H$, $h$, LCCDE.
   - SP2023 #6 (20 pts): causal and stable; $X=\dfrac{1}{(1-2z^{-1})(1-z^{-1})}$, $Y=\dfrac{1}{(1-\frac12z^{-1})(1-z^{-1})(1-\frac14z^{-1})}$.
   - [[exams/midterm-1/past-exams/spring-2021|SP2021 #7]] (21 pts): causal; $x=\tfrac14\left(-\tfrac13\right)^n u[n]-3\cdot4^n u[-n-1]$, $Y(z)=\dfrac{13/4}{(1-\frac12z^{-1})(1-z^{-1})(1+\frac13z^{-1})}$.
   - [[homework/hw4|HW4 #4]]: causal; $2^n(u[n]-3u[n-1])\mapsto(3^n-2^n)u[n]$. $h$, stable?
5. **Described by a formula: feed it $\delta$.** [[exams/midterm-1/past-exams/fall-2025|FA2025 #4(b)]]: $y[n]=\frac1L\sum_{k=0}^{L-1}x[n-Sk]$, $L=3$, $S=4$.

> [!success]- Answers
> | instance | answer |
> |---|---|
> | SP2025 #3 | $h_2=\delta[n+1]$; $h=\{1,\underset{\uparrow}{0},1\}$; not causal |
> | FA2024 #3 | $x*h_2=\{\underset{\uparrow}{2},-1,-1\}$, $h_1=2\delta[n+1]$; $h=\{4,\underset{\uparrow}{2}\}$; not causal |
> | FA2019 #3 | $h=\tfrac12\delta[n+1]+\delta[n]+\tfrac12\delta[n-1]$; step response $\tfrac12u[n+1]+u[n]+\tfrac12u[n-1]$; not causal |
> | SP2023 #4 | $x_1[n]-3x_2[n-1]=\delta[n]$: $h[n]=y_1[n]-3y_2[n-1]$ |
> | HW2 #4 | $x[n]-\tfrac13x[n-1]=\delta[n]$: $h[n]=\left(\tfrac15\right)^n u[n-1]-\tfrac13\left(\tfrac15\right)^{n-1}u[n-2]$ |
> | HW2 #3 | $y[n]=\big(x[n]-x[n-1]\big)*g[n]$ |
> | FA2023 #4 | $h=\delta[n]-\delta[n-2]$, choice (b) |
> | FA2024 #6 | $H=\dfrac{1+\frac12z^{-1}}{1+\frac13z^{-1}}$, $\lvert z\rvert>\tfrac13$; $h=\tfrac32\delta[n]-\tfrac12\left(-\tfrac13\right)^n u[n]$; $y[n]=-\tfrac13y[n-1]+x[n]+\tfrac12x[n-1]$ |
> | SP2023 #6 | $H=\dfrac{1-2z^{-1}}{(1-\frac12z^{-1})(1-\frac14z^{-1})}$, $\lvert z\rvert>\tfrac12$; $h=-6\left(\tfrac12\right)^n u[n]+7\left(\tfrac14\right)^n u[n]$; $y[n]=\tfrac34y[n-1]-\tfrac18y[n-2]+x[n]-2x[n-1]$ (key's LCCDE has a typo: [[0-toolkit/05-errata\|errata]]) |
> | SP2021 #7 | $X=\dfrac{13/4}{(1+\frac13z^{-1})(1-4z^{-1})}$ on $\tfrac13<\lvert z\rvert<4$; $H=\dfrac{1-4z^{-1}}{(1-\frac12z^{-1})(1-z^{-1})}$, $\lvert z\rvert>1$; $h=7\left(\tfrac12\right)^n u[n]-6u[n]$; not stable |
> | HW4 #4 | $H=\dfrac{z^{-1}}{(1-3z^{-1})(1-6z^{-1})}$, $\lvert z\rvert>6$; $h=\tfrac13\left(6^n-3^n\right)u[n]$; not stable |
> | FA2025 #4(b) | $h=\tfrac13\left(\delta[n]+\delta[n-4]+\delta[n-8]\right)$, FIR, stable |

## The recipe

> [!recipe] Pick the move from the data
> 1. **Known branch? Remove it.** Parallel: deconvolve $y-x*h_1$. Series: compare $x*h_2$ with $y$. Overall: parallel $h_1+h_2$, series $h_1*h_2$.
> 2. **Short sequences: deconvolve.** $h$ starts at (start of $y$) − (start of $x$), length $L_y-L_x+1$. Spot shifted copies of $x$, or peel: $h[\text{first}]=y[\text{first}]/x[\text{first}]$, subtract, repeat.
> 3. **Make a delta.** Find $\sum_i c_i\,x_i[n-k_i]=\delta[n]$; then $h[n]=\sum_i c_i\,y_i[n-k_i]$. For $a^nu[n]$: $x[n]-a\,x[n-1]=\delta[n]$.
> 4. **Step response:** $h[n]=g[n]-g[n-1]$.
> 5. **Divide:** $H=Y/X$, cancel, ROC from "causal"/"stable" (never from $X$ alone); long-divide if not proper; PFE; LCCDE by cross-multiplying.
> 6. **Check:** $x*h=y$, $\sum y=\sum x\sum h$; read causality and stability off $h$.

> [!trap] Where the points go
> - **Parallel vs series:** $h_1+h_2$ vs $h_1*h_2$; subtract the known branch before deconvolving.
> - **Start index of $h$:** FA2024 #3's $h=\{4,\underset{\uparrow}{2}\}$ starts at $n=-1$: not causal.
> - **Step trick:** $g[n]-g[n-1]$, not $g[n+1]-g[n]$.
> - **ROC of $H$** comes from the statement; $\text{ROC}_Y\supseteq\text{ROC}_X\cap\text{ROC}_H$ is only a check (SP2021 #7: the pole of $X$ at 4 cancels).
> - **Cancelling and dividing.** SP2023 #6: $1-z^{-1}$ cancels; the zero $1-2z^{-1}$ comes from $X$'s denominator. FA2024 #6: equal degrees, so $h$ has a $\delta[n]$ term.

## Practice problems

> [!question] Practice 1 — parallel connection with one known branch
> Parallel, $h_1[n]=2\delta[n-2]$. $x=\{\underset{\uparrow}{1},-1,2\}$ gives $y=\{1,\underset{\uparrow}{0},1,4,-2,4\}$. Find $h_2$ and $h$. Causal?

> [!success]- Solution
> $x*h_1=\{2,-2,4\}$ at $n=2,3,4$:
> $$
> y-x*h_1=\{1,\underset{\uparrow}{0},1,2\}.
> $$
> $h_2$ starts at $-1$, length 2: $h_2[-1]=1$, $h_2[0]=1$. Check $\{1,-1,2\}*\{1,1\}=\{1,0,1,2\}$ ✓.
> $$
> h_2[n]=\delta[n+1]+\delta[n],\qquad h[n]=\{1,\underset{\uparrow}{1},0,2\}.
> $$
> Not causal: $h[-1]=1$.

> [!question] Practice 2 — two ways to get δ
> (a) $x_1=\{\underset{\uparrow}{1},2,-2,6\}\mapsto y_1=\{\underset{\uparrow}{2},3,-5,16,-8,6\}$, $x_2=\{\underset{\uparrow}{1},-1,3\}\mapsto y_2=\{\underset{\uparrow}{2},-3,8,-4,3\}$. Find $h$.
> (b) Step response $g[n]=\delta[n+1]+3u[n]-2u[n-2]$. Find $h$. Causal? Stable?

> [!success]- Solution
> **(a)** $x_1[n]-2x_2[n-1]=\delta[n]$, so
> $$
> h[n]=y_1[n]-2y_2[n-1]=\{\underset{\uparrow}{2},-1,1\}.
> $$
> **(b)**
> $$
> h[n]=g[n]-g[n-1]=\delta[n+1]+2\delta[n]-2\delta[n-2]=\{1,\underset{\uparrow}{2},0,-2\}.
> $$
> Not causal; stable (FIR).

> [!question] Practice 3 — H = Y/X
> Causal LTI: $x[n]=\left(\tfrac12\right)^n u[n]\mapsto y[n]=\left[10\left(\tfrac13\right)^n-9\left(\tfrac12\right)^n\right]u[n]$. $H(z)$ and ROC, $h[n]$, LCCDE, stable?

> [!success]- Solution
> $$
> \begin{gathered}
> Y(z)=\frac{1-2z^{-1}}{\left(1-\frac13z^{-1}\right)\left(1-\frac12z^{-1}\right)},\\
> H(z)=\frac{1-2z^{-1}}{1-\frac13z^{-1}}=6-\frac{5}{1-\frac13z^{-1}},\quad\lvert z\rvert>\tfrac13.
> \end{gathered}
> $$
> $$
> h[n]=6\,\delta[n]-5\left(\tfrac13\right)^n u[n]=\delta[n]-5\left(\tfrac13\right)^n u[n-1].
> $$
> LCCDE: $y[n]-\tfrac13y[n-1]=x[n]-2x[n-1]$. Stable: pole $\tfrac13$, causal.

## Related

[[problems/finite-length-convolution|Finite-length convolution]] · [[problems/lccde-to-transfer-function-and-response|LCCDE ⇄ H(z)]] · [[problems/all-possible-rocs|all possible ROCs]] · [[concepts/step-response|step response]] · [[concepts/system-algebra|system algebra]] · [[2-z-transform/10-improper-transfer-functions-and-system-algebra|Lecture 10]]

### Sources for this page

Lectures 4, 9, 10 notes and slides; HW2 #3–4, HW4 #4 with solutions; past Midterm 1 exams FA2019–FA2025 with keys; Midterm 1 review slides.
