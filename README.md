# t7d-site

Public website for **東方七日祭 ～ Seven Days of Leisure**.

> 非官方东方 Project 二次创作站点，与上海爱丽丝幻乐团 / Team Shanghai Alice 无隶属关系。

## Stack

- Astro 7.3.5
- TypeScript
- static output
- GitHub Pages
- minimal vanilla JavaScript for reader preferences

## Local development

```bash
npm install
npm run dev
```

Build:

```bash
npm run build
```

## Sections

- `/` — work landing page
- `/novel/` — illustrated novel reader
- `/manga/` — manga reader / releases
- `/characters/` — public character gallery
- `/game/` — game landing / downloads / stores
- `/about/` — fan-work notice and project information

## Publish boundary

See [PUBLICATION.md](PUBLICATION.md).

Production source remains in `odango-chan/touhou-seven-days`. This repository receives only approved public release content.

## GitHub Pages

Deployment is handled by GitHub Actions using Astro's official Pages action.

For a public repository, standard GitHub-hosted Actions runners are free under GitHub's current billing rules.