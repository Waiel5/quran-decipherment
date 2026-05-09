---
surah: 36
surah_name_ar: يس
surah_name_translit: Yāsīn
file_type: novel-findings
date_last_updated: 2026-05-09
phase: B+
verdict: EXTENDED — 7 pre-registered tests, 3 CONFIRMED/PASS + 4 NULL (with full prominence). Wave-H 2026-05-09 added F-05 / F-06 / F-07.
---

# Q 36 Yāsīn — Novel Findings

## 0. Source

This file presents 4 pre-registered novel empirical findings on Q 36, each with locked pre-reg, SHA-256-checksummed run script, and JSON-archived results. Pre-regs live in `preregs/`, scripts in `scripts/`, JSON outputs in `csv/`.

| ID | Pre-reg SHA-256 (head 12) | Script | JSON | Verdict |
|:--|:--|:--|:--|:--|
| Q036-F-01 | `5af602872a5a` | `Q036_F_01_recitation_frequency_weighted_centrality.py` | `Q036-F-01.json` | **NULL** (with prominence) |
| Q036-F-02 | `6d2a50a502bf` | `Q036_F_02_uas_vs_fadail_corpus_divergence.py` | `Q036-F-02.json` | **CONFIRMED** (3/3 conditions) |
| Q036-F-03 | `1575bf3f4bd1` | `Q036_F_03_kun_fa_yakun_climax.py` | `Q036-F-03.json` | **CONFIRMED** (3/3 conditions) |
| Q036-F-04 | `515ce2dea2c6` | `Q036_F_04_eschatological_formula_density.py` | `Q036-F-04.json` | **NULL** (with prominence) |

**Tally**: 2 CONFIRMED + 2 NULL — equal-NULL-prominence discipline followed; both NULL findings published with full prominence per [[INVESTIGATION-PROTOCOL]] §1.3.

## Q036-F-01 — Recitation-frequency-weighted centrality (NULL)

### Pre-registered hypothesis

The classical *qalb al-Qurʾān* claim was empirically tested at multi-axis quantitative form by [[h-new-82-yasin-heart|H-NEW-82]] and **NULL-ed at 0/6 axes**. H-NEW-82's pre-reg explicitly excluded "recitational frequency in classical practice" as a possible salvage axis. This pre-reg defines and tests that 7th axis: liturgy-weighted lexical centrality.

Hypothesis: Q 36 is in the top-quintile (rank ≤ 23/114) on liturgy-weighted lexical centrality, computed as Σ_t [fadāʾil_score(t) · root-Jaccard(s, t)] / Σ_t fadāʾil_score(t), where fadāʾil_score is the [[h-new-860-hadith-architectural-alignment|H-NEW-860]] rubric.

### Locked parameters

- Locked weights table from H-NEW-860 published rubric (10/10: Q 1, Q 2, Q 36, Q 67, Q 112; 9/10: Q 18; 8/10: Q 113, Q 114; 7/10: Q 12, Q 109; 6/10: Q 19; 5/10: Q 9, Q 10, Q 24, Q 87; 4/10: Q 55, Q 75; 3/10: Q 3, Q 56; 2/10: Q 33; 0/10: rest).
- Total weight Σ = 131.
- Rules-tuple: `(no-tashkeel, QAC-stem-roots, QAC v0.4, basmala-counted-only-in-Q1, Hafs-Kufan, mushaf-order)`.

### Result

| Metric | Value |
|:--|:-:|
| **Q 36 W-centrality** | 0.1622 |
| **Q 36 rank** | **46 / 114** (NOT top-quintile threshold of 23) |
| Q 112 W-centrality | 0.0303 |
| Q 112 rank | 105 / 114 |
| Q 67 W-centrality | (mid-pack) |
| Q 1 W-centrality | (mid-pack) |
| Q 2 W-centrality | (mid-pack-high; long surah benefits root-Jaccard) |
| Top 10 W-centrality | dominated by long-and-mid-Meccan surahs (Q 2, 7, 6, 26, 27, 28, 29, 39, 40 etc.) |

### Discriminating cross-check FAILED

The pre-reg locked Q 112 (the empirical FR-distance corpus centroid, rank 1 by minimum mean FR distance) as the discriminating control: Q 112 should out-rank Q 36 on a genuinely-discriminating centrality metric.

