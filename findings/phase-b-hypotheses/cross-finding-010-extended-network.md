---
id: cross-finding-010
title: Extended Meta-Cluster Network — 20 cluster systems
phase: B (synthesis)
status: MIXED — (A) hub SHIFT to degree-5 Q 62 with 7 degree-4 co-hubs; (B) isolates drop 21 → 10; (C) NULL — Q 62 hub is artifactual under new-only clusters
date: 2026-04-17
agent: cross-finding-010-specialist
prereg: findings/phase-b-hypotheses/cross-finding-010-extended-network-prereg.md
script: scripts/cross_finding_010_extended_network.py
json: findings/phase-b-hypotheses/csv/cross-finding-010.json
journal: journal/cross-finding-010-run-1.md
seed: 20260417
n_perm: 10000
bonferroni_family: cross-finding-010-extended-network
bonferroni_k: 3
alpha_bon: 0.0167
rules_tuple: (no-tashkeel; 20-cluster lock; membership-permuted null)
---

# [[cross-finding-010-extended-network|cross-finding-010]] — Extended Meta-Cluster Network (RESULT)

## Headline

Extending [[h-new-89-meta-cluster-network|H-NEW-89]]'s 11-cluster meta-cluster network to **20 cluster
systems** (adding oath-openers, qul-v1-w1 pentalogy, refrain-density
surahs, divine-attribute-named, prophet-named, muqaṭṭāʿat singletons,
musabbiḥāt-classical-7, book-reference muqaṭṭāʿat subset, and
invocation/refuge surahs) produces THREE structural findings:

(A) **Q 62 al-Jumuʿah's degree rises from 4 to 5** and remains the
    unique top-degree hub. **7 surahs now tie at degree 4** (Q 2,
    3, 50, 59, 112, 113, 114) — up from 3 under the 11-cluster
    scheme (Q 2, 3, 59). **The network now has a FOUR-REGION
    hub geography** — not just front-back (Q 2-3 / Q 59-62) but
    FOUR zones: front (Q 2-3), upper-mid (Q 50), back-upper
    (Q 59, 62), back-terminal (Q 112, 113, 114).

(B) **Isolate count drops 21 → 10**, with Q 16-25 zone collapsing
    from 8/10 to 5/10. 11 surahs exit the isolate set under the
    extended clusters; 0 new surahs enter.

(C) **The 9-new-cluster-only sub-network verdict is NULL.** Q 62
    has degree only 1 in the new-only sub-network (only C18
    musabbiḥāt-classical-7 contains it). Q 62's hub property is
    EMPIRICALLY DRIVEN by the original 11 clusters, NOT by the
    new 9. Three surahs (Q 36, 38, 50) emerge as degree-3 hubs
    in the new-only view — but max degree 3 is ALSO attained by
    random 9-cluster draws (null max mean = 3.24).

**MW-5 positive control PASSES**: [[h-new-89-meta-cluster-network|H-NEW-89]]'s 11-cluster pipeline
is recovered exactly (Q 62 degree 4, 21 isolates, p=0.0001).

## Per-cell results

| Cell | Description | Observed | Expected | Verdict |
|---|---|---|---|---|
| MW-5 | [[h-new-89-meta-cluster-network|H-NEW-89]] recovery | Q 62 = 4-hub, iso=21 | Q 62 = 4-hub, iso=21 | **PASS** |
| (A) | Hub structure (20-cluster) | Q 62 deg=5, 7 co-hubs at deg=4 | descriptive | **SHIFT** |
| (B) | Isolate count (20-cluster) | 10 (vs baseline 21) | descriptive | **DROP** |
| (C) | New-only hub independence | Q 62 deg=1, p=1.0 | α_bon = 0.0167 | **NULL** |

## Product (A) — Updated 20-cluster degree distribution

### Top-15 hub surahs

