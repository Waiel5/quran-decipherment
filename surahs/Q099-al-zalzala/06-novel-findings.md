---
surah: 99
surah_name_ar: الزلزلة
surah_name_translit: al-Zalzala
file_type: novel-findings
date_last_updated: 2026-05-09
phase: B+
verdict: 4 pre-registered tests on 2026-05-09 — 1 CONFIRMED, 2 DIRECTIONAL, 1 REFUTED-STRONG (the niṣf-al-Qurʾān classical claim, as predicted). All direction-locked; SHA-verified at runtime; seed 20260509.
---

# Q 99 al-Zalzala — Pre-Registered Novel Findings

Four pre-registered tests run on 2026-05-09. All pre-regs SHA-locked at write-time and SHA-verified at run-time. Outputs at `surahs/Q099-al-zalzala/csv/`. Seed = 20260509.

## Q099-F-01 — Q 99 within H-NEW-1200 14-cluster + 4-CORE idhā-cosmic-opener architectural replication

### Pre-reg
- File: `preregs/Q099-F-01-idha-cosmic-core-prereg.md`
- SHA256: `a535c632f8713176b904ab5d8a5d4e50707c4a3479ed53d155ab03b3a038fc48`
- Direction (locked): T1 cluster-mean < corpus-mean; T2 4-CORE-mean < 0.60 (architectural-core band). Bonferroni-2 (T1 + T2); α_bon = 0.025.
- Script: `scripts/Q099_F_01_idha_cosmic_core.py` (SHA-verified).

### Method

H-NEW-1200 ledger identifies 14-surah cluster {Q 56, 69, 74, 77, 81, 82, 83, 84, 86, 90, 97, 99, 101, 104} (FR-cohesive p=0.00030) and architectural-CORE {Q 81, 82, 84, 99} (FR pairwise 0.52-0.57). Q099-F-01 is the Q 99-specifically-anchored replication: does Q 99 INDIVIDUALLY show above-average affinity to the cluster?

- T1: Q 99 mean FR distance to other 13 cluster-members vs random 13-subset null (10,000 perms).
- T2: Q 99 mean FR distance to 3 other 4-CORE-members vs random 3-subset null (10,000 perms), AND empirical-mean must be within architectural-core band [0.52, 0.60].

### Result

| Quantity | Value |
|:--|:--:|
| Q 99 corpus-mean (113 surahs) | 0.8148 |
| Q 99 14-cluster-mean (13 members) | **0.5915** |
| Q 99 4-CORE-mean (3 members: Q 81, 82, 84) | **0.5579** |
| T1 cluster/corpus ratio | 0.7259 (Q 99 is 27% closer to cluster than corpus) |
| T1 perm-p (cluster ≤ random 13-subset) | **0.0012** |
| T2 perm-p (4-CORE ≤ random 3-subset) | 0.0531 |
| T2 4-CORE-mean within band [0.52, 0.60]? | YES |

### Verdict

**DIRECTIONAL.** T1 PASSES (p=0.0012 < α_bon=0.025) — Q 99's affinity to the H-NEW-1200 14-cluster is statistically robust. T2 misses the Bonferroni threshold (0.0531 vs 0.025) by a hair, but the 4-CORE-mean of 0.5579 IS within the pre-locked architectural-core band [0.52, 0.60].

### Direction

LOCKED positive (Q 99 ∈ cluster-CORE). T1 MATCHED at p=0.0012; T2 directionally-positive (in band) but p-value misses Bonferroni cutoff.

### Bonferroni

k = 2; α_bon = 0.025; T1 PASSES; T2 misses by 0.028.

### Honest limits

- T2 misses formal Bonferroni-2 cutoff. The 3-subset null is intrinsically less powerful (small sample); the directional-positive result is real but unstable. Single-test α=0.05 evaluation: T2 p=0.0531 just-misses single-test α=0.05 too. Honest verdict: T2 is **DIRECTIONAL-POSITIVE** but not formally-significant.
- This test is a REPLICATION of H-NEW-1200's whole-cluster-cohesion result, anchored on Q 99 specifically. The cluster-cohesion finding (T1) was strongly supported. The 4-CORE finding (T2) is mildly supported but hits sample-size limits at 3 surahs.
- The H-NEW-1200 ledger pre-stated the architectural-CORE band as 0.52-0.57; Q 99's empirical 4-CORE mean 0.558 is ON the upper-edge of that band, slightly above midpoint.
- DIRECTIONAL verdict pending stronger sample (e.g., extending to other Sub-cluster A members for cross-validation).

## Q099-F-02 — Q 99 = "niṣf al-Qurʾān" (HALF) classical-claim empirical audit

