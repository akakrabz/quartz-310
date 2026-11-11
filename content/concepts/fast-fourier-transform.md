---
title: "Fast Fourier transform (FFT)"
description: "The FFT computes the same DFT in N log2 N instead of N² multiply-adds: the twiddle factor, the radix-2 decimation-in-time merging equations X[k] = A[k] ± W_N^k B[k], the recursion on N = 4 and N = 8, and why the cost is N log N."
tags: [concept, dft, fft]
aliases: ["FFT", "fast Fourier transform", "decimation in time", "DIT FFT", "radix-2 FFT", "merging equations", "divide and conquer", "big O notation", "cost of the DFT", "N log N"]
---

*Lecture 25 (Wed Oct 28: cost · Fri Oct 30: twiddle factor, derivation, start of Example 1 · Fri Nov 6: Examples 1–2, cost per stage, code demo) §1–2.1 · [[homework/hw10|HW10]] #1 · pictures: [[concepts/butterfly-diagram|butterfly diagram]] · first topic after Midterm 2*

> [!abstract] In one breath
> - The FFT is **not a new transform**. It is a faster way to compute the same $X[k]$: $N\log_2N$ multiply-adds instead of $N^2$.
> - Radix-2 decimation in time: split $x[n]$ into its even and odd samples, take the two half-length DFTs $A[k]$ and $B[k]$, and merge them: $X[k]=A[k]+W_N^kB[k]$, $X[k+\frac N2]=A[k]-W_N^kB[k]$.
> - Keep splitting down to length 1 (a length-1 sequence is its own DFT), then merge back up: $\log_2N$ stages, $N$ multiply-adds each.

## 1. What the DFT costs when computed directly (§1)

> [!key] Cost of the DFT sum (Lecture 25, eqs. 1–3)
> $$
> X[k]=\sum_{n=0}^{N-1}x[n]\,e^{-j\frac{2\pi k}{N}n},\qquad 0\le k\le N-1.
> $$
> - One **multiply-add** = multiply $x[n]$ by a complex exponential and add it to the running sum. This is the unit of cost.
> - One value of $k$ needs $N$ multiply-adds, and there are $N$ values of $k$: $N\cdot N=N^2$ in total, written $O(N^2)$, "on the order of $N^2$".
> - Big-O keeps only the fastest-growing term and drops constant factors: $8N^3+20N^2+N=O(N^3)$, $N\log N+N=O(N\log N)$. Nothing more about big-O is needed in this course.
> - Computing the [[concepts/dft|DFT]] as a matrix times a vector is also $O(N^2)$; it is faster only by a constant factor.
>
> | $N$ | DFT sum: $N^2$ | FFT: $N\log_2N$ | ratio |
> |---|---|---|---|
> | 16 | 256 | 64 | 4 |
> | 1024 | 1 048 576 | 10 240 | about 100 |
> | $10^5$ (10 s of audio at 8 kHz, rounded up) | $10^{10}$ | $1.7\times10^{6}$ | about 6000 |

> [!lecture] In lecture — L25, Oct 28
> "This is not a new transform … no new tables, no new pairs and properties." Ten seconds at 8 kHz is 80,000 samples, about $10^5$: $N^2=10^{10}$ against $N\log N\approx17\times10^5$, which he rounded to four orders of magnitude. Streamed music has tens of millions of samples: "take 10 million, which is $10^7$, and square it. That's $10^{14}$." So the FFT matters "not just because, oh hey, it's more efficient": it "crossed over from something being impossible to now being feasible."

## 2. The twiddle factor (slide 5)

> [!key] Twiddle factor (Lecture 25, eqs. 4–5)
> $$
> W=e^{-j2\pi},\qquad W_N=e^{-j\frac{2\pi}{N}},\qquad W_N^{k}=e^{-j\frac{2\pi k}{N}}.
> $$
> The subscript **divides** the $2\pi$ in the exponent, the superscript **multiplies** it. $W_N^k$ is the point on the unit circle $k$ steps of $\frac{2\pi}{N}$ clockwise from 1. The DFT becomes $X[k]=\sum_{n=0}^{N-1}x[n]\,W_N^{kn}$.
>
> Three facts used all the time:
> - $W_N^{2kn}=W_{N/2}^{kn}$ (eq. 11): doubling the superscript is the same as halving the subscript.
> - $W_N^{k+N/2}=-W_N^{k}$, because $e^{-j\pi}=-1$: half a turn flips the sign.
> - $W_N^{0}=1$; $W_4^{1}=W_8^{2}=W_{16}^{4}=-j$.

