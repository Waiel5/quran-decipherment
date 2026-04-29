---
id: H-NEW-94
title: Q 16-25 cluster-empty zone deep-dive — isolate-count reconciliation + shadow-cluster hunt
phase: B
status: Cell A DESCRIPTIVE (reconciled with H-NEW-89 reporting correction); Cell B NULL-BROKEN (MW-5 failed)
prereg: h-new-94-q16-q25-zone-prereg.md
script: scripts/h_new_94_q16_q25_zone.py
json: findings/phase-b-hypotheses/csv/h-new-94.json
date: 2026-04-17
agent: h-new-94-specialist
seed: 20260417
n_perm: 10000
bonferroni_family: h-new-94-cluster-empty-zone
bonferroni_k: 2
alpha_bon: 0.025
rules_tuple: "(no-tashkeel; morphology-0.4-roots; H-NEW-89 locked clusters; H-NEW-66 top-50 verse-twin edges)"
---

# [[h-new-94-q16-q25-zone|H-NEW-94]] — Q 16-25 cluster-empty zone deep-dive (RESULT)

## Headline

- **Cell A (descriptive)**: The [[h-new-89-meta-cluster-network|H-NEW-89]] isolate count of **21 total**
  is CONFIRMED. But [[h-new-89-meta-cluster-network|H-NEW-89]]'s in-text claim of "**8 of 10** isolates
  in Q 16-25" is a minor reporting error; under its own locked rules
  the correct figure is **9 of 10**. The only non-isolate in the zone
  is **Q 18 al-Kahf** (via C7 Friday-liturgy cluster). Q 19 Maryam
  (كهيعص) and Q 20 Ṭā-Hā (طه) are classical **singletons**; under
  [[h-new-89-meta-cluster-network|H-NEW-89]]'s ≥2-surah multi-surah-cluster rule they correctly do
  not count as muqaṭṭāʿat-cluster members. Their isolate status is
  faithful to the rule, not an error.

- **Cell B (primary inferential)**: **NULL-BROKEN.** MW-5 positive
  control failed. The Q 16-25 internal similarity (T = 5019) is
  directionally above the null mean of 3918 (**83rd percentile** /
  rank 18 of 105 contiguous 10-surah windows), but at p = 0.168
  — far from α_bon = 0.025 and far from unadjusted α = 0.05.
  The MW-5 positive-control windows Q 57-64 (musabbiḥāt) and
  Q 40-46 (ḥawāmīm) also FAILED to fire at α = 0.05 (p = 0.38
  and p = 0.18 respectively). This tells us the contiguous-window
  test against contiguous-window null is under-powered against
  classically-verified clusters that are NOT tightly contiguous
  (the musabbiḥāt skip Q 58, 60, 63; the ḥawāmīm are contiguous
  but so are many other similar-length back-of-mushaf zones).
  Per pre-reg, MW-5 failure → NULL-BROKEN regardless of the
  target result.

## Per-cell results

### Cell A — Isolate-count reconciliation

Under [[h-new-89-meta-cluster-network|H-NEW-89]]'s locked 11-cluster rule set (≥2-surah classical
multi-surah clusters; cluster list verbatim from
`scripts/h_new_89_meta_cluster_network.py`):

```
All 21 isolates (H-NEW-89 rule):
  {1, 8, 13, 16, 17, 19, 20, 21, 22, 23, 24, 25, 33, 34, 35, 36, 37, 38, 39, 47, 48}

Q 16-25 zone isolates (9 of 10):
  {16, 17, 19, 20, 21, 22, 23, 24, 25}

Q 16-25 zone non-isolate (1 of 10):
  Q 18 al-Kahf — member of C7 Friday-liturgy cluster
```

| [[h-new-89-meta-cluster-network|H-NEW-89]] in-text claim | [[h-new-89-meta-cluster-network|H-NEW-89]] correct value under rule | Note |
|---|---|---|
| "21 isolates total" | 21 | ✓ match |
| "8 of 10 isolates in Q 16-25" | **9 of 10** | **reporting correction** |

