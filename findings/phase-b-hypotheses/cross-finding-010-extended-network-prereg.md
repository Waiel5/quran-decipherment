---
id: cross-finding-010
title: Meta-Cluster Network EXTENDED — from 11 to 20+ cluster systems
phase: B (synthesis)
status: PRE-REGISTERED 2026-04-17
spec_locked_at: 2026-04-17 (BEFORE graph projection of the 9 new clusters)
agent: cross-finding-010-specialist
parent_findings:
  - H-NEW-89 / cross-finding-009 (11-cluster network, Q 62 4-hub)
  - H-NEW-85 (oath-opener corpus, 21 surahs)
  - H-NEW-74 (qul-v1-w1 pentalogy, 5 surahs)
  - H-NEW-83 (Q 55 and Q 77 refrain-density corpus)
  - H-NEW-58c / H-NEW-103 (musabbiḥāt 4-form typology)
  - H-NEW-53 (book-reference enrichment in muqaṭṭāʿat)
  - H-NEW-49 / 49.1 (prophet-named surahs)
  - H-NEW-93 (Q 29 + Q 30 non-book-reference sub-cluster)
  - cross-finding-008 (muqaṭṭāʿat-as-book-introduction markers)
bonferroni_family: cross-finding-010-extended-network
bonferroni_k: 3
alpha_bon: 0.0167   # 0.05 / 3
seed: 20260417
n_perm: 10000
rules_tuple: (no-tashkeel; cluster-membership taken verbatim from existing locked finding files; 20-cluster extended lock)
prior_runs_consumed: 0   # THIS PRE-REG LOCKED BEFORE THE 20-CLUSTER RUN
---

# [[cross-finding-010-extended-network|cross-finding-010]] — Extended Meta-Cluster Network (Pre-registration)

## Purpose and relation to [[cross-finding-009-meta-cluster-network|cross-finding-009]]

[[h-new-89-meta-cluster-network|H-NEW-89]] / [[cross-finding-009-meta-cluster-network|cross-finding-009]] established an 11-cluster meta-cluster
network of the Quran, with Q 62 al-Jumuʿah as the unique 4-cluster
meta-hub. This synthesis finding EXTENDS the incidence matrix from
11 to 20 cluster systems by adding 9 classically- or empirically-
attested cluster systems that were not included in the locked [[h-new-89-meta-cluster-network|H-NEW-89]]
pre-reg. The extension asks:

(A) Does Q 62 remain the top-degree meta-hub under the extended
    20-cluster network, or does a new hub emerge?
(B) Does the 21-isolate count ([[h-new-89-meta-cluster-network|H-NEW-89]]) persist? In particular,
    does the Q 16-25 zone retain its 8/10 isolate density?
(C) Under a new-cluster-only sub-network (the 9 additions, original
    11 DROPPED), do the same hubs emerge, or are the hubs artifacts
    of the original 11-cluster choice?

This is a SYNTHESIS finding, not a single-hypothesis test. Still
pre-registered to the project's PRE-REG-STANDARD-04 discipline.

## Locked 20-cluster system list

### C1-C11 — Original [[h-new-89-meta-cluster-network|H-NEW-89]] clusters (verbatim, NOT re-derived)

From `findings/phase-b-hypotheses/csv/h-new-89.json`:

| ID | Label | Members | Size |
|----|-------|---------|-----:|
| C1 | الم muqaṭṭāʿat | {2, 3, 29, 30, 31, 32} | 6 |
| C2 | الر muqaṭṭāʿat | {10, 11, 12, 14, 15} | 5 |
| C3 | ḥm muqaṭṭāʿat | {40, 41, 42, 43, 44, 45, 46} | 7 |
| C4 | طسم muqaṭṭāʿat | {26, 27, 28} | 3 |
| C5 | musabbiḥāt (core, [[h-new-58c-musabbihat-tense-split|H-NEW-58c]]) | {57, 59, 61, 62, 64} | 5 |
| C6 | al-sabʿ al-ṭiwāl | {2, 3, 4, 5, 6, 7, 9} | 7 |
| C7 | Friday liturgy | {18, 32, 62, 76} | 4 |
| C8 | Khawātim al-Ḥashr extended | {59, 62} | 2 |
| C9 | al-muʿawwidhatān | {113, 114} | 2 |
| C10 | al-Zahrāwān | {2, 3} | 2 |
| C11 | al-mufaṣṣal | {49..114} | 66 |

### C12-C20 — New clusters (LOCKED 2026-04-17 before any graph run)

#### C12 — Oath-opener surahs ([[h-new-85-oath-openers|H-NEW-85]] OATH_PARTICLE class) — n=21

Surahs: {36, 37, 38, 43, 44, 50, 51, 52, 53, 68, 77, 79, 85, 86,
         89, 91, 92, 93, 95, 100, 103}

