---
id: H-NEW-61
title: Surah opening-word distribution — comprehensive analysis of first non-muqaṭṭaʿāt word per surah
status: PRE-REGISTERED 2026-04-15
spec_locked_at: 2026-04-15 (taxonomy + extractor locked BEFORE any distributional counting; allowed to consult JSON structure, not first-word content beyond MW-5 surahs)
bonferroni_family: 2026-04-15-Wave-H-NEW-61-Opening-Words
bonferroni_k: 6
alpha_bon: 0.05 / 6 ≈ 0.00833
rules_tuple: (no-tashkeel, hafs-kufan, canonical-114, Tanzil-JSON, 29-muqaṭṭaʿāt-set, opener=first word-token AFTER any muqaṭṭaʿāt-letter string AND AFTER basmala)
primary_data: /Users/grey/Downloads/quran/quran-text/quran-no-tashkeel.json
chronology: /Users/grey/Downloads/quran/data/revelation-order.csv
morphology: /Users/grey/Downloads/quran/data/morphology/quranic-corpus-morphology-0.4.txt (POS enrichment only)
seed: 20260416
author: h-new-61-specialist
---

# [[h-new-61-opening-words|H-NEW-61]] — Surah Opening-Word Distribution

## Questions

1. For each of 114 surahs, what is the first WORD (after any muqaṭṭaʿāt opener and after basmala for Q1)?
2. What is the distribution of opening words? Which are most common? Which particles, vocatives, praise-words dominate?
3. Are there exact opening-word matches across surahs (twin-openers)?
4. Does opening-word class correlate with (a) surah length, (b) Meccan/Medinan, (c) muqaṭṭaʿāt status?
5. What about the FIRST-3 incipit — exact matches of (w1, w2, w3)?

## Classical anchor — al-Suyūṭī's Itqān nawʿ on *fawātiḥ al-suwar*

al-Suyūṭī in *al-Itqān fī ʿulūm al-Qurʾān* enumerates 10 classical types of surah openings: (i) praise (*ḥamd/subḥāna*), (ii) muqaṭṭaʿāt, (iii) vocative (*yā-ayyuhā*), (iv) conditional/temporal (*idhā*), (v) report (*qad*, *innā*), (vi) imperative (*qul*), (vii) oath (*wa-/tā-/la*), (viii) negation (*mā*), (ix) exclamatory (*wayl*), (x) interrogative (*a-/hal*). This typology is the target taxonomy, adapted where modern philological counting admits cleaner cuts.

## Garden-of-forking-paths disclosure (pre-test)

Before running distributional tests I already know from Qurʾān memorisation / project context:
- Q1 al-Fātiḥa opens *al-ḥamdu lillāh* (PRAISE) — after skipping basmala if present.
- Q6 al-Anʿām, Q18 al-Kahf, Q34 Sabaʾ, Q35 Fāṭir open with *al-ḥamdu lillāh* (5 total *al-ḥamd* openers — this is the MW-5 confirmation).
- Q17 al-Isrāʾ and Q87 al-Aʿlā open with *subḥāna/sabbiḥ* (praise-family PRAISE extended).
- Q19 Maryam after muqaṭṭaʿāt opens with *dhikru raḥmati rabbika* — starts with *dhikru* (report-type).
- Q4 al-Nisāʾ, Q5 al-Māʾidah, Q22 al-Ḥajj, Q33 al-Aḥzāb, Q49 al-Ḥujurāt, Q65 al-Ṭalāq, Q66 al-Taḥrīm, Q60 al-Mumtaḥina, Q73 al-Muzzammil, Q74 al-Muddathir open with vocative *yā-ayyuhā* (VOCATIVE).
- Q109 al-Kāfirūn, Q112 al-Ikhlāṣ, Q113 al-Falaq, Q114 al-Nās all open with *qul* (IMPERATIVE).
- Q2, Q3, Q29, Q30, Q31, Q32 open with muqaṭṭaʿāt then *dhālika/ALLĀH/ḥasiba/al-ḥamdu/tanzīlu*.
- Q81 al-Takwīr, Q82 al-Infiṭār, Q84 al-Inshiqāq, Q99 al-Zalzala, Q100 al-ʿĀdiyāt, Q101 al-Qāriʿa open with *idhā* or oath *wa-* (conditional/oath).
- Q38 Ṣād, Q50 Qāf open with muqaṭṭaʿāt letter then *wa-l-qurʾāni* (oath).

The MW-5 positive control (5 *al-ḥamd* openers Q 1, 6, 18, 34, 35) is explicitly pre-registered before running any code.

These known facts DO NOT bias the distributional χ² because the taxonomy is set apriori and the counting mechanism is mechanical from the locked extractor. Twin-incipit matches will be entirely mechanical.

