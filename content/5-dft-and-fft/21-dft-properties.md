---
title: "Lecture 21 — DFT properties"
description: "N-periodicity and modulo notation ⟨n⟩_N; circular time reversal; circular convolution x⊛h ↔ X[k]H[k] by table and circulant matrix; Table 1 of DFT properties."
tags: [lecture, midterm-2, dft]
lecture: 21
---

*Lecture 21 · Mon Oct 19, 2026 · notes + slides "DFT properties" · prev: [[5-dft-and-fft/20-discrete-fourier-transform|Lecture 20]] · next: [[5-dft-and-fft/22-spectral-analysis|Lecture 22]]*

> [!abstract] In one breath
> - DFT and inverse DFT are $N$-periodic: a length-$N$ signal acts as its periodic extension $x[\langle n\rangle_N]$.
> - Product of DFTs ↔ **circular** convolution $\sum_m x[m]\,h[\langle n-m\rangle_N]$: modified table or circulant matrix.
> - DTFT properties return with circular shifts and reversals (Table 1).

## What was covered

1. **§1 Periodicity of the DFT** (eqs. 1–6, 19, Figure 1, slides 4–6) → [[concepts/circular-shift-and-reversal|circular shift and reversal]]
2. **§2 Circular convolution** (eqs. 7–16, slides 9–10) → [[concepts/circular-convolution|circular convolution]] §1
3. **§2.1 Computing circular convolution** (eqs. 17–24, slides 11–12) → [[concepts/circular-convolution|circular convolution]] §2
4. **§3 More DFT properties** (eqs. 25–29, Table 1, slide 14) → [[concepts/dft-properties|DFT properties]]

## Exercises from this lecture

- Example 1 (slide 8), $x=\{3,1,2,4,5\}$: $x[\langle-n\rangle_5]$, $x[\langle n+2\rangle_5]$, $x[\langle1-n\rangle_5]$ → [[concepts/circular-shift-and-reversal|circular shift and reversal]] §2
- Notes example (eqs. 17–24), the 6-point $\{3,1,0,3,1,1\}\circledast\{-4,-1,-7,5,5,1\}$, table and matrix → [[concepts/circular-convolution|circular convolution]] §2 (computation not on Fall 2026 MT2)
- Example 2 (slide 13), the 5-point $\{2,0,1,3,0\}\circledast\{4,1,0,2,2\}$ vs linear → [[concepts/circular-convolution|circular convolution]] §3 (computation not on Fall 2026 MT2)
- Example 3 (slide 15), $y[n]$ from $Y[k]=\{X_2,-X_3,X_4,-X_5,X_0,-X_1\}$ → [[concepts/dft-properties|DFT properties]]

**Practice:** HW9 #1–2 · [[problems/circular-convolution-and-dft-properties|circular convolution and DFT properties family]] · [[exams/midterm-2/true-false-bank|T/F bank]] §6, §8

## Related
[[5-dft-and-fft/index|Unit 5]] · [[5-dft-and-fft/20-discrete-fourier-transform|Lecture 20]] · [[5-dft-and-fft/22-spectral-analysis|Lecture 22]] · [[concepts/index|Concepts]]

### Sources for this page
Snyder, Lecture 21 notes (§1–3, eqs. 1–29, Figure 1, Table 1) and slides (Examples 1–3), Oct 19, 2026.