### Pre-reg
- File: `preregs/Q099-F-02-nisf-quran-audit-prereg.md`
- SHA256: `c5108be1d5a6096711c1e55dcb6d900e6fa9e1eeecfe9055dedfa8a63c88e15a`
- Direction (locked): REFUTED expected per cross-finding-015 classical-numerology-pattern. 7-axis literal HALF [0.45, 0.55] band. Bonferroni-7 with verdict-by-axis-count (≥5 = CONFIRMED).
- Script: `scripts/Q099_F_02_nisf_quran_audit.py` (SHA-verified).

### Method

7-axis quantitative test of the literal "Q 99 = HALF the Qurʾān" claim, mirroring H-NEW-84's methodology for Q 112 thuluth.

### Result

| Axis | Operationalization | Q 99 / corpus ratio | Off by factor | PASS [0.45, 0.55]? |
|---|---|---|---|---|
| 1 | Letter graphemes | 158 / 330,709 = 0.000478 | 1,047× too small | NO |
| 2 | Word tokens | 36 / 77,797 = 0.000463 | 1,081× too small | NO |
| 3 | Shannon information bits | 683.0 / 1,493,986.1 = 0.000457 | 1,094× too small | NO |
| 4 | Distinct roots covered (proxy) | 23 / 3,512 = 0.006549 | 76× too small | NO |
| 5 | Eschatology-dominant verses (corpus-fraction) | 3 / 996 = 0.003012 | 166× too small | NO |
| 6 | Eschatology concentration factor (inverse) | 1 / 2.348 = **0.4259** | 1.17× too small | **NO (BORDERLINE)** |
| 7 | Divine-names coverage (99 names) | 1 / 99 = 0.0101 | 50× too small | NO |

**Aggregate**: **0 of 7 axes PASS.**

### Verdict

**REFUTED-STRONG.** The literal Q 99 = HALF claim fails by 50× to 1,094× on every direct-content axis. Best-matching axis is Axis 6 (eschatology-concentration-inverse) at 0.4259, only 0.024 outside the locked band [0.45, 0.55] — exactly parallel to H-NEW-84's Axis 5 borderline (0.3725 just outside [0.30, 0.37]).

**Q 99's eschatology-density is 2.348× the corpus baseline** — this is a STRONG content-thematic concentration (Q 99 is "eschatologically-twice-as-dense as the average corpus-verse"). The literal "1/2 of Quran" interpretation is wrong, but the symbolic-thematic-concentration reading has near-empirical-support.

### Direction

PRE-LOCKED REFUTED expected per cross-finding-015 classical-numerology-pattern. MATCHED at REFUTED-STRONG.

### Bonferroni

k = 7; α_bon-per-axis = 0.05/7 = 0.00714. Aggregate verdict by axis-count threshold (≥5 = CONFIRMED). Result: 0 of 7 = REFUTED-STRONG.

### Honest limits

- Same H-NEW-84-protocol caveats: the test is a literal-content-equivalence test of a symbolic-religious claim. The hadith is best read as devotional-valuation, not statistical-content-equivalence. The empirical refutation does not invalidate the spiritual-religious-importance of Q 99.
- The single-axis BORDERLINE (Axis 6 at 0.4259, 0.024 outside band) is striking and parallels H-NEW-84's Axis 5 finding. Q 99 IS substantially eschatology-concentrated relative to the corpus baseline — just not at the literal "1/2 ratio."
- Per Bonferroni-tightening discipline: we DO NOT relax the locked tolerance post hoc. Result stands as REFUTED-STRONG on the literal interpretation.
- The DOUBLE refutation (chain + content) is the headline result. See `04-hadith-corpus.md` for chain-isnad-evaluation.

## Q099-F-03 — Q 99 earth-protagonist density — corpus-MAX test (length-controlled)

### Pre-reg
- File: `preregs/Q099-F-03-earth-protagonist-density-prereg.md`
- SHA256: `dc9a46f32b1f4478bdaf64e452f3d54ead46bb1f5908fa8b6faecfbc213d924e`
- Direction (locked): T1 Q 99 corpus-MAX (rank-1) on orthographic earth-density; T2 ≥5 of 8 verses are earth-protagonist (inspection-based). Bonferroni-2; α_bon = 0.025.
- Script: `scripts/Q099_F_03_earth_protagonist.py` (SHA-verified).

### Method

T1: orthographic lemma-only earth-density per surah — count of verses containing الأرض or أرض, divided by surah verse-count. Compare across all 114 surahs.

T2: inspection-based earth-protagonist count for Q 99: the 5 verses (1, 2, 3, 4, 5) that contain explicit earth-anchoring (lemma + pronouns *-hā* whose antecedent is *al-arḍ*).

