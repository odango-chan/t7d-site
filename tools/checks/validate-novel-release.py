#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import re
from pathlib import Path
import sys
import tempfile
from urllib.request import urlopen
import yaml


SITE_ROOT = Path(__file__).resolve().parents[2]
DEFAULT_UPSTREAM = SITE_ROOT.parent / "touhou-seven-days"
RAW_BASE = "https://raw.githubusercontent.com/odango-chan/touhou-seven-days/{ref}/{path}"

FRONTMATTER_RE = re.compile(r"^---\n([\s\S]*?)\n---\n?", re.MULTILINE)
HTML_COMMENT_RE = re.compile(r"<!--([\s\S]*?)-->", re.MULTILINE)

UPSTREAM_REPO = "odango-chan/touhou-seven-days"
UPSTREAM_MANIFEST = Path("docs/production/novel/release/manifest.yaml")
SITE_NOVEL_DIR = Path("src/content/novel")

LEAK_TOKENS = (
    "<!--",
    "Canonical:",
    "Characters:",
    "GitHub Issue",
    "PROSE_READY",
    "PROSE_REVIEW_REQUIRED",
    "VOICE_PASS",
    "VOICE_GAP",
    "VOICE_CONFLICT",
    "VOICE_GENERIC",
    "pressure-test",
    "copyedit pass",
)


def fetch_bytes(ref: str, relative_path: str) -> bytes:
    url = RAW_BASE.format(ref=ref, path=relative_path)
    with urlopen(url, timeout=30) as response:
        return response.read()


def materialize_public_upstream(ref: str, root: Path) -> None:
    manifest_rel = str(UPSTREAM_MANIFEST)
    manifest_bytes = fetch_bytes(ref, manifest_rel)
    manifest_path = root / UPSTREAM_MANIFEST
    manifest_path.parent.mkdir(parents=True, exist_ok=True)
    manifest_path.write_bytes(manifest_bytes)

    manifest = yaml.safe_load(manifest_bytes.decode("utf-8"))
    if not isinstance(manifest, dict):
        raise ValueError("downloaded upstream release manifest must be a mapping")

    sources: set[str] = {"docs/production/novel/release/reader-guide.md"}
    for entry in chapter_entries(manifest):
        source = entry.get("source")
        if isinstance(source, str):
            sources.add(source)

    for relative_path in sorted(sources):
        data = fetch_bytes(ref, relative_path)
        target = root / relative_path
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(data)


def git_blob_sha(path: Path) -> str:
    data = path.read_bytes()
    payload = f"blob {len(data)}\0".encode("utf-8") + data
    return hashlib.sha1(payload).hexdigest()


def parse_frontmatter(path: Path) -> tuple[dict, str]:
    text = path.read_text(encoding="utf-8").replace("\r\n", "\n")
    match = FRONTMATTER_RE.match(text)
    if not match:
        raise ValueError(f"{path}: missing YAML frontmatter")
    data = yaml.safe_load(match.group(1))
    if not isinstance(data, dict):
        raise ValueError(f"{path}: frontmatter must be a mapping")
    return data, text[match.end():].strip()


def normalize_upstream_body(path: Path, kind: str) -> str:
    text = path.read_text(encoding="utf-8").replace("\r\n", "\n")
    text = HTML_COMMENT_RE.sub("", text).strip()
    lines = text.splitlines()

    if kind == "chapter":
        while lines and not lines[0].strip():
            lines.pop(0)
        if not lines or not lines[0].startswith("# "):
            raise ValueError(f"{path}: expected book H1")
        lines.pop(0)

        while lines and not lines[0].strip():
            lines.pop(0)
        if not lines or not lines[0].startswith("## "):
            raise ValueError(f"{path}: expected chapter H2")
        lines.pop(0)
    elif kind == "guide":
        while lines and not lines[0].strip():
            lines.pop(0)
        if not lines or not lines[0].startswith("# "):
            raise ValueError(f"{path}: expected guide H1")
        lines.pop(0)
    else:
        raise ValueError(f"unknown source kind: {kind}")

    return "\n".join(lines).strip()


def validate_public_body(label: str, body: str) -> list[str]:
    errors: list[str] = []
    for token in LEAK_TOKENS:
        if token in body:
            errors.append(f"{label}: production-only token leaked into public prose: {token!r}")
    return errors


def chapter_entries(manifest: dict) -> list[dict]:
    assembly = manifest.get("assembly")
    if not isinstance(assembly, list):
        raise ValueError("upstream release manifest: assembly must be a list")
    return [entry for entry in assembly if isinstance(entry, dict) and entry.get("kind") == "chapter"]