**Alternative-rule sensitivity**: under a ruleset that admits
singleton-muqaṭṭāʿat self-clusters {13}, {19}, {20}, {36}, {38},
{50}, {68}, the total isolate count drops to 16 and the zone
isolate count drops to 7 (Q 19 and Q 20 gain degree 1). This is
the "non-H-NEW-89" reading referenced in the [[h-new-89-meta-cluster-network|H-NEW-89]] honest
caveats §1. We report it for transparency and do NOT alter the
[[h-new-89-meta-cluster-network|H-NEW-89]] verdict.

**Reconciliation summary**: Q 19 and Q 20 are NOT "missing"
muqaṭṭāʿat clusters; they are *singleton* muqaṭṭāʿat openers
that the [[h-new-89-meta-cluster-network|H-NEW-89]] rule-set (≥2-member clusters only) legitimately
excludes from cluster membership. The 8-vs-9 discrepancy in the
zone tally is a minor reporting error in [[h-new-89-meta-cluster-network|H-NEW-89]]'s published
findings file; the underlying data and top-line total (21) stand.

### Cell B — Shadow-cluster hunt

Three per-surah similarity axes aggregated by rank-mean (see pre-reg):

| Axis | Operationalization | Range | Mean |
|---|---|---|---|
| S1 root-Jaccard | surah × root binary membership (morphology-0.4) | [0, 0.496] | 0.134 |
| S2 char 5-gram Dice | concatenated normalized text | [0, 0.417] | 0.071 |
| S3 verse-twin edges | [[h-new-66-verse-twins-network|H-NEW-66]] top-50 inter-surah edge count | [0, 4] | 0.007 |

Test statistic: **T = mean(S_agg) over the 45 pairs inside the
10-surah zone Q 16-25**. Null: 10,000 contiguous 10-surah windows
{a, a+1, ..., a+9} with a ∈ {1..105} \ {16}, seed 20260417.

| Metric | Observed | Null |
|---|---|---|
| T (mean S_agg) | **5019.4** | mean = 3918.4 (median 4096.0) |
| Null min / max | — | 1624.0 / 5504.0 |
| p (one-sided upper) | **0.168** | (not significant at α_bon=0.025) |
| Bonferroni pass | **NO** | — |

Q 16-25 ranks **18 of 105** contiguous 10-surah windows by
internal S_agg density (83rd percentile). The densest-10-surah
window is actually **Q 2-11** (T = 5504), followed by Q 3-12
(T = 5384), Q 4-13 (T = 5327). The front of the mushaf (long
Meccan surahs sharing thematic bulk) produces the highest
contiguous-window similarity densities.

**Top-5 Q 16-25 internal pairs by S_agg** (descriptive, POST-HOC;
not an inferential test):

| Pair | S_agg (rank-mean) | S1 root-Jaccard | S2 char-5gram Dice | S3 twins |
|---|---:|---:|---:|---:|
| Q 16 ↔ Q 22 | 5330.5 | 0.406 | 0.282 | 0 |
| Q 17 ↔ Q 25 | 5299.0 | 0.380 | 0.260 | 0 |
| Q 21 ↔ Q 23 | 5292.7 | 0.367 | 0.267 | 0 |
| Q 16 ↔ Q 23 | 5270.8 | 0.370 | 0.246 | 0 |
| Q 17 ↔ Q 18 | 5239.5 | 0.362 | 0.235 | 0 |

Interpretation-safe observation (NOT an inferential claim): the
top-5 list's top pair is Q 16 al-Naḥl ↔ Q 22 al-Ḥajj — Q 16 is
Late Meccan natural-theology (the Bee, the sky, the creation
argument) and Q 22 is Medinan pilgrimage/idolatry-refutation; they
share creation-argument root vocabulary. Q 17 ↔ Q 25 are both
dhikr-of-Quran + Judgment polemic surahs.

### MW-5 positive controls

