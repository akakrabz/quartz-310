---
title: "BIBO stability"
description: "Bounded input ⇒ bounded output. Three equivalent tests (definition with the bounded-input bound, absolutely summable h[n], ROC contains the unit circle), the HW4 proof, FIR always stable, recurring T/F traps."
tags: [concept, stability, systems, midterm-1]
aliases: ["BIBO stable", "BIBO stability", "stability", "stable", "unstable", "bounded-input bounded-output"]
---

*Lectures 3 (Fri Aug 28) §2.4, 4 §2.1 and 11 (Fri Sep 18) §1–1.1 · [[homework/hw4|HW4]] #2–#5 · families: [[problems/classifying-system-properties|classifying system properties]], [[problems/parameters-for-stability|parameters for stability]]*

> [!abstract] In one breath
> - Any system: every input with $\lvert x[n]\rvert<\beta$ gives $\lvert y[n]\rvert<\alpha<\infty$; prove by bounding, disprove with one bounded input.
> - LTI: stable $\iff \sum_n \lvert h[n]\rvert < \infty \iff$ ROC of $H(z)$ contains $\lvert z\rvert = 1$.
> - Causal: all poles inside the unit circle; anti-causal: all outside; two-sided: the unit circle runs through the ring. FIR is always stable.

## 1. Definition and the bounded-input test (Lecture 3 §2.4)

> [!key] BIBO stability (Lecture 3, eq. 11)
> $T$ is **BIBO stable** if for **every** input with $\lvert x[n]\rvert < \beta < \infty$ for all $n$, $\lvert y[n]\rvert < \alpha < \infty$ for all $n$. $\alpha$ may depend on $\beta$, not on $n$.

> [!recipe] Stability check for any system
> - **Stable:** assume $\lvert x[n]\rvert < \beta$; bound $\lvert y[n]\rvert$ by a constant (triangle inequality, $\lvert\sin(\cdot)\rvert \le 1$).
> - **Unstable:** **one** bounded input with unbounded output (grows as $n \to \pm\infty$, or infinite at some $n$: $\log 0$, division by $0$).

> [!question] Lecture 3, Exercise 7 and slides: BIBO stable?
> (E7) $y[n] = x^{10}[n] + e^{x[n]}$ (S1) $y[n] = \sin^2(x[n])$ (S2) $y[n] = \ln(\lvert x[n]\rvert)$

> [!success]- Answers
> **E7, stable:**
> $$
> \lvert y[n]\rvert \le \lvert x[n]\rvert^{10} + e^{\lvert x[n]\rvert} < \beta^{10} + e^{\beta} = \alpha < \infty .
> $$
> **S1, stable:** $0 \le y[n] \le 1$. **S2, unstable:** $x[n] = 0$ (or $\delta[n]$) gives $\ln 0 = -\infty$.

> [!question] Lecture 3 slides, extra practice: BIBO stable?
> (1) $y[n] = \dfrac{x[n]}{\lvert n\rvert + 1}$ (2) $y[n] = n\,(x[n]-x[n-1])$ (3) $y[n] = e^{x[n]}$ (4) $y[n] = x[n]\,x[0]$

> [!success]- Answers
> 1. Stable: $\lvert y[n]\rvert < \beta/(\lvert n\rvert + 1) \le \beta$.
> 2. **Unstable**: $x[n] = (-1)^n$ gives $\lvert y[n]\rvert = 2\lvert n\rvert \to \infty$.
> 3. Stable: $e^{x[n]} < e^{\beta}$.
> 4. Stable: $\lvert x[n]\,x[0]\rvert < \beta^2$.

## 2. Three equivalent tests for LTI systems (Lecture 11 §1)

> [!key] BIBO stability in the z-domain (Lecture 11, eqs. 1–2)
> 1. **Definition** (any system): $\lvert x[n]\rvert < \beta$ for all $n$ ⇒ $\lvert y[n]\rvert < \alpha$ for all $n$.
> 2. **Impulse response** (LTI, Lecture 4): $\sum_{n=-\infty}^{\infty} \lvert h[n]\rvert < \infty$.
> 3. **Transfer function** (LTI): the ROC of $H(z)$ contains $\lvert z\rvert = 1$.
> $$
> \text{LTI BIBO stable}\iff \sum_{n=-\infty}^{\infty}\lvert h[n]\rvert < \infty \iff \text{ROC of } H(z) \text{ contains } \lvert z\rvert = 1 .
> $$
> "Contains" is strict: $\lvert z\rvert > 1$ touches the unit circle but does not contain it ([[concepts/marginal-stability|marginally stable]]). Poles counted **after** cancellation.

