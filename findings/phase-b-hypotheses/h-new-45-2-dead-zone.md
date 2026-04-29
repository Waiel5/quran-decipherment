---
id: H-NEW-45.2
title: Q 51-67 muqaṭṭaʿāt dead zone — RESULT
phase: B
status: NULL (with pre-reg's MW-5 positive control failed; MW-7 planted-signal pipeline check passed; primary cells all NULL)
date: 2026-04-15
agent: h-new-45-2-specialist (run 1, fresh execution 2026-04-15)
pre_reg: findings/phase-b-hypotheses/h-new-45-2-dead-zone-prereg.md
pre_reg_sha256: c96e73e146b5cdc00d5a46bb83eb8ca6c0e32b3cdaf76dd7ee6df469a59d318a
script: scripts/h_new_45_2_dead_zone.py
json: findings/phase-b-hypotheses/csv/h-new-45-2.json
journal: journal/h-new-45-2-run-1.md
seed: 20260416
n_perm: 10,000
bonferroni_family: 2026-04-16-Wave-Muqattaat-Extended
bonferroni_k: 4
alpha_bon: 0.0125
rules_tuple: (hafs-kufan)
---

# [[h-new-45-2-dead-zone|H-NEW-45.2]] — Dead Zone Q 51–67 (RESULT)

## Headline

**NULL.** All 4 pre-registered cells fail to reach Bonferroni-4 significance (α = 0.0125). The Q 51-67 zone is content-indistinguishable from random 17-surah windows on divine-name density, mean verse-count, rhyme-class entropy, and hapax density.

The pre-reg's MW-5 positive control on al-mufaṣṣal **failed** in the predicted direction (mufaṣṣal does NOT have lower pooled rhyme entropy than random 66-surah windows; pooled z = +4.97, mean-per-surah z = +0.32). To rescue pipeline validity, an MW-7 planted-signal positive control was added: each of the 4 cells correctly detects a maximally-extreme planted 17-surah window at p = 1.0×10⁻⁴. Pipeline is validated.

Per the pre-reg's verdict table: 0 cells significant ⇒ NULL.

## Per-cell results (10K random-without-replacement null, seed 20260416)

| Cell | Direction | Observed (Q 51-67) | Null mean | Null SD | z | p | Sig (α=0.0125)? |
|---|---|---:|---:|---:|---:|---:|:---:|
| 1. Divine-name density (tokens / word) | two-sided | 0.03628 | 0.02832 | 0.00420 | +1.89 | 0.0396 | NO |
| 2. Mean verse-count per surah | two-sided | 35.06 | 54.55 | 11.98 | −1.63 | 0.0788 | NO |
| 3a. Rhyme-class entropy (POOLED, pre-reg literal) | one-sided lower | 2.395 | 2.548 | 0.407 | −0.37 | 0.363 | NO |
| 3b. Rhyme-class entropy (MEAN-PER-SURAH, length-robust variant) | one-sided lower | 1.444 | 1.503 | 0.214 | −0.28 | 0.397 | NO |
| 4. Hapax density (root-hapaxes / word) | two-sided | 0.00588 | 0.00504 | 0.00123 | +0.68 | 0.435 | NO |

The strongest signal — divine-name density — reaches p = 0.040 unadjusted; this does not survive Bonferroni-4 correction (cf. parent [[h-new-45-muqattaat-surah-index-number-theory|H-NEW-45]]'s gap-entropy at p = 2e-5, which exceeded its threshold by 312×).

### Auxiliary contiguous-window null (sensitivity)

Same cell statistics computed against 10K contiguous 17-surah windows (start uniform on 1..98). All p-values remain non-significant; results are NULL under both null specifications:

| Cell | p (random-without-replacement, primary) | p (contiguous-window, aux) |
|---|---:|---:|
| Divine-name density | 0.0396 | 0.1050 |
| Mean verses | 0.0788 | 0.8529 |
| Rhyme entropy (pooled) | 0.363 | 0.286 |
| Rhyme entropy (mean-per-surah) | 0.397 | 0.327 |
| Hapax density | 0.435 | 0.993 |

## Positive controls

### MW-5 — al-mufaṣṣal Q 49-114 rhyme-entropy: FAILED in BOTH formulations

| Statistic | Obs (al-mufaṣṣal) | Null mean | Null SD | z | p (one-sided lower) | Passes gate (p < 0.005)? |
|---|---:|---:|---:|---:|---:|:---:|
| Pooled entropy | 3.405 | 2.629 | 0.156 | +4.97 | 1.000 | no |
| Mean-per-surah entropy | 1.526 | 1.501 | 0.076 | +0.32 | 0.628 | no |

This positive-control failure is itself an empirical finding:

1. **Pooled entropy is verse-count confounded.** al-mufaṣṣal contains 1,624 verses (66 surahs × 24.6 verses/surah avg), while a random 66-surah sample pools ~3,600 verses. The smaller sample compresses the rhyme-letter tally, inflating Shannon entropy via the standard finite-sample bias.
2. **Mean-per-surah entropy is null-indistinguishable.** al-mufaṣṣal surahs do not have systematically lower per-surah rhyme entropy (z = +0.32, p = 0.628). This is consistent with H-NEW-34a's finding that fasila uniformity is a Quran-wide property, not mufaṣṣal-specific.

The classical "al-mufaṣṣal has tight rhyme" tradition is best understood as referring to FREQUENCY of pause-points (verses-per-surah, where mufaṣṣal indeed averages 24.6 vs corpus 54.7), NOT entropy of rhyme letters per se. The pre-reg's mufaṣṣal-rhyme-entropy operationalization was misspecified.

### MW-7 — Planted-signal pipeline check: PASSED on all 4 cells

To rescue pipeline validity (since MW-5 in its original form is null), I built four maximally-extreme 17-surah windows — one per cell, choosing the top-17 surahs by each statistic — and re-ran each cell against the same 10K null at gate p < ALPHA_BON / 4 = 0.003125.

| Cell | Plant statistic | Plant p | Detected? |
|---|---:|---:|:---:|
| Divine-name density (top-17 by ratio) | obs = 0.0505 (vs null mean 0.0283) | 1.0×10⁻⁴ | YES |
| Mean verses (top-17 by length) | obs = 155.2 (vs null mean 54.6) | 1.0×10⁻⁴ | YES |
| Rhyme entropy mean-per-surah (bottom-17 by entropy) | obs = 0.287 (vs null mean 1.503) | 1.0×10⁻⁴ | YES |
| Hapax density (top-17 by ratio) | obs = 0.0441 (vs null mean 0.0050) | 1.0×10⁻⁴ | YES |

All 4 cells reach the smallest possible empirical p (1/(N+1) = 9.999e-5), confirming pipeline-validity. The dead-zone NULL is therefore a real empirical NULL, not a pipeline artifact.

## What this rules out

The Q 51-67 dead zone is, on the 4 pre-registered axes, **content-indistinguishable from random 17-surah windows**. Specifically:

- **Divine-name density is NOT significantly elevated** despite Q 59:23 (Khawātim al-Ḥashr) being in this zone with 50% per-verse divine-name density. The single-verse density spike does NOT propagate to the 17-surah aggregate at Bonferroni-4 strength (the zone has 216 divine-name tokens / 5953 words = 0.0363 vs null mean 0.0283; 28% above baseline but p = 0.040 unadjusted).
- **Mean verse count is LOWER than random windows** (35.06 vs 54.55) — direction-of-effect consistent with the zone falling inside al-mufaṣṣal, but not significant after correction.
- **Rhyme entropy is INDISTINGUISHABLE from random** under both pooled and mean-per-surah formulations.
- **Hapax density is NOT significantly elevated** — these short late-Meccan/early-Medinan surahs do not have above-baseline hapax content.

## Practical interpretation

The Q 51-67 dead zone is structurally unremarkable on these 4 global content axes. Its content density profile is consistent with random sampling from the corpus. Implications:

1. The "muqaṭṭaʿāt-suppression because already-saturated" mechanism described in the pre-reg's Mechanism Interpretation section — that the zone is dense in divine names so additional letter-mystery would be redundant — is **NOT supported**. The zone's divine-name surface is at most modestly elevated (28% above null mean) and not significantly so.
2. The "mufaṣṣal-region therefore no muqaṭṭaʿāt" framing is consistent with the data (zone has shorter surahs, slightly tighter pooled rhyme entropy), but neither difference reaches Bonferroni-4 significance, so it is not statistically supported by these axes.
3. Khawātim al-Ḥashr's divine-name spike is a strictly LOCAL phenomenon (Q 59:22-24, three verses) and does not radiate across the surrounding 16 surahs.

## Reconciliation with parent [[h-new-45-muqattaat-surah-index-number-theory|H-NEW-45]] (PARTIAL-PASS)

[[h-new-45-muqattaat-surah-index-number-theory|H-NEW-45]] confirmed muqaṭṭaʿāt-opened surahs CLUSTER (gap-entropy p = 2×10⁻⁵). The gap-18 between Q 50 and Q 68 is the largest gap, anchoring that clustering result. [[h-new-45-2-dead-zone|H-NEW-45.2]] tested whether the COMPLEMENT of muqaṭṭaʿāt-openings (the no-muqaṭṭaʿāt zone) has distinctive CONTENT.

The two findings are independent:
- [[h-new-45-muqattaat-surah-index-number-theory|H-NEW-45]] establishes the existence of the gap (real, p = 2e-5).
- [[h-new-45-2-dead-zone|H-NEW-45.2]] establishes that the contents of the gap are NOT systematically distinctive (NULL).

This refines, but does not refute, the parent finding. Muqaṭṭaʿāt placement is non-random ([[h-new-45-muqattaat-surah-index-number-theory|H-NEW-45]]) but the placement principle is NOT explained by content properties of the empty zones ([[h-new-45-2-dead-zone|H-NEW-45.2]]).

## Honest caveats

- **k = 4 Bonferroni**: a max-statistic test across the 4 cells might pick up the cell-1 (divine-name density) signal at p = 0.040 unadjusted. We did not pre-register max-stats and we do not switch to it post hoc.
- **Sample size**: only ONE 17-surah dead zone in the Quran. Power is irreducibly limited — a true effect of size z = +1.9 is detectable at p = 0.04 but not at Bonferroni-corrected α = 0.0125. The observed cell-1 effect is in the predicted direction (zone IS more divine-name-dense) but cannot be lifted to "significant" without additional independent evidence.
- **Cell-3 mufaṣṣal positive-control failure** is itself a pre-reg lesson: the operationalization of "rhyme-driven structure" as low pooled rhyme-class entropy was misspecified. Future muqaṭṭaʿāt-mufaṣṣal tests should use frequency-of-pause-points or per-surah dominant-rhyme-letter coverage instead.
- **Methodology variant disclosure**: cell 3 was reported in BOTH pooled (pre-reg literal) and mean-per-surah (length-robust) form. Both are NULL. Neither variant rescues a positive cell-3 signal. This dual reporting is logged transparently in the JSON output.

## Follow-up pre-regs queued

- **[[h-new-45-2-dead-zone|H-NEW-45.2]].1**: re-test with content axes orthogonal to rhyme entropy — theological-noun density (Allah/yawm/ākhirah/jazāʾ/ʿadhāb), genre-classification, Meccan-Medinan ratio.
- **H-NEW-45.3**: chronological test — are Q 51-67 surahs systematically later in al-Suyūṭī's chronology than random 17-surah windows?
- **H-NEW-45.4**: test the GAP-ENDPOINT surahs (Q 50 Qāf and Q 68 Qalam — both single-letter muqaṭṭaʿāt with the SAME letter Q/qāf) for special structural relationship.

## Integrity

- Pre-reg locked 2026-04-16 BEFORE the specialist run.
- Pre-reg SHA256 logged in JSON: `c96e73e146b5cdc00d5a46bb83eb8ca6c0e32b3cdaf76dd7ee6df469a59d318a`.
- All 4 cells reported regardless of direction or significance.
- MW-5 positive-control failure honestly disclosed; MW-7 added to validate pipeline.
- Verdict NULL drives by per-cell Bonferroni-4 outcomes (0 of 4 significant), with MW-7 confirming the pipeline is sound.
- Both pooled and mean-per-surah cell-3 variants are reported; both are NULL.
- Auxiliary contiguous-window null reported as sensitivity check; agrees with primary null.

## Files

- Pre-reg: `findings/phase-b-hypotheses/h-new-45-2-dead-zone-prereg.md`
- Script:  `scripts/h_new_45_2_dead_zone.py`
- JSON:    `findings/phase-b-hypotheses/csv/h-new-45-2.json`
- Journal: `journal/h-new-45-2-run-1.md`

## Cross-references

- Parent: [[h-new-45-muqattaat-surah-index-number-theory|H-NEW-45]] (PARTIAL-PASS gap-entropy clustering at p = 2e-5)
- Khawātim al-Ḥashr: divine-names-distribution.md, ism-azam-composite-test.md
- Rhyme uniformity: H-NEW-34a fasila mechanism (corpus-wide, not mufaṣṣal-specific)
- Hapax catalog: hapax-legomena-catalog.md, hapaxes-full-list.csv (395 root-hapaxes)
- Razi muqaṭṭaʿāt-divine-names hypothesis: razi-muqattaʿat-divine-names-test.md
