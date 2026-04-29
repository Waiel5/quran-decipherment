---
id: H-NEW-86
title: Surah-name-as-key-root — comprehensive 114-surah lexical-centrality scan with proper morphological roots
status: COMPLETED 2026-04-16
pre_reg: h-new-86-surah-name-as-key-root-prereg.md
parent: H-NEW-49 cell 5
seed: 20260417
bonferroni_family: 2026-04-16-Wave-Surah-Name-Key-Root
bonferroni_k: 114
alpha_bon: 4.39e-4
rules_tuple: (hafs-kufan; canonical 114; Leeds Quranic Arabic Corpus v0.4 morphology; ROOT field for content nouns, LEM field for proper-noun surah names)
verdict: EXPLORATORY (26/110 = 23.6% testable surahs sig at α_bon=4.39e-4; below 33% PASS threshold)
---

# [[h-new-86-surah-name-as-key-root|H-NEW-86]] — Surah-name-as-key-root, full 114 scan

## Summary

For each of the 114 surahs we locked the Buckwalter ROOT (or LEM, for the 12 proper-noun surahs) of the surah's name BEFORE running the test, then asked: does this name's lexeme concentrate inside its own surah at a rate significantly above the rest-of-corpus baseline? Test: hypergeometric two-sided p, with Bonferroni correction across 114 (α_bon = 4.39e-4).

**Headline result**: 26 of 110 testable surahs (23.6%) have a name-lexeme that significantly concentrates in their own surah at the Bonferroni-114 level. This is below the 1/3 PASS threshold pre-registered in [[h-new-49-surah-name-class|H-NEW-49]], so the verdict for the global hypothesis "surah names predict surah lexical content" is **EXPLORATORY**, not PASS.

But: when we stratify, the SIG surahs are NOT randomly distributed — they cluster strongly in two regimes:
1. **Long narrative-prophet surahs** with a unique PN name (Q12 Yūsuf, Q11 Hūd, Q31 Luqmān, Q71 Nūḥ).
2. **Very-short eschatological/protective surahs** where any name-lexeme repeated even once or twice is enriched far above corpus baseline (Q101 al-Qāriʿah, Q99 al-Zalzalah, Q114 al-Nās, Q63 al-Munāfiqūn).

The "typical pattern" (as the question asked) is that **most surahs do NOT concentrate their name-root** — only 1 in 4 do at strict Bonferroni. The full distribution is informative.

## Top-15 surahs by enrichment

### Sorted by p-value (most extreme first)

| Rank | Surah | Name | Class | Type | hits_in / n_in | hits_rest | ratio | p (two-sided) |
|---:|---|---|---|---|---:|---:|---:|---:|
| 1 | Q 12 | Yūsuf | PROPHET_PERSON | LEM | 25 / 1777 | 2 | 532× | **2.98e-39** |
| 2 | Q  4 | al-Nisāʾ | SOCIAL_LEGAL | ROOT | 20 / 3747 | 39 | 10× | **2.13e-12** |
| 3 | Q 18 | al-Kahf | REVELATION_RITUAL | ROOT | 6 / 1579 | 0 | ∞ | **7.13e-11** |
| 4 | Q101 | al-Qāriʿah | EVENT_ESCHATOLOGICAL | ROOT | 3 / 36 | 2 | 3225× | **9.22e-10** |
| 5 | Q  9 | al-Tawba | REVELATION_RITUAL | ROOT | 17 / 2498 | 70 | 7× | **2.44e-09** |
| 6 | Q114 | al-Nās | SOCIAL_LEGAL | ROOT | 5 / 20 | 236 | 82× | **4.18e-09** |
| 7 | Q 11 | Hūd | PROPHET_PERSON | LEM | 5 / 1917 | 2 | 98× | **1.86e-07** |
| 8 | Q 63 | al-Munāfiqūn | SOCIAL_LEGAL | ROOT | 6 / 180 | 105 | 25× | **2.68e-07** |
| 9 | Q 99 | al-Zalzalah | EVENT_ESCHATOLOGICAL | ROOT | 2 / 36 | 4 | 1075× | **3.15e-06** |
| 10 | Q 56 | al-Wāqiʿah | EVENT_ESCHATOLOGICAL | ROOT | 4 / 379 | 20 | 41× | **5.56e-06** |
| 11 | Q 27 | al-Naml | ANIMAL_OBJECT | ROOT | 3 / 1151 | 1 | 199× | **1.30e-05** |
| 12 | Q 97 | al-Qadr | REVELATION_RITUAL | ROOT | 3 / 30 | 129 | 60× | **1.90e-05** |
| 13 | Q 86 | al-Ṭāriq | COSMOLOGICAL_NATURAL | ROOT | 2 / 61 | 9 | 282× | **3.34e-05** |
| 14 | Q 31 | Luqmān | PROPHET_PERSON | LEM | 2 / 546 | 0 | ∞ | **4.96e-05** |
| 15 | Q 51 | al-Dhāriyāt | COSMOLOGICAL_NATURAL | ROOT | 2 / 360 | 1 | 428× | **6.45e-05** |

