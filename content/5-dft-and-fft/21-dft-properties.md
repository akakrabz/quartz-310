---
title: "Lecture 21 — DFT properties"
description: "N-periodicity and modulo notation ⟨n⟩_N; circular time reversal; circular convolution x⊛h ↔ X[k]H[k] by modified table and circulant matrix; Table 1 of DFT properties; slide Examples 1–3 solved."
tags: [lecture, midterm-2, dft]
lecture: 21
---

*Lecture 21 · Mon Oct 19, 2026 · notes + slides "DFT properties" · prev: [[5-dft-and-fft/20-discrete-fourier-transform|Lecture 20]] · next: Lecture 22 (to come)*

> [!abstract] In one breath
> - DFT and inverse DFT are $N$-periodic: a length-$N$ signal acts as its periodic extension $x[\langle n\rangle_N]$.
> - Product of DFTs ↔ **circular** convolution $\sum_m x[m]\,h[\langle n-m\rangle_N]$: modified table or circulant matrix.
> - DTFT properties return with circular shifts and reversals (Table 1).

## 1. Periodicity of the DFT

DFT pair ([[5-dft-and-fft/20-discrete-fourier-transform|Lecture 20]]):
$$
\begin{gathered}
X[k]=\sum_{n=0}^{N-1}x[n]\,e^{-j\frac{2\pi k}{N}n},\ \ 0\le k\le N-1,\\
x[n]=\frac1N\sum_{k=0}^{N-1}X[k]\,e^{j\frac{2\pi k}{N}n},\ \ 0\le n\le N-1.
\end{gathered}
$$

> [!key] $N$-periodicity in frequency and time (eqs. 3–6)
> $$
> X[k+mN]=X[k],\qquad x[n+mN]=x[n],\qquad m\in\mathbb{Z}
> $$
> - Time: $X[k]$ uses only $x[0],\dots,x[N-1]$; the inverse DFT returns those values, periodically extended. Proofs: Lecture 20.
> - Modulo form: $x[n]=x[\langle n\rangle_N]$, $X[k]=X[\langle k\rangle_N]$ for all $n,k$.
> - $\langle n\rangle_N$ = remainder of $n$ divided by $N$, in $\{0,\dots,N-1\}$: $\langle 11\rangle_3=2$, $\langle 7\rangle_4=3$, $\langle -1\rangle_3=2$, $\langle 6\rangle_3=0$.

Every DFT belongs to a finite-length signal, periodically extended.

> [!key] Circular time reversal (eq. 19)
> $$
> x[\langle -n\rangle_N]=\begin{cases}x[0], & n=0\\ x[N-n], & 1\le n\le N-1\end{cases}
> $$
> Reverse the periodic extension, keep one period.

