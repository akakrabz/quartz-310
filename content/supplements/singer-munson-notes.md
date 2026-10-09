---
title: "Singer & Munson course notes — reading guide"
description: "A section-by-section guide to the 321-page ECE 310 notes by Singer and Munson (ECE310_notes_2019.pdf): which sections cover Lectures 1–16 (Units 1–3, the DTFT and the frequency response included), with PDF page numbers, how the notes' notation differs (LSI, unit pulse response, X_d, unilateral z-transform first), and what to skip for now."
tags: [supplement, midterm-1, dtft]
---

*Supplement · `suppliment/ECE310_notes_2019.pdf` · "Signal Processing of Discrete-time Signals", A. C. Singer and D. C. Munson Jr. (dated 2013, © 2015), 321 PDF pages*

These are the long-form course notes that ECE 310 used before the current lecture notes. They are a good second explanation when a lecture's two pages are too terse — but they are organised differently (the unilateral z-transform first, systems after Fourier analysis), so do not read them front to back the night before an exam. Use the table below to jump to the section you need.

> [!tip] Page numbers
> All page numbers here are **PDF page numbers**. In Chapters 1–6 (PDF pp. 1–188) they coincide with the printed numbers. The scanned chapters that follow carry their own "9.1 … 15.12" numbering, and the appendices restart at 195, so trust the PDF viewer's page counter, not the header.

## What is in the file

| PDF pages | part | lectures |
|---|---|---|
| 3–8 | Ch. 1 Overview: DSP overview (§1.1), CT signals (§1.2), DT signals (§1.3) | L1 |
| 9–70 | Ch. 2 CT and DT signal representations: Fourier series, CTFT, DFS, **DTFT (§2.4, pp. 35–53)**, DFT (§2.5), DFT spectral analysis (§2.6) | §2.1–2.4: L13–L14 (Unit 3); §2.5–2.6: later |
| 71–100 | Ch. 3 CT and DT systems: systems as mappings (§3.1), sampling (§3.2), examples (§3.3), linear (§3.4), shift-invariant (§3.5), causal (§3.6), LSI systems and convolution (§3.7), properties of LSI systems (§3.8), difference equations (§3.9) | L3–L5, except §3.2 (later) |
| 101–152 | Ch. 4 z-transform: unilateral (§4.2–4.5), two-sided (§4.6–4.9), block diagrams (§4.10), system analysis and BIBO stability (§4.12–4.14) | L6–L11 — the core of Unit 2 and Midterm 1 |
| 153–172 | Ch. 5 Frequency response of systems (§5.1–5.2), DT processing of CT signals (§5.3) | §5.1–5.2: L15–L16 (Unit 3); §5.3–5.4: later |
| 173–188 | Ch. 6 DT filters and filter design (FIR/IIR, generalized linear phase) | later; §6.4 (generalized linear phase) goes one step past L16 |
| 189–303 | Scanned ECE 410 notes (Munson): Ch. 9 D/A and A/D, Ch. 11 FIR design, Ch. 12 IIR design, Ch. 13 interpolation and decimation, Ch. 14 FFT, Ch. 15 applications (CT imaging, SAR, speech) | later |
| 304–313 | Appendix A: complex numbers | L2 |
| 314–317 | Appendices B, C: outlines only (vectors and matrices; image processing) | — |
| 318–321 | Appendix D: "Impulses, samples, and delta's, Oh My!" — Dirac vs Kronecker delta, the unit pulse $\delta[n]$ | L2 |

## Lecture by lecture

