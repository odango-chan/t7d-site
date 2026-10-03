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

Normal site presentation media stays under `src/assets/`.

### Stable press-download exception

`public/press/` is reserved only for **Accepted public press exports that require stable, non-hashed external download URLs**.

Allowed examples:

- approved Logo PNG / SVG;
- approved Key Visual Web export;
- approved poster export;
- approved social / OG press derivative.

Not allowed:

- production previews;
- reference sheets;
- prompts;
- QA screenshots;
- source masters;
- working files;
- unaccepted generated art.

Every press file must be represented in `src/data/releases/press-assets.ts` with upstream provenance.

Do not use `public/press/` as a general media dump.

Working-source files and production masters remain upstream.

Working-source files and production masters remain upstream.

If public media eventually makes this repository too large, move heavy delivery assets to object storage / CDN instead of turning this repository into an archive.
## Provenance validation direction

The public site validates only facts it owns locally:

- public release files exist;
- provenance metadata is structurally valid;
- chapter ordering is valid;
- production comments / QA metadata do not leak.

For upstream-owned prose, **freshness is validated from the production repository toward this public repository**.

Do not give `t7d-site` credentials merely so its CI can read private production sources.

```text
touhou-seven-days
  ├─ owns current Release Draft
  ├─ computes current Git blob SHA
  ├─ checks t7d-site release copy
  ↓
t7d-site
  ├─ owns public presentation
  └─ validates its own public boundary
```

This keeps the dependency one-way and prevents the public presentation repository from becoming coupled to production-repository permissions.
