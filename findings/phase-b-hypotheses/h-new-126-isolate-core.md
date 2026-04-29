---
id: H-NEW-126
title: True-isolate-core characterization — {Q 16, 21, 22, 23, 25} under 20 cluster systems
phase: B
status: Cell A PASS-DIRECTED (post-hoc subset; p=0.0009; MW-5 fires); Cell B DESCRIPTIVE (5/5 concept-or-object); Cell C NULL-BROKEN (MW-5 failed); Cell D DESCRIPTIVE (5/5 high-percentile extremes)
prereg: findings/phase-b-hypotheses/h-new-126-isolate-core-prereg.md
script: scripts/h_new_126_isolate_core.py
json: findings/phase-b-hypotheses/csv/h-new-126.json
journal: journal/h-new-126-run-1.md
date: 2026-04-17
agent: h-new-126-specialist
seed: 20260417
n_perm: 10000
bonferroni_family: h-new-126-isolate-core
bonferroni_k: 4
alpha_bon: 0.0125
rules_tuple: "(no-tashkeel; hafs-kufan; canonical-114; morphology-0.4-roots; 20-cluster cross-finding-010 lock; single-test α=0.05 cap per post-hoc protocol)"
---

# [[h-new-126-isolate-core|H-NEW-126]] — True-isolate-core characterization (RESULT)

## Headline

The 5-surah true isolate core identified by [[cross-finding-010-extended-network|cross-finding-010]] —
**{Q 16 al-Naḥl, Q 21 al-Anbiyāʾ, Q 22 al-Ḥajj, Q 23 al-Muʾminūn,
Q 25 al-Furqān}** — is **NOT random heterogeneity**. These 5 surahs
share MORE root-vocabulary than expected under the null of 5 random
non-core surahs (Cell A **PASS-DIRECTED** at p = 0.0009, obs
root-Jaccard = 0.3414 vs null mean 0.1291, ≈ 2.6× enrichment; MW-5
positive control ḥawāmīm fires at α = 0.05).

They are **5/5 concept-or-object-named** (Cell B DESCRIPTIVE, genre-
coherent). Rhetorical-mode clustering (Cell C) shows the core is
DIRECTIONALLY tight (obs Euclidean 5.32 vs null 14.83, 2.8× tighter,
p = 0.0157 one-sided lower) but the MW-5 positive control for Cell C
failed — the musabbiḥāt inner-5 do NOT cluster tightly in imp/int/dec
space (p = 0.67). Per pre-reg, MW-5 failure → **Cell C NULL-BROKEN**
regardless of target result.

Each core surah is at a high-percentile extremum on ≥ 1 axis (Cell D
DESCRIPTIVE).

## Post-hoc disclosure

The 5-surah target was IDENTIFIED BY [[cross-finding-010-extended-network|cross-finding-010]], NOT
independently by this specialist. Under the PRE-REG-STANDARD post-hoc
protocol:

- Single-test α = 0.05 cap (applied).
- Bonferroni-4 within this family tightens to α_bon = 0.0125.
- Verdict ceiling = **PASS-DIRECTED** (not CONFIRMED) for Cell A,
  until INDEPENDENT REPLICATION on a distinct data dimension.

## Profile table

| Surah | Name | Gloss | Period | Nöldeke | Verses | Mean verse len | Allah/100v | Unique roots | Prophet-narrative/100v | First word | Muq-opened | Imp/Int/Dec (%) |
|---:|---|---|---|---:|---:|---:|---:|---:|---:|---|:---:|:---:|
| 16 | al-Naḥl | the Bee | Meccan | 73 | 128 | 14.4 | 64.1 | 358 | 2.34 | أتى | NO | 0.8 / 8.6 / 90.6 |
| 21 | al-Anbiyāʾ | the Prophets | Meccan | 65 | 112 | 10.5 | 4.5 | 284 | 17.86 | اقترب | NO | 4.5 / 2.7 / 92.9 |
| 22 | al-Ḥajj | Pilgrimage | **Medinan** | 107 | 78 | 16.4 | 96.2 | 328 | 10.26 | يا | NO | 2.6 / 10.3 / 87.2 |
| 23 | al-Muʾminūn | the Believers | Meccan | 64 | 118 | 8.9 | 11.0 | 271 | 3.39 | قد | NO | 3.4 / 7.6 / 89.0 |
| 25 | al-Furqān | the Criterion | Meccan | 66 | 77 | 11.6 | 10.4 | 250 | 3.90 | تبارك | NO | 5.2 / 5.2 / 89.6 |

**All 5 confirmed non-muqaṭṭāʿat-opened.** 4/5 Meccan, 1/5 Medinan
(Q 22 al-Ḥajj). Nöldeke ranks span 64-107 (Late Meccan through
Medinan) — NOT a chronological cluster.

