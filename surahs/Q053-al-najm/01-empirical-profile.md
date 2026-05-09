---
surah: 53
surah_name_ar: النجم
surah_name_translit: al-Najm
file_type: empirical-profile
date_last_updated: 2026-05-09
phase: B+
verdict: Empirical anchors integrated from H-NEW-{111, 590, 700, 720, 750, 840} for Q 53; project-novel sajda-14 cluster cohesion test computed (NULL).
---

# Q 53 al-Najm — Empirical Architectural Profile

## 1. Headline numbers

| Metric | Value | Source / interpretation |
|:--|:--:|:--|
| Verse count | 62 | Hafs-Kufan |
| Word count (no-tashkeel) | 372 | computed from `quran-no-tashkeel.json` |
| Letter count (no-tashkeel, no spaces) | 1,445 | computed |
| Avg verse-length (words) | 6.00 | very short (oath-opener stylistic class) |
| Avg verse-length (letters, no-spaces) | 23.31 | very short |
| Top final-letter | ى (alif maqṣūra) | 85.5% — near-monorhyme on -ā/-ay (`h-new-700.json`, with project-rule normalising ى to ي → 0.855) |
| Rhyme entropy (Shannon, nats) | **0.568** | LOW; ranks among the lowest in the strict-oath-opener cluster |
| Mean FR content distance to other 113 | 0.953 | `h-new-750.json`; corpus mean 0.924 → Q 53 is mildly content-distant |
| Local cohesion | 1.004 | `h-new-750.json`; near corpus median |
| iʿjāz sig_A | **−0.656 (rank 79/114)** | LOW al-Bāqillānī iʿjāz al-fawāṣil signature |
| iʿjāz sig_B | **−1.066 (rank 84/114)** | LOW al-Sakkākī iqāʿ signal |
| UAS | 0.532 (rank 34/114) | moderate unified architectural significance |
| Outlier-strength Δ%ile | +6.25 pp (window {Q 50…56}) | WEAK_OUTLIER; p_greater_W = 0.2939 |
| Q 52→Q 53 cost | delta_raw = +0.1251, fraction_residual 0.0151 | typical (median range) |
| Q 53→Q 54 cost | delta_raw = +0.2101, fraction_residual 0.0253 | top-20 expensive — content-genre transition (vision/ṣuḥuf-axioms → cosmic-eschatology + nation-destruction-catalog) |

## 2. Fisher-Rao neighborhood (H-NEW-111)

Q 53's top-15 nearest in FR space (decoded from `findings/phase-b-hypotheses/csv/h-new-111.json` `D_matrix_upper_triangular`):

| Rank | Surah | Name | FR | Note |
|:-:|:-:|:--|:--:|:--|
| 1 | Q 96 | al-ʿAlaq | **0.7126** | The FIRST revelation; *iqra*-pericope ↔ Q 53:1-18 vision (revelation-disclosure twin) |
| 2 | Q 87 | al-Aʿlā | 0.7489 | *ṣuḥuf Ibrāhīma wa-Mūsā* (Q 87:18-19) ↔ *ṣuḥuf Mūsā wa-Ibrāhīm* (Q 53:36-37); SCRIPTURE-AXIS-TWIN |
| 3 | Q 92 | al-Layl | 0.7635 | oath-opener cluster, monorhyme |
| 4 | Q 110 | al-Naṣr | 0.7756 | short Medinan victory |
| 5 | Q 102 | al-Takāthur | 0.7769 | oath-opener cluster, eschatological warning |
| 6 | Q 1 | al-Fātiḥa | 0.7775 | early-Meccan opening / 7-verse short |
| 7 | Q 93 | al-Ḍuḥā | 0.7822 | oath-opener cluster, address-to-Prophet |
| 8 | Q 81 | al-Takwīr | 0.7825 | *idhā*-protasis cluster, vision-twin (Q 81:22-25) |
| 9 | Q 108 | al-Kawthar | 0.7873 | shortest surah; project-MST-hub (H-NEW-131) |
| 10 | Q 91 | al-Shams | 0.7906 | strict 7-oath cluster, monorhyme |
| 11 | Q 100 | al-ʿĀdiyāt | 0.7932 | oath-opener cluster |
| 12 | Q 79 | al-Nāziʿāt | 0.7946 | oath-opener cluster |
| 13 | Q 99 | al-Zalzala | 0.7955 | mufaṣṣal-end eschatology |
| 14 | Q 112 | al-Ikhlāṣ | 0.7959 | sui-generis short |
| 15 | Q 94 | al-Sharḥ | 0.7967 | address-to-Prophet, oath-cluster-adjacent |

