# Publishing Boundary

`t7d-site` is the public release surface for **東方七日祭 ～ Seven Days of Leisure**.

Production source of truth:

- `odango-chan/touhou-seven-days`

## Public material allowed here

- approved release prose;
- accepted manga Web pages;
- accepted character portraits;
- accepted novel illustrations;
- public game screenshots / trailers / store metadata;
- release notes;
- download and store links;
- public fan-work notice.

## Production material forbidden here

- prompts;
- internal production documents;
- Story / Character draft discussions;
- gap ledgers;
- QA history;
- issue-only planning;
- unpublished plot;
- unapproved art;
- high-resolution production-only source images;
- game signing material;
- secrets.

## Imported content provenance

Imported release material must retain provenance where practical:

```yaml
upstreamRepo:
upstreamPath:
upstreamSha:
releaseStatus:
```

The public copy is a release artifact, not the editing owner.

```text
touhou-seven-days
  ↓ review / acceptance
public export
  ↓
t7d-site
```

Emergency typo fixes made in `t7d-site` must be reconciled upstream before the next export.

## Game distribution

Do not commit native installation packages into this repository.

Use GitHub Releases, App Store / TestFlight, Android stores, HarmonyOS distribution, or other approved distribution services.

The site owns presentation, release metadata and links.

## Media boundary

Only Web-ready accepted assets belong in this repository.

Working-source files and production masters remain upstream.

If public media eventually makes this repository too large, move heavy delivery assets to object storage / CDN instead of turning this repository into an archive.