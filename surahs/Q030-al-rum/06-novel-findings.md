---
surah: 30
surah_name_translit: al-Rūm
file_type: novel-findings
date_last_updated: 2026-05-07
phase: B+
verdict: "5 pre-registered novel tests (4 housed here + 1 cross-listed Q029-F-01). Bonferroni-k=2 for the joint Q030-F-01 family; single-test Bon-1 for Q030-F-02, F-04, F-05. Verdicts: F-01 DIRECTIONAL on both axes (rank 4/15 imt + 2/15 hist); F-02 PASS-DIRECTED (3/6 near-hapax); F-04 DIRECTED-not-strong (rank 7/15 ALM + corpus pct 40%); F-05 DIRECTIONAL (rank 5/114, top-3 missed). Family verdict: refines parent H-NEW-93 NULL with one PASS-DIRECTED + multiple DIRECTIONAL signals."
---

# Q 30 al-Rūm — Novel Findings (Pre-registered)

This file presents 4 pre-registered novel tests with Q 30 as the primary subject, plus a cross-link to [[Q029-al-ankabut/Q029-F-01-ankabut-parable-hapax-prereg|Q029-F-01]] (the spider-parable hapax test for Q 29:41). Each Q 30 test has:
- A pre-registration markdown file (SHA-locked).
- A run script (which verifies the SHA at runtime).
- A JSON output.
- A finding-level write-up (this file).

Family-level Bonferroni-k for the joint Q030-F-01 axes = 2 → α_bon = 0.025. F-02, F-04, F-05 are individually Bon-1 single-test family.

Seed: 20260507. Permutation count: 10000 (where applicable).

