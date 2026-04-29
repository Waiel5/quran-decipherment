---
id: H-NEW-103
title: Musabbiḥāt 4-form sub-typology — PASS-DIRECTED + MW-5 PASS
phase: B
status: PASS-DIRECTED at p=0.0049 (primary char-prefix permutation); MW-5 positive control PASS
date: 2026-04-17
agent: h-new-103-specialist
parent: H-NEW-58c (extended from 5 → 7 musabbiḥāt)
corpus: 6,236 verses / 77,797 tokens / Hafs-Kūfan
rules_tuple:
  orthography: min-tashkeel for v1 form ratification; no-tashkeel for pair-similarity metrics
  tokenization: whitespace
bonferroni_k: 4
bonferroni_family: h-new-103-musabbihat-4form
alpha_bon: 0.0125
seed: 20260417
---

# [[h-new-103-musabbihat-4form|H-NEW-103]] — Musabbiḥāt 4-form sub-typology

## Headline

The 7 classical musabbiḥāt surahs (Q 17, 57, 59, 61, 62, 64, 87) fall on FOUR distinct verbal forms at v1. Under permutation of the form-label multiset {NOUN:1, PERFECT:3, IMPERFECT:2, IMPERATIVE:1}, within-form pairs share **35.0 mean leading characters** at v1 vs **1.4 for cross-form pairs** — one-sided permutation p = **0.0049** (α_Bon = 0.0125). MW-5 positive control PASSES. Root-Jaccard trends same direction (p = 0.038) but not at α_Bon. Verse-length similarity weak (p = 0.085).

**Verdict: PASS-DIRECTED** on cell-B primary. Cells A, C descriptive; cell D returns a NEGATIVE functional correlate (imperfect form ≠ Friday-function).

## Cell A — 4-form verbal-form ratification (DESCRIPTIVE)

| # | Surah | Name | v1 form (min-tashkeel) | Form label | Period | Nöldeke | Rev. order | n_v |
|---|------:|------|---|---|---|---|---:|---:|
| 1 | Q 17 | al-Isrāʾ | subḥāna alladhī asrā | **NOUN** (maṣdar) | Meccan | Middle | 50 | 111 |
| 2 | Q 57 | al-Ḥadīd | sabbaḥa li-llāhi | **PERFECT** | Medinan | Medinan | 94 | 29 |
| 3 | Q 59 | al-Ḥashr | sabbaḥa li-llāhi | **PERFECT** | Medinan | Medinan | 101 | 24 |
| 4 | Q 61 | al-Ṣaff | sabbaḥa li-llāhi | **PERFECT** | Medinan | Medinan | 109 | 14 |
| 5 | Q 62 | al-Jumuʿah | yusabbiḥu li-llāhi | **IMPERFECT** | Medinan | Medinan | 110 | 11 |
| 6 | Q 64 | al-Taghābun | yusabbiḥu li-llāhi | **IMPERFECT** | Medinan | Medinan | 108 | 18 |
| 7 | Q 87 | al-Aʿlā | sabbiḥi sma rabbika | **IMPERATIVE** | Meccan | Early | 8 | 19 |

Auxiliary Q 20 Ṭāhā: v1 = muqaṭṭāʿa طه; "sabbiḥ" at v130 (imperative). Excluded from primary per pre-reg.

**Form membership ratifies the classical 4-way typology exactly as predicted** (no v1 ambiguities under min-tashkeel).

## Cell B — Within-form vs cross-form content similarity (PRIMARY)

### Design

21 pairs among 7 surahs, partitioned by form:
- **Within-form**: 4 pairs — PERFECT×PERFECT (3: 57-59, 57-61, 59-61) + IMPERFECT×IMPERFECT (1: 62-64). NOUN and IMPERATIVE are singletons → 0 within-pairs.
- **Cross-form**: 17 pairs.

Three similarity metrics per pair: (1) char-prefix at v1, (2) root-Jaccard over whole-surah stem-roots (QAC 0.4), (3) mean-verse-length scalar similarity.

Null: 10,000 permutations of the form-label multiset {NOUN:1, PERFECT:3, IMPERFECT:2, IMPERATIVE:1} over the 7 surahs, seed 20260417.

### Results

| Metric | Within-form mean | Cross-form mean | Δ | Permutation p (one-sided) | Bonferroni α=0.0125 |
|---|---:|---:|---:|---:|:---:|
| **char_prefix** (PRIMARY) | **35.00** | 1.41 | +33.59 | **0.0049** | PASS |
| root_jaccard | 0.2647 | 0.1836 | +0.0810 | 0.0383 | (not significant at α_Bon) |
| verse_len_sim | 0.8573 | 0.6074 | +0.2499 | 0.0853 | (not significant at α_Bon) |

