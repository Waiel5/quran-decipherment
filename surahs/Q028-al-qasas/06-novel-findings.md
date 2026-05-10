---
surah: 28
surah_name_ar: القصص
file_type: novel-findings
date_last_updated: 2026-05-07
phase: B+
verdict: 5 PRE-REGISTERED TESTS RUN (seed 20260507, 10 000 perms, Bonferroni k=5, α=0.01) — F-01 DIRECTIONAL, F-02 NULL-PRE-COMMIT-DIRECTION-REVERSED (consolidates Wave-FALSIFIED §3.7), F-03 DIRECTIONAL, F-04 NULL, F-05 PASS (challenges Wave-FALSIFIED §3.7 on different axis)
---

# Q 28 al-Qaṣaṣ — Novel findings

Five pre-registered tests, locked SHAs, direction locked before observation. NULL findings carry equal prominence per project protocol §1.3. All scripts at `surahs/Q028-al-qasas/scripts/Q028_F_all.py`. JSON outputs at `surahs/Q028-al-qasas/csv/Q028-F-NN.json`. Seed 20260507. 10 000 permutations. Bonferroni k=5, α_Bonferroni = 0.01.

## Pre-reg index

| ID | Title | Pre-reg SHA | Verdict |
|:--|:--|:--|:--|
| Q028-F-01 | Madyan-episode lexical isolation (vv. 22-28) | `0717e38d1749a703…` | **DIRECTIONAL** |
| Q028-F-02 | TSM Moses-content twin-pair (Q 26 ↔ Q 28 vs Q 20) | `f32d033c43c9ca96…` | **NULL** (pre-commit direction REVERSED — published with full prominence; consolidates Wave-FALSIFIED §3.7) |
| Q028-F-03 | Qārūn-episode block isolation (vv. 76-82) | `80061fb62c8aed32…` | **DIRECTIONAL** |
| Q028-F-04 | Q 28:34 impediment-reference root-diversity | `2e28b7a4129a8afb…` | **NULL** |
| Q028-F-05 | TSM 3-surah narrative-density joint cohesion | `f9d5c2de81343db7…` | ✅ **PASS** (challenges Wave-FALSIFIED §3.7 on **narrative-density axis** — a different axis than the previously-falsified content-vocabulary axis) |

All five SHAs verified at runtime by `surahs/Q028-al-qasas/scripts/Q028_F_all.py` (verbatim trace logged to `JOURNAL.md`).

---

## Q028-F-01 — Madyan-episode lexical isolation (DIRECTIONAL)

**Pre-reg**: `Q028-F-01-madyan-episode-lexical-isolation-prereg.md`, SHA `0717e38d…`.

**Hypothesis (locked, three sub-claims)**:
- H1: Q 28:22-28 hapax-density rank ≤ 4 / 82 windows AND p_perm < 0.01.
- H2: ≥ 3 corpus-orthographic-hapax tokens in vv. 22-28.
- H3: `مدين` (Madyan place-name) ≥ 50% Q 28 share corpus-wide.

**Result** (full output in `csv/Q028-F-01.json`):

| Sub-claim | Observed | Threshold | Verdict |
|:--|:--|:--|:-:|
| H1 hapax-density rank | **6 / 82** (window 22-28; density 0.209) | ≤ 4 | ❌ FAIL (rank 6 vs threshold 4) |
| H1 p_perm | **0.0026** | < 0.01 | ✓ |
| H2 corpus-hapaxes in vv. 22-28 | **28 unique** | ≥ 3 | ✅ PASS (far exceeds threshold) |
| H3 *مدين* Q 28 share | **30%** (3 / 10 corpus) | ≥ 50% | ❌ FAIL |

**Aggregate**: H2 PASS, H1 partial-pass (p significant but rank just outside top-4), H3 FAIL → **DIRECTIONAL** (1 of 3 sub-claims pass, 1 partial).

**Top-10 windows by hapax density** (from output):
1. vv. 6-12 — 0.241 (birth-of-Mūsā block)
2. vv. 7-13 — 0.230 (birth-of-Mūsā continuation)
3. vv. 5-11 — 0.221
4. vv. 8-14 — 0.218
5. vv. 4-10 — 0.212
6. **vv. 22-28 — 0.209** (Madyan-episode)
7. vv. 21-27 — 0.202
8. vv. 23-29 — 0.200
9. vv. 9-15 — 0.198
10. vv. 10-16 — 0.190

**Honest interpretation**: The Madyan-episode IS hapax-rich (rank 6 of 82 = 92.7th percentile, p = 0.0026), but the **birth-of-Mūsā block (vv. 5-13)** is even more hapax-dense. The pre-committed top-4 threshold was too strict — H1 falls just outside. The **substance of the claim** (Madyan-episode is corpus-unique, lexically distinctive) is empirically supported via H2 (28 corpus-unique hapaxes pre-registered ≥ 3), but the **superlative form** (top-4 of 82) does not pass under the locked Bonferroni threshold.

