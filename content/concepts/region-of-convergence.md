---
title: "Region of convergence (ROC)"
description: "The set of z where the z-transform sum converges: a ring bounded by pole radii that makes X(z) unique and decides causality and BIBO stability."
tags: [concept, z-transform, roc, stability]
aliases: ["ROC", "region of convergence"]
---

> [!key] Definition
> The ROC of $X(z)=\sum_{n=-\infty}^{\infty}x[n]\,z^{-n}$ is the set of $z$ where the sum converges: a **ring**
> $$
> r_1 < |z| < r_2, \qquad 0 \le r_1 < r_2 \le \infty ,
> $$
> possibly with $z=0$ or $z=\infty$. Formula **plus** ROC is one signal: $u[n]$ and $-u[-n-1]$ share $\dfrac{1}{1-z^{-1}}$ ($|z|>1$ vs $|z|<1$).

> [!key] ROC rules (Lecture 7)
> 1. No poles in the ROC; zeros allowed. 2. Connected.
> 3. Right-sided: $|z| > |p_{\max}|$. 4. Left-sided: $|z| < |p_{\min}|$. 5. Two-sided: annulus between consecutive pole radii.
> 6. Finite-length: whole plane, except $z=0$ if some $x[n]\neq0$ with $n>0$, and $z=\infty$ if some $x[n]\neq0$ with $n<0$.
>
> **Stable $\iff$ ROC contains $|z|=1$. Causal $\iff$ ROC is outside a circle and includes $z=\infty$** (Lecture 11).

