---
finding_id: h-new-150
title: "Liturgical prominence ↔ cluster-network hub-degree — empirical link for P3 mechanism"
specialist: specialist-B (quran-equation-solvers)
date_prereg: 2026-04-17
seed: 20260417
bonferroni_k: 2
bonferroni_family: h-new-150-liturgical-hub
alpha_bon: 0.025
alpha_raw: 0.05
parent_findings: [cross-finding-010 (Q 50 hub status), h-new-146 (Q 50 hub UNEXPLAINED at content-axis), h-new-89 (meta-cluster)]
rules_tuple: "(114 surahs Hafs-Kūfan; cluster-network from cross-finding-010; liturgical-prominence score coded from classical hadith + daily-prayer-manual sources PRE-RESULT)"
pre_reg_standard: PRE-REG-STANDARD-04
---

# [[h-new-150-liturgical-hub|H-NEW-150]] — Liturgical prominence ↔ cluster-network hub-degree

## Motivation

[[h-new-146-q50-qaf-hub|H-NEW-146]] left Q 50's hub status UNEXPLAINED at Bonferroni-3 after
testing position, content (qurʾān-reflexivity), and structural
(FR-distance) axes. All three were near-misses at single-test α=0.05.
The finding suggests Q 50's hub-role may be constituted by a
mechanism I haven't tested — specifically LITURGICAL PROMINENCE.

Classical Islamic liturgy prescribes specific surahs for specific
occasions:
- **Q 1 al-Fātiḥa**: recited in EVERY cycle of every prayer (17+ times daily)
- **Q 50 al-Qāf**: prescribed in Friday ʿĪd prayer (Sahih Muslim 878)
- **Q 87 al-Aʿlā + Q 88 al-Ghāshiya**: prescribed for Friday and ʿĪd
- **Q 62 al-Jumuʿa + Q 63 al-Munāfiqūn**: Friday prayer
- **Q 2 al-Baqara + Q 3 Āl ʿImrān**: "al-Zahrāwān" with protection/closing recitations
- **Q 112, 113, 114 (al-Ikhlāṣ, al-Muʿawwidhatān)**: daily morning/evening dhikr
- **Q 36 Yā-Sīn**: classically recited on Friday eve, for the dying
- **Q 67 al-Mulk**: nightly recitation (hadith)
- **Q 18 al-Kahf**: Friday (hadith)
- **Q 32 al-Sajda + Q 76 al-Insān**: Fajr prayer on Friday

[[cross-finding-010-extended-network|Cross-finding-010]] identified 4 hub regions: Q 2-3 (front), Q 50
(upper-mid), Q 59-62 (back-upper), Q 112-114 (back-terminal). ALL of
these are also liturgically prominent.

## Hypothesis

**H1 (PRIMARY)**: Liturgical-prominence score per surah is POSITIVELY
correlated with cluster-network degree ([[cross-finding-010-extended-network|cross-finding-010]]). Spearman
ρ ≥ 0.3 at p < 0.025.

**H2 (SECONDARY)**: The relationship survives length-residualization
(controlling for surah length, which trivially correlates with some
cluster memberships).

If H1 passes at ρ ≥ 0.3, theorist's P3 ("liturgical-hub mechanism") gets
its first direct empirical anchor.

## Method

### Data

**Cluster-network degree**: from `findings/phase-b-hypotheses/csv/cross-finding-010.json`, field `product_A_degree_distribution.per_surah_degree`.

**Liturgical-prominence score**: hand-coded per surah from classical
sources PRE-RESULT. The coding will be LOCKED in this pre-reg BEFORE
computing any correlation. Score = weighted sum of liturgical features:

- `fatiha_role`: 17 points if Q 1 (recited in every prayer cycle; 17×/day baseline)
- `eid_friday`: 3 points per prescribed occasion (Friday, Eid-al-Fitr, Eid-al-Adha, Taraweeh)
- `daily_morning_evening`: 2 points per daily dhikr occasion
- `protection_refuge`: 2 points (Muʿawwidhāt, Āyat-al-Kursī-bearing)
- `witr_tahajjud_night`: 1 point per nightly-recitation hadith
- `tafkhīm_liturgical`: 1 point for classical-recognized recitation-honored surah (e.g., al-Baqara, al-Kahf)
- Baseline score: 0 (surahs with no classical liturgical prescription)

### Pre-locked liturgical-prominence score (FROZEN BEFORE DATA VIEWING)

Sources consulted for the coding (pre-result):

1. Sahih al-Bukhari, Sahih Muslim (ḥadīth collections on prayer)
2. Ibn Taymiyya's "al-Kalim al-Ṭayyib" (dhikr manual)
3. al-Nawawi's "al-Adhkār" (supplications)
4. Standard daily-prayer manuals (Madina Qur'an layout, Al-Ma'thurat compilations)
5. Classical fiqh on prescribed-recitations (Kitāb al-Ṣalāh sections)

Pre-locked scores below:

