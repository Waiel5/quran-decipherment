# H-NEW-288 Run 1 Journal

- Date: 2026-04-19
- Specialist: codex
- Script: `scripts/h_new_288_normalization_family_adjudication.py`
- Pre-reg:
  `findings/phase-b-hypotheses/h-new-288-normalization-family-adjudication-prereg.md`
- JSON:
  `findings/phase-b-hypotheses/csv/h-new-288.json`

## Command

```bash
python3 scripts/h_new_288_normalization_family_adjudication.py
```

## Purpose

Hold the H-NEW-279 five-metric MST panel fixed and adjudicate the two
live OQ-19 length-control families directly:

- literal `count / N_i` normalization
- residualized `alpha_i = 0.5 * mean_tokens / N_i` smoothing

## Key run outputs

- Pre-reg SHA-256:
  `fd57dfe5ff98fcf84c70cf54312d62b4cbf5160466907959e4853a813b0df8df`
- Inherited anchors:
  - literal Fisher-Rao replicated H-NEW-278 exactly:
    `Q108 degree = 1`, `Q7 degree = 15`
  - residualized Fisher-Rao replicated H-NEW-284 exactly:
    `Q108 degree = 16`, `Q108 rank = 1`
- Primary counts:
  - `C_lit = 0`
  - `C_res = 4`
  - `Delta_C = 4`
- Final verdict:
  `RESIDUALIZED-FAMILY-DOMINANCE`

## Per-family Q108 ranks

### Literal family

- Fisher-Rao: degree `1`, rank `40`
- Jensen-Shannon: degree `1`, rank `40`
- Total variation: degree `5`, rank `5`
- Euclidean L2: degree `1`, rank `43`
- Cosine-angle: degree `1`, rank `43`

### Residualized family

- Fisher-Rao: degree `16`, rank `1`
- Jensen-Shannon: degree `16`, rank `1`
- Total variation: degree `3`, rank `12`
- Euclidean L2: degree `15`, rank `1`
- Cosine-angle: degree `15`, rank `1`

## Mechanism note

The local neighbor pattern is cleaner than the rank table alone:

- literal family collapses Q108 to a `Q89` leaf in `4 / 5` metrics
- residualized family preserves a recurring Q108 core with
  `Q106`, `Q111`, and `Q112` present in `5 / 5` metrics

So the family difference is structural at the edge level, not just a
change in one summary number.