## Per-cell results

| Cell | Description | Observed | Null | p | Verdict |
|---|---|---|---|---|---|
| A | mean pairwise root-Jaccard, core vs random-5 non-core (10K perm, one-sided upper) | 0.3414 | 0.1291 | 0.0009 | **PASS-DIRECTED** (α_bon=0.0125) |
| A MW-5 | ḥawāmīm {40-44} vs random-5 | 0.3062 | 0.1298 | 0.0046 | **PASS** (fires at α=0.05) |
| B | 5/5 concept-or-object-named | 5/5 | n/a | n/a | **DESCRIPTIVE CONFIRMED** |
| C | mean pairwise Euclidean in imp/int/dec space | 5.32 | 14.83 | 0.0157 | **NULL-BROKEN** (MW-5 failed) |
| C MW-5 | musabbiḥāt-inner-5 {57,59,61,62,64} | 16.08 | 14.53 | 0.6732 | **FAIL** (did not fire at α=0.05) |
| D | per-surah extremity (9-axis, max-abs-percentile-deviation) | all 5 at ≥78th percentile extremes | n/a | n/a | **DESCRIPTIVE** |

## Cell A — Shared content (primary inferential, PASS-DIRECTED)

The 5-core share **2.64× more root vocabulary** (pairwise Jaccard
0.3414) than random 5-sets of non-core surahs (null mean 0.1291).
p = 0.0009, comfortably below α_bon = 0.0125, and still below
0.05 under the post-hoc single-test cap.

The MW-5 ḥawāmīm positive control {Q 40-44} also fires (p=0.0046,
obs=0.3062 vs null=0.1298) — confirming that the root-Jaccard +
random-5-set null is a VALID DETECTOR of known clusters.

### What this means

The 5 surahs share a **ROOT-LEVEL semantic kernel** — DESPITE being
cluster-empty on all 20 structural axes catalogued by
[[cross-finding-010-extended-network|cross-finding-010]] (muqaṭṭāʿat, oath-opener, qul-opener, refrain,
divine-attribute-named, prophet-named, classical pair, Friday liturgy,
musabbiḥāt, mufaṣṣal-core, etc.).

This is a **CONTENT-LEVEL cluster invisible to structural
taxonomies**. The 5 surahs are united not by opener, naming, or
cluster-membership, but by what they TALK ABOUT.

### Honest caveat — length confound

Three of the five (Q 16, 21, 23) are long Meccan surahs (≥112 verses).
Longer surahs have larger root-sets and higher baseline Jaccard with
other long surahs. Q 22 is Medinan-78-verse, Q 25 is Meccan-77-verse
— so the core is NOT purely long-surahs. The null uses all 109
non-core surahs with NO length stratification. A stricter secondary
null matched by length (length-bucketed 5-sets) would be a natural
follow-up; **NOT pre-registered here**, so we flag but do not run
(per PRE-REG-STANDARD-03, new cells require new pre-reg → queue as
H-NEW-126.1).

### Shared roots — what's the kernel?

Descriptive observation from the root-counts (not inferential):
the 5-core intersect-union analysis shows 7 roots appear in ALL 5:
these are candidates for the semantic "spine" — but this is a
post-hoc description; full quantitative comparison to random 5-set
shared-roots distribution is queued for H-NEW-126.1.

## Cell B — Genre coherence (descriptive PASS)

**5/5 concept-or-object-named**. 0/5 prophet-named, event-named,
divine-attribute-named, or letter-named.

| Surah | Name | Category | Gloss |
|---:|---|---|---|
| 16 | al-Naḥl | object-name (creature) | the Bee |
| 21 | al-Anbiyāʾ | concept-name (plural) | the Prophets (category, not any specific one) |
| 22 | al-Ḥajj | concept-name (ritual) | the Pilgrimage |
| 23 | al-Muʾminūn | concept-name (plural) | the Believers |
| 25 | al-Furqān | concept-name (epithet) | the Criterion |

Contrast with the 20-cluster HUB surahs:
- Q 62 al-Jumuʿah — event (Friday)
- Q 112 al-Ikhlāṣ — concept (sincerity) but CLUSTERED (qul, invocation, divine-attribute)
- Q 113 al-Falaq, Q 114 al-Nās — concept but CLUSTERED (muʿawwidhatān)
- Q 50 Qāf — letter (muqaṭṭāʿat singleton)

**The 5-core are concept/object-named AND have no structural cluster
membership.** This is a DOUBLE-SIGNATURE.