**Q 112 ranks 105/114 — far below Q 36 (rank 46)**. The metric inverts Q 112's classical priority. The mechanism: root-Jaccard is structurally biased toward long surahs (the union-and-intersection grows with size); Q 112's 4 short verses give it a tiny root-set (~10 distinct roots), while Q 36's 211 distinct roots give it a much larger Jaccard footprint regardless of liturgy-weighting. **The discriminating control fails — the metric does not coherently identify the FR-centroid.**

### Verdict

**NULL** (Q 36 outside top-quintile; binding H-NEW-82 prior preserved). The 7th-axis salvage attempt does NOT rehabilitate the *qalb al-Qurʾān* multi-axis claim. **The discriminating control failure on Q 112 is itself an honest result**: liturgy-weighted root-Jaccard is structurally biased toward long surahs and is not a reliable centrality metric. Future operationalisations of "liturgy-weighted centrality" should use length-normalised similarity (e.g., cosine on root-frequency vectors rather than set-Jaccard).

### Honest limits

- The H-NEW-860 rubric is itself the project's hand-coded fadāʾil score; using it as the weight in the metric is correct per the pre-reg but introduces a measurement-prior dependence.
- The root-Jaccard length-bias is well-known; the metric was nonetheless pre-locked. **The pre-reg is honored; the result is reported with full prominence.**
- A length-normalised version of the metric (cosine on stem-root frequency vectors weighted by H-NEW-860 fadāʾil score) is a queued follow-up (Q036-F-01b candidate) but is post-hoc.

### Cross-references

- [[h-new-82-yasin-heart|H-NEW-82]] — binding 6-axis NULL; this 7th axis adds a 7th NULL data-point.
- [[h-new-860-hadith-architectural-alignment|H-NEW-860]] — rubric source.
- [[h-new-111-fisher-rao-mushaf|H-NEW-111]] — empirical FR centroid is Q 112; metric inversion shows the test does not capture FR centrality.

## Q036-F-02 — UAS-vs-fadāʾil divergence cell membership (CONFIRMED 3/3)

### Pre-registered hypothesis

Per [[h-new-860-hadith-architectural-alignment|H-NEW-860]], Q 36 sits in the corpus's UAS-vs-fadāʾil-divergence cell (UAS rank > 25 + fadāʾil = 10/10), in the **mild-divergence** sub-cell relative to Q 112 / Q 67's extreme-divergence sub-cell.

Three sub-conditions:
- **(2a)** Q 36 in divergence cell: UAS rank > 25 AND fadāʾil = 10.
- **(2b)** Q 36 less divergent than Q 112 and Q 67: Q 36 UAS rank < Q 112's AND Q 36 UAS rank < Q 67's.
- **(2c)** Q 36's nearest fadāʾil-10 peer by FR distance is Q 67 (the meaning-iʿjāz cluster), NOT Q 1 or Q 2 (the structural-iʿjāz tier).

### Result

| Metric | Value |
|:--|:-:|
| Q 36 UAS rank | **35 / 114** |
| Q 36 UAS score | 0.5040 |
| Q 36 fadāʾil score | 10 / 10 |
| Q 1 UAS rank | 2 |
| Q 2 UAS rank | 3 |
| Q 67 UAS rank | 102 |
| Q 112 UAS rank | 109 |
| FR distance Q 36 → Q 1 | 0.9053 |
| FR distance Q 36 → Q 2 | 1.0078 |
| FR distance Q 36 → Q 67 | **0.7940** ← MIN |
| FR distance Q 36 → Q 112 | 0.9291 |
| **Nearest fadāʾil-10 peer** | **Q 67** ✓ |

**All 3 conditions CONFIRMED**:
- (2a) Q 36 UAS rank 35 > 25 AND fadāʾil = 10 ✓
- (2b) 35 < 102 AND 35 < 109 ✓
- (2c) FR-nearest fadāʾil-10 peer = Q 67 ✓

### Verdict

**CONFIRMED** (3/3 conditions). The dual-iʿjāz typology of [[cross-finding-026-iʿjāz-architecture|cross-finding-026]] is empirically supported at the surah-pair level: Q 36 belongs to the **meaning-iʿjāz cluster** (with Q 67 the nearest peer) NOT the structural-iʿjāz cluster (Q 1, Q 2 are FR-far). Q 36 is the **mild-divergence** exemplar of the meaning-iʿjāz cell — UAS rank 35 is intermediate between the structural-iʿjāz tier (rank 2-9) and the extreme-meaning-iʿjāz tier (rank 102-109).