| Control | Window | Observed T | Null mean | p (one-sided upper) | Fires at α=0.05? |
|---|---|---:|---:|---:|:---:|
| Q 57-64 (musabbiḥāt — 5 of 8 are musabbiḥāt) | Q 57-64, n=8 | 4706 | 3917 | 0.382 | **NO** |
| Q 40-46 (ḥawāmīm — all 7 are) | Q 40-46, n=7 | 5029 | 3916 | 0.179 | **NO** |

**MW-5 DIAGNOSIS**: both controls FAIL. The test instrument is
under-powered against classically-verified clusters. Two reasons:

1. **Musabbiḥāt are discontiguous**: 5 of 5 musabbiḥāt are in
   {57, 59, 61, 62, 64}, but the contiguous 8-surah window Q 57-64
   includes Q 58 al-Mujādila, Q 60 al-Mumtaḥana, Q 63 al-Munāfiqūn
   — three short Medinan polemical surahs that do NOT share the
   musabbiḥ-opening + divine-name-list formula. The window dilutes
   the signal.
2. **Ḥawāmīm are internally similar but so are many back-of-mushaf
   windows**: the null includes many mufaṣṣal contiguous windows
   whose internal similarity is comparable to the ḥawāmīm's.
   S_agg is insufficiently sensitive to the specific *opening-formula*
   + *divine-name-list* signature that characterizes the ḥawāmīm.

Per pre-reg, Cell B is declared **NULL-BROKEN**.

## What this tells us about Q 16-25

Even though Cell B is formally NULL-BROKEN (so we cannot make a
statistical claim), the DESCRIPTIVE pattern is honest:

1. Q 16-25 internal similarity IS above the median contiguous 10-surah
   window (83rd percentile).
2. The zone has **two hub surahs by internal S_agg**: Q 16 (al-Naḥl)
   appears in 2 of top 5, Q 17 (al-Isrāʾ) in 2 of top 5, Q 23 in 2.
3. The zone is NOT more similar than the front-of-mushaf long-Meccan
   block Q 2-11 (the densest contiguous 10-surah window by this test).
4. Q 19 and Q 20 do NOT stand out as outliers inside the zone — their
   pairs have S_agg in the middle of the 45-pair distribution.

**Interpretation**: Q 16-25 is a **moderately-internally-similar
stretch of mid-mushaf Late-Meccan-to-Medinan prophet-narrative
and reminder-exhortation surahs**. Q 22 al-Ḥajj is the Medinan
outlier but shares root-level vocabulary with the Meccan surahs
around it because pilgrimage vocabulary overlaps with
creation-argument vocabulary (divine-sign language). The zone
has NO discovered shadow cluster of the [[h-new-58c-musabbihat-tense-split|H-NEW-58c]] or [[h-new-67-sab-tiwal-mathani|H-NEW-67]]
type (neither a shared-formula opening cluster like musabbiḥāt
nor a shared-structural-class like the long surahs). It is
genuinely **cluster-empty in the [[h-new-89-meta-cluster-network|H-NEW-89]] sense** — these surahs
each tell their own story without a classical collective tag
binding them, and the content-similarity instrument applied here
does NOT resolve a sub-cluster that the [[h-new-89-meta-cluster-network|H-NEW-89]] cluster-taxonomy
missed.

## Thematic context (one paragraph)

