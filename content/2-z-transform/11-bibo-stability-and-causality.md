---
title: "Lecture 11 — BIBO stability and causality in the z-domain"
description: "The third BIBO test (the ROC contains the unit circle), how the shape of the ROC encodes causal / anti-causal / two-sided, reading stability off the poles, why FIR systems are always stable, and which bounded inputs break an unstable or marginally stable system (pole matching)."
tags: [lecture, midterm-1, stability, roc, z-transform]
lecture: 11
---

*Lecture 11 · Fri Sep 18, 2026 · notes + slides "BIBO stability and causality" · prev: [[2-z-transform/10-improper-transfer-functions-and-system-algebra|Lecture 10]] · next: [[3-fourier-analysis/12-convolution-as-template-matching|Lecture 12]]*

> [!abstract] In one breath
> An LTI system is BIBO stable $\iff \sum_n |h[n]| < \infty \iff$ **the ROC of $H(z)$ contains the unit circle $|z| = 1$.** The *shape* of the ROC says which way $h[n]$ runs: outside a circle (all the way to $\infty$) = causal, inside a circle = left-sided, a ring = two-sided. Put the two together and stability becomes a glance at the poles: a causal system is stable iff every pole is inside the unit circle, an anti-causal one iff every pole is outside, a two-sided one iff its ring straddles $|z| = 1$. Unstable systems blow up for almost any bounded input — unless the input's zero cancels the bad pole. **Marginally stable** systems (poles *on* the unit circle) blow up only when the input puts a pole exactly on one of those poles: **pole matching**, which appears on all seven past exams.

## 1. Three equivalent tests for BIBO stability

By now we have three ways to decide whether a system is bounded-input bounded-output stable:

1. **Definition** (any system, [[1-signals-and-systems/03-system-properties|Lecture 3]]): for every input with $|x[n]| < \beta$ for all $n$, the output satisfies $|y[n]| < \alpha$ for all $n$ ($\alpha, \beta < \infty$).
2. **Impulse response** (LTI only, [[1-signals-and-systems/04-impulse-response-and-convolution|Lecture 4]]): $\sum_{n=-\infty}^{\infty} |h[n]| < \infty$.
3. **Transfer function** (LTI with a z-transform, this lecture): the ROC of $H(z)$ contains $|z| = 1$.

> [!key] BIBO stability in the z-domain
> $$
> \begin{aligned}
> &\text{LTI system BIBO stable} \\
> &\iff \sum_{n=-\infty}^{\infty}|h[n]| < \infty \\
> &\iff \text{ROC of } H(z) \text{ contains the unit circle } |z| = 1 .
> \end{aligned}
> $$
> "Contains" is strict: an ROC $|z| > 1$ *touches* the unit circle but does not contain it — that system is **not** stable (it is marginally stable, §6).

> [!derivation]- Why the unit circle (notes, eqs. 3–7)
> The ROC is where the z-transform sum converges absolutely. On the unit circle write $z = e^{j\theta}$; since $|e^{-j\theta n}| = 1$,
> $$
> \sum_{n=-\infty}^{\infty}\bigl|h[n]z^{-n}\bigr|\Big|_{z=e^{j\theta}} = \sum_{n=-\infty}^{\infty}|h[n]|\,\bigl|e^{-j\theta n}\bigr| = \sum_{n=-\infty}^{\infty}|h[n]| .
> $$
> So "the sum converges at a point of $|z|=1$" and "$h$ is absolutely summable" are literally the same statement (the notes write $|h[n]e^{-j\theta n}|$ as $\sqrt{(h[n]e^{-j\theta n})(h^*[n]e^{j\theta n})}$ to get there). The converse direction holds as well.

## 2. Sidedness, causality and the shape of the ROC

A sequence is **right-sided** if $x[n] = 0$ for $n < n_0$, **left-sided** if $x[n] = 0$ for $n > n_0$ ($n_0$ may be positive or negative), and **two-sided** if it extends to both $-\infty$ and $+\infty$ ([[concepts/sided-sequences|sided sequences]]). For systems the notes use three words:

- **Causal** — depends only on present and past inputs (and outputs): $h[n] = 0$ for $n < 0$.
- **Anti-causal** — depends only on *future* inputs and outputs: $h[n] = 0$ for $n \ge 0$.
- **Non-causal** — depends on some future inputs *and* on present and/or past ones. (The notes print "Non-causal – a system is *causal* if…"; read "non-causal".)

Where $n_0$ sits decides whether $z = \infty$ and $z = 0$ belong to the ROC: a sample at $n < 0$ contributes a positive power $z^{|n|}$, which blows up at $|z| = \infty$; a sample at $n > 0$ contributes $z^{-n}$, which blows up at $z = 0$. That gives the four corner cases of the slides (all four checked by partial sums):

| | $n_0 < 0$ | $n_0 \ge 0$ |
|---|---|---|
| **right-sided** | non-causal, ROC $\lvert p_{\max}\rvert < \lvert z\rvert < \infty$ — e.g. $u[n+1] = \delta[n+1] + u[n] \leftrightarrow z + \dfrac{1}{1-z^{-1}}$, $1 < \lvert z\rvert < \infty$ | **causal**, ROC $\lvert z\rvert > \lvert p_{\max}\rvert$ (includes $\infty$) — e.g. $(\tfrac12)^{n-3}u[n-3] \leftrightarrow \dfrac{z^{-3}}{1-\frac12 z^{-1}}$, $\lvert z\rvert > \tfrac12$ |
| **left-sided** | **anti-causal**, ROC $\lvert z\rvert < \lvert p_{\min}\rvert$ (includes $0$) — e.g. $-3^{n+2}u[-n-3] \leftrightarrow \dfrac{z^{2}}{1-3z^{-1}}$, $\lvert z\rvert < 3$ | non-causal, ROC $0 < \lvert z\rvert < \lvert p_{\min}\rvert$ — e.g. $-3^{n-3}u[-n+2] \leftrightarrow \dfrac{z^{-3}}{1-3z^{-1}}$, $0 < \lvert z\rvert < 3$ |

Here $p_{\max}$ and $p_{\min}$ are the largest- and smallest-magnitude **finite** poles (poles not at $z = 0$ or $z = \infty$); the ROC can never contain a pole, so it stops at the first pole it meets.

