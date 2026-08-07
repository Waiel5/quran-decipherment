---
surah: 99
surah_name_ar: الزلزلة
surah_name_translit: al-Zalzala
file_type: empirical-profile
date_last_updated: 2026-05-09
phase: B+
verdict: Empirical anchors integrated from H-NEW-{111,590,700,720,750,840,860,1190,1200,1220}.
---

# Q 99 al-Zalzala — Empirical Architectural Profile


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

## 1. Headline numbers

| Metric | Value | Source / interpretation |
|:--|:--:|:--|
| Verse count | 8 | Hafs-Kufan |
| Word count (no-tashkeel) | 36 | computed |
| Letter count (no-tashkeel, sans spaces) | 158 | computed |
| Avg verse length (letters) | 19.75 | short-mufaṣṣal-qiṣār register |
| Avg verse length (words) | 4.50 | short-mufaṣṣal-qiṣār register |
| Top final-letter | ا (alif) | 5/8 verses (62.5%) — the *-hā* feminine-pronoun-suffix terminal |
| Rhyme entropy (nats) | 0.900 | mild rhyme-diversity (z = +0.236; Q 99 is NOT a strict monorhyme — 3 distinct rhyme-segments in 8 verses) |
| Mean content distance (FR) | 0.8148 | **BELOW corpus mean (0.92)** — Q 99 is content-CENTRAL |
| Local cohesion | 2.181 | **HIGH** — Q 99 is well-embedded in its short-tail neighborhood |
| iʿjāz sig_A | +1.309 (rank **20/114**) | **HIGH al-Bāqillānī iʿjāz al-fawāṣil signal** (top 18%) |
| iʿjāz sig_B | +1.138 (rank **24/114**) | **HIGH al-Sakkākī iqāʿ signal** (top 21%) |
| UAS | -0.483 (rank 61/114) | mid-pack overall (HIGH iʿjāz partly offset by low max-cost from being well-embedded in tail-cluster) |
| Outlier-strength Δ%ile | -0.07 pp | **NULL** (window {Q 96-102}; p_greater = 0.9999); Q 99 is highly cluster-typical, NOT a content outlier |
| Q 98→Q 99 cost | +0.1265 (delta_raw +0.1265) | mild seam (al-Bayyina to al-Zalzala) — content-shift from polemical-Medinan to eschatological-cosmic |
| Q 99→Q 100 cost | +0.0487 (delta_raw +0.0487) | low seam (al-Zalzala to al-ʿĀdiyāt is smooth) — both eschatological short-tail surahs |
| H-NEW-1200 14-cluster cohesion | mean dist to other 13 = 0.5915 vs corpus 0.815 | Q 99 is HIGH-COHESION member of the 14-cluster (cluster-mean / corpus-mean = 0.726) |
| H-NEW-1200 Sub-cluster A core | Q 99 ↔ {Q 81, 82, 84} mean = 0.558 | architectural CORE pairs FR ~0.52-0.57 |
| Hadith-emphasis score (H-NEW-860) | 4 (mid-low; Tirmidhī 2893→ corrected to 2976+2977 ḥalf-Qurʾān) | hadith corpus weakly emphasizes Q 99 — primarily through Tirmidhī gharīb chains (verified ḍaʿīf, see `04-hadith-corpus.md`) |
| FR-centroid rank (H-NEW-1220) | mean d = 0.8148, **rank ~14/114** | content-CENTRAL (top 12% of corpus by FR-centroid proximity) |

## 2. Fisher-Rao neighborhood (H-NEW-111)

Q 99's top-12 nearest in FR space (extracted from `findings/phase-b-hypotheses/csv/h-new-111.json` `D_matrix_upper_triangular`):

| Rank | Surah | Name | FR | Note |
|:-:|:-:|:--|:--:|:--|
| 1 | Q 108 | al-Kawthar | 0.3636 | shortest surah; corpus-rank-3 FR-centroid |
| 2 | Q 113 | al-Falaq | 0.3650 | muʿawwidhatān |
| 3 | Q 103 | al-ʿAṣr | 0.3727 | corpus-shortest 3-verse oath-eschatology |
| 4 | Q 114 | al-Nās | 0.3751 | muʿawwidhatān + ring-closure pair-with-Q-1 |
| 5 | Q 107 | al-Māʿūn | 0.3770 | charity-dispute eschatology |
| 6 | Q 100 | al-ʿĀdiyāt | 0.3793 | mushaf-RIGHT-NEIGHBOR (oath-cosmic-event opener) |
| 7 | Q 106 | Quraysh | 0.3911 | Quraysh-favor short-Meccan |
| 8 | Q 94 | al-Sharḥ | 0.3914 | divine-intimacy-pair-with-Q-93 |
| 9 | Q 110 | al-Naṣr | 0.3942 | last-revealed (Medinan), short |
| 10 | Q 105 | al-Fīl | 0.3942 | Year-of-Elephant short narrative |
| 11 | Q 112 | al-Ikhlāṣ | 0.3998 | corpus-rank-1 FR-centroid + theology-iʿjāz exemplar |
| 12 | Q 111 | al-Masad | 0.4022 | Abū Lahab curse |

