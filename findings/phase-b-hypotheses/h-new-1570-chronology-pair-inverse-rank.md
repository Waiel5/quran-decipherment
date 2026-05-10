---
finding_id: H-NEW-1570
title: "Chronology-paired surahs inverse-rank lexical-key principle (corpus-wide formalization)"
date: 2026-05-10
status: NULL (locked criterion not met) — informative single-pair confirmation
parent_finding: Q068-F-06
verdict: NULL
prereg_sha: 911bdda399a7abec7da27c32d2231b2ca4a746327881771d20ef94839054a955
---

# H-NEW-1570 — CHRONOLOGY-PAIRED SURAHS INVERSE-RANK LEXICAL-KEY PRINCIPLE

## TL;DR

The Q068-F-06 observation that Q 96 (rev #1) holds rank-1 by *qlm* density and Q 68 (rev #2,
title-bearer) holds rank-2 — chronology-adjacent pair, inverse-rank — is an **isolated
structural coincidence**, NOT a corpus-wide principle. Of 5 chronology-adjacent pairs tested
under pre-committed direction, **only the parent pair satisfies** the strict inverse-rank
criterion. **VERDICT: NULL** under the locked ≥3-of-5 success rule.

A subtle but important secondary observation: the single hit IS surprising under a random null
(p = 0.0004), which means **Q068-F-06 remains a striking isolated finding**, just not a
generalizable principle.

## Pre-registered hypothesis (locked SHA: `911bdda3…`)

For each chronology-adjacent revelation pair (n, n+1) where the LATER-revealed surah is
title-eponymous, the EARLIER-revealed surah should hold rank-1 (and the LATER hold rank-2) in
the corpus-wide density ranking of the LATER surah's title-root.

Five pairs locked from `data/revelation-order.csv` (Tanzil Egyptian + Nöldeke):

| # | early (rev) | later (rev) | title-root | category |
|:-:|:--|:--|:-:|:--|
| 1 | Q 96 al-ʿAlaq (1) | Q 68 al-Qalam (2) | `qlm` | parent finding (Q068-F-06) |
| 2 | Q 73 al-Muzzammil (3) | Q 74 al-Muddaththir (4) | `dvr` | singleton-root |
| 3 | Q 1 al-Fātiḥa (5) | Q 111 al-Masad (6) | `msd` | singleton-root |
| 4 | Q 81 al-Takwīr (7) | Q 87 al-Aʿlā (8) | `Elw` | rich-root, no early-Q attestation |
| 5 | Q 93 al-Ḍuḥā (11) | Q 94 al-Sharḥ (12) | `$rH` | mid-N root, no early-Q attestation |

Success criterion (LOCKED): ≥3 of 5 pairs satisfy rank_early=1 AND rank_later=2 AND
density_early > density_later, AND permutation p < 0.01 (Bonferroni k=5).

## Result

Per-pair (full table at `csv/h-new-1570.json`):

| pair | early rank | early count | early dens/1000 | later rank | later count | later dens/1000 | strict |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| Q96 → Q68 [qlm] | **1** | 1 | 20.41 | **2** | 1 | 5.24 | **YES** |
| Q73 → Q74 [dvr] | 74 | 0 | 0.00 | 1 | 1 | 6.17 | no |
| Q1 → Q111 [msd] | 2 | 0 | 0.00 | 1 | 1 | 58.82 | no |
| Q81 → Q87 [Elw] | 85 | 0 | 0.00 | 2 | 1 | 20.41 | no |
| Q93 → Q94 [$rH] | 94 | 0 | 0.00 | 1 | 1 | 62.50 | no |

- **n_strict_observed = 1 / 5** (threshold for PASS: ≥3)
- **permutation p (n_strict ≥ 1) = 0.0004** (10,000 perms, seed 20260509)
- **null mean (strict) = 0.0004** — getting EVEN ONE pair satisfying the strict criterion is
  rare under a random pairing of surahs.

**VERDICT: NULL** under the locked ≥3-of-5 criterion. The principle does NOT generalize.

## Pre-committed acknowledgment (transparency)

The pre-reg explicitly acknowledged BEFORE observation that 3 of 5 pairs (2, 3, 5) had
structurally impossible early-density (the title-root is a singleton or near-singleton with
zero attestations in the early-pair surah), and pair 4 was likely similar. The pre-reg framed
this as a **falsification attempt** of the corpus-wide claim. The result confirms the
falsification: Q068-F-06 is isolated.

## Why pair 1 is still striking (informative-NULL)

