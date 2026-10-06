from __future__ import annotations

import base64
import hashlib
from pathlib import Path

root = Path(".site-tmp/shishi-cover")
parts: list[str] = []

for name in ("chunk-00", "chunk-01", "chunk-02"):
    parts.append((root / name).read_text(encoding="utf-8"))

parts.append((root / "chunk-03.rev").read_text(encoding="utf-8")[::-1])

for name in (
    "chunk-04.wrap",
    "chunk-05.wrap",
    "chunk-06.wrap",
    "chunk-07a.wrap",
    "chunk-07b.wrap",
    "chunk-08.wrap",
):
    lines = (root / name).read_text(encoding="utf-8").splitlines()
    parts.append("".join(line[2:] if line.startswith("x:") else line for line in lines))

raw = base64.b64decode("".join(parts), validate=True)
assert len(raw) == 2933483, len(raw)

target = Path("public/media/music/covers/echoes-of-shishi.png")
target.parent.mkdir(parents=True, exist_ok=True)
target.write_bytes(raw)

blob = b"blob " + str(len(raw)).encode() + b"\0" + raw
assert hashlib.sha1(blob).hexdigest() == "0da540065450d0602def1ef6e3f0d0b2f8c808e9"
print(target)
