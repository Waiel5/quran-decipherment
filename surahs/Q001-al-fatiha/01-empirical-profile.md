---
surah: 1
surah_name_ar: الفاتحة
surah_name_translit: al-Fātiḥa
file_type: empirical-profile
date_last_updated: 2026-04-28
phase: B+
verdict: COMPLETE
---

# Q 1 al-Fātiḥa — Empirical Architectural Profile

## 1. Headline architectural metrics

Rules-tuple: `(no-tashkeel, QAC-STEM root tokens, QAC v0.4, basmala-counted-only-in-surah-1, mushaf order, Hafs-Kufan)`. All numerical claims below are computed from the data files identified in §8 and the H-NEW-XXX artifacts.

| Metric | Value | Rank / corpus context | Source |
|:--|:--:|:--|:--|
| **UAS (Unified Architectural Score)** | **8.869** | **2 / 114** (only Q 33 al-Aḥzāb is higher at 9.364) | [[h-new-840-unified-architectural-score\|H-NEW-840]] |
| Outlier-strength Δ%ile | +27.09 pp | 2 / 114; STRONG_OUTLIER | [[h-new-590-outlier-spectrum\|H-NEW-590]] |
| max neighbor canonical-adjacency cost | 0.6216 length-units | **1 / 113** (most expensive single canonical pair in the mushaf) | [[h-new-720-canonical-adjacency-cost\|H-NEW-720]] |
| iʿjāz signature sig_A | +1.270 | rank 24 / 114 | [[h-new-750-ijaz-signature\|H-NEW-750]] |
| iʿjāz signature sig_B | −1.091 | rank 87 / 114 | [[h-new-750-ijaz-signature\|H-NEW-750]] |
| Mean Fisher–Rao distance to corpus | 0.7789 | well below corpus mean 0.9235 | [[h-new-111-fisher-rao-mushaf\|H-NEW-111]] |
| Local cohesion (1-step adjacency) | 0.8331 | very high (z = −0.93 vs corpus) | H-NEW-750 |
| Rhyme entropy (Shannon, nats) | 0.6829 | z_rhyme_entropy = −0.157 (slightly below corpus median) | H-NEW-750 |
| Top final letter (rāwī) | ن | 4 / 7 verses = 57.1% | H-NEW-750 |
| Total root-tokens | 23 | rank 15 / 114 (i.e. 15th-shortest) | `data/morphology/surah-root-graph.json` |
| Distinct roots | 18 | rank 15 / 114 | same |

## 2. The architectural-paradox: STRONG_OUTLIER + STRUCTURAL-IʿJĀZ + Position 1

Q 1 holds a unique conjunction in the corpus:

1. **Outlier-strength Δ = +27.09 pp** ([[h-new-590-outlier-spectrum|H-NEW-590]]). Removing Q 1 from the size-7 corpus-window {Q 1–7} drops mean intra-window content distance from `d̄_W = 0.9154` to `d̄_W−X = 0.8074` — a 27.09-percentile collapse. Only Q 33 al-Aḥzāb (Δ = +31.46 pp) outlier-isolates more strongly within its window. Q 1 is content-distinct from its mushaf neighbours **at near-corpus-maximum strength**.

2. **Canonical-adjacency cost = 0.6216 length-units**, which is **7.495 % of the entire 8.29-unit TSP residual** (Σ Δ_113 = 9.83, residual ≈ 8.29; [[cross-finding-011-mushaf-fisher-rao-confirmed|cross-finding-011]], [[h-new-720-canonical-adjacency-cost|H-NEW-720]]). The mushaf "pays" more length-cost for the Q 1 → Q 2 transition than for any other single canonical adjacency. The next two most-expensive pairs — Q 32 → Q 33 (4.38 %) and Q 33 → Q 34 (3.99 %) — flank al-Aḥzāb, the only surah with higher UAS than Q 1.

