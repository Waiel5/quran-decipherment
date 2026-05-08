---
finding_id: Q020-F-02
title: Q 20 Ṭā Hā second-person-singular density — Ibn ʿAbbās vocative interpretation test
date: 2026-05-07
seed: 20260507
phase: B+
specialist: Q020-ta-ha-specialist
bonferroni_k: 2
bonferroni_family: "second-person-singular density (vs corpus-mean, 2-tailed permutation) + 2nd-person-marker count (vs corpus z-score)"
alpha_bon: 0.025
direction_locked: greater (Q 20 2nd-person-singular density > corpus mean)
status: PRE-REGISTERED
---

# Q020-F-02 — Ibn ʿAbbās vocative test

## Background (classical claim)

al-Ṭabarī, *Jāmiʿ al-bayān*, on Q 20:1, reports Ibn ʿAbbās's interpretation of طه as a vocative meaning "O man" (rajul) in some Hijāzī / Nabaṭī / ḥabashī dialects. Other interpretations include divine-name initials (al-Ḥasan al-Baṣrī), simple muqaṭṭaʿāt (al-Suyūṭī's epistemic humility — *Itqān* nawʿ 40), and "ṭāhir hādī" (Saʿīd b. Jubayr).

If the vocative reading is correct, Q 20:1-2 = "O man, We have not sent down the Quran upon you that you should suffer." This would imply the body of Q 20 sustains a 2nd-person-singular address.

## Hypothesis (direction-locked)

Q 20's body (vv. 2-135) has 2nd-person-singular addressee density GREATER than the corpus mean.

Markers (no-tashkeel orthographic, whole-word):
- ك- pronoun-suffix at verse end or post-verb (kāf as 2sg-obj/poss).
- أنت (anta — 2sg subject pronoun)
- إياك (iyyāka — 2sg accusative)
- 2sg verb forms: تقول (taqūl), تخش, تخف, ترى, لتشقى ending pattern, تذكرة (general — excluded — only verbal-2sg-forms accepted).

Practical operationalization: count tokens matching:
- whole-word `\bانت\b`, `\bأنت\b`
- whole-word `\bاياك\b`, `\bإياك\b`
- final-consonant ك attached to a verb-stem → approximated by: ANY token ending in ك of length ≥ 4 (this captures `قلنالك`, `عليك`, `لتشقى` etc. — ك-suffix proxy)
- Direct 2sg verbs: تشقى, تخشى, تذكر(?), ترى — case-by-case excluded; we use the ك-suffix proxy + أنت + إياك as the locked metric.

Density metric: `count(2sg-tokens) / total_word_count`.

## Pre-committed thresholds

- **PASS**: Q 20 density z ≥ +1.5 vs corpus null (114 surahs); permutation p ≤ 0.025 (Bonf-2).
- **DIRECTIONAL**: Q 20 density z ≥ +1.0 but p > 0.025.
- **NULL**: Q 20 density z < +1.0.

Permutation null: 10000 random shuffles of all word tokens across the corpus into surah-sized bags; recompute Q 20 density.

## Rules-tuple

`(no-tashkeel, orthographic-token, graphemes, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)`.

## Honest limits

- The ك-suffix proxy will include some 2-plural (kum) and 2-feminine (ki) forms; this is a length-of-suffix-1 noisy proxy. It applies UNIFORMLY to every surah, so the cross-surah comparison is fair.
- The vocative-interpretation hypothesis is more general than 2sg-density. A NULL on this test does NOT falsify the Ibn ʿAbbās interpretation; it only fails to support it on this particular metric.
- Specifically excludes 2pl forms because the vocative would be 2sg ("O man" not "O people").
