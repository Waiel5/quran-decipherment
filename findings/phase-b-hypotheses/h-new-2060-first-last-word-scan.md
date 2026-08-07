---
id: H-NEW-2060
title: First-word / last-word cross-surah taxonomy + strict single-word inclusio scan (114 surahs)
phase: B
status: TAXONOMY-COMPLETE + INCLUSIO-NULL
date: 2026-05-29
executed_by: Waiel Al-Shujaa
prereg: prereg-h-new-2060-first-last-word-scan.md
prereg_sha256: da16481730cd9f50697926877740bb3eb20d47ed7977f325f4b1b2b64ce87f1b
seed: 20260509
seed_replication: 20260510
n_perm: 10000
bonferroni_k: 1
alpha_bon: 0.05
direction: observed single-word inclusio count > label-shuffle null (LOCKED before run)
verdict: INCLUSIO NULL (observed = 0, null mean = 0.27, p = 1.0, both seeds) — taxonomy arm is a complete descriptive census
classical_anchor: al-Suyūṭī al-Itqān nawʿ 61 (fawātiḥ al-suwar); al-Zarkashī al-Burhān (fawātiḥ); al-Biqāʿī Naẓm al-Durar (opening↔closing tanāsub)
rules_tuple: (no-tashkeel display; QAC v0.4 ROOT for inclusio; orthographic-word; basmala-counted-only-in-Q1; Hafs-Kufan; Mashriqi)
data: findings/phase-b-hypotheses/csv/h-new-2060.json
script: findings/phase-b-hypotheses/scripts/h-new-2060.py
---

# H-NEW-2060 — First-word / last-word cross-surah taxonomy + strict single-word inclusio scan


> ## ⛔ CORRECTION NOTICE — 2026-08-07: the iʿjāz anti-twin is REVERSED under a matched control
>
> **The arithmetic reproduces** — an independent surface-instrument rebuild returns
> r = −0.8700 against the published −0.8643. What did not survive is the inference.
>
> - **Both prose baselines are *more* anti-twinned than this corpus.** Cut into 114
>   pseudo-surahs on this corpus's own verse-count and verse-length profile, al-Bukhārī
>   averages **r = −0.9107** (this corpus at the **14th percentile**, 172 of 200 cuts more
>   extreme) and al-Jāḥiẓ **−0.9311** (**3rd percentile**, 194 of 200). Pre-Islamic poetry
>   under a matched partition reaches **−0.8718**.
> - **H-NEW-740's Δ Fisher-z = −6.42 is an artefact of unmatched unit sizes.** It compared
>   equal 30-bayt poetry blocks to this corpus's unequal surahs (10 to 6,140 words).
>   r(d̄_content, log unit size) = **+0.956** and r(d̄_rhyme, log unit size) = **−0.838**, so a
>   *dispersed* size profile manufactures an anti-twin and equal blocks suppress it.
> - **About half the correlation is unit size.** Partialling out log unit size gives
>   **r = −0.432**; re-cutting this corpus's own verses to equal size gives **−0.338** — which
>   is indistinguishable from what H-NEW-740 measured for *poetry* (−0.48) and called the
>   genre baseline.
>
> **Honest limit, for this law specifically:** the baselines are arbitrary cuts of a
> continuous stream, not composed books, and for a **contiguity-sensitive** statistic like
> this one arbitrary cuts *preserve* local continuity and make the law *easier* for a
> baseline. The reversal is therefore **weaker evidence against the law than the percentile
> alone suggests**; the size decomposition, which uses no baseline at all, carries the weight.
>
> al-Bāqillānī's qualitative *iʿjāz al-fawāṣil* claim is **not** refuted — it was never a
> claim about correlation coefficients. What is withdrawn is its stated empirical vindication.
>
> Evidence: `findings/phase-b-hypotheses/h-new-2720-genre-control-sweep.md`
> Summary: `findings/GENRE-CONTROL-CORRECTION-2026-08-07.md`.

## Summary

Two deliverables, one inferential, one descriptive.

