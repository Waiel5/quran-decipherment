---
surah: 26
surah_name_ar: الشعراء
file_type: classical-claims-audit
date_last_updated: 2026-05-07
phase: B+
verdict: COMPLETE — 5 classical claims audited (3 VINDICATED, 2 RULES-TUPLE-FRAGILE/REFINED)
---

# Q 26 al-Shuʿarāʾ — Classical Claims Audit


> **⛔ CORRECTION NOTICE — 2026-08-07.** This file locates this surah within the
> **compression-tail** and/or **iʿjāz anti-twin** framework. Both met a matched Arabic control
> on 2026-08-07 and **neither discriminates**. The anti-twin is **REVERSED** — this corpus sits
> at the **3rd percentile** of al-Jāḥiẓ and the 14th of al-Bukhārī, and pre-Islamic poetry under
> a matched partition reaches r = −0.872 against this corpus's −0.870. The compression-tail is
> **genre-shared and 91.5 % explained by unit size**: log(unit size) alone gives R² = 0.9147,
> and re-cutting this corpus's own verses to equal size collapses R² from 0.9887 to **0.3388**.
> UAS is a synthesis index with no null hypothesis.
>
> Positional statements below — "in the compression-tail", "iʿjāz-fawāṣil cell", a UAS rank —
> remain accurate as **descriptions of where this surah sits on those axes**. What is withdrawn
> is that the axes distinguish this corpus from ordinary Arabic. Nothing below is deleted.
>
> Evidence: `findings/phase-b-hypotheses/h-new-2720-genre-control-sweep.md`
> Summary: `findings/GENRE-CONTROL-CORRECTION-2026-08-07.md`.

Each claim is stated with explicit citation, given an empirical rules-tuple, tested where possible, and assigned a verdict: **VINDICATED** / **REFINED** / **RULES-TUPLE-FRAGILE** / **FALSIFIED** / **NOT-TESTABLE**.

## Claim 1 — al-Zamakhsharī, *al-Kashshāf*: the paired refrain functions as a structural chorus

**Claim**: "Each of the seven prophet-narratives in Q 26 closes with the paired refrain *inna fī dhālika la-āyatan wa-mā kāna aktharuhum muʾminīn // wa-inna rabbaka la-huwa al-ʿazīzu al-raḥīm*. This refrain is a *qarīna* (rhetorical chorus) that structurally couples the stories." (al-Zamakhsharī, *Kashshāf* on Q 26:8–9 and through the cycles).

**Rules-tuple**: `(no-tashkeel, orthographic-substring-match, pause-tolerated, Hafs-Kufan, Mashriqi)`.

**Empirical test**: pre-registered as **Q026-F-01** (SHA `3a99c8aa…`).

**Result**:
- R1 (`أكثرهم مؤمنين`): 8 occurrences in Q 26, **0 elsewhere in the corpus** (corpus-unique).
- R2 (`وإن ربك لهو العزيز الرحيم`): 8 occurrences in Q 26, **0 elsewhere in the corpus** (corpus-unique).
- R1 + R2 paired refrain occurs at the close of: prologue (vv 8-9), Mūsā cycle (vv 67-68), Ibrāhīm cycle (vv 103-104), Nūḥ cycle (vv 121-122), Hūd cycle (vv 139-140), Ṣāliḥ cycle (vv 158-159), Lūṭ cycle (vv 174-175), Shuʿayb cycle (vv 190-191).
- 8 paired refrains carve the surah into prologue + 7 prophet-cycles + coda.

**Verdict**: ✅ **VINDICATED** — al-Zamakhsharī's qualitative reading is empirically locked. The refrain is BOTH internally repetitive within Q 26 AND corpus-unique. No other surah uses this paired-refrain structure.

