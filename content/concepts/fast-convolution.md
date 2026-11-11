---
title: "Fast convolution via the DFT"
description: "The convolution sum costs O(N²). Zero-pad both sequences to M ≥ N + L − 1, take FFTs, multiply, invert: the circular convolution then equals the linear one and the cost drops to O(N log N). Wrap-around, radix-2 padding, and when it pays off."
tags: [concept, dft, fft]
aliases: ["fast convolution", "fast linear convolution", "convolution via the DFT", "convolution via the FFT", "FFT convolution", "cost of convolution", "wrap-around"]
---

*Lecture 26 (Fri Nov 6, the last ten minutes; repeated more slowly in the makeup recording posted that day) §1–2.1 · [[homework/hw10|HW10]] #2–#3 · builds on [[concepts/circular-convolution|circular convolution]], [[concepts/zero-padding|zero padding]] and the [[concepts/fast-fourier-transform|FFT]]*

> [!abstract] In one breath
> - Convolving two length-$N$ sequences with the convolution sum costs $O(N^2)$.
> - Multiplying their DFTs is cheap, but it computes a **circular** convolution: the tail of $x*h$ wraps around and lands on top of its beginning.
> - Zero-pad both sequences to a common length $M\ge N+L-1$ first. Then nothing wraps, circular equals linear, and pad → FFT → multiply → inverse FFT costs $O(N\log N)$.

## 1. What the convolution sum costs (§1)

> [!key] Cost of the convolution sum (Lecture 26, eqs. 1–2)
> $$
> y[n]=x[n]*h[n]=\sum_{k=-\infty}^{\infty}x[k]\,h[n-k].
> $$
> Take $x$ and $h$ both of length $N$ (the worst case).
> - One output sample needs at most $N$ multiply-adds: the case of full overlap in the flip-and-shift picture. That is $O(N)$ per sample.
> - The output has $2N-1$ samples, which is also $O(N)$.
> - Total: $O(N)\cdot O(N)=O(N^2)$. The matrix form of [[concepts/convolution|convolution]] has the same order, only a better constant.
>
> After a lecture on why $N^2$ is too slow for the DFT, the same growth here is the motivation: use the $O(N\log N)$ FFT to convolve.

## 2. Why multiplying DFTs is not enough: wrap-around (§2)

The [[concepts/circular-convolution|circular convolution]] property says $x[n]\circledast h[n]\overset{\text{DFT}}{\longleftrightarrow}X[k]H[k]$. So $\mathrm{IDFT}\{X[k]H[k]\}$ is the circular convolution, not the linear one we want. The slides compare the two on

$$
x[n]=\{\underset{\uparrow}{1},\ 2,\ 3,\ 4\},\qquad h[n]=\{\underset{\uparrow}{-1},\ 1,\ -2,\ 2\}.
$$

| | $n=0$ | 1 | 2 | 3 | 4 | 5 | 6 |
|---|---|---|---|---|---|---|---|
| linear $y[n]=x*h$ | $-1$ | $-1$ | $-3$ | $-3$ | $2$ | $-2$ | $8$ |
| 4-point circular $\tilde y[n]=x\circledast_4h$ | $1$ | $-3$ | $5$ | $-3$ | | | |

The lengths cannot match: the linear result has $4+4-1=7$ samples, the circular one 4. The values differ as well, in a specific way: the samples $y[4],y[5],y[6]$ that do not fit are folded back onto $n=0,1,2$:

$$
\tilde y[0]=y[0]+y[4]=-1+2=1,\quad\tilde y[1]=y[1]+y[5]=-1-2=-3,\quad\tilde y[2]=y[2]+y[6]=-3+8=5,\quad\tilde y[3]=y[3]=-3.
$$

That folding is the **wrap-around**: in the circulant matrix the entries that linear convolution would multiply by zeros are instead filled with the periodic repetition of $h$.

