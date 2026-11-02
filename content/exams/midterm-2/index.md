---
title: "Midterm 2 review guide · Wed Nov 4, 7–9 pm"
description: "ECE 310 Midterm 2, Wed Nov 4, 2026, 7–9 pm (ECEB 1002 or 2017 by NetID): HW5–9, Lectures 13–23; one handwritten sheet, no calculator. Scope, format, problem types, day-by-day plan, formula boxes."
tags: [exam, midterm-2]
---

*Midterm 2 · **Wed Nov 4, 2026, 7–9 pm** (no class that day) · ECEB 1002 (NetIDs aa–sz), ECEB 2017 (ta–zz) · conflict exam: MT2-specific request form (course website) · one handwritten 8.5 × 11 in sheet, both sides, no printed notes · no calculator · HW5–9, Lectures 13–23 · [[exams/midterm-2/practice-exam|practice midterm]] · [[exams/index|Exams]]*

> [!abstract] In one breath
> - **Wed Nov 4, 7–9 pm**, ECEB 1002 (aa–sz) or ECEB 2017 (ta–zz); one handwritten sheet, no calculator.
> - HW5–9 = Lectures 13–23: [[3-fourier-analysis/index|Unit 3]] DTFT, frequency response; [[4-sampling-and-reconstruction/index|Unit 4]] sampling, D/A; [[5-dft-and-fft/index|Unit 5]] DFT, its properties, spectral analysis, windows. **Not on it:** computing circular convolution, spectral analysis part 3 (spectrograms), the FFT, Lecture 12.
> - What he said in lecture about the exam (§5): scope ends with spectral analysis part 2 (L23); DFT properties yes, computing circular convolution no; windows and lobe criteria at homework depth; no DFT pairs table needed; review class Mon Nov 2, 3 pm.
> - Plan (§4): topics Fri–Sun, sheet Sun night, FA2025 timed Mon (newest; Do & Snyder), practice midterm Tue, rest Wed.

## 1. Scope

| part | lectures | homework | skills (topic pages) |
|---|---|---|---|
| [[3-fourier-analysis/index\|Unit 3]] | [[3-fourier-analysis/13-fourier-analysis-and-the-dtft\|L13]] (Sep 23) · [[3-fourier-analysis/14-dtft-properties\|L14]] (Sep 25, Oct 2) · [[3-fourier-analysis/15-frequency-response\|L15]] (Oct 5) · [[3-fourier-analysis/16-magnitude-and-phase-response\|L16]] (Oct 5, 7) | [[homework/hw5\|HW5]] · [[homework/hw6\|HW6]] · HW7 #1–2 ([[exams/quiz-2\|Quiz 2 page]]) | [[concepts/dtft\|DTFT]] and inverse from definition, [[concepts/dtft-pairs\|pairs]], [[concepts/dtft-properties\|properties]]; $X_d(0)$, $X_d(\pi)$, $\int X_d$, $\int\lvert X_d\rvert^2$; when $X_d(\omega) = X(e^{j\omega})$; [[concepts/frequency-response\|frequency response]] $H_d(\omega)$ from $h$, $H(z)$ or LCCDE; response to sinusoids; [[concepts/magnitude-and-phase-response\|magnitude/phase]] sketches; [[concepts/group-delay\|group delay]] |
| [[4-sampling-and-reconstruction/index\|Unit 4]] | [[4-sampling-and-reconstruction/17-ideal-analog-to-digital-conversion\|L17]] (Oct 9) · [[4-sampling-and-reconstruction/18-ideal-digital-to-analog-conversion\|L18]] (Oct 12, 14) · [[4-sampling-and-reconstruction/19-aliasing\|L19]] (Oct 14, 16) | HW7 #3–4 ([[exams/quiz-2\|Quiz 2 page]]) · [[homework/hw8\|HW8]]: #1–2 aliasing of sinusoids, #3 sampled spectra and $T_{\max}$, #4 ZOH and ideal D/A, #5–6 A/D → filter → D/A | [[concepts/nyquist-criterion\|Nyquist rate]]; sketch $X_d$ after [[concepts/sampling\|sampling]]; [[concepts/ideal-reconstruction\|ideal D/A]] output; consistent sampling periods ([[concepts/aliasing\|aliasing]]); $T$ and $\omega_c$ for [[concepts/digital-processing-of-analog-signals\|A/D → filter → D/A]] |
| [[5-dft-and-fft/index\|Unit 5]] | [[5-dft-and-fft/20-discrete-fourier-transform\|L20]] (Oct 16) · [[5-dft-and-fft/21-dft-properties\|L21]] (Oct 19, guest lecture) · [[5-dft-and-fft/22-spectral-analysis\|L22]] (Oct 21, 23) · [[5-dft-and-fft/23-spectral-analysis-and-window-functions\|L23]] (Oct 23, 26; demos Oct 28) | [[homework/hw9\|HW9]] #1–5 | [[concepts/dft\|DFT]] values, $X[k]=X_d(2\pi k/N)$; [[concepts/zero-padding\|zero padding]]; [[concepts/circular-shift-and-reversal\|circular shift, reversal]], modulation, conjugation, symmetry ([[concepts/dft-properties\|DFT properties]]) · finite cosine via the [[concepts/periodic-sinc\|periodic sinc]]; [[concepts/spectral-leakage\|leakage]] vs two clean bins; frequencies and amplitudes from a DFT plot ([[concepts/spectral-analysis\|spectral analysis]]); full- and half-lobe [[concepts/frequency-resolution\|separation]]; rectangular vs Hamming [[concepts/window-functions\|windows]] |

