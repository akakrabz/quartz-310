---
title: "DFT values and zero padding"
description: "Midterm 2 DFT questions: X[0], X[N/2] or one bin from the definition, the DFT as DTFT samples X[k] = X_d(2πk/N), which padded bin equals X[k], the inverse DFT, bins in hertz."
tags: [problem-family, problem, dft, midterm-2]
family_frequency: "7 of 7 Midterm 2 exams"
typical_points: "6–15"
lectures: [20]
---

*Problem family · all seven past Midterm 2 exams · 6–15 points, plus two or three True/False items · [[5-dft-and-fft/20-discrete-fourier-transform|Lecture 20]] · in the course: Lecture 20 Exercise 1, slide Examples 1–2*

## What it looks like on the exam

- **A** $X[0]$, $X[N/2]$ or one bin $X[k]$ from the definition, for a short list $x[n]$.
- **B** The DFT as DTFT samples: $X[k]=X_d\!\left(\frac{2\pi k}{N}\right)$; which bin holds a given $\omega$; smallest $N$.
- **C** Zero padding: which $Z[k]$ of the padded signal equals $X[k]$; conjugates for real $x$.
- **D** Inverse DFT: $x[0]=\frac1N\sum_kX[k]$; the result is $N$-periodic; is $x$ real?
- **E** Bins in hertz: $f_k=\frac{k f_s}{N}$, upper half negative, spacing $\frac{f_s}{N}$.

Exams write $X_k$ or $X[m]$ for $X[k]$, $\{x[n]\}_{n=0}^{N-1}$ for a length-$N$ signal.

| instance | given → asked |
|---|---|
| [[exams/midterm-2/past-exams/fall-2019\|FA2019]] #2 | $f_s=40$ kHz, $N=1000$ → Hz of bins $k=300$, $800$; bin spacing |
| FA2019 #1(a), (i) | T/F: padding changes the DTFT? $X[0]=0$ for $\{1,-1,-2,3,4,-3\}$? |
| [[exams/midterm-2/past-exams/spring-2021\|SP2021]] #5 | 7-point $X[k]=\{-2,-4j,3,5,3,4j,-2j\}$ → is $x$ real? |
| SP2021 #6 | three descriptions → CTFT, DTFT or DFT |
| SP2021 #1(c), (e) | T/F: $X[0]$ real for real $x$? $X[0]=0$ for $\{1,-1,6,7,9,-6,-7,9\}$? |
| [[exams/midterm-2/past-exams/fall-2021\|FA2021]] #3(a) | $x=\{1,3,2,0,1,3,2,0\}$ → $X[k]$ at $k=0,2,4,6$ |
| FA2021 #1(b), (d) | T/F: two sequences, one DFT? length 20 padded to 32: $X[10]=Y[16]$? |
| [[exams/midterm-2/past-exams/spring-2023\|SP2023]] #9(a), (c) | $x=\{1,2,-3,-4,5,6\}$ → $X_0$, $X_3$; padded with 24 zeros: which of $X[0]=Z[0]$, $X[1]=Z[4]$, $X[2]=Z[10]$, $X[1]=Z^*[25]$, $X[2]=Z^*[22]$ |
| SP2023 #1(c), (d) | T/F: padding keeps $X_d$? inverse DFT of $\{1,2,3,4\}$ zero outside $0\le n\le3$? |
| [[exams/midterm-2/past-exams/fall-2023\|FA2023]] #1(f), (h) | T/F: padding keeps $X_d$? length 14: $X[11]=X_d(-\frac{3\pi}{7})$? |
| FA2023 #7(a), (b) | prove $b^*[n]\leftrightarrow B^*[N-k]$ from the definition; $B^*[N]$ ((c): [[problems/circular-convolution-and-dft-properties\|properties family]]) |
| [[exams/midterm-2/past-exams/fall-2024\|FA2024]] #6 | $f_s=1000$ Hz, $N=1024$, aliasing allowed → all analog Hz in bin $k$ |
| FA2024 #7 | DFT must contain $X_d(\frac{2\pi}{5})$ and $X_d(\frac{\pi}{3})$ → smallest $N$ |
| FA2024 #1(d) | T/F with reason: padded to $2N$: $X[k]=Y[2k]$ and $X_d=Y_d$? |
| [[exams/midterm-2/past-exams/spring-2025\|SP2025]] #7(a), (c) | $x=\{1,2,-3,-4,5,6,-2,2\}$ → $X_0$; padded with 52 zeros: which of $X[0]=Z[0]$, $X[1]=Z[1]$, $X[7]=Z[59]$, $X[2]=Z[15]$, $X[4]=Z^*[30]$, $X[6]=Z^*[15]$ |
| SP2025 #1(a), (b), (d) | T/F: inverse DTFT vs inverse DFT of $\{1,2,3,4\}$; padded to $3N$: $X_d(\omega)=Y_d(3\omega)$? |
| course | Lecture 20 Exercise 1: length 16 padded to 64, which $\tilde X[k]$ equal $X[1]$, $X[9]$ · slide Example 2: smallest $N$ holding $X_d(\frac{\pi}{5})$, $X_d(\frac{\pi}{3})$ · [[exams/midterm-2/true-false-bank\|T/F bank]] Q12–Q17, Q30–Q36 |

