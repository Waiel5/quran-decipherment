---
surah: 17
surah_name_ar: الإسراء
file_type: empirical-profile
date_last_updated: 2026-04-28
phase: B+
verdict: All H-NEW metrics integrated; cross-validated across 4 tashkeel variants
---

# Q 17 al-Isrāʾ — Empirical Profile

All values cited from on-disk artifacts. Rules-tuple defaults to project standard `(no-tashkeel, orthographic-token, graphemes, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)` unless otherwise noted.

## 1. Headline scores

| Metric | Value | Rank | Source |
|:--|--:|:-:|:--|
| **UAS (Unified Architectural Score)** | 2.220 | **10/114** | `findings/phase-b-hypotheses/csv/h-new-840.json` |
| Outlier-strength Δ%ile | **−3.94pp** | NULL | `findings/phase-b-hypotheses/csv/h-new-590.json` |
| iʿjāz signature sig_A | **−2.396** | **111/114** | `findings/phase-b-hypotheses/csv/h-new-750.json` |
| iʿjāz signature sig_B | **−1.901** | **109/114** | same |
| Mean content distance (FR-roots) | 1.034 | high | same |
| Local cohesion | 1.077 | high | same |
| Rhyme entropy (Shannon, nats) | **0.0514** | **2nd lowest tier** | same |
| Top final letter | **ا (alif)** | n/a | same |
| Top final letter fraction | **0.9910** | **dense-rank 2/114** | Q017-F-01 |

UAS is the geometric integration of |outlier|, max-cost, |sig_A|. Q 17 sits in the UAS top-10 because of the strong |sig_A|=2.40 contribution and the moderate Q16-Q17 adjacency-cost contribution — NOT because of outlier strength (|outlier|=3.94 is mid-pack).

## 2. UAS decomposition

```
UAS = sqrt( |outlier| · max_cost · |sig_A| )
    = sqrt( 3.94 · 0.191 · 2.396 )
    = sqrt( 1.803 )
    = 2.220
```

Component-by-component:
- |outlier| = 3.94 (moderate; rank ~60 of 114)
- max_cost = 0.191 (moderate; the larger of {Q16-Q17 cost = 0.191, Q17-Q18 cost = 0.028})
- |sig_A| = 2.396 (high; rank 111/114, i.e., 4th-strongest absolute deviation from iʿjāz al-fawāṣil neutrality)

The signal driving Q 17's UAS top-10 is **iʿjāz al-fawāṣil deviation**, in the negative direction: Q 17 is one of the corpus's most rhyme-uniform, most-poetry-like-form surahs.

## 3. Outlier-strength detail (H-NEW-590)

From `h-new-590.json`, candidate Q 17 record:
- Window: surahs `[14, 15, 16, 17, 18, 19, 20]` (the 7-window centered on 17).
- d̄_W (full window mean content distance): 0.9577.
- d̄_{W minus X} (window without Q 17): 0.9679.
- pct_W = 62.11; pct_{W minus X} = 66.05; **Δpct = −3.94**.
- p_greater = 0.3789 (NS even at α=0.05).
- Classification: **NULL** (Q 17 is not a strong-outlier nor a strong-anchor in its window).