def validate(upstream_root: Path) -> list[str]:
    errors: list[str] = []

    manifest_path = upstream_root / UPSTREAM_MANIFEST
    if not manifest_path.is_file():
        return [f"missing upstream release manifest: {manifest_path}"]

    manifest = yaml.safe_load(manifest_path.read_text(encoding="utf-8"))
    if not isinstance(manifest, dict):
        return ["upstream release manifest must be a mapping"]

    chapters = chapter_entries(manifest)
    expected_ids = [
        "day-01",
        "day-02",
        "day-03",
        "day-04",
        "day-05",
        "day-06",
        "day-07",
        "extra-day-08",
    ]
    manifest_ids = [entry.get("id") for entry in chapters]
    if manifest_ids != expected_ids:
        errors.append(
            "upstream chapter order drift: "
            f"expected {expected_ids}, got {manifest_ids}"
        )

    seen_orders: set[int] = set()

    for expected_order, entry in enumerate(chapters, start=1):
        chapter_id = entry.get("id")
        source = entry.get("source")
        if not isinstance(chapter_id, str) or not isinstance(source, str):
            errors.append(f"manifest chapter entry malformed: {entry!r}")
            continue

        upstream_path = upstream_root / source
        site_path = SITE_ROOT / SITE_NOVEL_DIR / f"{chapter_id}.md"
        if not upstream_path.is_file():
            errors.append(f"{chapter_id}: upstream source missing: {source}")
            continue
        if not site_path.is_file():
            errors.append(f"{chapter_id}: site release copy missing: {site_path.relative_to(SITE_ROOT)}")
            continue

        try:
            fm, site_body = parse_frontmatter(site_path)
        except Exception as exc:
            errors.append(str(exc))
            continue

        required = {
            "title",
            "slug",
            "order",
            "section",
            "upstreamRepo",
            "upstreamPath",
            "upstreamSha",
            "releaseStatus",
        }
        missing = required - set(fm)
        if missing:
            errors.append(f"{chapter_id}: missing frontmatter keys: {sorted(missing)}")

        if fm.get("slug") != chapter_id:
            errors.append(f"{chapter_id}: slug must equal chapter id")
        if fm.get("section") != "novel":
            errors.append(f"{chapter_id}: section must be novel")
        if fm.get("order") != expected_order:
            errors.append(
                f"{chapter_id}: order must be {expected_order}, got {fm.get('order')!r}"
            )
        if isinstance(fm.get("order"), int):
            if fm["order"] in seen_orders:
                errors.append(f"{chapter_id}: duplicate order {fm['order']}")
            seen_orders.add(fm["order"])

        if fm.get("upstreamRepo") != UPSTREAM_REPO:
            errors.append(f"{chapter_id}: upstreamRepo drift")
        if fm.get("upstreamPath") != source:
            errors.append(
                f"{chapter_id}: upstreamPath drift: "
                f"{fm.get('upstreamPath')!r} != {source!r}"
            )

        actual_sha = git_blob_sha(upstream_path)
        if fm.get("upstreamSha") != actual_sha:
            errors.append(
                f"{chapter_id}: stale upstreamSha "
                f"{fm.get('upstreamSha')!r} != {actual_sha!r}"
            )

        try:
            upstream_body = normalize_upstream_body(upstream_path, "chapter")
        except Exception as exc:
            errors.append(str(exc))
            continue

        if site_body != upstream_body:
            errors.append(
                f"{chapter_id}: public prose differs from upstream release source "
                "after stripping production wrapper"
            )

        errors.extend(validate_public_body(chapter_id, site_body))

    if seen_orders != set(range(1, 9)):
        errors.append(f"public chapter orders must be exactly 1..8, got {sorted(seen_orders)}")

    # Reader guide is part of the release contract but not a chapter.
    upstream_guide_rel = Path("docs/production/novel/release/reader-guide.md")
    upstream_guide = upstream_root / upstream_guide_rel
    site_guide = SITE_ROOT / SITE_NOVEL_DIR / "reader-guide.md"

    if not upstream_guide.is_file():
        errors.append("reader-guide: upstream source missing")
    elif not site_guide.is_file():
        errors.append("reader-guide: site release copy missing")
    else:
        try:
            fm, site_body = parse_frontmatter(site_guide)
            if fm.get("section") != "guide":
                errors.append("reader-guide: section must be guide")
            if fm.get("slug") != "guide":
                errors.append("reader-guide: slug must be guide")
            if fm.get("upstreamRepo") != UPSTREAM_REPO:
                errors.append("reader-guide: upstreamRepo drift")
            if fm.get("upstreamPath") != str(upstream_guide_rel):
                errors.append("reader-guide: upstreamPath drift")

            actual_sha = git_blob_sha(upstream_guide)
            if fm.get("upstreamSha") != actual_sha:
                errors.append(
                    f"reader-guide: stale upstreamSha "
                    f"{fm.get('upstreamSha')!r} != {actual_sha!r}"
                )

            upstream_body = normalize_upstream_body(upstream_guide, "guide")
            if site_body != upstream_body:
                errors.append(
                    "reader-guide: public prose differs from upstream release source "
                    "after stripping H1"
                )
            errors.extend(validate_public_body("reader-guide", site_body))
        except Exception as exc:
            errors.append(str(exc))

    return errors


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--upstream-root",
        type=Path,
        help="Path to a local odango-chan/touhou-seven-days checkout",
    )
    parser.add_argument(
        "--fetch-upstream",
        action="store_true",
        help="Fetch the public upstream release contract from raw.githubusercontent.com",
    )
    parser.add_argument(
        "--upstream-ref",
        default="main",
        help="Public upstream ref used with --fetch-upstream (default: main)",
    )
    args = parser.parse_args()

    if args.upstream_root and args.fetch_upstream:
        parser.error("choose either --upstream-root or --fetch-upstream")

    if args.fetch_upstream:
        with tempfile.TemporaryDirectory(prefix="t7d-upstream-") as temp:
            upstream_root = Path(temp)
            try:
                materialize_public_upstream(args.upstream_ref, upstream_root)
            except Exception as exc:
                print(f"Novel release contract FAILED\n- unable to fetch upstream: {exc}")
                return 1
            errors = validate(upstream_root)
    else:
        upstream_root = (args.upstream_root or DEFAULT_UPSTREAM).resolve()
        errors = validate(upstream_root)

    if errors:
        print("Novel release contract FAILED")
        for error in errors:
            print(f"- {error}")
        return 1

    print("Novel release contract PASS: 8 chapters + reader guide are in sync")
    return 0


if __name__ == "__main__":
    sys.exit(main())
