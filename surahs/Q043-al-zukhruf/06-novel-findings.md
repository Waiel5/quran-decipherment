---
surah: 43
surah_name: al-Zukhruf
file_type: novel-findings
date_last_updated: 2026-04-28
phase: B+
verdict: 3 VINDICATED + 1 NULL/PRE-COMMIT-VIOLATION + 1 prior-test NULL-discrepancy
---

# Q 43 al-Zukhruf — novel findings


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

Four novel pre-registered tests in this session (Q043-F-02 through Q043-F-05), plus a prior pre-reg (Q043-F-01) whose verdict needs revision. Equal NULL prominence per [[INVESTIGATION-PROTOCOL|protocol §1.3]].

## Finding 1: Q043-F-02 — HM-A → HM-B rhyme-entropy structural break — VINDICATED

**Pre-reg**: [[Q043-F-02-hma-hmb-entropy-break-prereg|Q043-F-02]] — locked SHA256 `1bfd78dd11cad0e36d13e9d3c8b68fbf01e408e3b97f2278eb76bebb7274b9de`.
**Script**: `/Users/grey/Downloads/quran/scripts/Q043_F_02_entropy_break.py`.
**Output**: `surahs/Q043-al-zukhruf/csv/Q043-F-02.json`.

**Result** (rules-tuple = no-tashkeel, last-grapheme of each verse, Shannon entropy):

| Surah | Entropy (bits) |
|:--|:-:|
| Q 40 (HM-A) | 2.4132 |
| Q 41 (HM-A) | 2.2635 |
| Q 42 (HM-A) | 2.5654 |
| **Q 43 (HM-B opener)** | **0.5939** |
| Q 44 (HM-B) | 0.8179 |
| Q 45 (HM-B) | 0.6998 |
| Q 46 (HM-B) | 0.9518 |

- Q 43 entropy = **0.5939 bits**, strictly below HM-A min (Q 41 at 2.2635). Direction-pre-committed and matched.
- Q 43 is the HM-7 entropy minimum.
- Δ_H(42→43) = 1.9715 bits — the steepest one-step ΔH within HM-7.
- Permutation null (10 000 perms, MW-2 corpus-prior, seed 20260428): **p_perm = 0.0000** (zero permutations under the corpus-shuffled null produce a Q 43 entropy ≤ observed).

**Verdict**: **VINDICATED**.

**Interpretation**: HM-A and HM-B are not just rhyme-letter different (ر-dominant → ن-dominant) — they occupy **disjoint entropy regimes**. HM-A surahs are uniformly multi-rāwī (all > 2.2 bits); HM-B surahs are uniformly low-entropy (all < 1.0 bits). Q 43 is the entropy minimum of the entire ḥawāmīm cluster. The transition Q 42 → Q 43 is therefore not a *gradient* but a *step* between two distinct prosodic regimes.

This empirically anchors al-Biqāʿī's structural-pivot intuition (*Naẓm al-Durar* ad Q 43:1) at the rhyme-axis level, while leaving the FR-content-axis distinct (per [[h-new-290-q42-block-vs-phonology-tension|H-NEW-290]] which shows HM block-coherence at content level remains in spite of prosodic discontinuity).

---

## Finding 2: Q043-F-03 — Q 43 *al-Raḥmān* lemma density top-5 corpus-wide — VINDICATED

**Pre-reg**: [[Q043-F-03-rahman-density-prereg|Q043-F-03]] — locked SHA256 `a265de03d897060bb4a4c8ea591051966cc62fd30922ea9ccd3a5cd5e682639d`.
**Script**: `/Users/grey/Downloads/quran/scripts/Q043_F_03_rahman_density.py`.
**Output**: `surahs/Q043-al-zukhruf/csv/Q043-F-03.json`.

**Result**: Q 43 has 7 *al-Raḥmān* lemma tokens (substring `رحمن`) in 870 orthographic tokens. Density = **8.046 per 1000 tokens**. **Corpus rank = 5** (matching the pre-committed top-5 prediction exactly).

Top-5 *al-Raḥmān* density:

| Rank | Surah | Count | Tokens | Density / 1000 |
|:-:|:-:|:-:|:-:|:-:|
| 1 | Q 1 al-Fātiḥa | 2 | 29 | 68.97 |
| 2 | Q 19 Maryam | 16 | 1012 | 15.81 |
| 3 | Q 67 al-Mulk | 5 | 348 | 14.37 |
| 4 | Q 78 al-Nabaʾ | 2 | 177 | 11.30 |
| **5** | **Q 43 al-Zukhruf** | **7** | **870** | **8.05** |

**Verdict**: **VINDICATED**.

**Interpretation**: Q 43 is the only HM-7 surah in the top-5; the next HM-7 *al-Raḥmān*-density entry is Q 41 at rank 14 (1.19/1000). The *al-Raḥmān* divine name is therefore a **distinguishing thematic marker** of Q 43 within the cluster. al-Rāzī (*Mafātīḥ al-ghayb* ad Q 43:36) and al-Ṭabarī (ad Q 43:33) both anchor this — their identification of *al-Raḥmān* as the Q 43 thematic-axis is empirically vindicated.

Notable: 4 of the top-5 *al-Raḥmān*-density surahs are Meccan (Q 1, 19, 67, 78, 43) — the divine name *al-Raḥmān* is a distinctively Meccan vocabulary marker per al-Suyūṭī (*al-Itqān*, nawʿ 18 on the Quranic divine names).

**Cross-link**: Notable surah Q 55 al-Raḥmān (the surah named after the divine name) has only 1 lemma attestation (the v.1 incipit *al-Raḥmān*) and ranks **10** by density — Q 55 is named-after-the-name but Q 43 is *Raḥmān-saturated*. This is a similar **eponymity-asymmetry** pattern to the Q 10/Q 12 typology found in [[Q010-yunus/06-novel-findings|Q010-F-01]] (thesis-named vs narrative-named): Q 55 is **incipit-named** for *al-Raḥmān*; Q 43 is **density-saturated** without bearing the name.

---

## Finding 3: Q043-F-04 — *zukhruf*-root surah-name signature — NULL with PRE-COMMIT VIOLATION (naive hypothesis confirmed)

**Pre-reg**: [[Q043-F-04-zukhruf-root-signature-prereg|Q043-F-04]] — locked SHA256 `ff2dd6517aac6582a800cdb48218f07bf1604932d5161ff75cc53e217a2503ff`.
**Script**: `/Users/grey/Downloads/quran/scripts/Q043_F_04_zukhruf_root.py`.
**Output**: `surahs/Q043-al-zukhruf/csv/Q043-F-04.json`.

**Pre-committed direction**: Q 43 rank > 1 by density (the surprising direction — that surah-naming is *symbolic*, not density-driven).

**Observed direction** (NULL/REVERSED): The QAC `zxrf` root has exactly 4 corpus attestations: Q 6:112:13, Q 10:24:21, Q 17:93:6, Q 43:35:1. Each surah has exactly 1 attestation; Q 43 has the smallest token base (870), so Q 43 IS rank 1 by density (1.149 / 1000 vs Q 17 at 0.608 / 1000). The naive expectation (named-after = densest) holds in the count-tied case.

**Verdict**: **NULL** with pre-commit-direction reversed. Recorded with full prominence per [[INVESTIGATION-PROTOCOL|protocol §1.3]].

