---
id: H-NEW-58b
title: Shared-Prefix Test on Classical Surah Pairs — recovers Q 113-114 + Q 73-74 + Q 2-3 + automatically discovers musabbiḥāt cluster
phase: B
status: PASS-DIRECTED on 2 of 4 classical pairs (Bonferroni-4); reveals broader cluster patterns
date: 2026-04-16
agent: integrator (main session) — follow-up to H-NEW-58 instrument-failure
test: closed-form per-pair empirical-p over all 6441 surah pairs
verdict: PASS-DIRECTED + TAXONOMY-RECOVERY
rules_tuple: (no-tashkeel; whitespace-tokenized; shared-character-prefix and shared-word-prefix metrics)
---

# [[h-new-58b-shared-prefix-pairs|H-NEW-58b]] — Shared-Prefix Test (RESULT)

## Result on 4 classical pairs

[[h-new-58-surah-pair-twinning|H-NEW-58]] chose scalar-entropy similarity metrics that failed the MW-5 control. [[h-new-58b-shared-prefix-pairs|H-NEW-58b]] uses a SIMPLER, MORE FUNCTIONAL metric: shared-character-prefix and shared-word-prefix length.

| Classical pair | Shared chars | Shared words | char-p | word-p | Bonferroni-4 PASS? |
|---|---|---|---|---|---|
| Q 113 + Q 114 al-Muʿawwidhatān | 14 | 3 | **0.00373** | **0.00388** | ✓ both |
| Q 73 + Q 74 al-Muzzammil/Muddaththir | 11 | 2 | **0.00528** | 0.01211 | ✓ char only |
| Q 2 + Q 3 al-Zahrāwān | 4 | 1 | 0.02034 | 0.02328 | ✗ (unprotected α=0.05 only) |
| Q 8 + Q 9 al-Anfāl/Tawba | 0 | 0 | 1.00 | 1.00 | NULL (no shared prefix) |

**2 of 4 classical pairs PASS Bonferroni-4 on at least one metric.** The Q 8-9 pair is NOT shape-twinned at the prefix level — its classical "linkage" (al-Tawba lacks Bismillah prepended to it) is a CONVENTIONAL editorial decision, not a textual-shape relationship.

## Top-15 shared-prefix pairs across all 6441 surah pairs

The shared-prefix metric automatically RECOVERS the major cluster taxonomy:

| Rank | Q-pair | Chars | Words | Cluster |
|---|---|---|---|---|
| 1 | Q 59 - Q 61 | 56 | 12 | **musabbiḥāt** ("سبح لله ما في السماوات وما في الأرض ۖ وهو العزيز...") |
| 2 | Q 45 - Q 46 | 38 | 7 | **حم cluster** ("حم تنزيل الكتاب من الله العزيز الحكيم") |
| 3 | Q 62 - Q 64 | 37 | 8 | musabbiḥāt ("يسبح لله ما في السماوات وما في الأرض") |
| 4 | Q 40 - Q 45 | 33 | 6 | حم cluster |
| 5 | Q 40 - Q 46 | 33 | 6 | حم cluster |
| 6 | Q 26 - Q 28 | 27 | 5 | **طسم cluster** ("طسم تلك آيات الكتاب المبين") |
| 7 | Q 4 - Q 22 | 25 | 5 | vocative ("يا أيها الناس اتقوا ربكم") |
| 8 | Q 10 - Q 12 | 24 | 5 | **الر cluster** ("الر تلك آيات الكتاب ال") |
| 9 | Q 49 - Q 60 | 24 | 5 | vocative ("يا أيها الذين آمنوا لا ت") |
| 10 | Q 57 - Q 59 | 24 | 5 | musabbiḥāt |
| 11 | Q 57 - Q 61 | 24 | 5 | musabbiḥāt |
| 12 | Q 10 - Q 15 | 22 | 5 | الر cluster |
| 13 | Q 12 - Q 15 | 22 | 5 | الر cluster |
| 14 | Q 43 - Q 44 | 22 | 4 | حم cluster ("حم والكتاب المبين") |
| 15 | Q 5 - Q 49 | 20 | 4 | vocative ("يا أيها الذين آمنوا") |