<figure class="ece-fig"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 640 372" width="640" height="372" role="img" aria-label="Three stem plots: a length-5 ramp x[n]; its periodic extension repeating every 5 samples from -5 to 9; the circular reversal, where n=0 keeps x[0] and n=1..4 hold x[4], x[3], x[2], x[1]." style="font-family:'Source Sans 3','Source Sans Pro',system-ui,sans-serif;font-size:13px"><text x="325.0" y="20.0" text-anchor="middle" fill="currentColor" style="font-size:13px;font-weight:600">(a) finite-length x[n], 0 ≤ n ≤ N−1</text><line x1="30.0" y1="104.0" x2="620.0" y2="104.0" stroke="currentColor" stroke-width="1" opacity="0.75"/><line x1="248.4" y1="26.0" x2="248.4" y2="104.0" stroke="currentColor" stroke-width="1" opacity="0.75"/><line x1="56.8" y1="101.0" x2="56.8" y2="107.0" stroke="currentColor" stroke-width="1"/><text x="56.8" y="118.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">−N</text><line x1="210.1" y1="101.0" x2="210.1" y2="107.0" stroke="currentColor" stroke-width="1"/><text x="210.1" y="118.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">−1</text><line x1="248.4" y1="101.0" x2="248.4" y2="107.0" stroke="currentColor" stroke-width="1"/><text x="248.4" y="118.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">0</text><line x1="286.7" y1="101.0" x2="286.7" y2="107.0" stroke="currentColor" stroke-width="1"/><text x="286.7" y="118.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">1</text><line x1="401.6" y1="101.0" x2="401.6" y2="107.0" stroke="currentColor" stroke-width="1"/><text x="401.6" y="118.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">N−1</text><line x1="439.9" y1="101.0" x2="439.9" y2="107.0" stroke="currentColor" stroke-width="1"/><text x="439.9" y="118.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">N</text><line x1="593.2" y1="101.0" x2="593.2" y2="107.0" stroke="currentColor" stroke-width="1"/><text x="593.2" y="118.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">2N−1</text><text x="620.0" y="98.0" text-anchor="end" fill="var(--muted)" style="font-size:12px">n</text><rect x="231.1" y="26.0" width="187.7" height="78.0" fill="var(--accent)" fill-opacity="0.1" stroke="none"/><line x1="248.4" y1="104.0" x2="248.4" y2="80.4" stroke="var(--hi)" stroke-width="1.6"/><circle cx="248.4" cy="80.4" r="3.2" fill="var(--hi)"/><line x1="286.7" y1="104.0" x2="286.7" y2="68.5" stroke="var(--accent)" stroke-width="1.6"/><circle cx="286.7" cy="68.5" r="3.2" fill="var(--accent)"/><line x1="325.0" y1="104.0" x2="325.0" y2="56.7" stroke="var(--accent)" stroke-width="1.6"/><circle cx="325.0" cy="56.7" r="3.2" fill="var(--accent)"/><line x1="363.3" y1="104.0" x2="363.3" y2="44.9" stroke="var(--accent)" stroke-width="1.6"/><circle cx="363.3" cy="44.9" r="3.2" fill="var(--accent)"/><line x1="401.6" y1="104.0" x2="401.6" y2="33.1" stroke="var(--accent)" stroke-width="1.6"/><circle cx="401.6" cy="33.1" r="3.2" fill="var(--accent)"/><text x="325.0" y="140.0" text-anchor="middle" fill="currentColor" style="font-size:13px;font-weight:600">(b) periodic extension x[⟨n⟩<tspan baseline-shift="sub" style="font-size:75%">N</tspan>]</text><line x1="30.0" y1="224.0" x2="620.0" y2="224.0" stroke="currentColor" stroke-width="1" opacity="0.75"/><line x1="248.4" y1="146.0" x2="248.4" y2="224.0" stroke="currentColor" stroke-width="1" opacity="0.75"/><line x1="56.8" y1="221.0" x2="56.8" y2="227.0" stroke="currentColor" stroke-width="1"/><text x="56.8" y="238.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">−N</text><line x1="210.1" y1="221.0" x2="210.1" y2="227.0" stroke="currentColor" stroke-width="1"/><text x="210.1" y="238.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">−1</text><line x1="248.4" y1="221.0" x2="248.4" y2="227.0" stroke="currentColor" stroke-width="1"/><text x="248.4" y="238.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">0</text><line x1="286.7" y1="221.0" x2="286.7" y2="227.0" stroke="currentColor" stroke-width="1"/><text x="286.7" y="238.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">1</text><line x1="401.6" y1="221.0" x2="401.6" y2="227.0" stroke="currentColor" stroke-width="1"/><text x="401.6" y="238.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">N−1</text><line x1="439.9" y1="221.0" x2="439.9" y2="227.0" stroke="currentColor" stroke-width="1"/><text x="439.9" y="238.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">N</text><line x1="593.2" y1="221.0" x2="593.2" y2="227.0" stroke="currentColor" stroke-width="1"/><text x="593.2" y="238.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">2N−1</text><text x="620.0" y="218.0" text-anchor="end" fill="var(--muted)" style="font-size:12px">n</text><rect x="231.1" y="146.0" width="187.7" height="78.0" fill="var(--accent)" fill-opacity="0.1" stroke="none"/><line x1="56.8" y1="224.0" x2="56.8" y2="200.4" stroke="var(--hi)" stroke-width="1.6"/><circle cx="56.8" cy="200.4" r="3.2" fill="var(--hi)"/><line x1="95.1" y1="224.0" x2="95.1" y2="188.5" stroke="var(--muted)" stroke-width="1.6"/><circle cx="95.1" cy="188.5" r="3.2" fill="var(--muted)"/><line x1="133.4" y1="224.0" x2="133.4" y2="176.7" stroke="var(--muted)" stroke-width="1.6"/><circle cx="133.4" cy="176.7" r="3.2" fill="var(--muted)"/><line x1="171.8" y1="224.0" x2="171.8" y2="164.9" stroke="var(--muted)" stroke-width="1.6"/><circle cx="171.8" cy="164.9" r="3.2" fill="var(--muted)"/><line x1="210.1" y1="224.0" x2="210.1" y2="153.1" stroke="var(--muted)" stroke-width="1.6"/><circle cx="210.1" cy="153.1" r="3.2" fill="var(--muted)"/><line x1="248.4" y1="224.0" x2="248.4" y2="200.4" stroke="var(--hi)" stroke-width="1.6"/><circle cx="248.4" cy="200.4" r="3.2" fill="var(--hi)"/><line x1="286.7" y1="224.0" x2="286.7" y2="188.5" stroke="var(--accent)" stroke-width="1.6"/><circle cx="286.7" cy="188.5" r="3.2" fill="var(--accent)"/><line x1="325.0" y1="224.0" x2="325.0" y2="176.7" stroke="var(--accent)" stroke-width="1.6"/><circle cx="325.0" cy="176.7" r="3.2" fill="var(--accent)"/><line x1="363.3" y1="224.0" x2="363.3" y2="164.9" stroke="var(--accent)" stroke-width="1.6"/><circle cx="363.3" cy="164.9" r="3.2" fill="var(--accent)"/><line x1="401.6" y1="224.0" x2="401.6" y2="153.1" stroke="var(--accent)" stroke-width="1.6"/><circle cx="401.6" cy="153.1" r="3.2" fill="var(--accent)"/><line x1="439.9" y1="224.0" x2="439.9" y2="200.4" stroke="var(--hi)" stroke-width="1.6"/><circle cx="439.9" cy="200.4" r="3.2" fill="var(--hi)"/><line x1="478.2" y1="224.0" x2="478.2" y2="188.5" stroke="var(--muted)" stroke-width="1.6"/><circle cx="478.2" cy="188.5" r="3.2" fill="var(--muted)"/><line x1="516.6" y1="224.0" x2="516.6" y2="176.7" stroke="var(--muted)" stroke-width="1.6"/><circle cx="516.6" cy="176.7" r="3.2" fill="var(--muted)"/><line x1="554.9" y1="224.0" x2="554.9" y2="164.9" stroke="var(--muted)" stroke-width="1.6"/><circle cx="554.9" cy="164.9" r="3.2" fill="var(--muted)"/><line x1="593.2" y1="224.0" x2="593.2" y2="153.1" stroke="var(--muted)" stroke-width="1.6"/><circle cx="593.2" cy="153.1" r="3.2" fill="var(--muted)"/><text x="41.5" y="188.5" text-anchor="middle" fill="var(--muted)" style="font-size:16px">…</text><text x="608.5" y="188.5" text-anchor="middle" fill="var(--muted)" style="font-size:16px">…</text><text x="325.0" y="260.0" text-anchor="middle" fill="currentColor" style="font-size:13px;font-weight:600">(c) circular reversal x[⟨−n⟩<tspan baseline-shift="sub" style="font-size:75%">N</tspan>]</text><line x1="30.0" y1="344.0" x2="620.0" y2="344.0" stroke="currentColor" stroke-width="1" opacity="0.75"/><line x1="248.4" y1="266.0" x2="248.4" y2="344.0" stroke="currentColor" stroke-width="1" opacity="0.75"/><line x1="56.8" y1="341.0" x2="56.8" y2="347.0" stroke="currentColor" stroke-width="1"/><text x="56.8" y="358.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">−N</text><line x1="210.1" y1="341.0" x2="210.1" y2="347.0" stroke="currentColor" stroke-width="1"/><text x="210.1" y="358.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">−1</text><line x1="248.4" y1="341.0" x2="248.4" y2="347.0" stroke="currentColor" stroke-width="1"/><text x="248.4" y="358.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">0</text><line x1="286.7" y1="341.0" x2="286.7" y2="347.0" stroke="currentColor" stroke-width="1"/><text x="286.7" y="358.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">1</text><line x1="401.6" y1="341.0" x2="401.6" y2="347.0" stroke="currentColor" stroke-width="1"/><text x="401.6" y="358.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">N−1</text><line x1="439.9" y1="341.0" x2="439.9" y2="347.0" stroke="currentColor" stroke-width="1"/><text x="439.9" y="358.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">N</text><line x1="593.2" y1="341.0" x2="593.2" y2="347.0" stroke="currentColor" stroke-width="1"/><text x="593.2" y="358.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">2N−1</text><text x="620.0" y="338.0" text-anchor="end" fill="var(--muted)" style="font-size:12px">n</text><rect x="231.1" y="266.0" width="187.7" height="78.0" fill="var(--accent)" fill-opacity="0.1" stroke="none"/><line x1="56.8" y1="344.0" x2="56.8" y2="320.4" stroke="var(--hi)" stroke-width="1.6"/><circle cx="56.8" cy="320.4" r="3.2" fill="var(--hi)"/><line x1="95.1" y1="344.0" x2="95.1" y2="273.1" stroke="var(--muted)" stroke-width="1.6"/><circle cx="95.1" cy="273.1" r="3.2" fill="var(--muted)"/><line x1="133.4" y1="344.0" x2="133.4" y2="284.9" stroke="var(--muted)" stroke-width="1.6"/><circle cx="133.4" cy="284.9" r="3.2" fill="var(--muted)"/><line x1="171.8" y1="344.0" x2="171.8" y2="296.7" stroke="var(--muted)" stroke-width="1.6"/><circle cx="171.8" cy="296.7" r="3.2" fill="var(--muted)"/><line x1="210.1" y1="344.0" x2="210.1" y2="308.5" stroke="var(--muted)" stroke-width="1.6"/><circle cx="210.1" cy="308.5" r="3.2" fill="var(--muted)"/><line x1="248.4" y1="344.0" x2="248.4" y2="320.4" stroke="var(--hi)" stroke-width="1.6"/><circle cx="248.4" cy="320.4" r="3.2" fill="var(--hi)"/><line x1="286.7" y1="344.0" x2="286.7" y2="273.1" stroke="var(--accent)" stroke-width="1.6"/><circle cx="286.7" cy="273.1" r="3.2" fill="var(--accent)"/><line x1="325.0" y1="344.0" x2="325.0" y2="284.9" stroke="var(--accent)" stroke-width="1.6"/><circle cx="325.0" cy="284.9" r="3.2" fill="var(--accent)"/><line x1="363.3" y1="344.0" x2="363.3" y2="296.7" stroke="var(--accent)" stroke-width="1.6"/><circle cx="363.3" cy="296.7" r="3.2" fill="var(--accent)"/><line x1="401.6" y1="344.0" x2="401.6" y2="308.5" stroke="var(--accent)" stroke-width="1.6"/><circle cx="401.6" cy="308.5" r="3.2" fill="var(--accent)"/><line x1="439.9" y1="344.0" x2="439.9" y2="320.4" stroke="var(--hi)" stroke-width="1.6"/><circle cx="439.9" cy="320.4" r="3.2" fill="var(--hi)"/><line x1="478.2" y1="344.0" x2="478.2" y2="273.1" stroke="var(--muted)" stroke-width="1.6"/><circle cx="478.2" cy="273.1" r="3.2" fill="var(--muted)"/><line x1="516.6" y1="344.0" x2="516.6" y2="284.9" stroke="var(--muted)" stroke-width="1.6"/><circle cx="516.6" cy="284.9" r="3.2" fill="var(--muted)"/><line x1="554.9" y1="344.0" x2="554.9" y2="296.7" stroke="var(--muted)" stroke-width="1.6"/><circle cx="554.9" cy="296.7" r="3.2" fill="var(--muted)"/><line x1="593.2" y1="344.0" x2="593.2" y2="308.5" stroke="var(--muted)" stroke-width="1.6"/><circle cx="593.2" cy="308.5" r="3.2" fill="var(--muted)"/><text x="41.5" y="308.5" text-anchor="middle" fill="var(--muted)" style="font-size:16px">…</text><text x="608.5" y="308.5" text-anchor="middle" fill="var(--muted)" style="font-size:16px">…</text></svg><figcaption><strong>Notes Figure 1 for N = 5.</strong> The shaded period 0 ≤ n ≤ N−1 is the stored signal; red marks every copy of x[0], which stays at n = 0 under circular reversal while x[N−n] fills 1 ≤ n ≤ N−1.</figcaption></figure>