> [!note] The $n_0 = 0$ corner
> A left-sided response with $n_0 = 0$, e.g. $h[n] = 2^n u[-n] \leftrightarrow \dfrac{1}{1 - z/2}$, has ROC $|z| < 2$ *including* $z = 0$, yet it is non-causal (it uses $x[n]$ and future inputs), not anti-causal. The notes flag this ("except when $n_0$ is exactly zero, but it is still non-causal!"). The rule you actually use on exams is the one at infinity: **ROC includes $|z| = \infty$ $\iff$ causal.**

Right-sided systems have *past* feedback and run forward in time ($y[n] = y[n-1] + x[n]$); left-sided systems have *future* feedback and run backward from the far future (slide 7: $y[n] = 3y[n+1] + x[n+1]$, i.e. $H(z) = \dfrac{z}{1-3z}$ with ROC $|z| < \tfrac13$). That is exactly how an exam asks you to implement the anti-causal half of a stable two-sided system (§7).

A two-sided $h[n]$ splits as $h[n] = h_l[n] + h_r[n]$ with $h_r[n] = h[n]u[n]$ and $h_l[n] = h[n]u[-n-1]$, so its ROC is at least the intersection $\{|z| > |p_{\max,h_r}|\} \cap \{|z| < |p_{\min,h_l}|\}$ — a ring — and exactly that ring unless a zero cancels one of those poles.