> [!key] The fix: zero-pad to the length of the answer (Lecture 26, eqs. 8–10)
> Pad both sequences with zeros to length $7$, the length of $x*h$:
> $$
> x_{zp}[n]=\{\underset{\uparrow}{1},\ 2,\ 3,\ 4,\ 0,\ 0,\ 0\},\qquad h_{zp}[n]=\{\underset{\uparrow}{-1},\ 1,\ -2,\ 2,\ 0,\ 0,\ 0\}.
> $$
> Their 7-point circular convolution is $\{\underset{\uparrow}{-1},\ -1,\ -3,\ -3,\ 2,\ -2,\ 8\}=x*h$ exactly. The padded zeros sit where the wrapped samples used to land, so nothing is added to the wrong place.
> - In general: $x$ of length $N$, $h$ of length $L$ → pad **both** to the same $M\ge N+L-1$.
> - Padding with zeros does not change $x*h$ (it only appends zeros to it) and does not change either DTFT ([[concepts/zero-padding|zero padding]]).
> - The notes' own example, $\{3,1,0,-1\}*\{5,1,-1,4\}=\{15,8,-2,6,3,1,-4\}$, wraps to $\{18,9,-6,6\}$ without padding ($15+3$, $8+1$, $-2-4$, $6$).

> [!lecture] In lecture — L26, Nov 6
> Padding was meant only as a first step, "to make sure that the result is the correct length … and maybe from there we can figure out what else needs to be done." Then: "we see that, oh, we're actually done. We don't need to do anything else. That's why this lecture is so fast, because it's a really simple trick." On circular convolution itself: it "sounds awful, but I promise you it's actually not too bad", since there is only one case: two finite sequences of equal length.

## 3. The algorithm (§2.1)

