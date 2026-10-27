---
title: "Circular convolution and DFT properties"
description: "Midterm 2 DFT-property problems: y[n] from a phase ramp or a rearranged X[k], Y[k] of a reversed and shifted x[n], circular vs linear convolution and padding to N1+N2−1, conjugation, symmetry, Parseval."
tags: [problem-family, problem, dft, midterm-2]
family_frequency: "7 of 7 Midterm 2 exams"
typical_points: "5–18"
lectures: [21]
---

*Problem family · all seven past Midterm 2 exams · 5–18 points · [[5-dft-and-fft/21-dft-properties|Lecture 21]] · in the course: Lecture 21 Examples 1–3, the notes' circular convolution*

## What it looks like on the exam

- **A** $y[n]$ whose DFT is $e^{\pm j\frac{2\pi m}{N}k}X[k]$, possibly with a sign: a circular shift.
- **B** $y[n]$ whose DFT is a rearranged, sign-flipped list of the $X_k$: frequency shift (modulation) plus time shift.
- **C** $Y[k]$ in terms of the $X_k$ for a reversed and shifted $x[n]$.
- **D** Linear vs $N$-point circular convolution; the $N$ that makes them agree; zeros to pad.
- **E** Conjugation and symmetry: is $x$ real? two real DFTs from one complex DFT; Parseval.

Exams write $X_k$ or $X[m]$; $\langle n\rangle_N$ is $n$ mod $N$; $W_N=e^{-j\frac{2\pi}{N}}$.

| instance | given → asked |
|---|---|
| [[exams/midterm-2/past-exams/fall-2019\|FA2019]] #4 | $x=\{1,\dots,8\}$, $Y[k]=e^{-j\frac{\pi}{4}k}X[k]$ → $y[n]$ |
| FA2019 #11 | lengths 15 and 8 → zeros to pad each for linear convolution by DFT; by radix-2 FFT |
| FA2019 #1(g), (h) | T/F: linear convolution via circular + padding? circular convolution for any two lengths? |
| [[exams/midterm-2/past-exams/spring-2021\|SP2021]] #4 | $x=\{1,-2,3,-4,5,-6,7,-8\}$, $Y[k]=e^{-j(\frac{6\pi}{8}k+\pi)}X[k]$ → $y[n]$ |
| [[exams/midterm-2/past-exams/fall-2021\|FA2021]] #3(b) | $x=\{1,3,2,0,1,3,2,0\}$, $y[n]=x[\langle3-n\rangle_8]\,j^n$ → $Y[k]$ at $k=0,2,4,6$ |
| FA2021 #6 | $x=\{-2,3,0,3\}$, $h=\{-2,5,1,5,-3\}$ → $x*h$; 6-point $x\circledast h$; is $N=7$ enough? |
| [[exams/midterm-2/past-exams/spring-2023\|SP2023]] #9(b) | $x=\{1,2,-3,-4,5,6\}$, $Y=\{X_4,-X_5,X_0,-X_1,X_2,-X_3\}$ → $y[n]$ |
| [[exams/midterm-2/past-exams/fall-2023\|FA2023]] #7 | prove $b^*[n]\leftrightarrow B^*[N-k]$; $B^*[N]$; $X[k]$, $Y[k]$ of real $x$, $y$ from $Z=\mathrm{DFT}\{x+jy\}$ |
| [[exams/midterm-2/past-exams/fall-2024\|FA2024]] #8 | $x=\{3,0,-1,2,4\}$, $y=\{0,3,4,2,-1\}$ → $Y[k]$ in terms of $X_0,\dots,X_4$ |
| [[exams/midterm-2/past-exams/spring-2025\|SP2025]] #7(b) | $x=\{1,2,-3,-4,5,6,-2,2\}$, $Y=\{-X_5,X_6,-X_7,X_0,-X_1,X_2,-X_3,X_4\}$ → $y[n]$ |
| SP2025 #8 | $x=\{1,\dots,8\}$, $Y[m]=X[m]e^{j\frac{3\pi}{4}m}$ → $y[n]$ |
| course | Lecture 21 Example 2: $\{2,0,1,3,0\}\circledast\{4,1,0,2,2\}$ · Example 3: $x=\{1,\dots,6\}$, $Y=\{X_2,-X_3,X_4,-X_5,X_0,-X_1\}$ · [[exams/midterm-2/true-false-bank\|T/F bank]] Q41–Q42 |