> [!warning] On and not on Midterm 2 (instructor announcement)
> | on | not on |
> |---|---|
> | Every DFT property: circular shift and reversal, modulation, conjugation and symmetry, Parseval, $x\circledast h\leftrightarrow X[k]H[k]$ as a property | **Computing** a [[concepts/circular-convolution\|circular convolution]]: modified table, circulant matrix, linear-vs-circular wrap-around, padding length (FA2021 #6, FA2019 #1(g)–(h), #11) |
> | Zero padding; spectral analysis parts 1–2 (L22–23, the last content): leakage, lobe-separation criteria, windows — at homework depth, "mostly identifying frequencies" (Oct 30; [[homework/hw9\|HW9]] #4–5) | Spectral analysis part 3: sliding-window DFT / spectrograms (Oct 26–28 demos, "optional content") · the FFT (FA2019 #1(j), #10) |
> | Units 1–2 as tools: the ROC decides whether $X_d(\omega)=X(e^{j\omega})$ (FA2023 #1(a), FA2024 #1(a), FA2021 #2) | [[3-fourier-analysis/12-convolution-as-template-matching\|Lecture 12]] |
>
> ZOH ([[homework/hw8|HW8]] #4(a), 0 points in the key; not in Lecture 18): know it briefly.

## 2. Format

| | Fall 2026 | past exams FA2019–FA2025 |
|---|---|---|
| when | Wed Nov 4, 7–9 pm; conflict exam: the MT2-specific request form on the course website (the MT1 and MT2 forms differ, Oct 30) | fall: evenings, Nov 1–9 (2019, 2021, 2023, 2024, 2025); spring: early April |
| length | 2 hours | 2 hours (SP2023–FA2025); 90 min FA2019, FA2021; 110 min SP2021 |
| size | not announced | 7–11 problems, 100 points (FA2025: 12 + 14 + 12 + 12 + 16 + 10 + 10 + 14; SP2025: 12 + 10 + 12 + 10 + 16 + 12 + 12 + 6 + 10) |
| notes | one handwritten sheet, 8.5 × 11 in, two-sided; no printed notes | two sheets (FA2019, FA2023, FA2024, SP2025, FA2025); one (SP2021, SP2023); FA2021 online, open notes |
| calculator | none | none |
| answers, T/F | closed form; show all work | T/F is problem 1, 10–20 points; +2 / −1 / 0 on SP2023, SP2025; reasons on FA2024; plain T/F on FA2025 (no penalty stated) |

## 3. Problem types × past exams

| problem type | [[exams/midterm-2/past-exams/fall-2025\|FA25]] | [[exams/midterm-2/past-exams/spring-2025\|SP25]] | [[exams/midterm-2/past-exams/fall-2024\|FA24]] | [[exams/midterm-2/past-exams/fall-2023\|FA23]] | [[exams/midterm-2/past-exams/spring-2023\|SP23]] | [[exams/midterm-2/past-exams/fall-2021\|FA21]] | [[exams/midterm-2/past-exams/spring-2021\|SP21]] | [[exams/midterm-2/past-exams/fall-2019\|FA19]] | exams |
|---|---|---|---|---|---|---|---|---|---|
| ***Unit 3*** | | | | | | | | | |
| T/F on DTFT → [[exams/midterm-2/true-false-bank\|bank]] §1–3 | #1(c,f) | #1(a,d) | #1(a,b,d) | #1(a–c,f) | #1(c) | #1(a) | — | #1(a–e) | 7/8 |
| [[problems/dtft-and-inverse-dtft\|DTFTs and inverse DTFTs]] | #2 | #2 | #2 | #2 | #2, #3, #4 | #2 | #3, #6(a), #7 | #3, #5, #6 | 8/8 |
| [[problems/lti-response-to-sinusoids\|Response to sinusoids]] | #2(b), #1(c) | #4 | #4 | #4(b) | #6 | — | — | #7 | 6/8 |
| [[problems/magnitude-phase-and-group-delay\|Magnitude, phase, group delay]] | #3 | #3 | #3 | #4(a) | #5 | — | #2 | — | 6/8 |
| *Unit 3 points* | 30 | 36 | 41 | 32 | 35 | 18 | 36 | 42 | 18–42 |
| ***Unit 4*** | | | | | | | | | |
| T/F on sampling, D/A → [[exams/midterm-2/true-false-bank\|bank]] §4–5 | #1(d,e) | #1(c) | #1(c) | #1(d,e) | #1(a,b,e) | #1(c,e) | #1(a,b,d) | — | 7/8 |
| [[problems/sampling-and-the-nyquist-rate\|Sampling, Nyquist, aliasing, ideal D/A]] | #4 | #6 | #5(a,b) | #3 | #8 | — | #8, #9 | #8 | 7/8 |
| [[problems/digital-filtering-of-analog-signals\|A/D → filter → D/A]] | #5 | #5 | #5(b), (c) | #5 | #7 | #4, #5 | — | #9 | 7/8 |
| ***Unit 5*** | | | | | | | | | |
| T/F on the DFT, spectral analysis → [[exams/midterm-2/true-false-bank\|bank]] §6–7 | #1(a,b) | #1(b,e,f) | #1(d) | #1(f,g,h) | #1(d) | #1(b,d) | #1(c,e) | #1(f), (i) | 8/8 |
| [[problems/dft-values-and-zero-padding\|DFT values and zero padding]] | #6 | #7(a), (c) | #6, #7 | #7(a), (b) | #9(a), (c) | #3(a) | #5, #6 | #2 | 8/8 |
| [[problems/circular-convolution-and-dft-properties\|DFT properties]]: shift, reversal, modulation, conjugation | #7 | #7(b), #8 | #8 | #7 | #9(b) | #3(b) | #4 | #4 | 8/8 |
| *circular-convolution computation: not on Fall 2026 MT2* | — | — | — | — | — | #6 | — | #1(g, h), #11 | 2/8 |
| [[problems/dft-spectral-analysis\|DFT spectral analysis]] | #8 | #9 | #9 | #1(g), #6 | #10 | #7 | — | #1(c), (f) | 7/8 |

A problem counts in every row it uses. Zero-padding T/F statements only about the DTFT count as Unit 3. Every A/D → $H_d$ → D/A problem also samples, so sampling is on 8/8. FFT (FA2019 #1(j), #10): not on Fall 2026 MT2. Per-problem detail: [[exams/midterm-2/past-exams/index|past exams]].

> [!exam] Patterns
> - Every exam: a DTFT or inverse DTFT. Snyder's five (SP2023–FA2025) add a magnitude/phase sketch and a sinusoid response.
> - Sampling and DFT properties: 8/8; DFT spectral analysis: 7/8.
> - T/F: 18 of 49 statements Unit 3, 14 sampling and D/A, 17 DFT (Q41–Q43 not on Fall 2026).
> - Snyder exams, points: T/F 10–16 · DTFT 6–14 · magnitude/phase 12–14 · sinusoids 8–12 · sampling-and-filtering 16–22 · sampling puzzle 6–12 · DFT values and properties 14–20 · spectral analysis 10–20.
> - New on FA2025 (Do & Snyder, the Fall 2026 pair): a DFT proof from the definitions (#7) and matching four DFT plots — 16-point, zero-padded, 32-point, Hamming (#8).

## 4. Day-by-day plan

Topic days: topic page → family recipe → past problems, closed book → repair misses. Keep FA2025 unseen until Monday (SP2025 is the backup if you have already seen it).

| day | do | families · past problems |
|---|---|---|
| **Fri Oct 30** | Submit HW9 (11:59 pm): DFT properties, zero padding, spectral analysis. Then the DTFT | [[problems/dtft-and-inverse-dtft\|DTFTs]]: FA2024 #2, FA2023 #2, SP2023 #2–#4, SP2021 #3, #7 · T/F bank §1 |
| **Sat Oct 31** | Unit 3 frequency response, then Unit 4 (fresh from Quiz 2); redo HW8 | [[problems/magnitude-phase-and-group-delay\|magnitude/phase]]: FA2024 #3, FA2023 #4, SP2023 #5 · [[problems/lti-response-to-sinusoids\|sinusoids]]: FA2024 #4, SP2023 #6 · [[problems/sampling-and-the-nyquist-rate\|sampling]]: FA2023 #3, SP2023 #8, SP2021 #9 · [[problems/digital-filtering-of-analog-signals\|A/D → filter → D/A]]: FA2024 #5, FA2023 #5, FA2021 #4–#5 · T/F §2–5 |
| **Sun Nov 1** | Unit 5. Evening: **write the sheet** (checklist below) | [[problems/dft-values-and-zero-padding\|DFT values]]: FA2024 #6–#7, SP2023 #9(a, c) · [[problems/circular-convolution-and-dft-properties\|DFT properties]]: FA2024 #8, FA2023 #7, SP2023 #9(b), FA2021 #3(b) · [[problems/dft-spectral-analysis\|spectral analysis]]: FA2024 #9, FA2023 #6, SP2023 #10, FA2021 #7 · T/F §6–7 |
| **Mon Nov 2** | **Timed full exam:** [[exams/midterm-2/past-exams/fall-2025\|FA2025]] (newest; Do & Snyder, the Fall 2026 pair; one sheet instead of its two), 2 h, no calculator — before class, in case he works its problems. Backup if you have already seen FA2025: [[exams/midterm-2/past-exams/spring-2025\|SP2025]]. **3 pm class: in-class review of past-exam problems** (§5) | grade; tag each lost point by family; repair; fix the sheet |
| **Tue Nov 3** | **[[exams/midterm-2/practice-exam\|Practice midterm]]**, timed 2 h | grade, repair; weakest family: its practice problems |
| **Wed Nov 4** | Rest. Reread the sheet and the trap callouts; no new problems | exam 7–9 pm, your NetID's room |

> [!tip] What to put on your sheet
> - [ ] §6 Unit 3 box: DTFT pairs and properties (sign of $n\,x[n]$), free values, Parseval; real- vs complex-$h$ sinusoid rules; $e^{-jM\omega}R(\omega)$; group delay.
> - [ ] §7 Unit 4 box: $\omega=\Omega T$, copies scaled $\frac1T$, Nyquist, alias reduction, ideal D/A both ways, cutoff $\omega_c/T$; ZOH in one line.
> - [ ] §8 Unit 5 box: DFT and inverse, bin ↔ $\omega_k$ ↔ Hz, zero padding, the property table read both ways — no DFT pairs table (Oct 16: $X[k]=X_d(2\pi k/N)$ is the pair), periodic sinc, two-bin cosine, lobe separation, window numbers.
> - [ ] One sketch template: $X_a\to X_d\to Y_d\to Y_a$ with axis labels; the rearranged-DFT steps (DFT-properties recipe, step 2).
> - [ ] Values without a calculator: $e^{-j\frac{2\pi}{N}k}$ for $N=4,6,8$; $\cos$, $\sin$ at multiples of $\frac{\pi}{6}$, $\frac{\pi}{4}$.
> - [ ] Your repeated mistakes from Monday and Tuesday.
> - [ ] Skip: circular-convolution tables and the FFT (keep the one line $N\ge N_1+N_2-1$).

## 5. What was said in lecture about the exam

Condensed from the recordings, Oct 7–30; quotes lightly edited. The official list is his email of Oct 28 and the course website.

- **Oct 7 · L16.** "Am I gonna ask you to freely draw a function like $1-2\cos\omega-\cos2\omega$? No, that's not fair." Non-symmetric FIR ($\{3,2,1\}$): "We never ask you to do it by hand."
  → Sketch magnitude and phase by hand only when the real amplitude is one cos or sin ($e^{-jM\omega}R(\omega)$, [[concepts/magnitude-and-phase-response|magnitude and phase]]); for unequal taps know the route (arctan, sign of the denominator), not the plot.
- **Oct 16 · L20.** A student asked how to summarise all the tables for the exam: "We don't actually need new table pairs. There's no need for it with the DFT … There are different properties, unfortunately."
  → Sheet: the DTFT pairs and the DFT property table ([[concepts/dft-properties|DFT properties]]); no DFT pairs table — $X[k]=X_d(2\pi k/N)$ does that job.
- **Oct 19 · L21 (guest lecturer).** Bin ↔ analog frequency: "These are the kinds of questions you can expect — homeworks, quizzes, exams." Modulo: "it has to become almost second nature."
  → Drill $k\leftrightarrow\omega_k=\frac{2\pi k}{N}\leftrightarrow f_k=\frac{kf_s}{N}$ both ways, bins past $N/2$ as negative frequencies ([[concepts/dft|DFT]]); $\langle n\rangle_N$ with negative arguments ([[concepts/circular-shift-and-reversal|circular shift]]).
- **Oct 21 · L22.** "Midterm two will cover all the lectures until this Friday." "Spectral analysis is on midterm two, but only the content of parts one and two." Part 3 (Oct 26): "not material that we can technically test you on."
  → Scope ends with spectral analysis part 2 = L23 (separation criteria, windows); skip the sliding-window / spectrogram demos.
- **Oct 21 · L22.** "Circular convolution will not be on midterm two." "You are responsible for DFT properties on midterm two, but not to do circular convolution" — it is "one of multiple properties"; on past exams "we X them out."
  → Read the property table both ways; keep one line for $x\circledast h\leftrightarrow X[k]H[k]$; skip FA2021 #6, FA2019 #1(g)–(h), #11.
- **Oct 21 · L22.** L21 slide Example 3: "this is midterm two content. This is applying DFT properties, but no circular convolution." HW9: properties (#1–2), zero padding (#3), notes from a DFT plot — "boils down to reading a table" (#5).
  → Do Example 3 on [[concepts/dft-properties|DFT properties]] cold ($Y[k]=\{X_2,-X_3,X_4,-X_5,X_0,-X_1\}$); redo [[homework/hw9|HW9]].
- **Oct 23 · L22–23.** "Finishing up those lecture 23 slides will be the last of your content for midterm two." On how the quizzes are written: the work "is, in effect, the same as what you did on very specific homework questions."
  → Said of Quiz 2, not promised for MT2 — still, HW5–9 are the closest template, and a Quiz 2 miss marks a topic to repair first ([[exams/quiz-2|Quiz 2 review]]).
- **Oct 26 · L23.** "Cover lectures 13 through 23 … which corresponds to homework five through nine." "I will upload midterm two practice exams, just like we had for midterm one" (with solutions). Part 3: "optional content … things that we can't really test you on."
  → Past exams with keys are on the course site; §3 maps them to families; FA2025 timed on Monday, SP2025 as the backup (§4).
- **Oct 28 · L23 wrap-up.** Computing circular convolution: "You have not had anything like that on your homeworks thus far." Responsible for the properties "like circular time shifting, circular frequency shifting, windowing." Practice exams: items with circular convolution "we strike it out."
  → Properties yes — shifts, modulation, the $x[n]w[n]$ row included; computation no.
- **Oct 28.** Email: homework and topic list, "one note sheet you can write for the exam"; HKN review "this Sunday from 3:30 to 6" (room heard as 1013 — check the email); Monday: "previous exam problems that I think are a good representation of your midterm content."
  → Mon Nov 2, 3 pm class = review of past-exam problems: bring the §3 table and your sheet draft.
- **Oct 30 · L24 (FFT).** "Fill out the conflict request form … specific to midterm two — the midterm one and midterm two forms are in fact different." The FFT "is not going to be on your midterm two … the first of the content that is post-midterm."
  → Need a conflict exam? Use the MT2 form on the course website. FFT: skip (FA2019 #1(j), #10).
- **Oct 30 · L24.** Which parts of spectral analysis? "One and two": "we would like you to be familiar with window functions and those … resolution criteria", "to the extent they're used on homework … mostly identifying frequencies." "We do not have class on Wednesday due to the midterm."
  → Windows and lobe criteria at HW9 #4–5 depth: peak bin → $\omega$ → Hz, amplitudes from heights, the rectangular/Hamming numbers ([[concepts/window-functions|windows]], [[concepts/frequency-resolution|resolution]]).

## 6. Unit 3 formulas for your sheet

> [!key] Formulas — Unit 3
> | | formula |
> |---|---|
> | [[concepts/dtft\|DTFT]] and inverse | $X_d(\omega)=\sum_{n=-\infty}^{\infty}x[n]\,e^{-j\omega n}$, $\quad x[n]=\frac{1}{2\pi}\int_{-\pi}^{\pi}X_d(\omega)\,e^{j\omega n}\,d\omega$ |
> | existence | $2\pi$-periodic; exists if $\sum_n\lvert x[n]\rvert<\infty$; $X_d(\omega)=X(e^{j\omega})$ needs the unit circle in the ROC ($2^nu[n]$: none; $u[n]\leftrightarrow\frac{1}{1-e^{-j\omega}}+\pi\delta(\omega)$) |
> | free values | $X_d(0)=\sum_n x[n]$, $\quad X_d(\pi)=\sum_n(-1)^n\,x[n]$, $\quad\int_{-\pi}^{\pi}X_d(\omega)\,d\omega=2\pi\,x[0]$ |
> | Parseval | $\sum_n\lvert x[n]\rvert^2=\frac{1}{2\pi}\int_{-\pi}^{\pi}\lvert X_d(\omega)\rvert^2\,d\omega$ |
> | finite [[concepts/dtft-pairs\|pairs]] | $\delta[n-k]\leftrightarrow e^{-j\omega k}$, $\quad u[n]-u[n-L]\leftrightarrow e^{-j\omega(L-1)/2}\,\frac{\sin(L\omega/2)}{\sin(\omega/2)}$ ($L$ odd, centred at $n=0$: no exponential) |
> | exponentials, $\lvert a\rvert<1$ | $a^nu[n]\leftrightarrow\frac{1}{1-ae^{-j\omega}}$, $\quad n\,a^nu[n]\leftrightarrow\frac{ae^{-j\omega}}{(1-ae^{-j\omega})^2}$ |
> | ideal low-pass | $\frac{\sin(\omega_cn)}{\pi n}$ ($\frac{\omega_c}{\pi}$ at $n=0$) $\leftrightarrow$ $1$ for $\lvert\omega\rvert\le\omega_c$, $0$ for $\omega_c<\lvert\omega\rvert\le\pi$ |
> | impulses (one period) | $1\leftrightarrow2\pi\delta(\omega)$, $\quad e^{j\omega_0n}\leftrightarrow2\pi\delta(\omega-\omega_0)$, $\quad\cos(\omega_0n)\leftrightarrow\pi[\delta(\omega-\omega_0)+\delta(\omega+\omega_0)]$, $\quad\sin(\omega_0n)\leftrightarrow-j\pi[\delta(\omega-\omega_0)-\delta(\omega+\omega_0)]$ |
> | shift, modulation ([[concepts/dtft-properties\|properties]]) | $x[n-k]\leftrightarrow e^{-j\omega k}X_d(\omega)$, $\quad e^{j\omega_0n}x[n]\leftrightarrow X_d(\omega-\omega_0)$, $\quad x[n]\cos(\omega_0n)\leftrightarrow\frac12X_d(\omega-\omega_0)+\frac12X_d(\omega+\omega_0)$ |
> | reversal, conjugation | $x[-n]\leftrightarrow X_d(-\omega)$, $\quad x^*[n]\leftrightarrow X_d^*(-\omega)$, $\quad x$ real $\Leftrightarrow X_d(-\omega)=X_d^*(\omega)$ |
> | $n\,x[n]$, convolution, window | $n\,x[n]\leftrightarrow+j\,\frac{dX_d(\omega)}{d\omega}$ (L14 prints $-j$: erratum), $\quad x[n]*h[n]\leftrightarrow X_d(\omega)H_d(\omega)$, $\quad x[n]w[n]\leftrightarrow\frac{1}{2\pi}\int_{-\pi}^{\pi}X_d(\theta)\,W_d(\omega-\theta)\,d\theta$ |
> | [[concepts/frequency-response\|frequency response]] | $H_d(\omega)=\sum_n h[n]\,e^{-j\omega n}$; inputs on all $n$: $e^{j\omega_0n}\mapsto H_d(\omega_0)\,e^{j\omega_0n}$, $\quad c\mapsto H_d(0)\,c$, $\quad(-1)^n\mapsto H_d(\pi)\,(-1)^n$ |
> | real $h$ | check $H_d(-\omega)=H_d^*(\omega)$; $A\cos(\omega_0n+\theta)\mapsto A\lvert H_d(\omega_0)\rvert\cos\big(\omega_0n+\theta+\angle H_d(\omega_0)\big)$ |
> | complex $h$ | $\cos(\omega_0n+\theta)\mapsto\frac12H_d(\omega_0)\,e^{j(\omega_0n+\theta)}+\frac12H_d(-\omega_0)\,e^{-j(\omega_0n+\theta)}$ |
> | [[concepts/magnitude-and-phase-response\|magnitude and phase]] | $H_d(\omega)=e^{-jM\omega}R(\omega)$, $R$ real ($M$ = centre of symmetric taps; antisymmetric: $j\,e^{-jM\omega}R(\omega)$, add $\frac{\pi}{2}$): $\lvert H_d\rvert=\lvert R\rvert$, $\;\angle H_d=-M\omega$, $\pm\pi$ where $R<0$, wrapped into $[-\pi,\pi]$ |
> | [[concepts/group-delay\|group delay]] | $\tau_{gd}(\omega)=-\frac{d\angle H_d(\omega)}{d\omega}$ between jumps; linear phase $-M\omega$ gives $\tau_{gd}=M$ |

## 7. Unit 4 formulas for your sheet

> [!key] Formulas — Unit 4
> | | formula |
> |---|---|
> | [[concepts/sampling\|sampling]] | $x[n]=x_a(nT)$, $f_s=\frac1T$; $X_d(\omega)=\frac1T\sum_{n}X_a\!\left(\frac{\omega-2\pi n}{T}\right)$: copies every $2\pi$, scaled $\frac1T$; $\omega=\Omega T$; $f$ Hz lands at $\omega=2\pi f/f_s$ |
> | [[concepts/nyquist-criterion\|Nyquist]] | $X_a(\Omega)=0$ for $\lvert\Omega\rvert\gt2\pi B$: no overlap $\iff f_s\gt2B\iff T\lt\frac{1}{2B}$ |
> | [[concepts/aliasing\|aliasing]] | $\cos(\Omega_0t)\to\cos(\Omega_0Tn)$; reduce $\Omega_0T$ mod $2\pi$ into $(-\pi,\pi]$; the D/A returns the $f_0-kf_s$ closest to $0$ (sine: sign matters) |
> | [[concepts/ideal-reconstruction\|ideal D/A]] | $x_a(t)=\sum_nx[n]\,\mathrm{sinc}\!\left(\frac{\pi(t-nT)}{T}\right)$, $\mathrm{sinc}(t)=\frac{\sin t}{t}$; $Y_a(\Omega)=T\,Y_d(\Omega T)$ for $\lvert\Omega\rvert\le\frac{\pi}{T}$, $0$ outside |
> | ZOH ([[homework/hw8\|HW8]] #4(a), briefly) | $x_a(t)=\sum_nx[n]\,p(t-nT)$, $p(t)=1$ for $0\le t\lt T$, else $0$: each sample held for $T$, a staircase |
> | [[concepts/digital-processing-of-analog-signals\|A/D → filter → D/A]] | digital cutoff $\omega_c$ ↔ analog $\omega_c/T$; no aliasing into the passband ⇒ $H_a(\Omega)=H_d(\Omega T)$ on $\lvert\Omega\rvert\lt\frac{\pi}{T}$ |

## 8. Unit 5 formulas for your sheet

> [!key] Formulas — Unit 5
> | | formula |
> |---|---|
> | [[concepts/dft\|DFT]] and inverse | $X[k]=\sum_{n=0}^{N-1}x[n]\,e^{-j\frac{2\pi k}{N}n}$, $\quad x[n]=\frac1N\sum_{k=0}^{N-1}X[k]\,e^{j\frac{2\pi k}{N}n}$, $\quad 0\le n,k\le N-1$; $N$-periodic in $n$ and $k$ |
> | evaluates the DTFT | $X[k]=X_d\!\left(\frac{2\pi k}{N}\right)$; bin $k$ ↔ $\omega_k=\frac{2\pi k}{N}$ ↔ $f_k=\frac{k\,f_s}{N}$ Hz (plus aliases $f_k+mf_s$); $X[0]=\sum_nx[n]$, $X[\frac N2]=\sum_n(-1)^nx[n]$ |
> | [[concepts/zero-padding\|zero padding]] | $L$ zeros appended: $\tilde X[k]=X_d\!\left(\frac{2\pi k}{N+L}\right)$ — the same DTFT, evaluated more densely; no new information, no better separation |
> | [[concepts/circular-shift-and-reversal\|shift, modulation]] | $x[\langle n-m\rangle_N]\leftrightarrow e^{-j\frac{2\pi km}{N}}X[k]$, $\quad e^{j\frac{2\pi ln}{N}}x[n]\leftrightarrow X[\langle k-l\rangle_N]$, $\quad\langle n\rangle_N$ = remainder of $n/N$ |
> | reversal, conjugation ([[concepts/dft-properties\|properties]]) | $x[\langle -n\rangle_N]\leftrightarrow X[\langle -k\rangle_N]$, $\quad x^*[n]\leftrightarrow X^*[\langle -k\rangle_N]$; real $x\Leftrightarrow X[\langle -k\rangle_N]=X^*[k]$; Parseval $\sum_n\lvert x[n]\rvert^2=\frac1N\sum_k\lvert X[k]\rvert^2$ |
> | [[concepts/circular-convolution\|circular convolution]] (property only; computation not on MT2) | $x[n]\circledast h[n]=\sum_{m=0}^{N-1}x[m]\,h[\langle n-m\rangle_N]\leftrightarrow X[k]H[k]$; equals $x*h$ when $N\ge N_1+N_2-1$ (pad both) |
> | [[concepts/periodic-sinc\|periodic sinc]] | $C(\omega)=e^{-j\omega(N-1)/2}\,\dfrac{\sin(N\omega/2)}{\sin(\omega/2)}$, $C(0)=N$; zeros at $\omega=\frac{2\pi k}{N}$, $k\ne0$; main lobe width $\frac{4\pi}{N}$ |
> | finite cosine ([[concepts/spectral-leakage\|leakage]]) | $x[n]=A\cos(\omega_0n)$, $0\le n\le N-1$: $X_d(\omega)=\frac A2C(\omega-\omega_0)+\frac A2C(\omega+\omega_0)$, $X[k]=X_d(\frac{2\pi k}{N})$. If $\omega_0=\frac{2\pi k_0}{N}$: two bins of height $\frac{NA}{2}$ at $k_0$ and $N-k_0$; otherwise leakage into every bin |
> | [[concepts/frequency-resolution\|lobe separation]] | full-lobe $\omega_2-\omega_1\gt\frac{4\pi}{N}\iff N\gt\frac{4\pi}{\Delta\omega}$; half-lobe $N\gt\frac{2\pi}{\Delta\omega}$; with $\Delta\omega=2\pi\,\Delta f/f_s$: $N\gt\frac{2f_s}{\Delta f}$ (full), $\frac{f_s}{\Delta f}$ (half). Zero padding does not help; a longer record does |
> | [[concepts/window-functions\|windows]] | $x[n]w[n]\leftrightarrow\frac{1}{2\pi}X_d*W_d$ (not an LTI system). Rectangular $u[n]-u[n-N]$: main lobe $\frac{4\pi}{N}$, first side lobe $-13$ dB. Hamming $0.54-0.46\cos\!\left(\frac{2\pi n}{N-1}\right)$: main lobe $\frac{8\pi}{N}$, side lobes $-42$ dB. Trade-off: narrow main lobe vs low side lobes |

## Related
[[exams/midterm-2/practice-exam|practice midterm]] · [[exams/midterm-2/past-exams/index|past exams]] · [[exams/midterm-2/true-false-bank|T/F bank]] · [[exams/quiz-2|Quiz 2 review]] · [[problems/index|problem families]] · [[concepts/index|topic pages]] · [[supplements/transform-tables|transform tables]] · [[0-toolkit/05-errata|errata]] · [[exams/index|all exams]]

### Sources for this page
Course website and instructor announcement (Oct 30, 2026); HW5–HW9 and HW8 key; Lectures 12–23 notes; the eight past Midterm 2 exams with keys (FA2019–FA2025); numbers in `verify/MT2_MREV_formulas.py`; lecture recordings Oct 7, 16, 19, 21, 23, 26, 28 and 30 (condensed).
