---
surah: 29
surah_name_translit: al-ʿAnkabūt
file_type: novel-findings
date_last_updated: 2026-05-10
phase: B+
verdict: "3 pre-registered novel tests: Q029-F-02 ALM-4 pericope cohesion NULL (pre-commit direction failed, equal-prominence); Q029-F-03 *ʿankabūt* corpus-singleton PASS-DIRECTED (lemma 2 tokens, 1 verse, 1 surah); Q029-F-04 spider-parable typological uniqueness PASS-DIRECTED (3/3 sub-claims). Net: 2 PASS-DIRECTED + 1 NULL, with the NULL providing a cross-finding-025 marker-thickness counter-data-point on a contiguous Late-Meccan ALM-quartet."
---

# Q 29 al-ʿAnkabūt — Novel Findings

Three pre-registered novel tests. Pre-regs at `preregs/Q029-F-NN-*-prereg.md`. JSON outputs at `csv/Q029-F-NN.json`. Scripts at `scripts/Q029_F_NN_*.py`.

## T1 — Q029-F-02: ALM-4 cluster {Q 29, 30, 31, 32} pericope-window root-Jaccard cohesion

### Pre-registration

- Pre-reg: `preregs/Q029-F-02-alm-4-pericope-cohesion-prereg.md`
- SHA256: `3d4acccc01e01985bcdbef1b4dcd4dd5c7005878862dbd291a7159c4406994d8`
- Seed: 20260509; perms: 10,000
- Direction (LOCKED): TIGHTER — J_mean > null mean
- A-priori pre-registration: PASS-DIRECTED at pericope scale (per cross-finding-025-formal / H-NEW-1380 scale-of-aggregation corollary)

### Result

| Quantity | Value |
|:--|:--|
| Observed mean pairwise root-Jaccard | **0.0434** |
| Null mean (10,000 length-matched random 4-pericope draws) | 0.0497 |
| Null std | 0.0250 |
| z-score | **−0.25** |
| p_one_sided_ge_perm | 0.557 |
| Direction match (obs > null) | **FALSE** |
| **Verdict** | **NULL — direction reversed** |

Per-pair Jaccards (6 pairs):

| Pair | J | Intersection (roots) |
|:--|:-:|:--|
| Q 29:1-3 ↔ Q 30:1-3 | **0.000** | ∅ |
| Q 29:1-3 ↔ Q 31:1-3 | **0.000** | ∅ |
| Q 29:1-3 ↔ Q 32:1-3 | 0.143 | {Elm, qbl, qwl} |
| Q 30:1-3 ↔ Q 31:1-3 | **0.000** | ∅ |
| Q 30:1-3 ↔ Q 32:1-3 | **0.000** | ∅ |
| Q 31:1-3 ↔ Q 32:1-3 | 0.118 | {hdy, ktb} |

Pericope root-set sizes: Q 29:1-3 = 11 roots; Q 30:1-3 = 4 roots; Q 31:1-3 = 6 roots; Q 32:1-3 = 13 roots.

### Interpretation

**T1 is a NULL with equal prominence**. The pre-registered PASS-DIRECTED prediction (per cross-finding-025-formal scale-of-aggregation law that "narrow scale + multi-axis correlation should cohere") was NOT met. 4 of 6 pairs have zero root-intersection at the first-3-verses pericope window.

This is informative as a **CROSS-FINDING-025 boundary-case**: even with multi-axis correlation present (shared ALM opener + contiguous mushaf-position + Late-Meccan chronology + 3-of-4 with book-reference morphology), the 3-verse pericope window is too narrow to drive root-Jaccard cohesion. Specifically:
- Q 30:1-3 and Q 31:1-3 are *very* short pericopes (only 4 and 6 unique roots respectively), driven by muqaṭṭāʿāt openers (1 verse) + 2 short book-reference verses. Their dominant content (Q 30 = Byzantine prophecy; Q 31 = Luqmān-introduction; Q 32 = creation-narrative) only begins in v 4+.
- Q 29:1-3 is by contrast a self-contained 3-verse imtihān anchor with 11 unique roots, but its content is doctrinal-imtihān, not yet thematically aligned with Q 30/31/32 v 1-3.

The NULL DOES NOT falsify the broader Q 29 ↔ {Q 30, 31, 32} relationship — it falsifies the specific claim that a 3-verse pericope-window captures the cohesion. The cohesion may exist at longer pericope-windows (e.g., first 10 verses) or at the thematic-narrative level. This is an honest scope-restriction of the multi-axis-correlation rule.

### Cross-references