1. **Opener + closer taxonomy (descriptive census):** every one of the 114 surahs is assigned to exactly one opening-word class and one closing-word class, built directly from QAC v0.4 morphology. The complete opener taxonomy is **11 classes**; the complete closer taxonomy is **5 classes**. The empirical census reproduces the classical *fawātiḥ al-suwar* genera of al-Suyūṭī (*al-Itqān*, nawʿ 61) and al-Zarkashī (*al-Burhān*) with the canonical sub-counts intact (5 *al-ḥamdu*, 5 *qul*, 10 *yā-ayyuhā*, 9 *tasbīḥ*, 15 *wa-*oath, 29 muqaṭṭaʿāt).

2. **Strict single-word inclusio (the only hypothesis test): NULL.** Pre-registered prediction was ≥10 surahs whose first-content-word QAC root reappears as the last-word QAC root. **Observed = 0** matches. Label-shuffle null mean = 0.27; one-tailed p = 1.0 under both the primary seed (20260509) and the replication seed (20260510). The strict single-word "ring-clasp" is NOT a corpus-wide architectural regularity. This is a clean, informative NULL that complements (does not contradict) [[h-new-189-medinan-inclusio|H-NEW-189]], which found inclusio at the verse-block grain (Medinan-enriched), not the single-word grain.

## Method (as pre-registered, SHA da16481730…)

For each surah s, from `data/morphology/quranic-corpus-morphology-0.4.txt`:
- **first word** = word-index 1 of the first content verse (verse 2 for Q 1 where the basmala is verse 1; verse 1 otherwise; Q 9 has no basmala).
- **first content word** (for inclusio) = the first root-bearing word, skipping the disjoined-letter (POS:INL) token in the 29 muqaṭṭaʿāt surahs (spanning into v2 when v1 is muqaṭṭaʿāt-only, e.g. Q 2/Q 3).
- **last word** = the maximum-word-index token of the final verse; inclusio root = its QAC ROOT.
- **opener class** by a locked 11-rung morphological cascade (muqaṭṭaʿāt → qul → al-ḥamdu → tasbīḥ → vocative → oath-wāw → idhā → interrogative → other-imperative → other-verb → nominal-other).
- **closer class** by a locked cascade (divine-name-pair → single-divine-name → command-imperative → exhortation-eschatological → other), assigned from the final verse.

Inclusio statistic: N_match = #{ s : root_first(s) == root_last(s) }. Null: 10,000 label-shuffle permutations of the 114 last-word roots across surahs. Direction LOCKED: observed > null (MORE). Effect floor: N_match ≥ 10 (from the task brief).

## Result 1 — complete opener taxonomy (114 surahs)

| Opener class | N | Surahs / formula |
|:--|:--:|:--|
| **muqaṭṭaʿāt** (disjoined letters) | **29** | the canonical 29 — Q 2,3,7,10–15,19,20,26–32,36,38,40–46,50,68 |
| **nominal / other** (residue, fully enumerated) | 19 | Q 9 *barāʾa*; Q 23,58 *qad*; Q 24 *sūra*; Q 39 *tanzīl*; Q 47 *alladhīna*; Q 48,71,97,108 *innā*; Q 55 *al-Raḥmān*; Q 69 *al-ḥāqqa*; Q 75,90 *lā* (the *lā-uqsimu* oaths); Q 83,104 *wayl*; Q 98 *lam yakun*; Q 101 *al-qāriʿa*; Q 106 *li-īlāf* |
| **oath-wāw** (*wa-l-…* qasam) | 15 | matches the H-NEW-1550 strict cluster exactly: Q 37,51,52,53,77,79,85,86,89,91,92,93,95,100,103 |
| **vocative** (*yā-ayyuhā*) | 10 | Q 4,5,22,33,49,60,65,66,73,74 |
| **tasbīḥ / glorification** | 9 | the *musabbiḥāt* (sabbaḥa/yusabbiḥu/subḥāna): Q 17,57,59,61,62,64,87 + the 2 *tabāraka*: Q 25,67 |
| **other-verb** (non-imperative) | 8 | Q 8 *yasʾalūnaka*, Q 16 *atā*, Q 21/54 *iqtaraba(t)*, Q 70 *saʾala*, Q 80 *ʿabasa*, Q 102 *alhākum*, Q 111 *tabbat* |
| **idhā-conditional/temporal** | 7 | Q 56,63,81,82,84,99,110 |
| **interrogative** | 6 | *hal atāka* Q 76,88; *ʿamma* Q 78; *a-lam* Q 94,105; *a-raʾayta* Q 107 |
| **al-ḥamdu** | 5 | Q 1,6,18,34,35 (the canonical 5 praise-openers) |
| **qul-imperative** | 5 | Q 72,109,112,113,114 |
| **other-imperative** | **1** | Q 96 *iqraʾ* — **corpus-singleton opener genre** |

