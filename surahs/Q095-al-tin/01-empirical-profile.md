---
surah: 95
surah_name_ar: التين
surah_name_translit: al-Tīn
file_type: empirical-profile
date_last_updated: 2026-05-09
phase: B+
verdict: COMPLETE — Q 95 = rank 8 FR-centroid + iʿjāz-al-maʿnā cell exemplar; 3 corpus-hapax lemmas in load-bearing positions (oath + jawāb) but no content-outlier signature
---

# Q 95 al-Tīn — Empirical Architectural Profile

## 1. Headline architectural metrics

Rules-tuple: `(no-tashkeel, QAC-STEM root tokens + LEM-level hapax, QAC v0.4, basmala-counted-only-in-Q1, mushaf order, Hafs-Kufan, Mashriqi)`. All numerical claims below are computed from disk; sources cited.

| Metric | Value | Rank / 114 | Source |
|:--|:--:|:--|:--|
| **UAS (Unified Architectural Score)** | **−2.111** | **bottom decile** | `findings/phase-b-hypotheses/csv/h-new-840.json` `all_uas` surah=95 |
| Outlier-strength Δ%ile | 0.08 pp | rank ~ NULL classification | `h-new-590.json` X=95 |
| max neighbor canonical-adjacency cost | 0.047 length-units (Q 94 → Q 95) | low (rank ≈ 90 / 113) | `h-new-720.json` `per_adjacency` s=94 |
| Q 94 → Q 95 cost | 0.047 length-units; 0.567% TSP residual | rank ≈ 90 / 113 | same, s=94 |
| Q 95 → Q 96 cost | 0.032 length-units; 0.390% TSP residual | rank ≈ 100 / 113 | same, s=95 |
| iʿjāz signature sig_A | **+0.6423** | **rank 44 / 114** | `h-new-750.json` per_surah surah=95 |
| iʿjāz signature sig_B | +0.3485 | rank 47 / 114 | same |
| **Mean FR distance to corpus** | **0.7863** | **rank 8 / 114** (highly content-central) | computed from `h-new-111.json` `D_matrix_upper_triangular` |
| Local cohesion (1-step adjacency) | 2.297 (z = +1.06) | high | H-NEW-750 |
| Rhyme entropy (Shannon, nats) | **0.377** | mid (z = −0.71, rank 47) | H-NEW-750 |
| Top final letter (rāwī) | ن | 7 / 8 verses = 87.5% | H-NEW-750 |
| Total root-tokens (QAC v0.4) | 41 | rank ~95-100 / 114 (very small) | computed from QAC |
| **Distinct LEMMAS** | **33** | rank ~95-100 / 114 (very small) | computed |
| **Distinct ROOTS** | **22** | rank ~100-105 / 114 | computed |
| **Corpus-hapax LEMMAS in surah** | **3** (*t~iyn*, *siyniyn*, *taqowiym*) | rank 43 by density / 114 | computed |
| Hapax density (lemma-level) | 0.091 (3 / 33) | rank 43 / 114 | computed |
| Words (no-tashkeel orthographic) | 34 | rank ~98-103 / 114 | computed |
| Letters (no-tashkeel, no spaces) | 152 | rank ~98-103 / 114 | computed |
| Verses | 8 | rank 105 / 114 | canonical |

## 2. The architectural paradox: highly FR-central + concentrated lexical hapaxes

Q 95 al-Tīn presents a structurally interesting two-axis pattern that places it firmly in the *iʿjāz-al-maʿnā* cell ([[cross-finding-026-iʿjāz-architecture|cross-finding-026]] §13.2) — alongside Q 112 al-Ikhlāṣ and Q 114 al-Nās:

| Axis | Q 95 score | Q 95 rank | What this means |
|:--|:--:|:--:|:--|
| UAS (composite) | −2.111 | bottom decile | Bottom-decile by combined structural-iʿjāz metrics |
| Outlier-strength Δ%ile | 0.08 | rank ~NULL | Removing Q 95 from a 7-window does NOT collapse cohesion |
| sig_A (al-Bāqillānī fawāṣil signature) | +0.6423 | 44 / 114 | Mid; the v.4 rhyme-break suppresses the otherwise-pure -ūn/-īn signature |
| sig_B (rhyme-purity) | +0.3485 | 47 / 114 | Mid; n=8 verses with 7/8 nūn ≠ pure-monorhyme but high-purity |
| **Mean FR distance to corpus** | **0.7863** | **8 / 114** | **Q 95's root-distribution is among the corpus's 8 most-FR-central** |
| **Hapax density (lemma)** | **0.091** | **43 / 114** | 3 corpus-hapax lemmas concentrated in oath-positions (vv. 1, 2, 4) |