> [!success]- Answers
> | instance | answer |
> |---|---|
> | FA2019 #2 | $\omega_k=\frac{2\pi k}{N}$, $f=\frac{\omega}{2\pi}f_s$: $k=300\to12$ kHz; $k=800$: $\frac{8\pi}{5}\equiv-\frac{2\pi}{5}\to-8$ kHz. Spacing $\frac{f_s}{N}=40$ Hz |
> | FA2019 #1 | (a) F: zeros add nothing to $\sum x[n]e^{-j\omega n}$. (i) F: $X[0]=\sum x[n]=2$ |
> | SP2021 #5 | Not real: $x[0]=\frac17\sum X[k]=\frac{9-2j}{7}$; also $X[1]=-4j\ne X^*[6]=2j$ |
> | SP2021 #6 | (a) DTFT (unit circle in the ROC); (b) DFT; (c) CTFT |
> | SP2021 #1 | (c) T. (e) F: $X[0]=18$ |
> | FA2021 #3(a) | $x[n+4]=x[n]$: $X[k]=(1+(-1)^k)(1+3e^{-j\frac{\pi}{4}k}+2e^{-j\frac{\pi}{2}k})$: $12$, $-2-6j$, $0$, $-2+6j$ |
> | FA2021 #1 | (b) F: invertible. (d) T: both are $X_d(\pi)$ |
> | SP2023 #9 | (a) $X_0=7$, $X_3=\sum(-1)^nx[n]=-1$. (c) $Z[k]=X_d(\frac{2\pi k}{30})$, $X[k]=Z[5k]$: i, iii true; ii false ($Z[5]$); iv true ($Z[25]=X_d(-\frac{\pi}{3})=X^*[1]$); v false ($Z^*[20]$) |
> | SP2023 #1 | (c) T. (d) F: $x[4]=x[0]=2.5$ |
> | FA2023 #1 | (f) T. (h) T: $X[11]=X_d(\frac{11\pi}{7})=X_d(\frac{11\pi}{7}-2\pi)$ |
> | FA2023 #7(a), (b) | conjugate the sum, insert $e^{-j2\pi n}=1$, read off $B^*[N-k]$; $B^*[N]=B^*[0]$ ($N$-periodic) |
> | FA2024 #6 | $\frac{2\pi f}{f_s}=\frac{2\pi k}{N}+2\pi m$: $f=\frac{1000k}{1024}+1000m$ Hz, $m\in\mathbb Z$ |
> | FA2024 #7 | $\frac{N}{5}$ and $\frac{N}{6}$ integers: $N=\mathrm{lcm}(5,6)=30$, bins 6 and 5 |
> | FA2024 #1(d) | T: $Y_d=X_d$; $Y[2k]=X_d(\frac{2\pi\cdot2k}{2N})=X[k]$ |
> | SP2025 #7 | (a) $X_0=7$. (c) $X[k]=Z[\frac{60}{8}k]$ only when integer: i, iv ($Z[15]=X_d(\frac{\pi}{2})$), v ($X[4]=X_d(\pi)$ real), vi ($X[6]=X_d(-\frac{\pi}{2})=Z^*[15]$); ii, iii false |
> | SP2025 #1 | (a) T: inverse DTFT of a finite sum is finite. (b) F: periodic, $x[4]=x[0]=\frac52$. (d) F: $Y_d=X_d$ ($X_d(3\omega)$ is zeros between samples) |
> | course | Ex. 1: $X[1]=\tilde X[4]$, $X[9]=\tilde X[36]$ · slide Ex. 2: $\frac{N}{10},\frac{N}{6}$ integers: $N=30$, then $60$ |

## The recipe