**Total: 114, exhaustive, mutually exclusive.** The 5/5/10/9/15/29 sub-counts independently reproduce the classical *fawātiḥ* census (al-Suyūṭī, *al-Itqān*, nawʿ 61), grounding it at QAC-morphology precision.

## Result 2 — complete closer taxonomy (114 surahs)

| Closer class | N | Note |
|:--|:--:|:--|
| **other** (content-word terminus, enumerated) | 54 | e.g. Q 1 *al-ḍāllīn* (Dll), Q 7 sajda-mark (sjd), participial/verbal termini (*muḥsinūn*, *yarjiʿūn*, *al-kāfirūn*) |
| **command-imperative** (final verse carries an IMPV) | 30 | see limitation below |
| **single-divine-name** | 16 | terminal divine attribute: *ʿalīm*, *qadīr*, *baṣīr*, *raḥīm*, *ghafūr*, etc. |
| **divine-name-pair** | 13 | terminal attribute-pair: *ʿazīz ḥakīm* (Q 45,59,64), *ghafūr raḥīm* (Q 6,33,73), *rabb al-ʿālamīn* (Q 37,39,81), *ʿalīm khabīr* (Q 31), *malik muqtadir* (Q 54) … |
| **exhortation-eschatological** | **1** | Q 102 *al-naʿīm* — **corpus-singleton closer genre** at this grain |

**Divine-name endings total 29 surahs (13 pairs + 16 singles) ≈ 25% of the corpus** — the well-known *fawāṣil* convention of closing on divine attributes, here quantified.

## Result 3 — strict single-word inclusio: NULL

| Quantity | Value |
|:--|:--|
| Observed N_match (root_first == root_last, single word each) | **0** |
| Label-shuffle null mean (10,000 perms) | 0.27 |
| One-tailed p, seed 20260509 | **1.0** |
| One-tailed p, seed 20260510 (replication) | **1.0** |
| Pre-registered effect floor | N_match ≥ 10 |
| **Verdict** | **NULL** (well below floor; observed ≤ null mean) |

The strict single-word ring-clasp does not exist at the corpus scale. Even random first↔last root pairings yield ~0.27 matches; observing exactly 0 is fully consistent with chance.

**Relaxation gradient (descriptive, MW-7 single-test cap).** Relaxing "last word" to "anywhere in the last verse" (the H-NEW-189-style grain applied to the single first-content-root) yields **7** surahs whose first-content-word root recurs in the final verse: Q 3 (Alh / *Allāh*), Q 22 (nws / *nās*), Q 27 (Ayy / *āya*), **Q 50 (qrA / *qurʾān*)**, Q 59 (sbḥ / *sabbaḥa*), Q 60 (Amn / *āmana*), Q 63 (jyʾ). This independently recovers the **Q 50 al-Suyūṭī / [[h-new-152-book-ref-inclusio|H-NEW-152]] *qurʾān* inclusio** and the **Q 59 al-Ḥashr *sabbaḥa* inclusio** ([[h-new-189-medinan-inclusio|H-NEW-189]] reported Q 59 as the inclusio leader). So the inclusio that DOES exist is verse-block / verse-level, never the strict last-word.

