---
surah: 109
surah_name_ar: الكافرون
surah_name_translit: al-Kāfirūn
surah_name_english: The Disbelievers
file_type: overview
date_last_updated: 2026-05-09
phase: B+
verdict: SCAFFOLD-COMPLETE — 9-file template + 4 pre-registered tests + 5 classical claims audited
specialist: Q109-al-kafirun-specialist
saturation_rank: 2
saturation_value: 0.333
five_qul_cluster_member: true
ring_topology_neighbor: Q108→Q109→Q110 in 13 seamless seams (Q 109→Q 110 rank-1 cheapest seam)
fr_centroid_rank: 19/114
---

# Q 109 al-Kāfirūn — Overview


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

## 1. Basic facts

| Property | Value | Source |
|:--|:--|:--|
| Surah ID | 109 | canonical |
| Arabic name | الكافرون | canonical |
| Transliteration | al-Kāfirūn | canonical |
| English meaning | "The Disbelievers" / "The Rejecters" / sometimes "The Rejection Chapter" | classical |
| Verse count | 6 | `/Users/grey/Downloads/quran/quran-text/quran-no-tashkeel.json` Q109 (Hafs-Kūfan) |
| Position in mushaf | 109 (sixth-from-last) | canonical |
| Type | Meccan (majority view: al-Suyūṭī *al-Itqān*; minority Medinan asbāb on Hudaybiyya) | classical disagreement |
| Position in revelation order (Egyptian) | 18 | `/Users/grey/Downloads/quran/data/revelation-order.csv` |
| Word count (no-tashkeel orthographic) | 27 | computed from `quran-no-tashkeel.json` |
| Letter count (no-tashkeel, no spaces) | 99 | computed |
| Distinct roots (QAC v0.4) | 4 | qwl, kfr, ʿbd, dyn |
| Root tokens (QAC v0.4) | computed; root mass dominated by ʿbd (8 tokens of 27 words ≈ 30%) | `data/morphology/quranic-corpus-morphology-0.4.txt` |
| Bismala status | Standard (counted only in Q 1 per project rules-tuple) | canonical |
| Predominant rāwī (final-letter) | ن (3/6 = 50%; د 2/6 = 33%; م 1/6 = 17%) | computed |
| Rhyme entropy (Shannon, nats) | 1.0114 | `findings/phase-b-hypotheses/csv/h-new-750.json` |

## 2. Classical names of this surah