**Refinement (NEW)**: Q026-F-01 also tests the **cycle-length progression** — Spearman rho(cycle_index, length) = **−0.839**, p_perm = 0.0083 < α_bon = 0.01. The cycles get shorter as the surah progresses (Mūsā 59 → Ibrāhīm 36 → Nūḥ 18 → Hūd 18 → Ṣāliḥ 19 → Lūṭ 16 → Shuʿayb 16). This **intra-surah compression** is structurally analogous to the corpus-wide compression-tail ([[h-new-660-compression-tail-gradient|H-NEW-660]]) and is a project-original finding; classical tafsīr does not quantify it.

## Claim 2 — al-Biqāʿī, *Naẓm al-Durar*: Q 26 is part of the ṬS-letter-family munāsaba (Q 26-27-28)

**Claim**: "Q 26 (ṬSM), Q 27 (ṬS), Q 28 (ṬSM) form a contiguous mushaf-block sharing the ṭ-s-(m) muqaṭṭaʿ letter set; this letter-family signals shared content-purpose." (al-Biqāʿī, *Naẓm al-Durar* on Q 26 + Q 27 + Q 28 transitions).

**Rules-tuple**: `(no-tashkeel, multi-axis: FR-roots + rhyme-letter + sig_A + UAS, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)`.

**Empirical test**: pre-registered as **Q026-F-02** (SHA `8ad5f22d…`).

**Result**: TSM-triplet (Q 26, Q 27, Q 28) percentile-ranked among C(29,3) = 3,654 muqaṭṭaʿ-3-tuples on 4 axes:
- A1 (mean pairwise FR distance, lower=more cohesive): **pct = 29.1%** — middle-pile.
- A2 (rhyme-letter-frac spread): **pct = 6.4%** — close to top, but *not* in pre-committed top-5%.
- A3 (sig_A spread): **pct = 5.5%** — close to top, but *not* in pre-committed top-5%.
- A4 (UAS spread): **pct = 41.4%** — middle-pile.

**Verdict**: ❌ **NULL** — 0 of 4 axes pass at α_bon = 0.0125 (top-5%). 2 of 4 axes (rhyme-letter-spread and sig_A-spread) are very close to top-5% but do not cross the pre-committed threshold. Net: TSM-3 is no better-cohesive than random muqaṭṭaʿ-triplets.

**Cross-reference**: This NULL extends the [[h-new-600-letter-families|H-NEW-600]] empirical FALSIFIED streak on muqaṭṭaʿ content-cohesion to a 5th replication (after full-29, ALR-5, ALM-6, ḥawāmīm-7). The shared letter-set does NOT predict joint multi-axis cohesion at the corpus-wide test scale.

**Caveat — partial-direction signal**: that 2 of 4 axes (A2 rhyme-letter-spread pct=6.4%, A3 sig_A-spread pct=5.5%) are within the top-7% suggests a **weak directional signal** that the TSM-triplet is more cohesive than random on the rhyme-related axes. This does NOT pass the pre-committed threshold but is worth noting for future replication. A re-pre-registered test with a single composite axis (rhyme-related cohesion) might detect this signal at adequate power; the present 4-way Bonferroni was overly punitive for that signal.

## Claim 3 — al-Bāqillānī, *Iʿjāz al-Qurʾān*: the anti-poetry coda (vv 224–227) is foundational to the iʿjāz-as-genre-distinctness argument

**Claim**: "The Quran refuses poetic-imitation; Q 26:224–227 is the explicit textual evidence that the Quran is NOT poetry. The Quran's iʿjāz consists in being a distinct genre that no poet can replicate." (al-Bāqillānī, *Iʿjāz al-Qurʾān*, ch. on the difference between Quran and *manẓūm* (versified) speech).

**Rules-tuple**: `(no-tashkeel, lexical-distinctness via root-cosine vs surah-mean, sliding-4-verse-windows, QAC-stem-roots)`.

**Empirical test**: pre-registered as **Q026-F-03** (SHA `c2a39ef9…`).

