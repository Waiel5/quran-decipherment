#!/usr/bin/env python3
"""
linkify_findings.py — Convert plain-text references in findings markdown
files into Obsidian wikilinks so the corpus forms a navigable graph.

USAGE:
    python3 linkify_findings.py            # dry-run, prints stats only
    python3 linkify_findings.py --apply    # writes changes to disk

WHAT IT DOES:
    1. Scans /findings/phase-b-hypotheses/, /findings/cross-finding/, plus
       /MASTER-FINDINGS-LEDGER.md.
    2. Builds a map of finding-id -> filename-without-extension by
       inspecting every h-new-*.md and cross-finding-*.md file.
    3. For each markdown file, replaces plain-text references such as:
         H-NEW-580          -> [[h-new-580-five-factor-regression|H-NEW-580]]
         H-NEW-127.10       -> [[h-new-127-10-pooled-within-phase-rank|H-NEW-127.10]]
         cross-finding-024  -> [[cross-finding-024-five-factor-cohesion-model|cross-finding-024]]
       Display text (after the pipe) preserves the original casing /
       punctuation so the rendered prose is unchanged.
    4. Skips matches that are already inside a wikilink, inside a code
       block, or inside YAML front-matter values that look like file
       references.
    5. Writes a list of orphan references (mentions with no matching
       file) to /findings/ORPHAN-REFERENCES.md.

REVERSAL:
    All edits are pure regex insertions. To revert run:
        rg -l "\\[\\[h-new-" findings/ MASTER-FINDINGS-LEDGER.md \\
          | xargs sed -i '' -E "s/\\[\\[(h-new-[^|]+)\\|([^]]+)\\]\\]/\\2/g; s/\\[\\[(cross-finding-[^|]+)\\|([^]]+)\\]\\]/\\2/g"
"""

from __future__ import annotations

import argparse
import os
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path("/Users/grey/Downloads/quran")
FINDINGS_DIR = ROOT / "findings"
PHASE_B = FINDINGS_DIR / "phase-b-hypotheses"
CROSS_DIR = FINDINGS_DIR / "cross-finding"
LEDGER = ROOT / "MASTER-FINDINGS-LEDGER.md"
ORPHAN_REPORT = FINDINGS_DIR / "ORPHAN-REFERENCES.md"


def discover_finding_files() -> tuple[dict[str, str], dict[str, list[str]]]:
    """Return ({canonical-id: filename-stem}, collisions) mapping.

    canonical-id examples:
        h-new-580
        h-new-111b
        h-new-127-10
        cross-finding-024
    """
    mapping: dict[str, str] = {}
    collisions: dict[str, list[str]] = defaultdict(list)

    # Match the canonical id at the start of the stem.
    # A canonical id is one of:
    #   h-new-<digits>
    #   h-new-<digits><letter>          (e.g. h-new-111b)
    #   h-new-<digits>-<digits>         (e.g. h-new-127-10)
    # The id terminates at end-of-stem or before a non-id character
    # (typically '-' followed by a non-digit slug word).
    # canonical id forms:
    #   h-new-236
    #   h-new-111b               (single letter suffix)
    #   h-new-127-10             (sub-number)
    #   h-new-236-1a             (sub-number + letter)
    #   h-new-44-2-1             (sub-sub-number)
    HNEW_FILE_RE = re.compile(
        r"^(h-new-\d+(?:[a-z](?![a-z]))?"
        r"(?:-\d+(?:[a-z](?![a-z]))?)?"
        r"(?:-\d+(?:[a-z](?![a-z]))?)?"
        r")(?=-|$)"
    )
    CROSS_FILE_RE = re.compile(r"^(cross-finding-\d+)(?:-|$)")

    search_dirs = [PHASE_B, CROSS_DIR, FINDINGS_DIR / "phase-c-structures"]
    for d in search_dirs:
        if not d.exists():
            continue
        for md in d.iterdir():
            if md.suffix != ".md":
                continue
            stem = md.stem
            if stem.endswith("-prereg"):
                continue

            m = HNEW_FILE_RE.match(stem)
            if m:
                canon = m.group(1)
                # Skip prereg-style backfill files — prefer the
                # primary writeup with the descriptive slug.
                is_secondary = (
                    "prereg" in stem
                    or stem.endswith("-rerun")
                    or stem.endswith("-mst-analysis")
                )
                if canon in mapping:
                    collisions[canon].append(stem)
                    existing = mapping[canon]
                    existing_secondary = (
                        "prereg" in existing
                        or existing.endswith("-rerun")
                        or existing.endswith("-mst-analysis")
                    )
                    # Prefer non-secondary; if both are secondary or
                    # both primary, prefer the shorter (more canonical) stem.
                    if existing_secondary and not is_secondary:
                        mapping[canon] = stem
                    elif (not existing_secondary) == (not is_secondary):
                        if len(stem) < len(existing):
                            mapping[canon] = stem
                else:
                    mapping[canon] = stem
                continue

            m = CROSS_FILE_RE.match(stem)
            if m:
                canon = m.group(1)
                if canon in mapping:
                    collisions[canon].append(stem)
                    existing = mapping[canon]
                    # Prefer file living in CROSS_DIR over phase-b copy.
                    if (CROSS_DIR / f"{stem}.md").exists() and not (
                        CROSS_DIR / f"{existing}.md"
                    ).exists():
                        mapping[canon] = stem
                else:
                    mapping[canon] = stem
    return mapping, collisions


