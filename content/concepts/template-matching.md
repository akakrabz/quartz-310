---
title: "Template matching"
description: "Finding a known pattern by sliding it along a signal: convolution as an inner product, the matched filter h[n] = t[−n], peak height and position, 2-D image kernels, the inner product behind the DTFT."
tags: [concept, convolution, template-matching, unit-3]
aliases: ["matched filter", "matched filters", "cross-correlation", "normalized cross-correlation", "template", "2-D convolution", "two-dimensional convolution", "image kernel"]
---

*Lecture 12 (Mon Sep 21), all sections · not tested on homework or exams (notes and slide 2) · bridge from [[concepts/convolution|convolution]] to the [[concepts/dtft|DTFT]]*

> [!abstract] In one breath
> - Each convolution output is an inner product of the input with the flipped, shifted kernel: a similarity score.
> - Matched filter $h[n]=t[-n]$: the flips cancel, the template itself slides, the output peaks at copies of $t$.
> - In 2-D the same flip–slide–multiply–add runs a kernel over an image: shape templates, line features.

## 1. Convolution as an inner product

$y[n]=\sum_k x[k]\,h[n-k]$ with $n$ frozen is an inner product in $k$ (Lecture 12 §1):

$$
\langle a,b\rangle=\sum_k a[k]\,b[k],\qquad\quad y[n]=\big\langle\, x[k],\ h[n-k]\,\big\rangle_k .
$$

Large when both sequences are big in the same places with the same signs, zero when orthogonal, negative when opposite. Filtering and pattern finding are the same computation read two ways. Known pattern → use it as a template, drag it along the signal, find where it lines up best; reverse it first, because convolution flips.

> [!question] Slide 5: at each shift location, what operation does convolution perform?

> [!success]- Answer
> An inner (dot) product: multiply input and flipped, shifted kernel sample by sample, add. Its size measures the **correlation** (alignment) at that shift (notes §1.1).

## 2. Matched filters

> [!key] The matched filter (Lecture 12, eqs. 1–2, slide 4)
> $$
> \begin{gathered}
> h[n]=t[-n]\qquad\text{(the matched filter for the template } t\text{)}\\[4pt]
> y[n]=x[n]*h[n]=\sum_{k=-\infty}^{\infty}x[k]\,h[n-k]=\sum_{k=-\infty}^{\infty}x[k]\,t[k-n].
> \end{gathered}
> $$
> $t[k-n]$ is the template with sample $0$ moved to $k=n$; the output is largest where the input looks most like the template. The notes call the pattern $h[n]$ and the filter $\tilde h[n]$.