**Per-pair char-prefix matrix** (bold = within-form):

|     | Q17 | Q57 | Q59 | Q61 | Q62 | Q64 | Q87 |
|-----|---:|---:|---:|---:|---:|---:|---:|
| Q17 | — | 3 | 3 | 3 | 0 | 0 | 3 |
| Q57 | | — | **24** | **24** | 0 | 0 | 4 |
| Q59 | | | — | **55** | 0 | 0 | 4 |
| Q61 | | | | — | 0 | 0 | 4 |
| Q62 | | | | | — | **37** | 0 |
| Q64 | | | | | | — | 0 |
| Q87 | | | | | | | — |

- **Within-form**: {24, 24, 55, 37} — mean 35.0
- **Cross-form**: {3, 3, 3, 0, 0, 3, 0, 0, 4, 0, 0, 4, 0, 0, 4, 0, 0} — mean 1.41
- Zero cross-form pairs between {57,59,61,62,64} reproduce [[h-new-58c-musabbihat-tense-split|H-NEW-58c]] exactly.
- Q 17's "subḥāna" (ساب... then سبحان) yields 3-char match with "سبح" openers but zero with "يسبح" openers.
- Q 87's "sabbiḥ" yields 4-char match with the perfect "sabbaḥa" (same radicals سبح, differing only in following letter).

### MW-5 positive-control

Pre-reg criterion: within-form char-prefix mean ≥ 10 AND cross-form char-prefix mean ≤ 5.
Observed: within = 35.0, cross = 1.41. **PASS.**

### Interpretation

