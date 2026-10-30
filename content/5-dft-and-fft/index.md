---
title: "Unit 5 · The DFT and FFT"
description: "Lectures 20–23: the DFT as N samples of the DTFT, N-periodicity, zero padding; circular shifts and convolution, the properties table; spectral analysis: periodic sinc, leakage, lobe separation, window functions."
tags: [dft, spectral-analysis, midterm-2]
---

*Unit 5 · Lectures 20 (Oct 16) to 23 (Oct 23) · prev: [[4-sampling-and-reconstruction/index|Unit 4]] · Lecture 23 is the last Midterm 2 content*

**Midterm 2** (Wed Nov 4, 7–9 pm) covers all of Unit 5 → [[exams/midterm-2/index|Midterm 2 review]]. DFT properties (circular shift, reversal, modulation, symmetry) are tested; computing circular convolution is not (instructor).

- The DTFT is an infinite sum over a continuous $\omega$: not computable. Keep $N$ samples and $N$ frequencies $\omega_k=\frac{2\pi k}{N}$: the DFT.
- The DFT periodically extends both $x[n]$ and $X[k]$, so shifts, reversals and convolution become circular.
- A finite cosine is a periodic-sinc lobe pair, not an impulse pair: leakage, resolution limits and side-lobe masking are the price, windows and longer records the remedies.

## Topics

| topic | one line |
|---|---|
| [[concepts/dft\|DFT]] | $X[k]=\sum_{n=0}^{N-1}x[n]e^{-j\frac{2\pi k}{N}n}=X_d\!\left(\frac{2\pi k}{N}\right)$; $N$-periodic; DFT matrix |
| [[concepts/zero-padding\|Zero padding]] | append zeros: same DTFT, denser bins $\frac{2\pi}{N+L}$; $\tilde X[k']=X[k]$ when $\frac{k'}{N+L}=\frac kN$; never better resolution |
| [[concepts/circular-shift-and-reversal\|Circular shift, reversal, modulo]] | $x[\langle n\rangle_N]$, $\langle-1\rangle_3=2$; $x[\langle-n\rangle_N]=x[0],x[N-1],\dots,x[1]$ |
| [[concepts/circular-convolution\|Circular convolution]] | $\sum_mx[m]h[\langle n-m\rangle_N]\leftrightarrow X[k]H[k]$; table or circulant matrix; = linear when padded to $N\ge N_1+N_2-1$ |
| [[concepts/dft-properties\|DFT properties]] | Table 1: circular shifts ↔ phase ramps, modulation, reversal, conjugation, Parseval; reading a permuted DFT |
| [[concepts/periodic-sinc\|Periodic sinc]] | $C(\omega)=e^{-j\frac\omega2(N-1)}\frac{\sin(N\omega/2)}{\sin(\omega/2)}$: lobe of height $N$, width $\frac{4\pi}{N}$; finite cosine $=\frac A2C(\omega\mp\omega_0)$ |
| [[concepts/spectral-leakage\|Spectral leakage]] | on-bin cosine ($\frac{\omega_0N}{2\pi}$ integer): two bins of $\frac{AN}{2}$; off-bin: energy in every bin |
| [[concepts/spectral-analysis\|Spectral analysis]] | find $M$, $\omega_m$, $A_m$ from a DFT plot; the $0.55\pi/0.65\pi$ example; two challenges |
| [[concepts/frequency-resolution\|Frequency resolution]] | full-lobe $N\gt\frac{4\pi}{\Delta\omega}$, half-lobe $N\gt\frac{2\pi}{\Delta\omega}$; duration $\frac{2}{\Delta f}$ s whatever $f_s$ |
| [[concepts/window-functions\|Window functions]] | $x[n]w[n]\leftrightarrow\frac1{2\pi}X_d*W_d$; rectangular $-13$ dB, $\frac{4\pi}{N}$; Hamming $-42$ dB, $\frac{8\pi}{N}$; not LTI |

## Lectures