- The last sum is the **cross-correlation** of $x$ with $t$: $r_{xt}[n]=\sum_k x[k]\,t[k-n]=x[n]*t[-n]$.
- An exact copy $x[n_0+m]=t[m]$ scores $E_t=\sum_m t[m]^2$; by Cauchy–Schwarz no window of the same energy scores more, with equality only when the window is a multiple of the template.
- Raw scores also grow with loudness: a bright stretch can beat a faint exact copy (why the notes' triangles look "fairly bright" to the diamond template, §4). Dividing by the window energy (normalized cross-correlation) fixes it.

> [!example] The lecture's sawtooth (slides 3–5, notes Figs. 1–2)
> Template: ramp $t[n]=n/8$, $0\le n\le 8$ (width $W=8$), $E_t=\sum_{n=0}^{8}(n/8)^2=\tfrac{204}{64}=3.1875$. Input: 80 samples, five copies starting at $n=10,22,38,54,70$. Output: five equal peaks of height $3.19$; between the first two copies (12 samples apart) it dips only to $0.72$, because the responses overlap. A block of nine ones scores $4.5$ (loud is not similar); a half-height copy $1.59$.

- With $h[n]=t[-n]$ exactly, peaks sit on the **first** sample of each copy ($n=10,22,\dots$). The slide plot shows $18,30,46,62,78$, the **last** samples: a stored array is the causal $h[n-W]$, so the output is delayed by $W=8$ ("accounting for the width of the template").

## 3. Two-dimensional convolution

> [!key] 2-D convolution (Lecture 12, eq. 3)
> $$
> y[i,j]=x[i,j]*h[i,j]=\sum_{k=-\infty}^{\infty}\sum_{m=-\infty}^{\infty}x[k,m]\,h[i-k,\,j-m].
> $$
> Image $x$: $H\times W$, row $i$, column $j$. Flip the kernel in both directions (180°), centre it on $(i,j)$, multiply, add.

- Centre sample (underlined) is $h[0,0]$: the kernel is non-causal, harmless for images ("future" samples are the next row or column).
- Pixels outside the image count as $0$ (**zero-extension**).
- Symmetric kernels ignore the flip.

> [!question] Slide 6 (notes Fig. 3): compute three output pixels
> $$
> h=\begin{bmatrix}0&-1&0\\-1&\underline{2}&-1\\0&-1&0\end{bmatrix},\qquad
> x=\begin{bmatrix}1&6&3&9&6&2&4\\9&\mathbf{6}&4&4&3&7&6\\2&3&4&1&2&3&\mathbf{8}\\7&4&0&2&2&4&3\\5&6&5&\mathbf{8}&0&0&3\\2&1&4&1&5&8&7\\7&3&8&0&3&1&9\end{bmatrix}
> $$
> $y=x*h$ at the bold pixels: row 1, column 1 (orange); row 4, column 3 (yellow); row 2, column 6 (green, border). Rows and columns from 0.

> [!success]- Answer
> The kernel is unchanged by a 180° rotation: output = twice the centre minus its four neighbours.
> - orange: $2(6)-(6+9+4+3)=12-22=-10$
> - yellow: $2(8)-(2+5+0+1)=16-8=8$
> - green: $2(8)-(6+3+3+0)=16-12=4$ (the $0$ is the missing right neighbour, zero-extension).

## 4. Two-dimensional pattern matching

Slides 7–10, notes Figs. 4–6: an image of triangles, diamonds and boxes; one template per shape. Each response image is brightest at the centres of the matching shapes; diamond and box responses have exactly one brightest pixel per shape. Triangles are also "fairly bright" in the diamond response, but the maxima sit on the true diamonds.

## 5. Highlighting features in handwritten digits

Whole-digit templates fail on handwriting variation (crossed sevens, looped twos, open fours, size, slant). Match simple **features** instead (slides 11–14, Lecture 12, eqs. 4–5):

$$
h_v=\begin{bmatrix}-2&1&1&1&-2\\-2&1&1&1&-2\\-2&1&\underline{1}&1&-2\\-2&1&1&1&-2\\-2&1&1&1&-2\end{bmatrix},\qquad
h_h=\begin{bmatrix}-2&-2&-2&-2&-2\\1&1&1&1&1\\1&1&\underline{1}&1&1\\1&1&1&1&1\\-2&-2&-2&-2&-2\end{bmatrix}.
$$

- Positive entries want bright pixels, negative want dark, zeros "don't care". $h_v$: a vertical bar with dark sides; $h_h$: a horizontal one.
- MNIST (notes Figs. 7–9): the "1" responds almost only to $h_v$; the "7" to both (tall stroke, top bar); the "4" strongly to $h_v$ and to $h_h$ along its crossbar.
- Hand-designing many kernels is hard; convolutional neural networks **learn** them.

## 6. The same inner product in frequency

The [[concepts/dtft|DTFT]] $X_d(\omega)=\sum_n x[n]\,e^{-j\omega n}$ scores a signal against the templates $e^{j\omega n}$ (Lecture 14 §1.1: $X_d(\omega)=\mathbf{v}^*\mathbf{u}$); the [[concepts/frequency-response|frequency response]] $H_d(\omega)$ scores $h$ against $e^{j\omega k}$. Fourier analysis is template matching with one template per frequency ([[concepts/fourier-series|Fourier series]]).

> [!trap]
> - $x*t$ (no flip) compares the input with the **reversed** template; use $x*t[-n]$. Symmetric templates ($t[-n]=t[n]$): convolution and correlation coincide.
> - `np.convolve(x, t[::-1])` delays by the template width $W$: index $m$ is $n=m-W$.
> - Raw correlation rewards loudness; normalize by window energy to rank similarity.

**Where it appears:** [[3-fourier-analysis/12-convolution-as-template-matching|Lecture 12]] (not tested), [[3-fourier-analysis/13-fourier-analysis-and-the-dtft|Lecture 13]], [[3-fourier-analysis/14-dtft-properties|Lecture 14]] §1.1; [[demos/convolution-explorer|convolution explorer]], [[demos/python-demos|Python demos]].

## Related
[[concepts/convolution|convolution]] · [[concepts/impulse-response|impulse response]] · [[concepts/lti-system|LTI system]] · [[concepts/dtft|DTFT]] · [[concepts/fourier-series|Fourier series]] · [[concepts/frequency-response|frequency response]] · [[1-signals-and-systems/04-impulse-response-and-convolution|Lecture 4]]

### Sources for this page
Lecture 12 notes §1–2.2 (eqs. 1–5, Figs. 1–9), slides 1–14 (unannotated; slide 5 and 6 answers ours); Lecture 13 notes §2; Lecture 14 §1.1.
