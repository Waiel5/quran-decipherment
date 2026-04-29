---
id: H-NEW-44.3
title: Muqaṭṭaʿāt subset family — the "م-parallelogram" structure
phase: B
status: OBSERVED-ALGEBRAIC-FACT (extension of H-NEW-44; null deferred to H-NEW-44.1)
date: 2026-04-16
agent: integrator (main session)
parent: h-new-44-muqattaat-combinatorial-closure.md
script_inline: hand-computed Python (ad-hoc; verified by independent Gaussian elimination over GF(2) and ℝ)
rules_tuple: (no-tashkeel; structure independent of orthography/abjad)
---

# [[h-new-44-3-parallelogram-structure|H-NEW-44.3]] — The "م-parallelogram" sub-lattice in muqaṭṭaʿāt subsets

## Headline observation

The 14 muqaṭṭaʿāt subsets contain **two and only two non-trivial algebraic dependencies** (kernel dim = 2 over BOTH GF(2) and ℝ — the same kernel basis works for both fields):

### Dependency 1 — "ص-decoration"

```
ص ⊕ الم ⊕ المص = 0
```

In set language: **ص ∪ الم = المص** (and the symmetric difference vanishes because ص ∩ الم = ∅).

Surahs involved:
- ص = Q 38 (Sūrat Ṣād)
- الم = Q 2, 3, 29, 30, 31, 32 (the long الم-cluster)
- المص = Q 7 (Sūrat al-Aʿrāf, **uniquely**)

Reading: Q 7's opener is the disjoint union of Q 38's opener and Q 2-cluster's opener. Sūrat al-Aʿrāf "inherits" the disconnected-letter signature of Q 38 (Ṣād) layered on top of Q 2 (al-Baqara)'s signature.

### Dependency 2 — "م-parallelogram"

```
طس ⊕ الر ⊕ طسم ⊕ المر = 0
```

In set language, both pairs (طس, طسم) and (الر, المر) are **single-letter "add-م" edges in the powerset lattice**:

```
طس Δ طسم = {م}        (size 1 symmetric difference)
الر Δ المر = {م}       (size 1 symmetric difference)
```

This means {طس, طسم, الر, المر} form a **parallelogram in the 14-letter powerset lattice**:

```
     طس   ─add م→   طسم
                              
                              ↑ same letter م
                              
     الر  ─add م→   المر
```

Algebraically: the multiset XOR of all four subsets is zero because every letter appears in exactly 2 of the 4 subsets:
- س: in {طس, طسم} → 2
- ط: in {طس, طسم} → 2
- ا: in {الر, المر} → 2
- ر: in {الر, المر} → 2
- ل: in {الر, المر} → 2
- م: in {طسم, المر} → 2

Surahs involved (9 total):
- طس = Q 27 (Sūrat al-Naml)
- طسم = Q 26 (al-Shuʿarāʾ), Q 28 (al-Qaṣaṣ)
- الر = Q 10 (Yūnus), Q 11 (Hūd), Q 12 (Yūsuf), Q 14 (Ibrāhīm), Q 15 (al-Ḥijr)
- المر = Q 13 (al-Raʿd) — **uniquely**

## Surah-level reading

The "م-parallelogram" links four classically-distinguished surah groups:
- The al-Naml surah (Q 27) and the al-Shuʿarāʾ + al-Qaṣaṣ pair (Q 26, Q 28) are the **طس + م** triangle: Q 27 has طس, and the two surahs flanking it (Q 26, Q 28) have طس + م.
- The al-Raʿd surah (Q 13) sits **inside** the الر-cluster (Q 10–15) with the EXTRA letter م. This makes Q 13 the **unique Quranic surah** whose opener is الم + ر — analogous to how Q 26/28 are the unique surahs whose opener is طس + م.

The structural symmetry: both Q 13 and the Q 26/28 pair are "м-decorated" muqaṭṭaʿāt surahs sitting inside their respective base-cluster (الر vs طس). The base-clusters are non-overlapping (الر uses ا,ل,ر; طس uses ط,س), but the م-decoration mechanism is identical.

This is **previously unnoted** in classical or modern muqaṭṭaʿāt scholarship to the integrator's knowledge.

## Why ص-decoration is its own dependency, not a parallelogram

The first dependency (ص + الم = المص) is a 3-term relation, not a 4-term parallelogram. It works because:
- ص and الم are disjoint sets ({ص} ∩ {ا,ل,م} = ∅)
- Their disjoint union is المص = {ا,ل,م,ص}

There is no "ص-parallelogram" (i.e., no second pair of subsets in the family that differ by exactly {ص}). The only ص-Δ-relations involving the family are ص Δ المص = {ا,ل,م} (which is الم) and ص Δ كهيعص = {ك,ه,ي,ع} (a 4-letter set NOT in the family).

So the first dependency is a strict 3-term decomposition, while the second is a 4-term parallelogram.

## Significance — H-NEW-44.1 NULL update (2026-04-16)

Update from H-NEW-44.1 10K cardinality-matched uniform null: **rank-deficiency by exactly 2 (= 14 muqaṭṭaʿāt subsets having rank 12) is the second-most-common outcome under the uniform null (29.91% of random samples).** Modal null real-rank is 13 (50.43%); only 13.7% of random samples reach full rank 14.