Source: `findings/phase-b-hypotheses/h-new-85-oath-openers.md`
Cell 1 (PASS 21/21); [[h-new-61-opening-words|H-NEW-61]] OATH_PARTICLE class. All 21 are Meccan.
Q 91 al-Shams is the 7-oath apex on 3 structural axes.

#### C13 — qul-v1-w1 openers ([[h-new-74-qul-distribution|H-NEW-74]] Cell 3) — n=5

Surahs: {72, 109, 112, 113, 114}

Source: `findings/phase-b-hypotheses/h-new-74-qul-distribution.md`
Cell 3 PASS. The "qul-pentalogy" (classical muʿawwidhāt-pair +
Q 112 + Q 109 + Q 72 al-Jinn as the 5th structural member).

#### C14 — Refrain-density surahs ([[h-new-83-rahman-refrain-extension|H-NEW-83]] + prior §3b) — n=2

Surahs: {55, 77}

Source: `findings/phase-b-hypotheses/h-new-83-rahman-refrain-extension.md`
and MASTER-LEDGER §3b. Q 55 al-Raḥmān refrain density ≈0.40 (31
refrain verses in 78); Q 77 al-Mursalāt refrain density ≈0.20
(10 refrain verses in 50). Cluster cardinality is conservative
(threshold density ≥ 0.20); no other surah exceeds 0.15 on the
same operationalization per ledger.

#### C15 — Divine-attribute-named surahs — n=5

Surahs: {24, 35, 40, 55, 112}

Source: al-Asmāʾ al-Ḥusnā list + classical naming convention. The
5 surahs whose TITLES are divine names/attributes:
- Q 24 al-Nūr (the Light — one of the 99 names)
- Q 35 Fāṭir (the Originator — one of the 99 names)
- Q 40 Ghāfir (the Forgiver — one of the 99 names)
- Q 55 al-Raḥmān (the Merciful — one of the 99 names)
- Q 112 al-Ikhlāṣ (the Pure Unity — the surah's NAME is an
  attribute of divine oneness; also known as al-Tawḥīd)

CONSERVATIVE choice: surahs named for divine ACTS (Q 17 al-Isrāʾ
"Night-Journey", Q 97 al-Qadr "Divine Decree") are EXCLUDED — these
are named for acts/events, not for the divine person. If a later
run wants to include these, it requires an independent pre-reg.
This is locked BEFORE seeing graph numbers.

#### C16 — Prophet-named surahs — n=7

Surahs: {10, 11, 12, 14, 19, 47, 71}

Source: classical naming + [[h-new-49-surah-name-class|H-NEW-49]]/49.1. Named after:
- Q 10 Yūnus (Jonah)
- Q 11 Hūd (Hud)
- Q 12 Yūsuf (Joseph)
- Q 14 Ibrāhīm (Abraham)
- Q 19 Maryam (Mary — not a prophet in Sunni tradition but a
  named Quranic figure; classically grouped with prophet-named
  surahs per [[h-new-49-surah-name-class|H-NEW-49]] PROPHET_PERSON class)
- Q 47 Muḥammad (the Prophet)
- Q 71 Nūḥ (Noah)

