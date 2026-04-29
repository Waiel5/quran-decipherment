---
surah: 18
surah_name_ar: الكهف
surah_name_translit: al-Kahf
file_type: empirical-profile
date_last_updated: 2026-04-28
phase: B+
verdict: COMPLETE
---

# Q 18 al-Kahf — Empirical Architectural Profile

## 1. Headline architectural metrics

Rules-tuple: `(no-tashkeel, QAC-STEM root tokens, QAC v0.4, basmala-counted-only-in-Q1, mushaf order, Hafs-Kufan)`. All numerical claims below are computed from disk; sources cited.

| Metric | Value | Rank / corpus context | Source |
|:--|:--:|:--|:--|
| **UAS (Unified Architectural Score)** | **0.0456** | **rank 46 / 114** (mid; not top-decile) | `findings/phase-b-hypotheses/csv/h-new-840.json` `all_uas[surah=18]` |
| Outlier-strength Δ%ile | **+0.39 pp** | rank 31 / 114; **WEAK_OUTLIER** | `h-new-590.json` `all_surahs_results[X=18]` |
| max neighbor canonical-adjacency cost | **0.0279** length-units | rank 86 / 113 (Q 17 → Q 18) | `h-new-720.json` `per_adjacency` |
| Q 17 → Q 18 cost | 0.0279 | rank 86 / 113 (CHEAP) | same |
| Q 18 → Q 19 cost | **0.0193** | rank 92 / 113 (CHEAPEST third) | same |
| iʿjāz signature sig_A (structural-fawāṣil) | **−2.3950** | **rank 110 / 114** (5th-from-bottom; extreme anti-iʿjāz) | `h-new-750.json` `per_surah[surah=18]` |
| iʿjāz signature sig_B (rhyme-purity inverse) | **−1.9222** | **rank 110 / 114** | same |
| Mean Fisher–Rao distance to corpus | **1.0344** | **rank 19 / 114** (high content-distance; corpus mean = 0.9235) | `h-new-111.json` D_matrix (computed) |
| Local cohesion (1-step adjacency) | 1.0616 | z = −0.622 | H-NEW-750 |
| Rhyme entropy (Shannon, nats) | **0.0518** | **rank 113 / 114** (second-lowest) | H-NEW-750; cross-validated below |
| Top final letter (rāwī) | **ا (alif)** | **0.9909 = 109 of 110 verses** | H-NEW-750; cross-validated |
| Total root-tokens | **1,057** | **rank 12 / 114** (high) | `data/morphology/quranic-corpus-morphology-0.4.txt` (computed) |
| Distinct roots | 369 | high — typical for late-Meccan multi-narrative | same |
| Words (no-tashkeel orthographic, mushaf-stripped) | **1,583** | mid-Meccan-large | computed `quran-no-tashkeel.json` |
| Letters (no-tashkeel, no spaces, mushaf-stripped) | **6,552** | mid-Meccan-large | same |
| Verse count | 110 | Hafs-Kufan | `data/hafs-verse-counts.tsv` |

**Source files**: all H-NEW JSON files referenced live in `/Users/grey/Downloads/quran/findings/phase-b-hypotheses/csv/`; the morphology file is `/Users/grey/Downloads/quran/data/morphology/quranic-corpus-morphology-0.4.txt`.

## 2. The architectural paradox: ANTI-IʿJĀZ AL-FAWĀṢIL with HIGH CONTENT-DISTANCE and LOW NEIGHBOR-COST

Q 18 occupies a distinctive cell in the project's three-axis architecture map:

| Axis | Q 18 score | Q 18 rank | What this means |
|:--|:--:|:--:|:--|
| Outlier-strength (Δ%ile in 7-window) | +0.39 pp | 31 / 114 | Q 18's content fits its window {15-21}; removing it barely changes window cohesion |
| Canonical-adjacency cost (max-of-2 sides) | 0.0279 (rank 86/113) | low | Q 17 al-Isrāʾ and Q 19 Maryam are content-near to Q 18; mushaf "pays nothing" to insert Q 18 |
| iʿjāz signature sig_A (al-Bāqillānī fawāṣil) | **−2.395** | **rank 110 / 114** | Extreme anti-structural-iʿjāz: rhyme is 99% alif (entropy 0.05 nats vs corpus ~0.7); content-distance is HIGH (1.03 vs corpus 0.92) — the hallmark anti-iʿjāz combination |
| Mean FR distance to corpus | **1.0344** | **rank 19 / 114** | Q 18's root-distribution is far from corpus centroid; the four-narrative arc gives it a content-signature distinct from typical surahs |

