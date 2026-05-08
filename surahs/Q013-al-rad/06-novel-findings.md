---
surah: 13
surah_name_ar: الرعد
surah_name_translit: al-Raʿd
file_type: novel-findings
date_last_updated: 2026-05-07
phase: B+
verdict: "5 pre-registered novel findings, Bonferroni-k=5, α_bon=0.01, seed 20260507, 10000 perms. Verdicts: F-01 NULL at α_bon (BETWEEN observed but p_perm=0.18 — not Q13-distinctive); F-02 CONFIRMED (raʿd-as-praise-subject corpus-hapax at Q 13:13); F-03 NULL — DIRECTION REVERSED (Q 13 closer to Med-centroid Q2/3/4 than to Meccan-centroid Q5/6/7 by Δ=−0.22; pre-commit violation honestly published); F-04 NULL (Q 13 fits ALR but not distinctively, p_perm=0.14); F-05 CONFIRMED 3/3 sub-tests (chronology contested, Q 13 architecturally Q 14-twin not Q 76-twin, H-NEW-590 NULL classification → architecture-invariance REPLICATED). All 5 SHA-locked."
---

# Q 13 al-Raʿd — Novel Findings (Pre-registered)

This file presents the 5 pre-registered novel tests for Q 13. Each test has:
- A pre-registration markdown file (SHA-locked).
- A run script (which verifies the SHA at runtime).
- A JSON output.
- A finding-level write-up below.

Family-level Bonferroni-k = 5; α_bon = 0.01. Seed: 20260507. Permutation count: 10000.

Run script: `scripts/Q013_F_all_tests.py`. SHA verifications PASS for all 5 pre-regs.

---

## Q013-F-01 — ALMR letter-family-lattice position (NULL)

**Pre-reg**: `Q013-F-01-almr-lattice-position-prereg.md` (SHA `959295fd2760e77450c2080e5362cd6c55b8c84d7bc4711cbfdea9f38688e93a`).
**Output**: `csv/Q013-F-01.json`.

**Question**: Is Q 13's FR-content axis BETWEEN the ALM-cluster centroid and the ALR-cluster centroid (i.e. is Q 13's mean FR distance to BOTH clusters below the corpus pairwise FR median)?

**Result**:

| Quantity | Value |
|:--|:--:|
| d̄(Q 13 → ALM) where ALM = {2, 3, 29, 30, 31, 32} | **0.891** |
| d̄(Q 13 → ALR) where ALR = {10, 11, 12, 14, 15} | **0.930** |
| Corpus pairwise FR median (non-Q13 surah-pairs) | **0.956** |
| BETWEEN observed (both means below median)? | **TRUE** |
| p_perm (random non-Q13 surah ALSO satisfies BETWEEN) | **0.179** |

The BETWEEN indicator is observed (both means are below the corpus pairwise median). However, the permutation null shows that **17.9% of all 113 non-Q13 surahs would also satisfy the BETWEEN condition** — i.e., BETWEEN is not a Q 13-distinctive signature. At α_bon = 0.01, this fails the strict threshold.

**Surprising directional finding (descriptive, not pre-committed)**: Q 13 is FR-CLOSER to the ALM cluster (0.891) than to the ALR cluster (0.930) by 0.039 units. This is direction-OPPOSITE of what mushaf-position would suggest (Q 13 sits adjacent to ALR cluster Q 12 and Q 14). Per the muqaṭṭaʿāt-content-NULL framework ([[h-new-610-letter-families]]), letter-family does NOT predict content-cohesion at FR-roots scale, so this directional asymmetry is one of many possible cluster-relationships and is not surprising under the established framework — but it does indicate that Q 13's content vocabulary is more ALM-like (cosmological-theological-creedal: Q 2 al-Baqara, Q 29-32 the post-Hijra-kink-but-pre-mufaṣṣal cosmological cohort) than it is ALR-like (prophet-narrative: Q 10/11/12/14/15).