The task prompt mentioned 8 "prophet-named"; I find only 7 under
the strict reading (surah title = the prophet's personal name).
Q 3 Āl ʿImrān ("Family of Imran") and Q 21 al-Anbiyāʾ ("The
Prophets") are named for FAMILIES or for the collective category,
not for an individual prophet. Locked at n=7 with honest deviation
disclosure.

#### C17 — Muqaṭṭāʿat singletons — n=7

Surahs: {13, 19, 20, 36, 38, 50, 68}

Source: muqaṭṭāʿat-opened surahs with a UNIQUE letter-subset
(not shared with any other surah):
- Q 13 المر (unique)
- Q 19 كهيعص (unique, 5-letter)
- Q 20 طه (unique)
- Q 36 يس (unique)
- Q 38 ص (unique)
- Q 50 ق (unique)
- Q 68 ن (unique)

These were EXCLUDED from [[h-new-89-meta-cluster-network|H-NEW-89]]'s C1-C4 because those clusters
locked on ≥2-surah letter-sharing. The singletons are their own
cluster system: "muqaṭṭāʿat-opened with unique letter-subset."
Q 7 al-Aʿrāf (المص) is also a singleton but is sometimes grouped
with الم — we EXCLUDE Q 7 conservatively from this cluster (its
letter-set is unique but it shares 3 letters with الم). Locked.

#### C18 — Musabbiḥāt extended (classical 7) — n=7

Surahs: {17, 57, 59, 61, 62, 64, 87}

Source: classical "7 musabbiḥāt" reading (4 imperfect + 3
perfect forms, EXTENDED beyond [[h-new-58c-musabbihat-tense-split|H-NEW-58c]]'s 5-surah inner cluster):
- Q 17 al-Isrāʾ — "subḥāna alladhī asrā" (noun form)
- Q 57 al-Ḥadīd — "sabbaḥa" (perfect)
- Q 59 al-Ḥashr — "sabbaḥa" (perfect)
- Q 61 al-Ṣaff — "sabbaḥa" (perfect)
- Q 62 al-Jumuʿah — "yusabbiḥu" (imperfect)
- Q 64 al-Taghābun — "yusabbiḥu" (imperfect)
- Q 87 al-Aʿlā — "sabbiḥ" (imperative)

Per [[h-new-103-musabbihat-4form|H-NEW-103]] pre-reg. This cluster REPLACES the inner-5 C5 with
the canonical 7 per classical tradition. We KEEP C5 as-is and
ADD C18 alongside it (nested relationship: C5 ⊂ C18). This is
a METHODOLOGICAL CHOICE logged in garden-of-forking-paths.

#### C19 — Book-reference muqaṭṭāʿat subset ([[h-new-53-muqattaat-book-reference|H-NEW-53]]) — n=24

Surahs: {2, 3, 7, 10, 11, 12, 13, 14, 15, 20, 26, 27, 28, 31, 32,
         36, 38, 40, 41, 43, 44, 45, 46, 50}

Source: `findings/phase-b-hypotheses/h-new-53-muqattaat-book-reference.md`
The 24 of 29 muqaṭṭāʿat-opened surahs that reference kitāb or
qurʾān within v1-3. Per-surah table rows marked ✓. The 5
exceptions are Q 19, 29, 30, 42, 68.

Note: this cluster has extensive overlap with C1-C4 and the
singletons in C17 — that is the POINT (it's a PARTIAL subset
of the full muqaṭṭāʿat family). The overlap is logged and
we do NOT attempt to de-duplicate in the incidence matrix.

#### C20 — Invocation / refuge surahs — n=4

Surahs: {1, 112, 113, 114}

Source: classical daily-recitation grouping:
- Q 1 al-Fātiḥa (the opening invocation; recited in every ṣalāh)
- Q 112 al-Ikhlāṣ (declaration of tawḥīd)
- Q 113 al-Falaq (first muʿawwidha)
- Q 114 al-Nās (second muʿawwidha)

Classical tradition treats these 4 together as the core
daily-protection / daily-invocation bundle. This is a FUNCTIONAL
cluster, analogous to the Friday-liturgy cluster (C7). Locked at 4.

Notable: Q 1 is isolated in [[h-new-89-meta-cluster-network|H-NEW-89]] (degree 0 under the
11-cluster scheme). This cluster tests whether adding C20
removes Q 1 from the isolate list.

### Total: 20 cluster systems

## Pre-committed analytical products (three, per Bonferroni k=3)

### Product (A) — Updated degree distribution

Using the observed 20-cluster incidence matrix, compute:
- Per-surah degree (number of clusters containing each surah)
- Degree histogram
- Ranked top-15 hub surahs
- Does Q 62 retain degree ≥ 4? Does its degree INCREASE under the
  extended scheme?
- Which surahs (if any) emerge as new hubs at degree ≥ 4?

Acceptance window: Q 62 retains degree ≥ 4 → HUB PERSISTENCE
CONFIRMED. If a new surah ties or exceeds Q 62, report honestly
(no post-hoc reframing).

### Product (B) — Updated isolate count

- Total isolates (degree 0 under the 20-cluster scheme)
- Isolates in Q 16-25 (is it still 8/10?)
- Compare to [[h-new-89-meta-cluster-network|H-NEW-89]] baseline (21 isolates)
- Report all isolates by mushaf position

Acceptance: descriptive reporting. Flag any change of ≥ 3 isolates
as a NOTABLE structural shift.

### Product (C) — New-cluster-only independence test

EXCLUDE the 11 original systems (C1-C11). Compute the 9-new-only
network (C12-C20) under the same pipeline. Test whether Q 62
remains the top-degree surah in this sub-network.

H₀: Under a new-cluster-only sub-network, Q 62's degree is not
significantly distinguishable from the maximum degree of any
random 114 surahs under the same 9 membership-permuted null.

Null test: for each of 10,000 membership-permuted draws of
C12-C20 (each cluster keeping its cardinality, members re-drawn
from {1..114}), compute the maximum degree. Two-sided p-value
on Q 62's observed degree in the new-cluster-only sub-network
against this null's mean.

Acceptance: NEW HUBS identified at permutation p < 0.0167
(Bonferroni-3-corrected).

## Bonferroni declaration

- `bonferroni_k: 3` (3 pre-committed analytical cells: A, B, C)
- `bonferroni_family: [[cross-finding-010-extended-network|cross-finding-010]]-extended-network`
- `alpha_bon: 0.0167` (= 0.05 / 3)
- PASS criterion on inferential cell (C): Q 62 or another surah
  emerges as a hub at p ≤ 0.0167
- Cells (A) and (B) are DESCRIPTIVE; no p-value gate

## MW-5 positive control

[[h-new-89-meta-cluster-network|H-NEW-89]]'s 11-cluster network is RE-COMPUTED inside this script
(using the same permuted-null pipeline). If the re-computation
does NOT recover Q 62 as the unique 4-hub (degree 4, p ≤ 0.0001
on isolate count), the null is broken → STOP and report
NULL-BROKEN.

This is the MW-5 positive control: our pipeline must recover the
[[h-new-89-meta-cluster-network|H-NEW-89]] result when given the [[h-new-89-meta-cluster-network|H-NEW-89]] input. Without this,
we cannot trust the extended-20 numbers.

## Null distribution (membership-permuted, 10K draws)

Same as [[h-new-89-meta-cluster-network|H-NEW-89]]:
- For each cluster with cardinality k, draw a random k-subset of
  {1..114} without replacement within cluster.
- Compute permuted incidence and recompute all metrics.
- Seed 20260417.

## Garden-of-forking-paths (locked BEFORE run)

1. **20 clusters** (not 15, not 25): the task prompt specified
   "at least 9 new" on top of 11; n=20 is exactly that.

2. **C18 replaces-and-extends C5**: both clusters coexist in the
   incidence matrix. C5 is the inner-5 ([[h-new-58c-musabbihat-tense-split|H-NEW-58c]] PASS); C18 is
   the classical 7. This introduces a DELIBERATE overlap at Q 57,
   59, 61, 62, 64 (which count in both). This is a methodologically
   HONEST choice — the 7-musabbiḥāt reading is classical, the 5-inner
   is data-driven. We keep both.

3. **C19 heavily overlaps C1-C4 + C17**: the book-reference subset
   mostly re-uses muqaṭṭāʿat-opened surahs. This inflates the
   degree of muqaṭṭāʿat surahs. DELIBERATE — C19 tests a
   DIFFERENT functional role (book-introduction marker) even
   within muqaṭṭāʿat. Declared before run.

4. **C20 removes Q 1 from isolate list** by construction. This
   is a KNOWN consequence of adding an invocation cluster that
   includes Q 1. The test of interest is NOT whether Q 1 moves
   but whether the EXTENDED network's overall isolate count
   drops significantly below the [[h-new-89-meta-cluster-network|H-NEW-89]] baseline.

5. **Prophet-named as n=7** (not 8): justified above. If a
   later run wants to include Q 3 or Q 21, re-pre-reg.

6. **Divine-attribute-named as n=5** (not including Q 17, Q 97):
   justified above. Conservative choice.

7. **Membership-permuted null** (same as [[h-new-89-meta-cluster-network|H-NEW-89]]) — NOT
   degree-preserving rewiring. Consistency with prior finding.

8. **No C-combination rules**: e.g., "belong to ≥ 2 muqaṭṭāʿat
   sub-clusters" is NOT a 21st cluster. We lock at exactly 20
   and do not add derived/joint clusters.

## Anti-HARK pre-commitments

- All 20-cluster incidence and all degrees reported regardless
  of whether Q 62 retains hub status.
- NEW hubs (if any) reported honestly; no re-ranking to
  re-elevate Q 62.
- The isolate list is reported in full under BOTH the 20-cluster
  and the 9-new-only schemes.
- NULL-BROKEN (if MW-5 positive control fails) = HARD STOP.
- NULL results (if cell C fails) reported with SAME PROMINENCE
  as PASS results.

## Expected outcomes (priors, disclosed before run)

- **Q 62 will likely gain ≥ 2 new cluster memberships** from C18
  (musabbiḥāt 7) and possibly C19 (book-reference muqaṭṭāʿat
  subset) or others. Predicted new degree ≈ 5-6.
- **Q 2, Q 3 will gain C19 membership** (both are book-reference
  muqaṭṭāʿat). Predicted new degree ≈ 4.
- **Q 1 will exit the isolate set** via C20. Expected isolates:
  drop from 21 to ~15-18 under the 20-cluster scheme (Q 1 exits,
  the singletons C17 remove 7 from isolate list, the oath-opener
  cluster C12 adds 21 new surah memberships many of which were
  isolates).

These PRIORS are disclosed; the actual run is still blind to
the numbers.

## Data + outputs

- Script: `scripts/cross_finding_010_extended_network.py`
- JSON: `findings/phase-b-hypotheses/csv/cross-finding-010.json`
- Findings: `findings/phase-b-hypotheses/cross-finding-010-extended-network.md`
- Journal: `journal/cross-finding-010-run-1.md`

## Status

PRE-REGISTERED 2026-04-17 BEFORE script execution.
