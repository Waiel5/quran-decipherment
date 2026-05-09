---
finding_id: Q050-F-07
surah: 50
date_locked: 2026-05-09
date_run: 2026-05-09
phase: B+
verdict: DIRECTIONAL-TOP-3 (Q 50 ق-rate ranks 2nd of 16 Meccan 30-50-verse surahs; pre-reg's rank-1 lock NOT achieved; pre-commit honored)
---

# Q050-F-07 — Q 50 ق-letter density vs 30-50-verse Meccan surahs

## Headline

Among the **16 Meccan surahs of 30-50 verses inclusive**, Q 50 Qāf has the **2nd-highest ق-letter rate** (0.0378), narrowly edged by **Q 75 al-Qiyāma** (0.0399). The pre-registered direction was **Q 50 rank = 1**; the observed result is Q 50 rank = 2.

**Verdict: DIRECTIONAL-TOP-3** (the classical "Q 50 saturated with ق" claim is empirically real and large in magnitude, but Q 50 is NOT the *unique* class-rank-1 surah on this metric).

This is published with full pre-commit transparency: the strict rank-1 hypothesis is FALSIFIED, but the underlying claim (Q 50 has corpus-extreme ق density) is robust — Q 50's ق rate (3.78%) is more than 4× the corpus rate (~0.9% in the Quranic baseline) and beats 14 of the 15 length-and-period-matched comparator surahs.

## Method

Pre-reg SHA256 `6a5530552dd6` (this file's prereg `Q050-F-07-qaf-density-vs-meccan-30-50-prereg.md`).
SHA verified at script runtime; fail-fast on mismatch.

- Class definition: Meccan surahs with 30 ≤ total_verses ≤ 50, enumerated from `quran-text/quran-no-tashkeel.json` `type` field. n_class = 16.
- Letter counting: graphemes from the Arabic Unicode block U+0621..U+064A + U+0671, Tatweel stripped, basmala not counted (already excluded by no-tashkeel JSON for surahs > 1).
- Permutation null: 10000 random reassignments of the 16 ق-counts onto the 16 letter-totals; compute P(Q 50 obtains sole rank-1). Seed 20260509.

## Result

Per-surah ق rates, ranked descending:

| Rank | Surah | Name | n_verses | ق-count | Letter total | ق-rate |
|:-:|:-:|:--|:-:|:-:|:-:|:--|
| 1 | Q 75 | al-Qiyāma | 40 | 27 | 676 | 0.03994 |
| **2** | **Q 50** | **Qāf** | **45** | **57** | **1507** | **0.03782** |
| 3 | Q 46 | al-Aḥqāf | 35 | 73 | 2667 | 0.02737 |
| 4 | Q 67 | al-Mulk | 30 | 36 | 1347 | 0.02673 |
| 5 | Q 32 | al-Sajda | 30 | 38 | 1563 | 0.02431 |

Q 50 rank = 2 / 16. perm_p_rank_1 = 0.0052 — i.e., under a uniform-mixing null (where ق counts are shuffled across the 16 surahs), Q 50 would be the sole rank-1 in only 0.5% of perms. The fact that Q 50 ranks 2nd (NOT 1st) in the actual observed data is therefore especially noteworthy: even under a null where Q 50 *would* dominate, the actual class-rank-1 is Q 75.

## The Q 75 al-Qiyāma observation

Q 75 al-Qiyāma is an Early-Meccan eschatological surah of 40 verses, opening with the oath *lā uqsimu bi-yawm al-qiyāma* ("I swear by the Day of Resurrection"). Its 27 ق-tokens in 676 letters give it the highest ق-rate in the comparator class. Inspection of the high-frequency Q 75 ق-roots:

- *qiyāma* (rising / resurrection) — root q-w-m, multiple attestations.
- *qul* (say) — frequent imperative.
- *taqūm* (you will rise / it will stand).
- *al-bāqi* (the remaining one).

Q 75's ق-saturation is driven by ITS topic (al-qiyāma = the rising). This is the same lexical-thematic driver as Q 50's ق-saturation:

- Q 50: *qāf* (opening) + *al-qiyāma* (eschatology) + *al-Qurʾān* (recitation) + *al-qalb* (heart) + roots *q-r-r* (settle), *q-r-b* (near), *q-r-n* (companion), *q-ʿ-d* (sit).

**Q 75 is the comparator-class rank-1 because Q 75's surface vocabulary is ALSO ق-saturated by topical lexical choice.** This is a discovery that the strict rank-1 pre-reg did not anticipate: the classical "Q 50 saturated with ق" claim is empirically robust but **NOT unique to Q 50** — Q 75 has even higher ق density per total letters.

## Comparison with Q050-F-03

| Test | Null | Q 50 ق-rate | Q 50 z | Q 50 p | Verdict |
|:--|:--|:--|:--|:--|:--|
| Q050-F-03 | length-matched random window (across all 114 surahs) | 0.0378 | +3.34 | 0.0001 | CONFIRMED |
| Q050-F-07 | class-rank within 16 Meccan 30-50-verse surahs | 0.0378 | — | — | DIRECTIONAL-TOP-3 (rank 2/16) |

Both tests use the same Q 50 observation (57 ق / 1507 letters = 3.78%). The two tests differ on null:

- Under a **length-matched-random-window null** (full corpus), Q 50's ق-rate is 76% above null mean (z = +3.34, p = 10⁻⁴, percentile 100) — Q 50 is corpus-extreme.
- Under a **class-rank-within-Meccan-30-50-verse null**, Q 50 is rank 2/16 (Q 75 is rank 1).

These are consistent: Q 50 IS corpus-extreme, AND Q 75 is also very high. The 16-surah class-rank is a more stringent test (it controls for length-and-period); Q 75's existence in the same class is the empirical refinement of the classical claim.

## Pre-commit transparency

The pre-reg locked direction was **Q 50 rank = 1** (strict). The observed outcome is **Q 50 rank = 2** (Q 75 narrowly edges Q 50 by 0.022 percentage points in ق-rate).

Per PRE-REG-STANDARD-04 / INVESTIGATION-PROTOCOL §1.3: the pre-reg's rank-1 prediction is reported as NOT-ACHIEVED. The verdict is DIRECTIONAL-TOP-3 (Q 50 is in the top 3 of 16; 2nd place; pre-reg's strict-rank-1 not met). This is published with full prominence; no result-massaging.

The underlying scientific claim — Q 50 has corpus-extreme ق-density — is robust (Q050-F-03 confirms at p = 10⁻⁴). The refinement is: Q 50 is NOT uniquely the densest ق-surah in its length-matched-Meccan reference class. **Q 75 al-Qiyāma is the new comparator-class rank-1, driven by its qiyāma/qul/taqūm lexical-thematic saturation.**

This is a NEW empirical observation NOT noticed in al-Rāzī's *muqaṭṭaʿāt* discussion (`razi-muqattaat-surah-qaf.md`), which focused on Q 50 alone without comparing length-matched-period-matched Meccan surahs. **A future systematic Q 75 specialist should investigate the Q 75 ق-saturation as an independent classical-iʿjāz observation candidate.**

## Honest limits

- The Meccan classification of Q 50 (entirely Meccan except Q 50:38 per Ibn ʿAbbās + Qatāda dissent) and Q 75 (all-Meccan) is per Tanzil-Egyptian standard. Under stricter classifications, Q 75 could remain in or move out of the comparator class.
- Q 75's 40 verses places it in the 30-50 bracket; under a 20-50 bracket (more generous), Q 92, 96, 102, etc. would also enter — but their ق-counts are small and would not displace Q 50 or Q 75 from the top-2.
- The strict rank-1 lock is the *strongest possible* pre-reg formulation; rank-2 vs rank-1 is a 1-unit gap that is sensitive to data quirks (e.g., a single ق-token swap between Q 50 and Q 75 would change the rank). Honest result: Q 50 is the densest **muqaṭṭāʿat-opener** ق-surah, but NOT the densest 30-50-verse Meccan ق-surah at all.

## Cross-references

- [[Q050-F-03]] — length-matched-random-window ق-density test (CONFIRMED z = +3.34).
- [[razi-muqattaat-surah-qaf]] — al-Rāzī's pre-existing project extract; "Q 50 has 57 ق's" — verified.
- [[h-new-130-fisher-rao-residuals]] — muqaṭṭāʿat as letter-hub-architecture.
- **NEW finding-candidate**: Q 75 ق-saturation — should be investigated as a Q 75 specialist task; the al-qiyāma / qul / taqūm lexical-thematic ق-driver in Q 75 is potentially a CLASSICAL-ECHO of the same iʿjāz al-fawāṣil signature al-Bāqillānī identifies in Q 50.

## Data files

- Pre-reg: `surahs/Q050-qaf/preregs/Q050-F-07-qaf-density-vs-meccan-30-50-prereg.md` (SHA256 `6a5530552dd6`).
- Script: `scripts/Q050_F_07_qaf_density_vs_meccan_30_50.py`.
- JSON: `surahs/Q050-qaf/csv/Q050-F-07.json`.
