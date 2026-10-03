#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path
import re
import sys
import yaml


ROOT = Path(__file__).resolve().parents[2]
NOVEL_DIR = ROOT / "src/content/novel"

EXPECTED = [
    ("day-01", 1, "docs/production/novel/chapters/day-01.md"),
    ("day-02", 2, "docs/production/novel/chapters/day-02.md"),
    ("day-03", 3, "docs/production/novel/chapters/day-03.md"),
    ("day-04", 4, "docs/production/novel/chapters/day-04.md"),
    ("day-05", 5, "docs/production/novel/chapters/day-05.md"),
    ("day-06", 6, "docs/production/novel/chapters/day-06.md"),
    ("day-07", 7, "docs/production/novel/chapters/day-07.md"),
    ("extra-day-08", 8, "docs/production/novel/chapters/extra-day-08.md"),
]

FRONTMATTER_RE = re.compile(r"^---\n([\s\S]*?)\n---\n?", re.MULTILINE)
SHA_RE = re.compile(r"^[0-9a-f]{40}$")

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

UPSTREAM_REPO = "odango-chan/touhou-seven-days"


def parse_frontmatter(path: Path) -> tuple[dict, str]:
    text = path.read_text(encoding="utf-8").replace("\r\n", "\n")
    match = FRONTMATTER_RE.match(text)
    if not match:
        raise ValueError(f"{path.relative_to(ROOT)}: missing YAML frontmatter")
    data = yaml.safe_load(match.group(1))
    if not isinstance(data, dict):
        raise ValueError(f"{path.relative_to(ROOT)}: frontmatter must be a mapping")
    return data, text[match.end():].strip()


def validate_body(label: str, body: str) -> list[str]:
    errors: list[str] = []
    if not body:
        errors.append(f"{label}: public body must not be empty")
    for token in LEAK_TOKENS:
        if token in body:
            errors.append(f"{label}: production-only token leaked: {token!r}")
    return errors


def validate_release_copy(
    path: Path,
    *,
    slug: str,
    section: str,
    upstream_path: str,
    order: int | None,
) -> list[str]:
    errors: list[str] = []

    if not path.is_file():
        return [f"missing public release copy: {path.relative_to(ROOT)}"]

    try:
        fm, body = parse_frontmatter(path)
    except Exception as exc:
        return [str(exc)]

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
        errors.append(f"{slug}: missing frontmatter keys: {sorted(missing)}")

    if fm.get("slug") != slug:
        errors.append(f"{slug}: slug drift: {fm.get('slug')!r}")
    if fm.get("section") != section:
        errors.append(f"{slug}: section must be {section!r}")

    if order is not None and fm.get("order") != order:
        errors.append(f"{slug}: order must be {order}, got {fm.get('order')!r}")

    if fm.get("upstreamRepo") != UPSTREAM_REPO:
        errors.append(f"{slug}: upstreamRepo drift")
    if fm.get("upstreamPath") != upstream_path:
        errors.append(
            f"{slug}: upstreamPath drift: "
            f"{fm.get('upstreamPath')!r} != {upstream_path!r}"
        )

    sha = fm.get("upstreamSha")
    if not isinstance(sha, str) or not SHA_RE.fullmatch(sha):
        errors.append(f"{slug}: upstreamSha must be a 40-character lowercase Git blob SHA")

    status = fm.get("releaseStatus")
    if not isinstance(status, str) or not status.strip():
        errors.append(f"{slug}: releaseStatus must be non-empty")

    errors.extend(validate_body(slug, body))
    return errors


def main() -> int:
    errors: list[str] = []
    seen_orders: set[int] = set()

    for slug, order, upstream_path in EXPECTED:
        path = NOVEL_DIR / f"{slug}.md"
        errors.extend(
            validate_release_copy(
                path,
                slug=slug,
                section="novel",
                upstream_path=upstream_path,
                order=order,
            )
        )

        if path.is_file():
            try:
                fm, _ = parse_frontmatter(path)
                value = fm.get("order")
                if isinstance(value, int):
                    if value in seen_orders:
                        errors.append(f"{slug}: duplicate public chapter order {value}")
                    seen_orders.add(value)
            except Exception:
                pass

    if seen_orders != set(range(1, 9)):
        errors.append(f"public chapter orders must be exactly 1..8, got {sorted(seen_orders)}")

    errors.extend(
        validate_release_copy(
            NOVEL_DIR / "reader-guide.md",
            slug="guide",
            section="guide",
            upstream_path="docs/production/novel/release/reader-guide.md",
            order=0,
        )
    )

    expected_files = {f"{slug}.md" for slug, _, _ in EXPECTED} | {"reader-guide.md"}
    actual_files = {p.name for p in NOVEL_DIR.glob("*.md")}
    unexpected = actual_files - expected_files
    if unexpected:
        errors.append(
            "unexpected novel content file(s) require explicit release routing: "
            + ", ".join(sorted(unexpected))
        )

    if errors:
        print("Novel public release contract FAILED")
        for error in errors:
            print(f"- {error}")
        return 1

    print(
        "Novel public release contract PASS: "
        "8 chapters + reader guide have safe provenance metadata and no production leakage"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
