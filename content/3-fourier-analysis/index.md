---
title: "Unit 3 · Fourier analysis and frequency response"
description: "Topics of Lectures 12–16: periodic signals, Fourier series to the DTFT, DTFT pairs and properties, the link to the z-transform, frequency response, magnitude, phase and group delay. Opens Midterm 2."
tags: [dtft, frequency-response, fourier-analysis]
---

*Unit 3 · Lectures 12–16 · Midterm 2 · prev: [[2-z-transform/index|Unit 2]] · next: [[4-sampling-and-reconstruction/index|Unit 4]]*

- What an LTI system does to each frequency: L13 builds the DTFT, L14 ties it to $X(z)$.
- L15–16: the DTFT of $h[n]$ is the frequency response $H_d(\omega)$: magnitude, phase, group delay.

**Midterm 2:** Wed Nov 4, 7–9 pm, Lectures 13–23 (this unit opens it) → [[exams/midterm-2/index|Midterm 2 review]].

## Topics

**Fourier analysis**
- [[concepts/periodic-signals|Periodic signals]] — $x[n+N_0]=x[n]$; periodic only if $\omega_0/2\pi$ is rational; $\omega_0$ and $\omega_0+2\pi$ coincide.
- [[concepts/fourier-series|Fourier series]] — harmonics by orthogonality; towards the DTFT.
- [[concepts/dtft|DTFT]] — $X_d(\omega)=\sum_n x[n]e^{-j\omega n}$ and inverse; $2\pi$-periodic; $=X(e^{j\omega})$ when the ROC contains the unit circle.
- [[concepts/dtft-pairs|DTFT pairs]] — $\delta$, $a^nu[n]$, pulse, $e^{j\omega_0n}$, cosine, sine, $u[n]$, ideal low-pass.
- [[concepts/dtft-properties|DTFT properties]] — shift, modulation, reversal, convolution, windowing, Parseval, Hermitian symmetry; $X_d(0)$, $X_d(\pi)$, $\int X_d$ for free.

**Frequency response**
- [[concepts/frequency-response|Frequency response]] — $e^{j\omega_0n}\mapsto H_d(\omega_0)e^{j\omega_0n}$; real $h$: cosine in, scaled shifted cosine out; $Y_d=H_dX_d$.
- [[concepts/magnitude-and-phase-response|Magnitude and phase]] — linear and dB magnitude; principal phase with jumps; FIR examples.
- [[concepts/group-delay|Group delay]] — $\tau_{gd}(\omega)=-\frac{d\angle H_d(\omega)}{d\omega}$; linear phase.
- [[concepts/template-matching|Template matching]] (L12, not tested) — matched filter $h[-n]$.

## Lectures
12. [[3-fourier-analysis/12-convolution-as-template-matching|Convolution as template matching]] (Sep 21)
13. [[3-fourier-analysis/13-fourier-analysis-and-the-dtft|Fourier analysis, DTFT]] (Sep 23)
14. [[3-fourier-analysis/14-dtft-properties|DTFT properties]] (Sep 25)
15. [[3-fourier-analysis/15-frequency-response|Frequency response]] (Oct 2)
16. [[3-fourier-analysis/16-magnitude-and-phase-response|Magnitude and phase]] (Oct 5, 7)