> [!question] Example 1 (slide 8) — circular shift and reversal
> $x[n]=\{\underset{\uparrow}{3},\ 1,\ 2,\ 4,\ 5\}$, length 5. Write the length-5 sequences (a) $x[\langle -n\rangle_5]$, (b) $x[\langle n+2\rangle_5]$, (c) $x[\langle 1-n\rangle_5]$.

> [!success]- Answer
> Reduce the index mod 5 for $n=0,\dots,4$:
> - (a) indices $0,4,3,2,1$: $\{\underset{\uparrow}{3},\ 5,\ 4,\ 2,\ 1\}$.
> - (b) indices $2,3,4,0,1$: $\{\underset{\uparrow}{2},\ 4,\ 5,\ 3,\ 1\}$ (circular advance by 2).
> - (c) indices $1,0,4,3,2$: $\{\underset{\uparrow}{1},\ 3,\ 5,\ 4,\ 2\}$ = (a) circularly delayed by 1, since $x[\langle 1-n\rangle_5]=x[\langle -(n-1)\rangle_5]$.

## 2. Circular convolution

z-transform and DTFT: $x*h\leftrightarrow X(z)H(z)$, $X_d(\omega)H_d(\omega)$. DFT: for length-$N$ $x,h$, what is the inverse DFT of $Y[k]=X[k]H[k]$?

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