> [!success]- Answers
> | instance | answer |
> |---|---|
> | FA2019 #4 | $e^{-j\frac{2\pi}{8}k\cdot1}$: delay 1, $y=x[\langle n-1\rangle_8]=\{8,1,2,3,4,5,6,7\}$ |
> | FA2019 #11 | $N\ge15+8-1=22$: DFT 7 and 14 zeros; FFT $N=32$: 17 and 24 |
> | FA2019 #1 | (g) T. (h) F (key): equal lengths, pad first |
> | SP2021 #4 | $e^{-j\pi}=-1$, $\frac{6\pi}{8}=\frac{2\pi\cdot3}{8}$: $y=-x[\langle n-3\rangle_8]=\{6,-7,8,-1,2,-3,4,-5\}$ |
> | FA2021 #3(b) | $Z[k]=W_8^{3k}X[\langle-k\rangle_8]$ (reverse, delay 3), $Y[k]=Z[\langle k-2\rangle_8]$ ($j^n=e^{j\frac{2\pi\cdot2}{8}n}$): $-6+2j$, $12$, $-6-2j$, $0$ |
> | FA2021 #6 | (a) $\{4,-16,13,-13,36,-6,15,-9\}$. (b) wrap $y[6],y[7]$ onto $n=0,1$: $\{19,-25,13,-13,36,-6\}$. (c) F: need $N\ge8$ |
> | SP2023 #9(b) | $Y[k]=(-1)^kX[\langle k-2\rangle_6]$: $y=e^{j\frac{2\pi}{3}n}x[\langle n-3\rangle_6]=\{-4,5e^{j\frac{2\pi}{3}},6e^{j\frac{4\pi}{3}},1,2e^{j\frac{2\pi}{3}},-3e^{j\frac{4\pi}{3}}\}$ |
> | FA2023 #7 | (a) conjugate the sum, insert $e^{-j2\pi n}$. (b) $B^*[0]$. (c) $X=\frac12(Z[k]+Z^*[N-k])$, $Y=\frac{1}{2j}(Z[k]-Z^*[N-k])$ |
> | FA2024 #8 | $y=x[\langle-(n-1)\rangle_5]$: $Y[k]=X[\langle-k\rangle_5]e^{-j\frac{2\pi k}{5}}=\{X_0,X_4e^{-j\frac{2\pi}{5}},X_3e^{-j\frac{4\pi}{5}},X_2e^{-j\frac{6\pi}{5}},X_1e^{-j\frac{8\pi}{5}}\}$ |
> | SP2025 #7(b) | $Y[m]=(-1)^{m+1}X[\langle m-3\rangle_8]$: $y=e^{j\frac{3\pi}{4}n}x[\langle n-4\rangle_8]=\{5,6e^{j\frac{3\pi}{4}},2j,2e^{j\frac{\pi}{4}},-1,2e^{-j\frac{\pi}{4}},-3j,4e^{j\frac{\pi}{4}}\}$ |
> | SP2025 #8 | $e^{+j\frac{2\pi\cdot3}{8}m}$: advance 3, $y=x[\langle n+3\rangle_8]=\{4,5,6,7,8,1,2,3\}$ |
> | course | Ex. 2: $\{10,10,10,17,7\}$ · Ex. 3: $Y=(-1)^kX[\langle k+2\rangle_6]$, $y=e^{-j\frac{2\pi}{3}n}x[\langle n-3\rangle_6]=\{4,5e^{-j\frac{2\pi}{3}},6e^{j\frac{2\pi}{3}},1,2e^{-j\frac{2\pi}{3}},3e^{j\frac{2\pi}{3}}\}$ |

## The recipe

