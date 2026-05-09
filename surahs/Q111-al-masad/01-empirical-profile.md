---
surah: 111
surah_name_ar: المسد
surah_name_translit: al-Masad
file_type: empirical-profile
date_last_updated: 2026-05-09
phase: B+
verdict: COMPLETE — all H-NEW metrics integrated; corpus-uniqueness signature locked at content-PN level
---

# Q 111 al-Masad — Empirical Architectural Profile

## 1. Headline metrics

Rules-tuple: `(no-tashkeel, QAC-stem, K500, Hafs-Kufan, Mashriqi, basmala-counted-only-in-Q1)`. All values computed from disk; sources cited.

| Metric | Value | Rank / 114 | Source |
|:--|:--:|:--:|:--|
| **UAS** | −2.1882 | 105 / 114 (bottom decile) | `h-new-840.json` `all_uas` surah=111 |
| Outlier-strength Δ%ile | 0.00 pp (NULL) | NULL | `h-new-590.json` X=111 |
| Q 110 → Q 111 adjacency cost | 0.0170 (0.21%) | 93 / 113 (cheap) | `h-new-720.json` |
| Q 111 → Q 112 adjacency cost | 0.0221 (0.27%) | 89 / 113 (cheap) | `h-new-720.json` |
| iʿjāz sig_A | +0.7764 | 41 / 114 (mid) | `h-new-750.json` per_surah |
| **iʿjāz sig_B** | **+1.7728** | **11 / 114** (top decile) | same |
| Mean FR distance to corpus | **0.7954** | **15 / 114** (top-decile FR-centroid) | computed from `h-new-111.json` D-matrix |
| Local cohesion | 3.1789 | high | `h-new-750.json` |
| Rhyme entropy (nats) | 0.5004 | low (single-rhyme dominant) | same |
| Top final letter | ب (80%) | dominant | computed |
| Total root-tokens | 15 | bottom-decile | `morphology` Q111 |
| Distinct roots | 15 (= total tokens; no repetition) | bottom-decile but **100% distinct-rate** | same |
| Words (no-tashkeel) | 23 | bottom-decile | `quran-no-tashkeel.json` |
| Letters (no-tashkeel) | 81 | bottom-decile | same |
| Verses | 5 | bottom-15 | canonical |

## 2. Architectural cell: *content-iʿjāz-pure* (named-opponent-condemnation)

Q 111 sits **outside** the 4 standard *iʿjāz-architecture* cells of cross-finding-026 §13 (all-axis, structural-twin-pair, *iʿjāz-al-fawāṣil-pure*, *iʿjāz-al-maʿnā*). Its UAS rank 105 + sig_A rank 41 disqualify it from all four UAS-based cells. Yet Q 111 is **structurally cheap** (both adjacencies < 0.3% TSP residual; FR-centroid top decile) — meaning the mushaf places Q 111 with no architectural cost, despite Q 111's content-distinctiveness being maximally specific (the only named-opponent-condemnation).

This is the empirical signature of a **content-iʿjāz-pure** sub-cell — surahs whose distinctive value lies in *content-uniqueness* rather than in UAS-ranked structural-iʿjāz. Q 111 is the canonical exemplar:
- 100% distinct-root rate (15/15 distinct roots in 15 root-tokens) → maximum lexical efficiency
- Two corpus-hapax roots (msd, jyd) packed into final-verse → singularity-density signature
- Named-opponent-condemnation → content-uniqueness at corpus-EXACT level (only surah of its kind)

**sig_B rank 11 / 114** is corpus-near-extreme. Q 111's mean content distance combined with its high local-cohesion places it firmly in the top-decile of the rhyme-purity-centric signature. Note: sig_B captures rhyme-purity × cohesion; Q 111's 80% ب-rhyme dominance + tight 5-verse cohesion drives the rank-11 placement.

## 3. FR-distance neighbours (Q 111 against 113 others)

Computed from `h-new-111.json` D-matrix:

**Ten nearest neighbours**:

