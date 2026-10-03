# Home & Promotion Architecture

Status: Draft / implementation-ready
Tracking: #7
Upstream: odango-chan/touhou-seven-days#72

## Purpose
The home page is the public game landing page, not a grid of links. In the first seconds it must establish the title and mood, explain the seven-day premise without solving it, and offer clear paths into Game, Characters, Manga, and Novel.

## Publishing boundary
Promotional art is produced upstream. This site accepts only approved public-safe Key Visuals, Logo exports, posters, character art, screenshots, trailers, and release metadata.
Without an Accepted KV, the home page must still work through typography, paper/ink texture, spacing, and deterministic layout. Never use temporary generated art as if it were final.

## Home information architecture
### 01 Hero
- 東方七日祭
- Seven Days of Leisure
- one spoiler-free premise line
- primary CTA: current playable/release entry when one exists
- secondary CTA: learn about the seven days
- Accepted KV when available

Desktop uses landscape art; mobile prefers a portrait composition rather than a hard crop.

### 02 Premise
Only answer what it feels like: 幻想乡忽然多出了七日闲暇。没有人等着谁来宣布，大家已经各自过起假来。
Do not answer why.

### 03 Seven Days
Use Day 1 → Day 7 as a narrative scrolling rhythm, not a plot index. Each day may expose only the day marker, one daily-life atmosphere line, and one public-safe visual anchor.
Never expose boss progression, Final identity, hidden mechanism, or Extra explanation.

### 04 Game
Explain the vertical danmaku experience, current release state/platforms, accepted gameplay media, and a Game CTA. Do not expose engine/repository implementation details.

### 05 Characters
Show only a small representative cast: name, one public identity/personality line, public-safe image, and Characters CTA. Full profiles stay under /characters/.

### 06 Read
Manga and Novel sit together but report their real release states independently. Show current readable state, latest public chapter, and one CTA each.

### 07 Latest / Release
Connect News, store, and download/release entry points. Do not show a fake Download button before a real release exists.

### 08 Footer
Keep the unofficial Touhou Project fan-work notice and About link.

## Visual behavior
Keep the current editorial direction: warm paper, ink, restrained vermilion accents, whitespace, quiet asymmetry. A future KV must not turn the site into a glossy mobile-game landing page.
Preferred rhythm: large image → quiet prose → seven-day rhythm → gameplay → people → reading → release. Avoid a long run of same-size cards.

## Responsive rules
Desktop may use a wide hero and broader Seven Days rhythm. Mobile uses portrait hero art, keeps titles off complex faces, converts Seven Days to a vertical flow, and keeps core content usable without animation.

## Site asset contract
Release copies should use stable semantic names:

    src/assets/promotion/hero-landscape.*
    src/assets/promotion/hero-portrait.*
    src/assets/promotion/poster-main.*
    src/assets/promotion/social-og.*

Keep upstream provenance for imported assets.

## SEO / social
Provide title, description, canonical URL, OG title, OG description, OG image, and fan-work wording where appropriate. OG art is an explicitly reviewed 1.91:1 derivative, not a browser screenshot.

## Acceptance
Before final KV: desktop/mobile home is complete, no broken image, no production-only data, no placeholder presented as official art.
After KV acceptance: syncing presentation assets is sufficient; IA does not need redesign, and all existing Characters/Manga/Novel/Game pages remain second-level destinations.