Therefore the algebraic facts identified here (two kernel relations, one of which forms a parallelogram) are **statistically generic** for uniform random subset families with cardinalities [1,1,1,2,2,2,2,3,3,3,4,4,5,5]. The kernel-dim-2 result is NOT a "structural" surprise.

**What this REVISION changes:** the previously-stated reading "Q 13's anomaly is structurally load-bearing" is honestly downgraded. Q 13 IS algebraically-required to balance the 4-term parallelogram if we INSIST that the 14 subsets have rank exactly 12. But under random subset selection with these cardinalities, rank exactly 12 is generic. So the parallelogram is not a designed feature; it's a typical-feature.

**What SURVIVES the revision:** the Boolean decompositions and parallelogram are still REAL algebraic facts about the OBSERVED 14 muqaṭṭaʿāt subsets. They are not "designed" — they are typical for any 14-subset family with this cardinality distribution. The interpretation as "Q 7's opener is decomposable into Q 38's + Q 2-cluster's openers" is true as a set-equation, just not statistically surprising.

The qualitative reading — that the muqaṭṭaʿāt assignment exhibits clean inclusion chains and inheritance relations across surahs — remains a useful structural observation for tafsīr, but NOT a statistical signature of design.

## Consequences for the [[h-new-45-muqattaat-surah-index-number-theory|H-NEW-45]] cluster pattern (REVISED 2026-04-16)

Recall [[h-new-45-muqattaat-surah-index-number-theory|H-NEW-45]] confirmed the **gap-entropy clustering** (p = 2×10⁻⁵, z = −9.6): muqaṭṭaʿāt-opened surahs cluster in contiguous blocks. The biggest cluster (Q 10–15, the الر-cluster) is internally homogeneous EXCEPT for Q 13 (al-Raʿd, opener المر).

The PRE-REVISION reading proposed Q 13 as "algebraically load-bearing" via the parallelogram. This reading is RETRACTED in light of H-NEW-44.1 NULL. Q 13's المر is a real opener that pairs with the rest of the family in a parallelogram, but the parallelogram is not a designed feature — it's typical for cardinality-matched random families.

What remains valid: Q 13 is the SOLE المر surah, sitting INSIDE the contiguous الر-cluster (10-15). The clustering itself ([[h-new-45-muqattaat-surah-index-number-theory|H-NEW-45]] gap-entropy at p=2e-5) is the load-bearing finding. The internal heterogeneity of the cluster (Q 13's المر) is a SEPARATE phenomenon that the parallelogram correctly identifies algebraically but that does NOT signal design.

## Cross-finding (UPDATED 2026-04-16): muqaṭṭaʿāt structure across multiple axes

| Axis | Test | Verdict | Stat |
|---|---|---|---|
| Surah-position clustering | [[h-new-45-muqattaat-surah-index-number-theory|H-NEW-45]] gap-entropy | **PARTIAL-PASS** | p = 2×10⁻⁵ |
| Surah-length skew | [[h-new-46-muqattaat-vs-surah-length|H-NEW-46]] (4 cells) | **STRONG-PASS (4/4)** | p = 1×10⁻⁵ to 1.6×10⁻⁴ |
| Subset closure properties | H-NEW-44.1 (6 cells) | **NULL** | 0/6 sig at α=0.00833 |
| Subset-letter frequency | [[h-new-44-muqattaat-combinatorial-closure|H-NEW-44]] secondary | CONFIRMED | ρ = −0.54 (Welch 1986 quantified) |
| Subset-decomposition specifics | [[h-new-44-3-parallelogram-structure|H-NEW-44.3]] (this file) | OBSERVED-FACT (no surprise under null) | — |

**Updated conclusion:** The muqaṭṭaʿāt design is NON-RANDOM at the SURAH-LEVEL (clustering + length) but the SUBSET-COMBINATORIAL design is generic given the cardinalities. The 14 letter-set choices (with their cardinalities locked) could have been any cardinality-matched random family without changing the closure structure. But the ASSIGNMENT of these 14 subsets to specific surahs is highly non-random (clustered + length-skewed). Two-axis design.

## Garden-of-forking-paths

- The kernel-basis computation was straightforward Gaussian elimination; no tuple-shopping.
- The "parallelogram" interpretation of dependency 2 is the natural reading of a 4-term XOR=0 relation where two of the symmetric differences are size-1 with the same letter.
- The 9-surah involvement count (4 surahs from الر + Q 13 + Q 26 + Q 27 + Q 28) is direct enumeration.
- No null model was viewed when constructing this finding; H-NEW-44.1 will confirm whether parallelograms of this exact type are unusual under the cardinality-matched uniform null.

## Integrity

- Pure algebraic observation, no statistical claim.
- Falsifiable by H-NEW-44.1 if such parallelograms are common under uniform-random subset families.
- Reading of Q 13 as "structurally load-bearing" is interpretive but rests on the algebraic fact (Q 13 is the unique الر-cluster member contributing to the م-parallelogram).

## Prior art

No published muqaṭṭaʿāt analysis identifies the "م-parallelogram" structure to the integrator's knowledge:
- Welch 1986 catalogs letter frequencies, not lattice structure
- Massey 1996 proposes mnemonic readings, not algebraic ones
- Ibn ʿArabī esoteric letter-science treats subsets as combinatorial keys but without explicit GF(2) structure
- Modern academic studies (Sells, Mir, Saleh, Neuwirth) focus on stylistic and theological readings, not subset algebra

This is the first published recognition of the parallelogram structure to the integrator's knowledge.
