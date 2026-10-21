---
title: "Template matching"
description: "Finding a known pattern by sliding it along a signal: the matched filter h[n] = t[−n], convolution vs correlation, peak height E_t, 2-D kernels, and the same inner product behind the DTFT. Not tested."
tags: [concept, convolution, template-matching, unit-3]
aliases: ["matched filter", "matched filters", "cross-correlation", "normalized cross-correlation", "template"]
---

> [!key] The matched filter (Lecture 12)
> $$
> h[n]=t[-n],\qquad y[n]=x[n]*h[n]=\sum_{k}x[k]\,t[k-n]
> $$
> $y[n]$ is the inner product of the input with the template placed at $n$. An exact copy starting at $n_0$ gives the peak $y[n_0]=E_t=\sum_m t[m]^2$.

- **Why:** every convolution output is a similarity score; flipping the template cancels convolution's flip. Cauchy–Schwarz: equality only when the window is a multiple of the template.
- **Lecture's ramp** $t[n]=n/8$, $0\le n\le 8$ ($E_t=3.1875$): five copies give peaks $3.19$; a block of nine ones scores $4.5$ (loud is not similar); a half-height copy $1.59$.
- **2-D:** kernel flipped both ways, centred on $h[0,0]$; symmetric kernels ignore the flip.
- **Frequency:** $X_d(\omega)=\sum_nx[n]e^{-j\omega n}$ is a template score against $e^{j\omega n}$; $H_d(\omega)$ scores $h$ against $e^{j\omega k}$.

> [!trap]
> - Convolution flips, correlation does not; $x*t$ finds the reversed pattern unless $t$ is symmetric.
> - `np.convolve(x, t[::-1])` delays by the template width $W$: index $m$ is $n=m-W$.

**Where it appears:** [[3-fourier-analysis/12-convolution-as-template-matching|Lecture 12]] (not tested), [[3-fourier-analysis/13-fourier-analysis-and-the-dtft|Lecture 13]]; [[demos/convolution-explorer|convolution explorer]].

## Related
[[concepts/convolution|convolution]] · [[concepts/impulse-response|impulse response]] · [[concepts/dtft|DTFT]] · [[concepts/fourier-series|Fourier series]] · [[concepts/frequency-response|frequency response]]

### Sources for this page
Lecture 12 notes §1.1–2.2 (eqs. 1–5), slides 3–14; Lecture 13 notes §2.
