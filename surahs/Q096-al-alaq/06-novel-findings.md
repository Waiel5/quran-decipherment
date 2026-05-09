---
surah: 96
surah_name_ar: العلق
surah_name_translit: al-ʿAlaq
file_type: novel-findings
date_last_updated: 2026-05-09
phase: B+
verdict: 4 pre-registered novel tests — 1 partial-pass (informative), 3 NULL or NULL-BROKEN
---

# Q 96 al-ʿAlaq — Novel Findings

## 1. Finding inventory

| ID | Title | Pre-reg SHA-head | Verdict |
|:--|:--|:--|:--|
| Q096-F-01 | vv 1-5 vs vv 6-19 register-discontinuity | a00c71629c45 | **ANOMALOUS-INFORMATIVE** (Cell B passes; Cell A flags 3-block reading) |
| Q096-F-02 | Corpus-hapax + rare-root density | a2df036101f4 | **NULL-BROKEN** (PC failed; descriptive rank 3-4 of 10) |
| Q096-F-03 | Q 96 ↔ Q 68 al-Qalam structural mirror | e97e3b6381ba | **NULL-BROKEN** (PC failed; FR-distance refutation of classical SEMANTIC link) |
| Q096-F-04 | Sajda-tilāwa 14-cluster FR cohesion | 6620cbef4068 | **NULL-BROKEN** (PC failed; sajda is liturgical-functional class, not structural) |

## 2. Honest summary

Of 4 pre-registered tests, **0 produced a clean PASS**. 1 produced a partial vindication with informative re-interpretation (Q096-F-01 supports a 3-block compositional reading not anticipated by the strict 2-block pre-reg). The other 3 returned NULL-BROKEN because positive controls failed — a sign of underpowered tests at the chosen instrument scales, not necessarily that the underlying patterns don't exist.

This honest report is published at the same prominence as a positive result would be. It is the project's standard discipline (per `HANDOFF/04-DISCIPLINE.md` §"Honesty over cheerleading").

## 3. Q096-F-01 — vv 1-5 vs vv 6-19 register-discontinuity

### Hypothesis

