---
title: "Template matching"
description: "Finding a known pattern by sliding it along a signal and scoring the overlap: the matched filter h[n] = t[−n], convolution vs correlation, peak height E_t = Σt² and where the peak lands, normalized correlation (Cauchy–Schwarz), 2-D kernels — and the same inner product behind Fourier coefficients and the DTFT. Not tested."
tags: [concept, convolution, template-matching, unit-3]
aliases: ["matched filter", "matched filters", "cross-correlation", "normalized cross-correlation", "template"]
---

> [!key] The matched filter (Lecture 12)
> To find copies of a template $t[n]$ in an input $x[n]$, convolve with the **flipped** template:
> $$
> h[n]=t[-n],\qquad y[n]=x[n]*h[n]=\sum_{k}x[k]\,t[k-n]=r_{xt}[n]\quad\text{(the cross-correlation of } x \text{ with } t\text{)}.
> $$
> $y[n]$ is the inner product of the input with the template placed at $n$: largest where the input looks like the template. An exact copy starting at $n_0$ gives the peak $y[n_0]=E_t=\sum_m t[m]^2$, the template's energy.

**Why it works.** Every convolution output is an inner product of the input with a flipped, shifted kernel, a similarity score. Flipping the template in advance cancels convolution's own flip, so the score compares the input with the template as drawn. By Cauchy–Schwarz, $|y[n]|\le\sqrt{\text{energy of the window}}\cdot\sqrt{E_t}$, with equality only when the window is a multiple of the template ([[3-fourier-analysis/12-convolution-as-template-matching|Lecture 12]]).

**When to use it.** Whenever the question is "where, and how strongly, does this known pattern occur?": a synchronization word in a data stream, a radar echo, a heartbeat, a shape in an image. In noise that is independent from sample to sample, the matched filter gives the best possible peak-to-noise ratio, $\sqrt{E_t}/\sigma$, of any linear filter: long or strong templates are easy to find.

> [!key] Normalized cross-correlation: score the shape, not the loudness
> $$
> \rho[n]=\frac{\sum_m x[n+m]\,t[m]}{\sqrt{\sum_m x[n+m]^2}\,\sqrt{\sum_m t[m]^2}}\in[-1,1],
> $$
> equal to $1$ exactly when the window under the template is a positive multiple of the template. The denominator's window energies come from one more convolution (a box of ones slid over $x^2$).

> [!example] The lecture's ramp, $t[n]=n/8$ for $0\le n\le 8$ ($E_t=\tfrac{204}{64}=3.1875$)
> Five copies in an 80-sample input give five peaks of height $3.19$ at the copies' first samples ($n=10,22,38,54,70$). A flat block of nine ones scores $4.5$, more than a perfect copy; a half-height copy scores $1.59$. Normalized, both copies score $1$ and the block at most $0.94$. Plots and code: [[3-fourier-analysis/12-convolution-as-template-matching|Lecture 12]], §2–3.

**In two dimensions** the kernel is flipped in both directions (a 180° rotation), centred on its sample $h[0,0]$, and slid over the image; pixels outside the image count as $0$. Symmetric kernels, like the lecture's $\begin{bmatrix}0&-1&0\\-1&2&-1\\0&-1&0\end{bmatrix}$ and its $5\times5$ line detectors $h_v$, $h_h$, do not care about the flip. Shape templates light up at shape centres; feature kernels highlight strokes of handwritten digits; convolutional neural networks learn their kernels from data.

**The same idea in frequency.** A Fourier coefficient is a template score with a harmonic as the template, $c_k=\frac{1}{T_0}\int_{T_0}x(t)e^{-jk\Omega_0t}dt$, and the DTFT is one with a complex exponential, $X_d(\omega)=\sum_nx[n]e^{-j\omega n}=\langle x,e^{j\omega n}\rangle$ ([[concepts/fourier-series|Fourier series]], [[concepts/dtft|DTFT]]). Because harmonics are orthogonal, these templates do not respond to each other. And a filter responds to the frequencies its impulse response resembles: the frequency response $H_d(\omega)=\sum_kh[k]e^{-j\omega k}$ is the score of $h$ against $e^{j\omega k}$ (the moving average $\{\underset{\uparrow}{1},1,1,1\}$ scores $4$ at $\omega=0$ and $0$ at $\omega=\frac{\pi}{2}$ and $\pi$).

> [!trap]
> - **Convolution flips, correlation does not.** Convolving with the template itself, $x*t$, looks for the *reversed* pattern. Only symmetric templates ($t[-n]=t[n]$) make the two operations agree. With the asymmetric kernel $[\,1\ \ \underline{0}\ \ {-1}\,]$, correlation and convolution give opposite signs.
> - **Where the peak lands.** With $h[n]=t[-n]$ the peak sits on the copy's first sample (for a template that starts at $m=0$). A computer stores the flipped template as an array starting at index $0$, which delays everything by the template width $W$: the lecture's plot shows the peaks at the copies' *last* samples ($18,30,46,62,78$). Index $m$ of `np.convolve(x, t[::-1])` is $n=m-W$.
> - **Loud is not similar.** Raw scores grow with amplitude; a bright region that vaguely resembles the template can beat a faint exact copy. Normalize, or at least compare peaks of similar energy. (The notes' shape example shows the effect: triangles are "fairly bright" in the diamond response.)
> - **Normalized is not foolproof.** $\rho$ ignores amplitude, so a quiet stretch of noise that happens to resemble the template scores high too; practical detectors also require enough energy, and often subtract the window mean first.

**Where it appears.**
- Lectures: [[3-fourier-analysis/12-convolution-as-template-matching|Lecture 12]] (the whole lecture: matched filters, normalization, 2-D convolution, shapes and digit features), [[3-fourier-analysis/13-fourier-analysis-and-the-dtft|Lecture 13]] (Fourier coefficients and the DTFT as inner products with harmonics), [[1-signals-and-systems/04-impulse-response-and-convolution|Lecture 4]] (the flip-and-slide mechanics).
- Exams and homework: **not tested** ("this lecture will not be tested on homeworks or exams"). The tested material that rests on the same inner product is the DTFT: [[problems/dtft-and-inverse-dtft|computing DTFTs and inverse DTFTs]], [[homework/hw5|HW5]].
- Try it: the [[demos/convolution-explorer|convolution explorer]] (watch the flipped kernel slide over the input).

Related: [[concepts/convolution|convolution]] · [[concepts/impulse-response|impulse response]] · [[concepts/lti-system|LTI system]] · [[concepts/dtft|DTFT]] · [[concepts/fourier-series|Fourier series]] · [[concepts/frequency-response|frequency response]]

### Sources for this page
Lecture 12 notes (§1.1 matched filters, eqs. 1–2; §2 two-dimensional convolution, eq. 3; §2.1–2.2 shape templates and digit features, eqs. 4–5) and slides 3–14; Lecture 13 notes §2 (Fourier coefficients). Normalized correlation, the peak-position bookkeeping and the noise remarks are additions to the lecture. All numbers are checked in `verify/LA_l12.py`.