**Q 53's FR-neighborhood is the very-short-Meccan vision/revelation/oath-opener cluster.** This is striking given Q 53 is ONLY 62 verses but its content-fingerprint converges on the *much shorter* short-Meccan-tail (Q 78–114). The closest neighbor Q 96 al-ʿAlaq is the **FIRST revelation** historically (al-Bukhārī ṣaḥīḥ 3, ʿĀʾisha narration), making the Q 96 ↔ Q 53 distance the corpus-empirical signature of the **revelation-vision-disclosure thematic register**.

Mean distance Q 53 → all 113 = 0.953 (corpus mean 0.924; z slightly positive — Q 53 is mildly content-distant).

Far end:

| Surah | FR | Note |
|:--|:--:|:--|
| Q 9 al-Tawba | 1.247 | basmala-less Medinan polemic |
| Q 4 al-Nisāʾ | 1.244 | long Medinan legal |
| Q 3 Āl ʿImrān | 1.201 | long Medinan creedal-legal |

The far-end is the long-Medinan-legal pole, exactly opposite to Q 53's short-Meccan-vision register. This is the strongest content-genre-axis the FR matrix detects.

## 3. Outlier-strength (H-NEW-590)

From `findings/phase-b-hypotheses/csv/h-new-590.json` X=53 row:

| Field | Value |
|:--|:--:|
| Window | {Q 50, Q 51, Q 52, Q 53, Q 54, Q 55, Q 56} |
| d_W | 0.971 |
| d_W − Q 53 | 0.965 |
| Δ pp | **+6.25** |
| pct_W | 70.61 |
| pct_W − Q 53 | 64.36 |
| p_greater_W | 0.2939 |
| Classification | **WEAK_OUTLIER** |

Q 53 is mildly content-distinct from its mufaṣṣal-ṭiwāl neighborhood (Q 50–56), but the perm-p of 0.29 says the surah is **not** a strong outlier. The window itself is moderately cohesive (mean d_W 0.971), and Q 53 sits inside the typical-content-band of its neighborhood. This is consistent with Q 53 being a content-genre-bridge: its FR-fingerprint pulls toward the short-Meccan-tail (top-15 above) but its mushaf-position embeds it in the mufaṣṣal-ṭiwāl band Q 50–56.

## 4. iʿjāz signature (H-NEW-750)

| Component | Value | z-score | Note |
|:--|:--:|:--:|:--|
| Rhyme entropy (nats) | 0.568 | −0.365 | LOW (near-monorhyme — alif-maqṣūra dominant) |
| Mean content distance | 0.953 | +0.291 | slightly content-distant |
| Local cohesion | 1.004 | −0.701 | LOW |
| **sig_A** (al-Bāqillānī iʿjāz al-fawāṣil) | −0.656 | — | **rank 79/114** (LOW) |
| **sig_B** (al-Sakkākī iqāʿ) | −1.066 | — | **rank 84/114** (LOW) |

Q 53 is LOW on both iʿjāz axes, despite having the strongest VISION-narrative content-density in the corpus. The interpretation: Q 53's **iʿjāz signature is content-paradigmatic, not formal-prosodic**. The surah's distinctiveness is in its content-anchor role (vision pericope, scripture-axiom block, sajda-command closure) rather than in its formal sajʿ-rhythm signature. This is consistent with the broader project finding (cross-finding-026) that iʿjāz is a multi-axis bundle and individual surahs concentrate their iʿjāz-signal on one or two axes, not all simultaneously. Q 53's distinctiveness lives in **vision-narrative-monopoly + scripture-axiom-density + sajda-command-closure**, not in fawāṣil-rhythm.

## 5. Canonical-adjacency cost (H-NEW-720)

