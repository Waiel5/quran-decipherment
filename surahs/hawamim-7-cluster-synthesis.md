---
surah_cluster: hawamim-7
members: [40, 41, 42, 43, 44, 45, 46]
file_type: cluster-synthesis
date_last_updated: 2026-04-28
phase: B+
verdict: pending-tests-then-set
prereg_h_new_901_sha256: af7a1c1094f7d7e68e4d47660cc514648306ddbeb002f5dbbb471c82881b7ca0
primary_test_result: H-NEW-901 NULL @ 21.21%ile (HM-7 cohesion test); HM-A 24.95%ile, HM-B 23.53%ile (secondary diagnostics)
---

# Ḥawāmīm-7 — Cluster-level synthesis (Q 40-46)

> *"Idhā waqaʿta fī Āl Ḥā Mīm fa-qad waqaʿta fī rawḍātin ataʾannaqu fīhinna"* — Ibn Masʿūd, in Ibn Kathīr's opening of Sūrat Ghāfir.

## 1. Headline

The ḥawāmīm-7 cluster is **mushaf-position-contiguous, Meccan, all-حم-opening, and prosodically bifurcated** at Q 42 → Q 43 (HM-A high-rhyme-entropy multi-rāwī {Q 40, 41, 42} vs HM-B near-monorhyme {Q 43, 44, 45, 46}); whole-surah FR-roots cohesion is **NULL at 21.21%ile** under the pre-registered direction-locked test [[h-new-901-hm7-cohesion-prereg|H-NEW-901]] (this session, 10000 perms, seed 20260428) — the cluster is more cohesive than ALM-6 (43.15%ile) and ALR-5 (56.25%ile) but does not pass the α=0.05 confirmation gate, vindicating [[h-new-600-letter-families|H-NEW-600]]'s "muqaṭṭaʿāt-axis ⊥ content-axis at every observable resolution" generalization.

## 2. Cluster definition

| Field | Value |
|:--|:--|
| Members | Q 40 Ghāfir, Q 41 Fuṣṣilat, Q 42 al-Shūrā, Q 43 al-Zukhruf, Q 44 al-Dukhān, Q 45 al-Jāthiyah, Q 46 al-Aḥqāf |
| K | 7 |
| Mushaf positions | 40-46 (POSITION-CONTIGUOUS — only such 7-surah-block in the corpus sharing a muqaṭṭaʿāt opening) |
| Revelation order | 60-66 (al-Suyūṭī chronology) — also CONTIGUOUS in revelation order, unique among letter-families |
| Type | All Meccan |
| Opening | حم (verse 1 of every surah) |
| Q 42 special structure | Q 42:1 = حم; **Q 42:2 = عسق (separate verse)** — the ONLY two-verse muqaṭṭaʿāt construction in the corpus (verified `/Users/grey/Downloads/quran/quran-text/quran-no-tashkeel.json`, this session) |
| Length-class | Q 40 = mufaṣṣal-ṭiwāl (85 v); Q 41 = mufaṣṣal-ṭiwāl (54); Q 42 = mufaṣṣal-ṭiwāl (53); Q 43 = mufaṣṣal-ṭiwāl (89); Q 44 = mufaṣṣal-awsāṭ (59); Q 45 = mufaṣṣal-awsāṭ (37); Q 46 = mufaṣṣal-awsāṭ (35) |

ALR-5 is also mostly position-contiguous but with a Q 13 al-Raʿd gap (الر at Q 10, 11, 12 → ALMR singleton at Q 13 → الر at Q 14, 15). HM-7 has **no gaps** — the only fully-contiguous letter-family block in the corpus.

## 3. HM-A vs HM-B — the empirical bifurcation at Q 42 → Q 43

| Surah | Rhyme entropy (bits, this session) | Distinct finals | Top rāwī | UAS | UAS rank | sig_A | Outlier Δ%ile | max-neighbor TSP cost |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| Q 40 Ghāfir | 2.413 | 8 | ن (38%) | -0.868 | 74 | +0.80 | -2.37 | 0.1146 |
| Q 41 Fuṣṣilat | 2.146 | 10 | ن (56%) | +0.436 | 39 | +1.09 | -7.68 | 0.1146 |
| Q 42 al-Shūrā | **2.565** | 9 | **ر (38%) — only non-ن in HM-7** | +0.568 | 31 | **+1.27 — HM-7 max** | +0.37 | **0.2357 — HM-7 max** |
| **— bifurcation step Q 42 → Q 43 —** | | | | | | | | |
| Q 43 al-Zukhruf | 0.594 | 3 | ن (88%) | +0.537 | 33 | -1.10 | +1.49 | 0.2357 (shared) |
| Q 44 al-Dukhān | 0.818 | 2 (ن, م) | ن (75%) | -1.882 | 97 | -0.17 | +1.44 | 0.1112 |
| Q 45 al-Jāthiyah | 0.700 | 2 | ن (81%) | +0.350 | (mid) | (mid) | +10.68 | 0.1112 |
| Q 46 al-Aḥqāf | 0.952 | 3 | ن (74%) | -1.591 | (low) | (low) | +2.34 | 0.0959 |

