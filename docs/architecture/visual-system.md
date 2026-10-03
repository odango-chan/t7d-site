# Visual System — Seven-Day Editorial

**Issue:** #3  
**Status:** Accepted baseline

## Direction

Public-site visual language:

> **七日文库 / Seven-Day Editorial**

The goal is a restrained doujin-book / literary-edition feeling rather than a generic web landing page.

## Principles

- warm paper base;
- near-black ink typography;
- vermilion only as a small editorial mark;
- Mincho / Song-style serif for display and reading;
- sans-serif only for metadata and controls;
- asymmetry, whitespace and hairlines over cards and shadows;
- no fake calligraphy;
- no sakura / torii / red-black-gold cliché theming;
- no glossy game-key-visual treatment;
- illustration placeholders look like reserved print plates, not developer boxes.

## Core tokens

Light:

- paper: `#f1ede4`
- sheet: `#f8f5ee`
- ink: `#282621`
- secondary ink: `#69635b`
- hairline: `#c9c0b3`
- vermilion: `#a8463f`

Dark mode remains charcoal / warm paper-in-night rather than pure black.

## Typography

Primary serif stack:

`Yu Mincho → Hiragino Mincho ProN → Noto Serif CJK JP → Source Han Serif SC → Songti SC`

Metadata / controls:

`Hiragino Sans → Yu Gothic → Noto Sans CJK SC → system-ui`

## Composition

### Home

- vertical work title;
- epigraph as primary emotional entry;
- reserved cover plate;
- work catalogue as ruled editorial rows;
- no card grid.

### Section index

- large title;
- small red section marker;
- content list separated by hairlines.

### Novel reader

- no floating paper card / drop shadow;
- title separated by editorial rule;
- controls visually secondary;
- body line-height around 2.0;
- illustration reservations use print-plate language;
- wide illustrations may temporarily break the text measure.

## Media

When real art lands, the design should become quieter rather than more decorated.

Do not add ornamental UI around accepted art unless the art itself requires framing.

## Future domains

Manga / Characters / Game should reuse these tokens and editorial hierarchy.

They may have domain-specific layouts, but must not invent an unrelated color system or card language without an ADR.