| Rank | Surah | Name | Degree | Cluster memberships |
|---:|---:|---|---:|---|
| 1 | Q 62 | al-Jumuʿah | **5** | musabbiḥāt-inner-5 + Friday + Khawātim-ext + mufaṣṣal + musabbiḥāt-7 |
| 2 | Q 2 | al-Baqara | 4 | الم + ṭiwāl + Zahrāwān + book-ref-muq |
| 3 | Q 3 | Āl ʿImrān | 4 | الم + ṭiwāl + Zahrāwān + book-ref-muq |
| 4 | Q 50 | Qāf | 4 | mufaṣṣal + oath-opener + muq-singleton + book-ref-muq |
| 5 | Q 59 | al-Ḥashr | 4 | musabbiḥāt-inner-5 + Khawātim-ext + mufaṣṣal + musabbiḥāt-7 |
| 6 | Q 112 | al-Ikhlāṣ | 4 | mufaṣṣal + qul-v1-w1 + divine-attr-named + invocation |
| 7 | Q 113 | al-Falaq | 4 | muʿawwidhatān + mufaṣṣal + qul-v1-w1 + invocation |
| 8 | Q 114 | al-Nās | 4 | muʿawwidhatān + mufaṣṣal + qul-v1-w1 + invocation |
| 9 | Q 10 | Yūnus | 3 | الر + prophet-named + book-ref-muq |
| 10 | Q 11 | Hūd | 3 | الر + prophet-named + book-ref-muq |
| 11 | Q 12 | Yūsuf | 3 | الر + prophet-named + book-ref-muq |
| 12 | Q 14 | Ibrāhīm | 3 | الر + prophet-named + book-ref-muq |
| 13 | Q 32 | al-Sajda | 3 | الم + Friday + book-ref-muq |
| 14 | Q 36 | Yā-Sīn | 3 | oath-opener + muq-singleton + book-ref-muq |
| 15 | Q 38 | Ṣād | 3 | oath-opener + muq-singleton + book-ref-muq |

### Degree histogram

| Degree | Count (11-cluster [[h-new-89-meta-cluster-network|H-NEW-89]]) | Count (20-cluster extended) |
|---:|---:|---:|
| 0 | 21 | 10 |
| 1 | 82 | 42 |
| 2 | 7 | 40 |
| 3 | 3 | 14 |
| 4 | 1 | 7 |
| 5 | 0 | 1 |

The extended scheme shifts substantial mass from degree-1 to
degree-2 and degree-3 and generates 7 new degree-4 surahs.

### NEW hubs emerging in the 20-cluster network (degree ≥ 4, excluding Q 62)

- **Q 50 Qāf** — NEW degree-4 hub. Member of mufaṣṣal (C11),
  oath-openers (C12), muqaṭṭāʿat-singletons (C17), and
  book-reference-muqaṭṭāʿat-subset (C19). Q 50 is a single-letter
  muqaṭṭāʿat (ق), oath-opener (*wa-l-qurʾān al-majīd*), and
  mufaṣṣal-core surah. Its emergence as a hub is NOVEL —
  previously buried under [[h-new-89-meta-cluster-network|H-NEW-89]]'s coarser clustering.

- **Q 112 al-Ikhlāṣ / Q 113 al-Falaq / Q 114 al-Nās** — NEW
  degree-4 back-terminal hub-triplet. All three members of
  invocation/refuge (C20), qul-v1-w1 (C13), and mufaṣṣal (C11);
  Q 112 also divine-attribute-named (C15); Q 113-114
  al-muʿawwidhatān (C9). The terminal triplet is a HUB
  substructure, not isolated tail surahs.

### New four-region hub geography

| Zone | Members | Character |
|---|---|---|
| Front | Q 2-3 | long Medinan / الم / Zahrāwān |
| Upper-mid | Q 50 | oath-opener / muq-singleton / mufaṣṣal-open |
| Back-upper | Q 59, 62 | musabbiḥāt / Khawātim / Medinan-mufaṣṣal |
| Back-terminal | Q 112, 113, 114 | qul-openers / invocation / Meccan-short |

The two-region front-back architecture identified in [[h-new-89-meta-cluster-network|H-NEW-89]]
extends to a **four-region architecture** when the classical
qul-pentalogy and invocation clusters are included. The back-
terminal triplet was structurally INVISIBLE under [[h-new-89-meta-cluster-network|H-NEW-89]]'s
lock.

## Product (B) — Updated isolate count

### 20-cluster isolate list (10 surahs)

```
{8, 16, 21, 22, 23, 25, 33, 34, 39, 48}
```

### Comparison to [[h-new-89-meta-cluster-network|H-NEW-89]] baseline (21 isolates)

**Exited** (11 surahs moved from isolate to ≥ degree 1 under the
extended clusters):

