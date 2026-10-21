---
title: "Finite-length convolution"
description: "Convolve two short sequences with n = 0 marked: predict start, end and length, compute by shifted copies, table or matrix, then run the sum and alternating-sum checks. On every past Midterm 1."
tags: [problem-family, problem, convolution, midterm-1]
family_frequency: "7 of 7 exams"
typical_points: "5–10"
lectures: [4]
---

*Problem family · all seven past exams, usually part (a) of the convolution problem · 5–10 points · [[1-signals-and-systems/04-impulse-response-and-convolution|Lecture 4]] · [[demos/convolution-explorer|convolution explorer]]*

## What it looks like on the exam

Two short integer lists with an arrow under $n=0$, rarely on the first sample, often an interior zero. Compute $y=x*h$ and mark $n=0$. Part (b) is usually [[problems/infinite-length-convolution|infinite-length convolution]].

| instance | $x[n]$ | $h[n]$ |
|---|---|---|
| [[exams/midterm-1/past-exams/fall-2025\|FA2025 #3a]] | $\{\underset{\uparrow}{1},2,3,0,-1,-2,-3\}$ | $\{1,0,\underset{\uparrow}{1}\}$ |
| [[exams/midterm-1/past-exams/spring-2025\|SP2025 #4a]] | $\{1,-2,\underset{\uparrow}{0},3,-1,1\}$ | $\{\underset{\uparrow}{2},-1,3\}$ |
| [[exams/midterm-1/past-exams/fall-2024\|FA2024 #4a]] | $\{1,-3,\underset{\uparrow}{2},-1,4\}$ | $\{2,\underset{\uparrow}{0},-1\}$ |
| [[exams/midterm-1/past-exams/fall-2023\|FA2023 #3a]] | $\{\underset{\uparrow}{1},2,3,2,1\}$ | $\{\underset{\uparrow}{-1},1\}$ |
| [[exams/midterm-1/past-exams/spring-2023\|SP2023 #3a]] | $\{\underset{\uparrow}{1},-2,2\}$ | $\{3,1,\underset{\uparrow}{0},3,1,1\}$ |
| [[exams/midterm-1/past-exams/spring-2021\|SP2021 #2]] | $\{\underset{\uparrow}{-1},-2,3,-3,2,1\}$ | $\{-1,\underset{\uparrow}{0},1\}$ |
| [[exams/midterm-1/past-exams/fall-2019\|FA2019 #4]] | $\{\underset{\uparrow}{1},-4,2,-1,3,1\}$ | $\{\underset{\uparrow}{-1},1,-1\}$ |
| [[homework/hw2\|HW2 #5(a)]] | $\{-1,\underset{\uparrow}{0},1\}$ | $\{\underset{\uparrow}{1},2,3,4,5\}$ |
| Lecture 4 | $\{\underset{\uparrow}{3},1,0,3,1,1\}$ | $\{2,\underset{\uparrow}{-1},1\}$ |

> [!success]- Answers
> | instance | $y[n]$ | first index |
> |---|---|---|
> | FA2025 #3a | $\{1,2,\underset{\uparrow}{4},2,2,-2,-4,-2,-3\}$ | $-2$ |
> | SP2025 #4a | $\{2,-5,\underset{\uparrow}{5},0,-5,12,-4,3\}$ | $-2$ |
> | FA2024 #4a | $\{2,-6,3,\underset{\uparrow}{1},6,1,-4\}$ | $-3$ |
> | FA2023 #3a | $\{\underset{\uparrow}{-1},-1,-1,1,1,1\}$ | $0$ |
> | SP2023 #3a | $\{3,-5,\underset{\uparrow}{4},5,-5,5,0,2\}$ | $-2$ |
> | SP2021 #2 | $\{1,\underset{\uparrow}{2},-4,1,1,-4,2,1\}$ | $-1$ |
> | FA2019 #4 | $\{\underset{\uparrow}{-1},5,-7,7,-6,3,-2,-1\}$ | $0$ |
> | HW2 #5(a) | $\{-1,\underset{\uparrow}{-2},-2,-2,-2,4,5\}$ | $-1$ |
> | Lecture 4 | $\{6,\underset{\uparrow}{-1},2,7,-1,4,0,1\}$ | $-1$ |
>
> The SP2025 key boxes $\{2,-5,6,0,-5,10,-4,3\}$; its own matrix product gives the row above, and the box fails the sum check ($7\neq 2\cdot4$). See [[0-toolkit/05-errata|errata]].

## The recipe

> [!recipe] Finite-length convolution
> 1. **Index both:** $x$ starts at $n_x$, $N$ samples; $h$ at $n_h$, $M$ samples. Interior zeros count.
> 2. **Predict the frame:**
> $$
> \begin{gathered}
> \text{start} = n_x+n_h,\qquad\text{end} = (n_x+N-1)+(n_h+M-1),\\
> \text{length} = N+M-1;
> \end{gathered}
> $$
> $y[\text{start}]=x[n_x]\,h[n_h]$, $y[\text{end}]$ = (last of $x$)(last of $h$).
> 3. **Compute.** Shifted copies: $y[n]=\sum_k h[k]\,x[n-k]$, one row per nonzero $h[k]$ (fastest; $h=\{1,\underset{\uparrow}{2},-1\}$ gives $x[n+1]+2x[n]-x[n-1]$). Table: flip $h$, slide, multiply, add. Matrix: Toeplitz columns of shifted copies; row 1 is the start index.
> 4. **Place the arrow** from the start index.
> 5. **Check:**
> $$
> \begin{gathered}
> \sum_n y[n] = \Big(\sum_n x[n]\Big)\Big(\sum_n h[n]\Big),\\
> \sum_n (-1)^n y[n] = \Big(\sum_n (-1)^n x[n]\Big)\Big(\sum_n (-1)^n h[n]\Big).
> \end{gathered}
> $$
> The second also catches an arrow off by an odd shift.

> [!trap] Where the points go
> - **The arrow.** Derive the start index $n_x+n_h$; FA2019 #4 starts at $n=0$, SP2021 #2 at $n=-1$.
> - **Forgetting to flip** in the table: $h[k-n]$ computes a correlation; visible with $\{2,\underset{\uparrow}{0},-1\}$.
> - **Dropped zeros.** $\{1,0,\underset{\uparrow}{1}\}$ is $\delta[n+2]+\delta[n]$.
> - **Sign slips:** the sum check catches almost all.
> - **Equation → $h$:** $y[n]=x[n+1]-2x[n]+3x[n-2]$ has $h=\{1,\underset{\uparrow}{-2},0,3\}$.

## Practice problems

> [!question] Practice 1 — shifted copies and one table row
> $x[n]=\{2,-1,\underset{\uparrow}{0},3,1\}$, $h[n]=\{1,\underset{\uparrow}{2},-1\}$. Compute $y$ and mark $n=0$; recompute $y[0]$ with one table row.

> [!success]- Solution
> Frame $-3$ to $3$; $y[n]=x[n+1]+2x[n]-x[n-1]$:
>
> | $n$ | $-3$ | $-2$ | $-1$ | $0$ | $1$ | $2$ | $3$ |
> |---|---|---|---|---|---|---|---|
> | $x[n+1]$ | 2 | $-1$ | 0 | 3 | 1 | | |
> | $2x[n]$ | | 4 | $-2$ | 0 | 6 | 2 | |
> | $-x[n-1]$ | | | $-2$ | 1 | 0 | $-3$ | $-1$ |
> | $y[n]$ | **2** | **3** | **$-4$** | **4** | **7** | **$-1$** | **$-1$** |
>
> $y[0]=x[-1]h[1]+x[0]h[0]+x[1]h[-1] = (-1)(-1)+0\cdot2+3\cdot1 = 4$ ✓. Checks: $\sum y = 10 = 5\cdot2$; alternating $2 = (1)(2)$.

> [!question] Practice 2 — a system given by its equation
> $y[n]=x[n+1]-2x[n]+3x[n-2]$. Find $h$, then the output for $x=\{\underset{\uparrow}{1},3,-1,2\}$ by the matrix layout.

> [!success]- Solution
> $h=\{1,\underset{\uparrow}{-2},0,3\}$. $y$ starts at $-1$, 7 samples:
> $$
> \begin{bmatrix} 1&0&0&0\\ -2&1&0&0\\ 0&-2&1&0\\ 3&0&-2&1\\ 0&3&0&-2\\ 0&0&3&0\\ 0&0&0&3 \end{bmatrix}
> \begin{bmatrix} 1\\3\\-1\\2 \end{bmatrix}
> = \begin{bmatrix} 1\\1\\-7\\7\\5\\-3\\6 \end{bmatrix},\qquad y[n]=\{1,\ \underset{\uparrow}{1},\ -7,\ 7,\ 5,\ -3,\ 6\}.
> $$

> [!question] Practice 3 — grade two classmates
> $x=\{2,\underset{\uparrow}{1},-1,3\}$, $h=\{1,-1,\underset{\uparrow}{2}\}$. A answers $\{2,-1,4,\underset{\uparrow}{6},-5,6\}$; B answers $\{2,-1,\underset{\uparrow}{2},6,-5,6\}$. Correct $y$? Which check exposes each?

> [!success]- Solution
> $$
> y[n]=\{2,\ -1,\ 2,\ \underset{\uparrow}{6},\ -5,\ 6\}\qquad(\text{starts at } -3).
> $$
> A fails the sum check ($12\ne5\cdot2$). B starts at $-2$, not $n_x+n_h=-3$; its alternating sum is $-12$, not $3\cdot4=12$.

## Related

[[concepts/convolution|Convolution]] · [[concepts/impulse-response|impulse response]] · [[problems/infinite-length-convolution|infinite-length convolution]] · [[problems/finding-h-from-input-output-pairs|finding h]] · [[demos/practice-drills|practice drills]]

### Sources for this page

Lecture 4 notes and slides; HW2 #5(a) with solution; past Midterm 1 exams FA2019–FA2025 with keys; Midterm 1 review slides.
