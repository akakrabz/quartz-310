# ECE 310 notes site — how to build, preview, and host

This folder is a **Quartz 5** site (`quartz.config.yaml`, `quartz.ts`, `content/`, `quartz/static/demos/`, `quartz/styles/custom.scss`),
built the same way as the ECE 329 site. The notes are plain Markdown with Obsidian-style wikilinks and callouts, so the `content/`
folder also opens directly as an Obsidian vault (the concept map `.canvas` and the problem-family `.base` open there too).

## 1. Build and preview

Requirements: Node ≥ 22, npm ≥ 10.9. `node_modules/` is already installed in this folder (it came with the 329 copy and
contains every plugin this site uses), so no internet is needed for a build.

```bash
cd "~/Nextcloud/Notes/ECE 310/quartz"
npm run install-plugins       # regenerates .quartz/plugins/index.ts — needed once, because this site adds two plugins (see §6)
npx quartz build --serve      # http://localhost:8080  (rebuilds on save)
```

`npx quartz build` alone writes the static site to `public/`. On a fresh clone run `npm ci` first.
If the build fails with `Could not resolve "./.quartz/plugins"`, run `npm run install-plugins`.

## 2. Before hosting

`configuration.baseUrl` in `quartz.config.yaml` is `quartz-310.vops.ch` (host plus any sub-path, no protocol, no trailing slash).
It only affects the sitemap and social-preview URLs. If the site lives under a sub-path (e.g. `example.com/ece310/`),
build with `npx quartz build --baseDir /ece310`.

## 3. Hosting: the one rule your server needs

Quartz emits `page.html` files but links to them **without** the extension (`/concepts/convolution`), and folders are served with
a trailing slash. Your web server must try `$uri`, then `$uri.html`, then `$uri/`:

```nginx
location / {
    try_files $uri $uri.html $uri/ =404;
}
error_page 404 /404.html;
```

Caddy: `try_files {path} {path}.html {path}/ =404`. Opening `public/index.html` from disk (file://) does not work — search, graph,
page previews and the interactive demos load over HTTP.

### Docker / Portainer

`docker-compose.yml` is the same self-contained stack as for 329, pointed at this site: a `builder` container clones
`https://github.com/akakrabz/quartz-310`, checks it every 5 minutes and rebuilds whenever `master` moves; nginx serves the result on
port **8310** with the `try_files` rule above. Point the reverse proxy for `quartz-310.vops.ch` at port 8310.
Publishing a change is `git push`; the site follows within `SYNC_INTERVAL`.

External requests at page load: Google Fonts (theme fonts), jsdelivr (KaTeX CSS) and cdnjs (Mermaid, only on the few pages with a
Mermaid diagram). The demos and drills are fully self-contained.

## 4. Writing conventions (so new pages match)

- One page per lecture in `content/<unit>/NN-slug.md`, in the unit folders `1-signals-and-systems/`, `2-z-transform/` and
  `3-fourier-analysis/` (each with an `index.md` overview); frontmatter `title`, `description`, `tags`, `lecture`.
  Concepts in `content/concepts/` (the concept map is `concepts/concept-map.canvas`), problem families in `content/problems/`
  (frontmatter also `family_frequency`, `typical_points`, `lectures` — the Bases table `problems/exam-problem-families.base`
  reads them), past exams in `content/exams/midterm-1/past-exams/` and `content/exams/midterm-2/past-exams/` (hub:
  `exams/index.md`), homework walkthroughs in `content/homework/`, demo pages in `content/demos/` (the drills page is
  `demos/practice-drills.md`).
- Link with full paths: `[[concepts/region-of-convergence|ROC]]`. Inside tables escape the pipe: `[[page\|text]]`.
- Math: `$…$` inline, `$$…$$` on its own lines (every line prefixed with `> ` inside a callout). Use `\lvert z\rvert` instead of `|z|`
  inside tables. No custom macros. Sequences mark $n = 0$ with `\underset{\uparrow}{…}`; transforms are written in powers of $z^{-1}$
  with the ROC; LCCDEs use Lecture 9's form $y[n] + \sum a_k y[n-k] = \sum b_k x[n-k]$ (the same `b, a` as `scipy.signal.lfilter`).
  Unit 3 writes the DTFT $X_d(\omega)$ and the frequency response $H_d(\omega)$, with $\omega$ in radians per sample plotted on
  $[-\pi,\pi]$, the phase as a principal angle in $[-\pi,\pi]$ and the magnitude never negative; continuous-time transforms are
  $X_c(\Omega)$ or $X_a(\Omega)$, as the exams write them.
- Callouts: the Obsidian types plus this site's `key`, `recipe`, `trap`, `exam`, `intuition`, `derivation` (styled in
  `quartz/styles/custom.scss`). Worked answers go in folded `> [!success]-` callouts so pages work for self-testing.
  Exam material is one layer: on a lecture page, one `exam` callout near the end; citations name term, exam and problem
  (`FA2024 MT2 #4`) and link the exam page.