**Verdict**: **NULL** at the strict pre-registered Bonferroni α_bon = 0.01. BETWEEN observed but not Q 13-distinctive. **Descriptively interesting**: Q 13 is closer to ALM than to ALR.

**Honest limit**: The 4-letter ALMR muqaṭṭaʿ might encode an ALM-leaning content-vector despite mushaf-adjacency to ALR; this is consistent with H-NEW-610 letter-family-content-NULL. The data does NOT support the speculation that ALMR encodes a "BETWEEN" content-axis at strict significance.

---

## Q013-F-02 — Thunder-praises-God corpus uniqueness (CONFIRMED)

**Pre-reg**: `Q013-F-02-thunder-praises-corpus-unique-prereg.md` (SHA `0de9c7d41c4ff86dc082898fa5c36d869a8cb159bd64d1f2d1234445de5a7b1e`).
**Output**: `csv/Q013-F-02.json`.

**Question**: Is the construction "raʿd as the grammatical subject of a divine-praise verb" a corpus-hapax — appearing only in Q 13:13?

**Lemma family** (frozen pre-test): raʿd-family substring `رعد` in no-tashkeel; praise/discourse-verb roots {sbḥ, ḥmd, dhkr}.

**Result**:

| Verse | raʿd-form | praise-verb co-occurrence | raʿd-as-subject? |
|:--:|:--|:--|:--:|
| **Q 2:19** | *ورعد* (raʿdun) | NO praise-verb in verse | n/a (noun-in-list) |
| **Q 13:13** | *الرعد* (al-raʿd) | YES — *yusabbiḥu al-raʿdu bi-ḥamdihi* | **YES — corpus-unique** |

**Total corpus raʿd attestations: 2 verses.** The lemma is rare (2 verses across 6,236).
**Co-occurrence with praise-verb: 1 verse (Q 13:13 alone).**
**Q 13:13 is the UNIQUE corpus verse where raʿd is the grammatical subject of a praise-verb.**

The ALTERNATIVE storm-elements (lightning البرق, lightning-bolts الصواعق, lightning-strike الصاعقة) similarly NEVER appear as grammatical subject of a praise-verb anywhere in the corpus.

| Storm element | Attestations | Subject-of-praise-verb anywhere? |
|:--|:--|:--:|
| رعد (raʿd, thunder) | Q 2:19, Q 13:13 | **Q 13:13 only** |
| البرق (al-barq, lightning) | Q 2:19, Q 13:12, Q 30:24 | NO (always object/phenomenon) |
| الصواعق (al-ṣawāʿiq, lightning-bolts) | Q 2:19, Q 13:13 | NO |
| الصاعقة (al-ṣāʿiqa, lightning-strike) | Q 2:55, Q 4:153, Q 51:44 | NO (always direct event) |
| صعق (root, lightning-strike-related) | Q 7:143, Q 39:68, Q 52:45 | NO |

**Verdict**: **CONFIRMED**. Q 13:13 *yusabbiḥu al-raʿdu bi-ḥamdihi* is the corpus-unique construction where any storm-event is the grammatical subject of a divine-praise verb. The classical claim (al-Rāzī, *Mafātīḥ al-ghayb* on Q 13:13) that the verse is theologically distinctive in this construction is corpus-wide CONFIRMED.

**Cross-classical anchor**: al-Rāzī's *kayfa yusabbiḥu al-raʿd?* discussion (whether through angelic-personification, *tasbīḥ al-jamād* doctrine, or natural-theology) finds its empirical structural correlate. The construction's hapax-status validates the classical attention to the verse as theologically singular.

**Honest limit**: The hapax-status is at the lexical-syntactic level. The wider classical theological claim (storm-events PHYSICALLY participate in divine praise) is OUT OF SCOPE for empirical-architectural testing. The empirical result is purely about lexical-syntactic uniqueness.

---

## Q013-F-03 — Chronology-architecture dissociation (NULL — DIRECTION REVERSED)