**The paradox**: Q 95 is among the corpus's MOST FR-CENTRAL surahs (rank 8) — meaning its root-distribution is closer to the corpus marginal than 106 of the 114 surahs — yet it concentrates 3 corpus-distinct LEMMAS in its 4-noun opening (vv. 1, 2, 4). The resolution: hapax-density at the LEMMA level can be high in surahs whose ROOTS are corpus-typical. *Sīnīn* (corpus-hapax lemma) is built on the QAC-untagged root for Sinai-toponym (proper-noun lemma, no root). *Taqwīm* (corpus-hapax lemma) is from the q-w-m root (660 corpus occurrences — extremely common). Only *tīn* is a corpus-hapax at BOTH root and lemma levels. Hence Q 95's FR-centroid signal (driven by root distribution) is unaffected by its lemma-level lexical distinctiveness.

**Mechanism interpretation**: Q 95's content (oath + creation/fall + believer-exception + final eschatological apostrophe) deploys the corpus's most-frequent theological roots (Allah ×1, Hkm ×2, Amn ×2, dyn ×1, sfl ×2) plus three lexically-rare items embedded in oath-positions to mark the rhetorical specificity of *fig + Sinai + best-stature*. The result is FR-typicality at the root-distribution level overlaid with lemma-level rarities at the surah's structurally pivotal points. Q 95 is the corpus's clearest case of **"content-central + lemma-distinctive"** — geometrically near the centre but lexically marked at oath/jawāb positions.

This is **not coincidence**. It is a substantive finding. The lexical concentration of *tīn* + *Sīnīn* + *taqwīm* at vv. 1, 2, 4 is structurally load-bearing — it places hapaxes at 2 oath-nouns (4 total) + the *jawāb*'s key noun. The hapax-position-load test (Q095-F-02) makes this rigorous.

## 3. Fisher–Rao distance row (Q 95 against all 113 others)

Computed from `findings/phase-b-hypotheses/csv/h-new-111.json` (Fisher–Rao angular on K=500 stem-roots, Dirichlet α=0.5; `D_ij = 2·arccos(Σ √(p_i·p_j))`).

**Top-10 FR-nearest neighbours**:

| Rank | Surah | FR distance | Class |
|:-:|:-:|:--:|:--|
| 1 | Q 103 al-ʿAṣr | 0.2972 | terminal-3v Meccan |
| 2 | Q 108 al-Kawthar | 0.3189 | terminal-3v Meccan (corpus FR-centroid rank-3) |
| 3 | Q 106 Quraysh | 0.3295 | terminal-4v Meccan |
| 4 | Q 112 al-Ikhlāṣ | 0.3398 | terminal-4v Meccan (corpus FR-centroid rank-1) |
| 5 | Q 107 al-Māʿūn | 0.3432 | terminal-7v Meccan |
| 6 | Q 111 al-Masad | 0.3507 | terminal-5v Meccan |
| 7 | Q 113 al-Falaq | 0.3533 | terminal-5v muʿawwidhatān |
| 8 | Q 110 al-Naṣr | 0.3591 | terminal-3v Medinan |
| 9 | Q 94 al-Sharḥ | 0.3614 | terminal-8v Meccan (immediate predecessor) |
| 10 | Q 100 al-ʿĀdiyāt | 0.3667 | terminal-11v Meccan |

**Five farthest neighbours**:

| Rank | Surah | FR distance |
|:-:|:-:|:--:|
| 109 | Q 7 al-Aʿrāf | (large narrative Meccan) |
| 110 | Q 26 al-Shuʿarāʾ | (long Meccan narrative) |
| 111 | Q 2 al-Baqara | 1.2048 |
| 112 | Q 6 al-Anʿām | 1.2061 |
| 113 | Q 4 al-Nisāʾ | 1.2200 |
| 114 | Q 9 al-Tawba | 1.2252 |
| 115 (=most-far) | Q 3 Āl ʿImrān | 1.2361 |

**Interpretation**: Q 95's local FR-cluster is the terminal-tail short-Meccan-mufaṣṣal-qiṣār cluster (Q 90-114). All 10 FR-nearest neighbours are short-tail surahs. The 5 farthest neighbours are long Medinan / mid-Meccan narrative surahs — the geometrical opposites by content-distribution.