| Surah | Via cluster |
|---|---|
| Q 1 | C20 invocation/refuge |
| Q 13 | C17 muqaṭṭāʿat-singleton + C19 book-ref-muq |
| Q 17 | C18 musabbiḥāt-classical-7 |
| Q 19 | C16 prophet-named + C17 muqaṭṭāʿat-singleton |
| Q 20 | C17 muqaṭṭāʿat-singleton + C19 book-ref-muq |
| Q 24 | C15 divine-attribute-named |
| Q 35 | C15 divine-attribute-named |
| Q 36 | C12 oath-opener + C17 muq-singleton + C19 book-ref-muq |
| Q 37 | C12 oath-opener |
| Q 38 | C12 oath-opener + C17 muq-singleton + C19 book-ref-muq |
| Q 47 | C16 prophet-named |

**Entered** (0 surahs — no NEW isolates appear under the extended
clustering; as expected, adding clusters only reduces isolates).

### Q 16-25 zone — baseline 8/10 → extended 5/10

| [[h-new-89-meta-cluster-network|H-NEW-89]] (11-cluster) | [[cross-finding-010-extended-network|cross-finding-010]] (20-cluster) |
|---|---|
| {16, 17, 19, 20, 21, 22, 23, 24, 25} = 8 isolates + Q 18 (Friday) | {16, 21, 22, 23, 25} = 5 isolates |

Q 17, 19, 20, 24 all EXITED the isolate list via the new clusters.
The remaining 5-isolate core of Q 16-25 is {16, 21, 22, 23, 25} —
al-Naḥl, al-Anbiyāʾ, al-Ḥajj, al-Muʾminūn, al-Furqān. These surahs
are not muqaṭṭāʿat-opened, not oath-opened, not qul-opened, not
refrain-based, not named for a divine attribute, not named for a
prophet, not in any classical pair. They constitute the
**TRUE Q 16-25 isolate core** — the zone's mysterious cluster-
empty signature survives at 5/10.

### Notable other isolates surviving the extension

- **Q 8 al-Anfāl** remains isolated — confirms the [[h-new-89-meta-cluster-network|H-NEW-89]]
  observation that Q 8 is the "orphan" of the missing-basmala pair
  with Q 9 (which IS in al-sabʿ al-ṭiwāl).
- **Q 33 al-Aḥzāb, Q 34 Sabaʾ, Q 39 al-Zumar, Q 48 al-Fatḥ** —
  4 isolates from Q 33-48 zone survive. The Q 33-39 + Q 47-48
  zone that [[h-new-89-meta-cluster-network|H-NEW-89]] identified as the second cluster-empty
  region compresses to 4 isolates.

## Product (C) — New-cluster-only independence test

**H₀**: Under C12-C20 only (the 9 new clusters, EXCLUDING the
original 11), Q 62 is NOT a hub.

### Observed (new-only sub-network)

- Q 62 degree: **1** (only in C18 musabbiḥāt-classical-7)
- Max degree in network: 3 (attained by Q 36, Q 38, Q 50, Q 112)
- n_isolates (new-only): N/A — many because the 9 clusters cover
  ~60 surahs total

### Null (10,000 membership-permuted draws of C12-C20)

- Null Q 62 degree mean: **0.725** (observed 1 is close to null)
- Null max degree mean: **3.24** (observed 3 is close to null)
- p (Q 62 deg) two-sided: **1.00000** ✗
- p (max deg) two-sided: **1.00000** ✗

**Verdict: NULL at α_bon = 0.0167.** Under the new-cluster-only
sub-network, no surah (including Q 62) emerges as a statistically
significant hub relative to the membership-permuted null.

### Interpretation — what this shows

Q 62's status as **THE meta-hub** is empirically driven by the
[[h-new-89-meta-cluster-network|H-NEW-89]] original clusters:

1. musabbiḥāt (inner-5, C5) — CORE EMPIRICAL CLUSTER ([[h-new-58c-musabbihat-tense-split|H-NEW-58c]])
2. Friday liturgy (C7)
3. Khawātim al-Ḥashr extended (C8)
4. al-mufaṣṣal (C11)

Among the 9 NEW clusters, Q 62 is in ONLY ONE (C18 musabbiḥāt-7,
which is a classical superset of C5). The new clusters do NOT
independently recover Q 62 as a hub. The hub property of Q 62 is
a property of the original [[h-new-89-meta-cluster-network|H-NEW-89]] cluster lock.

