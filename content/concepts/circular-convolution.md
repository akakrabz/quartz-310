---
title: "Circular convolution"
description: "x⊛h = Σ x[m] h[⟨n−m⟩_N] for length-N sequences: the inverse DFT of X[k]H[k], derived; the modified table and circulant-matrix methods on the notes' 6-point example; equals linear convolution once padded to N ≥ N1+N2−1."
tags: [concept, dft, midterm-2]
aliases: ["circular convolution", "⊛", "circulant matrix", "modified table method", "linear vs circular convolution"]
---

*Lecture 21 (Mon Oct 19) §2–2.1 · family: [[problems/circular-convolution-and-dft-properties|circular convolution and DFT properties]]*

> [!abstract] In one breath
> - Product of DFTs ↔ **circular** convolution $\sum_mx[m]\,h[\langle n-m\rangle_N]$, length $N$.
> - Compute it with Lecture 4's table, the moving sequence periodically extended (rows = rotations of the circular reversal), or as a circulant matrix times a vector.
> - It equals linear convolution once both inputs are zero-padded to $N\ge N_1+N_2-1$; otherwise the tail wraps around.

## 1. Inverse DFT of a product

z-transform and DTFT: $x*h\leftrightarrow X(z)H(z)$, $X_d(\omega)H_d(\omega)$ (eqs. 7–8). DFT: for length-$N$ $x,h$, what is the inverse DFT of $Y[k]=X[k]H[k]$?

> [!derivation]- Inverse DFT of $X[k]H[k]$ (eqs. 9–14)
> $$
> \begin{aligned}
> y[n]&=\frac1N\sum_{k=0}^{N-1}X[k]H[k]\,e^{j\frac{2\pi k}{N}n}\\
> &=\frac1N\sum_{k=0}^{N-1}\Big(\sum_{m=0}^{N-1}x[m]e^{-j\frac{2\pi k}{N}m}\Big)\Big(\sum_{l=0}^{N-1}h[l]e^{-j\frac{2\pi k}{N}l}\Big)e^{j\frac{2\pi k}{N}n}\\
> &=\sum_{m=0}^{N-1}\sum_{l=0}^{N-1}x[m]\,h[l]\Big(\frac1N\sum_{k=0}^{N-1}e^{j2\pi k\frac{n-m-l}{N}}\Big)
> \end{aligned}
> $$
> Orthogonality ([[3-fourier-analysis/13-fourier-analysis-and-the-dtft|Lecture 13]]): the bracket is 1 if $\langle n-m-l\rangle_N=0$, else 0. Only $l=\langle n-m\rangle_N$ survives:
> $$
> y[n]=\sum_{m=0}^{N-1}x[m]\,h[\langle n-m\rangle_N].
> $$

> [!key] Circular convolution (Lecture 21, eqs. 15–16)
> For length-$N$ $x[n]$, $h[n]$, with $\langle n\rangle_N$ the remainder of $n$ divided by $N$ ([[concepts/circular-shift-and-reversal|modulo indexing]]):
> $$
> x[n]\circledast h[n]\ \overset{\text{DFT}}{\longleftrightarrow}\ X[k]H[k]
> $$
> $$
> x[n]\circledast h[n]=\sum_{m=0}^{N-1}x[m]\,h[\langle n-m\rangle_N]=\sum_{m=0}^{N-1}h[m]\,x[\langle n-m\rangle_N].
> $$
> - Two length-$N$ inputs, length-$N$ output ($0\le n\le N-1$). Unequal lengths: zero-pad the shorter; $\circledast_N$ = both padded to $N$ (slide 10).
> - The DFT version of [[concepts/convolution|convolution]] ↔ multiplication. Dual (windowing): $x[n]w[n]\leftrightarrow\frac1NX[k]\circledast W[k]$.

## 2. Computing it (§2.1)

$x[n]=\{\underset{\uparrow}{3},\ 1,\ 0,\ 3,\ 1,\ 1\}$, $h[n]=\{\underset{\uparrow}{-4},\ -1,\ -7,\ 5,\ 5,\ 1\}$, $N=6$ (eqs. 17–18).

**Modified table method.** [[1-signals-and-systems/04-impulse-response-and-convolution|Lecture 4]]'s flip-and-shift table, with the moving sequence periodically extended instead of zero-extended. Row $n$ holds $h[\langle n-m\rangle_6]$: row 0 is the circular reversal, each next row rotates right one place; $y[n]=\sum_mx[m]\,h[\langle n-m\rangle_6]$.

| | m = 0 | 1 | 2 | 3 | 4 | 5 | $y[n]$ |
|---|---|---|---|---|---|---|---|
| $x[m]$ | 3 | 1 | 0 | 3 | 1 | 1 | |
| $n=0$ | −4 | 1 | 5 | 5 | −7 | −1 | −4 |
| $n=1$ | −1 | −4 | 1 | 5 | 5 | −7 | 6 |
| $n=2$ | −7 | −1 | −4 | 1 | 5 | 5 | −9 |
| $n=3$ | 5 | −7 | −1 | −4 | 1 | 5 | 2 |
| $n=4$ | 5 | 5 | −7 | −1 | −4 | 1 | 14 |
| $n=5$ | 1 | 5 | 5 | −7 | −1 | −4 | −18 |

