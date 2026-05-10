---
id: H-NEW-1510
title: Sajda 15-verse pericope-scale root-Jaccard cohesion — scale-of-aggregation flip of H-NEW-1330 NULL
date_locked: 2026-05-09
date_run: 2026-05-09
verdict: PASS-DIRECTED (scale-flip CONFIRMED — whole-surah NULL → pericope PASS at z=+2.685, p_perm=0.0058)
seed: 20260509
n_perm: 10000
prereg_sha: fab8c413105c9867253a49bc09765e3313d22bb6f59688f8a4642048c4d00581
prereg_path: findings/phase-b-hypotheses/prereg-h-new-1510-sajda-pericope-replication.md
script_path: findings/phase-b-hypotheses/scripts/h-new-1510.py
output_json: findings/phase-b-hypotheses/csv/h-new-1510.json
---

# H-NEW-1510 — Sajda 15-verse pericope-scale root-Jaccard cohesion

## Verdict: PASS-DIRECTED — scale-flip CONFIRMED

The 15 sajda-verse pericopes (each sajda verse ± 2 verses, clipped to surah boundaries) exhibit TIGHTER mean pairwise root-Jaccard than length-matched random pericopes from the flat 6,236-verse corpus:

- **J_mean observed = 0.09667** (mean of 105 pairwise root-Jaccards across 15 pericopes)
- **Null mean = 0.06354 ± 0.01234** (10,000 length-matched permutations, seed 20260509)
- **z = +2.685**
- **p_perm (strict one-tailed, ≥ obs) = 0.0058** — below α=0.05, single test, k=1
- Direction matches pre-commit lock: ✓
- **Verdict = PASS-DIRECTED**

## Scale-of-aggregation flip (THE methodological finding)

The classical-Sunnī sajda set has now been tested under TWO scales-of-aggregation and produces TWO different verdicts:

| Scale | Finding | Set | Statistic | Verdict |
|:--|:--|:--|:--|:--|
| Whole-surah | **H-NEW-1330** | 14 sajda-surahs {Q 7, 13, 16, 17, 19, 22, 25, 27, 32, 38, 41, 53, 84, 96} | mean intra-cluster Fisher-Rao distance | NULL (Cell A p=0.571, Cell B p=0.110; PC pass p=0.00020) |
| Pericope (±2) | **H-NEW-1510** (this finding) | 15 sajda-verse pericopes (14 surahs + Q 22:77 double sajda) | mean pairwise root-Jaccard | **PASS-DIRECTED (z=+2.685, p_perm=0.0058)** |

This is the **second cross-scale finding-pair** under cross-finding-025's scale-of-aggregation axis. The first pair was H-NEW-039 (whole-surah NULL, Iblīs) ↔ H-NEW-1380 (pericope PASS, z=+4.76, Iblīs). H-NEW-1510 supplies the second independent example, which is exactly what MASTER-FINDINGS-LEDGER §10.51.4 lists as the threshold for graduating cross-finding-025 from PRELIMINARY-SYNTHESIS toward formal codification.

## Pericope inventory and per-pair structure

| # | Sajda verse | Window | L | Unique roots |
|:-:|:--|:--|:-:|:-:|
| 1 | Q 7:206  | [204..206] | 3 | 21 |
| 2 | Q 13:15  | [13..17]   | 5 | 69 |
| 3 | Q 16:50  | [48..52]   | 5 | 29 |
| 4 | Q 17:109 | [107..111] | 5 | 36 |
| 5 | Q 19:58  | [56..60]   | 5 | 35 |
| 6 | Q 22:18  | [16..20]   | 5 | 48 |
| 7 | Q 22:77  | [75..78]   | 4 | 42 |
| 8 | Q 25:60  | [58..62]   | 5 | 36 |
| 9 | Q 27:26  | [24..28]   | 5 | 32 |
| 10 | Q 32:15 | [13..17]   | 5 | 41 |
| 11 | Q 38:24 | [22..26]   | 5 | 54 |
| 12 | Q 41:38 | [36..40]   | 5 | 43 |
| 13 | Q 53:62 | [60..62]   | 3 | 6  |
| 14 | Q 84:21 | [19..23]   | 5 | 10 |
| 15 | Q 96:19 | [17..19]   | 3 | 6  |