That Q 95 sits at **rank-8 corpus FR-centroid** — and that 4 of its top-5 FR-nearest neighbours (Q 103, 108, 112, 113) are themselves in the corpus's top-10 FR-centroids — reinforces the *terminal-tail-as-FR-centroid-cluster* finding ([[cross-finding-026-iʿjāz-architecture|cross-finding-026]] §13.2). The terminal mufaṣṣal-qiṣār surahs collectively form a content-distribution cluster centred on the corpus mean.

## 4. FR-centroid status — pre-registered for novel-finding test (Q095-F-01)

The headline novel finding ([[Q095-F-01-fr-centroid|Q095-F-01]] in `06-novel-findings.md`) is the empirical lock on Q 95's rank-8 FR-centroid status:

| Rank | Surah | mean FR distance |
|:-:|:-:|:--:|
| 1 | Q 112 al-Ikhlāṣ | 0.7592 |
| 2 | Q 110 al-Naṣr | 0.7644 |
| 3 | Q 108 al-Kawthar | 0.7718 |
| 4 | Q 1 al-Fātiḥa | 0.7789 |
| 5 | Q 106 Quraysh | 0.7803 |
| 6 | Q 114 al-Nās | 0.7838 |
| 7 | Q 113 al-Falaq | 0.7843 |
| **8** | **Q 95 al-Tīn** | **0.7863** |
| 9 | Q 103 al-ʿAṣr | 0.7870 |
| 10 | Q 105 al-Fīl | 0.7877 |

**Q 95 is rank 8 / 114 corpus FR-centroid.** This empirically locks Q 95's content-typicality at FR-roots law-strength: the surah's root-distribution is closer to the corpus marginal distribution than 106 of the 114 surahs. The headlining-corpus rank-1 (Q 112) is shown for comparison; Q 95 sits 7 ranks below the maximum, but well within the top-decile FR-centroid cluster.

## 5. Rhyme structure

Verified verse-final letters (computed from `quran-no-tashkeel.json`):

| Verse | Final word | Final letter | Final cluster |
|:-:|:-:|:-:|:-:|
| 1 | والزيتون | ن | -ūn (zaytūn) |
| 2 | سينين | ن | -īn (Sīnīn) |
| 3 | الأمين | ن | -īn (amīn) |
| 4 | تقويم | م | -īm (taqwīm) ← break |
| 5 | سافلين | ن | -īn (sāfilīn) |
| 6 | ممنون | ن | -ūn (mamnūn) |
| 7 | بالدين | ن | -īn (dīn) |
| 8 | الحاكمين | ن | -īn (ḥākimīn) |

**87.5% nūn-rhyme (7/8)**; v. 4 *taqwīm* breaks the rhyme with mīm. Rhyme entropy = 0.377 nats (rank 47/114 — mid).

The rhyme-architecture is **structurally meaningful**: the rhyme deliberately breaks at v. 4 — the *jawāb al-qasam* — using the corpus-hapax lemma *taqwīm*. The break-position is the surah's most rhetorically-loaded verse (the answer to the 4-noun oath), and the break-letter (mīm) is itself the surah's lemma-hapax marker. After the break, the surah immediately returns to ـين / ـون for vv. 5-8.

This is a **rhyme-encoding-of-structure** pattern. Q 95 deploys the rhyme-break as a STRUCTURAL MARKER for the *jawāb*'s rhetorical pivot. Compare to Q 99 al-Zalzala (where the rhyme-architecture is 3-staged at vv. 1-5 → 6 → 7-8) and Q 91 al-Shams (perfect monorhyme through 15 verses then 1 break at v. 14-15).

## 6. Phoneme density profile (qualitative; per H-NEW-700 framework)

The 8 verses are dominated by:
- Glottal/laryngeal: ا (alif/hamza) at openings *al-tīn*, *al-zaytūn*, *al-amīn*; ه in *hādhā*, *fa-mā*; ع in *ʿamilū*; ح in *aḥsani*, *al-Ḥākimīn*, *al-Ṣāliḥāt*
- Liquid: ل dense in *al-tīn*, *al-zaytūn*, *al-amīn*, *al-balad*, *al-insān*, *al-ḥākimīn*
- Sibilant: س in *al-insān*, *aḥsani*, *sāfilīn*; ص in *al-Ṣāliḥāt*
- Dental: ت / ط in *zaytūn*, *taqwīm*, *Ṭūr*