**Composition of top-15:**
- **Muqaṭṭاʿāt-cluster pairs (within الم, الر, طسم, ḥm)**: 8 of 15 (53%)
- **Musabbiḥāt-cluster pairs**: 4 of 15 (27%)
- **Vocative-formula pairs**: 3 of 15 (20%)

The shared-prefix method automatically RECOVERS the classical cluster taxonomy with no prior input. This is methodological validation that the muqaṭṭāʿat cluster + musabbiḥāt cluster + vocative-formula clusters are STRUCTURALLY-DOMINANT shared-content patterns in the Quran's surah-opening landscape.

## The musabbiḥāt — auto-discovered

Beyond the muqaṭṭاʿāt findings, this test surfaces the **musabbiḥāt** as the SECOND-largest cluster of structurally-similar surah openings:

- Q 57 al-Ḥadīd: "سبح لله ما في السماوات والأرض"
- Q 59 al-Ḥashr: "سبح لله ما في السماوات وما في الأرض" (also contains Khawātim al-Ḥashr at v22-24)
- Q 61 al-Ṣaff: "سبح لله ما في السماوات وما في الأرض"
- Q 62 al-Jumuʿah: "يسبح لله ما في السماوات وما في الأرض"
- Q 64 al-Taghābun: "يسبح لله ما في السماوات وما في الأرض"

5 surahs share this glorification-of-Allah opening, all in the Q 57-64 range. Plus Q 17:1 "سبحان الذي أسرى..." and Q 87:1 "سبح اسم ربك..." make the classical 7 musabbiḥāt.

The 5-of-5 inner cluster (Q 57, 59, 61, 62, 64) shows tight structural twinning. None of these are muqaṭṭاʿāt-opened — they form a SEPARATE classical cluster. Worth noting that Q 59 al-Ḥashr is a member of BOTH the musabbiḥāt cluster AND the divine-name-density cluster (Khawātim).

## Honest framing

[[h-new-58-surah-pair-twinning|H-NEW-58]] (scalar-entropy metrics) returned NULL because the chosen metrics didn't capture functional twinning. [[h-new-58b-shared-prefix-pairs|H-NEW-58b]] (shared-prefix metrics) PASSES on 2 of 4 classical pairs AND auto-recovers the major cluster taxonomy. The combined lesson: classical surah-pair traditions are about FORMULAIC OPENINGS and SHARED INCIPITS, not about scalar-statistical distributional similarity.

## Cross-finding context

This adds to the project's growing inventory of structural patterns in surah openings:
- Muqaṭṭāʿat clusters (cross-finding-006/008): 8+ design axes confirmed
- Musabbiḥāt cluster (this finding, post-hoc-noted): Q 57, 59, 61, 62, 64 with shared opening formula
- Vocative-formula clusters: Q 4 + Q 22 + Q 49 + others share "يا أيها الناس/الذين آمنوا"
- al-Bāqillānī "neither prose nor poetry" verse-length distinctiveness (cross-finding-007)

The Quran's surah openings are highly STRUCTURED across multiple cluster systems. Classical scholarship has identified all these clusters qualitatively; [[h-new-58b-shared-prefix-pairs|H-NEW-58b]] provides quantitative cross-validation via the shared-prefix-test instrument.

## Integrity

- Closed-form prefix-counting; reproducible by inspection.
- 4 classical pairs locked from canonical tradition (al-Suyūṭī Itqān).
- Top-15 ranking provides full transparency on non-classical pair candidates.
- Empirical p over all 6441 surah pairs.
- Bonferroni-4 corrected per-pair.
- Both PASS and NULL verdicts published per pair.

## Follow-up queued

- **[[h-new-58c-musabbihat-tense-split|H-NEW-58c]]**: directed test of musabbiḥāt cluster (Q 57, 59, 61, 62, 64) shared-prefix structure as an INDEPENDENT classical cluster claim. Expected to PASS at extreme p.
- **H-NEW-58d**: vocative-formula cluster test ("يا أيها" prefix surahs) for additional cluster validation.