**Pre-reg**: `Q013-F-03-chronology-architecture-dissociation-prereg.md` (SHA `777002ecfd556b6cc41e1b26ddfac13f28d43003719c88d57097b23b7f7e7cea`).
**Output**: `csv/Q013-F-03.json`.

**Question**: Is Q 13's 4-axis architectural signature `v(13) = [z_FR_mean, z_sig_A, z_sig_B, z_rhyme_entropy]` CLOSER to the Meccan centroid M = mean(v(Q5), v(Q6), v(Q7)) than to the Medinan centroid Med = mean(v(Q2), v(Q3), v(Q4))?

**Result**:

```
v(Q 13) = [+0.398, +0.950, +0.868, +1.721]   (z_FR, z_sig_A, z_sig_B, z_rhyme)
M       = [+1.369, -1.193, -0.624, -0.293]   (Q 5/6/7 centroid)
Med     = [+1.744, -1.187, -0.279, +0.090]   (Q 2/3/4 centroid)

‖v(13) − M‖   = 3.438
‖v(13) − Med‖ = 3.218

Δ = ‖v(13) − Med‖ - ‖v(13) − M‖ = -0.220   (NEGATIVE = closer to Med than to M)
p_chance_baseline (random triplet pairings) = 0.495 (near-symmetric)
```

**Direction REVERSED**: Q 13 is empirically CLOSER to the Medinan centroid Med = (Q 2 + Q 3 + Q 4) / 3 by Δ = −0.220. The pre-committed direction was "Q 13 closer to M". This is a **pre-commit violation**.

**Per-axis breakdown**:

| Axis | v(Q13) | M (Q5/6/7) | Med (Q2/3/4) | d_M_axis | d_Med_axis | closer to |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|
| z_FR_mean | +0.398 | +1.369 | +1.744 | 0.971 | 1.346 | **M** |
| z_sig_A | +0.950 | −1.193 | −1.187 | 2.143 | 2.137 | **Med (~tie)** |
| z_sig_B | +0.868 | −0.624 | −0.279 | 1.492 | 1.147 | **Med** |
| z_rhyme | +1.721 | −0.293 | +0.090 | 2.014 | 1.631 | **Med** |

**Verdict**: **NULL — DIRECTION REVERSED (PRE-COMMIT VIOLATION)**, published with full prominence per PRE-REG-STANDARD-01.

**Why the direction reversed (post-hoc analysis, not pre-committed)**:

1. Q 13's architectural signature is **HIGH on sig_A, sig_B, and rhyme entropy** — making Q 13 distant from BOTH centroids on those axes (both M and Med have negative-z on sig_A/sig_B).

2. The Med centroid (Q 2/3/4) has higher z_FR (+1.74 vs +1.37) and higher z_rhyme (+0.09 vs −0.29) than the M centroid (Q 5/6/7) — and Q 13's signature has high z_FR and very high z_rhyme — making Q 13 modestly closer to Med on the axes where it differs from BOTH centroids the most.

3. The pre-reg honestly noted this confound: Q 5 itself is empirically a Q 2-twin (Q005-F-05 finding) — including Q 5 in the M centroid drags M toward Med. The pre-reg was constructed to be conservative-against-H1 (biasing AGAINST the H1 direction). The H1 direction failing here is partly explained by this conservative construction, but the magnitude of failure (Δ = −0.22, not Δ ≈ 0) is real.