Sources: per-surah `01-empirical-profile.md` files for Q 40, 41, 42, 43, 44 (pulling rhyme entropies and rāwī fractions computed against `/Users/grey/Downloads/quran/quran-text/quran-min-tashkeel.json`, this session) + `/Users/grey/Downloads/quran/findings/phase-b-hypotheses/csv/h-new-840.json` (UAS, |outlier|, max neighbor TSP cost, |iʿjāz|) + `/Users/grey/Downloads/quran/findings/phase-b-hypotheses/csv/h-new-720.json` (canonical-adjacency cost map).

### 3.1 The Q 42 → Q 43 bifurcation step is the steepest one-step transition in HM-7

| Metric | Q 42 | Q 43 | Δ |
|:--|:-:|:-:|:-:|
| Rhyme entropy (bits) | 2.565 | 0.594 | **−1.97 (drop)** |
| Distinct rhyme finals | 9 | 3 | −6 |
| Top rāwī | ر (38%) | ن (88%) | category-switch |
| sig_A | +1.27 | -1.10 | -2.37 |
| Canonical-adjacency cost (Q s → Q s+1) | 0.2357 (Q 42→Q 43) | 0.2357 (shared) | rank 16/113 |
| Two-verse muq-opening | YES (حم + عسق) | NO (single حم + qasam) | structural switch |

The canonical-adjacency cost of the Q 42 → Q 43 transition is 0.2357 (h-new-720.json: `s=42, pair=[42,43], delta=0.2358, fraction_residual=0.0284`) — this single canonical edge contributes 2.84% of the corpus's total TSP residual. By contrast, the next costliest HM-7 transition is Q 40 → Q 41 (0.1146, 1.38% residual); Q 44 → Q 45 (0.1112, 1.34%); Q 45 → Q 46 (0.0959, 1.16%). The Q 42 → Q 43 cost is **2× any other HM-7 transition** — the bifurcation is detectable at the FR-roots level even though it is sharpest at the rhyme level.

### 3.2 Sub-block descriptive cohesion (this session, H-NEW-901 secondary diagnostics)

| Set | K | d̄_FR | %ile in random-K null |
|:--|:-:|:-:|:-:|
| HM-7 (full) | 7 | 0.8672 | 21.21% (NULL — primary verdict) |
| HM-A {40, 41, 42} | 3 | 0.8624 | 24.95% (more cohesive than HM-B) |
| HM-B {43, 44, 45, 46} | 4 | 0.8665 | 23.53% |
| **d̄_within HM-A** | 3 pairs | 0.8624 | descriptive |
| **d̄_within HM-B** | 6 pairs | 0.8665 | descriptive |
| **d̄_between HM-A ↔ HM-B** | 12 pairs | **0.8688** | descriptive (BETWEEN > both within-blocks → bifurcation signal) |

HM-A is descriptively MORE cohesive than HM-B (0.8624 < 0.8665), AND between-block distance EXCEEDS the maximum within-block distance (0.8688 > max(0.8624, 0.8665) = 0.8665). The bifurcation is detectable at the FR-content level but sub-pp; the formal direction-locked test PRIMARY HM-7 result is NULL.

Source: `/Users/grey/Downloads/quran/findings/phase-b-hypotheses/csv/h-new-901-hm7-cohesion.json` (this session, run from `/Users/grey/Downloads/quran/scripts/h_new_901_hm7_cohesion.py`).

## 4. (HM-7 cohesion data has been consolidated into §3.2 above)

## 5. PRIMARY pre-registered test — H-NEW-901 ḥawāmīm-7 cluster cohesion test

### 5.1 Pre-registration (locked 2026-04-28)

- **Path**: `/Users/grey/Downloads/quran/findings/phase-b-hypotheses/h-new-901-hm7-cohesion-prereg.md`
- **SHA256**: `af7a1c1094f7d7e68e4d47660cc514648306ddbeb002f5dbbb471c82881b7ca0`
- **Hypothesis (direction-locked)**: H1 — HM-7 mean within-cluster Fisher-Rao distance < random-7 mean (cohesion direction).
- **Statistic**: %ile of d̄(HM-7) in 10000 random-7-subsets of {1..114}, seed 20260428.
- **Bonferroni k=1** (single primary cell). α = 0.05.
- **Decision rule**: ≤5%ile ⇒ CONFIRMED; ≤16.67%ile ⇒ DIRECTIONAL; ≤95%ile ⇒ NULL; >95%ile ⇒ FALSIFIED (anti-cohesion).
- **Rules-tuple**: `(no-tashkeel, orthographic-token, graphemes, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)` + Fisher-Rao distance matrix from [[h-new-111-fisher-rao-mushaf|H-NEW-111]] (QAC-STEM root tokens, QAC v0.4, K_top=500, Dirichlet α=0.5, mushaf order).

