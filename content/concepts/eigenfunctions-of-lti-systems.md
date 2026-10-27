---
title: "Eigenfunctions of LTI systems"
description: "Feed zⁿ (all n) into an LTI system and zⁿ comes out scaled by H(z): why the z-transform exists, convolution becomes multiplication, a zero blocks and a pole resonates."
tags: [concept, systems, z-transform, midterm-1]
aliases: ["eigenfunction", "eigenfunctions", "eigenvalue", "eigensequence", "eigensignal"]
---

*Lecture 6 (Fri Sep 4) §1 · also Lecture 9 §1, Lecture 11 §1.2.1, Lecture 15 §1 · family: [[problems/unbounded-outputs-and-pole-matching|unbounded outputs and pole matching]]*

> [!abstract] In one breath
> - $z_0^{\,n}$ for all $n$ through any LTI system comes out as $H(z_0)\,z_0^{\,n}$: same shape, scaled by the eigenvalue $H(z_0)=\sum_k h[k]z_0^{-k}$.
> - That eigenvalue, as a function of $z$, is the transfer function; it is why convolution becomes multiplication.
> - On the unit circle it is the frequency response $H_d(\omega)$ of Unit 3.

## 1. Motivation: inputs whose shape no LTI system changes

- Convolution gives any output; LCCDEs give $h[n]$. Neither says *what a system does* (slide 3: $h[n] = (\tfrac12)^n u[n]$).
- Wanted: inputs that come out only **scaled**: $y[n] = x[n] * h[n] = A(x[n])\,x[n]$ (Lecture 6, eqs. 1–2).
- Needs $x[n-k]$ to split into an $n$-part and a $k$-part: $z^{n-k} = z^n z^{-k}$. Slide example: $z_0 = 1 + j2$.

> [!key] Complex exponentials are eigenfunctions of LTI systems (Lecture 6, eqs. 5–7)
> For an LTI system with impulse response $h$ and any $z_0$ in the ROC of $H(z)$:
> $$
> \begin{gathered}
> x[n]=z_0^{\,n}\ \ (-\infty<n<\infty)\quad\Longrightarrow\\[4pt]
> y[n]=\sum_{k=-\infty}^{\infty}h[k]\,z_0^{\,n-k}=\Big(\sum_{k=-\infty}^{\infty}h[k]\,z_0^{-k}\Big)z_0^{\,n}=H(z_0)\,z_0^{\,n},\qquad\forall n .
> \end{gathered}
> $$
> - $H(z_0)$ depends on $h$ and $z_0$ only, not on $n$: the **eigenvalue**. $H(z)$ is the [[concepts/transfer-function|transfer function]] (the [[concepts/z-transform|z-transform]] of $h$).
> - Holds only for inputs defined for **all** $n$, and only if the sum converges ($z_0$ in the ROC of $H$).

Sums of exponentials pass term by term (eqs. 8–9):
$$
x[n]=\sum_{k=1}^{K}b_k\,z_k^{\,n}\quad\Longrightarrow\quad y[n]=\sum_{k=1}^{K}H(z_k)\,b_k\,z_k^{\,n}.
$$
Slide 6: $\lvert H(z_k)\rvert > 1$ amplifies, $0 < \lvert H(z_k)\rvert < 1$ attenuates, $H(z_k) = 0$ removes the $z_k$ component (filtering).

## 2. Why the z-transform works

$H(z)=\sum_k h[k]z^{-k}$ is *defined* as that eigenvalue. Think of a signal as a combination of exponentials $z^n$ with weights $X(z)$; the system multiplies each weight by $H(z)$, which is why convolution in time becomes multiplication, $Y(z)=H(z)X(z)$ (Lecture 9 §1).

> [!question] $h[n]=(\frac12)^nu[n]$, $H(z)=\frac{1}{1-\frac12z^{-1}}$, ROC $\lvert z\rvert>\frac12$. Outputs for $x[n]=2^n$ (all $n$), $x[n]=(\frac14)^n$ (all $n$), $x[n]=u[n]$; and the constant $1$ into $y[n]=x[n]-x[n-1]$?

