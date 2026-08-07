---
surah: 25
surah_name_ar: الفرقان
surah_name_translit: al-Furqān
file_type: novel-findings
date_last_updated: 2026-05-09
phase: B+
---

# Q 25 al-Furqān — Novel findings


> **⛔ CORRECTION NOTICE — 2026-08-07.** This file locates this surah within the
> **compression-tail** and/or **iʿjāz anti-twin** framework. Both met a matched Arabic control
> on 2026-08-07 and **neither discriminates**. The anti-twin is **REVERSED** — this corpus sits
> at the **3rd percentile** of al-Jāḥiẓ and the 14th of al-Bukhārī, and pre-Islamic poetry under
> a matched partition reaches r = −0.872 against this corpus's −0.870. The compression-tail is
> **genre-shared and 91.5 % explained by unit size**: log(unit size) alone gives R² = 0.9147,
> and re-cutting this corpus's own verses to equal size collapses R² from 0.9887 to **0.3388**.
> UAS is a synthesis index with no null hypothesis.
>
> Positional statements below — "in the compression-tail", "iʿjāz-fawāṣil cell", a UAS rank —
> remain accurate as **descriptions of where this surah sits on those axes**. What is withdrawn
> is that the axes distinguish this corpus from ordinary Arabic. Nothing below is deleted.
>
> Evidence: `findings/phase-b-hypotheses/h-new-2720-genre-control-sweep.md`
> Summary: `findings/GENRE-CONTROL-CORRECTION-2026-08-07.md`.

Five pre-registered tests on Q 25, all SHA-locked seed = 20260507, 10000 permutations where applicable, Bonferroni-corrected per family. All pre-reg files in `surahs/Q025-al-furqan/Q025-F-NN-*-prereg.md`; all scripts in `surahs/Q025-al-furqan/scripts/`; all outputs in `surahs/Q025-al-furqan/csv/Q025-F-NN.json`. Independent re-verification of corpus-EXACT counts by Q 25 specialist 2026-05-09.

| ID | Hypothesis | Verdict |
|:--|:--|:--|
| Q025-F-01 | TRUE-ISOLATE persistence of Q 25 across 8 alternative similarity instruments | **NULL — instrument-fragile** |
| Q025-F-02 | Q 25:1's autonymic-titular use of *al-furqān* structurally unique among 7 corpus attestations | **DESCRIPTIVE-CONFIRMED** |
| Q025-F-03 | Q 25 / Q 67 *tabāraka alladhī* opener-pair = deep structural twin | **NULL — surface-only pair** |
| Q025-F-04 | Q 25's *qālū / qāla / yaqūl* polemic-quotative density places Q 25 in TOP quartile | **NULL** |
| Q025-F-05 | Q 25:63-77 ʿibād-al-Raḥmān block self-cohesive AND cross-block twin with Q 23:1-11 | **DIRECTIONAL** (Cell A PASS, Cell B NULL) |

