---
surah: 67
surah_name_ar: الملك
surah_name_translit: al-Mulk
file_type: empirical-profile
date_last_updated: 2026-04-28
phase: B+
verdict: COMPLETE
---

# Q 67 al-Mulk — Empirical Architectural Profile

## 1. Headline architectural metrics

Rules-tuple: `(no-tashkeel, QAC-STEM root tokens, QAC v0.4, basmala-counted-only-in-Q1, mushaf order, Hafs-Kufan)`. All numerical claims below are computed from disk; sources cited.

| Metric | Value | Rank / corpus context | Source |
|:--|:--:|:--|:--|
| **UAS (Unified Architectural Score)** | **−2.0526** | **102 / 114** (bottom decile) | `findings/phase-b-hypotheses/csv/h-new-840.json` `all_uas[surah=67]` |
| Outlier-strength Δ%ile (window {64-70}) | **−0.20 pp** | **NULL** classification | `h-new-590.json` `all_surahs_results[X=67]` |
| iʿjāz signature sig_A (structural / fawāṣila-content correlation) | **+0.3108** | **rank 52 / 114** | `h-new-750.json` `per_surah[surah=67]` |
| iʿjāz signature sig_B (rhyme-purity) | −0.5663 | rank 67 / 114 | same |
| Mean Fisher-Rao distance to corpus | **0.8920** | **rank 67 / 114** (middle, slightly below corpus mean 0.9235) | computed from QAC stem-roots, K=500, Dirichlet α=0.5 |
| Local cohesion (1-step adjacency) | **1.1026** | high (z = +0.566) — Q 67 is content-similar to its mushaf neighbours | `h-new-750.json` |
| Mean content distance | 0.892 | z = −0.311 (slightly below window mean) | same |
| Q 66 → Q 67 canonical-adjacency cost | 0.0780 length-units | **rank 47 / 113** (mid-pack) | `h-new-720.json` `per_adjacency` |
| Q 67 → Q 68 canonical-adjacency cost | 0.0962 length-units | **rank 36 / 113** (mid-pack) | same |
| Rhyme entropy (Shannon, nats) | **0.7698** | rank ~38 / 114 (moderately monorhyme) | `h-new-750.json` |
| Top final letter (rāwī) | **ر** | 21 / 30 verses = **70.0%** | computed; cross-validated against H-NEW-750 |
| QAC root-tokens | 208 | rank 59 / 114 | `data/morphology/quranic-corpus-morphology-0.4.txt` |
| QAC distinct roots | 127 | rank 55 / 114 | same |
| Words (no-tashkeel orthographic, mushaf-marks-stripped) | 333 | mid-mufaṣṣal | `quran-text/quran-no-tashkeel.json` |
| Letters (no-tashkeel, no spaces) | 1,347 | mid-mufaṣṣal | same |
| mlk-stem (mulk / malik / malāʾika / etc.) tokens | **1** | **rank 54 / 114 by raw count** | `data/morphology/quranic-corpus-morphology-0.4.txt`; see §6 |
| mlk-stem density (per 1000 root-tokens) | 4.81 | rank 37 / 114 | same |

## 2. The architectural paradox: HIGH RECITATION-TRADITION STATUS, LOW UAS RANK

Q 67's UAS = −2.053, rank 102/114, places it firmly in the **bottom decile** — alongside Q 112 al-Ikhlāṣ (rank 109), Q 87 (rank 114), Q 73 (rank 111), Q 83 (rank 110). All four of Q 67's UAS components are weak:

| UAS component | Q 67 value | Top-5 average | Bottom-5 average | Q 67 cell |
|:--|:--:|:--:|:--:|:--|
| abs_outlier (|Δ%ile|) | 0.20 | 24.85 | 0.18 | bottom-cell |
| max_cost (max neighbour adjacency cost) | 0.096 | 0.434 | 0.078 | bottom-cell |
| abs_ijaz (|sig_A|) | 0.311 | 1.851 | 0.236 | bottom-cell |