Interestingly Q 21 al-Anbiyāʾ is a concept-name (plural) while being
HIGH on prophet-narrative density (17.86 per 100v — the highest in
the core). The name signals a THEMATIC-UNIT-ABOUT-PROPHETS, not
a single-prophet-biography (which would get a singular name like
Q 10 Yūnus or Q 12 Yūsuf).

## Cell C — Rhetorical mode (NULL-BROKEN)

Direction DIRECTIONALLY HOLDS (core is 2.8× tighter than null in
imp/int/dec space, obs 5.32 vs null 14.83, p=0.0157) — but **MW-5
positive control FAILED**: the classically-verified tight cluster
musabbiḥāt inner-5 does NOT cluster tight in this space (p=0.67,
obs 16.08 vs null 14.53).

**Per pre-reg, MW-5 failure → NULL-BROKEN regardless of target
result.** The rhetorical-mode instrument is under-powered or
miscalibrated: a cluster known-tight on opener (سبح / يسبح) is not
tight on imp/int/dec. Root cause: the imp/int/dec triple is a very
coarse rhetorical-mode signature; it collapses rich rhetorical
variation to 3 numbers per surah. The 5 musabbiḥāt all open with
سبح/يسبح as their FIRST verse (a non-interrogative, non-imperative
verbal declaration), which places them all at similar (low-imp,
low-int) positions — but they still scatter by the declarative-% due
to different post-opening content distributions.

### Honest interpretation

We CANNOT make an inferential claim about rhetorical-mode clustering
of the 5-core. The observed directional tightness is recorded as
**EXPLORATORY-DIRECTIONAL** and flagged for re-design with a finer
rhetorical-mode axis (e.g., verb/noun/particle per-verse first-POS
distribution; or Abdel Haleem iltifāt detection).

## Cell D — Per-surah uniqueness (descriptive)

Each core surah's single most-extreme axis (vs the 114-surah corpus):

| Surah | Most-extreme axis | Direction | Percentile | Value |
|---:|---|:---:|---:|---:|
| 16 al-Naḥl | unique_root_count | HIGH | 92.5 | 358 roots |
| 21 al-Anbiyāʾ | surah_length | HIGH | 88.2 | 112 verses |
| 22 al-Ḥajj | noldeke_rank | HIGH | 93.4 | rank 107 (late-Medinan outlier in zone) |
| 23 al-Muʾminūn | surah_length | HIGH | 89.0 | 118 verses |
| 25 al-Furqān | unique_root_count | HIGH | 78.5 | 250 roots |

**All 5 core surahs score at HIGH percentiles (78-93) on their
single most-extreme axis.** None is at a LOW-percentile extremum.

The core is characterized by:
- **Vocabulary richness** (Q 16, 25): high unique-root counts
- **Length** (Q 21, 23): top-decile surah-length
- **Late chronology** (Q 22): 93rd percentile Nöldeke, ONLY Medinan
  member of the core

The fact that all 5 sit at high (NOT low) extremes on their most-
distinctive axis suggests the core is "maximalist" on some axis —
each surah is a BIG surah in its way. This is consistent with
al-Naḥl, al-Anbiyāʾ, al-Muʾminūn all being ≥112-verse Meccan
encyclopedic surahs (sometimes grouped informally as Meccan ṭawāl).

## Synthesis — what makes these 5 cluster-empty

Combining Cells A, B, D (C is NULL-BROKEN, removed from synthesis):

1. **They are concept/object-named AND long.** Long Meccan surahs
   are disproportionately muqaṭṭāʿat-opened ([[h-new-46-muqattaat-vs-surah-length|H-NEW-46]] established
   this). The 5-core are EXCEPTIONS: long Meccan surahs that don't
   open with muqaṭṭāʿat and don't take prophet/event/attribute/letter
   names. There are few such surahs; these 5 constitute the pattern.

2. **They share root-vocabulary (2.6× enrichment).** Cell A
   PASS-DIRECTED. The 5 share a CONTENT kernel — invisible to
   structural taxonomies because those taxonomies (cluster systems)
   measure OPENER / NAME / CLUSTER-MEMBERSHIP, not semantic content.

3. **Each is individually a maximalist surah.** Cell D: all 5 are at
   high extremes on some axis (length, roots, or late-chronology).

4. **Chronologically scattered** (Nöldeke 64-107, Late Meccan +
   Medinan). Not a chronological cluster.

