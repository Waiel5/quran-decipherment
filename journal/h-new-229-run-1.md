# H-NEW-229 — Run log

**Date**: 2026-04-17
**Agent**: autonomous
**Seed**: 20260419
**Task**: Does the ±58 Nöldeke chronology-reversal mirror at Q 49→50 / Q 56→57 exist under other chronologies (Bell, Egyptian, Blachère)?

## Procedure

1. Read parent finding H-NEW-142 (identifies ±58 mirror) and H-NEW-158 (flags chronology-specificity in honest-limit #1).
2. Located chronology data sources:
   - Nöldeke 1860 + Egyptian 1924 in `data/revelation-order.csv` (dense ranks 1..114)
   - Bell 1937 + Blachère 1947 hard-coded in `scripts/h_new_212_alt_chronology_fisher_rao.py` with documented ties and imputation of surah 15 Bell rank (52, middle-Meccan median)
3. Wrote pre-reg with frozen method + garden-of-forking-paths (strict mirror, ±0 tolerance, above-median-magnitude requirement, Bonferroni k=1). SHA-256 `a3e72d061b55fb7a5aeb7b34e7237975768339f675eac09c52e2c632c59b878f`.
4. Wrote script that:
   - Resolves Bell/Blachère ties to dense 1..114 ranks (mushaf-order ascending, inherited H-NEW-212 pre-reg §5)
   - Computes signed Δ for all 113 consecutive mushaf pairs under each chronology
   - Tests strict mirror on the specific {Q 49→50, Q 56→57} pair-pair
   - Also computes top-6 |Δ| per chronology and largest mirrored |Δ| per chronology (secondary diagnostics)
5. Ran script → clear NOLDEKE_ARTIFACT result.

## Raw results

Per-chronology Δ at the target pairs:

| Chronology | Δ(Q49→50) | Δ(Q56→57) | |equal? | opposite? | above-median? | PRIMARY |
|---|---:|---:|:-:|:-:|:-:|:-:|
| Nöldeke 1860   | −58 | +58 | YES | YES | YES | PASS |
| Egyptian 1924  | −72 | +48 | NO  | YES | YES | FAIL |
| Bell 1937      | −57 | +76 | NO  | YES | YES | FAIL |
| Blachère 1947  | −72 | +48 | NO  | YES | YES | FAIL |

Under Bell, both boundaries are in top-6 (|57| rank 6; |76| rank 2). The architectural prominence partially survives Bell but exact magnitude equality does not.

Largest mirrored |Δ| per chronology:
- Nöldeke: **58 at {Q49→50, Q56→57}**
- Egyptian: 75 at {Q67→68, Q81→82, Q97→98}
- Bell: 33 at {Q32→33, Q85→86}
- Blachère: 75 at {Q67→68, Q97→98}

## Unanticipated finding

Although the strict mirror fails under 3/4 chronologies, the SIGN-PATTERN (Q 49→50 backward, Q 56→57 forward, both above-median) is **robust across all 4**. The architectural claim — "mushaf frames surahs 50–56 with opposite-sign large chronology reversals" — survives chronology variation even though the precise magnitude symmetry does not.

## Verdict

NOLDEKE_ARTIFACT (strict).
SIGN-MIRROR ROBUST (loose, unanticipated).

Recommend amending H-NEW-142 to foreground the robust sign-pattern claim and demote the "exact ±58" claim to Nöldeke-specific coincidence.

## Files emitted

- `findings/phase-b-hypotheses/h-new-229-mirror-pair-structure-across-chronologies.md`
- `findings/phase-b-hypotheses/h-new-229-mirror-pair-structure-across-chronologies-prereg.md`
- `findings/phase-b-hypotheses/csv/h-new-229.json`
- `scripts/h_new_229_mirror_across_chronologies.py`
- this journal entry
