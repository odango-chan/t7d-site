# AGENTS.md

This repository is the public site for **東方七日祭 ～ Seven Days of Leisure**.

## Read first

1. `README.md`
2. `docs/governance/repository-structure.md`
3. `docs/governance/publishing-boundary.md`
4. the relevant domain files under `src/`
5. the tracking GitHub Issue

## Core boundary

Production truth lives in `odango-chan/touhou-seven-days`.

`t7d-site` contains only public-safe release material and presentation code.

Never copy production-only material into this repository.

## Repository owners

- routes: `src/pages/`
- reusable UI: `src/components/`
- public editorial content: `src/content/`
- structured public data: `src/data/`
- web media: `src/assets/`
- browser-side behavior: `src/scripts/`
- shared code: `src/lib/`
- passthrough-only static files: `public/`
- repo tools: `tools/`
- governance / architecture / ADRs: `docs/`

## Rules

- Do not put feature JS/CSS/content/media in `public/`.
- Do not add game binaries to Git.
- Do not edit upstream-owned novel prose directly unless fixing an emergency typo; normal changes land upstream and are re-exported.
- Keep upstream provenance on imported content.
- Do not create `misc/`, `temp/`, `others/`, `final/`, or empty placeholder directories.
- Generated output is never committed.
- New top-level directories require a governance update or ADR.

## Naming

- directories: lowercase kebab-case
- Astro components/layouts: PascalCase
- TS/data modules: kebab-case
- content IDs: stable machine IDs such as `day-01.md`
- manga pages: `page-001.webp`

## Issue workflow

For multi-file or durable work:

1. search existing Issues;
2. create / update an Issue;
3. change the canonical owner file;
4. update governance / ADR if the responsibility model changed;
5. validate build / public boundary;
6. close only after acceptance criteria are met.