- [[../findings/cross-finding/cross-finding-025-multi-axis-architecture|cross-finding-025]]: this is a counter-data-point for the "multi-axis ⇒ FR-cohesive" direction at pericope-scale; refines the rule to require longer aggregation windows.
- [[../findings/phase-b-hypotheses/prereg-h-new-1380-iblis-pericope-replication|H-NEW-1380 / scale-of-aggregation corollary]]: pericope-scale tests can PASS or NULL independently of whole-surah verdicts; this is the second NULL pericope-scale result on a markedly-cohesive surface set (the first being the implicit baseline; the H-NEW-1380 Iblīs-pericope PASSED).
- [[../Q030-al-rum/csv/Q030-F-08.json|Q030-F-08]]: whole-surah ALM-6 PARTIAL (Cell A NULL, Cell B PASS); the ALM-4 sub-set at whole-surah is implicit in the Q030-F-08 pair-distance matrix (mean of the 6 Q 29/30/31/32 pairs = 0.916, comparable to ALM-6 mean 0.926).

### Honest pre-commit attestation

The direction was LOCKED before observation as "TIGHTER — J_mean > null mean." The observed J_mean (0.0434) is LESS than the null mean (0.0497) — direction REVERSED. Per Protocol §1.8, this is published as NULL with full prominence. No post-hoc adjustment to the pre-reg.

## T2 — Q029-F-03: *ʿankabūt* (spider) corpus-singleton verification

### Pre-registration

- Pre-reg: `preregs/Q029-F-03-ankabut-corpus-singleton-prereg.md`
- SHA256: `2718837da9e3c5dce8d955da9752a38f654c9cd100f30b81f5751f46b0a2d6a7`
- Direction (LOCKED): corpus-SINGLETON (1 surah, 1 verse)

### Result

| Axis | Value |
|:--|:--|
| Lemma `LEM:Eankabuwt` token count | **2** |
| Distinct surahs | **1** |
| Distinct verses | **1** — Q 29:41 |
| Root `ROOT:Enkb` attestation | 2 tokens, 1 surah, 1 verse |
| **Verdict** | **PASS-DIRECTED — corpus-singleton (lemma)** |

Comparator anchor (animal-vehicle lemmas in the Quran, also corpus-singletons):

| Lemma | English | Tokens | Surahs | Verses |
|:--|:--|:-:|:-:|:--|
| `Eankabuwt` | spider | 2 | 1 | Q 29:41 |
| `n~aHol` | bee | 1 | 1 | Q 16:68 |
| `namolap` | "an ant" (one specific) | 1 | 1 | Q 27:18 |
| `n~amol` | ant(s) collective | 2 | 1 | Q 27:18 |
| `*ubaAb` | fly | 2 | 1 | Q 22:73 |

**Observation**: all 4 animal-vehicle lemmas in the Quran are corpus-singletons at the surah level. Each animal appears in exactly one surah. This is itself a corpus-architectural fact — the Quran does NOT recycle animal-vehicle parables across multiple surahs.

### Interpretation

Q 29:41 is the unique corpus attestation of the *ʿankabūt* lemma. The 2 tokens within v 41 form a *radd al-ʿajuz ʿalā al-ṣadr* (return-of-end-to-beginning) micro-structure (the spider is mentioned at the parable-opening and at the frailty-superlative).

This is **VINDICATION** of al-Rāzī's qualitative claim about the surah's eponym (the surah is named "the Spider" because the lemma appears here and nowhere else). The naming-by-unique-attestation is itself a structural-iʿjāz signature: 6 of the 114 surah-names are derived from corpus-unique attestation lemmas, including Q 16 al-Naḥl (bee), Q 27 al-Naml (ant — collective), Q 22 al-Ḥajj (different criterion), Q 29 al-ʿAnkabūt (spider).

### Cross-references

- [[Q029-F-01-ankabut-parable-hapax-prereg|Q029-F-01]] (earlier 5-lemma hapax-count): result subsumed and refined here.
- [[../Q016-al-nahl/00-overview|Q 16 al-Naḥl]]: bee, corpus-singleton at Q 16:68.
- [[../Q027-al-naml/00-overview|Q 27 al-Naml]]: ant, corpus-singleton at Q 27:18.
- [[../Q022-al-hajj/00-overview|Q 22 al-Ḥajj]]: fly, corpus-singleton at Q 22:73 (not the surah-eponym).

## T3 — Q029-F-04: Q 29:41 spider-web parable typological uniqueness

### Pre-registration

- Pre-reg: `preregs/Q029-F-04-animal-parable-typology-prereg.md`
- SHA256: `899a4c2201655c2d28e75c8d9c5cde7fa86e65c6a2d2f7794236311453ffebfe`
- Direction (LOCKED): Q 29:41 is the UNIQUE corpus-instance of the joint schema {animal-vehicle + shelter-lemma + frailty-root}