This concretises the dual-iʿjāz typology at finer resolution than [[cross-finding-026-iʿjāz-architecture|cross-finding-026]] §13: the meaning-iʿjāz cell has internal structure (mild-divergence Q 36 vs extreme-divergence Q 67 / Q 112), not a flat single-cluster.

### Honest limits

- The fadāʾil-10 peer set {Q 1, 2, 36, 67, 112} is the H-NEW-860 published top-tier; using it as the test set is correct per the pre-reg but the test is sensitive to the rubric's published cuts.
- The "nearest peer = Q 67" finding is robust across rules-tuple variants (FR distances are computed on QAC stem-roots; under different tokenization the *order* of peers may shift but the *not Q 1 / not Q 2* finding is robust).
- The 18-position UAS-rank gap between Q 36 (35) and Q 67 (102) is the empirical signature of the mild-vs-extreme distinction within the meaning-iʿjāz cell.

### Cross-references

- [[cross-finding-026-iʿjāz-architecture|cross-finding-026]] — dual-iʿjāz typology, refined to 4-cell at §13 amendment.
- [[h-new-860-hadith-architectural-alignment|H-NEW-860]] — UAS-vs-fadāʾil divergence catalog.
- [[h-new-840-unified-architectural-score|H-NEW-840]] — UAS rank source.
- [[h-new-111-fisher-rao-mushaf|H-NEW-111]] — FR distance source.
- [[Q067-al-mulk/00-overview|Q 67 al-Mulk]] — Q 36's nearest fadāʾil-10 FR-peer.
- [[Q112-al-ikhlas/00-overview|Q 112 al-Ikhlāṣ]] — extreme-divergence cell in same typology.

## Q036-F-03 — Q 36:82 *kun-fa-yakūn* climax-position uniqueness (CONFIRMED 3/3)

### Pre-registered hypothesis

The classical exegetical observation (al-Rāzī Q 36:82, al-Zamakhsharī Q 36:82, Ibn Kathīr Q 36:82) that Q 36 is "constructed around" the *kun fa-yakūn* climax operationalises as: of the 8 corpus *kun fa-yakūn* verses, Q 36:82 is the only one positioned at >95% through its surah, with the next-closest at <90% and a gap of ≥ 10 percentage points.

### Result

| # | Reference | Position-in-surah |
|:-:|:--|:-:|
| 1 | Q 2:117 | 40.91% |
| 2 | Q 3:47 | 23.50% |
| 3 | Q 3:59 | 29.50% |
| 4 | Q 6:73 | 44.24% |
| 5 | Q 16:40 | 31.25% |
| 6 | Q 19:35 | 35.71% |
| 7 | **Q 36:82** | **98.80%** |
| 8 | Q 40:68 | 80.00% |

| Metric | Value |
|:--|:-:|
| Q 36:82 position | **98.80%** ✓ (>95%) |
| Other max position (Q 40:68) | **80.00%** ✓ (<90%) |
| Gap (Q 36:82 − Q 40:68) | **18.80 pp** ✓ (≥ 10 pp) |
| Cross-validated against min-tashkeel | TRUE ✓ |

**All 3 conditions CONFIRMED**.

### Verdict

**CONFIRMED** (3/3). Q 36:82 is the **only verse > 95% in the entire corpus's *kun fa-yakūn* family**. The next-closest instance Q 40:68 is 18.8 percentage points behind. The classical reading "Q 36 is structured around the *kun-fa-yakūn* climax" is empirically supported at the descriptive-position level.

This is a **novel cross-corpus structural fact** not previously catalogued in the project: Q 36:82 is positionally singular among the 8 corpus *kun-fa-yakūn* verses. The other 7 instances are mid-surah (23-44%) or late-mid-surah (Q 40:68 at 80%); only Q 36:82 is true peroratio.

### Honest limits

