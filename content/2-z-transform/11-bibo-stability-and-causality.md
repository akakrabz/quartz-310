---
title: "Lecture 11 — BIBO stability and causality in the z-domain"
description: "Third BIBO test (ROC contains the unit circle); ROC shape ⇔ causal, anti-causal, two-sided; stability from the poles; FIR always stable; bounded inputs that break unstable and marginally stable systems (pole matching)."
tags: [lecture, midterm-1, stability, roc, z-transform]
lecture: 11
---

*Lecture 11 · Fri Sep 18, 2026 · notes + slides "BIBO stability and causality" · prev: [[2-z-transform/10-improper-transfer-functions-and-system-algebra|Lecture 10]] · next: [[3-fourier-analysis/12-convolution-as-template-matching|Lecture 12]]*

> [!abstract] In one breath
> - LTI BIBO stable $\iff \sum_n |h[n]| < \infty \iff$ ROC of $H(z)$ contains $|z| = 1$.
> - ROC outside a circle (to $\infty$) = causal, inside = left-sided, ring = two-sided: causal stable iff all poles inside the unit circle.
> - Marginally stable (poles on $|z|=1$): only inputs with a matching pole give unbounded outputs.

## 1. BIBO stability in the z-domain

Three tests:

1. **Definition** (any system, [[1-signals-and-systems/03-system-properties|Lecture 3]]): $|x[n]| < \beta$ for all $n$ ⇒ $|y[n]| < \alpha$ for all $n$ ($\alpha, \beta < \infty$).
2. **Impulse response** (LTI, [[1-signals-and-systems/04-impulse-response-and-convolution|Lecture 4]]): $\sum_{n=-\infty}^{\infty} |h[n]| < \infty$.
3. **Transfer function** (LTI): the ROC of $H(z)$ contains $|z| = 1$.

> [!key] BIBO stability in the z-domain
> $$
> \begin{aligned}
> &\text{LTI system BIBO stable} \\
> &\iff \sum_{n=-\infty}^{\infty}|h[n]| < \infty \\
> &\iff \text{ROC of } H(z) \text{ contains the unit circle } |z| = 1 .
> \end{aligned}
> $$
> "Contains" is strict: $|z| > 1$ touches the unit circle but does not contain it (marginally stable, §1.2.1).

> [!derivation]- Why the unit circle (notes, eqs. 3–7)
> The ROC is where the sum converges absolutely. On $|z| = 1$, $z = e^{j\theta}$ and $|e^{-j\theta n}| = 1$:
> $$
> \sum_{n=-\infty}^{\infty}\bigl|h[n]z^{-n}\bigr|\Big|_{z=e^{j\theta}} = \sum_{n=-\infty}^{\infty}|h[n]|\,\bigl|e^{-j\theta n}\bigr| = \sum_{n=-\infty}^{\infty}|h[n]| .
> $$
> (The notes write $|h[n]e^{-j\theta n}|$ as $\sqrt{(h[n]e^{-j\theta n})(h^*[n]e^{j\theta n})}$.) The converse also holds.

### 1.1 Identifying causal and non-causal systems

- **Right-sided**: $x[n] = 0$ for $n < n_0$; **left-sided**: $x[n] = 0$ for $n > n_0$ ($n_0$ any sign); **two-sided**: both directions ([[concepts/sided-sequences|sided sequences]]).
- **Causal**: present and past only, $h[n] = 0$ for $n < 0$. **Anti-causal**: future only, $h[n] = 0$ for $n \ge 0$. **Non-causal**: some future and some present/past. (Notes print "Non-causal – a system is *causal* if…"; read "non-causal".)
- A sample at $n < 0$ gives $z^{|n|}$ (blows up at $|z| = \infty$); at $n > 0$, $z^{-n}$ (blows up at $z = 0$). Slides 6–7 corners:

| | $n_0 < 0$ | $n_0 \ge 0$ |
|---|---|---|
| **right-sided** | non-causal, $\lvert p_{\max}\rvert < \lvert z\rvert < \infty$; e.g. $u[n+1] = \delta[n+1] + u[n] \leftrightarrow z + \dfrac{1}{1-z^{-1}}$, $1 < \lvert z\rvert < \infty$ | **causal**, $\lvert z\rvert > \lvert p_{\max}\rvert$; e.g. $(\tfrac12)^{n-3}u[n-3] \leftrightarrow \dfrac{z^{-3}}{1-\frac12 z^{-1}}$, $\lvert z\rvert > \tfrac12$ |
| **left-sided** | **anti-causal**, $\lvert z\rvert < \lvert p_{\min}\rvert$; e.g. $-3^{n+2}u[-n-3] \leftrightarrow \dfrac{z^{2}}{1-3z^{-1}}$, $\lvert z\rvert < 3$ | non-causal, $0 < \lvert z\rvert < \lvert p_{\min}\rvert$; e.g. $-3^{n-3}u[-n+2] \leftrightarrow \dfrac{z^{-3}}{1-3z^{-1}}$, $0 < \lvert z\rvert < 3$ |