> [!key] Circular convolution property (eqs. 15–16)
> $$
> x[n]\circledast h[n]\ \overset{\text{DFT}}{\longleftrightarrow}\ X[k]H[k]
> $$
> $$
> x[n]\circledast h[n]=\sum_{m=0}^{N-1}x[m]\,h[\langle n-m\rangle_N]=\sum_{m=0}^{N-1}h[m]\,x[\langle n-m\rangle_N]
> $$
> - Two length-$N$ inputs, length-$N$ output.
> - Unequal lengths: zero-pad the shorter one. $\circledast_N$: both padded to length $N$ (slide 10).

### 2.1 Computing circular convolution

$x[n]=\{\underset{\uparrow}{3},\ 1,\ 0,\ 3,\ 1,\ 1\}$, $h[n]=\{\underset{\uparrow}{-4},\ -1,\ -7,\ 5,\ 5,\ 1\}$, $N=6$ (eqs. 17–18).

**Modified table method.** [[1-signals-and-systems/04-impulse-response-and-convolution|Lecture 4]]'s flip-and-shift table, with the moving sequence periodically extended instead of zero-extended. Row $n$ holds $h[\langle n-m\rangle_6]$: row 0 is the circular reversal, each next row rotates right one place; $y[n]=\sum_m x[m]\,h[\langle n-m\rangle_6]$.

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