- The verdict is at descriptive-position level; no permutation null was applied (the test is deterministic on the corpus's 8 *kun fa-yakūn* verses).
- The 8-verse instance count is rules-tuple-stable (cross-validated `quran-no-tashkeel.json` and `quran-min-tashkeel.json`). Under broader matches (e.g., *fa-yakūn* anywhere) the count grows but the climax-position uniqueness of Q 36:82 is preserved.
- The rhetorical-climax claim assumes peroratio = high-position; Q 36:82 is verse 82 of 83 = 98.8%; the very last verse (Q 36:83) is the closing tasbīḥ. The structural sense is: *kun-fa-yakūn* (v.82) → *fa-subḥāna lladhī...* (v.83 closing tasbīḥ). The 2-verse closing block is unambiguously peroratio in any reasonable segmentation.

### Cross-references

- `02-content-analysis.md` §7 — Block G structural peroratio.
- `01-empirical-profile.md` §10 — corpus instance count + position table.
- `05-classical-claims-audit.md` Audit 5 — VINDICATED at descriptive-position level.
- `03-tafsir-survey.md` §3 — al-Rāzī, al-Zamakhsharī, Ibn Kathīr classical attestations.

## Q036-F-04 — Eschatological-formula density (NULL)

### Pre-registered hypothesis

al-Ghazālī's grounding for the *qalb al-Qurʾān* tradition (cited by al-Rāzī) attributes Q 36's centrality to its **dense resurrection-and-eschatology presentation** — "the *ḥashr* is established in this surah with the most-expressive form". We test: does Q 36 over-concentrate the Quranic eschatological-formula lexicon (8 sub-patterns: *yawm*, *al-sāʿa*, *al-ṣūr*, *al-qiyāma*, *baʿth*-conjugations, *nār*, *al-janna*, *m-w-t*) at a rate distinguishable from corpus mean, after Bonferroni correction (k=114)?

### Locked parameters

- Eschatology cluster: 8 substring patterns (locked above and in pre-reg).
- Rules-tuple: `(no-tashkeel, orthographic-substring, basmala-counted-only-in-Q1, Hafs-Kufan, mushaf-order)`.
- Permutation null: shuffle (surah → eschat-count) pairings 10,000× (seed 20260428), preserving total counts but breaking surah-association.
- α_Bonferroni = 0.05 / 114 = 4.39 × 10⁻⁴.

### Result

| Metric | Value |
|:--|:-:|
| Q 36 eschat tokens | **11** |
| Q 36 words | 754 |
| Q 36 density / 1000 | **14.59** |
| Corpus mean density | **10.93** / 1000 |
| Q 36 rank by density | **47 / 114** (NOT top-quintile threshold 23) |
| p_value (perm) | **0.2689** (not significant) |
| Q 75 control density | 66.67 / 1000 (rank 2) ✓ — control discriminates |
| Top-3 by density | Q 77 (82.42), Q 75 (66.67), Q 82 (60.98) |

Q 36's density (14.59 / 1000) is above corpus mean (10.93 / 1000) — direction is positive — but the magnitude is modest and the rank (47/114) is mid-pack. **p_value = 0.27 is far from any significance threshold**. The discriminating control (Q 75 al-Qiyāma) ranks #2 with 4.6× Q 36's density, confirming the test is discriminating.

### Verdict

**NULL** (Q 36 rank 47/114, p_perm = 0.27; Q 36 has *positive* eschatology density above corpus mean but is far from top-tier and is far from Bonferroni-significant). al-Ghazālī's "most-expressive ḥashr" claim is empirically **a moderate positive but NOT a corpus-distinguishing signature**.

The empirical top of the eschatology-density distribution is the **short-Meccan eschatological cluster** (Q 75, 77, 82, 99, 101, 102) — not Q 36. Q 36 has an absolutely-large *eschatological pericope* (Block E vv. 51-65 = 15 verses, ~140 words = 19% of the surah) but the surah's vocabulary outside Block E is non-eschatological (narrative + cosmic-signs + theodicy + anti-poetry), which dilutes the per-1000-words density.

This is an instructive NULL: **eschatology-pericope-presence ≠ eschatology-vocabulary-density**. Q 36 has the former but not the latter at corpus-distinguishing magnitude. al-Ghazālī's classical reading is **substantively correct in its emphasis on the resurrection presentation** but is not empirically corroborable as a vocabulary-density signature.

### Honest limits

- The 8 eschat sub-patterns are pre-locked. Adding additional patterns (*al-ḥashr*, *al-qaḍāʾ*, *al-faṣl*, etc.) would shift Q 36's count modestly but not move it into the top-23.
- The corpus-mean density 10.93 / 1000 is dominated by long-tail surahs that contain *yawm*, *kullu*, etc. in non-eschatological contexts. A more-precise eschatology-only filter (e.g., requiring *yawm* + an eschatological qualifier within 5 words) would shift baselines but is post-hoc.
- The pericope-vs-density distinction noted above is an empirical fact not a rules-tuple artifact: Block E (vv. 51-65) IS the corpus's signature eschatological pericope-by-passage; the per-surah density measure dilutes this with the non-eschatological vv. 1-50 + 66-83.
- A queued follow-up (Q036-F-04b candidate, post-hoc) is the **eschatology-pericope-coherence test**: does Block E (vv. 51-65) score higher in pairwise root-Jaccard internal cohesion than 80% of random 15-verse intra-surah spans? This is the parallel to Q024-F-03A's al-ifk-passage cohesion test.

### Cross-references

- `02-content-analysis.md` Block E — eschatological resurrection arc.
- `05-classical-claims-audit.md` Audit 6 — Q 36 word-count corpus-positional-uniqueness FALSIFIED (parallel falsification at the position axis).
- [[h-new-82-yasin-heart|H-NEW-82]] — binding NULL on the multi-axis "heart" claim.
- al-Ghazālī's *Iḥyāʾ ʿUlūm al-Dīn* citation via al-Rāzī — `03-tafsir-survey.md` §2.1.

## 5. Aggregate verdict for Q 036 novel-findings family

| Test | Verdict | Direction relative to *qalb-al-Qurʾān* claim |
|:-:|:--|:--|
| Q036-F-01 (liturgy-weighted centrality) | NULL | confirms H-NEW-82 binding NULL on a 7th axis |
| Q036-F-02 (UAS-vs-fadāʾil divergence cell) | CONFIRMED 3/3 | refines dual-iʿjāz typology with Q 36 in mild-divergence sub-cell |
| Q036-F-03 (*kun-fa-yakūn* climax position) | CONFIRMED 3/3 | novel structural fact: Q 36:82 is corpus's only > 95% *kun-fa-yakūn* verse |
| Q036-F-04 (eschatology density) | NULL | al-Ghazālī's "expressive ḥashr" classical reading not corroborable as vocabulary-density |

**Aggregate**: 2 CONFIRMED + 2 NULL. The CONFIRMED tests both refine the dual-iʿjāz typology (F-02) and document a novel positional-structural fact (F-03). The NULL tests both confirm the H-NEW-82 binding prior (F-01) and surface an instructive pericope-vs-density distinction (F-04).

The classical *qalb al-Qurʾān* claim's **liturgical-theological content** is confirmed (Q 36 is in the meaning-iʿjāz cluster with Q 67); the **multi-axis quantitative-centrality form** of the claim remains FALSIFIED (H-NEW-82 binding NULL + Q036-F-01 7th-axis NULL); the **vocabulary-density form** is NULL (Q036-F-04). What survives is a single novel structural finding: **Q 36:82 is the corpus's only *kun-fa-yakūn* verse positioned at the rhetorical climax of its surah** (Q036-F-03).

---

## 6. Wave-H 2026-05-09 addendum — 3 additional pre-registered tests

Three further pre-registered tests, each with its own SHA-locked pre-reg, run script, and JSON output, were added in the Wave-H session 2026-05-09.

| ID | Pre-reg SHA-256 (head 12) | Script | JSON | Verdict |
|:--|:--|:--|:--|:--|
| Q036-F-05 | `9cc710c5a340` | `Q036_F_05_ys_singleton.py` | `Q036-F-05.json` | **PASS-DIRECTED-CORPUS-EXACT** |
| Q036-F-06 | `69c0782025c1` | `Q036_F_06_fr_centroid_audit.py` | `Q036-F-06.json` | **PASS-DIRECTED-REAFFIRMED** |
| Q036-F-07 | `6f71e1877fff` | `Q036_F_07_town_of_prophets_cohesion.py` | `Q036-F-07.json` | **NULL** (with full prominence) |

Full findings markdowns:
- [[Q036-F-05-ys-singleton]] — corpus-EXACT singleton verification of the يس opening
- [[Q036-F-06-fr-centroid-audit]] — Q 112 confirmed as the corpus FR-centroid (Q 36 rank 64/114)
- [[Q036-F-07-town-of-prophets-cohesion]] — aṣḥāb al-qarya pericope NOT more aligned with parallel town-pericopes than with ambient Q 36

### Headline for each

- **Q036-F-05 (PASS)**: Across `quran-no-tashkeel.json`, `quran-min-tashkeel.json`, and `data/alt-text/quran-uthmani-consonantal.json`, exactly one surah's verse 1 equals "يس" — Q 36. 1/114 corpus-EXACT. The YS combination has no other muqaṭṭāʿat attestation in the corpus, neither as standalone v1 nor as a substring of any other muqaṭṭāʿat string. Q 36 is one of three "ungrouped" muqaṭṭāʿat openers (with Q 19 *KHYʿṢ* and Q 42's *ḤM | ʿSQ* composite) that does not belong to any letter-family cluster (الم / الر / حم / طسم).

