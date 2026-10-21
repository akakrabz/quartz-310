---
title: "Lecture 10 — Improper transfer functions and system algebra"
description: "Improper H(z) (input taps reaching as far back as feedback taps): long division then PFE, or PFE of 1/A(z) plus shifts; system algebra: series multiplies, parallel adds."
tags: [lecture, midterm-1, z-transform, lccde, systems]
lecture: 10
---

*Lecture 10 · Wed Sep 16, 2026 · notes + slides "Transfer functions and LTI system response: Part 2" · prev: [[2-z-transform/09-transfer-functions|Lecture 9]] · next: [[2-z-transform/11-bibo-stability-and-causality|Lecture 11]]*

> [!abstract] In one breath
> - PFE needs a **proper** $H(z)$ (degrees counted in $z^{-1}$). Improper: long-divide first (quotient → impulses, remainder → PFE), or expand $1/A(z)$ and add shifted copies.
> - Series multiplies ($h_1*h_2 \leftrightarrow H_1H_2$), parallel adds ($h_1+h_2 \leftrightarrow H_1+H_2$): any network collapses to one $H(z)$.

## 1. Improper rational expressions

Proper (Lecture 9):
$$
H(z) = \frac{\sum_{k=0}^{M-1} b_k z^{-k}}{1 + \sum_{k=1}^{N} a_k z^{-k}}, \qquad M \le N .
$$
$M > N$: **improper**. In LCCDE terms: some input term is delayed at least as far as the most-delayed feedback term ($x[n-3]$ against $y[n-2]$ below).

> [!key] Improper = impulses + exponentials
> $$
> H(z) = \sum_{k=0}^{M-N-1} C_k z^{-k} + \frac{\sum_{k=0}^{N-1} d_k z^{-k}}{1 + \sum_{k=1}^{N} a_k z^{-k}}
> = \sum_{k=0}^{M-N-1} C_k z^{-k} + \sum_{k=1}^{N}\frac{A_k}{1 - p_k z^{-1}}
> $$
> $$
> \Longrightarrow\quad h[n] = \sum_{k} C_k\,\delta[n-k] + \sum_k A_k\,p_k^n\,u[n] \qquad(\text{causal}).
> $$
> $C_k$: long division. $A_k$: PFE of the **remainder** over the denominator.

