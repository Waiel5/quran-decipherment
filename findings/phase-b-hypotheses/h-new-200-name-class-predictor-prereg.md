---
id: H-NEW-200
title: Surah-name etymology class × mushaf position / Meccan–Medinan / Nöldeke-phase cluster predictor
status: PRE-REGISTERED 2026-04-17
bonferroni_family: 2026-04-17-H-NEW-200-name-class-predictor
bonferroni_k: 3
alpha_bon: 0.01667
rules_tuple: (hafs-kufan; no-tashkeel; canonical 114; Tanzil Egyptian Standard + Wikipedia Nöldeke revelation-order table, data/revelation-order.csv; etymology taxonomy locked from H-NEW-49)
seed: 20260419
primary_data:
  - H-NEW-49 locked 9-way etymology class for each of the 114 surah names
  - data/revelation-order.csv (mushaf rank, Meccan/Medinan, Nöldeke phase Early/Middle/Late-Meccan + Medinan)
n_surahs: 114
---

# [[h-new-200-name-class-predictor|H-NEW-200]] — Etymology-class predictor of mushaf position, Meccan/Medinan, and Nöldeke compositional-phase cluster

## Question

Does the etymology class of a surah's *name* (prophet-person, animal/object,
divine-attribute, cosmological-natural, event-eschatological, social-legal,
revelation-ritual, muqaṭṭaʿāt-letter, other-abstract) non-randomly predict:

(T1) its mushaf position (1–114)?
(T2) its Meccan/Medinan declared type?
(T3) its Nöldeke compositional-phase cluster (Early-Meccan / Middle-Meccan /
     Late-Meccan / Medinan)?

## Why this is a NEW hypothesis vs [[h-new-49-surah-name-class|H-NEW-49]]

[[h-new-49-surah-name-class|H-NEW-49]] tested (a) class distribution, (b) muqaṭṭaʿāt × class, (c) long-vs-short
mufaṣṣal divine-attribute enrichment, (d) lexical centrality of the name-root.
[[h-new-200-name-class-predictor|H-NEW-200]] tests THREE DIFFERENT dependent variables — mushaf position as a
continuous ordinal, Meccan/Medinan as a binary, and Nöldeke-phase as a 4-way
categorical. None of these were any cell of [[h-new-49-surah-name-class|H-NEW-49]]; all three are
standard targets in the project (cf. [[h-new-183-chronology-predictor|H-NEW-183]] Nöldeke predictor,
[[h-new-192-mushaf-position-decomposition|H-NEW-192]] mushaf-position decomposition, [[cross-finding-012-late-meccan-scripture-announcement|cross-finding-012]] Late-Meccan
apparatus). [[h-new-200-name-class-predictor|H-NEW-200]] asks whether the *name-class label alone* — a piece
of surface metadata with NO compositional statistics, no lexical counts,
no orthographic features — is sufficient to predict any of these three
structural placements.

## Etymology taxonomy (locked from [[h-new-49-surah-name-class|H-NEW-49]])

Classes (9):
- PROPHET_PERSON
- ANIMAL_OBJECT
- DIVINE_ATTRIBUTE
- COSMOLOGICAL_NATURAL
- EVENT_ESCHATOLOGICAL
- SOCIAL_LEGAL
- REVELATION_RITUAL
- MUQATTAAT_LETTER
- OTHER_ABSTRACT

The user's informal prompt collapses some of these: "cardinal (al-Baqara, al-Anfāl)"
overlaps with ANIMAL_OBJECT and SOCIAL_LEGAL rather than being a separate class,
so the locked [[h-new-49-surah-name-class|H-NEW-49]] taxonomy is used as the canonical 9-way partition.

## Tests

### T1 — Mushaf position vs class (Kruskal–Wallis + permutation null)

**Statistic**: Kruskal–Wallis H across the 9 classes, with mushaf_rank
ranging 1 to 114 as the continuous ordinal outcome.

