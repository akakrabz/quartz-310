---
title: "Eigenfunctions of LTI systems"
description: "Feed zⁿ (for all n) into an LTI system and zⁿ comes out, scaled by H(z): the reason the z-transform exists, why convolution becomes multiplication, why a zero blocks an exponential and a pole resonates with it."
tags: [concept, systems, z-transform, midterm-1]
aliases: ["eigenfunction", "eigenfunctions", "eigenvalue", "eigensequence", "eigensignal"]
---

> [!key] $z^n$ in, $H(z)\,z^n$ out (Lecture 6 §1)
> For an LTI system with impulse response $h$ and any $z_0$ in the ROC of $H(z)$:
> $$
> \begin{gathered}
> x[n]=z_0^n\ \ (-\infty<n<\infty)\quad\Longrightarrow\\[4pt]
> y[n]=\sum_k h[k]\,z_0^{\,n-k}=\Big(\sum_k h[k]\,z_0^{-k}\Big)z_0^n=H(z_0)\,z_0^n .
> \end{gathered}
> $$
> The input keeps its shape; only the complex number $H(z_0)$, the **eigenvalue**, multiplies it. Sums pass term by term: $x=\sum_k b_k z_k^n\Rightarrow y=\sum_k H(z_k)\,b_k z_k^n$. On the unit circle, $z_0=e^{j\omega}$ gives $e^{j\omega n}\mapsto H(e^{j\omega})\,e^{j\omega n}$: the [[concepts/frequency-response|frequency response]] of Unit 3 (see *In Unit 3* below).

**Why the z-transform works.** $H(z)=\sum_k h[k]z^{-k}$ is *defined* as that eigenvalue: this is the [[concepts/transfer-function|transfer function]]. Think of a signal as a combination of exponentials $z^n$ with weights $X(z)$; the system multiplies each weight by $H(z)$, which is why convolution in time becomes multiplication, $Y(z)=H(z)X(z)$.

**Worked example.** $h[n]=(\frac12)^nu[n]$, $H(z)=\frac{1}{1-\frac12z^{-1}}$, ROC $\lvert z\rvert>\frac12$.
- $x[n]=2^n$ for all $n$: $y[n]=H(2)\,2^n=\frac{1}{1-1/4}\,2^n=\frac43\,2^n$.
- $x[n]=(\frac14)^n$ for all $n$: $z_0=\frac14$ is **outside** the ROC, and $\sum_k(\frac12)^k(\frac14)^{n-k}=(\frac14)^n\sum_{k\ge0}2^k$ diverges. The formula's value $H(\frac14)=-1$ means nothing here.
- **A zero blocks**: $y[n]=x[n]-x[n-1]$ has $H(z)=1-z^{-1}$, $H(1)=0$, so the constant input $x[n]=1$ gives $y=0$.
- **One-sided inputs are not eigenfunctions**: $x=u[n]$ gives $y=2u[n]-(\frac12)^nu[n]$: the "eigen" part $H(1)u[n]$ plus a transient from the pole at $\frac12$.

> [!trap]
> - **"For all $n$" is essential** (Lecture 6): $z_0^nu[n]$ is not an eigenfunction; its response carries transients from the poles of $H$.
> - **$z_0$ must lie in the ROC of $H$**, otherwise the sum defining the output diverges.
> - **A cosine is two eigenfunctions** with eigenvalues $H(e^{j\omega_0})$ and $H(e^{-j\omega_0})$. For real $h$ the output is $\lvert H(e^{j\omega_0})\rvert\cos\!\big(\omega_0n+\angle H(e^{j\omega_0})\big)$: same frequency, new amplitude and phase. An LTI system never creates a frequency that is not in its input.
> - **$e^{j\omega n}$ for all $n$ has an empty ROC** ([[exams/midterm-1/past-exams/spring-2025|SP2025 #1c]] T), yet it is an eigenfunction: the eigen relation needs the ROC of $H$, not a transform of the input.
> - **At a pole the eigenvalue is infinite**: a one-sided input whose exponential sits on a unit-circle pole of $H$ resonates and grows like $n\,z_0^n$ ([[concepts/marginal-stability|marginal stability]]; [[exams/midterm-1/past-exams/spring-2025|SP2025 #6]], [[exams/midterm-1/past-exams/fall-2025|FA2025 #8b]]).

**In Unit 3.** On the unit circle the eigenvalue gets its own name: $H_d(\omega)=\sum_k h[k]\,e^{-j\omega k}$, the [[concepts/frequency-response|frequency response]], equal to $H(e^{j\omega})$ for a stable system (whose ROC contains every $e^{j\omega}$). So $e^{j\omega_0n}\mapsto H_d(\omega_0)\,e^{j\omega_0n}$, and for real $h$ a sinusoid leaves as $A\cos(\omega_0n+\theta)\mapsto A\lvert H_d(\omega_0)\rvert\cos\big(\omega_0n+\theta+\angle H_d(\omega_0)\big)$: same frequency, scaled by the [[concepts/magnitude-and-phase-response|magnitude response]] and shifted by the phase response. [[3-fourier-analysis/15-frequency-response|Lecture 15]] builds the frequency-domain view of LTI systems on exactly this property. The cosine itself is not an eigenfunction unless its two eigenvalues happen to be equal, which [[exams/midterm-2/past-exams/fall-2021|FA2021 MT2]] #1(a) tests.

**Where it appears.** [[2-z-transform/06-the-z-transform|Lecture 6]] §1 (Eqs. 1–9, the motivation for the z-transform), [[2-z-transform/09-transfer-functions|Lecture 9]] §1 ($Y=HX$), [[2-z-transform/11-bibo-stability-and-causality|Lecture 11]] §1.2.1 (resonance of $e^{j\omega n}u[n]$). Exams: [[exams/midterm-1/past-exams/spring-2025|SP2025 #1c, #6]], [[exams/midterm-1/past-exams/fall-2025|FA2025 #8]], [[exams/midterm-1/past-exams/spring-2021|SP2021 #5b]]; family [[problems/unbounded-outputs-and-pole-matching]].

**Related.** [[concepts/complex-exponential|complex exponential]] · [[concepts/transfer-function|transfer function]] · [[concepts/z-transform|z-transform]] · [[concepts/lti-system|LTI system]] · [[concepts/convolution|convolution]] · [[concepts/poles-and-zeros|poles and zeros]] · [[concepts/marginal-stability|marginal stability]]

### Sources for this page
Lecture 6 §1 (Eqs. 1–9 and the eigenfunction paragraph); Lecture 9 §1; Lecture 11 §1.2.1 (Eqs. 24–28); SP2025 #1c and #6, FA2025 #8b. The example values are checked in `verify/concepts/verify_glossary_time.py` and `verify_stability.py`. The *In Unit 3* paragraph: Lecture 15 §1 (frequency response as the eigenvalue, sinusoidal response); FA2021 MT2 #1(a); checked in `verify/CLEAN_unit3.py`.