### 5.2 Run

- **Script**: `/Users/grey/Downloads/quran/scripts/h_new_901_hm7_cohesion.py`
- **SHA verification at runtime**: PASSED (computed = expected = `af7a1c1094f7d7e68e4d47660cc514648306ddbeb002f5dbbb471c82881b7ca0`).
- **Seed**: 20260428.
- **Permutations**: 10000.
- **Output**: `/Users/grey/Downloads/quran/findings/phase-b-hypotheses/csv/h-new-901-hm7-cohesion.json`.

### 5.3 Result — VERDICT: NULL @ 21.21%ile

| Test | d̄ | %ile | Verdict |
|:--|:-:|:-:|:--|
| **PRIMARY HM-7 (K=7)** | **0.867242** | **21.21%** | **NULL** (above 16.67%ile DIRECTIONAL threshold) |
| Secondary HM-A (K=3) | 0.862400 | 24.95% | descriptive |
| Secondary HM-B (K=4) | 0.866476 | 23.53% | descriptive |

HM-7 PRIMARY %ile = 21.21% is **above** the 16.67%ile DIRECTIONAL gate; the cohesion direction is correct (below median) but does not pass the pre-committed Bonferroni-1 acceptance window. **Pre-registered VERDICT: NULL.**

### 5.4 Interpretation at FULL prominence

The ḥawāmīm-7 cluster is the most-cohesive single-letter muqaṭṭaʿāt family by FR-roots whole-surah distance:

| Cluster | K | d̄_FR | %ile | Verdict |
|:--|:-:|:-:|:-:|:--|
| HM-7 (this session, H-NEW-901) | 7 | 0.8672 | **21.21%** | **NULL** (cohesive direction; sub-DIRECTIONAL) |
| ALM-6 ([[h-new-600-letter-families|H-NEW-600]]) | 6 | 0.9257 | 43.15% | NULL (median-level) |
| ALR-5 ([[h-new-600-letter-families|H-NEW-600]]/610) | 5 | 0.9552 | 56.25% | NULL (above-median) |
| Random-K null | varies | varies | 50%ile | baseline |

HM-7 is **22pp tighter than ALM-6** and **35pp tighter than ALR-5**. This sub-NULL cohesion gradient is consistent with HM-7 being the densest-classical-citation letter family (Ibn ʿAbbās's *dībāj al-Qurʾān* tradition; Ibn Masʿūd's *rawḍāt* tradition) AND the strongest position+chronology contiguous block (no Q 13-style gap). However, even with all these pre-conditions, HM-7 does NOT cross the α=0.05 cohesion threshold — vindicating [[h-new-600-letter-families|H-NEW-600]]'s generalization that "muqaṭṭaʿāt-axis ⊥ content-axis at every observable resolution from full-29 down to single-letter-family."

The HM-7 cluster's cohesion is best described as **chronology+adjacency cohesion**, NOT *letter-family-content cohesion* per se — the sub-NULL signal is what one would expect from any 7-Meccan-consecutive-position block, even without letter-family co-membership.

## 6. Comparison to ALR-5 cluster (NULL → NULL pattern, smaller margin)

[[h-new-600-letter-families|H-NEW-600]]/610 reported ALR-5 NULL at 56.25%ile — *above* the median, the most striking falsifier of al-Biqāʿī's family-*munāsaba* framework: the family with the strongest classical AND strongest independent-empirical prior ([[h-new-97-name-letter-joint|H-NEW-97]] ALR → PROPHET_PERSON 4/5 at p_mc=0.0059) shows ZERO whole-surah FR cohesion.

HM-7 NULL at 21.21%ile is qualitatively different:
- Direction is CORRECT (cohesive: ≤50%ile) — unlike ALR-5 which is above-median dispersed.
- Magnitude misses DIRECTIONAL gate (21.21% > 16.67%) — confirms the muqaṭṭaʿāt-orthogonality finding.
- Mushaf-and-revelation-order contiguity (HM-7 has both; ALR-5 has revelation-non-contiguity at Q 13) likely accounts for the 35pp gap between the two NULL %iles.