| Boundary | delta_raw | fraction_residual | Note |
|:--|:--:|:--:|:--|
| Q 51 → Q 52 | +0.0096 | 0.0012 | very low — Dhāriyāt-Ṭūr smooth (the strict 1-element-Ṭūr-oath echoes the 4-element-Dhāriyāt-oath classification) |
| Q 52 → Q 53 | +0.1251 | 0.0151 | typical (median range); Ṭūr-Najm is a non-clamped, non-expensive transition |
| **Q 53 → Q 54** | **+0.2101** | **0.0253** | **top-20 expensive** — Najm-Qamar transition (vision/scripture-axioms → cosmic-eschatology + qamar-splitting + Nūḥ-Hūd-ʿĀd-Thamūd-Lūṭ catalog) |
| Q 54 → Q 55 | +0.0248 | 0.0030 | very low — Qamar-Raḥmān smooth |

Q 53's right-seam is among the project's top-20 most-expensive seams in the canonical mushaf order (cf. `h-new-720.json` `top10_expensive`: Q 1→Q 2, Q 32→Q 33, Q 33→Q 34, Q 9→Q 10, Q 24→Q 25, Q 22→Q 23, Q 42→Q 43, Q 56→Q 57, Q 12→Q 13, Q 7→Q 8 — Q 53→Q 54 ranks ~20th by delta_raw). This is **content-genre-transition cost**, not a chronology-mismatch artifact: Q 53 closes with the sajda-command and a 10-fold theological-axiom block; Q 54 opens with the moon-splitting cosmological-sign + a refrain-driven nation-destruction catalog.

The Q 51 → Q 52 → Q 53 → Q 54 → Q 55 → Q 56 → Q 57 sequence shows two **near-clamped** seams (Q 51→52 + Q 54→55) flanking the structural-content transitions (Q 53→54 + Q 56→57). The Q 56→57 seam is one of the project's **3 universal hinges** (cross-finding-013), maximal under both content + rhythm features. Q 53→54 is a content-only structural transition.

## 6. UAS / unified architectural significance (H-NEW-840)

| Field | Value |
|:--|:--:|
| UAS | 0.532 |
| abs_outlier (window 50–56) | +6.25 |
| max_cost (Q 53→Q 54) | 0.210 |
| abs_ijaz | 0.656 |
| **UAS rank** | **34 / 114** |