- Figures: inline `<figure class="ece-fig">…SVG…</figure>` with **no blank lines inside** and **a blank line after**; strokes use
  `currentColor` and the CSS variables `--accent`, `--accent2`, `--hi`, `--muted` so they follow dark mode.
- Demos: standalone HTML in `quartz/static/demos/<name>/index.html`, embedded with `<iframe src="/static/demos/<name>/">` inside
  `<div class="ece-demo">`.
- Python snippets are real: each was run and its output pasted underneath.
- Pages with `draft: true` in the frontmatter (e.g. a homework walkthrough before its due date) are left out of the build by the
  `remove-draft` filter, so published pages must not link to them. For HW6 (due Fri Oct 9, 2026) every link to `homework/hw6`
  and every HW6-labelled answer on a published page is wrapped in a comment marker `%%hw6:<base64 of the text>%%<shown now>%%/hw6%%`
  (Obsidian `%%…%%` comments are stripped by the build). **After the due date run `python3 tools/hw6_release.py`** (add
  `--dry-run` to preview): it restores the links and labels exactly, updates the "published after the due date" wording on the hub
  pages and removes the draft flag; then build or commit as usual.

## 5. Checking a page without building

`python3 tools/check.py content path/to/katex.min.js` validates every wikilink, embed and heading anchor (`.canvas`/`.base` files count
as targets) and compiles every equation with KaTeX in strict mode. Run it before every push; every build has passed it (build 1: 90 pages,
2,827 links, 12,321 equations).

## 6. What's here (build 2, October 2026 — Lectures 1–16)

- **Home**: a learning hub — how to learn with the site (lecture → concept hubs → folded questions → problem families → homework →
  drills and demos → past exams as self-tests), the course map, the conventions table and the callout legend.
- **Lectures 1–16** in three units, each with an overview page: signals and systems (L1–5), the z-transform and LTI systems (L6–11),
  Fourier analysis and frequency response (L12–16, `3-fourier-analysis/`), written from Prof. Snyder's notes and slides.
  Lectures 17 onward (ideal filters, sampling and reconstruction, the DFT and FFT) are to come.
- **36 concept pages** (the graph's hubs, 8 of them for Unit 3) and the **concept map** of Units 1–2 (`concepts/concept-map.canvas`).
- **13 problem families** — 10 from the past Midterm 1 exams, 3 from the past Midterm 2 exams — each with a recipe, traps, every past
  instance and fresh practice problems with folded solutions, listed in a live table by the Bases plugin
  (`problems/exam-problem-families.base`).
- **Exams** (`exams/index.md`, the self-test layer). Midterm 1: a review guide (scope, format, frequency of every problem type, a plan
  for the last day, top traps, the review-lecture problems), a cheat sheet, a true/false bank (43 statements), a system-property bank
  (46 systems) and 7 past exams (FA2025 … FA2019). Midterm 2: an overview (scope, format, what gets asked on each past exam, a
  preparation plan and a Unit 3 formula box), a true/false bank (all 43 statements of the seven exams) and 7 past exams
  (FA2019 … SP2025), typed with folded solutions; the problems on topics after Lecture 16 are marked as later material.
- **Homework walkthroughs** HW1–HW6; HW6's is written but stays a draft until after its due date (Oct 9) — see §4 for `tools/hw6_release.py`.
- A **toolkit** (complex numbers, geometric series, signal transformations, factoring and long division, errata in the course
  materials) and **supplements** (Singer–Munson notes reading guide, notation, course summary, transform tables, the demo notebooks).
- **Interactive**: convolution explorer, pole-zero & ROC explorer, difference-equation simulator, frequency-response explorer, Python
  demos, and autograded randomized **practice drills** (TheorieLearn-style: fresh variants, hints after a wrong answer, worked
  solutions, exam scoring).
- Plugins added to the 329 setup: `@quartz-community/canvas-page` (renders the `.canvas` concept map) and
  `@quartz-community/bases-page` (renders the `.base` table). Both ship in `node_modules/`; run `npm run install-plugins` once.

Every number on the site is recomputed in Python (numpy/scipy) by verification scripts kept outside the repository: about 2,700
scripted checks plus 47,000 randomized checks of the drill generators in build 1, with more for every Unit 3 page in build 2. Slips
found in the official materials are listed on `0-toolkit/05-errata`.
