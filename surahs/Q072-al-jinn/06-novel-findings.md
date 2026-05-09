---
surah: 72
surah_name_ar: الجن
surah_name_translit: al-Jinn
file_type: novel-findings
date_last_updated: 2026-05-09
phase: B+
verdict: "3 pre-registered novel findings, Bonferroni-k=3, α_bon=0.0167, seed=20260509. Verdicts: Q072-F-01 PASS-STRONG (5-qul cluster FR-cohesion REPLICATED p=0.0026 with MW-5 PC pass); Q072-F-02 PASS (Q 72 corpus-rank-1 in strict LEM:jin~ density at 10.24/1k); Q072-F-03 PASS (Q72:1-19 ↔ Q46:29-32 Jaccard=0.085 vs length-matched null p=0.0068 z=+2.81). All 3 SHA-locked."
---

# Q 72 al-Jinn — Novel Findings (Pre-registered)

This file presents the 3 pre-registered novel tests for Q 72. Each test has a SHA-locked pre-registration markdown file, a run script, a JSON output, and a write-up below.

Family-level Bonferroni-k = 3; α_bon = 0.05 / 3 ≈ 0.01667. Seed: 20260509. Permutation count: 10,000 (where applicable).

All three pre-reg SHAs are verified by the embedded script-level SHA check. SHA verifications PASS for all 3 pre-regs.

---

## Q072-F-01 — 5-qul opener cluster {Q 72, 109, 112, 113, 114} FR-cohesion REPLICATION

**Pre-reg**: `preregs/Q072-F-01-five-qul-cluster-fr-cohesion-prereg.md` (SHA `b4faaeeea844cf372b8e101fa2d53994b11c8db25e789728c36bd7a719b4f540`).
**Script**: `scripts/Q072_F_01_five_qul_replication.py`.
**Output**: `csv/Q072-F-01.json`.

### Question

Does the 5-qul opener cluster {Q 72 al-Jinn, Q 109 al-Kāfirūn, Q 112 al-Ikhlāṣ, Q 113 al-Falaq, Q 114 al-Nās} REPLICATE the H-NEW-74 / MASTER-LEDGER §10.18 finding that within-cluster mean FR is significantly below random-5-subset null at p < 0.01? Today's test uses a NEW seed (20260509) and adds an MW-5 positive control with the H-NEW-1190 sub-sample {Q 69, Q 97, Q 101} per the SESSION-HANDOFF-2026-05-09-PM §1.b lesson.

### Theoretical rationale

The 4-qul classical sub-cluster {Q 109, 112, 113, 114} = al-muʿawwidhāt-extended is a well-established short-Meccan creedal-protective grouping. al-Suyūṭī's *Itqān* lists *qul*-opening as one of 10 classical *fawātiḥ* categories. The 5-qul cluster extends this classical 4-tail to include Q 72 (the only OTHER v.1-w.1 *qul*-opener in the corpus). The empirical question is whether Q 72 — a 28-verse middle-Meccan reported-speech surah, an order of magnitude longer than the 4-tail short-creedal surahs — participates in the FR-content cohesion of this opener-family beyond the syntactic shared opener.

### Result

| Quantity | Value |
|:--|:--:|
| Cluster {72, 109, 112, 113, 114} within-mean FR | **0.4983** |
| 10,000-perm random-5-subset null mean | 0.9236 |
| Null sd | 0.1009 |
| Null min / max | (extreme tails) |
| z-score | **−4.217** |
| p (one-sided ≤) | **0.0026** |
| Bonferroni-α (k=3 family) | 0.0167 |
| Pass Bonferroni? | **YES** |
| MW-5 PC: H-NEW-1190 sub-sample {69, 97, 101} within-mean | 0.6078 |
| MW-5 PC random-3 null mean | 0.9255 |
| MW-5 PC p | **0.0362** ✓ PASS at α=0.05 |

#### Pairwise distances within cluster