- **al-Kāfirūn** (الكافرون) — "The Disbelievers" (canonical name; from v.1 *yā ayyuhā al-kāfirūn*)
- **Sūrat al-Munābadha** (المنابذة) / **Sūrat al-Barāʾa** (البراءة) — the surah of disavowal / quittance (al-Suyūṭī *al-Itqān*, listing of surah-names; classical thematic naming)
- **Sūrat al-Muqashqisha** (المقشقشة, "the cleansing surah") — alongside Q 112 al-Ikhlāṣ; named so because the Companion ʿAbdullāh b. ʿAbbās is reported to have said *al-muqashqishatān humā* "the two cleansing surahs" referring to the pair (al-Suyūṭī, *al-Itqān*; al-Ṭabarī)
- **Qul yā ayyuhā al-Kāfirūn** — by its opening verse (classical citation form, e.g., al-Tirmidhī ḥadīth #2976)

The naming-multiplicity (≥4 classical names) is moderate. The pair-name *al-muqashqishatān* (the two cleansing surahs) for Q 109 + Q 112 specifically links the two as a doctrinally-paired unit independent of recitational pairing — see §10 below.

## 3. Opening formula

Q 109 opens with **qul yā ayyuhā al-kāfirūn** ("Say, O you disbelievers"). It is the *only* surah in the corpus whose opening words are *qul yā ayyuhā* + a vocative addressed-to-disbelievers. The construction has no other surah-initial attestation. The *qul yā ayyuhā* family at full-corpus scale appears at:

| Slot | Vocative | Surahs |
|:--|:--|:--|
| qul yā ayyuhā al-kāfirūn | (only opener) | Q 109:1 |
| qul yā ayyuhā al-nās | mid-surah | multiple (Q 7:158, Q 10:104, Q 22:49) |
| qul yā ayyuhā ahla al-kitāb | mid-surah | Q 5:59, Q 5:68 |

The *qul yā ayyuhā al-kāfirūn* construction is **corpus-unique as a surah opener** and one of two corpus-unique direct-address rhetorical openers (the other being Q 33's *yā ayyuhā al-nabī*). See [[h-new-74-qul-distribution|H-NEW-74]] Cell 3 for the full v1-w1 *qul* opener inventory.

Q 109 sits inside the **5-surah *qul*-opener cluster** {Q 72, Q 109, Q 112, Q 113, Q 114} — exactly the surahs whose first word is the bare imperative *qul* (per [[h-new-74-qul-distribution|H-NEW-74]] Cell 3). Within this cluster:
- Q 72 al-Jinn: *qul ūḥiya ilayya* — revelation-disclosure opener
- **Q 109 al-Kāfirūn**: *qul yā ayyuhā al-kāfirūn* — confrontation opener (the only one)
- Q 112 al-Ikhlāṣ: *qul huwa Allāh aḥad* — theological declaration
- Q 113 al-Falaq: *qul aʿūdhu bi-rabbi al-falaq* — refuge-formula
- Q 114 al-Nās: *qul aʿūdhu bi-rabbi al-nās* — refuge-formula

Q 109 is the **only confrontation-opener** in the 5-*qul* cluster. The other four are revelation-disclosure (Q 72), theological declaration (Q 112), and refuge-formulae (Q 113-114). This makes Q 109 the **rhetorical-extreme of the cluster** — the surah explicitly framed against the disbelievers, while the others articulate creed or seek refuge.

## 4. Length classification

Q 109 is in the **mufaṣṣal-qiṣār** zone (Q 93-114 per al-Zarkashī *al-Burhān fī ʿulūm al-Qurʾān*). At 6 verses / 27 words / 99 letters it is in the bottom-decile by length (rank ~14 from the bottom). Among the 5-*qul*-openers it is **mid-length** (Q 112 = 4v, Q 113 = 5v, **Q 109 = 6v**, Q 114 = 6v, Q 72 = 28v).

## 5. Rhyme structure

Verified verse-final letters (computed from `quran-no-tashkeel.json`):

| Verse | Last word | Final letter (rāwī) | Final phoneme cluster |
|:-:|:-:|:-:|:-:|
| 1 | الكافرون | ن | -ūn |
| 2 | تعبدون | ن | -ūn |
| 3 | أعبد | د | -ʿbud |
| 4 | عبدتم | م | -tum |
| 5 | أعبد | د | -ʿbud |
| 6 | دين | ن | -īn |

**Rhyme distribution**: ن × 3 (50%, vv. 1,2,6), د × 2 (33%, vv. 3,5 — the refrain), م × 1 (17%, v.4). Rhyme entropy = 1.0114 nats — moderate-high diversity.

The rhyme structure mirrors the **content architecture**:
- ن (vv. 1-2): outward-address ("disbelievers" → "what you worship")
- د (vv. 3, 5 — the refrain): "what I worship" — the identical-line refrain
- م (v.4): "what you worshipped (past)" — the temporal extension
- ن (v.6): closing detente ("your religion"/"my religion" — *dīn*)

The rhyme returns to ن at v.6, **closing the inclusio** with the vv. 1-2 ن frame. This makes Q 109 a rhyme-bracketed inclusio (ن...د/م/د...ن), with the doctrinal divergence inside the bracket.

## 6. Empirical architectural profile (headline)

Pulled from `findings/phase-b-hypotheses/csv/h-new-{590,720,750,840,111,1320}.json`:

| Metric | Value | Rank / 114 | Source |
|:--|:--:|:--:|:--|
| **UAS (Unified Architectural Score)** | **−0.1433** | 53 / 114 (mid-corpus) | `h-new-840.json` `all_uas` |
| Outlier-strength Δ%ile | 0.00 pp | rank 45 / 114 (NULL) | `h-new-590.json` `all_surahs_results` |
| **iʿjāz signature sig_A** (rhyme-purity & local-cohesion) | **+1.5232** | **rank 17 / 114** (top-15%) | `h-new-750.json` per_surah |
| **iʿjāz signature sig_B** (rhyme + content distinctiveness) | **+2.1584** | **rank 5 / 114** (top decile, near-extreme) | `h-new-750.json` |
| Local cohesion (1-step) | 2.7825 | very high | `h-new-750.json` |
| Mean FR distance to corpus | 0.8135 | **rank 19 / 114** (more central than typical) | `h-new-111.json` D_matrix (computed) |
| Q 108-Q 109 canonical-adjacency cost | 0.1341 length-units (1.62% of TSP residual) | rank 31 / 113 | `h-new-720.json` |
| **Q 109-Q 110 canonical-adjacency cost** | **0.0000 (clamped from delta_raw = −0.0307)** | **rank 1 / 113 (RANK-1 cheapest seam)** | `h-new-720.json` |
| **Refrain saturation (max-repeat / verse-count)** | **0.333** (2/6) | **rank 2 / 114** | `h-new-1320.json` |
| FR distance to Q 112 al-Ikhlāṣ | 0.3611 | **4th-closest neighbor** in corpus | computed |

**Architectural-cell classification**: Q 109 is in the *iʿjāz al-fawāṣil* cell of [[cross-finding-026-iʿjāz-architecture|cross-finding-026]] §13 (rhyme-purity-driven), with **rank 5 in sig_B** placing it in the top decile of rhyme-residualized iʿjāz signature — among the very-strongest fawāṣil-driven short surahs.

**Three superlatives**:
1. **Rank-1 cheapest TSP-seam** at Q 109→Q 110 (one of the 13 corpus-EXACT seamless-transitions per [[h-new-1240|H-NEW-1240]])
2. **Rank-2 by saturation** in [[h-new-1320|H-NEW-1320]] (33.3% of verses are the refrain *wa-lā antum ʿābidūna mā aʿbud*)
3. **Rank-5 in iʿjāz sig_B** — top-decile rhyme-residualized iʿjāz score

## 7. Verbatim text (canonical, no-tashkeel)

Source: `/Users/grey/Downloads/quran/quran-text/quran-no-tashkeel.json` Q 109 verses (cross-validated against `quran-min-tashkeel.json` and `quran-full-tashkeel.json`).

| Verse | Arabic (no-tashkeel) | Transliteration | English (Sahih Intl, illustrative) |
|:-:|:--|:--|:--|
| 1 | قل يا أيها الكافرون | *qul yā ayyuhā l-kāfirūn* | "Say, O disbelievers!" |
| 2 | لا أعبد ما تعبدون | *lā aʿbudu mā taʿbudūn* | "I do not worship what you worship." |
| 3 | ولا أنتم عابدون ما أعبد | *wa-lā antum ʿābidūna mā aʿbud* | "Nor are you worshippers of what I worship." |
| 4 | ولا أنا عابد ما عبدتم | *wa-lā anā ʿābidun mā ʿabadtum* | "Nor will I be a worshipper of what you have worshipped." |
| 5 | ولا أنتم عابدون ما أعبد | *wa-lā antum ʿābidūna mā aʿbud* | "Nor are you worshippers of what I worship." |
| 6 | لكم دينكم ولي دين | *lakum dīnukum wa-liya dīn* | "For you is your religion, and for me is mine." |

**Identity check**: vv. 3 and 5 are **byte-identical** (computed: `verse_3 == verse_5` → True). This is the ḥaqīqī refrain — corpus-rare for back-to-back identical lines separated by a single intervening verse.

## 8. Saturation outlier — Q 109's rank in [[h-new-1320|H-NEW-1320]]

H-NEW-1320 (refrain-saturation corpus-rank, locked 2026-05-09) found:

| Rank | Surah | Repeat count | Saturation | Top repeated verse |
|:-:|:--|:-:|:-:|:--|
| 1 | Q 55 al-Raḥmān | 31 | 0.397 | *fa-bi-ayyi ālāʾ rabbikumā tukadhdhibān* |
| 2 | Q 77 al-Mursalāt | 10 | 0.200 | *waylun yawmaʾidhin li-l-mukadhdhibīn* |
| 3 | Q 26 al-Shuʿarāʾ | 8 | 0.035 | *wa-inna rabbaka la-huwa al-ʿazīzu al-raḥīm* |
| ... | | | | |
| 15 | **Q 109 al-Kāfirūn** | **2** | **0.333** | ***wa-lā antum ʿābidūna mā aʿbud*** |

Q 109 ranks **#15 by absolute repeat count** (only 2) but **#2 by saturation** (only Q 55 saturates higher at 0.397). The saturation interpretation: among all 114 surahs, only Q 55 al-Raḥmān has a higher fraction of its verses occupied by an exact-identical refrain.

**Q 109 is therefore the corpus's "hyper-compressed refrain surah"** — a 6-verse short-Meccan structure where 1/3 of the verses (vv. 3 and 5) are byte-identical. This is in contrast to:
- Q 55: macro-refrain (31 repeats / 78 verses = 39.7%) — long surah, high count + high saturation
- **Q 109: micro-refrain (2 repeats / 6 verses = 33.3%) — short surah, low count + extreme saturation**
- Q 77: tier-2 macro (10 repeats / 50 verses = 20%) — eschatological-warning refrain

## 9. Refrain-architecture interpretation

The Q 109 refrain *wa-lā antum ʿābidūna mā aʿbud* is structurally distinct from the Q 55 / Q 77 / Q 26 refrains:

| Surah | Refrain | Function | Audience |
|:--|:--|:--|:--|
| Q 55 | *fa-bi-ayyi ālāʾ rabbikumā tukadhdhibān* | Blessing-acknowledgement-rebuke | Dual (jinn + ins) |
| Q 77 | *waylun yawmaʾidhin li-l-mukadhdhibīn* | Eschatological-judgment-warning | 3rd-person deniers |
| Q 26 | *wa-inna rabbaka la-huwa al-ʿazīzu al-raḥīm* | Prophet-cycle pericope-closer | Prophet (consolation) |
| **Q 109** | ***wa-lā antum ʿābidūna mā aʿbud*** | **Mutual-exclusion declaration** | **2nd-person disbelievers (direct)** |

Q 109's refrain is the **only refrain in the top-15 saturation set that is a direct-address declaration to the disbelievers**. This makes Q 109's rhetorical function corpus-unique even within the 4-tier refrain architecture extended by H-NEW-1320:

- Q 55 (tier-1 macro): the dual-audience joint-creation announcement
- Q 77 (tier-2 macro): the eschatological warning to deniers
- Q 26 (tier-3 macro): the prophet-cycle consolation
- **Q 109 (saturation-extreme micro)**: the mutual-exclusion declaration

The saturation-axis ranking (vs absolute-count-axis ranking) is itself a separate test family ([[Q109-F-01-saturation-rank-replication|H-NEW-1322]] queued in this folder, see §06).

## 10. The *al-muqashqishatān* doctrinal pair (Q 109 + Q 112)

Classical usage names Q 109 + Q 112 together as the **al-muqashqishatān** ("the two cleansing surahs"). The naming is reported on Companion authority (Ibn ʿAbbās per al-Suyūṭī *al-Itqān*) and underscores a **doctrinal pairing**: Q 109 disavows polytheism (*barāʾa*), Q 112 affirms tawḥīd (*ikhlāṣ*) — together they form the negation/affirmation of the creed.

**Empirically, Q 109 + Q 112 form an FR-cohesive pair**:
- Q 109 ↔ Q 112 FR distance = **0.3611** (Q 112 is the **4th-closest neighbor** of Q 109 out of 113)
- Random-pair null mean = 0.9232 (perm p = 0.0175 single-test)
- This pair is one of the 6 canonical 9-book-hadith-attested pair-recitation traditions catalogued in [[cross-finding-028|cross-finding-028]]

The pair survives:
- Permutation test against random pairs (single-test p = 0.0175)
- Inclusion in the 6-pair cross-finding-028 PASS-DIRECTED ensemble (mean FR=0.611 vs corpus mean 0.9235, perm p=0.00090; length-controlled p=0.0224)
- Even though the prompt-flagged "Maghrib/Fajr-sunnah/ṭawāf Q 109/Q 112" label was identified as the "lone exception" pair in cross-finding-028's length-controlled secondary, this is because the pair is itself **inside the muʿawwidhāt-saturated tail** (Q 109 is rank 19/114 by FR-centroid, Q 112 is rank 1/114 — **Q 112 sits at the structural center**, so all its short-mufaṣṣal neighbors look "expected-close" under length-control). The pair does *not* fail the cohesion test; it passes the unconditional one and lands at the boundary of the conditional one (cross-finding-028 explicitly labels Q 109/Q 112 a saturation-tail exception, not a NULL).

## 11. The 5-*qul*-opener cluster cohesion

Inline-Python test (this file's specialist run, seed = 20260509, n_perm = 10000):

```
5-qul cluster {Q 72, Q 109, Q 112, Q 113, Q 114}:
  Mean intra-pair FR distance: 0.4983
  Random-5 null mean: 0.9236 ± 0.1009
  z = −4.217
  perm p = 0.00260   PASS at α=0.025

4-qul subset {Q 109, Q 112, Q 113, Q 114} (Mufaṣṣal-only):
  Mean intra-pair FR distance: 0.3327
  Random-4 null mean: 0.9244
  perm p = 0.00020   PASS at α=0.025
```

The Mufaṣṣal-only 4-qul subset is **substantially tighter** than the full 5-qul cluster (0.3327 vs 0.4983), consistent with [[h-new-265-qul-openers-microcluster|H-NEW-265]] finding that Q 72 acts as the lexical "spoiler" of the 5-cluster once openers are stripped. **The Mufaṣṣal-tail 4-qul subset is the empirically-tightest qul-cluster.**

This replicates [[h-new-74-qul-distribution|H-NEW-74]]'s structural identification of the 5-qul-opener inventory under a different operationalization (FR-cohesion vs structural-extractor inventory). H-NEW-74 says "these are exactly the v1-w1 qul-openers"; this overview's inline test says "they are also FR-cohesive at p=0.0026 raw, p=0.00020 for the 4-qul Mufaṣṣal subset". Two orthogonal empirical axes converge on the same cluster.

See [[Q109-F-04-qul-cluster-cohesion|Q109-F-04]] for the formal pre-registered version of this test.

## 12. Asbāb al-nuzūl (classical occasion-of-revelation)

Standard chain (al-Ṭabarī *Jāmiʿ al-Bayān*, al-Wāḥidī *Asbāb al-nuzūl*, Ibn Kathīr): the polytheists of Quraysh proposed to the Prophet:

> *"naʿbudu ilāhaka sanatan wa-anta taʿbudu ālihatanā sanatan"*
> "We will worship your god for a year, and you worship our gods for a year."

The surah was revealed to refuse this proposal — making it a **doctrinal demarcation revelation** (an absolute *barāʾa*, "disavowal", parallel to the opening of Q 9 al-Tawba which is named *Sūrat al-Barāʾa*). This is the classical chain underwriting the alternative names *Sūrat al-Munābadha* / *Sūrat al-Barāʾa* (§2 above).

The chain quality is **mursal/marfūʿ** at best (cited by al-Wāḥidī, with multiple supporting reports in al-Ṭabarī); not *ṣaḥīḥ*-class but consistent across at least 3 collections — the classical asbāb is on solid traditional ground without being unimpeachable hadith-science-wise.

## 13. Hadith-corpus headline (the paired-prayer tradition)

Q 109 + Q 112 are the canonical pair for several voluntary-prayer recitations attested in:

| Tradition | Source | Chain | Audit verdict |
|:--|:--|:--|:--|
| Pre-Fajr 2-rakaʿah sunna | Tirmidhī #418 (Ibn ʿUmar); Ibn Mājah #883 (Ibn ʿUmar) | ḥasan ṣaḥīḥ at Tirmidhī | VERIFIED on disk |
| Post-Maghrib 2-rakaʿah | Ibn Mājah #900 (Ibn Masʿūd) | ḥasan | VERIFIED on disk |
| Two-rakaʿah after ṭawāf | Tirmidhī #870 (Jābir) | ḥasan ṣaḥīḥ | VERIFIED on disk |
| Witr triad (Q 87 + Q 109 + Q 112) | Tirmidhī #462-463; Nasāʾī #1704-1759 (multiple chains, esp. Ubayy b. Kaʿb); Ibn Mājah #905-907; Abū Dāwūd #1424 | ṣaḥīḥ-level on at least Ubayy chain | VERIFIED on disk (Q 109 + Q 112 + Q 87) |
| 1/4 of Quran (Q 109 = "rubʿ al-Qurʾān") | **Tirmidhī #2976 (Anas) + #2977 (Ibn ʿAbbās) + #2978 (Anas, alt chain)** | **ḥasan-disputed (see §14)** | **VERIFIED on disk; chain quality flagged below** |

**Critical correction to a common framing**: the prompt characterized the pair as "pre-fajr & post-maghrib voluntary prayers" specifically. Verified on the on-disk corpus this is an accurate but partial description. The fuller picture is:
- The 2-rakaʿah-paired contexts are **multiple** (pre-Fajr, post-Maghrib, post-ṭawāf)
- The **Witr triad** (Q 87 *al-Aʿlā* + Q 109 + Q 112) is the **most-narrated** Q 109 recitation context in the on-disk 9-book corpus (≥30 chains across Nasāʾī alone)
- **Bukhārī and Muslim do NOT contain the paired-recitation tradition** in the on-disk JSON corpus — the paired tradition is concentrated in **Tirmidhī, Nasāʾī, Ibn Mājah, and Abū Dāwūd**

See [[Q109-al-kafirun/04-hadith-corpus|04-hadith-corpus]] for the complete enumeration with hadith numbers and chain audit.

## 14. The "1/4 of the Quran" classical claim — adversarial-audit anchor

Q 109 carries a *thuluth*-parallel valuation in the *fadāʾil* tradition: **"reciting Q 109 equals 1/4 of the Quran"** (*rubʿ al-Qurʾān*). This is the formal parallel-of-parallels with the Q 112 *thuluth al-Qurʾān* claim ([[h-new-84-ikhlas-third|H-NEW-84]] REFUTED-STRONG, 0/7 axes pass).

**The Q 109 "1/4" hadith chain** (Tirmidhī #2976):
> *"man qaraʾa idhā zulzilat ʿudilat lahu bi-niṣf al-Qurʾān, wa-man qaraʾa qul yā ayyuhā al-kāfirūn ʿudilat lahu bi-rubʿ al-Qurʾān, wa-man qaraʾa qul huwa Allāh aḥad ʿudilat lahu bi-thuluth al-Qurʾān."*
> "Whoever recites *Idhā zulzilat* (Q 99), it equals half of the Quran for him; whoever recites *Qul yā ayyuhā al-kāfirūn* (Q 109), it equals a fourth of the Quran for him; and whoever recites *Qul huwa Allāh aḥad* (Q 112), it equals a third of the Quran for him."

The chain runs Anas b. Mālik → Thābit al-Bunānī → al-Ḥasan b. Salam → Muḥammad b. Mūsā al-Ḥarashī → al-Tirmidhī. **Al-Tirmidhī's own grading**: he reports the principal chain as *gharīb* (rare/single-strand at one tier) and notes that *al-Ḥasan b. Salam* is contested by some traditionists.

The parallel chain at Tirmidhī #2977 runs Ibn ʿAbbās → ʿAṭāʾ → Yamān b. al-Mughīra → Yazīd b. Hārūn → ʿAlī b. Ḥujr → al-Tirmidhī. Yamān b. al-Mughīra is graded *ḍaʿīf* by Yaḥyā b. Maʿīn and Ibn Ḥajar (*Tahdhīb al-Tahdhīb*); al-Tirmidhī himself does NOT grade #2977 *ḥasan ṣaḥīḥ*.

**Verdict on chain-quality (this audit, [[Q109-al-kafirun/05-classical-claims-audit|05-classical-claims-audit]] Claim 4)**:

| Hadith | Best chain grade | Cross-collection | Audit verdict |
|:--|:--|:--|:--|
| Tirmidhī #2976 (Anas chain) | gharīb (Tirmidhī's own grade) | NOT in Bukhārī/Muslim/Aḥmad on-disk | Single-strand Tirmidhī; not at *ṣaḥīḥ*-level |
| Tirmidhī #2977 (Ibn ʿAbbās chain) | weak (Yamān b. al-Mughīra ḍaʿīf) | NOT in Bukhārī/Muslim | Below ḥasan |
| Tirmidhī #2978 (Anas alt chain) | weak (Salama b. Wardān ḍaʿīf — al-Bukhārī al-Tārīkh al-Kabīr) | NOT in Bukhārī/Muslim | Below ḥasan |
| **Q 112 *thuluth* parallel** (Bukhārī #5013-5015) | **ṣaḥīḥ (mutawātir-class)** | **all 4 highest collections** | Highest-grade |
| **Q 99 *niṣf* parallel** (within #2976) | gharīb (paired with Q 109) | NOT independently in B/M | Same chain-strength as Q 109 |

**Critical asymmetry**: The Q 112 *thuluth* claim has **mutawātir-class transmission** (≥4 independent chains in Bukhārī + Muslim + Tirmidhī + Aḥmad). The **Q 109 *rubʿ* claim has only Tirmidhī-internal transmission with chain-grade contests**. This asymmetry in chain-quality is the principal classical reason that the "1/3" claim achieved doctrinal anchoring while the "1/4" claim is treated more loosely in classical *fadāʾil*.

**Empirical adversarial audit** (parallel to H-NEW-84 for Q 112 1/3):

If the hadith were taken as a literal content-equivalence claim, Q 109 should equal 1/4 = 0.25 of the Quran on some content axis. Pre-locked tolerance band [0.225, 0.275] (±10%):

| Axis | Operationalization | Q 109 / Quran ratio | Off by factor | PASS [0.225, 0.275]? |
|------|---------------------|---------------------|---------------|--------------------|
| 1 | Letter graphemes | 99 / 330,709 = **0.00030** | 833× too small | NO |
| 2 | Word tokens | 27 / 77,797 = **0.00035** | 718× too small | NO |
| 3 | Verse count | 6 / 6,236 = **0.00096** | 260× too small | NO |
| 4 | Distinct roots | 4 / 1,642 = **0.00244** | 102× too small | NO |
| 5 | Theology-dominant verses (al-Ghazālī schema) — NOT applicable: Q 109 is a *barāʾa*-disavowal, NOT a theological-doctrinal exposition. Cell N/A. | — | — | N/A |
| 6 | *qul*-token inventory | 1 / 332 = **0.00301** | 83× too small | NO |
| 7 | *kfr*-root inventory | 6 / 525 = **0.01143** | 22× too small | NO |

**Verdict**: REFUTED-STRONG (0/6 PASS-applicable axes; 1 axis N/A). Q 109 fails the literal "1/4 of Quran" reading by **22× to 833×** on every direct-content operationalization. **The literal-quantitative reading is empirically untenable**, parallel to H-NEW-84 for Q 112.

**Honest framing**: The Q 109 *rubʿ* hadith, like the Q 112 *thuluth* hadith, is **best read as a spiritual/devotional valuation statement** about recitation reward, not a content-equivalence claim. **The asymmetric difference** is that the Q 112 hadith has *ṣaḥīḥ*-grade transmission while the Q 109 hadith does not — so the spiritual valuation rests on **strong** chain-grounds for Q 112 and on **weak** chain-grounds for Q 109. Classical scholars (e.g., al-Albānī, *Silsilat al-Aḥādīth al-Ḍaʿīfa*) have flagged the Q 109 *rubʿ* chain as questionable; Ibn Ḥajar in *al-Iṣāba* notes the chain weakness without retracting the surah's *fadāʾil* status (which rests on the multi-chain pair-recitation traditions independently).

## 15. Cross-finding connections

This surah connects to the project's confirmed findings as follows:

- **[[h-new-1320|H-NEW-1320]]** (refrain-saturation): Q 109 is **rank-2 by saturation** (33%). The saturation outlier-flag was queued from H-NEW-1320 §"Saturation outlier"; this specialist landing addresses it formally.
- **[[h-new-74-qul-distribution|H-NEW-74]]** Cell 3 (5-qul-openers): Q 109 ∈ {Q 72, Q 109, Q 112, Q 113, Q 114}. Confirmed v1-w1 *qul* opener.
- **[[h-new-265-qul-openers-microcluster|H-NEW-265]]** (opener-stripped 5-qul micro-cluster): NULL on the strict micro-cluster test. The 4-qul Mufaṣṣal subset is tighter (this overview's §11 inline-test).
- **[[cross-finding-028|cross-finding-028]]** (liturgical-pair FR cohesion): Q 109/Q 112 is the "exception pair" in the length-control secondary, but PASSES the unconditional primary. Saturation-tail effect.
- **[[h-new-1240|H-NEW-1240]]** (13 empirically-seamless mushaf-transitions): **Q 109→Q 110 is rank-1 (most-cheap) seamless transition** in the corpus. Q 109 sits at one of the 13 corpus-EXACT zero-cost seams.
- **[[h-new-84-ikhlas-third|H-NEW-84]]** (Q 112 1/3 REFUTED): structural parallel; Q 109 1/4 hadith is now adversarially audited and lands REFUTED-STRONG (this file §14, formal at [[Q109-F-03-rubu-quran-audit|Q109-F-03]]).
- **[[cross-finding-026|cross-finding-026]]** (iʿjāz-architecture 4-cell typology): Q 109 sits in the *iʿjāz al-fawāṣil* cell (rank 5 in sig_B, rank 17 in sig_A).
- **[[cross-finding-013|cross-finding-013]]** (mushaf as topological ring + wrap-around): Q 109 is part of the TERMINAL_TRIAD-adjacent zone (Q 108-114). The wrap-around finding showed Q 1 ↔ Q 114 is rank-1 nearest-neighbor under verse-length; Q 109 sits inside the wrap-around closure.

## 16. Pre-registered tests in this folder

Four tests are pre-registered in `preregs/` (all SHA-locked before run, seed = 20260509, n_perm = 10000, Bonferroni-corrected):

1. **[[Q109-F-01-saturation-rank-replication|Q109-F-01]]** — Saturation-axis rank-2 replication on a different operationalization (longest-repeated 5-token window per surah). Replicates [[h-new-1320|H-NEW-1320]] saturation finding under a different statistic. (Filed as [[h-new-1322|H-NEW-1322]].)
2. **[[Q109-F-02-five-qul-cluster-cohesion|Q109-F-02]]** — 5-*qul*-opener cluster FR-cohesion replication with ledger-locked Bonferroni-2 (5-cluster + 4-cluster Mufaṣṣal-subset). Replicates [[h-new-74-qul-distribution|H-NEW-74]] structural inventory under FR-cohesion operationalization. (Filed as [[h-new-1410|H-NEW-1410]].)
3. **[[Q109-F-03-rubu-quran-audit|Q109-F-03]]** — Adversarial empirical audit of the Q 109 = "1/4 of Quran" classical claim, parallel to [[h-new-84-ikhlas-third|H-NEW-84]] for Q 112's "1/3". 6 axes locked, ±10% tolerance band. (Filed as [[h-new-1420|H-NEW-1420]].)
4. **[[Q109-F-04-pair-recitation-fr|Q109-F-04]]** — Verifies that Q 109 ↔ Q 112 FR-cohesion is structurally non-trivial under length-controlled null (length-matched short-Mufaṣṣal pairs). Cross-finding-028 secondary replication. (Filed as [[h-new-1430|H-NEW-1430]].)

## 17. Honest limits

- **Saturation-rank inversion warning**: Q 109's rank-2 by saturation is on a different axis from Q 109's rank-15 by absolute-count in H-NEW-1320. The two ranks are not reconcilable by re-weighting; they are answers to different questions. Q 109 is "the corpus's most-saturated short-surah" but NOT "a high-count refrain-architectured surah" in any absolute sense.
- **Hadith chain-quality**: the on-disk JSON corpus does not contain Bukhārī or Muslim entries for the Q 109+Q 112 paired-recitation tradition or the Q 109 *rubʿ* tradition. The paired-recitation is concentrated in Tirmidhī (#418, #462-463, #870), Nasāʾī (#947, #994, #1704-1759, #2969), Ibn Mājah (#883, #900, #905-907), and Abū Dāwūd (#1424). The *rubʿ* tradition is concentrated in Tirmidhī (#2976-2978). I have NOT cross-checked against Bayhaqī, al-Ṭabarānī, or other tier-3 collections.
- **Asbāb al-nuzūl chain quality**: the Quraysh-pact asbāb is *mursal/marfūʿ* at best across al-Ṭabarī + al-Wāḥidī + Ibn Kathīr; not *ṣaḥīḥ*-grade.
- **Rules-tuple sensitivity**: all tests in `preregs/` use no-tashkeel orthographic word-tokens and Hafs-Kūfan verse numbering. Min-tashkeel or full-tashkeel might shift the saturation count for surahs with vocalic-distinct-but-orthographically-identical refrains (not relevant to Q 109's exact-byte refrain).
- **Verdict ceiling**: this is a specialist landing replicating known findings under specialist-judgment + new operationalizations. Promotion of Q109-F-01..04 to CONFIRMED requires independent replication on a distinct data dimension; verdicts here cap at PASS-DIRECTED.

---

## Files in this directory

```
Q109-al-kafirun/
├── 00-overview.md                                    # this file
├── 01-empirical-profile.md                            # full architectural metric pull
├── 02-content-analysis.md                             # verse-by-verse + saturation analysis
├── 03-tafsir-survey.md                                # al-Ṭabarī, Ibn Kathīr, al-Suyūṭī, al-Rāzī
├── 04-hadith-corpus.md                                # full Q 109 hadith enumeration with chain audit
├── 05-classical-claims-audit.md                       # 5 classical claims, MW-6 verified
├── 06-novel-findings.md                               # 4 pre-registered novel-finding test results
├── 07-cross-references.md                             # connections to other findings + surahs
├── JOURNAL.md                                         # methodological-decision log
├── preregs/
│   ├── Q109-F-01-saturation-rank-replication-prereg.md
│   ├── Q109-F-02-five-qul-cluster-cohesion-prereg.md
│   ├── Q109-F-03-rubu-quran-audit-prereg.md
│   └── Q109-F-04-pair-recitation-fr-prereg.md
├── csv/
│   └── Q109-F-01..04.json (pending run)
└── scripts/
    └── Q109_F_01..04_*.py (pending run)
```

*Bismillāhi al-Raḥmāni al-Raḥīm.*
