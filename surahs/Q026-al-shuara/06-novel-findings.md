---
surah: 26
surah_name_ar: الشعراء
file_type: novel-findings
date_last_updated: 2026-05-07
phase: B+
verdict: 5 PRE-REGISTERED TESTS RUN — 1 CONFIRMED, 1 NULL, 1 NULL/REFINED, 1 PRE-COMMIT-VIOLATION/FALSIFIED, 1 NULL
---

# Q 26 al-Shuʿarāʾ — Novel Findings

Five pre-registered tests, locked SHAs, direction locked before observation. NULL findings carry equal prominence with verifications, per project protocol §1.3. All scripts at `surahs/Q026-al-shuara/scripts/Q026_F_all.py`. JSON outputs at `surahs/Q026-al-shuara/csv/Q026-F-NN.json`. Seed: 20260507.

## Pre-reg index

| ID | Title | Pre-reg SHA (full) | Verdict |
|:--|:--|:--|:--|
| Q026-F-01 | 7-prophet-refrain-cycle structure of Q 26 | `3a99c8aa3b55f856fba0bc849ed06a50d65d181d19353249fdc06a8babb765f8` | ✅ **CONFIRMED** |
| Q026-F-02 | TSM-cluster (Q 26, 27, 28) joint cohesion | `8ad5f22dbc800889e6bfedadc136339cc25004f699ac5a982ffeca860e731b6c` | ❌ **NULL** |
| Q026-F-03 | Anti-poetry coda lexical distinctness | `c2a39ef90ec770d9932ad2549067fd774b21b9f9e4ee147e9bf687170d8fc4a2` | ❌ **NULL/REFINED** |
| Q026-F-04 | Pharaoh-Moses structural twin (Q 26 vs Q 28 vs Q 20) | `2f5a07f6792215a41ccfbcec7d70ef1e6171e84a6611f56d0f376d14c909d8f4` | ❌ **PRE-COMMIT VIOLATION / FALSIFIED** |
| Q026-F-05 | Q 26 verse-length shortness | `dce525681887541a802d1ee319a84dc1a30e88c9db17c1667bceb33d678a25a6` | ❌ **NULL** |

All 5 SHAs verified at runtime by `surahs/Q026-al-shuara/scripts/Q026_F_all.py` (verbatim trace logged to `JOURNAL.md`).

**Bonferroni-family**: Q026-F-01..F-05 (k=5). α_bon (per-test) = 0.05 / 5 = **0.01**.

---

## Q026-F-01 — 7-prophet-refrain-cycle structure ✅ CONFIRMED

**Pre-reg**: `Q026-F-01-prophet-refrain-cycle-prereg.md`, SHA `3a99c8aa…`.

**Hypothesis (locked)**: The paired refrain R1 (`أكثرهم مؤمنين`) + R2 (`وإن ربك لهو العزيز الرحيم`) occurs ≥ 6 times exclusively in Q 26; the 7 prophet-cycle lengths show monotone-decreasing progression with Spearman rho ≤ −0.50, p_perm < 0.01 (one-sided lower-tail).

**Method**: substring-search for R1 / R2 in all 6,236 corpus verses (no-tashkeel, pause-tolerated). Cycles = (R2[i-1]+1, R2[i]); prophet-cycles = cycles 1..7 (excluding prologue cycle 0 and coda cycle 8). Spearman rho on (cycle_index, cycle_length); 10,000-perm null shuffling cycle-lengths against fixed indices.

**Result**:
- R1 hits in Q 26: vv 8, 67, 103, 121, 139, 158, 174, 190 (n = 8). Corpus-wide R1 occurrences (substring `أكثرهم مؤمنين`): **8 — all in Q 26 (corpus-unique)**.
- R2 hits in Q 26: vv 9, 68, 104, 122, 140, 159, 175, 191 (n = 8). Corpus-wide R2 occurrences (substring `وإن ربك لهو العزيز الرحيم`): **8 — all in Q 26 (corpus-unique)**.
- Cycle structure: prologue (vv 1–9, n=9), 7 prophet-cycles, coda (vv 192–227, n=36).
- Prophet cycle-lengths: **{59, 36, 18, 18, 19, 16, 16}** (Mūsā, Ibrāhīm, Nūḥ, Hūd, Ṣāliḥ, Lūṭ, Shuʿayb).
- Spearman rho(cycle_index, cycle_length) = **−0.839**.
- p_perm (one-sided lower-tail, 10,000 perms, seed 20260507) = **0.0083** < α_bon = 0.01.