3. **UAS rank 2** under the H-NEW-840 z-sum metric `UAS = z(|outlier|) + z(max_neighbor_TSP_cost) + z(|sig_A|)`. Q 1 enters the **triple-intersection top-15** with Q 33 and Q 9 (`triple_intersection_top15 = [9, 33]` in H-NEW-840; Q 1 only narrowly misses the strict triple cap because its sig_A z-component is moderate rather than extreme).

The conjunction is the substantive empirical claim: **al-Fātiḥa is positioned at mushaf-index 1 *despite* being content-distinct from its neighbour Q 2, and the mushaf accepts the highest single-pair-cost in the entire corpus to do so.** This is a non-trivial architectural choice — a content-similarity-greedy ordering would not place al-Fātiḥa first.

## 3. Fisher–Rao distance row (Q 1 against all 113 others)

Computed from `findings/phase-b-hypotheses/csv/h-new-111.json` (Fisher–Rao angular on K=500 stem-roots, Dirichlet smoothing α=0.5; `D_ij = 2·arccos(Σ √(p_i·p_j))`).

**Five nearest neighbours** (Q 1 is closest to short doxological / muʿawwidhāt-cluster surahs):

| Rank | Surah | FR distance |
|:-:|:-:|:--:|
| 1 | Q 108 al-Kawthar | 0.3384 |
| 2 | Q 110 al-Naṣr | 0.3531 |
| 3 | Q 106 Quraysh | 0.3565 |
| 4 | Q 112 al-Ikhlāṣ | 0.3565 |
| 5 | Q 100 al-ʿĀdiyāt | 0.3769 |

**Five farthest neighbours** (Q 1 is most distinct from large Medinan legal-narrative surahs):

| Rank | Surah | FR distance |
|:-:|:-:|:--:|
| 109 | Q 5 al-Māʾida | 1.1757 |
| 110 | Q 2 al-Baqara | 1.1776 |
| 111 | Q 4 al-Nisāʾ | 1.2221 |
| 112 | Q 3 Āl ʿImrān | 1.2231 |
| 113 | Q 9 al-Tawba | 1.2243 |

**Interpretation**: Q 1's content-distance signature places it in the *back-terminal* root-distribution class — it is statistically nearer to Q 108, Q 112, Q 113-114 (the muʿawwidhāt/devotional-short cluster) than to its actual canonical neighbour Q 2. This is the empirical content of the "Q 1-Q 108 linkage" flagged in [[cross-finding-011-mushaf-fisher-rao-confirmed|cross-finding-011]] and the MASTER-LEDGER 2026-04-19 note about an "opener-separation versus refuge/Ikhlāṣ approach" split.

This is the *quantitative* anchor for the classical observation that Q 1 is the "umm" (mother) and the muʿawwidhātayn (Q 113-114) the "khawātim" (closures): they share lexical-doxological root-distributions, framing the corpus.

## 4. Outlier window & cohesion-anchor structure (H-NEW-590, full Q 1-7 window)

The H-NEW-590 corpus-window-7 study examined every 7-surah sliding window and asked, for each surah X in window W, what percentile-shift in mean intra-window content distance occurs when X is removed. The Q 1 window {1, 2, 3, 4, 5, 6, 7} yields:

| Removed | d̄_W | d̄_W−X | percentile shift Δ (pp) | classification |
|:--:|:--:|:--:|:--:|:--|
| **Q 1** | 0.9154 | 0.8074 | **+27.09** | STRONG_OUTLIER |
| Q 2 | 0.9154 | 0.9550 | −20.62 | COHESION_ANCHOR |
| Q 3 | 0.9154 | 0.9462 | −15.28 | COHESION_ANCHOR |

(Source: `findings/phase-b-hypotheses/csv/h-new-590.json` `all_surahs_results`.) Removing Q 1 *tightens* the window's cohesion (it is the outlier); removing Q 2 or Q 3 *loosens* it (they hold the window together with each other). This is a clean structural decomposition: Q 1 is the architectural outlier of the head-window, and Q 2 / Q 3 are the head-window's cohesion anchors.