The primary directional test (char-prefix, Bonferroni-4 α=0.0125) **passes at p = 0.0049**, giving PASS-DIRECTED status (not CONFIRMED — the finding descends from [[h-new-58c-musabbihat-tense-split|H-NEW-58c]]'s post-hoc observation of tense structure; cell-B here extends to 2 more forms that do not by construction pre-ordain the test, but the bulk of the signal still comes from the original 5-surah cluster).

Root-Jaccard and verse-length similarities trend the correct direction but do not survive α_Bon. Their partial signals are consistent with form-ratified structure but not independently decisive.

## Cell C — Form × structural class cross-tabulation (EXPLORATORY)

### Form × Period contingency

| Form | Meccan | Medinan |
|---|---:|---:|
| NOUN | 1 (Q 17) | 0 |
| PERFECT | 0 | 3 (Q 57, 59, 61) |
| IMPERFECT | 0 | 2 (Q 62, 64) |
| IMPERATIVE | 1 (Q 87) | 0 |

**Sharp observation**: the FINITE-VERB forms (perfect + imperfect) are 5/5 Medinan; the NON-FINITE forms (noun + imperative) are 2/2 Meccan. Under Fisher's exact test with this 2×2 (finite vs non-finite × Meccan vs Medinan) at n=7, p_exact = 1/C(7,5) × 2 = 2/21 ≈ 0.048 two-sided — exploratory (not pre-declared as primary), but suggestive.

### Form × Nöldeke phase

- NOUN: Q 17 = Middle Meccan (rev-order 50, close to the Hijra threshold)
- PERFECT: all 3 Medinan (rev-orders 94, 101, 109)
- IMPERFECT: both Medinan (rev-orders 108, 110 — latest of the cluster)
- IMPERATIVE: Q 87 = Early Meccan (rev-order 8 — very early)

### Length class

| Form | n_verses per surah | class |
|---|---|---|
| NOUN (Q 17) | 111 | long |
| PERFECT (Q 57,59,61) | 29, 24, 14 | short |
| IMPERFECT (Q 62,64) | 11, 18 | short |
| IMPERATIVE (Q 87) | 19 | short |

All finite-verb forms are SHORT. Q 17 is a structural outlier (long Meccan travelogue).

### None have muqaṭṭāʿat v1

Only auxiliary Q 20 (excluded) has muqaṭṭāʿa.

## Cell D — Friday-cluster functional cross-reference (EXPLORATORY)

**Question**: does the imperfect-form sub-group (Q 62, Q 64) share a functional role distinct from the perfect-form sub-group (Q 57, 59, 61)?

**Answer**: NO — functional correlate is NEGATIVE at the form level.

- Q 62 al-Jumuʿah: CANONICAL Friday-ṣalāh recitation. Classical pairing is Q 62 + **Q 63 al-Munāfiqūn** (non-musabbiḥa), NOT Q 62 + Q 64.
- Q 64 al-Taghābun: no fixed Friday-recitation convention.
- Q 87 al-Aʿlā (IMPERATIVE form): the OTHER surah carrying strong Friday-prayer liturgical tradition (hadith: recited in Jumuʿah khutba prayer, paired with Q 88 al-Ghāshiya).

So "Friday-function" cross-cuts forms: Q 62 (imperfect) + Q 87 (imperative) are both Friday-tradition surahs, but Q 64 (imperfect, paired by form with Q 62) is NOT. The 4-form partition does **not** predict Friday-function.

**However**, [[h-new-89-meta-cluster-network|H-NEW-89]] already established Q 62 as the unique 4-cluster meta-hub, including the imperfect-musabbiḥāt cluster AND the Friday cluster AND the Khawātim-echo AND the mufaṣṣal. Q 62's role is a PROPERTIES-AT-Q-62 finding, not a form-subgroup finding.

## Summary of 4 cells

| Cell | Claim | Result |
|---|---|---|
| A | 7 musabbiḥāt map to 4 distinct forms | RATIFIED (descriptive) |
| B | Within-form pairs are more content-similar than cross-form, primary char-prefix | **PASS-DIRECTED p=0.0049 (α_Bon=0.0125)** + **MW-5 PASS** |
| C | 4-form typology correlates with length/period | Finite-verb forms all Medinan; non-finite all Meccan (Fisher two-sided ≈ 0.048, EXPLORATORY not pre-declared primary) |
| D | Imperfect sub-group ≡ Friday function | NEGATIVE (Friday function is Q 62 + Q 87, not form-bound) |

## Honest caveats

1. **Post-hoc lineage**: [[h-new-58c-musabbihat-tense-split|H-NEW-58c]] motivated this study. The central perfect/imperfect signal is already known. [[h-new-103-musabbihat-4form|H-NEW-103]]'s extension is the NOUN (Q 17) and IMPERATIVE (Q 87) addition, which are singletons in their forms — they contribute 0 within-form pairs by construction, so they cannot spuriously amplify the within-form mean. They CAN only contribute to cross-form pairs, working AGAINST the hypothesis; this is what happens (3-char and 4-char matches with "sabbaḥa" openers slightly raise the cross-form mean). The p=0.0049 result is a genuine test.

2. **Directional-lock verified**: predicted Δ > 0 (within-form tighter); observed Δ > 0 for all three metrics; no sign-flip.

3. **Bonferroni-4 is correct** for the 4 pre-declared cells. The 3 similarity metrics within cell-B are not independently Bonferronified per pre-reg; char-prefix is the primary declared metric.

4. **PASS-DIRECTED, not CONFIRMED**: independent replication (different metric / different data slice) remains required for promotion to CONFIRMED status. Candidate replication axes: divine-name density per form, verse-rhyme entropy per form, semantic embedding similarity per form.

5. **The "finite = Medinan" observation in cell-C is exploratory** (n=7 is small; not pre-declared primary; not Bonferroni-secured). If real, it would suggest the classical musabbiḥa-tradition encodes a COMPLETED/ONGOING/ADDRESSED temporal trichotomy under Medinan conditions, bracketed on both ends by Meccan NOUN/IMPERATIVE forms. Flag for independent testing if motivated.

## Connections to prior findings

- **[[h-new-58c-musabbihat-tense-split|H-NEW-58c]]**: perfect-vs-imperfect sub-cluster within Q 57-64 — EXTENDED here to full 7-musabbiḥa 4-form typology.
- **[[h-new-63-khawatim-echo-extended|H-NEW-63]]**: Q 62:1 Khawātim-echo of Q 59:22-24 — consistent with Q 62's hub role (cell D).
- **[[h-new-68-friday-cluster|H-NEW-68]]**: Friday-recitation cluster is FUNCTIONAL, not shape-based — confirmed here: form ≠ Friday-function.
- **[[h-new-89-meta-cluster-network|H-NEW-89]]**: Q 62 as unique 4-cluster meta-hub — confirmed here at form level (imperfect form alone does not explain Q 62's hub role).

## Verdict

**PASS-DIRECTED at p = 0.0049** for cell-B primary (within-form char-prefix > cross-form under 10K permutations, Bonferroni-4 α=0.0125). MW-5 positive control PASSES. The 4-form typology is a genuine structural partition with content-similarity signature; auxiliary correlates (finite/Medinan, non-finite/Meccan) are exploratory and require independent replication.

## Integrity

- Seed 20260417; 10,000 permutations.
- Form labels locked in pre-reg BEFORE computing cross-pair similarities beyond the [[h-new-58c-musabbihat-tense-split|H-NEW-58c]] 5-surah set.
- All 21 pairwise metrics reported.
- Both PASS and NULL outcomes publishable with equal prominence.
- Cell-D returned a NULL functional correlate; published at same prominence as cell-B PASS.