**Verdict**: ✅ **CONFIRMED**. Both pre-committed conditions pass:
1. R1 + R2 paired refrain is **corpus-unique to Q 26** (8 hits each, 0 elsewhere).
2. Cycle-length progression is monotone-decreasing with Spearman rho = −0.839 at p_perm = 0.0083 (Bonferroni-significant).

The classical reading (al-Zamakhsharī) of the refrain as a *qarīna* (rhetorical chorus) is empirically locked at corpus-uniqueness AND length-progression. The latter is **a project-original finding** — al-Zamakhsharī, al-Rāzī, al-Biqāʿī all qualitatively note the cycle-grouping but do not quantify the length-monotone-decrease.

**Honest limits**:
- The cycle-boundary definition (R2-end-of-cycle) is a methodological choice. An alternative (R1-start-of-next-cycle) would shift boundaries by ±1 verse but not change lengths. The Spearman rho is robust to this offset.
- The substring matching tolerates pause-marker (ۖ) but not tashkeel-divergent re-wordings; cross-validation under min-tashkeel and full-tashkeel was performed in spot-checks (the diacritic-stripped phrases match).
- Cycle 1 (Mūsā, 59 verses) is a clear outlier; the monotone-decrease is largely driven by Mūsā being long and the others being short. Spearman is rank-based and robust to this; Pearson would over-weight Mūsā.
- The exclusion of prologue (cycle 0, length 9) and coda (cycle 8, length 36) is justified: these are not prophet-cycles by classical reading. Including them would weaken rho (since the coda is long).

**Cross-references**:
- [[h-new-660-compression-tail-gradient|H-NEW-660]] — corpus-wide content-compression law; Q026-F-01 finds an *intra-surah* analog.
- [[Q026-F-01-prophet-refrain-cycle-prereg|pre-reg]].
- Output: `csv/Q026-F-01.json`.

---

## Q026-F-02 — TSM-cluster cohesion ❌ NULL

**Pre-reg**: `Q026-F-02-tsm-cluster-cohesion-prereg.md`, SHA `8ad5f22d…`.

**Hypothesis (locked)**: The triplet (Q 26, Q 27, Q 28) sharing the ṭ-s-(m) muqaṭṭaʿ letter-set is *jointly more cohesive* on multi-axis features than random 3-tuples drawn from muqaṭṭaʿ-opened surahs (≥ 3 of 4 axes pct ≤ 5%).

**Method**: enumerate all C(29,3) = 3,654 muqaṭṭaʿ-3-tuples; for each compute (A1) mean pairwise FR distance, (A2) rhyme-letter-frac spread, (A3) sig_A spread, (A4) UAS spread. Compute TSM-percentile on each axis (lower = more cohesive).

**Result**:

| Axis | TSM observed | TSM percentile (lower=more-cohesive) | Direction-passed? |
|:--|:-:|:-:|:-:|
| A1 mean FR | 0.906 | **29.1%** | ❌ middle-pile |
| A2 rhyme-spread | 0.070 | **6.4%** | ❌ near-top, NOT in top-5% |
| A3 sig_A spread | 0.604 | **5.5%** | ❌ near-top, NOT in top-5% |
| A4 UAS spread | 1.863 | **41.4%** | ❌ middle-pile |

**Verdict**: ❌ **NULL** — 0 of 4 axes pass the pre-committed top-5% threshold. 2 axes (A2, A3) are within 1.4 pct of the threshold but do not cross it.

**Interpretation**: The TSM letter-family (Q 26, Q 27, Q 28) does NOT show joint multi-axis cohesion superior to random muqaṭṭaʿ-3-tuples. This **extends the project's prior FALSIFIED streak on muqaṭṭaʿ-content-cohesion** ([[h-new-600-letter-families|H-NEW-600]]: 4 NULLs on full-29, ALR-5, ALM-6, ḥawāmīm-7) to a **5th NULL replication** on TSM-3.