**Interpretation**: Q 17 is *integrated* into the mathānī Meccan-narrative neighborhood (Q 14-20 surrounds it: Ibrāhīm, al-Ḥijr, al-Naḥl, al-Isrāʾ, al-Kahf, Maryam, Ṭāhā). This is consistent with the Ibn Masʿūd ḥadīth (al-Bukhārī #4502, #4533): the five "ʿitāq al-uwal" surahs (Banī Isrāʾīl, al-Kahf, Maryam, Ṭāhā, al-Anbiyāʾ) are precisely Q 17, 18, 19, 20, 21 — five canonical neighbors. Q 17 leads a tightly-clustered run.

## 4. iʿjāz signature (H-NEW-750)

From `h-new-750.json`:
- n_verses = 111
- rhyme_entropy_nats = 0.05140 (very low)
- top_final_letter = ا (alif)
- top_final_letter_frac = 0.99099
- mean_content_distance = 1.0344 (above corpus mean)
- local_cohesion = 1.0775
- z_rhyme_entropy = −1.301 (low)
- z_mean_content_distance = +1.095 (high)
- z_local_cohesion = −0.600 (slightly low)
- **sig_A = −2.396** (rank 111/114)
- **sig_B = −1.901** (rank 109/114)

Q 17's negative sig_A signature is the **anti-iʿjāz al-fawāṣil profile**: high rhyme uniformity (alif-monorhyme) AND high content-distance (vocabulary-spread). This is the *qaṣīda*-like form: a poet's monorhyme controlled across diverse content. al-Bāqillānī's *iʿjāz al-fawāṣil* doctrine — that the Qurʾān excels by VARYING its rhyme to follow content — would mark Q 17 as far from his ideal. But classical tradition's response is precisely to assign Q 17 a different iʿjāz axis: the *taḥaddī* (challenge-of-inimitability) at v.88, which is the **maximal** taḥaddī in the corpus.

This is one example of the **dual-iʿjāz typology** at work (al-Bāqillānī structural-iʿjāz vs al-Khaṭṭābī theological-iʿjāz): Q 17 wins on the theological-iʿjāz axis (taḥaddī) while embodying *anti*-structural-iʿjāz (qaṣīda monorhyme).

## 5. Position in compression-tail laws (Wave 2026-04-28)

Q 17 is at s=17, well below the s=50 Meccan-Medinan kink. By the established laws:
- d̄_content predicted by law: 0.96 (plateau region; max(0, s-50) = 0). **Observed mean content distance: 1.034** — above the law's predicted plateau, consistent with Q 17 being slightly distinctive in content-spread within the head.
- d̄_rhyme predicted by law: 0.36 (plateau). **Observed rhyme entropy of 0.0514 nats** is far below 0.36 — Q 17 is rhyme-COMPRESSED far below corpus head-norm. This is the alif-monorhyme effect.
- d̄_phoneme predicted by law: 0.001 (plateau, kink at s=75). Q 17 is consistent with this baseline.
- d̄_verse-length: Q 17's verses are mid-length (avg ≈ 14.8 words/verse: 1644 words / 111 verses = 14.81), above the Meccan-mufaṣṣal range. Verses are longer than Q 87-114 but shorter than Q 2-9.

## 6. Canonical adjacency costs (H-NEW-720)

- **Q 16-17 (al-Naḥl → al-Isrāʾ)**: Δ = **0.191** (`fraction_residual = 0.0230`). This is rank 12 of 113 — moderately high. Q 16 al-Naḥl is itself an alif-monorhyme-LEANING (but mixed) surah; Q 17 sharpens to nearly-pure alif-monorhyme. The transition is content-rich.
- **Q 17-18 (al-Isrāʾ → al-Kahf)**: Δ = **0.028** (`fraction_residual = 0.0034`). This is bottom-quartile cost — Q 17 → Q 18 is a **natural** transition. Both are Meccan, both alif-monorhyme (Q 17 at 0.991, Q 18 at 1.000), and they share the Ibn Masʿūd ʿitāq-al-uwal ḥadīth grouping.

The Q 16-17 / Q 17-18 cost asymmetry is a classical-empirical resonance: classical tradition treats Q 17, 18, 19, 20, 21 as a **block** (the ʿitāq al-uwal), and the empirical TSP-cost confirms cheap intra-block transitions.

## 7. Fisher-Rao (FR) distance neighbors (H-NEW-111)

Q 17's 10 nearest neighbors by FR-roots distance:

| Rank | Neighbor | FR distance | Relationship |
|--:|:-:|--:|:--|
| 1 | Q 25 al-Furqān | 0.809 | Meccan, alif-monorhyme tier (rank 10), criterion-of-truth surah |
| 2 | Q 41 Fuṣṣilat | 0.864 | Ḥawāmīm; Meccan |
| 3 | Q 34 Sabaʾ | 0.865 | Meccan; David/Solomon |
| 4 | Q 27 al-Naml | 0.868 | Meccan; Solomon |
| 5 | Q 7 al-Aʿrāf | 0.878 | Meccan; long; Banī Isrāʾīl narrative |
| 6 | Q 23 al-Muʾminūn | 0.894 | Meccan; UAS rank 9 (next-door neighbor in UAS) |
| 7 | Q 46 al-Aḥqāf | 0.894 | Meccan, ḥawāmīm-tail |
| 8 | Q 10 Yūnus | 0.897 | Meccan; UAS rank 8 |
| 9 | Q 43 al-Zukhruf | 0.901 | Meccan ḥawāmīm |
| 10 | Q 18 al-Kahf | 0.901 | Meccan; canonical neighbor; ʿitāq al-uwal partner |

The cluster is a **mathānī Meccan-narrative core**, with strong overlap to ḥawāmīm and Solomon-Pharaoh-Israel cycles. Q 17 sits at this cluster's center.

## 8. FR-distance to key cross-references

- Q 17 ↔ Q 33 (al-Aḥzāb, alif-monorhyme tier-mate): 1.091 (mid-far). Q 17 and Q 33 share rhyme-form but differ sharply in content-distribution (Q 17 Meccan-narrative; Q 33 Medinan-legal).
- Q 17 ↔ Q 1 (al-Fātiḥa): 1.076 (far).
- Q 17 ↔ Q 2 (al-Baqara): 0.983 (mid).
- Q 17 ↔ Q 18 (al-Kahf): 0.901 (close; canonical neighbor).
- Q 17 ↔ Q 16 (al-Naḥl): 0.962 (mid; cf. canonical adjacency cost 0.191).

## 9. Phoneme density (H-NEW-700)

H-NEW-700 reports per-surah phoneme distributions. Q 17 sits in the head zone (s=17, kink at s=75 for phoneme law) at near-baseline d̄_phoneme. No phonemic outlier signature.

## 10. Architectural type classification

- **NOT structural-iʿjāz hub** (UAS rank 10 — close to the elite but not in the al-Bāqillānī structural-iʿjāz top tier).
- **NOT outlier** (Δ_outlier = −3.94pp NULL).
- **YES anti-iʿjāz al-fawāṣil** (sig_A rank 111/114) — qaṣīda-form surah.
- **YES theological-iʿjāz hub** via Q 17:88 maximal taḥaddī (verified Q017-F-03).
- **YES architectural-classical-name vindication**: Banī-Isrāʾīl content rank 4/114 (Q017-F-04 vindicated).

**Type label**: **dual-iʿjāz hybrid — qaṣīda-form host of the maximal taḥaddī**. Q 17 is rare in the corpus: it has the most poetry-adjacent FORM and the most content-confident anti-poetry CHALLENGE in the same text.

## 11. Cross-references to all H-NEW findings touching Q 17

- [[h-new-111-fr-roots-distance]] — full 114×114 distance matrix; Q 17 nearest neighbors above.
- [[h-new-590-outlier-spectrum]] — Q 17 NULL outlier window [14-20].
- [[h-new-700-phonological-compression-tail]] — Q 17 in plateau region.
- [[h-new-720-canonical-adjacency-cost]] — Q 16-17 rank 12; Q 17-18 cheap.
- [[h-new-750-ijaz-signature]] — Q 17 sig_A rank 111.
- [[h-new-840-unified-architectural-score]] — Q 17 UAS rank 10.
- [[h-new-660-compression-tail-gradient]] — Q 17 head-zone, plateau-conformant.
- [[h-new-770-verse-length-compression-tail]] — Q 17 14.8 words/verse, head-mathānī tier.
- [[cross-finding-026-ijaz-architecture]] — Q 17 anti-fawāṣil + pro-taḥaddī dual signature.
- [[Q017-F-01]], [[Q017-F-02]], [[Q017-F-03]], [[Q017-F-04]] — surah-local pre-registered findings, all VINDICATED.

## 12. Honest limits

- The classical name **Banū Isrāʾīl** is an internally-Quranic-content classification (Q017-F-04 vindicates the *content-density* basis); but it is also possible that Companions used the name simply because of v.4 *qaḍaynā ilā Banī Isrāʾīla* (the surah's narrative pivot). Both can be true; we have not separated them empirically.
- The 8 perfect-monorhyme surahs (Q 18, 48, 65, 72, 76, 87, 91, 92) all have **fewer than 31 verses**. Q 17 has 111 verses. **Sustaining 99.10% alif over 111 verses is mechanically harder than sustaining 100% over 12-31 verses.** A length-controlled rhyme-purity metric would likely promote Q 17 above the small-surah perfectionists. This is a follow-up test (Q017-F-05?) flagged but not pre-registered here.
- The *Subḥān* alternative name is rare in the classical tafsir we extracted (witnessed in Ibn Kathīr opening; absent from al-Suyūṭī's *al-Itqān*'s standard listing); flagged as a minor naming-tradition variant.
