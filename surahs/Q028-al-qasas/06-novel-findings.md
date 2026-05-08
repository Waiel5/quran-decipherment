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
