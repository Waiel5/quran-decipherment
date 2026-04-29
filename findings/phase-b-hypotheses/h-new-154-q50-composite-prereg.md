---
finding_id: h-new-154
title: "Q 50 composite hub-mechanism score — does Q 50 rank top-3 on a joint indicator?"
specialist: specialist-B (quran-equation-solvers)
date_prereg: 2026-04-17
seed: 20260417
bonferroni_k: 1
bonferroni_family: h-new-154-q50-composite
alpha_bon: 0.05
alpha_raw: 0.05
parent_findings: [h-new-146 (3 near-misses for Q 50 hub), h-new-150 (liturgical WEAK-LINK), h-new-152 (Q 50 qrA-inclusio UNIQUE descriptively), cross-finding-010 (Q 50 degree 4)]
rules_tuple: "(114 surahs Hafs-Kūfan; 5 pre-committed binary/normalized features; equal-weight sum; QAC v0.4)"
pre_reg_standard: PRE-REG-STANDARD-04
warning: "Post-hoc-composite risk acknowledged; features pre-committed from CLASSICAL-BALAGHA categories BEFORE computing Q 50's score per feature. Shuffle-null used for post-hoc-fit protection."
---

# [[h-new-154-q50-composite|H-NEW-154]] — Q 50 composite hub-mechanism score

## Motivation and post-hoc-risk disclosure

[[h-new-146-q50-qaf-hub|H-NEW-146]] left Q 50's hub status UNEXPLAINED at Bonferroni-3 after 3
near-misses. Team-lead proposed a COMPOSITE test hypothesis: Q 50's
hub status is multi-factor, not single-axis, and a JOINT predictor
should place Q 50 high.

**Methodological hazard**: if I hand-pick features that I've already
noticed Q 50 scores high on, the composite will trivially privilege
Q 50. This is the classic post-hoc-composite fallacy.

**Mitigation strategy**:

1. **Feature set pre-committed from classical-balāgha categories**, not
   from post-hoc Q-50-inspection. Features are:
   - Position centrality (any surah in Q 40-60 can score high)
   - Book-reflexive opening (MANY surahs open with Qurʾān/kitāb
     references — see [[h-new-53-muqattaat-book-reference|H-NEW-53]], Q 2, 3, 10, 11, ... all do)
   - Muqaṭṭāʿat-opened (29 of 114 qualify broadly)
   - Oath-opener (Q 36, 37, 51, 52, 53, 68, ..., 14 surahs start with an oath)
   - Mufaṣṣal-start position (Q 49+ cluster)

2. **Uniform application to 114 surahs**: each surah gets the same
   score for the same feature value, not Q-50-privileged.

3. **Shuffle-null for MW-5**: shuffle feature scores across surahs;
   expected Q 50 rank under null = 1/114 × 114 = uniformly distributed.

4. **Pre-committed decision**: Q 50 top-3 rank with permutation p<0.05
   is the PASS criterion. If Q 50 scores well BUT so do many other
   surahs (ties or near-ties), the composite is non-distinctive.

## Features (pre-committed)

Each surah gets 5 binary/normalized components, summed with EQUAL
WEIGHT to produce a composite-hub-mechanism-score.

### F1 — position centrality (binary)
1 if surah ID ∈ [40, 60] (21 surahs: Q 40-60); else 0.
Covers "mid-mushaf" heuristic.

### F2 — book-reflexive opening (binary)
1 if ANY verse in v1-3 contains QAC STEM root qrA or ktb; else 0.
Per [[h-new-53-muqattaat-book-reference|H-NEW-53]] this covers ~24+ of the muqaṭṭāʿat surahs plus some
non-muq surahs.

### F3 — muqaṭṭāʿat-opened (binary)
1 if surah is in the canonical 29-muq list; else 0.