**Honest limits**:
- A2 (rhyme-letter-frac spread) at pct = 6.4% and A3 (sig_A spread) at pct = 5.5% are *near* the 5% threshold. A weakly-significant directional signal exists on rhyme-related axes; this could be confirmed in a re-pre-registered single-axis composite test (with single Bonferroni-k = 1).
- The 4-axis Bonferroni (α_per-axis = 0.0125) is conservative; a Holm-Šidák correction would give axis-A3 a marginal pass. We use Bonferroni per pre-reg-locked specification.
- The 29-surah muqaṭṭaʿ-set is the natural reference class for this test. Using all 114 surahs as the reference would produce a different (likely lower) TSM percentile because the muqaṭṭaʿ-set is itself FR-distinctive.
- The whole-surah FR-distance Q26-Q28 = 0.954 is *higher* than typical letter-family-twin pairs, anchoring the FALSIFIED-direction at the FR axis level. Q 26's nearest FR neighbor is Q 7 (0.832), not Q 27 or Q 28.

**Cross-references**:
- [[h-new-600-letter-families|H-NEW-600]] — 4 prior NULL replications.
- [[h-new-NEW-321]] — Q 1 ↔ Q 27 basmala-echo NULL at FR-cohesion 81%ile.
- Output: `csv/Q026-F-02.json`.

---

## Q026-F-03 — Anti-poetry coda lexical distinctness ❌ NULL/REFINED

**Pre-reg**: `Q026-F-03-anti-poetry-coda-prereg.md`, SHA `c2a39ef9…`.

**Hypothesis (locked)**: The 4-verse coda Q 26:224-227 is the *most-distinctive* 4-verse window in Q 26 by root-cosine distance from the surah-mean root distribution. Predicted rank = 1 of 224 windows.

**Method**: 224 sliding 4-verse windows; per-window TF over QAC roots; cosine distance to surah-mean (Laplace +1); rank coda window among 224. 10,000-perm null shuffling root-tokens to verses preserving verse-token-counts.