Plus 1 directly pre-committed **descriptive comparison** (the longer-checklist claim, dispatched as part of Q025-F-05's Cell C):

| ID | Hypothesis | Verdict |
|:--|:--|:--|
| Q025-F-05c | Q 25:63-77 ʿibād-al-Raḥmān checklist LONGER (verse-count) than Q 23:1-11 muʾminūn checklist | **VINDICATED** (15 > 11 verses) |

---

## Q025-F-01 — True-isolate persistence of Q 25 across 8 alternative similarity instruments

**Pre-reg**: `Q025-F-01-true-isolate-persistence-prereg.md`. SHA256: `1653d24f358cc1ce37bf35443944ebdd2dfa61b199d680882a8f38a5380b0330`. Seed 20260507; n_perm 10000; Bonferroni-8; α_bon = 0.00625.

**Parent OQ**: OQ-2 (Q 16-25 cluster-empty zone) + OQ-18 (true-isolate-core mechanism).

**Parent finding**: [[h-new-126-isolate-core|H-NEW-126]] established Q 25 as a member of the 5-surah true-isolate core {Q 16, 21, 22, 23, 25} — invisible to all 20 cluster-taxonomy systems (per [[cross-finding-010-extended-network|cross-finding-010]] dedup).

**Hypothesis**: Under each of 8 alternative similarity instruments (root-Jaccard, content-cosine, char-trigram-Dice, FR-similarity from h-new-111, rhyme-cosine, root-Zipf-overlap, divine-name-Jaccard, char-5-gram-Dice), Q 25's mean similarity to its 3 nearest non-self neighbors places Q 25 in the bottom-quartile (rank ≤ 28/114) of the corpus. **Direction-locked LOW** (Q 25 is isolated).

**Success criterion**: ≥ 6/8 instruments place Q 25 in bottom-quartile AND each passes per-instrument permutation null at α_bon.
**Failure criterion**: < 4/8.

### Results (computed 2026-05-09)

| Instrument | Q 25 rank (ascending) | In bottom-quartile? | p_one_sided_lower | MW-5 (ḥawāmīm) passes? |
|:--|:-:|:-:|:-:|:-:|
| I1 — root-Jaccard | 83 | No | 0.7229 | yes (rank 63 / mean 87.4) |
| I2 — content-cosine | 76 | No | 0.6672 | yes (rank 57 / mean 79.2) |
| I3 — char-trigram-Dice | 93 | No | 0.8111 | yes |
| I4 — Fisher-Rao similarity (h-new-111) | 30 | No (just outside) | 0.2541 | yes |
| I5 — rhyme final-letter cosine | 104 | No (in TOP quartile! near-monorhyme similarity) | 0.9171 | yes |
| I6 — root Zipf-overlap | 86 | No | 0.7524 | yes |
| I7 — divine-name Jaccard | 86 | No | 0.7555 | yes |
| I8 — char-5-gram Dice | 72 | No | 0.6307 | yes |

**Aggregate**: 0/8 instruments place Q 25 in bottom-quartile. 0/8 pass per-instrument α_bon. MW-5 fires on 7/8 instruments (ḥawāmīm cluster correctly NOT bottom-quartile).

### Verdict: **NULL — Q 25's TRUE-ISOLATE status is INSTRUMENT-SPECIFIC**

This is a substantive empirical refinement of [[h-new-126-isolate-core|H-NEW-126]]:

- H-NEW-126 reported Q 25 as one of 5 surahs invisible to **all 20 cluster-taxonomy systems**. That finding stands.
- Q025-F-01 shows Q 25 is NOT a global similarity-isolate under any of 8 alternative instrument-families. Q 25's mean-top-3-similarity ranks in the upper-middle to upper-top quartile (ranks 30-104 across the 8 instruments).

**Interpretation**: the "true-isolate" verdict from H-NEW-126 is a property of the **clustering procedure** (the 20 cluster-systems all use thresholding + clustering algorithms), not a property of Q 25's overall similarity to other surahs. The graded-similarity profile of Q 25 to the rest of the corpus is unexceptional; what is exceptional is that Q 25 doesn't survive any cluster-membership threshold.

This is consistent with the [[h-new-281-true-isolate-core-within-zone-jaccard|H-NEW-281]] / [[h-new-285-oq18-within-zone-contrast|H-NEW-285]] / [[h-new-286-oq18-within-zone-name-class-contrast|H-NEW-286]] within-zone findings: the 5-isolate-core IS the strongest local-cohesion nucleus within Q 16-25 (i.e., at the local scale they ARE somewhat cohesive together, just not at the global cluster-membership scale).

**Output JSON**: [`csv/Q025-F-01.json`](csv/Q025-F-01.json).
**Pre-reg + script + JSON**: see file listing above.

### MW-1..MW-7 check

- MW-1 (instrument-prior): ✓ 8 instruments specified pre-reg.
- MW-2 (corpus-prior): ✓ 10000-permutation null.
- MW-3 (alternative-models): ✓ 8 mathematically distinct instruments.
- MW-5 (positive-control): ✓ 7/8 ḥawāmīm controls fired correctly.
- MW-7 (post-hoc cap): ✓ thresholds pre-registered.

---

## Q025-F-02 — Q 25:1's autonymic-titular use of *al-furqān* is structurally unique among 7 corpus attestations

**Pre-reg**: `Q025-F-02-furqan-vocabulary-specificity-prereg.md`. SHA256: `ed2f43c714440ac471979230121ef0ba27ff51f807b1ab0d915b8ed8ed2f4a97`. k = 3 cells. α_bon = 0.01666 (descriptive-binary cells).

**Hypothesis**: Q 25:1 is the unique attestation of the 7 corpus *al-furqān/furqān* occurrences where the noun functions as the autonymic title of the very revelation being announced — with (i) verse-1 position, (ii) *nazzala* form-II verbal frame, and (iii) *ʿabdihi* + *al-ʿālamīn* co-occurrence.

The 7 corpus attestations (verified): Q 2:53, Q 2:185, Q 3:4, Q 8:29, Q 8:41, Q 21:48, Q 25:1.

### Results (computed 2026-05-09)

| Locus | v.1? | Verb frame | *ʿabdihi*? | *al-ʿālamīn*? | Cell-C match? |
|:--|:-:|:--|:-:|:-:|:-:|
| Q 2:53 | No | *ātaynā* (form IV) | No | No | No |
| Q 2:185 | No | *anzala* (form IV) | No | No | No |
| Q 3:4 | No | *anzala* (form IV) | No | No | No |
| Q 8:29 | No | *yajʿalu* (form I) | No | No | No |
| Q 8:41 | No | *anzalnā* (form IV) | No | No | No |
| Q 21:48 | No | *ātaynā* (form IV) | No | No | No |
| **Q 25:1** | **YES** | ***nazzala*** (form II) | **YES** | **YES** | **YES** |

| Cell | Q 25:1 unique? |
|:--|:-:|
| A (v.1 position uniqueness) | **YES** (1/7) |
| B (*nazzala* form-II verbal frame) | **YES** (1/7) |
| C (*ʿabdihi* + *al-ʿālamīn* co-occurrence) | **YES** (1/7) |

**3/3 cells verify.**

### Verdict: **DESCRIPTIVE-CONFIRMED — Q 25:1's autonymic-titular use of *al-furqān* is structurally unique among the 7 corpus attestations**

This empirically vindicates the classical multi-mufassir consensus reading (al-Ṭabarī, al-Zamakhsharī, al-Rāzī, al-Qurṭubī, Ibn Kathīr, al-Biqāʿī, al-Suyūṭī) that Q 25:1's *al-furqān* uniquely autonymizes the very surah/revelation it announces. The empirical signature is multi-dimensional: position-uniqueness + verb-form-uniqueness + co-occurrence-uniqueness.

**Output JSON**: [`csv/Q025-F-02.json`](csv/Q025-F-02.json).

---

## Q025-F-03 — Q 25 / Q 67 *tabāraka alladhī* opener-pair — structural-twin test (NULL — surface-only pair)

**Pre-reg**: `Q025-F-03-tabaraka-pair-prereg.md`. SHA256: `0c0f1095a911f5b206d3009f949389ddeba80e722cc3e9fe297e75f7c80a5b40`. k = 4 instruments. α_bon = 0.0125.

**Hypothesis**: The 2 surah-openers of the corpus with *tabāraka alladhī* (Q 25:1 and Q 67:1) form a structural pair on at least 3 of 4 corpus-wide similarity instruments — i.e., the pair scores in the top-decile vs random non-tabāraka pairs.

### Corpus-EXACT verification

Verified 2026-05-09 from `quran-text/quran-no-tashkeel.json`: exactly 5 attestations of `تبارك الذي` corpus-wide:

| # | Locus | Position | Verbal frame |
|:-:|:--|:--|:--|
| 1 | Q 25:1 | **surah-opener** | *nazzala* (form II) |
| 2 | Q 25:10 | mid-surah | *jaʿala* (form I) + conditional |
| 3 | Q 25:61 | mid-surah | *jaʿala* (form I) + cosmological |
| 4 | Q 43:85 | mid-surah | predicate (genitive) + *wa-* coordinator |
| 5 | Q 67:1 | **surah-opener** | predicate *bi-yadihi* (genitive) |

Q 25 owns 3 of 5 (60%). The two surah-openers are Q 25:1 and Q 67:1. **Pre-reg corpus-EXACT count VERIFIED.**

### 4-instrument structural-twin test

| Instrument | Target (Q 25, Q 67) score | Target percentile | In top-decile? | Pass α_bon? | Control (Q 1, Q 6) in top-decile? |
|:--|:-:|:-:|:-:|:-:|:-:|
| I1 — Fisher-Rao similarity (h-new-111) | 0.5395 | 29.05% | No | No | No (control: 91.4% — fail) |
| I2 — top-rhyme-letter identity | 0 | 51.33% | No | No | YES (control: 0.06% — pass) |
| I3 — opening-word identity (positive-control by construction) | 1 | 0.78% | YES | No | YES (control: 2.39% — pass) |
| I4 — sig_A iʿjāz similarity | 0.6548 | 70.66% | No | No | No (control: 88.68% — fail) |

**Aggregate**: 1/4 instruments place (Q 25, Q 67) in the top-decile (only I3 — opening-word identity by construction). 0/3 inferential instruments. MW-6 control (Q 1, Q 6 *al-ḥamd lillāhi* opener-pair) passes on 2/4 instruments.

### Verdict: **NULL — *tabāraka alladhī* opener is SURFACE-FORMAL pair only**

Q 25 and Q 67 share the formal-opener-construction but do NOT share:
- Content-fingerprint (Fisher-Rao similarity at 29th percentile = below median);
- Rhyme structure (Q 25 alif-monorhyme @ 98.7%; Q 67 rāʾ-dominant @ 70%);
- iʿjāz signature (different sig_A values).

This independently corroborates the [[Q067-al-mulk/06-novel-findings|Q067-F-06]] near-miss verdict (high-faḍāʾil prominence of Q 67 ≠ elevated structural-iʿjāz). The two surahs sit on opposite sides of the recitation-virtue-vs-architectural-significance dimension: Q 25 has high UAS + low recitation-virtue-prominence; Q 67 has modest UAS + high recitation-virtue-prominence.

**Project-level implication**: shared formal-opener construction (single lexical-token marker) is INSUFFICIENT to drive deep structural cohesion. This is consistent with cross-finding-025 marker-thickness rule: thin markers (a single 2-word formal-opener) need multi-axis correlation to drive FR-cohesion; absent multi-axis correlation, the pair NULLs out on root-distribution-FR.

**Output JSON**: [`csv/Q025-F-03.json`](csv/Q025-F-03.json).

---

## Q025-F-04 — Q 25's *qālū / qāla / yaqūl* polemic-quotative density (NULL — Q 25 NOT in TOP quartile)

**Pre-reg**: `Q025-F-04-qalu-polemic-density-prereg.md`. SHA256: `61ce8ac21bc80d8e7c2bf979687c3a82c6fa67e0339525e397ae2c8f7165d3cc`. k = 2 cells. α_bon = 0.025.

**Hypothesis**: Q 25's per-100-verses density of inflected *qwl*-root narrating-disbelievers verbs places Q 25 in the TOP quartile (rank ≤ 28/114).

### Results

| Cell | Description | Q 25 density | Q 25 rank | TOP-quartile? | p_one_sided_upper | Pass α_bon? |
|:--|:--|:-:|:-:|:-:|:-:|:-:|
| A — polemic-attributed *qālū* / regex `(و)?قالوا|قال (الذين كفروا...)` | 8 attestations / 77 v = 10.39 per 100v | 7th rank descending | **YES** | 0.0627 | No (α_bon = 0.025) |
| A2 — broad *qwl* (any subject, regex `قال`/`يقول`) | 10 attestations / 77 v = 12.99 per 100v | 44th rank descending | **NO** | 0.3834 | No |

MW-5 control: Q 12 Yūsuf rank 1 on Cell A2 (the narrative-rich gold-standard). VERIFIED.

### Verdict: **NULL** (Cell A near-pass at p=0.063 marginal but not significant after Bonferroni; Cell A2 NULL at rank 44)

**Honest interpretation**: Q 25's polemic-quotative DOES place it in the top-decile by raw rank on the targeted Cell-A metric (rank 7 / 114), but the permutation null gives p = 0.0627 — just above α_bon = 0.025. The broader Cell-A2 (corpus-prior-blind) shows Q 25 at rank 44/114 — mid-pack.

Q 25 is **rhetorically heavily polemic** but **NOT statistically distinguished** as a top-quartile polemic-density surah. The polemic register is REAL (Cell-A targeted regex finds 8 attestations), but it does NOT statistically dominate the corpus's polemic-density distribution. Q 25's polemic is more **structurally embedded** (positioned at block-boundary pivots) than **statistically dominant** (in raw density).

**Output JSON**: [`csv/Q025-F-04.json`](csv/Q025-F-04.json).

---

## Q025-F-05 — Q 25:63-77 *ʿibād al-Raḥmān* block self-similarity AND cross-block twin with Q 23:1-11

**Pre-reg**: `Q025-F-05-ibad-rahman-portrait-prereg.md`. SHA256: `8593ef9ff8aa3ec463dcbdcba1a6d686fe39b6720b1d375a2de84a797061fe8e`. k = 3 cells. α_bon = 0.01666.

**Hypothesis** (3 cells, all pre-committed direction HIGHER):
- A — Q 25:63-77 intra-block self-similarity HIGHER vs Q-25-internal random null.
- B — Q 25:63-77 ↔ Q 23:1-11 cross-block similarity HIGHER vs random cross-surah equal-length-block null.
- C — both blocks have dense *alladhīna* relative-clause cascades (descriptive).

### Results

| Cell | Result | p_one_sided_upper | Pass α_bon = 0.01666? |
|:--|:--|:-:|:-:|
| A — Q 25:63-77 intra-block self-sim | obs mean cosine = 0.0213; null mean = 0.0121 | **0.0069** | **YES — PASS** |
| B — (Q 25:63-77, Q 23:1-11) cross-block sim | obs mean cosine = 0.0083; null mean = 0.0087 | **0.4661** | **NO — NULL** |
| C — *alladhīna* marker count | Q 25:63-77 = 8; Q 23:1-11 = 7 (15-verse block 8 markers vs 11-verse block 7 markers; density 0.53 vs 0.64) | n/a | descriptive **VERIFY** |

MW-5 control: Q 23:1-11 intra-block self-similarity p_one_sided_upper = 0.0000 (PASS — Q 23 portrait is internally tighter than Q 23-internal null). MW-6 control: (Q 25:63-77, Q 70:22-35) cross-block similarity = 0.0512 (moderate descriptive only).

### Verdict: **DIRECTIONAL — Cell A PASS, Cell B NULL, Cell C verifies descriptively**

**Honest interpretation**: The *ʿibād al-Raḥmān* catalog IS self-cohesive within Q 25 (al-Ṭabarī's "unified portrait" reading VINDICATED at p = 0.0069). However, the structural-twin claim with Q 23:1-11 is NOT vocabulary-cohesive on TF-IDF.

This suggests a project-novel structural typology: **the *alladhīna*-cascade-portrait genre is FORM-stable across Q 23:1-11, Q 25:63-77, Q 70:22-35 — but each block uses surah-specific vocabulary**. The form-vocabulary asymmetry is exactly the type of pattern the project's cross-finding-025 marker-thickness rule predicts: a single thematic marker + single grammatical structure is NECESSARY for portrait-genre recognition but INSUFFICIENT for cross-block vocabulary cohesion.

### Q025-F-05c (Cell C extended — pre-committed direction)

**Pre-committed claim** (from team-lead dispatch, before observation): Q 25:63-77 ʿibād-al-Raḥmān checklist is LONGER (verse-count) than Q 23:1-11 muʾminūn-checklist.

| Block | Verse range | Verse-count |
|:--|:--|:-:|
| Q 25 ʿibād al-Raḥmān | 63–77 | **15** |
| Q 23 muʾminūn | 1–11 | **11** |
| Q 70 muṣallīn | 22–35 | 14 |

**VINDICATED**: Q 25's checklist (15 verses) > Q 23's checklist (11 verses), as pre-committed. Q 70's (14 verses) is intermediate.

**Output JSON**: [`csv/Q025-F-05.json`](csv/Q025-F-05.json).

---

## Overall Q 25 finding-family summary

| ID | Pre-reg SHA prefix | Verdict | Strength |
|:--|:--|:--|:--|
| Q025-F-01 | 1653d24f | NULL — instrument-fragile isolate | substantive — refines H-NEW-126 |
| Q025-F-02 | ed2f43c7 | DESCRIPTIVE-CONFIRMED | corpus-EXACT 3/3 cells |
| Q025-F-03 | 0c0f1095 | NULL — surface-only opener pair | substantive — corroborates Q067-F-06 |
| Q025-F-04 | 61ce8ac2 | NULL (marginal Cell A near-pass) | descriptive — Q 25 polemic structurally embedded |
| Q025-F-05 | 8593ef9f | DIRECTIONAL — Cell A PASS, Cell B NULL, Cell C VERIFY | substantive — ʿibād-genre is form-stable, vocabulary-asymmetric |
| Q025-F-05c | (Cell C extension) | VINDICATED (15 > 11 verses) | descriptive — pre-committed length comparison |

**Headline novel-finding (project-level): Q 25 is the iconic *tabāraka-opener + autonymic-title* surah, but its TRUE-ISOLATE status (H-NEW-126) is INSTRUMENT-FRAGILE.** The 5-axis architectural profile (UAS rank 13, low sig_A/B, expensive Q24→Q25 seam, near-monorhyme, isolate-core member) makes Q 25 a project-novel INVERTED-IʿJĀZ exemplar. The 3-axis structural-pair test with Q 67 NULLs out: the *tabāraka alladhī* opener is formal-only, not deep-structural.

**3 NULL verdicts published with full prominence** (Q025-F-01, Q025-F-03, Q025-F-04) per project protocol. NULL findings carry full publication weight; they refine prior findings and reduce overconfidence.

**2 DESCRIPTIVE-VINDICATED + 1 DIRECTIONAL-PARTIAL** (Q025-F-02, Q025-F-05c; Q025-F-05 Cell A) — corpus-EXACT and pre-committed comparisons that strengthen the classical multi-mufassir reading of Q 25:1's autonymic title and the ʿibād-al-Raḥmān catalog's self-cohesion.