| Pair | d_FR |
|:--|:--:|
| Q 72 – Q 109 | 0.7976 |
| Q 72 – Q 112 | 0.6945 |
| Q 72 – Q 113 | 0.7509 |
| Q 72 – Q 114 | 0.7433 |
| Q 109 – Q 112 | 0.3611 |
| Q 109 – Q 113 | 0.3663 |
| Q 109 – Q 114 | 0.4000 |
| Q 112 – Q 113 | 0.2886 |
| Q 112 – Q 114 | 0.3086 |
| Q 113 – Q 114 | 0.2718 |

Q 72's mean distance to the 4-tail {109, 112, 113, 114} is **0.7466** — substantially looser than the 4-tail's internal mean (0.333) but still tighter than corpus mean (0.92).

### Verdict

**PASS-STRONG** (replicated prior at predicted bound p<0.01; MW-5 PC also passes).

### Significance

This REPLICATES the prior inline finding (MASTER-LEDGER §10.18, p=0.00233 at seed 20260508 with 100,000 perms). Today's independent seed 20260509 with 10,000 perms yields p=0.0026 — consistent with the prior to within sampling noise. The MW-5 PC pass at p=0.036 confirms that the H-NEW-111 instrument carries genuine root-distribution cohesion for FR-cohesive clusters; the test is not artifactually permissive.

**Structural interpretation**: The 5-qul cluster is empirically FR-cohesive on root-distribution, dominated by the muʿawwidhāt-extended 4-tail. Q 72 is a partial-member: it shares the *qul*-opener syntactic feature and sits at FR-rank-1 to the cluster centroid Q 112, but Q 72 is content-broader (jinn-confession + prophet-cycle vs the 4-tail's pure short-creedal-protective). The cluster cohesion at α=0.01 survives this asymmetry, supporting the al-Suyūṭī classical extension of the *fawātiḥ* category.

### Cross-references

- `findings/phase-b-hypotheses/h-new-265-qul-openers-microcluster.md` — opener-stripped residual NULL (the cluster cohesion IS opener-driven; residual roots do not show 5-way family beyond the trivial shared *qul*)
- `MASTER-FINDINGS-LEDGER.md` §10.18 — the prior inline finding being replicated
- `cross-finding-008` — multi-axis classical-fawātiḥ cluster pattern
- `cross-finding-028` — al-muʿawwidhāt-extended liturgical-pair pattern (Q 72 partial-member)

### Honest limit

The PC for H-NEW-1190 sub-sample passes at p=0.036 (above α=0.01 but below α=0.05). The PC is not Bonferroni-tight but passes the family-α=0.05 PC criterion specified in the pre-reg. The cluster cohesion p=0.0026 is robust independently of PC strength. Per cross-finding-025 marker-thickness rule: the 5-qul cluster's marker (the *qul* opener) is a SURFACE 1-verse feature, marker-thickness ~3-7% per surah — yet cohesion holds. This is consistent with the "single-thematic-marker is sufficient when length-class is also shared" sub-rule (4 of 5 cluster members are short-mufaṣṣal-tail; Q 72 is the length-outlier).

---

## Q072-F-02 — Q 72 is corpus-rank-1 in jinn-being lemma density (strict LEM:jin~)

**Pre-reg**: `preregs/Q072-F-02-jinn-density-rank-prereg.md` (SHA `0129c9a395bc084e4b6df785af3f97c3f0abd5054e8288ab1dc6357e72864e69`).
**Script**: `scripts/Q072_F_02_jinn_density_rank.py`.
**Output**: `csv/Q072-F-02.json`.

### Question

Does Q 72 al-Jinn have the highest density of the jinn-being lemma per 1000 tokens of any surah in the corpus, under the STRICT LEM:jin~ lens (excluding the homophone lemmas jin~ap=garden, jaA^n~=alt-form, junnap=shield, majonuwn=mad)?

### Theoretical rationale

The QAC v0.4 morphological annotation lists 8 distinct lemmas under root `jnn`. The semantically primary jinn-being lemma is **LEM:jin~** (22 tokens corpus-wide). If the al-Biqāʿī surah-naming convention is content-faithful, the surah named *al-Jinn* should rank #1 in this lemma's density.

### Counting protocol

For each surah s ∈ {1, ..., 114}: count QAC tokens with `LEM:jin~` AND `ROOT:jnn`; divide by surah word-count (no-tashkeel); rank descending.

### Result

| Quantity | Value |
|:--|:--:|
| Q 72 LEM:jin~ token count | **3** |
| Q 72 word count (no-tashkeel) | 293 |
| Q 72 density per 1k | **10.239** |
| Q 72 rank | **1 / 114** ← **PASS** |
| Q 34 (rank 2) density | 3.19 / 1k |
| Q 46 (rank 3) density | 2.96 / 1k |
| Margin: Q 72 / Q 34 | **3.21×** |

#### Top-5 strict-lens surahs

| Rank | Surah | jin~ count | Word count | Density (per 1k) |
|:-:|:-:|:-:|:-:|:-:|
| 1 | Q 72 al-Jinn | 3 | 293 | **10.24** |
| 2 | Q 34 Sabā | 3 | 940 | 3.19 |
| 3 | Q 46 al-Aḥqāf | 2 | 676 | 2.96 |
| 4 | Q 55 al-Raḥmān | 1 | 355 | 2.82 |
| 5 | Q 51 al-Dhāriyāt | 1 | 371 | 2.70 |

#### Sensitivity (expanded lens jin~ + jaA^n~)

Under the EXPANDED lens (combining jin~ + jaA^n~ both = jinn-beings):
- Q 55 al-Raḥmān: 14.08 / 1k (rank 1 — driven by *al-jaAn~* refrain in Q 55:15, 39, etc.)
- Q 72 al-Jinn: 10.24 / 1k (rank 2)
- This is the pre-committed secondary observation: Q 72 secondary rank ≥ 2 (PASS, predicted).

### Verdict

**PASS (corpus-rank-1 in strict LEM:jin~ density; 3.2× margin over rank-2)**

### Significance

The al-Biqāʿī double-naming convention (al-Jinn / qul ūḥiya) is empirically VINDICATED at the corpus-extreme: Q 72 is THE surah of *al-jinn* in the strict lemma sense. The 3.2× margin over the rank-2 surah (Q 34 Sabā) is robust — even though Q 72 has only 3 jin~ tokens in absolute count (vs Q 34 also at 3), Q 72's short length (293 words vs Q 34's 940 words) concentrates the density extreme.