<figure class="ece-fig"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 680 306" width="680" height="306" role="img" style="font-family:'Source Sans 3','Source Sans Pro',system-ui,sans-serif;font-size:14px;max-width:100%;height:auto"><line x1="170.0" y1="14.0" x2="200.0" y2="14.0" stroke="currentColor" stroke-width="1.6" stroke-dasharray="5 4" stroke-linecap="round"/><text x="206.0" y="18.0" text-anchor="start" fill="currentColor" style="font-size:12.5px;">unit circle |z| = 1</text><line x1="347.0" y1="9.0" x2="357.0" y2="19.0" stroke="var(--hi)" stroke-width="2.4" stroke-linecap="round"/><line x1="347.0" y1="19.0" x2="357.0" y2="9.0" stroke="var(--hi)" stroke-width="2.4" stroke-linecap="round"/><text x="362.0" y="18.0" text-anchor="start" fill="currentColor" style="font-size:12.5px;">pole</text><rect x="410" y="7" width="16" height="14" fill="var(--accent)" fill-opacity="0.22" stroke="var(--accent)" stroke-width="1.2"/><text x="432.0" y="18.0" text-anchor="start" fill="currentColor" style="font-size:12.5px;">ROC</text><clipPath id="l11ca"><rect x="15.0" y="29.0" width="196.0" height="196.0"/></clipPath><path d="M15.0,29.0 h196.0 v196.0 h-196.0 Z M153.00,127.00 A40.00,40.00 0 1,0 73.00,127.00 A40.00,40.00 0 1,0 153.00,127.00 Z" fill="var(--accent)" fill-opacity="0.22" fill-rule="evenodd" stroke="none" clip-path="url(#l11ca)"/><circle cx="113.0" cy="127.0" r="40.0" fill="none" stroke="var(--accent)" stroke-width="1.6"/><line x1="15.0" y1="127.0" x2="211.0" y2="127.0" stroke="currentColor" stroke-width="1.0" opacity="0.7" stroke-linecap="round"/><line x1="113.0" y1="29.0" x2="113.0" y2="225.0" stroke="currentColor" stroke-width="1.0" opacity="0.7" stroke-linecap="round"/><circle cx="113.0" cy="127.0" r="50.0" fill="none" stroke="currentColor" stroke-width="1.6" stroke-dasharray="5 4"/><line x1="117.0" y1="121.0" x2="129.0" y2="133.0" stroke="var(--hi)" stroke-width="2.4" stroke-linecap="round"/><line x1="117.0" y1="133.0" x2="129.0" y2="121.0" stroke="var(--hi)" stroke-width="2.4" stroke-linecap="round"/><line x1="147.0" y1="121.0" x2="159.0" y2="133.0" stroke="var(--hi)" stroke-width="2.4" stroke-linecap="round"/><line x1="147.0" y1="133.0" x2="159.0" y2="121.0" stroke="var(--hi)" stroke-width="2.4" stroke-linecap="round"/><text x="210.0" y="144.0" text-anchor="end" fill="var(--muted)" style="font-size:11px;">Re</text><text x="118.0" y="41.0" text-anchor="start" fill="var(--muted)" style="font-size:11px;">Im</text><text x="113.0" y="245.0" text-anchor="middle" fill="currentColor" style="font-size:14px;font-weight:600;">causal: |z| &gt; |p_max|</text><text x="113.0" y="263.0" text-anchor="middle" fill="currentColor" style="font-size:13px;">poles ⅕, ⅘ → |z| &gt; ⅘</text><text x="113.0" y="280.0" text-anchor="middle" fill="var(--muted)" style="font-size:12px;">stable ⇔ |p_max| &lt; 1</text><clipPath id="l11cb"><rect x="242.0" y="29.0" width="196.0" height="196.0"/></clipPath><path d="M415.00,127.00 A75.00,75.00 0 1,0 265.00,127.00 A75.00,75.00 0 1,0 415.00,127.00 Z" fill="var(--accent)" fill-opacity="0.22" fill-rule="evenodd" stroke="none" clip-path="url(#l11cb)"/><circle cx="340.0" cy="127.0" r="75.0" fill="none" stroke="var(--accent)" stroke-width="1.6"/><line x1="242.0" y1="127.0" x2="438.0" y2="127.0" stroke="currentColor" stroke-width="1.0" opacity="0.7" stroke-linecap="round"/><line x1="340.0" y1="29.0" x2="340.0" y2="225.0" stroke="currentColor" stroke-width="1.0" opacity="0.7" stroke-linecap="round"/><circle cx="340.0" cy="127.0" r="50.0" fill="none" stroke="currentColor" stroke-width="1.6" stroke-dasharray="5 4"/><line x1="409.0" y1="121.0" x2="421.0" y2="133.0" stroke="var(--hi)" stroke-width="2.4" stroke-linecap="round"/><line x1="409.0" y1="133.0" x2="421.0" y2="121.0" stroke="var(--hi)" stroke-width="2.4" stroke-linecap="round"/><text x="437.0" y="144.0" text-anchor="end" fill="var(--muted)" style="font-size:11px;">Re</text><text x="345.0" y="41.0" text-anchor="start" fill="var(--muted)" style="font-size:11px;">Im</text><text x="340.0" y="245.0" text-anchor="middle" fill="currentColor" style="font-size:14px;font-weight:600;">anti-causal: |z| &lt; |p_min|</text><text x="340.0" y="263.0" text-anchor="middle" fill="currentColor" style="font-size:13px;">pole 3/2 → |z| &lt; 3/2</text><text x="340.0" y="280.0" text-anchor="middle" fill="var(--muted)" style="font-size:12px;">stable ⇔ |p_min| &gt; 1</text><clipPath id="l11cc"><rect x="469.0" y="29.0" width="196.0" height="196.0"/></clipPath><path d="M633.67,127.00 A66.67,66.67 0 1,0 500.33,127.00 A66.67,66.67 0 1,0 633.67,127.00 Z M592.00,127.00 A25.00,25.00 0 1,0 542.00,127.00 A25.00,25.00 0 1,0 592.00,127.00 Z" fill="var(--accent)" fill-opacity="0.22" fill-rule="evenodd" stroke="none" clip-path="url(#l11cc)"/><circle cx="567.0" cy="127.0" r="25.0" fill="none" stroke="var(--accent)" stroke-width="1.6"/><circle cx="567.0" cy="127.0" r="66.7" fill="none" stroke="var(--accent)" stroke-width="1.6"/><line x1="469.0" y1="127.0" x2="665.0" y2="127.0" stroke="currentColor" stroke-width="1.0" opacity="0.7" stroke-linecap="round"/><line x1="567.0" y1="29.0" x2="567.0" y2="225.0" stroke="currentColor" stroke-width="1.0" opacity="0.7" stroke-linecap="round"/><circle cx="567.0" cy="127.0" r="50.0" fill="none" stroke="currentColor" stroke-width="1.6" stroke-dasharray="5 4"/><line x1="586.0" y1="121.0" x2="598.0" y2="133.0" stroke="var(--hi)" stroke-width="2.4" stroke-linecap="round"/><line x1="586.0" y1="133.0" x2="598.0" y2="121.0" stroke="var(--hi)" stroke-width="2.4" stroke-linecap="round"/><line x1="494.3" y1="121.0" x2="506.3" y2="133.0" stroke="var(--hi)" stroke-width="2.4" stroke-linecap="round"/><line x1="494.3" y1="133.0" x2="506.3" y2="121.0" stroke="var(--hi)" stroke-width="2.4" stroke-linecap="round"/><text x="664.0" y="144.0" text-anchor="end" fill="var(--muted)" style="font-size:11px;">Re</text><text x="572.0" y="41.0" text-anchor="start" fill="var(--muted)" style="font-size:11px;">Im</text><text x="567.0" y="245.0" text-anchor="middle" fill="currentColor" style="font-size:14px;font-weight:600;">two-sided: a &lt; |z| &lt; b</text><text x="567.0" y="263.0" text-anchor="middle" fill="currentColor" style="font-size:13px;">poles ½, −4/3 → ½ &lt; |z| &lt; 4/3</text><text x="567.0" y="280.0" text-anchor="middle" fill="var(--muted)" style="font-size:12px;">stable ⇔ a &lt; 1 &lt; b</text></svg><figcaption><strong>The shape of the ROC tells you causality; the dashed unit circle tells you stability.</strong> Poles are red ×, the ROC is shaded. Left: slide 10's H(z) = 1/(1−⅕z⁻¹) + 1/(1−⅘z⁻¹) taken causal — outside the largest pole. Middle: h[n] = −(3/2)ⁿu[−n−1] (notes, Fig. 2b) — inside the smallest pole. Right: slide 10's H(z) = 1/(1−½z⁻¹) + 1/(1+(4/3)z⁻¹) — the annulus between the poles, h[n] = (½)ⁿu[n] − (−4/3)ⁿu[−n−1]. All three regions contain |z| = 1, so all three systems are BIBO stable.</figcaption></figure>

> [!key] Table 1 of the notes — ROC shape ⇔ causality ⇔ stability
> | ROC of $H(z)$ | causality type | right-sided | left-sided | BIBO stable iff |
> |---|---|---|---|---|
> | $\lvert z\rvert > \lvert p_{\max}\rvert$ | causal | ✓ | ✗ | $\lvert p_{\max}\rvert < 1$ |
> | $\lvert z\rvert < \lvert p_{\min}\rvert$ | anti-causal | ✗ | ✓ | $\lvert p_{\min}\rvert > 1$ |
> | $\lvert p_{\max}\rvert < \lvert z\rvert < \infty$ | non-causal | ✓ | ✗ | $\lvert p_{\max}\rvert < 1$ |
> | $0 < \lvert z\rvert < \lvert p_{\min}\rvert$ | non-causal | ✗ | ✓ | $\lvert p_{\min}\rvert > 1$ |
> | $a < \lvert z\rvert < b$ | non-causal (two-sided) | ✓ | ✓ | $a = \lvert p_{\max,h_r}\rvert < 1$ and $b = \lvert p_{\min,h_l}\rvert > 1$ |
>
> In words: **a causal system is stable iff all its poles are inside the unit circle; an anti-causal one iff all its poles are outside; a two-sided one iff the unit circle runs through its ring.**

## 3. Reading stability (and causality) off the poles

> [!recipe] "Is it stable?" / "Which $h[n]$ is the stable one?"
> 1. Factor numerator and denominator; **cancel common factors first** (a cancelled pole is not a pole). List the finite poles with their magnitudes.
> 2. *Causality given* → the ROC is forced (outside the largest pole if causal, inside the smallest if anti-causal) → check whether it contains $|z| = 1$.
> 3. *Stability given* → the ROC is forced the other way: it is the ring that contains $|z| = 1$. Every pole **inside** the unit circle gets a right-sided term $A\,p^n u[n]$; every pole **outside** gets a left-sided term $-A\,p^n u[-n-1]$. A pole **on** the unit circle means no stable version exists.
> 4. Read the causality type off the ROC you ended up with (Table 1).

> [!question] Slide 10 — stable $h[n]$ and its causality type
> For each system find the $h[n]$ that makes it BIBO stable, and say whether that system is causal, anti-causal or non-causal.
> (A) $H(z) = \dfrac{1}{1-\frac12 z^{-1}} + \dfrac{1}{1+\frac43 z^{-1}}$  (B) $H(z) = \dfrac{1}{1-\frac15 z^{-1}} + \dfrac{1}{1-\frac45 z^{-1}}$

> [!success]- Answers (checked: partial sums on the unit circle, $\sum|h|$)
> **(A)** Poles $\tfrac12$ and $-\tfrac43$. Both right-sided gives $|z| > \tfrac43$ ✗ (misses the unit circle); both left-sided gives $|z| < \tfrac12$ ✗. Right + left gives $\tfrac12 < |z| < \tfrac43$ ✓:
> $$
> h[n] = \left(\tfrac12\right)^n u[n] - \left(-\tfrac43\right)^n u[-n-1], \qquad \sum_n |h[n]| = 2 + 3 = 5 ,
> $$
> **non-causal** (two-sided).
> **(B)** Poles $\tfrac15$ and $\tfrac45$, both inside the unit circle: ROC $|z| > \tfrac45$ contains $|z| = 1$, so $h[n] = \left(\tfrac15\right)^n u[n] + \left(\tfrac45\right)^n u[n]$ ($\sum|h| = \tfrac{25}{4}$), **causal**.

> [!trap] Poles alone do not decide stability — the ROC does
> "$H(z) = \dfrac{1}{1-0.5z^{-1}} + \dfrac{1}{1-2z^{-1}}$ must not be BIBO stable" is **False** (FA2024 1(f)): pick ROC $\tfrac12 < |z| < 2$. Likewise "$\dfrac{1-z^{-1}}{1-2z^{-1}}$ cannot be stable" is False (SP2021 1(a): take $|z| < 2$). Conversely, once you are *told* the system is stable, the ROC is forced: stable $\dfrac{1}{1-3z^{-1}}$ **must be non-causal** (FA2023 1(f), True — it is anti-causal); stable $\dfrac{1}{1-\sqrt2 z^{-1}}$ **must be anti-causal** (SP2025 1(e), True); stable with poles $\tfrac14$ and $3$ **must be two-sided** (FA2025 1(c), True).

## 4. FIR systems are always stable

Slide 11 asks: can an LTI FIR system be unstable? No. Let $h[n] = \{\underset{\uparrow}{b_0}, b_1, \dots, b_{N-1}\}$, i.e. $y[n] = \sum_{k=0}^{N-1} b_k x[n-k]$.

- **Time domain:** $\sum_n |h[n]| = \sum_{k=0}^{N-1}|b_k| \le N \max_k|b_k| < \infty$.
- **z-domain:** $H(z) = \sum_{k=0}^{N-1} b_k z^{-k}$ has **no finite poles**, so its ROC is every $z$ except possibly $z = 0$ (or $z = \infty$ for a non-causal FIR filter) — it always contains $|z| = 1$.

(FA2019 1(e): "An LSI system with a finite-length impulse response can be BIBO stable or unstable" — **False**. FA2025 #4(c): the modified moving average is always stable because it is FIR.)

## 5. Unstable systems: which bounded inputs break them?

**A pole strictly outside the unit circle (causal case).** Take $h[n] = 3^n u[n]$, $H(z) = \dfrac{1}{1-3z^{-1}}$, $|z| > 3$. Already $x[n] = \delta[n]$ gives $y[n] = 3^n u[n]$; so do $u[n]$, $(\tfrac13)^n u[n]$ — *almost any* bounded input. The only way out is to **cancel the pole with a zero of $X(z)$**:
$$
\begin{aligned}
X(z) &= 1 - 3z^{-1} \;\leftrightarrow\; x[n] = \delta[n] - 3\delta[n-1] \\
\quad\Longrightarrow\quad Y(z) &= \frac{1-3z^{-1}}{1-3z^{-1}} = 1,\qquad y[n] = \delta[n] ,
\end{aligned}
$$
and any scaled or shifted copy of this $x[n]$ works too.

**A pole on the unit circle.** Now take $h[n] = (-1)^n u[n]$, $H(z) = \dfrac{1}{1+z^{-1}}$, $|z| > 1$: unstable ($\sum|h| = \infty$), yet $h$ is **bounded**, so $\delta[n]$ gives the bounded output $(-1)^n u[n]$, and $u[n]$ gives $\tfrac12(1 + (-1)^n)u[n]$ — also bounded. You need an input *at the same frequency*: $x[n] = (-1)^n u[n]$ gives $y[n] = (n+1)(-1)^n u[n]$. That is the marginally stable case of §6.

> [!trap] "Find a bounded input that gives an unbounded output"
> $\delta[n]$ is a valid answer **only if $h[n]$ itself is unbounded** (for a causal system: an uncancelled pole with $|p| > 1$, like $p = 3$ above). If the only offending poles are *on* the unit circle, $h$ is bounded and $\delta[n]$ earns nothing: HW4 #3(c) has $H(z) = \dfrac{z+1}{z-1}$, $h[n] = u[n] + u[n-1]$ (bounded); the answer is $x = u[n]$, giving $y[n] = (2n+1)u[n]$.

## 6. Marginal stability and pole matching

> [!key] Marginal stability (slide 15)
> An LTI system is **marginally stable** if its ROC is open on the unit circle — it *touches* $|z| = 1$ without containing it, e.g. $|z| > 1$ for a causal system whose largest poles lie on the unit circle. It is still **unstable**, but its impulse response stays bounded (undamped terms $e^{j\omega n}u[n]$ — cosines/sines for conjugate pairs — plus decaying ones), and only inputs that *resonate* with it produce unbounded outputs.

**Time-domain picture (slides 16–17).** Let $h[n] = a^n u[n]$ with $|a| = 1$ and try $x[n] = b^n u[n]$:

- $|b| > 1$: the input is itself unbounded — not a legal test input for BIBO.
- $|b| < 1$: $Y(z) = \dfrac{1}{(1-bz^{-1})(1-az^{-1})} = \dfrac{A_1}{1-bz^{-1}} + \dfrac{A_2}{1-az^{-1}}$, so $y[n] = A_1 b^n u[n] + A_2 a^n u[n]$: one term decays, the other has constant magnitude. **Bounded.**
- $|b| = 1$: write $a = e^{j\theta}$, $b = e^{j\phi}$. Then
$$
\begin{aligned}
y[n] &= \sum_{k=0}^{n} e^{j\theta k}e^{j\phi(n-k)} \\
&= e^{j\phi n}\sum_{k=0}^{n} e^{j(\theta-\phi)k} \\
&= \begin{cases} e^{j\phi n}\,(n+1)\,u[n], & \theta = \phi \quad\text{(unbounded)}\\[4pt]
e^{j\phi n}\,\dfrac{1-e^{j(\theta-\phi)(n+1)}}{1-e^{j(\theta-\phi)}}\,u[n], & \theta \ne \phi \quad\text{(bounded by } \tfrac{2}{|1-e^{j(\theta-\phi)}|}\text{)} \end{cases}
\end{aligned}
$$

With $a = b = 1$ this is the notes' example: $h = u[n]$, $x = u[n]$ gives $y = (n+1)u[n]$, while a decaying input $c^n u[n]$ ($|c| < 1$) gives the bounded $y[n] = \sum_{k=0}^n c^k$.

> [!derivation]- Lecture exercise: a double pole on the unit circle is an unbounded output
> From the pair $n\,a^n u[n] \leftrightarrow \dfrac{a z^{-1}}{(1-az^{-1})^2}$ (or by differentiating the geometric series),
> $$
> \frac{1}{(1-az^{-1})^2} = \sum_{n=0}^{\infty}(n+1)\,a^n z^{-n} \;\leftrightarrow\; (n+1)\,a^n u[n], \qquad |z| > |a| .
> $$
> If $|a| = 1$ then $|y[n]| = n+1 \to \infty$. If $|a| < 1$ the same double pole gives $(n+1)a^n \to 0$ — harmless. So "input pole = system pole" is dangerous **only on the unit circle**. (If $H$ itself has a double pole on $|z| = 1$, e.g. $\frac{1}{(1-z^{-1})^2}$, then $h[n] = (n+1)u[n]$ is unbounded and $\delta[n]$ already breaks it.)

> [!key] Pole matching
> A marginally stable system gives an unbounded output **iff the input's z-transform has a pole exactly on one of the system's (uncancelled) poles on the unit circle** — then $Y = HX$ has a double pole on $|z| = 1$ and $y[n]$ contains $n\,e^{j\omega_0 n}$. Matching a pole *inside* the unit circle, or putting an input pole on the unit circle where $H$ has no pole, keeps the output bounded.

> [!recipe] Which bounded inputs give unbounded outputs? (FA2025 #8, SP2025 #6, SP2021 #5, HW4 #3)
> 1. Factor $H(z)$, cancel common factors, and list its poles **with their angles**. If $H$ is causal and has an uncancelled pole with $|p| > 1$, then $h$ itself is unbounded: $\delta[n]$ and almost everything else blow up (§5).
> 2. Write each input's poles: $a^n u[n] \to a$; $u[n] \to 1$; $(-1)^n u[n] \to -1$; $j^n u[n] \to j = e^{j\pi/2}$; $\cos(\omega_0 n)u[n]$ and $\sin(\omega_0 n)u[n] \to e^{\pm j\omega_0}$ (Euler: both exponentials are present). Finite-length inputs have no finite poles, so they never match (they can only add zeros).
> 3. **Unbounded iff an input pole coincides with a unit-circle pole of $H$** (and no zero cancels it). One matching exponential is enough — a cosine matches if *either* $e^{j\omega_0}$ or $e^{-j\omega_0}$ is a pole.
> 4. Compare angles exactly: $e^{j2/3}$ (angle $\tfrac23$ rad $\approx 38^\circ$) is **not** $e^{j2\pi/3}$ ($120^\circ$).

> [!question] Slide 18 — which inputs lead to an unbounded output?
> Causal $H(z) = \dfrac{1}{(1-jz^{-1})(1+z^{-1})(1-\frac23 z^{-1})}$ (ROC $|z| > 1$). Inputs: (1) $(-1)^n u[n]$ (2) $u[n]$ (3) $e^{j\frac{\pi}{2}n}u[n]$ (4) $e^{-j\frac{\pi}{2}n}u[n]$ (5) $(\tfrac23)^n u[n]$ (6) $\sin(-\tfrac{\pi}{2}n)u[n]$ (7) $\cos(\tfrac{\pi}{2}n)u[n]$ (8) $\sin(\tfrac{2\pi}{3}n)u[n]$.

> [!success]- Answer (checked with `lfilter` over 40 000 samples: linear growth vs. flat)
> System poles: $j$ and $-1$ on the unit circle, $\tfrac23$ inside — marginally stable.
> **Unbounded: (1), (3), (6), (7).** (1) has its pole at $-1$; (3) at $j$; (6) $\sin(-\tfrac{\pi}{2}n) = -\tfrac{1}{2j}\bigl(e^{j\frac{\pi}{2}n} - e^{-j\frac{\pi}{2}n}\bigr)$ and (7) both contain $e^{j\frac{\pi}{2}n}$, pole at $j$.
> **Bounded: (2), (4), (5), (8).** (2) pole at $1$ and (8) poles at $e^{\pm j2\pi/3}$ are not system poles; (4) has its pole at $-j$, and $-j$ is *not* a pole of this $H$ (its coefficients are complex, so its poles need not come in conjugate pairs); (5) makes a double pole at $\tfrac23$, giving an $n(\tfrac23)^n u[n]$ term, which decays.

<figure class="ece-fig"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 680 372" width="680" height="372" role="img" style="font-family:'Source Sans 3','Source Sans Pro',system-ui,sans-serif;font-size:14px;max-width:100%;height:auto"><text x="340.0" y="22.0" text-anchor="middle" fill="currentColor" style="font-size:14px;font-weight:600;">Causal H(z) = 1 / [(1 − jz⁻¹)(1 + z⁻¹)(1 − ⅔z⁻¹)],  ROC |z| &gt; 1  (marginally stable)</text><path d="M287.00,200.00 A112.00,112.00 0 1,0 63.00,200.00 A112.00,112.00 0 1,0 287.00,200.00 Z" fill="none" stroke="currentColor" stroke-width="1.8" stroke-dasharray="6 4"/><line x1="27.0" y1="200.0" x2="323.0" y2="200.0" stroke="currentColor" stroke-width="1.0" opacity="0.7" stroke-linecap="round"/><line x1="175.0" y1="52.0" x2="175.0" y2="348.0" stroke="currentColor" stroke-width="1.0" opacity="0.7" stroke-linecap="round"/><text x="321.0" y="215.0" text-anchor="end" fill="var(--muted)" style="font-size:11px;">Re</text><text x="181.0" y="64.0" text-anchor="start" fill="var(--muted)" style="font-size:11px;">Im</text><text x="263.9" y="296.9" text-anchor="start" fill="currentColor" style="font-size:12px;">|z| = 1</text><circle cx="63.0" cy="200.0" r="7.0" fill="none" stroke="var(--accent)" stroke-width="2.0"/><text x="50.0" y="188.0" text-anchor="end" fill="var(--accent)" style="font-size:13px;font-weight:600;">1</text><circle cx="287.0" cy="200.0" r="7.0" fill="none" stroke="var(--accent)" stroke-width="2.0"/><text x="300.0" y="188.0" text-anchor="start" fill="var(--accent)" style="font-size:13px;font-weight:600;">2</text><circle cx="175.0" cy="88.0" r="7.0" fill="none" stroke="var(--accent)" stroke-width="2.0"/><text x="190.0" y="76.0" text-anchor="start" fill="var(--accent)" style="font-size:13px;font-weight:600;">3, 6, 7</text><circle cx="175.0" cy="312.0" r="7.0" fill="none" stroke="var(--accent)" stroke-width="2.0"/><text x="190.0" y="332.0" text-anchor="start" fill="var(--accent)" style="font-size:13px;font-weight:600;">4, 6, 7</text><circle cx="249.7" cy="200.0" r="7.0" fill="none" stroke="var(--accent)" stroke-width="2.0"/><text x="249.7" y="226.0" text-anchor="middle" fill="var(--accent)" style="font-size:13px;font-weight:600;">5</text><circle cx="119.0" cy="103.0" r="7.0" fill="none" stroke="var(--accent)" stroke-width="2.0"/><text x="106.0" y="93.0" text-anchor="end" fill="var(--accent)" style="font-size:13px;font-weight:600;">8</text><circle cx="119.0" cy="297.0" r="7.0" fill="none" stroke="var(--accent)" stroke-width="2.0"/><text x="106.0" y="317.0" text-anchor="end" fill="var(--accent)" style="font-size:13px;font-weight:600;">8</text><line x1="168.0" y1="81.0" x2="182.0" y2="95.0" stroke="var(--hi)" stroke-width="2.4" stroke-linecap="round"/><line x1="168.0" y1="95.0" x2="182.0" y2="81.0" stroke="var(--hi)" stroke-width="2.4" stroke-linecap="round"/><line x1="56.0" y1="193.0" x2="70.0" y2="207.0" stroke="var(--hi)" stroke-width="2.4" stroke-linecap="round"/><line x1="56.0" y1="207.0" x2="70.0" y2="193.0" stroke="var(--hi)" stroke-width="2.4" stroke-linecap="round"/><line x1="242.7" y1="193.0" x2="256.7" y2="207.0" stroke="var(--hi)" stroke-width="2.4" stroke-linecap="round"/><line x1="242.7" y1="207.0" x2="256.7" y2="193.0" stroke="var(--hi)" stroke-width="2.4" stroke-linecap="round"/><circle cx="175.0" cy="88.0" r="15.0" fill="none" stroke="var(--hi)" stroke-width="2.2" stroke-dasharray="3 3"/><circle cx="63.0" cy="200.0" r="15.0" fill="none" stroke="var(--hi)" stroke-width="2.2" stroke-dasharray="3 3"/><line x1="372.0" y1="52.0" x2="384.0" y2="64.0" stroke="var(--hi)" stroke-width="2.4" stroke-linecap="round"/><line x1="372.0" y1="64.0" x2="384.0" y2="52.0" stroke="var(--hi)" stroke-width="2.4" stroke-linecap="round"/><text x="392.0" y="63.0" text-anchor="start" fill="currentColor" style="font-size:13px;">system pole</text><circle cx="522.0" cy="58.0" r="7.0" fill="none" stroke="var(--accent)" stroke-width="2.0"/><text x="536.0" y="63.0" text-anchor="start" fill="currentColor" style="font-size:13px;">input pole (input #)</text><text x="372.0" y="98.0" text-anchor="start" fill="var(--hi)" style="font-size:12.5px;font-weight:700;">unbounded</text><text x="454.0" y="98.0" text-anchor="start" fill="currentColor" style="font-size:13px;">#1  (−1)<tspan baseline-shift="super" font-size="10">n</tspan>u[n]</text><text x="454.0" y="114.0" text-anchor="start" fill="var(--muted)" style="font-size:11.5px;">pole −1: a system pole on |z| = 1</text><text x="372.0" y="136.0" text-anchor="start" fill="var(--hi)" style="font-size:12.5px;font-weight:700;">unbounded</text><text x="454.0" y="136.0" text-anchor="start" fill="currentColor" style="font-size:13px;">#3  e<tspan baseline-shift="super" font-size="10">jπn/2</tspan>u[n]</text><text x="454.0" y="152.0" text-anchor="start" fill="var(--muted)" style="font-size:11.5px;">pole j: a system pole on |z| = 1</text><text x="372.0" y="174.0" text-anchor="start" fill="var(--hi)" style="font-size:12.5px;font-weight:700;">unbounded</text><text x="454.0" y="174.0" text-anchor="start" fill="currentColor" style="font-size:13px;">#6, 7  sin(−πn/2), cos(πn/2)</text><text x="454.0" y="190.0" text-anchor="start" fill="var(--muted)" style="font-size:11.5px;">poles ±j: the j half matches</text><text x="372.0" y="212.0" text-anchor="start" fill="var(--muted)" style="font-size:12.5px;font-weight:700;">bounded</text><text x="454.0" y="212.0" text-anchor="start" fill="currentColor" style="font-size:13px;">#2  u[n]</text><text x="454.0" y="228.0" text-anchor="start" fill="var(--muted)" style="font-size:11.5px;">pole 1: no system pole there</text><text x="372.0" y="250.0" text-anchor="start" fill="var(--muted)" style="font-size:12.5px;font-weight:700;">bounded</text><text x="454.0" y="250.0" text-anchor="start" fill="currentColor" style="font-size:13px;">#4  e<tspan baseline-shift="super" font-size="10">−jπn/2</tspan>u[n]</text><text x="454.0" y="266.0" text-anchor="start" fill="var(--muted)" style="font-size:11.5px;">pole −j: not a system pole</text><text x="372.0" y="288.0" text-anchor="start" fill="var(--muted)" style="font-size:12.5px;font-weight:700;">bounded</text><text x="454.0" y="288.0" text-anchor="start" fill="currentColor" style="font-size:13px;">#8  sin(2πn/3)u[n]</text><text x="454.0" y="304.0" text-anchor="start" fill="var(--muted)" style="font-size:11.5px;">poles e<tspan baseline-shift="super" font-size="10">±j2π/3</tspan>: no match</text><text x="372.0" y="326.0" text-anchor="start" fill="var(--muted)" style="font-size:12.5px;font-weight:700;">bounded</text><text x="454.0" y="326.0" text-anchor="start" fill="currentColor" style="font-size:13px;">#5  (⅔)<tspan baseline-shift="super" font-size="10">n</tspan>u[n]</text><text x="454.0" y="342.0" text-anchor="start" fill="var(--muted)" style="font-size:11.5px;">matches ⅔, but inside: n(⅔)<tspan baseline-shift="super" font-size="10">n</tspan> → 0</text></svg><figcaption><strong>Pole matching (slide 18).</strong> The system has poles j and −1 on the unit circle and ⅔ inside, so it is marginally stable. Each bounded input (all are switched on at n = 0, i.e. multiplied by u[n]) brings its own poles (circles, labelled by input number). The output is unbounded exactly when an input pole lands on a system pole <em>that sits on the unit circle</em> (dashed red rings): the product Y = HX then has a double pole on |z| = 1, i.e. a term that grows like n. A cosine or sine has two poles e<sup>±jω₀</sup>; one match is enough.</figcaption></figure>

> [!trap] FA2025 #8(b): $e^{j2/3}$ is not $e^{j2\pi/3}$
> Causal $H(z) = \dfrac{1}{(1-\frac34 z^{-1})(1-jz^{-1})(1-e^{j\frac23}z^{-1})}$, $|z| > 1$. The third pole has angle $\tfrac23$ **radian**, not $\tfrac{2\pi}{3}$. So $\cos(\tfrac{2\pi}{3}n)u[n]$ (poles $e^{\pm j2\pi/3}$) does **not** match anything → bounded output (key: False), while $j^n u[n]$ and $\sin(\tfrac{\pi}{2}n)u[n]$ match the pole at $j$ → unbounded (True). $\delta[n] - \tfrac34\delta[n-1]$ only cancels the harmless pole $\tfrac34$ (False); $(\tfrac23)^n u[n]$ puts a pole inside the circle (False).

The same check in Python — note the tolerance: the unit-circle poles come back from `np.roots` as $0.9999999999999997$ and $0.9999999999999986$, so a naive `abs(p) < 1` would wrongly report "stable".

```python
import numpy as np
from scipy.signal import lfilter

# FA2025 #8(b): causal H(z) = 1 / ((1 - 3/4 z^-1)(1 - j z^-1)(1 - e^{j2/3} z^-1))
a = np.poly([0.75, 1j, np.exp(2j/3)])   # denominator coefficients, powers of z^-1
p = np.roots(a)                          # the poles (same as tf2zpk([1, 0, 0, 0], a))
print("|p|      :", np.round(np.abs(p), 3))
print("angle/pi :", np.round(np.angle(p) / np.pi, 3))
print("stable?  :", np.all(np.abs(p) < 1 - 1e-9))  # causal: every |p| < 1 (with a tolerance!)

n = np.arange(4000)
for name, x in [("j^n u[n]", 1j**n), ("cos(2pi n/3) u[n]", np.cos(2*np.pi*n/3))]:
    y = lfilter([1], a, x.astype(complex))
    print(f"{name:17s} max|y|: n<2000 {abs(y[:2000]).max():7.1f}   n>=2000 {abs(y[2000:]).max():7.1f}")
```

```text
|p|      : [1.   1.   0.75]
angle/pi : [0.5   0.212 0.   ]
stable?  : False
j^n u[n]          max|y|: n<2000  1833.5   n>=2000  3665.6
cos(2pi n/3) u[n] max|y|: n<2000     2.6   n>=2000     2.6
```

The pole angles are $0.5\pi$ (the pole $j$) and $0.212\pi = \tfrac23$ rad; the $j^n$ input's output doubles when the window doubles (linear growth), the $\cos(\tfrac{2\pi}{3}n)$ output stays flat.

## 7. How the exam uses this lecture

> [!exam] Unbounded outputs and pole matching — 7/7 exams
> - [[exams/midterm-1/past-exams/fall-2025|FA2025 #8]] (10 pts): (a) causal $H = \dfrac{1-\frac34 z^{-1}}{1+3z^{-1}}$, pole $-3$ **outside** — only inputs whose zero sits at $-3$ give bounded outputs: $\tfrac13(\tfrac12)^n u[n] + (\tfrac12)^{n-1}u[n-1]$ (its $X = \tfrac13\,\frac{1+3z^{-1}}{1-\frac12 z^{-1}}$) and $\delta[n] + 3\delta[n-1]$; $(\tfrac34)^n u[n]$ cancels the *zero*, not the pole (still unbounded). (b) the $e^{j2/3}$ trap above.
> - [[exams/midterm-1/past-exams/spring-2025|SP2025 #6]]: $H = \dfrac{z}{z-e^{j\pi/4}}$, $|z|>1$ — unbounded for $e^{j\pi n/4}u[n]$, $\cos(\tfrac{\pi}{4}n)u[n]$ and $4^n u[n]$; bounded for $u[n]$, $e^{-j\pi n/4}u[n]$, $e^{-j3\pi n/4}u[n]$.
> - [[exams/midterm-1/past-exams/spring-2021|SP2021 #5]]: $H = \dfrac{3z^{-1}}{1+z^{-2}}$, $|z|>1$, $h[n] = 3\sin(\tfrac{\pi}{2}n)u[n]$; unbounded for $j^n u[n]$, $\cos(\tfrac{\pi}{2}n)u[n]$, $\sin(\tfrac{\pi}{2}n)u[n]$.
> - [[exams/midterm-1/past-exams/fall-2023|FA2023 #7(c)]]: poles $\tfrac14, -1$, causal → not stable; $x = \cos(\pi n)u[n] = (-1)^n u[n]$ breaks it.
> - [[exams/midterm-1/past-exams/spring-2023|SP2023 #7]]: $H = \dfrac{z-3}{z-4}$, $|z|>4$: bounded→unbounded ($\delta[n]$), unbounded→bounded ($X = \frac{z-4}{z-3}$, $y = \delta[n]$), bounded→bounded ($x = \delta[n] - 4\delta[n-1]$, $y = \delta[n] - 3\delta[n-1]$).
> - [[exams/midterm-1/past-exams/fall-2024|FA2024 #7(c)–(d)]]: the input's zero at $2$ cancels the system's unstable pole at $2$, so $y[n] = 2n(\tfrac12)^n u[n]$ is bounded. [[exams/midterm-1/past-exams/fall-2019|FA2019 #10(d)]]: the zero of $H$ at $2$ cancels the pole of the cascaded unstable $2^n u[n]$, so the cascade is stable ("overall unstable" is False).
>
> Recipes and more worked cases: [[problems/unbounded-outputs-and-pole-matching|unbounded outputs & pole matching]].

> [!exam] Parameters for stability — 3/7 exams
> A parameter in the numerator can only help by **placing a zero on top of the bad pole**. [[exams/midterm-1/past-exams/spring-2025|SP2025 #7]]: causal, poles $-2$ and $\tfrac12$, numerator $1 - \alpha^2 z^{-2} = (1-\alpha z^{-1})(1+\alpha z^{-1})$ → stable iff $\alpha = \pm 2$ (only $\alpha^2$ enters, so both signs). [[exams/midterm-1/past-exams/fall-2024|FA2024 #8]]: (a) non-causal first-order $\dfrac{1+3z^{-1}}{1+\alpha z^{-1}}$, ROC $|z| < |\alpha|$ → stable iff $|\alpha| > 1$; (b) causal, poles $2, \tfrac12$ → $\beta = -2$. [[exams/midterm-1/past-exams/fall-2023|FA2023 #8]]: (a) causal, poles $\tfrac43, -\tfrac23$ → $\alpha = -4$; (b) two-sided → ROC $\tfrac23 < |z| < \tfrac43$ already contains $|z| = 1$: stable for every $\alpha$. See [[problems/parameters-for-stability|parameters for stability]].

> [!exam] Two-sided systems as recursions — 2/7 exams
> A stable two-sided $H = H_1 + H_2$ is run as two recursions: the right-sided part forward, the left-sided part **backward in time**. [[exams/midterm-1/past-exams/fall-2025|FA2025 #7(b)]]: $H_2 = \dfrac{-5/4}{1+\frac23 z^{-1}}$ (causal) → $y_2[n] = -\tfrac23 y_2[n-1] - \tfrac54 x[n]$; $H_1 = \dfrac{9/4}{1+2z^{-1}}$ (ROC $|z|<2$, anti-causal) → $y_1[n-1] = -\tfrac12 y_1[n] + \tfrac98 x[n]$. See [[problems/two-sided-systems-as-recursions|two-sided systems as recursions]].

> [!success]- True/False from this lecture (answers)
> - A bounded $h[n]$ means stable — **F** ($h = u[n]$; FA2025 1(a), FA2024 1(b), FA2019 1(c)).
> - A right-sided $h[n]$ must be causal — **F** ($u[n+1]$; SP2023 1(c)).
> - A stable system maps every unbounded input to an unbounded output — **F** ($h = \delta[n] - 2\delta[n-1]$, $x = 2^n u[n]$ gives $y = \delta[n]$; FA2025 1(e), SP2023 1(b)).
> - A two-sided $h[n]$ is never stable — **F** ($(\tfrac12)^{|n|}$; SP2025 1(f)).
> - An LTI system with a left-sided $h$ can never be causal — **T** in the key's sense (a left-sided $h$ extending to $-\infty$; FA2025 1(d)).
> - Causal $H = \dfrac{z^{-1}}{1-z^{-1}}$ with input $u[n]$ gives an unbounded output — **T** ($y = n\,u[n]$; SP2021 1(d)).
> - An unstable system's response to any nonzero input is unbounded — **F** ($u[n] * (\delta[n]-\delta[n-1]) = \delta[n]$; FA2019 1(j)).
>
> All of them, with reasons: [[exams/midterm-1/true-false-bank|T/F bank]].

## Related

[[concepts/bibo-stability|BIBO stability]] · [[concepts/marginal-stability|marginal stability]] · [[concepts/region-of-convergence|region of convergence]] · [[concepts/causality|causality]] · [[concepts/sided-sequences|sided sequences]] · [[concepts/poles-and-zeros|poles and zeros]] · [[concepts/pole-zero-cancellation|pole-zero cancellation]] · [[concepts/fir-and-iir|FIR and IIR]] · [[concepts/transfer-function|transfer function]] · [[problems/all-possible-rocs|all possible ROCs]] · [[demos/pole-zero-and-roc-explorer|pole-zero & ROC explorer]] · previous: [[2-z-transform/10-improper-transfer-functions-and-system-algebra|Lecture 10]] · unit: [[2-z-transform/index|Unit 2]]

### Sources for this page

Snyder, *ECE 310 Lecture 11* notes (§1 z-domain BIBO test, §1.1 sidedness, Figs. 1–2, Table 1, §1.2 unstable inputs, §1.2.1 marginal stability and the lecture exercise) and slides 1–18 with the annotated in-class answers (slides 6–7 sidedness examples, 10 IIR stability, 11 FIR stability, 12–14 unstable inputs, 15 marginal stability, 16–17 pole matching in time, 18 pole-matching example). HW4 #3. Past exams FA2025 #1, #7, #8; SP2025 #1, #6, #7; FA2024 #1, #7, #8; FA2023 #1, #7, #8; SP2023 #1, #7; SP2021 #1, #5; FA2019 #1, #10. Every number above is checked in `verify/lectures/l11_verify.py`.