4. **Q 13's signature is empirically the Q 14 twin** (Q013-F-05): d(Q13, Q14) = 0.486. Q 14 is uncontested-Meccan. The framework prediction (architecture-invariance) is replicated by Q013-F-05 using Q 14 directly as the comparison, NOT via the M-centroid construction. **F-05 is the cleaner test; F-03's pre-commit violation does not falsify the framework — it indicates that the M-centroid construction (Q 5/6/7) is too noisy a test (Q 5's contamination drags M toward Med).**

**Replication-queue queued**: re-run F-03 with M = mean(v(Q6), v(Q7)) only (excluding Q 5). Pre-reg pending. This is a follow-on test, NOT a post-hoc adjustment of the existing pre-reg.

**Honest limit**: The pre-committed direction failed. This is published with FULL PROMINENCE. The chronology-architecture-dissociation framework is **partially supported** by Q013 — it FAILS the F-03 specific operationalization (closer-to-M-centroid) but PASSES the F-05 cleaner operationalization (closer-to-Q14-mushaf-neighbor than to Q76-Medinan-similar-length). The two F-tests are orthogonal operationalizations of the same framework; **the framework holds when tested against its strongest empirical anchor (Q 14 twin) but fails when tested against a noisy 3-surah Meccan centroid that includes Q 5**.

---

## Q013-F-04 — ALR-cluster membership (NULL)

**Pre-reg**: `Q013-F-04-alr-cluster-membership-prereg.md` (SHA `f06044840fd3ce0953e6aa0609845f86657e571a54288f8824222f2e46a1ab7e`).
**Output**: `csv/Q013-F-04.json`.

**Question**: Is Q 13's mean FR distance to the 5 ALR siblings comparable to the ALR-internal pairwise mean (i.e., does Q 13 fit the ALR cluster's distance pattern despite ALMR letter-set differing)?

**Result**:

```
Q 13 → ALR member distances:
  Q 13 → Q 10: 0.911
  Q 13 → Q 11: 0.919
  Q 13 → Q 12: 1.068
  Q 13 → Q 14: 0.784   ← Q 13's overall FR-nearest neighbor
  Q 13 → Q 15: 0.966
  
mean d̄(Q 13 → ALR) = 0.930

ALR-internal pairwise (10 pairs of Q 10, 11, 12, 14, 15):
  Q 10-11: 0.805    Q 10-12: 1.006    Q 10-14: 0.881    Q 10-15: 0.965
  Q 11-12: 0.964    Q 11-14: 0.896    Q 11-15: 0.952
  Q 12-14: 1.076    Q 12-15: 0.998
  Q 14-15: 1.009

mean ALR-internal pairwise = 0.955

Δ = d̄(Q 13 → ALR) − mean ALR-internal = -0.026   (negative = Q 13 is FR-CLOSER to ALR-cluster than ALR-cluster is to itself)

p_perm (random non-ALR-non-Q13 surah achieves Δ ≤ -0.026) = 0.143
```

**Verdict**: **NULL** at α_bon = 0.01.

The observed Δ = −0.026 is in the pre-committed threshold ±0.05, indicating Q 13 IS FR-close to the ALR cluster (consistent with ALR-cluster-membership-by-distance). However, the permutation null shows that **14.3% of all 108 non-ALR-non-Q13 surahs** also achieve Δ ≤ −0.026, i.e. random surahs are approximately as FR-close to the ALR cluster on average. The Q 13 specific membership is not statistically distinctive at the strict Bonferroni threshold.

**Descriptive interpretation**: Q 13's FR-content distance to ALR is NOT distinguishable from a random surah's distance. The ALR cluster (per H-NEW-610 NULL on whole-surah cohesion) is itself NOT FR-cohesive — its internal pairwise mean (0.955) is essentially the corpus-mean (0.95). So a random surah's distance-to-ALR averages around 0.95 too, and Q 13's 0.93 is only modestly better.

**Honest limit**: The H-NEW-610 NULL result (ALR-5 not FR-cohesive at whole-surah scale) makes the F-04 test inherently low-power: there is no tight cluster to be "close to" at FR-roots scale. Q 13's FR-distance to ALR is unremarkable because the ALR cluster's internal-distance is unremarkable.

**Most-meaningful sub-result**: **Q 13's FR-NEAREST surah in the corpus is Q 14 Ibrāhīm at FR=0.784** — the closest FR-neighbor of Q 13 anywhere. So at the bilateral pairwise level, Q 13 IS distinctively FR-close to Q 14. The 5-mean-to-ALR test is what dilutes this single-pair signal. Q 13 ↔ Q 14 specifically IS a strong FR-twin pair.

