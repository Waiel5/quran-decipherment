---
finding_id: Q049-F-01
H-NEW: H-NEW-1260
title: "Q 49 al-Ḥujurāt is the corpus-EXTREME on yā-ayyuhā-alladhīna-āmanū address-formula density"
date_pre_registered: 2026-05-09
status: PRE-REGISTERED
seed: 20260509
n_perm: 0 (corpus exhaustive enumeration; ranking against 95 surahs of length ≥ 10 verses)
bonferroni_k: 1
bonferroni_family: Q049-F-01-singleton-density
alpha_raw: 0.05
alpha_bon: 0.05
direction: "POSITIVE — Q 49 is hypothesized to be the corpus-rank-1 surah (length-controlled, surahs with verse-count ≥ 10) on per-verse density of the canonical Medinan address-formula yā-ayyuhā-alladhīna-āmanū."
rules_tuple: "(no-tashkeel, orthographic-token, exact substring match, basmala-not-counted, Hafs-Kufan, mushaf-order, length-control verse-count ≥ 10)"
---

# Q049-F-01 — yā-ayyuhā-alladhīna-āmanū address-formula density

## Hypothesis (LOCKED)

The opening formula `يا أيها الذين آمنوا` ("O you who have believed") is the canonical Medinan address-formula for the Muslim community. Across the Quranic corpus, it appears 89 times by exact substring (verified pre-test) and is **uniquely Medinan** in distribution (zero Meccan attestations under the standard 27-Medinan list).

The hypothesis: **Q 49 al-Ḥujurāt has the highest per-verse density of yā-ayyuhā-alladhīna-āmanū of any Quranic surah with verse-count ≥ 10**. This is operationalized as:

```
density(s) = count_amanu(s) / verse_count(s)
```

The threshold verse-count ≥ 10 is chosen because (i) most ultra-short Mufaṣṣal surahs are Meccan and contain zero amanu-formula instances (so the test would degenerate), (ii) it preserves a length-control comparator pool of ~95 surahs.

## Direction (LOCKED)

POSITIVE — Q 49 is hypothesized to **rank #1 of the comparator pool**, where the comparator pool = {114 surahs with verse-count ≥ 10}.

## Test family

Single test (k = 1). Not a Bonferroni-multiple-comparison family.

## Operationalization

1. Load `quran-text/quran-no-tashkeel.json`.
2. For each surah, strip mushaf pause/decorative marks (ۖ, ۚ, ۗ, ۘ, ۙ, ۛ, ۜ, ۞, ۤ).
3. Count exact substring `يا أيها الذين آمنوا` per verse; sum to surah-level count.
4. Compute density = count / verse_count.
5. Rank all 95 surahs (verse-count ≥ 10).

## Rules-tuple (LOCKED)

`(no-tashkeel, orthographic-token, exact substring match after Quranic-mark stripping, basmala-not-counted, Hafs-Kufan, mushaf-order, length-control verse-count ≥ 10)`

## Success criteria

| Metric | Predicted | Verdict |
|:--|:--|:--|
| Q 49 rank by density | 1 of 95 | **CONFIRMED** |
| Q 49 rank by density | 2 of 95 | PASS-DIRECTED-WEAK |
| Q 49 rank by density | 3-5 of 95 | PARTIAL |
| Q 49 rank by density | > 5 of 95 | NULL |

## Independent corpus-extreme check (secondary)

A secondary, post-hoc-flagged-IF-needed check: confirm that all 89 attestations are within the 27-Medinan list (i.e., zero Meccan attestations). This is a length-invariant categorical confirmation of the formula's Medinan-marker status.

## Honesty disclosures

- The Medinan-vs-Meccan classification used is the standard Hafs-Kufan attribution per al-Suyūṭī's *Itqān* nawʿ 1; alternative classifications (Nöldeke, al-Zarkashī edge cases) may shift 1-2 surahs across the boundary.
- Q 49 has 5 attestations of the formula in 18 verses (density 0.2778). The next-highest density is Q 60 al-Mumtaḥanah at 3/13 = 0.2308.
- This finding's "post-hoc origin" disclosure: density-ranking observed pre-test by visual inspection in dispatch brief; this pre-reg locks the test BEFORE numerically verifying Q 49 is rank-1 (the brief stated "verify root counts" without committing the rank).

## Related corpus claim

al-Suyūṭī (*Itqān* nawʿ 1) attributes the *yā-ayyuhā-alladhīna-āmanū*-formula entirely to Medinan provenance and notes it as a chief Medinan-marker. This pre-reg empirically tests his claim AND the surah-level density extreme.

## Output files

- Pre-reg: this file.
- Script: `scripts/Q049_F_01_amanu_density.py`.
- JSON: `csv/Q049-F-01.json`.
- Findings: `06-novel-findings.md` §Q049-F-01.