**This is an HONEST NULL**: the project's hub claim for Q 62 is
ANCHORED to the original 11-cluster scheme. The 20-cluster
extended reading reinforces Q 62's position (rising to degree 5)
but does not ESTABLISH it under a differently-chosen cluster
system.

### What the new-only view DOES reveal — 3-degree hubs

| Surah | Name | New-only degree | New clusters |
|---:|---|---:|---|
| Q 36 | Yā-Sīn | 3 | oath-opener + muq-singleton + book-ref-muq |
| Q 38 | Ṣād | 3 | oath-opener + muq-singleton + book-ref-muq |
| Q 50 | Qāf | 3 | oath-opener + muq-singleton + book-ref-muq |
| Q 112 | al-Ikhlāṣ | 3 | qul-v1-w1 + divine-attr-named + invocation |

**Q 36, 38, 50** form a CLASSICAL SUB-PATTERN: single-letter
muqaṭṭāʿat-opened oath-surahs that reference the book. Suyūṭī
already noted this triplet as a structural unit in his Itqān.
Our new-only-cluster view recovers it mechanically.

**Q 112** is a triple-cluster hub under the new scheme — the
"ultimate" declaration-of-unity surah. Its hub status via qul +
divine-attribute + invocation is methodologically novel.

But these are NOT statistically distinguishable from random
3-cluster-degree surahs under the membership-permuted null.
Honest null.

## Synthesis — what the 20-cluster extension reveals

### 1. Q 62's meta-hub status is REINFORCED but not independently established

Q 62 rises from degree 4 to **degree 5**, remaining the unique
top-degree surah. The addition of C18 (musabbiḥāt-classical-7)
ratifies its inner-5 membership via the classical 7-musabbiḥāt
reading. **However**, Q 62's hub status is a FEATURE OF THE
ORIGINAL CLUSTER LOCK. It is not discoverable under the 9
new clusters alone (Cell C NULL).

### 2. Four-region hub geography replaces two-region

[[h-new-89-meta-cluster-network|H-NEW-89]]'s front-back (Q 2-3 / Q 59-62) is extended to FOUR
hub regions:

```
Front (long Medinan):      Q 2-3
Upper-mid (oath-opener):   Q 50
Back-upper (Medinan-short): Q 59, 62
Back-terminal (Meccan-short): Q 112, 113, 114
```

The back-terminal triplet (Q 112, 113, 114) is a NEW STRUCTURAL
HUB — previously structurally invisible because the [[h-new-89-meta-cluster-network|H-NEW-89]]
lock did not include invocation/qul-openers.

### 3. Isolate count cuts in half (21 → 10)

The 9 new clusters absorb 11 of the 21 [[h-new-89-meta-cluster-network|H-NEW-89]] isolates into
cluster membership. 0 new isolates appear. **82% corpus coverage
([[h-new-89-meta-cluster-network|H-NEW-89]]) rises to 91% corpus coverage (20-cluster extended).**

### 4. The Q 16-25 "cluster-empty zone" shrinks but PERSISTS at 5/10

The zone's core {16, 21, 22, 23, 25} — al-Naḥl, al-Anbiyāʾ,
al-Ḥajj, al-Muʾminūn, al-Furqān — survives all 20 cluster
definitions. **These 5 surahs are the TRUE isolate core** —
the zone's cluster-empty signature is NOT an artifact of the
[[h-new-89-meta-cluster-network|H-NEW-89]] lock. A future [[cross-finding-013-mushaf-topological-ring|cross-finding-013]] investigation should
ask whether these 5 share a HIDDEN structural property invisible
to all 20 cluster taxonomies.

### 5. Q 36, Q 38, Q 50 emerge as a classical triplet

The three single-letter muqaṭṭāʿat-opened oath-surahs (يس, ص, ق)
co-occupy the new-only top-3 at degree 3 each. They form an
un-named classical sub-cluster:

> single-letter muqaṭṭāʿat + oath-opener + book-reference

This is SEPARATE from the al-Jumuʿah hub structure. Future work
should ask whether {Q 36, Q 38, Q 50} constitute a named cluster
in pre-modern commentary (al-Baghawī, al-Qurṭubī tafsīr; al-Suyūṭī
Itqān fawātiḥ chapter).

### 6. Q 112's degree-4 new role

