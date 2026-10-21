---
title: "Circular convolution"
description: "x⊛h = Σ x[m] h[⟨n−m⟩_N] for length-N sequences: the inverse DFT of X[k]H[k]; equals linear convolution once both are zero-padded to N ≥ N1+N2−1; circulant-matrix form."
tags: [concept, dft]
aliases: ["circular convolution", "⊛"]
---

> [!key] Definition (Lecture 21)
> For length-$N$ $x[n]$, $h[n]$, with $\langle n\rangle_N$ the remainder of $n$ divided by $N$:
> $$
> \begin{aligned}
> x[n]\circledast h[n]&=\sum_{m=0}^{N-1}x[m]\,h[\langle n-m\rangle_N]\\
> &=\sum_{m=0}^{N-1}h[m]\,x[\langle n-m\rangle_N],\qquad 0\le n\le N-1.
> \end{aligned}
> $$
> Output length $N$. Unequal lengths: zero-pad the shorter; $\circledast_N$ = both padded to $N$.

> [!key] DFT property
> $$
> x[n]\circledast h[n]\ \overset{\text{DFT}}{\longleftrightarrow}\ X[k]H[k]
> $$
> The DFT version of [[concepts/convolution|convolution]] ↔ multiplication. Dual: $x[n]w[n]\leftrightarrow\frac1N X[k]\circledast W[k]$.

**Relation to linear convolution.** $x$ of length $N_1$, $h$ of length $N_2$: $x*h$ has length $N_1+N_2-1$.
- $N$-point circular = linear with the tail wrapped (time aliasing): $(x\circledast_N h)[n]=\sum_r (x*h)[n+rN]$, $0\le n\le N-1$.
- Equal for all such inputs iff $N\ge N_1+N_2-1$: zero-pad both to $N$, multiply the [[concepts/dft|DFTs]], invert.
- $\{2,0,1,3,0\}\circledast_5\{4,1,0,2,2\}=\{10,10,10,17,7\}$; linear $\{8,2,4,17,7,2,8,6,0\}$, tail $\{2,8,6,0\}$ added onto $n=0,\dots,3$.

**Computing it.**
- Table: row $n$ holds $h[\langle n-m\rangle_N]$; row 0 is the circular reversal $\{h[0],h[N-1],\dots,h[1]\}$, each next row rotates right one place; dot each row with $x$.
- Circulant matrix: $\mathbf y=\tilde{\mathbf H}\mathbf x$, $\tilde{\mathbf H}_{nm}=h[\langle n-m\rangle_N]$; rows = table rows, constant diagonals.
- Lecture 21's example: $\{3,1,0,3,1,1\}\circledast\{-4,-1,-7,5,5,1\}=\{-4,6,-9,2,14,-18\}$.

> [!trap]
> - Circular reversal keeps $h[0]$ first; the plain flip does not.
> - $X[k]H[k]$ with $N<N_1+N_2-1$ gives the wrapped result, not $x*h$.

## Related
[[5-dft-and-fft/21-dft-properties|Lecture 21]] · [[concepts/convolution|convolution]] · [[concepts/dft|DFT]]

### Sources for this page
Snyder, Lecture 21 notes (eqs. 9–24, Table 1) and slides (Example 2), Oct 19, 2026.