By contrast, Q 67's *recitation-tradition* status is high — see `04-hadith-corpus.md` §2 for the *al-Mānīʿa* / *al-Munjiya* grave-protection tradition (Tirmidhī #2890 idInBook 2974, Abū Dāwūd #1400 idInBook 1401, Ibn Mājah #3786 idInBook 3522, Mālik *Muwaṭṭaʾ* idInBook 497) and the Prophetic nightly-recitation tradition (Tirmidhī idInBook 2975). The two empirical signatures are **orthogonal**: classical attention pours into Q 67 via *faḍāʾil* / grave-protection / nightly recitation, but the surah's mushaf-architectural profile is unremarkable.

This is the **theological-iʿjāz / architectural-iʿjāz orthogonality** cell predicted by [[cross-finding-026-iʿjāz-architecture|cross-finding-026]] and the al-Khaṭṭābī *iʿjāz al-maʿnā* tradition. Q 67 joins Q 112, Q 36, Q 18 as canonical examples of high-*faḍāʾil* + middling-or-low-UAS surahs (see Q067-F-01 in `06-novel-findings.md` for the formal cross-comparison test).

## 3. The (NON-) bracketing-cost claim

Per `h-new-720.json`, the 113 canonical-adjacency costs are sorted. Q 67's two adjacencies:

| Adjacency | Cost (delta) | Frac of TSP residual | Rank |
|:--|:--:|:--:|:--:|
| Q 66 → Q 67 | 0.0780 | 0.94% | **47 / 113** |
| Q 67 → Q 68 | 0.0962 | 1.16% | **36 / 113** |

Combined: 0.174 length-units = 2.10% of the 8.29-unit residual.

Compare Q 24 (the canonical *high-bracketing-cost* surah): combined 6.04%, both ranks ≤ 11. Compare Q 33: combined ~8.4%, both ranks ≤ 3.

**Q 67 has UNREMARKABLE adjacency cost on both sides** — the mushaf does not "pay" structurally to keep Q 67 between Q 66 (al-Taḥrīm) and Q 68 (al-Qalam). The transition is content-natural at FR distance and at TSP-cost: Q 66 is Medinan-late but post-kink, Q 68 is Meccan-mufaṣṣal — and Q 67 fits between them as another Meccan-mufaṣṣal surah.

This is a contrastive vindication of the *bracketing-cost* claim's discriminating power: a surah of high recitation-tradition status (Q 67) does NOT necessarily produce high adjacency costs.

## 4. Fisher-Rao distance row (Q 67 against all 113 others)

Computed from QAC root distributions (K=500 most-frequent stem-roots, Dirichlet α=0.5 smoothing, FR angular: D_ij = 2·arccos(Σ √(p_i·p_j))).