## 3. Decimation in time: the merging equations (§2.1)

The idea is to build a length-$N$ DFT out of two length-$\frac N2$ DFTs. Take $N$ even and split $x[n]$ by index: $a[n]=x[2n]$ (even samples), $b[n]=x[2n+1]$ (odd samples), with DFTs $A[k]$ and $B[k]$ of length $\frac N2$.

> [!key] Merging equations (Lecture 25, eqs. 16–17)
> $$
> \begin{aligned}
> X[k]&=A[k]+W_N^{k}\,B[k],\\
> X\!\left[k+\tfrac N2\right]&=A[k]-W_N^{k}\,B[k],
> \end{aligned}
> \qquad 0\le k\le\tfrac N2-1.
> $$
> - Two half-length DFTs in, one full-length DFT out. Each $k$ produces **two** outputs, $X[k]$ and $X[k+\frac N2]$, from the same product $W_N^kB[k]$: compute it once, add it and subtract it.
> - The subscript of the twiddle factor is the length you are merging **to**.

> [!derivation]- Where the merging equations come from (eqs. 6–17)
> Split the DFT sum into even and odd $n$ and use $W_N^{2kn}=W_{N/2}^{kn}$:
> $$
> \begin{aligned}
> X[k]&=\sum_{n=0}^{N-1}x[n]\,W_N^{kn}=\sum_{m=0}^{\frac N2-1}x[2m]\,W_N^{k(2m)}+\sum_{m=0}^{\frac N2-1}x[2m+1]\,W_N^{k(2m+1)}\\
> &=\sum_{n=0}^{\frac N2-1}a[n]\,W_{N/2}^{kn}+W_N^{k}\sum_{n=0}^{\frac N2-1}b[n]\,W_{N/2}^{kn}=A[k]+W_N^{k}\,B[k].
> \end{aligned}
> $$
> $A[k]$ and $B[k]$ are length-$\frac N2$ DFTs, so they are only defined for $0\le k\le\frac N2-1$, but like every DFT they repeat: $A[k+\frac N2]=A[k]$, $B[k+\frac N2]=B[k]$ (eqs. 14–15). For the second half of the outputs replace $k$ by $k+\frac N2$:
> $$
> X\!\left[k+\tfrac N2\right]=A[k]+W_N^{k+N/2}\,B[k]=A[k]-W_N^{k}\,B[k],
> $$
> since $W_N^{k+N/2}=e^{-j\frac{2\pi k}{N}}e^{-j\pi}=-W_N^k$.

> [!lecture] In lecture — L25, Oct 30
> "Decimation" comes from the Latin for ten, the Roman practice of removing one in ten; here "when we decimate we are reducing the size of something by discarding some number of samples", every other one. The FFT is "an example of what we like to call a divide and conquer algorithm." On the derivation: "I am not showing you this because you need to reproduce this derivation," but because handing over only the final equations "robs you of any potential intuition." Asked on Nov 6 why there are two equations: "It just saves us a little bit of extra computation … we can compute one twiddle factor once and use it twice."

## 4. The algorithm, on $N=4$ and $N=8$

> [!recipe] Radix-2 decimation-in-time FFT (slide 9)
> 1. **Split** $x[n]$ into even-index and odd-index samples. Split each half the same way, and again, until every piece has length 1. Draw the tree so you know later which pieces belong together.
> 2. **Base case:** a length-1 sequence is its own DFT. (Its only bin is $k=0$, the sum of the one sample: $\{2\}\leftrightarrow\{2\}$.) Nothing to compute.
> 3. **Merge** the two pieces that came from the same split. Merging two length-$\frac L2$ DFTs $A$, $B$ into a length-$L$ DFT $C$:
> $$
> C[k]=A[k]+W_L^{k}B[k],\qquad C\!\left[k+\tfrac L2\right]=A[k]-W_L^{k}B[k],\qquad 0\le k\le\tfrac L2-1.
> $$
> 4. Repeat step 3 with $L=2,4,8,\dots$ until $L=N$.
>
> "Radix 2" = the signal is halved each time, so $N$ must be a power of 2.