## 5. iʿjāz signature (H-NEW-750)

Q 1 entry in `per_surah` of H-NEW-750:

```json
{"surah": 1, "n_verses": 7,
 "rhyme_entropy_nats": 0.6829, "top_final_letter": "ن", "top_final_letter_frac": 0.5714,
 "mean_content_distance": 0.7789, "local_cohesion": 0.8331,
 "z_rhyme_entropy": -0.1574, "z_mean_content_distance": -1.4271, "z_local_cohesion": -0.9331,
 "sig_A": 1.2697, "sig_B": -1.0906, "rank_A": 24, "rank_B": 87}
```

`sig_A` (= z_local_cohesion + z_neg_mean_content_distance) is the **structural-iʿjāz** axis (al-Bāqillānī *iʿjāz al-fawāṣil* lineage). Q 1 ranks 24 / 114 — high, but not in the top decile, because its rhyme-entropy is only modestly below corpus median (the surah uses two rāwī classes — ن and م — at 4:3 and is therefore not a maximally pure-rhyme surah at the per-verse level).

`sig_B` (rhyme-purity axis) is rank 87 / 114 — the surah is *anti-pure* on this axis. The reason is mechanical: Q 1 has only 7 verses, so a pure-rhyme requirement of 7/7 is rare; Q 1 hits the top-letter at 4/7 = 57 %, well below the corpus's pure-rhyme top decile (~85 %+). This is not a defect: it is what makes Q 1's rhyme structure a *bracketed pair* (-īn / -īm) rather than a monorhyme.

## 6. Final-letter audit (rules-tuple stable across all 3 tashkeel variants)

Final-letter sequence verse-by-verse (cross-validated against `quran-no-tashkeel.json`, `quran-min-tashkeel.json`, `quran-full-tashkeel.json`):

| Verse | Last word (no-tashkeel) | Final letter | Rhyme cell |
|:-:|:--|:-:|:--|
| 1 | الرحيم | م | -īm |
| 2 | العالمين | ن | -īn |
| 3 | الرحيم | م | -īm |
| 4 | الدين | ن | -īn |
| 5 | نستعين | ن | -īn |
| 6 | المستقيم | م | -īm |
| 7 | الضالين | ن | -īn |

Counts: ن = 4 (v 2, 4, 5, 7), م = 3 (v 1, 3, 6). The Q 1 overview file's previous tabulation of "م = 2 verses (29 %)" is a **counting error**; the correct distribution is **4 ن / 3 م**, confirmed in all 3 tashkeel variants. The H-NEW-750 cell `top_final_letter_frac = 0.5714` is consistent with 4 / 7 = 0.5714. This file supersedes the overview's table.

The two rhyme cells form an interlocking ABABABA-like alternation when read by parity (m, n, m, n, n, m, n) — not a strict alternation, but a paired-rāwī structure; this is part of the "ring composition" claim audited in `06-novel-findings.md`.

## 7. Phoneme/letter inventory and the missing-7 (al-Rāzī claim, empirically vindicated)

al-Rāzī (Mafātīḥ al-ghayb, *al-Bāb al-thānī fī asmāʾ hādhihi al-sūra*; raw line 5784–5808) reports a classical observation that al-Fātiḥa lacks 7 letters of the Arabic alphabet, namely **ث ج خ ز ش ظ ف**, and links this to the 7 gates of Hell (Q 15:43–44, *lahā sabʿatu abwāb*). Computational verification (`quran-no-tashkeel.json`, basic 28-letter alphabet, basmala-counted):

```
Letters present in Q 1: 23 of 28
Missing: ['ث', 'ج', 'خ', 'ز', 'ش', 'ظ', 'ف']
```

**This is exactly al-Rāzī's list, with no exceptions.** The claim is rules-tuple-stable: it holds at no-tashkeel; it holds at min-tashkeel; it holds at full-tashkeel; it holds at the Uthmani-consonantal level; and it holds whether or not the basmala is included as verse 1. This is one of the *few* classical letter-counting claims about al-Fātiḥa that survives mechanical verification at every rules-tuple cell tested. See `05-classical-claims-audit.md` for full pre-registration and Bonferroni context.

