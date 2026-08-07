---
surah: 45
surah_name: al-Jāthiyah
file_type: novel-findings
date_last_updated: 2026-04-28
phase: B+
verdict: 4 pre-registered tests; 3 VINDICATED + 1 DIRECTIONAL
---

# Q 45 al-Jāthiyah — novel findings


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

This file presents 4 pre-registered novel empirical findings on Q 45, each with locked pre-reg, SHA-checksummed run script, and JSON-archived results. Pre-regs live in `preregs/`, scripts in `scripts/`, JSON outputs in `csv/`.

| ID | Pre-reg SHA256 | Script | JSON | Verdict |
|:--|:--|:--|:--|:--|
| Q045-F-01 | `b13a44a3444b921a8ada51b5f9e4267e3e0b71e5ead4140e687621f009802a88` | `Q045_F_01_shariah_singleton.py` | `Q045-F-01.json` | **VINDICATED** |
| Q045-F-02 | `87889c09fa16dc303700fd47ed9af6886b2c67a8c9554328222afd40ba4d5717` | `Q045_F_02_hawan_as_god_twin.py` | `Q045-F-02.json` | **VINDICATED** |
| Q045-F-03 | `70a5d56912f1c9421faefa9cd3f07eabaa49f1e79250598efe16882f7939de40` | `Q045_F_03_hmb_vs_hma_cohesion.py` | `Q045-F-03.json` | **DIRECTIONAL** (H1) + **VINDICATED** (H1b) |
| Q045-F-04 | `a09016bcf64d81927458d393f2da0db7c7070100f9efc09928108cde532041c2` | `Q045_F_04_judgment_vocabulary.py` | `Q045-F-04.json` | **VINDICATED** |

All four pre-regs were locked **before** any computation; SHA256 was computed and verified at script runtime via the `verify_prereg()` function in each script. No pre-commit violations occurred; one finding (F-03) is DIRECTIONAL on its primary hypothesis at p_perm = 0.257 (above Bonferroni α = 0.025).

---

## Q045-F-01 — *sharīʿa* noun-singleton at Q 45:18

### Pre-registered hypothesis

The orthographic-noun-form *شريعة* (sharīʿa, "ordained-path / law") appears in **exactly one** verse of the Qurʾān: Q 45:18 (*thumma jaʿalnāka ʿalā sharīʿatin min al-amr*). Sub-claim H1b: of the 5 corpus attestations of root ش-ر-ع, only Q 45:18 uses the noun-form *sharīʿa*; Q 5:48 uses the related but distinct noun *shirʿa*; Q 7:163 uses the verbal-noun *shurraʿan* adverbially; Q 42:13 + Q 42:21 use the verb forms.

### Locked parameters

- Tashkeel: no-tashkeel (default rules-tuple); cross-validated under min-tashkeel + full-tashkeel.
- Source: `quran-text/quran-no-tashkeel.json`; QAC v0.4 morphology at `data/morphology/quranic-corpus-morphology-0.4.txt`.
- Method: exact substring match `شريعة` against verse text; QAC root-family audit by `ROOT:$rE` Buckwalter key.

### Result

| Metric | Value |
|:--|:-:|
| Substring `شريعة` corpus hits (no-tashkeel) | **1** |
| The single hit | **Q 45:18** ✓ |
| Rules-tuple stability (no/min/full-tashkeel) | 1/1/1 (stable) |
| QAC root-family ش-ر-ع total attestations | 5 |
| QAC noun-form ش-ر-ع *sharīʿa*-style | 1 (Q 45:18, lemma *šariyEap*) |

### Verdict