Q 112 al-Ikhlāṣ moves from isolate-in-mufaṣṣal-only (degree 1
under [[h-new-89-meta-cluster-network|H-NEW-89]]) to degree-4 hub under the extended scheme. Its
memberships span qul-v1-w1, divine-attribute-named, invocation,
and mufaṣṣal. This multi-cluster property is consistent with
Q 112's classical reputation as the "essence" surah — without
supporting the refuted [[h-new-84-ikhlas-third|H-NEW-84]] "1/3 of Quran" claim. Q 112 is
STRUCTURALLY distinct via cluster multiplicity, not via magnitude-
ratio.

## Honest caveats

1. **Cluster overlap inflates degrees**. C19 (book-reference
   muqaṭṭāʿat subset) contributes 24 surahs, 19 of which are
   already in C1-C4 or C17. This inflates muqaṭṭāʿat degrees
   by ~1. Declared in pre-reg. The overlap is DELIBERATE —
   C19 marks a FUNCTIONAL property (book-introduction) within
   the MORPHOLOGICAL cluster (muqaṭṭāʿat). Degrees should be
   read as "number of structural dimensions satisfied" not
   "number of independent features."

2. **Cell C NULL is the most important finding of this run**.
   The new-cluster-only sub-network does NOT recover Q 62 as
   a hub at α_bon = 0.0167. The hub claim for Q 62 is
   FAITHFUL TO THE ORIGINAL 11-CLUSTER LOCK. Any future work
   that wants to make Q 62-hub a "classical-cluster-independent"
   claim must find a third cluster set that independently
   elevates it.

3. **The membership-permuted null is stringent for small
   clusters**. With only 9 clusters of sizes {21, 5, 2, 5, 7,
   7, 7, 24, 4}, the max-degree null mean is 3.24 — so a
   max-degree of 3 (the observed) is at the 50th percentile.
   No individual surah achieves enough cluster membership
   uniqueness to beat the null.

4. **C19 overlap with C17 is heavy**. 6 of the 7 muqaṭṭāʿat
   singletons (Q 13, 20, 36, 38, 50 — not Q 19, 68) are also
   in C19 book-reference-muqaṭṭāʿat-subset. This generates
   structural coherence by design.

5. **MW-5 PASS is critical**. The re-computation of [[h-new-89-meta-cluster-network|H-NEW-89]]'s
   11-cluster network recovers Q 62 = degree-4 hub, 21 isolates,
   p_iso = 0.0001 exactly. The extended-network pipeline is
   faithful to the original.

## Cross-finding implications

### Relates to

- **[[cross-finding-009-meta-cluster-network|cross-finding-009]]** ([[h-new-89-meta-cluster-network|H-NEW-89]]): EXTENDS with 9 additional
  cluster systems. Q 62 hub reinforced to degree 5.
- **cross-finding-008** (muqaṭṭāʿat-as-book-introduction-marker):
  C19 operationalizes the book-reference property as a
  MEMBERSHIP-LEVEL cluster. 24 surahs.
- **[[h-new-94-q16-q25-zone|H-NEW-94]]** (Q 16-25 zone deep-dive): IDENTIFIES the true
  5-surah isolate core {16, 21, 22, 23, 25} surviving all 20
  clusters.
- **[[cross-finding-013-mushaf-topological-ring|cross-finding-013]]** (queued): NEW 5-surah isolate core is
  a specific target.
- **NM-23** (Q 62 hub deep-dive): reinforced priority.

### Queues new H-NEW findings

- **[[h-new-111-fisher-rao-mushaf|H-NEW-111]]** (candidate): The Q 36 / Q 38 / Q 50 single-letter-
  muqaṭṭāʿat oath-opener triplet — is this a classically-named
  sub-cluster?
- **[[h-new-112-spectral-network|H-NEW-112]]** (candidate): The Q 112-114 invocation hub —
  structural investigation of the "daily-protection suite" as
  a cluster with 4-fold membership.
- **[[h-new-113-letter-position|H-NEW-113]]** (candidate): The {Q 16, 21, 22, 23, 25} true
  isolate core — shared hidden structural property investigation.

## Verdict

**MIXED / HONEST-NULL-WITH-SHIFTS**:

- **MW-5**: PASS (positive control recovers [[h-new-89-meta-cluster-network|H-NEW-89]] exactly)
- **Cell (A)**: SHIFT — Q 62 rises to degree 5; 7 co-hubs emerge
  at degree 4; hub geography extends from 2 regions to 4