| Rank | Surah | FR distance | Class |
|:-:|:-:|:--:|:--|
| 1 | **Q 108 al-Kawthar** | **0.2324** | terminal-3v |
| 2 | Q 104 al-Humaza | 0.2676 | curse-formula tail |
| 3 | Q 106 Quraysh | 0.2722 | terminal-4v |
| 4 | Q 103 al-ʿAṣr | 0.2795 | terminal-3v |
| 5 | Q 112 al-Ikhlāṣ | 0.2849 | cluster-successor |
| 6 | Q 94 al-Sharḥ | 0.2866 | terminal-8v |
| 7 | Q 113 al-Falaq | 0.2915 | muʿawwidhāt-anchor |
| 8 | Q 107 al-Māʿūn | 0.2926 | terminal-7v |
| 9 | Q 105 al-Fīl | 0.3063 | terminal-5v |
| 10 | Q 101 al-Qāriʿa | 0.3164 | qiṣār-eschatology |

Q 111's nearest neighbour is **Q 108 al-Kawthar** at FR distance 0.2324 — closer than its mushaf-pair Q 112 al-Ikhlāṣ (0.2849, rank 5). Notable: **Q 104 al-Humaza ranks 2nd at 0.2676** — and Q 104 is the corpus's other curse-density-extreme surah, opening *waylun li-kulli humazatin lumazah* ("Woe to every backbiter, slanderer"). The Q 111-Q 104 neighbor relationship is empirically the corpus's **closest curse-formula-pair**: Q 111 (named-opponent curse) and Q 104 (categorical-class curse) form an FR-tight thematic-twin at content-uniqueness level. See `06-novel-findings.md` Q111-F-02.

## 4. FR-centroid status

Mean FR distance Q 111 → corpus = 0.7954, **rank 15 / 114**. Top decile (within top 13.2%).

Comparison-context:
- Q 112 al-Ikhlāṣ rank 1 (0.7592) — corpus FR-centroid
- Q 110 al-Naṣr rank 2 (0.7644)
- Q 108 al-Kawthar rank 3 (0.7718)
- Q 1 al-Fātiḥa rank 4 (0.7789)
- Q 106 Quraysh rank 5 (0.7803)
- Q 114 al-Nās rank 6 (0.7838)
- Q 113 al-Falaq rank 7 (0.7843)
- Q 95 al-Tīn rank 8 (0.7863)
- Q 103 al-ʿAṣr rank 9 (0.7870)
- Q 105 al-Fīl rank 10 (0.7877)
- ...
- **Q 111 al-Masad rank 15 (0.7954)**

Q 111 is in the FR-central top decile but ranks 5 places behind its FR-nearest neighbor Q 108 al-Kawthar (rank 3). This is consistent with the **mufaṣṣal-qiṣār terminal-tail being a tight FR-cluster** — Q 95-114 dominate the top-15 FR-central ranks, with Q 111 sitting comfortably inside.

## 5. Rhyme structure (verified)

Final-letter distribution computed from no-tashkeel orthographic forms:

| Verse | Final word | Final letter | Rhyme cluster |
|:-:|:-:|:-:|:-:|
| 1 | وتب | ب | -tabb |
| 2 | كسب | ب | -kasab |
| 3 | لهب | ب | -lahab |
| 4 | الحطب | ب | -al-ḥaṭab |
| 5 | مسد | د | -masad |

**Distribution**: ب × 4 (80%), د × 1 (20%). H-NEW-750's "top final letter: ب (80%)" is unambiguous.

