# H-NEW-940 Run 1 — Journal

**Date**: 2026-05-07
**Agent**: prophet-cycle-order-specialist
**Test**: Prophet-cycle order conservation across 8 narrative surahs (Q 6, 7, 11, 19, 21, 26, 37, 38)
**Pre-reg**: `/Users/grey/Downloads/quran/findings/phase-b-hypotheses/h-new-940-prophet-order-conservation-prereg.md`
**Pre-reg SHA256**: `2351e2c7569e3ce22054edd709b127b234ac662ca23879dc41f62be494b27f66`
**Seed**: 20260507
**Permutations**: 10,000

## Timeline

1. **Pre-flight reading**: SKILL.md, INVESTIGATION-PROTOCOL.md, HANDOFF/04-DISCIPLINE.md, prophet-mention-chronology.md, prophet-suppression-classical-ordering.md (existing prior art on prophet lemmas + classical-source citations).
2. **QAC lemma verification**: directly grepped `data/morphology/quranic-corpus-morphology-0.4.txt` for each of the 25 al-Suyūṭī-canonical prophet PN-lemmas. Verified Hūd (`huwd`) ≠ huwd2 (= "al-yahūd"); Ṣāliḥ (`Sa\`liH2`) ≠ adjective ṣāliḥ; Dhū al-Kifl is NOT a single PN-lemma (must verse-anchor at Q 21:85 word-3 segment-2 and Q 38:48 word-3 segment-2 with root `kfl`).
3. **Pre-reg authored** with locked direction (positive), 10,000 perms, seed 20260507, Bonferroni-4 on H2 sub-axes.
4. **SHA256 computed and embedded** in script: `2351e2c7569e3ce22054edd709b127b234ac662ca23879dc41f62be494b27f66`.
5. **Script run** — initial run executed all primary statistics. Discovered chronology-CSV-lookup-bug (used `revelation_order` column instead of `mushaf_order`) but only AFTER primary stats were computed; affected only H3 descriptive phase-labels, not H1/H2.
6. **Bug-fix and re-run** of chronology lookup (column-name search). Primary statistics unchanged; H3 phase-labels now correct.
7. **Findings doc and JSON output** written.

## Decision points

- **Decision (pre-run)**: Dhū al-Kifl is not a PN-lemma in QAC. Hard-coded as verse-anchored at Q 21:85 and Q 38:48 with root `kfl` cross-check. Documented in pre-reg §5 and §12.
- **Decision (pre-run)**: Q 19's Hārūn (Q 19:28 *ʾukhta Hārūn*) is treated under strict PN-lemma identity (same lemma `ha\`ruwn` as Mūsā's brother). al-Ṭabarī's contextual disambiguation is NOT applied; this could spoil H2c, and the pre-reg honors the locked rules-tuple. Documented as known fragility before run.
- **Decision (post-run, transparent)**: H2b's canonical chain (Ibrāhīm-Ismāʿīl-Isḥāq) was a-priori chosen per the task-spec but turns out to be the wrong direction in the Quran (which prefers Ibrāhīm-Isḥāq-Ismāʿīl). H2b is reported as NULL with this disclosure; the corrected-chain test is NOT promoted post-hoc but queued as H-NEW-940.1.
- **Decision (post-run)**: H1 perm p = 0.047 fails locked α=0.01. Direction was POSITIVE (pre-committed). No pre-commit violation, but verdict is DIRECTIONAL (not CONFIRMED). Honest publication: H1 is positive but does not clear the locked threshold.

## Garden-of-forking paths

The chronology-column-lookup bug was a script-level error in the H3 phase-label readout, NOT in primary statistics. Fixed mid-session before publishing findings; primary stats were locked and re-confirmed identical post-fix. No methodology shift.

## Verdicts

| Test | Verdict | Stat |
|:---|:---|:---|
| H1 (corpus mean τ) | **DIRECTIONAL** | mean τ = +0.144, perm p = 0.047 (vs locked α=0.01) |
| H2a (Ādam-Nūḥ-Hūd-Ṣāliḥ) | **CONFIRMED, Bonferroni-4** | mean τ = +1.0, perm p = 0.001 |
| H2b (Ibrāhīm-Ismāʿīl-Isḥāq) | **NULL** | mean τ = +0.556, perm p = 0.060 |
| H2c (Mūsā-Hārūn) | **NULL** | 5/6 = 0.833, binomial p = 0.109 |
| H2d (Q 21 vs Q 6:83-87) | **NULL** | τ = +0.359 (threshold 0.7), perm p = 0.049 |
| H3 (consensus + typology) | **DESCRIPTIVE** | 23-prophet narrative-prominence consensus; no clean phase-typology |

## Output artifacts

- `/Users/grey/Downloads/quran/findings/phase-b-hypotheses/h-new-940-prophet-order-conservation-prereg.md`
- `/Users/grey/Downloads/quran/scripts/h_new_940_prophet_order_conservation.py`
- `/Users/grey/Downloads/quran/findings/phase-b-hypotheses/csv/h-new-940.json`
- `/Users/grey/Downloads/quran/findings/phase-b-hypotheses/h-new-940-prophet-order-conservation.md`
- `/Users/grey/Downloads/quran/journal/h-new-940-run-1.md` (this file)

Runtime: ~30 seconds on Apple Silicon.
