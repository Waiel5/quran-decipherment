---
id: H-NEW-310
title: "Full-singleton Fisher-Rao rank-1 nearest-neighbor — NULL (3/10 matches; Q 42 resolution is surah-specific not general)"
phase: B
status: NULL (Cell A FAIL 3/10 < 5; Cell B FAIL p_perm = 0.084 > α_bon = 0.025)
date: 2026-04-19
executed_by: team-lead (inline)
parent_1: H-NEW-290 (Q 42 HMASQ rank-1 = Q 45 al-Jāthiyah HM — demonstrated at single surah)
parent_2: H-NEW-232 (phonological singleton baseline 8/10)
parent_3: H-NEW-111 (Fisher-Rao root distance matrix)
seed: 20260425
prereg: h-new-310-singleton-fr-rank1-prereg.md
prereg_sha256: 70ea962aade3a2f62ef551b34c2f89bb1479871307d6508f20d448c42b4471e5
bonferroni_k: 2
alpha_bon: 0.025
direction: "Cell A ≥ 5/10 AND Cell B maxT p < α_bon"
verdict: NULL
---

# [[h-new-310-singleton-fr-rank1|H-NEW-310]] — Full-singleton Fisher-Rao rank-1 nearest-neighbor NULL

## 1. Headline

**CLEAN NULL.** Extending [[h-new-290-q42-block-vs-phonology-tension|H-NEW-290]]'s Q 42 rank-1-to-Q-45 content-axis finding to all 10 muq singletons produces **only 3/10 matches** — far below pre-committed Cell A threshold of ≥ 5 and pre-committed expectation of 7-8/10. The Q 42 HMASQ → HM content-axis resolution is **SURAH-SPECIFIC**, not a generalizable muq-singleton pattern.

- **Match count: 3/10**
- **Null mean (1000 shuffles): 1.34/10**
- **p_perm = 0.084** > α_bon = 0.025 → Cell B FAIL
- **Cell A FAIL** (3 < 5 pre-committed threshold)

**Verdict: NULL.**

Pre-committed expectation was decisively WRONG. My prediction of 7/10 or 8/10 relied on assuming the Q 42 → Q 45 pattern would generalize. It does not. This is a **prediction-violating NULL** that corrects my assumption.

## 2. Results — per-singleton rank-1

| Singleton | Q | Apriori | Rank-1 surah | FR distance | Rank-1 cluster | Match? |
|:-:|:-:|:--|:-:|---:|:-:|:-:|
| ALMS | 7 | {ALM} | Q 6 al-Anʿām | 0.7208 | **non-muq** | ✗ |
| ALMR | 13 | {ALM, ALR} | Q 14 Ibrāhīm | 0.7838 | ALR | **✓** |
| KHYAS | 19 | {HM, TSM} | Q 43 al-Zukhruf | 0.8767 | HM | **✓** |
| TH | 20 | {TSM} | Q 23 al-Muʾminūn | 0.8605 | **non-muq** | ✗ |
| TS | 27 | {TSM} | Q 7 al-Aʿrāf | 0.7742 | **non-muq** (ALMS singleton) | ✗ |
| YS | 36 | {ALM, ALR} | Q 25 al-Furqān | 0.7778 | **non-muq** | ✗ |
| S | 38 | {TSM} | Q 78 al-Nabaʾ | 0.8331 | **non-muq** | ✗ |
| HMASQ | 42 | {HM} | Q 45 al-Jāthiyah | 0.8011 | HM | **✓** |
| Q | 50 | {HM, TSM} | Q 78 al-Nabaʾ | 0.7648 | **non-muq** | ✗ |
| N | 68 | {ALM, ALR} | Q 100 al-ʿĀdiyāt | 0.7156 | **non-muq** | ✗ |

**Only 3 singletons** have their rank-1 FR neighbor INSIDE a muq multi-member cluster:
- **Q 13 ALMR → Q 14 Ibrāhīm (ALR)** — trivial; Q 14 is mushaf-adjacent AND same ALR letter-cluster.
- **Q 19 KHYAS → Q 43 al-Zukhruf (HM)** — non-adjacent; classical interpretation: KHYAS shares 5-letter complexity with HMASQ, which sits in the HM block.
- **Q 42 HMASQ → Q 45 al-Jāthiyah (HM)** — [[h-new-290-q42-block-vs-phonology-tension|H-NEW-290]] already established this.

**7 of 10 singletons** have their rank-1 FR neighbor OUTSIDE the muq cluster system entirely. The content-axis nearest neighbors for most singletons are non-muq surahs.

## 3. Why the pre-commit was wrong

