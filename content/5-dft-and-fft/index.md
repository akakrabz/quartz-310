---
title: "Unit 5 · The DFT and FFT"
description: "Lecture 20 onward: the DFT as N samples of the DTFT of a length-N signal, N-periodicity, zero-padding; DFT properties and circular convolution; later lectures to come."
tags: [dft, midterm-2]
---

*Unit 5 · Lectures 20 (Oct 16) and 21 (Oct 19) onward · prev: [[4-sampling-and-reconstruction/index|Unit 4]]*

- The DTFT is an infinite sum over a continuous $\omega$: not computable. Keep $N$ samples and $N$ frequencies $\omega_k=\frac{2\pi k}{N}$: the DFT.
- The DFT periodically extends both $x[n]$ and $X[k]$, so shifts, reversals and convolution become circular.
- Later lectures to come.

| # | page | one line |
|---|---|---|
| 20 | [[5-dft-and-fft/20-discrete-fourier-transform\|The discrete Fourier transform]] | computing the DTFT; $X[k] = X_d(2\pi k/N)$; $N$-periodicity; zero padding; matrix form (optional) |
| 21 | [[5-dft-and-fft/21-dft-properties\|DFT properties]] | modulo $\langle n\rangle_N$ and circular reversal; circular convolution (table, circulant matrix); properties table |

> [!key] The unit on one card
> - **DFT** ([[concepts/dft|DFT]]): $X[k]=\sum_{n=0}^{N-1}x[n]\,e^{-j\frac{2\pi k}{N}n}$, $0\le k\le N-1$; inverse $x[n]=\frac1N\sum_{k=0}^{N-1}X[k]\,e^{j\frac{2\pi k}{N}n}$, $0\le n\le N-1$.
> - **DTFT samples:** $X[k]=X_d(\omega)\big|_{\omega=\omega_k}$, spacing $\frac{2\pi}{N}$ on $[0,2\pi)$. Zero-padding to $N+L$: $\tilde X[k]=X_d\!\left(\frac{2\pi k}{N+L}\right)$, same DTFT, denser.
> - **Periodicity:** $X[k+mN]=X[k]$, $x[n+mN]=x[n]$; $x[n]=x[\langle n\rangle_N]$, $\langle n\rangle_N$ = remainder of $n/N$.
> - **Circular convolution** ([[concepts/circular-convolution|circular convolution]]): $x[n]\circledast h[n]=\sum_{m=0}^{N-1}x[m]\,h[\langle n-m\rangle_N]\ \overset{\text{DFT}}{\longleftrightarrow}\ X[k]H[k]$; length $N$.
> - **Circular shift and reversal:** $x[\langle n-m\rangle_N]\leftrightarrow e^{-j\frac{2\pi km}{N}}X[k]$; $\;x[\langle -n\rangle_N]\leftrightarrow X[\langle -k\rangle_N]$; $\;x^*[n]\leftrightarrow X^*[\langle -k\rangle_N]$.

> [!exam] Exam
> DFT computation and properties on 7/7 past Midterm 2 exams, spectral analysis on 6/7, linear vs circular convolution and the FFT on 2/7: [[exams/midterm-2/index|Midterm 2]] · [[exams/midterm-2/past-exams/index|past exams]].

## Related
[[4-sampling-and-reconstruction/index|Unit 4]] · [[concepts/dtft|DTFT]] · [[concepts/dft|DFT]] · [[concepts/circular-convolution|circular convolution]] · [[exams/index|Exams]]

### Sources for this page
Snyder, ECE 310 Lecture 20 (Oct 16) and Lecture 21 (Oct 19) notes and slides, Fall 2026; past Midterm 2 exams.
