---
title: "Infinite-length convolution"
description: "Convolutions where a sequence never ends: the convolution sum with step-derived limits and a geometric sum, the finite-times-infinite shortcut, divergence, and Y = XH as a check."
tags: [problem-family, problem, convolution, z-transform, midterm-1]
family_frequency: "5 of 7 exams"
typical_points: "5–8"
lectures: [4, 7]
---

*Problem family · part (b) of the convolution problem on the five most recent exams · 5–8 points · [[1-signals-and-systems/04-impulse-response-and-convolution|Lecture 4]], [[2-z-transform/07-z-transform-properties|Lecture 7]] · [[0-toolkit/02-geometric-series|geometric series]]*

## What it looks like on the exam

Two kinds; recognizing which is half the problem.

**Exponential * exponential** (sum + geometric series):
- [[exams/midterm-1/past-exams/spring-2025|SP2025 #4b]]: $\left(-\tfrac13\right)^n u[n]*\left(\tfrac12\right)^n u[n-3]$.
- [[exams/midterm-1/past-exams/spring-2023|SP2023 #3b]]: $\left(-\tfrac12\right)^n u[n]*\left(\tfrac23\right)^n u[n-1]$.
- [[homework/hw2|HW2 #5(d)]]: $(-1)^n u[n] * e^{-n}u[n]$; #5(e): $0.5^n u[n] * 2^{-n}u[-n]$, which does not exist.
- Lecture 4: $u[n]*\left(-\tfrac34\right)^n u[n]$.

**Finite * infinite** (finite one as deltas → shifted copies):
- [[exams/midterm-1/past-exams/fall-2025|FA2025 #3b]]: $x=n\,u[n+1]\,u[-n+1]$, $h=n\left(\tfrac13\right)^n\cos(n)$.
- [[exams/midterm-1/past-exams/fall-2024|FA2024 #4b]]: $x=e^{-n}u[n]$, $h=(n+1)(u[n]-u[n-3])$.
- [[exams/midterm-1/past-exams/fall-2023|FA2023 #3b]]: $x=\left(\tfrac34\right)^n u[n]$, $h=2u[n]-u[n-1]-u[n-2]$.
- SP2023 #3c: $x=\log(\lvert n\rvert+1)$, $h=u[n+1]-u[n-2]$.
- HW2 #5(b): $3^{-n}u[n]*\{\underset{\uparrow}{0},1,2\}$; #5(c): $u[n]*n(u[n]-u[n-4])$; Lecture 4: $\{\underset{\uparrow}{1},0,2,0,-3\}$ against a sinusoidal $h$.

> [!success]- Answers
> | instance | $y[n]$ |
> |---|---|
> | SP2025 #4b | $\tfrac1{20}\left(-\tfrac13\right)^{n-3}u[n-3]+\tfrac{3}{40}\left(\tfrac12\right)^{n-3}u[n-3]$ |
> | SP2023 #3b | $\tfrac47\left[\left(\tfrac23\right)^n-\left(-\tfrac12\right)^n\right]u[n-1]$ |
> | FA2025 #3b | $x=\{-1,\underset{\uparrow}{0},1\}$: $y[n]=-h[n+1]+h[n-1]$ |
> | FA2024 #4b | $h=\{\underset{\uparrow}{1},2,3\}$: $e^{-n}u[n]+2e^{-(n-1)}u[n-1]+3e^{-(n-2)}u[n-2]$ |
> | FA2023 #3b | $h=2\delta[n]+\delta[n-1]$: $2\left(\tfrac34\right)^n u[n]+\left(\tfrac34\right)^{n-1}u[n-1]$ |
> | SP2023 #3c | $h=\{1,\underset{\uparrow}{1},1\}$: $\log(\lvert n+1\rvert+1)+\log(\lvert n\rvert+1)+\log(\lvert n-1\rvert+1)$ |
> | HW2 #5(b) | $3^{-(n-1)}u[n-1]+2\cdot3^{-(n-2)}u[n-2]$ |
> | HW2 #5(c) | $u[n-1]+2u[n-2]+3u[n-3]$ |
> | HW2 #5(d) | $\dfrac{e^{-n}+(-1)^n e}{1+e}\,u[n]$ |
> | HW2 #5(e) | diverges: every term equals $0.5^n$, infinitely many |
> | Lecture 4 | $\tfrac47\left[1-\left(-\tfrac34\right)^{n+1}\right]u[n]$ |

## The recipe

> [!recipe] Infinite-length convolution
> 1. **Finite in disguise?** Tabulate: $2u[n]-u[n-1]-u[n-2]=2\delta[n]+\delta[n-1]$; $(n+1)(u[n]-u[n-3])=\{\underset{\uparrow}{1},2,3\}$. Then $y[n]=\sum_k c_k\,h[n-k]$, each copy shifted everywhere, step included.
> 2. **Otherwise write the sum with the steps:** $y[n]=\sum_k x[k]\,h[n-k]$; $u[k-a]$ → $k\ge a$, $u[n-k-b]$ → $k\le n-b$.
> 3. **Where $y$ lives:** lower $\le$ upper gives the answer's step factor (e.g. $n\ge1$ → $u[n-1]$).
> 4. **Geometric sum:**
> $$
> \sum_{k=K_1}^{K_2} r^k=\frac{r^{K_1}-r^{K_2+1}}{1-r}\quad(r\neq1).
> $$
> Shortcuts (pull a shift out with its constant, $\left(\tfrac12\right)^n u[n-3] = \tfrac18\left(\tfrac12\right)^{n-3}u[n-3]$):
> $$
> \begin{gathered}
> a^n u[n] * b^n u[n] = \frac{a^{n+1}-b^{n+1}}{a-b}\,u[n]\ \ (a\neq b),\\
> a^n u[n]*a^n u[n] = (n+1)\,a^n u[n].
> \end{gathered}
> $$
> 5. **Exists?** Infinitely many terms must shrink; in $z$: $\text{ROC}_x\cap\text{ROC}_h$ non-empty (HW2 #5(e): $\lvert z\rvert>0.5$ vs $\lvert z\rvert<0.5$).
> 6. **Check:** first sample $=x[\text{first}]h[\text{first}]$; $Y=XH$ with cover-up gives the constants.

> [!trap] Where the points go
> - **Dropping the step factor:** without $u[n-1]$ the output starts before the input arrives.
> - **Limits from habit:** $\sum_{k=0}^{n}$ only if both start at 0.
> - **Off-by-one:** $\sum_{k=0}^{n}r^k=\frac{1-r^{n+1}}{1-r}$, $n+1$ terms.
> - **Half-shifted copy or lost constant:** $h[n-2]$ shifts exponent and step; $\left(\tfrac12\right)^n u[n-3]\ne\left(\tfrac12\right)^{n-3}u[n-3]$.
> - **$a=b$:** the identity divides by zero; use $(n+1)a^n u[n]$.

## Practice problems

> [!question] Practice 1 — both steps shifted
> $x[n]=\left(\tfrac13\right)^n u[n+1]$, $h[n]=\left(\tfrac12\right)^n u[n-1]$. Find $y=x*h$; confirm in $z$.

> [!success]- Solution
> $-1\le k\le n-1$, non-empty iff $n\ge0$; $y[0]=x[-1]h[1]=\tfrac32$. With $r=\tfrac23$:
> $$
> y[n]=\left(\tfrac12\right)^n\sum_{k=-1}^{n-1}\left(\tfrac23\right)^k=\left(\tfrac12\right)^n\left[\tfrac92-3\left(\tfrac23\right)^n\right],\qquad\boxed{\,y[n]=\left[\tfrac92\left(\tfrac12\right)^n-3\left(\tfrac13\right)^n\right]u[n]\,}
> $$
> $$
> Y(z)=\frac{3/2}{\left(1-\frac13z^{-1}\right)\left(1-\frac12z^{-1}\right)},\quad A_{1/2}=\tfrac92,\quad A_{1/3}=-3\ \checkmark
> $$

> [!question] Practice 2 — a finite sequence in disguise
> $x[n]=2u[n]-3u[n-1]+u[n-2]$, $h[n]=n\left(\tfrac12\right)^n u[n]$. Simplest form of $y$?

> [!success]- Solution
> $x=2\delta[n]-\delta[n-1]$:
> $$
> y[n]=2n\left(\tfrac12\right)^n u[n]-(n-1)\left(\tfrac12\right)^{n-1}u[n-1]=\left(\tfrac12\right)^{n-1}u[n-1].
> $$

> [!question] Practice 3 — mixed sides
> (a) $2^n u[-n-1] * \left(\tfrac13\right)^n u[n]$. (b) Does $u[n]*\left(\tfrac12\right)^n u[-n]$ exist?

> [!success]- Solution
> **(a)** $y[n]=\left(\tfrac13\right)^n\sum_{k\le\min(n,-1)}6^k$: $n\le-1$ gives $\tfrac65\,2^n$; $n\ge0$ gives $\tfrac15\left(\tfrac13\right)^n$.
> $$
> y[n]=\tfrac65\,2^n u[-n-1]+\tfrac15\left(\tfrac13\right)^n u[n]
> $$
> **(b)** No: $y[n]=\sum_{k\ge\max(0,n)}2^{k-n}$ grows without bound; $\lvert z\rvert>1$ and $\lvert z\rvert<\tfrac12$ do not overlap.

## Related

[[problems/finite-length-convolution|Finite-length convolution]] · [[concepts/convolution|convolution]] · [[concepts/sided-sequences|sided sequences]] · [[2-z-transform/08-inverse-z-transform|Lecture 8]] · [[demos/convolution-explorer|convolution explorer]]

### Sources for this page

Lectures 4 and 7 notes and slides; HW2 #5(b)–(e) with solutions; past Midterm 1 exams FA2023–FA2025 with keys; Midterm 1 review slides.