```python
LITURGICAL_SCORES = {
    1:   17,   # al-Fatiha: every prayer cycle (~17×/day canonical)
    2:   8,    # al-Baqara: last 2 verses nightly; Ayat al-Kursi; protection
    3:   4,    # Al ʿImran: al-Zahrawan pair with Q 2; morning/evening dhikr
    18:  4,    # al-Kahf: Friday recitation (hadith; Sunan Abu Dawud 1074)
    24:  3,    # al-Nur: Ayat al-Nur commonly recited
    32:  3,    # al-Sajda: Fajr Friday
    36:  4,    # Ya-Sin: Friday eve / for the dying (classical)
    40:  1,    # al-Mu'min: openings of certain dhikr
    50:  3,    # al-Qaf: Friday/Eid prayer (Sahih Muslim 878)
    55:  2,    # al-Rahman: refrain-based recitation / mawlid
    56:  2,    # al-Waqi'a: nightly for sustenance (classical)
    57:  1,    # al-Hadid: opens with musabbiḥāt; Q 57:22-24 protection
    59:  3,    # al-Hashr: last 3 verses (al-Khawātim); morning/evening
    62:  3,    # al-Jumu'a: Friday prayer
    63:  3,    # al-Munafiqun: Friday prayer (paired with Q 62)
    67:  3,    # al-Mulk: nightly (hadith al-Tirmidhi 2890)
    73:  1,    # al-Muzzammil: for night prayer
    76:  2,    # al-Insan: Fajr Friday (paired with Q 32)
    87:  2,    # al-A'la: Friday + Eid (paired with Q 88)
    88:  2,    # al-Ghashiya: Friday + Eid
    94:  1,    # al-Sharh: dhikr
    97:  1,    # al-Qadr: Laylat al-Qadr
    109: 1,    # al-Kafirun: nightly (paired with Ikhlas)
    110: 1,    # al-Nasr: final-revelation honor
    112: 4,    # al-Ikhlas: daily 3×; 1/3-Quran hadith
    113: 3,    # al-Falaq: Muʿawwidhatayn; daily morning/evening + refuge
    114: 3,    # al-Nas: Muʿawwidhatayn; daily morning/evening + refuge
}
```

All other surahs (87 of 114) get score 0 (no classical prescribed-
recitation in the above sources).

### Primary test

1. Compute Spearman ρ between `LITURGICAL_SCORES[s]` and
   `per_surah_degree[s]` across all 114 surahs.
2. 10,000-permutation null (shuffle LITURGICAL_SCORES across surahs).
3. p_one_sided_upper = proportion of shuffles with ρ ≥ observed.

**PASS**: ρ ≥ 0.3 AND p < 0.025.

### Secondary test (length-residualized)

1. Regress LITURGICAL_SCORES on log(nverses) across 114 surahs → obtain residuals.
2. Regress per_surah_degree on log(nverses) → obtain residuals.
3. Spearman ρ between the two residual vectors.
4. Permutation null as above.

**PASS**: residual ρ ≥ 0.2 AND p < 0.025 (slightly weaker threshold for
the length-residualized version since the core hypothesis is less
sensitive after controlling for length).

### MW-5 positive control

Use a KNOWN non-liturgical correlate: Nöldeke chronology rank. Correlate
chronology-rank with cluster-degree. Expected: no strong positive
correlation (chronology ≠ hub-status directly). If chronology ρ is
LARGER than liturgical-ρ, liturgical claim is weak.

Also: INTERNAL sanity check — if liturgical-score-as-coded has 0
correlation with degree (ρ < 0.05), my coding was too coarse, scale
back the claim.

## Garden of forking paths

- **Scoring scheme** locked above pre-result. Alternatives rejected:
  binary (prescribed/not-prescribed — too coarse; Q 1 = Q 112 violates
  common sense), log-scale (log(17+1) for Q 1 = 2.9 vs linear 17 — the
  log scale compresses the dramatic Q 1 advantage artificially),
  per-occasion binary indicators (high-dim sparse).
- **Sources used** are classical mainstream. Alternatives rejected:
  modern-sectarian specific manuals (violates rules-tuple), single-
  madhhab specific (would need 4 variants for 4 madhāhib), secular
  orientalist (available ≠ authoritative for liturgical claims).
- **ρ ≥ 0.3 threshold**: corresponds to "moderate correlation" in
  behavioral-science conventions. Alternatives rejected: ρ ≥ 0.5
  (too strict for n=114; implausibly high), ρ > 0 (too weak).
- **Cluster-network degree** from [[cross-finding-010-extended-network|cross-finding-010]] rather than [[h-new-111-fisher-rao-mushaf|H-NEW-111]]
  Fisher-Rao MST degrees. Reason: [[cross-finding-010-extended-network|cross-finding-010]] uses taxonomic
  cluster-membership (different from content-similarity); liturgical
  prominence is a taxonomic feature, so taxonomic-network is the right
  target.
- **Length-residualization** in secondary because very long surahs
  (Q 2, Q 3) get BOTH high liturgical scores and high cluster-membership
  (more coincidences-with-clusters purely due to size). Controlling
  for this is honest.

## Pre-committed acceptance matrix

| Primary (ρ ≥ 0.3, p < 0.025) | Secondary (residual ρ ≥ 0.2, p < 0.025) | Final |
|---|---|---|
| PASS | PASS | STRONG-LINK — liturgical prominence predicts hub-status even controlling for length |
| PASS | FAIL | WEAK-LINK — apparent liturgy-hub link dissolves under length control |
| FAIL | PASS | COUNTERINTUITIVE — residual signal but not raw |
| FAIL | FAIL | NULL — liturgical-hub hypothesis not empirically supported at pre-registered thresholds |

MW-5 chronology control must show weaker ρ than liturgical for any claim
to stand.

## Deliverables

- Pre-reg: this file
- Script: `scripts/h_new_150_liturgical_hub.py`
- JSON: `findings/phase-b-hypotheses/csv/h-new-150.json`
- Findings: `findings/phase-b-hypotheses/h-new-150-liturgical-hub.md`
- Journal: `journal/h-new-150-run-1.md`

Null and pass published with equal prominence. Runtime target < 1 min.