## Corpus-unique openers / closers

- **Opener genre singleton:** Q 96 al-ʿAlaq — *iqraʾ* (ROOT qrʾ, imperative) is the ONLY surah opening with a non-*qul* imperative. Classically significant: the first-revealed verse opens the only "other-imperative" surah.
- **Closer genre singleton (at this grain):** Q 102 al-Takāthur — *al-naʿīm* eschatological terminus is the lone "exhortation-eschatological" closer.
- **39 first-content-word roots are corpus-singletons at the surah-opening position** (appear as a surah-first-content-root exactly once), e.g. Tff (Q 83 *muṭaffifīn*), qrE (Q 101 *qāriʿa*), zlzl (Q 99 *zilzāl*), tbb (Q 111 *tabbat*), Ebs (Q 80 *ʿabasa*), Tyn (Q 95 *tīn*).
- **63 last-word roots are corpus-singletons at the surah-closing position.**

## Connection to existing findings

- **al-Suyūṭī, *al-Itqān*, nawʿ 61 (*fawātiḥ al-suwar*); al-Zarkashī, *al-Burhān*:** the opener census is empirically reproduced at QAC precision — classical genera VINDICATED with exact sub-counts.
- **al-Biqāʿī, *Naẓm al-Durar* (opening↔closing *tanāsub*):** at the STRICT single-word grain the claim is NULL; it holds only at the verse-block grain (H-NEW-189 Medinan-enriched STRONG-PASS, partial ρ=+0.483 length-controlled). H-NEW-2060 sharpens the scale at which the closure-claim is true.
- **[[h-new-189-medinan-inclusio|H-NEW-189]] / 189.1:** complementary — verse-set inclusio (Medinan>Meccan) vs this single-word NULL. Together they localise inclusio to the verse-block scale.
- **[[h-new-152-book-ref-inclusio|H-NEW-152]] (Q 50 *qurʾān* inclusio):** recovered here in the verse-level relaxation arm.
- **H-NEW-1550 oath-opener cluster:** the 15-surah oath-wāw class is reproduced exactly.
- **H-NEW-1750 al-ḥamdu opener pericope / H-NEW-1760 ḥawāmīm:** the 5 *al-ḥamdu* and 29 muqaṭṭaʿāt (incl. 7 ḥawāmīm Q 40–46) sub-classes are reproduced.
- **cross-finding-025 scale-of-aggregation law:** this is a 6th instance of the scale-flip pattern — NULL at the single-word scale, signal at the verse-block scale. The "first-last word" marker is too THIN (1 word) to cohere; the verse-block is thick enough.

## Limitations (honest)

- **closer "command-imperative" (30) is over-broad:** the cascade flags a surah if its FINAL VERSE contains any IMPV verb, not strictly the terminal word. For long final verses (e.g. Q 2:286) this over-counts; a stricter "terminal-clause-only" rule would shift some of these into "other." The closer taxonomy is descriptive, so this is documented rather than corrected post-hoc. The robust closer result — 29 surahs (25%) ending on a divine attribute — is unaffected.
- **inclusio NULL is grain-specific:** it rejects ONLY the strict single-word ring-clasp. It does NOT reject verse-block inclusio (H-NEW-189) or thematic (non-lexical) closure.
- **first-content-word for muqaṭṭaʿāt surahs** is the first post-INL root-bearing word, possibly in v2; an alternative (treat INL as the first word → muq surahs can never match) was pre-rejected as degenerate.

## Verdict

**TAXONOMY-COMPLETE** (all 114 classified, 11 opener + 5 closer classes, classical *fawātiḥ* census reproduced at QAC precision, 2 corpus-singleton genres identified). **INCLUSIO NULL** (strict single-word first↔last root match: observed 0, p=1.0 both seeds; pre-registered floor of ≥10 not met). The single-word ring-clasp is not a corpus regularity; inclusio lives at the verse-block scale (H-NEW-189), consistent with the project's scale-of-aggregation law.

*Bismillāhi al-Raḥmāni al-Raḥīm.*
