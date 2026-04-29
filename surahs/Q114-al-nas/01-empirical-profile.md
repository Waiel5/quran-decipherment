---
surah: 114
surah_name_ar: الناس
surah_name_translit: al-Nās
file_type: empirical-profile
date_last_updated: 2026-04-28
phase: B+
verdict: COMPLETE — all H-NEW metrics integrated; iʿjāz-al-maʿnā cell co-member
---

# Q 114 al-Nās — Empirical Architectural Profile

## 1. Headline metrics

Rules-tuple: `(no-tashkeel, QAC-stem, K500, Hafs-Kufan, Mashriqi, basmala-counted-only-in-Q1)`. All values computed from disk; sources cited.

| Metric | Value | Rank / 114 | Source |
|:--|:--:|:--:|:--|
| **UAS** | −2.7968 | **113 / 114** (rank-2 lowest in corpus) | `h-new-840.json` |
| Outlier-strength Δ%ile | 0.00 (NULL) | 46 / 114 | `h-new-590.json` |
| Q 113 → Q 114 adjacency cost | 0.0623 (0.75%) | 56 / 113 | `h-new-720.json` |
| iʿjāz signature sig_A | −0.0152 | 60 / 114 | `h-new-750.json` per_surah |
| iʿjāz signature sig_B | +1.2302 | 21 / 114 (top quintile) | same |
| **Mean FR distance to corpus** | **0.7838** | **6 / 114** (FR-centroid top decile) | `h-new-111.json` |
| Local cohesion | 3.4459 | high | `h-new-750.json` |
| Rhyme entropy (nats) | 0.000 | tied at 0 (100% س monorhyme) | same |
| Top final letter | س | 100% | computed |
| Total root-tokens | 15 | bottom-decile | `morphology` |
| Distinct roots | 10 | bottom-decile | same |
| Words (no-tashkeel) | 20 | bottom-decile | computed |
| Letters (no-tashkeel) | 80 | bottom-decile | same |
| Verses | 6 | bottom-15 | canonical |

## 2. Architectural cell: *iʿjāz-al-maʿnā* (co-member with Q 112)

| Cell criterion | Q 114 value | Match? |
|:--|:--:|:-:|
| Low UAS | rank 113 / 114 | ✓ (corpus rank-2 lowest) |
| Low outlier-strength | 0.00 (NULL) | ✓ |
| Low TSP / adjacency cost | combined 0.75%, non-top-15 | ✓ |
| **High FR-centrality / theological-content density** | **rank 6 / 114** | ✓ (top decile) |
| Classical anchor | al-Bukhārī #4439 muʿawwidhatān + #5017 hand-blowing | ✓ |

**Q 114 is the second member** of the *iʿjāz-al-maʿnā* cell (Q 112 is the rank-1 exemplar). Q 114 has FR-centrality top decile (rank 6) but does NOT achieve Q 112's rank-1 status. The cell-membership is empirically supported.

## 3. FR-distance neighbours

**Five nearest neighbours**:

| Rank | Surah | FR distance |
|:-:|:-:|:--:|
| 1 | **Q 113 al-Falaq** | **0.2718** |
| 2 | Q 108 al-Kawthar | 0.2862 |
| 3 | Q 110 al-Naṣr | 0.3001 |
| 4 | Q 112 al-Ikhlāṣ | 0.3086 |
| 5 | Q 94 al-Sharḥ | 0.3194 |

Q 114's **#1-nearest neighbour is Q 113 al-Falaq**. The pair is FR-asymmetrically tight: Q 114 → Q 113 = #1, while Q 113 → Q 114 = #2 (Q 113's #1 is Q 108).

This **asymmetric FR-tightness** is the empirical signature of the muʿawwidhatān-pair: Q 114 is "more dependent" on Q 113 than Q 113 is on Q 114, in FR-roots geometric terms.

## 4. FR-centroid status

