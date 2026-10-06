---
title: "Midterm 2"
description: "Orientation for ECE 310 Midterm 2 (Fall 2026 date and exact scope not yet announced): it covers Unit 3, the DTFT, frequency response and magnitude and phase (Lectures 13–16), plus the lectures after it on ideal filters, sampling and reconstruction, the DFT and FFT; this page gives the format of the seven past exams, which problem types each of them set, how to prepare as the course goes, and a verified Unit 3 formula box for the handwritten sheet."
tags: [exam, midterm-2]
---

*Midterm 2 · Fall 2026 date and exact scope not yet announced (past fall Midterm 2s were in early November) · [[3-fourier-analysis/index|Unit 3]] (Lectures 13–16) and the lectures after it · [[exams/midterm-2/past-exams/index|seven past exams]] with folded solutions · part of [[exams/index|Exams]]*

> [!abstract] In one breath
> Midterm 2 tests the frequency domain: [[3-fourier-analysis/index|Unit 3]] (the DTFT, frequency response, magnitude and phase; Lectures 13–16) and the lectures that follow it (ideal filters, sampling and reconstruction, the DFT and FFT, spectral analysis). The Fall 2026 date and exact scope have not been announced; past fall Midterm 2s were held in early November. On the seven past exams it was two hours (90–110 minutes in 2019–2021), 7–11 problems and 100 points, with one or two handwritten sheets depending on the term (open notes in the online FA2021), no calculator and closed-form answers. About a third of a typical exam (18–42 points) is Unit 3: True/False items on the DTFT, a DTFT or inverse DTFT, a magnitude/phase sketch and a response to sinusoids. The rest is sampling, filtering and the DFT, which come after Lecture 16 and are not on this site yet. **Now:** learn Unit 3 from its lectures, concept hubs and three problem families, drill it, and test yourself on the Unit 3 problems of the recent exams. **Later:** try each new lecture's past problems as it is taught, then take whole exams under exam conditions.

## 1. Scope

**The Fall 2026 scope has not been announced yet.** On all seven past exams Midterm 2 had two parts:

| part | lectures | what you must be able to do |
|---|---|---|
| [[3-fourier-analysis/index\|Unit 3 · Fourier analysis and frequency response]] | [[3-fourier-analysis/13-fourier-analysis-and-the-dtft\|L13 the DTFT]] (Sep 23) · [[3-fourier-analysis/14-dtft-properties\|L14 DTFT properties]] (Sep 25) · [[3-fourier-analysis/15-frequency-response\|L15 frequency response]] (Oct 2) · [[3-fourier-analysis/16-magnitude-and-phase-response\|L16 magnitude and phase]] (Oct 5 and 7) | compute a DTFT or an inverse DTFT from the definition, the pairs and the properties; read $X_d(0)$, $X_d(\pi)$, $\int X_d$ and $\int\lvert X_d\rvert^2$ off the sequence; decide when $X_d(\omega) = X(e^{j\omega})$; use symmetry and periodicity; sketch modulated spectra; find $H_d(\omega)$ from $h[n]$, $H(z)$ or an LCCDE; push constants, $(-1)^n$, exponentials and sinusoids through it; sketch $\lvert H_d\rvert$ and $\angle H_d$ with their jumps; give the group delay |
| after Lecture 16, not yet on this site | ideal filters · sampling and reconstruction (A/D, D/A, aliasing) · the DFT and FFT · spectral analysis and windowing | find a Nyquist rate; sketch the DTFT of a sampled signal and the output of an ideal D/A; decide which sampling periods fit given sinusoids; choose $T$ and the cutoff $\omega_c$ of an A/D → $H_d$ → D/A chain; compute DFT values and use the DFT's properties (circular shift, symmetry, zero padding); read frequencies and amplitudes off a DFT plot; explain leakage, resolution and windows; relate linear and circular convolution |

