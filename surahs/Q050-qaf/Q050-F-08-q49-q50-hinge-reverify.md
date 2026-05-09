---
finding_id: Q050-F-08
surah: 50
date_locked: 2026-05-09
date_run: 2026-05-09
phase: B+
verdict: STRONG-REPLICATION (Q 49 → Q 50 universal hinge confirmed in_all_three=True; direct re-extraction from H-NEW-130, 130b, 130c agrees with Q049-F-03 JSON cross-read)
---

# Q050-F-08 — Q 49 → Q 50 universal hinge re-verification (H-NEW-1262 replication)

## Headline

The Q 49 al-Ḥujurāt → Q 50 Qāf mushaf adjacency is **REPLICATED as a universal hinge**: the (49, 50) pair appears in the **top-15 most-extreme adjacency entries across ALL THREE independent feature sets**:

- **H-NEW-130** (QAC-root residuals): pair distance = 1.0035, `in_top15_root = True`.
- **H-NEW-130b** (character-4-gram residuals): pair distance = 1.0939, `in_top15_char4gram = True`.
- **H-NEW-130c** (verse-length residuals): pair distance = 1.3718, `in_top15_verselen = True`.

Q049-F-03 JSON `primary_all_three = True`. Direct re-extraction from h-new-130/130b/130c JSONs CONFIRMS the JSON cross-read with full agreement.

**Verdict: STRONG-REPLICATION.** Q 50 inherits the H-NEW-1262 universal-hinge cross-reference.

## Method

Pre-reg SHA256 `a5abbd224371` (this file's prereg `Q050-F-08-q49-q50-hinge-reverify-prereg.md`).
SHA verified at script runtime; fail-fast on mismatch.

Two independent verification paths:

1. **JSON cross-read**: open `surahs/Q049-al-hujurat/csv/Q049-F-03.json` and verify:
   - `in_h130_top15_root = True`
   - `in_h130b_top15_char4gram = True`
   - `in_h130c_top15_verselen = True`
   - `primary_all_three = True`
   - `q49_q50_pair = [49, 50]`

2. **Direct re-extraction**: open each of `h-new-130.json`, `h-new-130b.json`, `h-new-130c.json`, extract `top15_largest_jumps`, search for the (49, 50) entry. Record distance.

The two verification paths AGREE iff (a-d) above are True in both reads.

## Result

| Source | In top-15? | Distance | Method |
|:--|:--|:--|:--|
| h-new-130 (root) | YES | 1.0035 | Direct extraction |
| h-new-130b (char-4-gram) | YES | 1.0939 | Direct extraction |
| h-new-130c (verse-length) | YES | 1.3718 | Direct extraction |
| Q049-F-03 JSON `primary_all_three` | True | — | JSON cross-read |
| Q049-F-03 JSON `q49_q50_pair` | [49, 50] | — | JSON cross-read |
| JSON ↔ Direct agreement | YES | — | Cross-method check |

All 6 cells PASS. The replication is STRONG — both methodological paths independently arrive at the same conclusion. The pre-commit-direction-locked verdict (REPLICATED) is achieved at the strongest possible standard (STRONG-REPLICATION).

## Interpretation

Q 49 → Q 50 is one of the **three universal hinges** in the project's mushaf-structure findings (per [[cross-finding-013-ring-topology]] / H-NEW-142): the three (i, i+1) adjacencies that appear in the top-15 most-extreme adjacency entries on ALL THREE feature axes:

1. **Q 14 → Q 15** (al-Ibrāhīm → al-Ḥijr)
2. **Q 49 → Q 50** (al-Ḥujurāt → Qāf)
3. **Q 56 → Q 57** (al-Wāqiʿa → al-Ḥadīd)

These three universal hinges share two structural properties:
- Each marks a **chronological-period transition** (Medinan → Meccan or Meccan → Medinan).
- Each marks a **muqaṭṭāʿat-presence change** (muqaṭṭāʿat-opener ↔ non-muqaṭṭāʿat-opener) on at least one side.

For Q 49 → Q 50 specifically:
- **Period**: Medinan (Q 49 al-Ḥujurāt, revelation #105) → Middle Meccan (Q 50, revelation #34). Nöldeke gap = 72 positions.
- **Muqaṭṭāʿat-presence**: Q 49 (no opener) → Q 50 (singleton-letter opener ق). The hinge crosses a muqaṭṭāʿat-presence boundary.
- **Mufaṣṣal-onset**: Per Ibn Kathīr's classical claim, Q 50 is the *first surah of al-mufaṣṣal*. The Q 49 → Q 50 hinge is therefore ALSO the *empirical onset of the mufaṣṣal cluster* (FR-roots nearest-5 of Q 50 = post-s=75 mufaṣṣal-qiṣār surahs Q 78, 86, 112, 79, 110).

## Why Q 50 needs this re-verification

Q 50 specialist's cross-reference network (07-cross-references.md §10) cites the Q 49 → Q 50 universal hinge as one of Q 50's defining structural properties. Before that cross-reference was published, the Q050-F-08 test verifies that the dependency finding (Q049-F-03 / H-NEW-1262) is STILL replicable on the disk JSONs — i.e., the underlying H-NEW-130 / 130b / 130c data have not been modified, and Q049-F-03 JSON has not been tampered with.

This is a **method-discipline test** (a check on dependencies), not a new scientific claim. Its value is in the discipline.

## Honest limits

- This is intentionally a LOW-NOVELTY test. Its purpose is verification of a dependency, not new science.
- The "STRONG-REPLICATION" verdict applies to the disk state on 2026-05-09. Future re-runs of H-NEW-130 / 130b / 130c (e.g., if QAC v0.5 is released and the corpus morphology shifts) would require a new replication check.
- The top-15 size is exactly 15 in each JSON; we did not test sensitivity to alternate cutoffs (e.g., top-10 or top-20). Under top-10, the (49, 50) entry would need to be in the top-10 of each feature set — direct verification would be needed.

## Cross-references

- [[h-new-130-fisher-rao-residuals]] — the root-residual ranking; Q 49 → Q 50 at distance 1.0035.
- [[h-new-130b-fisher-rao-residuals-char4gram]] — the char-4-gram ranking; Q 49 → Q 50 at distance 1.0939.
- [[h-new-130c-fisher-rao-residuals-verselen]] — the verse-length ranking; Q 49 → Q 50 at distance 1.3718.
- [[surahs/Q049-al-hujurat/csv/Q049-F-03|Q049-F-03 JSON]] — the original Q 49 specialist's universal-hinge finding.
- [[h-new-1262]] / [[cross-finding-013-ring-topology]] — the universal-hinge collection (3 hinges).
- [[Q050-qaf/07-cross-references]] — incorporates the universal-hinge cross-reference (verified by this test).

## Data files

- Pre-reg: `surahs/Q050-qaf/preregs/Q050-F-08-q49-q50-hinge-reverify-prereg.md` (SHA256 `a5abbd224371`).
- Script: `scripts/Q050_F_08_q49_q50_hinge_reverify.py`.
- JSON: `surahs/Q050-qaf/csv/Q050-F-08.json`.