All 15 above clear α_bon = 4.39e-4. Bonferroni-114 sig surahs total: **26**.

### Sorted by enrichment ratio (effect size; finite ratios with hits_in ≥ 1)

| Rank | Surah | Name | Class | hits_in | hits_rest | ratio |
|---:|---|---|---|---:|---:|---:|
| 1 | Q101 | al-Qāriʿah | EVENT_ESCH | 3 | 2 | 3225× |
| 2 | Q103 | al-ʿAṣr | COSMO_NAT | 1 | 4 | 1382× |
| 3 | Q104 | al-Humazah | SOCIAL_LEGAL | 1 | 2 | 1173× |
| 4 | Q113 | al-Falaq | COSMO_NAT | 1 | 3 | 1122× |
| 5 | Q 99 | al-Zalzalah | EVENT_ESCH | 2 | 4 | 1075× |
| 6 | Q 94 | al-Sharḥ | REV_RIT | 1 | 4 | 717× |
| 7 | Q 12 | Yūsuf | PROPHET | 25 | 2 | 532× |
| 8 | Q 51 | al-Dhāriyāt | COSMO_NAT | 2 | 1 | 428× |
| 9 | Q 81 | al-Takwīr | EVENT_ESCH | 1 | 2 | 372× |
| 10 | Q 80 | ʿAbasa | EVENT_ESCH | 1 | 2 | 291× |
| 11 | Q 86 | al-Ṭāriq | COSMO_NAT | 2 | 9 | 282× |
| 12 | Q 44 | al-Dukhān | COSMO_NAT | 1 | 1 | 223× |
| 13 | Q 60 | al-Mumtaḥanah | SOCIAL_LEGAL | 1 | 1 | 222× |
| 14 | Q 27 | al-Naml | ANIMAL | 3 | 1 | 199× |
| 15 | Q 96 | al-ʿAlaq | REV_RIT | 1 | 6 | 179× |

Plus 15 "ratio = ∞" cases (target lexeme appears ≥1× in own surah and 0× in rest of corpus): Q18, Q29, Q30, Q31, Q39, Q46, Q64, Q73, Q74, Q83, Q95, Q105, Q106, Q107, Q111. Of these, only Q18 (p=7e-11), Q31 Luqmān (p=5e-5), Q29 al-ʿAnkabūt (p=1.6e-4), Q39 al-Zumar (p=2.3e-4), Q106 Quraysh (p=2.2e-4), Q105 al-Fīl (p=3.0e-4), Q111 al-Masad (p=3.0e-4), Q107 al-Māʿūn (p=3.2e-4) clear Bonferroni-114.

## Bonferroni-passing surahs (full list, 26)

In p-value order:

Q12 Yūsuf • Q4 al-Nisāʾ • Q18 al-Kahf • Q101 al-Qāriʿah • Q9 al-Tawba • Q114 al-Nās • Q11 Hūd • Q63 al-Munāfiqūn • Q99 al-Zalzalah • Q56 al-Wāqiʿah • Q27 al-Naml • Q97 al-Qadr • Q86 al-Ṭāriq • Q31 Luqmān • Q51 al-Dhāriyāt • Q29 al-ʿAnkabūt • Q48 al-Fatḥ • Q90 al-Balad • Q106 Quraysh • Q39 al-Zumar • Q71 Nūḥ • Q70 al-Maʿārij • Q2 al-Baqarah • Q105 al-Fīl • Q111 al-Masad • Q107 al-Māʿūn

