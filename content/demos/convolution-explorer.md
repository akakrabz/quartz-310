---
title: "Demo — Convolution explorer (flip, shift, multiply, add)"
description: "Enter two finite sequences and their start indices, then slide n to watch h[n−k] pass over x[k]. The demo shows the shift-and-overlap table, the matrix form y = Hx, and the start/end/length bookkeeping, with presets for every past-exam convolution."
tags: [demo, convolution, midterm-1]
---

*Demo · pairs with [[1-signals-and-systems/04-impulse-response-and-convolution|Lecture 4]] · recipe: [[problems/finite-length-convolution|finite-length convolution]] (on all 7 past exams) · concepts: [[concepts/convolution]], [[concepts/impulse-response]], [[concepts/lti-system]]*

<div class="ece-demo">
<iframe src="/static/demos/convolution/" title="Convolution explorer — interactive demo" loading="lazy" style="height:1750px"></iframe>
</div>

[Open the demo in its own tab](/static/demos/convolution/) if the frame is cramped on your screen.

Type the samples of $x[n]$ and $h[n]$ as comma-separated lists. Then say where each one **starts**: the index of its first entry, which is how you read off the arrow ↑ that marks $n = 0$. The top plot keeps $x[k]$ fixed. It draws $h[n-k]$ flipped and shifted so that its $h[0]$ sample (big dot) sits at $k = n$ (▲), and multiplies the two where they overlap. The sum of those products is $y[n]$. Below it are the full output, the start/end/length facts, the Lecture 4 shift-and-overlap table (click a row to jump to that $n$) and the matrix form $y = \mathbf{H}x$.

## What to try

1. **Rebuild Lecture 4's Table 1, one row at a time.** Load *Lecture 4 notes*, press ◀ until $n = -1$ and predict each $y[n]$ before you press ▶. The start is $k_s = n_s + m_s = 0 + (-1) = -1$, the end is $k_e = n_e + m_e = 5 + 1 = 6$, and the length is $K = N + M - 1 = 8$, so there are exactly 8 rows to fill. Answer: $y[n] = \{6,\ \underset{\uparrow}{-1},\ 2,\ 7,\ -1,\ 4,\ 0,\ 1\}$.
2. **The arrow is worth points.** Load *FA2025 #3a*. The arrow on $h = \{1, 0, \underset{\uparrow}{1}\}$ sits under the *last* entry, so $h = \delta[n+2] + \delta[n]$ starts at $n = -2$ and $y[0] = 4$. Now change h's start to 0: every value stays the same, but the whole answer slides two places and the arrow lands on a different number. That is the most common way to lose points on this problem ([[exams/midterm-1/past-exams/fall-2025|FA2025 #3a]]).
3. **Catch a wrong answer key.** Load *SP2025 #4a* and read $y[0] = 5$ and $y[3] = 12$ off the table. The key's boxed answer says 6 and 10, but the key's own matrix column agrees with the demo ([[exams/midterm-1/past-exams/spring-2025|SP2025 #4a]], [[0-toolkit/05-errata|errata]]).
4. **Find where n = 0 is before you compute anything.** Load *FA2019 #4*. Both arrows sit under the *first* entries, so $y$ starts at $n = 0$: $\{\underset{\uparrow}{-1}, 5, -7, 7, -6, 3, -2, -1\}$. Then load *SP2021 #2*, where h's arrow is on its middle entry, so y starts at $n = -1$ and the arrow moves to the second entry. In the matrix view the row labelled "← n = 0" moves with it ([[exams/midterm-1/past-exams/fall-2019|FA2019 #4]], [[exams/midterm-1/past-exams/spring-2021|SP2021 #2]]).
5. **Use deltas instead of the table.** In *SP2021 #2*, $h = -\delta[n+1] + \delta[n-1]$, so $y[n] = x[n-1] - x[n+1]$ with no table needed. Check two samples against the demo, then do the same for *Lecture 4 slides — extra practice*, where $y[n] = x[n+1] - x[n]$.
6. **Flip the shorter one.** *HW2 #5a* flips $x = \{-1, \underset{\uparrow}{0}, 1\}$ because it is shorter. Switch "flip" to h and nothing in $y$ changes, because convolution commutes; only the table and the matrix are built from the other sequence ([[homework/hw2|HW2 #5]]).
7. **See the moving average fill up and drain.** With *Moving average, L = 4*, the first and last $L - 1 = 3$ outputs come from partial overlaps: $y[0] = \tfrac14 x[0]$ is not an average of four samples yet. This is the same filter as the FIR preset in the [[demos/difference-equation-simulator|difference-equation simulator]].
8. **Check the matrix against the table.** In the matrix, row $n$ of $\mathbf{H}$ holds exactly the numbers of table row $h[n-k]$, and each column is $h$ shifted down one row. Several exam keys (FA2019, SP2021, SP2025) solve this problem as $y = \mathbf{H}x$.

