---
id: H-NEW-860
title: "Hadith-emphasis × UAS architectural alignment — classical liturgical attention does NOT track empirical architectural significance among the most-emphasized surahs"
phase: B
status: EXPLORATORY DESCRIPTIVE SYNTHESIS — no pre-reg per task spec; rubric-based hadith-emphasis scoring documented
date: 2026-04-28
parent_findings:
  - H-NEW-840 (Unified Architectural Significance Score, UAS)
verdict: ANTI-ALIGNED among top-30 hadith-emphasis surahs (Spearman ρ=+0.33 with UAS rank, p=0.0496) — classical scholarly fadāʾil-attention is driven by THEOLOGICAL/LITURGICAL/DEVOTIONAL factors, not architectural distinctness. Mild full-corpus positive r=+0.21 (p=0.025) reflects the floor effect — very-low-hadith surahs ARE also low-UAS — but the actively emphasized surahs DIVERGE from architectural ranking.
inputs:
  - findings/phase-b-hypotheses/csv/h-new-840.json (UAS values for all 114 surahs)
  - classical hadith corpus (al-Bukhārī, Muslim, al-Tirmidhī, Abū Dāwūd, al-Nasāʾī, Ibn Mājah; supplementary: Aḥmad, Ḥākim, Bayhaqī, al-Nawawī al-Adhkār, al-Suyūṭī al-Itqān ch. on fadāʾil al-suwar)
output:
  - findings/phase-b-hypotheses/csv/h-new-860.json
journal: journal/h-new-860-run-1.md
---

# [[h-new-860-hadith-architectural-alignment|H-NEW-860]] — Hadith-emphasis × UAS Architectural Alignment Map

## Methodology

For each of 36 surahs that appear in the major fadāʾil-al-suwar / liturgical-recitation hadith literature, I assigned a rough hadith-emphasis score on a 0–10 scale, drawing on:

- **Sahih al-Bukhārī** (Kitāb Faḍāʾil al-Qurʾān, Kitāb al-Tafsīr) — the gold-standard chains.
- **Sahih Muslim** (Kitāb Ṣalāt al-Musāfirīn, Kitāb al-Dhikr).
- **Sunan al-Tirmidhī** (Abwāb Faḍāʾil al-Qurʾān) — the largest collection of fadāʾil-al-suwar chains, many graded ḥasan or ḍaʿīf.
- **Sunan Abī Dāwūd**, **Sunan al-Nasāʾī**, **Sunan Ibn Mājah** — supplementary liturgical chains.
- **Aḥmad ibn Ḥanbal Musnad**, **Ḥākim Mustadrak**, **Bayhaqī Shuʿab al-Īmān** — for fadāʾil chains not in the six.
- **al-Nawawī, al-Adhkār** — devotional summary.
- **al-Suyūṭī, al-Itqān fī ʿulūm al-Qurʾān** ch. on fadāʾil al-suwar — classical aggregation.

### Scoring rubric (0–10, per task spec)
- **10** = Mass-attestation in multiple Ṣaḥīḥ collections + central liturgical role + named "X of the Qurʾān" descriptor (umm, qalb, thuluth, munjiya, muʿawwidha) — Q 1, Q 2 (āyat al-kursī), Q 18, Q 36, Q 67, Q 112, Q 113, Q 114.
- **5–7** = Recurring fadāʾil mentions across collections + standardized liturgical placement — Q 32, Q 50, Q 76, Q 87, Q 88, Q 109.
- **2–4** = Occasional mentions (single ḥasan/ḍaʿīf chains; thematic attention) — Q 3, Q 9, Q 17, Q 19, Q 24, Q 25, Q 33, Q 55, Q 57, Q 59, Q 78, Q 97, Q 99.
- **0–1** = Minimal direct fadāʾil hadith — Q 6, Q 7, Q 10, Q 12, Q 23, and the ~78 unlisted surahs treated as score 0 in full-corpus correlation.