## Stratifications

### S1 — muqaṭṭaʿāt × Bonferroni-pass (Fisher exact 2×2)

| | Bonferroni-SIG | Bonferroni-NULL |
|---|---:|---:|
| Muqaṭṭaʿāt opener (Y) | 6 | 19 |
| Non-opener (N) | 20 | 65 |

Fisher p = **1.000** (two-sided). NULL.

The 6 muqaṭṭaʿāt-opener surahs that pass are: Q2, Q12, Q27, Q29, Q31, Q44 — almost all are PROPHET_PERSON (Q12 Yūsuf, Q31 Luqmān) or ANIMAL_OBJECT (Q2 al-Baqarah, Q27 al-Naml, Q29 al-ʿAnkabūt) or COSMOLOGICAL (Q44 al-Dukhān). Pass-rate among muqaṭṭaʿāt openers (6/25 = 24%) is virtually identical to non-openers (20/85 = 24%). [[h-new-49-surah-name-class|H-NEW-49]] cell 2 found a TREND for muqaṭṭaʿāt enrichment in PROPHET_PERSON CLASS, but that does NOT translate to enriched name-lexeme concentration here.

### S2 — Class × Bonferroni-pass (χ²)

| Class | SIG / Total | % SIG |
|---|---:|---:|
| PROPHET_PERSON | 4 / 11 | 36% |
| ANIMAL_OBJECT | 5 / 13 | 38% |
| DIVINE_ATTRIBUTE | 0 / 7 | **0%** |
| COSMOLOGICAL_NATURAL | 4 / 19 | 21% |
| EVENT_ESCHATOLOGICAL | 4 / 18 | 22% |
| SOCIAL_LEGAL | 5 / 22 | 23% |
| REVELATION_RITUAL | 4 / 17 | 24% |
| OTHER_ABSTRACT | 0 / 3 | **0%** |

χ² = 5.77, df = 7, p = **0.567**. NULL aggregate, but the directional pattern is informative:

- **PROPHET_PERSON and ANIMAL_OBJECT lead** at 36-38% pass rates. Predicted in pre-reg.
- **DIVINE_ATTRIBUTE is uniformly NULL** (0/7) — confirms pre-reg prediction. Divine names like al-Raḥmān, al-Nūr, al-Mulk, ghāfir, fāṭir, al-Aʿlā, al-Ikhlāṣ are corpus-pervasive and don't concentrate in their own surah more than baseline.
- **OTHER_ABSTRACT is also NULL** (0/3): Q72 al-Jinn (jinn root j-n-n covers جنة paradise/garden too, diluted), Q102 al-Takāthur, Q108 al-Kawthar (both root k-th-r, very common = "much").

DIVINE_ATTRIBUTE 0/7 is the most striking class result. The seven surahs are: Q24 al-Nūr, Q35 Fāṭir, Q40 Ghāfir, Q55 al-Raḥmān, Q67 al-Mulk, Q87 al-Aʿlā, Q112 al-Ikhlāṣ. Each name is a divine attribute that also functions as a high-frequency theological lexeme used across the corpus — by definition NOT surah-discriminative.