> [!trap] Improper or not
> - Count degrees in $z^{-1}$: $\dfrac{z(z-4)}{z^2-5z+6} = \dfrac{1-4z^{-1}}{(1-2z^{-1})(1-3z^{-1})}$ is **proper** ([[homework/hw4|HW4]] #3(a)).
> - **Equal** degrees in $z^{-1}$ are improper: a constant $C_0$ hides. Cover-up still gives the right $A_k$; without $C_0$, $h[0]$ is wrong.
> - Divide from the **highest** power of $z^{-1}$; from the constant end the division never terminates (it produces $h[0], h[1], \dots$).

### 1.1 Applying polynomial long-division

> [!question] Exercise 1 (notes, slides 4–8): $h[n]$ of the causal LCCDE $y[n] = 2y[n-1] + 3y[n-2] + x[n] - 3x[n-1] + x[n-2] + 4x[n-3]$

> [!success]- Answer
> $Y(z)\bigl(1 - 2z^{-1} - 3z^{-2}\bigr) = X(z)\bigl(1 - 3z^{-1} + z^{-2} + 4z^{-3}\bigr)$:
> $$
> H(z) = \frac{1 - 3z^{-1} + z^{-2} + 4z^{-3}}{1 - 2z^{-1} - 3z^{-2}} = \frac{1 - 3z^{-1} + z^{-2} + 4z^{-3}}{(1-3z^{-1})(1+z^{-1})}, \qquad |z| > 3 ,
> $$
> $M = 4$, $N = 2$: improper, quotient $C_0 + C_1 z^{-1}$. Divide from the highest power:
> $$
> \begin{aligned}
> &4z^{-3} \div (-3z^{-2}) = -\tfrac43 z^{-1}: \\
> &\bigl(1 - 3z^{-1} + z^{-2} + 4z^{-3}\bigr) - \left(-\tfrac43 z^{-1}\right)\bigl(1 - 2z^{-1} - 3z^{-2}\bigr) = 1 - \tfrac53 z^{-1} - \tfrac53 z^{-2}\\
> &-\tfrac53 z^{-2} \div (-3z^{-2}) = \tfrac59: \\
> &\bigl(1 - \tfrac53 z^{-1} - \tfrac53 z^{-2}\bigr) - \tfrac59\bigl(1 - 2z^{-1} - 3z^{-2}\bigr) = \tfrac49 - \tfrac59 z^{-1}
> \end{aligned}
> $$
> $C_0 = \tfrac59$, $C_1 = -\tfrac43$:
> $$
> H(z) = \frac59 - \frac43 z^{-1} + \frac{\frac49 - \frac59 z^{-1}}{(1-3z^{-1})(1+z^{-1})} = \frac59 - \frac43 z^{-1} + \frac{A_1}{1-3z^{-1}} + \frac{A_2}{1+z^{-1}} .
> $$
> Cover-up on the remainder: $A_1 = \dfrac{\frac49 - \frac59\cdot\frac13}{1 + \frac13} = \dfrac{7}{36}$ ($z = 3$), $A_2 = \dfrac{\frac49 + \frac59}{1 + 3} = \dfrac14$ ($z = -1$). Causal:
> $$
> h[n] = \tfrac59\,\delta[n] - \tfrac43\,\delta[n-1] + \tfrac{7}{36}\,3^n u[n] + \tfrac14\,(-1)^n u[n] .
> $$
> $h = \{\underset{\uparrow}{1}, -1, 2, 5, 16, 47, \dots\}$; $h[0] = \tfrac59 + \tfrac{7}{36} + \tfrac14 = 1 = b_0$.

### 1.2 A simpler approach to improper rational expressions

Factor out the numerator; PFE with numerator 1:
$$
\begin{aligned}
H(z) &= \bigl(1 - 3z^{-1} + z^{-2} + 4z^{-3}\bigr)\,G(z), \qquad \\
G(z) &= \frac{1}{(1-3z^{-1})(1+z^{-1})} = \frac{\frac34}{1-3z^{-1}} + \frac{\frac14}{1+z^{-1}} ,
\end{aligned}
$$
so $g[n] = \tfrac34\,3^n u[n] + \tfrac14(-1)^n u[n]$ and, by linearity and time shifting,
$$
h[n] = g[n] - 3g[n-1] + g[n-2] + 4g[n-3] .
$$
"Unseemly" (notes), but identical sample for sample.

> [!recipe] Improper $H(z) \to h[n]$
> 1. Powers of $z^{-1}$; numerator degree $\ge$ denominator degree ⇒ improper.
> 2. Long-divide from the highest power of $z^{-1}$ until the remainder's degree is below the denominator's: quotient $C_0 + C_1 z^{-1} + \dots$
> 3. Cover-up PFE of remainder ÷ denominator (the original numerator gives the same $A_k$; only division gives the $C_k$).
> 4. $C_k z^{-k} \to C_k\,\delta[n-k]$; $\dfrac{A_k}{1-p_kz^{-1}} \to A_k p_k^n u[n]$ (or $-A_k p_k^n u[-n-1]$).
> 5. Check $h[0] = b_0$ (causal).

## 2. System algebra

**Parallel**: same input, outputs added.
$$
\begin{aligned}
y[n] &= x[n]*h_1[n] + x[n]*h_2[n] = x[n]*\bigl(h_1[n] + h_2[n]\bigr) \quad(\text{distributivity}) \\
\;\Longrightarrow\; H(z) &= H_1(z) + H_2(z).
\end{aligned}
$$
**Series** (cascade): output of one is input of the next.
$$
\begin{aligned}
y[n] &= \bigl(x[n]*h_1[n]\bigr)*h_2[n] = x[n]*\bigl(h_1[n]*h_2[n]\bigr) \quad(\text{associativity}) \\
\;\Longrightarrow\; H(z) &= H_1(z)\,H_2(z).
\end{aligned}
$$

<figure class="ece-fig"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 680 300" width="680" height="300" role="img" style="font-family:'Source Sans 3','Source Sans Pro',system-ui,sans-serif;font-size:14px;max-width:100%;height:auto"><defs><marker id="l10ah" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="context-stroke"/></marker></defs><text x="170.0" y="24.0" text-anchor="middle" fill="currentColor" style="font-size:14px;font-weight:600;">series (cascade)</text><text x="22.0" y="65.0" text-anchor="start" fill="currentColor" style="font-size:13px;font-family:'STIX Two Math','Latin Modern Math','Cambria Math','Times New Roman',serif;font-style:italic;">x[n]</text><path d="M55.0,60.0 L88.0,60.0" fill="none" stroke="currentColor" stroke-width="1.6" marker-end="url(#l10ah)" stroke-linejoin="round"/><rect x="88.0" y="42.0" width="74" height="36" rx="4" fill="var(--accent)" fill-opacity="0.16" stroke="currentColor" stroke-width="1.5"/><text x="125.0" y="65.0" text-anchor="middle" fill="currentColor" style="font-size:14px;">H₁(z)</text><path d="M162.0,60.0 L196.0,60.0" fill="none" stroke="currentColor" stroke-width="1.6" marker-end="url(#l10ah)" stroke-linejoin="round"/><rect x="196.0" y="42.0" width="74" height="36" rx="4" fill="var(--accent)" fill-opacity="0.16" stroke="currentColor" stroke-width="1.5"/><text x="233.0" y="65.0" text-anchor="middle" fill="currentColor" style="font-size:14px;">H₂(z)</text><path d="M270.0,60.0 L300.0,60.0" fill="none" stroke="currentColor" stroke-width="1.6" marker-end="url(#l10ah)" stroke-linejoin="round"/><text x="305.0" y="65.0" text-anchor="start" fill="currentColor" style="font-size:13px;font-family:'STIX Two Math','Latin Modern Math','Cambria Math','Times New Roman',serif;font-style:italic;">y[n]</text><text x="170.0" y="104.0" text-anchor="middle" fill="currentColor" style="font-size:20px;">≡</text><text x="22.0" y="147.0" text-anchor="start" fill="currentColor" style="font-size:13px;font-family:'STIX Two Math','Latin Modern Math','Cambria Math','Times New Roman',serif;font-style:italic;">x[n]</text><path d="M55.0,142.0 L110.0,142.0" fill="none" stroke="currentColor" stroke-width="1.6" marker-end="url(#l10ah)" stroke-linejoin="round"/><rect x="112.0" y="124.0" width="134" height="36" rx="4" fill="var(--accent2)" fill-opacity="0.16" stroke="currentColor" stroke-width="1.5"/><text x="179.0" y="147.0" text-anchor="middle" fill="currentColor" style="font-size:14px;">H₁(z) H₂(z)</text><path d="M246.0,142.0 L300.0,142.0" fill="none" stroke="currentColor" stroke-width="1.6" marker-end="url(#l10ah)" stroke-linejoin="round"/><text x="305.0" y="147.0" text-anchor="start" fill="currentColor" style="font-size:13px;font-family:'STIX Two Math','Latin Modern Math','Cambria Math','Times New Roman',serif;font-style:italic;">y[n]</text><text x="170.0" y="190.0" text-anchor="middle" fill="currentColor" style="font-size:13.5px;">h[n] = h₁[n] ∗ h₂[n]</text><text x="170.0" y="210.0" text-anchor="middle" fill="var(--muted)" style="font-size:12.5px;">ROC ⊇ ROC₁ ∩ ROC₂</text><text x="170.0" y="228.0" text-anchor="middle" fill="var(--muted)" style="font-size:12.5px;">order does not matter (commutative)</text><text x="510.0" y="24.0" text-anchor="middle" fill="currentColor" style="font-size:14px;font-weight:600;">parallel</text><text x="368.0" y="85.0" text-anchor="start" fill="currentColor" style="font-size:13px;font-family:'STIX Two Math','Latin Modern Math','Cambria Math','Times New Roman',serif;font-style:italic;">x[n]</text><path d="M400.0,80.0 L420.0,80.0" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linejoin="round"/><circle cx="420" cy="80" r="3" fill="currentColor"/><path d="M420.0,48.0 L420.0,112.0" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linejoin="round"/><path d="M420.0,48.0 L466.0,48.0" fill="none" stroke="currentColor" stroke-width="1.6" marker-end="url(#l10ah)" stroke-linejoin="round"/><rect x="466.0" y="30.0" width="74" height="36" rx="4" fill="var(--accent)" fill-opacity="0.16" stroke="currentColor" stroke-width="1.5"/><text x="503.0" y="53.0" text-anchor="middle" fill="currentColor" style="font-size:14px;">H₁(z)</text><path d="M540.0,48.0 L590.0,48.0" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linejoin="round"/><path d="M590.0,48.0 L590.0,68.0" fill="none" stroke="currentColor" stroke-width="1.6" marker-end="url(#l10ah)" stroke-linejoin="round"/><path d="M420.0,112.0 L466.0,112.0" fill="none" stroke="currentColor" stroke-width="1.6" marker-end="url(#l10ah)" stroke-linejoin="round"/><rect x="466.0" y="94.0" width="74" height="36" rx="4" fill="var(--accent)" fill-opacity="0.16" stroke="currentColor" stroke-width="1.5"/><text x="503.0" y="117.0" text-anchor="middle" fill="currentColor" style="font-size:14px;">H₂(z)</text><path d="M540.0,112.0 L590.0,112.0" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linejoin="round"/><path d="M590.0,112.0 L590.0,92.0" fill="none" stroke="currentColor" stroke-width="1.6" marker-end="url(#l10ah)" stroke-linejoin="round"/><circle cx="590" cy="80" r="11" fill="none" stroke="currentColor" stroke-width="1.5"/><path d="M584.0,80.0 L596.0,80.0" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linejoin="round"/><path d="M590.0,74.0 L590.0,86.0" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linejoin="round"/><path d="M601.0,80.0 L632.0,80.0" fill="none" stroke="currentColor" stroke-width="1.6" marker-end="url(#l10ah)" stroke-linejoin="round"/><text x="636.0" y="85.0" text-anchor="start" fill="currentColor" style="font-size:13px;font-family:'STIX Two Math','Latin Modern Math','Cambria Math','Times New Roman',serif;font-style:italic;">y[n]</text><text x="510.0" y="158.0" text-anchor="middle" fill="currentColor" style="font-size:20px;">≡</text><text x="368.0" y="195.0" text-anchor="start" fill="currentColor" style="font-size:13px;font-family:'STIX Two Math','Latin Modern Math','Cambria Math','Times New Roman',serif;font-style:italic;">x[n]</text><path d="M400.0,190.0 L448.0,190.0" fill="none" stroke="currentColor" stroke-width="1.6" marker-end="url(#l10ah)" stroke-linejoin="round"/><rect x="448.0" y="172.0" width="140" height="36" rx="4" fill="var(--accent2)" fill-opacity="0.16" stroke="currentColor" stroke-width="1.5"/><text x="518.0" y="195.0" text-anchor="middle" fill="currentColor" style="font-size:14px;">H₁(z) + H₂(z)</text><path d="M588.0,190.0 L632.0,190.0" fill="none" stroke="currentColor" stroke-width="1.6" marker-end="url(#l10ah)" stroke-linejoin="round"/><text x="636.0" y="195.0" text-anchor="start" fill="currentColor" style="font-size:13px;font-family:'STIX Two Math','Latin Modern Math','Cambria Math','Times New Roman',serif;font-style:italic;">y[n]</text><text x="510.0" y="238.0" text-anchor="middle" fill="currentColor" style="font-size:13.5px;">h[n] = h₁[n] + h₂[n]</text><text x="510.0" y="258.0" text-anchor="middle" fill="var(--muted)" style="font-size:12.5px;">ROC ⊇ ROC₁ ∩ ROC₂</text><path d="M340.0,20.0 L340.0,280.0" fill="none" stroke="var(--muted)" stroke-width="1" stroke-linejoin="round"/></svg><figcaption><strong>System algebra (notes Fig. 1).</strong> Series: h = h₁ ∗ h₂, H = H₁H₂; parallel: h = h₁ + h₂, H = H₁ + H₂; the ROC contains ROC₁ ∩ ROC₂.</figcaption></figure>

> [!key] Table 1 of the notes
> | connection | impulse response $h[n]$ | transfer function $H(z)$ |
> |---|---|---|
> | parallel | $h_1[n] + h_2[n]$ | $H_1(z) + H_2(z)$ |
> | series | $h_1[n] * h_2[n]$ | $H_1(z)\,H_2(z)$ |
>
> Series/parallel networks "collapse" into **one** LTI system; cascade order does not matter (convolution commutes).

Combined ROC: at least $\text{ROC}_1 \cap \text{ROC}_2$. A zero of one system can cancel a pole of the other, so a combination with unstable parts can be stable: $u[n] * (\delta[n] - \delta[n-1]) = \delta[n]$ (series, one unstable); $u[n] + (\delta[n] - u[n]) = \delta[n]$ (parallel, both unstable).

> [!question] Slide 11 — overall $H(z)$ in terms of $H_1,\dots,H_5$ ($H_1$, then $H_5$ in parallel with $H_2$ followed by $H_3 \parallel H_4$)

> [!success]- Answer
> Track the z-transform on every wire: $XH_1$ after $H_1$, $XH_1H_2$ after $H_2$; the adder inputs are $XH_1H_5$, $XH_1H_2H_3$, $XH_1H_2H_4$:
> $$
> \begin{aligned}
> Y &= X\,H_1\bigl(H_5 + H_2(H_3 + H_4)\bigr) \\
> \quad\Longrightarrow\quad H(z) &= H_1(z)\Bigl[H_5(z) + H_2(z)\bigl(H_3(z) + H_4(z)\bigr)\Bigr].
> \end{aligned}
> $$

<figure class="ece-fig"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 680 250" width="680" height="250" role="img" style="font-family:'Source Sans 3','Source Sans Pro',system-ui,sans-serif;font-size:14px;max-width:100%;height:auto"><defs><marker id="l10bh" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="context-stroke"/></marker></defs><text x="20.0" y="125.0" text-anchor="start" fill="currentColor" style="font-size:13px;font-family:'STIX Two Math','Latin Modern Math','Cambria Math','Times New Roman',serif;font-style:italic;">x[n]</text><path d="M52.0,120.0 L92.0,120.0" fill="none" stroke="currentColor" stroke-width="1.6" marker-end="url(#l10bh)" stroke-linejoin="round"/><rect x="93.0" y="102.0" width="74" height="36" rx="4" fill="var(--accent)" fill-opacity="0.16" stroke="currentColor" stroke-width="1.5"/><text x="130.0" y="125.0" text-anchor="middle" fill="currentColor" style="font-size:14px;">H₁(z)</text><path d="M167.0,120.0 L200.0,120.0" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linejoin="round"/><circle cx="200" cy="120" r="3" fill="currentColor"/><path d="M200.0,40.0 L200.0,181.0" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linejoin="round"/><path d="M200.0,40.0 L395.0,40.0" fill="none" stroke="currentColor" stroke-width="1.6" marker-end="url(#l10bh)" stroke-linejoin="round"/><rect x="395.0" y="22.0" width="74" height="36" rx="4" fill="var(--accent)" fill-opacity="0.16" stroke="currentColor" stroke-width="1.5"/><text x="432.0" y="45.0" text-anchor="middle" fill="currentColor" style="font-size:14px;">H₅(z)</text><path d="M200.0,181.0 L246.0,181.0" fill="none" stroke="currentColor" stroke-width="1.6" marker-end="url(#l10bh)" stroke-linejoin="round"/><rect x="246.0" y="163.0" width="74" height="36" rx="4" fill="var(--accent)" fill-opacity="0.16" stroke="currentColor" stroke-width="1.5"/><text x="283.0" y="186.0" text-anchor="middle" fill="currentColor" style="font-size:14px;">H₂(z)</text><path d="M320.0,181.0 L345.0,181.0" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linejoin="round"/><circle cx="345" cy="181" r="3" fill="currentColor"/><path d="M345.0,150.0 L345.0,212.0" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linejoin="round"/><path d="M345.0,150.0 L395.0,150.0" fill="none" stroke="currentColor" stroke-width="1.6" marker-end="url(#l10bh)" stroke-linejoin="round"/><rect x="395.0" y="132.0" width="74" height="36" rx="4" fill="var(--accent)" fill-opacity="0.16" stroke="currentColor" stroke-width="1.5"/><text x="432.0" y="155.0" text-anchor="middle" fill="currentColor" style="font-size:14px;">H₃(z)</text><path d="M345.0,212.0 L395.0,212.0" fill="none" stroke="currentColor" stroke-width="1.6" marker-end="url(#l10bh)" stroke-linejoin="round"/><rect x="395.0" y="194.0" width="74" height="36" rx="4" fill="var(--accent)" fill-opacity="0.16" stroke="currentColor" stroke-width="1.5"/><text x="432.0" y="217.0" text-anchor="middle" fill="currentColor" style="font-size:14px;">H₄(z)</text><path d="M469.0,40.0 L540.0,40.0 L540.0,107.0" fill="none" stroke="currentColor" stroke-width="1.6" marker-end="url(#l10bh)" stroke-linejoin="round"/><path d="M469.0,150.0 L534.0,150.0 L534.0,131.5" fill="none" stroke="currentColor" stroke-width="1.6" marker-end="url(#l10bh)" stroke-linejoin="round"/><path d="M469.0,212.0 L546.0,212.0 L546.0,131.5" fill="none" stroke="currentColor" stroke-width="1.6" marker-end="url(#l10bh)" stroke-linejoin="round"/><circle cx="540" cy="120" r="13" fill="none" stroke="currentColor" stroke-width="1.5"/><path d="M534.0,120.0 L546.0,120.0" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linejoin="round"/><path d="M540.0,114.0 L540.0,126.0" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linejoin="round"/><path d="M553.0,120.0 L590.0,120.0" fill="none" stroke="currentColor" stroke-width="1.6" marker-end="url(#l10bh)" stroke-linejoin="round"/><text x="596.0" y="125.0" text-anchor="start" fill="currentColor" style="font-size:13px;font-family:'STIX Two Math','Latin Modern Math','Cambria Math','Times New Roman',serif;font-style:italic;">y[n]</text><text x="300.0" y="30.0" text-anchor="middle" fill="var(--accent)" style="font-size:12px;">X H₁</text><text x="345.0" y="138.0" text-anchor="end" fill="var(--accent)" style="font-size:12px;">X H₁H₂</text><text x="500.0" y="32.0" text-anchor="start" fill="var(--accent)" style="font-size:12px;">X H₁H₅</text><text x="472.0" y="167.0" text-anchor="start" fill="var(--accent)" style="font-size:11px;">X H₁H₂H₃</text><text x="472.0" y="204.0" text-anchor="start" fill="var(--accent)" style="font-size:11px;">X H₁H₂H₄</text></svg><figcaption><strong>Slide 11 with every wire labelled.</strong> The three adder inputs are XH₁H₅, XH₁H₂H₃ and XH₁H₂H₄.</figcaption></figure>

> [!exam] On the exams
> Improper $H(z)$ inside LCCDE problems; series/parallel with sequences; True/False on stability of combined systems (cancellation).
> [[exams/midterm-1/past-exams/fall-2025|FA2025 #1(f), #6]] · [[exams/midterm-1/past-exams/spring-2025|SP2025 #1(d), #3]] · [[exams/midterm-1/past-exams/fall-2024|FA2024 #1(c), #3]] · [[exams/midterm-1/past-exams/fall-2023|FA2023 #1(c), #1(e)]] · [[exams/midterm-1/past-exams/spring-2021|SP2021 #1(c), #6]] · [[exams/midterm-1/past-exams/fall-2019|FA2019 #1(d), #10(d)]] · [[problems/lccde-to-transfer-function-and-response|LCCDE ↔ H(z) ↔ response]] · [[problems/finding-h-from-input-output-pairs|finding h from input–output pairs]] · [[exams/midterm-1/true-false-bank|T/F bank]]

## Related

[[concepts/system-algebra|system algebra]] · [[concepts/pole-zero-cancellation|pole-zero cancellation]] · [[concepts/partial-fraction-expansion|partial-fraction expansion]] · [[concepts/inverse-z-transform|inverse z-transform]] · [[concepts/transfer-function|transfer function]] · [[concepts/block-diagram|block diagram]] · [[concepts/bibo-stability|BIBO stability]] · [[0-toolkit/04-factoring-and-long-division|factoring and long division]] · [[homework/hw4|HW4]] · unit: [[2-z-transform/index|Unit 2]]

### Sources for this page

Snyder, Lecture 10 notes (§1 improper expressions, §1.1 Exercise 1, §1.2 numerator-1 approach, §2 system algebra, Table 1, Fig. 1) and slides 1–11; HW4 #3(a); past exams above.