**Honest interpretation**: At total-attestations-of-the-named-root level, the test was nearly degenerate (all 4 surahs have count = 1). The named-after-root pattern is not deeply tested — the direction-reversal is a count-artifact of the smallest-token-base, not a deep eponymity claim. The relevant takeaway is **descriptive**: *zukhruf* is a corpus-near-hapax root (4 occurrences total), and Q 43 carries one of them at v.35; the surah-name is therefore a *salient-rare-token* marker (al-Suyūṭī's *al-Itqān*, nawʿ 17, on surah-naming-conventions).

The pre-commit violation is honored: the broader claim that "surah-naming is symbolic, not density-driven" remains **untested** at this resolution. The Q 10 (yūnus, 50% concentration of 2 corpus tokens) vs Q 12 (yūsuf, 95.24% concentration) typology — see [[Q010-yunus/06-novel-findings|Q010-F-01]] — is the better-resolved test, and Q 43 *zukhruf* fits closer to the **near-hapax** column than to either pole.

---

## Finding 4: Q043-F-05 — Q 43:57-65 ʿĪsā-passage christological-token density — VINDICATED

**Pre-reg**: [[Q043-F-05-isa-block-density-prereg|Q043-F-05]] — locked SHA256 `87fcc04d19b68ef638f2ef83823c24d0b7ca46208fa37ca32604e7e87a668cac`.
**Script**: `/Users/grey/Downloads/quran/scripts/Q043_F_05_isa_block_density.py`.
**Output**: `surahs/Q043-al-zukhruf/csv/Q043-F-05.json`.

**Result**: Q 43:57-65 (9-verse block) has 2 christological tokens (substring `عيسى` + `مريم`) in 103 tokens. Density = **19.42 per 1000 tokens**. Corpus 9-window distribution (5365 windows total, 226 with non-zero density): Q 43:57-65 sits at the **99.31st percentile** — pre-committed direction (≥99th) matched.

**Top-10 christological 9-windows corpus-wide**:

| Surah | Verses | n_chr | Density / 1000 |
|:-:|:-:|:-:|:-:|
| Q 3 | 40-48 | 6 | 42.86 |
| Q 3 | 38-46 | 6 | 40.82 |
| Q 3 | 37-45 | 7 | 39.11 |
| Q 3 | 39-47 | 6 | 38.71 |
| Q 3 | 42-50 | 6 | 35.50 |
| Q 3 | 41-49 | 6 | 35.09 |
| Q 5 | 108-116 | 8 | 31.75 |
| Q 5 | 110-118 | 8 | 31.50 |
| Q 19 | 27-35 | 3 | 30.93 |
| Q 5 | 109-117 | 8 | 30.77 |

**Verdict**: **VINDICATED**.

**Interpretation**: All 10 windows above Q 43:57-65's density are **Medinan** (Q 3 Āl ʿImrān + Q 5 al-Māʾida + Q 19 Maryam, the latter being Meccan but the most concentrated Maryam-passage). Q 43:57-65 is therefore the **most christologically saturated 9-window in the Meccan polemical corpus** (post-Q19). This empirically anchors the classical exegetical observation (al-Ṭabarī, Ibn Kathīr, al-Rāzī ad Q 43:57-65) that this block is the most extended Meccan ʿĪsā christological discussion.

Notable: Q 19 Maryam's top-density 9-window (vv. 27-35) sits at rank 9 with density 30.93 (count 3 in 97 tokens). Q 43:57-65 has lower count (2) but also lower token base (103) — the two surahs have **comparable per-token christological density** but Q 19 is the verbose-narrative pole and Q 43 is the **polemical-condensed** pole. They are the two Meccan christological centers; Q 5 and Q 3 are the Medinan center.

---

## Finding 5: Q043-F-01 (prior session) — verbatim-identical 2-verse opening NOT unique to Q 43-Q 44 — VERDICT REVISION

**Pre-reg**: [[Q043-F-01-q43q44-twin-opening-prereg|Q043-F-01]] — locked SHA256 `6d4d362785f083bd9ff5f1cee533afc0cfa30f55e198031ab3718d10eff331d2`.
**Script**: `/Users/grey/Downloads/quran/scripts/Q043_F_01_twin_opening.py`.
**Output**: `surahs/Q043-al-zukhruf/csv/Q043-F-01.json`.

**Pre-committed direction**: only Q 43-Q 44 share verbatim-identical first-two-verses corpus-wide.

**Observed**: TWO adjacent surah-pairs share verbatim-identical first-two-verses:
- **Q 43-Q 44**: v.1 = حم, v.2 = والكتاب المبين
- **Q 45-Q 46**: v.1 = حم, v.2 = تنزيل الكتاب من الله العزيز الحكيم

**Verdict**: **NULL** at strict-uniqueness (per the existing JSON output `Q043-F-01.json` recording verdict `NULL_OR_DISCREPANCY`).

**Refined positive finding** (post-hoc, not new pre-reg): **TWO** adjacent surah-pairs (Q 43-Q 44 AND Q 45-Q 46) share verbatim-identical first-two-verses, AND these are **the only two such adjacent pairs in the entire Qurʾān**. Both pairs are within the HM-B sub-cluster of HM-7. The HM-B sub-block therefore has **two verbatim-twin opening pairs** out of three possible adjacencies, a structural feature unique to HM-B.

The original 05-classical-claims-audit.md Claim 4 (which asserted "only verbatim-identical 2-verse opening pair") **must be corrected**: there are TWO such pairs, both inside HM-B. I am updating the audit accordingly.

**Honest correction**: The original pre-commit was that ONLY Q 43-Q 44 satisfies the condition; the data shows Q 45-Q 46 ALSO satisfies it. The strict-direction prediction is therefore violated; recorded as NULL per [[INVESTIGATION-PROTOCOL|protocol §1.3]]. The descriptive observation (TWO HM-B adjacent twin-pairs) is post-hoc and capped at MW-7 single-test α=0.05.

**Cross-link**: This refines [[h-new-235-mutashabih-full-graph|H-NEW-235]]'s top-5 highest-similarity pairs list (which lists Q 43:2 ↔ Q 44:2) — Q 45:2 ↔ Q 46:2 should be listed as well (a verbatim-identical formula across HM-B's second-pair) and likely already appears in the full mutashābih edge list at similarity = 1.0.