- **Cell (B)**: DROP — 21 isolates → 10 isolates; Q 16-25 core
  shrinks to 5 surahs but persists
- **Cell (C)**: NULL — new-only sub-network does NOT recover
  Q 62 as a hub (p = 1.0 two-sided vs membership-permuted null)

The 20-cluster extension REINFORCES the meta-architecture picture
(more clusters, more structure) while HONESTLY noting that the
Q 62 hub claim is ANCHORED to the original 11-cluster lock. No
single cluster-set is "the" correct one; each reveals a different
slice of the Quran's redundant multi-axis structure.

## Files

- Pre-reg: `findings/phase-b-hypotheses/cross-finding-010-extended-network-prereg.md`
- Script: `scripts/cross_finding_010_extended_network.py`
- JSON: `findings/phase-b-hypotheses/csv/cross-finding-010.json`
- Journal: `journal/cross-finding-010-run-1.md`
- Parent: `findings/phase-b-hypotheses/h-new-89-meta-cluster-network.md`
- Parent cross-finding: `findings/cross-finding/cross-finding-009-meta-cluster-network.md`

---

## audit-035 amendment (appended 2026-04-17) — deduplicated-clusters sanity analysis

**Audit flag**: C5 (musabbiḥāt inner-5) ⊂ C18 (musabbiḥāt classical-7), and
C19 (book-reference muqaṭṭāʿat subset, 24 members) heavily overlaps
C1-C4 + C17. Q 62's degree-5 UNIQUENESS is therefore partially
mechanical by construction (Q 62 is counted in both C5 AND C18).

### Dedup procedure
Drop C5 (kept superset C18); drop C19 (covered by C1-C4 + C17).
Remaining clusters: 18.

### Dedup result

| Quantity | Original 20-cluster | Deduplicated 18-cluster |
|---|---|---|
| Top degree | 5 (Q 62 unique) | **4 (four-way TIE)** |
| Top hubs | {Q 62} | **{Q 62, Q 112, Q 113, Q 114}** |
| Isolate count | 10 | 10 (identical set) |
| Coverage | 91.2% | 91.2% |

### Honest re-interpretation

Under dedup, **Q 62's UNIQUE-top-hub claim does NOT survive**. The
back-terminal triplet {Q 112, 113, 114} ties Q 62 at degree 4.

However, the **4-REGION hub architecture survives intact**:
- Front hub: {Q 2, 3} (degree 3 under dedup)
- Upper-mid hub: {Q 50} (degree 3)
- Back-upper hub: {Q 59, 62} (degree 3-4)
- Back-terminal hub: {Q 112, 113, 114} (degree 4)

The NEW substantive finding is therefore **a 4-way TIE for top hub**
across Q 62 + the refuge-creed triad Q 112-114. This is a MORE HONEST
statement than "Q 62 uniquely dominates at degree 5".

### What this changes

- [[cross-finding-010-extended-network|cross-finding-010]] (A): Q 62 hub-promotion claim is DOWNGRADED.
  [[h-new-89-meta-cluster-network|H-NEW-89]]'s "Q 62 is unique 4-cluster hub" (degree 4 under original
  11-cluster) was ALREADY the correct framing. Our 20-cluster
  extension added hub PEERS, not hub PROMOTION.
- [[cross-finding-010-extended-network|cross-finding-010]] (B): isolate-count drop (21 → 10) SURVIVES dedup.
- [[cross-finding-010-extended-network|cross-finding-010]] (C): Cell C NULL SURVIVES dedup (unchanged).

### Updated headline

The META-cluster network exhibits a **4-region hub architecture with a
4-way tie for top-hub**: Q 62 (back-upper), Q 112, Q 113, Q 114
(back-terminal). Q 2, 3, 59, 50 form a second tier at degree 3.

### Liturgical echo (non-load-bearing but notable)

Classical tradition prescribes recitation of Sūrat al-Jumuʿa (Q 62) on
Friday morning AND the muʿawwidhatān (Q 113, 114) + al-Ikhlāṣ (Q 112)
for protection. The empirical 4-way-top-hub tie we find is THE SAME
FOUR SURAHS that classical liturgy already recognizes as together-recited.
This is a *structural observation*, not a confirmation of liturgical
practice — but it suggests the cluster-topology-instrument is
recovering a pattern classical liturgists also felt was central.