## Locked opening-word extractor (binding, frozen HERE)

For each surah S:
1. Load verses from `quran-no-tashkeel.json`.
2. If S == 1 (al-Fātiḥa): the basmala IS v1 and IS liturgically part of the surah, but for the Itqān "opening" question the convention is to count al-ḥamdu (v2:1). So for S1 the opener is the first word of v2 = *al-ḥamdu*. Rationale: other surahs' basmala is not v1; we treat the basmala structurally equivalent across all 114 surahs.
3. For all other surahs (S != 1), concatenate verses in order into a word stream.
4. If the surah is in MUQATTAAT_SURAHS = {2, 3, 7, 10, 11, 12, 13, 14, 15, 19, 20, 26, 27, 28, 29, 30, 31, 32, 36, 38, 40, 41, 42, 43, 44, 45, 46, 50, 68} (29 surahs), then SKIP the muqaṭṭaʿāt letter-tokens from the head of the word stream.
   - Muqaṭṭaʿāt tokens are detected as the leading contiguous run of single- or multi-letter isolated-letter strings (after tashkeel removal); the detection list is:
     `{الم, المص, الر, المر, كهيعص, طه, طسم, طس, يس, ص, حم, عسق, ق, ن}` (= the 14 unique muqaṭṭaʿāt openers documented in standard classical sources; note عسق follows حم in Q42, treated as a two-opener run).
   - Specifically for Q42 (حم / عسق spans verses 1 and 2): the extractor skips BOTH muqaṭṭaʿāt tokens and takes the first word of v3 as the opener.
5. First non-muqaṭṭaʿāt, non-punctuation, non-basmala word in the stream is the **opener** (word-1 or w1).
6. The next two words are w2 and w3. (w1, w2, w3) = the **incipit triple**.
7. Tashkeel-normalize: strip all tashkeel marks, collapse أ إ آ ٱ ء → ا, ة → ه, ى → ي. Store BOTH raw and normalized forms.

This extractor is mechanical and fully deterministic once the muqaṭṭaʿāt token-list is fixed (and it IS fixed here).

## Locked opening-word taxonomy (9 classes, frozen before run)

Each opener maps to exactly ONE of:

1. **PRAISE** — *al-ḥamd*, *ḥamd*, *subḥān*, *sabbaḥa*, *yusabbiḥu*, *tabāraka*
2. **VOCATIVE** — starts with *yā* (*yā-ayyuhā*, *yā-banī*, *yā-nisāʾ*, bare *yā*)
3. **CONDITIONAL_TEMPORAL** — *idhā*, *idh*, *yawma*, *ḥīna*, *law*
4. **OATH_PARTICLE** — *wa-* + noun (ex: *wa-l-qurʾān*, *wa-l-fajr*, *wa-l-layl*, *wa-l-tīn*), *ta-llāh*, *la-* swearing, *fa-wa-*
5. **IMPERATIVE** — *qul*, *iqraʾ*, *anẓur*, *dhakkir*, *iʿbud*, *ādhan*, *adhin*, *ādhinhum*, *baligh*
6. **REPORT_ASSERTIVE** — *qad*, *innā*, *inna*, *tanzīl*, *tabāraka* (if reading as "blessed-is-who" report rather than praise — here we route tabāraka to PRAISE; then the report cases are *innā*, *inna*, *qad*, *tanzīl*, *ḥāʾ-mīm-tanzīl*, *al-qāriʿa*, *al-ḥāqqa* = noun-report "X is Y" style)
7. **DEMONSTRATIVE_PRONOMINAL** — *dhālika*, *tilka*, *hādhā*, *huwa*, *allāh* (bare "Allāh..." as subject)
8. **INTERROGATIVE_NEGATIVE** — *hal*, *a-*, *mā*, *a-lam*, *a-lā*, *limā*, *li-maʾa*
9. **OTHER_CONTENT** — content noun not matching above (e.g., *dhikru*, *sūratun*, *al-ḥāqqa*, *al-qāriʿa*, *iqtarabat*, *iqrabat*)

**Tie-breaker** (in case one opener matches two classes): priority order is as listed above (PRAISE > VOCATIVE > CONDITIONAL > OATH > IMPER > REPORT > DEMONSTRATIVE > INTERROG > OTHER). Tabāraka → PRAISE.

**Classification is on the RAW opener-token**, with Arabic-definite-article and common prefixes stripped before matching (i.e., *wa-l-qurʾān* → prefix *wa-* triggers OATH_PARTICLE even if the rest is *al-qurʾān*).

## Pre-registered test cells (Bonferroni k=6, α_bon ≈ 0.00833)

### Cell 1 — Descriptive opener distribution
Tabulate (a) top-10 most frequent EXACT opening-word strings (normalized), (b) 9-class distribution. PASS = published table.