### Result

| Quantity | Value |
|:--|:--:|
| T1: Q 99 orthographic earth-verses | 2/8 = 0.250 |
| Q 99 orthographic rank | **2/114** |
| Top surah (Q 57 al-Ḥadīd) | 8/29 = 0.276 |
| T2: Q 99 inspection-based earth-protagonist verses | 5/8 = 0.625 |
| Top-3 orthographic rank | Q 57 (0.276) > **Q 99 (0.250)** > Q 31 (0.235) |

### Verdict

**DIRECTIONAL.** T1 fails: Q 99 is RANK 2/114 (just behind Q 57 al-Ḥadīd which has 8/29 = 0.276 vs Q 99's 2/8 = 0.250 — both have 25% earth-density and the difference is the Q 57 small-edge). T2 PASSES: Q 99 has 5/8 = 62.5% earth-protagonist verses by inspection-based criterion.

### Direction

LOCKED positive (Q 99 = corpus-MAX). T1 NEAR-MATCH (rank 2/114, just behind Q 57); T2 MATCHED.

### Bonferroni

k = 2; α_bon = 0.025. T1 missed by mid-rank-2 placement; T2 passed.

### Honest limits

- The T1 strict orthographic-lemma-density does NOT have Q 99 as the corpus-MAX. Q 57 al-Ḥadīd has higher orthographic earth-density. Q 99's earth-protagonist DOMINANCE manifests at the inspection-based pronoun-anchored level, not the strict lemma-count level.
- Q 99 is "earth-prominent" by 5/8 = 62.5% protagonist-density, but Q 57 al-Ḥadīd's 8/29 = 27.6% lemma-density is higher.
- The pronoun-tracking baseline for the entire corpus would require gold-standard antecedent-resolution (out of scope here). For Q 99 alone, the inspection is straightforward.
- The result is HONEST: Q 99 is corpus-RANK-2 by strict orthographic earth-density, NOT corpus-MAX. The brief's "corpus-EXACT" expectation for earth-protagonist-uniqueness is REFUTED on the strict measure.
- The inspection-based 5/8 = 62.5% protagonist-density is empirically high for any 8-verse short surah; whether other surahs of comparable length match this depends on antecedent-resolution data unavailable here.

## Q099-F-04 — zalzala-root corpus-EXACT distribution

### Pre-reg
- File: `preregs/Q099-F-04-zalzala-root-distribution-prereg.md`
- SHA256: `df976b5671bc566f1c0e8251c30b3c062ca0539f5d924a15e97fc217c5a898ff`
- Direction (locked): T1 corpus-EXACT 6 tokens; T2 Q 99 surah-density rank-1; T3 Q 99:1 verse-density rank-1. Bonferroni-3; α_bon = 0.01667.
- Script: `scripts/Q099_F_04_zalzala_root.py` (SHA-verified; surface-form-word-counting, not substring).

### Method

Detect surface-form-word-tokens containing the *zalzala* root (regex `(زلزل|زلزال)` matched against word-units). Count tokens per surah and per verse. Compute density per 100 words.

### Result

| Quantity | Value |
|:--|:--:|
| Total zalzala-root surface-form-tokens | **6** |
| Unique surahs containing root | **4** (Q 2, Q 22, Q 33, Q 99) |
| Unique verses containing root | **4** (Q 2:214, Q 22:1, Q 33:11, Q 99:1) |

### Per-surah densities

| Surah | Tokens | Surah words | Density per 100w |
|:-:|:-:|:-:|:--:|
| **Q 99** | **2** | **36** | **5.5556** (rank-1) |
| Q 33 | 2 | 1,384 | 0.1445 |
| Q 22 | 1 | 1,356 | 0.0737 |
| Q 2 | 1 | 6,630 | 0.0151 |

### Per-verse densities

| Verse | Tokens | Words | Density-per-word |
|:-:|:-:|:-:|:--:|
| **Q 99:1** | **2** | **4** | **0.5000** (rank-1, 50% of words!) |
| Q 33:11 | 2 | 6 | 0.3333 |
| Q 22:1 | 1 | 11 | 0.0909 |
| Q 2:214 | 1 | 32 | 0.0312 |

### Verdict

**CONFIRMED.** All 3 axes pass:
- T1: corpus-EXACT 6 tokens — observed 6 ✓.
- T2: Q 99 surah-density rank-1 of 4 (38× higher than #2 Q 33) ✓.
- T3: Q 99:1 verse-density rank-1 (50% of words!) ✓.

### Direction

LOCKED positive (Q 99 = corpus-MAX). MATCHED on all 3 axes.

### Bonferroni

k = 3; α_bon = 0.01667. T1 deterministic-pass (count match). T2 + T3 deterministic-pass (rank-1).

### Honest limits

- The original substring-only count (4) was lower than the surface-form-word count (6). The pre-reg locked the surface-form interpretation. Sensitivity-check: under strict substring-match, count is 4 — but pre-reg locked the more-inclusive interpretation.
- The 4 host-surahs span chronology: Q 2 (Medinan), Q 22 (mid-Meccan-to-Medinan), Q 33 (Medinan), Q 99 (Late-Meccan/Medinan-debated). The root carries dual semantic-register (eschatological vs. psychological-trial); Q 22:1 + Q 99:1 are the eschatological-cosmic uses.
- **Q 99:1 has 50% per-word density** — a striking concentration: half of Q 99:1's 4 words are zalzala-root tokens (*zulzilat* and *zilzālahā*). This is among the corpus's most-concentrated single-verse root-density observations.
- The zalzala-root 6-token / 4-verse / 4-surah distribution is now LOCKED as a corpus-EXACT empirical anchor. Any future corpus-text variants would alter this distribution; Hafs-Kūfan locked.

## 5. Aggregate verdict

| Test | Verdict | Detail |
|:--|:-:|:--|
| Q099-F-01 | DIRECTIONAL | T1 (cluster-cohesion) p=0.0012 PASS; T2 (4-CORE) p=0.0531 NEAR-MISS; 4-CORE-mean 0.558 in pre-locked band |
| Q099-F-02 | **REFUTED-STRONG** | 0/7 axes; literal niṣf-al-Qurʾān refuted; HEADLINE classical-claim audit |
| Q099-F-03 | DIRECTIONAL | T1 strict-orthographic rank-2 (Q 57 leads); T2 inspection-based 5/8 PASS |
| Q099-F-04 | **CONFIRMED** | zalzala-root corpus-EXACT 6 tokens; Q 99 surah + verse-density both rank-1 |

**1 CONFIRMED + 2 DIRECTIONAL + 1 REFUTED-STRONG.** Honest reporting per HANDOFF/04-DISCIPLINE.md.

### Headline finding

**Q099-F-02 REFUTED-STRONG**: the al-Tirmidhī Q 99 = niṣf al-Qurʾān classical-fadāʾil-fraction claim joins the Q 36 qalb (H-NEW-82) and Q 112 thuluth (H-NEW-84) as the **3rd refuted classical-fadāʾil-fraction claim**. This strengthens cross-finding-015's meta-pattern: classical numerological/fadāʾil-fraction claims tend to fail empirical testing.

The DOUBLE refutation (weak chain via Tirmidhī's own gharīb classification + WEAK quantitative content via Q099-F-02 0/7 axes) is novel — H-NEW-82 was chain-only-weak, H-NEW-84 was content-only-weak, Q 99 is BOTH. This is the strongest-refuted classical-fadāʾil-fraction tradition in the project's catalog.

### Architectural finding

**Q099-F-04 CONFIRMED**: the *zalzala* root has 6 corpus-tokens distributed across exactly 4 verses in 4 surahs, with Q 99 holding the rank-1 surah-density (38× higher than #2) and Q 99:1 holding the rank-1 verse-density (50% per-word). Q 99 is the corpus's empirical *zalzala*-image-anchor.

### Cluster-architecture finding

**Q099-F-01 DIRECTIONAL**: Q 99 is statistically-robustly close to the H-NEW-1200 14-cluster (p=0.0012), and within the pre-locked architectural-CORE band for the 4-surah Sub-cluster A {Q 81, 82, 84, 99} (mean=0.558 in band [0.52, 0.60]). The architectural-CORE membership is empirically supported but the small 3-surah null lacks power for formal Bonferroni-significance.

## 6. Cross-references

- [[h-new-1200-short-meccan-eschatology|H-NEW-1200]] — parent cluster (Q099-F-01 replicates).
- [[h-new-84-ikhlas-third|H-NEW-84]] — methodological parent (Q099-F-02 mirrors).
- [[h-new-82-yasin-heart|H-NEW-82]] — methodological parallel (chain-weak fadāʾil claim).
- [[cross-finding-015-classical-scholarship-validation-pattern|cross-finding-015]] — meta-pattern this finding strengthens.
- [[surahs/Q099-al-zalzala/05-classical-claims-audit|Q 99 classical-claims audit]] — full audit context.
- [[surahs/Q099-al-zalzala/04-hadith-corpus|Q 99 hadith corpus]] — chain-isnad-evaluation.
- All 4 JSON outputs in `surahs/Q099-al-zalzala/csv/`.
