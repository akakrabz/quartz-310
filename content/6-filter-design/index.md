---
title: "Unit 6 · Filter design"
description: "Lecture 27 so far: ideal low-pass, high-pass, band-pass and band-stop filters and why they are unattainable; passband ripple, stopband attenuation and transition band; direct form I and II. FIR and IIR design follow in Lectures 28–29."
tags: [filter-design]
---

*Unit 6 · Lecture 27 (Mon Nov 9) onward · prev: [[5-dft-and-fft/index|Unit 5]] · in progress: the instructor plans Lectures 27–29 for filter design (Lecture 28 over two class days), then a last unit on multirate signal processing · all of it is after Midterm 2*

- So far "filter" meant any LTI system we happened to analyse. Now the direction is reversed: given what should pass and what should be removed, **design** the system.
- The ideal answer, a box in frequency, is a sinc in time: endless, two-sided, not summable. Every real filter is an approximation, and the unit's vocabulary (ripple, attenuation, transition band) measures how good the approximation is.
- Whatever is designed ends up as an [[concepts/lccde|LCCDE]], [[concepts/fir-and-iir|FIR or IIR]], and is wired as a direct form.

## Topics

| topic | one line |
|---|---|
| [[concepts/ideal-filters\|Ideal filters]] | low-pass, high-pass, band-pass, band-stop; $h_{lpf}[n]=\frac{\sin(\omega_cn)}{\pi n}$: infinite, non-causal, unstable; $h_{hpf}=\delta[n]-h_{lpf}[n]$ |
| [[concepts/filter-specifications\|Filter specifications]] | passband ripple, stopband attenuation ($-20$ dB $=\frac1{10}$, $-40$ dB $=\frac1{100}$), transition bandwidth $\lvert\omega_p-\omega_s\rvert$; scenario → type and edges with $\omega=\frac{2\pi f}{f_s}$ |
| [[concepts/direct-form-structures\|Direct form I and II]] | flow graphs of $y[n]=\sum b_iy[n-i]+\sum c_jx[n-j]$; I: $K+M-1$ delays; II: one shared delay line, $\max(K,M-1)$ delays |
| [[concepts/fir-and-iir\|FIR and IIR]] (Unit 1) | the two families every design falls into; FIR: no feedback, always stable |
| [[concepts/block-diagram\|Block diagram]] (Unit 1) | Lecture 5's delay, gain and adder blocks; direct form I in box notation |

## Lectures

| # | page | one line |
|---|---|---|
| 27 | [[6-filter-design/27-practical-filter-design\|Practical filter design]] | Mon Nov 9: ideal filters and their three problems; specifications of a practical filter; choosing a filter for a scenario; direct form I (direct form II: Nov 11) |

> [!key] The unit on one card (so far)
> - **Ideal low-pass:** $H_{lpf}(\omega)=1$ for $\lvert\omega\rvert\le\omega_c$, else 0 ↔ $h_{lpf}[n]=\frac{\sin(\omega_cn)}{\pi n}=\frac{\omega_c}{\pi}\mathrm{sinc}(\omega_cn)$. Infinite with no LCCDE, non-causal, not BIBO stable.
> - **From a low-pass:** $H_{hpf}=1-H_{lpf}$ ↔ $\delta[n]-h_{lpf}[n]$; band-pass by $\cos(\omega_0n)\,h_{lpf}[n]$; band-stop $=1-$ band-pass.
> - **Specifications:** passband ripple (variation of the passband gain), stopband attenuation (highest stopband gain, in dB: $20\log_{10}\lvert H_d\rvert$), transition bandwidth $\lvert\omega_p-\omega_s\rvert$. Narrower transition ⇔ weaker attenuation.
> - **Scenario → filter:** $\omega=\Omega T=\frac{2\pi f}{f_s}$; passband edge on what you keep, stopband edge on what you remove.
> - **Direct forms** of $H(z)=\frac{\sum c_jz^{-j}}{1-\sum b_iz^{-i}}$: I uses a delay line on $x$ and one on $y$; II uses one line on $v[n]$ with $v[n]=x[n]+\sum b_iv[n-i]$, $y[n]=\sum c_jv[n-j]$.

> [!exam] Final exam
> Announced Nov 9: the final is expected to be one third Midterm 1 content, one third Midterm 2 content and one third post-Midterm 2 content, which is HW10–HW13: the FFT and fast convolution ([[5-dft-and-fft/index|Unit 5]]), this unit and multirate. Practice so far: [[homework/hw11|HW11]].

## Related
[[5-dft-and-fft/index|Unit 5]] · [[concepts/frequency-response|frequency response]] · [[concepts/magnitude-and-phase-response|magnitude and phase response]] · [[concepts/window-functions|window functions]] · [[concepts/index|Concepts]] · [[exams/index|Exams]]

### Sources for this page
Snyder, ECE 310 Lecture 27 notes and slides (Nov 9, 2026); lecture recording Nov 9 (condensed).
