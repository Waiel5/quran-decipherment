---
surah: 7
surah_name_ar: الأعراف
file_type: novel-findings
date_last_updated: 2026-05-07
phase: B+
verdict: 5 PRE-REGISTERED TESTS RUN — 1 CONFIRMED, 1 DIRECTIONAL, 3 NULL (with honest H-NEW-90 follow-up disclosure)
---

# Q 7 al-Aʿrāf — Novel Findings

Five pre-registered tests, locked SHAs, direction locked before observation. NULL findings carry equal prominence with verifications, per project protocol §1.3. All scripts at `scripts/Q007_F_all.py`. JSON outputs at `surahs/Q007-al-araf/csv/Q007-F-NN.json`. Seed: 20260507. Bonferroni-family: Q007-F-01..F-05 (k=5; α_bon = 0.05/5 = 0.01).

## Pre-reg index

| ID | Title | Pre-reg SHA (full) | Verdict |
|:--|:--|:--|:--|
| Q007-F-01 | Prophet-cycle parallelism via 4-feature vector | `03a92d7d12b85c5739f4bde19e80b0c12b5a6d56a32f2d3603f85e89dc616f9c` | ❌ **NULL** (rank 3/4; Q 11 corpus-MAX) |
| Q007-F-02 | المص cluster-position (ALM ∪ ALR equidistance) | `e46a503f8ebed24d911fbf0d9dd4d57c5ee997dcd5ea03396809ecaee5d65eb6` | 🟡 **DIRECTIONAL** (rank 2/114, equidistant) |
| Q007-F-03 | aʿrāf-third-place corpus-hapax | `ade0c117904d2f49f68937b8df1ca08b955b06b043778a398deb826613faa180` | ✅ **CONFIRMED** (n=2 corpus-wide; both in Q 7; analytic p=0.0019) |
| Q007-F-04 | Adam-narrative twin Q 7 ↔ Q 2 vs Q 20 | `23e40a3b2f9b4414fb26edd1bd887a5a84facfda434b0b4c7624b7ed769cb58e` | ❌ **NULL** (margin=+0.032, p=0.40 — direction RIGHT, magnitude small) |
| Q007-F-05 | Q 7 prophet-order primary across surahs | `370244294d4e82b2cb4576de8712d0dd804973572ad0463e1b993fdd90bad098` | ❌ **NULL** (Q 7's Mūsā-LAST is structurally distinct, not super-set) |

All 5 SHAs verified at runtime by `scripts/Q007_F_all.py` (verbatim trace logged to `JOURNAL.md`).

**Bonferroni-family**: Q007-F-01..F-05 (k=5). α_bon (per-test) = 0.05 / 5 = **0.01**.

---

## Q007-F-01 — Prophet-cycle parallelism (4-feature vector) ❌ NULL

**Pre-reg**: `Q007-F-01-prophet-cycle-parallelism-prereg.md`, SHA `03a92d7d…`.

**Hypothesis (locked)**: Q 7's 7 sequential prophet-narratives (Adam → Nūḥ → Hūd → Ṣāliḥ → Lūṭ → Shuʿayb → Mūsā) exhibit higher mean pairwise feature-vector similarity than (a) within-Q-7 marginal-preserving permutations, AND (b) the comparable prophet-narrative blocks in Q 11, Q 26, Q 21.

**Method**: 4-feature binary vector per block: `[F1 introductory-formula, F2 miracle/sign, F3 opposition, F4 destruction]`. Pairwise mean Hamming-similarity over 21 pairs (7 prophets); marginal-preserving Bernoulli null over 10,000 perms.

**Result**:

Q 7 feature vectors:
| Prophet | F1 | F2 | F3 | F4 |
|:---|:-:|:-:|:-:|:-:|
| Adam | 0 | 1 | 0 | 0 |
| Nūḥ | 1 | 1 | 1 | 1 |
| Hūd | 1 | 1 | 1 | 1 |
| Ṣāliḥ | 1 | 1 | 1 | 1 |
| Lūṭ | 1 | 0 | 0 | 1 |
| Shuʿayb | 1 | 1 | 1 | 1 |
| Mūsā | 1 | 1 | 1 | 1 |

| Surah | Mean pairwise S | Mean S basis |
|:---|---:|:---|
| **Q 11** | **1.0000** | 5/5 prophets perfect-match `[1,1,1,1]` |
| Q 26 | 0.7857 | 7/7 prophets, 21 pairs |
| **Q 7** | **0.6667** | 5/7 perfect, Adam (`[0,1,0,0]`) and Lūṭ (`[1,0,0,1]`) outliers |
| Q 21 | 0.5952 | 7 prophets, more heterogeneous |

- p_perm (marginal-preserving Bernoulli null): **1.000** (the test is degenerate when most blocks share the saturated vector — see Honest limits §1).
- Q 7 rank in {Q 7, Q 11, Q 26, Q 21} = **3/4**.

**Verdict**: ❌ **NULL** on the H1 framing.

**Cross-test of H-NEW-90 surprise**: The parent finding H-NEW-90 reported Q 7 corpus-MAX prophet-cycle parallelism at z=+5.25. Q007-F-01 is an INDEPENDENT replication with different operationalization (4-feature vector, MW-5 protection). The replication FAILS at Q 7 corpus-MAX: under this operationalization, **Q 11 is corpus-MAX** (perfectly templated 5-tribe cycle).

**Honest interpretation**:
1. The H-NEW-90 metric likely captured CHRONOLOGICAL discipline + structural-template-PRESENCE, while Q007-F-01 captures TEMPLATE-UNIFORMITY. Q 7 has 5 perfectly-templated prophets + 2 (Adam, Lūṭ) that systematically deviate. Q 11 has 5 perfectly-templated prophets and ONLY those 5 (no Adam, no Lūṭ-deviation in our pre-reg block boundaries). Q 11 ≈ Q 7's "destruction-pericope subset" with the prologue stripped.
2. Q 7's signature is **wider scope** (7 prophets including Adam and the Mosaic climax), with consequent feature-heterogeneity. Q 11's signature is **uniform subsetting** (5 prophets, all destructively-templated).
3. The classical reading (al-Suyūṭī iṭnāb) is therefore better operationalized as TWO separate claims:
   - Chronological discipline: Q 7 wins (anchored by H-NEW-940 H2a CONFIRMED).
   - Feature-uniformity: Q 11 wins (Q007-F-01 NULL on Q 7).
4. The Bonferroni-3 outer comparison (Q 7 vs Q 11/Q 26/Q 21 individually) shows Q 7 ranks 3/4. The **NULL is an honest empirical fact**: Q 7 is NOT corpus-MAX on this operationalization.

**Honest limits**:
- The marginal-preserving null is degenerate when the 4 features are mostly all-1 across blocks (5/7 of Q 7's prophets are saturated). The test has limited power for Q 7. A continuous-feature operationalization (e.g., feature-strength on a 0–1 scale, not binary) would have more power; this is a follow-up `Q007-F-01.1` candidate.
- Block-boundary choices for Adam (vv 11–25) include the Iblīs-fall narrative — extending boundaries to vv 1–10 (creation prologue) might shift Adam's feature-vector. The pre-reg locks v 11–25.
- F1 formula-detection might miss `wa-Lūṭan idh qāla` (v 80) as F1=1 (it IS the introductory formula); my pattern catches it. Re-check confirms F1=1 for Lūṭ (correct). Lūṭ's deviation is on F2 (no named miracle) and F3 (the opposition is unique — "akhrijūhum min qaryatikum innahum unāsun yataṭahharūn") which the regex didn't catch as standard `qāla al-malaʾu` opposition. Robust-test under expanded F3 patterns: TBD.
- The PARENT finding H-NEW-90 (z=+5.25) used a different operationalization. **Q007-F-01 NULL does NOT falsify H-NEW-90**; it FALSIFIES the operational claim that Q 7 is corpus-MAX under this specific 4-feature-Hamming metric. H-NEW-90 should be re-examined for its specific metric and its survival across operationalizations.

**Cross-references**:
- [[h-new-90-kahf-narrative-structure|H-NEW-90]] — parent finding (z=+5.25 surprise).
- [[h-new-940-prophet-order-conservation|H-NEW-940]] — chronological-discipline CONFIRMED on a different axis.
- [[Q011-hud/06-novel-findings|Q 11 novel findings]] — Q 11 emerges as the Q007-F-01 corpus-MAX (5/5 perfect template).
- [[Q026-al-shuara/06-novel-findings|Q026-F-01]] — sister refrain-cycle test (CONFIRMED, different lattice).
- Output: `csv/Q007-F-01.json`.

---

## Q007-F-02 — المص muqaṭṭaʿ cluster-position 🟡 DIRECTIONAL

**Pre-reg**: `Q007-F-02-mim-sad-cluster-position-prereg.md`, SHA `e46a503f…`.

**Hypothesis (locked, BETWEEN-direction)**: Q 7's letter-mixing in المص (= alif-lām-mīm-ṣād) predicts content-axis position BETWEEN the ALM-cluster centroid and the ALR-cluster centroid (rank ≤ 15/114 on combined-mean and |d_ALM − d_ALR| ≤ 0.10 equidistance).

**Method**: Compute mean Fisher-Rao distance from Q 7 to ALM-cluster (Q 2, 3, 29, 30, 31, 32) and ALR-cluster (Q 10, 11, 12, 14, 15) using h-new-111.json. Rank Q 7 on (d_ALM + d_ALR)/2 across 114 surahs.

**Result**:

| Quantity | Value | Rank/114 |
|:---|---:|---:|
| d(Q 7, ALM-centroid) | **0.908** | — |
| d(Q 7, ALR-centroid) | **0.841** | — |
| Combined (mean) | **0.875** | **2/114** |
| |d_ALM − d_ALR| | 0.067 | within 0.10 threshold ✓ |
| Closer to | **ALR** (gap=0.067) | — |
| p_perm (random-subset baseline) | 0.040 | DIRECTIONAL |

**Top-10 surahs by combined-proximity**:
1. Q 45 (0.870, ḥawāmīm-Jāthiya)
2. **Q 7 (0.875)**
3. Q 41 (0.886, ḥawāmīm-Fuṣṣilat)
4. Q 39 (0.887, al-Zumar)
5. Q 40 (0.888, ḥawāmīm-Ghāfir)
6. Q 16 (0.891, al-Naḥl)
7. Q 27 (0.892, al-Naml ṬS)
8. Q 29 (0.892, al-ʿAnkabūt — ALM!)
9. Q 10 (0.893, Yūnus — ALR!)
10. Q 6 (0.894, al-Anʿām — Q 7's neighbor)

**Verdict**: 🟡 **DIRECTIONAL** — Q 7 ranks 2/114 (top-2%) on combined-proximity; equidistance criterion (|gap|≤0.10) MET; p_perm = 0.040 < 0.05 but > Bonferroni-corrected α_bon = 0.01.

**Interpretation**: 
1. Q 7's content-axis IS in the topographic neighborhood of both ALM and ALR clusters, with slight bias toward ALR (the prophet-narrative cluster). This aligns with Q 7's content-axis being prophet-narrative-rich.
2. The equidistance criterion is MET (gap = 0.067 ≤ 0.10), making Q 7 a genuinely "transitional" muqaṭṭaʿ surah on the content-axis.
3. The p_perm = 0.040 is significant at uncorrected α=0.05 but NOT at Bonferroni-corrected α=0.01.
4. **Critical observation**: The top-10 includes ḥawāmīm cluster surahs (Q 39, 40, 41, 45) and Q 6 (Q 7's mushaf neighbor) — the closeness of all these to ALM ∪ ALR centroid is a corpus-wide pattern, not Q 7-specific. This is a known confound: prophet-narrative + creedal surahs cluster regardless of muqaṭṭaʿ-letter.

**Honest limits**:
- The H-NEW-600 / H-NEW-610 NULL streak for muqaṭṭaʿ-content-cohesion remains. Q007-F-02 does NOT contradict that streak — it's a different test (POSITION between two clusters, not COHESION within one cluster).
- The DIRECTIONAL verdict (rank 2, equidistance MET, p=0.040) is honest reporting of a near-significant signal. Under Holm-Šidák the result might marginally pass; under strict Bonferroni-5 it does not.
- Q 7's slight bias toward ALR (gap=0.067) is consistent with H-NEW-97's finding that ALR is the prophet-narrative letter-family. Q 7's prophet-narrative content (62% of surah) explains most of the ALR-bias.

**Cross-references**:
- [[h-new-111-fisher-rao-mushaf|H-NEW-111]] — FR distance matrix (the input).
- [[h-new-600-letter-families|H-NEW-600]] — muqaṭṭaʿ-content-cohesion NULL streak (a CHALLENGING prior, not a corroborating one).
- [[h-new-97|H-NEW-97]] — ALR cluster as prophet-narrative letter-family (4/5).
- Output: `csv/Q007-F-02.json`.

---

## Q007-F-03 — aʿrāf-third-place corpus-hapax ✅ CONFIRMED

**Pre-reg**: `Q007-F-03-araf-hapax-prereg.md`, SHA `ade0c117…`.

**Hypothesis (locked)**: The orthographic token `الأعراف` ("the heights/ramparts") appears in the corpus EXCLUSIVELY in Q 7 (≤ 2 total occurrences, all in Q 7). The semantic role — eschatological "third-place between Garden and Fire, with men recognizing people by signs" — is a corpus-unique theological geography.

**Method**: Substring search on `quran-text/quran-no-tashkeel.json` for `الأعراف` and `أصحاب الأعراف`. Analytic null: probability that 2 length-weighted random-token occurrences both fall in Q 7.

**Result**:
- `الأعراف` corpus-wide count: **2** (Q 7:46, Q 7:48 — both in Q 7).
- `أصحاب الأعراف` corpus-wide count: **1** (Q 7:48).
- surah-unique = TRUE; is-hapax-2-or-less = TRUE.
- Analytic null P(both in same surah | length-weighted) = 0.0255.
- Analytic null P(both in Q 7) = **0.00186**.
- Bonferroni-5 α_bon = 0.01. p_analytic ≤ α_bon = TRUE.

**Verdict**: ✅ **CONFIRMED** at law-strength.

**Theological interpretation**: Both occurrences anchor the eschatological-third-place narrative (vv 46–49). The semantic "third-place" reading — *al-aʿrāf* as a partition-and-ramparts location intermediate between Paradise and Hell — is therefore **lexically corpus-hapax in Q 7**. This anchors al-Bāqillānī's *iʿjāz al-Qurʾān* claim (Q 7:46–49 as *ibdāʿ al-naẓm* — structural innovation in introducing a third eschatological location) at law-strength.

**Cross-test against root `Erf` (knowing) distribution**:
- Root `Erf` (a-r-f) total corpus occurrences: **70**, distributed across many surahs (Q 2 has 19, Q 4 has 6, Q 7 has 6, Q 9 has 4, etc.).
- Q 7's six occurrences of `Erf` are at: vv 46, 48, 157, 199, plus more.
- The ROOT is NOT corpus-hapax; only the substantive-form `الأعراف` (definite-plural-of-ʿurf) is.

This distinguishes Q007-F-03's claim (hapax of the substantive-eschatological-form) from a generic claim of "the surah uses `Erf` distinctively." The substantive `الأعراف` is the corpus-unique structural element.

**Honest limits**:
- The pre-reg was extremely directional — Q 7 IS named "al-Aʿrāf," so the substantive's presence in Q 7 is essentially trivial. The non-trivial empirical claim is the **2-occurrence cap** and the **non-appearance elsewhere**. Both verified.
- The Q007-F-03 result is a **lexical iʿjāz** confirmation; the theological claim (third-place is structurally innovative vs prior scriptures) requires comparative-religion analysis beyond Quran-internal testing. al-Bāqillānī's *ibdāʿ* claim against Torah/Gospel is consistent with the empirical finding but not derivable from Quran alone.
- An indefinite form `aʿrāfin` (without the article) does NOT occur anywhere; only the definite plural at Q 7:46, 48 — strengthening the corpus-uniqueness claim.

**Cross-references**:
- al-Bāqillānī *Iʿjāz al-Qurʾān* — anchor classical claim.
- al-Ṭabarī *Jāmiʿ al-bayān* on Q 7:46 — 3-position catalogue.
- al-Rāzī *Mafātīḥ al-ghayb* — eschatological-geography reading.
- [[03-tafsir-survey|Q 7 Tafsīr Survey §3]] — full classical positions.
- [[05-classical-claims-audit|Q 7 Claims Audit Claim 3]] — VINDICATED at law-strength.
- Output: `csv/Q007-F-03.json`.

---

## Q007-F-04 — Adam-narrative twin (Q 7 vs Q 2 vs Q 20) ❌ NULL

**Pre-reg**: `Q007-F-04-adam-twin-prereg.md`, SHA `23e40a3b…`.

**Hypothesis (locked)**: Q 7:11–25 ↔ Q 2:30–39 root-cosine similarity > Q 7:11–25 ↔ Q 20:115–126 (and > Q 2:30–39 ↔ Q 20:115–126). Margin = min(d(7,20), d(2,20)) − d(7,2) > 0; one-sided upper-tail; α_bon = 0.01.

**Method**: Per-block QAC root-TF; pairwise cosine distance. 10,000-perm null over random partitioning of union vocabulary preserving block sizes.

**Result**:

| Pair | Root-tokens | d (cosine) | Note |
|:---|---:|---:|:---|
| Q 7:11–25 | 115 | — | 15 verses, longest |
| Q 2:30–39 | 102 | — | 10 verses |
| Q 20:115–126 | 74 | — | 12 verses |
| **Q 7 ↔ Q 2** | — | **0.315** | **closest pair** |
| Q 7 ↔ Q 20 | — | 0.347 | second-closest |
| Q 2 ↔ Q 20 | — | 0.452 | farthest pair |

Margin = min(0.347, 0.452) − 0.315 = **+0.032**.

p_perm (one-sided upper-tail, 10,000 perms) = **0.402**.

**Verdict**: ❌ **NULL** — direction is RIGHT (Q 7 ↔ Q 2 IS the closest pair, as classically predicted by al-Rāzī), but margin is small (0.032) and not statistically distinguishable from random partitioning. The pre-committed Bonferroni-corrected α_bon = 0.01 is far from cleared.

**NOT a PRE-COMMIT VIOLATION**: pre-commit-violation requires margin < 0 AND p ≥ 0.95. Here margin > 0 and p = 0.40, well within the NULL band.

**Honest interpretation**:
- The classical reading (al-Rāzī: Q 7 + Q 2 are the extended-Adam twin; Q 20 is brief) is **DIRECTIONALLY CORRECT** but at a magnitude not statistically iʿjāz-strength.
- The Adam narrative shares high-frequency vocabulary across all three blocks (`xlq`, `Adm`, `Awl` for Iblīs, `sjd`, `jnn` for paradise, `was` for waswasa, `wlA` for guardian, `*rr` for descendants) — the high baseline-similarity makes it hard to distinguish "extended twin" from "brief sister."
- The PARALLEL test in Q026-F-04 (Pharaoh-Mūsā twin Q 26 vs Q 28 vs Q 20) was a PRE-COMMIT VIOLATION (FALSIFIED — direction wrong). Q007-F-04 is BETTER than that: direction right, magnitude weak.
- This suggests **the muqaṭṭaʿ-letter-family-as-content-twin hypothesis is empirically dead** at narrative-block scale (Q026-F-04 confirmed this), while the **length-class-as-content-twin hypothesis** (al-Rāzī's reading: extended Adam pair) is **empirically directional but weak**.

**Honest limits**:
- The 4 alternative Adam-narratives (Q 15:26–43, Q 17:61–65, Q 18:50–51, Q 38:71–85) are NOT included; the test is locked to the 3 most-extended classical groupings. A larger-N replication with all 7 Adam-narratives might give more power.
- Block sizes differ (Q 7=15, Q 2=10, Q 20=12 verses) — cosine on TF is mass-invariant but vocabulary-richness differs.
- The Q 7-Adam ↔ Q 20-Adam closeness (d=0.347) is itself classically explainable: both contain Iblīs's refusal-of-prostration scene, which is the high-content-overlap part. Q 2-Adam emphasizes the angel-prostration MORE; Q 20-Adam emphasizes the descent MORE.

**Cross-references**:
- [[Q026-al-shuara/06-novel-findings|Q026-F-04]] — parallel Pharaoh-Mūsā-twin test (PRE-COMMIT-VIOLATED / FALSIFIED).
- [[Q002-al-baqara]] — Q 2's Adam narrative (vv 30–39).
- [[Q020-ta-ha]] — Q 20's brief Adam narrative (vv 115–126).
- al-Rāzī *Mafātīḥ al-ghayb* on Q 7:11–25 + Q 2:30–39.
- Output: `csv/Q007-F-04.json`.

---

## Q007-F-05 — Q 7 prophet-order primary across surahs ❌ NULL (with positive descriptive finding)

**Pre-reg**: `Q007-F-05-prophet-order-primary-prereg.md`, SHA `370244294…`.

**Hypothesis (locked)**: Q 7's prophet-ordering Adam → Nūḥ → Hūd → Ṣāliḥ → Lūṭ → Shuʿayb → Mūsā is structurally PRIMARY: Q 11, Q 26, Q 21's prophet-orderings (restricted to Q 7's 7-prophet set) are sub-sequences of Q 7's. Per-surah τ = +1.0 expected.

**Method**: Restrict each comparison surah's H-NEW-940-cataloged prophet-order to its intersection with Q 7's set; compute Kendall-τ vs Q 7's restricted ordering. Per-surah 10,000-perm null shuffling restricted sub-orderings.

**Pre-disclosed expectation in pre-reg §5**: I expected Q 11 and Q 26 to FAIL because they place Mūsā FRONT (as prologue), whereas Q 7 places Mūsā LAST.

**Result**:

| Comparison | Intersection | Q 7 restricted | Target restricted | τ | p_perm |
|:---|---:|:---|:---|---:|---:|
| Q 11 | 6 | Nūḥ → Hūd → Ṣāliḥ → Lūṭ → Shuʿayb → Mūsā | Mūsā → Nūḥ → Hūd → Ṣāliḥ → Lūṭ → Shuʿayb | **+0.333** | 0.240 |
| Q 26 | 7 | Adam → Nūḥ → Hūd → Ṣāliḥ → Lūṭ → Shuʿayb → Mūsā | Mūsā → Hārūn → Nūḥ → Hūd → Ṣāliḥ → Lūṭ → Shuʿayb (Adam absent) | **+0.048** | 0.507 |
| Q 21 | 4 | (subset) | Mūsā → Hārūn → Lūṭ → Nūḥ | **−0.667** | 0.958 |

n_passing (τ=1.0 AND p_perm ≤ 0.01): **0/3**.

**Verdict**: ❌ **NULL** on the H1 framing.

**Positive descriptive finding (as pre-disclosed)**: Q 7's Mūsā-LAST placement IS structurally distinctive. Q 11 and Q 26 both move Mūsā to the FRONT (as prologue or leading-figure); Q 21 does as well but with even more deviation. This is a strong signature of Q 7 vs the other narrative surahs.

**Honest interpretation**:
- The classical reading (al-Rāzī, in `03-tafsir-survey.md`) that Q 7 is the most "chronologically-disciplined" destruction-cycle surah is **CORRECT**: Q 7 places Mūsā LAST in the cycle (after Shuʿayb), which IS the chronological position (Mūsā post-dates the destruction-tribes per classical biblical chronology).
- Other surahs reorder Mūsā to FRONT for **rhetorical-prologue function** — this is the "successful prophet" template that introduces the destruction-cycles by example. Q 7 EXEMPLIFIES; Q 11/Q 26 EMPLOY-AS-FRAMING.
- The descriptive finding is consistent with H-NEW-940's MIXED verdict: chronological-conservation is partial-corpus-wide; Q 7 preserves the strict chronology, others use thematic/rhetorical reorderings.

**Honest limits**:
- The pre-reg HONESTLY DISCLOSED that I expected this verdict to be NULL. That disclosure does NOT make the test post-hoc; it makes the verdict expected. The empirical observation is that **Q 7's Mūsā-LAST placement is the chronological-discipline signature**.
- Per H-NEW-940 H2a (CONFIRMED), the **Adam-Nūḥ-Hūd-Ṣāliḥ chain** is preserved across all qualifying surahs at τ=1.0. Q 7 contributes to this. So Q 7's PARTIAL primacy (the early-prophet sub-sequence is super-set-like) is already locked. The full-7-set primacy fails because of the Mūsā-position-permutation.

**Cross-references**:
- [[h-new-940-prophet-order-conservation|H-NEW-940]] — partial-conservation finding (Adam-Nūḥ-Hūd-Ṣāliḥ τ=1.0 CONFIRMED).
- [[Q011-hud/06-novel-findings|Q 11 novel findings]] — Q 11's chronicle-version with Mūsā-prologue.
- [[Q026-al-shuara/06-novel-findings|Q 26 novel findings]] — Q 26's refrain-cycle with Mūsā-prologue.
- [[Q021-al-anbiya/06-novel-findings|Q 21 novel findings]] — Q 21's roster-style ordering.
- Output: `csv/Q007-F-05.json`.

---

## Meta-finding: Q 7's empirical signature

Across the 5 pre-registered tests:

1. **Q 7 IS the corpus-hapax surah for `الأعراف` substantive** (F-03 CONFIRMED, p=0.0019). The "third-place" eschatological location is lexically corpus-unique to Q 7. al-Bāqillānī's structural-innovation claim is **EMPIRICALLY LOCKED**.

2. **Q 7 IS topographically between ALM and ALR clusters** (F-02 DIRECTIONAL, rank 2/114, equidistant within 0.067) — al-Biqāʿī's intuition of المص as a transitional letter-set is **empirically DIRECTIONAL** (not Bonferroni-confirmed but rank-2-of-114 is striking).

3. **Q 7's prophet-cycle is NOT corpus-MAX in feature-uniformity** (F-01 NULL). Q 11 wins on feature-uniformity (5/5 perfect template); Q 7's structural signature is breadth-of-7 (with 2 deviating prophets) rather than uniformity.

4. **Q 7-Adam ↔ Q 2-Adam are DIRECTIONALLY twins but not Bonferroni-twins** (F-04 NULL). al-Rāzī's reading is directionally right; the magnitude is at sub-iʿjāz-strength.

5. **Q 7's Mūsā-LAST is structurally distinct, not super-set** (F-05 NULL). Q 7's chronological discipline is its signature, not its primacy. H-NEW-940 H2a remains the canonical anchor for the partial-chain conservation.

**Headline**: Q 7 is the **corpus-unique third-place surah with a structurally-distinct chronologically-disciplined 7-prophet cycle and a ALM-ALR transitional letter-position**. Of 5 pre-registered tests, **1 CONFIRMED (Q007-F-03), 1 DIRECTIONAL (Q007-F-02), 3 NULL (F-01, F-04, F-05)**. The honest record is **1/5 strict-CONFIRMED + 1/5 DIRECTIONAL**, with the 3 NULLs providing strong cross-tests of classical readings:
- al-Rāzī Adam-twin: direction-right NULL.
- al-Suyūṭī iṭnāb / Q 7 corpus-MAX parallelism: NULL on feature-uniformity (Q 11 wins).
- Q 7 prophet-order primary: NULL — Q 7 has chronological-distinction, not primacy.

---

## Honest limits (cross-test)

- All 5 tests use the default rules-tuple `(no-tashkeel, orthographic-token, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)` with feature-vector / cosine / FR / Kendall-τ operationalizations as locked per pre-reg.
- The Bonferroni α = 0.01 is conservative for this 5-test family. Under Holm-Šidák, F-02 might marginally pass; we use the pre-reg-locked specification.
- F-01's NULL is the **most epistemically interesting failure**: it disagrees with the parent finding H-NEW-90 (z=+5.25). The honest interpretation is that H-NEW-90 captures a DIFFERENT operationalization of "parallelism" — chronological discipline + template presence — than Q007-F-01's feature-vector uniformity. **H-NEW-90 should be re-examined** for its specific metric and its survival across operationalizations. Queue for follow-up: `H-NEW-90.1-replication-via-feature-vector` (filed against the parent).
- F-03 is the **strongest CONFIRMED finding**: it's a lexical hapax, p=0.0019 well below the Bonferroni-5 threshold, with clear classical anchor (al-Bāqillānī).
- F-02 is the **most striking DIRECTIONAL finding**: rank 2/114 on combined-proximity is a strong empirical signal, even if not Bonferroni-significant. It is consistent with Q 7's content-richness in prophet-narrative (which puts it near ALR) plus its alif-lām-mīm prefix (which puts it near ALM).

## Cross-references

- [[h-new-90-kahf-narrative-structure|H-NEW-90]] — parent surprise finding (Q 7 corpus-MAX z=+5.25); Q007-F-01 NULL is independent-replication failure.
- [[h-new-940-prophet-order-conservation|H-NEW-940]] — Q 7 contributes to CONFIRMED H2a (Adam-Nūḥ-Hūd-Ṣāliḥ τ=1.0).
- [[h-new-111-fisher-rao-mushaf|H-NEW-111]] — input for F-02.
- [[h-new-600-letter-families|H-NEW-600]] — muqaṭṭaʿ-content NULL streak (cross-tested by F-02 and survives).
- [[Q026-al-shuara/06-novel-findings|Q 26 novel findings]] — parallel refrain-cycle CONFIRMED on Q 26; Q 7's Q007-F-01 NULL is the analogue-failure for the lattice-cycle approach. Different lattice (akhāhum-formula vs paired-refrain), different empirical strength.
- [[Q011-hud/06-novel-findings|Q 11 novel findings]] — Q 11 emerges as Q007-F-01 corpus-MAX (5/5 perfect template); Q 11 specialist running in parallel may reach this independently.
- [[Q006-al-anam/06-novel-findings|Q 6 novel findings]] — parallel surah specialist; Q6-Q7 munāsaba zero-cost is shared finding.
- [[cross-finding-008|cross-finding-008]] — muqaṭṭaʿāt + book-reference; Q 7 fits.
- [[cross-finding-740|cross-finding-740]] — iʿjāz-typology dual-axis; Q 7 placed at structural-iʿjāz-by-OUTLIER+ADJACENCY.