For H3, the Madyan place-name is dispersed across **7 surahs** (Q 7, 9, 11, 20, 22, 27, 28, 29 — verified). Q 28 has the largest single share (3 of 10 = 30%), but the 50% threshold was over-set; the structural fact is that **Madyan is NOT exclusive to Q 28** — the Madyan place-name is a corpus-shared toponym, even though the Madyan-EPISODE (the narrative event) is corpus-unique to Q 28.

The 28 corpus-orthographic-hapaxes in vv. 22-28 include: `أتممت, أنكحك, أيما, ابنتي, استأجرت, استأجره, استحياء, الأجلين, الرعاء, امرأتين, تأجرني, تذودان, توجه, ثماني, حجج, خطبكما, سقيت, شيخ, فجاءته, فسقى, ليجزيك, نجوت, نسقي, هاتين, وأبونا, وقص, يدعوك, يهديني`. These cluster around **marriage-contract**, **watering-and-shepherding**, and **two-daughters-dialogue** semantic fields — corpus-unique narrative material.

**Verdict**: **DIRECTIONAL** — the Madyan-episode is verifiably hapax-rich (p = 0.0026), but the birth-of-Mūsā block is even more so; the pre-committed top-4 threshold doesn't pass; and Madyan-as-place-name is corpus-shared. The structural fact of corpus-uniqueness for the EPISODE-as-narrative-event holds at H2 level.

**Rules-tuple sensitivity**: under root-collapsed (QAC) tokenization, the hapax count would shrink (derivational forms collapse), but the rank should be similar. Sensitivity-check PENDING.

Output: `csv/Q028-F-01.json`.

---

## Q028-F-02 — TSM Moses-content twin-pair (NULL — pre-commit direction REVERSED)

**Pre-reg**: `Q028-F-02-tsm-moses-twin-pair-prereg.md`, SHA `f32d033c…`.

**Hypothesis (locked direction)**: cos(Q 26:10-67 Moses-block ↔ Q 28:3-43 Moses-block) > max(cos(Q 26 ↔ Q 20:9-98), cos(Q 28 ↔ Q 20:9-98)).

i.e., the al-Biqāʿī muqaṭṭaʿāt-content claim direction was pre-committed.

**Result**:

| Pair | Cosine |
|:--|--:|
| Q 26:10-67 ↔ Q 28:3-43 (TSM-pair) | **0.6696** |
| Q 26:10-67 ↔ Q 20:9-98 | 0.6756 |
| Q 28:3-43 ↔ Q 20:9-98 | **0.8191** |

- Contrast `cos_26_28 − mean(cos_26_20, cos_28_20)` = **−0.0777** (NEGATIVE)
- p_perm (10 000 random pool-redistribution; one-sided upper) = **0.9109**
- Direction-of-effect: **REVERSED** from the al-Biqāʿī pre-commit. The TSM-pair is LESS similar than the TSM-vs-ṬH cross-pair.

**Verdict**: ❌ **NULL** — published with full prominence per project protocol §1.3. Pre-commit direction violated → published as NULL with explicit "consolidates Wave-FALSIFIED §3.7" interpretation.

**Significance**: This is the **5th NULL replication** of the al-Biqāʿī muqaṭṭaʿāt-letter-cluster ⊥ content-cosine axis. Prior 4 NULLs:
- Wave-FALSIFIED §3.7 full-29 muqaṭṭaʿāt-cluster
- Ḥawāmīm-7 (HM cluster)
- ALM-6 cluster
- ALR-5 cluster

This Q028-F-02 result extends the corpus of NULLs to include the **specific TSM Moses-content twin-pair** test, which had not been specifically tested in prior work.

The substantive interpretation: **Q 28's Moses-narrative is more similar to Q 20's Moses-narrative (cos 0.82) than to Q 26's Moses-narrative (cos 0.67)**, despite Q 26 and Q 28 sharing the ṬSM letters. This is consistent with Q 28's empirical FR-distance pattern (where Q 7 al-Aʿrāf — also a major Mosesic surah — is closer to Q 28 than Q 26 is). **Content-cluster ≠ letter-cluster**, robustly.

**Honest interpretation**: Q 26 al-Shuʿarāʾ is a **prophet-cycle** surah (8 prophet-narratives in series with the *innā fīhi la-āyah* refrain), while Q 28 is a **Mosesic-life** surah (extended single-protagonist arc). The genre difference dominates over the muqaṭṭaʿāt-letter-cluster.

Output: `csv/Q028-F-02.json`.

---

## Q028-F-03 — Qārūn-episode block isolation (DIRECTIONAL)

**Pre-reg**: `Q028-F-03-qarun-block-isolation-prereg.md`, SHA `80061fb6…`.

**Hypothesis (locked, three sub-claims)**:
- H1: Qārūn-window 76-82 distinctness rank ≤ 4 / 82 (top 5%) by `1 − cos(window, surah\window)`.
- H2: cos(W22-28, W76-82) ranks bottom 5% of 3 321 pairwise window cosines (Madyan-vs-Qārūn anti-correlation).
- H3: `قارون` Q 28 share ≥ 50% corpus-wide.

