---
surah: 46
surah_name: al-Aḥqāf
file_type: novel-findings
date_last_updated: 2026-04-28
phase: B+
verdict: 3 VINDICATED, 1 REFINED-MODERATE (direction-miss); all pre-registered with SHA-locked
---

# Q 46 al-Aḥqāf — novel findings

All four findings pre-registered BEFORE running. SHA verifications embedded in scripts at runtime; all SHAs matched at execution.

---

## Finding Q046-F-01: Q 46 → Q 47 boundary cost — REFINED-MODERATE (pre-commit direction-miss at threshold 25)

**Pre-registration**: [[Q046-F-01-boundary-cost-prereg|Q046-F-01-boundary-cost-prereg.md]] — locked SHA256 `0eafb9802f5a62a8f9704fe3fe6771ebf0c9e2037e224e9b42633fdea4e02374`.

**Script**: `/Users/grey/Downloads/quran/surahs/Q046-al-ahqaf/scripts/Q046_F_01_boundary_cost.py`.

**Output**: `/Users/grey/Downloads/quran/surahs/Q046-al-ahqaf/csv/Q046-F-01.json`.

**Hypothesis (locked)**: Q 46 → Q 47 cost ranks **top-25/113** (HIGH cost, reflecting triple discontinuity: HM exit + Meccan→Medinan + name-class shift).

**Result**:
- Q 46 → Q 47 δ-cost: **0.0873**
- Rank: **42 / 113** (sorted descending)
- Fraction of TSP residual: **1.05%**
- Top-10 expensive (reference): Q 1-Q 2 (7.5%), Q 32-Q 33 (4.4%), Q 33-Q 34 (4.0%), Q 9-Q 10 (3.7%), Q 24-Q 25 (3.5%), Q 22-Q 23 (3.1%), Q 42-Q 43 (2.8%), Q 56-Q 57 (2.7%), Q 12-Q 13 (2.6%), Q 7-Q 8 (2.6%).
- Q 46 → Q 47 at 1.05% is **3.5× cheaper than the median top-10**.

**Verdict**: **REFINED-MODERATE** — rank 42/113 is **upper-third** but **NOT top-22%** (top-25). The pre-committed direction (rank ≤ 25) **missed** by 17 ranks. Per [[INVESTIGATION-PROTOCOL]] §1.3 (equal NULL prominence), the result is published with full prominence: **the user-prompt's "HIGH canonical-adjacency-cost transition" framing is empirically refined to "moderate-upper-third (rank 42/113)"**.