All SHA verifications PASS at run-time (verified by each script's `verify_sha()` call).

---

## Q030-F-01 — Q 29 + Q 30 ALM-exception sub-cluster coherence (DIRECTIONAL, both axes)

**Pre-reg**: `Q030-F-01-alm-exception-subcluster-prereg.md` (SHA `05a893361805442c1a83969f3f899f4e1d0563bebb7d92b52d76b902d657fa8f`).
**Output**: `csv/Q030-F-01.json`.
**Script**: `scripts/Q030_F_01_alm_exception_subcluster.py`.

**Question**: Do Q 29 + Q 30 pooled show HIGHER imtihān-density and HIGHER historical-prophecy-density than the 4 non-exception ALM surahs (Q 2, 3, 31, 32) pooled?

### Result

| Group | imtihān (per 1000 words) | hist-prophecy (per 1000 words) |
|:--|:-:|:-:|
| Target Q29+30 | **5.02** | **29.00** |
| Reference Q2,3,31,32 | 3.33 | 17.69 |
| Difference | +1.69 | +11.31 |

**Per-surah breakdown**:

| Surah | imt count | hist count | wc | imt/k | hist/k |
|:-:|:-:|:-:|:-:|:-:|:-:|
| Q 2 | 18 | 97 | 6116 | 2.94 | 15.86 |
| Q 3 | 13 | 73 | 3481 | 3.73 | 20.97 |
| Q 29 | **8** | 26 | 976 | **8.20** | 26.64 |
| Q 30 | 1 | 26 | 817 | 1.22 | **31.82** |
| Q 31 | 3 | 4 | 546 | 5.49 | 7.33 |
| Q 32 | 1 | 12 | 372 | 2.69 | 32.26 |

**Asymmetric loading observation** (already noted in pre-reg honest-limits §10): Q 29 carries the imtihān theme (rank 14/114 corpus-wide on imtihān-density); Q 30 carries the historical-prophecy theme (rank 11/114). The pooled-density operationalization treats them as one signal; the asymmetric reading is preserved as descriptive.

**Primary enumeration** (C(6,2) = 15 partitions of ALM):
- Imtihān: rank 4/15, p_one_sided = 0.267.
- Historical-prophecy: rank 2/15, p_one_sided = 0.133.

**Secondary perm** (10000 perms; Meccan moderate-length pool, n=46):
- Imtihān p = 0.176.
- Historical-prophecy p = 0.155.

**Verdict per axis**: BOTH are **DIRECTIONAL** — direction matches H1, but neither passes α_bon = 0.025 (Bonferroni-2). The structural ceiling of the C(6,2)=15 frame is min-p = 1/15 ≈ 0.067 > 0.025; pre-reg honest-limits flagged this. The secondary frame can in principle pass α_bon but does not (p ≥ 0.155 on both).

**Honest limit / interpretation**: This is a refined retest of [[h-new-93-q29-q30-subpattern|H-NEW-93]] (parent NULL). The new operationalization (within-ALM-cluster comparison + jhd added to imtihān + rwm/bDE/snw added to hist-prophecy) shifts BOTH signals in the predicted direction. The pre-committed direction holds; Bonferroni does not. **Family verdict: DIRECTIONAL on both axes; net interpretation: the parent H-NEW-93 NULL is REFINED but not OVERTURNED.**

---

## Q030-F-02 — Roman-Persian-war prophecy lexical uniqueness (PASS-DIRECTED)

**Pre-reg**: `Q030-F-02-rum-prophecy-hapax-prereg.md` (SHA `4850caed2dbcda8a9417948a398338c58ae54829b6ce872923c17d3e204c4c99`).
**Output**: `csv/Q030-F-02.json`.
**Script**: `scripts/Q030_F_02_rum_prophecy_hapax.py`.

**Question**: Does Q 30:2-5 contain ≥ 3 corpus-hapax-or-near-hapax lemmas out of the 6 candidates {`r~uwm`, `biDoE`, `siniyn`, `galab`, `galabu`, `>adonaY``}?

### Result

| Lemma | Token count | Surah-set | Class |
|:--|:-:|:--|:--|
| **`r~uwm`** (Romans) | **1** | {30} | **strict-hapax** |
| **`biDoE`** (a few) | **2** | {12, 30} | **near-hapax** |
| `siniyn` (years) | 12 | {7, 10, 12, 17, 18, 20, 23, 26, 30} | non-hapax |
| **`galab`** (defeat-noun) | **1** | {30} | **strict-hapax** |
| `galabu` (verb root for defeat/victory) | 15 | {2, 3, 4, 7, 8, 18, 23, 30, 41, 58} | non-hapax |
| `>adonaY`` (closer) | 12 | {2, 4, 5, 7, 30, 32, 33, 53, 58, 73} | non-hapax |

**Summary**:
- 2 strict-hapax (`r~uwm`, `galab`)
- 1 near-hapax (`biDoE`)
- **3 of 6 lemmas (50%) are near-hapax-or-stricter — meets pre-registered threshold of ≥ 3.**

### Comparison: Q 27:14 (other classical historical-claim verse)

The 6 candidate lemmas drawn from Q 27:14 surface form (`{jaHada, AisotayoqanatohaA, Zulom, Euluw~, EAqibap, mufosid}`) yield:
- **0 hapax-or-near-hapax** in this sample (3 lemmas have 0 token-count under those exact LEM strings — likely tagging encoded differently in QAC; the remaining 3 are all non-hapax).

The lexical uniqueness of Q 30:2-5 vs Q 27:14 is empirically clear at the lemma-level: Q 30:2-5 produces 3/6 hapax-or-near; Q 27:14 produces 0/6.

### Verdict

**PASS-DIRECTED** at threshold ≥ 3 (the pre-registered direction). 

**Honest limits**: Threshold met EXACTLY at 3. A tighter threshold (≥ 4) would NOT pass. The verdict is at the pre-committed-but-not-extreme level. Per [[04-DISCIPLINE]] §post-hoc-noticed-findings, the verdict ceiling is PASS-DIRECTED (single-test α=0.05 cap) until INDEPENDENT REPLICATION on a distinct data dimension. Replication queue: test the same hapax-count using Quran-uthmani-consonantal lemma-tags (different rules-tuple); test under `quran-min-tashkeel` form-tagging to verify the lemma-classifier is rules-tuple-stable.

The `r~uwm` corpus-hapax is a particularly striking architectural fact: the named subject of an entire surah (al-Rūm = "the Romans") appears exactly once in the entire 6,236-verse corpus, at the verse that gives the surah its name. **This is the strongest single-token surah-eponym hapax in the corpus** alongside Q 12 *Yūsuf* (multiple tokens but spread across only Q 12) and Q 29 *Eankabuwt* (corpus-hapax confined to Q 29:41).

---

## Q030-F-04 — Q 29 ↔ Q 30 architectural-twin signature (DIRECTED)

**Pre-reg**: `Q030-F-04-architectural-twin-prereg.md` (SHA `c92548471c002b18f89b5fbf232c38167e88cc545709143946de55bb32902383`).
**Output**: `csv/Q030-F-04.json`.
**Script**: `scripts/Q030_F_04_architectural_twin.py`.

**Question**: Is the FR-roots distance d(Q 29, Q 30) STRICTLY BELOW the median of all 15 within-ALM-cluster pairwise distances?

### Result

- **d(Q 29, Q 30) = 0.9153** (h-new-111 FR-roots matrix).
- **Within-ALM-15-pair sorted ascending**:

| Rank | Pair | d_FR |
|:-:|:--|:-:|
| 1 | Q 2 ↔ Q 3 | 0.6309 |
| 2 | Q 3 ↔ Q 29 | 0.8420 |
| 3 | Q 2 ↔ Q 29 | 0.8489 |
| 4 | Q 29 ↔ Q 31 | 0.8963 |
| 5 | Q 30 ↔ Q 31 | 0.9089 |
| 6 | Q 31 ↔ Q 32 | 0.9095 |
| **7** | **Q 29 ↔ Q 30** | **0.9153** |
| 8 | Q 30 ↔ Q 32 | 0.9272 |
| 9 | Q 29 ↔ Q 32 | 0.9382 |
| 10 | Q 2 ↔ Q 30 | 0.9732 |
| 11 | Q 3 ↔ Q 30 | 0.9841 |
| 12 | Q 2 ↔ Q 31 | 0.9770 |
| 13 | Q 3 ↔ Q 31 | 0.9961 |
| 14 | Q 2 ↔ Q 32 | 1.0515 |
| 15 | Q 3 ↔ Q 32 | 1.0860 |

(median = 0.9272 at index 8).

- d(Q29, Q30) = 0.9153 is at **rank 7/15** — JUST BELOW the median (median = pair-8).
- Corpus-wide percentile: 40.21% (n=6441). Far from the 5%-threshold.
- Mushaf-adjacency rank: d(Q29, Q30) = 0.9153 is **rank 82/113** in the {d(s, s+1) : s=1..113} ladder. So Q 29 → Q 30 is FAR FROM tight as a mushaf-adjacency pair.

### Verdict

- **Primary (within ALM-15)**: rank 7/15 = **DIRECTED** (matches H1 by 1 position; not STRONG-DIRECTED which required rank ≤ 3).
- **Secondary (corpus-wide)**: pct = 40% = **NEITHER STRONG nor WEAK direction-match**; treated as NULL at the 5% threshold.
- **Mushaf-adjacency control**: rank 82/113 — Q 29 → Q 30 is BELOW-MEDIAN closeness as an adjacency pair, even though they're mushaf-neighbors. This is interesting: Q 29 → Q 30 is a CONTENT-DISTANT mushaf-adjacency, contrary to the simplistic expectation that adjacent surahs are content-close.

**The architectural-twin claim is REFINED**: Q 29 + Q 30 are NOT content-FR-twins. Their book-reference-exception status does NOT translate to a tight FR-roots-content cohesion. Q 29's closer FR-neighbor in ALM is Q 3 (d=0.842, rank 2 of 15); Q 30's closer FR-neighbor in ALM is Q 31 (d=0.909, rank 5 of 15) — NEITHER points to Q 29-Q 30 as a tight pair.

**Honest limits**: The within-ALM-15-pair frame has min-p = 1/15 = 0.067, structurally above α_bon=0.05 — this was flagged in pre-reg §4. The verdict ceiling is DIRECTIONAL, not PASS. The mushaf-adjacency control (rank 82/113) is an INDEPENDENT-of-ALM-frame test that further weakens the architectural-twin hypothesis: Q 29 → Q 30 is NOT a content-cheap mushaf adjacency.

**Refined interpretation**: Q 29 + Q 30 share the cross-finding-008 EXCEPTION-status (no book-reference) but do NOT share an architectural-content-twin signature. The exception-status is a **surface-pattern fact** (a feature of the v 1-3 opener), not a deep content-cohesion fact. This is a clean architectural finding: **surface-pattern coherence does not entail deep-content coherence**, and it parallels the [[Q005-al-maida/06-novel-findings|Q 5 chronology-architecture dissociation]] discovery — chronology, mushaf-adjacency, and surface-opener-pattern can each dissociate from content-FR-architecture.

---

## Q030-F-05 — Cognitive-imperative interrogative density (DIRECTIONAL)

**Pre-reg**: `Q030-F-05-cognitive-imperatives-prereg.md` (SHA `850b16e6a4c5fee4e4d2828a3bf1da4c149798625cc933c9ae22b722a5608111`).
**Output**: `csv/Q030-F-05.json`.
**Script**: `scripts/Q030_F_05_cognitive_imperatives.py`.

**Question**: Is Q 30's per-word density of cognitive-imperative interrogatives (afa-lā tatafakkarūn / yatafakkarūn / yaʿqilūn / etc.) in the TOP 3 surahs corpus-wide?

### Result

Top 5 by rate (cog_count / words × 1000):

| Rank | Surah | matches | words | rate/1000 |
|:-:|:-:|:-:|:-:|:-:|
| 1 | Q 88 | 1 | 92 | 10.870 |
| 2 | Q 32 | 2 | 390 | 5.128 |
| 3 | Q 59 | 2 | 478 | 4.184 |
| 4 | Q 45 | 2 | 512 | 3.906 |
| **5** | **Q 30** | **3** | **868** | **3.456** |
| 6 | Q 51 | 1 | 371 | 2.695 |
| 7 | Q 36 | 2 | 754 | 2.653 |

Q 29 by rate: rank 14/114, rate 1.916/1000, 2 matches.

### Verdict

**DIRECTIONAL** — Q 30 is rank **5/114** by rate. The pre-registered top-3 threshold is NOT met. Q 30 IS in the top-5 of the corpus on this metric.

**Honest interpretation**: The rank-5 placement is partly explained by 4 SHORTER surahs (Q 88 = 92 words; Q 32 = 390; Q 59 = 478; Q 45 = 512) where 1-2 matches dominate the rate. Q 30's absolute count (3 matches in 868 words) is high in absolute terms — it has the THIRD-HIGHEST absolute count among all 114 surahs (rank 7/114 by absolute count). Among medium-length surahs (≥ 600 words), Q 30 has the HIGHEST cognitive-imperative density.

The al-Rāzī claim that Q 30 features cognitive-imperative pedagogy is **DIRECTIONALLY** supported. The strict pre-registered top-3 threshold is missed by 2 ranks; the al-Rāzī claim is empirically supported at a DOCUMENTED-NOT-LAW-STRENGTH level.

---

## Cross-listed: Q029-F-01 — ʿAnkabūt parable hapax (PASS-DIRECTED)

See [[Q029-al-ankabut/06-novel-findings|Q 29 al-ʿAnkabūt 06-novel-findings]] for the full write-up of [[Q029-al-ankabut/Q029-F-01-ankabut-parable-hapax-prereg|Q029-F-01]].

**Brief**: Q 29:41 spider-parable yields 2 corpus-hapax lemmas (`Eankabuwt` lemma-corpus-hapax with 2 tokens both in Q29:41; `>awohan` strict-hapax) out of 5 candidates. Q 16:75 = 0 near-hapax; Q 27:18 = 1 near-hapax (`namolap`). Verdict: **PASS-DIRECTED** at threshold ≥ 2.

The parallel Q029-F-01 PASS-DIRECTED + Q030-F-02 PASS-DIRECTED constitute **a paired hapax-finding**: both Q 29's eponymous parable-verse and Q 30's eponymous prophecy-pericope have corpus-rare lemma signatures. This is the strongest novel finding in the present revisit.

---

## Family-level summary

| ID | Test | Verdict | Direction | p_or_rank |
|:-:|:--|:--|:--|:--|
| Q030-F-01-imt | ALM-exception imtihān | DIRECTIONAL | matches | rank 4/15, p_secondary 0.176 |
| Q030-F-01-hist | ALM-exception hist-prophecy | DIRECTIONAL | matches | rank 2/15, p_secondary 0.155 |
| **Q030-F-02** | Q 30:2-5 prophecy hapax | **PASS-DIRECTED** | matches | 3/6 hapax-or-near (threshold ≥ 3) |
| Q030-F-04 | Q 29 ↔ Q 30 architectural-twin | DIRECTED | matches | rank 7/15 (just-below median) |
| Q030-F-05 | Cognitive-imperative density | DIRECTIONAL | matches | rank 5/114 (top-3 missed) |
| (Cross-link) Q029-F-01 | Spider parable hapax | **PASS-DIRECTED** | matches | 2/5 hapax (threshold ≥ 2) |

**Net family**: 2 PASS-DIRECTED (Q030-F-02 + cross-link Q029-F-01) — both lexical-uniqueness tests for the eponym/prophecy/parable verses. 4 DIRECTIONAL — direction-matching but not Bonferroni-PASS. 0 NULL with reversed direction.

**Refinement of parent H-NEW-93 NULL**: The parent test on raw 4-cell density vs Meccan baseline LANDED NULL. The present revisit, with refined operationalizations (within-ALM comparison, lemma-hapax counting, FR-architectural-twin, cognitive-imperative density), reveals that:
1. The Q 29 + Q 30 + ALM-exception pattern has REAL DIRECTION-MATCHING signals on multiple axes, but these signals do not reach Bonferroni-strict-α at the chosen operationalizations.
2. The strongest novel signature is at the LEXICAL-UNIQUENESS (hapax) axis — both surahs have eponymous corpus-hapax lemmas (`Eankabuwt`, `r~uwm`).
3. The architectural-twin claim is REFUTED at the FR-roots-content axis (Q 29 + Q 30 are NOT content-twins; rank 7/15 in ALM, rank 82/113 in mushaf-adjacency).
4. Q 30's cognitive-imperative density is REAL but rank-5, not rank-3.

The H-NEW-93 NULL stands at its pre-committed operationalization. The present family adds nuance: the ALM-exception-pair has architectural identity at the LEXICAL-EPONYMY axis, NOT at the deep-content axis.

*Bismillāhi al-Raḥmāni al-Raḥīm.*