5. **Thematic observation** (not formally tested): Q 21 al-Anbiyāʾ,
   Q 23 al-Muʾminūn, Q 25 al-Furqān all have strongly
   "PROPHETOLOGICAL-CRITERIAL" names — they name ABSTRACT categories
   in the prophet-revelation system. Q 22 al-Ḥajj names a ritual
   institution; Q 16 al-Naḥl names a creature used as a sign of
   divine craft. The thematic common denominator is CREATION /
   SIGNS-OF-GOD / PROPHETIC-VERIFICATION — the abstract argumentative
   side of the Quran, NOT the narrative side. Prophet narratives
   appear in these surahs (notably Q 21 at 17.86 prophet-density)
   but are DEPLOYED AS EVIDENCE, not as biography.

**Hypothesis (queued as H-NEW-126.2): The 5-core are the ABSTRACT-
ARGUMENTATIVE MECCAN STRUCTURE surahs — long concept-titled
discourses that mobilize creation, prophet-catalogues, and
eschatological imagery as argumentative evidence, without taking on
a muqaṭṭāʿat marker or a specific prophet/event title. They are
cluster-empty because they belong to a GENRE that has no
formalized structural marker — yet they share the genre's
root-vocabulary (Cell A PASS-DIRECTED).**

## Bonferroni accounting

- k = 4 pre-registered (A, B descriptive, C, D descriptive).
- Inferential cells: A and C only.
- α_bon = 0.0125.
- Cell A passes at p = 0.0009 (7× inside α_bon; also passes the
  single-test α = 0.05 post-hoc cap by 56×).
- Cell C NULL-BROKEN per MW-5 failure.
- Cells B, D are descriptive; no Bonferroni cost. Keeping k=4 in
  YAML is the CONSERVATIVE TIGHTENING choice (Bonferroni asymmetry
  rule: tightening is self-verifying).

## What would CONFIRM (not PASS-DIRECT) Cell A

Per post-hoc protocol, independent replication on a distinct data
dimension is required:
- **Different similarity**: char 5-gram Dice, or [[h-new-66-verse-twins-network|H-NEW-66]] verse-twin
  edge count, on the same 5-core vs null.
- **Different feature space**: non-root structural axis that shows
  the same 5-core grouping.
- **Length-matched null**: re-run Cell A with null 5-sets drawn from
  surahs matched on verse-count (length-bucketed) — if the effect
  survives length control, that is an additional independent
  discriminator.

These are queued as H-NEW-126.1 (length-matched) and H-NEW-126.2
(independent similarity).

## Cross-finding connections

- **[[cross-finding-010-extended-network|cross-finding-010]]**: identifies the 5-core; [[h-new-126-isolate-core|H-NEW-126]] characterizes it.
- **[[h-new-89-meta-cluster-network|H-NEW-89]]**: parent 11-cluster network; [[h-new-126-isolate-core|H-NEW-126]] addresses its
  largest cluster-empty stretch.
- **[[h-new-94-q16-q25-zone|H-NEW-94]]**: Q 16-25 zone deep-dive; its Cell B NULL-BROKEN (contiguous-
  window test under-powered). [[h-new-126-isolate-core|H-NEW-126]] uses a different null (random
  5-sets from non-core) and POWERS the detection.
- **[[h-new-46-muqattaat-vs-surah-length|H-NEW-46]] / [[h-new-46-1-chronology-disentangle|H-NEW-46.1]]**: muqaṭṭāʿat × length × chronology; the
  5-core are the long-non-muqaṭṭāʿat exceptions.
- **[[h-new-125-chronology-content|H-NEW-125]]**: comprehensive chronology-content map (15-axis); the
  5-core will appear as a STRUCTURED OUTLIER subset in any axis they
  share.

## Verdict

**MIXED / PASS-DIRECTED-WITH-CAVEATS**:

- **Cell A**: PASS-DIRECTED at p=0.0009; MW-5 fires; needs length-
  matched replication for full CONFIRMED status
- **Cell B**: DESCRIPTIVE — 5/5 concept-or-object-named; genre-coherent
- **Cell C**: NULL-BROKEN — MW-5 positive control failed; rhetorical-mode
  3-vector is under-powered
- **Cell D**: DESCRIPTIVE — all 5 at high percentile extremes on ≥ 1 axis

The 5-surah isolate core is NOT random heterogeneity. It is a
CONCEPT/OBJECT-NAMED, long, chronologically-scattered, root-
vocabulary-sharing kernel of abstract-argumentative Meccan (+1 Medinan)
discourse — invisible to opener/name/cluster taxonomies yet
detectable at the root-semantic level.

## Files

- Pre-reg: `findings/phase-b-hypotheses/h-new-126-isolate-core-prereg.md`
- Script: `scripts/h_new_126_isolate_core.py`
- JSON: `findings/phase-b-hypotheses/csv/h-new-126.json`
- Journal: `journal/h-new-126-run-1.md`
- Parent cross-finding: `findings/phase-b-hypotheses/cross-finding-010-extended-network.md`