# Regex for plain-text references.
#   group "orig" = original-cased text exactly as it appeared
#   group "num"  = number portion (with optional sub-number / letter)
# Sub-number can be ".N", "-N", or a single trailing letter (a-h).
# We deliberately do not match ids inside an existing wikilink.
HNEW_RE = re.compile(
    r"(?P<orig>(?<![\w/\[-])"
    r"[Hh]-[Nn][Ee][Ww]-"
    r"(?P<num>\d+[A-Ha-h]?(?:[.\-]\d+[A-Ha-h]?)?)"
    r")(?![\w])"
)
CROSS_RE = re.compile(
    r"(?P<orig>(?<![\w/\[-])[Cc]ross-[Ff]inding-(?P<num>\d+))(?![\w])"
)


def canonical_hnew(num_token: str) -> str:
    """Convert reference number-token (e.g. '127.10', '111B', '34.1')
    into a canonical filename-prefix id (e.g. 'h-new-127-10', 'h-new-111b',
    'h-new-34-1')."""
    s = num_token.lower().replace(".", "-")
    return f"h-new-{s}"


def already_linked(text: str, start: int) -> bool:
    """Return True if position 'start' is already inside [[...]]."""
    # Look back for [[ before any ]] or newline
    open_idx = text.rfind("[[", max(0, start - 200), start)
    if open_idx == -1:
        return False
    close_idx = text.rfind("]]", open_idx, start)
    if close_idx > open_idx:
        return False
    # There's an unclosed [[ before us → we're inside a wikilink
    return True


def in_code_block(lines_before: list[str]) -> bool:
    """Return True if we're currently inside a fenced code block."""
    fences = sum(1 for ln in lines_before if ln.lstrip().startswith("```"))
    return fences % 2 == 1


def linkify_text(
    text: str,
    mapping: dict[str, str],
    orphan_counter: Counter,
) -> tuple[str, int]:
    """Return (new_text, n_links_added)."""
    lines = text.split("\n")
    out_lines: list[str] = []
    n_added = 0

    # Detect YAML front-matter range (only if file STARTS with '---')
    yaml_end = -1
    if lines and lines[0].strip() == "---":
        for j in range(1, len(lines)):
            if lines[j].strip() == "---":
                yaml_end = j
                break

    for i, line in enumerate(lines):
        if i <= yaml_end:
            # Inside YAML front-matter — skip linkification to avoid
            # breaking parsers that don't understand wikilinks.
            out_lines.append(line)
            continue
        if in_code_block(out_lines):
            out_lines.append(line)
            continue

        new_line = line

        def replace_hnew(m: re.Match) -> str:
            nonlocal n_added
            orig = m.group("orig")
            num = m.group("num")
            canon = canonical_hnew(num)
            if already_linked(new_line, m.start()):
                return orig
            stem = mapping.get(canon)
            if stem is None:
                # Normalized key for orphan counting (e.g. H-NEW-127.10)
                orphan_counter[f"H-NEW-{num.upper()}"] += 1
                return orig
            n_added += 1
            return f"[[{stem}|{orig}]]"

        def replace_cross(m: re.Match) -> str:
            nonlocal n_added
            orig = m.group("orig")
            num = m.group("num")
            canon = f"cross-finding-{num}"
            if already_linked(new_line, m.start()):
                return orig
            stem = mapping.get(canon)
            if stem is None:
                orphan_counter[canon] += 1
                return orig
            n_added += 1
            return f"[[{stem}|{orig}]]"

        # Replace cross-finding first (more specific), then H-NEW
        new_line = CROSS_RE.sub(replace_cross, new_line)
        # Re-run HNEW pass on the (possibly already-modified) line
        new_line = HNEW_RE.sub(replace_hnew, new_line)
        out_lines.append(new_line)

    return "\n".join(out_lines), n_added