**Matrix method.** $\mathbf y=\tilde{\mathbf H}\mathbf x=\tilde{\mathbf X}\mathbf h$ (eq. 21), with **circulant** matrices: $\tilde{\mathbf H}_{nm}=h[\langle n-m\rangle_N]$. First row = circular reversal; each next row = previous one shifted right, last entry wrapped to the front; diagonals constant. The rows of $\tilde{\mathbf H}$ are the table rows.
$$
\begin{gathered}
\tilde{\mathbf H}=\begin{bmatrix}-4&1&5&5&-7&-1\\-1&-4&1&5&5&-7\\-7&-1&-4&1&5&5\\5&-7&-1&-4&1&5\\5&5&-7&-1&-4&1\\1&5&5&-7&-1&-4\end{bmatrix},\\
\mathbf y=\tilde{\mathbf X}\mathbf h=\begin{bmatrix}3&1&1&3&0&1\\1&3&1&1&3&0\\0&1&3&1&1&3\\3&0&1&3&1&1\\1&3&0&1&3&1\\1&1&3&0&1&3\end{bmatrix}\begin{bmatrix}-4\\-1\\-7\\5\\5\\1\end{bmatrix}=\begin{bmatrix}-4\\6\\-9\\2\\14\\-18\end{bmatrix}
\end{gathered}
$$

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
> Linear: $x*h=\{\underset{\uparrow}{8},\ 2,\ 4,\ 17,\ 7,\ 2,\ 8,\ 6,\ 0\}$, length $5+5-1=9$. The tail $n=5,\dots,8$ wraps onto $n=0,\dots,3$: $\{8+2,\ 2+8,\ 4+6,\ 17+0,\ 7\}$. In general $(x\circledast_N h)[n]=\sum_r (x*h)[n+rN]$ (time aliasing); padding both to $N\ge N_1+N_2-1$ (here 9) makes circular = linear.

## 3. More DFT properties

Same as the DTFT properties, with circular shifts.