Mean FR distance = 0.7838, **rank 6/114**. Top decile but not corpus-extreme (Q 112 holds rank 1 at 0.7592).

## 5. Rhyme structure

100% س monorhyme via massive *al-nās* repetition (5/6 verses end with *al-nās*; 6th ends with *al-khannās*).

Rhyme entropy = 0.000 nats (corpus-min, tied with all 100%-monorhyme surahs).

The lexical-repetition mechanism for the monorhyme is corpus-extreme: *al-nās* appears 6 times in 6 verses (4 verse-finals as *al-nās*, 1 verse-final as *al-khannās* sharing سname-suffix; 5/6 in *fī ṣudūri l-nās* and verse-2 *maliki l-nās*, etc.).

## 6. Phoneme density

Q 114's phonemic profile features:
- Sibilant: س extremely dense (every verse-final + internal positions)
- Nasal: ن in *al-nās* repetitions
- Glottal: ا in *al-nās*, *aʿūdhu*

The 6× *al-nās* repetition (root nws attested 5×) is the highest single-root token-density in the corpus tail.

## 7. Outlier-window decomposition (H-NEW-590)
Q 114 NULL outlier (Δ%=0.00, rank 46). Removing Q 114 does NOT collapse local cohesion in the terminal-window.

## 8. iʿjāz signature decomposition

- **sig_A = −0.0152, rank 60/114** — corpus-mid. The 100% monorhyme would push high but n=6 verses + corpus-mean-distance components compress sig_A to mid-corpus.
- **sig_B = +1.2302, rank 21/114** — top quintile rhyme-purity signature.

The sig_A vs sig_B divergence (mid sig_A, high sig_B) places Q 114 in a similar profile to Q 112 (mid sig_A, high sig_B): both are **rhyme-pure but not structurally singular** by sig_A.

## 9. Canonical-adjacency cost (H-NEW-720)

| Adjacency | Cost (length-units) | Frac of TSP residual | Rank / 113 |
|:--|:--:|:--:|:--:|
| Q 113 → Q 114 | 0.0623 | 0.75% | 56 |
| (Q 114 has no following surah; corpus terminus) | — | — | — |

The single Q 113-Q 114 adjacency is mid (rank 56/113), non-top-15. The pair is structurally cheap.

## 10. Cross-references to H-NEW findings

- [[h-new-111-fisher-rao-distance|H-NEW-111]] — FR-centroid rank 6; nearest = Q 113.
- [[h-new-590-outlier-spectrum|H-NEW-590]] — NULL outlier.
- [[h-new-660-compression-tail-gradient|H-NEW-660]] — terminal compression-tail.
- [[h-new-700-phonological-compression-tail|H-NEW-700]] — phoneme-dispersion-tail.
- [[h-new-720-canonical-adjacency-cost|H-NEW-720]] — Q 113-Q 114 mid; pair FR-cheap.
- [[h-new-750-per-surah-iʿjāz-signature|H-NEW-750]] — sig_A rank 60, sig_B rank 21.
- [[h-new-840-unified-architectural-score|H-NEW-840]] — UAS rank 113.
- [[cross-finding-026-iʿjāz-architecture|cross-finding-026]] §13.2 — *iʿjāz-al-maʿnā* cell.

## 11. Honest limits

1. Q 114 is the corpus's second-lowest UAS (rank 113); only Q 87 al-Aʿlā has lower UAS. The low UAS is consistent with the *iʿjāz-al-maʿnā* cell's "structurally invisible" signature.
2. The 100% monorhyme via lexical-repetition is structurally distinct from Q 112's monorhyme via rhyme-cluster (-aḥad/-ṣamad/-yūlad/-aḥad). The mechanism differs: Q 114 = repetition-driven; Q 112 = rhyme-cluster-driven.
3. The Ibn Masʿūd muṣḥaf-omission tradition is doctrinally sensitive; chain-quality summary in `05-classical-claims-audit.md` Claim 3.

*Bismillāhi al-Raḥmāni al-Raḥīm.*
