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

- One page per lecture in `content/<unit>/NN-slug.md`; frontmatter `title`, `description`, `tags`, `lecture`.
  Concepts in `content/concepts/`, exam problem families in `content/problems/` (frontmatter also `family_frequency`,
  `typical_points`, `lectures` — the Bases table reads them), past exams in `content/0-midterm-1/past-exams/`.
- Link with full paths: `[[concepts/region-of-convergence|ROC]]`. Inside tables escape the pipe: `[[page\|text]]`.
- Math: `$…$` inline, `$$…$$` on its own lines (every line prefixed with `> ` inside a callout). Use `\lvert z\rvert` instead of `|z|`
  inside tables. No custom macros. Sequences mark $n = 0$ with `\underset{\uparrow}{…}`; transforms are written in powers of $z^{-1}$
  with the ROC; LCCDEs use Lecture 9's form $y[n] + \sum a_k y[n-k] = \sum b_k x[n-k]$ (the same `b, a` as `scipy.signal.lfilter`).
- Callouts: the Obsidian types plus this site's `key`, `recipe`, `trap`, `exam`, `intuition`, `derivation` (styled in
  `quartz/styles/custom.scss`). Worked answers go in folded `> [!success]-` callouts so pages work for self-testing.
- Figures: inline `<figure class="ece-fig">…SVG…</figure>` with **no blank lines inside** and **a blank line after**; strokes use
  `currentColor` and the CSS variables `--accent`, `--accent2`, `--hi`, `--muted` so they follow dark mode.
- Demos: standalone HTML in `quartz/static/demos/<name>/index.html`, embedded with `<iframe src="/static/demos/<name>/">` inside
  `<div class="ece-demo">`.
- Python snippets are real: each was run and its output pasted underneath.

## 5. Checking a page without building

`python3 tools/check.py content path/to/katex.min.js` validates every wikilink, embed and heading anchor (`.canvas`/`.base` files count
as targets) and compiles every equation with KaTeX in strict mode. The delivered site passes it: 90 pages, 2,827 links, 12,321 equations.

## 6. What's here (build 1, 2026-09-30 — Midterm 1 scope: Lectures 1–11, HW1–HW4, no DTFT)

- **Home** with the course map, conventions and callout legend; **Midterm 1 survival guide** (scope, format, frequency of every
  problem type, a plan for exam day, top traps, the review-lecture problems); **cheat sheet** (what to put on the handwritten page);
  **concept map** (`0-midterm-1/concept-map.canvas`).
- **Lectures 1–11** in two units (signals and systems; the z-transform and LTI systems), written from Prof. Snyder's notes and slides;
  Lectures 12–14 outlined as "beyond Midterm 1".
- **28 concept pages** (the graph's hubs) and **10 exam problem families** (recipe, traps, every past instance, fresh practice problems
  with folded solutions), listed in a live table by the Bases plugin (`problems/exam-problem-families.base`).
- **7 past Midterm 1 exams** (FA2025 … FA2019) typed out with folded solutions, a **true/false bank** (43 statements) and a
  **system-property bank** (46 systems).
- **HW1–HW4 walkthroughs**, a **toolkit** (complex numbers, geometric series, signal transformations, factoring and long division,
  errata in the course materials) and **supplements** (Singer–Munson notes reading guide, notation, course summary, transform tables,
  the demo notebooks).
- **Interactive**: convolution explorer, pole-zero & ROC explorer, difference-equation simulator, and autograded randomized
  **practice drills** (7 drill types, TheorieLearn-style: fresh variants, hints after a wrong answer, worked solutions, exam scoring).
- Plugins added to the 329 setup: `@quartz-community/canvas-page` (renders the `.canvas` concept map) and
  `@quartz-community/bases-page` (renders the `.base` table). Both ship in `node_modules/`; run `npm run install-plugins` once.

Every number on the site was recomputed in Python (numpy/scipy: `np.convolve`, `lfilter`, `residuez`, truncated z-transform sums
inside the ROC) — about 2,700 scripted checks, plus 47,000 randomized checks of the drill generators. Slips found in the official
materials are listed on `0-toolkit/05-errata`.
