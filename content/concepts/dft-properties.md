---
title: "DFT properties"
description: "Table 1 of Lecture 21: linearity, circular time and frequency shifts, circular modulation, reversal, conjugation, duality, circular convolution, windowing, Parseval, for length-N signals; how to read a permuted or phase-ramped DFT (slide Example 3)."
tags: [concept, dft, midterm-2]
aliases: ["DFT property table", "circular time shift", "circular frequency shift", "circular modulation", "DFT conjugation", "DFT duality", "DFT Parseval"]
---

*Lecture 21 (Mon Oct 19) §3 · [[homework/hw9|HW9]] #1–2 · family: [[problems/circular-convolution-and-dft-properties|circular convolution and DFT properties]]*

> [!abstract] In one breath
> - The [[concepts/dtft-properties|DTFT properties]] return with every shift and reversal circular: both $x[n]$ and $X[k]$ are $N$-periodic.
> - Shift by $m$ ↔ phase ramp $e^{-j\frac{2\pi mk}{N}}$; ramp $e^{j\frac{2\pi mn}{N}}$ ↔ circular shift of $X[k]$ by $m$.
> - A permuted, sign-flipped DFT list is a product of these (Example 3).

**On Fall 2026 MT2 (instructor):** DFT properties incl. circular shifting are tested; computing circular convolution is not.

## 1. Table 1 — DFT properties of length-N signals

| property | $x[n]$ | $X[k]$ |
|---|---|---|
| linearity | $ax_1[n]+bx_2[n]$ | $aX_1[k]+bX_2[k]$ |
| circular time shift (eq. 25) | $x[\langle n-m\rangle_N]$ | $e^{-j\frac{2\pi mk}{N}}X[k]$ |
| circular frequency shift (eq. 26) | $e^{j\frac{2\pi mn}{N}}x[n]$ | $X[\langle k-m\rangle_N]$ |
| circular modulation (eq. 27) | $\cos\!\left(\frac{2\pi m}{N}n\right)x[n]$ | $\frac12X[\langle k+m\rangle_N]+\frac12X[\langle k-m\rangle_N]$ |
| circular time reversal (eq. 28) | $x[\langle -n\rangle_N]$ | $X[\langle -k\rangle_N]$ |
| conjugation (eq. 29) | $x^*[n]$ | $X^*[\langle -k\rangle_N]$ |
| duality | $X[n]$ | $N\,x[\langle -k\rangle_N]$ |
| circular convolution | $x[n]\circledast h[n]$ | $X[k]H[k]$ |
| windowing | $x[n]w[n]$ | $\frac1N X[k]\circledast W[k]$ |
| Parseval's theorem | $\sum_{n=0}^{N-1}x[n]y^*[n]$ | $\frac1N\sum_{k=0}^{N-1}X[k]Y^*[k]$ |
| Parseval's relation | $\sum_{n=0}^{N-1}\lvert x[n]\rvert^2$ | $\frac1N\sum_{k=0}^{N-1}\lvert X[k]\rvert^2$ |

- **Circular time shift** (eq. 25): linear phase in $k$, slope $-\frac{2\pi m}{N}$ ↔ delay by $m$, circular because both domains are $N$-periodic ([[concepts/circular-shift-and-reversal|circular shift]]).
- **Circular frequency shift** (eq. 26): linear phase in $n$ ↔ circular shift of $X[k]$; the dual of eq. 25. **Modulation** (eq. 27): that shift applied to both exponentials of the cosine.
- **Reversal, conjugation** (eqs. 28–29): $X[\langle -k\rangle_N]$ is $X[0]$ at $k=0$, $X[N-k]$ otherwise. Real $x$: $X[k]=X^*[\langle -k\rangle_N]$.
- **Circular convolution**, **windowing**: [[concepts/circular-convolution|circular convolution]] (computing it: not on MT2).
- **Shift by $\frac N2$:** $m=\frac N2$ in eq. 26 gives $e^{j\pi n}=(-1)^n$, so $(-1)^nx[n]\leftrightarrow X[\langle k-\frac N2\rangle_N]$; by eq. 25, $(-1)^kX[k]\leftrightarrow x[\langle n-\frac N2\rangle_N]$ ($N$ even).
- Notes typos: p. 2 "refer to lecture 21" means Lecture 20 (its eqs. 13–17); under eq. 25 "slope $-2\pi m/M$" means $-2\pi m/N$.

> [!question] Example 3 (slide 15) — applying DFT properties
> $x[n]=\{\underset{\uparrow}{1},\ 2,\ 3,\ 4,\ 5,\ 6\}$ has DFT $X[k]=\{X_0,X_1,X_2,X_3,X_4,X_5\}$. Find $y[n]$ with $Y[k]=\{X_2,\ -X_3,\ X_4,\ -X_5,\ X_0,\ -X_1\}$.