## What the demo is (and isn't)

It handles **finite-length, real-valued** sequences (up to 40 samples each). Samples outside the range you type are zero ("zero extension", Lecture 4). Zeros you type at the ends count towards $N$ and $M$, so they move $k_s$ and $k_e$ but not the non-zero values. Values appear as fractions when they are simple (1/4, 3/2) and as 4-significant-digit decimals otherwise.

It does not do convolutions with an infinite-length sequence. For example, $\left(\tfrac12\right)^n u[n] * u[n]$ needs the convolution sum plus a geometric series (or the z-transform). In FA2025 #3b, $x = \{-1, \underset{\uparrow}{0}, 1\}$ meets $h[n] = n(\tfrac13)^n\cos(n)$, and the answer is just $y[n] = -h[n+1] + h[n-1]$. See [[problems/infinite-length-convolution|infinite / mixed convolution]].

Every preset's output was checked against `np.convolve` with the start-index bookkeeping. They were also checked against the published answers (lecture notes and slides, HW2 solution, exam keys), with the SP2025 #4a erratum applied. The FA2019 #4 statement puts h's arrow under its first entry ($-\underset{\uparrow}{1}$, easy to misread as the middle entry), and the key's answer starts at $n = 0$. numpy only gives you the *values*; the position is your job:

```python
import numpy as np
x, ns = [3, 1, 0, 3, 1, 1], 0      # x[n] = {3↑, 1, 0, 3, 1, 1}
h, ms = [2, -1, 1], -1             # h[n] = {2, −1↑, 1}
y = np.convolve(x, h)              # values only
ks = ns + ms                       # start index: numpy does not track it
print(y, "starts at n =", ks, "  y[0] =", y[0 - ks])
```

```text
[ 6 -1  2  7 -1  4  0  1] starts at n = -1   y[0] = -1
```

## Related

[[concepts/convolution]] · [[concepts/impulse-response]] · [[concepts/kronecker-delta]] · [[concepts/lti-system]] · [[problems/finite-length-convolution]] · [[problems/infinite-length-convolution]] · [[1-signals-and-systems/04-impulse-response-and-convolution|Lecture 4]] · [[1-signals-and-systems/05-difference-equations-and-block-diagrams|Lecture 5 (moving average)]] · [[demos/difference-equation-simulator]] · [[supplements/demo-notebooks|course notebooks]] (`demo_convolution.ipynb`)

### Sources for this page

Lecture 4 notes §2 (start point, end point and length, Eqs. 15–17; Table 1; operator matrix, Eq. 18). Lecture 4 slides 10–11 (shift-and-overlap and matrix method, $x = \{\underset{\uparrow}{1}, 2, 0, -4, -1\}$, $h = \{-2, \underset{\uparrow}{0}, 1\}$) and slide 15 (extra practice). Lecture 5 notes Eq. 3 (moving average). HW2 #5(a) and its solution. Exam keys: FA2025 #3a, SP2025 #4a (key's matrix column), FA2019 #4, SP2021 #2. Course notebook `demo_convolution.ipynb`.