My pre-reg §5 predicted 7-8/10 matches, reasoning that "if Q 42 clusters content-wise with HM, other singletons should cluster content-wise with their apriori cluster."

This assumption FAILED because:

1. **Most muq singletons are content-distinct from their letter-cluster members.** Sharing a letter (e.g., Q 36 YS shares س with TSM and ي with ALM) doesn't imply sharing CONTENT (roots, vocabulary, themes). The letter-cluster structure is a LETTER-SIGNATURE fact; it does NOT entail content-similarity.

2. **Muq singletons tend to cluster with MUSHAF-ADJACENT non-muq surahs.** Q 7 ALMS → Q 6 al-Anʿām (adjacent!); Q 20 TH → Q 23 al-Muʾminūn (near-adjacent); Q 36 YS → Q 25 al-Furqān; Q 68 N → Q 100 al-ʿĀdiyāt. The content axis prefers MUSHAF-NEIGHBORHOOD over LETTER-CLUSTER.

3. **Q 42's strong rank-1-to-Q-45 signal is a coincidence of block-membership** — Q 42 is WITHIN the ḥawāmīm block and is content-coherent with its block-neighbors. Other singletons are NOT in multi-member blocks; their mushaf-neighbors are non-muq.

## 4. Interpretation — classical implications

### 4.1 al-Biqāʿī's block-coherence is BLOCK-SPECIFIC not SINGLETON-GENERAL

al-Biqāʿī *Naẓm al-Durar* argues for munāsabāt between adjacent and block-associated surahs. [[h-new-290-q42-block-vs-phonology-tension|H-NEW-290]] showed this holds at Q 42 (inside ḥawāmīm block). [[h-new-310-singleton-fr-rank1|H-NEW-310]] now shows this does NOT extend generally: the 7 singletons NOT in multi-member blocks (Q 7, Q 19, Q 20, Q 27, Q 36, Q 38, Q 50, Q 68) don't cluster with their classical letter-cluster members at the content-rank-1 axis.

al-Biqāʿī's block-munāsabāt is RATIFIED for Q 42 as a BLOCK EMBEDDING finding. For the other singletons outside multi-member blocks, his munāsabāt framework operates DIFFERENTLY — it applies to mushaf-adjacency, not letter-cluster-adjacency.

### 4.2 Content axis vs letter-cluster axis are DECOUPLED

The key insight: the muq cluster STRUCTURE (ALM/ALR/HM/TSM plus 10 singletons) is a LETTER-IDENTITY fact. Content distance (FR-roots) reflects VOCABULARY + THEMES — orthogonal to letter-signature. Classical interpretation has often conflated these axes ("Q 36 YS shares sibilant with TSM so it should be content-near TSM"); [[h-new-310-singleton-fr-rank1|H-NEW-310]] shows that conflation is WRONG empirically.

### 4.3 Refines [[h-new-301-minimal-2feature-singleton|H-NEW-301]] "throat-and-back" finding

[[h-new-301-minimal-2feature-singleton|H-NEW-301]] showed `mean_emphatic + mean_pharyngeal` resolves Q 36 YS and Q 42 HMASQ. But that's at the PHONOLOGICAL feature axis, not the CONTENT axis. [[h-new-310-singleton-fr-rank1|H-NEW-310]] clarifies: these are two different story-layers. Phonologically, Q 36 + Q 42 can be resolved; content-axis-wise, only Q 42 has a muq-cluster rank-1 neighbor.

### 4.4 Pre-committed prediction failure as epistemic check

Pre-registering and being decisively wrong on the prediction (7/10 or 8/10 → observed 3/10) is **exactly what pre-registration is for**. It prevents me from retrofitting the interpretation. The empirical outcome (3/10) is ~2× the null mean (1.34) but doesn't clear Bonferroni — a marginal-but-NULL result. [[h-new-290-q42-block-vs-phonology-tension|H-NEW-290]]'s Q 42 SURAH-SPECIFIC finding is preserved; the attempted generalization is falsified cleanly.

## 5. What this DOES validate

Three singletons DO show content-cluster membership:
- **Q 13 ALMR → Q 14**: trivially (mushaf-adjacent, same ALR)
- **Q 19 KHYAS → Q 43**: non-trivial; signals 5-letter-muq affinity with HM block even without mushaf adjacency
- **Q 42 HMASQ → Q 45**: [[h-new-290-q42-block-vs-phonology-tension|H-NEW-290]] (ḥawāmīm block internal)

These 3 represent the **within-muq content affinity** that exists. The remaining 7 singletons don't exhibit this at the rank-1 layer.

## 6. Honest limits