<figure class="ece-fig"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 660 262" width="660" height="262" role="img" aria-label="splitting a length-8 signal into even and odd samples three times" style="font-family:'Source Sans 3','Source Sans Pro',system-ui,sans-serif;font-size:13px"><defs><marker id="ah-fft-split-tree" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="context-stroke"/></marker></defs><rect x="175.0" y="16.0" width="310.0" height="28.0" fill="none" rx="4" stroke="currentColor" stroke-width="1.2"/><text x="330.0" y="34.5" text-anchor="middle" fill="currentColor" style="font-size:13px;">x[n] = { x₀, x₁, x₂, x₃, x₄, x₅, x₆, x₇ }</text><line x1="330.0" y1="44.0" x2="170.0" y2="80.0" stroke="currentColor" stroke-width="1.2" stroke-linecap="round"/><rect x="52.0" y="80.0" width="236.0" height="28.0" fill="none" rx="4" stroke="currentColor" stroke-width="1.2"/><text x="170.0" y="98.5" text-anchor="middle" fill="currentColor" style="font-size:13px;">a[n] = { x₀, x₂, x₄, x₆ }</text><line x1="330.0" y1="44.0" x2="490.0" y2="80.0" stroke="currentColor" stroke-width="1.2" stroke-linecap="round"/><rect x="372.0" y="80.0" width="236.0" height="28.0" fill="none" rx="4" stroke="currentColor" stroke-width="1.2"/><text x="490.0" y="98.5" text-anchor="middle" fill="currentColor" style="font-size:13px;">b[n] = { x₁, x₃, x₅, x₇ }</text><text x="228.0" y="66.0" text-anchor="end" fill="var(--muted)" style="font-size:11px;">even n</text><text x="432.0" y="66.0" text-anchor="start" fill="var(--muted)" style="font-size:11px;">odd n</text><line x1="170.0" y1="108.0" x2="90.0" y2="144.0" stroke="currentColor" stroke-width="1.2" stroke-linecap="round"/><rect x="24.0" y="144.0" width="132.0" height="28.0" fill="none" rx="4" stroke="currentColor" stroke-width="1.2"/><text x="90.0" y="162.5" text-anchor="middle" fill="currentColor" style="font-size:13px;">c = { x₀, x₄ }</text><line x1="170.0" y1="108.0" x2="250.0" y2="144.0" stroke="currentColor" stroke-width="1.2" stroke-linecap="round"/><rect x="184.0" y="144.0" width="132.0" height="28.0" fill="none" rx="4" stroke="currentColor" stroke-width="1.2"/><text x="250.0" y="162.5" text-anchor="middle" fill="currentColor" style="font-size:13px;">d = { x₂, x₆ }</text><line x1="490.0" y1="108.0" x2="410.0" y2="144.0" stroke="currentColor" stroke-width="1.2" stroke-linecap="round"/><rect x="344.0" y="144.0" width="132.0" height="28.0" fill="none" rx="4" stroke="currentColor" stroke-width="1.2"/><text x="410.0" y="162.5" text-anchor="middle" fill="currentColor" style="font-size:13px;">e = { x₁, x₅ }</text><line x1="490.0" y1="108.0" x2="570.0" y2="144.0" stroke="currentColor" stroke-width="1.2" stroke-linecap="round"/><rect x="504.0" y="144.0" width="132.0" height="28.0" fill="none" rx="4" stroke="currentColor" stroke-width="1.2"/><text x="570.0" y="162.5" text-anchor="middle" fill="currentColor" style="font-size:13px;">f = { x₃, x₇ }</text><line x1="90.0" y1="172.0" x2="55.0" y2="208.0" stroke="currentColor" stroke-width="1.2" stroke-linecap="round"/><rect x="31.0" y="208.0" width="48.0" height="28.0" fill="var(--accent)" rx="4" fill-opacity="0.12" stroke="currentColor" stroke-width="1.2"/><text x="55.0" y="226.5" text-anchor="middle" fill="currentColor" style="font-size:13px;">x₀</text><line x1="90.0" y1="172.0" x2="125.0" y2="208.0" stroke="currentColor" stroke-width="1.2" stroke-linecap="round"/><rect x="101.0" y="208.0" width="48.0" height="28.0" fill="var(--accent)" rx="4" fill-opacity="0.12" stroke="currentColor" stroke-width="1.2"/><text x="125.0" y="226.5" text-anchor="middle" fill="currentColor" style="font-size:13px;">x₄</text><line x1="250.0" y1="172.0" x2="215.0" y2="208.0" stroke="currentColor" stroke-width="1.2" stroke-linecap="round"/><rect x="191.0" y="208.0" width="48.0" height="28.0" fill="var(--accent)" rx="4" fill-opacity="0.12" stroke="currentColor" stroke-width="1.2"/><text x="215.0" y="226.5" text-anchor="middle" fill="currentColor" style="font-size:13px;">x₂</text><line x1="250.0" y1="172.0" x2="285.0" y2="208.0" stroke="currentColor" stroke-width="1.2" stroke-linecap="round"/><rect x="261.0" y="208.0" width="48.0" height="28.0" fill="var(--accent)" rx="4" fill-opacity="0.12" stroke="currentColor" stroke-width="1.2"/><text x="285.0" y="226.5" text-anchor="middle" fill="currentColor" style="font-size:13px;">x₆</text><line x1="410.0" y1="172.0" x2="375.0" y2="208.0" stroke="currentColor" stroke-width="1.2" stroke-linecap="round"/><rect x="351.0" y="208.0" width="48.0" height="28.0" fill="var(--accent)" rx="4" fill-opacity="0.12" stroke="currentColor" stroke-width="1.2"/><text x="375.0" y="226.5" text-anchor="middle" fill="currentColor" style="font-size:13px;">x₁</text><line x1="410.0" y1="172.0" x2="445.0" y2="208.0" stroke="currentColor" stroke-width="1.2" stroke-linecap="round"/><rect x="421.0" y="208.0" width="48.0" height="28.0" fill="var(--accent)" rx="4" fill-opacity="0.12" stroke="currentColor" stroke-width="1.2"/><text x="445.0" y="226.5" text-anchor="middle" fill="currentColor" style="font-size:13px;">x₅</text><line x1="570.0" y1="172.0" x2="535.0" y2="208.0" stroke="currentColor" stroke-width="1.2" stroke-linecap="round"/><rect x="511.0" y="208.0" width="48.0" height="28.0" fill="var(--accent)" rx="4" fill-opacity="0.12" stroke="currentColor" stroke-width="1.2"/><text x="535.0" y="226.5" text-anchor="middle" fill="currentColor" style="font-size:13px;">x₃</text><line x1="570.0" y1="172.0" x2="605.0" y2="208.0" stroke="currentColor" stroke-width="1.2" stroke-linecap="round"/><rect x="581.0" y="208.0" width="48.0" height="28.0" fill="var(--accent)" rx="4" fill-opacity="0.12" stroke="currentColor" stroke-width="1.2"/><text x="605.0" y="226.5" text-anchor="middle" fill="currentColor" style="font-size:13px;">x₇</text><text x="330.0" y="256.0" text-anchor="middle" fill="var(--muted)" style="font-size:12px;">length-1 sequences: each one is its own DFT, so the merging can start here</text></svg><figcaption><strong>Step 1 for N = 8: split by even and odd index until every piece has length 1.</strong> The names a to f follow the lecture; the tree records which pairs are merged later (c with d into A, e with f into B, A with B into X). The bottom row is the input order of the butterfly diagram: x<sub>0</sub>, x<sub>4</sub>, x<sub>2</sub>, x<sub>6</sub>, x<sub>1</sub>, x<sub>5</sub>, x<sub>3</sub>, x<sub>7</sub>.</figcaption></figure>