**Not tested:** [[3-fourier-analysis/12-convolution-as-template-matching|Lecture 12]] (template matching: "this lecture will not be tested on homeworks or exams"). **Used throughout:** Units 1–2. Systems often arrive as $H(z)$ or an LCCDE, and the ROC decides whether the DTFT is $X(e^{j\omega})$ (FA2023 #1(a), FA2024 #1(a), FA2021 #2).

Homework: [[homework/hw5|HW5]] (L13–L14) · HW6 (L13–L16, due Oct 9; its walkthrough is published after the due date) · the sets that follow Lecture 16.

## 2. Format

What the covers of the seven past exams (FA2019–SP2025) say. The Fall 2026 instructions are not out yet; read them when they are, especially the number of sheets.

| | past Midterm 2 exams |
|---|---|
| when | Fall 2026: **not announced**. Past fall exams: Wed Nov 6, 2019 · Tue Nov 9, 2021 · Wed Nov 1, 2023 · Wed Nov 6, 2024, all in the evening; the spring exams were in early April |
| length | **2 hours** (7:00–9:00 pm) on SP2023, FA2023, FA2024 and SP2025; 90 minutes on FA2019 and FA2021, 110 on SP2021 |
| size | **7–11 problems, always 100 points** (SP2025: 12 + 10 + 12 + 10 + 16 + 12 + 12 + 6 + 10) |
| allowed | handwritten two-sided 8.5″ × 11″ sheets, and **the number varies by term**: two on FA2019, FA2023, FA2024 and SP2025; one on SP2021 and SP2023 (and on this term's Midterm 1); FA2021 was online and open-notes. No books, **no calculator** on any of them |
| answers | "calculate", "determine", "find" mean a **closed form**: no $\Sigma$ or $\int$ left in the answer |
| grading | "Show all your work to receive full credit"; "Neatness counts" (these two rules and the closed-form rule are printed on the five in-person exams) |
| True/False | always problem 1, 10–20 points; **+2 / −1 / 0** on SP2023 and SP2025, **a reason of at most two sentences** on FA2024, no penalty printed on the others |

More per exam (instructors, Unit 3 points, what each is good for): [[exams/midterm-2/past-exams/index|past Midterm 2 exams]].

## 3. What gets asked — problem types × past exams

Each cell lists the problems of that type; letters are parts.

| problem type | [[exams/midterm-2/past-exams/spring-2025\|SP25]] | [[exams/midterm-2/past-exams/fall-2024\|FA24]] | [[exams/midterm-2/past-exams/fall-2023\|FA23]] | [[exams/midterm-2/past-exams/spring-2023\|SP23]] | [[exams/midterm-2/past-exams/fall-2021\|FA21]] | [[exams/midterm-2/past-exams/spring-2021\|SP21]] | [[exams/midterm-2/past-exams/fall-2019\|FA19]] | exams |
|---|---|---|---|---|---|---|---|---|
| ***Unit 3 · Lectures 13–16*** | | | | | | | | |
| True/False on the DTFT and frequency response → [[exams/midterm-2/true-false-bank\|T/F bank]] §1–3 | #1(a,d) | #1(a,b,d) | #1(a–c,f) | #1(c) | #1(a) | — | #1(a–e) | 6/7 |
| [[problems/dtft-and-inverse-dtft\|Computing DTFTs and inverse DTFTs]] | #2 | #2 | #2 | #2, #3, #4 | #2 | #3, #6(a), #7 | #3, #5, #6 | 7/7 |
| [[problems/lti-response-to-sinusoids\|LTI response to sinusoids]] | #4 | #4 | #4(b) | #6 | — | — | #7 | 5/7 |
| [[problems/magnitude-phase-and-group-delay\|Magnitude, phase and group delay]] | #3 | #3 | #4(a) | #5 | — | #2 | — | 5/7 |
| *Unit 3 share, points of 100* | 36 | 41 | 32 | 35 | 18 | 36 | 42 | 18–42 |
| ***After Lecture 16 · not yet on this site*** | | | | | | | | |
| True/False on sampling, D/A conversion, the DFT and FFT → [[exams/midterm-2/true-false-bank\|T/F bank]] §4–8 | #1(b,c,e,f) | #1(c,d) | #1(d,e,g,h) | #1(a,b,d,e) | #1(b–e) | #1(a–e) | #1(f–j) | 7/7 |
| Sampling and reconstruction: Nyquist rate, aliasing, ideal D/A | #6 | #5(a,b) | #3 | #8 | — | #8, #9 | #8 | 6/7 |
| Digital filtering of analog signals: A/D → $H_d$ → D/A with an ideal filter | #5 | #5(c) | #5 | #7 | #4, #5 | — | #9 | 6/7 |
| DFT computation and properties | #7, #8 | #7, #8 | #7 | #9 | #3 | #4, #5, #6(b) | #4 | 7/7 |
| DFT spectral analysis and resolution | #9 | #6, #9 | #6 | #10 | #7 | — | #2 | 6/7 |
| Linear vs circular convolution, the FFT | — | — | — | — | #6 | — | #10, #11 | 2/7 |

How to read it: a problem appears in every row it draws on. Zero-padding statements that claim something only about the DTFT (FA2019 #1(a), SP2023 #1(c), FA2023 #1(f), SP2025 #1(d)) count as Unit 3, as in the T/F bank; FA2021 #1(d) is about DFT values; FA2024 #1(d) is about both and sits in both True/False rows. SP2021 #6 asks which transform fits three descriptions: (a) is the DTFT, (b) the DFT, (c) the CTFT. "Sampling and reconstruction" lists the problems without a digital filter; every A/D → $H_d$ → D/A problem samples too (a Nyquist rate, a largest $T$, sketches of $X_d$), so sampling is on all seven exams. The Unit 3 share adds up the Unit 3 problems and True/False parts, with only part (a) of SP2021 #6, as on the past-exams page; the single exam pages file zero padding under the DFT and so give 30, 38 and 34 for FA2023, FA2024 and SP2025. The problem-by-problem maps are on [[exams/midterm-2/past-exams/index|past Midterm 2 exams]] and on each exam page.

> [!exam] Read the table as a map
> - **Unit 3 always shows up, in a few fixed shapes.** Every exam has a DTFT or inverse-DTFT problem. The four exams Prof. Snyder co-wrote (SP2023, FA2023, FA2024, SP2025) each add both a magnitude/phase sketch and a response to sinusoids.
> - **The later lectures carry most of the points.** Sampling, alone or inside an A/D → $H_d$ → D/A chain, and the DFT's properties are on all seven exams; DFT spectral analysis is on six. Circular convolution and the FFT appear only in 2019 and 2021 (the FA2019 key even marks the FFT and circular convolution "not on our Midterm 2"), and not at all since 2023.
> - **True/False leans on the later material too:** 16 of the 43 statements are about Unit 3, 27 about later topics.
> - **Typical points on the four Snyder exams:** True/False 10–16 · DTFT or inverse DTFT 6–11 · magnitude and phase 12–14 · response to sinusoids 8–12 (FA2023 joins the two in one 18-point problem) · the big sampling-and-filtering problem 16–22 · a sampling puzzle 6–12 · DFT properties 14–18 · DFT spectral analysis 10–20.

## 4. How to prepare, as the course goes

### Now: Unit 3, Lectures 13–16

1. **Learn it.** Read [[3-fourier-analysis/13-fourier-analysis-and-the-dtft|Lecture 13]], [[3-fourier-analysis/14-dtft-properties|Lecture 14]], [[3-fourier-analysis/15-frequency-response|Lecture 15]] and [[3-fourier-analysis/16-magnitude-and-phase-response|Lecture 16]], trying each folded question before opening it. Keep the concept hubs at hand: [[concepts/dtft|DTFT]] · [[concepts/dtft-pairs|DTFT pairs]] · [[concepts/dtft-properties|DTFT properties]] · [[concepts/frequency-response|frequency response]] · [[concepts/magnitude-and-phase-response|magnitude and phase response]] · [[concepts/group-delay|group delay]] · [[concepts/eigenfunctions-of-lti-systems|eigenfunctions of LTI systems]].
2. **Learn the three problem types.** Each family page has a recipe, the traps seen on real exams, every past instance and fresh practice problems: [[problems/dtft-and-inverse-dtft|DTFTs and inverse DTFTs]] · [[problems/lti-response-to-sinusoids|response to sinusoids]] · [[problems/magnitude-phase-and-group-delay|magnitude, phase and group delay]]. Compare your homework with the [[homework/hw5|HW5]] walkthrough (HW6's appears after its due date).
3. **Drill until the method is automatic.** The [[demos/practice-drills|practice drills]] *DTFT values*, *sinusoidal response* and *magnitude & phase* generate fresh variants, with hints after a wrong answer.
4. **Check a sketch against the real thing.** Draw $\lvert H_d\rvert$ and $\angle H_d$ for SP2025 #3, $h[n] = \{\underset{\uparrow}{1},\ 0,\ 0,\ 2,\ 0,\ 0,\ 1\}$, by hand; then type the taps into the [[demos/frequency-response-explorer|frequency-response explorer]] and compare the zeros, the jumps and the group delay.
5. **Test yourself.** Take [[exams/midterm-2/past-exams/spring-2025|SP2025]] #2–#4 in one sitting (32 points, about 40 minutes at exam pace) with only a handwritten sheet, then [[exams/midterm-2/past-exams/fall-2024|FA2024]] #2–#4 the same way. Grade with the folded solutions and repair every lost point with its family page. Then go through the Unit 3 statements of the [[exams/midterm-2/true-false-bank|T/F bank]] (sections 1–3, 16 statements), saying each reason out loud. The other Unit 3 cells of the table above (each linked from [[exams/midterm-2/past-exams/index|past Midterm 2 exams]]) and the DTFT problems of two old Midterm 1 exams ([[exams/midterm-1/past-exams/spring-2023|SP2023 MT1]] #8–#9, [[exams/midterm-1/past-exams/fall-2019|FA2019 MT1]] #8–#9, answered on the [[problems/dtft-and-inverse-dtft|DTFT family]] page) make a bank for later rounds.

### Later: as the lectures after Lecture 16 arrive

1. **After each new lecture, try its past problems.** The rows of §3 say where they are: sampling SP2025 #6, FA2023 #3, SP2023 #8; the A/D → $H_d$ → D/A chain SP2025 #5, FA2023 #5; DFT properties SP2025 #7–#8, FA2024 #8; spectral analysis SP2025 #9, FA2024 #9; then the matching *(later)* sections of the T/F bank. The exam pages have them typed with folded solutions; lecture pages and problem families for these topics will follow.
2. **Once the scope is announced, take [[exams/midterm-2/past-exams/spring-2025|SP2025]] and then [[exams/midterm-2/past-exams/fall-2024|FA2024]] whole:** two hours, only your handwritten sheets, no calculator. Grade, repair by family, and use the other five exams by topic rather than as more full runs.
3. **Write your sheet by hand.** §5 is a start for the Unit 3 part; add each later topic as you learn it.

## 5. Formulas for your sheet — Unit 3

The Unit 3 formulas the past exams use, in one box, with the sign that Lecture 14's table gets wrong corrected. Copy them by hand: choosing what goes on the sheet is part of the review.

> [!key] Formulas for your sheet — Unit 3
> | | formula |
> |---|---|
> | DTFT and inverse | $X_d(\omega)=\sum_{n=-\infty}^{\infty}x[n]\,e^{-j\omega n}$, $\quad x[n]=\frac{1}{2\pi}\int_{-\pi}^{\pi}X_d(\omega)\,e^{j\omega n}\,d\omega$ |
> | existence | $X_d$ is $2\pi$-periodic; it exists if $\sum_n\lvert x[n]\rvert<\infty$; $X_d(\omega)=X(e^{j\omega})$ needs the unit circle in the ROC ($2^nu[n]$: no DTFT; $u[n]\leftrightarrow\frac{1}{1-e^{-j\omega}}+\pi\delta(\omega)$) |
> | free values | $X_d(0)=\sum_n x[n]$, $\quad X_d(\pi)=\sum_n(-1)^n\,x[n]$, $\quad\int_{-\pi}^{\pi}X_d(\omega)\,d\omega=2\pi\,x[0]$ |
> | Parseval | $\sum_n\lvert x[n]\rvert^2=\frac{1}{2\pi}\int_{-\pi}^{\pi}\lvert X_d(\omega)\rvert^2\,d\omega$ |
> | finite pairs | $\delta[n-k]\leftrightarrow e^{-j\omega k}$, $\quad u[n]-u[n-L]\leftrightarrow e^{-j\omega(L-1)/2}\,\frac{\sin(L\omega/2)}{\sin(\omega/2)}$ ($L$ ones centred at $n=0$, $L$ odd: no exponential) |
> | exponentials, $\lvert a\rvert<1$ | $a^nu[n]\leftrightarrow\frac{1}{1-ae^{-j\omega}}$, $\quad n\,a^nu[n]\leftrightarrow\frac{ae^{-j\omega}}{(1-ae^{-j\omega})^2}$ |
> | ideal low-pass | $\frac{\sin(\omega_cn)}{\pi n}$ (equal to $\frac{\omega_c}{\pi}$ at $n=0$) $\leftrightarrow$ $1$ for $\lvert\omega\rvert\le\omega_c$, $0$ for $\omega_c<\lvert\omega\rvert\le\pi$ |
> | impulses (one period) | $1\leftrightarrow2\pi\delta(\omega)$, $\quad e^{j\omega_0n}\leftrightarrow2\pi\delta(\omega-\omega_0)$, $\quad\cos(\omega_0n)\leftrightarrow\pi[\delta(\omega-\omega_0)+\delta(\omega+\omega_0)]$, $\quad\sin(\omega_0n)\leftrightarrow-j\pi[\delta(\omega-\omega_0)-\delta(\omega+\omega_0)]$ |
> | shift and modulation | $x[n-k]\leftrightarrow e^{-j\omega k}X_d(\omega)$, $\quad e^{j\omega_0n}x[n]\leftrightarrow X_d(\omega-\omega_0)$, $\quad x[n]\cos(\omega_0n)\leftrightarrow\frac12X_d(\omega-\omega_0)+\frac12X_d(\omega+\omega_0)$ |
> | reversal, conjugation | $x[-n]\leftrightarrow X_d(-\omega)$, $\quad x^*[n]\leftrightarrow X_d^*(-\omega)$, $\quad x$ real $\Leftrightarrow X_d(-\omega)=X_d^*(\omega)$ (Hermitian) |
> | multiply by $n$, convolve, window | $n\,x[n]\leftrightarrow+j\,\frac{dX_d(\omega)}{d\omega}$ (Lecture 14 prints $-j$: an erratum), $\quad x[n]*h[n]\leftrightarrow X_d(\omega)H_d(\omega)$, $\quad x[n]w[n]\leftrightarrow\frac{1}{2\pi}\int_{-\pi}^{\pi}X_d(\theta)\,W_d(\omega-\theta)\,d\theta$ |
> | frequency response | $H_d(\omega)=\sum_n h[n]\,e^{-j\omega n}$; for inputs on all $n$: $e^{j\omega_0n}\mapsto H_d(\omega_0)\,e^{j\omega_0n}$, $\quad c\mapsto H_d(0)\,c$, $\quad(-1)^n\mapsto H_d(\pi)\,(-1)^n$ |
> | real $h$: the cosine rule | check $H_d(-\omega)=H_d^*(\omega)$ first; then $A\cos(\omega_0n+\theta)\mapsto A\lvert H_d(\omega_0)\rvert\cos\big(\omega_0n+\theta+\angle H_d(\omega_0)\big)$ |
> | complex $h$ | split the cosine: $\cos(\omega_0n+\theta)\mapsto\frac12H_d(\omega_0)\,e^{j(\omega_0n+\theta)}+\frac12H_d(-\omega_0)\,e^{-j(\omega_0n+\theta)}$ |
> | magnitude and phase | factor $H_d(\omega)=e^{-jM\omega}R(\omega)$ with $R$ real ($M$ the centre of symmetric taps; antisymmetric taps give $j\,e^{-jM\omega}R(\omega)$, add $\frac{\pi}{2}$): $\lvert H_d\rvert=\lvert R\rvert\ge0$, $\;\angle H_d=-M\omega$, plus $\pm\pi$ where $R<0$, wrapped into $[-\pi,\pi]$ |
> | group delay | $\tau_{gd}(\omega)=-\frac{d\angle H_d(\omega)}{d\omega}$ samples, read between the jumps; a linear phase $-M\omega$ gives $\tau_{gd}=M$ at every $\omega$ |
>
> Every line was re-checked numerically on random sequences. Longer versions with examples: [[3-fourier-analysis/index|the Unit 3 card]], [[concepts/dtft-pairs|DTFT pairs]], [[concepts/dtft-properties|DTFT properties]]; the traps that cost the most points on these formulas: [[exams/midterm-2/past-exams/index|past Midterm 2 exams]].

## Related

[[exams/midterm-2/past-exams/index|past Midterm 2 exams]] · [[exams/midterm-2/true-false-bank|T/F bank]] · [[3-fourier-analysis/index|Unit 3]] · [[problems/index|problem families]] · [[demos/practice-drills|practice drills]] · [[demos/frequency-response-explorer|frequency-response explorer]] · [[supplements/transform-tables|transform tables]] · [[0-toolkit/05-errata|errata]] · [[exams/midterm-1/index|Midterm 1 review guide]] · [[exams/index|all exams]] · [[index|home]]

### Sources for this page

The cover pages and point tables of the seven past Midterm 2 exams with their keys (FA2019, SP2021, FA2021, SP2023, FA2023, FA2024, SP2025) for dates, length, sheets, rules and points; the "Map of the exam" tables of the seven exam pages for the problem-type table, recounted and cross-checked against `verify/FAM_counts.py` (the same exam counts wherever the categories coincide, and the Unit 3 shares of the past-exams page); the Lecture 12 notes for "not tested"; Lectures 13–16 (notes and slides, Fall 2026) and the Unit 3 concept pages for the formula box. Each formula in the box was re-checked with numpy/scipy on random complex sequences with arbitrary start indices: the inverse DTFT, the four free values, every pair and property (including the $+j$ sign of $n\,x[n]$ and the $\pi\delta(\omega)$ of $u[n]$), the cosine rule for real $h$ and the split for complex $h$, and the phase and group delay of symmetric and antisymmetric FIR filters.