> [!recipe] Properties, read in the right direction
> | $x[n]$ (length $N$) | $X[k]$ |
> |---|---|
> | $x[\langle n-m\rangle_N]$ | $e^{-j\frac{2\pi m}{N}k}X[k]$ |
> | $e^{j\frac{2\pi m}{N}n}x[n]$ | $X[\langle k-m\rangle_N]$ |
> | $\cos(\frac{2\pi m}{N}n)x[n]$ | $\frac12X[\langle k-m\rangle_N]+\frac12X[\langle k+m\rangle_N]$ |
> | $x[\langle-n\rangle_N]$ | $X[\langle-k\rangle_N]$ |
> | $x^*[n]$ | $X^*[\langle-k\rangle_N]$ |
> | $x\circledast h=\sum_mx[m]h[\langle n-m\rangle_N]$ | $X[k]H[k]$ |
> | $\sum\lvert x\rvert^2$ | $\frac1N\sum\lvert X\rvert^2$ |
> 1. **Phase ramp on $X[k]$.** Write it as $e^{-j\frac{2\pi}{N}km}$: $m\gt0$ delays, $e^{+j\dots}$ advances ($x[\langle n+m\rangle_N]=x[\langle n-(N-m)\rangle_N]$); a constant $e^{j\phi}$ scales every sample ($e^{-j\pi}=-1$). Shifts are circular: the list keeps its length and wraps.
> 2. **Rearranged $X_k$.** Find $m$ with $Y[k]=\pm X[\langle k-m\rangle_N]$, then read the sign pattern as a shift: $(-1)^k=e^{-j\frac{2\pi}{N}k\frac N2}$ delays by $\frac N2$. Build $y$ in that order: $V[k]=X[\langle k-m\rangle_N]$ is $v[n]=e^{j\frac{2\pi m}{N}n}x[n]$; $Y[k]=(-1)^kV[k]$ is $y[n]=v[\langle n-\frac N2\rangle_N]=(-1)^me^{j\frac{2\pi m}{N}n}x[\langle n-\frac N2\rangle_N]$ (the exponential picks up $(-1)^m$ from the shift). A pattern $(-1)^{k+1}$ adds one more minus. Test with $Y[0]=\sum y[n]$.
> 3. **Reversed and shifted $x$.** Match $y$ to $x[\langle\pm(n-m)\rangle_N]$: reversal keeps $x[0]$ in place, $\{x_0,x_{N-1},\dots,x_1\}$; then count the delay. $Y[k]=e^{-j\frac{2\pi m}{N}k}X[\langle-k\rangle_N]$; with $j^n$ or $(-1)^n$ attached, shift $k$ afterwards (FA2021 #3(b)).
> 4. **Circular convolution.** Pad both to the DFT length $N$. Either run the table with $h[\langle n-m\rangle_N]$ (periodically extended rows, each a circular shift of the reversed $h$), or compute the linear $y=x*h$ and wrap: $y_N[n]=\sum_ry[n+rN]$. Linear $=$ circular iff $N\ge N_1+N_2-1$; pad each to that $N$ (next power of 2 for a radix-2 FFT). Check $\sum y=\sum x\cdot\sum h$ either way.
> 5. **Symmetry.** $x$ real $\iff X[\langle-k\rangle_N]=X^*[k]$; $X[0]$, $X[\frac N2]$ real. Two real signals in one DFT: $z=x+jy$, $Z^*[\langle-k\rangle_N]\leftrightarrow z^*$, so $X=\frac12(Z[k]+Z^*[\langle-k\rangle_N])$, $Y=\frac{1}{2j}(Z[k]-Z^*[\langle-k\rangle_N])$ with $Z^*[N]=Z^*[0]$.
> 6. **Check** with $N$-periodicity ($Y[N]=Y[0]$), $Y[0]=\sum y[n]$, Parseval, and one sample from the inverse DFT.

> [!trap] Where the points go
> - **Sign of the ramp.** $e^{+j\frac{3\pi}{4}m}$ is an advance, $\{4,5,6,7,8,1,2,3\}$; the delay $\{6,7,8,1,2,3,4,5\}$ loses it (SP2025 #8). A linear shift giving nine samples $\{0,1,\dots,8\}$ is wrong (FA2019 #4).
> - **$X[\langle k-m\rangle_N]$ means $e^{+j\frac{2\pi m}{N}n}$**, not $e^{-j\dots}$ (SP2025 #7(b)).
> - **Alternating signs are a shift by $\frac N2$**, not a negation (SP2023 #9(b)); $e^{-j\pi}$ alone is the negation (SP2021 #4).
> - **Reversal keeps $x[0]$**: $\{x_0,x_4,x_3,x_2,x_1\}$ (FA2024 #8); it reverses $k$ as well (FA2021 #3(b)).
> - **Wrap, don't drop.** $y_6[0]=y[0]+y[6]$ (FA2021 #6(b)); $N=7\lt8$ still wraps $y[7]$; $N\ge N_1+N_2-1$, not $\max(N_1,N_2)$ (FA2019 #11).

## Practice problems

> [!question] Practice 1 — linear vs circular
> $x=\{\underset{\uparrow}{1},\ 2,\ 0,\ -1\}$, $h=\{\underset{\uparrow}{3},\ 1,\ 2\}$. (a) $x*h$. (b) The 4-point $x\circledast h$ (pad $h$ with one zero). (c) Smallest $N$ for which the $N$-point circular convolution equals $x*h$. (d) The 5-point circular convolution.

> [!success]- Solution
> **(a)** Length $4+3-1=6$: $x*h=\{\underset{\uparrow}{3},\ 7,\ 4,\ 1,\ -1,\ -2\}$; $\sum y=12=2\cdot6$.
> **(b)** Wrap $y[4]=-1$ onto $n=0$ and $y[5]=-2$ onto $n=1$: $\{\underset{\uparrow}{2},\ 5,\ 4,\ 1\}$ (sum still 12).
> **(c)** $N=6$.
> **(d)** Only $y[5]=-2$ wraps, onto $n=0$: $\{\underset{\uparrow}{1},\ 7,\ 4,\ 1,\ -1\}$.

> [!question] Practice 2 — four rearrangements of one DFT
> $x=\{\underset{\uparrow}{4},\ 1,\ -2,\ 0,\ 3,\ 2,\ -1,\ 5\}$, $N=8$, DFT $\{X_0,\dots,X_7\}$. Find $y[n]$ when (a) $Y[k]=e^{j\frac{\pi}{2}k}X[k]$; (b) $Y[k]=X[\langle k-4\rangle_8]$; (c) $Y[k]=\{X_6,-X_7,X_0,-X_1,X_2,-X_3,X_4,-X_5\}$. (d) Now $y[n]=x[\langle2-n\rangle_8]$: write $Y[k]$ as a list in the $X_i$.

> [!success]- Solution
> **(a)** $e^{j\frac{2\pi\cdot2}{8}k}$: advance 2, $y=x[\langle n+2\rangle_8]=\{\underset{\uparrow}{-2},\ 0,\ 3,\ 2,\ -1,\ 5,\ 4,\ 1\}$.
> **(b)** $y=e^{j\frac{2\pi\cdot4}{8}n}x[n]=(-1)^nx[n]=\{\underset{\uparrow}{4},\ -1,\ -2,\ 0,\ 3,\ -2,\ -1,\ -5\}$.
> **(c)** $Y[k]=(-1)^kX[\langle k-2\rangle_8]$. $(-1)^k$: delay 4, $v=x[\langle n-4\rangle_8]=\{3,2,-1,5,4,1,-2,0\}$; $\langle k-2\rangle$: times $e^{j\frac{\pi}{2}n}=j^n$:
> $$
> y[n]=j^n\,x[\langle n-4\rangle_8]=\{\underset{\uparrow}{3},\ 2j,\ 1,\ -5j,\ 4,\ j,\ 2,\ 0\}.
> $$
> Check: $Y[0]=X_6=X_d(-\frac{\pi}{2})=\sum x[n]j^n=(4+2+3+1)+j(1+2-5)=10-2j$, and $\sum y[n]=3+2j+1-5j+4+j+2=10-2j$.
> **(d)** $x[\langle2-n\rangle_8]=x[\langle-(n-2)\rangle_8]$: reverse, delay 2: $Y[k]=e^{-j\frac{\pi}{2}k}X[\langle-k\rangle_8]=\{X_0,\ -jX_7,\ -X_6,\ jX_5,\ X_4,\ -jX_3,\ -X_2,\ jX_1\}$. ($y=\{-2,1,4,5,-1,2,3,0\}$.)

> [!question] Practice 3 — symmetry, Parseval, two for one
> (a) $X[k]=\{3,\ 1+j,\ -2j,\ 5,\ 2j,\ 1-j\}$, $N=6$: is $x$ real? (b) $x[0]$. (c) $\sum_n\lvert x[n]\rvert^2$. (d) $z=x+jy$ with $x,y$ real, $N=4$, $Z[k]=\{2+2j,\ 1+j,\ 3,\ -1-j\}$: find $X[k]$, $Y[k]$, then $x$ and $y$.

> [!success]- Solution
> **(a)** $X[5]=X^*[1]$, $X[4]=X^*[2]$, $X[0]$, $X[3]$ real: yes.
> **(b)** $x[0]=\frac16\sum X[k]=\frac{10}{6}=\frac53$ (imaginary parts cancel).
> **(c)** $\frac16\sum\lvert X[k]\rvert^2=\frac{9+2+4+25+4+2}{6}=\frac{23}{3}$.
> **(d)** $Z^*[\langle-k\rangle_4]=\{2-2j,\ -1+j,\ 3,\ 1-j\}$. $X=\frac12(Z+Z^*[\langle-k\rangle])=\{2,\ j,\ 3,\ -j\}$, $Y=\frac{1}{2j}(Z-Z^*[\langle-k\rangle])=\{2,\ -j,\ 0,\ j\}$, both Hermitian. Inverse DFTs: $x[n]=\frac14\left(2+3(-1)^n-2\sin\frac{\pi n}{2}\right)=\{\frac54,\ -\frac34,\ \frac54,\ \frac14\}$, $y[n]=\frac14\left(2+2\sin\frac{\pi n}{2}\right)=\{\frac12,\ 1,\ \frac12,\ 0\}$. Check: $\mathrm{DFT}\{x+jy\}[0]=\sum x+j\sum y=2+2j=Z[0]$.

## Related

[[concepts/dft-properties|DFT properties]] · [[concepts/circular-shift-and-reversal|circular shift]] · [[concepts/circular-convolution|circular convolution]] · [[concepts/dft|DFT]] · [[concepts/zero-padding|zero padding]] · [[problems/dft-values-and-zero-padding|DFT values and zero padding]] · [[problems/finite-length-convolution|finite-length convolution]] · [[exams/midterm-2/index|Midterm 2]]

### Sources for this page

Lecture 21 notes (eqs. 14–16, 19, 25–29, Table 1) and slides (Examples 1–3); past Midterm 2 exams FA2019–SP2025 with keys. Practice problems are new (verified numerically).