Although the verdict is NULL on the locked corpus-wide criterion, the single pair (Q 96 ↔ Q 68)
that DOES satisfy is itself a low-probability event:

- Under random pairing, the chance that the pair selected as (early, later) for a single locked
  root holds rank-1 AND rank-2 in that root's density ranking is approximately 2 / (114 × 113)
  ≈ 1.55 × 10⁻⁴ per pair.
- The observed null mean across 10,000 permutations is 0.0004 hits across 5 pairs — i.e.
  expected 0.0004, observed 1.
- This is a ~2500× enrichment over expectation for pair 1 alone — but it is a SINGLE pair,
  and the pre-committed gate required ≥3 pairs.

## Interpretation

Two things can be true simultaneously:

1. **Q068-F-06 is genuinely surprising** (Q 96 rank-1 + Q 68 rank-2 in *qlm*-density is a
   ~10⁻⁴ event for a randomly chosen pair).
2. **Q068-F-06 is NOT a corpus-wide principle** — the other four chronology-adjacent pairs
   that should also exhibit the pattern under the locked operationalization do not. The
   parent finding is a *qalam-specific* phenomenon, not a structural law of chronology-pair
   architecture.

The most likely explanation: *qalam* (the pen) has a particular semantic gravity in early
revelation — it appears in the FIRST revealed verse (Q 96:4 — *alladhī ʿallama bi-l-qalam*)
AND becomes the title of the SECOND revealed surah (Q 68). The Q 96 verse contains the only
*qalam* attestation in its surah; Q 68 takes the root for its title and oath-opening but
exhibits LOWER density. This is plausibly a **narrative thematic continuity** between the
first two revealed surahs rather than a general inverse-rank law.

The other four candidate pairs lack this narrative continuity:
- Pair 2 (al-Muzzammil → al-Muddaththir): both are Form-V participle vocatives but the roots
  *zml* and *dvr* are mutually exclusive singletons.
- Pair 3 (al-Fātiḥa → al-Masad): al-Fātiḥa is a liturgical opening; al-Masad is a polemic
  against Abū Lahab. No shared *msd* vocabulary.
- Pair 4 (al-Takwīr → al-Aʿlā): apocalyptic scene → divine-name praise. No shared *Elw*.
- Pair 5 (al-Ḍuḥā → al-Sharḥ): consolation-pair (both addressed to the Prophet at low ebb).
  Q 94 opens with *na-shraḥ* but Q 93 does not invoke *sharḥ*.

The pattern Q068-F-06 captures is therefore better described as: **a single chronological
keyword-bridge between the first two revealed surahs**, not a structural principle of
chronology-pair architecture.

## Rules-tuple and replication

- `(no-tashkeel, QAC v0.4 ROOT, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)`
- Seed 20260509, n_perm = 10000
- Replication: pair 1 = Q068-F-06 exact replication (passes)
- Out-of-sample: pairs 2-5 all fail
- Bonferroni k=5, α_bon = 0.01

## Limits and honest caveats

- The locked operationalization is BLIND to whether the root is corpus-rare. Pairs 2-5 used
  singleton-or-near-singleton roots that geometrically excluded inverse-rank.
- A more permissive variant — "title-root density ranking, early-pair has > 0 attestations" —
  would have eliminated pairs 2, 3, 5 ex ante. But that would be post-hoc; we publish the
  locked result.
- The single positive (pair 1) is sufficient to keep Q068-F-06 standing as an isolated
  finding, but H-NEW-1570 itself is **NULL** as a corpus-wide claim.

## Files

- Pre-reg: `findings/phase-b-hypotheses/prereg-h-new-1570-chronology-pair-inverse-rank.md` (SHA `911bdda3…`)
- Script: `findings/phase-b-hypotheses/scripts/h-new-1570.py`
- Data: `findings/phase-b-hypotheses/csv/h-new-1570.json`
- Parent: `surahs/Q068-al-qalam/preregs/Q068-F-06-qlm-root-density-rank-prereg.md`
- This file: `findings/phase-b-hypotheses/h-new-1570-chronology-pair-inverse-rank.md`

## Verdict line

H-NEW-1570 is published as **NULL** with equal prominence. The corpus-wide chronology-pair
inverse-rank lexical-key principle is **NOT** supported by the locked 5-pair test
(n_strict = 1, threshold = 3). The parent finding Q068-F-06 remains a **striking isolated
2-surah phenomenon** (p ≈ 0.0004 under the random null), not a generalizable law.