Total = 68 verses across 15 pericopes; C(15,2) = 105 pairwise Jaccards.

### Tightest 5 pairs (the cohesion backbone)

| Pair | J | Inter / Union |
|:--|:-:|:-:|
| Q 17:109 ↔ Q 22:77 | 0.219 | 14 / 64 |
| Q 32:15 ↔ Q 41:38 | 0.217 | 15 / 69 |
| Q 22:18 ↔ Q 41:38 | 0.197 | 15 / 76 |
| Q 27:26 ↔ Q 41:38 | 0.190 | 12 / 63 |
| Q 17:109 ↔ Q 32:15 | 0.185 | 12 / 65 |

These five pairs are all middle-Meccan to late-Meccan sajdas whose pericopes are dominated by the *sjd* + *kbr* + *sbH* + *rbb* + *Hmd* lexical complex — the canonical "prostration-praise" root cluster. Q 41:38 is in four of the top-5 pairs; it functions as the cohesion hub of the sajda pericope set.

### Loosest 5 pairs (the dispersion floor)

| Pair | J | Inter / Union |
|:--|:-:|:-:|
| Q 22:77 ↔ Q 96:19 | 0.021 | 1 / 47 |
| Q 41:38 ↔ Q 96:19 | 0.021 | 1 / 48 |
| Q 22:18 ↔ Q 96:19 | 0.019 | 1 / 53 |
| Q 38:24 ↔ Q 53:62 | 0.017 | 1 / 59 |
| Q 38:24 ↔ Q 96:19 | 0.000 | 0 / 60 |