| lecture on this site | read in the notes | PDF pages | what you get there |
|---|---|---|---|
| [[1-signals-and-systems/01-digital-signals\|L1 digital signals]] | §1.1–1.3 | 3–8 | analog vs discrete-time vs digital; finite, infinite, periodic sequences |
| [[1-signals-and-systems/02-complex-numbers-and-elementary-signals\|L2 complex numbers, elementary signals]] | Appendix A; Appendix D.2 | 304–313; 319–321 | rectangular/polar, Euler; the unit pulse $\delta[n]$ as a Kronecker delta |
| [[1-signals-and-systems/03-system-properties\|L3 system properties]] | §3.1, §3.3–3.6 | 71, 80–86 | memoryless vs with-memory systems (Systems 3.1–3.4), linearity with the zero-state / zero-input distinction, shift-invariance proofs (Examples 1–5, incl. modulation $\cos(\omega_0 n)x[n]$ = shift-varying), causality |
| [[1-signals-and-systems/04-impulse-response-and-convolution\|L4 convolution]] | §3.7–3.8 | 87–99 | convolution sum from linearity + shift-invariance; Examples 8–9 ($x[-n]$, $x[\lvert n\rvert]$: linear, shift-varying, non-causal); causality and stability read off $h[n]$; §3.8.1 impulse response of a recursion |
| [[1-signals-and-systems/05-difference-equations-and-block-diagrams\|L5 difference equations, block diagrams]] | §3.9; §4.10 | 100; 138–143 | the LCCDE $y[n] + \sum a_k y[n-k] = \sum b_k x[n-k]$ (same signs as Lecture 9); delay–adder–gain flowgraphs, direct forms |
| [[2-z-transform/06-the-z-transform\|L6 z-transform]] | §4.1, §4.6 | 101–102, 123–131 | two-sided definition, ROC as the convergence region, annulus ROCs, the empty-ROC case ($\lvert a\rvert\ge\lvert b\rvert$, p. 126) |
| [[2-z-transform/07-z-transform-properties\|L7 properties]] | §4.7 (two-sided); §4.3 (unilateral) | 132–134; 108–112 | linearity (ROC at least the intersection, with pole-zero cancellation), shifting, convolution |
| [[2-z-transform/08-inverse-z-transform\|L8 inverse z-transform]] | §4.4, §4.9 | 113–117, 135–137 | PFE with residues ("cover-up" formula), inverse two-sided transforms (e.g. $\cos(\tfrac{\pi}{2}n)u[-n]$, p. 138) |
| [[2-z-transform/09-transfer-functions\|L9 transfer functions]] | §4.8, §4.5 | 135, 118–122 | system function $H(z) = Y(z)/X(z)$, poles and zeros; solving LCCDEs with the z-transform |
| [[2-z-transform/10-improper-transfer-functions-and-system-algebra\|L10 improper TFs, system algebra]] | §4.3.6, §4.10 | 110, 143 | "direct long division" (power-series inverse, p. 110); cascade and parallel combinations of LSI systems (p. 143) |
| [[2-z-transform/11-bibo-stability-and-causality\|L11 BIBO stability, causality]] | §4.13–4.14 | 145–152 | $\sum\lvert h\rvert<\infty$ proof in both directions; "BIBO stable ⇔ $\mathrm{ROC}_H \supset \{\lvert z\rvert = 1\}$" (p. 147); causal + stable examples; poles on the unit circle (p. 151: "marginally stable … in our terminology, simply unstable") |
| [[3-fourier-analysis/12-convolution-as-template-matching\|L12 template matching]] | — | — | the notes have no section on template matching; the Lecture 12 notes are the source |
| [[3-fourier-analysis/13-fourier-analysis-and-the-dtft\|L13 Fourier analysis, DTFT]] | §2.1–2.4 | 10–41 | CT Fourier series (§2.1, pp. 10–19), CTFT (§2.2, pp. 20–27), DT Fourier series (§2.3, pp. 27–35), then the DTFT, its inverse and the complex exponentials as eigensignals (§2.4, pp. 35–41) |
| [[3-fourier-analysis/14-dtft-properties\|L14 DTFT properties]] | §2.4.1–2.4.2 | 41–53 | linearity, periodicity, real/imaginary-part and magnitude/phase symmetries (pp. 41–43); shift, modulation, time reversal, conjugation, products, convolution, Parseval (pp. 44–47); worked magnitude and phase plots, $a^nu[n]$, and the impulse "distribution" for $\cos(\omega_0n)$ (pp. 48–53) |
| [[3-fourier-analysis/15-frequency-response\|L15 frequency response]] | §5.1 | 153–160 | $Y_d=H_dX_d$; $e^{j\omega_0n}$ as an eigensequence with eigenvalue $H_d(\omega_0)$, and why $e^{j\omega_0n}u[n]$ is not one; sinusoids through real and complex $h$, with a worked example (p. 156); ideal low-, high- and band-pass filters (pp. 157–159, ahead of the lectures); the two-point average (p. 160) |
| [[3-fourier-analysis/16-magnitude-and-phase-response\|L16 magnitude, phase, group delay]] | §5.2; §6.4 | 161–164; 179–187 | why the phase matters: zero phase, linear phase $\angle H_d=-\omega M$ as a pure delay, distortion from non-linear phase (§5.2); group delay from the phase "with jumps of $\pi$ and $2\pi$ removed", generalized linear phase and the four symmetric FIR types (§6.4, ahead of the lectures) |