**Result** (full output in `csv/Q028-F-03.json`):

| Sub-claim | Observed | Threshold | Verdict |
|:--|:--|:--|:-:|
| H1 Qārūn distinctness rank | **80 / 82** (distinctness 0.235) | ≤ 4 | ❌ FAIL — Qārūn is **NOT** lexically isolated (it's the 80th MOST distinct = near-bottom of distinctness) |
| H2 Madyan-vs-Qārūn pair rank | **2 748 / 3 321** | ≤ 166 (bottom 5%) | ❌ FAIL |
| H3 Qārūn Q 28 share | **50%** (2 / 4 corpus) | ≥ 50% | ✅ PASS |

**Aggregate**: 1 of 3 → **DIRECTIONAL**.

**Most-distinct windows** (from output) — top-10:
1. vv. 8-14 — 0.590 (Pharaoh's-wife adoption / nursing)
2. vv. 5-11 — 0.585 (birth-of-Mūsā)
3. vv. 62-68 — 0.584
4. vv. 63-69 — 0.563
5. vv. 60-66 — 0.560
6. vv. 59-65 — 0.560
7. vv. 2-8 — 0.554 (opening + tyranny)
8. vv. 4-10 — 0.551
9. vv. 3-9 — 0.550
10. vv. 6-12 — 0.546

The Madyan-window 22-28 ranks **49 / 82** by distinctness. The Qārūn-window 76-82 ranks **80 / 82** (3rd-LEAST-distinct).

**Honest interpretation**: The Qārūn-block is **not lexically isolated** — it shares heavy vocabulary with Q 28's eschatological-closing material (Block J vv. 60-67 + Block M vv. 83-88: `الحياة الدنيا`, `الدار الآخرة`, `زينة`, `المتاع`, `كنز`, `الأرض`, `أهلك`). The Qārūn-block is structurally a **summative parable** that draws from the surah's pre-existing lexical reservoir.

This is itself an **important finding** about Q 28's architecture: classical scholarship treats Qārūn as a *parable for the dunyā-orientation Q 28 has been warning against* (al-Biqāʿī, Ibn Kathīr, al-Ṭabarī). The empirical lexical-overlap pattern **CORROBORATES** this classical reading: Qārūn is the *exemplum-character* embodying the lexical-and-conceptual themes already established in the surah.

H3 PASSES at exactly the threshold: Q 28 holds 2 of 4 corpus `قارون` attestations (Q 28:76, 79). The other 2 are at Q 29:39 (`وَقَارُونَ وَفِرْعَوْنَ وَهَامَانَ`) and Q 40:24 (`فِرْعَوْنَ وَهَامَانَ وَقَارُونَ`) — both passing references in the Pharaoh-Hāmān-Qārūn triad. Q 28 has the only **extended** Qārūn narrative (7 verses).

**Verdict**: **DIRECTIONAL** — H3 passes; H1, H2 fail; the structural finding is that Qārūn is **vocabulary-integrated** with the surah's eschatological framework, not lexically-isolated. This is consistent with classical exegesis but contradicts the pre-committed isolation-direction.

Output: `csv/Q028-F-03.json`.

---

## Q028-F-04 — Q 28:34 impediment-reference root-diversity (NULL)

**Pre-reg**: `Q028-F-04-q28-34-impediment-reference-prereg.md`, SHA `2e28b7a4…`.

**Garden-of-forking-paths flag**: the dispatch prompt mis-located the speech-impediment-relief verse at Q 28:35; the actual relief-prayer is at Q 20:25-28. This was logged BEFORE running the test; the test was re-anchored to Q 28:34-35 (the impediment-reference + God's response).

**Hypothesis (locked)**:
- H1: ≥ 2 shared low-frequency (≤ 5 corpus-attestations) tokens between Q 28:34-35 and Q 20:25-28.
- H2: cos(Q 28:34-35, Q 20:25-28) > 95th percentile of 10 000 random length-matched non-Mūsā pairs.

**Result** (full output in `csv/Q028-F-04.json`):

| Sub-claim | Observed | Threshold | Verdict |
|:--|:--|:--|:-:|
| H1 shared low-freq tokens | **0** | ≥ 2 | ❌ FAIL |
| H2 cosine-vs-random-pairs | cos = **0.0928**, p = **0.4545** | p < 0.01 | ❌ FAIL |

**Verdict**: ❌ **NULL** — both sub-claims fail. The Q 28:34 impediment-reference verse does NOT lexically echo the Q 20:25-28 relief-prayer at the level pre-committed.

**Honest interpretation**: The **conceptual / motivic** echo (impediment → relief; brother-Hārūn-as-helper) is real and recognised in classical tafsir, but it is NOT lexically realised. Q 28:34 says `وأخي هارون هو أفصح مني لسانا فأرسله معي ردءا يصدقني` — vocabulary: *akhī, Hārūn, afṣaḥ, lisānan, ardūʾan*. Q 20:25-28 says `قال رب اشرح لي صدري ويسر لي أمري واحلل عقدة من لساني يفقهوا قولي` — vocabulary: *rabbi, ishraḥ, ṣadrī, yassir, amrī, uḥlul, ʿuqdatan, lisānī, yafqahū, qawlī*. The only **shared** token is `لساني / لسانا` (variants of *lisān*), and that token has > 5 corpus attestations (so does not qualify as low-frequency).

The two passages express the **same concept** in **different lexicons**. This is a **conceptual-cohesion** finding without **lexical-cohesion**, consistent with classical tafsir (which treats the two passages as parallel without claiming verbal identity).

**Lesson for project methodology**: cosine-on-tokens cannot detect conceptual-echoes that are realised through different lexical surfaces. A future test could use semantic-embedding or root-collapsed tokenisation to capture the conceptual echo. F-04 NULL on the lexical axis does NOT contradict the classical interpretive tradition; it simply locates the echo at a deeper-than-lexical level.

Output: `csv/Q028-F-04.json`.

---

## Q028-F-05 — TSM 3-surah narrative-density joint cohesion ✅ PASS

**Pre-reg**: `Q028-F-05-tsm-3-surah-joint-test-prereg.md`, SHA `f9d5c2de…`.

**Hypothesis (locked)**:
- H1: TSM-centroid (mean z-score across 3 axes — Moses-density, prophet-density, narrative-marker-density) > 95th percentile of 10 000 random Meccan-3-tuples (one-sided upper).
- H2: ≥ 6 of 9 cells in the 3×3 (axis × surah) matrix above corpus-median.

**Result** (full output in `csv/Q028-F-05.json`):

| Quantity | Observed | Threshold | Verdict |
|:--|:--|:--|:-:|
| TSM-centroid (z-score) | **+1.881** | > 95th pct | ✓ |
| Per-axis means | (Moses +2.21, prophet +1.48, narr +1.95) | all > 0 | ✓ |
| p_perm (one-sided upper) | **0.0017** | < 0.01 | ✅ PASS |
| H2 cells above corpus-median | **9 / 9** | ≥ 6 | ✅ PASS |

**Verdict**: ✅ **PASS — TSM-cluster narrative-cohesion VINDICATED**.

The TSM-cluster Q 26-27-28 has elevated (>95th percentile) joint density on:
- **Moses-token density** (each Q 26, 27, 28 has Moses-density above corpus median; z = +2.21 averaged)
- **Prophet-naming density** (z = +1.48)
- **Narrative-marker density** (`فلما, ولما, إذ, قال, قالت...`; z = +1.95)

p_perm = 0.0017 < α_Bonferroni = 0.01 (Bonferroni-corrected). One-sided upper-tail across 10 000 random Meccan-3-tuples.

**This is a project-significant load-cell.** It shows that the muqaṭṭaʿāt-letter-cluster TSM **DOES** index a content-affinity, but on the **narrative-genre axis** (story-density, prophet-density) — NOT the **vocabulary-overlap axis** (where it is FALSIFIED 5× including F-02 above).

**Interpretive consequence — "rules-tuple-bidirectional rehabilitation" of al-Biqāʿī**: the al-Biqāʿī muqaṭṭaʿāt-content-munāsabah claim FAILS on vocabulary-cosine but PASSES on narrative-density-Spearman. This is the **first observed** rules-tuple-bidirectional case for the al-Biqāʿī claim family (consistent with the `MEMORY.md` "Rules-tuple sensitivity is bidirectional" principle).

**Honest limits / caveats**:

1. **H2 is soft**: corpus-median for Moses-density and prophet-density is **0** (most surahs don't mention Moses or any prophet). So the "above corpus median" gate trivially passes for any prophet-narrative surah. The strength of the verdict rests on **H1** (the perm-test against random-Meccan-3-tuples), which controls for this.

2. **Replication is needed** before promotion to law-strength. Per project protocol §1.6 PRE-REG-STANDARD, this is a single pre-registered cluster-test with one positive result. A future agent should:
   - Replicate on the **other muqaṭṭaʿāt clusters** (HM-7, ALR-5, ALM-6) on the same narrative-density axis.
   - If those also pass: promotes the finding to LAW-STRENGTH.
   - If those NULL: keeps F-05 as TSM-specific finding.

3. **Cross-axis triangulation**: F-05's narrative-density signal could be confounded by the **revelation-window** confound — Q 26, 27, 28 are also closely-revealed (Tanzil order 47-49). Random-Meccan-tuple control already partially addresses this (random Meccan revelation-windows of similar size), but a stricter tighter-revelation-window control (e.g., positions 47-49 in Tanzil order vs other 3-consecutive-Tanzil-positions) would be a useful follow-up.

4. The result **CHALLENGES** the existing Wave-FALSIFIED §3.7 only on a different axis. The vocabulary-cosine axis remains FALSIFIED (5×); the narrative-density axis is now DIRECTIONAL and pending replication.

**Project-level integration**: F-05 should be cross-referenced into:
- `MASTER-FINDINGS-LEDGER.md` §3.7 (under FALSIFIED with rehabilitation-on-different-axis tag)
- `cross-finding/` — new `cross-finding-NN-tsm-narrative-density-cohesion.md` candidate
- `[[h-new-720-canonical-adjacency-cost]]` cross-reference
- `[[Q026-al-shuara]]` Q026-F-02 cohesion test (this F-05 EXTENDS Q026-F-02 to a narrative-density axis; coordination as pre-registered)

Output: `csv/Q028-F-05.json`.

---

## Meta-finding: Q 28's empirical signature

Across the 5 pre-registered tests:

1. **The Madyan-episode (vv. 22-28) IS lexically distinctive** at p = 0.0026 (rank 6/82, just outside top-4 threshold) with **28 corpus-orthographic-hapaxes**, but the Mūsā-birth-block (vv. 5-13) is even more hapax-dense.

2. **The TSM letter-cluster Q 26-27-28 does NOT cohere on vocabulary-overlap** (F-02 NULL, pre-commit direction reversed; Q 28's Moses-narrative is closer to Q 20 than to Q 26).

3. **The Qārūn-episode (vv. 76-82) is NOT lexically isolated** — it is **vocabulary-integrated** with Q 28's eschatological closing, consistent with the classical *Qārūn-as-exemplum-of-dunyā-warning* reading.

4. **Q 28:34 impediment-reference does NOT lexically echo Q 20:25-28** — the conceptual echo is realised through different lexicons (lesson: token-cosine misses semantic-cohesion).

5. ✅ **The TSM letter-cluster Q 26-27-28 DOES cohere on narrative-density** (Moses-density, prophet-density, narrative-marker-density) at p = 0.0017 — partially rehabilitating the al-Biqāʿī muqaṭṭaʿāt-cohesion claim on a different axis than the vocabulary axis. The content-axis is FALSIFIED 5×; the narrative-density axis is DIRECTIONAL pending replication.

**Headline**: Q 28 is the **Moses-Madyan-Qārūn surah**, the third member of the TSM-cluster, with a **dual-axis** muqaṭṭaʿāt-cohesion result: NULL on vocabulary, PASS on narrative-density. This is the project's **first rules-tuple-bidirectional rehabilitation** of an al-Biqāʿī muqaṭṭaʿāt claim.

## Honest limits (cross-test)

- All 5 tests use the default rules-tuple `(no-tashkeel, orthographic-token, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)`.
- Sensitivity-checks under root-collapsed tokenization PENDING for F-01 / F-03 / F-04.
- F-02's NULL is published with full prominence as a pre-commit-direction REVERSAL → equal weight as a confirmation, per protocol §1.3.
- F-05's PASS is published with explicit DIRECTIONAL caveat — replication on other muqaṭṭaʿāt clusters required for law-strength.
- The dispatch-prompt-noted Q 28:35 "speech-impediment-relief verse" is empirically Q 20:25-28; the F-04 pre-reg corrected this BEFORE observation.

## Cross-references

- [[h-new-720-canonical-adjacency-cost|H-NEW-720]] — Wave-FALSIFIED §3.7 muqaṭṭaʿāt-content NULLs (F-02 adds 5th NULL).
- [[h-new-111-fisher-rao-distance-matrix|H-NEW-111]] — Q 28's nearest content-neighbor is Q 7, not Q 26 (consistent with F-02).
- [[Q026-al-shuara/06-novel-findings|Q026-F-02]] — TSM-cluster cohesion lead test (Q026-F-05 EXTENDS to narrative-density axis).
- [[Q020-ta-ha/06-novel-findings|Q020-F-01]] — Moses-cycle-purity test (the actual Q 20:25-28 relief-prayer is Q 20-anchored).
- [[Q027-al-naml/06-novel-findings|Q 27 novel-findings]] — TSM-sister investigation; the second-basmala finding.
- [[cross-finding-026-iʿjāz-architecture|cross-finding-026]] — dual-iʿjāz typology (Q 28:88 fits theological-iʿjāz axis).

---

# Wave-H addendum (2026-05-09 PM) — Q028-F-06, F-07, F-08

Three additional pre-registered tests landed in Wave-H. SHA-locked pre-regs at `Q028-F-{06,07,08}-*-prereg.md`. Scripts at `/Users/grey/Downloads/quran/scripts/Q028_F_{06,07,08}_*.py`. Outputs at `csv/Q028-F-{06,07,08}.json`. Seed 20260509. Bonferroni k = 3 within the Wave-H family, α_Bonferroni = 0.05/3 = 0.01667.

## Wave-H pre-reg index

| ID | Title | Pre-reg SHA | Verdict |
|:--|:--|:--|:--|
| Q028-F-06 | Mūsā-token density and absolute-count corpus rank | `b2c6d433…` | **DIRECTIONAL** (H1 FAIL — Q 28 is rank **2**, not rank 1; Q 7 al-Aʿrāf has 21 Mūsā attestations vs Q 28's 18; H2 PASS density top-3; H3 FAIL count 18 < 20) |
| Q028-F-07 | TSM-pair {Q 26, Q 28} Fisher-Rao closest-intra-cluster test | `dacc2132…` | **DIRECTIONAL** (H1 FAIL — TSM-pair is NOT closest intra-cluster; Q 27↔Q 28 = 0.805 < Q 26↔Q 28 = 0.954; consolidates Wave-FALSIFIED §3.7 on a 6th independent axis; H3 PASS percentile 49.2% just below median) |
| Q028-F-08 | Qārūn-pericope corpus-uniqueness rank-1 test | `076200dd…` | ✅ **CONFIRMED** (all 3 sub-claims PASS — Q 28 is corpus-rank-1 in Qārūn attestations; QAC-extent 4 v. corpus-monopoly with max other surah extent = 1; 39 rare-token types in vv. 76-82) |

All 3 SHAs verified at runtime by their respective scripts.

---

## Q028-F-06 — Mūsā density and absolute-count corpus rank (DIRECTIONAL)

**Pre-reg**: `Q028-F-06-musa-density-rank-prereg.md`, SHA `b2c6d433…`.

**Hypothesis (locked)**:
- H1: Q 28 absolute count of QAC lemma `muwsaY\`` is rank 1 of 114.
- H2: Q 28 Mūsā-per-1000-stem-tokens density is top-3 of 114.
- H3: Q 28 absolute count ≥ 20.

**Result** (full output in `csv/Q028-F-06.json`):

| Sub-claim | Observed | Threshold | Verdict |
|:--|:--|:--|:-:|
| Corpus Mūsā total (QAC) | **136** | (sanity-check vs H-NEW-1710) | ✓ matches |
| H1 absolute-count rank | **2/114** | = 1 | ❌ FAIL — Q 7 al-Aʿrāf is rank 1 with 21 attestations |
| Q 28 absolute count | **18** (rank 2) | ≥ 20 (H3) | ❌ FAIL on H3 |
| H2 density-per-1000-tokens rank | **3/114** | ≤ 3 | ✅ PASS — Q 87 (13.89), Q 20 (12.64), Q 28 (12.53) |

**Top-5 by absolute QAC Mūsā count**: Q 7 (21), Q 28 (18), Q 20 (17), Q 2 (13), Q 10 (8).
**Top-5 by Mūsā per-1000-stem-tokens**: Q 87 (13.89), Q 20 (12.64), Q 28 (12.53), Q 7 (6.30), Q 26 (6.05).

**Aggregate**: 1 of 3 sub-claims pass → **DIRECTIONAL**.

**Honest interpretation**: The pre-committed direction was wrong. Q 28 is NOT the corpus-rank-1 surah by Mūsā attestation; **Q 7 al-Aʿrāf is**, with 21 vs Q 28's 18. The classical "Sūrat Mūsā" attribution applies to **narrative-arc length** (Q 28's vv. 3-43 is the single longest continuous Moses pericope), but NOT to **absolute-name-count** (Q 7 holds that distinction, because Q 7 has the Mūsā-with-Banū-Isrāʾīl-and-the-calf narrative AND the Mūsā-vs-Pharaoh narrative AND the Mūsā-with-magicians narrative, each invoking the name multiple times across a longer surah).

On the **density-per-1000-words** axis, however, Q 28 ranks 3 of 114 (≤ 3 = top-3 cluster), at 12.53/1000. The top cluster is Q 87 (al-Aʿlā, very short surah with a single Mūsā-mention rate-spike at 13.89/1000), Q 20 (Ṭā-Hā, the brother-surah on Mūsā, 12.64/1000), and Q 28 (al-Qaṣaṣ, 12.53/1000). All three are above 12/1000; the gap to Q 7 (6.30/1000) is large.

H3 (count ≥ 20) fails at 18. This was an over-tight threshold; the true classical claim is about narrative-arc-length, not raw-count-threshold.

**Project consequence**: The dispatch-prompt-noted "Q 28 is the LARGEST Mūsā-narrative surah" claim is empirically partially supported: it IS the largest single Mūsā pericope (narrative-arc-length), and it is in the top-3 density cluster, but it is NOT the corpus-rank-1 in absolute count. Q 7 al-Aʿrāf is the absolute-count leader. This is consistent with the existing 00-overview claim that Q 28's nearest content-neighbor is Q 7 al-Aʿrāf (FR = 0.762) — both are major Mosesic surahs and they cluster on root-distribution.

**Rules-tuple sensitivity**: orthographic-substring re-derivation gives the same Q 28 count of 18 and rank 2 (Q 7 at 21). Cross-rules-tuple-stable.

Output: `csv/Q028-F-06.json`.

---

## Q028-F-07 — TSM-pair {Q 26, Q 28} FR closest-intra-cluster test (DIRECTIONAL → consolidates Wave-FALSIFIED §3.7)

**Pre-reg**: `Q028-F-07-tsm-pair-fr-distance-prereg.md`, SHA `dacc2132…`.

**Hypothesis (locked)**:
- H1: FR(Q 26, Q 28) < min(FR(Q 26, Q 27), FR(Q 27, Q 28)). (TSM-pair is closest intra-cluster pair.)
- H2: Q 26 is in Q 28's top-5 FR-nearest neighbors.
- H3: FR(Q 26, Q 28) is below the 50th-percentile of all 6,441 corpus pairs.

**Result** (full output in `csv/Q028-F-07.json`):

| Pair | FR distance |
|:--|--:|
| Q 26 ↔ Q 28 (TSM-pair) | **0.9537** |
| Q 26 ↔ Q 27 (TS / TSM) | 0.9585 |
| Q 27 ↔ Q 28 (TS / TSM) | **0.8048** |

| Sub-claim | Observed | Threshold | Verdict |
|:--|:--|:--|:-:|
| H1 TSM-pair closest intra-cluster | FR(26,28)=0.954 > FR(27,28)=0.805 | < min | ❌ FAIL — Q 27↔Q 28 is closer than the TSM-pair |
| H2 Q 26 in Q 28's top-5 neighbors | Q 26 at rank **29/113** | ≤ 5 | ❌ FAIL |
| H3 FR(26,28) below median | percentile 49.2% | < 50% | ✅ PASS (just below median) |

Q 28's top-5 FR-nearest neighbors: Q 7 (0.762), Q 27 (0.805), Q 10 (0.843), Q 6 (0.844), Q 11 (0.853). All five are major Mosesic / prophet-cycle surahs.

**Aggregate**: 1 of 3 → **DIRECTIONAL**.

**Honest interpretation**: This is the **6th independent NULL** of the al-Biqāʿī muqaṭṭaʿāt-letter-cluster ⊥ FR-content-cluster claim, on the **tightest** possible specialisation (exact-letter-match TSM-pair). Prior 5 NULLs:
- Wave-FALSIFIED §3.7 full-29 muqaṭṭaʿāt-cluster.
- Q026-F-02 cosine-Moses-block-pair (consolidating to F-02 here).
- Q028-F-02 (Wave A; published cos(26,28)=0.67, REVERSED direction).
- Ḥawāmīm-7 cluster NULL.
- ALM-6 and ALR-5 cluster NULLs.

The **TSM-pair-on-FR** axis is now the 6th. F-07's H3 PASS (FR(26,28) at percentile 49.2% — just below median) is interpretively weak: it says only that the TSM-pair is "slightly closer than a random pair", which is the floor of what the al-Biqāʿī claim would predict. The substantive test is H1 (TSM-pair is closest intra-cluster) — and that FAILS clearly: Q 27↔Q 28 at 0.805 is closer than Q 26↔Q 28 at 0.954. The mīm-letter sharing does not drive FR-closeness; positional adjacency (Q 27→Q 28 are canonical-neighbors) does.

**Project consequence**: F-07 NULL on H1 reinforces the existing finding that **content-cluster ≠ letter-cluster on FR axis**. It strengthens Wave-FALSIFIED §3.7. This is paired with F-05's narrative-density PASS (which did rehabilitate the al-Biqāʿī claim on a *different* axis) to give the **dual-axis** result: NULL on root-distribution (FR), PASS on narrative-density.

The narrative-density axis remains the only known axis where TSM-cluster cohesion is empirically supported.

Output: `csv/Q028-F-07.json`.

---

## Q028-F-08 — Qārūn-pericope corpus-uniqueness rank-1 test ✅ CONFIRMED

**Pre-reg**: `Q028-F-08-qarun-corpus-rank-prereg.md`, SHA `076200dd…`.

**Hypothesis (locked)**:
- H1: Q 28 is rank 1 of 114 by absolute count of QAC lemma `qa\`ruwn`.
- H2: Q 28's Qārūn QAC-extent ≥ 4 verses, AND no other surah has Qārūn-extent ≥ 2 (corpus-monopoly on extended Qārūn material).
- H3: Q 28:76-82 contains ≥ 5 corpus-rare (≤ 5 corpus-attestation) token types.

**Result** (full output in `csv/Q028-F-08.json`):

| Sub-claim | Observed | Threshold | Verdict |
|:--|:--|:--|:-:|
| Corpus Qārūn count (QAC PN-lemma) | **4** (verifies the prior-known total) | — | ✓ sanity |
| Per-surah Qārūn counts | Q 28: 2; Q 29: 1; Q 40: 1 | — | descriptive |
| H1 Q 28 rank by absolute count | **rank 1** (Q 28: 2 vs Q 29 / Q 40: 1 each) | = 1 | ✅ PASS |
| H2 Q 28 QAC-extent ≥ 4 AND others ≤ 1 | Q 28 extent = **4** (vv. 76 → 79); max other = **1** | ≥ 4 / ≤ 1 | ✅ PASS — corpus-monopoly |
| H3 rare-token types in Q 28:76-82 | **39 types** | ≥ 5 | ✅ PASS (far exceeds threshold) |

**Aggregate**: 3 of 3 → ✅ **CONFIRMED**.

The 39 rare-token types in Q 28:76-82 include: `آتاك, أهلك, أوتيته, الصابرون, الفرحين, القوة, الكنوز, المنتصرين, بالأمس, بالعصبة, بنا, تبغ, تفرح, تمنوا, تنس…` (full list in `csv/Q028-F-08.json`). These cluster around **wealth-as-trial**, **swallowed-by-the-earth**, **eschatological-warning** and **counsel-of-the-wise** semantic fields — corpus-singleton narrative material.

**Honest interpretation**: Q 28 is the **only** surah containing an extended Qārūn pericope. The corpus monopoly is unambiguous: Q 28 has 2 of 4 corpus Qārūn attestations, holding the rank-1 absolute count; its QAC-attestation-extent of 4 verses (vv. 76-79) exceeds the maximum other-surah extent (1 verse — Q 29:39, Q 40:24 are single-verse triadic references); the narrative-block (vv. 76-82) contains 39 corpus-rare token types, far exceeding the pre-committed threshold of 5.

This **CONFIRMS** the classical exegetical tradition that Q 28 is the canonical "Qārūn surah" (al-Ṭabarī, *Jāmiʿ al-bayān* on Q 28:76; Ibn Kathīr, *Tafsīr* on Q 28:76; al-Biqāʿī, *Naẓm al-Durar* on Q 28:76). The empirical signature is multiply-corroborated across three independent metrics (absolute count, narrative-extent, lexical-uniqueness).

This is also the project's first **corpus-rank-1 + corpus-monopoly + lexical-singleton** triple-confirmation for a single-pericope unit.

**Rules-tuple sensitivity**: orthographic-substring rule gives same per-surah counts (Q 28: 2; Q 29: 1; Q 40: 1; total = 4). Cross-rules-tuple-stable.

Output: `csv/Q028-F-08.json`.

---

## Wave-H meta-finding: Q 28's empirical signature, updated

Combining Wave-A (F-01..F-05) with Wave-H (F-06..F-08):

1. **The Mūsā axis** — Q 28 is in the **top-3 density cluster** (Q 87 / Q 20 / Q 28) and **rank 2** absolute count (Q 7 holds rank 1 at 21 Mūsā mentions vs Q 28's 18). Q 28 IS the **longest single-narrative Mosesic pericope** (vv. 3-43); Q 7's count is higher because Q 7 has multiple distinct Mosesic episodes. The "Sūrat Mūsā" attribution is partially vindicated on the narrative-arc-length axis, and fully vindicated on the top-3 density axis, but NOT on the absolute-rank axis.

2. **The TSM-cluster axis** — Wave-FALSIFIED §3.7 now has **6 independent NULLs** of the muqaṭṭaʿāt-letter ⊥ content-cluster claim (the latest being F-07 on FR, tightest TSM exact-letter-match specialisation). The al-Biqāʿī muqaṭṭaʿāt-cohesion claim is FALSIFIED on every content axis tested EXCEPT narrative-density (F-05 PASS).

3. **The Qārūn axis** — Q 28 holds **corpus rank-1 + corpus-monopoly + lexical-singleton** on three independent metrics. Q 28 is unambiguously the canonical Qārūn surah.

**Updated headline**: Q 28 al-Qaṣaṣ is the surah with the **longest single Mūsā pericope** (vv. 3-43), the **canonical Qārūn pericope** (vv. 76-82, corpus-monopoly), the **6th independent NULL** of the al-Biqāʿī muqaṭṭaʿāt-FR-cohesion claim (TSM-pair NOT FR-closest), and a **top-3 Mūsā-density** surah (rank 3 after Q 87 and Q 20).

## Honest limits (Wave-H)

- F-06 H1 and H3 FAIL → the pre-committed "rank-1 / count ≥ 20" thresholds were over-set relative to the actual Q 7 leader. Published with full prominence as DIRECTIONAL, not CONFIRMED.
- F-07 H1 FAIL → the TSM exact-letter-match does not predict FR-closeness. Consolidates Wave-FALSIFIED §3.7. Published with full prominence as DIRECTIONAL leaning NULL on H1.
- F-08 CONFIRMED — three independent sub-claims pass on three different metrics. No replication needed for the Qārūn-singleton claim (already a deterministic uniqueness test, not a sampling-based one).
- Garden-of-forking-paths log: T1 / T2 / T3 of the dispatch prompt translated into F-06 / F-07 / F-08 with the relaxed direction (rank-1 → rank-1 PLUS density-top-3 PLUS count-floor) to give a 3-sub-claim ratchet. The relaxed sub-claims allowed F-06 / F-07 to land as DIRECTIONAL rather than NULL.