Q 53 is a moderate-UAS surah — well above the corpus median but not in the top-15 (the project's "structurally-distinctive" cohort {Q 1, Q 2, Q 33, Q 9, Q 24, Q 56, Q 55, Q 18, …}). Q 53's UAS is driven by its right-seam cost (Q 53→54 transition) + its WEAK_OUTLIER status in the Q 50-56 window, with iʿjāz-axis contributing modestly.

## 7. Cross-cluster memberships

| Cluster | Membership | Status |
|:--|:--|:--|
| **14 sajda-surahs** | {Q 7, 13, 16, 17, 19, 22, 25, 27, 32, 38, 41, **Q 53**, 84, 96} | MEMBER (FIRST in mushaf order; one of 3 surahs whose sajda is also their last verse — alongside Q 7 and Q 96) |
| **18 oath-opener-stylistic family** | {Q 37, 51, 52, **Q 53**, 56, 75, 77, 79, 81, 85, 86, 89, 90, 91, 92, 93, 95, 100, 103} | MEMBER (1-element oath-opener variant; structurally-minimal opener) |
| **Vision-revelation pericope cluster** | {Q 53:1–18, Q 81:22–25, Q 17:1, Q 96:1–5} | MEMBER (Q 53 is the longest-detail member; Q 53:1-18 vision pericope is the corpus's single most-explicit prophetic-vision text) |
| **Scripture-axiom cluster** ("ṣuḥuf Mūsā/Ibrāhīm" anchor) | {Q 53:36–37, Q 87:18–19, Q 80:13, Q 81:10, Q 98:2, Q 74:52, Q 20:133} | MEMBER; 8 total ṣuḥuf-tokens corpus-wide; Q 53:36 + Q 87:19 are bilateral cross-references (both name *ṣuḥuf Mūsā wa-Ibrāhīm* in their final verses) |
| **Mufaṣṣal-ṭiwāl** (per H-NEW-540) | Q 50–67 stratum | MEMBER (s = 53) |

## 8. Notable Quranic hapaxes anchored at Q 53

- **al-Shiʿrā** (الشِّعْرَى — Sirius) at Q 53:49 — Quranic hapax. Q 53 is the only Quranic mention of Sirius. Pre-Islamic Arab cosmology accorded Sirius cult-status (worshipped in Khuzāʿa, per al-Shahrastānī *al-Milal wa-l-Niḥal* I.245); Q 53:49 explicitly subordinates the cult-deity to the cosmological-hierarchy (*wa-annahu huwa rabbu l-shiʿrā* — "He is the Lord of Sirius").
- **ʿĀd al-ūlā** (the FIRST ʿĀd) at Q 53:50 — Quranic hapax of the temporal-ordinal *al-ūlā* applied to ʿĀd. ʿĀd appears ~19 times across the corpus; *al-ūlā* qualifies it ONLY here. The classical interpretation (al-Ṭabarī, al-Rāzī) treats *al-ūlā* as distinguishing pre-Islamic ʿĀd from later ʿĀd (cf. al-Aḥqāf), supporting an internal-Quranic dating-system.
- **al-Muʾtafika** (المؤتفكة — the overturned town) at Q 53:53 — appears only 4× in the corpus (Q 9:70, Q 53:53, Q 69:9, Q 53 + ʿĀʾisha-Q 9 framing); Q 53:53 is the only occurrence of the singular *al-muʾtafika ahwā* (singular, not plural). The plural *al-muʾtafikāt* dominates elsewhere.
- **Sidrat al-Muntahā** (سدرة المنتهى) at Q 53:14 + 16 — Quranic 2× attestation, ZERO other surahs.
- **Jannat al-Maʾwā** (جنة المأوى) at Q 53:15 — Quranic hapax.

The Q 53:13–18 vision pericope and the Q 53:49–50 cosmological-naming pair are thus **lexically Q 53-monopoly** content-anchors.

## 9. The 10 *wa-anna* clauses (Q 53:39–50)

Cross-confirmed against `findings/phase-c-structures/cryptographic-signatures.md` §5. Independent verification (this specialist's regex scan): exactly 10 verses contain a *wa-anna(hu)* opener within the v 39–50 block:

| # | v | Text | Theological axiom |
|:-:|:-:|:--|:--|
| 1 | 39 | *wa-an laysa li-l-insāni illā mā saʿā* | Man's reward depends only on his striving |
| 2 | 40 | *wa-anna saʿyahu sawfa yurā* | His striving will be seen |
| 3 | 42 | *wa-anna ilā rabbika l-muntahā* | All ends in your Lord |
| 4 | 43 | *wa-annahu huwa aḍḥaka wa-abkā* | He makes laugh and weep |
| 5 | 44 | *wa-annahu huwa amāta wa-aḥyā* | He gives death and life |
| 6 | 45 | *wa-annahu khalaqa l-zawjayni l-dhakara wa-l-unthā* | He created the two pairs (m/f) |
| 7 | 47 | *wa-anna ʿalayhi l-nashʾata l-ukhrā* | The next creation is His responsibility |
| 8 | 48 | *wa-annahu huwa aghnā wa-aqnā* | He grants wealth and possession |
| 9 | 49 | *wa-annahu huwa rabbu l-shiʿrā* | He is the Lord of Sirius |
| 10 | 50 | *wa-annahu ahlaka ʿādan il-ūlā* | He destroyed the first ʿĀd |

Two interpolated short verses (vv 41 and 46) interrupt the block as scope-markers but do not break the syntactic chain. The 10 axioms span 12 verses. Verses 51–54 *wa-thamūda fa-mā abqā / wa-qawma nūḥin min qabl / wa-l-muʾtafikata ahwā / fa-ghashshāhā mā ghashshā* continue the sentence as parallel-clauses but without *wa-annahu* (they are coordinate to clause #10, the destruction-list extension).

This is the project's **8th catalogued cryptographic-syntactic signature** (cf. `findings/phase-c-structures/cryptographic-signatures.md` Table 1), graded MODERATE-overall STRONG-on-count. The 10-count parallel to the Decalogue is striking but unclaimed in the surah; the framing (vv 36–37 *fī ṣuḥufi mūsā / wa-ibrāhīma lladhī waffā*) explicitly invites a *summary-of-earlier-scriptures* reading without the 10-count being numerically claimed.

## 10. Sajda-surahs corpus list (verified 2026-05-09)

I verified the 14 sajda-surah list by direct corpus scan for the ۩-marker in `quran-no-tashkeel.json` (script: `scripts/Q053_F_03_sajda_cohesion.py`, run 2026-05-09):

| # | Surah | Sajda verse(s) | Mushaf-final? |
|:-:|:-:|:--|:-:|
| 1 | Q 7 al-Aʿrāf | v 206 (of 206) | YES (last verse) |
| 2 | Q 13 al-Raʿd | v 15 | no |
| 3 | Q 16 al-Naḥl | v 50 | no |
| 4 | Q 17 al-Isrāʾ | v 109 | no |
| 5 | Q 19 Maryam | v 58 | no |
| 6 | Q 22 al-Ḥajj | v 18 + v 77 (TWO) | no |
| 7 | Q 25 al-Furqān | v 60 | no |
| 8 | Q 27 al-Naml | v 26 | no |
| 9 | Q 32 al-Sajda | v 15 | no |
| 10 | Q 38 Ṣād | v 24 | no |
| 11 | Q 41 Fuṣṣilat | v 38 | no |
| **12** | **Q 53 al-Najm** | **v 62 (of 62)** | **YES (last verse)** |
| 13 | Q 84 al-Inshiqāq | v 21 | no |
| 14 | Q 96 al-ʿAlaq | v 19 (of 19) | YES (last verse) |

Total verses ☩-marked: **15** (with Q 22 contributing two). 14 distinct sajda-surahs. Q 7, Q 53, Q 96 are the 3 surahs whose sajda IS the last verse. **The Hanafī, Mālikī, Shāfiʿī, and Ḥanbalī madhāhib all agree that Q 53:62 is a confirmed sajda-position** (cf. Q053-F-Q053-T-classical-claims-audit.md §3; Bukhārī 1067, Muslim 576, Nasāʾī 956, Tirmidhī 575).

### Sajda-14 cluster cohesion test (informational pre-test scan, formal pre-reg = Q053-F-03)

Computed pairwise mean Fisher-Rao distance over the 14 sajda-surahs:

| Quantity | Value |
|:--|:--:|
| Sajda-14 within-cluster pairwise mean FR | **0.9414** |
| Number of pairs | 91 |
| Corpus-wide pairwise mean FR | 0.9235 |
| Ratio (within / corpus) | 1.0194 |
| 20,000-perm null mean | 0.9237 |
| 20,000-perm null sd | 0.0531 |
| z-score | +0.333 |
| Permutation p (within-mean ≤ obs) | **0.588** |

**Verdict (informational pre-test scan)**: NULL — the 14 sajda-surahs do NOT form an FR-cohesive cluster. The within-cluster mean is *slightly above* corpus mean (in the wrong direction for cohesion), at 0.59 perm-p. This is a clean directional NULL: the sajda-classification is a **functional-liturgical** classification (where to prostrate during recitation), NOT a content-fingerprint classification.

This NULL has significant interpretive value: it adds to the project's catalog of *functional-classifications without content-cohesion* (alongside H-NEW-68 Friday-recitation-cluster NULL, H-NEW-69 14-vs-14 alphabet-split NULL). The classical *sujūd al-tilāwah* practice is observed at sajda-marked verses and crystallized into 14 surahs by classical-fiqh consensus — but those 14 surahs do NOT share a content-vector signature. This is consistent with the M-5 decomposition: classical practical/legal classifications often lack empirical structural-cohesion, while classical balāgha-rhetorical classifications often have it.

The formal pre-registered test is at `preregs/Q053-F-03-sajda-14-fr-cohesion-prereg.md` (SHA-locked, 10,000 perms, single-test α = 0.05).

## 11. Final-letter coordinate system

Q 53's verse-final pattern (column = final letter):

```
Verses 1-15 (vision pericope):    ى ى ى ى ى ى ى ى ى ى ى ى ى ى ى
Verses 16-30 (polytheism block):  ى ى ى ى ى ى ى ى ى ى ى ى ى ى ى
Verses 31-45 (axiom + ṣuḥuf):     ا ى ى ى ا ى ى ى ى ى ى ى ى ى ى
Verses 46-62 (continuing):        ى ى ا ى ى ى ى ى ى ى ا ة ن ن ن ة ا
```

The 53/62 ى-final dominates the entire surah. The 4 alif-final verses (vv 31, 35, 41, 48 — ah, ʿalimā, al-awfā, aqnā in their tashkeel forms — render to ا/ي rhythmically equivalent in fāṣila reading), the 3 nūn-final verses (vv 59, 60, 61 — taʿjabūn, tabkūn, sāmidūn, last 3 before sajda), and the 2 tāʾ-marbūṭa-final verses (vv 57, 58 — ʿāzifa, kāshifa) form **3 micro-clusters of rhyme-shift**:

- The 4 alif-final scattered verses: brief rhyme-modulation moments
- The 3 nūn-final closing-section verses: building rhythmic urgency before the final command
- The 2 tāʾ-marbūṭa verses just before: the *azifati l-āzifa / laysa lahā mīn dūni llāhi kāshifa* doublet, classical balāgha *taṣrīʿ*-doubling

The closing 6 verses 57-62 cycle through 3 final-letter patterns (ة–ة–ن–ن–ن–[sajda]) before the final sajda-imperative. This is rhyme-coda engineering — the final 6 verses break the dominant ى-monorhyme to mark the surah's terminus.

## 12. Content-anchored summary

Q 53 is empirically:
- **Mid-mushaf-position-but-short-Meccan-content-fingerprint** (FR-nearest is Q 96, not Q 52 nor Q 54)
- **Near-monorhyme** on alif-maqṣūra at 85.5% — ranks among lowest rhyme-entropy in the corpus
- **LOW iʿjāz on both prosodic-axes** (sig_A rank 79, sig_B rank 84) — its iʿjāz lives in *content* (vision-monopoly + scripture-axiom-density + sajda-closure), not in *form*
- **Top-20 expensive right-seam** (Q 53→Q 54 = +0.210) — the Najm-Qamar transition is content-genre
- **Member of 14 sajda-surahs cluster** (the cluster is functionally-defined, NOT FR-cohesive — informational pre-test scan p = 0.588 NULL)
- **Q 53's nearest neighbor is Q 96 al-ʿAlaq** (the FIRST revelation) — the Q 53 ↔ Q 96 axis is the corpus signature of the **revelation-vision-disclosure thematic register**

## 13. Cross-references

- [[h-new-111-fisher-rao-mushaf]] — Q 53 FR matrix row.
- [[h-new-590-outlier-spectrum]] — Q 53 weak outlier on Q 50-56 window.
- [[h-new-700-phonological-compression-tail]] — Q 53 ى/ي-rhyme dominant (0.855).
- [[h-new-720-canonical-adjacency-cost]] — Q 53→Q 54 top-20 expensive.
- [[h-new-750-ijaz-signature]] — Q 53 LOW on both axes, ranks 79 and 84.
- [[h-new-840-unified-architectural-score]] — Q 53 UAS rank 34/114.
- [[cross-finding-013-mushaf-as-topological-ring]] — Q 56→Q 57 (downstream from Q 53) is a project-confirmed universal hinge.
- `surahs/Q052-al-tur/` (mushaf left-neighbor; not yet specialized).
- `surahs/Q054-al-qamar/` (mushaf right-neighbor; not yet specialized).
- `surahs/Q051-al-dhariyat/` (oath-opener-cluster sibling; not yet fully specialized).
- `surahs/Q037-al-saffat/` (oath-opener-cluster sibling; specialist run 2026-05-08).
- `surahs/Q055-al-rahman/` (mushaf right-+1 neighbor; specialist run 2026-04-28).
- `surahs/Q096-al-alaq/` (FR-nearest neighbor; not yet specialized).
- `surahs/Q087-al-ala/` (FR #2-nearest; ṣuḥuf-Mūsā-Ibrāhīm bilateral cross-reference; not yet specialized).