> [!recipe] DFT values in six moves
> $$
> \begin{gathered}
> X[k]=\sum_{n=0}^{N-1}x[n]e^{-j\frac{2\pi k}{N}n}=X_d\!\left(\frac{2\pi k}{N}\right),\\
> x[n]=\frac1N\sum_{k=0}^{N-1}X[k]e^{j\frac{2\pi k}{N}n},\qquad W_N=e^{-j\frac{2\pi}{N}}.
> \end{gathered}
> $$
> 1. **Special bins.** $X[0]=\sum_nx[n]$; $X[\frac N2]=\sum_n(-1)^nx[n]$ ($N$ even); $X[\frac N4]=\sum_n(-j)^nx[n]$. Both $X[0]$ and $X[\frac N2]$ are real for real $x$. Any bin: multiply $x[n]$ by $W_N^{kn}$, reducing $kn$ mod $N$; a repeating $x$ factors (FA2021 #3(a)).
> 2. **Bins are DTFT samples.** $\omega_k=\frac{2\pi k}{N}$, $0\le k\lt N$. Bins past $\frac N2$ sit at $\omega_k-2\pi\lt0$: $X[N-k]=X_d(-\omega_k)=X^*[k]$ for real $x$. $X_d(\omega_0)$ is in the DFT iff $\frac{\omega_0N}{2\pi}$ is an integer; two frequencies $\frac{2\pi p_i}{q_i}$ need $N$ a multiple of every $q_i$: smallest $N=\mathrm{lcm}$.
> 3. **Zero padding.** $L$ zeros make $M=N+L$ bins of the same $X_d$: $\tilde X[k]=X_d(\frac{2\pi k}{M})$, spacing $\frac{2\pi}{M}$. $X[k]=\tilde X[\frac{kM}{N}]$ when $\frac{kM}{N}$ is an integer, nothing else matches; odd bins of a $2N$-padding are new. The DTFT never changes.
> 4. **Inverse DFT.** $x[0]=\frac1N\sum_kX[k]$; one bin $X[k_0]=N$ gives $e^{j\frac{2\pi k_0}{N}n}$; the formula returns $x[n+N]=x[n]$, so "$x[n]=0$ outside $0\le n\le N-1$" is false for an inverse DFT and true for an inverse DTFT of a finite sum.
> 5. **Real or not.** $x$ real $\iff X[\langle-k\rangle_N]=X^*[k]$ for every $k$; check the pairs $k\leftrightarrow N-k$, or compute $x[0]$. A real $X[0]$ alone proves nothing.
> 6. **Hertz.** $f_k=\frac{kf_s}{N}$ for $k\le\frac N2$, $\frac{(k-N)f_s}{N}$ above; spacing $\frac{f_s}{N}$; record length $NT=\frac{N}{f_s}$. With aliasing: $f=\frac{kf_s}{N}+mf_s$. Check: Parseval $\sum\lvert x\rvert^2=\frac1N\sum\lvert X\rvert^2$; $X[0]$ real.

> [!trap] Where the points go
> - **Upper half is negative frequency.** $k=800$ of 1000 at 40 kHz is $-8$ kHz, not 32 kHz (FA2019 #2); $k=25$ of 30 is $-\frac{\pi}{3}$ (SP2023 #9(c)).
> - **Padding changes the DFT, never the DTFT.** $X[1]=Z[1]$ fails (SP2025 #7(c) ii); $X_d(\omega)=Y_d(3\omega)$ is false (SP2025 #1(d)); $X[k]=Z[k\frac MN]$ needs an integer index.
> - **Inverse DFT is periodic.** $x[4]=x[0]=2.5$ for $\{1,2,3,4\}$ (SP2023 #1(d), SP2025 #1(b)); the inverse DTFT of the same four terms is finite (SP2025 #1(a)).
> - **Smallest $N$ is an lcm.** $N=15$ puts $\frac{\pi}{3}$ at $k=2.5$ (FA2024 #7).
> - **Real $X[0]$ proves nothing** (SP2021 #5): compare $X[k]$ with $X^*[N-k]$.

## Practice problems

> [!question] Practice 1 — bins from the definition and from padding
> $x[n]=\{\underset{\uparrow}{2},\ -1,\ 3,\ 0,\ 1,\ -2,\ 4,\ 1\}$, $N=8$, DFT $X[k]$. (a) $X[0]$, $X[4]$. (b) $X[2]$ and $X[6]$. (c) $z[n]$ is $x[n]$ padded with 24 zeros, DFT $Z[k]$: which $Z[k]$ equal $X[1]$, $X[5]$? Is $X[3]=Z^*[20]$? Is $X[3]=Z[3]$? (d) Smallest $N'$ whose DFT of a length-$N'$ signal contains both $X_d(\frac{3\pi}{4})$ and $X_d(\frac{\pi}{5})$.

> [!success]- Solution
> **(a)** $X[0]=\sum x[n]=8$; $X[4]=\sum(-1)^nx[n]=2+1+3-0+1+2+4-1=12$.
> **(b)** $X[2]=\sum x[n]\,(-j)^n=(2-3+1-4)+j(1+2+1)=-4+4j$; real $x$: $X[6]=X^*[2]=-4-4j$.
> **(c)** $Z[k]=X_d(\frac{2\pi k}{32})$, $X[k]=X_d(\frac{2\pi k}{8})=Z[4k]$: $X[1]=Z[4]$, $X[5]=Z[20]$. $Z^*[20]=X_d^*(\frac{5\pi}{4})=X_d^*(-\frac{3\pi}{4})=X_d(\frac{3\pi}{4})=X[3]$: yes. $Z[3]=X_d(\frac{3\pi}{16})\ne X[3]$.
> **(d)** $\frac{3\pi}{4}=\frac{2\pi k}{N'}$ needs $\frac{3N'}{8}$ integer ($8\mid N'$); $\frac{\pi}{5}$ needs $\frac{N'}{10}$ integer: $N'=\mathrm{lcm}(8,10)=40$, bins $k=15$ and $4$.
> Check: $\sum x^2=36$, $\frac18\sum\lvert X\rvert^2=\frac{288}{8}=36$.

> [!question] Practice 2 — bins in hertz
> $x_c(t)$ is sampled at $f_s=8$ kHz and $N=400$ samples are taken. (a) Bin spacing in Hz and record length. (b) Analog frequency of bins $k=50$, $250$, $399$. (c) Which bin holds 1.2 kHz? Which bins light up for $x_c(t)=3\cos(2\pi\cdot3000t)$, and how tall? (d) If $x_c$ is not bandlimited, every analog frequency that lands in bin 50.

> [!success]- Solution
> **(a)** $\frac{f_s}{N}=20$ Hz; $NT=50$ ms.
> **(b)** $f_k=\frac{kf_s}{N}$ reduced to $(-\frac{f_s}{2},\frac{f_s}{2}]$: $k=50\to1000$ Hz; $k=250\to5000-8000=-3000$ Hz; $k=399\to-20$ Hz.
> **(c)** $\frac{1200}{20}=60$: $k=60$. 3 kHz $\to\omega=\frac{3\pi}{4}=\frac{2\pi\cdot150}{400}$: bins 150 and 250, each $\frac{AN}{2}=600$; whole periods (150 cycles), every other bin 0.
> **(d)** $\frac{2\pi f}{8000}=\frac{2\pi\cdot50}{400}+2\pi m$: $f=1000+8000m$ Hz: $\dots,-7000,1000,9000,17000,\dots$

> [!question] Practice 3 — inverse DFT
> $X[k]=\{6,\ 0,\ 3,\ 0,\ 3,\ 0\}$, $N=6$. (a) $x[n]$ in closed form and as a list. (b) $x[0]$ from $X$ alone; $x[6]$ and $x[-1]$. (c) Is $x$ real, without computing it? (d) $x$ is padded to length 12, DFT $\tilde X[k]$: $\tilde X[0]$, $\tilde X[4]$, $\tilde X[6]$, $\tilde X[8]$; and $\tilde X[3]$.

> [!success]- Solution
> **(a)** $x[n]=\frac16\left(6+3e^{j\frac{2\pi}{3}n}+3e^{-j\frac{2\pi}{3}n}\right)=1+\cos\!\left(\frac{2\pi}{3}n\right)$: $\{\underset{\uparrow}{2},\ \frac12,\ \frac12,\ 2,\ \frac12,\ \frac12\}$.
> **(b)** $x[0]=\frac{6+3+3}{6}=2$. The inverse DFT is 6-periodic: $x[6]=x[0]=2$, $x[-1]=x[5]=\frac12$.
> **(c)** Yes: $X[0]$, $X[3]$ real and $X[4]=X^*[2]$, $X[5]=X^*[1]$.
> **(d)** $\tilde X[2k]=X[k]$: $6$, $3$, $0$, $3$. $\tilde X[3]=X_d(\frac{\pi}{2})=\sum x[n]\,(-j)^n=(2-\frac12+\frac12)+j(-\frac12+2-\frac12)=2+j$, a new sample of the same DTFT.

## Related

[[concepts/dft|DFT]] · [[concepts/zero-padding|zero padding]] · [[concepts/dft-properties|DFT properties]] · [[concepts/dtft|DTFT]] · [[problems/circular-convolution-and-dft-properties|circular convolution and DFT properties]] · [[problems/dft-spectral-analysis|DFT spectral analysis]] · [[problems/dtft-and-inverse-dtft|DTFT and inverse DTFT]] · [[exams/midterm-2/index|Midterm 2]]

### Sources for this page

Lecture 20 notes (eqs. 8–9, 12, 20–25, Exercise 1) and slides 11–13; past Midterm 2 exams FA2019–SP2025 with keys. Practice problems are new (verified numerically).
