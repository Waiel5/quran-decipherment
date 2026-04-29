---
surah: 33
surah_name_ar: الأحزاب
file_type: cross-references
date_last_updated: 2026-04-28
phase: B+
verdict: NEIGHBORS, CLUSTER MEMBERSHIP, CROSS-FINDING TIES MAPPED
---

# Q 33 al-Aḥzāb — Cross-References

## 1. Canonical-mushaf neighbors (Q 32, Q 34)

Q 33 is **inserted as the SOLE Medinan in a 15-surah Meccan run** (Q 28–42, per H-NEW-870). This positional anomaly drives Q 33's TSP-cost contribution to the cumulative mushaf residual.

| Pair | TSP Δ (length-units) | Fraction of TSP residual | Rank among 113 adjacencies |
|:--|--:|--:|--:|
| Q 1 ↔ Q 2 | 0.6216 | 7.50% | **1** |
| **Q 32 ↔ Q 33** | **0.3631** | **4.38%** | **2** |
| **Q 33 ↔ Q 34** | **0.3311** | **3.99%** | **3** |
| Q 9 ↔ Q 10 | 0.3094 | 3.73% | 4 |
| Q 24 ↔ Q 25 | 0.2896 | 3.49% | 5 |

Source: `findings/phase-b-hypotheses/csv/h-new-720.json`.

Combined Q 32–Q 33–Q 34 contribution: **8.37%** of the entire 8.29-length-unit mushaf TSP residual is concentrated in this 3-surah window. The Q 33 neighborhood is the **second-most-expensive transition** in the canonical mushaf order after Q 1 → Q 2.

- **Q 32 (al-Sajda)**: 30 verses, Meccan, mufaṣṣal-awsāṭ, alif-monorhyme moderate. Content: creedal/eschatological. Direct prosodic-content gap vs Q 33's Medinan-legal-narrative.
- **Q 34 (Sabaʾ)**: 54 verses, Meccan, mid-mufaṣṣal, narrative-eschatological (Sheba, Solomon, etc.). Content register: prophet-narrative + judgment.

The mushaf places a 73-verse Medinan-legal surah between two Meccan-narrative-eschatological surahs — generating two of the top-3 most-expensive canonical adjacencies.

## 2. Fisher-Rao nearest-neighbor cluster — the Medinan-legal cluster

Q 33's 10 FR-nearest neighbors (computed from `findings/phase-b-hypotheses/csv/h-new-111.json`):

| Rank | Surah | FR distance | Type | Length |
|--:|--:|--:|:--|--:|
| 1 | Q 4 (al-Nisāʾ) | 0.8374 | medinan | 176v |
| 2 | Q 2 (al-Baqara) | 0.8829 | medinan | 286v |
| 3 | Q 48 (al-Fatḥ) | 0.8895 | medinan | 29v |
| 4 | Q 3 (Āl ʿImrān) | 0.8991 | medinan | 200v |
| 5 | Q 49 (al-Ḥujurāt) | 0.9109 | medinan | 18v |
| 6 | Q 24 (al-Nūr) | 0.9134 | medinan | 64v |
| 7 | Q 8 (al-Anfāl) | 0.9166 | medinan | 75v |
| 8 | Q 9 (al-Tawba) | 0.9175 | medinan | 129v |
| 9 | Q 5 (al-Māʾida) | 0.9403 | medinan | 120v |
| 10 | Q 57 (al-Ḥadīd) | 0.9442 | medinan | 29v |

**ALL 10 nearest neighbors are Medinan**. Q 33 sits in a tight Medinan-legal-narrative cluster spanning the canonical positions 2-9, 24, 33, 48, 49, 57. This is the **Medinan-legal cluster** — a content-FR-defined community within the corpus.

Q 33's FR-farthest neighbor is **Q 55 (al-Raḥmān)** at d = 1.4921 — empirically the most opposite-content surah, per the dual-iʿjāz framework. Q 55 is the *ʿarūs al-Qurʾān* (al-Tirmidhī tradition) eschatological-rhyme surah; Q 33 is the Medinan-legal-content surah. The two anchor opposite ends of the iʿjāz axis (al-Bāqillānī structural-iʿjāz vs al-Khaṭṭābī theological-iʿjāz; cross-finding-026).

## 3. Cluster memberships

- **Medinan cluster** (29 surahs total): Q 33 is a member.
- **Direct vocative opening *yā ayyuhā al-nabī*** (3 surahs total): Q 33, Q 65, Q 66. All three are Medinan; all three address the Prophet directly; all three contain rules-for-the-Prophet specifically. Q 65, like Q 33, achieves 100% alif-monorhyme.
- **Surahs with battle-narrative + hypocrite-critique**: Q 8 (Badr), Q 9 (Tabūk), Q 33 (Trench), Q 47 (Muḥammad), Q 48 (Fatḥ / Ḥudaybiyya), Q 63 (al-Munāfiqūn). Q 33 is part of this Medinan-historical sub-cluster.
- **Surahs containing legal rules for the Prophet's wives**: only Q 33 has the explicit *ḥijāb*-and-*takhyīr* code, but Q 66 also addresses rules between the Prophet and his wives (asbāb regarding the Maria and Hafsa-ʿĀʾisha incident).
- **Surahs with explicit *amāna* terminology in trust-sense**: Q 4:58, Q 8:27, Q 23:8, Q 33:72, Q 70:32. The cosmic-trust framing is unique to Q 33:72.
- **Hapax: *khātam al-nabiyyīn*** (Q 33:40) — corpus-unique.
- **Hapax-pair: *ẓalūm jahūl*** (Q 33:72) — corpus-unique.

## 4. Cross-surah verse-twin links (per H-NEW-66 framework, where applicable)