> [!question] Example 1 (slide 10) — length-4 DFT
> $x[n]=\{x_0,x_1,x_2,x_3\}$. Write $X[k]$ using the decimation-in-time FFT. Check with $x[n]=\{\underset{\uparrow}{1},\ 2,\ 3,\ 4\}$.

> [!success]- Answer
> **Split.** $a[n]=\{x_0,x_2\}$, $b[n]=\{x_1,x_3\}$; then $c=\{x_0\}$, $d=\{x_2\}$, $e=\{x_1\}$, $f=\{x_3\}$, each its own DFT.
>
> **Merge to length 2** ($L=2$, only $k=0$, $W_2^0=1$): the sum and the difference.
> $$
> A[k]=\{x_0+x_2,\ x_0-x_2\},\qquad B[k]=\{x_1+x_3,\ x_1-x_3\}.
> $$
> This matches what a length-2 DFT should be: bin 0 is the DC value (the sum), bin 1 is $\omega=\pi$ (the alternating sum).
>
> **Merge to length 4** ($L=4$, $k=0,1$, $W_4^0=1$, $W_4^1=-j$):
> $$
> \begin{aligned}
> X[0]&=A[0]+W_4^0B[0]=x_0+x_2+x_1+x_3\\
> X[1]&=A[1]+W_4^1B[1]=(x_0-x_2)-j(x_1-x_3)\\
> X[2]&=A[0]-W_4^0B[0]=(x_0+x_2)-(x_1+x_3)\\
> X[3]&=A[1]-W_4^1B[1]=(x_0-x_2)+j(x_1-x_3)
> \end{aligned}
> $$
> **Check.** $\{1,2,3,4\}$: $A=\{4,-2\}$, $B=\{6,-2\}$, so $X[k]=\{10,\ -2+2j,\ -2,\ -2-2j\}$, the same as the DFT sum ($X[0]$ is the sum 10, $X[2]$ the alternating sum $1-2+3-4=-2$).

