# H-NEW-90 — Q 18 al-Kahf 4-narrative structural parallelism — run 1

**Date:** 2026-04-15
**Agent:** h-new-90-specialist
**Status:** EXECUTED — verdict WEAK (2 of 5 cells PASS)
**Prereg:** findings/phase-b-hypotheses/h-new-90-kahf-narrative-structure-prereg.md
**Script:** scripts/h_new_90_kahf_narrative_structure.py
**Result:** findings/phase-c-structures/h-new-90-kahf-narrative-structure.md

## Plan

Pre-register and execute a quantitative test of whether Al-Kahf's 4 narratives (Cave 9-26, Gardens 32-44, Moses-Khidr 60-82, Dhū'l-Qarnayn 83-98) are MORE structurally parallel than 4 narratives from Q 7, Q 11, Q 26.

## Decisions log (pre-execution)

1. **Boundary spec.** Locked Rāzī-Qadhi modal: 9-26, 32-44, 60-82, 83-98. NOT permitted to expand v9 to v8 or to fold interlude A (27-31) into the Cave block.

2. **Comparator surahs.** Pre-locked Q 7, Q 11, Q 26 as the three project-canonical "multi-narrative" surahs. NOT permitted to swap to Q 12 (single-narrative Yusuf) or Q 28 (single-narrative Qaṣaṣ) post-hoc.

3. **First-4 truncation policy.** Q 7, 11, 26 each have >4 narratives. Locked: take FIRST 4 by verse-order. Garden-of-forking-paths: this disadvantages comparators (since their 5th-7th narratives may be most parallel — e.g., Q 26's Hūd-Ṣāliḥ-Lūṭ-Shuʿayb chain). Accepted as conservative bias against the "Al-Kahf is unique" hypothesis (i.e., if it loses to comparators even on truncation, that is robust).

4. **Verse-count-tuple null.** Locked: random 4-block partition with sizes (18,13,23,16) (Al-Kahf's). This means each comparator's null is built using Al-Kahf-shaped block sizes — fair to compare z-scores across surahs.

5. **Bonferroni k=5.** Locked. α_outer = 0.010. z-threshold = 2.326.

## Execution log

- **00:14** wrote prereg
- **00:18** wrote script (~360 lines)
- **00:19** first run — completed in <30 s
- **00:20** verified MW-5 PASSES (N3↔N4 jaccard 0.199 > Kahf mean 0.148) — metric is responsive
- **00:21** Surprise: T2 Al-Kahf z = **-6.134** (Al-Kahf has LOWER inter-narrative root jaccard than random); Q 7 z = **+5.25** (al-Aʿrāf has HIGHER)
- **00:22** Surprise: T5 Q 11 Hūd z = **+3.25** (Hūd's prophet-cycle formula `wa-ilā [tribe] akhāhum [prophet]` is the project's most opener-parallel surah)
- **00:23** wrote findings doc

## Surprises (3)

1. **Al-Kahf's 4 narratives have LESS shared vocabulary than random partition predicts** (z=-6.13). The al-kahf-deep-dive (2026-04-12) qualitative claim of "structural parallelism" does NOT propagate to lexical-Jaccard level. The four narratives are deliberately diversified: cave-mythology / agricultural-parable / Moses-saga / world-conquest-saga, each with its own time-and-vocabulary register.

2. **Q 11 Hūd is the Quran's strongest opener-formula-parallel surah** (z=+3.25 on opener-triple Jaccard). This is a NEW finding worth follow-up. Suggests H-NEW-91 to formalize the Hūd prophet-cycle formula.

3. **Q 7 al-Aʿrāf has the strongest inter-narrative Jaccard parallelism** (z=+5.25). The first-4-prophet pericopes (Adam, Nūḥ, Hūd, Ṣāliḥ) share substantial vocabulary — the canonical "prophets-cycle" pattern.

## What this DOES NOT undermine

- The v50 word-midpoint convergence (T3 PASSES — v50 is at interlude-B centre, not a narrative interior).
- The Moses-Khidr ↔ Dhū'l-Qarnayn 3-act isomorphism (al-kahf-deep-dive §6.1) — pair Jaccard 0.199 is the ONLY above-mean pair within Al-Kahf.
- The 4-trial CLASSICAL reading (Rāzī, Qadhi) — that mapping is thematic and sound; it just doesn't operate at the lexical-root level.
- Al-Kahf's 5-method midpoint convergence (al-kahf-deep-dive §1) — those metrics measure word/letter midpoints and ring structures, not inter-narrative parallelism.

## What this DOES undermine

- The al-kahf-deep-dive §2 grid's claim that Al-Kahf's 4 narratives have unusual STRUCTURAL parallelism beyond their thematic 4-trial reading. RECLASSIFIED to: the parallelism is real for the Moses-Khidr ↔ Dhū'l-Qarnayn pair only; the other 5 pairs are at-or-below random.

## Sensitivity tests NOT run

- Expanded boundaries (Cave 9-31, Moses-Khidr 45-82): deferred to follow-up.
- QAC orthographic-token tokenization (vs whitespace): the QAC tokens differ minimally from whitespace for root-Jaccard; deferred.
- Larger null (10000 iterations): given |z|>4.9 on multiple cells, additional iterations will not flip verdict.

## Outputs

- findings/phase-b-hypotheses/h-new-90-kahf-narrative-structure-prereg.md
- scripts/h_new_90_kahf_narrative_structure.py
- findings/phase-c-structures/h-new-90-kahf-narrative-structure.md
- findings/phase-c-structures/csv/h-new-90-results.json
- (this) journal/h-new-90-kahf-narrative-structure-run-1.md

## Status

Reported. Verdict WEAK. Two PASS cells (T1, T3) survive Bonferroni; three FAIL cells (T2, T4, T5) are robustly NULL with negative z-scores. The al-kahf-deep-dive §2 claim is reclassified.

Followup hypothesis suggested: **H-NEW-91 — Q 11 Hūd as the Quran's prophet-cycle template surah** (opener-formula z=+3.25).