| # | page | one line |
|---|---|---|
| 20 | [[5-dft-and-fft/20-discrete-fourier-transform\|The discrete Fourier transform]] | computing the DTFT; $X[k]=X_d(2\pi k/N)$; $N$-periodicity; zero padding; matrix form (optional) |
| 21 | [[5-dft-and-fft/21-dft-properties\|DFT properties]] | modulo $\langle n\rangle_N$ and circular reversal; circular convolution (table, circulant matrix); properties table |
| 22 | [[5-dft-and-fft/22-spectral-analysis\|Spectral analysis with the DFT]] | finite cosine and the periodic sinc; leakage; the spectral analysis problem; zero padding; two challenges |
| 23 | [[5-dft-and-fft/23-spectral-analysis-and-window-functions\|Spectral analysis and window functions]] | full/half-lobe separation; guitar example; rectangular vs Hamming; the tradeoff. **Last Midterm 2 lecture.** |

> [!key] The unit on one card
> - **DFT** ([[concepts/dft|DFT]]): $X[k]=\sum_{n=0}^{N-1}x[n]\,e^{-j\frac{2\pi k}{N}n}$, $0\le k\le N-1$; inverse $x[n]=\frac1N\sum_{k=0}^{N-1}X[k]\,e^{j\frac{2\pi k}{N}n}$, $0\le n\le N-1$.
> - **DTFT samples:** $X[k]=X_d(\omega)\big|_{\omega=\omega_k}$, spacing $\frac{2\pi}{N}$ on $[0,2\pi)$. Zero-padding to $N+L$: $\tilde X[k]=X_d\!\left(\frac{2\pi k}{N+L}\right)$, same DTFT, denser.
> - **Periodicity:** $X[k+mN]=X[k]$, $x[n+mN]=x[n]$; $x[n]=x[\langle n\rangle_N]$, $\langle n\rangle_N$ = remainder of $n/N$.
> - **Circular convolution** ([[concepts/circular-convolution|circular convolution]]): $x[n]\circledast h[n]=\sum_{m=0}^{N-1}x[m]\,h[\langle n-m\rangle_N]\ \overset{\text{DFT}}{\longleftrightarrow}\ X[k]H[k]$; length $N$.
> - **Circular shift and reversal:** $x[\langle n-m\rangle_N]\leftrightarrow e^{-j\frac{2\pi km}{N}}X[k]$; $\;x[\langle -n\rangle_N]\leftrightarrow X[\langle -k\rangle_N]$; $\;x^*[n]\leftrightarrow X^*[\langle -k\rangle_N]$.
> - **Finite cosine** ([[concepts/periodic-sinc|periodic sinc]]): $A\cos(\omega_0n)$ on $N$ samples $\leftrightarrow\frac A2C(\omega-\omega_0)+\frac A2C(\omega+\omega_0)$, lobe height $\frac{AN}{2}$, width $\frac{4\pi}{N}$; DFT has two bins iff $\frac{\omega_0N}{2\pi}\in\mathbb Z$.
> - **Resolution and windows:** $N\gt\frac{4\pi}{\Delta\omega}$ (full lobe), $\frac{2\pi}{\Delta\omega}$ (half); rectangular $-13$ dB vs Hamming $-42$ dB with twice the lobe width.

> [!exam] Exam
> DFT computation and properties on 7/7 past Midterm 2 exams, spectral analysis on 6/7, linear vs circular convolution and the FFT on 2/7 (neither on Fall 2026 Midterm 2): [[exams/midterm-2/index|Midterm 2]] · [[exams/midterm-2/past-exams/index|past exams]] · families: [[problems/dft-values-and-zero-padding|DFT values and zero padding]] · [[problems/circular-convolution-and-dft-properties|circular convolution and DFT properties]] · [[problems/dft-spectral-analysis|DFT spectral analysis]].

## Related
[[4-sampling-and-reconstruction/index|Unit 4]] · [[concepts/dtft|DTFT]] · [[concepts/dft|DFT]] · [[concepts/spectral-analysis|spectral analysis]] · [[concepts/index|Concepts]] · [[exams/index|Exams]]

### Sources for this page
Snyder, ECE 310 Lectures 20–23 notes and slides (Oct 16–23, 2026); past Midterm 2 exams.
