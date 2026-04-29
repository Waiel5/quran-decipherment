---
journal_entry: linkifier-2026-04-28
agent: obsidian-knowledge-graph-specialist
date: 2026-04-28
scope: convert plain-text finding references into Obsidian wikilinks
script: scripts/linkify_findings.py
---

# Linkifier run — 2026-04-28

## What was done

Built `scripts/linkify_findings.py`, an idempotent regex-based linkifier
that converts plain-text finding references (`H-NEW-NNN`, `H-NEW-NNN.M`,
`cross-finding-NNN`) into Obsidian wikilinks
`[[filename-stem|original-text]]`. The display text after the pipe
preserves original casing/punctuation, so prose reads exactly the same;
Obsidian builds the navigable graph from the canonical filename target.

### Scope

- `MASTER-FINDINGS-LEDGER.md` — single root index
- `findings/phase-b-hypotheses/*.md` — primary writeups + cross-findings 010-024
- `findings/cross-finding/*.md` — cross-findings 009, 025, 026 + meta files

YAML front-matter is intentionally **skipped** (linkifier detects opening
`---` on line 1 and resumes at the closing `---`). Code-fence blocks are
also skipped. Already-wikilinked references are detected by walking back
to find an unclosed `[[` on the same line.

### Canonical-id grammar

Filenames map to canonical ids via a regex tolerant of:

- bare numeric: `h-new-580`
- letter-suffixed: `h-new-111b`
- sub-numbered: `h-new-127-10`
- sub-num + letter: `h-new-236-1a`
- sub-sub-num: `h-new-44-2-1`

Reference text (`H-NEW-127.10`, `H-NEW-236.1A`, `H-NEW-44.2.1`) is
canonicalized by lowercasing and replacing `.` with `-`.

### Collision policy

Where two non-prereg files match the same canonical id, prefer:
1. the non-secondary (no `prereg` / `-rerun` / `-mst-analysis` in stem),
2. otherwise the shorter (more canonical) stem.

For cross-finding ids appearing in both `cross-finding/` and
`phase-b-hypotheses/` directories, prefer `cross-finding/`. Six canonical
ids hit the collision branch; all resolved sensibly (e.g. `h-new-189`
prefers `h-new-189-medinan-inclusio.md` over the `-prereg-backfill.md`
variant; `cross-finding-023` prefers `causal-generative-closure.md` over
the `-oq15-` peel-out).

## Stats

| Metric | Value |
|---|---|
| Canonical finding ids discovered | 321 |
| Markdown files scanned | 749 |
| Files modified | 605 + 57 (Capitalized cross-finding pass) |
| Wikilinks added | 9,268 + 89 = **9,357** |
| Unique orphan references | 364 |
| Orphan-report file | `findings/ORPHAN-REFERENCES.md` |

## Top orphan references

These are mentions where no matching `.md` file was found:

| Reference | Mentions | Likely status |
|---|---|---|
| `cross-finding-008` | 123 | Synthesis ID never split into its own file |
| `H-NEW-35` | 75 | Early bare-numbered finding, no standalone writeup |
| `H-NEW-59` | 66 | Early aggregate ID, may live inside another file |
| `H-NEW-1`, `H-NEW-19`, `H-NEW-20`, `H-NEW-23`, `H-NEW-29`, `H-NEW-34` | 40-61 each | Pre-numbering-scheme legacy IDs |
| `cross-finding-006`, `cross-finding-007` | 50 / 23 | Earlier synthesis stubs |
| `H-NEW-136.1`, `H-NEW-96.2` | 21 each | Sub-numbered tests possibly inside parent file |

These do not represent broken linkages — most are references to findings
documented inline within other markdown files rather than promoted to
their own `.md`. The orphan report is generated fresh each run, so once
those files are added the orphans count will fall.

## Reversal

All edits are pure regex insertions. To revert:

```bash
rg -l "\[\[h-new-" findings/ MASTER-FINDINGS-LEDGER.md \
  | xargs sed -i '' -E "s/\[\[(h-new-[^|]+)\|([^]]+)\]\]/\2/g; s/\[\[(cross-finding-[^|]+)\|([^]]+)\]\]/\2/g"
```

## Spot checks (3 files)

1. **`findings/phase-b-hypotheses/cross-finding-024-five-factor-cohesion-model.md`** — heading line gets `[[cross-finding-024-five-factor-cohesion-model|Cross-Finding-024]]` self-link (graph-friendly), interior H-NEW-321/360/390 links resolve to their writeups, YAML front-matter untouched.
2. **`MASTER-FINDINGS-LEDGER.md`** — ~1,500 wikilinks inserted; H-NEW-24, H-NEW-2, H-NEW-4, H-NEW-11 all resolve. One filename-like reference (`...h-new-24-letter-ordering-suppression.md`) inside parens partially linkified — acceptable trade-off, Obsidian renders both halves.
3. **`findings/phase-b-hypotheses/h-new-580-five-factor-regression.md`** — heading self-link, cross-finding-024 outbound link, four H-NEW-3XX outbound links to subsidiary cohesion findings.

Idempotency confirmed: re-running `python3 scripts/linkify_findings.py`
(dry-run) reports 0 files would change.

## Notes for future graph maintenance

- The script auto-discovers any new `h-new-*.md` or `cross-finding-*.md`
  added to `findings/phase-b-hypotheses/`, `findings/cross-finding/`,
  `findings/phase-c-structures/`. Re-running with `--apply` after writing
  new findings will linkify any new mentions automatically.
- Scholar-name linking (`al-Suyūṭī`, `al-Biqāʿī`, etc.) was deliberately
  **skipped** per the brief's "prioritize finding-to-finding linking"
  fallback. The orphan report flags ~364 unresolved IDs which is the
  more actionable backlog.
- Capitalized-prefix variants (`Cross-Finding-024`, `Cross-finding-023`)
  are now handled in a second pass added after spot-check showed them
  remaining unlinked.