<figure class="ece-fig"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 680 176" width="680" height="176" role="img" aria-label="the four steps of fast linear convolution with the FFT" style="font-family:'Source Sans 3','Source Sans Pro',system-ui,sans-serif;font-size:13px"><defs><marker id="ah-fastconv-pipeline" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="context-stroke"/></marker></defs><text x="64.0" y="43.0" text-anchor="end" fill="currentColor" style="font-size:14px;font-family:'STIX Two Math','Latin Modern Math','Cambria Math','Times New Roman',serif;font-style:italic;">x[n]</text><text x="64.0" y="58.0" text-anchor="end" fill="var(--muted)" style="font-size:10px;">length N</text><text x="64.0" y="109.0" text-anchor="end" fill="currentColor" style="font-size:14px;font-family:'STIX Two Math','Latin Modern Math','Cambria Math','Times New Roman',serif;font-style:italic;">h[n]</text><text x="64.0" y="124.0" text-anchor="end" fill="var(--muted)" style="font-size:10px;">length L</text><line x1="70.0" y1="45.0" x2="92.0" y2="45.0" stroke="currentColor" stroke-width="1.3" marker-end="url(#ah-fastconv-pipeline)" stroke-linecap="round"/><rect x="96.0" y="30.0" width="150.0" height="30.0" fill="var(--accent)" rx="4" fill-opacity="0.1" stroke="currentColor" stroke-width="1.2"/><text x="171.0" y="49.5" text-anchor="middle" fill="currentColor" style="font-size:12px;">zero-pad to length M</text><line x1="246.0" y1="45.0" x2="276.0" y2="45.0" stroke="currentColor" stroke-width="1.3" marker-end="url(#ah-fastconv-pipeline)" stroke-linecap="round"/><rect x="280.0" y="30.0" width="92.0" height="30.0" fill="var(--accent)" rx="4" fill-opacity="0.1" stroke="currentColor" stroke-width="1.2"/><text x="326.0" y="49.5" text-anchor="middle" fill="currentColor" style="font-size:12px;">M-point FFT</text><line x1="70.0" y1="111.0" x2="92.0" y2="111.0" stroke="currentColor" stroke-width="1.3" marker-end="url(#ah-fastconv-pipeline)" stroke-linecap="round"/><rect x="96.0" y="96.0" width="150.0" height="30.0" fill="var(--accent)" rx="4" fill-opacity="0.1" stroke="currentColor" stroke-width="1.2"/><text x="171.0" y="115.5" text-anchor="middle" fill="currentColor" style="font-size:12px;">zero-pad to length M</text><line x1="246.0" y1="111.0" x2="276.0" y2="111.0" stroke="currentColor" stroke-width="1.3" marker-end="url(#ah-fastconv-pipeline)" stroke-linecap="round"/><rect x="280.0" y="96.0" width="92.0" height="30.0" fill="var(--accent)" rx="4" fill-opacity="0.1" stroke="currentColor" stroke-width="1.2"/><text x="326.0" y="115.5" text-anchor="middle" fill="currentColor" style="font-size:12px;">M-point FFT</text><line x1="372.0" y1="45.0" x2="414.0" y2="73.0" stroke="currentColor" stroke-width="1.3" marker-end="url(#ah-fastconv-pipeline)" stroke-linecap="round"/><line x1="372.0" y1="111.0" x2="414.0" y2="83.0" stroke="currentColor" stroke-width="1.3" marker-end="url(#ah-fastconv-pipeline)" stroke-linecap="round"/><circle cx="430" cy="78" r="14" fill="none" stroke="currentColor" stroke-width="1.4"/><text x="430.0" y="83.0" text-anchor="middle" fill="currentColor" style="font-size:16px;">×</text><text x="430.0" y="52.0" text-anchor="middle" fill="var(--muted)" style="font-size:10px;">bin by bin</text><line x1="444.0" y1="78.0" x2="470.0" y2="78.0" stroke="currentColor" stroke-width="1.3" marker-end="url(#ah-fastconv-pipeline)" stroke-linecap="round"/><rect x="474.0" y="63.0" width="100.0" height="30.0" fill="var(--accent)" rx="4" fill-opacity="0.1" stroke="currentColor" stroke-width="1.2"/><text x="524.0" y="82.5" text-anchor="middle" fill="currentColor" style="font-size:12px;">inverse FFT</text><line x1="574.0" y1="78.0" x2="598.0" y2="78.0" stroke="currentColor" stroke-width="1.3" marker-end="url(#ah-fastconv-pipeline)" stroke-linecap="round"/><text x="604.0" y="76.0" text-anchor="start" fill="currentColor" style="font-size:14px;font-family:'STIX Two Math','Latin Modern Math','Cambria Math','Times New Roman',serif;font-style:italic;">x[n] ∗ h[n]</text><text x="604.0" y="92.0" text-anchor="start" fill="var(--muted)" style="font-size:10px;">N + L − 1</text><text x="604.0" y="104.0" text-anchor="start" fill="var(--muted)" style="font-size:10px;">samples</text><text x="171.0" y="156.0" text-anchor="middle" fill="var(--accent2)" style="font-size:12px;font-weight:600;">① O(1)</text><text x="326.0" y="156.0" text-anchor="middle" fill="var(--accent2)" style="font-size:12px;font-weight:600;">② 2 · O(M log M)</text><text x="430.0" y="156.0" text-anchor="middle" fill="var(--accent2)" style="font-size:12px;font-weight:600;">③ O(M)</text><text x="524.0" y="156.0" text-anchor="middle" fill="var(--accent2)" style="font-size:12px;font-weight:600;">④ O(M log M)</text></svg><figcaption><strong>Fast linear convolution (Lecture 26, §2.1).</strong> Pad both sequences to a common length M ≥ N + L − 1 (the next power of 2 for a radix-2 FFT), transform, multiply bin by bin, transform back. The padding makes the circular convolution that the DFT product computes equal to the linear one; the total cost is O(M log M) instead of O(N²).</figcaption></figure>

> [!recipe] Fast linear convolution (Lecture 26 §2.1, slide 7)
> $x[n]$ of length $N$, $h[n]$ of length $L$, with $L$ of the same order as $N$.
> 1. **Zero-pad** both to length $M=N+L-1$ → $x_{zp}[n]$, $h_{zp}[n]$. For a radix-2 FFT pad a little further, to the next power of 2 that is $\ge N+L-1$. Cost $O(1)$.
> 2. **FFT** both → $X_{zp}[k]$, $H_{zp}[k]$. Cost $O(N\log N)$.
> 3. **Multiply** bin by bin: $Y_{zp}[k]=X_{zp}[k]\,H_{zp}[k]$. Cost $O(N)$.
> 4. **Inverse FFT** → $y[n]=x[n]*h[n]$. Cost $O(N\log N)$.
>
> Total: $O(1)+O(N\log N)+O(N)+O(N\log N)=O(N\log N)$, against $O(N^2)$ for the convolution sum.
>
> Example of step 1: $N=8$, $L=5$ gives $8+5-1=12$; with a radix-2 FFT pad to 16. If the padded length is larger than $N+L-1$, the extra output samples are zeros.

Run in Python (output pasted):

```python
import numpy as np

x = np.array([1, 2, 3, 4]); h = np.array([-1, 1, -2, 2])
M = len(x) + len(h) - 1                          # 7 (use 8 for a radix-2 FFT)
y = np.fft.ifft(np.fft.fft(x, M) * np.fft.fft(h, M)).real
print(np.round(y, 10) + 0.0)
print(np.convolve(x, h))
```

```text
[-1. -1. -3. -3.  2. -2.  8.]
[-1 -1 -3 -3  2 -2  8]
```

`np.fft.fft(x, M)` pads to length `M` by itself, which is the sense in which step 1 is free.

> [!lecture] In lecture — L26, Nov 6
> "Zero padding is a constant time operation. You don't even need to physically pad the zeros … You can just tell whatever system you're using, I need you to pretend like there's 12 zeros padded to the end of you. That's it. You just need to tell it a number." And on the two forward transforms: "yes there are two of them, but $O(2N\log N)$ is the same as $O(N\log N)$."

## 4. When it pays off

Big-O hides constants. The algorithm runs **three** FFT-sized transforms (two forward, one inverse) plus $M$ multiplications, so for short sequences the plain convolution sum is cheaper. A rough count with $M=2N$, not from the notes:

| $N$ | convolution sum, about $N^2$ | FFT route, about $3M\log_2M+M$ | cheaper |
|---|---|---|---|
| 16 | 256 | 512 | sum |
| 32 | 1 024 | 1 216 | sum |
| 64 | 4 096 | 2 816 | FFT |
| 1024 | 1 048 576 | 69 632 | FFT, by 15× |

The notes make the same point ("$3N\log_2N+N\gt N^2$ for some values of $N$"), and Lab 5 of ECE 311 measures it. The takeaway of the lecture: the FFT route becomes more advantageous as $N$ grows.

> [!question] Practice — how many zeros?
> $x[n]$ has 100 samples and $h[n]$ has 30. How many zeros must be appended to each (a) for the DFT method, (b) if the FFT is radix-2?

> [!success]- Answer
> $x*h$ has $100+30-1=129$ samples.
> (a) $M=129$: 29 zeros on $x$, 99 zeros on $h$.
> (b) Next power of 2 is $2^8=256$ ($2^7=128$ is one short): 156 zeros on $x$, 226 zeros on $h$. The last $256-129=127$ output samples are zero.

> [!trap]
> - Pad both to the **same** $M\ge N+L-1$, not to $\max(N,L)$. The two sequences therefore get different numbers of zeros.
> - $X[k]H[k]$ without padding is not wrong arithmetic, it is the answer to a different question: the wrapped convolution.
> - The zeros may also be put in front of the sequences, but then the result comes out circularly shifted and has to be rotated back ([[homework/hw10|HW10]] #3(c)).
> - $O(N\log N)$ does not mean faster for every $N$.
> - The same wrap-around is why you cannot low-pass filter by zeroing DFT bins ([[concepts/ideal-filters|ideal filters]]).

> [!exam] Homework and old exams
> [[homework/hw10|HW10]] #2 (linear vs circular, smallest $N$) and #3 (zeros for the DFT and radix-2 methods). The same count on [[exams/midterm-2/past-exams/fall-2019|FA2019 MT2 #11]]. Not on Fall 2026 Midterm 2; post-midterm material for the final.

**Where it appears:** [[5-dft-and-fft/26-fast-convolution-via-the-dft|Lecture 26]] §1–2.1 (eqs. 1–11, slides 3–7) · [[homework/hw10|HW10]] #2–#3 · ECE 311 Lab 5.

## Related
[[concepts/circular-convolution|circular convolution]] · [[concepts/convolution|convolution]] · [[concepts/zero-padding|zero padding]] · [[concepts/fast-fourier-transform|FFT]] · [[concepts/dft-properties|DFT properties]] · [[5-dft-and-fft/index|Unit 5]]

### Sources for this page
Snyder, Lecture 26 notes (§1–2.1, eqs. 1–11) and annotated slides 1–7, Nov 6, 2026; lecture recording Nov 6 and the makeup recording posted Nov 6 (condensed). The operation counts of §4, the practice problem and the code are worked here (`tools/verify_l24_27.py`).
