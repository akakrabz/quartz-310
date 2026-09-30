---
title: "Finite-length convolution"
description: "Convolve two short sequences with n = 0 marked: predict start, end and length, compute by table, matrix or sum of shifted copies, then run the two 10-second checks (sum and alternating sum). On every past Midterm 1."
tags: [problem-family, problem, convolution, midterm-1]
family_frequency: "7 of 7 exams"
typical_points: "5–10"
lectures: [4]
---

*Problem family · on all seven past exams, usually part (a) of the convolution problem · 5–10 points · uses [[1-signals-and-systems/04-impulse-response-and-convolution|Lecture 4]] · concepts: [[concepts/convolution]], [[concepts/kronecker-delta]], [[concepts/impulse-response]] · try it live: [[demos/convolution-explorer|convolution explorer]]*

## What it looks like on the exam

Two short sequences written as lists with an arrow under the $n=0$ sample; compute $y[n]=x[n]*h[n]$ and mark $n=0$ in the answer. The numbers are small integers, the arrows are rarely on the first sample, and one sequence often has a zero inside it. Part (b) of the same problem is almost always an infinite-length convolution — see [[problems/infinite-length-convolution|infinite-length convolution]].

| instance | $x[n]$ | $h[n]$ |
|---|---|---|
| [[0-midterm-1/past-exams/fall-2025\|FA2025 #3a]] | $\{\underset{\uparrow}{1},2,3,0,-1,-2,-3\}$ | $\{1,0,\underset{\uparrow}{1}\}$ |
| [[0-midterm-1/past-exams/spring-2025\|SP2025 #4a]] | $\{1,-2,\underset{\uparrow}{0},3,-1,1\}$ | $\{\underset{\uparrow}{2},-1,3\}$ |
| [[0-midterm-1/past-exams/fall-2024\|FA2024 #4a]] | $\{1,-3,\underset{\uparrow}{2},-1,4\}$ | $\{2,\underset{\uparrow}{0},-1\}$ |
| [[0-midterm-1/past-exams/fall-2023\|FA2023 #3a]] | $\{\underset{\uparrow}{1},2,3,2,1\}$ | $\{\underset{\uparrow}{-1},1\}$ |
| [[0-midterm-1/past-exams/spring-2023\|SP2023 #3a]] | $\{\underset{\uparrow}{1},-2,2\}$ | $\{3,1,\underset{\uparrow}{0},3,1,1\}$ |
| [[0-midterm-1/past-exams/spring-2021\|SP2021 #2]] | $\{\underset{\uparrow}{-1},-2,3,-3,2,1\}$ | $\{-1,\underset{\uparrow}{0},1\}$ |
| [[0-midterm-1/past-exams/fall-2019\|FA2019 #4]] | $\{\underset{\uparrow}{1},-4,2,-1,3,1\}$ | $\{\underset{\uparrow}{-1},1,-1\}$ |
| [[homework/hw2\|HW2 #5(a)]] | $\{-1,\underset{\uparrow}{0},1\}$ | $\{\underset{\uparrow}{1},2,3,4,5\}$ |
| [[1-signals-and-systems/04-impulse-response-and-convolution\|Lecture 4 §2.2]] | $\{\underset{\uparrow}{3},1,0,3,1,1\}$ | $\{2,\underset{\uparrow}{-1},1\}$ |

> [!success]- Answers (try them first — each takes 3–5 minutes)
> | instance | $y[n]$ | first index |
> |---|---|---|
> | FA2025 #3a | $\{1,2,\underset{\uparrow}{4},2,2,-2,-4,-2,-3\}$ | $-2$ |
> | SP2025 #4a | $\{2,-5,\underset{\uparrow}{5},0,-5,12,-4,3\}$ (the key's box is wrong, see below) | $-2$ |
> | FA2024 #4a | $\{2,-6,3,\underset{\uparrow}{1},6,1,-4\}$ | $-3$ |
> | FA2023 #3a | $\{\underset{\uparrow}{-1},-1,-1,1,1,1\}$ | $0$ |
> | SP2023 #3a | $\{3,-5,\underset{\uparrow}{4},5,-5,5,0,2\}$ | $-2$ |
> | SP2021 #2 | $\{1,\underset{\uparrow}{2},-4,1,1,-4,2,1\}$ | $-1$ |
> | FA2019 #4 | $\{\underset{\uparrow}{-1},5,-7,7,-6,3,-2,-1\}$ | $0$ |
> | HW2 #5(a) | $\{-1,\underset{\uparrow}{-2},-2,-2,-2,4,5\}$ | $-1$ |
> | Lecture 4 | $\{6,\underset{\uparrow}{-1},2,7,-1,4,0,1\}$ | $-1$ |
>
> All verified with `np.convolve` plus start-index bookkeeping, and each passes both checks below (`verify/problems/finite_convolution.py`).

## The method

> [!recipe] Finite-length convolution in five steps
> 1. **Index both sequences.** Write the first index and length of each: $x$ starts at $n_x$ with $N$ samples, $h$ starts at $n_h$ with $M$ samples. Count interior zeros as samples ($\{1,0,1\}$ has length 3).
> 2. **Predict the frame before computing.**
> $$
> \begin{aligned}
> \text{start} &= n_x+n_h,\\
> \text{end} &= (n_x+N-1)+(n_h+M-1),\\
> \text{length} &= N+M-1,
> \end{aligned}
> $$
> and the two end samples are free: $y[\text{start}] = x[n_x]\,h[n_h]$, $y[\text{end}]$ = (last of $x$)(last of $h$).
> 3. **Compute with one of the three layouts below** — use the one with the fewest multiplications: shifted copies when one sequence has only two or three nonzero samples, the table otherwise, the matrix if you like linear algebra.
> 4. **Place the arrow**: the first sample of $y$ is at the start index from step 2; count forward to $n=0$.
> 5. **Check** (10 seconds each):
> $$
> \begin{aligned}
> \sum_n y[n] &= \Big(\sum_n x[n]\Big)\Big(\sum_n h[n]\Big),\\
> \sum_n (-1)^n y[n] &= \Big(\sum_n (-1)^n x[n]\Big)\Big(\sum_n (-1)^n h[n]\Big).
> \end{aligned}
> $$
> These are $Y(1)=X(1)H(1)$ and $Y(-1)=X(-1)H(-1)$. The first catches arithmetic slips; the second also catches a misplaced arrow (shifting the answer by an odd number of samples flips its sign).

**Layout A — shifted copies (impulse decomposition).** Write $h$ as a sum of deltas, $h[n]=\sum_k h[k]\,\delta[n-k]$; then $y[n]=\sum_k h[k]\,x[n-k]$ is a sum of scaled, shifted copies of $x$. One row per nonzero $h[k]$, aligned by $n$, add the columns. For $h=\{1,\underset{\uparrow}{2},-1\}$ this is $y[n]=x[n+1]+2x[n]-x[n-1]$. It is the fastest layout on the exam and it is exactly how a system given as "$y[n]=x[n+1]-2x[n]+3x[n-2]$" should be read.

**Layout B — the table (flip and slide).** Top row $x[k]$ against $k$. For each output index $n$, write $h[n-k]$ (i.e. $h$ *flipped*, then slid so that $h[0]$ sits under $k=n$), multiply the overlapping entries, and add: $y[n]=\sum_k x[k]\,h[n-k]$. This is Lecture 4's "shift-and-overlap" table; zero-extend both sequences where they do not overlap.

**Layout C — the matrix.** Build a Toeplitz matrix whose columns are shifted copies of one sequence ($N+M-1$ rows), and multiply by the other as a column vector. Row 1 is the start index from step 2, **not** $n=0$.

> [!example] Python: `np.convolve` does the arithmetic, you do the indices
> ```python
> import numpy as np
>
> x, nx = np.array([1, -2, 0, 3, -1, 1]), -2    # SP2025 #4(a): x starts at n = -2
> h, nh = np.array([2, -1, 3]), 0                # h starts at n = 0
> y = np.convolve(x, h)                          # np.convolve knows nothing about n ...
> ny = nx + nh                                   # ... so track the start index yourself
> n = np.arange(ny, ny + len(y))
> print(dict(zip(n.tolist(), y.tolist())))
> print("start", ny, "end", n[-1], "length", len(y), "=", len(x), "+", len(h), "- 1")
> print("sum check:", y.sum(), "=", x.sum() * h.sum())
> alt = lambda v, n0: int(np.sum(v * (-1) ** np.abs(np.arange(n0, n0 + len(v)))))
> print("alternating check:", alt(y, ny), "=", alt(x, nx) * alt(h, nh))
> key = np.array([2, -5, 6, 0, -5, 10, -4, 3])   # the answer key's boxed y
> print("key's boxed answer sums to", key.sum())
> ```
> ```text
> {-2: 2, -1: -5, 0: 5, 1: 0, 2: -5, 3: 12, 4: -4, 5: 3}
> start -2 end 5 length 8 = 6 + 3 - 1
> sum check: 8 = 8
> alternating check: -12 = -12
> key's boxed answer sums to 7
> ```
> The SP2025 key boxed $\{2,-5,6,0,-5,10,-4,3\}$; its own matrix product gives the values above, and the box fails the sum check ($7\neq 2\cdot4$). See [[0-toolkit/05-errata|errata]].

> [!trap] Where the points go
> - **The arrow.** A correct list with $n=0$ in the wrong place is a wrong answer. Always derive the start index ($n_x+n_h$) instead of eyeballing it; in FA2019 #4 *both* arrows sit under the first entries, so $y$ starts at $n=0$; in SP2021 #2 $h$ starts at $n=-1$, so $y$ starts at $n=-1$ and its arrow sits on the second entry. Same method, different bookkeeping — read the arrows before you compute.
> - **Forgetting to flip** in the table method: sliding $h[k-n]$ instead of $h[n-k]$ computes a correlation. With a symmetric $h$ you will not notice; with $\{2,\underset{\uparrow}{0},-1\}$ you will.
> - **Dropping interior or edge zeros.** $h=\{1,0,\underset{\uparrow}{1}\}$ is $\delta[n+2]+\delta[n]$, not $\delta[n+1]+\delta[n]$.
> - **Sign slips with negative samples** — the sum check catches almost all of them.
> - **Reading a difference equation's coefficients as $h$ without the indices:** $y[n]=x[n+1]-2x[n]+3x[n-2]$ has $h=\{1,\underset{\uparrow}{-2},0,3\}$ (starts at $n=-1$, with a 0 at $n=1$).

## Practice problems

> [!question] Practice 1 — shifted copies and one table row
> $x[n]=\{2,-1,\underset{\uparrow}{0},3,1\}$, $h[n]=\{1,\underset{\uparrow}{2},-1\}$. Compute $y=x*h$ and mark $n=0$. Then recompute $y[0]$ alone with one row of the flip-and-slide table.

> [!success]- Solution
> **Frame:** $x$ starts at $-2$ (length 5), $h$ at $-1$ (length 3), so $y$ runs from $-3$ to $3$, length 7; $y[-3]=2\cdot1=2$, $y[3]=1\cdot(-1)=-1$.
>
> **Shifted copies:** $h=\delta[n+1]+2\delta[n]-\delta[n-1]$, so $y[n]=x[n+1]+2x[n]-x[n-1]$:
>
> | $n$ | $-3$ | $-2$ | $-1$ | $0$ | $1$ | $2$ | $3$ |
> |---|---|---|---|---|---|---|---|
> | $x[n+1]$ | 2 | $-1$ | 0 | 3 | 1 | | |
> | $2x[n]$ | | 4 | $-2$ | 0 | 6 | 2 | |
> | $-x[n-1]$ | | | $-2$ | 1 | 0 | $-3$ | $-1$ |
> | $y[n]$ | **2** | **3** | **$-4$** | **4** | **7** | **$-1$** | **$-1$** |
>
> $$
> y[n]=\{2,\ 3,\ -4,\ \underset{\uparrow}{4},\ 7,\ -1,\ -1\}\qquad(\text{starts at } n=-3).
> $$
> **One table row:** $y[0]=\sum_k x[k]h[-k] = x[-1]h[1]+x[0]h[0]+x[1]h[-1] = (-1)(-1)+0\cdot2+3\cdot1 = 4$ ✓.
>
> **Checks:** $\sum y = 10 = 5\cdot2$ ✓; alternating: $\sum(-1)^n y[n] = 2 = (1)(2)$ ✓.

> [!question] Practice 2 — a system given by its equation (matrix layout)
> An LTI system is $y[n]=x[n+1]-2x[n]+3x[n-2]$. Find $h[n]$, then the output for $x[n]=\{\underset{\uparrow}{1},3,-1,2\}$ using the matrix layout.

> [!success]- Solution
> Put $x=\delta$: $h[n]=\delta[n+1]-2\delta[n]+3\delta[n-2]=\{1,\underset{\uparrow}{-2},0,3\}$ (starts at $-1$; the 0 at $n=1$ must be kept).
>
> $y$ starts at $0+(-1)=-1$ and has $4+4-1=7$ samples. Columns of the Toeplitz matrix are copies of $h$ shifted down one row each:
> $$
> \begin{gathered}
> \begin{bmatrix} 1&0&0&0\\ -2&1&0&0\\ 0&-2&1&0\\ 3&0&-2&1\\ 0&3&0&-2\\ 0&0&3&0\\ 0&0&0&3 \end{bmatrix}
> \begin{bmatrix} 1\\3\\-1\\2 \end{bmatrix}
> = \begin{bmatrix} 1\\1\\-7\\7\\5\\-3\\6 \end{bmatrix}
> \\
> \Longrightarrow\quad
> y[n]=\{1,\ \underset{\uparrow}{1},\ -7,\ 7,\ 5,\ -3,\ 6\}.
> \end{gathered}
> $$
> The first row is $n=-1$, so the arrow goes on the second entry. Shifted-copies cross-check: $y[2]=x[3]-2x[2]+3x[0]=2+2+3=7$ ✓. Sum check: $10 = 5\cdot2$ ✓.

> [!question] Practice 3 — grade two classmates
> $x[n]=\{2,\underset{\uparrow}{1},-1,3\}$ and $h[n]=\{1,-1,\underset{\uparrow}{2}\}$. Classmate A answers $\{2,-1,4,\underset{\uparrow}{6},-5,6\}$; classmate B answers $\{2,-1,\underset{\uparrow}{2},6,-5,6\}$. Find the correct $y$ and say which check exposes each classmate — without redoing their arithmetic.

> [!success]- Solution
> Frame: start $=-1+(-2)=-3$, length $4+3-1=6$, $y[-3]=2\cdot1=2$, $y[2]=3\cdot2=6$. Computing (e.g. by shifted copies of $x$ with weights $1,-1,2$ at $n=-2,-1,0$):
> $$
> y[n]=\{2,\ -1,\ 2,\ \underset{\uparrow}{6},\ -5,\ 6\}\qquad(\text{starts at } -3).
> $$
> - **A** fails the **sum check**: $2-1+4+6-5+6=12$, but $\sum x\cdot\sum h = 5\cdot2=10$. (A's third entry is wrong.)
> - **B** has the right numbers but the arrow says $y$ starts at $-2$: that violates the **start rule** ($n_x+n_h=-3$), and the **alternating check** catches it too — B's list gives $\sum(-1)^n y[n]=-12$, while $X(-1)H(-1)=3\cdot4=12$.
>
> The correct answer passes both: $\sum y=10$, $\sum(-1)^n y[n]=12$.

All three solutions (and every instance above) are verified in `verify/problems/finite_convolution.py`; the snippet is `verify/problems/snippets/finite_conv_snippet.py`.

## Related

- [[demos/convolution-explorer|Convolution explorer]] — type in two sequences with any $n=0$ position and watch the flip-and-slide; [[0-midterm-1/practice-drills|practice drills]] generate fresh finite convolutions with auto-grading.
- [[1-signals-and-systems/04-impulse-response-and-convolution|Lecture 4]] — the convolution sum, the start/end/length rules, and the three hand methods.
- Concepts: [[concepts/convolution]] (properties: commutative, associative, identity $\delta$), [[concepts/kronecker-delta]], [[concepts/impulse-response]], [[concepts/lti-system]].
- Neighbours: [[problems/infinite-length-convolution|infinite-length convolution]] (part (b) of the same exam problem), [[problems/finding-h-from-input-output-pairs|finding h from input–output pairs]] (convolution run backwards); all families: [[problems/index|exam problem families]].

### Sources for this page

Lecture 4 notes §2 (start/end/length rules, shift-and-overlap table, Toeplitz matrix, example $\{3,1,0,3,1,1\}*\{2,-1,1\}$) and slides; HW2 #5(a) and solution; FA2025 #3a, SP2025 #4a, FA2024 #4a, FA2023 #3a, SP2023 #3a, SP2021 #2, FA2019 #4 with keys (SP2025 #4a box corrected, see [[0-toolkit/05-errata|errata]]); Midterm 1 review slides (FA2023 #3). Verification: `verify/problems/finite_convolution.py`, `verify/exams/*.py`.