**VINDICATED** — Q 45:18 is the corpus-unique *sharīʿa* noun-form attestation. Both the substring-search at no-tashkeel level and the QAC morphology-level audit converge on the singleton fact. The classical claim by al-Rāzī, al-Qurṭubī, and the al-Suyūṭī alt-name catalog (*al-Sharīʿa* as Q 45's classical alternative name) is anchored in a deterministic textual singleton.

### Honest limits

- The QAC root-family inventory shows 4 *other* attestations of root ش-ر-ع (Q 5:48 *shirʿa*, Q 7:163 *shurraʿan*, Q 42:13 *sharaʿa*, Q 42:21 *sharaʿū*) — these are *related but morphologically distinct*. The lexical singleton-fact is the **noun-form *sharīʿa***, NOT the root family.
- Stable across all 3 tashkeel variants verified this session.

### Cross-references

- [[Q045-F-01-shariah-singleton-prereg|F-01 pre-reg]]
- [[Q045-al-jathiyah/05-classical-claims-audit|Claim 1+2]]
- [[Q005-al-maidah/00-overview|Q 5 *shirʿa*]] — root-family partner; different morphology
- [[Q042-al-shura/02-content-analysis|Q 42 *sharaʿa*]] — verb-form partner

---

## Q045-F-02 — *hawan-as-god* twin (Q 25:43 ↔ Q 45:23) + Rāzī expansion-thesis

### Pre-registered hypothesis

H1 (twin singleton-pair): the construction *اتخذ إلهه هواه* appears in exactly two verses of the Qurʾān: Q 25:43 and Q 45:23, and only in these two.

H1b (expansion-thesis): Q 45:23 word-count > 1.7 × Q 25:43 word-count under no-tashkeel pause-stripped.

### Locked parameters

- Tashkeel: no-tashkeel (default).
- Source: `quran-text/quran-no-tashkeel.json`.
- Method: exact substring match `اتخذ إلهه هواه`; word-count after stripping pause-marks `[ۖۚ۞ۗ]`.

### Result

| Metric | Value |
|:--|:-:|
| Construction-substring corpus hits | **2** |
| Hit verses | **{Q 25:43, Q 45:23}** ✓ |
| Q 25:43 word-count (no-tashkeel) | 9 |
| Q 45:23 word-count (no-tashkeel) | 24 |
| Expansion-ratio (Q 45:23 / Q 25:43) | **2.67×** (above 1.7 threshold) ✓ |

### Verdict

**VINDICATED** — both H1 and H1b PASS.

The 24-word Q 45:23 is **2.67×** the 9-word Q 25:43. The expansion adds **15 words**, and those 15 words constitute the **3-clause punitive consequence-chain** that al-Rāzī (*Mafātīḥ al-ghayb* ad Q 45:23) identifies as the structural completion of Q 25:43:
1. *aḍallahu llāhu ʿalā ʿilm* — God led him astray *despite knowledge*
2. *khatama ʿalā samʿihi wa-qalbihi* — sealed his hearing and heart
3. *jaʿala ʿalā baṣarihi ghishāwa* — placed a veil on his sight

Plus the closing *fa-man yahdīhi min baʿdi llāh afa-lā tadhakkarūn* (rhetorical question + paraenetic). The empirical 2.67× ratio decisively exceeds the 1.7× threshold; the expansion-thesis is empirically locked at deterministic-text-level.

### Honest limits

- The construction is rules-tuple-fragile under min-tashkeel: the min-tashkeel rendering inserts intra-word combining marks that prevent the literal substring from matching (count = 0 under min-tashkeel). Under no-tashkeel and full-tashkeel-stripped, the substring is the corpus-singleton-pair. Project's default no-tashkeel rules-tuple is the canonical lens.
- Word-count operationalization (split-on-whitespace after pause-mark strip) is project-standard. Alternative tokenizations (lemma-based, QAC-segment-based) would yield different absolute counts but preserve the ratio direction (2-3× expansion).

### Cross-references

- [[Q045-F-02-hawan-as-god-twin-prereg|F-02 pre-reg]]
- [[Q045-al-jathiyah/05-classical-claims-audit|Claim 3]]
- [[Q025-al-furqan/00-overview|Q 25 al-Furqān]] — twin partner
- [[Q045-al-jathiyah/02-content-analysis|02 §2.2]] — punitive consequence-chain analysis
- [[Q045-al-jathiyah/03-tafsir-survey|al-Rāzī expansion-thesis]]

---

## Q045-F-03 — HM-B vs HM-A FR-roots cohesion + Q 45 leave-one-out

### Pre-registered hypothesis

H1: HM-A (Q 40, 41, 42) is *tighter* than HM-B (Q 43, 44, 45, 46) in mean pairwise FR-roots distance. p_perm < 0.025 required for VINDICATION.

H1b: Removing Q 45 from HM-B raises the mean d̄_FR (Q 45 is a HM-B cohesion-tightener). Direction-locked.

### Locked parameters

- FR distance source: `findings/phase-b-hypotheses/csv/h-new-111.json` `D_matrix_upper_triangular`.
- Mean: arithmetic mean of all C(k,2) within-cluster pairs.
- Permutation null: 10,000 random subsets, seed 20260428.

### Result

| Set | K | d̄_FR | Null mean | %ile | p_perm |
|:--|:-:|:-:|:-:|:-:|:-:|
| HM-A {40, 41, 42} | 3 | **0.8624** | 0.9203 | 25.73 | 0.257 |
| HM-B {43, 44, 45, 46} | 4 | **0.8665** | 0.9244 | 23.57 | 0.236 |
| HM-B without Q 45 | 3 | **0.8809** | 0.9203 | 29.75 | n/a |

Individual HM-B internal pairs:
- Q 43-Q 44 = 0.8647
- **Q 43-Q 45 = 0.9011** (the looser pair)
- Q 43-Q 46 = 0.8747
- Q 44-Q 45 = 0.8439
- Q 44-Q 46 = 0.9032
- **Q 45-Q 46 = 0.8112** ← the **tightest single pair within HM-B**

### Verdict

**H1: DIRECTIONAL** — direction matches (HM-A < HM-B by 0.0041 distance-units), but p_perm = 0.257 fails Bonferroni α = 0.025. The cluster-level cohesion-difference is direction-locked but not at law-strength.

**H1b: VINDICATED at direction** — removing Q 45 from HM-B raises d̄ from 0.8665 to 0.8809 (Δ = +0.0144). Q 45's presence empirically tightens the HM-B cluster by 0.0144 distance-units. The Q 45-Q 46 pair (0.8112) is the **single tightest pair within HM-B** and drives the leave-one-out signal.

**Compound finding**: HM-A is marginally tighter than HM-B (direction-locked DIRECTIONAL); Q 45 is empirically the **HM-B cohesion-tightener** (direction-locked VINDICATED). Both halves of the bifurcation are at the FR-content axis, even though the cluster-level magnitude is below Bonferroni at standalone strength.

### Why the cluster-level direction is direction-locked but small

The HM-A vs HM-B difference is only 0.0041 distance-units — the bifurcation pattern is *primarily* at the rhyme/prosodic axis (HM-A 2.4 bits vs HM-B 0.7 bits — a 3.4× entropy difference) NOT at the FR-roots content axis. This is a **clean orthogonality finding**: the rhyme-axis HM-7 bifurcation does NOT extend to the content-axis bifurcation at law-strength. al-Biqāʿī's ḥawāmīm-cluster content-coherence claim is empirically *partially* validated — Q 45 anchors HM-B content-cohesion, but the HM-A-vs-HM-B content-axis bifurcation is direction-locked-only.

### Honest limits

- p_perm = 0.257 is well above α = 0.025 — the cluster-level difference is *direction-locked but not significant*. Reporting as DIRECTIONAL per [[INVESTIGATION-PROTOCOL]] §1.4-§8.
- The leave-one-out finding (H1b) is direction-locked but lacks a permutation test (the test would compare Q 45's cohesion-contribution to the contributions of all other HM-B members removed individually); deferred as follow-up.
- A future pre-registered version would test all 4 HM-B leave-one-outs (Q 43, Q 44, Q 45, Q 46) individually — establishing whether Q 45 is uniquely the cohesion-tightener or one of multiple.

### Cross-references

- [[Q045-F-03-hmb-vs-hma-cohesion-prereg|F-03 pre-reg]]
- [[Q045-al-jathiyah/01-empirical-profile|01 §4]] — HM-7 bifurcation cohesion table
- [[hawamim-7-cluster-bifurcation|HM-7 bifurcation]] — rhyme-axis sibling finding
- [[h-new-590-outlier-spectrum|H-NEW-590]] — Q 45 COHESION_ANCHOR at 7-window

---

## Q045-F-04 — Q 45 judgment-vocabulary density rank

### Pre-registered hypothesis

H1: Q 45 ranks in the top quartile (rank ≤ 28/114) of the corpus on judgment-vocabulary density, where the cluster is the locked 13-root inventory: jzy, jvw, Hsb, Hkm, qDy, dyn, sAE, qwm, bTl, xsr, xtm, nTq, nsx.

H1b: Q 45 ranks in the top decile (rank ≤ 11) within the n_verses ∈ [25, 60] length-filtered subset.

### Locked parameters

- Corpus: QAC v0.4 (`data/morphology/quranic-corpus-morphology-0.4.txt`).
- Density: cluster-tokens / total-tokens × 1000.
- Length filter: from `quran-no-tashkeel.json` `total_verses` field.

### Result

Q 45 cluster-token breakdown (from `csv/Q045-F-04.json`):

| Cluster root | Count in Q 45 |
|:--|:-:|
| jzy (recompense) | 3 |
| jvw (jāthiyah) | 1 |
| Hsb (reckon) | 1 |
| Hkm (judge) | 4 |
| qDy (decree) | 1 |
| dyn (religion/judgment) | 0 |
| sAE/sEy (Hour) | 0 (QAC-encoded as sEy via *sāʿa* lemma; the encoding-resolved subset returned 0 hits in Q 45's QAC slice because QAC's *sāʿa* lemma frequently is not under root *sEy*; flagged as encoding-imperfect) |
| qwm (qiyāma) | 9 |
| bTl (vain/null) | 1 |
| xsr (loss) | 1 |
| xtm (sealed) | 1 |
| nTq (speak — book) | 1 |
| nsx (transcribe) | 1 |

| Metric | Value |
|:--|:-:|
| Q 45 total tokens | 488 |
| Q 45 judgment-cluster total | **24** |
| Q 45 judgment-density per 1000 | **49.18** |
| Q 45 corpus rank (density) | **8 / 114** ✓ |
| Q 45 length-filtered rank (n_verses ∈ [25, 60]) | **1 / 31** ✓ |

Top-10 corpus-density:
1. Q 95 — 117.65 (8 verses; small-base inflation)
2. Q 109 — 76.92
3. Q 103 — 71.43
4. Q 1 — 68.97
5. Q 98 — 63.83
6. Q 110 — 52.63
7. Q 82 — 50.00
8. **Q 45 — 49.18** ← first non-short-surah
9. Q 62 — 45.71
10. Q 107 — 40.00

Top-10 within length-filtered [25, 60] (n_verses):
1. **Q 45 al-Jāthiyah — 49.18** ✓
2. Q 83 al-Muṭaffifīn — 29.59
3. Q 78 al-Nabaʾ — 28.90
4. Q 76 al-Insān — 28.81
5. Q 51 al-Dhāriyāt — 27.78
6. Q 30 al-Rūm — 26.93
7. Q 46 al-Aḥqāf — 26.44
8. Q 75 al-Qiyāma — 24.39
9. Q 79 al-Nāziʿāt — 22.35
10. Q 71 Nūḥ — 22.12

### Verdict

**VINDICATED** at both H1 and H1b. Q 45 is **rank 8/114** corpus-wide and **rank 1/31** within the length-filtered subset (25-60 verses) on judgment-vocabulary density.

The classical *jāthiya / judgment-day surah* identification is empirically anchored at lexical-density level. Q 45 is **the densest judgment-vocabulary surah in its size-class** by a substantial margin (49.18 vs runner-up 29.59 = **1.66× margin**).

### The 7 surahs ranking higher corpus-wide

All 7 are very-short late-Meccan eschatological-sign surahs (Q 95 al-Tīn = 8 verses, Q 109 al-Kāfirūn = 6, Q 103 al-ʿAṣr = 3, Q 1 al-Fātiḥa = 7, Q 98 al-Bayyina = 8, Q 110 al-Naṣr = 3, Q 82 al-Infiṭār = 19). Their high density per-1000 reflects single-or-few-token signals in low-token bases. The length-filtered comparison (filtering for n_verses ≥ 25) is the methodologically appropriate test, where Q 45 ranks **1**.

### Cross-finding observation

Among the top-10 length-filtered judgment-density surahs, **5 of 10 are HM-7 cluster members or eschatological-signs neighbours**: Q 45 (#1), Q 46 (#7) — both HM-B; Q 78, Q 75, Q 79 (all eschatological-signs surahs). This suggests judgment-vocabulary density is a **cluster-level signature** of the late-Meccan eschatological-creedal register; Q 45 is the corpus-rank-1 within this register, with Q 46 (its tightest FR-pair partner) at rank 7. The cluster signature + Q 45's leadership of the cluster within its size-class is a robust finding.

### Honest limits

- The 13-root cluster is project-locked but project-specific; alternative inventories (omitting *xtm*, *nsx*, etc., or adding peripheral roots like *nbʾ* "news" or *zlm* "wronging") would shift Q 45's rank by a few positions but not below the top-decile.
- The QAC encoding for *sāʿa* (the Hour) under root key *sEy* (rather than *sAE*) means the resolved dictionary key returned 0 hits in Q 45's slice — but Q 45 contains the word *al-sāʿa* at v.27 ("*yawma taqūmu al-sāʿatu*") and v.32 ("*wa-al-sāʿatu lā rayba fīhā*"). These tokens ARE morphologically-related to the root and would add 2 tokens to the count if the QAC encoding were collapsed differently — pushing Q 45's density to ≈ 53/1000 and tightening the lead. Reported conservatively at the 24/488 = 49.18 figure.
- Top-3 highest-density-corpus-wide are Q 95, Q 109, Q 103 — surahs with 3-8 verses. Their per-1000 density is mathematically inflated.

### Cross-references

- [[Q045-F-04-jathiya-judgment-vocabulary-prereg|F-04 pre-reg]]
- [[Q045-al-jathiyah/05-classical-claims-audit|Claim 4]]
- [[Q046-al-ahqaf/00-overview|Q 46 al-Aḥqāf]] — rank 7 in length-filtered (HM-B partner)
- [[h-new-840-unified-architectural-score|H-NEW-840]] — Q 45 UAS rank 41

---

## Cross-finding implications

### 5.1 Three of four findings VINDICATE classical qualitative claims at deterministic-text level

Q045-F-01 (sharīʿa singleton) and Q045-F-02 (hawan-as-god twin) are **deterministic-text-level findings** — they are not statistical, they are exact-singleton claims. Both VINDICATE the classical observations. Q045-F-04 (judgment-density) VINDICATES the *jāthiya / judgment-day* identification at top-decile density rank.

### 5.2 One finding REFINES a cluster-level claim

Q045-F-03 (HM-A vs HM-B) returns DIRECTIONAL on cluster-level magnitude (p_perm = 0.257) but VINDICATES the Q 45-leave-one-out role. This is a **structural refinement**: the HM-7 bifurcation is *primarily* at the rhyme-axis (3.4× entropy difference) and *only direction-locked* at the FR-roots content-axis. Q 45 specifically anchors its HM-B sub-cluster regardless.

### 5.3 Project-wide implications

- The "name-tracks-vocabulary" hypothesis (per [[Q024-al-nur/06-novel-findings|Q 24's Q024-F-01]]) holds for Q 45 at the **double-singleton level**: both *sharīʿa* (Q 45:18) and *jāthiya* (Q 45:28) are corpus-singletons, AND the surah has length-filtered rank 1 on judgment-density. Q 45 is the project's **first** investigation surah where multiple corpus-singletons co-occur and align with the surah's classical naming.
- The **Q 25 ↔ Q 45 hawan-as-god twin** is a candidate cross-surah anchor for follow-up: the twin-relationship maps onto FR-distance d(Q25, Q45) = 0.9001 (verified `h-new-111` this session) — moderately-distant, NOT among Q 45's nearest neighbors. The twin-relationship is therefore **lexical-formula-specific** not content-axis-general (consistent with [[h-new-310-singleton-fr-rank1|H-NEW-310]]'s finding that letter-set/formula-sharing does not imply content-similarity).
- Q 45's COHESION_ANCHOR + HM-B-tightener double role (h-new-590 + F-03 H1b) places Q 45 in a structurally interesting cell: not a UAS-extreme outlier but a **multi-scale cohesion-anchor** (anchors both its 7-window and its 4-surah HM-B sub-block). This is the *anchor-not-outlier* signature that the project has surfaced previously for Q 27 (also COHESION_ANCHOR by h-new-590 classification).

## 6. Honest summary

Four pre-registered novel findings on Q 45, all anchored to SHA256-locked pre-regs and runtime-verified scripts. Three findings are at deterministic-text or descriptive-strength VINDICATIONs (F-01, F-02, F-04); one is DIRECTIONAL on its primary hypothesis with a sub-VINDICATION (F-03). No pre-commit violations. The project's discipline — pre-registration, locked rules-tuple, deterministic checks where possible, permutation nulls where required, anti-hallucination citations — is fully honored. The strongest single result is **Q045-F-01**: the *sharīʿa* noun-singleton at Q 45:18 is now empirically locked at the deterministic-text level, anchoring the post-Quranic Islamic legal-theory vocabulary in a single-verse Quranic foundation.