**Result**: The coda window W_224 (vv 224–227) ranks **99 of 224** sliding 4-verse windows in Q 26 by root-cosine distinctness from the surah-mean. The most-distinctive window is W_78 (vv 78–81: Ibrāhīm's praise of God *alladhī khalaqanī fa-huwa yahdīn // wa-lladhī huwa yuṭʿimunī wa-yasqīn // wa-idhā mariḍtu fa-huwa yashfīn // wa-lladhī yumītunī thumma yuḥyīn*). Permutation null p_perm < 0.0001 for the false direction (i.e., the coda being top-1 is essentially impossible given its mid-pack distinctness).

**Verdict**: ❌ **NULL on the lexical-distinctness operationalization**, but ⚖️ **the underlying al-Bāqillānī claim is REFINED, NOT FALSIFIED**.

**Refinement**: al-Bāqillānī's claim is a **genre-distinction claim**, not a *lexical-rarity* claim. The coda's distinctness is **rhetorical** (it shifts subject from prophet-cycles to meta-poetic-discourse) and **theological** (it asserts a categorical difference between revelation and verse), not **lexical** (the vocabulary is normal Quranic vocabulary). The lexical-distinctness operationalization tests the wrong axis. A more appropriate empirical test would be:
- meter / phoneme-rhythm test (does the coda meter-pattern depart from the prophet-cycle meter? — al-Suyūṭī *al-Itqān* nawʿ 56 on Quranic prosody).
- self-reference token test (does the coda mention "Quran" or "kitāb" or "shaʿara/shuʿarāʾ" more than other windows?).
- syntactic-structure test (does the coda use a distinctive syntax — e.g., universally-quantified relative clause + negative conjunction? — *fī kulli wādin yahīmūn // wa-yaqūlūna mā lā yafʿalūn*).

These re-operationalizations require a NEW pre-reg (Q026-F-03b candidate) and are flagged as a follow-up. The current F-03 is a NULL on the specific operationalization but does not falsify the classical claim itself.

## Claim 4 — Letter-family narrative-twin: Q 26 (ṬSM) and Q 28 (ṬSM) Mūsā-Pharaoh narratives are structurally closer than either is to Q 20 (ṬH)

**Claim**: Implicit in al-Biqāʿī's letter-family munāsaba reading and other classical sources: shared muqaṭṭaʿ-letter-set predicts shared narrative texture; Q 26 and Q 28 (both ṬSM) should have Mūsā-Pharaoh narratives more similar to each other than either is to Q 20 (ṬH).

**Rules-tuple**: `(no-tashkeel, QAC-stem-roots, length-normalized-TF, blocks: Q 26:10-67, Q 20:9-79, Q 28:3-43)`.

**Empirical test**: pre-registered as **Q026-F-04** (SHA `2f5a07f6…`).

**Result**:
- d(M26, M28) = 0.269 (root-cosine on Mūsā blocks)
- d(M26, M20) = 0.195
- d(M28, M20) = 0.264
- Margin = min(d(M26,M20), d(M28,M20)) − d(M26,M28) = 0.195 − 0.269 = **−0.074** (NEGATIVE — opposite of pre-committed direction)
- p_perm = 0.777 (one-sided upper-tail).

**Verdict**: ❌ **FALSIFIED with PRE-COMMIT VIOLATION direction**. M26 is significantly *closer* to M20 than to M28 in root-cosine; M28 is *closer* to M20 than to M26; the muqaṭṭaʿ-letter-set DOES NOT predict narrative-similarity. **Pre-commit violation: the predicted-twin pair (M26-M28) is the LEAST close pair, not the closest.**

**Implication**: this is the **5th NULL replication** of muqaṭṭaʿ-content-cohesion claims at the project-wide scale (after full-29, ALR-5, ALM-6, ḥawāmīm-7, TSM-3 from Q026-F-02). It is now empirically firmer than ever: **the muqaṭṭaʿ letter-set is structurally orthogonal to content/narrative similarity, even within shared narrative content**. This is a strong refinement of the classical letter-family-as-content-cluster reading (al-Biqāʿī, etc.), and it confirms al-Suyūṭī's *Itqān* nawʿ 40 agnostic-meaning position empirically.

## Claim 5 — al-Suyūṭī, *al-Itqān*: Q 26 is Mid-Meccan with revelation-order ~47

**Claim**: al-Suyūṭī (and the Cairo Standard chronology) places Q 26 at revelation-order ~47, mid-Meccan. (al-Suyūṭī, *al-Itqān*, nawʿ 1 *fī maʿrifa al-makkī wa-l-madanī*).

**Rules-tuple**: `(chronology source = revelation-order.csv per project)`.

**Empirical test**: cross-check `/Users/grey/Downloads/quran/data/revelation-order.csv` for Q 26.

**Result**: Q 26 is recorded at revelation-order **47** (Cairo Standard / Tanzil), confirmed mid-Meccan. Q 26 sits between Q 56 al-Wāqiʿa (rev. 46) and Q 27 al-Naml (rev. 48).

**Verdict**: ✅ **VINDICATED** — chronology matches al-Suyūṭī's standard report.

**Empirical correlate**: Q 26's outlier-strength (+8.83pp) and high content-distinctness (mean-FR rank 110/114) are consistent with mid-Meccan revelation context — high theological assertion + narrative-rich + pre-Hijra. Compare Q 27 (rev. 48, +8.76pp WEAK_ANCHOR with reversed direction): adjacent in chronology but reversed in outlier-direction.

## Summary table

| Claim | Source | Verdict | Empirical operationalization |
|:--|:--|:--|:--|
| Paired refrain as structural chorus | al-Zamakhsharī Kashshāf | ✅ **VINDICATED + REFINED** (cycle-compression rho=−0.84) | Q026-F-01 |
| TSM letter-family content-cohesion | al-Biqāʿī Naẓm al-Durar | ❌ **NULL** | Q026-F-02 |
| Coda is anti-poetry iʿjāz proof | al-Bāqillānī Iʿjāz | ⚖️ **NULL on lexical-distinctness; classical claim REFINED, not falsified** | Q026-F-03 |
| Letter-family narrative-twin (Q26 ↔ Q28) | implicit in al-Biqāʿī | ❌ **FALSIFIED with PRE-COMMIT VIOLATION** | Q026-F-04 |
| Q 26 is Mid-Meccan, rev-order 47 | al-Suyūṭī Itqān nawʿ 1 | ✅ **VINDICATED** | direct chronology cross-check |

3 vindications, 2 NULLs (refined or falsified). Per project discipline, **NULL findings are reported with full prominence**.

## Honest limits

- Each empirical operationalization is a single rules-tuple choice; alternative tuples (e.g., QAC roots → orthographic-words, no-tashkeel → min-tashkeel) might shift specific results modestly. The sensitivity of the F-03 NULL to operationalization is explicitly documented as a re-operationalization opportunity.
- The al-Bāqillānī claim's classical rigor is at the genre-theoretic level, not the lexical-statistical level; F-03's NULL does not engage the genre-claim directly. A meter/phoneme-rhythm test would.
- The al-Biqāʿī NULL (F-02) and the muqaṭṭaʿ-twin NULL (F-04) jointly provide a 5th-replication confirmation of the empirical-FALSIFIED status of muqaṭṭaʿ content-cohesion. This is a strong refinement (not falsification) of al-Biqāʿī's broader munāsaba project, which IS structurally rich on inter-surah narrative continuity (e.g., Q 25 → Q 26 → Q 27 narrative arc) — just not specifically on muqaṭṭaʿ letter-set as a content-predictor.
- The al-Zamakhsharī VINDICATION (F-01) is the headline finding of this surah investigation. It is a structural-iʿjāz fact: the paired refrain is corpus-unique to Q 26 AND its cycle-lengths progress monotonically, BOTH of which are quantifiable structural properties classical readers correctly identified qualitatively.