- **Circular time shift** (eq. 25): linear phase in $k$, slope $-\frac{2\pi m}{N}$ ↔ shift by $m$ in $n$, circular because both domains are $N$-periodic.
- **Circular frequency shift** (eq. 26): linear phase in $n$ ↔ circular shift of $X[k]$; the dual of eq. 25.
- **Circular modulation** (eq. 27): the frequency shift applied to both exponentials of the cosine.
- **Reversal, conjugation** (eqs. 28–29): $X[\langle -k\rangle_N]$ is $X[0]$ at $k=0$, $X[N-k]$ otherwise. Real $x$: $X[k]=X^*[\langle -k\rangle_N]$.

**Table 1 — DFT properties** (length-$N$ signals):

| property | $x[n]$ | $X[k]$ |
|---|---|---|
| linearity | $ax_1[n]+bx_2[n]$ | $aX_1[k]+bX_2[k]$ |
| circular time shift | $x[\langle n-m\rangle_N]$ | $e^{-j\frac{2\pi mk}{N}}X[k]$ |
| circular frequency shift | $e^{j\frac{2\pi mn}{N}}x[n]$ | $X[\langle k-m\rangle_N]$ |
| circular modulation | $\cos\!\left(\frac{2\pi m}{N}n\right)x[n]$ | $\frac12X[\langle k+m\rangle_N]+\frac12X[\langle k-m\rangle_N]$ |
| circular time reversal | $x[\langle -n\rangle_N]$ | $X[\langle -k\rangle_N]$ |
| conjugation | $x^*[n]$ | $X^*[\langle -k\rangle_N]$ |
| duality | $X[n]$ | $N\,x[\langle -k\rangle_N]$ |
| circular convolution | $x[n]\circledast h[n]$ | $X[k]H[k]$ |
| windowing | $x[n]w[n]$ | $\frac1N X[k]\circledast W[k]$ |
| Parseval's theorem | $\sum_{n=0}^{N-1}x[n]y^*[n]$ | $\frac1N\sum_{k=0}^{N-1}X[k]Y^*[k]$ |
| Parseval's relation | $\sum_{n=0}^{N-1}\lvert x[n]\rvert^2$ | $\frac1N\sum_{k=0}^{N-1}\lvert X[k]\rvert^2$ |

Notes typos: p. 2 "refer to lecture 21" means Lecture 20 (its eqs. 13–17); the text under eq. 25 "slope $-2\pi m/M$" means $-2\pi m/N$.

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

> [!trap] Circular, not linear
> - $x[\langle -n\rangle_N]=\{x[0],x[N-1],\dots,x[1]\}$: $x[0]$ stays put; not the plain flip.
> - Remainders lie in $0,\dots,N-1$: $\langle -1\rangle_3=2$.
> - DFT shifts rotate: samples leaving one end re-enter at the other; length stays $N$.
> - $x\circledast h\ne x*h$ unless both are padded to $N\ge N_1+N_2-1$.
> - Exponent sign sets direction: $e^{-j\frac{2\pi mk}{N}}$ delays $x$ by $m$; $e^{+j\frac{2\pi mn}{N}}$ moves $X$ right by $m$.

> [!exam] Past Midterm 2 — DFT properties and circular convolution
> Read a permuted or phase-ramped DFT list as shifts, modulation, reversal; compare circular with linear convolution.
> [[exams/midterm-2/past-exams/spring-2025|SP2025 #1(b), #7(b), #8]] · [[exams/midterm-2/past-exams/fall-2024|FA2024 #8]] · [[exams/midterm-2/past-exams/fall-2023|FA2023 #7]] · [[exams/midterm-2/past-exams/spring-2023|SP2023 #1(d), #9(b)]] · [[exams/midterm-2/past-exams/fall-2021|FA2021 #3(b), #6]] · [[exams/midterm-2/past-exams/spring-2021|SP2021 #4, #5]] · [[exams/midterm-2/past-exams/fall-2019|FA2019 #1(g)–(h), #4, #11]]

## Related
[[concepts/circular-convolution|circular convolution]] · [[concepts/dft|DFT]] · [[concepts/convolution|convolution]] · [[concepts/dtft-properties|DTFT properties]] · [[5-dft-and-fft/20-discrete-fourier-transform|Lecture 20]] · unit: [[5-dft-and-fft/index|Unit 5]]

### Sources for this page
Snyder, ECE 310 Lecture 21 notes (§1–3, eqs. 1–29, Figure 1, Table 1) and slides (Examples 1–3), Oct 19, 2026; past Midterm 2 exams.