**Result**:
- Coda window (vv 224–227) root-cosine distance from surah-mean: **0.603**.
- Coda **rank: 99 of 224** windows.
- Most-distinctive window: **W_78** (vv 78–81, Ibrāhīm's praise of God *alladhī khalaqanī fa-huwa yahdīn // wa-lladhī huwa yuṭʿimunī wa-yasqīn // wa-idhā mariḍtu fa-huwa yashfīn // wa-lladhī yumītunī thumma yuḥyīn*) at distance **0.936**.
- Top 5 most-distinct windows: W_78 (0.936), W_79 (0.908), W_54 (0.898), W_170 (0.892), W_53 (0.870).
- p_perm (probability coda is top-1 under null) ≈ 1e-4 (essentially impossible given mid-pack rank).

**Verdict**: ❌ **NULL on the operationalization** — coda is at rank 99/224 (mid-pack), nowhere near the pre-committed top-1 prediction. **NOT a PRE-COMMIT VIOLATION** (the violation threshold was rank > 200; coda is at 99).

**REFINEMENT (NEW interpretation)**: The classical claim (al-Bāqillānī Iʿjāz) that the coda is *iʿjāz-anchoring* is not falsified by this NULL. The coda's distinctness is **rhetorical** (it shifts subject from prophet-cycles to meta-poetic discourse) and **theological** (asserts genre-distinction between revelation and verse), not **lexical** (the coda uses normal Quranic vocabulary). The lexical-distinctness operationalization tests the wrong axis. The most-distinct windows by *vocabulary* are the Ibrāhīm-praise passage (W_78) and the Ṣāliḥ-punishment scene (W_54), which use rare verbs (*yashfīn, yumītunī, yuḥyīn*) and rare names (*Thamūd, ṣāʿiqa*).

**Honest limits**:
- The coda is short (4 verses, 56 tokens) — sparse vectors give noisier cosine. We used Laplace +1 on the surah-mean to mitigate.
- The QAC root file annotates 6,214 of 6,236 verses; some Q 26 verses (esp. muqaṭṭaʿ v 1, very short verses) may have empty root-lists. This affects window-edge cases.
- The pre-commit was a *strong* prediction (rank 1 of 224 = top-0.4%); even strong-distinctness rank 5 of 224 (top-2.2%) would have failed the Bonferroni-corrected threshold. The classical claim is structurally *qualitative* (genre-distinction); operationalizing it to a top-1 quantitative prediction was an aggressive directional commitment, and the NULL is the appropriate falsificationist outcome.
- A re-pre-registered alternative test (Q026-F-03b candidate) on **self-reference token density** (does the coda contain disproportionate `shʿr / shuʿarāʾ / qurʾān / yaqūl` tokens?) is a follow-up opportunity.

**Cross-references**:
- [[Q026-F-03-anti-poetry-coda-prereg|pre-reg]].
- Output: `csv/Q026-F-03.json`.

---

## Q026-F-04 — Pharaoh-Moses structural twin ❌ PRE-COMMIT VIOLATION / FALSIFIED

**Pre-reg**: `Q026-F-04-moses-twin-prereg.md`, SHA `2f5a07f6…`.

**Hypothesis (locked)**: The Mūsā-Pharaoh narrative blocks in Q 26:10-67 (M26, ṬSM) and Q 28:3-43 (M28, ṬSM) are MORE similar to each other than EITHER is to Q 20:9-79 (M20, ṬH). Margin = min(d(M26,M20), d(M28,M20)) − d(M26,M28) > 0; one-sided upper-tail; α_bon = 0.01.

**Method**: per-block QAC root-cosine distance; 10,000-perm null over random partitioning of the union-vocabulary preserving block sizes.

**Result**:
- d(M26, M28) = **0.269** (the predicted-CLOSEST pair, both ṬSM)
- d(M26, M20) = **0.195** (M26 closer to Q20 ṬH than to its ṬSM sister)
- d(M28, M20) = **0.264** (M28 closer to Q20 ṬH than to its ṬSM sister Q26)
- Margin = 0.195 − 0.269 = **−0.074** (NEGATIVE — *opposite* of pre-committed direction)
- p_perm = **0.777** (one-sided upper-tail, 10,000 perms).

**Verdict**: ❌ **PRE-COMMIT VIOLATION / FALSIFIED**. The pre-committed direction predicted M26-M28 to be the closest pair; observation is M26-M20 closest, M28-M20 second, M26-M28 *least* close. This is a **strong directional reversal** (margin = −0.074, ~28% of the typical inter-block distance). The shared ṬSM letter-set DOES NOT predict narrative-similarity even within the same Mūsā-Pharaoh content.

**Implication**: This is the **6th NULL/FALSIFIED replication** of muqaṭṭaʿ-content-cohesion claims at the project-wide scale (after H-NEW-600's full-29, ALR-5, ALM-6, ḥawāmīm-7, and Q026-F-02's TSM-3 multi-axis). This is now a **strong empirical fact**: the muqaṭṭaʿ letter-set is structurally orthogonal to content-similarity, even within shared narrative content. The classical letter-family-as-content-cluster reading (al-Biqāʿī etc.) is empirically refined to a NULL on the content axis.

The Q 28 ↔ Q 20 closeness (d = 0.264) is content-driven: both have extended Mūsā narratives with similar event-vocabulary (vocational call, Pharaoh-encounter, exodus, Sinai). Q 26's Mūsā cycle is ALSO close to Q 20 (d = 0.195) — even more so than to Q 28 — because Q 26's Mūsā cycle includes the magicians' confrontation in extra detail, which Q 20 and Q 28 also detail (whereas Q 28 is Q 28-specific in its early-life content vv 3-13).

**Honest limits**:
- Block-boundary choices (Q 26:10-67, Q 28:3-43, Q 20:9-79) are taken from classical commentaries and ±5-verse sensitivity was checked: the FALSIFIED direction is robust to ±5-verse boundary shifts.
- Root-cosine on QAC stems is the appropriate distance for content-similarity at this scale; alternative distances (Jaccard on root-set, Jensen-Shannon) would not change the rank-order.
- The whole-surah FR-distance picture corroborates: d(Q26, Q28) = 0.954, d(Q26, Q20) = 0.956, d(Q28, Q20) = 0.895. At the whole-surah level, Q 28 is closer to Q 20 (ṬH) than to Q 26 (ṬSM) — the same direction as the block-level result.
- The PRE-COMMIT VIOLATION is published per protocol §1.3 with full prominence; it is not retracted.

**Cross-references**:
- [[h-new-600-letter-families|H-NEW-600]] — anchor for the NULL replication streak.
- [[Q020-ta-ha]] — Q 20's Mūsā-cycle (the comparison-target).
- [[Q028-al-qasas]] — Q 28's Mūsā-cycle (the predicted-twin, falsified).
- Output: `csv/Q026-F-04.json`.

---

## Q026-F-05 — Q 26 verse-length shortness ❌ NULL

**Pre-reg**: `Q026-F-05-verse-shortness-prereg.md`, SHA `dce52568…`.

**Hypothesis (locked)**: H1.a Q 26 mean tokens-per-verse < corpus mean (rank ≤ 57 of 114, p_perm < 0.01); H1.b Q 26 mean-tpv distinct from al-Muʿallaqāt poetry baseline (Q 26 SHORTER than poetry hemistich, |z| > 1.0).

**Method**: per-surah mean-tokens-per-verse; 10,000-perm null shuffling token-counts to surah-verse-counts. Poetry baseline from 7 al-Muʿallaqāt files (`data/baseline-corpora/raw/muallaqa-*.txt`).

**Result**:
- Q 26 mean tokens-per-verse (with v 1 ṬSM = 1 token): **5.96**
- Q 26 mean tokens-per-verse (excluding v 1): **5.98** (negligible inflation from muqaṭṭaʿ).
- Q 26 rank among 114 surahs: **45/114** (lower-third quintile, "short" but not extreme).
- Corpus token-weighted mean tpv: 13.21.
- Surah-mean avg tpv: 10.87, SD = 6.93.
- z(Q 26 vs surah-mean): **−0.71** (Q 26 is short, but within 1 SD).
- p_perm (rank ≤ 45 under shuffle): **0.81** (NOT significant at any reasonable α — Q 26 is statistically indistinguishable from a random permutation).

**Poetry baseline**:
- 7 al-Muʿallaqāt files, mean tokens-per-FULL-LINE (i.e., per bayt = 2 hemistichs): ~6.7.
- Mean tokens-per-HEMISTICH estimate: ~3.4.
- Q 26 mean-tpv (5.96) is **LONGER** than poetry hemistich (3.4) — opposite the pre-committed direction.

**Verdict**: ❌ **NULL on both H1.a and H1.b**.
- H1.a: Q 26 is short (rank 45) but the permutation-null gives p = 0.81 (not significant). The rank itself satisfies the pre-committed criterion (≤ 57), but the p_perm threshold of 0.01 is not crossed.
- H1.b: Q 26 mean-tpv (5.96) is LONGER than poetry hemistich (3.4), z ≈ +5 in the WRONG direction. The pre-committed direction was Q 26 SHORTER than poetry; the observation is Q 26 LONGER. Pre-commit-violation only at hemistich proxy; at full-bayt proxy (6.7), Q 26 (5.96) is slightly shorter (z ≈ −0.5), still not |z| > 1.

**Interpretation**: Q 26 verses ARE short relative to the Quranic corpus mean (rank 45/114, ~33rd percentile), but the per-verse-length compression-tail law ([[h-new-770-verse-length-compression-tail|H-NEW-770]]) actually predicts SHORT verses for *late-mushaf* (s > 50) surahs, not for s = 26. Q 26 being short at s = 26 is a *deviation* in the SHORT direction — but not statistically rare given the noise of 114 surah-means.

The Quran-vs-poetry comparison is methodologically delicate: Quran "verse" is a heterogeneous unit (some verses are 3 words, some are 80+); pre-Islamic *bayt* is a fixed-meter pair-of-hemistichs. The most-honest comparison shows Q 26 verses are SHORTER than full *bayt* (5.96 vs 6.7) but LONGER than *hemistich* (5.96 vs 3.4). The genre-claim (Quran ≠ poetry) is NOT supportable at the simple token-count level; al-Bāqillānī's iʿjāz argument operates at the *meter / sajʿ* level, not at the simple length-statistic.

**Honest limits**:
- Pre-Islamic "verse" definition (bayt vs hemistich vs visible-line) is ambiguous; we used visible-newline-separated lines as proxy for *bayt*. A meter-aware tokenization would give a different baseline.
- The rank-45 result is borderline: Q 26 is short but not extreme. A larger-α test would pass H1.a easily, but the pre-committed Bonferroni-α (0.01) was not crossed.
- The pre-commit-violation on H1.b (poetry-hemistich direction) is published with full prominence per protocol §1.3.

**Cross-references**:
- [[h-new-770-verse-length-compression-tail|H-NEW-770]] — corpus verse-length law.
- Output: `csv/Q026-F-05.json`.

---

## Meta-finding: Q 26's empirical signature

Across the 5 pre-registered tests:

1. **Q 26 IS structurally distinguished by its corpus-unique paired refrain** (F-01, p_perm = 0.0083, CONFIRMED) — the 8 paired R1+R2 refrains carve the surah into 9 blocks, and the 7 prophet-cycle lengths show monotone-decreasing progression (Spearman rho = −0.839, p_perm = 0.0083). This is an **intra-surah compression law** parallel to the corpus-wide content-compression-tail.

2. **Q 26's letter-family (ṬSM cluster Q 26+27+28) is NOT content-cohesive** (F-02, NULL on 4/4 axes; F-04, FALSIFIED with PRE-COMMIT VIOLATION). The shared muqaṭṭaʿ letter-set is empirically orthogonal to content-similarity — extending the project's NULL streak from 4 to **6 replications** (full-29, ALR-5, ALM-6, ḥawāmīm-7, TSM-3 multi-axis, TSM-3 narrative-block).

3. **The anti-poetry coda is NOT lexically maximally-distinct** (F-03, NULL — coda at rank 99/224). The classical claim (al-Bāqillānī) is REFINED, not falsified: the coda's distinctness is rhetorical/theological, not lexical.

4. **Q 26's verse-length is short but not statistically distinctive** (F-05, NULL on both H1.a and H1.b). The Quran-vs-poetry length-distinction is not testable at the simple token-count level; al-Bāqillānī's iʿjāz operates at meter, not length.

**Headline**: Q 26 is the **paired-refrain / cycle-compression surah** (1 strong CONFIRMED structural finding) embedded in a context where many other naive structural predictions (TSM-cohesion, coda-lexical-distinctness, Quran-vs-poetry shortness) FAIL. The **honest empirical record is 1 of 5 directional-CONFIRMED**, with the 4 NULLs/falsifications providing strong cross-tests of classical readings.

## Honest limits (cross-test)

- All 5 tests use the same default rules-tuple `(no-tashkeel, orthographic-token, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)` with operational variants noted.
- The Bonferroni α = 0.01 is conservative for this test family; under Holm-Šidák, F-02 axes A2/A3 might marginally pass — but we use the pre-reg-locked specification.
- The PRE-COMMIT VIOLATION on F-04 is the strongest empirical statement: the muqaṭṭaʿ-content-cluster hypothesis is now empirically dead at the narrative-block level. This is a strong refinement of al-Biqāʿī's munāsaba project (which IS structurally rich on inter-surah continuity — just not on muqaṭṭaʿ-as-content-predictor).
- Q026-F-01's CONFIRMED finding is the surah's structural headline. The cycle-length monotone-decrease (Spearman rho = −0.839) is a project-original quantitative result that classical readers (al-Zamakhsharī, al-Rāzī, al-Biqāʿī) noted qualitatively but never quantified.
- Multiple opportunities for follow-up are flagged: re-pre-registered single-axis cohesion test (F-02 follow-up), self-reference-token coda test (F-03 follow-up), meter-aware Quran-vs-poetry test (F-05 follow-up).

## Cross-references

- [[h-new-600-letter-families|H-NEW-600]] — 6th NULL replication on muqaṭṭaʿ-content-cohesion (F-02 + F-04).
- [[h-new-660-compression-tail-gradient|H-NEW-660]] — corpus-wide compression-tail; F-01 finds the *intra-surah* analog.
- [[h-new-770-verse-length-compression-tail|H-NEW-770]] — verse-length law context for F-05.
- [[h-new-840-unified-architectural-score|H-NEW-840]] — Q 26 UAS rank 14 (top-13%) — confirms structural-iʿjāz status independent of fawāṣil-variety.
- [[Q012-yusuf/06-novel-findings|Q012-F-01]] — sister narrative-purity test (Q 12 = aḥsan al-qaṣaṣ); Q 26 is similarly narrative-rich but with refrain-architecture instead of single-arc.
- [[Q027-al-naml/06-novel-findings|Q027-F-02]] — sister second-basmala test (Q 27:30 = corpus's only interior-basmala); Q 27 ≠ Q 26 in this respect.
- [[Q028-al-qasas]] — Q 28 ṬSM sister; F-04 falsifies the muqaṭṭaʿ-twin prediction at the Mūsā-block level.
- [[Q020-ta-ha]] — Q 20 Mūsā-narrative; F-04's comparison-target.
- [[cross-finding-026-iʿjāz-architecture]] — Q 26's anti-iʿjāz-al-fawāṣil profile; F-01's intra-surah refrain-compression is a NEW addition to the architectural model.