### Cell 2 — MW-5 *al-ḥamd* control
Assert that {Q1, Q6, Q18, Q34, Q35} ALL have opener ∈ {*al-ḥamd*, *al-ḥamdu*} (normalized). Count must equal 5/5. This is the positive-control tautology (MW-5). Expected p ≪ 10⁻⁶.
- PASS = all 5 classical *al-ḥamd* surahs correctly identified.

### Cell 3 — Non-uniform opener-class distribution (χ²)
Null: 9 classes are uniformly distributed over 114 surahs (expected ≈ 12.67 per class). Test: χ² goodness-of-fit. Pool any classes with expected count < 5 only if they arise (expected cells ≈ 12.67 so pooling unlikely).
- α_bon = 0.00833.
- PASS = χ² p < 0.00833 (opener-class is non-uniform).
- Expected to pass trivially; this is a baseline sanity check, not a novelty claim.

### Cell 4 — Opener-class × Meccan/Medinan Fisher exact
For each class with ≥ 3 instances, build a 2×2 (class-Y/N × Meccan/Medinan) table and run Fisher's exact, two-sided. Report per-class p-values. Within-Cell-4 Bonferroni by number of tested classes.
- α_per_class = 0.00833 / k_classes.
- PASS_per_class = p < α_per_class.
- Cell-4 VERDICT: REPORT per-class pass/fail. Aggregate "any class passes" flagged separately.
- Pre-registered prediction (from H-NEW-31 and Itqān): VOCATIVE skews Medinan; PRAISE skews neither; CONDITIONAL/OATH skews Meccan.

### Cell 5 — Opener-class × muqaṭṭaʿāt-opener status
Same structure as Cell 4, but replace Meccan/Medinan with muqaṭṭaʿāt-opener (Y/N). Bonferroni within cell.
- Pre-registered prediction: REPORT_ASSERTIVE (tanzīl-style) and OATH_PARTICLE enriched in muqaṭṭaʿāt-opener surahs; VOCATIVE enriched in non-muqaṭṭaʿāt-opener surahs.

### Cell 6 — Twin-incipit (exact (w1,w2,w3) match) count
Build (w1, w2, w3) normalized tuples for all 114 surahs. Count the number of distinct tuples that appear ≥ 2 times (= twin-incipit groups) and the size of the largest. Also count TWIN-W1 (shared first-word only) separately.
- Null model: permute opener-tuples within the corpus and re-count twin-groups. 10⁴ permutations. Compute empirical p for observed twin-count.
- One-sided (observed > expected under permutation).
- α_bon = 0.00833.
- PASS = empirical p < 0.00833 (i.e., observed twin-incipit count is extreme under the null of re-assignment).

## Opener-length/period correlation (Cell 4 extra analysis, inside Cell 4 Bonferroni)

Length: number of verses per surah (from JSON). Compute Spearman ρ of opener-class (one-hot per class) vs log(verse_count). Reported descriptively only; no separate Bonferroni cell.

## POS tagging (descriptive enrichment, NOT a test cell)

For each opener w1, attempt to look up its POS in the QAC morphology file by (surah, verse, word) location. Report POS distribution. Descriptive only; no p-value.

## MW-5 positive control

Cell 2 IS the MW-5: all 5 *al-ḥamd* openers (Q 1, 6, 18, 34, 35) must be correctly identified. If Cell 2 fails, the extractor is broken and ALL other cells are invalidated.

## Null models (summary)

- Cell 2: deterministic; no random.
- Cell 3: analytical χ².
- Cell 4, Cell 5: Fisher exact analytical + within-cell Bonferroni.
- Cell 6: 10⁴ permutations (seed 20260416) of opener-tuples re-assigned to surah-ids; empirical p.

## Pre-committed verdict table

| Outcome | Verdict |
|---|---|
| Cell 2 fails | EXTRACTOR_BROKEN (invalidate all) |
| Cell 2 passes, Cell 3 sig | baseline non-uniformity CONFIRMED |
| Cell 4 any class passes Bonferroni | period-opener correlation |
| Cell 5 any class passes Bonferroni | muqaṭṭaʿāt-opener correlation |
| Cell 6 sig | twin-incipit anomaly (opening repertoire is non-random) |
| Cell 6 null | twin-incipit count is ordinary under the lexicon |
| All post-2 cells null | openers non-uniform but no structural correlate |

## Integrity

- Taxonomy + extractor locked HERE before reading the first-word list beyond MW-5 surahs.
- Bonferroni k=6 declared.
- Cell 2 is explicit MW-5 tautological control.
- Seed 20260416.
- Author: [[h-new-61-opening-words|h-new-61]]-specialist.