Worked examples worth the detour: the convolution of two causal exponentials $a^n u[n] * b^n u[n] = \dfrac{b^{n+1}-a^{n+1}}{b-a}u[n]$ (p. 123), an LCCDE solved by convolving its $h[n]$ with the input $(\tfrac14)^n u[n]$ (pp. 91–93), and the input $x = h$ that makes a unit-circle pole pair blow up (p. 151) — the same idea as [[problems/unbounded-outputs-and-pole-matching|pole matching]].

## Notation and convention differences

| notes | course (lectures, this site) |
|---|---|
| LSI — linear shift-invariant | LTI — linear time-invariant (same thing) |
| unit pulse, unit pulse response | Kronecker delta / impulse $\delta[n]$, impulse response $h[n]$ |
| system function $H(z)$ | transfer function $H(z)$ |
| "zero-state linear" and "zero-input linear" (§3.4) | "linear" — with the system initially at rest, i.e. zero-state linearity |
| unilateral z-transform $\sum_{n\ge0}$ first (§4.2–4.5), with initial conditions | bilateral $\sum_{n\in\mathbb Z}$ throughout; systems initially at rest |
| $X_d(\omega)$, $H_d(\omega)$ for the DTFT | same in lectures ($X_d$); textbooks write $X(e^{j\omega})$ |
| convolution written out as a sum, no operator symbol | $x[n]*h[n]$ or $(x*h)[n]$ |
| $\langle\langle k\rangle\rangle_N$ for $k$ mod $N$ | $\langle k\rangle_N$ |

Full list across textbooks: [[supplements/notation-translation|notation translation]].

## What to skip for now

- **What comes after Lecture 16:** the DFT (§2.5–2.6), sampling (§3.2) and DT processing of CT signals (§5.3), Chapter 6 apart from §6.4, and the scanned chapters. Sampling and the DFT come later in the course (they are on Midterm 2).
- **Unilateral z-transform with initial conditions:** Delay Property #2 and the advance property (p. 109), and the initial-condition terms in §4.5. The PFE technique in §4.4 is still useful — just ignore the $n\ge0$-only framing.
- **Everything from PDF p. 165 on**, except §6.4 (pp. 179–187, a look ahead from [[3-fourier-analysis/16-magnitude-and-phase-response|Lecture 16]]) and Appendices A and D.

### Sources for this page

`suppliment/ECE310_notes_2019.pdf`, every page extracted with `pdftotext -f P -l P` to locate chapter and section starts (pp. 3, 9, 71, 101, 153, 173, 189, 201, 229, 254, 272, 292, 304, 314, 316, 318; for Unit 3 also §2.1–2.4 and their subsections on pp. 10, 20, 27, 35, 41–47, §5.1–5.3 on pp. 153, 161, 165, §6.4 on p. 179) and skimmed for content and notation; `suppliment/ece310_notation.pdf` for the modulo notation; Lecture 1–16 notes for the mapping.
