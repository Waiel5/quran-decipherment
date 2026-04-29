---
id: H-NEW-125
title: "Comprehensive chronology-content map — 15-axis Nöldeke correlation & phase-transition scan"
status: PRE-REGISTERED 2026-04-17
spec_locked_at: 2026-04-17 (axis list LOCKED BEFORE any correlations computed)
bonferroni_family: h-new-125-chronology-content
bonferroni_k: 15
alpha_bon: 0.00333  # 0.05 / 15
direction: 2-sided per axis
acceptance_window: "Spearman ρ(axis_per_surah, Nöldeke_rank) with permutation p < 0.00333 (10K perms) survives Bonferroni-15"
rules_tuple: (no-tashkeel, hafs-kufan, canonical-114, Tanzil-JSON for verse text, Leeds-QAC-v0.4 for morphology where used, Nöldeke-rank from data/revelation-order.csv column noldeke_order)
primary_text: /Users/grey/Downloads/quran/quran-text/quran-no-tashkeel.json
chronology: /Users/grey/Downloads/quran/data/revelation-order.csv  (column: noldeke_order = continuous rank 1..114)
morphology: /Users/grey/Downloads/quran/data/morphology/quranic-corpus-morphology-0.4.txt
asma_list:  /Users/grey/Downloads/quran/data/asma-al-husna.txt  (99 divine names; Tirmidhī canonical list)
loanwords:  /Users/grey/Downloads/quran/data/loanwords/jeffery-1938-loanwords.tsv  (218 Jeffery entries)
seed: 20260417
n_perm: 10000
author: h-new-125-specialist
prior_work_consulted:
  - findings/phase-b-hypotheses/chronological-revelation.md (H-NEW-46.1 length × phase ramp)
  - findings/phase-b-hypotheses/h-new-51-1-noldeke-replication.md (cardinality ρ=+0.54)
  - findings/phase-b-hypotheses/h-new-71-allah-distribution.md (Allah-density × phase; 6× Medinan jump)
  - findings/phase-b-hypotheses/h-new-74-qul-distribution.md (qul-density Late Meccan peak, KW p ≈ 10⁻⁷)
  - findings/phase-b-hypotheses/h-new-49-surah-name-classification.md (if present)
---

# [[h-new-125-chronology-content|H-NEW-125]] — Comprehensive Chronology-Content Map

## Question

**Do 15 content/structural axes of the Quran vary systematically with Nöldeke revelation rank?**
Which axes show monotone trends vs jump-discontinuities at phase boundaries?
Can we assemble a unified per-phase structural fingerprint (Early / Middle / Late Meccan / Medinan)?

## Motivation (OQ-12)

Five prior findings ([[h-new-46-1-chronology-disentangle|H-NEW-46.1]], -49, -51.1, -71, -74) each touched chronology on ONE axis.
No systematic cross-axis map exists. [[h-new-125-chronology-content|H-NEW-125]] closes that gap under a single pre-registered
Bonferroni-15 family.

## Axes (LOCKED 2026-04-17; NO POST-HOC ADDITIONS)

Each axis is computed PER SURAH (114 values). Spearman ρ vs Nöldeke rank; 2-sided permutation null.