> [!success]- Answer
> - Pattern: $Y[k]=(-1)^k\,X[\langle k+2\rangle_6]$.
> - $X[\langle k-(-2)\rangle_6]$: frequency shift, $m=-2$ ⇒ $v[n]=e^{-j\frac{2\pi\cdot 2}{6}n}x[n]=e^{-j\frac{2\pi}{3}n}x[n]$.
> - $(-1)^k=e^{-j\pi k}=e^{-j\frac{2\pi\cdot 3}{6}k}$: time shift, $m=3$ ⇒ $y[n]=v[\langle n-3\rangle_6]$.
> - $y[n]=e^{-j\frac{2\pi}{3}(n-3)}x[\langle n-3\rangle_6]=e^{-j\frac{2\pi}{3}n}x[\langle n-3\rangle_6]$, with $x[\langle n-3\rangle_6]=\{4,5,6,1,2,3\}$:
>
> $$
> y[n]=\left\{\underset{\uparrow}{4},\ 5e^{-j\frac{2\pi}{3}},\ 6e^{j\frac{2\pi}{3}},\ 1,\ 2e^{-j\frac{2\pi}{3}},\ 3e^{j\frac{2\pi}{3}}\right\}
> $$

## 2. Midterm 2 quick check

> [!question] Q1 · a shift and a $(-1)^n$
> $x[n]=\{\underset{\uparrow}{1},\ 2,\ 3,\ 4,\ 5,\ 6\}$ has DFT $\{X_0,\dots,X_5\}$. Let $y[n]=(-1)^n\,x[\langle n-1\rangle_6]$. (a) Express $Y[k]$ through $X_0,\dots,X_5$. (b) Check $Y[0]$ two ways.

> [!success]- Answer
> - Delay: $v[n]=x[\langle n-1\rangle_6]\leftrightarrow e^{-j\frac{\pi k}{3}}X[k]$.
> - $(-1)^n$ shifts the DFT by $\frac N2=3$: $Y[k]=V[\langle k-3\rangle_6]=e^{-j\frac{\pi(k-3)}{3}}X[\langle k-3\rangle_6]=-e^{-j\frac{\pi k}{3}}X[\langle k-3\rangle_6]$:
> $$
> Y[k]=\left\{-X_3,\ -e^{-j\frac{\pi}{3}}X_4,\ -e^{-j\frac{2\pi}{3}}X_5,\ X_0,\ e^{-j\frac{\pi}{3}}X_1,\ e^{-j\frac{2\pi}{3}}X_2\right\}
> $$
> - (b) $y=\{6,-1,2,-3,4,-5\}$, $Y[0]=\sum_ny[n]=3$; also $-X_3=-\sum_n(-1)^nx[n]=-(-3)=3$.

> [!question] Q2 · True or false
> (a) A real length-6 signal can have $X[1]=2+j$ and $X[5]=2+j$. (b) If every $X[k]$ is real, $x[n]$ is real. (c) $x[n]=\{1,-1,1,-1\}$ has $\sum_k\lvert X[k]\rvert^2=16$.

> [!success]- Answer
> - (a) **False:** real $x$ gives $X[N-k]=X^*[k]$, so $X[5]=2-j$.
> - (b) **False:** $X=\{0,1,0,0\}$ gives $x[n]=\frac14e^{j\frac{\pi}{2}n}$. Real $X$ means $x[n]=x^*[\langle-n\rangle_N]$.
> - (c) **True:** Parseval, $\sum\lvert X\rvert^2=N\sum\lvert x\rvert^2=4\cdot4$; indeed $(-1)^n\leftrightarrow X=\{0,0,4,0\}$.

> [!trap]
> - Exponent sign sets direction: $e^{-j\frac{2\pi mk}{N}}$ delays $x$ by $m$; $e^{+j\frac{2\pi mn}{N}}$ moves $X$ right by $m$.
> - Shifts rotate: samples leaving one end re-enter at the other; length stays $N$.
> - $X[\langle -k\rangle_N]$ keeps $X[0]$ first; real $x$ gives $X[N-k]=X^*[k]$, so $X[0]$ and $X[\frac N2]$ are real.
> - Parseval carries the $\frac1N$ on the frequency side; windowing is a circular convolution of DFTs over $N$.

> [!exam] Midterm 2
> Fall 2026 MT2 (Wed Nov 4) covers this topic. Read a permuted or phase-ramped DFT list as shifts, modulation, reversal; prove a property. [[exams/midterm-2/past-exams/spring-2025|SP2025 #7(b), #8]] · [[exams/midterm-2/past-exams/fall-2024|FA2024 #8]] · [[exams/midterm-2/past-exams/fall-2023|FA2023 #7]] · [[exams/midterm-2/past-exams/spring-2023|SP2023 #9(b)]] · [[exams/midterm-2/past-exams/fall-2021|FA2021 #3(b)]] · [[exams/midterm-2/past-exams/spring-2021|SP2021 #4, #5]] · [[exams/midterm-2/past-exams/fall-2019|FA2019 #1(h), #4]] · [[exams/midterm-2/true-false-bank|T/F bank]] §6.

**Where it appears:** [[5-dft-and-fft/21-dft-properties|L21]] §3 (eqs. 25–29, Table 1, slides 14–15) · [[problems/circular-convolution-and-dft-properties|circular convolution and DFT properties]].

## Related
[[concepts/dft|DFT]] · [[concepts/circular-shift-and-reversal|circular shift and reversal]] · [[concepts/circular-convolution|circular convolution]] · [[concepts/dtft-properties|DTFT properties]]

### Sources for this page
Snyder, Lecture 21 notes §3 (eqs. 25–29, Table 1) and slides 14–15 (Example 3), Oct 19, 2026; past Midterm 2 exams.