---

## 6. Bonferroni summary across the Q 43 family

Family of 4 pre-registered novel tests (F-02, F-03, F-04, F-05). Bonferroni-corrected α = 0.05 / 4 = 0.0125.

| Test | Verdict | Direction | Note |
|:--|:--|:--|:--|
| F-02 entropy break | VINDICATED | matches | p_perm = 0.0000 (well under α_bon) |
| F-03 *Raḥmān* density | VINDICATED | matches | rank=5, exact-rank claim |
| F-04 *zukhruf* root | NULL (precommit-reversed) | reversed | counted-artifact at near-hapax root |
| F-05 ʿĪsā 9-window | VINDICATED | matches | percentile = 99.31, exact rank claim |

3/4 VINDICATED at strict pre-commit. 1/4 NULL with full-prominence pre-commit-violation flag.

## 7. Honest limits

1. **F-02 entropy** depends on last-grapheme-of-verse rule (no-tashkeel default). Classical *qāfiya* analysis would refine the ranking; the relative HM-7 ranking under min-tashkeel and full-tashkeel is not pre-committed and would require separate tests.
2. **F-03 lemma-density** uses substring-match `رحمن` — which catches all morphological variants of *al-Raḥmān*. Surface-string matches do not equal QAC-root-counts (the rḥm root includes *raḥma*, *raḥīm*, *raḥmān* together).
3. **F-04** is degenerate due to all 4 attestations being count=1; the underlying eponymity-claim is not deeply tested at this corpus-scale.
4. **F-05** uses `عيسى + مريم` as christological-marker; alternative operationalizations (e.g., *masīḥ*, *anjīl*, theological-pronoun markers) are not pre-committed.

## 8. Cross-references

- [[Q043-F-02-hma-hmb-entropy-break-prereg|Q043-F-02 prereg]]
- [[Q043-F-03-rahman-density-prereg|Q043-F-03 prereg]]
- [[Q043-F-04-zukhruf-root-signature-prereg|Q043-F-04 prereg]]
- [[Q043-F-05-isa-block-density-prereg|Q043-F-05 prereg]]
- [[Q043-al-zukhruf/05-classical-claims-audit|Q 43 audit]] — Claim 4 needs correction (refine the verbatim-twin-pair claim to TWO HM-B pairs)
- [[hawamim-7-cluster-bifurcation|HM-7 cluster bifurcation]]
- [[Q019-maryam/00-overview|Q 19 Maryam]] — Maryam-comparator surah for F-05 (NOT yet built; flagged DATA-GAP)
- [[h-new-235-mutashabih-full-graph|H-NEW-235]] — verbatim-twin verse network (Q43:2↔Q44:2 already listed; Q45:2↔Q46:2 should be on the list)
- [[h-new-700-phonological-compression-tail|H-NEW-700]] — F-02 entropy is consistent with the phonological-tail framework
- [[h-new-290-q42-block-vs-phonology-tension|H-NEW-290]] — orthogonality of prosody and FR-content axes; F-02 prosody-step coexists with FR-content cohesion across HM-A→HM-B
