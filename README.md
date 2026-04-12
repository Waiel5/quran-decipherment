# Quran Decipherment Project

A systematic, replication-first analysis of the Quranic Arabic text.

- **Phase A** — replicate every published mathematical/numerical claim about the Quran against the raw text, with explicit counting rules
- **Phase B** — hunt for novel statistical patterns with proper null models
- **Phase C** — structural and semantic cartography (chiastic, ring composition, root-anchoring)

See `docs/design.md` for the full spec and `docs/methodology.md` for counting conventions.

## Layout

```
quran-text/      # raw data from amrayn/quran-text (cloned)
data/            # additional datasets (morphology, alt text, translations)
docs/            # spec, methodology, claims catalog, stats protocol
analysis/        # tools, tests, exploratory notebooks
findings/        # phase A/B/C results, one md per finding
journal/         # agent run logs and decisions
```

## Status

In progress. See `journal/` for the running log of agent runs.