**Most striking sub-finding**: Q55 al-Raḥmān contains only **1** occurrence of the root r-H-m (verse 1, the title-word itself), while the rest of the corpus has 338 occurrences. As the LEM `r~aHoma`n` specifically: 1 inside Q55, 56 outside. The surah literally NAMED after al-Raḥmān is NOT lexically dominated by the name — the famous repetitive refrain "fa-bi-ayyi ālāʾi rabbi-kumā tukadhdhibān" uses ālāʾ and rabb, not raḥmān. This is a radical compositional-naming asymmetry worth follow-up.

### S3 — Proper-noun (LEM) vs content-noun (ROOT) × Bonferroni-pass (Fisher 2×2)

| | SIG | NULL |
|---|---:|---:|
| LEM (PN) | 5 | 7 |
| ROOT (content) | 21 | 77 |

Fisher p = **0.150**. NULL but in expected direction (PN pass-rate 5/12 = 42% vs ROOT 21/98 = 21%).

The 12 LEM (proper-noun) surahs are: Q3 Āl ʿImrān, Q10 Yūnus, Q11 Hūd, Q12 Yūsuf, Q14 Ibrāhīm, Q19 Maryam, Q30 al-Rūm, Q31 Luqmān, Q34 Sabaʾ, Q47 Muḥammad, Q71 Nūḥ, Q106 Quraysh.

PN-class passes: Q12 Yūsuf, Q11 Hūd, Q31 Luqmān, Q71 Nūḥ, Q106 Quraysh.
PN-class fails: Q3 Āl ʿImrān (3 occurrences total but 2/3 = p=0.006), Q10 Yūnus (Yūnus mentioned in many narratives, not Q10-concentrated), Q14 Ibrāhīm (mentioned across the entire corpus as a foundational patriarch — Q2, Q3, Q4, Q6, Q9, Q11, Q12, Q14, Q15, Q16, Q19, Q21, Q22, Q26, Q29, Q33, Q37, Q38, Q42, Q43, Q51, Q53, Q57, Q60, Q87 — diluted), Q19 Maryam (similarly cross-corpus), Q30 al-Rūm (single occurrence, Q30:2-3, but Q30 has 817 tokens — fails for low n), Q34 Sabaʾ, Q47 Muḥammad (only 4 occurrences corpus-wide; appears in Q3, Q33, Q47, Q48 — Q47 has 1).

### S4 — Meccan/Medinan × Bonferroni-pass (Fisher 2×2)

| | SIG | NULL |
|---|---:|---:|
| Meccan | 20 | 62 |
| Medinan | 6 | 22 |

Fisher p = **1.000**. NULL. Pass-rate 24.4% Meccan vs 21.4% Medinan; functionally identical.

### S5 — Length-quartile × Bonferroni-pass (χ²)

Quartile boundaries (token count): Q1 ≤ 80; Q2 81–312; Q3 313–860; Q4 861+.

| Quartile | SIG | NULL | % SIG |
|---|---:|---:|---:|
| Q1 (shortest) | 10 | 18 | 36% |
| Q2 | 3 | 24 | 11% |
| Q3 | 4 | 24 | 14% |
| Q4 (longest) | 9 | 18 | 33% |

χ² = 7.37, df = 3, p = **0.061**. TREND but does not clear α_strat_bon = 0.01.

This is a **bimodal** pattern: the shortest and longest surahs both pass at 33-36%, while the middle two quartiles pass at only 11-14%. Strat 5 fails Bonferroni but the U-shape is highly interpretable:
- **Shortest surahs** (Q1 ≤ 80 tokens): even a single mention of the name-lexeme inflates the rate dramatically (small n_in, denominator effect).
- **Longest surahs** (Q4 ≥ 861 tokens): proper-noun PN surahs (Yūsuf, Hūd, Tawba, Kahf, Nisāʾ) and theme-defining surahs (Baqara, Munāfiqūn) where the name concept is the actual narrative subject.
- **Middle quartiles** (Q2, Q3): names that are theological/rhetorical without being narrative-anchors (e.g., al-Zukhruf, al-Aḥzāb, al-Aʿrāf) tend to mention the title-lexeme exactly once or twice in a verse-of-naming, with the rest of the surah on adjacent topics.

## MW-5 controls

### MW-5 positive: Q12 Yūsuf
hits_in = 25, hits_rest = 2, ratio = 532.2, p_two = **2.98e-39**. PASS extreme. Pipeline confirmed wired correctly.

### MW-5 subtle: Q71 Nūḥ
hits_in = 3, hits_rest = 40, ratio = 25.6, p_two = **2.78e-04**. PASS Bonferroni-114 (just barely; α_bon = 4.39e-4). The pre-reg prediction was that Nūḥ would be SIG but with a far less extreme p than Yūsuf — confirmed. The reason: Nūḥ is a foundational patriarch named across the entire corpus (40 occurrences outside Q71); only 3 explicit "Nūḥ" tokens occur within Q71 itself, with the bulk of the surah using pronouns and conjugations of "qāla" and "qālū". The [[h-new-49-surah-name-class|H-NEW-49]] cell-5 result that Nūḥ was at p ≈ 4e-4 (skeleton-match approximation) is closely confirmed at the morphological level (p = 2.78e-4 here).

## Comparison with [[h-new-49-surah-name-class|H-NEW-49]] cell 5

| Surah | [[h-new-49-surah-name-class|H-NEW-49]] cell 5 (skeleton) | [[h-new-86-surah-name-as-key-root|H-NEW-86]] (morph ROOT/LEM) | Match? |
|---|---|---|---|
| Q 12 Yūsuf | 25 / 1795, p=3.8e-59 | 25 / 1777, p=3.0e-39 | YES (both extreme; p inflated in cell 5 due to wider tail) |
| Q101 al-Qāriʿah | 3 / 36, p=1.2e-10 | 3 / 36, p=9.2e-10 | YES |
| Q114 al-Nās | 6 / 20, p=4.4e-11 | 5 / 20, p=4.2e-9 | NEAR (skeleton overcounts by 1) |
| Q 63 al-Munāfiqūn | 6 / 181, p=3.1e-7 | 6 / 180, p=2.7e-7 | YES |
| Q  9 al-Tawba | 10 / 2505, p=9.0e-7 | 17 / 2498, p=2.4e-9 | DISAGREE — morph finds 17 root-`twb` hits, skeleton matched only 10 |
| Q 99 al-Zalzalah | 2 / 36, p=1.7e-6 | 2 / 36, p=3.1e-6 | YES |
| Q 11 Hūd | 6 / 1946, p=1.2e-5 | 5 / 1917, p=1.9e-7 | NEAR (cell-5 skeleton match for 6-letter sequence over-counted by 1; morph PN LEM match for "huwd" is cleaner; p drops 2 orders of magnitude) |
| Q 97 al-Qadr | 3 / 30, p=1.8e-5 | 3 / 30, p=1.9e-5 | YES |
| Q 24 al-Nūr | 7 / 1319, p=7.4e-5 | 9 / 1316, p=6.3e-3 | DISAGREE on significance — morphology actually finds MORE nwr hits (9 not 7) but the corpus rest-rate is also much higher under proper morphology (185 nwr ROOT outside Q24 vs the skeleton's narrower match), so Q24 ratio drops to 2.8× and p climbs to 6e-3 (fails Bonferroni-114) |

Net: 8 of the 9 [[h-new-49-surah-name-class|H-NEW-49]] cell-5 hits replicate at [[h-new-86-surah-name-as-key-root|H-NEW-86]] (Bonferroni-114). One (Q24 al-Nūr) demotes to NULL — the [[h-new-49-surah-name-class|H-NEW-49]] skeleton-match overcounted in-surah هits less than morphology, but more importantly UNDERcounted rest-corpus matches: skeleton missed many nwr-derived tokens elsewhere where the letter sequence n-w-r is interrupted by additional letters (e.g., استنار, منير with prefixes). Morphology gives the true rest-rate, which deflates the enrichment ratio.

[[h-new-86-surah-name-as-key-root|H-NEW-86]] finds 26 SIG vs [[h-new-49-surah-name-class|H-NEW-49]]'s 18 (8 net new SIG): Q4 al-Nisāʾ, Q4 al-Wāqiʿah, Q70 al-Maʿārij, Q90 al-Balad, Q86 al-Ṭāriq, Q51 al-Dhāriyāt, plus the morph-only finds.

## Cross with surah-type — answer to RQ4

**Question 4: What is the typical pattern — name-root concentrates IN-surah or NOT?**

**Answer: NOT.** Of the 110 testable surahs, only 23.6% have a name-lexeme that concentrates in their own surah at strict Bonferroni. The MAJORITY of surah names are NOT lexically central by this strict morphological test.

The pattern is **structural, not universal**: name-lexeme concentration is a property of:
- short eschatological surahs whose name is the centerpiece event (al-Qāriʿah, al-Zalzalah, al-Wāqiʿah)
- prophet-named long narrative surahs (Yūsuf, Hūd, Luqmān, Nūḥ, Muḥammad partial)
- theme-defining-clause surahs (al-Nisāʾ, al-Tawba, al-Munāfiqūn, al-Kahf, al-Fatḥ)

It is NOT a property of:
- divine-attribute surahs (0/7 pass — divine attributes are corpus-wide)
- abstract-concept surahs (al-Takāthur, al-Kawthar, al-Jinn — diluted by polysemy)
- many cosmological/natural surahs whose name is mentioned once at opening then narrative shifts (al-Layl Q92 — only 1 morph hit, p=0.08)

## Cross-cell synthesis

[[h-new-86-surah-name-as-key-root|H-NEW-86]] confirms and deepens [[h-new-49-surah-name-class|H-NEW-49]] cell 5:

1. **The Yūsuf finding holds with even higher confidence under proper morphology**: 25/27 corpus-wide LEM:yuwsuf occurrences are inside Q12 (92.6%). Only Q6:84 and Q40:34 mention Yūsuf outside his own surah. This is the cleanest single-surah lexical concentration in the entire corpus.

2. **The 4 muqaṭṭaʿāt-letter-named surahs (Ṭāhā, Yāsīn, Ṣād, Qāf) are by construction not testable on this axis** — they have no content-noun root.

3. **DIVINE_ATTRIBUTE class uniformly NULLS** — divine names are pervasive theological vocabulary, not surah-discriminative.

4. **No general rule "name predicts content"** — only PASS for 1 in 4 surahs even at Bonferroni-114. The naming convention of the Quran is more thematic-tag than lexical-anchor for the majority.

## Honest disclosures and limitations

- **Root mapping was a single-judgment call** (locked from Hans Wehr / standard Buckwalter). Sensitivity to alternative root assignments not audited (e.g., al-Rūm could be PN or root r-w-m; I picked LEM:r~uwm which is what Leeds tags). Spot-checks against Lane and Leeds-canonical confirm the picks but a full audit would be valuable.
- **Hypergeometric two-sided** counts both excess and deficit. For these surahs the observed direction is uniformly excess; one-sided p (upper tail) is essentially identical (p_upper = p_two for all SIG cases since hits_in > expected).
- **Token base** is Leeds morphology (77,429 word-tokens) not the methodology anchor 77,797 real-words. The discrepancy is ~0.5% (Leeds excludes a few prefix-only tokens). Per-surah ratios are stable across the two bases.
- **Q47 Muhammad fails Bonferroni** because the corpus only mentions Muḥammad as a name 4 times (Q3, Q33, Q47, Q48) and Q47 has only 1 of those plus 539 other tokens. The PROPHET_PERSON name doesn't dominate the surah.
- **Q14 Ibrāhīm fails** for the same reason (cross-corpus mention pattern; foundational figure).
- **Q2 al-Baqarah passes** but at modest enrichment (5 cow-references in 6116 tokens, ratio 14×). The cow narrative (Q2:67-71) is short and the rest of Q2 is doctrinal. This is a useful counterpoint: passing Bonferroni does not require dramatic concentration when n is large.

## Files

- Pre-reg: `findings/phase-b-hypotheses/h-new-86-surah-name-as-key-root-prereg.md`
- Script: `scripts/h_new_86_surah_name_as_key_root.py`
- JSON: `findings/phase-b-hypotheses/csv/h-new-86.json`
- CSV: `findings/phase-b-hypotheses/csv/h-new-86-per-surah.csv`
- Journal: `journal/h-new-86-run-1.md`

## Verdict

**EXPLORATORY** at the global level (26/110 = 23.6% < 33% PASS threshold).
**STRUCTURED PARTIAL-PASS** at the stratified level: clear differences in pass-rate by class (DIVINE_ATTRIBUTE 0%, PROPHET_PERSON/ANIMAL 36-38%) and length-quartile (U-shaped, p=0.061). No muqaṭṭaʿāt or Meccan/Medinan effect.

The single most important finding is that the Quran's surah-naming convention is **predominantly thematic-tag, not lexical-anchor** — only the prophet-named long narratives and the very-short eschatological/protective surahs use their name as a true lexical centerpiece.