> [!question] Example 2 (slide 11; notes, Exercise 1) — length-8 DFT
> $x[n]=\{x_0,\dots,x_7\}$. Set up the three merging stages. Then compute the DFT of $x[n]=\{\underset{\uparrow}{1},\ 2,\ 3,\ 4,\ 4,\ 3,\ 2,\ 1\}$.

> [!success]- Answer
> **Split** (the tree above): $a=\{x_0,x_2,x_4,x_6\}$, $b=\{x_1,x_3,x_5,x_7\}$; $c=\{x_0,x_4\}$, $d=\{x_2,x_6\}$, $e=\{x_1,x_5\}$, $f=\{x_3,x_7\}$ (eqs. 26–31).
>
> **Stage 1, to length 2** (eqs. 32–35): $C=\{x_0+x_4,\ x_0-x_4\}$, and likewise $D$, $E$, $F$.
>
> **Stage 2, to length 4** (eqs. 36–37), $0\le k\le1$:
> $$
> A[k]=C[k]+W_4^kD[k],\quad A[k+2]=C[k]-W_4^kD[k];\qquad B[k]=E[k]+W_4^kF[k],\quad B[k+2]=E[k]-W_4^kF[k].
> $$
> **Stage 3, to length 8** (eqs. 38–39), $0\le k\le3$:
> $$
> X[k]=A[k]+W_8^kB[k],\qquad X[k+4]=A[k]-W_8^kB[k].
> $$
> **Numbers** (not in the notes). $C=\{5,-3\}$, $D=\{5,1\}$, $E=\{5,-1\}$, $F=\{5,3\}$. With $W_4^1=-j$:
> $$
> A=\{10,\ -3-j,\ 0,\ -3+j\},\qquad B=\{10,\ -1-3j,\ 0,\ -1+3j\}.
> $$
> With $W_8^1=\frac{1-j}{\sqrt2}$, $W_8^2=-j$, $W_8^3=\frac{-1-j}{\sqrt2}$: $W_8^1B[1]=-2\sqrt2-j\sqrt2$ and $W_8^3B[3]=2\sqrt2-j\sqrt2$, so
> $$
> X[k]=\{20,\ -(3+2\sqrt2)-j(1+\sqrt2),\ 0,\ -(3-2\sqrt2)+j(1-\sqrt2),\ 0,\ X^*[3],\ 0,\ X^*[1]\}.
> $$
> Numerically $X[1]\approx-5.828-2.414j$ and $X[3]\approx-0.172-0.414j$. $X[0]=20$ is the sum of the samples, and $X[8-k]=X^*[k]$ because $x[n]$ is real ([[concepts/dft-properties|DFT properties]]).

The same recursion in a few lines of Python (run; the output is pasted below):