- $p_{\max}$, $p_{\min}$: largest/smallest-magnitude **finite** poles; the ROC stops at the first pole.
- Exception $n_0 = 0$ left-sided ($2^n u[-n] \leftrightarrow \frac{1}{1 - z/2}$, $|z| < 2$): includes $z = 0$, still non-causal. Exam rule: **ROC includes $|z| = \infty$ $\iff$ causal.**
- Left-sided systems run backward in time (slide 7: $y[n] = 3y[n+1] + x[n+1]$, $H(z) = \dfrac{z}{1-3z}$, $|z| < \tfrac13$).
- Two-sided: $h[n] = h_l[n] + h_r[n]$, $h_r = h[n]u[n]$, $h_l = h[n]u[-n-1]$; ROC at least $\{|z| > |p_{\max,h_r}|\} \cap \{|z| < |p_{\min,h_l}|\}$, exactly that unless a zero cancels one of those poles.

<figure class="ece-fig"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 680 306" width="680" height="306" role="img" style="font-family:'Source Sans 3','Source Sans Pro',system-ui,sans-serif;font-size:14px;max-width:100%;height:auto"><line x1="170.0" y1="14.0" x2="200.0" y2="14.0" stroke="currentColor" stroke-width="1.6" stroke-dasharray="5 4" stroke-linecap="round"/><text x="206.0" y="18.0" text-anchor="start" fill="currentColor" style="font-size:12.5px;">unit circle |z| = 1</text><line x1="347.0" y1="9.0" x2="357.0" y2="19.0" stroke="var(--hi)" stroke-width="2.4" stroke-linecap="round"/><line x1="347.0" y1="19.0" x2="357.0" y2="9.0" stroke="var(--hi)" stroke-width="2.4" stroke-linecap="round"/><text x="362.0" y="18.0" text-anchor="start" fill="currentColor" style="font-size:12.5px;">pole</text><rect x="410" y="7" width="16" height="14" fill="var(--accent)" fill-opacity="0.22" stroke="var(--accent)" stroke-width="1.2"/><text x="432.0" y="18.0" text-anchor="start" fill="currentColor" style="font-size:12.5px;">ROC</text><clipPath id="l11ca"><rect x="15.0" y="29.0" width="196.0" height="196.0"/></clipPath><path d="M15.0,29.0 h196.0 v196.0 h-196.0 Z M153.00,127.00 A40.00,40.00 0 1,0 73.00,127.00 A40.00,40.00 0 1,0 153.00,127.00 Z" fill="var(--accent)" fill-opacity="0.22" fill-rule="evenodd" stroke="none" clip-path="url(#l11ca)"/><circle cx="113.0" cy="127.0" r="40.0" fill="none" stroke="var(--accent)" stroke-width="1.6"/><line x1="15.0" y1="127.0" x2="211.0" y2="127.0" stroke="currentColor" stroke-width="1.0" opacity="0.7" stroke-linecap="round"/><line x1="113.0" y1="29.0" x2="113.0" y2="225.0" stroke="currentColor" stroke-width="1.0" opacity="0.7" stroke-linecap="round"/><circle cx="113.0" cy="127.0" r="50.0" fill="none" stroke="currentColor" stroke-width="1.6" stroke-dasharray="5 4"/><line x1="117.0" y1="121.0" x2="129.0" y2="133.0" stroke="var(--hi)" stroke-width="2.4" stroke-linecap="round"/><line x1="117.0" y1="133.0" x2="129.0" y2="121.0" stroke="var(--hi)" stroke-width="2.4" stroke-linecap="round"/><line x1="147.0" y1="121.0" x2="159.0" y2="133.0" stroke="var(--hi)" stroke-width="2.4" stroke-linecap="round"/><line x1="147.0" y1="133.0" x2="159.0" y2="121.0" stroke="var(--hi)" stroke-width="2.4" stroke-linecap="round"/><text x="210.0" y="144.0" text-anchor="end" fill="var(--muted)" style="font-size:11px;">Re</text><text x="118.0" y="41.0" text-anchor="start" fill="var(--muted)" style="font-size:11px;">Im</text><text x="113.0" y="245.0" text-anchor="middle" fill="currentColor" style="font-size:14px;font-weight:600;">causal: |z| &gt; |p_max|</text><text x="113.0" y="263.0" text-anchor="middle" fill="currentColor" style="font-size:13px;">poles ⅕, ⅘ → |z| &gt; ⅘</text><text x="113.0" y="280.0" text-anchor="middle" fill="var(--muted)" style="font-size:12px;">stable ⇔ |p_max| &lt; 1</text><clipPath id="l11cb"><rect x="242.0" y="29.0" width="196.0" height="196.0"/></clipPath><path d="M415.00,127.00 A75.00,75.00 0 1,0 265.00,127.00 A75.00,75.00 0 1,0 415.00,127.00 Z" fill="var(--accent)" fill-opacity="0.22" fill-rule="evenodd" stroke="none" clip-path="url(#l11cb)"/><circle cx="340.0" cy="127.0" r="75.0" fill="none" stroke="var(--accent)" stroke-width="1.6"/><line x1="242.0" y1="127.0" x2="438.0" y2="127.0" stroke="currentColor" stroke-width="1.0" opacity="0.7" stroke-linecap="round"/><line x1="340.0" y1="29.0" x2="340.0" y2="225.0" stroke="currentColor" stroke-width="1.0" opacity="0.7" stroke-linecap="round"/><circle cx="340.0" cy="127.0" r="50.0" fill="none" stroke="currentColor" stroke-width="1.6" stroke-dasharray="5 4"/><line x1="409.0" y1="121.0" x2="421.0" y2="133.0" stroke="var(--hi)" stroke-width="2.4" stroke-linecap="round"/><line x1="409.0" y1="133.0" x2="421.0" y2="121.0" stroke="var(--hi)" stroke-width="2.4" stroke-linecap="round"/><text x="437.0" y="144.0" text-anchor="end" fill="var(--muted)" style="font-size:11px;">Re</text><text x="345.0" y="41.0" text-anchor="start" fill="var(--muted)" style="font-size:11px;">Im</text><text x="340.0" y="245.0" text-anchor="middle" fill="currentColor" style="font-size:14px;font-weight:600;">anti-causal: |z| &lt; |p_min|</text><text x="340.0" y="263.0" text-anchor="middle" fill="currentColor" style="font-size:13px;">pole 3/2 → |z| &lt; 3/2</text><text x="340.0" y="280.0" text-anchor="middle" fill="var(--muted)" style="font-size:12px;">stable ⇔ |p_min| &gt; 1</text><clipPath id="l11cc"><rect x="469.0" y="29.0" width="196.0" height="196.0"/></clipPath><path d="M633.67,127.00 A66.67,66.67 0 1,0 500.33,127.00 A66.67,66.67 0 1,0 633.67,127.00 Z M592.00,127.00 A25.00,25.00 0 1,0 542.00,127.00 A25.00,25.00 0 1,0 592.00,127.00 Z" fill="var(--accent)" fill-opacity="0.22" fill-rule="evenodd" stroke="none" clip-path="url(#l11cc)"/><circle cx="567.0" cy="127.0" r="25.0" fill="none" stroke="var(--accent)" stroke-width="1.6"/><circle cx="567.0" cy="127.0" r="66.7" fill="none" stroke="var(--accent)" stroke-width="1.6"/><line x1="469.0" y1="127.0" x2="665.0" y2="127.0" stroke="currentColor" stroke-width="1.0" opacity="0.7" stroke-linecap="round"/><line x1="567.0" y1="29.0" x2="567.0" y2="225.0" stroke="currentColor" stroke-width="1.0" opacity="0.7" stroke-linecap="round"/><circle cx="567.0" cy="127.0" r="50.0" fill="none" stroke="currentColor" stroke-width="1.6" stroke-dasharray="5 4"/><line x1="586.0" y1="121.0" x2="598.0" y2="133.0" stroke="var(--hi)" stroke-width="2.4" stroke-linecap="round"/><line x1="586.0" y1="133.0" x2="598.0" y2="121.0" stroke="var(--hi)" stroke-width="2.4" stroke-linecap="round"/><line x1="494.3" y1="121.0" x2="506.3" y2="133.0" stroke="var(--hi)" stroke-width="2.4" stroke-linecap="round"/><line x1="494.3" y1="133.0" x2="506.3" y2="121.0" stroke="var(--hi)" stroke-width="2.4" stroke-linecap="round"/><text x="664.0" y="144.0" text-anchor="end" fill="var(--muted)" style="font-size:11px;">Re</text><text x="572.0" y="41.0" text-anchor="start" fill="var(--muted)" style="font-size:11px;">Im</text><text x="567.0" y="245.0" text-anchor="middle" fill="currentColor" style="font-size:14px;font-weight:600;">two-sided: a &lt; |z| &lt; b</text><text x="567.0" y="263.0" text-anchor="middle" fill="currentColor" style="font-size:13px;">poles ½, −4/3 → ½ &lt; |z| &lt; 4/3</text><text x="567.0" y="280.0" text-anchor="middle" fill="var(--muted)" style="font-size:12px;">stable ⇔ a &lt; 1 &lt; b</text></svg><figcaption><strong>ROC shape gives causality; the dashed unit circle gives stability.</strong> Left to right: slide 10 causal (poles ⅕, ⅘), notes Fig. 2b left-sided −(3/2)ⁿu[−n−1], slide 10 two-sided (poles ½, −4/3); all three ROCs contain |z| = 1.</figcaption></figure>

> [!key] Table 1 of the notes — ROC shape ⇔ causality ⇔ stability
> | ROC of $H(z)$ | causality type | right-sided | left-sided | BIBO stable iff |
> |---|---|---|---|---|
> | $\lvert z\rvert > \lvert p_{\max}\rvert$ | causal | ✓ | ✗ | $\lvert p_{\max}\rvert < 1$ |
> | $\lvert z\rvert < \lvert p_{\min}\rvert$ | anti-causal | ✗ | ✓ | $\lvert p_{\min}\rvert > 1$ |
> | $\lvert p_{\max}\rvert < \lvert z\rvert < \infty$ | non-causal | ✓ | ✗ | $\lvert p_{\max}\rvert < 1$ |
> | $0 < \lvert z\rvert < \lvert p_{\min}\rvert$ | non-causal | ✗ | ✓ | $\lvert p_{\min}\rvert > 1$ |
> | $a < \lvert z\rvert < b$ | non-causal (two-sided) | ✓ | ✓ | $a = \lvert p_{\max,h_r}\rvert < 1$ and $b = \lvert p_{\min,h_l}\rvert > 1$ |
>
> **Causal: stable iff all poles inside the unit circle; anti-causal: iff all outside; two-sided: iff the unit circle runs through the ring.**

> [!recipe] "Is it stable?" / "Which $h[n]$ is the stable one?"
> 1. Factor; **cancel common factors first**; list finite poles and magnitudes.
> 2. *Causality given* → ROC forced → does it contain $|z| = 1$?
> 3. *Stability given* → ROC = the ring containing $|z| = 1$: pole **inside** → $A\,p^n u[n]$; pole **outside** → $-A\,p^n u[-n-1]$; pole **on** the circle → no stable version.
> 4. Causality type from the ROC (Table 1).

> [!question] Slide 10 — stable $h[n]$ and its causality type
> (A) $H(z) = \dfrac{1}{1-\frac12 z^{-1}} + \dfrac{1}{1+\frac43 z^{-1}}$  (B) $H(z) = \dfrac{1}{1-\frac15 z^{-1}} + \dfrac{1}{1-\frac45 z^{-1}}$

> [!success]- Answers
> **(A)** Poles $\tfrac12$, $-\tfrac43$. $|z| > \tfrac43$ ✗; $|z| < \tfrac12$ ✗; $\tfrac12 < |z| < \tfrac43$ ✓:
> $$
> h[n] = \left(\tfrac12\right)^n u[n] - \left(-\tfrac43\right)^n u[-n-1], \qquad \sum_n |h[n]| = 2 + 3 = 5 ,
> $$
> **non-causal** (two-sided).
> **(B)** Poles $\tfrac15$, $\tfrac45$ inside: $|z| > \tfrac45$ contains $|z| = 1$; $h[n] = \left(\tfrac15\right)^n u[n] + \left(\tfrac45\right)^n u[n]$ ($\sum|h| = \tfrac{25}{4}$), **causal**.

> [!question] Slide 11 — can an LTI FIR system be unstable? Time and z-domain.

> [!success]- Answer
> No. $h[n] = \{\underset{\uparrow}{b_0}, b_1, \dots, b_{N-1}\}$.
> - Time: $\sum_n |h[n]| = \sum_{k=0}^{N-1}|b_k| \le N \max_k|b_k| < \infty$.
> - z: $H(z) = \sum_{k=0}^{N-1} b_k z^{-k}$ has **no finite poles**; ROC is all $z$ except possibly $0$ (or $\infty$ if non-causal), so it contains $|z| = 1$.

### 1.2 Unstable inputs and marginal stability

**Pole outside the unit circle** (slides 12–13): $h[n] = 3^n u[n]$, $H(z) = \dfrac{1}{1-3z^{-1}}$, $|z| > 3$. $\delta[n]$, $u[n]$, $(\tfrac13)^n u[n]$ — almost any bounded input — give unbounded outputs. Only a zero of $X(z)$ at $3$ helps:
$$
\begin{aligned}
X(z) &= 1 - 3z^{-1} \;\leftrightarrow\; x[n] = \delta[n] - 3\delta[n-1] \\
\quad\Longrightarrow\quad Y(z) &= \frac{1-3z^{-1}}{1-3z^{-1}} = 1,\qquad y[n] = \delta[n]
\end{aligned}
$$
(and any scaled or shifted copy).

**Pole on the unit circle** (slide 14): $h[n] = (-1)^n u[n]$, $H(z) = \dfrac{1}{1+z^{-1}}$, $|z| > 1$: unstable but $h$ bounded. $\delta[n] \to (-1)^n u[n]$ and $u[n] \to \tfrac12(1 + (-1)^n)u[n]$ are bounded; $x[n] = (-1)^n u[n]$ gives $y[n] = (n+1)(-1)^n u[n]$.

### 1.2.1 Marginal stability

> [!key] Marginal stability (slide 15)
> ROC **open on the unit circle** (touches $|z| = 1$, e.g. $|z| > 1$ causal). Still **unstable**, but $h$ stays bounded (undamped $e^{j\omega n}u[n]$ terms, cosines/sines for conjugate pairs); only inputs that **resonate** give unbounded outputs.

Slides 16–17: $h[n] = a^n u[n]$, $|a| = 1$; input $x[n] = b^n u[n]$:

- $|b| > 1$: input unbounded; not a BIBO test input.
- $|b| < 1$: $Y(z) = \dfrac{1}{(1-bz^{-1})(1-az^{-1})} = \dfrac{A_1}{1-bz^{-1}} + \dfrac{A_2}{1-az^{-1}}$, $y[n] = A_1 b^n u[n] + A_2 a^n u[n]$: **bounded**.
- $|b| = 1$, $a = e^{j\theta}$, $b = e^{j\phi}$:
$$
\begin{aligned}
y[n] &= \sum_{k=0}^{n} e^{j\theta k}e^{j\phi(n-k)} \\
&= e^{j\phi n}\sum_{k=0}^{n} e^{j(\theta-\phi)k} \\
&= \begin{cases} e^{j\phi n}\,(n+1)\,u[n], & \theta = \phi \quad\text{(unbounded)}\\[4pt]
e^{j\phi n}\,\dfrac{1-e^{j(\theta-\phi)(n+1)}}{1-e^{j(\theta-\phi)}}\,u[n], & \theta \ne \phi \quad\text{(bounded by } \tfrac{2}{|1-e^{j(\theta-\phi)}|}\text{)} \end{cases}
\end{aligned}
$$

Notes example ($a = b = 1$): $h = u[n]$, $x = u[n]$ gives $y = (n+1)u[n]$; $x = c^n u[n]$, $|c| < 1$, gives the bounded $\sum_{k=0}^n c^k$.

> [!derivation]- Lecture exercise: a double pole on the unit circle is an unbounded output
> From $n\,a^n u[n] \leftrightarrow \dfrac{a z^{-1}}{(1-az^{-1})^2}$:
> $$
> \frac{1}{(1-az^{-1})^2} = \sum_{n=0}^{\infty}(n+1)\,a^n z^{-n} \;\leftrightarrow\; (n+1)\,a^n u[n], \qquad |z| > |a| .
> $$
> $|a| = 1$: $|y[n]| = n+1 \to \infty$. $|a| < 1$: $(n+1)a^n \to 0$. Matching is dangerous **only on the unit circle**.

> [!key] Pole matching
> A marginally stable system gives an unbounded output **iff the input's z-transform has a pole exactly on one of the system's uncancelled unit-circle poles**: $Y = HX$ then has a double pole on $|z| = 1$ and $y[n]$ contains $n\,e^{j\omega_0 n}$.

> [!recipe] Which bounded inputs give unbounded outputs?
> 1. Factor $H$, cancel, list poles **with angles**. Causal with an uncancelled $|p| > 1$: $h$ unbounded, almost every input fails.
> 2. Input poles: $a^n u[n] \to a$; $u[n] \to 1$; $(-1)^n u[n] \to -1$; $j^n u[n] \to j$; $\cos(\omega_0 n)u[n]$, $\sin(\omega_0 n)u[n] \to e^{\pm j\omega_0}$. Finite-length inputs: no finite poles, never match.
> 3. **Unbounded iff an input pole sits on a unit-circle pole of $H$** (not cancelled). One of $e^{\pm j\omega_0}$ is enough.
> 4. Compare angles exactly: $e^{j2/3}$ ($\tfrac23$ rad) is not $e^{j2\pi/3}$.

> [!question] Slide 18 — which inputs give an unbounded output?
> Causal $H(z) = \dfrac{1}{(1-jz^{-1})(1+z^{-1})(1-\frac23 z^{-1})}$, $|z| > 1$. (1) $(-1)^n u[n]$ (2) $u[n]$ (3) $e^{j\frac{\pi}{2}n}u[n]$ (4) $e^{-j\frac{\pi}{2}n}u[n]$ (5) $(\tfrac23)^n u[n]$ (6) $\sin(-\tfrac{\pi}{2}n)u[n]$ (7) $\cos(\tfrac{\pi}{2}n)u[n]$ (8) $\sin(\tfrac{2\pi}{3}n)u[n]$

> [!success]- Answer
> Poles $j$, $-1$ on the unit circle, $\tfrac23$ inside: marginally stable.
> **Unbounded: (1), (3), (6), (7).** (1) pole $-1$; (3) pole $j$; (6) $\sin(-\tfrac{\pi}{2}n) = -\tfrac{1}{2j}\bigl(e^{j\frac{\pi}{2}n} - e^{-j\frac{\pi}{2}n}\bigr)$ and (7) contain $e^{j\frac{\pi}{2}n}$.
> **Bounded: (2), (4), (5), (8).** Poles $1$ and $e^{\pm j2\pi/3}$ are not system poles; $-j$ is not a pole of this $H$ (complex coefficients: no conjugate pairs needed); (5) double pole at $\tfrac23$ gives a decaying $n(\tfrac23)^n u[n]$.

<figure class="ece-fig"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 680 372" width="680" height="372" role="img" style="font-family:'Source Sans 3','Source Sans Pro',system-ui,sans-serif;font-size:14px;max-width:100%;height:auto"><text x="340.0" y="22.0" text-anchor="middle" fill="currentColor" style="font-size:14px;font-weight:600;">Causal H(z) = 1 / [(1 − jz⁻¹)(1 + z⁻¹)(1 − ⅔z⁻¹)],  ROC |z| &gt; 1  (marginally stable)</text><path d="M287.00,200.00 A112.00,112.00 0 1,0 63.00,200.00 A112.00,112.00 0 1,0 287.00,200.00 Z" fill="none" stroke="currentColor" stroke-width="1.8" stroke-dasharray="6 4"/><line x1="27.0" y1="200.0" x2="323.0" y2="200.0" stroke="currentColor" stroke-width="1.0" opacity="0.7" stroke-linecap="round"/><line x1="175.0" y1="52.0" x2="175.0" y2="348.0" stroke="currentColor" stroke-width="1.0" opacity="0.7" stroke-linecap="round"/><text x="321.0" y="215.0" text-anchor="end" fill="var(--muted)" style="font-size:11px;">Re</text><text x="181.0" y="64.0" text-anchor="start" fill="var(--muted)" style="font-size:11px;">Im</text><text x="263.9" y="296.9" text-anchor="start" fill="currentColor" style="font-size:12px;">|z| = 1</text><circle cx="63.0" cy="200.0" r="7.0" fill="none" stroke="var(--accent)" stroke-width="2.0"/><text x="50.0" y="188.0" text-anchor="end" fill="var(--accent)" style="font-size:13px;font-weight:600;">1</text><circle cx="287.0" cy="200.0" r="7.0" fill="none" stroke="var(--accent)" stroke-width="2.0"/><text x="300.0" y="188.0" text-anchor="start" fill="var(--accent)" style="font-size:13px;font-weight:600;">2</text><circle cx="175.0" cy="88.0" r="7.0" fill="none" stroke="var(--accent)" stroke-width="2.0"/><text x="190.0" y="76.0" text-anchor="start" fill="var(--accent)" style="font-size:13px;font-weight:600;">3, 6, 7</text><circle cx="175.0" cy="312.0" r="7.0" fill="none" stroke="var(--accent)" stroke-width="2.0"/><text x="190.0" y="332.0" text-anchor="start" fill="var(--accent)" style="font-size:13px;font-weight:600;">4, 6, 7</text><circle cx="249.7" cy="200.0" r="7.0" fill="none" stroke="var(--accent)" stroke-width="2.0"/><text x="249.7" y="226.0" text-anchor="middle" fill="var(--accent)" style="font-size:13px;font-weight:600;">5</text><circle cx="119.0" cy="103.0" r="7.0" fill="none" stroke="var(--accent)" stroke-width="2.0"/><text x="106.0" y="93.0" text-anchor="end" fill="var(--accent)" style="font-size:13px;font-weight:600;">8</text><circle cx="119.0" cy="297.0" r="7.0" fill="none" stroke="var(--accent)" stroke-width="2.0"/><text x="106.0" y="317.0" text-anchor="end" fill="var(--accent)" style="font-size:13px;font-weight:600;">8</text><line x1="168.0" y1="81.0" x2="182.0" y2="95.0" stroke="var(--hi)" stroke-width="2.4" stroke-linecap="round"/><line x1="168.0" y1="95.0" x2="182.0" y2="81.0" stroke="var(--hi)" stroke-width="2.4" stroke-linecap="round"/><line x1="56.0" y1="193.0" x2="70.0" y2="207.0" stroke="var(--hi)" stroke-width="2.4" stroke-linecap="round"/><line x1="56.0" y1="207.0" x2="70.0" y2="193.0" stroke="var(--hi)" stroke-width="2.4" stroke-linecap="round"/><line x1="242.7" y1="193.0" x2="256.7" y2="207.0" stroke="var(--hi)" stroke-width="2.4" stroke-linecap="round"/><line x1="242.7" y1="207.0" x2="256.7" y2="193.0" stroke="var(--hi)" stroke-width="2.4" stroke-linecap="round"/><circle cx="175.0" cy="88.0" r="15.0" fill="none" stroke="var(--hi)" stroke-width="2.2" stroke-dasharray="3 3"/><circle cx="63.0" cy="200.0" r="15.0" fill="none" stroke="var(--hi)" stroke-width="2.2" stroke-dasharray="3 3"/><line x1="372.0" y1="52.0" x2="384.0" y2="64.0" stroke="var(--hi)" stroke-width="2.4" stroke-linecap="round"/><line x1="372.0" y1="64.0" x2="384.0" y2="52.0" stroke="var(--hi)" stroke-width="2.4" stroke-linecap="round"/><text x="392.0" y="63.0" text-anchor="start" fill="currentColor" style="font-size:13px;">system pole</text><circle cx="522.0" cy="58.0" r="7.0" fill="none" stroke="var(--accent)" stroke-width="2.0"/><text x="536.0" y="63.0" text-anchor="start" fill="currentColor" style="font-size:13px;">input pole (input #)</text><text x="372.0" y="98.0" text-anchor="start" fill="var(--hi)" style="font-size:12.5px;font-weight:700;">unbounded</text><text x="454.0" y="98.0" text-anchor="start" fill="currentColor" style="font-size:13px;">#1  (−1)<tspan baseline-shift="super" font-size="10">n</tspan>u[n]</text><text x="454.0" y="114.0" text-anchor="start" fill="var(--muted)" style="font-size:11.5px;">pole −1: a system pole on |z| = 1</text><text x="372.0" y="136.0" text-anchor="start" fill="var(--hi)" style="font-size:12.5px;font-weight:700;">unbounded</text><text x="454.0" y="136.0" text-anchor="start" fill="currentColor" style="font-size:13px;">#3  e<tspan baseline-shift="super" font-size="10">jπn/2</tspan>u[n]</text><text x="454.0" y="152.0" text-anchor="start" fill="var(--muted)" style="font-size:11.5px;">pole j: a system pole on |z| = 1</text><text x="372.0" y="174.0" text-anchor="start" fill="var(--hi)" style="font-size:12.5px;font-weight:700;">unbounded</text><text x="454.0" y="174.0" text-anchor="start" fill="currentColor" style="font-size:13px;">#6, 7  sin(−πn/2), cos(πn/2)</text><text x="454.0" y="190.0" text-anchor="start" fill="var(--muted)" style="font-size:11.5px;">poles ±j: the j half matches</text><text x="372.0" y="212.0" text-anchor="start" fill="var(--muted)" style="font-size:12.5px;font-weight:700;">bounded</text><text x="454.0" y="212.0" text-anchor="start" fill="currentColor" style="font-size:13px;">#2  u[n]</text><text x="454.0" y="228.0" text-anchor="start" fill="var(--muted)" style="font-size:11.5px;">pole 1: no system pole there</text><text x="372.0" y="250.0" text-anchor="start" fill="var(--muted)" style="font-size:12.5px;font-weight:700;">bounded</text><text x="454.0" y="250.0" text-anchor="start" fill="currentColor" style="font-size:13px;">#4  e<tspan baseline-shift="super" font-size="10">−jπn/2</tspan>u[n]</text><text x="454.0" y="266.0" text-anchor="start" fill="var(--muted)" style="font-size:11.5px;">pole −j: not a system pole</text><text x="372.0" y="288.0" text-anchor="start" fill="var(--muted)" style="font-size:12.5px;font-weight:700;">bounded</text><text x="454.0" y="288.0" text-anchor="start" fill="currentColor" style="font-size:13px;">#8  sin(2πn/3)u[n]</text><text x="454.0" y="304.0" text-anchor="start" fill="var(--muted)" style="font-size:11.5px;">poles e<tspan baseline-shift="super" font-size="10">±j2π/3</tspan>: no match</text><text x="372.0" y="326.0" text-anchor="start" fill="var(--muted)" style="font-size:12.5px;font-weight:700;">bounded</text><text x="454.0" y="326.0" text-anchor="start" fill="currentColor" style="font-size:13px;">#5  (⅔)<tspan baseline-shift="super" font-size="10">n</tspan>u[n]</text><text x="454.0" y="342.0" text-anchor="start" fill="var(--muted)" style="font-size:11.5px;">matches ⅔, but inside: n(⅔)<tspan baseline-shift="super" font-size="10">n</tspan> → 0</text></svg><figcaption><strong>Pole matching (slide 18).</strong> An input gives an unbounded output exactly when one of its poles (circles, labelled by input number) lands on a system pole on the unit circle.</figcaption></figure>

> [!trap] Stability slips
> - Poles alone do not decide stability; the ROC does: $\dfrac{1}{1-0.5z^{-1}} + \dfrac{1}{1-2z^{-1}}$ is stable with $\tfrac12 < |z| < 2$.
> - Told "stable": the ROC is forced. Stable $\dfrac{1}{1-3z^{-1}}$ must be anti-causal.
> - $\delta[n]$ breaks a system only if $h$ itself is unbounded; for poles on $|z|=1$ use a matching input.
> - $|z| > 1$ does not contain $|z| = 1$.
> - Angles in radians vs. multiples of $\pi$: $e^{j2/3} \ne e^{j2\pi/3}$.

> [!exam] On all 7 past exams
> Unbounded outputs and pole matching; stable/causal $h[n]$ from poles; parameters that place a zero on a bad pole; two-sided systems as backward/forward recursions; many True/False items.
> [[exams/midterm-1/past-exams/fall-2025|FA2025 #1, #7(b), #8]] · [[exams/midterm-1/past-exams/spring-2025|SP2025 #1, #6, #7]] · [[exams/midterm-1/past-exams/fall-2024|FA2024 #1, #7, #8]] · [[exams/midterm-1/past-exams/fall-2023|FA2023 #1, #7(c), #8]] · [[exams/midterm-1/past-exams/spring-2023|SP2023 #1, #7]] · [[exams/midterm-1/past-exams/spring-2021|SP2021 #1, #5]] · [[exams/midterm-1/past-exams/fall-2019|FA2019 #1, #10(d)]] · [[problems/unbounded-outputs-and-pole-matching|pole matching]] · [[problems/parameters-for-stability|parameters for stability]] · [[problems/two-sided-systems-as-recursions|two-sided recursions]] · [[exams/midterm-1/true-false-bank|T/F bank]]

## Related

[[concepts/bibo-stability|BIBO stability]] · [[concepts/marginal-stability|marginal stability]] · [[concepts/region-of-convergence|region of convergence]] · [[concepts/causality|causality]] · [[concepts/sided-sequences|sided sequences]] · [[concepts/poles-and-zeros|poles and zeros]] · [[concepts/pole-zero-cancellation|pole-zero cancellation]] · [[concepts/fir-and-iir|FIR and IIR]] · [[concepts/transfer-function|transfer function]] · [[problems/all-possible-rocs|all possible ROCs]] · [[demos/pole-zero-and-roc-explorer|pole-zero & ROC explorer]] · [[homework/hw4|HW4]] · unit: [[2-z-transform/index|Unit 2]]

### Sources for this page

Snyder, Lecture 11 notes (§1, §1.1 Figs. 1–2 and Table 1, §1.2, §1.2.1 with the lecture exercise) and slides 1–18; past exams above.