**Five nearest neighbours** (Q 67's root-distribution maps to short-mufaṣṣal Meccan surahs):

| Rank | Surah | FR distance | Class |
|:-:|:-:|:--:|:--|
| 1 | Q 81 al-Takwīr | **0.7531** | Meccan-eschatological-mufaṣṣal |
| 2 | Q 32 al-Sajda | 0.7534 | Meccan-mid (cf. *Alif-Lām-Mīm-Tanzīl*) |
| 3 | Q 105 al-Fīl | 0.7558 | Meccan-short |
| 4 | Q 1 al-Fātiḥa | 0.7577 | Meccan-opener (head-window) |
| 5 | Q 112 al-Ikhlāṣ | 0.7609 | Meccan-creedal-thuluth |
| 6 | Q 86 al-Ṭāriq | 0.7657 | Meccan-mufaṣṣal |
| 7 | Q 110 al-Naṣr | 0.7682 | Medinan-short |

**Five farthest neighbours** (Q 67 maximally distinct from large-Medinan-legal):

| Rank | Surah | FR distance |
|:-:|:-:|:--:|
| 109 | Q 5 al-Māʾida | 1.1038 |
| 110 | Q 3 Āl ʿImrān | 1.1240 |
| 111 | Q 55 al-Raḥmān | 1.1481 |
| 112 | Q 4 al-Nisāʾ | 1.1688 |
| 113 | Q 9 al-Tawba | 1.2044 |

**Interpretation**: Q 67's root-distribution sits in a cluster with Q 32 al-Sajda (which the Q 67 grave-protection tradition explicitly pairs with — see `04-hadith-corpus.md` §3 for the *Alif-Lām-Mīm-Tanzīl + tabāraka* pair-recitation hadith). Q 67 ↔ Q 32 FR distance 0.7534 is well below corpus mean — **the empirical cluster matches the classical recitation pair**. This is a non-trivial vindication of a recitation-tradition-derived cluster claim.

Q 67's nearest neighbours are otherwise short-Meccan-doxological-eschatological (Q 81, Q 105, Q 1, Q 112, Q 86, Q 110) — exactly the register-class one would describe Q 67 as occupying qualitatively.

The farthest pair Q 9 al-Tawba (1.204) is consistent with the project's empirical architecture: al-Tawba is the no-basmala Medinan-legal-political outlier; Q 67 is its content-inverse.

## 5. Outlier-window decomposition (H-NEW-590)

The 7-window centred on Q 67 is `[64, 65, 66, 67, 68, 69, 70]` per `h-new-590.json`:

| Removed | d̄_W | d̄_W−X | percentile shift Δ (pp) | classification |
|:--:|:--:|:--:|:--:|:--|
| **Q 67** | 0.8797 | 0.8765 | **−0.20** | **NULL** |

(Source: `h-new-590.json` `all_surahs_results`; entry `{"X":67, "window":[64,...,70], "d_W":0.8797, "d_W_minus_X":0.8765, "delta_pct":-0.20, "p_greater_W":0.758, "classification":"NULL"}`.)

Removing Q 67 *barely* shifts the window's d̄ — Q 67 is content-typical for its 7-window. It is not a register-disrupter (unlike Q 24's +23.51 pp) nor a window-cohesion anchor (unlike Q 2's −20.62 pp). Q 67 is a *typical-member* of its post-kink Meccan-mufaṣṣal window.

This is direct empirical evidence that **Q 67's recitation-tradition prominence does not arise from a structural-disrupter signature**.

## 6. mlk-stem (m-l-k root) lexical concentration — KEY NULL FINDING

A core pre-registered novel hypothesis (Q067-F-04, see `06-novel-findings.md` and `preregs/Q067-F-04-mulk-stem-density-prereg.md`): does the surah named *al-Mulk* over-concentrate the *mlk* (m-l-k) root family, the way Q 24 al-Nūr over-concentrates the light-cluster (Q024-F-01 at p<10⁻⁶)?

Computed from QAC v0.4 morphology (`data/morphology/quranic-corpus-morphology-0.4.txt`):

| Quantity | Value |
|:--|:-:|
| Q 67 mlk-stem tokens | **1** |
| Q 67 total root-tokens | 208 |
| Q 67 mlk density | 4.81 / 1000 |
| Corpus mlk total | 206 |
| Corpus total root-tokens | 49,968 |
| Expected under uniform | (208 × 206) / 49,968 ≈ **0.86** |
| Hypergeometric P(X ≥ 1) | **0.5773** |
| Bonferroni α (k=114) | 4.39 × 10⁻⁴ |
| Verdict | **NULL — does not pass any threshold** |

Top 10 surahs by mlk-stem RAW count:

| Rank | Surah | mlk-tokens | Total root-tokens | Density / 1000 |
|:-:|:-:|:-:|:-:|:-:|
| 1 | Q 2 al-Baqara | 20 | 3,884 | 5.15 |
| 2 | Q 3 Āl ʿImrān | 13 | 2,274 | 5.72 |
| 3 | Q 4 al-Nisāʾ | 10 | 2,462 | 4.06 |
| 4 | Q 5 al-Māʾida | 9 | 1,798 | 5.01 |
| 5 | Q 6 al-Anʿām | 9 | 1,946 | 4.62 |
| 6 | **Q 25 al-Furqān** | **9** | **608** | **14.80** |
| 7 | Q 16 al-Naḥl | 8 | 1,184 | 6.76 |
| 8 | Q 17 al-Isrāʾ | 8 | 1,043 | 7.67 |
| 9 | Q 12 Yūsuf | 7 | 1,126 | 6.22 |
| 10 | Q 43 al-Zukhruf | 7 | 512 | 13.67 |

**Q 67 al-Mulk is rank 54 / 114 by raw count, rank 37 / 114 by density.** It does NOT over-concentrate the *mlk*-stem family. The surah's name comes from the **single occurrence of *al-mulk* in v.1**, not from a lexical concentration spread through the surah.

This is a **direct NULL** on the "name-tracks-vocabulary" hypothesis confirmed positively at p<10⁻⁶ for Q 24 (light-cluster, Q024-F-01). The hypothesis is therefore **rules-tuple-fragile across surahs**: it succeeds for Q 24 but fails for Q 67. The "name-tracks-vocabulary" generalization is FALSIFIED at the corpus-wide level. This is one of Wave D's substantive negative findings.

The classical naming convention for Q 67 is therefore *opening-word-naming* (the standard convention for surahs without a clear thematic-content-cluster: Q 1 al-Fātiḥa, Q 2 al-Baqara, Q 16 al-Naḥl, etc.) rather than *thematic-content-naming* (which works for Q 24 al-Nūr, Q 12 Yūsuf, etc.).

## 7. Q 67:3-4 — corpus-singleton phrase signature

Pre-registered novel test (Q067-F-03 — see `06-novel-findings.md`): the imperative *fa-rjiʿi al-baṣar* and the doxological-cosmological *bi-yadihi al-mulk* are corpus-singletons.

Computed from full corpus search across 6,236 verses (`quran-text/quran-no-tashkeel.json`):

| Phrase | Q 67 occurrences | Corpus occurrences | Verdict |
|:--|:-:|:-:|:--|
| *bi-yadihi al-mulk* (بيده الملك) | 1 (v. 1) | **1** | **CORPUS-SINGLETON** |
| *fa-rjiʿi al-baṣar* (فارجع البصر, with fāʾ) | 1 (v. 3) | **1** | **CORPUS-SINGLETON** |
| *irjiʿi al-baṣar* (ارجع البصر, no fāʾ) | 1 (v. 4) | 2 (Q 67:3 [via fa-rjiʿi] + Q 67:4) | corpus-singleton-doublet (Q 67-only) |
| *sabʿa samāwātin ṭibāqan* (سبع سماوات طباقا) | 1 (v. 3) | 2 (Q 67:3 + Q 71:15) | corpus-pair |
| *tabāraka alladhī* (تبارك الذي) | 1 (v. 1) | **5** (Q 25:1, 25:10, 25:61, 43:85, 67:1) | corpus-cluster (Q 25 dominant) |

The *bi-yadihi al-mulk* + *fa-rjiʿi al-baṣar* dyad gives Q 67:1-3 a **double-singleton signature** unmatched in the corpus. By comparison, Q 24:35 (āyat al-nūr) has *zero* corpus-singleton phrases at the 2-3-word level — its uniqueness is in its *parable structure*, not in any token-string. Q 67:1-4 sits in a different sub-class: **token-level lexical singularity**.

## 8. Position s=67 — post-Hijra-kink content-prediction

Q 67 sits at s = 67, well past the s=50 kink ([[h-new-660-compression-tail-gradient|H-NEW-660]]; [[h-new-700-phonological-compression-tail|H-NEW-700]]). The compression-tail laws predict:

- d̄_content(67) ≈ 0.96 − 0.012·17 = **0.756** (predicted)
- d̄_rhyme(67) ≈ 0.36 + 0.0041·17 = **0.430** (predicted)
- d̄_phoneme(67) ≈ at s<75 the kink is silent ≈ 0.001

Empirical (per `h-new-750.json` `per_surah[surah=67]`): mean_content_distance = **0.892**. This is *above* the predicted compression-tail value, consistent with the noise-level expected at single-surah grain (the law is window-level / regional, not pointwise).

Q 67 belongs to the **post-kink mufaṣṣal-awsāṭ zone** — content register loosens (lower d̄_content), rhyme tightens (lower entropy, dominant rāwī ر at 70%). The surah's empirical metrics are *typical for this zone*, not enhanced.

## 9. Architectural type classification

Per the project's three-class scheme + the Q 24 fourth-cell (see [[h-new-840-unified-architectural-score|H-NEW-840]], [[cross-finding-026-iʿjāz-architecture|cross-finding-026]]):

- **Structural-iʿjāz** (al-Bāqillānī *iʿjāz al-fawāṣil*): high UAS + high sig_A → Q 33, Q 1, Q 2, Q 9.
- **Theological-iʿjāz** (al-Khaṭṭābī *iʿjāz al-maʿnā*): low UAS but high *thuluth-al-Qurʾān* / *faḍāʾil* status → Q 112, Q 114.
- **Anti-iʿjāz**: low on both axes → Q 87, Q 105, Q 73, Q 83.
- **Outlier-without-fawāṣil-iʿjāz** (the Q 24 fourth-cell): high UAS via outlier+adjacency, low sig_A → Q 24 (sole exemplar).

**Q 67 is canonically *theological-iʿjāz*** — bottom-decile UAS (rank 102) but high recitation-tradition status. It pairs naturally with Q 112, Q 36 (Yāsīn), and Q 18 (al-Kahf). The corpus's classical *faḍāʾil*-rich-but-architecturally-modest cluster.

The empirical implication: **Q 67's distinctness lives in its CONTENT and RECITATION-TRADITION USE**, not in its *fawāṣil* virtuosity, outlier strength, or adjacency cost.

## 10. Cross-references to all H-NEW findings touching Q 67

- [[h-new-111-fisher-rao-mushaf|H-NEW-111]] — Q 67 mean FR distance to corpus = 0.892 (rank 67 / 114 — middle); nearest = Q 81 (0.753), Q 32 (0.753), Q 1 (0.758), Q 112 (0.761); farthest = Q 9 al-Tawba (1.204).
- [[h-new-590-outlier-spectrum|H-NEW-590]] — Q 67 NULL outlier; Δ = −0.20 pp; window {64-70}.
- [[h-new-700-phonological-compression-tail|H-NEW-700]] — Q 67 sits at s=67 in the post-kink zone; rhyme entropy 0.770 nats (moderately monorhyme; dominant ر at 70%).
- [[h-new-720-canonical-adjacency-cost|H-NEW-720]] — Q 66-Q 67 cost 0.078 (rank 47/113); Q 67-Q 68 cost 0.096 (rank 36/113); both mid-pack.
- [[h-new-750-ijaz-signature|H-NEW-750]] — Q 67 sig_A = +0.311 (rank 52/114, mid-pack); sig_B = −0.566 (rank 67); local cohesion 1.103 (high — Q 67 is content-similar to its mushaf neighbours).
- [[h-new-840-unified-architectural-score|H-NEW-840]] — Q 67 UAS = −2.053 (rank 102 / 114, bottom decile).
- [[h-new-860-hadith-architectural-alignment|H-NEW-860]] — Q 67 has high *faḍāʾil* density (grave-protection, nightly-recitation) without high UAS — classical attention is *recitation*-oriented, not *fawāṣila*-oriented; the *iʿjāz al-maʿnā* / *fadāʾil* lineage.
- [[cross-finding-026-iʿjāz-architecture|cross-finding-026]] — Q 67 confirms the *theological-iʿjāz* cell (high faḍāʾil + low UAS), alongside Q 112 and Q 36; the *al-Khaṭṭābī* axis.

## 11. Honest limits

- The **UAS rank 102/114 is a compound of three correlated axes** (outlier, adjacency-cost, |sig_A|). Each is z-scored and summed; no Bonferroni significance test on the rank itself. The "bottom decile" claim is *descriptive*, not *inferential*. See [[h-new-840-unified-architectural-score|H-NEW-840]] §5 for the UAS construction.
- The **NULL-classification of Q 67's outlier-strength** (Δ = −0.20 pp) means the H-NEW-590 7-window test fails to reject the null for Q 67. This is *not* the same as proving Q 67 has *no* architectural distinctness — only that the specific window-removal test does not detect a signal. Other tests (e.g., the corpus-singleton phrase signature in §7, or the recitation-tradition empirical profile in §3) capture different kinds of distinctness.
- The **mlk-stem NULL** (§6) uses QAC stem-root tokenization. Under different tokenization (e.g., counting the surface word *al-mulk* alone; or counting *malāʾika*-only; or splitting *malik*-king from *mulk*-dominion), the count would shift but not into significance: the highest possible interpretation gives ~3-4 tokens out of 208 (1.5%), still well above expected.
- The **FR-nearest-neighbour to Q 32** (rank 2, distance 0.753) is consistent with the classical *Alif-Lām-Mīm-Tanzīl + tabāraka* pair-recitation tradition (Tirmidhī idInBook 2975, Dārimī idInBook 2667). This is empirically vindicated — but the FR-distance K=500 root tokenization could have produced any neighbour by chance; the classical-tradition match is not a pre-registered prediction (it is post-hoc-noticed). A pre-registered version would be: "Q 67's FR-nearest-5 includes Q 32." Recorded as a post-hoc descriptive observation.
- The **rhyme entropy 0.770** places Q 67 at moderate monorhyme — *not* in the high-sig_A cluster (Q 55 ~0.4, Q 84 ~0.45). Q 67 has multi-rāwī fawāṣila (ر, ن, م) with some *yāʾ-zalāmiyya* / *nūn-zalāmiyya* alternations producing the sig_A=+0.31 mid-pack score.

## 12. One-paragraph synthesis

Q 67 al-Mulk is the project's clearest case of **theological-iʿjāz / faḍāʾil-prominence WITHOUT structural-architectural distinctness**. The mushaf places it at index 67 — well past the s=50 Hijra-kink, embedded in a Meccan-mufaṣṣal-awsāṭ zone (Q 64-70) where its content-distance, rhyme-dispersion, and adjacency-cost are all middle-of-pack. UAS rank 102 / 114 (bottom decile) sits Q 67 in the same architectural cell as Q 112, Q 87, Q 73, Q 83 — and yet Q 67's classical recitation-tradition prominence is high: the *al-Mānīʿa* / *al-Munjiya* grave-protection hadith corpus (Tirmidhī #2890 idInBook 2974, Abū Dāwūd idInBook 1401, Ibn Mājah idInBook 3522, Mālik idInBook 497) is one of the corpus's richest single-surah faḍāʾil traditions, and the Prophetic nightly-recitation tradition (Tirmidhī idInBook 2975, Dārimī idInBook 2667, paired with Q 32 *Alif-Lām-Mīm-Tanzīl*) crosses 9 books. The empirical FR-nearest-neighbour structure post-hoc supports the Q 32 ↔ Q 67 pairing (FR distance 0.753, rank 2 of 113). The mlk-stem density NULL (rank 54/114 by raw count, p=0.58 hypergeometric) refutes the "name-tracks-vocabulary" hypothesis at the corpus level — Q 67 is named for its *opening word*, not for any thematic-lexical concentration. The corpus-singleton phrase signature (*bi-yadihi al-mulk* and *fa-rjiʿi al-baṣar* are both unique to Q 67) is the surah's empirically-locked architectural fingerprint, but at the *token-level* not the *structural-architecture* level. Q 67 is therefore the corpus's canonical *al-Khaṭṭābī iʿjāz al-maʿnā* exemplar: its iʿjāz lives in its *content* and *use*, not in its *fawāṣila / outlier / adjacency* signature.