```python
import numpy as np

def fft_dit(x):                                  # len(x) must be a power of 2
    N = len(x)
    if N == 1:
        return np.array(x, dtype=complex)        # base case: its own DFT
    A = fft_dit(x[0::2])                         # DFT of the even-index samples
    B = fft_dit(x[1::2])                         # DFT of the odd-index samples
    t = np.exp(-2j * np.pi * np.arange(N // 2) / N) * B     # W_N^k B[k]
    return np.concatenate([A + t, A - t])        # X[k] and X[k + N/2]

x = np.array([1, 2, 3, 4, 4, 3, 2, 1])
print(np.round(fft_dit(x), 3))
print(np.allclose(fft_dit(x), np.fft.fft(x)))
```

```text
[20.   +0.j    -5.828-2.414j  0.   +0.j    -0.172-0.414j  0.   +0.j
 -0.172+0.414j  0.   +0.j    -5.828+2.414j]
True
```

## 5. Why the cost is $N\log_2N$

> [!key] Counting the work (Lecture 25 §2.2)
> - **One stage costs $N$.** A stage has $\frac N2$ pairs of merging equations, and each pair is two multiply-adds: $N$ in all, whatever the stage.
> - **There are $\log_2N$ stages**, because every merge doubles the length: $1\to2\to4\to\dots\to N$.
> - Total: $N\log_2N$. For $N=4$: $2\times4=8$ instead of 16. For $N=8$: $3\times8=24$ instead of 64.
>
> The saving comes from **reusing** results: $A[k]$ and $B[k]$ are computed once and used for two outputs each, at every level of the recursion. Smaller savings (every $W^0=1$ needs no multiplication) do not change the order.

> [!lecture] In lecture — L25, Nov 6
> Counting on the length-4 example: "it looks like we're adding four things, but keep in mind we already have these values of $A[k]$ and $B[k]$ stored. We're reusing computation here." Then the demo, a double for-loop DFT against the recursive FFT in plain Python: for $N=2^4$, 228 µs against 61 µs, the expected factor $2^8/2^6=4$; for $N=2^{10}$ about a hundred times faster, with an error against NumPy of $10^{-14}$. "I am always amazed at how almost exact these experiments are."

> [!trap]
> - The FFT gives the **same** $X[k]$ as the DFT sum. There is nothing new to learn about pairs or properties.
> - The twiddle subscript is the length merged **to**: merging two length-4 DFTs uses $W_8^k$, not $W_4^k$.
> - In the merging equations $k$ only runs to $\frac L2-1$. The outputs with index $\ge\frac L2$ come from the second (minus) equation, not from plugging a large $k$ into the first.
> - Radix 2 needs a power-of-2 length. Padding a signal with zeros to reach one changes which frequencies the DFT samples ([[concepts/zero-padding|zero padding]]), not the underlying DTFT.
> - $O(N\log N)$ is an order, not an exact count, and the log is base 2.

> [!exam] After Midterm 2
> Not on Midterm 2; "of course going to be important content for your final exam" (Oct 28). Twiddle factors may be left unsimplified, "as long as they're equivalent" (Nov 6). Older exams: [[exams/midterm-2/past-exams/fall-2019|FA2019 MT2]] #1(j) and #10 · practice: [[homework/hw10|HW10]] #1.

**Where it appears:** [[5-dft-and-fft/25-fast-fourier-transform|Lecture 25]] §1–2.1 (eqs. 1–39, slides 3–11) · reading the diagrams: [[concepts/butterfly-diagram|butterfly diagram]] · its main use: [[concepts/fast-convolution|fast convolution]].

## Related
[[concepts/dft|DFT]] · [[concepts/butterfly-diagram|butterfly diagram]] · [[concepts/fast-convolution|fast convolution]] · [[concepts/zero-padding|zero padding]] · [[concepts/short-time-fourier-transform|STFT]] · [[5-dft-and-fft/index|Unit 5]]

### Sources for this page
Snyder, Lecture 25 notes (§1–2.2, eqs. 1–39) and annotated slides 1–11, Oct 28 – Nov 6, 2026; lecture recordings Oct 28, Oct 30 and Nov 6 (condensed). The numeric length-8 example and the code are worked here and checked against NumPy (`tools/verify_l24_27.py`).
