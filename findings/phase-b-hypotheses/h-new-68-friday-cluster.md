---
id: H-NEW-68
title: Friday-recitation cluster cohesion test (Q 18, 32, 62, 76)
phase: B
status: NULL on cluster cohesion (0/4 axes Bonferroni-sig; 0/4 even at uncorrected α=0.05)
prereg: h-new-68-friday-cluster-prereg.md
script: scripts/h_new_68_friday_cluster.py
csv: findings/phase-b-hypotheses/csv/h-new-68.json
journal: journal/h-new-68-run-1.md
seed: 20260416
date: 2026-04-15
---

# [[h-new-68-friday-cluster|H-NEW-68]] — Friday-Recitation Cluster (results)

## TL;DR

The four classically-Friday-liturgy surahs (Q 18 al-Kahf, Q 32 al-Sajda,
Q 62 al-Jumuʿah, Q 76 al-Insān) are **NOT a structurally cohesive cluster**
on any of the 4 pre-registered axes. Of 10 000 random 4-surah subsets:

- A1 mean-pairwise shared-prefix: observed 0.33 chars vs null mean 0.32, p = 0.35
- A2 mean-pairwise root-jaccard:  observed 0.178 vs null mean 0.134, p = 0.24
- A3 length cohesion (1/(1+CV)):  observed 0.544 vs null mean 0.596, p = 0.70
- A4 divine-density cohesion:     observed 0.447 vs null mean 0.522, p = 0.77

**0 / 4 axes** Bonferroni-significant at α_bon = 0.0125. **0 / 4 axes**
even at uncorrected α = 0.05. Verdict: **NULL**.

The pre-registered Q 18 ↔ Q 62 secondary pair test is also **NULL**:
shared-prefix observed = 0 chars (literally no shared character beyond
the first letter), p = 1.0; root-jaccard observed 0.144, p = 0.42.

## Why the cluster is NOT structurally cohesive

The 4 Friday-liturgy surahs come from **four different opener-class families**:

| Surah | Opener (no-tashkeel) | Opener class |
|-------|----------------------|--------------|
| Q 18  | الحمد لله الذي أنزل على عبده الكتاب… | al-ḥamdu lillāh family (Q 1, 6, 18, 35) |
| Q 32  | الم | muqaṭṭaʿāt (alif-lām-mīm; 6 surahs) |
| Q 62  | يسبح لله ما في السماوات… | imperfect-tense musabbiḥāt (Q 62, 64) |
| Q 76  | هل أتى على الإنسان حين من الدهر… | interrogative opener (rare) |

**Zero pairs share even 3 chars of opener prefix.** The only non-zero
pair is Q 18 - Q 32 (2 chars: "ال" — the definite article alif-lām, which
is shared with thousands of opening words throughout the corpus). Every
other pair has 0 shared characters in the opening verse.

This is the cleanest possible demonstration that the Friday-liturgy
tradition operates on **liturgical-function** logic, not on
**structural-shape** logic. The four surahs are recited together on
Fridays because of:

- **Q 18** — eschatological narrative arc (cave of the sleepers, Khidr,
  Dhū l-Qarnayn, dajjāl protection) — 110 verses, classified Meccan.
- **Q 32** — short Meccan sajda surah (30 verses) with a recitation-
  prostration verse at v 15.
- **Q 62** — short Medinan surah (11 verses) on the Friday gathering
  for prayer.
- **Q 76** — Medinan/Meccan-disputed surah (31 verses) on the destiny
  of the righteous (the abrār) and on the human condition.

These are **thematically Fridayward** in different ways (eschatology,
ritual prostration, Friday-prayer, human destiny) but **share no
structural shape signature**.

## Per-axis detailed results

### A1 — Mean pairwise shared-prefix (chars)

| Pair | Q 18 | Q 32 | Q 62 | Q 76 |
|------|------|------|------|------|
| Q 18 |  -   |  2   |  0   |  0   |
| Q 32 |      |  -   |  0   |  0   |
| Q 62 |      |      |  -   |  0   |
| Q 76 |      |      |      |  -   |

Mean = (2 + 0 + 0 + 0 + 0 + 0) / 6 = **0.333 chars**
Null mean across 10K random 4-subsets = **0.317 chars**
Null q95 = 1.667, q99 = 3.167, max in 10K = 11.0. **p = 0.352.**