The sensitivity observation under the expanded lens is itself informative: there are TWO corpus-jinn-density-leading surahs depending on which jinn-being lemma is weighted: **Q 72 for the strict *jin~* lemma (the standard "the jinn" form) and Q 55 for the rarer *jaA^n~* lemma (the smokeless-flame poetic form, characteristic of the al-Raḥmān refrains)**. This empirically anchors the classical hadith observation that Q 55 was the surah RECITED to the jinn on the *laylat al-jinn* (Tirmidhī 3375 from Jābir) — Q 55's *al-jaAn~* density makes it the jinn-addressed surah, while Q 72's *jin~* density makes it the jinn-named surah.

### Cross-references

- `02-content-analysis.md` §3 — diagnostic lexicon
- `05-classical-claims-audit.md` §3 — al-Biqāʿī naming-convention audit
- `04-hadith-corpus.md` §3 — Tirmidhī 3375 (Q 55 recited to the jinn)
- `07-cross-references.md` §3 — Q 55 ↔ Q 72 cross-surah pair

### Honest limit

The strict LEM:jin~ versus expanded lens (jin~ + jaA^n~) is a pre-committed classification choice. The strict-lens primary test PASSES at rank 1; the expanded-lens secondary verdict is rank 2 — these are NOT inconsistent, they are complementary. The strict-lens rank-1 result is corpus-EXACT (deterministic; no permutation needed). The test is therefore inferentially weak (no null distribution) but verifies the surah-name → primary-lemma alignment as a corpus-EXACT empirical observation.