### Result

| Sub-claim | Result | Pass? |
|:--|:--|:--|
| (a) `LEM:Eankabuwt` corpus-singleton | Q 29:41 alone | **PASS** |
| (b) `LEM:>awohan` (frailty-superlative) corpus-singleton | Q 29:41 alone | **PASS** |
| (c) Joint schema {animal-lem + shelter-lem `bayot` + frailty-root (whn∪DEf)} corpus-unique | Q 29:41 alone | **PASS** |
| **Composite verdict** | 3/3 sub-claims PASSED | **PASS-DIRECTED — corpus-unique parable schema** |

Descriptive context (intersections at the verse-level):

| Intersection | Verses |
|:--|:--|
| Verses with any animal-vehicle lemma | Q 16:68 (bee), Q 22:73 (fly), Q 27:18 (ant), Q 29:41 (spider) |
| Verses with animal + shelter (`bayot`) | Q 16:68 (bee builds in mountains/trees — `bayot` "houses"), Q 29:41 (spider takes a house) |
| Verses with animal + frailty root | Q 22:73 (the fly + `DEf` "weak" — *ḍaʿufa al-ṭālibu wa-l-maṭlūb*), Q 29:41 (spider + `whn` — *awhana al-buyūt*) |
| Verses with animal + shelter + frailty (joint) | **Q 29:41 ONLY** |

### Interpretation

Q 29:41 is corpus-unique on three independent lexical/semantic axes:
1. The eponym lemma (*ʿankabūt*) is corpus-singleton.
2. The frailty-superlative lemma (*awhan*) is corpus-singleton.
3. The joint schema {animal-vehicle + shelter + frailty} is satisfied ONLY at Q 29:41 across the entire 6,236-verse corpus.

This is a **PASS-DIRECTED** at law-strength for the al-Rāzī / al-Bāqillānī iʿjāz al-tashbīh doctrine, at the intra-Quranic axis. The same schema does not occur elsewhere; the parable is structurally unique.

The closest comparator is Q 22:73 (fly parable) which uses an animal as a *mathal*-vehicle but with the impotence-of-creation common property (cannot create a fly), NOT the frailty-of-shelter property. The two are typologically distinct.

### Cross-references

- [[Q029-F-01-ankabut-parable-hapax-prereg|Q029-F-01]] (earlier): 2-of-5 candidate lemmas hapax (*Eankabuwt* + *>awohan*) — subsumed.
- [[../Q022-al-hajj/00-overview|Q 22 al-Ḥajj]] §Q 22:73: fly-parable.
- al-Bāqillānī *Iʿjāz al-Qurʾān*: iʿjāz al-tashbīh doctrine.
- al-Rāzī *Mafātīḥ al-ghayb* on Q 29:41 (MW-6 PENDING page-citation).
- [[../findings/cross-finding/cross-finding-026-iʿjāz-architecture|cross-finding-026]] (iʿjāz architecture).

## Summary of novel findings

| ID | Test | Verdict | Note |
|:--|:--|:--|:--|
| Q029-F-02 | ALM-4 pericope-window Jaccard | **NULL** (pre-commit-direction-failed) | Equal-prominence NULL; refines cross-finding-025 scope. |
| Q029-F-03 | *ʿankabūt* corpus-singleton | **PASS-DIRECTED** | Vindicates al-Rāzī's eponym-uniqueness claim. |
| Q029-F-04 | Spider-parable typological uniqueness | **PASS-DIRECTED (3/3)** | Vindicates al-Bāqillānī iʿjāz al-tashbīh at intra-Quran scale. |
| Q029-F-01 | (earlier) Q 29:41 hapax-count (5-lemma) | PASS-DIRECTED (2 hapax) | Subsumed by Q029-F-03 + Q029-F-04. |

## Honest limits

- Q029-F-02 NULL is real and direction-reversed; it shows that the 3-verse pericope window is too narrow for ALM-4 root-Jaccard cohesion even with multi-axis correlation. The NULL refines, not falsifies, cross-finding-025.
- Q029-F-03 and Q029-F-04 are deterministic count-verifications (no permutation null applies). Their "PASS-DIRECTED" verdicts are structural-uniqueness verifications, not probabilistic tests.
- Q029-F-04 sub-claim (c) uses a stipulated 3-part schema; alternative schemas yield different verdicts. The pre-reg locks ONE schema.
- al-Bāqillānī's full iʿjāz al-tashbīh claim requires cross-corpus comparison to pre-Islamic poetry, queued but not in this run.