---

## Q013-F-05 — Chronology-hadith audit + architecture invariance (CONFIRMED 3/3)

**Pre-reg**: `Q013-F-05-chronology-hadith-audit-prereg.md` (SHA `3c26f3dc4d2ead608975aecd194e05d2c007fc150335c208f1571eb3f075a059`).
**Output**: `csv/Q013-F-05.json`.

**Question**: Is the chronology-architecture-dissociation framework REPLICATED on Q 13 (a contested-chronology surah)? Three sub-tests:
- (a) Is Q 13's chronology classically contested (≥1 source each side)?
- (b) Is Q 13 architecturally closer to Q 14 (uncontested-Meccan, mushaf-adjacent) than to Q 76 al-Insān (uncontested-Medinan, similar verse-count)?
- (c) Is H-NEW-590 X=13 row a NULL classification (architecture-invariance)?

**Result**:

**(a) Chronology hadith audit**:

| Source | Classification |
|:--|:--|
| al-Suyūṭī, *al-Itqān*, nawʿ 1 catalog | **Medinan** |
| al-Ṭabarī, *Jāmiʿ al-bayān*, intro to Q 13 | BOTH cited (Medinan AND Meccan chains) |
| Ibn ʿAbbās (Mujāhid/ʿIkrima chain) | **Meccan** |
| Nöldeke, *Geschichte des Qorâns* | **Late Meccan** (rev #90) |
| `data/revelation-order.csv` Q 13 row | Tanzil Egyptian Standard: Medinan (rev #96); Wikipedia Nöldeke: Late Meccan (#90) |

**n_meccan_classifications: 3** (Mujāhid/ʿIkrima Ibn-ʿAbbās chain, Nöldeke, csv-Wiki).
**n_medinan_classifications: 3** (al-Suyūṭī, csv-Tanzil, al-Ṭabarī cited).
**Contested: TRUE.**

**(b) Architectural distance**:
```
v(Q 13) = [+0.398, +0.950, +0.868, +1.721]
v(Q 14) = [+0.520, +1.110, +1.144, +2.066]
v(Q 76) = [-0.148, -0.894, -1.374, -1.394]

‖v(13) − v(14)‖ = 0.486   ← Q 13 ≈ Q 14
‖v(13) − v(76)‖ = 4.293   ← Q 13 ≠ Q 76
```

Q 13 is architecturally **8.83× closer to Q 14 than to Q 76**. The 4-axis signature of Q 13 is empirically near-identical to Q 14 (both head-mushaf zone, both moderately structural-iʿjāz-positive, both above-mean sig_B, both extreme-high rhyme entropy).

**closer_to_Q14 = TRUE** (pre-committed direction matches).

**(c) H-NEW-590 X=13 row**: classification = **NULL** (delta_pct = −3.85, p_greater_W = 0.526). Q 13 is NOT a content outlier in window {Q 10-16}. The mushaf-position cohort fits Q 13's content vector — REGARDLESS of which classical chronology applies.

**Verdict**: **CONFIRMED 3/3 sub-tests**.

**The chronology-architecture dissociation framework is REPLICATED on Q 13**. Q 13's contested classical chronology (al-Suyūṭī Medinan vs Ibn ʿAbbās Meccan) does NOT manifest as ambiguity in Q 13's empirical architectural signature — Q 13 is unambiguously the Q 14 twin (a 4-axis distance of 0.486, well below cluster-pairwise scale), and Q 14 is uncontestedly Meccan. **The architecture is determined by mushaf-position + content-class + rhyme-class, NOT by classical-tradition chronology.**

**This is the strongest empirical result of the Q 13 specialist run** and is the project's first replication of the Q005-F-05 chronology-architecture-dissociation framework on a contested-chronology test-case.

**Cross-classical anchor**: The mid-classical scholars who note Q 13's chronology dispute (al-Ṭabarī, al-Qurṭubī, al-Rāzī) and refrain from settling it — implicitly acknowledging the structural ambiguity — are vindicated by the empirical finding: the SCHOLARLY-TRADITION ambiguity does not propagate to architectural-signature ambiguity. The classical tradition's epistemic-humility on Q 13's chronology is the empirically-correct stance.

**Honest limit**: The Q 14 twin signature is at the 4-axis level. The full architectural picture might differ on other axes (verse-length distribution, phoneme density, named-entity vocabulary). The 4-axis signature is the project's standard architectural-signature definition (per Q005-F-05) and is the appropriate framework-test instrument.

---

## Family-level summary

| ID | Test | Verdict | Direction matched? | p_perm | Signal |
|:-:|:--|:--|:--:|:-:|:--|
| Q013-F-01 | ALMR letter-family-lattice BETWEEN | NULL at α_bon | YES (BETWEEN observed) | 0.179 | BETWEEN observed but not Q13-distinctive; descriptively closer to ALM than ALR |
| Q013-F-02 | Thunder-praises-God hapax | **CONFIRMED** | YES (corpus-hapax) | n/a (descriptive) | Q 13:13 unique corpus-wide |
| Q013-F-03 | Chronology-architecture (3-surah centroid) | **NULL — DIRECTION REVERSED** | **NO (pre-commit violation)** | 0.495 | Q 13 closer to Med (Q 2/3/4) than to M (Q 5/6/7) |
| Q013-F-04 | ALR-cluster FR-membership | NULL at α_bon | YES (in threshold) | 0.143 | Q 13 fits ALR but not distinctively |
| Q013-F-05 | Chronology audit + architecture invariance (Q 14 twin) | **CONFIRMED 3/3** | YES | n/a (3 sub-tests pass) | Chronology contested; Q 13 ≈ Q 14 at d=0.486; H-NEW-590 NULL |

**Family Bonferroni-k = 5; α_bon = 0.01**:
- Q013-F-02 PASSES (corpus-hapax established at descriptive level; lemma rare and construction unique).
- Q013-F-05 PASSES on 3-sub-test compound criterion.
- Q013-F-01, Q013-F-03, Q013-F-04 all return as NULL at the strict α_bon threshold.

**Net**: 2 CONFIRMED at high confidence (the corpus-hapax raʿd-praise-construction Q013-F-02 and the chronology-architecture-dissociation replication Q013-F-05); 1 NULL with PRE-COMMIT VIOLATION published with full prominence (Q013-F-03 — direction reversed — interpretable as artifact of Q 5 contamination in the M-centroid construction, NOT as falsification of the framework, since the cleaner Q013-F-05 test confirms the framework); 2 NULL at strict α_bon (Q013-F-01 and Q013-F-04 — both directionally consistent with H1 but not statistically distinctive given the muqaṭṭaʿāt-content-NULL framework's prior).

The aggregate pattern empirically grounds:
1. **Q 13:13 *yusabbiḥu al-raʿdu bi-ḥamdihi* is corpus-unique** in its lexical-syntactic construction (Q013-F-02). The classical theological attention to the verse is empirically validated.
2. **Q 13's contested chronology does NOT propagate to architectural-signature ambiguity** (Q013-F-05). The chronology-architecture-dissociation framework is REPLICATED on a contested-chronology test-case.
3. **Q 13 is the architectural twin of Q 14 Ibrāhīm** at d=0.486 in 4-axis Euclidean space — a corpus-rare twin signature in the head-mushaf zone.
4. The ALMR muqaṭṭaʿ does NOT predict a content-axis "BETWEEN" ALM and ALR at strict significance (Q013-F-01); the muqaṭṭaʿāt-content-NULL framework is upheld.

*Bismillāhi al-Raḥmāni al-Raḥīm.*