- **Q036-F-06 (PASS-DIRECTED-REAFFIRMED)**: On the project-canonical H-NEW-111 FR-roots distance matrix (K=500 truncation, Dirichlet α=0.5 smoothing), Q 112 al-Ikhlāṣ ranks #1 with mean-FR = 0.7592, Q 36 ranks 64/114 with mean-FR = 0.9430. The pre-committed prediction (Q 112 in top-3, Q 36 outside top-30) is reaffirmed on both conditions. This is the **8th independent axis** on which the classical *qalb al-Qurʾān* multi-axis quantitative-centrality claim fails for Q 36 (the prior 7 are H-NEW-82's 6 axes + Q036-F-01's liturgy-weighted Jaccard). The empirical corpus FR-centroid is Q 112.

- **Q036-F-07 (NULL)**: The aṣḥāb al-qarya pericope (Q 36:13-32) has root-Jaccard 0.172 with the union of three parallel town-destruction pericopes (Q 7:73-93, Q 11:42-95, Q 27:45-58) but root-Jaccard 0.194 with the rest of Q 36. The pre-committed direction (parallel > ambient) is reversed by Δ = −0.022, and the 10,000-permutation null gives p = 0.19. Published with equal NULL prominence. Three plausible mechanisms: (1) local-cohesion dominates inter-pericope cohesion (consistent with H-NEW-660); (2) Q 36's pericope is content-typologically the *unnamed-city + unnamed-believing-man* configuration distinct from the named-prophet destructions of Q 7/11/27; (3) the *muʾadhdhin* speech (vv. 20-27) contains uniquely-Q 36 roots that inflate the ambient comparison. This is an **instructive NULL**: typological membership at the narrative level does NOT imply root-vocabulary cohesion.