This makes Q 18 **the corpus's clearest case of "high content-distance + low canonical-adjacency cost + extreme single-rāwī"**. Q 18 fits *cheaply* between its neighbors despite being content-distinct — because its content-distinctness is in the *narrative-arc* dimension (4 stories), and its neighbors Q 17 and Q 19 are also prophet-narrative-anchored Meccan-mid surahs. By contrast, Q 24 al-Nūr's content-distinctness is in the *register* dimension (Medinan-legal) and its neighbors are register-mismatched, hence the bracketing cost.

Q 18's UAS rank (46/114) is *mid-corpus* because the three UAS components partly cancel: high content-distance (boosts UAS via the FR component), but extreme negative sig_A (depresses UAS via |sig_A|; H-NEW-840 takes the absolute value, so sig_A=-2.395 contributes 2.395 to UAS — but H-NEW-840 also weights against high *|outlier|*; Q 18's near-zero outlier (+0.39 pp) provides little). Concretely, Q 18 UAS = |0.39| + 0.0279 + |-2.395| ≈ 2.81 in the raw-component sum; the z-normalized UAS reported in H-NEW-840 is 0.046.

## 3. The bracketing-cost claim — INVERTED for Q 18

Per `h-new-720.json`, the 113 canonical-adjacency costs are sorted. Q 18's two adjacencies:

| Adjacency | Cost | Frac of TSP residual | Rank |
|:--|:--:|:--:|:--:|
| Q 17 → Q 18 | 0.0279 | 0.34% | 86 / 113 |
| Q 18 → Q 19 | 0.0193 | 0.23% | **92 / 113** |

**Both adjacencies are in the cheap third.** Combined cost: 0.0472 length-units = 0.57% of the 8.29-unit TSP residual. Q 18 is the **structurally most "in-place" surah of its register-class** — both Q 17 al-Isrāʾ and Q 19 Maryam are Meccan-prophet-anchored, sharing register with Q 18's prophet-narrative core (vv. 60-82 Mūsā-Khaḍir).

This is the precise *opposite* of Q 24's bracketing-cost geometry. Q 24 has both adjacencies in the top-15 expensive (combined 6% of residual); Q 18 has both in the bottom-third (combined 0.57%). The two surahs occupy opposite cells in the *register-fits-position* axis.

## 4. Fisher–Rao distance row (Q 18 against all 113 others)

Computed from `findings/phase-b-hypotheses/csv/h-new-111.json` `D_matrix_upper_triangular` (Fisher–Rao angular on K=500 stem-roots, Dirichlet smoothing α=0.5; `D_ij = 2·arccos(Σ √(p_i·p_j))`).