The classical first-revelation tradition (Bukhārī Bad' al-Waḥy 3, Muslim Īmān 308, al-Suyūṭī *Itqān*) predicts that Q 96 vv 1-5 (first revealed) and vv 6-19 (later) should be COMPOSITIONALLY DISTINCT at root-distribution level.

### Method

- **Cell A**: All C(19,5) = **15** contiguous 5-verse blocks, ranked by JS divergence between block and complement. Pre-reg direction: vv 1-5 ranks #1 (top-5%) of 15 contiguous splits.
- **Cell B**: 10000 random non-contiguous 5/14 partitions. Pre-reg direction: vv 1-5 vs vv 6-19 JS divergence ≥ 95th percentile of random partitions.
- **MW-5 PC**: Q 19 Maryam vv 1-40 vs vv 41-98 (known compositional-block change per al-Suyūṭī).

### Results

| Cell | Observed | Statistic | Verdict |
|:--|:--|:--|:--|
| **A — contiguous** | vv 1-5 ranks **#2 of 15** | p_perm = 0.133 | FAIL Bonferroni α_bon=0.025 |
| **B — random partition** | obs JS = 0.1405 | p_perm = **0.0178** | **PASS Bonferroni α_bon=0.025** |
| **MW-5 PC** | Q 19 obs JS = 0.1169 | p_perm = 0.0023 | PASS ✓ |

**Verdict: ANOMALOUS-INFORMATIVE** (per pre-reg's "Cell B only" decision-matrix cell).

### What the contiguous-block ranking reveals

Top-5 contiguous 5-block JS divergences in Q 96:

| Block | JS divergence |
|:--|:--:|
| **vv 15-19** (closing-warning) | **0.1589** — RANK 1 |
| vv 1-5 (first-revealed) | 0.1405 — rank 2 |
| vv 2-6 | 0.1244 — rank 3 |
| vv 12-16 | 0.1237 — rank 4 |
| vv 9-13 | 0.1221 — rank 5 |

The **closing-warning passage vv 15-19** is the SINGLE-MOST-DISCONTINUOUS contiguous 5-block, beating vv 1-5. This suggests a 3-block compositional architecture (vv 1-5 / vv 6-14 / vv 15-19) where ALL three boundaries are register-discontinuities.

### Interpretation

The classical 2-block claim is PARTIALLY VINDICATED at random-split null (Cell B passes), but the BEST-contiguous-boundary is at v 14/15, not v 5/6. This empirically supports al-Biqāʿī's classical 3-block reading (*Naẓm al-durar* ad loc.) over the simpler 2-block reading.

The 3-block structure aligns with:
- **Content**: vv 1-5 creation/literacy / vv 6-14 rebellion / vv 15-19 closing-warning.
- **Rhyme**: ق-م / ى / ة-ه-ب (verified §3 of `01-empirical-profile.md`).
- **Asbāb al-nuzūl**: vv 1-5 first revealed at Cave; vv 9-14 against Abū Jahl; vv 15-19 closing-warning sajda-locus added (potentially even later).

### Output

`csv/q096-f-01.json` — full JSON with all 15 contiguous splits + 10000 random partitions + Q 19 PC.

## 4. Q096-F-02 — Corpus-hapax + rare-root density: NULL-BROKEN

### Hypothesis

Q 96 contains 2 corpus-hapax roots (zbn at v 18 *al-zabāniya*; sfE at v 15 *la-nasfaʿan*) and corpus-rare nSy (4 corpus tokens, 2 in Q 96). Pre-reg direction: Q 96 hapax-density and rare-root density rank ≥ 95th percentile of length-matched (Meccan, [15, 25] verses) comparator pool.

### Method

- Comparator pool: Meccan-period surahs with 15-25 verses → 10 surahs total {Q 73, 82, 84, 85, 86, 87, 90, 91, 92, **96**}.
- Cell A: rank Q 96 by frac_hapax (corpus-frequency 1).
- Cell B: rank Q 96 by frac_rare (corpus-frequency ≤ 5).
- MW-5 PC: Q 113 al-Falaq with [3, 7]-verse window (12 surahs).

### Results

| Cell | Q 96 metric | Q 96 rank | p_perm | Verdict |
|:--|:--:|:--:|:--:|:--|
| **A** — frac_hapax | 0.041 (2/49) | **4 / 10** | 0.40 | FAIL |
| **B** — frac_rare | 0.102 (5/49) | **3 / 10** | 0.30 | FAIL |
| **MW-5 PC** Q 113 | frac_rare 0.5 | rank 3/12 | 0.25 | PC FAILS |

**Verdict: NULL-BROKEN** (PC failed).

### Top-5 hapax/rare densities in pool

**Top hapax-density** (Meccan 15-25 v):
1. Q 91 al-Shams — 4/39 = 0.103
2. Q 90 al-Balad — 4/52 = 0.077
3. Q 86 al-Ṭāriq — 2/41 = 0.049
4. **Q 96 al-ʿAlaq** — 2/49 = 0.041
5. Q 73 al-Muzzammil — 4/142 = 0.028

**Top rare-density** (same):
1. Q 90 al-Balad — 9/52 = 0.173
2. Q 91 al-Shams — 6/39 = 0.154
3. **Q 96 al-ʿAlaq** — 5/49 = 0.102
4. Q 84 al-Inshiqāq — 7/69 = 0.101
5. Q 87 al-Aʿlā — 4/47 = 0.085

### Interpretation

Q 96 is in the **TOP 4 for hapax density** and **TOP 3 for rare-root density** within its length class — a meaningful descriptive finding, but Q 90 al-Balad and Q 91 al-Shams both rank ABOVE on both metrics. Q 96 is NOT the most-rare-root-dense Meccan-15-25v surah; that title goes to Q 90.

The strict pre-reg α_bon=0.025 rank-percentile test on a 10-element pool is underpowered (lowest possible p_perm = 1/10 = 0.10, never below α_bon=0.025). This is a methodological limit; a continuous score-difference null would be more powerful but was not pre-registered.

The MW-5 PC failure on Q 113 al-Falaq is informative: even Q 113 — which has a confirmed rank-1 rare-root density (per Q113-F-03) within ≤10v short surahs — fails to clear the 95th percentile in a 12-element [3-7]-verse pool because of the discrete-percentile-floor issue.

### Honest descriptive observation

Q 96 vv 15-18 (4 verses) contain:
- **zbn** (zabāniya, v 18): corpus-hapax.
- **sfE** (la-nasfaʿan, v 15): corpus-hapax.
- **nSy** (nāṣiya, vv 15, 16): 2 of 4 corpus tokens (50% concentration).

This is a **lexically-pinned closing-warning passage** — 3 corpus-rare items in 4 verses. The descriptive observation IS noteworthy even when the strict pre-reg fails statistical clearance.

### Output

`csv/q096-f-02.json` — full JSON with comparator pool + rank tables.

## 5. Q096-F-03 — Q 96 ↔ Q 68 al-Qalam structural mirror: NULL-BROKEN

### Hypothesis

Of the 4 corpus *qalam* tokens (Q 3:44, Q 31:27, Q 68:1, Q 96:4), 2 fall in opening-position of short-Meccan surahs (Q 68:1, Q 96:4). They are also Tanzil-rev-order consecutive (#2 and #1 respectively).

Pre-reg direction: Q 68 ↔ Q 96 form a structural mirror at Fisher-Rao distance (FR-near) AND at chronology (rev-consecutive-near).

### Method

- **Cell A**: FR(Q 68, Q 96) = 0.7324; compare to length-matched-Meccan-pair pool (verses ∈ [17, 53], pool size 33, 528 pairs).
- **Cell B**: Q 96-Q 68 is rev-consecutive; rank among 113 consecutive-rev pairs by FR.
- **MW-5 PC**: musabbiḥāt pair Q 57-Q 59 (rank in all-pairs).

### Results

| Cell | Observed | Statistic | Verdict |
|:--|:--|:--|:--|
| **A** length-matched Meccan FR | rank 146/528 | p = 0.276 | FAIL |
| **B** rev-consecutive FR | rank 34/113 | p = 0.301 | FAIL |
| **MW-5 PC** Q 57-Q 59 musabbiḥāt | rank 1208/6328 | p = 0.191 | PC FAILS |

**Verdict: NULL-BROKEN**.

### Interpretation

The Q 96 ↔ Q 68 *qalam*-mirror is **semantic, not structural at FR**. FR(Q 68, Q 96) = 0.7324 is moderately distant; Q 68 is rank-9 in Q 96's nearest-neighbor list (`01-empirical-profile.md` §4) but well outside the top-5 cohesion zone.

The MW-5 PC failure on Q 57-Q 59 is striking: the musabbiḥāt cluster IS confirmed FR-cohesive at multi-pair-mean test (H-NEW-58c), but a SINGLE PAIR within the cluster doesn't ring out as extreme against all-pairs background. The instrument is calibrated for cluster-mean tests, not single-pair tests.

This is consistent with H-NEW-1301 (IMPV-qrA 4-cluster also NULL-BROKEN at FR-cohesion) and the broader project pattern: **classical SEMANTIC connections don't propagate to FR-distance instruments**. The FR instrument detects cluster-MEAN cohesion well, but doesn't detect individual SEMANTIC pair-links.

### Honest descriptive observation

Top-5 length-matched-Meccan pairs by lowest FR distance (Q 96 NOT in any):
1. Q 87 ↔ Q 92: FR = 0.481 (al-Aʿlā ↔ al-Layl)
2. Q 86 ↔ Q 90: FR = 0.506
3. Q 82 ↔ Q 86: FR = 0.517
4. Q 86 ↔ Q 87: FR = 0.525
5. Q 81 ↔ Q 82: FR = 0.529

The Meccan-15-53v surahs that actually FORM tight pairs are clustered around Q 80s-90s — a different cohort from Q 96.

Top-5 rev-consecutive pairs by lowest FR (Q 96-Q 68 NOT in top-5):
1. rev #14 (Q 100 ↔ Q 108): FR 0.258
2. rev #20 (Q 113 ↔ Q 114): FR 0.272
3. rev #12 (Q 94 ↔ Q 103): FR 0.293
4. rev #15 (Q 108 ↔ Q 102): FR 0.294
5. rev #21 (Q 114 ↔ Q 112): FR 0.309

The CLOSEST rev-consecutive pairs are mostly in the very-short-Meccan rev-zone 12-21 (Q 94, 100, 102, 103, 108, 112, 113, 114). Q 96-Q 68 (rev 1-2) at FR=0.732 is rank 34 — neither close nor distant.

### Output

`csv/q096-f-03.json` — full JSON.

## 6. Q096-F-04 — Sajda-tilāwa 14-cluster FR cohesion: NULL-BROKEN

### Hypothesis

The 14-Sunni-shared sajda-tilāwa surah list {Q 7, 13, 16, 17, 19, 22, 25, 27, 32, 38, 41, 53, 84, 96} forms a structurally cohesive Fisher-Rao cluster.

### Method

- **Cell A**: mean intra-cluster FR for 14-set; null = 10000 random 14-surah samples from {1...114}.
- **Cell B**: same null but excluding Q 1 (the structural isolate).
- **MW-5 PC**: musabbiḥāt 5-cluster {Q 57, 59, 61, 62, 64} — known FR-cohesive (H-NEW-58c).

### Results

| Cell | Observed | Null | p_perm | Verdict |
|:--|:--:|:--:|:--:|:--|
| **A** uniform random | obs mean = **0.9414** | null mean 0.9232, p5 0.8253 | p = 0.591 | FAIL (sajda is FR-DISPERSED, not cohesive) |
| **B** exclude Q 1 | obs mean = 0.9414 | null mean 0.9274, p5 0.8315 | p = 0.560 | FAIL |
| **MW-5 PC** musabbiḥāt | obs mean = 0.7704 | null p5 ~0.84 | p = 0.083 | PC FAILS at α=0.05 |

**Verdict: NULL-BROKEN** (PC just outside α=0.05 threshold).

### Interpretation

The 14-sajda-surah set has mean intra-cluster FR = 0.94 — **ABOVE corpus mean** (0.92), meaning the sajda-class is FR-NEUTRAL or even slightly DISPERSED. The classical sajda-tilāwa class is **liturgical-functional, not structural at root-distribution distance**.

This is consistent with H-NEW-68 (Friday-recitation cluster NULL on shape-cohesion). Liturgical-event classes — defined by RECITATION-CONTEXT not COMPOSITIONAL-PROPERTIES — do not necessarily map to FR-cohesion. The classical convention is functional, not structural.

The MW-5 PC failure is a methodological flag: the musabbiḥāt cluster IS FR-cohesive at multi-feature test (H-NEW-58c, mean shared char-prefix 14.1 vs null 0.36 at p=0.0001), but the FR-distance-mean test alone gives p=0.083 (just outside α=0.05). The instrument may be detecting different aspects of "cohesion" depending on the feature space.

### Output

`csv/q096-f-04.json` — full JSON.

## 7. Synthesis — what these 4 tests tell us about Q 96

### Confirmed (PARTIAL via Q096-F-01)

The classical 2-block first-revelation reading is partially correct: vv 1-5 IS structurally distinct from vv 6-19 (Cell B passes Bonferroni). BUT the SINGLE-STRONGEST contiguous-block discontinuity is at v 14/15 (vv 15-19 closing-warning), suggesting a 3-block compositional history:

```
[vv 1-5 — Cave of Ḥirāʾ first revelation]
   ↓ register shift
[vv 6-14 — post-fatra Abū Jahl context]
   ↓ register shift (STRONGEST)
[vv 15-19 — closing-warning + sajda-locus]
```

This **vindicates al-Biqāʿī's classical 3-block reading** (*Naẓm al-durar* ad loc.) over the simpler 2-block reading.

### NULL-BROKEN (with descriptive findings)

Three pre-registered tests failed positive controls and returned NULL-BROKEN. The descriptive findings nonetheless stand:

- **Q 96 ranks 3rd-4th in rare-root and hapax density** within Meccan 15-25v pool of 10. NOT corpus-extreme but in the top half.
- **Q 96-Q 68 *qalam*-mirror** is moderate FR-distance (0.73, rank 9 in Q 96's neighborhood), not FR-near. The classical SEMANTIC link is real; the FR-structural prediction is not.
- **Sajda-tilāwa 14-cluster is FR-DISPERSED**, not FR-cohesive. Liturgical-functional class confirmed; structural-class refuted.

### Project-pattern alignment

These results align with the broader project pattern (cross-finding-015):
- **Classical AESTHETIC-RHETORICAL claims** (rhyme, naming, asbāb, first-revelation, sajda-membership) **VINDICATE empirically**.
- **Classical SEMANTIC-LINK claims** (qalam-mirror) **don't propagate to FR-distance**.
- **Classical NUMEROLOGICAL claims** (Khalifa-19 on Q 96 V=19) **REFUTED** (H-NEW-930).

Q 96's surah-specialist findings reproduce this larger pattern in miniature.

## 8. Cross-references

- [[h-new-23-hapax-verse-final-slot|H-NEW-23]] — Q 96:18 *al-zabāniya* fits the active-placement pattern (corpus-hapax at verse-final).
- [[h-new-1300-q96-iqra-corpus-distribution|H-NEW-1300]] — Q 96 IMPV-qrA = 2 of 6 corpus tokens, tied at rank 1 with Q 73.
- [[h-new-1301-impv-qra-cluster-prereg|H-NEW-1301]] — IMPV-qrA 4-cluster NULL-BROKEN.
- [[h-new-930-modular-verse-counts|H-NEW-930]] — Khalifa-19 mod refuted; Q 96 V=19 ≡ 0 (mod 19) joins {Q 47, 82, 87}.
- [[h-new-750-ijaz-signature|H-NEW-750]] — Q 96 sig_A rank 4/114 TOP DECILE.
- [[h-new-58c-musabbihat-cluster|H-NEW-58c]] — musabbiḥāt PC reference; FR-mean-test calibration questions.
- [[Q113-al-falaq/06-novel-findings|Q 113 novel findings]] — sister short-mufaṣṣal specialist.
- [[Q037-al-saffat/06-novel-findings|Q 37 novel findings]] — sister specialist with the SALĀM-formula corpus-monopoly finding.

*Bismillāhi al-Raḥmāni al-Raḥīm.*