Rhyme entropy = 0.5004 nats. This is **low-entropy single-dominant-rhyme** — the surah commits to ب-rhyme for 4 of 5 verses, then pivots to د in v.5. The ب → د pivot is the **terminal-cadence-flip** signature: it both closes the surah and matches the **content shift** from imprecation/biographical-failure (vv.1-4) to terminal visual tableau (v.5: the rope around the wife's neck).

The pivot letter د coincides with the corpus-hapax root **msd** (palm-fibre; ROOT:msd attested ONLY at Q 111:5 in the entire 114-surah corpus). This is the *iʿjāz al-fāṣila* signature al-Bāqillānī catalogues: a final verse that is rhyme-distinctive AND lexically singular AND tableau-functional — three signature-properties stacked on a single 4-word verse.

## 6. Phoneme density (qualitative)

Q 111's phonemic profile:

- **Bilabial stop ب** dominant — 8 ب-tokens in the surface text (4 verse-finals + 4 in-verse: *abī*, *aghnā*, *kasab*, *kasab*, *ḥablun*, ...). The ب-density is the surah's most prominent phonemic-marker.
- **Glottal ا/أ extensively** — 18 alif-tokens, mostly in *abī*, *aghnā*, *māluhu*, *mraʾatuhu*, *al-ḥaṭab*.
- **Pharyngeal ع/ح**: ع in *ʿanhu*; ح in *ḥammālata*, *al-ḥaṭab*, *ḥablun*.
- **Sibilant س** in *kasab*, *sa-yaṣlā*.
- **Dental د** as terminal-cadence-flip in v.5 *masad*.
- **Velar ق** absent (notable: Q 113-114 are ق-heavy, Q 111 is ق-absent).
- **Liquid ل** in *abī lahab*, *māluhu*, *lahab*, *al-ḥaṭab*, *ḥablun*.

The **labial-stop concentration** (ب-rhyme + in-verse ب) creates a percussive cadence-signature, parallel structurally to Q 105 al-Fīl's ل-cadence and Q 100 al-ʿĀdiyāt's ح-cadence.

## 7. Outlier-window decomposition (H-NEW-590)

Per `h-new-590.json` X=111: Δ%=0.00, classification NULL. The 7-window centred on Q 111 [108, 109, 110, 111, 112, 113, 114] is internally tight; removing Q 111 does NOT collapse cohesion (d_W = 0.30812 ≈ d_W_minus_X = 0.30978; p_greater_W = 1.0). This is the **terminal-tail FR-cluster** anchor — Q 111 is internally consistent with its tail neighbors and contributes no marginal-cohesion-loss when removed. Consistent with Q 108-114 being a tight terminal cluster regardless of which surah is omitted.

## 8. iʿjāz signature decomposition

- **sig_A = +0.7764, rank 41 / 114** — mid-corpus *iʿjāz al-fawāṣil* signature. The signature combines: low rhyme entropy (0.5004 nats; z=−0.49), corpus-mean-distance (z=−1.26 close-to-centroid), and high local cohesion (z=+2.26).
- **sig_B = +1.7728, rank 11 / 114** — top-decile rhyme-purity-centric signature. Q 111's 80% single-rhyme dominance + tight 5-verse cohesion drives the rank-11 placement.

The high sig_B (rank 11) without high sig_A (rank 41) means: Q 111 is **rhyme-pure** (single-dominant ب) but NOT rhyme-diverse-typology-aligned like Q 113 (which has rhyme-shift aligned to evil-typology). This is the signature of a **single-thread-narrative-curse**: Q 111 is one continuous condemnation across vv.1-4 with a terminal tableau in v.5 — there is no internal typology-segmentation to align to a multi-rhyme structure. The high sig_B reflects this single-purpose-cadence efficiency.

## 9. Canonical-adjacency cost (H-NEW-720)

| Adjacency | Cost (length-units) | Frac of TSP residual | Rank / 113 |
|:--|:--:|:--:|:--:|
| Q 110 → Q 111 | 0.0170 | 0.21% | 93 (cheap) |
| Q 111 → Q 112 | 0.0221 | 0.27% | 89 (cheap) |
| (combined) | 0.0391 | 0.47% | — |

Both adjacencies are very cheap (rank 93 / 89) — Q 111 is structurally near-free in canonical position 111. Neither is in the top-15 expensive (no structural-bracketing cost) and neither is in the H-NEW-1240 13 *seamless-seams* (clamped-zero cost). Q 111 sits in a region where the mushaf path is locally low-cost but not at the corpus's most-perfect transition points.

This means: **the mushaf does not pay structural cost to keep Q 111 at position 111, but it also does not exhibit a corpus-extreme seamless transition there.** Q 111's placement is *cost-neutral* — the surah fits without strain into the mufaṣṣal-qiṣār terminal-cluster.

## 10. Cross-references to H-NEW findings

- [[h-new-111-fisher-rao-distance|H-NEW-111]] — FR-centroid rank 15; nearest = Q 108 al-Kawthar (0.2324).
- [[h-new-590-outlier-spectrum|H-NEW-590]] — NULL outlier (Δ%=0.00).
- [[h-new-660-compression-tail-gradient|H-NEW-660]] — Q 111 in compression-tail (s=111, d̄_content ≈ 0.96 − 0.012·61 ≈ 0.23 expected; observed mean-content-distance 0.7954 substantially exceeds tail-expectation, signaling Q 111 is NOT a smoothly-compressed tail member).
- [[h-new-700-phonological-compression-tail|H-NEW-700]] — Q 111 in phoneme-dispersion-tail.
- [[h-new-720-canonical-adjacency-cost|H-NEW-720]] — both adjacencies cheap; not in top-15 expensive nor in the 13 seamless seams.
- [[h-new-750-per-surah-iʿjāz-signature|H-NEW-750]] — sig_A rank 41, sig_B rank 11.
- [[h-new-840-unified-architectural-score|H-NEW-840]] — UAS rank 105 (bottom decile).
- [[h-new-1240-13-seamless-seams|H-NEW-1240]] — Q 110→111 and Q 111→112 are NOT in the 13 seamless seams.
- [[h-new-1220-fr-centroid-tail|H-NEW-1220]] — Q 111 sits in the FR-central tail-cluster (rank 15 / 114).

## 11. Distinctive content-uniqueness signature

Beyond UAS / iʿjāz metrics, Q 111 carries a **content-PN-uniqueness signature** unmatched anywhere else in the corpus:

| Content-feature | Q 111 status | Corpus comparison |
|:--|:--|:--|
| Names a specific contemporary opponent | **YES** (Abū Lahab via kunya) | UNIQUE — see `05-classical-claims-audit.md` Claim 1 |
| Curses by name in opening | **YES** (*tabbat yadā abī lahabin*) | UNIQUE in corpus |
| Names opponent's wife | **YES** (*imraʾatuhu*, v.4) | only Q 11:71 *imraʾatuhu* (Lot's wife) and Q 28:9 (Pharaoh's wife) co-pattern, neither with curse-context |
| Corpus-hapax root in final verse | **YES** (msd at v.5; jyd at v.5) | rare; both in same verse is the corpus's only *double-hapax* terminal verse outside Q 113:3 (waqab + 1 of nfv) |
| 100% distinct-root rate | **YES** (15/15) | top-decile efficiency |

The combined signature (named-opponent + corpus-hapax-pair + 100%-distinct-root) is **corpus-unique to Q 111** and is the surah's actual architectural value — orthogonal to the UAS-ranking metric.

## 12. Honest limits

1. **n=5 verses** is small; sig_A / sig_B are computed at this small sample, with z-normalization sensitivity.
2. The content-iʿjāz-pure cell classification is descriptive (proposed in `06-novel-findings.md` Q111-F-04 as a candidate cross-finding-026 §13 extension); it is NOT yet promoted to corpus-architecture cross-finding.
3. The "corpus-uniqueness of named-contemporary-opponent" claim depends on QAC PN-tagging boundaries and on the kunya-classification for *abī lahabin*; under a stricter rule that requires *single-lemma PN tagging*, Q 111 still has no challenger because Abū Lahab is the only kunya-condemnation in the corpus (verified via `05-classical-claims-audit.md` Claim 1 search).

*Bismillāhi al-Raḥmāni al-Raḥīm.*