---

## Q072-F-03 — Q 72:1-19 ↔ Q 46:29-32 jinn-pericope-pair lexical-coupling

**Pre-reg**: `preregs/Q072-F-03-jinn-pericope-pair-prereg.md` (SHA `ff4ec27cb7e802f4a090ba3e419466a1d6594d7598a21b1d38ca009cd944f4bc`).
**Script**: `scripts/Q072_F_03_jinn_pericope_pair.py`.
**Output**: `csv/Q072-F-03.json`.

### Question

Do the two surviving Quranic pericopes that explicitly narrate the jinn-listening-to-recitation event — **Q 72:1-19 (the jinn-confession block) and Q 46:29-32 (the al-Aḥqāf jinn-pericope)** — share more lexical content (orthographic-token Jaccard) than a length-matched random pair drawn from the corpus?

### Theoretical rationale

Classical tafsir (al-Biqāʿī §Q72 op., citing Abū Ḥayyān; al-Rāzī ad Q 46:29 and Q 72:1) DIVIDES on whether the two pericopes refer to the SAME event or two distinct events. Empirical lexical-coupling above length-matched null SUPPORTS (but does not prove) the same-event reading.

### Result

| Quantity | Value |
|:--|:--:|
| Q 72:1-19 token-count | 193 words, 130 unique types |
| Q 46:29-32 token-count | 73 words, 60 unique types |
| Observed Jaccard | **0.0851** |
| Intersection size | **16 tokens** |
| Null mean Jaccard (length-matched, n=10,000) | 0.0469 |
| Null sd | 0.0136 |
| Null max | 0.130 (one extreme draw) |
| z-score | **+2.808** |
| p (one-sided ≥) | **0.0068** |
| Bonferroni-α (k=3) | 0.0167 |
| Pass Bonferroni? | **YES** |
| Number of candidate windows in null pool | 19,023 |

#### Intersection contents

Diagnostic jinn-event tokens present in BOTH pericopes:
- **الجن** (al-jinn)
- **سمعنا** (samiʿnā — "we heard")
- **يهدي** (yahdī — "guides")

Diagnostic tokens in Q 72 only (not Q 46:29-32): *nafar* (Q 72:1 *nafarun*; Q 46:29 uses *nafaran* — morphologically different surface form, did not match on whitespace-token), *قرآنا* (qurʾān-an), *آمنا* (āmannā).

Diagnostic tokens in Q 46:29-32 only: *قومهم* (their people), *منذرين* (warners), *موسى* (Mūsā — reference to "scripture-after-Mūsā").

Other intersecting tokens: function words (في، إلى، من، ما، له، إنا، به، لا، ومن) and content words (الأرض، الله، لما).

### Verdict

**PASS** (one-sided p = 0.0068 ≤ α_bon = 0.0167, direction correct).

### Significance

The two surviving Quranic jinn-pericopes share lexical content at p < 0.01 above length-matched corpus null. The shared diagnostic content includes *al-jinn*, *samiʿnā*, *yahdī* — the central narrative-actor (jinn), action (hearing), and reception (guidance). This empirically supports either (a) the same-event reading (Abū Ḥayyān's *mashhūr* view: Q 46:29 and Q 72:1 narrate the SAME jinn-listening event from different points of view — Q 72 from the jinn's reported-speech, Q 46 from the divine third-person frame), or (b) the shared-formula reading (two distinct events composed with the same formulaic jinn-event lexicon — a Quranic-lexical-coherence pattern at the pericope-thematic level).

The test is NECESSARY-NOT-SUFFICIENT for the same-event identity: a NULL result would have refuted the same-event reading; a PASS supports it without proving it. The cleaner discriminator (same-event vs same-formula) would require lexical-style or sentence-structure tests at a finer grain, which are out of scope here.