$$
y[n]=\{\underset{\uparrow}{-4},\ 6,\ -9,\ 2,\ 14,\ -18\}\qquad\text{(eq. 20)}
$$

**Matrix method.** $\mathbf y=\tilde{\mathbf H}\mathbf x=\tilde{\mathbf X}\mathbf h$ (eq. 21), with **circulant** matrices: $\tilde{\mathbf H}_{nm}=h[\langle n-m\rangle_N]$. First row = circular reversal; each next row = previous one shifted right, last entry wrapped to the front; diagonals constant. The rows of $\tilde{\mathbf H}$ are the table rows (eqs. 22–24).
$$
\begin{gathered}
\tilde{\mathbf H}=\begin{bmatrix}-4&1&5&5&-7&-1\\-1&-4&1&5&5&-7\\-7&-1&-4&1&5&5\\5&-7&-1&-4&1&5\\5&5&-7&-1&-4&1\\1&5&5&-7&-1&-4\end{bmatrix},\\
\mathbf y=\tilde{\mathbf X}\mathbf h=\begin{bmatrix}3&1&1&3&0&1\\1&3&1&1&3&0\\0&1&3&1&1&3\\3&0&1&3&1&1\\1&3&0&1&3&1\\1&1&3&0&1&3\end{bmatrix}\begin{bmatrix}-4\\-1\\-7\\5\\5\\1\end{bmatrix}=\begin{bmatrix}-4\\6\\-9\\2\\14\\-18\end{bmatrix}
\end{gathered}
$$

**Via DFTs.** $\mathrm{IDFT}\{X[k]H[k]\}$, the fast route for long sequences ([[concepts/dft|DFT]]).

## 3. Relation to linear convolution

$x$ of length $N_1$, $h$ of length $N_2$: $x*h$ has length $N_1+N_2-1$.
- $N$-point circular = linear with the tail wrapped (time aliasing): $(x\circledast_Nh)[n]=\sum_r(x*h)[n+rN]$, $0\le n\le N-1$.
- Equal for all such inputs iff $N\ge N_1+N_2-1$: zero-pad both to $N$, multiply the DFTs, invert.

> [!question] Example 2 (slide 13) — circular convolution
> $x[n]=\{\underset{\uparrow}{2},\ 0,\ 1,\ 3,\ 0\}$, $h[n]=\{\underset{\uparrow}{4},\ 1,\ 0,\ 2,\ 2\}$ (slide calls it $y[n]$). Compute the 5-point $x\circledast h$. Compare with the linear $x*h$.

> [!success]- Answer
> Rows $h[\langle n-m\rangle_5]$, starting from $\{4,2,2,0,1\}$; dot each with $x=\{2,0,1,3,0\}$:
> - $y[0]$: $\{4,2,2,0,1\}$ → $8+2=10$
> - $y[1]$: $\{1,4,2,2,0\}$ → $2+2+6=10$
> - $y[2]$: $\{0,1,4,2,2\}$ → $4+6=10$
> - $y[3]$: $\{2,0,1,4,2\}$ → $4+1+12=17$
> - $y[4]$: $\{2,2,0,1,4\}$ → $4+3=7$
>
> $$
> x\circledast h=\{\underset{\uparrow}{10},\ 10,\ 10,\ 17,\ 7\}
> $$
> Linear: $x*h=\{\underset{\uparrow}{8},\ 2,\ 4,\ 17,\ 7,\ 2,\ 8,\ 6,\ 0\}$, length $5+5-1=9$. The tail $n=5,\dots,8$ wraps onto $n=0,\dots,3$: $\{8+2,\ 2+8,\ 4+6,\ 17+0,\ 7\}$. Padding both to $N\ge9$ makes circular = linear.

> [!trap]
> - Circular reversal keeps $h[0]$ first; the plain flip does not.
> - $X[k]H[k]$ with $N\lt N_1+N_2-1$ gives the wrapped result, not $x*h$.
> - $x\circledast h\ne x*h$ unless both are padded to $N\ge N_1+N_2-1$; "is $N=7$ enough?" means compare $7$ with $N_1+N_2-1$.
> - Each table row is a rotation, never a shift with zeros entering.

> [!exam] Midterm 2
> Compute a circular convolution; compare with linear; the padding length that makes them equal. [[exams/midterm-2/past-exams/fall-2021|FA2021 #6]] · [[exams/midterm-2/past-exams/fall-2019|FA2019 #1(g), (h), #11]] · [[exams/midterm-2/true-false-bank|T/F bank]] §8 (Q41–Q42).

**Where it appears:** [[5-dft-and-fft/21-dft-properties|L21]] §2–2.1 (eqs. 7–24, slides 9–13) · [[problems/circular-convolution-and-dft-properties|circular convolution and DFT properties]] · [[exams/midterm-2/true-false-bank|T/F bank]] §8.

## Related
[[concepts/convolution|convolution]] · [[concepts/dft|DFT]] · [[concepts/dft-properties|DFT properties]] · [[concepts/circular-shift-and-reversal|circular shift and reversal]] · [[concepts/zero-padding|zero padding]] · [[problems/finite-length-convolution|finite-length convolution family]]

### Sources for this page
Snyder, Lecture 21 notes §2–2.1 (eqs. 7–24) and slides 9–13 (Example 2), Oct 19, 2026; past Midterm 2 exams.