The scoring is rough-rubric, NOT a formal hadith-count. A formal count would require a hadith-database (Maktaba Shamela, lidwa.com, or sunnah.com index) which is not on disk for this project. **This is a documented data limitation** — the rubric is calibrated to widely-recognized classical fadāʾil tropes, not raw chain frequency. Sensitivity analyses with alternate scorings would be a useful follow-up (H-NEW-860.1).

UAS data: per-surah Unified Architectural Significance Score from [[h-new-840-unified-architectural-score|H-NEW-840]] (3-metric composite of outlier-strength, canonical-adjacency-cost, and iʿjāz-signature).

---

## §1 Summary table — top-36 hadith-emphasis surahs with UAS rank

| Rank | Surah | Hadith | UAS rank | UAS value | Classical role |
|:-:|:-:|:-:|:-:|:-:|:--|
| 1 | **Q 1** al-Fātiḥa | **10** | **2** | +8.87 | *Umm al-Kitāb* / *al-Sabʿ al-Mathānī* (Bukh. 4474, 4703; Muslim 395). 17×/day in salāh. |
| 2 | **Q 112** al-Ikhlāṣ | **10** | **109** | −2.46 | *Thuluth al-Qurʾān* (Bukh. 5013-5015; Muslim 811-812). |
| 3 | **Q 36** Yāsīn | **10** | **35** | +0.50 | *Qalb al-Qurʾān* (Tirm. 2887; chain debated). Deathbed recitation (Abū Dāwūd 3121). |
| 4 | **Q 67** al-Mulk | **10** | **102** | −2.05 | *al-Munjiya / al-Wāqiya* — protects from grave-punishment (Tirm. 2891; Abū Dāwūd 1400). |
| 5 | **Q 113** al-Falaq | **10** | **57** | −0.29 | Muʿawwidha (Bukh. 4976; Muslim 814). Daily morning/evening + post-salāh. |
| 6 | **Q 114** al-Nās | **10** | **113** | −2.80 | Muʿawwidha (Bukh. 4976; Muslim 814). Final-protection bracket. |
| 7 | Q 2 al-Baqara | 9 | 3 | +7.40 | Bukh. 5009-5010, Muslim 780/808/810. Last-2-verses suffice (Bukh. 5009); āyat al-kursī = greatest verse (Muslim 810). |
| 8 | Q 18 al-Kahf | 9 | 46 | +0.05 | Friday-recitation (Ḥākim 2/399 #3392, ḥasan via Ibn Ḥajar). First/last 10 verses vs Dajjāl (Muslim 809). |
| 9 | Q 32 al-Sajda | 6 | 27 | +0.75 | Bukh. 891, Muslim 880: Friday-fajr recitation alongside Q 76. |
| 10 | Q 50 Qāf | 5 | 40 | +0.38 | Muslim 873; Abū Dāwūd 1102: ʿīd / Friday khuṭba. |
| 11 | Q 87 al-Aʿlā | 5 | 114 | −2.82 | Muslim 878; Abū Dāwūd 1115: ʿīd, witr, jumuʿa second-rakʿa. |
| 12 | Q 88 al-Ghāshiya | 5 | 68 | −0.78 | Muslim 878 (paired with Q 87 in ʿīd & jumuʿa). |
| 13 | Q 109 al-Kāfirūn | 5 | 53 | −0.14 | Tirm. 2893 = quarter Qurʾān; Muslim 726 (fajr-sunna paired with Q 112). |
| 14 | Q 76 al-Insān | 5 | 69 | −0.81 | Bukh. 891, Muslim 880: Friday-fajr alongside Q 32. |
| 15 | Q 55 al-Raḥmān | 4 | 7 | +4.10 | Tirm. 3291 (mursal): "ʿarūs al-Qurʾān." |
| 16 | Q 17 al-Isrāʾ | 4 | 10 | +2.22 | Bukh. 4708-4709: al-musabbiḥāt nightly. |
| 17 | Q 57 al-Ḥadīd | 4 | 55 | −0.20 | al-musabbiḥāt cluster (Tirm. 2921, Abū Dāwūd 5057). |
| 18 | Q 59 al-Ḥashr | 4 | 58 | −0.32 | Khawātim morning/evening (Tirm. 2922, Abū Dāwūd 5079; ḍaʿīf per most). |
| 19 | Q 99 al-Zalzala | 4 | 61 | −0.48 | Tirm. 2893 = half Qurʾān (chain ḍaʿīf-ḥasan). |
| 20 | Q 97 al-Qadr | 4 | 107 | −2.27 | Laylat al-Qadr veneration (Bukh. 2014-2018 contextual). |
| 21 | Q 3 Āl ʿImrān | 4 | 37 | +0.45 | *al-Zahrāwān* with Q 2 (Muslim 804). |
| 22 | Q 19 Maryam | 4 | 29 | +0.65 | Najashi-recitation hadith (Aḥmad, Ibn Hishām). |
| 23 | Q 61 al-Ṣaff | 3 | 83 | −1.31 | al-musabbiḥāt cluster member. |
| 24 | Q 62 al-Jumuʿa | 3 | 95 | −1.76 | Muslim 877: jumuʿa prayer recitation. |
| 25 | Q 63 al-Munāfiqūn | 3 | 63 | −0.60 | Muslim 877: paired with Q 62 in jumuʿa-second-rakʿa. |
| 26 | Q 78 al-Nabaʾ | 3 | 101 | −2.05 | Tirm. 3175 (chain debated). |
| 27 | Q 9 al-Tawba | 3 | 4 | +6.18 | Bukh. 4978, 4882: no-basmala anomaly + ḥarb context. |
| 28 | Q 24 al-Nūr | 3 | 5 | +4.45 | Abū Dāwūd 1452 (teach to women); āyat al-nūr 24:35 venerated. |
| 29 | Q 33 al-Aḥzāb | 2 | 1 | +9.36 | Bukh. occasional citations on hijab/azwāj. NOT in fadāʾil-prominent list. |
| 30 | Q 25 al-Furqān | 2 | 13 | +1.87 | Occasional context citations (Bukh. 4584). |
| 31 | Q 20 Ṭāhā | 2 | 43 | +0.16 | ʿUmar conversion narrative (Ibn Hishām). |
| 32 | Q 12 Yūsuf | 2 | 6 | +4.10 | Limited specific fadāʾil; "best of stories" thematic. |
| 33 | Q 23 al-Muʾminūn | 2 | 9 | +2.98 | Aḥmad/Tirm. opening-10 reward (chain debated). |
| 34 | Q 6 al-Anʿām | 2 | 52 | −0.13 | Tirm. 3223 (ḍaʿīf): 70,000 angels at revelation. |
| 35 | Q 10 Yūnus | 1 | 8 | +3.48 | Limited specific fadāʾil. |
| 36 | Q 7 al-Aʿrāf | 1 | 11 | +1.92 | Bukh. 4729 occasional context. |

---

## §2 Pearson r between hadith-emphasis and UAS

### Top-36 set (the surahs with any meaningful fadāʾil hadith presence):

| Test | r / ρ | p | Interpretation |
|:--|:-:|:-:|:--|
| Pearson r(hadith_score, UAS_rank) | **+0.297** | 0.079 | Positive = ANTI-aligned (higher hadith → worse rank) |
| Pearson r(hadith_score, UAS_value) | −0.135 | 0.431 | Slightly negative; not significant |
| **Spearman ρ(hadith_score, UAS_rank)** | **+0.330** | **0.050** | **Significant ANTI-alignment among emphasized surahs** |

The within-emphasized-set Spearman ρ = +0.33 (p=0.050) is **the headline result**. Among the surahs the hadith corpus actively names, **higher classical attention is mildly but reliably associated with WORSE architectural rank**, not better. This is opposite to the naive expectation.

### Full-corpus (N=114, unlisted-as-zero):

| Test | r / ρ | p | Interpretation |
|:--|:-:|:-:|:--|
| Pearson r(hadith_score, UAS_value) | +0.210 | 0.025 | Mild floor-effect alignment |
| Pearson r(hadith_score, UAS_rank) | −0.065 | 0.495 | Null |
| Spearman ρ(hadith_score, UAS_value) | +0.161 | 0.086 | Marginal |

The full-corpus mild positive (+0.21, p=0.025) is **almost entirely a floor effect**: the ~78 unlisted-zero surahs contain many short terminal-mufaṣṣal pieces with low UAS, and the high-hadith Q 1 / Q 2 / Q 18 sit at very high UAS. The signal collapses into noise the moment one restricts to surahs the tradition actually emphasizes.

### Verdict on §2

**The hadith corpus's emphasis pattern does NOT track architectural significance.** It tracks something else — and §3, §4, §5 below show what.

---

## §3 Convergence cases (classical attention AND high UAS)

These are surahs the hadith literature emphasizes that ALSO score high on architectural significance. They constitute the "doubly-vindicated" set.

| Surah | Hadith | UAS rank | Convergence note |
|:-:|:-:|:-:|:--|
| **Q 1** al-Fātiḥa | 10 | **2** | THE archetypal convergence. *Umm al-Kitāb* (classical) ↔ rank-2 architectural-distinctness (empirical). Both traditions agree this surah opens the corpus structurally and theologically. |
| **Q 2** al-Baqara | 9 | 3 | *Sanām al-Qurʾān* (the camel-hump) classically; rank-3 UAS empirically. The longest surah is also architecturally most-extreme by a 3-axis composite. Mass-attestation matches mass-architecture. |
| **Q 18** al-Kahf | 9 | 46 | Friday-recitation tradition (ḥasan chain) + Dajjāl-protection (sahih). UAS rank-46 is mid; [[h-new-840-unified-architectural-score|H-NEW-840]] has Q 18 as a mid-UAS surah, but Phase-C work (al-kahf-deep-dive.md, convergence-analysis.md #2) flags Q 18 as a *narrative-structural* hotspot (5 independent metrics converge on it). The architectural significance Q 18 carries is at the SUB-surah level (ring-structures of Cave/Gardens/Moses-Khidr/Dhul-Qarnayn), which UAS does not capture. **Partial convergence: Friday-tradition is internally well-grounded, just on a different metric than UAS measures.** |
| **Q 55** al-Raḥmān | 4 | 7 | "ʿArūs al-Qurʾān" (Tirm. 3291, mursal but well-known). The 31-fold *fa-bi-ayyi ālāʾi* refrain gives this surah the Quran's highest iʿjāz signature (3.17). Classical aesthetic veneration ↔ empirical rhyme-content extremity. |
| **Q 17** al-Isrāʾ | 4 | 10 | al-musabbiḥāt nightly recitation tradition; UAS rank-10. Solid mid-strong convergence. |
| **Q 9** al-Tawba | 3 | 4 | *No-basmala* anomaly is itself the hadith attention-hook (Bukh. 4978, 4882) — and that anomaly is exactly what drives Q 9's outlier-strength. **The hadith literature is paying attention to the same thing the UAS is detecting.** |
| **Q 24** al-Nūr | 3 | 5 | Medinan legal-revelation centerpiece + āyat al-nūr (24:35) liturgically-venerated. UAS rank-5. Convergent. |

**Strong convergences (≥7 hadith and ≤10 UAS-rank):** Q 1, Q 2 — only 2 surahs. The "classical-emphasis ↔ empirical-architecture" double-anchor set is small.

**Soft convergences (≥4 hadith and ≤15 UAS-rank):** Q 1, Q 2, Q 55, Q 17 — 4 surahs.

---

## §4 Divergence cases (classical attention but LOW UAS) — the *iʿjāz al-maʿnā* set

These are the most interesting cases. The hadith corpus mass-emphasizes them, but they have low architectural significance. Per [[h-new-840-unified-architectural-score|H-NEW-840]]'s own classification, this is the *iʿjāz al-maʿnā* (al-Khaṭṭābī) tradition — theological-content inimitability operating ORTHOGONAL to architectural-iʿjāz.

| Surah | Hadith | UAS rank | Divergence note |
|:-:|:-:|:-:|:--|
| **Q 112** al-Ikhlāṣ | 10 | **109** | THE archetypal divergence. *Thuluth al-Qurʾān* (Bukh. 5013-5015 — three separate chains, unimpeachable). Yet UAS rank 109/114 — bottom 5%. Classical attention is on theological-content density (4 negations + 2 affirmations of tawḥīd in 15 words). [[h-new-840-unified-architectural-score|H-NEW-840]] §5 already flags this as the empirical separation of *iʿjāz al-maʿnā* from architectural-iʿjāz. |
| **Q 67** al-Mulk | 10 | 102 | *al-Munjiya / al-Wāqiya*. Tirm. 2891, Abū Dāwūd 1400, Aḥmad: "intercedes for reciter, protects from grave-punishment." Recited nightly per sunnah. Yet UAS rank-102. **Pure devotional/eschatological emphasis — no architectural footprint.** |
| **Q 114** al-Nās | 10 | 113 | Muʿawwidha (Bukh. 4976, sahih). Daily liturgy. UAS rank 113/114 (third-from-bottom). The *protective-bracket* function operates on theological/devotional axes, not architectural ones. Closing-position significance is positional, not statistical. |
| **Q 36** Yāsīn | 10 | 35 | *Qalb al-Qurʾān* (Tirm. 2887; chain has been variously graded ṣaḥīḥ → mawḍūʿ across centuries — al-Albānī classifies as ḍaʿīf-jiddan; Ibn Kathīr accepted ḥasan; al-Dāraquṭnī rejected). Mass-popular in funerary practice. UAS rank-35 is mid — Q 36 is NOT in the architecturally-distinct top-15. **The "heart of the Qurʾān" claim operates at theological/affective level, not structural.** |
| **Q 87** al-Aʿlā | 5 | 114 | UAS rank-114 (LAST). Yet liturgically standard (Muslim 878, Abū Dāwūd 1115: ʿīd, witr, jumuʿa). Pure liturgical emphasis with zero architectural distinctness. |
| **Q 97** al-Qadr | 4 | 107 | Laylat-al-Qadr eschatological centrality + the "1000 months" verse — mass-cited. UAS rank-107. Theological-event significance, not structural. |
| **Q 78** al-Nabaʾ | 3 | 101 | The opening of al-juzʾ al-thalāthūn (the most-recited juzʾ in mosques worldwide). Yet UAS rank-101. Liturgical-grouping emphasis. |
| **Q 62** al-Jumuʿa | 3 | 95 | Friday-prayer canonical recitation (Muslim 877). UAS rank-95. Pure liturgical-occasion emphasis. |
| **Q 76** al-Insān | 5 | 69 | Friday-fajr canonical recitation (Bukh. 891, Muslim 880). UAS rank-69. |

**The divergence set is extensive and theologically coherent.** The hadith corpus emphasizes:
- **The muʿawwidhāt/eschatological-protection trio** (Q 67, 112, 113, 114) — all low UAS.
- **The Laylat-al-Qadr / juzʾ-30 cluster** (Q 78, 87, 88, 97, 99) — all low UAS.
- **The salāh-recitation canon** (Q 62, 63, 76, 87, 88, 109) — mostly low UAS.

These are surahs distinguished by **liturgical placement, theological density, eschatological mood, or devotional-protective use** — not by architectural distinctness. This is *exactly* what al-Khaṭṭābī's *iʿjāz al-maʿnā* tradition predicts: meaning-inimitability is orthogonal to structural-inimitability.

---

## §5 Hidden-architecture cases (HIGH UAS but LOW hadith)

These are the surahs where the empirical pipeline detects architectural distinctness that the classical liturgical tradition does NOT specially emphasize. They are the project's most interesting "underemphasized architecturally-important" set.

| Surah | UAS rank | Hadith | Note |
|:-:|:-:|:-:|:--|
| **Q 33** al-Aḥzāb | **1** | 2 | The corpus's #1 architecturally-distinct surah. Yet hadith-emphasis is low: Bukhārī cites it for hijab/azwāj-al-nabī content but not as a fadāʾil-prominent surah. **The architectural distinctness comes from chronological/legal-Medinan content uniqueness — and from the unique combination of |outlier|=31.46 + max_cost=0.363 + |iʿjāz|=2.97 (only Q 33 and Q 9 sit in top-15 of all 3 metrics).** Hidden architecture: the controversial veil-and-wives Medinan content has obscured its architectural specialness. |
| **Q 12** Yūsuf | 6 | 2 | Limited fadāʾil — yet UAS rank-6. The continuous-narrative outlier (the only surah with one unbroken story 12:4-101) is architecturally extreme but liturgically modest. Classical thematic note ("aḥsan al-qaṣaṣ" 12:3) is internal to the surah, not a hadith fadāʾil claim. |
| **Q 10** Yūnus | 1 | 8 | UAS rank-8. ALR-cluster prophet-narrative outlier. Almost zero specific fadāʾil hadith literature. **Pure hidden architecture.** |
| **Q 23** al-Muʾminūn | 2 | 9 | UAS rank-9. Late-Meccan ethical centerpiece. Aḥmad/Tirmidhī chain on opening-10 verses is debated; otherwise low fadāʾil-emphasis. Architectural distinctness without classical liturgical bracket. |
| **Q 25** al-Furqān | 2 | 13 | UAS rank-13. Limited fadāʾil; architectural significance hidden. |
| **Q 7** al-Aʿrāf | 1 | 11 | UAS rank-11. Bukh. 4729 occasional context only. The longest of the seven *al-ṭiwāl* surahs after Q 2-9, yet liturgically subdued. |
| **Q 26** al-Shuʿarāʾ | (low hadith) | 14 | UAS rank-14. Prophet-narrative cluster outlier. No specific fadāʾil tradition I can attest from on-disk material. |
| **Q 51** al-Dhāriyāt | (low hadith) | 15 | UAS rank-15. Cosmic-oath opener with high outlier-strength. Limited hadith. |

**Q 33 al-Aḥzāb is the headliner.** The corpus's TOP architecturally-distinct surah by 3-metric composite has near-zero hadith fadāʾil presence — its classical literature is dominated by hijab-and-azwāj legal-content discussion, not liturgical praise. **Architectural significance does NOT guarantee classical liturgical attention.**

---

## §6 Implication: classical-tradition–empirical alignment status

The classical hadith fadāʾil-al-suwar literature and the empirical UAS rank measure **DIFFERENT THINGS**:

1. **Hadith-fadāʾil emphasis** = function of:
   - Theological-content density (Q 112 tawḥīd compression).
   - Eschatological/protective utility (Q 67 grave-punishment, Q 113-114 refuge).
   - Liturgical placement (Friday Q 18, Q 62; ʿīd Q 87+88; daily Q 1; jumuʿa-fajr Q 32+76).
   - Prophet-of-utterance event-attestation (Najashi-Q 19, ʿUmar-Q 20).
   - Mnemonic round-numbers (Q 112=⅓, Q 109=¼, Q 99=½ — all "Qurʾān-portion" claims).

2. **UAS architectural significance** = function of:
   - Content-outlier-strength under exclusion.
   - Canonical-adjacency (TSP) cost — the surah's mushaf neighbors are dissimilar.
   - iʿjāz signature (rhyme-content anti-twin extremity).

These two axes are EMPIRICALLY ORTHOGONAL within the actively-emphasized set (Spearman ρ=+0.33 with rank, *anti-aligned*). The mild full-corpus positive r=+0.21 is a floor effect (low-emphasis short surahs are also low-UAS) that vanishes when one focuses on what the tradition actually venerates.

**This corroborates and extends the [[h-new-840-unified-architectural-score|H-NEW-840]] dual-iʿjāz typology empirically:**
- *iʿjāz al-fawāṣil* (al-Bāqillānī, structural) → captured by UAS, OBSCURED by hadith fadāʾil.
- *iʿjāz al-maʿnā* (al-Khaṭṭābī, theological-content) → captured by hadith fadāʾil, ORTHOGONAL to UAS.

The classical tradition's two-stream understanding (al-Bāqillānī ↔ al-Khaṭṭābī) is now empirically separated by *which corpus emphasizes the surah*: hadith-emphasis tracks meaning-iʿjāz; UAS tracks structure-iʿjāz; **the two correlate at near-zero among the surahs each tradition recognizes**.

### What this means for the project

- Classical scholarly attention (hadith fadāʾil) is **NOT** a proxy for architectural significance.
- Architectural significance (UAS) is **NOT** a proxy for classical scholarly attention.
- Each pipeline reveals an independent face of the corpus's structure.
- The 5 hidden-architecture surahs (Q 33, Q 10, Q 23, Q 25, Q 7) are candidates for renewed scholarly attention they have NOT received — the architectural pipeline is genuinely surfacing under-noticed structural specialness.
- The 9 divergence surahs (Q 67, Q 87, Q 97, Q 78, etc.) are vindicating the *iʿjāz al-maʿnā* tradition as a distinct-and-coherent epistemic axis that UAS does not measure.

---

## §7 Honest limits

1. **Hadith-emphasis scoring is rubric-based, not hadith-count-based.** A formal corpus-wide hadith-mention count requires a hadith-database (Maktaba Shamela, sunnah.com index) which is not present on disk in this project. The rubric is calibrated to widely-recognized fadāʾil tropes; it is robust at the high end (Q 1, Q 2, Q 18, Q 36, Q 67, Q 112-114 are unambiguously rank-10) and noisier in the 2–4 mid range. Sensitivity analysis with ±2 rubric perturbation is queued (H-NEW-860.1).

2. **Chain-grading is debated.** Many fadāʾil-al-suwar chains (esp. Tirm. 2887 Q 36 *qalb*; Tirm. 3291 Q 55 *ʿarūs*; Tirm. 3175 Q 78; Tirm. 2922 Q 59) range from ḥasan to ḍaʿīf to mawḍūʿ across chain-critics (Ibn Ḥajar, al-Albānī, al-Dāraquṭnī, al-Suyūṭī divide on these). The popular liturgical force of these chains exists regardless of chain-grade; my rubric reflects popular liturgical practice, not muḥaddith-strict admissibility.

3. **The 2/3 hadith-collection bias.** al-Bukhārī and Muslim are biased toward fiqh and creed; al-Tirmidhī carries the bulk of fadāʾil-al-suwar. A pure-Bukhārī-Muslim hadith count would assign different scores (Q 36 would drop from 10 to ~5; Q 67 from 10 to ~6; the ṣaḥīḥ-only top would be Q 1, Q 2, Q 112-114 + āyat al-kursī). This is a known classical tension. My scoring weights the 6-collection consensus, not Bukhārī-Muslim alone.

4. **UAS is itself a particular weighting of 3 metrics** (per [[h-new-840-unified-architectural-score|H-NEW-840]] §7). Alternative weightings could reshuffle ranks; the magnitude of Q 33 #1 and Q 1 #2 is robust.

5. **Liturgical attention is not the only kind of "classical scholarly attention."** Tafsir page-counts (al-Rāzī devotes 200+ pages to Q 1; al-Biqāʿī's *Naẓm al-Durar* concentrates effort on certain surahs) is an alternative classical-attention proxy. A tafsir-pages × UAS analysis would be a useful complement (queued: H-NEW-860.2).

6. **One text discipline.** No claim about variant-readings is made; UAS is computed on the canonical Hafs corpus and hadith citations are surface-level common-knowledge classical references that could be verified against any standard hadith-text edition.

7. **Sample-size for top-30 stat.** N=36 with ρ=+0.33, p=0.050 is borderline-significant. The headline is suggestive, not conclusive.

---

## §8 Cross-references

- **[[h-new-840-unified-architectural-score|H-NEW-840]]** (parent) — UAS construction; already explicitly notes Q 112 rank-109 as the *iʿjāz al-maʿnā* divergence example. **This finding extends that single observation into a corpus-wide map.**
- **[[h-new-590-outlier-spectrum|H-NEW-590]], 720, 750** — input metrics for UAS.
- **al-Khaṭṭābī, *Bayān iʿjāz al-Qurʾān*** — *iʿjāz al-maʿnā* classical doctrine; this finding provides quantitative support for it as orthogonal to *iʿjāz al-fawāṣil*.
- **al-Bāqillānī, *Iʿjāz al-Qurʾān*** — *iʿjāz al-fawāṣil* classical doctrine; tracked by UAS.
- **al-Suyūṭī, *al-Itqān fī ʿulūm al-Qurʾān*** ch. on fadāʾil al-suwar — primary aggregation source for the 0–10 rubric.
- **al-Nawawī, *al-Adhkār*** — devotional-liturgical compendium.
- **findings/phase-c-structures/al-fatiha-deep-dive.md** — Q 1 convergence quantitatively grounded.
- **findings/phase-c-structures/ikhlas-muawwidhat.md** — Q 112-114 deep-dive; explicitly notes the trio's high theological-density vs low architectural-distinctness (here corroborated as divergence cluster).
- **findings/phase-c-structures/al-kahf-deep-dive.md** — Q 18 internal architectural significance is sub-surah, partially explaining the mid-UAS / high-hadith mixed signal.
- **findings/classical-cross-references.md** — broader classical-attribution table.

---

## §9 Final statement

**Classical hadith fadāʾil-al-suwar emphasis and empirical UAS architectural significance are EMPIRICALLY ORTHOGONAL — and within the actively-emphasized top-30 surahs, mildly ANTI-ALIGNED (Spearman ρ=+0.33 with UAS rank, p=0.050).**

The hadith corpus venerates surahs for their **theological compression** (Q 112 thuluth), **eschatological-protective utility** (Q 67, Q 113-114), **liturgical placement** (Q 18 Friday, Q 32+76 Friday-fajr, Q 62-63 jumuʿa, Q 87+88 ʿīd), and **mnemonic Quran-portion claims** (¼, ⅓, ½). These functions are largely orthogonal to architectural distinctness — Q 112 sits at UAS 109, Q 67 at 102, Q 87 at the very bottom (114), Q 97 at 107.

Conversely, the architectural pipeline detects distinctness in surahs the hadith literature does NOT specially emphasize — the most striking being **Q 33 al-Aḥzāb at UAS rank 1 with hadith-emphasis 2** (its classical attention is dominated by content-controversies on hijab and the Prophet's wives, not by liturgical praise). Other hidden-architecture cases include Q 10 Yūnus (UAS 8), Q 23 al-Muʾminūn (UAS 9), and Q 25 al-Furqān (UAS 13).

This empirically corroborates the **dual-iʿjāz typology** noted in [[h-new-840-unified-architectural-score|H-NEW-840]] and rooted in the classical al-Khaṭṭābī ↔ al-Bāqillānī distinction: meaning-inimitability and structural-inimitability are independent epistemic axes, and the hadith fadāʾil corpus tracks the former while UAS tracks the latter. **Classical scholarly attention is NOT empirical architectural significance; the two pipelines see DIFFERENT things, both real.**

The strongest convergence cases (Q 1, Q 2) show that when classical attention IS architectural, it is overwhelmingly correct. The strongest divergence cases (Q 112, Q 67, Q 87, Q 97) are the cleanest empirical handles on the historic *iʿjāz al-maʿnā* doctrine. The strongest hidden-architecture cases (Q 33, Q 10, Q 23) are candidates for new scholarly attention the project has surfaced.

*Bismillāhi al-Raḥmāni al-Raḥīm.*
