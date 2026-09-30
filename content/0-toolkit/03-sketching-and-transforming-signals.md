---
title: "Sketching and transforming signals"
description: "Sequence notation with the n = 0 arrow, time shift, reversal, downsampling, the substitute-don't-guess rule for x[-n+3] and x[2n+1], even and odd parts, and writing a finite sequence with deltas and steps — the index bookkeeping behind HW1, every convolution and every shift-invariance proof."
tags: [toolkit, signals]
---

*Toolkit · reference page · Lectures 1–3 and HW1 #1–#3; used again in every [[concepts/convolution|convolution]] and every [[concepts/time-invariance|time-invariance]] test*

Most lost points in Unit 1 are index slips, not concept errors. The cure is mechanical: **write down where $n=0$ is, and transform by substitution**.

## Sequence notation

$x[n] = \{2,\ 4,\ \underset{\uparrow}{1},\ 0,\ -2,\ 5,\ 7,\ 3\}$ means $x[-2]=2$, $x[-1]=4$, $x[0]=1$, …, $x[5]=3$, and $x[n]=0$ for every other $n$. The arrow marks $n=0$ (Lecture 2 also uses bold or underline). No arrow means the list starts at $n=0$ — but on an exam, always draw it. Samples outside the list are zero.

## The three elementary operations

| operation | formula | what happens to the plot | example with $x$ above |
|---|---|---|---|
| shift (delay) | $x[n-n_0]$ | moves **right** by $n_0$ if $n_0>0$, left if $n_0<0$ | $x[n-2]$ starts at $n=0$ |
| reversal | $x[-n]$ | mirror about $n=0$ | $x[-n]$ runs from $n=-5$ to $2$ |
| downsampling | $x[Mn]$ | keep every $M$-th sample (those with index divisible by $M$), close the gaps | $x[2n] = \{2,\ \underset{\uparrow}{1},\ -2,\ 7\}$ on $n = -1..2$ |

Downsampling throws samples away, so it cannot be undone; the upsampled $x[n/M]$ (zero unless $M\mid n$) inserts zeros. A shift by a *fraction* of a sample does not exist in discrete time — which is exactly why the order of operations matters.

## Substitute, don't guess

> [!recipe] Evaluating $y[n] = x[\text{expression in } n]$
> 1. Make a table: for each $n$, compute the argument $m$ (e.g. $m = -n+3$).
> 2. Read $x[m]$ from the list (zero outside it).
> 3. Find where $y$ is nonzero by solving "$m$ inside the support of $x$" for $n$, and mark $n=0$.
>
> Two-step alternative: every operation acts on the **current** $n$. For $x[-n+3]$, reverse first ($v[n] = x[-n]$), then delay by 3 ($v[n-3] = x[-(n-3)] = x[-n+3]$); or advance by 3 first ($w[n] = x[n+3]$), then reverse ($w[-n] = x[-n+3]$).

> [!trap] "Shift by 3, then flip" is ambiguous — and usually wrong
> Delaying by 3 and *then* reversing gives $x[-n-3]$, not $x[-n+3]$: a six-sample error. Likewise $x[2n+1]$ is "advance by 1, then keep every 2nd sample"; downsampling first and then shifting gives $x[2(n+1)] = x[2n+2]$. When in doubt, use the table.