Q 16 al-Naḥl (the Bee — 128 verses Late Meccan; natural-theology
and creation-sign polemic), Q 17 al-Isrāʾ (the Night Journey —
opens with "subḥāna alladhī asrā bi-ʿabdihī", a musabbiḥa-adjacent
formula; 111 verses; Children-of-Israel and Prophet-mission themes),
Q 18 al-Kahf (the Cave — the Friday-liturgy surah; four narratives
— Cave sleepers / Adam and Iblīs rehearsed / Moses and al-Khiḍr /
Dhū al-Qarnayn; see [[h-new-90-kahf-narrative-structure|H-NEW-90]]), Q 19 Maryam (Mary — the كهيعص
singleton; infant Jesus, Zachariah, Abraham, Moses), Q 20 Ṭā-Hā
(the طه singleton; long Moses narrative + Adam narrative +
Qur'an self-description), Q 21 al-Anbiyāʾ (the Prophets — 18
prophets cycled in one surah), Q 22 al-Ḥajj (the Pilgrimage —
uniquely Medinan in the zone; mixes Meccan creation-sign material
with Medinan legal content; the only surah with two sajdas),
Q 23 al-Muʾminūn (the Believers — opens with prayer + zakāh
characterization of believers), Q 24 al-Nūr (Light — contains
āyat al-nūr Q 24:35, the project's light-vocabulary #1 verse;
Medinan legal-ethical content), Q 25 al-Furqān (the Criterion —
Quran as discriminator; prophetic defense). Five of ten are
Medinan or partially Medinan, five are Late Meccan. The
unifying thread is **individual prophet narratives + reminder
polemic** — not a formal cluster signature. The zone's
cluster-empty status in [[h-new-89-meta-cluster-network|H-NEW-89]] reflects the fact that these
surahs were NOT given classical collective names — each stands
on its own content, and the classical tradition did not abstract
any of them into a shared-formula cluster.

## Files

- Pre-reg: `findings/phase-b-hypotheses/h-new-94-q16-q25-zone-prereg.md`
- Script:  `scripts/h_new_94_q16_q25_zone.py`
- JSON:    `findings/phase-b-hypotheses/csv/h-new-94.json`
- Journal: `journal/h-new-94-run-1.md`

## Honest caveats

1. Cell B is NULL-BROKEN due to MW-5 failure, so the zone-vs-random
   test cannot be formally interpreted as "Q 16-25 is NOT a shadow
   cluster." It's more accurate to say: "the zone-vs-random
   contiguous-window test is under-powered to detect classically-
   verified content clusters at this resolution, so we cannot
   resolve a shadow cluster in Q 16-25 using this instrument."

2. A more powerful instrument (e.g., non-contiguous member-permuted
   null matching the known-cluster-density, or a higher-resolution
   similarity metric that captures opening-formula and divine-name
   signatures specifically) could resolve this. That would be a
   separate H-NEW-N.M pre-reg.

3. The [[h-new-89-meta-cluster-network|H-NEW-89]] "8 of 10" vs actual "9 of 10" reporting error is
   minor and does NOT alter the [[h-new-89-meta-cluster-network|H-NEW-89]] verdict (PASS at 2/3
   inferential cells was driven by the isolate-count total and
   the hub-zone back-loading, not by the zone-local count).

4. The [[h-new-89-meta-cluster-network|H-NEW-89]] caveat §1 about singleton-muqaṭṭāʿat rule choice
   is now operationalized: under the singleton-admitting rule,
   the zone isolate count is 7 and Q 19, 20 gain membership. Our
   Cell A is faithful to [[h-new-89-meta-cluster-network|H-NEW-89]]'s locked rule.

## Verdict

- **Cell A**: DESCRIPTIVE reconciliation complete; [[h-new-89-meta-cluster-network|H-NEW-89]] in-text
  count "8 of 10" corrected to **9 of 10**. Total isolate count 21
  confirmed.
- **Cell B**: **NULL-BROKEN** (MW-5 failure). Q 16-25 IS directionally
  more internally-similar than random contiguous 10-surah windows
  (83rd percentile, p = 0.168), but the instrument is under-powered
  and the result cannot be formally promoted. A shadow cluster in
  Q 16-25 is NOT resolved by this test; the zone remains genuinely
  cluster-empty under the [[h-new-89-meta-cluster-network|H-NEW-89]] taxonomy.

Updates to downstream:
- OQ-2 answer is PARTIAL: the zone is descriptively moderately-dense
  (not extreme) and has no statistically-resolved shadow cluster at
  this resolution. Future OQ-2 work should use a non-contiguous
  null and higher-resolution signatures.
- MASTER-LEDGER: [[h-new-89-meta-cluster-network|H-NEW-89]] reporting correction logged ("8 of 10" →
  "9 of 10"); total 21 stands.