<figure class="ece-fig"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 660 270" width="660" height="270" role="img" style="font-family:'Source Sans 3','Source Sans Pro',system-ui,sans-serif;font-size:14px"><defs><marker id="ahroc" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="context-stroke"/></marker></defs><clipPath id="rocout"><rect x="23.0" y="18.0" width="184.0" height="184.0"/></clipPath><path d="M23.0,18.0 h184.0 v184.0 h-184.0 Z M141.00,110.00 A26.00,26.00 0 1,0 89.00,110.00 A26.00,26.00 0 1,0 141.00,110.00 Z" fill="var(--accent)" fill-opacity="0.22" fill-rule="evenodd" stroke="none" clip-path="url(#rocout)"/><circle cx="115.0" cy="110.0" r="26.0" fill="none" stroke="var(--accent)" stroke-width="1.4"/><line x1="23.0" y1="110.0" x2="207.0" y2="110.0" stroke="currentColor" stroke-width="1.1" opacity="0.8" stroke-linecap="round"/><line x1="115.0" y1="18.0" x2="115.0" y2="202.0" stroke="currentColor" stroke-width="1.1" opacity="0.8" stroke-linecap="round"/><circle cx="115.0" cy="110.0" r="52.0" fill="none" stroke="currentColor" stroke-width="1.3" stroke-dasharray="5 4"/><line x1="109.0" y1="78.0" x2="121.0" y2="90.0" stroke="var(--hi)" stroke-width="2.4" stroke-linecap="round"/><line x1="109.0" y1="90.0" x2="121.0" y2="78.0" stroke="var(--hi)" stroke-width="2.4" stroke-linecap="round"/><line x1="109.0" y1="130.0" x2="121.0" y2="142.0" stroke="var(--hi)" stroke-width="2.4" stroke-linecap="round"/><line x1="109.0" y1="142.0" x2="121.0" y2="130.0" stroke="var(--hi)" stroke-width="2.4" stroke-linecap="round"/><text x="205.0" y="135.0" text-anchor="end" fill="var(--muted)" style="font-size:12px;">Re</text><text x="121.0" y="31.0" text-anchor="start" fill="var(--muted)" style="font-size:12px;">Im</text><text x="115.0" y="224.0" text-anchor="middle" fill="currentColor" style="font-size:14px;font-weight:600;">(a) causal: |z| &gt; ½</text><text x="115.0" y="242.0" text-anchor="middle" fill="var(--muted)" style="font-size:13px;">h = (½)ⁿ cos(πn/2) u[n]</text><clipPath id="rocin"><rect x="238.0" y="18.0" width="184.0" height="184.0"/></clipPath><path d="M408.00,110.00 A78.00,78.00 0 1,0 252.00,110.00 A78.00,78.00 0 1,0 408.00,110.00 Z" fill="var(--accent)" fill-opacity="0.22" fill-rule="evenodd" stroke="none" clip-path="url(#rocin)"/><circle cx="330.0" cy="110.0" r="78.0" fill="none" stroke="var(--accent)" stroke-width="1.4"/><line x1="238.0" y1="110.0" x2="422.0" y2="110.0" stroke="currentColor" stroke-width="1.1" opacity="0.8" stroke-linecap="round"/><line x1="330.0" y1="18.0" x2="330.0" y2="202.0" stroke="currentColor" stroke-width="1.1" opacity="0.8" stroke-linecap="round"/><circle cx="330.0" cy="110.0" r="52.0" fill="none" stroke="currentColor" stroke-width="1.3" stroke-dasharray="5 4"/><line x1="402.0" y1="104.0" x2="414.0" y2="116.0" stroke="var(--hi)" stroke-width="2.4" stroke-linecap="round"/><line x1="402.0" y1="116.0" x2="414.0" y2="104.0" stroke="var(--hi)" stroke-width="2.4" stroke-linecap="round"/><text x="420.0" y="135.0" text-anchor="end" fill="var(--muted)" style="font-size:12px;">Re</text><text x="336.0" y="31.0" text-anchor="start" fill="var(--muted)" style="font-size:12px;">Im</text><text x="330.0" y="224.0" text-anchor="middle" fill="currentColor" style="font-size:14px;font-weight:600;">(b) left-sided: |z| &lt; 3/2</text><text x="330.0" y="242.0" text-anchor="middle" fill="var(--muted)" style="font-size:13px;">h = −(3/2)ⁿ u[−n−1]</text><clipPath id="rocann"><rect x="453.0" y="18.0" width="184.0" height="184.0"/></clipPath><path d="M623.00,110.00 A78.00,78.00 0 1,0 467.00,110.00 A78.00,78.00 0 1,0 623.00,110.00 Z M571.00,110.00 A26.00,26.00 0 1,0 519.00,110.00 A26.00,26.00 0 1,0 571.00,110.00 Z" fill="var(--accent)" fill-opacity="0.22" fill-rule="evenodd" stroke="none" clip-path="url(#rocann)"/><circle cx="545.0" cy="110.0" r="26.0" fill="none" stroke="var(--accent)" stroke-width="1.4"/><circle cx="545.0" cy="110.0" r="78.0" fill="none" stroke="var(--accent)" stroke-width="1.4"/><line x1="453.0" y1="110.0" x2="637.0" y2="110.0" stroke="currentColor" stroke-width="1.1" opacity="0.8" stroke-linecap="round"/><line x1="545.0" y1="18.0" x2="545.0" y2="202.0" stroke="currentColor" stroke-width="1.1" opacity="0.8" stroke-linecap="round"/><circle cx="545.0" cy="110.0" r="52.0" fill="none" stroke="currentColor" stroke-width="1.3" stroke-dasharray="5 4"/><line x1="539.0" y1="78.0" x2="551.0" y2="90.0" stroke="var(--hi)" stroke-width="2.4" stroke-linecap="round"/><line x1="539.0" y1="90.0" x2="551.0" y2="78.0" stroke="var(--hi)" stroke-width="2.4" stroke-linecap="round"/><line x1="539.0" y1="130.0" x2="551.0" y2="142.0" stroke="var(--hi)" stroke-width="2.4" stroke-linecap="round"/><line x1="539.0" y1="142.0" x2="551.0" y2="130.0" stroke="var(--hi)" stroke-width="2.4" stroke-linecap="round"/><line x1="617.0" y1="104.0" x2="629.0" y2="116.0" stroke="var(--hi)" stroke-width="2.4" stroke-linecap="round"/><line x1="617.0" y1="116.0" x2="629.0" y2="104.0" stroke="var(--hi)" stroke-width="2.4" stroke-linecap="round"/><text x="635.0" y="135.0" text-anchor="end" fill="var(--muted)" style="font-size:12px;">Re</text><text x="551.0" y="31.0" text-anchor="start" fill="var(--muted)" style="font-size:12px;">Im</text><text x="545.0" y="224.0" text-anchor="middle" fill="currentColor" style="font-size:14px;font-weight:600;">(c) two-sided: ½ &lt; |z| &lt; 3/2</text><text x="545.0" y="242.0" text-anchor="middle" fill="var(--muted)" style="font-size:13px;">sum of (a) and (b)</text></svg><figcaption><strong>The three ROC shapes (Lecture 11, Fig. 2).</strong> (a) causal: outside the largest pole; (b) left-sided: inside the smallest pole; (c) their sum: the annulus, here containing the unit circle, so stable.</figcaption></figure>

> [!example] Lecture 7, Example 1: $X(z) = \dfrac{1+3z^{-1}}{1+\frac74 z^{-1}-\frac12 z^{-2}} = \dfrac{-\frac49}{1+2z^{-1}} + \dfrac{\frac{13}{9}}{1-\frac14 z^{-1}}$
> Poles $-2$, $\tfrac14$: three ROCs.

> [!success]- The three signals
> - $|z|>2$ (causal, unstable): $x[n] = -\tfrac49(-2)^n u[n] + \tfrac{13}{9}\left(\tfrac14\right)^n u[n]$.
> - $|z|<\tfrac14$ (anti-causal, unstable): $x[n] = \tfrac49(-2)^n u[-n-1] - \tfrac{13}{9}\left(\tfrac14\right)^n u[-n-1]$.
> - $\tfrac14<|z|<2$ (two-sided, stable): $x[n] = \tfrac{13}{9}\left(\tfrac14\right)^n u[n] + \tfrac49(-2)^n u[-n-1]$.

> [!trap]
> - Every z-transform answer needs its ROC; every inverse needs the ROC to choose each term's side.
> - Poles on the same circle ($\pm j/2$) go to the same side.
> - Right-sided is not causal: $\delta[n+1]+\delta[n]\leftrightarrow z+1$, ROC $|z|<\infty$.
> - After [[concepts/pole-zero-cancellation|pole-zero cancellation]] the ROC can be larger than $R_1\cap R_2$; an everlasting $e^{j\pi n/4}$ has an **empty** ROC.
> - $X_d(\omega)=X(e^{j\omega})$ only when the ROC contains $|z|=1$ ([[exams/midterm-1/past-exams/spring-2023|SP2023 MT1]] #1(d)).

**Where it appears:** [[2-z-transform/06-the-z-transform|L6]], [[2-z-transform/07-z-transform-properties|L7]], [[2-z-transform/08-inverse-z-transform|L8]], [[2-z-transform/11-bibo-stability-and-causality|L11]]; [[problems/z-transform-with-roc]], [[problems/all-possible-rocs]], [[problems/parameters-for-stability]]; [[homework/hw3|HW3]], [[homework/hw4|HW4]]; [[demos/pole-zero-and-roc-explorer|pole-zero and ROC explorer]].

## Related
[[concepts/z-transform]] · [[concepts/poles-and-zeros]] · [[concepts/sided-sequences]] · [[concepts/bibo-stability]] · [[concepts/causality]] · [[concepts/inverse-z-transform]]

### Sources for this page
Lecture 6 §2; Lecture 7 §1 and Example 1; Lecture 8 slides (Example 3); Lecture 11 §1.1 (Table 1, Fig. 2); Lecture 14 §1.