The verse-twin network (H-NEW-66, where computed) lists explicit cross-references between verses sharing high lexical similarity:

- **Q 33:6** "*uli al-arḥām baʿḍuhum awlā bi-baʿḍ fī kitāb Allāh*" ↔ **Q 8:75** (identical clause): a near-exact lexical twin in inheritance-priority law.
- **Q 33:7** *al-mīthāq al-ghalīẓ* ↔ **Q 4:154**: cognate ratification-of-covenant phrase.
- **Q 33:21** *uswa ḥasana* (in the Prophet) ↔ **Q 60:4, Q 60:6** (in Ibrāhīm and his followers): the *uswa ḥasana* trope is shared between Q 33 (Medinan, Trench) and Q 60 (Medinan, post-Hudaybiyya).
- **Q 33:35** gender-parity catalog ↔ **Q 49:13** (*innā khalaqnākum min dhakar wa unthā wa jaʿalnākum shuʿūban wa qabāʾila*): both Medinan, both establish equality-of-classes; structurally analogous parallelisms.
- **Q 33:53** ḥijāb-of-houses ↔ **Q 24:27-28** (house-entry etiquette in Q 24, the *Sūrat al-Nūr*): the two ḥijāb-house-entry codes form a tight cross-surah pair.
- **Q 33:59** *jalābīb* exterior-garment ↔ **Q 24:31** (*khumur*, head-covering — a different but doctrinally adjacent garment-rule). The two Medinan modesty-rule passages cluster lexically.

## 5. H-NEW finding integrations

Q 33 is referenced in the following empirical findings:

- **[[h-new-590-outlier-spectrum]]**: Q 33 corpus-strongest content outlier, Δ%ile = +31.46pp, **rank 1/114**.
- **[[h-new-700-phonological-compression-tail]]**: Q 33 rhyme-entropy 0.072 nats (very low — but see Q033-F-01 for rules-tuple correction).
- **[[h-new-720-canonical-adjacency-cost]]**: Q 32-Q 33 (rank 2) + Q 33-Q 34 (rank 3) = 8.37% of TSP residual.
- **[[h-new-750-iʿjāz-signature]]**: Q 33 sig_A = -2.966 (rank 112/114), sig_B = -2.085 (rank 113/114). VERY LOW iʿjāz al-fawāṣil.
- **[[h-new-840-unified-architectural-score]]**: Q 33 UAS = 9.36, **rank 1/114**.
- **[[h-new-860-hadith-architectural-alignment]]**: Q 33 hadith-emphasis = 2/10 (LOW), UAS = 1/114 (HIGH) — the project's clearest "hidden-architecture" example.
- **[[h-new-870-q33-architectural-keystone]]**: removing Q 33 and refitting the compression-tail law yields ΔR² = +0.0013 (Q 33 is **local-singular, NOT global-keystone**).

## 6. Cross-finding ties

- **[[cross-finding-026-iʿjāz-architecture]]**: Q 33 sits on the structural-iʿjāz axis (high UAS) but **NOT** the iʿjāz-al-fawāṣil axis (rhyme-uniform, low sig_A). Anchors the dual-iʿjāz typology.
- **[[cross-finding-011-mushaf-fisher-rao-confirmed]]**: the Q 32-Q 33-Q 34 expensive triple is one of the three pillars of the mushaf-FR confirmed structure.
- **[[cross-finding-025-multi-axis-architecture]]**: Q 33 occupies a corner of the (UAS, hadith-emphasis) plane — high-architectural / low-popular — diagnostic of the "hidden architecture" type.

## 7. Pre-Islamic poetry comparators

For the alif-monorhyme axis (Q033-F-01):
- **Labid b. Rabīʿa**, *Muʿallaqa* (alif-monorhyme): 176/178 = 0.9888 alif-final rate. Closest Q 33-comparator in pre-Islamic poetry. Genre: ode-of-praise, partly elegiac.
- **ʿAmr b. Kulthūm**, *Muʿallaqa* (alif-monorhyme): 103/105 = 0.9810. Genre: tribal-boast.
- The other 4 Muʿallaqāt tested (Imruʾ al-Qays, ʿAntara, Ṭarafa, al-Ḥārith) use NON-alif rāwī (lām, mīm, dāl etc.) — their alif-final rate is 0.

So the *qaṣīda*-Quran similarity-class for alif-monorhyme is well-populated on both sides; Q 33's structural analogy to Labid / ʿAmr-b.-Kulthūm is real but not exclusive.

Source: `data/baseline-corpora/raw/muallaqa-*.txt`.

## 8. Honest limits

- The neighbor analysis uses Fisher-Rao on QAC stem-roots (no-tashkeel default rules-tuple). A different distance (cosine on TF, char-NCD) might shift the top-10 ordering.
- Cluster memberships (e.g., *yā ayyuhā al-nabī* opening cluster) are taxonomic — they do not by themselves carry empirical weight without an associated test.
- Verse-twin links are listed where lexically explicit; a full verse-twin-network re-computation (H-NEW-66 successor) is outside this surah-investigation scope.

## 9. Pointers for follow-up

- Pre-register a TF-IDF-weighted Jaccard re-test of the wives-cluster (Q033-F-05's Jaccard FALSIFICATION may be rules-tuple-fragile under TF-IDF).
- Investigate whether Q 33's Q-20 / Q-25 / Q-17 alif-monorhyme cluster (the 9-11 ranked alif-final-rate surahs) is a coherent stylistic cluster across the corpus (not just by alif-rate, but by full prosodic profile).
- Cross-validate H-NEW-870's keystone-test against a permutation-based leave-one-out rather than a single-surah leave-out.
