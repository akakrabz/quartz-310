---
title: "Singer & Munson course notes — reading guide"
description: "Section-by-section guide to the 321-page Singer–Munson ECE 310 notes (ECE310_notes_2019.pdf): sections for Lectures 1–16 with PDF pages, notation differences, what to skip."
tags: [supplement, midterm-1, dtft]
---

*Supplement · `suppliment/ECE310_notes_2019.pdf` · "Signal Processing of Discrete-time Signals", A. C. Singer and D. C. Munson Jr., 321 PDF pages*

> [!abstract] In one breath
> - Older long-form notes: a second explanation when a lecture is terse.
> - Ordered differently (unilateral z-transform first, systems after Fourier); jump by the table, don't read front to back.
> - Page numbers are **PDF** pages (printed numbers diverge after p. 188).

## Lecture by lecture

| lecture | notes | PDF pages | what you get |
|---|---|---|---|
| [[1-signals-and-systems/01-digital-signals\|L1]] | §1.1–1.3 | 3–8 | analog vs discrete vs digital |
| [[1-signals-and-systems/02-complex-numbers-and-elementary-signals\|L2]] | App. A; App. D.2 | 304–313; 319–321 | complex numbers; unit pulse $\delta[n]$ |
| [[1-signals-and-systems/03-system-properties\|L3]] | §3.1, §3.3–3.6 | 71, 80–86 | linearity, shift-invariance proofs, causality |
| [[1-signals-and-systems/04-impulse-response-and-convolution\|L4]] | §3.7–3.8 | 87–99 | convolution sum; causality and stability from $h[n]$ |
| [[1-signals-and-systems/05-difference-equations-and-block-diagrams\|L5]] | §3.9; §4.10 | 100; 138–143 | LCCDE (Lecture 9 signs); flowgraphs |
| [[2-z-transform/06-the-z-transform\|L6]] | §4.1, §4.6 | 101–102, 123–131 | two-sided definition, annulus and empty ROCs |
| [[2-z-transform/07-z-transform-properties\|L7]] | §4.7; §4.3 | 132–134; 108–112 | linearity, shift, convolution |
| [[2-z-transform/08-inverse-z-transform\|L8]] | §4.4, §4.9 | 113–117, 135–137 | PFE, cover-up, two-sided inverses |
| [[2-z-transform/09-transfer-functions\|L9]] | §4.8, §4.5 | 135, 118–122 | $H(z)=Y(z)/X(z)$, poles and zeros |
| [[2-z-transform/10-improper-transfer-functions-and-system-algebra\|L10]] | §4.3.6, §4.10 | 110, 143 | long division; cascade and parallel |
| [[2-z-transform/11-bibo-stability-and-causality\|L11]] | §4.13–4.14 | 145–152 | $\sum\lvert h\rvert<\infty$ proof; ROC test; unit-circle poles |
| [[3-fourier-analysis/12-convolution-as-template-matching\|L12]] | — | — | not covered |
| [[3-fourier-analysis/13-fourier-analysis-and-the-dtft\|L13]] | §2.1–2.4 | 10–41 | CTFS, CTFT, DTFS, DTFT |
| [[3-fourier-analysis/14-dtft-properties\|L14]] | §2.4.1–2.4.2 | 41–53 | DTFT properties, symmetries, Parseval |
| [[3-fourier-analysis/15-frequency-response\|L15]] | §5.1 | 153–160 | $Y_d=H_dX_d$, eigensequences, sinusoids |
| [[3-fourier-analysis/16-magnitude-and-phase-response\|L16]] | §5.2; §6.4 | 161–164; 179–187 | linear phase as delay; group delay, generalized linear phase |

Worth the detour: $a^n u[n] * b^n u[n] = \dfrac{b^{n+1}-a^{n+1}}{b-a}u[n]$ (p. 123); a unit-circle pole pair driven unbounded (p. 151, cf. [[problems/unbounded-outputs-and-pole-matching|pole matching]]).

## Notation differences

| notes | course |
|---|---|
| LSI | LTI |
| unit pulse (response) | impulse $\delta[n]$, impulse response $h[n]$ |
| system function $H(z)$ | transfer function $H(z)$ |
| zero-state / zero-input linear | linear (initially at rest) |
| unilateral z-transform first | bilateral throughout |
| $\langle\langle k\rangle\rangle_N$ | $\langle k\rangle_N$ |

More: [[supplements/notation-translation|notation translation]].

## Skip for now

- Not mapped yet (Lectures 17–21): sampling (§3.2), DT processing of CT signals (§5.3), DFT (§2.5–2.6).
- Chapter 6 except §6.4; the scanned ECE 410 chapters (pp. 189–303).
- Unilateral initial-condition material (p. 109, §4.5); §4.4's PFE is still useful.

### Sources for this page
`suppliment/ECE310_notes_2019.pdf` (section starts located page by page); `suppliment/ece310_notation.pdf`; Lecture 1–16 notes.
