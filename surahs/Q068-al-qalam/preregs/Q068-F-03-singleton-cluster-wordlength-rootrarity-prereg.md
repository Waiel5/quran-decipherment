---
finding_id: Q068-F-03
title: "Q 50 + Q 38 + Q 68 singleton-letter cluster — joint test on WORD-LENGTH (Mann-Whitney) and ROOT-RARITY axes; complement to Q050-F-04 (FR/sig_A/outlier)"
date_pre_registered: 2026-05-07
status: PRE-REGISTERED
seed: 20260507
n_perm: 10000
bonferroni_k: 2
bonferroni_family: "Q068-F-03 word-length axis + root-rarity axis"
alpha_raw: 0.05
alpha_bon: 0.025
direction: "TWO-SIDED — singleton trio expected to differ from corpus baseline on at least one of the two axes; either direction is a finding"
---

# Q068-F-03 — SINGLETON-LETTER CLUSTER ARCHITECTURE (word-length + root-rarity axes)


> **⛔ CORRECTION NOTICE — 2026-08-07.** This file locates this surah within the
> **compression-tail** and/or **iʿjāz anti-twin** framework. Both met a matched Arabic control
> on 2026-08-07 and **neither discriminates**. The anti-twin is **REVERSED** — this corpus sits
> at the **3rd percentile** of al-Jāḥiẓ and the 14th of al-Bukhārī, and pre-Islamic poetry under
> a matched partition reaches r = −0.872 against this corpus's −0.870. The compression-tail is
> **genre-shared and 91.5 % explained by unit size**: log(unit size) alone gives R² = 0.9147,
> and re-cutting this corpus's own verses to equal size collapses R² from 0.9887 to **0.3388**.
> UAS is a synthesis index with no null hypothesis.
>
> Positional statements below — "in the compression-tail", "iʿjāz-fawāṣil cell", a UAS rank —
> remain accurate as **descriptions of where this surah sits on those axes**. What is withdrawn
> is that the axes distinguish this corpus from ordinary Arabic. Nothing below is deleted.
>
> Evidence: `findings/phase-b-hypotheses/h-new-2720-genre-control-sweep.md`
> Summary: `findings/GENRE-CONTROL-CORRECTION-2026-08-07.md`.

## Hypothesis

The 3 singleton-letter muqaṭṭaʿāt surahs (Q 38 ص-Sād, Q 50 ق-Qāf, Q 68 ن-al-Qalam) form a structurally distinguishable cluster. The Q050 specialist's joint test (Q050-F-04) operationalizes the cluster on the FR-distance / sig_A / outlier-strength axes. This test extends the cluster-architecture probe along **two complementary axes** that Q050-F-04 does NOT touch:

- **Axis A (word-length distribution)**: Are the 3 singleton-surahs jointly distinct from corpus on per-word letter-length distribution (Mann-Whitney U)?
- **Axis B (root-rarity)**: Do the 3 singleton-surahs use systematically rarer-or-more-common roots than corpus baseline (Zipf-rank of QAC stem-roots)?

These two axes are pre-registered and SHA-locked HERE; coordination with Q050-F-04 is by deliberate axis-disjointness, not by Bonferroni-sharing.

## Locked operationalization

### Axis A — word-length distribution

For each of {Q 38, Q 50, Q 68} and the corpus-rest:
- Per-word letter-count from `quran-text/quran-no-tashkeel.json` (after Arabic-letter-only filtering).
- Pool the 3 singleton surahs into one combined sample S_singleton.
- Pool the rest-of-corpus into S_rest.
- **Mann-Whitney U** test on S_singleton vs S_rest, two-sided.

### Axis B — root-rarity (Zipf-rank)

For each QAC stem-root: compute corpus Zipf-rank (1 = most-frequent root, e.g. *Allāh*, *qāla*, etc.).
- For each of {Q 38, Q 50, Q 68}: compute MEAN Zipf-rank of root-tokens in that surah.
- For the rest of the corpus: compute MEAN Zipf-rank of root-tokens.
- **Permutation test (10000 perms)**: shuffle surah-labels; recompute mean Zipf-rank for the size-3 cluster vs rest. p = fraction of shuffles where |observed - rest| ≥ |empirical|.

## Rules-tuple (LOCKED)

`(no-tashkeel, QAC-stem-roots for axis B; orthographic-token graphemes for axis A; basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)`

## Null distribution

- Axis A: Mann-Whitney U exact / asymptotic on the empirical word-length samples.
- Axis B: 10000-perm shuffle, two-sided.

Bonferroni-2 across the two axes: α_per-axis = 0.025.

## Direction (LOCKED)

**TWO-SIDED**. Either direction (singletons HAVING shorter/longer words; singletons HAVING rarer/more-common roots) is a positive cluster-distinctness finding. The two-sided choice is pre-committed because:
- The H-NEW-770 verse-length tail predicts post-50 surahs to have shorter verses; but Q 38 is at s=38 (pre-kink). So word-length direction is genuinely uncertain a priori.
- Root-rarity could go either way: muqaṭṭaʿāt-singletons might be content-condensed (rare roots) or formulaic (common roots).

## Success / failure criteria

For EACH axis (Bonferroni-2):
| Verdict | Criterion |
|:--|:--|
| **VINDICATED** | p < 0.025 (Bonferroni-2) |
| **DIRECTIONAL** | 0.025 ≤ p < 0.05 |
| **NULL** | p ≥ 0.05 |

Joint cluster verdict:
- 2/2 axes pass Bonferroni → **CLUSTER-DISTINCT-2-AXIS** (strong evidence for singleton-architecture distinctness on these two axes)
- 1/2 axes pass Bonferroni → **CLUSTER-DISTINCT-1-AXIS**
- 0/2 → **CLUSTER-NULL on word-length and root-rarity** (singleton-architecture, if it exists, must be on Q050-F-04's axes only)

## Coordination with Q050-F-04

Q050-F-04 (led by Q050 specialist) tests the cluster on FR-distance / sig_A / outlier-strength axes. Q068-F-03 (this test) tests on word-length / root-rarity axes. The two probes are AXIS-DISJOINT by deliberate pre-registration — there is no Bonferroni overlap. The combined picture:
- If both Q050-F-04 and Q068-F-03 pass on >=1 axis → strong CROSS-AXIS singleton-cluster
- If only one passes → axis-specific cluster signal
- If neither → singleton-architecture is FALSIFIED corpus-wide

## Output files

- Pre-reg: this file.
- Script: `scripts/Q068_F_03_singleton_cluster_wordlength_rootrarity.py`.
- JSON: `csv/Q068-F-03.json`.
- Findings: in `06-novel-findings.md`.