> [!derivation]- Why the unit circle (Lecture 11, eqs. 3–7)
> The ROC is where the sum converges absolutely. On $\lvert z\rvert = 1$, $z = e^{j\theta}$ and $\lvert e^{-j\theta n}\rvert = 1$:
> $$
> \sum_{n=-\infty}^{\infty}\bigl\lvert h[n]z^{-n}\bigr\rvert\Big|_{z=e^{j\theta}} = \sum_{n=-\infty}^{\infty}\lvert h[n]\rvert\,\bigl\lvert e^{-j\theta n}\bigr\rvert = \sum_{n=-\infty}^{\infty}\lvert h[n]\rvert .
> $$
> (The notes write $\lvert h[n]e^{-j\theta n}\rvert$ as $\sqrt{(h[n]e^{-j\theta n})(h^*[n]e^{j\theta n})}$.) The converse also holds.

> [!derivation]- Proof: $\sum\lvert h\rvert<\infty\iff$ BIBO stable (HW4 #2)
> **Sufficiency.**
> $$
> \lvert y[n]\rvert\le\sum_k\lvert h[k]\rvert\,\lvert x[n-k]\rvert\le B_x\sum_k\lvert h[k]\rvert<\infty .
> $$
> **Necessity.** If $\sum_k\lvert h[k]\rvert=\infty$, take $x[n]=h^*[-n]/\lvert h[-n]\rvert$ (0 where $h[-n]=0$); then $y[0]=\sum_k\lvert h[k]\rvert=\infty$.

- $a^nu[n]$ summable iff $\lvert a\rvert<1$; $a^nu[-n-1]$ iff $\lvert a\rvert>1$.
- **Not LTI:** bound $\lvert y\rvert$ by $\beta$, or give one bounded input with unbounded output ($x=1$ into $\lvert n\rvert x[n]$).

## 3. Stability from the ROC shape (Lecture 11 §1.1)

A sample at $n < 0$ gives $z^{\lvert n\rvert}$ (blows up at $\lvert z\rvert = \infty$); at $n > 0$, $z^{-n}$ (blows up at $z = 0$). Slides 6–7 corners ([[concepts/sided-sequences|sided sequences]], [[concepts/causality|causality]]):

| | $n_0 < 0$ | $n_0 \ge 0$ |
|---|---|---|
| **right-sided** | non-causal, $\lvert p_{\max}\rvert < \lvert z\rvert < \infty$; e.g. $u[n+1] = \delta[n+1] + u[n] \leftrightarrow z + \dfrac{1}{1-z^{-1}}$, $1 < \lvert z\rvert < \infty$ | **causal**, $\lvert z\rvert > \lvert p_{\max}\rvert$; e.g. $(\tfrac12)^{n-3}u[n-3] \leftrightarrow \dfrac{z^{-3}}{1-\frac12 z^{-1}}$, $\lvert z\rvert > \tfrac12$ |
| **left-sided** | **anti-causal**, $\lvert z\rvert < \lvert p_{\min}\rvert$; e.g. $-3^{n+2}u[-n-3] \leftrightarrow \dfrac{z^{2}}{1-3z^{-1}}$, $\lvert z\rvert < 3$ | non-causal, $0 < \lvert z\rvert < \lvert p_{\min}\rvert$; e.g. $-3^{n-3}u[-n+2] \leftrightarrow \dfrac{z^{-3}}{1-3z^{-1}}$, $0 < \lvert z\rvert < 3$ |

- $p_{\max}$, $p_{\min}$: largest/smallest-magnitude **finite** poles; the ROC stops at the first pole.
- Exception $n_0 = 0$ left-sided ($2^n u[-n] \leftrightarrow \frac{1}{1 - z/2}$, $\lvert z\rvert < 2$): includes $z = 0$, still non-causal. Exam rule: **ROC includes $\lvert z\rvert = \infty$ $\iff$ causal.**
- Two-sided: $h[n] = h_l[n] + h_r[n]$, $h_r = h[n]u[n]$, $h_l = h[n]u[-n-1]$; ROC at least $\{\lvert z\rvert > \lvert p_{\max,h_r}\rvert\} \cap \{\lvert z\rvert < \lvert p_{\min,h_l}\rvert\}$, exactly that unless a zero cancels one of those poles.
- The full ROC ⇔ causality ⇔ stability table (Lecture 11, Table 1): [[concepts/region-of-convergence|region of convergence]] §4. **Causal: stable iff all poles inside the unit circle; anti-causal: iff all outside; two-sided: iff the unit circle runs through the ring.**

<figure class="ece-fig"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 680 306" width="680" height="306" role="img" style="font-family:'Source Sans 3','Source Sans Pro',system-ui,sans-serif;font-size:14px;max-width:100%;height:auto"><line x1="170.0" y1="14.0" x2="200.0" y2="14.0" stroke="currentColor" stroke-width="1.6" stroke-dasharray="5 4" stroke-linecap="round"/><text x="206.0" y="18.0" text-anchor="start" fill="currentColor" style="font-size:12.5px;">unit circle |z| = 1</text><line x1="347.0" y1="9.0" x2="357.0" y2="19.0" stroke="var(--hi)" stroke-width="2.4" stroke-linecap="round"/><line x1="347.0" y1="19.0" x2="357.0" y2="9.0" stroke="var(--hi)" stroke-width="2.4" stroke-linecap="round"/><text x="362.0" y="18.0" text-anchor="start" fill="currentColor" style="font-size:12.5px;">pole</text><rect x="410" y="7" width="16" height="14" fill="var(--accent)" fill-opacity="0.22" stroke="var(--accent)" stroke-width="1.2"/><text x="432.0" y="18.0" text-anchor="start" fill="currentColor" style="font-size:12.5px;">ROC</text><clipPath id="l11ca"><rect x="15.0" y="29.0" width="196.0" height="196.0"/></clipPath><path d="M15.0,29.0 h196.0 v196.0 h-196.0 Z M153.00,127.00 A40.00,40.00 0 1,0 73.00,127.00 A40.00,40.00 0 1,0 153.00,127.00 Z" fill="var(--accent)" fill-opacity="0.22" fill-rule="evenodd" stroke="none" clip-path="url(#l11ca)"/><circle cx="113.0" cy="127.0" r="40.0" fill="none" stroke="var(--accent)" stroke-width="1.6"/><line x1="15.0" y1="127.0" x2="211.0" y2="127.0" stroke="currentColor" stroke-width="1.0" opacity="0.7" stroke-linecap="round"/><line x1="113.0" y1="29.0" x2="113.0" y2="225.0" stroke="currentColor" stroke-width="1.0" opacity="0.7" stroke-linecap="round"/><circle cx="113.0" cy="127.0" r="50.0" fill="none" stroke="currentColor" stroke-width="1.6" stroke-dasharray="5 4"/><line x1="117.0" y1="121.0" x2="129.0" y2="133.0" stroke="var(--hi)" stroke-width="2.4" stroke-linecap="round"/><line x1="117.0" y1="133.0" x2="129.0" y2="121.0" stroke="var(--hi)" stroke-width="2.4" stroke-linecap="round"/><line x1="147.0" y1="121.0" x2="159.0" y2="133.0" stroke="var(--hi)" stroke-width="2.4" stroke-linecap="round"/><line x1="147.0" y1="133.0" x2="159.0" y2="121.0" stroke="var(--hi)" stroke-width="2.4" stroke-linecap="round"/><text x="210.0" y="144.0" text-anchor="end" fill="var(--muted)" style="font-size:11px;">Re</text><text x="118.0" y="41.0" text-anchor="start" fill="var(--muted)" style="font-size:11px;">Im</text><text x="113.0" y="245.0" text-anchor="middle" fill="currentColor" style="font-size:14px;font-weight:600;">causal: |z| &gt; |p_max|</text><text x="113.0" y="263.0" text-anchor="middle" fill="currentColor" style="font-size:13px;">poles ⅕, ⅘ → |z| &gt; ⅘</text><text x="113.0" y="280.0" text-anchor="middle" fill="var(--muted)" style="font-size:12px;">stable ⇔ |p_max| &lt; 1</text><clipPath id="l11cb"><rect x="242.0" y="29.0" width="196.0" height="196.0"/></clipPath><path d="M415.00,127.00 A75.00,75.00 0 1,0 265.00,127.00 A75.00,75.00 0 1,0 415.00,127.00 Z" fill="var(--accent)" fill-opacity="0.22" fill-rule="evenodd" stroke="none" clip-path="url(#l11cb)"/><circle cx="340.0" cy="127.0" r="75.0" fill="none" stroke="var(--accent)" stroke-width="1.6"/><line x1="242.0" y1="127.0" x2="438.0" y2="127.0" stroke="currentColor" stroke-width="1.0" opacity="0.7" stroke-linecap="round"/><line x1="340.0" y1="29.0" x2="340.0" y2="225.0" stroke="currentColor" stroke-width="1.0" opacity="0.7" stroke-linecap="round"/><circle cx="340.0" cy="127.0" r="50.0" fill="none" stroke="currentColor" stroke-width="1.6" stroke-dasharray="5 4"/><line x1="409.0" y1="121.0" x2="421.0" y2="133.0" stroke="var(--hi)" stroke-width="2.4" stroke-linecap="round"/><line x1="409.0" y1="133.0" x2="421.0" y2="121.0" stroke="var(--hi)" stroke-width="2.4" stroke-linecap="round"/><text x="437.0" y="144.0" text-anchor="end" fill="var(--muted)" style="font-size:11px;">Re</text><text x="345.0" y="41.0" text-anchor="start" fill="var(--muted)" style="font-size:11px;">Im</text><text x="340.0" y="245.0" text-anchor="middle" fill="currentColor" style="font-size:14px;font-weight:600;">anti-causal: |z| &lt; |p_min|</text><text x="340.0" y="263.0" text-anchor="middle" fill="currentColor" style="font-size:13px;">pole 3/2 → |z| &lt; 3/2</text><text x="340.0" y="280.0" text-anchor="middle" fill="var(--muted)" style="font-size:12px;">stable ⇔ |p_min| &gt; 1</text><clipPath id="l11cc"><rect x="469.0" y="29.0" width="196.0" height="196.0"/></clipPath><path d="M633.67,127.00 A66.67,66.67 0 1,0 500.33,127.00 A66.67,66.67 0 1,0 633.67,127.00 Z M592.00,127.00 A25.00,25.00 0 1,0 542.00,127.00 A25.00,25.00 0 1,0 592.00,127.00 Z" fill="var(--accent)" fill-opacity="0.22" fill-rule="evenodd" stroke="none" clip-path="url(#l11cc)"/><circle cx="567.0" cy="127.0" r="25.0" fill="none" stroke="var(--accent)" stroke-width="1.6"/><circle cx="567.0" cy="127.0" r="66.7" fill="none" stroke="var(--accent)" stroke-width="1.6"/><line x1="469.0" y1="127.0" x2="665.0" y2="127.0" stroke="currentColor" stroke-width="1.0" opacity="0.7" stroke-linecap="round"/><line x1="567.0" y1="29.0" x2="567.0" y2="225.0" stroke="currentColor" stroke-width="1.0" opacity="0.7" stroke-linecap="round"/><circle cx="567.0" cy="127.0" r="50.0" fill="none" stroke="currentColor" stroke-width="1.6" stroke-dasharray="5 4"/><line x1="586.0" y1="121.0" x2="598.0" y2="133.0" stroke="var(--hi)" stroke-width="2.4" stroke-linecap="round"/><line x1="586.0" y1="133.0" x2="598.0" y2="121.0" stroke="var(--hi)" stroke-width="2.4" stroke-linecap="round"/><line x1="494.3" y1="121.0" x2="506.3" y2="133.0" stroke="var(--hi)" stroke-width="2.4" stroke-linecap="round"/><line x1="494.3" y1="133.0" x2="506.3" y2="121.0" stroke="var(--hi)" stroke-width="2.4" stroke-linecap="round"/><text x="664.0" y="144.0" text-anchor="end" fill="var(--muted)" style="font-size:11px;">Re</text><text x="572.0" y="41.0" text-anchor="start" fill="var(--muted)" style="font-size:11px;">Im</text><text x="567.0" y="245.0" text-anchor="middle" fill="currentColor" style="font-size:14px;font-weight:600;">two-sided: a &lt; |z| &lt; b</text><text x="567.0" y="263.0" text-anchor="middle" fill="currentColor" style="font-size:13px;">poles ½, −4/3 → ½ &lt; |z| &lt; 4/3</text><text x="567.0" y="280.0" text-anchor="middle" fill="var(--muted)" style="font-size:12px;">stable ⇔ a &lt; 1 &lt; b</text></svg><figcaption><strong>ROC shape gives causality; the dashed unit circle gives stability.</strong> Left to right: slide 10 causal (poles ⅕, ⅘), notes Fig. 2b left-sided −(3/2)ⁿu[−n−1], slide 10 two-sided (poles ½, −4/3); all three ROCs contain |z| = 1.</figcaption></figure>

> [!recipe] "Is it stable?" / "Which $h[n]$ is the stable one?"
> 1. Factor; **cancel common factors first**; list finite poles and magnitudes.
> 2. *Causality given* → ROC forced → does it contain $\lvert z\rvert = 1$?
> 3. *Stability given* → ROC = the ring containing $\lvert z\rvert = 1$: pole **inside** → $A\,p^n u[n]$; pole **outside** → $-A\,p^n u[-n-1]$; pole **on** the circle → no stable version.
> 4. Causality type from the ROC (Table 1).

> [!question] Lecture 11, slide 10 — stable $h[n]$ and its causality type
> (A) $H(z) = \dfrac{1}{1-\frac12 z^{-1}} + \dfrac{1}{1+\frac43 z^{-1}}$  (B) $H(z) = \dfrac{1}{1-\frac15 z^{-1}} + \dfrac{1}{1-\frac45 z^{-1}}$

> [!success]- Answers
> **(A)** Poles $\tfrac12$, $-\tfrac43$. $\lvert z\rvert > \tfrac43$ ✗; $\lvert z\rvert < \tfrac12$ ✗; $\tfrac12 < \lvert z\rvert < \tfrac43$ ✓:
> $$
> h[n] = \left(\tfrac12\right)^n u[n] - \left(-\tfrac43\right)^n u[-n-1], \qquad \sum_n \lvert h[n]\rvert = 2 + 3 = 5 ,
> $$
> **non-causal** (two-sided).
> **(B)** Poles $\tfrac15$, $\tfrac45$ inside: $\lvert z\rvert > \tfrac45$ contains $\lvert z\rvert = 1$; $h[n] = \left(\tfrac15\right)^n u[n] + \left(\tfrac45\right)^n u[n]$ ($\sum\lvert h\rvert = \tfrac{25}{4}$), **causal**.

> [!question] Lecture 11, slide 11 — can an LTI FIR system be unstable? Time and z-domain.

> [!success]- Answer
> No. $h[n] = \{\underset{\uparrow}{b_0}, b_1, \dots, b_{N-1}\}$.
> - Time: $\sum_n \lvert h[n]\rvert = \sum_{k=0}^{N-1}\lvert b_k\rvert \le N \max_k\lvert b_k\rvert < \infty$.
> - z: $H(z) = \sum_{k=0}^{N-1} b_k z^{-k}$ has **no finite poles**; ROC is all $z$ except possibly $0$ (or $\infty$ if non-causal), so it contains $\lvert z\rvert = 1$. **FIR ⇒ stable** ([[concepts/fir-and-iir|FIR and IIR]]).

> [!trap] Stability slips
> - Bounded $h$ is not stable: $h=u[n]$ ([[exams/midterm-1/past-exams/fall-2025|FA2025 #1a]], [[exams/midterm-1/past-exams/fall-2019|FA2019 #1c]]); $\sum\lvert h\rvert$ is an LTI-only test ([[exams/midterm-1/past-exams/spring-2025|SP2025 #1b]]).
> - Poles alone do not decide stability; the ROC does: $\dfrac{1}{1-0.5z^{-1}} + \dfrac{1}{1-2z^{-1}}$ is stable with $\tfrac12 < \lvert z\rvert < 2$; a formula without an ROC does not decide ([[exams/midterm-1/past-exams/fall-2024|FA2024 #1f]]). Told "stable": the ROC is forced; stable $\dfrac{1}{1-3z^{-1}}$ must be anti-causal.
> - $\lvert z\rvert > 1$ does not contain $\lvert z\rvert = 1$. $\delta[n]$ breaks a system only if $h$ itself is unbounded; for poles on $\lvert z\rvert=1$ use a matching input ([[concepts/marginal-stability|marginal stability]]).
> - Stable system, unbounded input: output can be bounded ($h=\delta[n]-2\delta[n-1]$ maps $2^nu[n]$ to $\delta[n]$). Unstable system: only *some* bounded input blows up.
> - Two unstable systems can combine to a stable one, in parallel ($u[n]+(\delta[n]-u[n])$) or series ($\frac{1-2z^{-1}}{1-3z^{-1}}\cdot\frac{1-3z^{-1}}{1-2z^{-1}}=1$, both causal); unstable in series with stable likewise ([[homework/hw4|HW4]] #5, [[concepts/pole-zero-cancellation|pole-zero cancellation]]).
> - Two-sided can be stable: $(\tfrac12)^{\lvert n\rvert}$.

> [!exam] On all 7 past exams
> Stable/causal $h[n]$ from poles; parameters that place a zero on a bad pole; two-sided systems as backward/forward recursions; the Stable column of every property table; many True/False items.
> [[exams/midterm-1/past-exams/fall-2025|FA2025 #1, #7(b)]] · [[exams/midterm-1/past-exams/spring-2025|SP2025 #1, #7]] · [[exams/midterm-1/past-exams/fall-2024|FA2024 #1, #7]] · [[exams/midterm-1/past-exams/fall-2023|FA2023 #1, #7(c)]] · [[exams/midterm-1/past-exams/spring-2023|SP2023 #1, #7]] · [[exams/midterm-1/past-exams/spring-2021|SP2021 #1, #5]] · [[exams/midterm-1/past-exams/fall-2019|FA2019 #1, #10(d)]] · families: [[problems/parameters-for-stability|parameters for stability]], [[problems/two-sided-systems-as-recursions|two-sided recursions]], [[problems/classifying-system-properties|classifying system properties]] · [[exams/midterm-1/true-false-bank|T/F bank]]

**Where it appears:** [[1-signals-and-systems/03-system-properties|L3]] §2.4 (eq. 11, Exercise 7), [[1-signals-and-systems/04-impulse-response-and-convolution|L4]] §2.1, [[2-z-transform/11-bibo-stability-and-causality|L11]] §1–1.1 (eqs. 1–18, Figs. 1–2, Table 1, slides 6–11), [[3-fourier-analysis/14-dtft-properties|L14]]; [[homework/hw4|HW4]] #2–#5; [[problems/classifying-system-properties|Classifying system properties (the L / TI / C / S table)]], [[problems/unbounded-outputs-and-pole-matching|Unbounded outputs and pole matching]], [[problems/parameters-for-stability|Parameters for stability]]; [[exams/midterm-1/true-false-bank]].

## Related
[[concepts/lti-system|LTI system]] · [[concepts/impulse-response|impulse response]] · [[concepts/region-of-convergence|ROC]] · [[concepts/poles-and-zeros|poles and zeros]] · [[concepts/pole-zero-cancellation|pole-zero cancellation]] · [[concepts/causality|causality]] · [[concepts/marginal-stability|marginal stability]] · [[concepts/sided-sequences|sided sequences]] · [[concepts/fir-and-iir|FIR and IIR]] · [[demos/pole-zero-and-roc-explorer|pole-zero and ROC explorer]]

### Sources for this page
Lecture 3 §2.4 (eq. 11, Exercise 7) and slides; Lecture 4 §2.1; Lecture 11 §1–1.1 (eqs. 1–18, Figs. 1–2, Table 1) and slides 6–11; Lecture 14 §1; HW4 #2, #3, #5 solutions; Midterm 1 T/F items and keys cited.