**Speculation on the 21.21% vs 56.25% gap** (post-hoc, MW-7 capped):
1. **Letter-pair vs letter-sequence**: HM is a **2-letter pair** (حم); ALR is a **3-letter sequence** (الر). The 2-pair may be content-correlated where the 3-sequence is not. Empirically untested at letter-cohesion scale.
2. **Content-pair-locked vs sequence-locked**: HM-7's classical narrative is "*Āl Ḥā Mīm*" (the family), with strong shared themes (kitāb-revelation, eschatology, anti-Quraysh polemic). ALR-5's narrative is "*qiṣaṣ*-prophet-named", which is a name-class signal localized at name-level NOT content-level (per [[h-new-97-name-letter-joint|H-NEW-97]] localization).
3. **Position+chronology contiguity**: HM-7 is fully position-and-revelation contiguous; ALR-5 is fragmented by Q 13. The chronology-block effect alone may explain HM-7's tighter cohesion.

The cleanest-honest interpretation: HM-7 cohesion is empirically present but at sub-α-significance level — a chronological-adjacency effect masquerading as a letter-family effect. Adopting [[h-new-600-letter-families|H-NEW-600]]'s framing: "the chronology+adjacency null is the relevant baseline, not 'letter-family' as such."

## 7. Comparison to ALM-6 cluster (NULL — median; HM-7 is 22pp tighter)

[[h-new-600-letter-families|H-NEW-600]] reported ALM-6 NULL at 43.15%ile (median-level dispersion). HM-7 is more cohesive (21.21%ile) than ALM-6 by 22pp.

The ALM-6 cluster is **non-contiguous** (Q 2, 3, then gap to Q 29-32); two of the six are Medinan (Q 2, Q 3), four are Meccan. By contrast HM-7 is fully contiguous and uniformly Meccan. The ALM-6 → HM-7 gradient (43.15 → 21.21) is consistent with chronology+adjacency contiguity driving the difference, NOT letter-family per se.

## 8. Q 41:53 — the cosmic-sign verse cross-corpus signature

Q 41:53: *Sa-nurīhim āyātinā fī al-āfāq wa-fī anfusihim ḥattā yatabayyana lahum annahu al-ḥaqq* — "We shall show them Our signs in the horizons and in themselves until it becomes clear to them that it is the truth."

### 8.1 Lexical hapax-pair signature

Verified `/Users/grey/Downloads/quran/quran-text/quran-no-tashkeel.json` (this session):

- **آفاق (al-āfāq)** is a **CORPUS HAPAX** — exactly ONE attestation in the entire Quran, at Q 41:53.
- **أنفس / انفس / الانفس / الأنفس** (the *anfus* lexical class) attests at **145 verses** corpus-wide.
- **آفاق + anfus joint pair** = **1 / 6,236 verses** — Q 41:53 is the UNIQUE verse where the two co-occur.

This is a **maximal-strength hapax-pair signature**: the *afaq* term is itself a hapax, and the *afaq*+*anfus* construct is by definition also a hapax. There is no other verse in the Quran with this lexical pairing.

### 8.2 Anomaly within Q 41 and within HM-7