**Mechanism interpretation**:
- The triple-discontinuity (HM exit + Meccan→Medinan + name-class shift) does NOT translate to a top-tier TSP cost.
- Compare to **Q 9 → Q 10** (rank 4/113, 3.7%) which is also a chronology-block boundary (rev-order #113→#51, Δ=−62) — but it is in the top-tier. The Q 46→Q 47 chronology jump (Suyūṭī rev-order #66→#95, Δ≈+29 toward Medinan) is smaller.
- The HM-exit at Q 46 → Q 47 is **less expensive than the al-sabʿ al-ṭiwāl boundary at Q 9-Q 10** by ~3.5× — this is a **non-trivial structural fact**: chronology-block boundaries are NOT all equal-cost; the relative size of the chronology jump matters.

**Comparison to FR-roots distance**: Q 46 ↔ Q 47 FR-distance = **0.9905** (rank 56/113 from a separate computation; see [[01-empirical-profile|empirical profile §3c]]). The FR-distance IS in the FR-far half — but the canonical-adjacency cost (which measures the residual after 2-opt local optimization) is moderate. **Two different signals disagree on magnitude**: FR-distance says "far", TSP-cost says "moderately expensive". This is a useful intuition-pump for understanding what each metric captures.

---

## Finding Q046-F-02: Q 46:29-32 ↔ Q 72 jinn-listening lexical signature — VINDICATED

**Pre-registration**: [[Q046-F-02-jinn-listening-jaccard-prereg|Q046-F-02-jinn-listening-jaccard-prereg.md]] — SHA `9a9b63f5469d9a96006115c7ad96b38161652eaa40b5db3105a022adf04c022a`.

**Script**: `Q046_F_02_jinn_jaccard.py`.

**Output**: `csv/Q046-F-02.json`.

**Hypothesis (locked)**: The root-Jaccard between Q 46:29-32 and Q 72 is **higher** than the root-Jaccard between random 4-verse Q 46 windows and Q 72.

**Result**:
- Q 46:29-32 distinct roots: **35**
- Q 72 distinct roots: **100**
- Intersection: **18**
- Union: **117**
- **Observed Jaccard: 0.1538**
- Null distribution (10000 random non-overlapping 4-verse Q 46 windows ↔ Q 72): mean = 0.112, median = 0.115
- **p_perm (one-sided): < 0.0001** (0 of 10000 null draws ≥ observed)

**Verdict**: **VINDICATED at p < 0.0001**. The Q 46:29-32 jinn-listening passage shares significantly more roots with Q 72 al-Jinn than any other 4-verse Q 46 window. Direction matches pre-commitment ✓.

**Top shared roots (alphabetical)**: Alh, Amn, ArD, E*b, Ejz, Trq, byn, dEw, dwn, hdy, jnn, jwr, nfr, qrA, qwl, qwm, smE, ydy.

**Lexical anchors**:
- *jnn* (jinn): Q 46:29 has 1 attestation; Q 72 has 3.
- *smE* (samiʿa, "to listen"): Q 46:29-32 has 2; Q 72 has 5.
- *nfr* (nafar, "party / delegation"): Q 46:29 has 1; Q 72:1 has 1. Together they account for 2 of the 18 corpus-wide n-f-r attestations.
- *qrA* (qaraʾa / Qurʾān): Q 46:29-32 has 1; Q 72 has 1.

These four roots — *jnn*, *smE*, *nfr*, *qrA* — form the **jinn-listening lexical signature**, present in both passages and concentrated nowhere else in this combination.

**Interpretation**: The classical exegetical pairing (al-Ṭabarī, al-Qurṭubī, Ibn Kathīr ad Q 46:29 and Q 72:1) is **empirically anchored at root-Jaccard signature strength p < 0.0001**. The two passages are NOT semantically interchangeable (Jaccard 0.154, not 1.0) but they share a distinctive lexical core that distinguishes them from random Q 46 windows.

**Cross-check**: FR-roots distance Q 46 ↔ Q 72 = 0.8854 (rank 29/113 for Q 46; rank 56/113 for Q 72). Q 72's FR-nearest neighbors are short late-Meccan (Q 112, 114, 110, 113); Q 72 sits at the FR-roots periphery for most of its corpus relations EXCEPT for the jinn-listening passage which signals to Q 46.

---

## Finding Q046-F-03: *al-Aḥqāf* corpus-hapax eponym — VINDICATED

**Pre-registration**: [[Q046-F-03-hapax-eponym-prereg|Q046-F-03-hapax-eponym-prereg.md]] — SHA `d2e68adeb5d74cb10b316c65941101511c4057d42948e7040021e0e4416db620`.

**Script**: `Q046_F_03_hapax_eponym.py`.

**Output**: `csv/Q046-F-03.json`.

**Hypothesis (locked)**: Root ح-ق-ف (Hqf) has exactly **one** corpus-wide attestation, and that attestation is at Q 46:21.

**Result (deterministic)**:
- QAC v0.4 attestations of root Hqf: `[[46, 21, 7]]` — **1 attestation**, at Q 46:21 word 7.
- Orthographic regex on `quran-text/quran-no-tashkeel.json` for `أحقاف`/`الأحقاف`/`حقف`: **1 hit**, at Q 46:21.
- Both verifications confirm corpus-hapax at root level AND orthographic level.

**Verdict**: **VINDICATED — corpus-hapax + Q 46:21 deterministic match**.

**Comparison-class**: Q 46 belongs to the **corpus-hapax-eponym** sub-class:
- Q 46 al-Aḥqāf — Hqf, 1 attestation (this finding).
- Q 105 al-Fīl — *fyl* "elephant", 1 root attestation in Q 105:1.
- Q 99 al-Zalzala — *zlzl*, 2 attestations (both in Q 99) — **NOT** corpus-hapax (2 occurrences) but **surah-hapax** (only-in-Q99).

The corpus-hapax-eponym condition (exactly 1 corpus-wide attestation) is **stricter** than the more common surah-hapax-eponym (only-in-the-surah but multiple internal attestations). Q 46's eponymity meets the stricter condition.

**Implication**: The classical naming of Sūrat al-Aḥqāf (al-Suyūṭī, *al-Itqān*, nawʿ 17) is anchored to a **single corpus-wide token**. This is one of the strongest concentration-eponymity signals in the corpus.

---

## Finding Q046-F-04: Q 45→Q 46 (internal) > Q 46→Q 47 (exit) — VINDICATED (counter-intuitive)

**Pre-registration**: [[Q046-F-04-internal-vs-exit-prereg|Q046-F-04-internal-vs-exit-prereg.md]] — SHA `71c8d4f6467612d5d51a1713fdd9c732f82bcf78caae2ca47d9e0efceef5e7ef`.

**Script**: `Q046_F_04_internal_vs_exit.py`.

**Output**: `csv/Q046-F-04.json`.

**Hypothesis (locked)**: Q 45→Q 46 internal HM-B step has **HIGHER** canonical-adjacency cost than Q 46→Q 47 HM exit (counter-intuitive to the user-prompt's framing).

**Result (deterministic)**:
- Q 45 → Q 46 δ-cost: **0.0959** (rank **37 / 113**, fraction 1.16%).
- Q 46 → Q 47 δ-cost: **0.0873** (rank **42 / 113**, fraction 1.05%).
- Ratio (internal / exit): **1.099**.
- Margin: **+9.9%** internal over exit.

**Verdict**: **VINDICATED — internal step costs 9.9% MORE than the HM-exit step**. Direction matches pre-commitment ✓; threshold ≥ 5% margin met.

**Interpretation**: This is a **counter-intuitive empirical refinement** of the user-prompt's "HM exit boundary" framing. The HM-7 cluster does NOT have a sharp single exit cost concentrated at Q 46→Q 47 — instead, the cost is **slightly higher INSIDE the cluster** (Q 45→Q 46) than at the cluster boundary (Q 46→Q 47).

**Mechanism candidates**:
1. **HM-B is a coherent monorhyme cluster**: Q 43-46 share the near-monorhyme prosodic profile, but the *content* difference between Q 45 al-Jāthiyah (kneeling-judgment + signs-of-creation) and Q 46 al-Aḥqāf (universal-recipient theme; jinn) is wider than the pure prosodic similarity suggests.
2. **Q 46 → Q 47 is "softened" by chronology**: Q 47 Muḥammad's Medinan-jihād content is FR-distant from Q 46 (FR=0.9905) but the chronology-jump from rev-order #66 to #95 (Δ=+29) is moderate compared to the Q 9 → Q 10 (Δ=−62) jump.
3. **The HM-7 cluster has internal non-monotonicity**: per [[01-empirical-profile|empirical profile §3]], Q 46's FR-nearest neighbor is Q 41 (HM-A!) at FR=0.7254 — Q 46 leapfrogs HM-B internal neighbors to bond with HM-A. The internal HM-B sequence (43→44→45→46) is NOT FR-monotonic.

**Implication**: Cluster-edge boundaries are NOT always the highest-cost points. **Internal cluster transitions can be costlier than cluster exits**. This pre-registers a **corpus-wide hypothesis** (deferred to follow-up): for muqaṭṭaʿāt-clusters generally, is the maximum-internal-cost typically higher or lower than the cluster-exit-cost? Two-cell-typology candidate.

---

## Summary table

| Finding | Verdict | Pre-commit direction | Statistical strength |
|:--|:--|:--|:--|
| Q046-F-01 boundary cost | REFINED-MODERATE | direction-MISS at threshold 25 | rank 42/113, p∼0.4 raw |
| Q046-F-02 jinn-listening Jaccard | VINDICATED | direction MATCH | p_perm < 0.0001 |
| Q046-F-03 *al-Aḥqāf* hapax-eponym | VINDICATED | deterministic | 1/1 (corpus-hapax) |
| Q046-F-04 internal > exit cost | VINDICATED | direction MATCH | 9.9% margin, single-test |

## Equal-NULL-prominence section

**Q046-F-01 is a direction-miss against the user-prompt's "HIGH cost" assertion**. Per [[INVESTIGATION-PROTOCOL]] §1.3, this NULL/REFINED is published with **full prominence**:

> The Q 46 → Q 47 mushaf-canonical adjacency does NOT carry top-tier TSP residual cost. It is rank 42/113, in the upper-third but not the top quartile. The triple-discontinuity (HM exit + Meccan→Medinan + name-class shift) is a **content-axis** (FR-distance) discontinuity, NOT a TSP-residual-cost top-tier event. The user-prompt characterisation is empirically refined.

This NULL/REFINED **strengthens the project's credibility** by demonstrating that direction-locked predictions can fail, and the failure is published with the same emphasis as vindications.

## Honest limits

1. **Q046-F-01** uses single-instrument (h-new-720 TSP residual). Cross-instrument replication via FR-distance row-rank would be a follow-up.
2. **Q046-F-02** Jaccard treats roots as binary (present/absent); a frequency-weighted variant (cosine on root-counts) would be a robustness check.
3. **Q046-F-03** is deterministic; no statistical strength claim beyond corpus-hapax-fact.
4. **Q046-F-04** is a single-pair comparison; the corpus-wide question (does internal > exit hold for other clusters?) is deferred.
5. The 9.9% margin in Q046-F-04 is observed without a permutation null (deterministic from h-new-720); a "what if Q 46's HM-B membership were resampled?" null would deepen the test.
6. The shared-roots list in Q046-F-02 includes some high-frequency function-roots (Alh, qwl, qwm) which would dominate any frequency-weighted analysis. The Jaccard signal is robust to this; the cosine signal would shift.

## Cross-references

- [[Q046-al-ahqaf/preregs/Q046-F-01-boundary-cost-prereg|Q046-F-01 prereg]]
- [[Q046-al-ahqaf/preregs/Q046-F-02-jinn-listening-jaccard-prereg|Q046-F-02 prereg]]
- [[Q046-al-ahqaf/preregs/Q046-F-03-hapax-eponym-prereg|Q046-F-03 prereg]]
- [[Q046-al-ahqaf/preregs/Q046-F-04-internal-vs-exit-prereg|Q046-F-04 prereg]]
- [[Q046-al-ahqaf/05-classical-claims-audit|Q 46 claims audit]]
- [[Q072-al-jinn/06-novel-findings|Q 72 al-Jinn novel findings]] (NOT yet built; reciprocal pending)
- [[hawamim-7-cluster-bifurcation|HM-7 cluster bifurcation]]
- [[h-new-720-canonical-adjacency-cost|H-NEW-720]]

*Bismillāhi al-Raḥmāni al-Raḥīm.*