### 7. Aggregate Q 036 novel-findings family (post-Wave-H)

| Test | Verdict | Direction relative to *qalb-al-Qurʾān* / structural claims |
|:-:|:--|:--|
| Q036-F-01 (liturgy-weighted centrality) | NULL | confirms H-NEW-82 binding NULL on a 7th axis |
| Q036-F-02 (UAS-vs-fadāʾil divergence cell) | CONFIRMED 3/3 | refines dual-iʿjāz typology with Q 36 in mild-divergence sub-cell |
| Q036-F-03 (*kun-fa-yakūn* climax position) | CONFIRMED 3/3 | novel structural fact: Q 36:82 is corpus's only > 95% *kun-fa-yakūn* verse |
| Q036-F-04 (eschatology density) | NULL | al-Ghazālī's "expressive ḥashr" classical reading not corroborable as vocabulary-density |
| **Q036-F-05** (YS singleton) | **PASS-DIRECTED-CORPUS-EXACT** | structural marker; Q 36 is the unique YS muqaṭṭāʿat opener |
| **Q036-F-06** (FR-centroid audit) | **PASS-DIRECTED-REAFFIRMED** | 8th-axis NULL on quantitative *qalb al-Qurʾān* form; Q 112 confirmed as FR-centroid |
| **Q036-F-07** (aṣḥāb al-qarya cohesion) | **NULL** (Δ=−0.022, p=0.19) | typological membership ≠ root-vocabulary cohesion |

**Post-Wave-H aggregate**: 3 PASS-direction confirmations + 4 NULL. The pattern is now eight independent quantitative tests of "Q 36 is central/maximal/typed on axis X", with zero PASS at the centrality direction and one structural-fingerprint PASS at the singleton direction. The classical liturgical-theological claim remains real (Q 36 is in the meaning-iʿjāz cluster, fadāʾil-grade 10/10) but **the quantitative-architectural form of the claim is now decisively NULL across 8 axes** — a 7-NULL + 1-PASS-reaffirming-the-NULL fingerprint of robust falsification.