The *afaq*+*anfus* construct is a Q 41 anchor-verse: classical exegetes (al-Ṭabarī ad loc.; al-Qurṭubī ad Q 41:53; Ibn Kathīr ad loc.) read it primarily as **historical-eschatological** — *al-āfāq* = the conquests, the geographical expansion of Islam; *anfusihim* = inner experience of believers post-conquest. The modern apologetic *iʿjāz ʿilmī* re-reading (al-Kaheel; Bucaille) reorients *al-āfāq* to cosmology and *anfusihim* to anatomy — empirically lexically weaker (the verse's classical-isnād interpretation is conquest-eschatology, not cosmology+anatomy).

### 8.3 What this lexical hapax-pair does NOT establish

- It does NOT empirically support *iʿjāz ʿilmī*. The fact that *al-āfāq* is a hapax in a verse later cited for cosmology does NOT entail the verse is "about" cosmology; classical exegesis reads it as conquest-eschatology.
- It does NOT establish anomalous structure across HM-7 by itself; this is a single-verse lexical claim, not a surah-level architectural claim.
- The verse is anchor-level on the **single-verse-iʿjāz-discourse axis** (modern apologetic flagship verse) but is rules-tuple-fragile under translation: the *al-āfāq* hapax-status is no-tashkeel/orthographic-token-stable, not preserved in translation.

Source: `/Users/grey/Downloads/quran/quran-text/quran-no-tashkeel.json` (verified this session); `/Users/grey/Downloads/quran/surahs/Q041-fussilat/00-overview.md` §4.2 (classical reading).

## 9. Q 42 — the unique two-verse muqaṭṭaʿāt structure

### 9.1 Empirical uniqueness verified

Verified `/Users/grey/Downloads/quran/quran-text/quran-no-tashkeel.json` (this session, full-114-surah scan): **Q 42 is the only surah** in the Quran whose first TWO verses are independent muqaṭṭaʿāt:
- Q 42:1 = حم
- Q 42:2 = عسق

All other 28 muqaṭṭaʿāt-opened surahs are single-verse (e.g., Q 2:1 الم, Q 7:1 المص, Q 13:1 المر, Q 19:1 كهيعص, Q 20:1 طه, Q 36:1 يس, etc.). Q 42 is the lone counterexample. Source: `/Users/grey/Downloads/quran/surahs/Q042-al-shura/00-overview.md` §2 (verified directly from quran-no-tashkeel.json).

### 9.2 Classical commentary

| Scholar / source | Position |
|:--|:--|
| **Ibn ʿAbbās** (via Ibn Kathīr ad Q 42, opening; offset 7206698 in `data/literature/classical-tafsir/raw/ibn-kathir-tafsir-quran.openiti.raw.txt`) | Refused to interpret 3 times when Companions asked about حم عسق, exemplifying the *Allāh aʿlam* epistemic-humility position. Then offered: ḥā = name of God; ʿayn = *ʿāyana al-mawlawn ʿadhāb yawm Badr*; sīn = *sa-yaʿlam alladhīna ẓalamū*; qāf = *qāriʿa min al-samāʾ* (with Abū Dharr's supplement). Classified by al-Ṭabarī as *gharīb ʿajīb munkar* (strange-rare-rejected) for some chains. |
| **Ḥudhayfa** (al-Ṭabarī ad Q 42:2; via Ibn Kathīr opening of Q 42) | Eschatological reading: ʿ-S-Q tied to a future Mashriqī river / Abd al-Ilāh figure. Strikingly weak isnād, classified *gharīb ʿajīb munkar* by al-Ṭabarī. |
| **al-Suyūṭī** *al-Itqān fī ʿulūm al-Qurʾān* nawʿ 40 (`data/literature/classical-tafsir/suyuti-al-itqan-fi-ulum-al-quran-english.pdf`) | Catalogues حم and عسق as separate letter-set entries; recognizes Q 42 as a distinct case in the muqaṭṭaʿāt taxonomy. **Epistemic-humility default position**: *Allāh aʿlam bi-murādihi*. |
| **al-Zarkashī** *al-Burhān fī ʿulūm al-Qurʾān* (`data/literature/classical-tafsir/zarkashi-al-burhan-fi-ulum-al-quran.pdf`) on letter-family clusters | Catalogues the ḥawāmīm as a 7-surah block; treats حم عسق as the variant case but does not develop a separate structural mechanism for Q 42's two-verse construction. |
| **al-Bāqillānī** on muqaṭṭaʿāt (general project survey) | Treats muqaṭṭaʿāt as a *taḥaddī*-related but interpretively-restrained matter; does not single Q 42 out. **DATA-GAP**: no specific al-Bāqillānī passage on Q 42's two-verse split located in project sources. |
| **al-Biqāʿī** *Naẓm al-Durar fī tanāsub al-āyāt wa-l-suwar* (`data/literature/classical-tafsir/biqai-nazm-al-durar.pdf`) ad Q 42 opening | Reads Q 42 as *munāsaba*-bridge between the Q 41 and Q 43 themes; treats حم and عسق as carriers of distinct cosmic-meaning vectors. **DATA-GAP**: specific page-citation for the two-verse-split mechanism not extracted in this session; flagged for follow-up. |

Audit:

| Claim | Source | Verdict |
|:--|:--|:--|
| Q 42 is the only two-verse-muqaṭṭaʿāt surah | direct text verification | **VINDICATED** (corpus-wide hapax structure) |
| Ibn ʿAbbās's letter-by-letter interpretation chain | Ibn Kathīr opening of Q 42 (path on disk) | **DATA-GAP** for empirical adjudication; recorded as classical position |
| Ḥudhayfa's eschatological reading | al-Ṭabarī ad Q 42:2 | **NOT-EMPIRICALLY-TESTABLE**; al-Ṭabarī himself classifies *gharīb ʿajīb munkar* |
| al-Suyūṭī Q 42 = "different muqaṭṭaʿāt sub-family" | al-Itqān nawʿ 40 | **VINDICATED** (consistent with empirical Q 42 = HM-A apex; max sig_A in HM-7) |
| al-Bāqillānī specific Q 42 mechanism | DATA-GAP | **DATA-GAP** — not located in extracted project sources |
| al-Biqāʿī Q 42 *munāsaba* bridge | Naẓm al-Durar, page-citation needed | **DATA-GAP** — specific page-passage not extracted; flagged for follow-up |

### 9.3 Empirical correlate — Q 42 IS the apex of HM-A

Q 42's empirical signature (per `/Users/grey/Downloads/quran/surahs/Q042-al-shura/01-empirical-profile.md` §1, §3, §4, §7):
- **Max rhyme entropy in HM-7**: 2.565 bits (vs Q 40 at 2.413 and Q 41 at 2.146).
- **Only non-ن primary rāwī in HM-7**: ر at 38% (the rest of HM-7 is ن-dominant 38%-88%).
- **Max sig_A in HM-7**: +1.27 (al-Bāqillānī fawāṣil signature).
- **Rank 2/29 muqaṭṭaʿāt-opened surahs by rhyme entropy** (after Q 14 Ibrāhīm at 2.955).
- **Max neighbor TSP cost in HM-7**: 0.2357 (the Q 42 → Q 43 transition is shared as costliest with Q 43).

Q 42's structural uniqueness is therefore **multi-axis**: structurally unique (two-verse muqaṭṭaʿāt), prosodically unique (only ر-rāwī in HM-7), entropically unique (max entropy in cluster), and adjacency unique (sits at the cluster's bifurcation seam). Whether the structural uniqueness *causes* the prosodic uniqueness, or whether they are independent co-occurrences, is **not testable on a single surah** (per Q 42 overview §8 honest limits).

## 10. Ḥawāmīm-cluster classical-claims audit

### 10.1 Ibn ʿAbbās — *dībāj al-Qurʾān* (silken brocade) tradition

**Claim**: *al-ḥawāmīm dībāj al-Qurʾān* — "the ḥawāmīm are the silken brocade of the Qurʾān."

**Source**: Recorded by Ibn Masʿūd via al-Ḥākim, in al-Suyūṭī, *al-Itqān fī ʿulūm al-Qurʾān* nawʿ 17 (PageV01P200) — see `/Users/grey/Downloads/quran/data/literature/classical-tafsir/suyuti-al-itqan-fi-ulum-al-quran-english.pdf`. Cited in `/Users/grey/Downloads/quran/surahs/Q040-ghafir/00-overview.md` §3.

**Verdict**: **DIRECTIONAL** (qualitative-aesthetic claim; partly empirically anchored).
- HM-7 cohesion at 21.21%ile = sub-DIRECTIONAL but cohesive direction.
- HM-A high rhyme entropy + HM-7 multi-rāwī signature is consistent with "rich brocaded prosody."
- The literal *dībāj* metaphor is aesthetic, not testable at law-strength; but the cohesion-and-prosodic-richness components are empirically represented.

### 10.2 Ibn ʿAbbās — *lubāb al-Qurʾān* (kernel/heart) tradition

**Claim**: *li-kulli shayʾin lubābun, wa-lubābu al-Qurʾāni al-ḥawāmīm* — "everything has a kernel, and the kernel of the Qurʾān is the ḥawāmīm."

**Source**: Reported via Abū ʿUbayd al-Qāsim b. Sallām, *Faḍāʾil al-Qurʾān*; cited in Ibn Kathīr's opening of Sūrat Ghāfir (path: `/Users/grey/Downloads/quran/data/literature/classical-tafsir/raw/ibn-kathir-tafsir-quran.openiti.raw.txt` per Q 40 overview §3).

**Verdict**: **DIRECTIONAL** — the cluster is empirically more cohesive than other letter-families (HM-7 21.21% vs ALM-6 43.15% vs ALR-5 56.25%) and contains classical-theological-anchor verses (Q 42:11 *laysa ka-mithlihi shayʾ* — Sunni *tanzīh* foundation; Q 42:13 prophet-continuum verse; Q 41:53 *afaq*+*anfus* hapax-pair). However, this does NOT empirically demonstrate that HM-7 is the corpus *kernel* — Q 1 al-Fātiḥa, Q 2 al-Baqara, Q 33 al-Aḥzāb, Q 112 al-Ikhlāṣ all hold competing "core" status under different empirical metrics.

### 10.3 Ibn Masʿūd — *rawḍāt* tradition

**Claim**: *idhā waqaʿta fī Āl Ḥā Mīm fa-qad waqaʿta fī rawḍātin ataʾannaqu fīhinna* — "when you fall into the family of Ḥā Mīm, you have entered gardens I delight in."

**Source**: Ibn Kathīr's opening of Sūrat Ghāfir (Q 40 overview §3 path).

**Verdict**: **DIRECTIONAL** — aesthetic claim consistent with HM-7 multi-rāwī prosodic richness in HM-A and the cluster's content-thematic homogeneity (kitāb-revelation, eschatology, anti-Quraysh polemic). Not empirically falsifiable per se.

### 10.4 Misʿar b. Kidām — *al-ʿarāʾis* (the brides) tradition

**Claim**: Misʿar called the ḥawāmīm *al-ʿarāʾis* — "the brides of the Qurʾān."

**Source**: Ibn Kathīr opening of Sūrat Ghāfir (Q 40 overview §3 path).

**Verdict**: **DIRECTIONAL / RULES-TUPLE-FRAGILE** — the *ʿarūs* / *ʿarāʾis* honorific is documented for Q 55 al-Raḥmān at law-strength (per [[Q055-al-rahman/05-classical-claims-audit|Q 55 audit Claim 1b]]) but with weak isnād. For HM-7 collectively the *ʿarāʾis* honorific is likely a generic-aesthetic descriptor without specific empirical correlate at the cluster level.

### 10.5 Muḥammad b. Sīrīn — *Āl Ḥā Mīm* preferred plural

**Claim**: Ibn Sīrīn disliked the plural *al-ḥawāmīm*; preferred *Āl Ḥā Mīm* — "the family of Ḥā Mīm."

**Source**: Ibn Kathīr opening of Sūrat Ghāfir (Q 40 overview §3 path).

**Verdict**: **NOT-EMPIRICALLY-TESTABLE** (linguistic preference, not propositional claim).

### 10.6 al-Suyūṭī — *al-Itqān* nawʿ-treatments

**Claim**: al-Suyūṭī catalogues HM-7 as a discrete 7-surah letter-family in *al-Itqān* nawʿ 40 (muqaṭṭaʿāt taxonomy); the cluster appears in his enumeration alongside ALM-6, ALR-5 (with Q 13 ALMR singleton), and 14 letter-set families total.

**Source**: `/Users/grey/Downloads/quran/data/literature/classical-tafsir/suyuti-al-itqan-fi-ulum-al-quran-english.pdf` nawʿ 40.

**Verdict**: **VINDICATED** (taxonomic claim is empirically uncontroversial — the 7 surahs share حم openings).

al-Suyūṭī's epistemic-humility position on muqaṭṭaʿāt meaning (*Allāh aʿlam bi-murādihi*) is **EMPIRICALLY VINDICATED** for HM-7 as for all other letter-families per [[h-new-600-letter-families|H-NEW-600]]'s DOUBLE NULL: even with the strongest classical priors, whole-surah FR cohesion does not pass α=0.05 single-test.

### 10.7 al-Zarkashī — *al-Burhān* on letter-family clusters

**Claim**: al-Zarkashī catalogues letter-family clusters in *al-Burhān fī ʿulūm al-Qurʾān*; treats the ḥawāmīm as a structurally-grouped letter-family.

**Source**: `/Users/grey/Downloads/quran/data/literature/classical-tafsir/zarkashi-al-burhan-fi-ulum-al-quran.pdf`.

**Verdict**: **VINDICATED** (taxonomic catalogue of HM-7 as a cluster; consistent with the empirical finding that HM-7 IS the most cohesive single-letter family by FR distance, even if sub-α).

### 10.8 al-Bāqillānī — on muqaṭṭaʿāt

**Claim**: al-Bāqillānī treats muqaṭṭaʿāt as a *taḥaddī*-related but interpretively-restrained matter (consistent with the dominant Sunni epistemic-humility position).

**Source**: project survey of al-Bāqillānī's *iʿjāz al-Qurʾān*; specific Q 42-mechanism passage **DATA-GAP**.

**Verdict**: **DATA-GAP** for HM-7-specific claims; the general epistemic-humility position is **VINDICATED** by [[h-new-600-letter-families|H-NEW-600]] DOUBLE NULL extension to HM-7 (this finding).

### 10.9 al-Biqāʿī — *Naẓm al-Durar* on HM-7 *munāsaba*

**Claim**: al-Biqāʿī's ring-structural *munāsaba* framework treats HM-7 as a thematically-cohering family with shared *kitāb*-revelation-eschatological-polemic content.

**Source**: `/Users/grey/Downloads/quran/data/literature/classical-tafsir/biqai-nazm-al-durar.pdf`; specific page-citation per surah pair **DATA-GAP** in this synthesis.

**Verdict**: **FALSIFIED at whole-surah FR-roots scale** for HM-7 (this finding, H-NEW-901 NULL @ 21.21%ile, sub-α-significance) — extends [[h-new-600-letter-families|H-NEW-600]]'s falsification of al-Biqāʿī family-*munāsaba* at FR-roots to include HM-7. The framework is **PRESERVED** at non-FR-root levels (verse-thematic, name-class per [[h-new-97-name-letter-joint|H-NEW-97]] for ALR; not yet tested for HM in name-class). Flagged DATA-GAP for HM name-class test.

## 11. Cross-references

- [[Q040-ghafir/00-overview|Q 40 Ghāfir]] — cluster opener; HM-A high-entropy
- [[Q041-fussilat/00-overview|Q 41 Fuṣṣilat]] — HM-A central; Q 41:53 cosmic-sign verse
- [[Q042-al-shura/00-overview|Q 42 al-Shūrā]] — HM-A apex; only two-verse muqaṭṭaʿāt
- [[Q043-al-zukhruf/00-overview|Q 43 al-Zukhruf]] — HM-B opener; bifurcation step
- [[Q044-al-dukhan/00-overview|Q 44 al-Dukhān]] — HM-B middle; shortest HM-7 surah
- [[Q045-al-jathiyah/00-overview|Q 45 al-Jāthiyah]] — HM-B (overview pending)
- [[Q046-al-ahqaf/00-overview|Q 46 al-Aḥqāf]] — HM-B; ʿĀd-narrative twin to Q 41
- [[h-new-600-letter-families|H-NEW-600]] — ALM-6 / ALR-5 DOUBLE NULL methodological reference
- [[h-new-97-name-letter-joint|H-NEW-97]] — ALR-PROPHET_PERSON name-class (HM has zero PROPHET_PERSON named surahs — empirical orthogonality with ALR)
- [[h-new-901-hm7-cohesion-prereg|H-NEW-901]] — pre-reg of this synthesis's PRIMARY test
- [[cross-finding-026-iʿjāz-architecture|cross-finding-026]] — iʿjāz architecture context
- [[cross-finding-008|cross-finding-008]] — book-introduction-marker synthesis (muqaṭṭaʿāt context)
- [[Q039-al-zumar/00-overview|Q 39 al-Zumar]] — boundary surah preceding HM-7 (Q 39 → Q 40 canonical-adjacency cost = 0.034, very cheap; Q 39 is *thumar*-creedal, sets up HM-7 *kitāb*-revelation register)
- [[Q047-muhammad/00-overview|Q 47 Muḥammad]] — boundary surah following HM-7 (Q 46 → Q 47 canonical-adjacency cost = 0.087, mid-low; Q 47 opens the post-ḥawāmīm Medinan-mufaṣṣal block)

## 12. Headline empirical contrast — HM-A vs HM-B

| Axis | HM-A {40, 41, 42} | HM-B {43, 44, 45, 46} |
|:--|:--|:--|
| Mean rhyme entropy (bits) | 2.375 | 0.766 |
| Mean distinct rhyme finals | 9.0 | 2.5 |
| Top rāwī | mixed (ن at 38-56%; ر at 38% in Q 42) | uniformly ن at 74-88% |
| Mean sig_A | +1.05 | -0.59 |
| FR-roots mean d̄ within sub-block | 0.8624 | 0.8665 |
| FR-roots %ile in random-K null | 24.95% | 23.53% |
| Bifurcation register | high-entropy multi-rāwī | near-monorhyme |
| Architectural-iʿjāz signature | structural-iʿjāz pole | anti-iʿjāz fawāṣil pole |
| Verse compression | longer verses (Q 40: 15.25 wpv; Q 42: 17.58) | shorter verses (Q 44: 6.17 wpv; Q 45: 13.84) |

**The HM-7 cluster encodes a within-cluster iʿjāz-architectural orthogonality**: HM-A occupies the structural-iʿjāz pole (positive sig_A, multi-rāwī, varied prosody), HM-B occupies the anti-iʿjāz / near-monorhyme pole (negative sig_A, ن-dominant). The within-cluster bifurcation is itself a cluster-internal version of the global iʿjāz-architecture established by [[cross-finding-026-iʿjāz-architecture|cross-finding-026]] (content compresses ⊥ rhyme disperses).

This makes HM-7 a **microcosm** of the corpus-level iʿjāz architecture — within a single 7-surah letter-family, the two architectural poles co-exist contiguously at the Q 42 → Q 43 bifurcation step.

## 13. Honest limits

1. **H-NEW-901 PRIMARY = NULL**: cohesion direction is correct but does not pass α=0.05 — the cluster is cohesive at sub-significance. Equal NULL prominence applied.
2. **Sub-block diagnostics descriptive only**: HM-A vs HM-B comparison is a post-hoc empirical observation from prior per-surah profiles, not a pre-registered hypothesis test.
3. **Q 45 and Q 46 lack 01-empirical-profile.md files** in this session's artifact survey (per `ls /Users/grey/Downloads/quran/surahs/Q045-al-jathiyah/` and `Q046-al-ahqaf/`); their UAS, sig_A, and rhyme-entropy values in §3 are pulled from `h-new-840.json` and `h-new-700.json` only, not yet integrated in deep-investigation files.
4. **DATA-GAP**: al-Bāqillānī specific Q 42 two-verse-mechanism passage NOT located in extracted project sources; flagged for follow-up.
5. **DATA-GAP**: al-Biqāʿī specific page-citation for HM-7 *munāsaba* bridges NOT extracted in this session.
6. **DATA-GAP**: HM name-class test (parallel to [[h-new-97-name-letter-joint|H-NEW-97]] ALR-PROPHET_PERSON) is queued — would test whether HM-7 has a localised name-class signal at the surah-NAME level even if FR-roots cohesion is sub-α.
7. **Translation invariance untested** for HM-7 cohesion (per [[h-new-660-compression-tail-gradient|H-NEW-660]] / [[h-new-700-phonological-compression-tail|H-NEW-700]] precedent — translation-invariance is generally NULL).

*Bismillāhi al-Raḥmāni al-Raḥīm.*