> [!success]- Answers
> - $x[n]=2^n$: $y[n]=H(2)\,2^n=\frac{1}{1-1/4}\,2^n=\frac43\,2^n$.
> - $x[n]=(\frac14)^n$: $z_0=\frac14$ is **outside** the ROC, and $\sum_k(\frac12)^k(\frac14)^{n-k}=(\frac14)^n\sum_{k\ge0}2^k$ diverges. The formula's value $H(\frac14)=-1$ means nothing here.
> - $x=u[n]$ is **not an eigenfunction**: $y=2u[n]-(\frac12)^nu[n]$, the "eigen" part $H(1)u[n]$ plus a transient from the pole at $\frac12$.
> - **A zero blocks**: $H(z)=1-z^{-1}$, $H(1)=0$, so the constant input gives $y=0$.

## 3. In Unit 3: the frequency response

On the unit circle, $z_0=e^{j\omega}$, the eigenvalue gets its own name: $H_d(\omega)=\sum_k h[k]\,e^{-j\omega k}$, the [[concepts/frequency-response|frequency response]], equal to $H(e^{j\omega})$ for a stable system (ROC contains every $e^{j\omega}$). So $e^{j\omega_0n}\mapsto H_d(\omega_0)\,e^{j\omega_0n}$, and for real $h$ a sinusoid leaves as $A\cos(\omega_0n+\theta)\mapsto A\lvert H_d(\omega_0)\rvert\cos\big(\omega_0n+\theta+\angle H_d(\omega_0)\big)$: same frequency, new amplitude and phase ([[concepts/magnitude-and-phase-response|magnitude and phase response]]). The full version is on the [[concepts/frequency-response|frequency response]] page (Lecture 15 §1). The cosine itself is not an eigenfunction unless its two eigenvalues happen to be equal, which [[exams/midterm-2/past-exams/fall-2021|FA2021 MT2]] #1(a) tests.

> [!trap]
> - **"For all $n$" is essential** (Lecture 6): $z_0^nu[n]$ is not an eigenfunction; switching on at $n=0$ adds transients from the poles of $H$.
> - **$z_0$ must lie in the ROC of $H$**, otherwise the sum defining the output diverges.
> - **A cosine is two eigenfunctions** with eigenvalues $H(e^{j\omega_0})$ and $H(e^{-j\omega_0})$; an LTI system never creates a frequency that is not in its input.
> - **$e^{j\omega n}$ for all $n$ has an empty ROC** ([[exams/midterm-1/past-exams/spring-2025|SP2025 #1c]] T), yet it is an eigenfunction: the eigen relation needs the ROC of $H$, not a transform of the input.
> - **At a pole the eigenvalue is infinite**: a one-sided input whose exponential sits on a unit-circle pole of $H$ resonates and grows like $n\,z_0^n$ ([[concepts/marginal-stability|marginal stability]]).

> [!exam] On the exams
> Eigen relation as T/F, and as the mechanism behind pole matching (Lecture 11).
> [[exams/midterm-1/past-exams/spring-2025|SP2025 #1c, #6]] · [[exams/midterm-1/past-exams/fall-2025|FA2025 #8b]] · [[exams/midterm-1/past-exams/spring-2021|SP2021 #5b]] · [[exams/midterm-2/past-exams/fall-2021|FA2021 MT2 #1a]]

**Where it appears:** [[2-z-transform/06-the-z-transform|Lecture 6]] §1 (eqs. 1–9), [[2-z-transform/09-transfer-functions|Lecture 9]] §1 ($Y=HX$), [[2-z-transform/11-bibo-stability-and-causality|Lecture 11]] §1.2.1 (resonance of $e^{j\omega n}u[n]$), [[3-fourier-analysis/15-frequency-response|Lecture 15]] §1; family [[problems/unbounded-outputs-and-pole-matching|Unbounded outputs and pole matching]].

## Related
[[concepts/complex-exponential|complex exponential]] · [[concepts/transfer-function|transfer function]] · [[concepts/z-transform|z-transform]] · [[concepts/lti-system|LTI system]] · [[concepts/convolution|convolution]] · [[concepts/poles-and-zeros|poles and zeros]] · [[concepts/marginal-stability|marginal stability]] · [[concepts/frequency-response|frequency response]]

### Sources for this page
Lecture 6 notes §1 (eqs. 1–9) and slides 3–6; Lecture 9 §1; Lecture 11 §1.2.1 (eqs. 24–28); Lecture 15 §1; SP2025 #1c and #6, FA2025 #8b, FA2021 MT2 #1(a).