| # | Axis | Operational definition |
|---|---|---|
| 1 | `surah_length` | number of verses in surah (Hafs-Kūfan canonical) |
| 2 | `mean_verse_length` | mean orthographic-token count per verse (no-tashkeel) |
| 3 | `muq_cardinality` | 0 for non-muqaṭṭāʿat surahs; cardinality = count of UNIQUE letters in the muqaṭṭāʿat opening for the 29 muqaṭṭāʿat surahs (e.g. الم → 3, حمعسق → 5) |
| 4 | `allah_density` | count of Allah-tokens ([[h-new-71-allah-distribution|H-NEW-71]] locked rule: {الله, لله, اللهم, آلله} + allowed proclitic prefixes) per 100 verses |
| 5 | `qul_density` | count of qul-imperatives (QAC: POS:V & IMPV & LEM:qaAla & 2MS) per 100 verses |
| 6 | `prophet_narrative_density` | count of surface tokens matching any of {موسى, عيسى, ابراهيم, نوح, يوسف, يونس, لوط, هود, صالح, شعيب, داود, سليمان, زكريا, يحيى, اسماعيل, اسحاق, يعقوب, ادم, ايوب, ادريس, الياس, اليسع, ذو, الكفل, فرعون, النبي, نبي, رسول, مرسل} per 100 verses; prefix-tolerant whole-word match |
| 7 | `legal_term_density` | count of surface tokens whose root (via QAC) is in {ktb (kitāb/ahl al-kitāb), Hkm (ḥukm), Amr (amr), nhy (nahy/nahā), frD (faraḍa)} per 100 verses |
| 8 | `eschatological_density` | count of surface tokens whose root (via QAC) is in {ywm (yawm = Day), Axr (ākhira), qwm (qiyāma via LEM filter), jhn~am (jahannam lemma), frds (firdaws lemma), nAr (nār), jn~ah (janna lemma)} per 100 verses; note: using lemma for 3 items to avoid root-homonym noise |
| 9 | `book_reference_density` | count of surface tokens whose root (via QAC) is in {ktb (kitāb/book), qrA (qurʾān/recite), Ayy (āyāt/signs-of-text), nzl (nazala/sent-down)} per 100 verses |
| 10 | `oath_density` | count of verses whose FIRST orthographic token starts with و + oath-lemma OR is exactly "و" prefix to one of {Al-Samāʾ, Al-Shams, Al-Layl, Al-Fajr, Al-Naḥl, Al-Tīn}; operationalised as: verse starts with surface-token matching regex `^و(?=.{2,})` AND QAC tags the first root as oath-class (heuristic: tokens starting with و followed by a noun at v_word_pos=1; true oaths are rare enough that this over-counts slightly — pre-committed as a noisy proxy). Density per 100 verses |
| 11 | `divine_name_density` | count of tokens matching any of the 99 names from asma-al-husna.txt, whole-word or with allowed proclitic prefixes (و,ف,ب,ل,ك,و+ال,ف+ال,ب+ال,ل+ال) per 100 verses |
| 12 | `personal_pronoun_density` | count of tokens exactly equal to {انا, انت, هو, هي, نحن, انتم, انتما, هم, هما, انتن, هن} per 100 verses (QAC-independent orthographic match on no-tashkeel) |
| 13 | `rhyme_letter_diversity` | size of the set of distinct verse-final letters across all verses in the surah (surah scored 1..28; larger = more diverse rhyme). "Final letter" = last Arabic grapheme in the verse's last token |
| 14 | `refrain_density` | count of verse-level repeats: number of verses whose EXACT normalised text matches the text of another verse in the SAME surah, per 100 verses. (Captures al-Raḥmān fa-bi-ayyi-ālāʾi pattern; captures al-Mursalāt repetition; 0 for most surahs) |
| 15 | `loanword_density` | count of surface tokens matching any of the 218 Jeffery-1938 arabic_lemma entries (whole-word or prefix-tolerant) per 100 verses |

### Why these 15?

- Axes 1-5: direct replications of prior findings ([[h-new-46-1-chronology-disentangle|H-NEW-46.1]], -71, -74, -51.1) — **MW-5 positive-control bank**
- Axes 6-9: classical Quranic studies content dimensions (prophet / law / eschatology / book)
- Axes 10-14: structural-rhetorical dimensions (oaths / names / pronouns / rhyme / refrain)
- Axis 15: historical-linguistic dimension (loanword arrival)

## Chronology variable (LOCKED)