<figure class="ece-fig"><svg viewBox="0 0 560 298" width="560" role="img" aria-label="Stem plots of x[n], x[-n+3] and x[2n+1]"><text x="6" y="48" font-size="13" fill="var(--accent)" font-style="italic">x[n]</text><line x1="108" y1="70" x2="550" y2="70" stroke="currentColor" stroke-width="1"/><line x1="120.0" y1="70" x2="120.0" y2="73" stroke="currentColor" stroke-width="1"/><text x="120.0" y="85" font-size="10" text-anchor="middle" fill="var(--muted)">−3</text><line x1="166.7" y1="70" x2="166.7" y2="73" stroke="currentColor" stroke-width="1"/><text x="166.7" y="85" font-size="10" text-anchor="middle" fill="var(--muted)">−2</text><line x1="166.7" y1="70" x2="166.7" y2="58.0" stroke="var(--accent)" stroke-width="2"/><circle cx="166.7" cy="58.0" r="3.6" fill="var(--accent)"/><text x="173.7" y="52.0" font-size="10.5" fill="currentColor">2</text><line x1="213.3" y1="70" x2="213.3" y2="73" stroke="currentColor" stroke-width="1"/><text x="213.3" y="85" font-size="10" text-anchor="middle" fill="var(--muted)">−1</text><line x1="213.3" y1="70" x2="213.3" y2="46.0" stroke="var(--accent)" stroke-width="2"/><circle cx="213.3" cy="46.0" r="3.6" fill="var(--accent)"/><text x="220.3" y="40.0" font-size="10.5" fill="currentColor">4</text><line x1="260.0" y1="70" x2="260.0" y2="73" stroke="currentColor" stroke-width="1"/><text x="260.0" y="85" font-size="10" text-anchor="middle" fill="var(--muted)" font-weight="bold">n=0</text><line x1="260.0" y1="70" x2="260.0" y2="64.0" stroke="var(--accent)" stroke-width="2"/><circle cx="260.0" cy="64.0" r="3.6" fill="var(--accent)"/><text x="267.0" y="58.0" font-size="10.5" fill="currentColor">1</text><line x1="306.7" y1="70" x2="306.7" y2="73" stroke="currentColor" stroke-width="1"/><text x="306.7" y="85" font-size="10" text-anchor="middle" fill="var(--muted)">1</text><line x1="306.7" y1="70" x2="306.7" y2="70.0" stroke="var(--accent)" stroke-width="2"/><circle cx="306.7" cy="70.0" r="3.6" fill="var(--accent)"/><text x="313.7" y="64.0" font-size="10.5" fill="currentColor">0</text><line x1="353.3" y1="70" x2="353.3" y2="73" stroke="currentColor" stroke-width="1"/><text x="353.3" y="85" font-size="10" text-anchor="middle" fill="var(--muted)">2</text><line x1="353.3" y1="70" x2="353.3" y2="82.0" stroke="var(--accent)" stroke-width="2"/><circle cx="353.3" cy="82.0" r="3.6" fill="var(--accent)"/><text x="360.3" y="96.0" font-size="10.5" fill="currentColor">−2</text><line x1="400.0" y1="70" x2="400.0" y2="73" stroke="currentColor" stroke-width="1"/><text x="400.0" y="85" font-size="10" text-anchor="middle" fill="var(--muted)">3</text><line x1="400.0" y1="70" x2="400.0" y2="40.0" stroke="var(--accent)" stroke-width="2"/><circle cx="400.0" cy="40.0" r="3.6" fill="var(--accent)"/><text x="407.0" y="34.0" font-size="10.5" fill="currentColor">5</text><line x1="446.7" y1="70" x2="446.7" y2="73" stroke="currentColor" stroke-width="1"/><text x="446.7" y="85" font-size="10" text-anchor="middle" fill="var(--muted)">4</text><line x1="446.7" y1="70" x2="446.7" y2="28.0" stroke="var(--accent)" stroke-width="2"/><circle cx="446.7" cy="28.0" r="3.6" fill="var(--accent)"/><text x="453.7" y="22.0" font-size="10.5" fill="currentColor">7</text><line x1="493.3" y1="70" x2="493.3" y2="73" stroke="currentColor" stroke-width="1"/><text x="493.3" y="85" font-size="10" text-anchor="middle" fill="var(--muted)">5</text><line x1="493.3" y1="70" x2="493.3" y2="52.0" stroke="var(--accent)" stroke-width="2"/><circle cx="493.3" cy="52.0" r="3.6" fill="var(--accent)"/><text x="500.3" y="46.0" font-size="10.5" fill="currentColor">3</text><line x1="540.0" y1="70" x2="540.0" y2="73" stroke="currentColor" stroke-width="1"/><text x="540.0" y="85" font-size="10" text-anchor="middle" fill="var(--muted)">6</text><text x="6" y="136" font-size="13" fill="var(--accent2)" font-style="italic">y[n] = x[−n+3]</text><line x1="108" y1="158" x2="550" y2="158" stroke="currentColor" stroke-width="1"/><line x1="120.0" y1="158" x2="120.0" y2="161" stroke="currentColor" stroke-width="1"/><text x="120.0" y="173" font-size="10" text-anchor="middle" fill="var(--muted)">−3</text><line x1="166.7" y1="158" x2="166.7" y2="161" stroke="currentColor" stroke-width="1"/><text x="166.7" y="173" font-size="10" text-anchor="middle" fill="var(--muted)">−2</text><line x1="166.7" y1="158" x2="166.7" y2="140.0" stroke="var(--accent2)" stroke-width="2"/><circle cx="166.7" cy="140.0" r="3.6" fill="var(--accent2)"/><text x="173.7" y="134.0" font-size="10.5" fill="currentColor">3</text><line x1="213.3" y1="158" x2="213.3" y2="161" stroke="currentColor" stroke-width="1"/><text x="213.3" y="173" font-size="10" text-anchor="middle" fill="var(--muted)">−1</text><line x1="213.3" y1="158" x2="213.3" y2="116.0" stroke="var(--accent2)" stroke-width="2"/><circle cx="213.3" cy="116.0" r="3.6" fill="var(--accent2)"/><text x="220.3" y="110.0" font-size="10.5" fill="currentColor">7</text><line x1="260.0" y1="158" x2="260.0" y2="161" stroke="currentColor" stroke-width="1"/><text x="260.0" y="173" font-size="10" text-anchor="middle" fill="var(--muted)" font-weight="bold">n=0</text><line x1="260.0" y1="158" x2="260.0" y2="128.0" stroke="var(--accent2)" stroke-width="2"/><circle cx="260.0" cy="128.0" r="3.6" fill="var(--accent2)"/><text x="267.0" y="122.0" font-size="10.5" fill="currentColor">5</text><line x1="306.7" y1="158" x2="306.7" y2="161" stroke="currentColor" stroke-width="1"/><text x="306.7" y="173" font-size="10" text-anchor="middle" fill="var(--muted)">1</text><line x1="306.7" y1="158" x2="306.7" y2="170.0" stroke="var(--accent2)" stroke-width="2"/><circle cx="306.7" cy="170.0" r="3.6" fill="var(--accent2)"/><text x="313.7" y="184.0" font-size="10.5" fill="currentColor">−2</text><line x1="353.3" y1="158" x2="353.3" y2="161" stroke="currentColor" stroke-width="1"/><text x="353.3" y="173" font-size="10" text-anchor="middle" fill="var(--muted)">2</text><line x1="353.3" y1="158" x2="353.3" y2="158.0" stroke="var(--accent2)" stroke-width="2"/><circle cx="353.3" cy="158.0" r="3.6" fill="var(--accent2)"/><text x="360.3" y="152.0" font-size="10.5" fill="currentColor">0</text><line x1="400.0" y1="158" x2="400.0" y2="161" stroke="currentColor" stroke-width="1"/><text x="400.0" y="173" font-size="10" text-anchor="middle" fill="var(--muted)">3</text><line x1="400.0" y1="158" x2="400.0" y2="152.0" stroke="var(--accent2)" stroke-width="2"/><circle cx="400.0" cy="152.0" r="3.6" fill="var(--accent2)"/><text x="407.0" y="146.0" font-size="10.5" fill="currentColor">1</text><line x1="446.7" y1="158" x2="446.7" y2="161" stroke="currentColor" stroke-width="1"/><text x="446.7" y="173" font-size="10" text-anchor="middle" fill="var(--muted)">4</text><line x1="446.7" y1="158" x2="446.7" y2="134.0" stroke="var(--accent2)" stroke-width="2"/><circle cx="446.7" cy="134.0" r="3.6" fill="var(--accent2)"/><text x="453.7" y="128.0" font-size="10.5" fill="currentColor">4</text><line x1="493.3" y1="158" x2="493.3" y2="161" stroke="currentColor" stroke-width="1"/><text x="493.3" y="173" font-size="10" text-anchor="middle" fill="var(--muted)">5</text><line x1="493.3" y1="158" x2="493.3" y2="146.0" stroke="var(--accent2)" stroke-width="2"/><circle cx="493.3" cy="146.0" r="3.6" fill="var(--accent2)"/><text x="500.3" y="140.0" font-size="10.5" fill="currentColor">2</text><line x1="540.0" y1="158" x2="540.0" y2="161" stroke="currentColor" stroke-width="1"/><text x="540.0" y="173" font-size="10" text-anchor="middle" fill="var(--muted)">6</text><text x="6" y="224" font-size="13" fill="var(--hi)" font-style="italic">z[n] = x[2n+1]</text><line x1="108" y1="246" x2="550" y2="246" stroke="currentColor" stroke-width="1"/><line x1="120.0" y1="246" x2="120.0" y2="249" stroke="currentColor" stroke-width="1"/><text x="120.0" y="261" font-size="10" text-anchor="middle" fill="var(--muted)">−3</text><line x1="166.7" y1="246" x2="166.7" y2="249" stroke="currentColor" stroke-width="1"/><text x="166.7" y="261" font-size="10" text-anchor="middle" fill="var(--muted)">−2</text><line x1="213.3" y1="246" x2="213.3" y2="249" stroke="currentColor" stroke-width="1"/><text x="213.3" y="261" font-size="10" text-anchor="middle" fill="var(--muted)">−1</text><line x1="213.3" y1="246" x2="213.3" y2="222.0" stroke="var(--hi)" stroke-width="2"/><circle cx="213.3" cy="222.0" r="3.6" fill="var(--hi)"/><text x="220.3" y="216.0" font-size="10.5" fill="currentColor">4</text><line x1="260.0" y1="246" x2="260.0" y2="249" stroke="currentColor" stroke-width="1"/><text x="260.0" y="261" font-size="10" text-anchor="middle" fill="var(--muted)" font-weight="bold">n=0</text><line x1="260.0" y1="246" x2="260.0" y2="246.0" stroke="var(--hi)" stroke-width="2"/><circle cx="260.0" cy="246.0" r="3.6" fill="var(--hi)"/><text x="267.0" y="240.0" font-size="10.5" fill="currentColor">0</text><line x1="306.7" y1="246" x2="306.7" y2="249" stroke="currentColor" stroke-width="1"/><text x="306.7" y="261" font-size="10" text-anchor="middle" fill="var(--muted)">1</text><line x1="306.7" y1="246" x2="306.7" y2="216.0" stroke="var(--hi)" stroke-width="2"/><circle cx="306.7" cy="216.0" r="3.6" fill="var(--hi)"/><text x="313.7" y="210.0" font-size="10.5" fill="currentColor">5</text><line x1="353.3" y1="246" x2="353.3" y2="249" stroke="currentColor" stroke-width="1"/><text x="353.3" y="261" font-size="10" text-anchor="middle" fill="var(--muted)">2</text><line x1="353.3" y1="246" x2="353.3" y2="228.0" stroke="var(--hi)" stroke-width="2"/><circle cx="353.3" cy="228.0" r="3.6" fill="var(--hi)"/><text x="360.3" y="222.0" font-size="10.5" fill="currentColor">3</text><line x1="400.0" y1="246" x2="400.0" y2="249" stroke="currentColor" stroke-width="1"/><text x="400.0" y="261" font-size="10" text-anchor="middle" fill="var(--muted)">3</text><line x1="446.7" y1="246" x2="446.7" y2="249" stroke="currentColor" stroke-width="1"/><text x="446.7" y="261" font-size="10" text-anchor="middle" fill="var(--muted)">4</text><line x1="493.3" y1="246" x2="493.3" y2="249" stroke="currentColor" stroke-width="1"/><text x="493.3" y="261" font-size="10" text-anchor="middle" fill="var(--muted)">5</text><line x1="540.0" y1="246" x2="540.0" y2="249" stroke="currentColor" stroke-width="1"/><text x="540.0" y="261" font-size="10" text-anchor="middle" fill="var(--muted)">6</text></svg><figcaption><b>Substitute, then plot.</b> Top: x[n] = {2, 4, <u>1</u>, 0, −2, 5, 7, 3} (x[0] = 1). Middle: y[n] = x[−n+3] is x reversed and delayed by 3 — y[0] = x[3] = 5. Bottom: z[n] = x[2n+1] keeps only the odd-index samples x[−1], x[1], x[3], x[5] and packs them at n = −1, 0, 1, 2 (HW1 #2).</figcaption></figure>

> [!question] HW1 #2: with $x[n] = \{2,4,\underset{\uparrow}{1},0,-2,5,7,3\}$, sketch (a) $y[n] = x[-n+3]$ and (b) $z[n] = x[2n+1]$.

> [!success]- Answers
> (a) $m = 3-n$ lies in $[-2,5]$ iff $-2\le n\le5$. Table: $n=-2\to x[5]=3$, $n=-1\to x[4]=7$, $n=0\to x[3]=5$, $n=1\to x[2]=-2$, $n=2\to x[1]=0$, $n=3\to x[0]=1$, $n=4\to x[-1]=4$, $n=5\to x[-2]=2$:
> $$
> y[n] = \{3,\ 7,\ \underset{\uparrow}{5},\ -2,\ 0,\ 1,\ 4,\ 2\},\qquad -2\le n\le5 .
> $$
> (b) $m = 2n+1$ is odd, and lies in $[-2,5]$ iff $-1\le n\le2$: $n=-1\to x[-1]=4$, $n=0\to x[1]=0$, $n=1\to x[3]=5$, $n=2\to x[5]=3$:
> $$
> z[n] = \{4,\ \underset{\uparrow}{0},\ 5,\ 3\},\qquad -1\le n\le2 .
> $$
> The even-index samples $x[-2], x[0], x[2], x[4]$ are gone for good.

**The same discipline proves shift-variance.** For $y[n] = x[2n]$: shifting the input gives $T\{x[n-n_0]\} = x[2n-n_0]$, while shifting the output gives $y[n-n_0] = x[2(n-n_0)] = x[2n-2n_0]$. Different, so the downsampler is **not** time-invariant. Every row of the [[problems/classifying-system-properties|system-property table]] that evaluates $x$ at a modified index — $x[\lvert n\rvert]$ (Lecture 3), $2x[\lvert n\rvert]+10$ (SP2025), $x[\lvert n\rvert+n]$ (FA2019) — is decided this way; see [[1-signals-and-systems/03-system-properties|Lecture 3]].

## Even and odd parts

Every signal splits uniquely as $x[n] = x_e[n] + x_o[n]$ with

$$
\begin{aligned}
x_e[n] &= \tfrac12\big(x[n]+x[-n]\big)\ \ (\text{even: } x_e[-n]=x_e[n]),\\
x_o[n] &= \tfrac12\big(x[n]-x[-n]\big)\ \ (\text{odd: } x_o[0]=0).
\end{aligned}
$$

Example: $x = \{\underset{\uparrow}{1},2,3\}$ gives $x_e = \{\tfrac32,1,\underset{\uparrow}{1},1,\tfrac32\}$ and $x_o = \{-\tfrac32,-1,\underset{\uparrow}{0},1,\tfrac32\}$; add them back to check.

## Writing a sequence with $\delta$'s and $u$'s

- **Deltas:** one term per nonzero sample, $x[n] = \sum_k x[k]\,\delta[n-k]$ (Lecture 4's sifting identity).
- **Steps:** walk left to right and add $c\,u[n-n_1]$ at every index $n_1$ where the level **jumps by $c$**. A pulse of height $A$ on $n_1\le n\le n_2$ is $A\big(u[n-n_1]-u[n-n_2-1]\big)$ — note the $-1$: $u[n]-u[n-8]$ has **8** samples.

> [!question] HW1 #3(b): $y[n] = 2$ for $-3\le n\le0$, $y[n] = -1$ for $1\le n\le4$, zero elsewhere. Write it with (i) $\delta$'s and (ii) $u$'s.

> [!success]- Answer
> (i) $y[n] = 2\big(\delta[n+3]+\delta[n+2]+\delta[n+1]+\delta[n]\big) - \big(\delta[n-1]+\delta[n-2]+\delta[n-3]+\delta[n-4]\big)$.
>
> (ii) Jumps: $+2$ at $n=-3$, $2\to-1$ (i.e. $-3$) at $n=1$, $-1\to0$ (i.e. $+1$) at $n=5$:
> $$
> y[n] = 2u[n+3] - 3u[n-1] + u[n-5].
> $$
> (Part (a) is $3\big(u[n+3]-u[n-2]\big)$, value 3 on $-3\le n\le1$.)

**Products of steps are windows.** $u[n+1]\,u[-n+1] = 1$ exactly for $-1\le n\le1$, so [[0-midterm-1/past-exams/fall-2025|FA2025 #3(b)]]'s input $x[n] = n\,u[n+1]u[-n+1] = \{-1,\underset{\uparrow}{0},1\}$. And $u[n]\,u[n-4] = u[n-4]$ (the later step wins), so HW1 #1(c)'s $n\,u[n]u[n-4]$ is $n\,u[n-4]$ — **not** $n\big(u[n]-u[n-4]\big)$. $4u[3-n]$ is 4 for all $n\le3$ (Lecture 2).

## Python: index bookkeeping with a dictionary

```python
x = dict(zip(range(-2, 6), [2, 4, 1, 0, -2, 5, 7, 3]))   # x[n], arrow under the 1 -> starts at n = -2
y = {n: x.get(-n + 3, 0) for n in range(-10, 11)}        # y[n] = x[-n+3]: substitute, don't guess
z = {n: x.get(2 * n + 1, 0) for n in range(-10, 11)}     # z[n] = x[2n+1]
print({n: v for n, v in y.items() if v != 0 or -2 <= n <= 5})
print({n: v for n, v in z.items() if v != 0 or -1 <= n <= 2})
```

```text
{-2: 3, -1: 7, 0: 5, 1: -2, 2: 0, 3: 1, 4: 4, 5: 2}
{-1: 4, 0: 0, 1: 5, 2: 3}
```

A dictionary keyed by $n$ keeps the index with the value — the same bookkeeping you need for `np.convolve`, whose output starts at (start of $x$) + (start of $h$); see [[problems/finite-length-convolution|finite-length convolution]].

## Related

[[1-signals-and-systems/01-digital-signals|Lecture 1]] · [[1-signals-and-systems/02-complex-numbers-and-elementary-signals|Lecture 2]] · [[concepts/discrete-time-signal|discrete-time signal]] · [[concepts/kronecker-delta|Kronecker delta]] · [[concepts/unit-step|unit step]] · [[concepts/time-invariance|time invariance]] · [[homework/hw1|HW1]] · [[demos/convolution-explorer|convolution explorer]].

### Sources for this page

Lecture 2 notes §2 (sequence notation, $\delta[n]$, $u[n]$, $4u[3-n]$); Lecture 3 notes (shift-invariance by substitution); Lecture 4 notes §1.1 (sifting); HW1 #1–#3 and official solutions; FA2025 #3(b). All sequences checked in `verify/hub/toolkit_sketching.py` (26 checks).
