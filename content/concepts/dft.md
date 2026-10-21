---
title: "Discrete Fourier transform (DFT)"
description: "The DFT of a length-N signal: analysis and synthesis equations, X[k] as samples of the DTFT at 2πk/N, N-periodicity in k and n, zero padding, the DFT matrix, and where it appears."
tags: [concept, dft, midterm-2]
aliases: ["DFT", "discrete Fourier transform", "X[k]"]
---

> [!key] Definition (Lecture 20)
> For a length-$N$ signal $x[n]$, $x[n]\overset{\text{DFT}}{\longleftrightarrow}X[k]$:
> $$
> \begin{gathered}
> X[k]=\sum_{n=0}^{N-1}x[n]e^{-j\frac{2\pi k}{N}n},\quad0\le k\le N-1\\
> x[n]=\frac1N\sum_{k=0}^{N-1}X[k]e^{j\frac{2\pi k}{N}n},\quad0\le n\le N-1
> \end{gathered}
> $$

> [!key] The DFT samples the DTFT
> With $X_d(\omega)=\sum_{n=0}^{N-1}x[n]e^{-j\omega n}$, the DTFT of the same length-$N$ sequence,
> $$
> X[k]=X_d\!\left(\frac{2\pi k}{N}\right),\qquad0\le k\le N-1 .
> $$
> $N$ samples on $[0,2\pi)$, spacing $\frac{2\pi}{N}$. A bin with $k\gt\frac N2$ is the negative frequency $\frac{2\pi k}{N}-2\pi$.

- **$N$-periodic:** $X[k+mN]=X[k]$; the inverse DFT is $N$-periodic in $n$ (periodic extension).
- **Zero padding** to length $N+L$ keeps $X_d(\omega)$ and samples it every $\frac{2\pi}{N+L}$.
- **Matrix form:** $\mathbf X=\mathbf W\mathbf x$, $\mathbf W_{kn}=W_N^{kn}$, $W_N=e^{-j\frac{2\pi}{N}}$, $\mathbf W^{-1}=\frac1N\mathbf W^*$.

| | DTFT $X_d(\omega)$ | DFT $X[k]$ |
|---|---|---|
| input | any summable $x[n]$ | length $N$ |
| frequencies | every $\omega$, $2\pi$-periodic | $N$ values, $N$-periodic in $k$ |
| on a computer | no | yes |

> [!trap]
> - The inverse DFT is not zero outside $0\le n\le N-1$; it repeats.
> - Zero padding changes the DFT grid, never $X_d(\omega)$.

**Where it appears.**
- Lectures: [[5-dft-and-fft/20-discrete-fourier-transform|L20]] (definition, DTFT samples, periodicity, zero padding, matrix form) · [[5-dft-and-fft/21-dft-properties|L21]] (periodic extension, circular convolution, properties).
- Past exams: on all seven past Midterm 2 exams ([[exams/midterm-2/index|Midterm 2 overview]] §3); True/False in the [[exams/midterm-2/true-false-bank|T/F bank]] §6.

Related: [[concepts/dtft|DTFT]] · [[concepts/circular-convolution|circular convolution]] · [[concepts/fourier-series|Fourier series]] · [[concepts/aliasing|aliasing]]

### Sources for this page
Snyder, Lecture 20 notes (eqs. 8–25, 39–45) and slides, Oct 16, 2026.