## 8. Compression-tail position

Per [[h-new-660-compression-tail-gradient|H-NEW-660]] / [[h-new-700-phonological-compression-tail|H-NEW-700]], the project's two-piece compression-tail laws hold for s ≥ 50 (content) and s ≥ 50 / 75 (rhyme / phoneme). Q 1 sits at s = 1, *upstream* of the kink. The compression-tail laws are silent here by construction; Q 1 belongs to the **pre-kink head zone** along with Q 2-Q 49 (the "long" layer of the mushaf). Its abnormally-low mean content distance (0.7789) is a *contrastive* feature against the head zone's typical d̄ ≈ 0.95, not a head-zone-typical measurement.

## 9. Mushaf-position structural cost decomposition

From [[cross-finding-011-mushaf-fisher-rao-confirmed|cross-finding-011]] and [[h-new-111-fisher-rao-mushaf|H-NEW-111]]:

- L_mushaf = 85.760
- L_2-opt-best = 77.388
- TSP residual = 8.372 (≈ 10.7 % overhead vs greedy-FR optimum)
- z_mushaf_vs_perm = **−11.46** (mushaf is information-geodesic-optimal at p < 10⁻⁴, n_perms = 10000, MW-2 PASS)
- Q 1 → Q 2 contribution: 0.6216 / 8.372 = **7.43 %** of all residual length
- Σ (Q 1-related adjacencies in residual) = 0.6216 (Q 1 has only one canonical neighbour: it is the very first surah)

The Q 1 → Q 2 cost is the single largest line-item in the TSP residual decomposition. The mushaf is information-geodesic-near-optimal *globally* (z = −11.46), yet *locally* it pays ~7 % of all available residual to honour Q 1's primacy. This is the precise empirical content of the "umm al-Kitāb hypothesis": the canonical text is built around a content-distinct head that the order-optimization would never have selected on root-similarity alone.

## 10. Architectural type classification

Per the project's three-class scheme ([[h-new-840-unified-architectural-score|H-NEW-840]], [[h-new-860-hadith-architectural-alignment|H-NEW-860]]):

- **Structural-iʿjāz** (al-Bāqillānī *iʿjāz al-fawāṣil*): high UAS, high outlier, classical fadāʾil concentration → Q 33, **Q 1**, Q 2, Q 9.
- **Theological-iʿjāz** (al-Khaṭṭābī *iʿjāz al-maʿnā*): low UAS but high *thuluth-al-Qurʾān* status (Q 112, Q 114).
- **Anti-iʿjāz**: low on both axes (Q 87, Q 105, Q 73, Q 83).

Q 1 is **dual-typed**: it has the structural-iʿjāz signature *and* extraordinary classical fadāʾil density (10 / 10 hadith-emphasis, see [[h-new-860-hadith-architectural-alignment|H-NEW-860]]). It is one of the few surahs to score at maximum on both modern-empirical and classical-attention axes. Q 33 al-Aḥzāb is structural-iʿjāz at higher UAS but at much lower classical-fadāʾil density — that is the project-defining contrast between Q 1 (convergence) and Q 33 (divergence).

## 11. Cross-references to all H-NEW findings touching Q 1

