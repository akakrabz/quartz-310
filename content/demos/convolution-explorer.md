---
title: "Demo — Convolution explorer (flip, shift, multiply, add)"
description: "Enter two finite sequences and their start indices, slide n to watch h[n−k] pass over x[k]; shift-and-overlap table, matrix form y = Hx, start/end/length bookkeeping, past-exam presets."
tags: [demo, convolution, midterm-1]
---

*Demo · pairs with [[1-signals-and-systems/04-impulse-response-and-convolution|Lecture 4]] · recipe: [[problems/finite-length-convolution|finite-length convolution]] · concepts: [[concepts/convolution]], [[concepts/impulse-response]], [[concepts/lti-system]]*

<div class="ece-demo">
<iframe src="/static/demos/convolution/" title="Convolution explorer — interactive demo" loading="lazy" style="height:1750px"></iframe>
</div>

[Open the demo in its own tab](/static/demos/convolution/).

**Input.** Samples of $x[n]$ and $h[n]$ as lists, plus each start index (where the arrow ↑ puts $n=0$). The plot draws $h[n-k]$ with $h[0]$ (big dot) at $k=n$ (▲); below: output, start/end/length, the Lecture 4 table, and $y = \mathbf{H}x$.

## What to try

1. **Lecture 4's Table 1:** start $0 + (-1) = -1$, end $5 + 1 = 6$, length $8$; $y[n] = \{6,\ \underset{\uparrow}{-1},\ 2,\ 7,\ -1,\ 4,\ 0,\ 1\}$.
2. **The arrow, [[exams/midterm-1/past-exams/fall-2025|FA2025 #3a]]:** $h = \{1, 0, \underset{\uparrow}{1}\}$ starts at $n=-2$; $y[0] = 4$. Set h's start to 0 and the whole answer slides.
3. **Wrong key, [[exams/midterm-1/past-exams/spring-2025|SP2025 #4a]]:** $y[0] = 5$, $y[3] = 12$; the boxed key says 6 and 10, its own matrix agrees with the demo ([[0-toolkit/05-errata|errata]]).
4. **[[exams/midterm-1/past-exams/fall-2019|FA2019 #4]]:** both arrows under the first entries: $\{\underset{\uparrow}{-1}, 5, -7, 7, -6, 3, -2, -1\}$.
5. **Deltas, [[exams/midterm-1/past-exams/spring-2021|SP2021 #2]]:** $h = -\delta[n+1] + \delta[n-1]$ gives $y[n] = x[n-1] - x[n+1]$.
6. **Flip the shorter one ([[homework/hw2|HW2 #5a]]):** switching the flipped sequence leaves $y$ unchanged.
7. **Moving average, L = 4:** first and last 3 outputs are partial overlaps.

> [!trap]
> - Finite, real sequences only (up to 40 samples); infinite-length cases need the sum ([[problems/infinite-length-convolution|infinite / mixed convolution]]).
> - Typed end zeros count toward $N$, $M$.
> - `np.convolve` returns values only; the start index is yours.

## Related
[[concepts/convolution]] · [[concepts/kronecker-delta]] · [[problems/finite-length-convolution]] · [[problems/infinite-length-convolution]] · [[demos/difference-equation-simulator]] · [[supplements/demo-notebooks|course notebooks]]

### Sources for this page
Lecture 4 notes §2 (Eqs. 15–18, Table 1), slides 10–11, 15; Lecture 5 Eq. 3; HW2 #5(a); FA2025 #3a, SP2025 #4a, FA2019 #4, SP2021 #2 keys.
