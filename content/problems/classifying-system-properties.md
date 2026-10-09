---
title: "Classifying system properties (the L / TI / C / S table)"
description: "The yes/no table of Linear, Time-invariant, Causal, Stable that opens every Midterm 1: fast rules that fill a cell in seconds, the four proof templates behind them, a counterexample library, and three new practice problems."
tags: [problem-family, problem, systems, stability, midterm-1]
family_frequency: "7 of 7 exams"
typical_points: "12"
lectures: [3, 4]
---

*Problem family · problem #2 on six of the seven past exams (#3 on SP2021) · 12 points, one per cell · uses [[1-signals-and-systems/03-system-properties|Lecture 3]] and [[1-signals-and-systems/04-impulse-response-and-convolution|Lecture 4]] · concepts: [[concepts/linearity]], [[concepts/time-invariance]], [[concepts/causality]], [[concepts/bibo-stability]], [[concepts/lti-system]]*

## What it looks like on the exam

Three systems, four columns (**Linear**, **Time-invariant** — older exams say *shift-invariant*, "LSI" = LTI — **Causal**, **Stable** in the BIBO sense), "yes" or "no" in each cell, **no proofs asked**. Twelve cells for 12 points: the best points-per-minute on the exam if the fast rules below are automatic. Grading has varied: SP2025 states "points will not be deducted for incorrect answers", while FA2019 #2 used +2 / −1 / 0, so there a blank beat a coin flip. The proof versions of the same questions are homework (HW1 #5–6, HW2 #1–2), and the same judgments reappear in the True/False problem.

Every instance:

- [[exams/midterm-1/past-exams/fall-2025|FA2025 #2]]: $\lvert n\rvert\,x[n]$; $\ \lvert x[n]-x[n-1]\rvert$; $\ x[n]*2^n u[-n]$. Plus [[exams/midterm-1/past-exams/fall-2025|FA2025 #4(a)]]: is the modified moving average $y[n]=\frac1L\sum_{k=0}^{L-1}x[n-Sk]$ linear? time-invariant?
- [[exams/midterm-1/past-exams/spring-2025|SP2025 #2]]: $x[n]*j^n u[n]$; $\ 2x[\lvert n\rvert]+10$; $\ e^{x[n]+1}$.
- [[exams/midterm-1/past-exams/fall-2024|FA2024 #2]]: $x[n]\,x[n+1]$; $\ \dfrac{x[n]}{\lvert n\rvert+1}$; $\ \sin(x[n])+x[0]$.
- [[exams/midterm-1/past-exams/fall-2023|FA2023 #2]]: $\log(\lvert n\rvert+1)\,x[n]$; $\ x[n]*u[n+1]$; $\ x[n]+3$.
- [[exams/midterm-1/past-exams/spring-2023|SP2023 #2]] (the instructor's worked example in the Midterm 1 review): $x[n]*(-1)^n u[n]$; $\ \dfrac{x[n]}{x[2]}$; $\ \cos^2\!\left(\tfrac{\pi}{2}n\right)x[n]$.
- [[exams/midterm-1/past-exams/spring-2021|SP2021 #3]] (24 pts): $x[n]\cos\!\left(\tfrac{\pi(n-2)}{3}\right)$; $\ x[3]\,x[n]$; $\ (0.8+0.8j)^n x[n]$.
- [[exams/midterm-1/past-exams/fall-2019|FA2019 #2]] (L / SI / C only): $x[\lvert n\rvert+n]$; $\ (0.2)^{\lvert n\rvert}\log x[n]$.
- Homework: [[homework/hw1|HW1 #5]] (clipping), [[homework/hw1|HW1 #6]] (windowing), [[homework/hw2|HW2 #1]] (two recursions and $(\tfrac12)^{\lvert n\rvert}x[n]$), [[homework/hw2|HW2 #2]] (convolution ⇒ LTI).
- Lecture: [[1-signals-and-systems/03-system-properties|Lecture 3]] exercises 1–7 ($x[n]-x[n-1]$, $x^p[n]$, $x[\lvert n\rvert]$, $n\,x[3n]$, $x[n]+x[n-2]-x[n-4]$, $x^{10}[n]+e^{x[n]}$).

> [!success]- Answers to every past-exam table (L / TI / C / S), with the deciding reason
> | exam | system | L | TI | C | S | deciding reason |
> |---|---|---|---|---|---|---|
> | FA25 | $\lvert n\rvert x[n]$ | Y | N | Y | N | gain depends on $n$ and grows: $x=1$ gives $\lvert n\rvert$ |
> | FA25 | $\lvert x[n]-x[n-1]\rvert$ | N | Y | Y | Y | $\lvert\cdot\rvert$ kills homogeneity for negative scalars; $\le 2B$ |
> | FA25 | $x*2^n u[-n]$ | Y | Y | N | Y | $h[-1]=\tfrac12\neq0$; $\sum\lvert h\rvert = 2$ |
> | SP25 | $x*j^n u[n]$ | Y | Y | Y | N | $\lvert h[n]\rvert=1$ for all $n\ge0$: not summable |
> | SP25 | $2x[\lvert n\rvert]+10$ | N | N | N | Y | $+10$; index warp; $y[-3]$ needs $x[3]$ |
> | SP25 | $e^{x[n]+1}$ | N | Y | Y | Y | $\le e^{B+1}$ |
> | FA24 | $x[n]x[n+1]$ | N | Y | N | Y | product of inputs; uses $x[n+1]$ |
> | FA24 | $x[n]/(\lvert n\rvert+1)$ | Y | N | Y | Y | gain depends on $n$ but $\le 1$ |
> | FA24 | $\sin(x[n])+x[0]$ | N | N | N | Y | $\sin$; fixed sample $x[0]$ (future for $n<0$) |
> | FA23 | $\log(\lvert n\rvert+1)x[n]$ | Y | N | Y | N | gain grows without bound |
> | FA23 | $x*u[n+1]$ | Y | Y | N | N | $h[-1]=1$; $\sum\lvert h\rvert=\infty$ |
> | FA23 | $x[n]+3$ | N | Y | Y | Y | $T\{0\}=3\neq0$ |
> | SP23 | $x*(-1)^n u[n]$ | Y | Y | Y | N | $\lvert h\rvert = 1$ forever |
> | SP23 | $x[n]/x[2]$ | N | N | N | N | $T\{2x\}=T\{x\}$; uses $x[2]$; $x[2]\to0$ blows up |
> | SP23 | $\cos^2(\tfrac{\pi}{2}n)x[n]$ | Y | N | Y | Y | gain $1,0,1,0,\dots$ depends on $n$ |
> | SP21 | $x[n]\cos(\tfrac{\pi(n-2)}{3})$ | Y | N | Y | Y | same pattern |
> | SP21 | $x[3]x[n]$ | N | N | N | Y | product of inputs; fixed future sample |
> | SP21 | $(0.8+0.8j)^n x[n]$ | Y | N | Y | N | $\lvert 0.8+0.8j\rvert=0.8\sqrt2\approx1.13>1$ |
> | FA19 | $x[\lvert n\rvert+n]$ | Y | N | N | (Y) | $y[n]=x[2n]$ for $n>0$; S not asked |
> | FA19 | $(0.2)^{\lvert n\rvert}\log x[n]$ | N | N | Y | (N) | $\log$; gain depends on $n$; S not asked |
>
> FA2025 #4(a): linear and time-invariant — the moving average is a sum of scaled, shifted copies of $x$, i.e. a convolution with an FIR $h$ (so also causal and stable).
>
> Every row is checked numerically (superposition with random complex inputs, shifted inputs, perturbing future samples, a bounded input that blows up) in `verify/exams/property_bank.py` and `verify/problems/classifying.py`. The full bank with the homework and lecture systems, and a one-line reason per cell, is the [[exams/midterm-1/system-property-bank|system-property bank]].

## The fast rules

Read the formula once, look for the features below, and you can fill most cells without writing anything.

| feature in $y[n]=T\{x\}[n]$ | L | TI | C | S |
|---|---|---|---|---|
| $y = x*h$ (a convolution) | Y | Y | Y iff $h[n]=0$ for $n<0$ | Y iff $\sum_n \lvert h[n]\rvert<\infty$ |
| additive constant ($x[n]+3$, $2x[\lvert n\rvert]+10$) | **N** | — | — | — |
| nonlinear function of the input ($x^2$, $\lvert x\rvert$, $e^x$, $\sin x$, $\log x$, $x[n]x[n+1]$, $x[n]/x[2]$) | **N** | — | — | — |
| gain that depends on $n$ ($g[n]\,x[n]$, $g$ not constant) | Y | **N** | Y | Y iff $g$ bounded |
| index other than $n-n_0$ ($x[-n]$, $x[2n]$, $x[\lvert n\rvert]$, $x[n^2]$) | Y | **N** | usually **N** | Y |
| fixed sample ($x[0]$, $x[2]$, $x[3]$) | usually N | **N** | **N** | — |
| uses $x[n+1]$, $x[n+k]$ with $k>0$, or a sum up to $+\infty$ | — | — | **N** | — |
| memoryless continuous function of $x$ ($e^x$, $\sin x$, $x^{10}$, $\lvert x\rvert$): bounded on $\lvert x\rvert\le B$ | N | Y | Y | Y |
| $\log x[n]$ | N | — | — | **N** ($x\to0^+$) |
| running sum $\sum_{k\le n}x[k]$ (accumulator) | Y | Y | Y | **N** ($u[n]\mapsto(n+1)u[n]$) |

A dash means "decide from the other features". Two combinations cause most mistakes: $g[n]x[n]$ with a *bounded* gain such as $\cos^2(\tfrac{\pi}{2}n)$ or $1/(\lvert n\rvert+1)$ is time-*varying* but stable; and a convolution system is *always* L and TI, whatever its $h$ looks like — only its causality and stability depend on $h$.

> [!recipe] Fill one row of the table
> 1. **Is it a convolution with a known $h$?** Then L = Y, TI = Y; C: is $h[n]=0$ for every $n<0$? S: is $\sum\lvert h[n]\rvert$ finite (geometric with ratio $<1$, or finitely many terms)? Done.
> 2. **Linear:** set $x=0$. If $y\neq0$ → N. Is every term exactly "(something not involving $x$) × one sample of $x$"? → Y. Any product of samples, power, $\lvert\cdot\rvert$, $e^{(\cdot)}$, $\sin$, $\log$, division by a sample → N.
> 3. **Time-invariant:** is every sample of $x$ read as $x[n-k]$ with a constant $k$, and does $n$ appear nowhere else? → Y. An $n$-dependent gain $g[n]$, a warped index ($x[2n]$, $x[\lvert n\rvert]$, $x[-n]$) or a fixed sample ($x[3]$) → N. If $n$ sits in the limits of a sum, substitute $m=n-k$ first: $\sum_{k=n-2}^{\infty}(\tfrac13)^{k-n}x[k]=\sum_{m\le2}3^m x[n-m]$ is a convolution (Practice 3).
> 4. **Causal:** list every index $k$ at which $x$ is read. Need $k\le n$ **for every $n$, negative $n$ included**: $x[\lvert n\rvert]$ at $n=-3$ reads $x[3]$ (N); $x[0]$ at $n=-1$ is the future (N).
> 5. **Stable:** assume $\lvert x[n]\rvert\le B$. Can you bound $\lvert y[n]\rvert$ by a constant? Gains must be bounded over *all* $n$ (both $n\to+\infty$ and $n\to-\infty$); no division by input samples; no $\log$; no unbounded accumulation.
> 6. **Check** with the classic pairs: "$T\{0\}\ne0$ ⇒ not linear", "LTI ⇒ judge by $h$", "$n$ outside the brackets ⇒ time-varying".

## The four proof templates

The table needs no proof, but HW1/HW2 and occasional exam parts do ("justify", "prove"). Each property has one template; a single counterexample disproves.

**1. Linearity (superposition).** Let $y_1=T\{x_1\}$, $y_2=T\{x_2\}$, and feed $x_3=a x_1+b x_2$:

$$
y_3[n] = T\{a x_1+b x_2\}[n] \overset{?}{=} a\,y_1[n]+b\,y_2[n]\quad\text{for all } x_1,x_2,\ a,b\in\mathbb C .
$$

For $y[n]=g[n]\,x[n-k]$: $y_3[n]=g[n](a x_1[n-k]+b x_2[n-k]) = a y_1[n]+b y_2[n]$ ✓. To disprove, one pair suffices: $x$ and $2x$ ($x^2\mapsto 4x^2\neq 2x^2$), or $x=0$ ($x[n]+3\mapsto 3\neq0$), or $x$ and $-x$ for $\lvert\cdot\rvert$.

**2. Time invariance (shifted input vs shifted output).** Compute both and compare:

$$
\underbrace{T\{x[\,\cdot-n_0]\}[n]}_{\text{replace } x[\,\cdot\,]\text{ by }x[\,\cdot-n_0]\text{ only}}
\quad\text{vs}\quad
\underbrace{y[n-n_0]}_{\text{replace every } n \text{ by } n-n_0} .
$$

For $y[n]=x[2n]$: the first is $x[2n-n_0]$, the second is $x[2(n-n_0)]=x[2n-2n_0]$ — different, so time-varying. For an index map $y[n]=x[f(n)]$ the two agree only if $f(n)=n+c$. For a gain $g[n]x[n]$: $g[n]x[n-n_0]$ vs $g[n-n_0]x[n-n_0]$ — equal only if $g$ is constant.

> [!trap] The classic slip in template 2
> When you shift the input, the $n$'s *outside* $x$ do **not** change. Writing $T\{x[n-n_0]\} = g[n-n_0]\,x[n-n_0]$ "proves" every gain system time-invariant. The $n$ in $g[n]$ is the clock of the system, not part of the input.

**3. Causality (index test).** $y[n_0]$ may depend only on $x[k]$ with $k\le n_0$, for every $n_0$. Write out the indices read and test the worst $n$ (usually a negative one for $\lvert n\rvert$, $-n$, fixed samples; a positive one for $2n$). For an LTI system: causal $\iff h[n]=0$ for all $n<0$.

**4. BIBO stability (bound, or one blow-up).** To prove: assume $\lvert x[n]\rvert\le B_x$ for all $n$ and produce $B_y<\infty$ with $\lvert y[n]\rvert\le B_y$ for all $n$; for LTI systems this is $\lvert y[n]\rvert \le \sum_k\lvert h[k]\rvert\,\lvert x[n-k]\rvert \le B_x\sum_k\lvert h[k]\rvert$. To disprove: exhibit **one** bounded input and show the output is unbounded (not "might be"). For a convolution with $\sum\lvert h\rvert=\infty$ the input $x[n]=\overline{h[-n]}/\lvert h[-n]\rvert$ (just $\operatorname{sign} h[-n]$ for real $h$) gives $y[0]=\sum_k\lvert h[k]\rvert=\infty$.

## Counterexample library

| to show … | for systems like … | use |
|---|---|---|
| not linear | $x[n]+c$, $2x[\lvert n\rvert]+10$ | $x=0$ gives $y\neq0$ |
| not linear | $x^2$, $e^x$, $\sin x$, $x[n]x[n+1]$ | $x=\delta[n]$ vs $2\delta[n]$ |
| not linear | $\lvert x[n]-x[n-1]\rvert$ | $x$ vs $-x$ (same output, should flip sign) |
| not linear | $x[n]/x[2]$ | $T\{2x\}=T\{x\}\neq 2T\{x\}$ |
| time-varying | $g[n]x[n]$ | $x=\delta[n]$ gives $g[0]\delta[n]$; $x=\delta[n-n_0]$ gives $g[n_0]\delta[n-n_0]$, not $g[0]\delta[n-n_0]$ (pick $n_0$ with $g[n_0]\neq g[0]$) |
| time-varying | $x[2n]$, $x[-n]$, $x[\lvert n\rvert]$ | $x=\delta[n-1]$ and compare with the shifted output |
| non-causal | $x[\lvert n\rvert]$, $x[-n]$, fixed $x[0]$ | $n=-1$ reads $x[1]$ (or $x[0]$) |
| non-causal | $x*h$ | any $h[n_0]\neq0$ with $n_0<0$ |
| unstable | $\lvert n\rvert x[n]$, $\log(\lvert n\rvert+1)x[n]$, $r^n x[n]$ with $r>1$ | $x[n]=1$ for all $n$ |
| unstable | $(\tfrac12)^n x[\cdot]$ (gain grows as $n\to-\infty$) | $x=u[-n]$ |
| unstable | accumulator, $x*u[n+1]$ | $x=u[n]$: the output grows like $n$ |
| unstable | $x*j^n u[n]$, $x*(-1)^n u[n]$ | the matched input $x=h$: $j^n u[n]*j^n u[n]=(n+1)j^n u[n]$ |
| unstable | $\log x[n]$, $1/x[n]$ | $x[n]=\varepsilon\to0$ |

> [!trap] Where the points go
> - **"Linear" for $x[n]+3$.** An affine system passes a "looks linear" glance; $T\{0\}\neq0$ settles it.
> - **"Time-invariant" for $\cos^2(\tfrac{\pi}{2}n)\,x[n]$ or $x[n]/(\lvert n\rvert+1)$.** A periodic or decaying gain is still a gain that depends on $n$.
> - **Judging a convolution system's linearity from the look of $h$.** $x*j^n u[n]$ and $x*2^n u[-n]$ are LTI no matter how strange $h$ is.
> - **Judging stability from the look of $h$.** Look at the side where $h$ lives: $2^n u[-n]$ lives on $n\le0$, where it decays — summable ($\sum=2$), stable; $2^n u[n]$ lives on $n\ge0$, where it grows. $u[n+1]$, $j^n u[n]$ and $(-1)^n u[n]$ are bounded but never decay — not summable, unstable.
> - **Testing causality only for $n\ge0$.** $x[\lvert n\rvert]$ and $x[n]x[0]$ look causal at $n\ge0$ and fail at $n=-1$.
> - **Calling $(0.8+0.8j)^n x[n]$ stable** because $0.8<1$: the magnitude is $0.8\sqrt2\approx1.13$.
> - **Calling $\log(\lvert n\rvert+1)\,x[n]$ stable** because $\log$ grows slowly: slowly is still without bound.

## Practice problems

> [!question] Practice 1 — table (12 cells)
> Fill in Linear / Time-invariant / Causal / Stable for
> (a) $y[n]=x[n]*\left(\tfrac12\right)^n u[n+2]$ (b) $y[n]=x[n]+x[-n]$ (c) $y[n]=\displaystyle\sum_{k=-\infty}^{n}x[k]$ (d) $y[n]=\cos(x[n])\,x[n-1]$.

> [!success]- Solution
> | system | L | TI | C | S | reason |
> |---|---|---|---|---|---|
> | (a) $x*(\tfrac12)^n u[n+2]$ | Y | Y | N | Y | convolution; $h[-2]=4$, $h[-1]=2\neq0$; $\sum\lvert h\rvert=4+2+\sum_{n\ge0}(\tfrac12)^n=8$ |
> | (b) $x[n]+x[-n]$ | Y | N | N | Y | index $-n$; at $n=-1$ it reads $x[1]$; $\lvert y\rvert\le2B$ |
> | (c) accumulator | Y | Y | Y | N | $h=u[n]$; bounded $x=u[n]$ gives $y=(n+1)u[n]$ |
> | (d) $\cos(x[n])x[n-1]$ | N | Y | Y | Y | $x=u[n]$: $y[1]=\cos1\approx0.540$, $x=2u[n]$: $y[1]=2\cos2\approx-0.832\neq2\cos 1$; $\lvert y\rvert\le\lvert x[n-1]\rvert\le B$ |
>
> For (c), notice the accumulator *is* a convolution with $h[n]=u[n]$, so L and TI come for free and C, S follow from $h$.

> [!question] Practice 2 — prove each property or give a counterexample
> $y[n]=x[n]+\left(\tfrac12\right)^n x[n-1]$.

> [!success]- Solution
> **Linear — yes.** With $x_3=ax_1+bx_2$:
> $$
> y_3[n]=a x_1[n]+b x_2[n]+\left(\tfrac12\right)^n\big(a x_1[n-1]+b x_2[n-1]\big)=a\,y_1[n]+b\,y_2[n].
> $$
> **Time-invariant — no.** Input $\delta[n-1]$ gives $\delta[n-1]+\left(\tfrac12\right)^2\delta[n-2]=\delta[n-1]+\tfrac14\delta[n-2]$. Input $\delta[n-2]$ gives $\delta[n-2]+\tfrac18\delta[n-3]$, but the first output shifted by one is $\delta[n-2]+\tfrac14\delta[n-3]$. ($\tfrac18\neq\tfrac14$.)
>
> **Causal — yes.** $y[n]$ reads $x[n]$ and $x[n-1]$ only.
>
> **Stable — no.** The gain $(\tfrac12)^n=2^{-n}$ explodes as $n\to-\infty$. Take $x[n]=u[-n]$ ($\lvert x\rvert\le1$): for $n\le0$, $y[n]=1+2^{-n}$, e.g. $y[-10]=1+2^{10}=1025$, unbounded as $n\to-\infty$.

> [!question] Practice 3 — recognize a convolution
> $y[n]=\displaystyle\sum_{k=n-2}^{\infty}\left(\tfrac13\right)^{k-n}x[k]$. Find $h[n]$, then fill the four cells.

> [!success]- Solution
> Put $x=\delta$: only $k=0$ survives, and only if $0\ge n-2$, so
> $$
> h[n]=\left(\tfrac13\right)^{-n}u[2-n]=3^n u[2-n]=\{\dots,\tfrac19,\tfrac13,\underset{\uparrow}{1},3,9\}.
> $$
> The sum has the form $\sum_k x[k]\,h[n-k]$ with $h[m]=3^m u[2-m]$ (substitute $m=n-k$: $(\tfrac13)^{k-n}=3^{m}$ and $k\ge n-2 \iff m\le2$), so the system is a convolution: **L = Y, TI = Y**. **C = N**: $h[m]\neq0$ for every $m<0$ (e.g. $h[-1]=\tfrac13$) — equivalently, $y[n]$ reads $x[k]$ for all $k$ up to $+\infty$. (The nonzero $h[1]$, $h[2]$ are harmless: positive indices are the past.) **S = Y**: $\sum\lvert h\rvert = 9+3+1+\sum_{m\ge1}3^{-m}=13+\tfrac12=\tfrac{27}{2}$.

All three are checked in `verify/problems/classifying.py` (random-input tests for each property, the quoted counterexample values, $\sum\lvert h\rvert = 8$ and $27/2$).

## Related

- [[exams/midterm-1/system-property-bank|System-property bank]] — every system from the seven past tables, HW1–HW2 and Lecture 3, with the reason per cell; [[exams/midterm-1/true-false-bank|True/False bank]] for the statement versions.
- [[demos/practice-drills|Practice drills]] — randomized property questions, auto-graded.
- Lectures: [[1-signals-and-systems/03-system-properties|Lecture 3]] (definitions and proofs), [[1-signals-and-systems/04-impulse-response-and-convolution|Lecture 4]] (LTI ⇒ convolution; stability via $\sum\lvert h\rvert$), [[2-z-transform/11-bibo-stability-and-causality|Lecture 11]] (the same two properties read off $H(z)$ and its ROC).
- Concepts: [[concepts/linearity]], [[concepts/time-invariance]], [[concepts/causality]], [[concepts/bibo-stability]], [[concepts/lti-system]], [[concepts/impulse-response]].
- Next family: [[problems/finite-length-convolution|finite-length convolution]]; all families: [[problems/index|exam problem families]].

### Sources for this page

Lecture 3 notes (exercises 1–7) and slides; Lecture 4 notes §1 (LTI systems, BIBO condition); HW1 #5–6, HW2 #1–2 and solutions; property tables of FA2025 #2, SP2025 #2, FA2024 #2, FA2023 #2, SP2023 #2, SP2021 #3, FA2019 #2 and FA2025 #4(a) with their keys; Midterm 1 review slides (SP2023 #2). Verification: `verify/exams/property_bank.py` (every row passes), `verify/problems/classifying.py`.
