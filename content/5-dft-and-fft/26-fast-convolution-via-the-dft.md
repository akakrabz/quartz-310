---
title: "Lecture 26 — Fast convolution via the DFT"
description: "The convolution sum is O(N²); DFT products give circular convolution; zero-padding to N + L − 1 makes it linear; the four-step O(N log N) algorithm."
tags: [lecture, dft, fft]
lecture: 26
---

*Lecture 26 · Fri Nov 6, 2026 (the last ten minutes of class; repeated more slowly in a makeup recording posted the same day) · "Fast convolution via the DFT" · prev: [[5-dft-and-fft/25-fast-fourier-transform|Lecture 25]] · next: [[6-filter-design/27-practical-filter-design|Lecture 27]] · last lecture on the DFT*

> [!abstract] In one breath
> - Convolving two length-$N$ sequences directly costs $O(N^2)$.
> - Multiplying DFTs gives circular, not linear, convolution; zero-padding both to $N+L-1$ removes the difference.
> - Pad, FFT, multiply, inverse FFT: $O(N\log N)$, worth it for long sequences.

> [!lecture] In lecture — L26, Nov 6
> Introduced as "arguably the quickest lecture all semester": we have "this wonderful $N\log N$ complexity, and can we push this forward to give us quicker computation of convolution?" The $N^2$ cost of the convolution sum "bothers me, and I want to do better." He closed with: "We got through everything … this is the extent to which we need to explore it. Monday's lecture, filter design."

## What was covered

1. **§1 Computational complexity of the convolution sum** (eqs. 1–2, slide 3) → [[concepts/fast-convolution|fast convolution]] §1
2. **§2 Linear convolution via the DFT:** the circular convolution property again (eq. 3, slide 4) → [[concepts/circular-convolution|circular convolution]]
3. **Circular against linear on an example, and the zero-padding fix** (eqs. 4–10, slides 5–6) → [[concepts/fast-convolution|fast convolution]] §2
4. **§2.1 Fast convolution algorithm** and its cost (eq. 11, slide 7) → [[concepts/fast-convolution|fast convolution]] §3–4

## Exercises from this lecture

- Slides 5–6: $\{1,2,3,4\}$ and $\{-1,1,-2,2\}$, linear, 4-point circular, and padded to 7 → [[concepts/fast-convolution|fast convolution]] §2
- Notes (eqs. 4–10): $\{3,1,0,-1\}$ and $\{5,1,-1,4\}$ → [[concepts/fast-convolution|fast convolution]] §2

**Practice:** [[homework/hw10|HW10]] #2–#3 · [[exams/midterm-2/past-exams/fall-2019|FA2019 MT2 #11]] · ECE 311 Lab 5

## Related
[[5-dft-and-fft/index|Unit 5]] · [[concepts/zero-padding|zero padding]] · [[concepts/fast-fourier-transform|FFT]] · [[concepts/index|Concepts]]

### Sources for this page
Snyder, Lecture 26 notes (§1–2.1, eqs. 1–11) and annotated slides 1–7, Nov 6, 2026; lecture recording Nov 6 and the makeup recording posted Nov 6 (condensed).