def find_target_files() -> list[Path]:
    targets: list[Path] = []
    if LEDGER.exists():
        targets.append(LEDGER)
    for d in [PHASE_B, CROSS_DIR]:
        if not d.exists():
            continue
        for md in sorted(d.iterdir()):
            if md.suffix == ".md":
                targets.append(md)
    return targets


def write_orphan_report(orphans: Counter, n_files: int) -> None:
    if not orphans:
        body = "_No orphan references detected._\n"
    else:
        rows = sorted(orphans.items(), key=lambda kv: (-kv[1], kv[0]))
        lines = [
            "| Reference | Mentions |",
            "|---|---|",
        ]
        for ref, count in rows:
            lines.append(f"| `{ref}` | {count} |")
        body = "\n".join(lines) + "\n"

    content = f"""---
document: Orphan References Report
generated_by: scripts/linkify_findings.py
date: 2026-04-28
scope: phase-b-hypotheses + cross-finding + MASTER-FINDINGS-LEDGER.md
---

# Orphan References

References mentioned in findings prose but with **no matching file** in
`findings/phase-b-hypotheses/`, `findings/cross-finding/`, or
`findings/phase-c-structures/`. These are plain-text identifiers that
could not be linkified into Obsidian wikilinks.

Most likely causes:

1. The finding was executed but never written up as its own `.md` file.
2. The reference is inside an aggregate analysis (e.g. ledger section
   reporting many bare IDs from a script run) where individual files
   weren't produced.
3. Sub-numbered identifier whose file uses a different sub-number scheme
   (e.g. `H-NEW-127.10` in prose vs `h-new-127-10-...md` on disk).

Total scanned files with linkification: {n_files}

{body}
"""
    ORPHAN_REPORT.write_text(content)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--apply", action="store_true", help="Write changes to disk"
    )
    args = parser.parse_args()

    mapping, collisions = discover_finding_files()
    targets = find_target_files()
    print(f"Discovered {len(mapping)} canonical finding ids.")
    print(f"Scanning {len(targets)} markdown files for references…")

    orphans: Counter = Counter()
    files_changed = 0
    total_links = 0

    for path in targets:
        try:
            original = path.read_text()
        except (UnicodeDecodeError, OSError):
            continue
        new_text, n_added = linkify_text(original, mapping, orphans)
        if n_added > 0 and new_text != original:
            files_changed += 1
            total_links += n_added
            if args.apply:
                path.write_text(new_text)

    print()
    print("=" * 60)
    print(f"Files {'modified' if args.apply else 'that WOULD change'}: {files_changed}")
    print(f"Wikilinks {'added' if args.apply else 'that WOULD be added'}: {total_links}")
    print(f"Orphan references (unique ids): {len(orphans)}")
    if orphans:
        print("Top 10 orphan references:")
        for ref, count in orphans.most_common(10):
            print(f"  {ref:25s} {count}")
    if collisions:
        print(f"\nFiles with multiple candidates ({len(collisions)} canonical ids):")
        for canon, alts in list(collisions.items())[:5]:
            print(f"  {canon}: kept={mapping[canon]}, alts={alts}")
    print("=" * 60)

    if args.apply:
        write_orphan_report(orphans, len(targets))
        print(f"Orphan report → {ORPHAN_REPORT}")
    else:
        print("(dry run — pass --apply to write changes)")

    return 0


if __name__ == "__main__":
    sys.exit(main())