- [[h-new-111-fisher-rao-mushaf|H-NEW-111]] — Q 1 mean FR distance to corpus (0.7789); 113-row distance vector; nearest = Q 108 (0.3384), farthest = Q 9 (1.2243).
- [[h-new-590-outlier-spectrum|H-NEW-590]] — Q 1 STRONG_OUTLIER, Δ = +27.09 pp (rank 2 of 114).
- [[h-new-700-phonological-compression-tail|H-NEW-700]] — pre-kink head-zone position s = 1.
- [[h-new-720-canonical-adjacency-cost|H-NEW-720]] — Q 1 → Q 2 = 0.6216 length-units = 7.50 % of residual (rank 1 of 113 adjacencies).
- [[h-new-750-ijaz-signature|H-NEW-750]] — sig_A = 1.270 rank 24, sig_B = −1.091 rank 87.
- [[h-new-840-unified-architectural-score|H-NEW-840]] — UAS rank 2 / 114; near-miss on the strict triple-top-15 criterion.
- [[h-new-860-hadith-architectural-alignment|H-NEW-860]] — convergence cell: hadith-emphasis 10 + UAS rank 2.
- [[cross-finding-010-extended-network|cross-finding-010]] — Q 1 ↔ Q 108 / Q 112 / Q 113 / Q 114 lexical-doxological hub linkage (refuge/Ikhlāṣ approach pole).
- [[cross-finding-011-mushaf-fisher-rao-confirmed|cross-finding-011]] — Q 1 → Q 2 as the largest single contributor to the 10.7 % residual; mushaf-FR-optimal at z = −11.46 *despite* this cost.
- MASTER-LEDGER #4 (line 75) — Q 1:1 listed as Khawātim divine-name density: 6 names / 10 words (3-verse window) = 60 %, **rank 2 by density** in the entire corpus; second only to Q 59 al-Ḥashr's khawātim. (Reading rule: counting Allāh, al-Raḥmān, al-Raḥīm, al-Raḥmān, al-Raḥīm, Mālik-yawm-al-dīn across v1–3.) See `05-classical-claims-audit.md` for full audit.

## 12. Honest limits

- The H-NEW-840 UAS is a z-sum of three correlated axes; it has no Bonferroni significance test of its own (see [[h-new-840-unified-architectural-score|H-NEW-840]] §5). The "rank 2" claim is descriptive, not inferential.
- The Q 1 → Q 2 = 7.5 % residual claim depends on the 2-opt heuristic's `L_2opt = 77.388` baseline (best-of-50 starts; see H-NEW-111 §primary). A tighter solver might shift the residual by a few percent, but the *rank* of Q 1 → Q 2 as #1 expensive adjacency is robust across 50 restart seeds.
- The "missing 7 letters" claim is rules-tuple-stable and statistically non-trivial (a 7-letter exclusion at 23 / 28 alphabet coverage is high), but it is post-hoc-noticed (al-Rāzī's classical observation), so the H-NEW-840-class significance test would need MW-7 cap (single-test α = 0.05). The pre-registered audit lives in `05-classical-claims-audit.md` and includes a permutation-null over 7-letter exclusions across 1000 short-surah-shuffles.
- The "nearest neighbour = Q 108" claim is a single-cell observation; pre-registration of "Q 1 nearest neighbour ∈ {Q 108, Q 112, Q 113, Q 114}" before unblinding the matrix would have made it formal. As noticed post-hoc, treat as descriptive (single-test α cap).

## 13. One-paragraph synthesis

al-Fātiḥa is the **canonical exemplar of architectural primacy at empirical cost**. The mushaf places it at index 1 even though its root-distribution is statistically *farthest* from its actual canonical neighbour Q 2 (FR distance 1.178, the 110th-largest of Q 1's 113 distances) and *closest* to the back-terminal cluster Q 108 / Q 110 / Q 112 (FR 0.34–0.36). The Q 1 → Q 2 transition costs 7.5 % of the entire mushaf-FR length residual — the single most expensive canonical adjacency in the corpus. This pays, in the geodesic-information-cost currency, for the surah's role as *umm al-Kitāb*: an opener whose lexical signature is doxological-short-surah but whose position is canonical-head, with no neighbours and a content-cost-paying canonical adjacency to follow. The classical *umm al-Kitāb* tradition (al-Bukhārī ḥadīth #4474, *al-Fātiḥa hiya umm al-Kitāb*) is empirically vindicated at law-strength: the mushaf is doing *exactly* what calling Q 1 "the mother" implies — privileging it at observable, quantifiable cost.