For comparison, the [[h-new-58c-musabbihat-tense-split|H-NEW-58c]] musabbiḥāt cluster (Q 57, 59, 61, 62, 64)
yielded mean pairwise prefix = **14.1 chars** with null mean 0.36 and
p = 0.0001. The Friday cluster has prefix cohesion **42× lower** than the
musabbiḥāt cluster, on the identical instrument.

### A2 — Mean pairwise root-jaccard

Pairwise Jaccard values across the 6 Friday-cluster pairs:

| Pair      | Roots A | Roots B | ∩  | ∪   | J     |
|-----------|---------|---------|----|----|-------|
| Q 18-Q 32 | 369     | 131     | 92 | 408 | 0.225 |
| Q 18-Q 62 | 369     | 76      | 56 | 389 | 0.144 |
| Q 18-Q 76 | 369     | 112     | 67 | 414 | 0.162 |
| Q 32-Q 62 | 131     | 76      | 37 | 170 | 0.218 |
| Q 32-Q 76 | 131     | 112     | 42 | 201 | 0.209 |
| Q 62-Q 76 | 76      | 112     | 19 | 169 | 0.112 |

Mean J = **0.178**. Null mean = 0.134, q95 = 0.261, q99 = 0.317. **p = 0.239.**

Slightly above null mean but well within the bulk of the null distribution.
The Q 62-Q 76 pair (J = 0.112) is actually **below null mean**, consistent
with the fact that Q 62 is a brief Medinan surah on Friday-prayer
and Q 76 is on human destiny — different lexical universes.

### A3 — Length cohesion (1 / (1 + CV(verse_counts)))

Verse counts: Q 18 = 110, Q 32 = 30, Q 62 = 11, Q 76 = 31.
Mean = 45.5, std ≈ 38.0, CV ≈ 0.836.
Cohesion = 1 / (1 + 0.836) = **0.544**.

Null mean cohesion = 0.596, q95 = 0.761. **p = 0.699.**

The Friday cluster is **less length-cohesive** than the typical 4-surah
random subset. Q 18 is 110 verses while Q 62 is only 11 — a 10× length
range, much wider than typical random subsets.

### A4 — Divine-name density cohesion (1 / (1 + CV))

Per-surah divine-name density (names per verse):
- Q 18: 0.145
- Q 32: 0.100
- Q 62: 1.364 ← outlier (high density of canonical divine names in 11 verses)
- Q 76: 0.129

Mean = 0.435, std ≈ 0.539, CV ≈ 1.240.
Cohesion = 1 / (1 + 1.240) = **0.447**.

Null mean = 0.522. **p = 0.767.**

Q 62 is a **divine-name density outlier** (1.36 names/verse — the surah
opens "yusabbiḥu lillāh… al-Maliki al-Quddūsi al-ʿAzīzi al-Ḥakīm" with
4 divine names in 11 chars). This single high-density surah dragged
the cluster's CV up and cohesion down. Other 3 surahs are in the 0.10-
0.15 range — cohesive among themselves, but Q 62 explodes the variance.

## Q 18 ↔ Q 62 specific link (secondary, pre-registered)

The two most unambiguously Friday-specific surahs (al-Kahf is THE
Friday surah; al-Jumuʿah literally means "Friday").

| Axis | Observed | Null mean | Null q95 | Null q99 | p | Sig (k=2)? |
|------|----------|-----------|----------|----------|---|------------|
| Shared prefix | **0 chars** | 0.346 | 2 | 8 | 1.000 | NO |
| Root jaccard  | 0.144 | 0.135 | 0.334 | 0.390 | 0.418 | NO |

**No structural link.** Q 18 opens with "al-ḥamdu lillāh alladhī anzala
ʿalā ʿabdihi l-kitāba…" and Q 62 opens with "yusabbiḥu lillāh mā fī
l-samāwāti wa-mā fī l-arḍi al-Maliki l-Quddūsi…". The two surahs share
the word "lillāh" early but their prefixes diverge after the FIRST
character (al-ḥ vs y). The first character difference suffices to make
shared-prefix = 0.

This cleanly NULLs the "Q 18 + Q 62 are linked because both are 'the
Friday surahs' " hypothesis at the structural-shape level. Their link
is **liturgical-functional**, not lexical-structural.

## Substantive interpretation