> [!key] The unit on one card
> - **DTFT:** $X_d(\omega)=\sum_{n=-\infty}^{\infty}x[n]\,e^{-j\omega n}$, $x[n]=\frac{1}{2\pi}\int_{-\pi}^{\pi}X_d(\omega)\,e^{j\omega n}\,d\omega$; $2\pi$-periodic; converges when $\sum_n\lvert x[n]\rvert\lt\infty$.
> - **From Unit 2:** $X_d(\omega)=X(z)\big|_{z=e^{j\omega}}$ only if the ROC contains the unit circle. $2^nu[n]$: no DTFT; $u[n]$: $\frac{1}{1-e^{-j\omega}}+\pi\delta(\omega)$, not $X(e^{j\omega})$.
> - **Pairs:** $\delta[n-n_0]\leftrightarrow e^{-j\omega n_0}$; $\;a^nu[n]\leftrightarrow\frac{1}{1-ae^{-j\omega}}$, $\lvert a\rvert\lt1$; $\;u[n]-u[n-L]\leftrightarrow e^{-j\omega(L-1)/2}\,\frac{\sin(L\omega/2)}{\sin(\omega/2)}$; $\;e^{j\omega_0n}\leftrightarrow2\pi\delta(\omega-\omega_0)$; $\;\cos(\omega_0n)\leftrightarrow\pi\big[\delta(\omega-\omega_0)+\delta(\omega+\omega_0)\big]$; $\;\frac{\sin(\omega_cn)}{\pi n}\leftrightarrow 1$ for $\lvert\omega\rvert\le\omega_c$, $0$ for $\omega_c\lt\lvert\omega\rvert\le\pi$.
> - **Properties:** $x[n-n_0]\leftrightarrow e^{-j\omega n_0}X_d(\omega)$; $\;e^{j\omega_0n}x[n]\leftrightarrow X_d(\omega-\omega_0)$; $\;x[n]\cos(\omega_0n)\leftrightarrow\frac12X_d(\omega-\omega_0)+\frac12X_d(\omega+\omega_0)$; $\;x[-n]\leftrightarrow X_d(-\omega)$; $\;x^*[n]\leftrightarrow X_d^*(-\omega)$; $\;n\,x[n]\leftrightarrow +j\,\frac{dX_d(\omega)}{d\omega}$ (L14 prints $-j$: erratum); $\;x[n]*h[n]\leftrightarrow X_d(\omega)H_d(\omega)$; $\;x[n]w[n]\leftrightarrow\frac{1}{2\pi}\int_{-\pi}^{\pi}X_d(\theta)\,W_d(\omega-\theta)\,d\theta$.
> - **Parseval:** $\sum_n\lvert x[n]\rvert^2=\frac{1}{2\pi}\int_{-\pi}^{\pi}\lvert X_d(\omega)\rvert^2\,d\omega$. **Hermitian:** real $x$ ⇒ $X_d(-\omega)=X_d^*(\omega)$. **Free values:** $X_d(0)=\sum_nx[n]$, $X_d(\pi)=\sum_n(-1)^nx[n]$, $\int_{-\pi}^{\pi}X_d(\omega)\,d\omega=2\pi\,x[0]$.
> - **Systems:** stable ⇒ $H_d(\omega)=H(e^{j\omega})$. $e^{j\omega_0n}\mapsto H_d(\omega_0)\,e^{j\omega_0n}$. Real $h$: $A\cos(\omega_0n+\theta)\mapsto A\,\lvert H_d(\omega_0)\rvert\cos\big(\omega_0n+\theta+\angle H_d(\omega_0)\big)$. $Y_d(\omega)=H_d(\omega)X_d(\omega)$.
> - **Magnitude, phase, delay:** $\lvert H_d\rvert\ge0$ (dB: $20\log_{10}\lvert H_d\rvert$); $\angle H_d\in[-\pi,\pi]$ jumps by $\pi$ where the real amplitude changes sign. $\tau_{gd}(\omega)=-\frac{d\angle H_d(\omega)}{d\omega}$; $h=\delta[n]-\delta[n-2]$: $H_d=2je^{-j\omega}\sin\omega$, $\lvert H_d\rvert=2\lvert\sin\omega\rvert$, $\tau_{gd}=1$.

> [!exam] Exam
> Opens Midterm 2 (18–42 points): [[problems/dtft-and-inverse-dtft|DTFTs and inverse DTFTs]] (L13–14) · [[problems/lti-response-to-sinusoids|response to sinusoids]] (L15) · [[problems/magnitude-phase-and-group-delay|magnitude, phase, group delay]] (L16). T/F: [[exams/midterm-2/true-false-bank|bank]] §1–3. Old MT1 items: [[exams/midterm-1/past-exams/spring-2023|SP2023 MT1]] #8–#9, [[exams/midterm-1/past-exams/fall-2019|FA2019 MT1]] #8–#9. Map: [[exams/midterm-2/index|Midterm 2]].

**Homework:** [[homework/hw5|HW5]] · [[homework/hw6|HW6]] · HW7 on [[exams/quiz-2|Quiz 2]] · **Demos:** [[demos/frequency-response-explorer|frequency-response explorer]] · [[demos/practice-drills|drills]] · [[supplements/demo-notebooks|notebooks]]

## Related
[[2-z-transform/index|Unit 2]] · [[4-sampling-and-reconstruction/index|Unit 4]] · [[concepts/index|Concepts]] · Unit 3 views of [[concepts/eigenfunctions-of-lti-systems|eigenfunctions]], [[concepts/region-of-convergence|ROC]], [[concepts/bibo-stability|BIBO stability]], [[concepts/poles-and-zeros|poles and zeros]] · [[supplements/transform-tables|transform tables]]

### Sources for this page
Snyder, ECE 310 Lectures 12–16 notes and slides (Fall 2026); HW5–HW7; past Midterm 2 exams; SP2023 and FA2019 Midterm 1 keys.