**Five nearest neighbours** (Q 18's root-distribution maps to the late-Meccan prophet-narrative cluster):

| Rank | Surah | FR distance | Class |
|:-:|:-:|:--:|:--|
| 1 | **Q 7 al-Aʿrāf** | **0.8709** | Meccan-large prophet-narrative (Mūsā/Pharaoh) |
| 2 | Q 25 al-Furqān | 0.8789 | Meccan-mid prophet-narrative |
| 3 | Q 28 al-Qaṣaṣ | 0.8794 | Meccan-mid prophet-narrative (Mūsā) |
| 4 | Q 41 Fuṣṣilat | 0.8848 | Meccan-mid (ḥā-mīm) |
| 5 | Q 23 al-Muʾminūn | 0.8895 | Meccan-mid prophet-doxology |

**Five farthest neighbours**:

| Rank | Surah | FR distance |
|:-:|:-:|:--:|
| 109 | Q 88 al-Ghāshiya | 1.1441 |
| 110 | Q 77 al-Mursalāt | 1.1564 |
| 111 | Q 80 ʿAbasa | 1.1649 |
| 112 | Q 56 al-Wāqiʿa | 1.1878 |
| 113 | **Q 55 al-Raḥmān** | **1.2711** |

**Interpretation**: Q 18's nearest five neighbours are ALL prophet-narrative or prophet-doxology Meccan surahs, with **Q 7 al-Aʿrāf** the single closest (0.871). Q 7 contains the longest Mūsā-Pharaoh stretch in the corpus; Q 18:60-82 is the Mūsā-Khaḍir stretch. The two Mūsā-narrative surahs are content-nearest *outside* the canonical adjacency.

The farthest pair Q 55 (al-Raḥmān, 1.271) is consistent with the project's anti-twin pattern: al-Raḥmān is monorhyme fawāṣil-driven (sig_A=+3.17, rank 1 of 114); Q 18 is also extreme monorhyme but via *content-monolithicity-with-low-fāṣila-virtuosity* (sig_A=-2.395, rank 110). Same near-monorhyme, opposite iʿjāz signature — an interesting empirical case.

Notable canonical-adjacency FR distances:
- Q 17 ↔ Q 18 = **0.9013** — among the cheapest in the immediate Q 17/18/19/20 block (FR 0.901 << corpus mean 0.924).
- Q 18 ↔ Q 19 = 0.9254 — at corpus mean.
- Q 18 ↔ Q 12 = 1.0041 — moderate distance to the single-narrative comparator.
- Q 18 ↔ Q 27 = 0.9406 — moderate distance to Q 27 al-Naml (Sulaymān comparator).

## 5. Outlier-window decomposition (H-NEW-590)

The 7-window centred on Q 18 is `[15, 16, 17, 18, 19, 20, 21]` per `h-new-590.json`:

| Field | Value |
|:--|:--:|
| Window | [15, 16, 17, 18, 19, 20, 21] |
| d̄_W | 0.9459 |
| d̄_W−X | 0.9480 |
| pct_W | 54.61 |
| pct_W−X | 54.22 |
| **Δ pct** | **+0.39** |
| p_greater_W | 0.4539 |
| **Classification** | **WEAK_OUTLIER** |

Removing Q 18 *increases* d̄ by a tiny amount (0.0021); the window is essentially indifferent to Q 18's presence. Q 18 fits its window perfectly: Q 15 al-Ḥijr (Meccan, prophet-narrative + muqaṭṭaʿāt ALR), Q 16 al-Naḥl (Meccan-late, didactic), Q 17 al-Isrāʾ (Meccan, Banū Isrāʾīl), Q 19 Maryam (Meccan-early, prophet-narrative), Q 20 Ṭāhā (Meccan, Mūsā-narrative + muqaṭṭaʿāt ṬH), Q 21 al-Anbiyāʾ (Meccan, prophet-doxology) — the late-Meccan-prophet-narrative cluster, of which Q 18's 4-narrative content is a natural member.

**This is the cleanest case of "register-fits-position" in the top-50 of UAS.** The opposite case — Q 24 al-Nūr — has Δ = +23.51 pp in the same outlier-strength scale; Q 18 has Δ = +0.39 pp. Q 24 disrupts; Q 18 conforms.

## 6. Compression-tail position

Q 18 sits at s = 18, well *before* the Hijra-kink at s = 50 ([[h-new-660-compression-tail-gradient|H-NEW-660]]; [[h-new-700-phonological-compression-tail|H-NEW-700]]). The compression-tail laws are silent here by construction. Q 18 belongs to the **pre-kink head zone** along with Q 17, 19, 20, 21, 23, 25-28 — the late-Meccan-prophet-narrative cluster. Its mean content distance d̄ = 1.034 sits *above* the head-zone typical d̄ ≈ 0.95 — Q 18 is content-FAR from corpus-centroid even within its head-zone neighbourhood, but content-NEAR to its specific neighbours (Q 17, 19).

## 7. Architectural type classification

Per the project's typology ([[h-new-840-unified-architectural-score|H-NEW-840]], [[cross-finding-026-iʿjāz-architecture|cross-finding-026]]):

- **Structural-iʿjāz** (al-Bāqillānī *iʿjāz al-fawāṣil*): high UAS + high sig_A → Q 33, Q 1, Q 2, Q 9, Q 55.
- **Theological-iʿjāz** (al-Khaṭṭābī *iʿjāz al-maʿnā*): low UAS but high *thuluth-al-Qurʾān* status → Q 112, Q 114.
- **Outlier-without-iʿjāz al-fawāṣil**: high UAS via outlier+adjacency, low sig_A → Q 24, Q 33 (the "fourth cell" identified by Q 24's investigation).
- **Anti-iʿjāz-with-monolithic-rhyme-register**: mid UAS via content-distance alone, EXTREME negative sig_A, low neighbor-cost → Q 18.

Q 18 is **a fifth distinct cell** in the typology: its empirical signature is mid UAS not driven by outlier or adjacency cost (both very low), but by the absolute magnitude of negative sig_A (−2.395 contributes 2.395 to UAS) plus high mean content-distance. The *mechanism* is NOT outlier-disruption (Q 24's mechanism) and NOT fāṣila-virtuosity (Q 33's mechanism); it is **content-monolithic single-rāwī** sustained over 110 verses — a fourth path to non-trivial architectural significance.

The empirical analogue: Q 18 is to *register-monolithicity* what Q 55 al-Raḥmān is to *fāṣila-virtuosity*. Both are extreme in rhyme; opposite in iʿjāz-signature. Q 18's mid UAS reflects that monolithic-register-sustained-over-large-N is architecturally distinctive but not in the al-Bāqillānī sense.

## 8. Q 18's high content-distance — what drives it

Q 18 is rank 19/114 by mean FR distance to corpus (1.0344 vs corpus mean 0.9235). The 4-narrative content packs unusual lexical breadth into a single surah:

| Narrative | Roots concentrated |
|:--|:--|
| Aṣḥāb al-Kahf | *khf* (cave, 6×), *ftw* (youth), *rqm* (al-Raqīm), *kalb* (dog), *yqẓ* (awakening) |
| Two gardens | *jnn* (gardens, 8×), *bws* (gardens), *zhq* (decay), *ṣḥb* (companion), *ḥwṭ* (encompass) |
| Mūsā-Khaḍir | *baḥr* (sea, *majmaʿ al-baḥrayn*), *ḥwt* (fish), *ṣbr* (patience, 8×), *kḥm* (knowledge of unseen) |
| Dhū al-Qarnayn | *qrn* (Two-Horned, 3×), *ʿyn* (spring), *sd* (barrier), *yʾjwj* (Yājūj), *qṭr* (molten metal) |

Each narrative contributes a vocabulary subset disjoint from the others. The 4 stories are lexically near-disjoint, giving Q 18 a *broad* root-distribution at high concentration in each — pushing its FR distance from the corpus centroid (which is dominated by single-narrative or theme-monolithic surahs). The mean FR rank 19/114 is therefore mechanistically attributable to the 4-narrative architecture itself.

## 9. The 4-narrative spacing geometry

Per `findings/phase-b-hypotheses/csv/h-new-268.json`, the locked four-narrative blocks are:
- Block 1: vv. 9-26 (length 18)
- Block 2: vv. 32-44 (length 13)
- Block 3: vv. 60-82 (length 23)
- Block 4: vv. 83-98 (length 16)

Block-start tuple: (9, 32, 60, 83). Start-gap tuple: **(23, 28, 23)**. Under the exact ordered-placement null over all 135,751 placements of these block-lengths in a 110-verse surah:

| Cell | Description | Count | Probability |
|:--|:--|:-:|:-:|
| A | outer equality (`d_outer_left = d_outer_right`) | 4,389 | 0.0323 |
| B | middle-widest (`d_middle > both outers`) | 18,110 | 0.1334 |
| **C** | **joint palindromic-expansion** (`d_outer_left = d_outer_right < d_middle`) | **1,089** | **0.00802** |

Cell C survives Bonferroni-3 (α_bon = 0.0167); cells A and B do not. **The geometric "small-LARGE-small" expansion** of the 4-narrative starts is real at p = 0.008, Bonferroni-3 corrected. This is a verse-index spacing finding, not a lexical/thematic symmetry — see [[h-new-90-kahf-narrative-structure|H-NEW-90]] for the lexical-parallelism null.

## 10. Cross-references to all H-NEW findings touching Q 18

- [[h-new-111-fisher-rao-mushaf|H-NEW-111]] — Q 18 mean FR distance 1.0344 (rank 19/114); nearest = Q 7 (0.871); farthest = Q 55 (1.271).
- [[h-new-590-outlier-spectrum|H-NEW-590]] — Q 18 WEAK_OUTLIER, Δ = +0.39 pp (rank 31/114); window {15-21}.
- [[h-new-700-phonological-compression-tail|H-NEW-700]] — pre-kink head-zone position s = 18.
- [[h-new-720-canonical-adjacency-cost|H-NEW-720]] — Q 17 → Q 18 = 0.0279 (rank 86/113); Q 18 → Q 19 = 0.0193 (rank 92/113); both cheap.
- [[h-new-750-ijaz-signature|H-NEW-750]] — sig_A = −2.395 (rank 110/114, extreme anti-structural-iʿjāz); sig_B = −1.922 (rank 110); rhyme entropy 0.052 nats (rank 113); top final letter alif at 99.09%.
- [[h-new-840-unified-architectural-score|H-NEW-840]] — UAS = 0.046 (rank 46/114); component breakdown above.
- [[h-new-90-kahf-narrative-structure|H-NEW-90]] — Q 18 four-narrative lexical-parallelism NULL (weak result).
- [[h-new-268-kahf-four-narratives|H-NEW-268]] — Q 18 four-narrative spacing-geometry DIMENSION-SPECIFIC verdict; joint palindromic-expansion p = 0.008, Bonferroni-3 pass.
- [[cross-finding-026-iʿjāz-architecture|cross-finding-026]] — Q 18 illustrates the *anti-iʿjāz al-fawāṣil + monolithic-rhyme-register* cell.

## 11. Honest limits

- The H-NEW-840 UAS is a z-sum of three correlated axes; Q 18's rank 46 is descriptive, not inferential.
- The "Q 17 → Q 18 cost rank 86" depends on the 2-opt heuristic's `L_2opt = 77.388` baseline; rank order in the cheap third is more robust than absolute fraction.
- The "rank 19 / 114 mean FR distance" is calculated only over the no-tashkeel root-distribution variant; under different tokenization the rank can shift modestly. The *direction* — Q 18 is well above corpus mean — is rules-tuple stable.
- The 99.09% alif-monorhyme figure is computed against `quran-text/quran-min-tashkeel.json`. Under other vocalization conventions (e.g., reading *hudan* of v. 13 as alif-bearing in pause-form), the figure could shift to 100% (109+1=110/110); the substantive claim — overwhelming alif-dominance — is rules-tuple stable. See `05-classical-claims-audit.md` Audit 5.
- The 4-narrative block-boundaries are locked at H-NEW-268 (vv. 9-26, 32-44, 60-82, 83-98). Alternative classical block-divisions exist (e.g., al-Biqāʿī's [[biqai-nazm-al-durar.openiti.raw.txt|Naẓm al-Durar]] divides Mūsā-Khaḍir as 60-82 too, but extends Dhū al-Qarnayn through v. 101 not v. 98). The H-NEW-268 segmentation uses a conservative block-end at v. 98; testing v. 101 endpoint shifts d_outer_right by 3, breaks the palindromic-expansion cell — a rules-tuple-fragile aspect of the spacing finding.
- Q 18's high content-distance is partly a 4-narrative artifact; it is therefore an *expected* signature for any 4-narrative surah. The empirical question of whether 4-narrative surahs *generally* have high FR distance is not addressed by Q 18 alone.

## 12. One-paragraph synthesis

Q 18 al-Kahf is the **canonical exemplar of "anti-structural-iʿjāz with monolithic-rhyme-register sustained at large N"**. The mushaf places it at index 18 — embedded in the late-Meccan-prophet-narrative zone (Q 15-21) where its 4-narrative content (Companions of the Cave, two gardens, Mūsā-Khaḍir, Dhū al-Qarnayn) fits register-naturally. Both canonical adjacencies are in the bottom-third of cost (Q 17-18 at rank 86, Q 18-19 at rank 92), the opposite geometry of the Q 24-Q 33 bracketing-cost cluster. Q 18's iʿjāz signature is the corpus's 5th-from-bottom on al-Bāqillānī's fawāṣil-axis (sig_A = −2.395, rank 110/114) — a function of its 99.09% alif-monorhyme combined with high content-distance to corpus (rank 19/114, FR mean 1.034). The four-narrative spacing geometry is real at p = 0.008 (Bonferroni-3) on the joint palindromic-expansion test (gaps 23, 28, 23) per [[h-new-268-kahf-four-narratives|H-NEW-268]], confirming the verse-index "small-LARGE-small" structure of the 4-narrative arc. UAS rank 46 / 114 is therefore a descriptive mid-corpus rank: Q 18 wins UAS via |sig_A| magnitude alone, with both outlier (+0.39 pp) and adjacency cost (0.028) near-zero. This is the project's clearest case of "monolithic-register signature dominating UAS without outlier or adjacency-cost contribution" — and it identifies a fifth typology cell (anti-iʿjāz-with-monolithic-rhyme-register) beyond the four cells previously isolated by Q 1, Q 24, Q 33, Q 55, Q 112.