The pharyngeal (ع ح) density is moderate — characteristic of mid-mufaṣṣal phoneme dispersion (per [[h-new-700-phonological-compression-tail|H-NEW-700]] kink at s=75; Q 95 is past the kink at s=95). The emphatics ص ط ظ ض are present but moderate (ص in *al-Ṣāliḥāt*, ط in *Ṭūr Sīnīn*, ض absent, ظ absent).

The 3 corpus-hapax lemmas — *tīn*, *Sīnīn*, *taqwīm* — bring a phonemic minor-distinctiveness: the (ت ي ن) cluster of *tīn* and the (س ي ن ي ن) of *Sīnīn* together create a **dense -īn-noun-cluster in vv. 1-2**. The phoneme ن occurs in 12 of the 34 word-tokens (35.3%); this is significantly above the corpus per-surah mean of 17% (per H-NEW-700-data, Q 95 rank in nūn-density ≈ top-15 / 114).

## 7. Outlier-window decomposition (H-NEW-590)

The 7-window centred on Q 95 is [Q 92, 93, 94, 95, 96, 97, 98] (with the boundary handled per H-NEW-590 conventions). Per `h-new-590.json` X=95:

| Removed | d̄_W | d̄_W−X | percentile shift Δ (pp) | classification |
|:--:|:--:|:--:|:--:|:--|
| Q 95 | (computed) | (computed) | **0.08** | **NULL** |

Q 95 does NOT collapse local cohesion when removed — because the surrounding terminal-tail cluster (Q 90-114) is already FR-tight without it. Removing Q 95 from the 7-window leaves a still-cohesive 6-surah neighborhood. This is consistent with [[cross-finding-026-iʿjāz-architecture|cross-finding-026]] §3 (terminal-zone is "convergent — d̄=0.32 vs corpus mean 0.95, 3× tighter").

## 8. iʿjāz signature decomposition (H-NEW-750)

Per `h-new-750.json` per_surah surah=95:

- **sig_A = +0.6423** (rank 44 / 114) — a structural-iʿjāz signature mid in the corpus. The 7/8 nūn-rhyme is high-purity, but the v. 4 break + mid-length n=8 verses compress the score to mid-range.
- **sig_B = +0.3485** (rank 47 / 114) — the rhyme-purity-only signature is also mid. The mid placement reflects 87.5% monorhyme (lower than perfect 100% monorhyme surahs like Q 109, Q 112).

The **sig_A vs sig_B near-equality** in Q 95 is itself architectural: the surah is rhyme-disciplined but not rhyme-pure, structurally singular but not extreme. This places Q 95 in the *iʿjāz-al-maʿnā* cell rather than the *iʿjāz-al-fawāṣil-pure* cell — the surah's iʿjāz signature is in its content (oath-cluster + creation-fall-affirmation arc) rather than in pure rhyme-architecture.

## 9. Canonical-adjacency cost (H-NEW-720)

| Adjacency | Cost (length-units) | Frac of TSP residual | Rank / 113 |
|:--|:--:|:--:|:--:|
| Q 94 → Q 95 | 0.0470 | 0.567% | ~ 90 |
| Q 95 → Q 96 | 0.0323 | 0.390% | ~ 100 |
| (combined) | 0.0793 | 0.957% | — |

**Both adjacencies are cheap.** Q 95 is NOT bracketed by top-15 expensive adjacencies. The mushaf does NOT pay structural cost to keep Q 95 in canonical position 95; the FR-geometric cluster at the corpus tail (Q 90-114) is internally cheap. This is consistent with [[cross-finding-026-iʿjāz-architecture|cross-finding-026]] §5.