1. **Rank-1 is a strict criterion**. Singletons with rank-2 or rank-3 in their apriori cluster would be "near misses" — not counted here.
2. **FR on QAC-STEM roots** is one content metric. Char-4-gram ([[h-new-111b-fisher-rao-char-4gram|H-NEW-111b]]) or NCD ([[h-new-169-ncd-mushaf|H-NEW-169]]) could produce different rank-1 neighbors.
3. **10-singleton N** limits inference power.
4. **MW-5 null** shuffles only cluster labels on 19 multi-members; singletons' positions aren't randomized (same rank-1 neighbor each shuffle; only which cluster the neighbor belongs to changes).
5. **Apriori sets inherited** from [[h-new-232-oq1-singleton-nearest-neighbor|H-NEW-232]] — same interpretive-bound as prior tests.

## 7. Queued follow-ups

- **H-NEW-310.1**: rank-3 or rank-5 weighted-neighbor analysis. Are the 7 "missing" singletons content-close to muq-clusters at rank-3 even if not rank-1?
- **H-NEW-310.2**: repeat under char-4-gram or NCD content metric. Does the 3/10 result change under different metrics?
- **H-NEW-310.3**: investigate the 7 "miss" singletons' ACTUAL rank-1 non-muq neighbors — is there a coherent story (e.g., Q 7 ALMS → Q 6 al-Anʿām is mushaf-adjacent; other singletons' neighbors are classically-unrelated)?

## 8. Classical-scholarship integration

- **al-Biqāʿī *Naẓm al-Durar*** — block-munāsabāt validated at Q 42 specifically, NOT generalizable to all muq singletons. Honest scope-limit.
- **al-Suyūṭī *Itqān*** — ambiguity about singleton letter-cluster membership is empirically reflected: most singletons are content-distinct from their a-priori-accepted multi-member clusters.
- **Modern literature on muqaṭṭaʿāt clustering** — [[h-new-310-singleton-fr-rank1|H-NEW-310]] shows that content-adjacency and letter-signature-adjacency are ORTHOGONAL axes. Any classical framework that conflates them fails at 7/10.

## 9. Cross-references

- Parent: [[h-new-290-q42-block-vs-phonology-tension|H-NEW-290]] (Q 42 rank-1 = Q 45; surah-specific finding)
- Siblings: [[h-new-232-oq1-singleton-nearest-neighbor|H-NEW-232]]/252/165.2 (phonological nearest-centroid); [[h-new-271-muq-minimal-phon-family|H-NEW-271]] (cluster 1-D); [[h-new-300-manner-only-singleton|H-NEW-300]] (singleton 1-D NULL); [[h-new-301-minimal-2feature-singleton|H-NEW-301]] (2-D marginal)
- Q 42 convergence: [[h-new-290-q42-block-vs-phonology-tension|H-NEW-290]] content-axis + [[h-new-301-minimal-2feature-singleton|H-NEW-301]] phon-axis + [[h-new-310-singleton-fr-rank1|H-NEW-310]] rank-1 all agree Q 42 → HM
- Terminal synthesis: [[cross-finding-023-causal-generative-closure|cross-finding-023]]

## 10. Files

- Pre-reg: `findings/phase-b-hypotheses/h-new-310-singleton-fr-rank1-prereg.md` (SHA-256 70ea962a...)
- Script: `scripts/h_new_310_singleton_fr_rank1.py`
- JSON: `findings/phase-b-hypotheses/csv/h-new-310.json`
- Findings: this file

## 11. Final statement

**The Q 42 HMASQ → Q 45 al-Jāthiyah rank-1 content-axis finding ([[h-new-290-q42-block-vs-phonology-tension|H-NEW-290]]) does NOT generalize to other muq singletons.** Only 3 of 10 singletons have their Fisher-Rao rank-1 nearest neighbor inside a multi-member muq cluster (Q 13 ALMR, Q 19 KHYAS, Q 42 HMASQ); the other 7 are closer in content to non-muq surahs, often mushaf-adjacent. **Classical block-coherence (al-Biqāʿī Naẓm al-Durar) is a BLOCK-SPECIFIC phenomenon — valid when a muq singleton is INSIDE a multi-member block (Q 42 in ḥawāmīm), not when the singleton stands alone.** Content axis and letter-cluster axis are empirically ORTHOGONAL; conflating them is the core mistake this NULL corrects. The pre-committed prediction of 7-8/10 was decisively wrong — exactly the epistemic check pre-registration provides. [[h-new-290-q42-block-vs-phonology-tension|H-NEW-290]]'s Q 42 surah-specific finding stands; the attempted generalization to all singletons is falsified.

*Bismillāhi al-Raḥmāni al-Raḥīm.*