**This is a novel empirical contribution**: prior corpus-wide tests have not (to the project's knowledge) measured the lexical-coupling of these two specific pericopes against a length-matched null. The PASS at p=0.0068 puts this on the empirical record as a corpus-anchored support for the classical Abū Ḥayyān reading.

### Cross-references

- `03-tafsir-survey.md` §1.3 — al-Biqāʿī citing Abū Ḥayyān
- `04-hadith-corpus.md` §4.1 — Aḥmad #1356 (ʿIkrima reciting Q 46:29 in Q 72 context)
- `findings/cross-finding/cross-finding-015-classical-scholarship-validation-pattern.md` — joins the al-Biqāʿī partial-vindication pattern
- Q 46 al-Aḥqāf future-specialist work: this finding should be cross-referenced when Q 46's full template is built

### Honest limit

Jaccard-on-orthographic-tokens is a coarse instrument; the length-matched null controls for length but NOT for genre (both pericopes are reported-speech-from-the-jinn). A more discriminating test would use lemma-level matching (which would collapse *nafar*/*nafaran* morphological variants) or character-n-gram NCD. Both are queued as Q072-F-03.1 follow-on tests.

The PASS at p=0.0068 SUPPORTS the same-event-or-shared-formula reading but does NOT distinguish between them. It also does NOT rule out the alternative explanation that ALL jinn-thematic-passages in the Quran share a formulaic lexicon irrespective of event-identity (e.g., the broader jinn-encounters at Q 15:27, Q 27:39, Q 34:14, Q 55:15 may show similar inter-coupling — out of scope for this test).

---

## Family-level summary

**3 pre-registered tests**:

| Test | Verdict | Direction | p / rank | Bonferroni-survives (k=3) |
|:--|:--|:--|:--|:--|
| Q072-F-01 | **PASS-STRONG** | predicted positive | p = 0.0026 | YES |
| Q072-F-02 | **PASS** | predicted positive | rank = 1 / 114 | n/a (deterministic) |
| Q072-F-03 | **PASS** | predicted positive | p = 0.0068, z=+2.81 | YES |

**Family verdict**: 3 / 3 PASS; all three directions match pre-commit; F-01 + F-03 survive Bonferroni-k=3 (α_bon = 0.0167). F-02 is a deterministic rank-test (no null distribution).

### The Q 72 specialist's contributions

1. **Q072-F-01 REPLICATION** of H-NEW-74 / §10.18 with independent seed + MW-5 PC pass: the al-Suyūṭī 5-qul-opener classical category is now CONFIRMED with two independent replications (seed 20260508 and seed 20260509).
2. **Q072-F-02 corpus-rank-1 anchor**: the surah-name → primary-lemma faithfulness is VINDICATED at corpus-EXACT for the *al-Jinn* surah-name (3.2× margin over rank-2).
3. **Q072-F-03 jinn-pericope-pair coupling**: the al-Biqāʿī / Abū Ḥayyān same-event reading is empirically SUPPORTED at p=0.0068 — the first corpus-anchored test of this specific classical claim.

All 3 findings are SHA-locked, replicable (seed 20260509), and align with the project's broader cross-finding-015 classical-scholarship-validation-pattern.

---

## Cross-references

- `00-overview.md` §8 — headline summary
- `01-empirical-profile.md` §2 — Q 72 FR-neighborhood (Q 112 rank-1)
- `03-tafsir-survey.md` — classical sources behind the three pre-regs
- `04-hadith-corpus.md` — Bukhārī 755/4713, Muslim 908/909, Tirmidhī 3342/3375/3407, Aḥmad 1356
- `05-classical-claims-audit.md` — verdict synthesis
- `07-cross-references.md` — cluster-membership and cross-surah network
- `JOURNAL.md` — full run log
- `MASTER-FINDINGS-LEDGER.md` §10.18 — prior 5-qul cluster inline finding being replicated by Q072-F-01