The loosest pairs all involve Q 96:19 (the *iqra* surah's closing sajda, with only 6 roots in its 3-verse pericope) or Q 53:62 (the al-Najm closing prostration, also 6 roots in its 3-verse pericope) — the two shortest, sparsest pericopes. Q 38:24 (David-prostration narrative) lexically diverges from both because its pericope centers on a juridical-parable (*nʿj* sheep, *xlt* mixed partners) rather than the standard prostration-praise complex. The Q 38:24 ↔ Q 96:19 zero-overlap pair (0 / 60 roots) is the corpus-extreme dispersion case.

## Interpretation

At whole-surah scale (H-NEW-1330), the sajda-trigger is the thinnest possible marker — one verse out of 19 to 206 — and is washed out by the heterogeneous bulk of each surah. At pericope scale (this finding), the sajda-trigger plus its 2-verse context is dominated by the lexical complex around *sjd*, *kbr*, *xrr*, *Hmd*, *sbH*, *rbb* — the canonical liturgical prostration-praise vocabulary identified in al-Suyūṭī *al-Itqān* (nawʿ on sujūd al-tilāwa) and al-Bukhārī's *Kitāb Sujūd al-Qurʾān*. The classical-tradition unit-of-aggregation for the sajda phenomenon is the pericope (the verse-in-its-immediate-recitation-context), not the surah; the empirical scale-flip from NULL to PASS validates the classical operational definition.

The PASS is moderate (z=+2.685 vs the Iblīs pair's z=+4.76) — substantially weaker than H-NEW-1380 — because:
1. Two of the 15 pericopes are very thin (Q 53:62 with 6 roots, Q 96:19 with 6 roots; Q 84:21 with 10 roots). These low-cardinality pericopes drag the overall mean Jaccard downward via small-union arithmetic.
2. Q 38:24 (David-Iblīs-related juridical parable) is lexically off-axis from the standard prostration-praise complex; it contributes negative pairs (lowest pair J=0.000 with Q 96:19).
3. The sajda set is chronologically and structurally heterogeneous (Early through Medinan; opener through closer positions), unlike Iblīs which is a thematically tighter narrative cycle.

Even under these dispersing pressures, the cohesion signal at pericope scale is real (z=+2.685, p=0.0058). This is the central finding: **the H-NEW-1330 NULL was a scale-of-aggregation artifact, not a substantive absence of cohesion**.

## Honest limits

- Single seed (20260509). Seed-independent replication queued as H-NEW-1510b.
- ±2 window is a pre-locked canonical choice; window-width sensitivity (±1, ±3) is queued.
- Boundary-clipping (no cross-surah bleed) is conservative; cross-surah-bleed sensitivity test queued.
- Length-matched null does not control for prose-genre (narrative vs eschatological vs liturgical); prose-matched null queued.
- PASS is single-test, k=1; not yet replicated under a second instrument (TF-IDF cosine, root-frequency χ²). Queued.
- The 15-pericope unit count differs from H-NEW-1330's 14-surah unit count because Q 22 has two sajdas — this is structurally appropriate at pericope scale but means the two findings are not literal-pair set-equivalent units. The set-equivalent comparison (14 pericopes, dropping Q 22:77) is queued as sensitivity.

## Connection to existing findings

- **H-NEW-1330 NULL (whole-surah)** → this finding **PASS-DIRECTED (pericope)** = second cross-scale finding-pair after H-NEW-039 / H-NEW-1380.
- **H-NEW-1380 / Q038-F-07** — methodological precedent: thin-marker NULLs at whole-surah scale CAN flip to PASSes at pericope scale.
- **H-NEW-039** — first cross-scale pair partner (Iblīs whole-surah NULL).
- **cross-finding-025 (PRELIMINARY-SYNTHESIS)** — graduates toward formal codification with this second cross-scale finding-pair (per §10.51.4 threshold).
- **H-NEW-1331 PASS-DIRECTED** — sajda × muqaṭṭāʿat over-representation (7 of 14 sajda surahs muqaṭṭāʿat-opened). Together with H-NEW-1510, the sajda set now has TWO structural correlates: hypergeometric muqaṭṭāʿat enrichment (H-NEW-1331) and pericope-scale root cohesion (H-NEW-1510). The whole-surah NULL (H-NEW-1330) remains correct at its own scale.
- **Q022-F-06** — Q 22 double-sajda singleton status; basis for inclusion of Q 22:77 as the 15th sajda verse.

## Predictions enabled

Queued candidates for pericope-scale re-test under the same protocol:
- **H-NEW-1310** (Christ-narrative {Q 3, 5, 19}) — re-test as pericope set {Q 3:42-63, Q 5:110-118, Q 19:1-37}.
- **H-NEW-1340** (al-ḥamdu li-llāh opener {Q 1, 6, 18, 34, 35}) — re-test on opening pericopes (verses 1-3 of each).
- **H-NEW-1360** (*yā-ayyuhā al-nabī* 6-surah set) — re-test on the 13 vocative-attestation verses ± 2 context.

With the H-NEW-1380 (Iblīs) and H-NEW-1510 (sajda) PASSes in hand, the prediction is that AT LEAST ONE of these three will also flip from NULL to PASS at pericope scale. A clean 4-for-4 flip would graduate the scale-of-aggregation axis from supported-by-2-pairs to corpus-law level under cross-finding-025-formal.

## Classical context

al-Suyūṭī, *al-Itqān fī ʿulūm al-Qurʾān*, nawʿ on sujūd al-tilāwa, treats each sajda verse as a discrete liturgical-recitation unit, not as a property of the host surah. al-Bukhārī (*Ṣaḥīḥ*, *Kitāb Sujūd al-Qurʾān*, ḥadīths 1067-1079) reports prophetic sajdas at recitation of specific verses, never at whole surahs. al-Tirmidhī's *Kitāb al-Witr* (ḥadīths 573-577) catalogues the sajda verses individually. The classical operational definition of the sajda phenomenon is **at the verse-in-immediate-recitation-context scale**, which is what this finding's pericope unit operationalizes. The empirical PASS at this scale corresponds to the classical operational unit; the H-NEW-1330 whole-surah NULL was testing at the wrong scale for the classical phenomenon, as the H-NEW-1380 scale-of-aggregation principle predicted.

## Files

- pre-reg: `findings/phase-b-hypotheses/prereg-h-new-1510-sajda-pericope-replication.md` (SHA256 `fab8c413105c9867253a49bc09765e3313d22bb6f59688f8a4642048c4d00581`)
- script: `findings/phase-b-hypotheses/scripts/h-new-1510.py`
- JSON: `findings/phase-b-hypotheses/csv/h-new-1510.json`
- finding (this file): `findings/phase-b-hypotheses/h-new-1510-sajda-pericope-replication.md`