1. **The Friday liturgy is a function/genre cluster, not a shape
   cluster.** The 4 surahs were chosen by tradition for liturgical
   appropriateness on Friday (eschatology, sajda-prostration, Friday-
   prayer, human-destiny themes), not for shared compositional shape.
   This NULL is the *correct* result for a function-cluster tested on
   shape-axes, exactly mirroring the [[h-new-58-surah-pair-twinning|H-NEW-58]] finding for surah-pairs.

2. **Comparison to musabbiḥāt cluster ([[h-new-58c-musabbihat-tense-split|H-NEW-58c]], p=0.0001):** The
   musabbiḥāt cluster shares an OPENER FORMULA — "sabbaḥa lillāh…" or
   "yusabbiḥu lillāh…" — and so the shared-prefix instrument detects
   it sharply. The Friday cluster has NO shared opener formula, NO
   shared muqaṭṭaʿāt, NO shared length-class, NO shared divine-density
   class. The instrument that detects musabbiḥāt does not detect
   Friday-cluster because the Friday cluster's coherence lives at a
   higher (functional/thematic) level.

3. **Cross-finding implication:** Q 62 is the SAME surah that anchors
   the imperfect-tense musabbiḥāt sub-cluster ([[h-new-58c-musabbihat-tense-split|H-NEW-58c]]) and bears
   the al-Ḥashr Khawātim echo ([[h-new-63-khawatim-echo-extended|H-NEW-63]]). Q 62 belongs to MULTIPLE
   structural systems (musabbiḥāt + Khawātim + Friday liturgy), only
   ONE of which (musabbiḥāt) shows quantitative structural cohesion.

4. **Honest framing:** the test was designed correctly (4 axes spanning
   structural-formula, lexical, length, divine-density). The instrument
   was independently validated by [[h-new-58c-musabbihat-tense-split|H-NEW-58c]]. The NULL is a real
   substantive finding: **classical Friday liturgy is NOT a shape-
   based curation.**

## Pre-registered PASS criterion verdict

PASS criterion (locked): "≥ 2 of 4 axes Bonferroni-significant at α =
0.0125 → PASS; 1 → MARGINAL; 0 → NULL."

Observed: **0 / 4 Bonferroni-significant. 0 / 4 even uncorrected.**
**Verdict: NULL.**

## MW-5 instrument check

The shared-prefix cluster instrument (A1) was independently validated
by [[h-new-58c-musabbihat-tense-split|H-NEW-58c]] on the musabbiḥāt cluster (Q 57, 59, 61, 62, 64) at
p = 0.0001 against 10 000 random 5-surah subsets. Same metric used here.
The instrument is known to detect cohesion when present. The Friday
cluster's null result is therefore informative (instrument can detect
cohesion; Friday cluster lacks cohesion on this axis).

## Files

- Pre-reg: `/Users/grey/Downloads/quran/findings/phase-b-hypotheses/h-new-68-friday-cluster-prereg.md`
- Script: `/Users/grey/Downloads/quran/scripts/h_new_68_friday_cluster.py`
- JSON: `/Users/grey/Downloads/quran/findings/phase-b-hypotheses/csv/h-new-68.json`
- Journal: `/Users/grey/Downloads/quran/journal/h-new-68-run-1.md`

## Verdict

- **Pre-registered PASS criterion**: **NULL** (0/4 axes; 0/4 even uncorrected)
- **Q 18 ↔ Q 62 secondary**: **NULL** (shared-prefix p=1.000; jaccard p=0.418)
- **Substantive finding**: classical Friday liturgy operates on
  function/theme/genre, not on shape. Mirrors the [[h-new-58-surah-pair-twinning|H-NEW-58]] finding
  for classical surah-pairs. No instrument failure (MW-5 already
  passed via [[h-new-58c-musabbihat-tense-split|H-NEW-58c]] on the musabbiḥāt cluster).

## Suggested follow-up

A future H-NEW-68b should test the Friday cluster on **functional /
thematic axes**:
- F1: presence of eschatological / Day-of-Judgment vocabulary (yawm,
  qiyāma, ḥisāb, jannah, nār, etc.)
- F2: presence of dhikr-formula vocabulary
- F3: shared narrative protagonists across the 4 surahs
- F4: length and frequency of divine-name pairings (al-ʿAzīz al-Ḥakīm,
  etc.) — Q 62 may carry the cluster on this axis

Those are the axes the classical Friday-recitation tradition actually
claims (via fadāʾil al-Qurʾān literature), not statistical shape.