**Nöldeke rank** (continuous 1..114) from `data/revelation-order.csv` column `noldeke_order`.
Used as the x-variable in all 15 Spearman tests. Phases (for the phase-transition scan):
- Early Meccan = rank 1-48 (48 surahs)
- Middle Meccan = rank 49-69 (21 surahs)
- Late Meccan = rank 70-90 (21 surahs)
- Medinan = rank 91-114 (24 surahs)

(Boundaries match `chronological-revelation.md` §3; these are Nöldeke's own classical boundaries.)

## Test procedure (LOCKED)

For each of 15 axes:
1. Compute axis value per surah (114 values).
2. Compute Spearman ρ(axis_values, noldeke_rank_values). Record observed ρ.
3. Permutation null: shuffle noldeke_rank assignment across surahs 10 000 times; recompute ρ each time. Two-sided p = (1 + #{|ρ_perm| ≥ |ρ_obs|}) / (1 + 10 000).
4. Verdict per axis: **PASS** if p < α_bon = 0.00333 (Bonferroni-15); else **NULL**.

### Phase-transition scan (descriptive + mechanistic)

For each axis:
- Compute mean ± SD within each of the 4 Nöldeke phases.
- Classify the trajectory as:
  - **MONOTONE** if means strictly increasing OR strictly decreasing across the 4 phases
  - **U-SHAPED** or **INVERTED-U** if one local extremum at Middle or Late Meccan
  - **JUMP** if Δ(phase_i → phase_{i+1}) > 2 × max(other Δs) — identifies a single phase-transition
  - **FLAT** if max-mean / min-mean < 1.25 (no meaningful chronological variation)

Phase-transition classification is a DESCRIPTIVE overlay on the inferential Spearman test.

## MW-5 positive-control

**Axis 1 (surah_length)** is the positive control: [[h-new-46-1-chronology-disentangle|H-NEW-46.1]] established this ρ strongly.
- Expected: ρ(verses_per_surah, noldeke_rank) strongly positive, p < 10⁻⁵
- If Axis-1 fails to register ρ > +0.4 at p < 10⁻³, the extractor or chronology file is **BROKEN** and the rest of the run is invalidated.

**Axes 4 and 5** are secondary positive controls ([[h-new-71-allah-distribution|H-NEW-71]], [[h-new-74-qul-distribution|H-NEW-74]]):
- Axis 4 (allah_density): expect strong positive ρ (Allah-density increases monotonically with revelation)
- Axis 5 (qul_density): expect Late Meccan peak — this is NOT monotone; Spearman ρ may be modest even though KW across phases is highly significant. Inclusion is still a replication check via phase-means.

## Garden-of-forking-paths disclosure (BEFORE running)

### Choices MADE BEFORE RUNNING (locked)
1. **15 axes, chosen from OQ-12 + replication set.** We considered but EXCLUDED: (i) hapax density (already studied in H-NEW-23), (ii) rhyme tightness / fāṣila uniformity (overlaps with axis 13), (iii) letter entropy (already-null per chronological-revelation.md §5), (iv) abjad totals (length-driven, trivially correlated), (v) per-root rarity / TTR (already covered in chronological-revelation.md §9).
2. **2-sided direction per axis.** No pre-registered sign for any axis because some (e.g., qul-density) are known non-monotone. Forcing 1-sided would require asymmetric Bonferroni.
3. **Bonferroni k=15** for the family of 15 per-axis Spearman tests. Phase-transition scan is descriptive, not inferential, so no additional correction needed.
4. **10K permutations** matches the repo-standard budget (see [[h-new-71-allah-distribution|H-NEW-71]] at 100K; we use 10K because 15× tests and α_bon = 0.00333 → we need resolution only to 0.0001, which 10K supports).
5. **Per-surah values** (not per-verse): chronology is surah-level (Nöldeke ranks surahs). Per-verse would inflate N and collapse onto surah-mean anyway.
6. **Axis operationalisations locked above.** Loanword list = Jeffery 1938 218 entries; asma list = Tirmidhī 99; prophet names = locked 29-item list (see axis 6). No swapping mid-run.

### Choices explicitly NOT made (to avoid forking)
- We are NOT computing partial ρ controlling for length. Length is itself an axis (axis 1). If a content axis correlates purely via length, both will pass and that IS the story; phase-transition scan will reveal whether it's length-artifact or independent.
- We are NOT running Kruskal-Wallis in parallel to Spearman. Spearman ρ is one number per axis; KW is the correct test if chronology is treated as categorical (4 phases). We choose Spearman + descriptive phase-means — cleaner single-family for Bonferroni.

### Potential alternative rule tuples considered and discarded
- **Bonferroni family size**: strictly 15. Adding phase-transition inferential test would inflate k and loosen per-test α. Phase-transition is kept DESCRIPTIVE.
- **Permutation model**: shuffle noldeke_rank across surahs (exchangeability under null of no chronological effect). Alternative — shuffle axis values — is equivalent for rank correlation.
- **Axis 3 muqaṭṭāʿat cardinality**: 0 for non-muq surahs (29 values > 0, 85 = 0). Alternative: restrict to 29 muq surahs only. Rejected because that duplicates [[h-new-51-1-noldeke-replication|H-NEW-51.1]]; the 0-padded axis tests whether the GLOBAL ρ is dominated by muq-status or by actual cardinality within muq surahs.

## Pre-committed verdict table

| Outcome | Verdict |
|---|---|
| Axis 1 fails MW-5 (ρ ≤ 0.4 or p ≥ 0.001) | EXTRACTOR_BROKEN — abort |
| 0 axes survive Bonferroni-15 | GLOBAL NULL — "chronology explains no axis beyond length" |
| 1-3 axes survive | MINIMAL SIGNAL — list, cite, but no unified profile |
| 4-9 axes survive | MULTI-AXIS CHRONOLOGY — structural signature exists |
| ≥10 axes survive | PERVASIVE CHRONOLOGY — Quran is a chronologically-stratified corpus at the structural level |

## Expected a-priori findings

Based on prior work:
- Axis 1 (length): ρ ≈ +0.65-0.75, p < 10⁻¹⁵ ([[h-new-46-1-chronology-disentangle|H-NEW-46.1]] replication) — **PASS expected**
- Axis 2 (verse length): ρ ≈ +0.70-0.80, p < 10⁻¹⁵ — **PASS expected**
- Axis 3 (muq cardinality): ρ ≈ +0.30, p ≈ 10⁻³ — **borderline** ([[h-new-51-1-noldeke-replication|H-NEW-51.1]] was +0.54 within-muq; 0-padded may dilute)
- Axis 4 (Allah-density): ρ ≈ +0.55, p < 10⁻⁹ ([[h-new-71-allah-distribution|H-NEW-71]]) — **PASS expected**
- Axis 5 (qul density): ρ uncertain sign; Late Meccan peak → non-monotone → modest Spearman
- Axes 6-9: unknown; this is the science
- Axes 10-14: unknown
- Axis 15 (loanword): Jeffery 1938 argued loanwords are disproportionately in late surahs (Medinan legal); expect ρ > 0, but signal may be weak given 218 items and most are high-frequency basics (Allah itself is Syriac-origin)

## Honesty

- If Axis 1 fails MW-5, abort.
- If 0 axes pass beyond Axis 1, publish with EQUAL prominence.
- Phase-transition scan is descriptive; no claim is inferential at that level.
- All 15 axes published whether pass or null, in the findings file.

## Integrity

- Seed: 20260417
- N_perm: 10 000
- Bonferroni k = 15; α_bon = 0.00333
- Direction 2-sided per axis (locked)
- Axis list LOCKED in this file BEFORE any correlations computed
- Author: [[h-new-125-chronology-content|h-new-125]]-specialist