### F4 — oath-opener (binary)
1 if v1 contains any STEM root in classical-oath lexicon: {HlF (swear),
or the wāw-al-qasam syntactic pattern detected via word-1 = "وَ" + oath
particle}. Operationalize as: v1 surface first non-basmala word is
"وَ" (wāw) AND v1 has no verb in first 3 words.
Alternative formalization (pre-committed): surface check for v1
opening patterns {"وَال", "وَ" + single letter muq, "وَالذين"}.
For precise reproducibility: list-based. The 14 oath-opened surahs per
classical tafsir are: Q 36 (يس وَالقرآن), Q 37 (وَالصافات), Q 43
(حم وَالكتاب), Q 44 (حم وَالكتاب), Q 50 (ق وَالقرآن), Q 51 (وَالذاريات),
Q 52 (وَالطور), Q 53 (وَالنجم), Q 68 (ن وَالقلم), Q 75 (لَا أُقْسِم), Q 77
(وَالمرسلات), Q 79 (وَالنازعات), Q 85 (وَالسماء), Q 86 (وَالسماء), Q 89
(وَالفجر), Q 90 (لَا أُقْسِم), Q 91 (وَالشمس), Q 92 (وَاللَّيْل), Q 93
(وَالضحى), Q 95 (وَالتين), Q 100 (وَالعاديات), Q 103 (وَالعصر). That's
22 oath-opened surahs (+/- edge cases). Locked list: those 22 get F4=1.

### F5 — mufaṣṣal-opening position (binary)
1 if surah ID ≥ 49 AND surah ID ≤ 60 (al-mufaṣṣal's opening segment,
classical "al-mufaṣṣal al-ṭiwāl"); else 0.
Per classical taxonomy, al-mufaṣṣal begins at Q 49 (al-Ḥujurāt).
This captures the early-mufaṣṣal boundary zone.

### Composite score

`hub_score[s] = F1[s] + F2[s] + F3[s] + F4[s] + F5[s]`

Range: 0 to 5 (integer). Q 50 gets 1 (position) + 1 (book-ref) +
1 (muq) + 1 (oath) + 1 (mufaṣṣal) = 5 if all features match.

## Hypothesis

**H_0**: Q 50's composite score is NOT in the top-3 of 114 surahs (i.e.,
at least 3 other surahs tie or exceed it).

**H_1**: Q 50's composite score IS in the top-3 of 114 surahs AND the
rank-in-top-3 is rarer than chance (permutation p<0.05).

## MW-5 positive control — shuffled feature-scores null

Shuffle EACH of the 5 feature vectors independently across 114 surahs.
Re-compute composite score. Rank-of-Q-50 distribution under 10,000 such
shuffles. Expected rank under null ≈ 57.5 (median).

**Pre-committed PASS**: observed Q 50 rank ≤ 3 AND p_perm < 0.05
(fraction of shuffles with Q 50 rank ≤ observed).

## Garden of forking paths

- **Equal weights**: chosen to avoid weight-tuning post-hoc. Alternatives
  rejected: classical-balāgha-weighted (arbitrary), inverse-rank-weighted
  (amplifies noise), Fisher-info-weighted (requires observing the data
  first).
- **Binary features** (0/1): avoids threshold manipulation. Alternatives
  rejected: continuous normalized scores (would require post-hoc
  normalization choice).
- **5 features, not fewer/more**: five is the team-lead-specified count
  for this test.
- **Oath-opener list**: hand-coded from classical tafsir (al-Suyūṭī
  al-Itqān on oath-openers); locked above.
- **F1 bracket Q 40-60**: matches [[h-new-146-q50-qaf-hub|H-NEW-146]] Cell A bracket.
- **F5 bracket Q 49-60**: matches classical al-mufaṣṣal al-ṭiwāl sub-
  classification.

## Pre-committed acceptance matrix

| Q 50 rank | p_perm | Verdict |
|---|---:|---|
| 1 (strict top) | <0.05 | COMPOSITE-CONFIRMED — Q 50 IS top-1 hub by composite score |
| 2-3 (tied-top) | <0.05 | COMPOSITE-TOP — Q 50 shares top-3 with other composite-hubs |
| 4-10 | <0.05 | COMPOSITE-HIGH — in top-10 but not top-3; [[h-new-146-q50-qaf-hub|H-NEW-146]] NULL verdict stands |
| any | ≥0.05 | NULL — composite test fails to distinguish Q 50 from baseline |

## Deliverables

- Pre-reg: this file
- Script: `scripts/h_new_154_q50_composite.py`
- JSON: `findings/phase-b-hypotheses/csv/h-new-154.json`
- Findings: `findings/phase-b-hypotheses/h-new-154-q50-composite.md`
- Journal: `journal/h-new-154-run-1.md`