**Q 99's FR-neighborhood is ENTIRELY SHORT-MUFAṢṢAL-QIṢĀR.** All 12 nearest neighbors have ≤ 11 verses. The closest 4 are all in the corpus's top-7 FR-centroid surahs (Q 108 = rank 3; Q 113 = rank 7; Q 114 = rank 6; Q 112 = rank 1). This places Q 99 at the heart of the corpus's architectural-anchor zone.

Far end (Q 99's 5 most-FR-distant surahs):
- Q 9 al-Tawba: 1.2936 (Medinan polemic; basmala-less)
- Q 4 al-Nisāʾ: 1.2890 (Medinan legal)
- Q 3 Āl ʿImrān: 1.2890 (Medinan)
- Q 5 al-Māʾida: 1.2472 (Medinan legal)
- Q 2 al-Baqara: 1.2442 (long Medinan)

The 5-most-distant pattern: Q 99 is content-MAXIMALLY-DISTANT from the LONG-MEDINAN-LEGAL block. This is the corpus's structural-asymmetry signature — short eschatological tail vs long Medinan legal head, exactly the cross-finding-016 mushaf-architecture polarization.

## 3. iʿjāz signature (H-NEW-750) — Q 99 is in the TOP-25

| Component | Value | z-score | Rank |
|:--|:--:|:--:|:--:|
| Rhyme entropy (nats) | 0.9003 | +0.236 | (mid-low entropy = mostly-monorhyme, 3-segment rhyme architecture) |
| Mean content distance | 0.8148 | -1.073 | (content-central) |
| Local cohesion | 2.181 | +0.902 | (HIGH local cohesion) |
| sig_A (iʿjāz al-fawāṣil) | **+1.309** | — | **rank 20/114 (TOP 18%)** |
| sig_B (iʿjāz iqāʿ) | **+1.138** | — | **rank 24/114 (TOP 21%)** |

Q 99 ranks in the TOP-25 of both al-Bāqillānī (iʿjāz al-fawāṣil = structural-rhetorical iʿjāz) and al-Sakkākī (iqāʿ = rhythm/cadence iʿjāz). This is striking for an 8-verse 36-word surah — Q 99 packs HIGH iʿjāz signature into very few words.

The iʿjāz fingerprint is consistent with the surah's empirical structure:
- **3-segment rhyme architecture** (vv. 1-5 *-hā* / v. 6 *-hum* / vv. 7-8 *-rah*) producing mid-entropy rhyme that scores high on al-Bāqillānī's fāṣila-virtuosity criterion.
- **Tight semantic-cohesion** (mean FR distance below corpus mean) yielding high local-cohesion z-score.
- **Short-verse pulse** (avg ~20 letters / verse) producing the iqāʿ rhythm-cadence signature.

This is among the strongest iʿjāz-signature scores in the short-mufaṣṣal-qiṣār region. Q 99 is **NOT** a UAS-top surah (UAS rank 61, mid) because UAS combines outlier-strength + max-cost + iʿjāz, and Q 99's outlier-strength is NULL (it is cluster-CENTRAL, not OUTLIER) and its max-cost is low (it is well-embedded). The HIGH iʿjāz signature is the surah's standalone architectural distinction.

## 4. Outlier-strength (H-NEW-590)

From `findings/phase-b-hypotheses/csv/h-new-590.json`:

| Field | Value |
|:--|:--:|
| Window | {Q 96, Q 97, Q 98, Q 99, Q 100, Q 101, Q 102} |
| d_W | 0.4719 |
| d_W − Q 99 | 0.4770 |
| Δ pp | -0.07 |
| pct_W | 0.01 |
| pct_W − Q 99 | 0.08 |
| p_greater_W | 0.9999 |
| Classification | **NULL** (NOT an outlier) |

Q 99 is **NOT** a content-outlier in its short-mufaṣṣal-qiṣār neighborhood. Removing Q 99 from the window {Q 96-102} produces a SLIGHT WORSENING of mean window-distance (0.4719 → 0.4770, Δ -0.07) — i.e. Q 99 is highly typical of its eschatological-tail cohort, not distinctive against it.

This is the architectural-counterpart to its FR-neighborhood profile (§2): Q 99 is the most cluster-typical member of the corpus's most-cohesive segment. Its iʿjāz-distinctiveness (§3) operates ABOVE the cluster-baseline rather than as separation from it.

## 5. Canonical-adjacency cost (H-NEW-720)

| Boundary | delta_raw | fraction_residual | Note |
|:--|:--:|:--:|:--|
| Q 98 → Q 99 | +0.1265 | 0.0153 | mild seam (al-Bayyina → al-Zalzala) — content-shift from polemical-Medinan to eschatological-cosmic; both surahs short-tail |
| Q 99 → Q 100 | +0.0487 | 0.0059 | LOW seam (al-Zalzala → al-ʿĀdiyāt) — both short-eschatological-tail; very smooth transition |

Neither adjacency is in the clamped-zero seamless set (13 corpus-wide) nor in the top-10 expensive seams (Q 9-Q 10 family). Q 99's mushaf-position shows MILD-LOW seam costs in both directions, consistent with its location in the short-mufaṣṣal-qiṣār cluster where adjacencies are generally low-cost.

The Q 99 → Q 100 adjacency at 0.0487 is among the lower-cost seams in the Q 95-110 region (alongside the seamless Q 91→92, Q 93→94, Q 105→106, Q 109→110). This is consistent with the H-NEW-1200 short-Meccan-tail-cohesion finding: the entire short-tail is internally low-cost.

## 6. H-NEW-1200 cluster role — Q 99 is a CORE member of the 14-surah eschatology meta-cluster

The 14-surah H-NEW-1200 cluster: **Q {56, 69, 74, 77, 81, 82, 83, 84, 86, 90, 97, 99, 101, 104}** — FR-cohesive at p=0.00030.

Q 99's distances to all other 13 cluster members:

| Member | FR to Q 99 | Cluster-role | Sub-cluster |
|:-:|:--:|:--|:-:|
| Q 56 al-Wāqiʿa | 0.8719 | idhā-cosmic-opener (peripheral) | A |
| Q 69 al-Ḥāqqa | 0.7347 | wa-mā adrāka mā | B |
| Q 74 al-Muddaththir | 0.7673 | wa-mā adrāka mā | B |
| Q 77 al-Mursalāt | 0.6956 | wa-mā adrāka mā + 10× refrain | B |
| **Q 81 al-Takwīr** | **0.5429** | **idhā-cosmic-opener (CORE)** | **A** |
| **Q 82 al-Infiṭār** | **0.5692** | **idhā-cosmic-opener (CORE)** | **A** (∩B) |
| Q 83 al-Muṭaffifīn | 0.6459 | refrain-bearing eschatology | B |
| **Q 84 al-Inshiqāq** | **0.5616** | **idhā-cosmic-opener (CORE)** | **A** |
| Q 86 al-Ṭāriq | 0.4799 | wa-mā adrāka mā | B |
| Q 90 al-Balad | 0.5202 | wa-mā adrāka mā | B |
| Q 97 al-Qadr | 0.4610 | wa-mā adrāka mā | B |
| Q 101 al-Qāriʿa | 0.4126 | wa-mā adrāka mā + idhā-imagery | B |
| Q 104 al-Humaza | 0.4261 | wa-mā adrāka mā | B |

**Q 99 mean distance to other 13 cluster members: 0.5915** vs Q 99's corpus-mean 0.8148. **Cluster-cohesion ratio: 0.726** (28% closer to cluster than to corpus on average).

**Q 99 is HIGHLY COHESIVE within H-NEW-1200.** It is closer to 12 of 13 other members than to corpus average; the only exception is Q 56 al-Wāqiʿa (0.872 vs 0.815 corpus mean), and Q 56 is itself the cluster-PERIPHERAL idhā-opener (consistent with its longer 96-verse length pulling it away from short-tail cohesion).

### Sub-cluster A architectural CORE: {Q 81, 82, 84, 99} at FR 0.52-0.57

The 4 idhā-cosmic-opener surahs that form the architectural CORE:

| Pair | FR distance |
|:-:|:--:|
| Q 81 ↔ Q 82 | (per H-NEW-1200 ledger: 0.52-0.57 band) |
| Q 81 ↔ Q 84 | (per H-NEW-1200 ledger: 0.52-0.57 band) |
| Q 81 ↔ Q 99 | **0.5429** |
| Q 82 ↔ Q 99 | **0.5692** |
| Q 84 ↔ Q 99 | **0.5616** |
| Q 82 ↔ Q 84 | (per H-NEW-1200 ledger) |

Q 99's mean distance to the 3 other CORE members (Q 81, 82, 84) = **0.5579**. This is among the corpus's tightest 4-surah architectural clusters.

The 4-CORE has an empirically-distinguishing property over the 5-surah Sub-cluster A: Q 56 al-Wāqiʿa has 96 verses (mid-Meccan length) while Q 81, 82, 84, 99 are all short (29, 19, 25, 8 verses respectively). The 4-CORE is the SHORT idhā-cosmic-opener architectural class. This is the cluster Q099-F-01 replicates (see `06-novel-findings.md`).

## 7. H-NEW-1190 wa-mā adrāka mā cluster — Q 99 is NOT a member

The 10-surah *wa-mā adrāka mā* cluster: Q {69, 74, 77, 82, 83, 86, 90, 97, 101, 104} — FR-cohesive at p=0.00068.

**Q 99 does NOT contain the *wa-mā adrāka mā* construction.** It is a member of H-NEW-1200 only via Sub-cluster A (idhā-cosmic-opener). The overlap pivot of A and B is **Q 82 al-Infiṭār** alone (the only surah that is BOTH an idhā-opener AND has a *wa-mā adrāka mā*).

Q 99 occupies a structurally-distinct position within H-NEW-1200: it is a PURE Sub-cluster A member, the only PURE-A member among the 4-CORE that does NOT also have *wa-mā adrāka* (Q 81 and Q 84 also lack it; Q 82 does have it). So the 3 PURE-A surahs are {Q 81, Q 84, Q 99} and the dual-membership pivot is Q 82.

## 8. Hadith-emphasis (H-NEW-860)

Q 99 hadith-emphasis score = 4 (mid-low). The H-NEW-860 catalog originally noted "Tirmidhī 2893: equals half the Qurʾān (chain ḍaʿīf-ḥasan)."

**EMPIRICAL VERIFICATION RESULT (this investigation)**: The exact Tirmidhī number is **2976** AND **2977** (NOT 2893 — that index references the chapter on red-garment-Salam). H-NEW-860 carries a clerical error in the hadith number; this investigation provides the verified primary-source hadith numbers.

The Tirmidhī 2976 + 2977 chains are BOTH **gharīb** by Tirmidhī's own classification, with single-channel transmissions through (a) al-Ḥasan b. Salm al-ʿIjlī [unique narrator] for 2976 and (b) Yamān b. al-Mughīra al-ʿAnazī [classified ḍaʿīf in the riyāl-al-jarḥ literature] for 2977. Per al-Albānī standards, both are **ḍaʿīf** (weak). See `04-hadith-corpus.md` for the full transcript and isnad-evaluation.

The hadith-emphasis score 4 for Q 99 is at the boundary between the structurally-emphasized (≥5) and weakly-emphasized (≤3) bands. Q 99's emphasis comes ENTIRELY from the (now-verified-weak) niṣf al-Qurʾān chain — it has no other major fadāʾil tradition.

## 9. Architectural typology — DUAL-IʿJĀZ profile

Per H-NEW-840 (UAS) + H-NEW-860 (hadith-fadāʾil), Q 99 sits in an interesting intermediate position:

- **al-Bāqillānī iʿjāz al-fawāṣil (structural)**: HIGH (sig_A rank 20/114).
- **al-Khaṭṭābī iʿjāz al-maʿnā (theological-content)**: HIGH (the Q 99:7-8 mithqāla-dharratin couplet is among the corpus's densest theological-summary verses).
- **Hadith-fadāʾil emphasis**: MID-LOW (score 4) — primarily through the verified-weak Tirmidhī niṣf chain.
- **Empirical centrality**: HIGH (mean FR distance 0.815, rank ~14/114 corpus-centroid; H-NEW-1200 cluster-CORE).

Q 99 is therefore architecturally distinctive on STRUCTURAL-IʿJĀZ axis AND theologically-distinctive on CONTENT-IʿJĀZ axis, but the hadith-tradition's emphasis on it (as half-the-Qurʾān) is empirically WEAK both at chain-authentication and at quantitative-ratio testing (see `05-classical-claims-audit.md`).

## 10. Cross-references

- [[h-new-111-fisher-rao-mushaf|H-NEW-111]] — FR matrix data source.
- [[h-new-590-outlier-spectrum|H-NEW-590]] — Q 99 NULL outlier classification.
- [[h-new-700-rhyme-phoneme-compression|H-NEW-700]] — rhyme-phoneme structure.
- [[h-new-720-canonical-adjacency-cost|H-NEW-720]] — adjacency cost data.
- [[h-new-750-ijaz-signature|H-NEW-750]] — iʿjāz sig_A/sig_B data.
- [[h-new-840-unified-architectural-score|H-NEW-840]] — UAS data.
- [[h-new-860-hadith-architectural-alignment|H-NEW-860]] — hadith emphasis (CORRECTED hadith-number provided by this investigation).
- [[h-new-1190-wa-ma-adraka-cluster|H-NEW-1190]] — wa-mā adrāka mā cluster (Q 99 NOT member).
- [[h-new-1200-short-meccan-eschatology|H-NEW-1200]] — 14-cluster (Q 99 CORE member of Sub-cluster A).
- [[h-new-1220-fr-centroid-ranking|H-NEW-1220]] — Q 99 mean d = 0.815 (rank ~14, content-central).