**Null**: permute class labels across the 114 surahs 100,000 times;
report p = (#H_perm ≥ H_obs + 1) / (n_perm + 1).

**Direction**: two-sided (no pre-committed directional hypothesis for
mushaf-position ordering within the 9 classes).

**PASS threshold**: p_perm < α_bon = 0.01667.

### T2 — Meccan/Medinan vs class (χ² + permutation null)

**Statistic**: Pearson χ² on the 2 × 9 contingency table
(rows = Meccan/Medinan, cols = 9 classes).

**Pooling rule** (locked before run): if min expected cell count < 5,
pool the smallest classes (in the fixed order OTHER_ABSTRACT,
MUQATTAAT_LETTER, REVELATION_RITUAL — same order as [[h-new-49-surah-name-class|H-NEW-49]] Cell 2) into
a POOLED_OTHER column until min-expected ≥ 5.

**Null**: permute class labels 100,000 times; report p_perm =
(#χ²_perm ≥ χ²_obs + 1) / (n_perm + 1).

**PASS threshold**: p_perm < α_bon = 0.01667.

### T3 — Nöldeke compositional-phase cluster vs class (χ² + permutation null)

**Statistic**: Pearson χ² on the 4 × 9 contingency table
(rows = Early Meccan / Middle Meccan / Late Meccan / Medinan, cols = 9 classes).

**Pooling rule** (locked before run): same as T2, pool OTHER_ABSTRACT,
MUQATTAAT_LETTER, REVELATION_RITUAL into POOLED_OTHER until min expected ≥ 5.

**Null**: permute class labels 100,000 times; report p_perm.

**PASS threshold**: p_perm < α_bon = 0.01667.

## Pre-committed expectations (garden-of-forking-paths disclosure)

Before running, I expect:
- **T1 likely PASS**: PROPHET_PERSON class is empirically concentrated in
  the ṭiwāl and Middle-Mushaf regions (Yūnus Q10 … Maryam Q19 … Muḥammad Q47,
  Nūḥ Q71), which should produce a lower mushaf-rank median than
  EVENT_ESCHATOLOGICAL (Q69, Q75, Q78–80, Q99–101) which clearly concentrates
  in short-mufaṣṣal back.
- **T2 likely PASS, weak**: SOCIAL_LEGAL class is expected to be
  Medinan-enriched (Q4 Nisāʾ, Q33 Aḥzāb, Q58 Mujādila, Q65 Ṭalāq, Q66 Taḥrīm).
  EVENT_ESCHATOLOGICAL and COSMOLOGICAL_NATURAL are expected Meccan-enriched.
- **T3 likely PASS**: COSMOLOGICAL_NATURAL clustering in Early-Meccan
  (Ash-Shams Q91, Al-Layl Q92, Ad-Ḍuḥā Q93, Al-Fajr Q89, etc.) is a strong
  known descriptive pattern. MUQATTAAT_LETTER clustering in Middle-Meccan
  is also known ([[h-new-46-muqattaat-vs-surah-length|H-NEW-46]]).

These prior expectations ALREADY motivate the three tests; the null
hypothesis is "etymology class is statistically independent of each of
the three structural placements" and would be falsified by any of them.

## Audit hooks

- If T1–T3 all PASS at p < 10⁻⁴, report as "etymology-class is a
  surface predictor of mushaf structure" and audit whether this is
  sub-explained by known signals (PROPHET_PERSON ≈ longer Middle-Meccan
  narratives, SOCIAL_LEGAL ≈ Medinan, COSMOLOGICAL_NATURAL ≈ Early-Meccan).
- If any PASS occurs without obvious mediating signal, flag for follow-up
  H-NEW-200.1 with feature-residualization (control for verse_count,
  mean_verse_length).

## Output

- `/findings/phase-b-hypotheses/h-new-200-name-class-predictor.md` — main writeup
- `/findings/phase-b-hypotheses/csv/h-new-200.json` — structured results
- `/findings/phase-b-hypotheses/csv/h-new-200-per-surah.csv` — per-surah table