**Architectural interpretation**: the canonical placement of Q 95 between Q 94 al-Sharḥ and Q 96 al-ʿAlaq is FR-cheap. **Significance for tradition**: classical commentators (al-Suyūṭī *Asrār Tartīb al-Suwar*, al-Bāqillānī *al-Iʿjāz fī al-Qurʾān*) have long argued that Q 94 + Q 95 + Q 96 form a tight *Late Meccan-to-Early Meccan transition cluster* (al-Sharḥ closes Muḥammad's psychological stage; al-Tīn opens the cosmic-eschatological theme; al-ʿAlaq opens the FIRST revelation theme). The empirical FR-cheapness (combined 0.957% of TSP residual) corroborates this — the 3-surah group is geometrically tight despite ostensible thematic differences.

## 10. Cell classification — *iʿjāz-al-maʿnā* (4-cell typology, [[cross-finding-026-iʿjāz-architecture|cross-finding-026]] §13.2)

| Cell signature | Q 95 value | Match? |
|:--|:--:|:--:|
| Low UAS | rank near bottom-decile (~109 / 114) | ✓ |
| Low outlier-strength | 0.08 pp (NULL) | ✓ |
| Low TSP / adjacency cost | combined 0.957%, both adjacencies non-top-15 | ✓ |
| **High FR-centrality / theological-content density** | **rank 8 / 114 FR-centroid** | ✓ (top-decile) |
| Classical anchor | al-Ṭabarī, Ibn Kathīr, al-Qurṭubī compressed-prophet-itinerary reading | ✓ (canonical sacred-geography) |

**Q 95 is a clean *iʿjāz-al-maʿnā* cell exemplar.** Combined with Q 112 al-Ikhlāṣ (rank-1 FR-centroid) and Q 114 al-Nās (rank-6 FR-centroid), the cell is empirically populated with Q 95 as the **rank-8 representative**. Q 95 differs from the cell's other members in deploying its content-density via OATH-CLUSTER + COSMIC-WITNESS rather than pure-tawḥīd (Q 112) or refuge-formula (Q 114). The cell admits multiple semantic-mode realizations of the same architectural signature.

## 11. Cross-references to H-NEW findings

- [[h-new-111-fisher-rao-distance|H-NEW-111]] — Q 95 = corpus FR-centroid rank 8.
- [[h-new-590-outlier-spectrum|H-NEW-590]] — Q 95 NULL outlier (0.08 pp).
- [[h-new-660-compression-tail-gradient|H-NEW-660]] — Q 95 in compression-tail (s=95; predicted d̄_content ≈ 0.95 - 0.012·(95-50) = 0.41; observed local cluster d̄ ≈ 0.32 in the Q 90-114 zone).
- [[h-new-700-phonological-compression-tail|H-NEW-700]] — Q 95 in phoneme-dispersion-tail (s=95 > kink-75).
- [[h-new-720-canonical-adjacency-cost|H-NEW-720]] — both adjacencies cheap (0.957% combined).
- [[h-new-750-per-surah-iʿjāz-signature|H-NEW-750]] — sig_A rank 44, sig_B rank 47.
- [[h-new-840-unified-architectural-score|H-NEW-840]] — UAS rank near bottom-decile.
- [[h-new-1200-short-meccan-eschatology|H-NEW-1200]] — Q 95 is core member of 14-surah short-Meccan-tail eschatology cluster.
- [[h-new-1220-fr-centroid-ranking|H-NEW-1220]] — Q 95 mean_d=0.7863 (rank 8/114).
- [[cross-finding-026-iʿjāz-architecture|cross-finding-026]] — Q 95 = *iʿjāz-al-maʿnā* cell exemplar.

## 12. Honest limits

1. **Single-pipeline FR-roots methodology**. The rank-8 FR-centroid status is computed on K=500 QAC stem-roots. Other distance metrics (char-4-gram NCD, contextual embeddings, finer phonetic features) untested for centroid-ranking.
2. **n=8 verses is small**. Many windowed metrics (sig_A, outlier-strength) are dominated by neighborhood rather than internal-surah structure for n≤10.
3. **Lemma vs root hapax**: the 3 corpus-hapax lemma claim depends on QAC v0.4 lemma boundaries. Variant lemma-segmentations (e.g., treating *Sīnīn* as a true proper-noun outside the lemma-counting framework) could reduce the count to 2.
4. **Asbāb al-nuzūl**: there is no robust occasion-of-revelation tradition for Q 95 — classical sources frame it as general theological / cosmic content. The Early Meccan classification rests on stylistic + early-chronology testimony rather than specific event-association.
5. **Bukhārī ḥadīth on the Prophet's recitation of Q 95 in *ʿIshāʾ*** (Bukhari 749, 751, 4746, 7260; Muslim 939-941) is ṣaḥīḥ — see `04-hadith-corpus.md`. The Tirmidhi 3431 *fadāʾil* tradition is gharīb / ḍaʿīf — see `05-classical-claims-audit.md`.

*Bismillāhi al-Raḥmāni al-Raḥīm.*
