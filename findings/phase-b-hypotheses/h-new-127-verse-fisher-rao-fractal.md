# [[h-new-127-verse-fisher-rao-fractal|H-NEW-127]] — Fisher-Rao fractal extension: verse-level path optimality within 5 surahs

**Finding ID**: [[h-new-127-verse-fisher-rao-fractal|h-new-127]]
**Date**: 2026-04-17
**Specialist**: [[h-new-127-verse-fisher-rao-fractal|h-new-127]]-specialist
**Parent**: [[h-new-111-fisher-rao-mushaf|h-new-111]] (surah-level mushaf Fisher-Rao optimality, PASS-DIRECTED)
**Pre-reg**: `findings/phase-b-hypotheses/h-new-127-prereg.md`
**Pre-reg SHA-256**: `bc42449238e4eb67c3b54e234d2f392d093c9993622261d510d8ab7a5fe29e95`
**Seed**: 20260417
**Rules tuple**: (no-tashkeel, QAC-STEM root tokens, QAC v0.4, basmala-counted-only-in-surah-1, mushaf verse order, Hafs-Kūfan)
**Verdict**: **INSTRUMENT-BROKEN** (per pre-committed MW-5 failure on Q 55) — but with a striking substantive split reported below with equal prominence.

---

## Headline

Four of the five pre-registered surahs (Q 2, Q 7, Q 12, Q 36) show the SAME Fisher-Rao information-geodesic optimality at the VERSE level that [[h-new-111-fisher-rao-mushaf|H-NEW-111]] found at the SURAH level. Canonical verse ordering is measurably shorter in Fisher-Rao path length than uniform random permutations within each of those four surahs, at z-scores from −2.82 to −10.26, all p ≤ 0.0046 (Bonferroni-5 threshold 0.01).

The fifth surah (Q 55 al-Raḥmān) shows the OPPOSITE pattern: canonical order is LONGER than 100% of random permutations (z = +5.39, p = 1.0). This is attributable to Q 55's unique refrain-interleaving structure (31 of 78 verses are the refrain "fa-bi-ayyi ālāʾi rabbikumā tukadhdhibān", alternating with 47 content verses): any verse-ordering that CLUSTERS the 31 near-identical refrain verses achieves a much shorter path than the canonical alternating structure does.

This Q 55 behavior ALSO caused the pre-committed MW-5 positive control (length-sorted verses must be WORSE than canonical) to FAIL: because the refrain verses are nearly identical in length, length-sorting accidentally clusters them, producing L_length_sorted = 8.58 < L_canon = 13.64.

Per the pre-reg's failure-mode clause, MW-5 failure → INSTRUMENT-BROKEN verdict. The 4-of-5 replication is held in abeyance until an independent test with a surah-specific MW-5 control validates the null construction.

---

## Numbers

### Per-surah primary test (Bonferroni-5, α_bon = 0.01)

| Sura | n_verses | L_canon | Null mean | Null SD | z-score | p (1-sided lower) | Verdict |
|------|----------|---------|-----------|---------|---------|-------------------|---------|
| 2    | 286      | 104.302 | 108.492   | 0.408   | **−10.26** | **0.0001** | PASS |
| 7    | 206      | 65.805  | 68.269    | 0.304   | **−8.11**  | **0.0001** | PASS |
| 12   | 111      | 32.795  | 34.261    | 0.218   | **−6.72**  | **0.0001** | PASS |
| 36   | 83       | 19.129  | 19.517    | 0.137   | **−2.82**  | **0.0046** | PASS |
| 55   | 78       | 13.639  | 11.253    | 0.442   | **+5.39**  | **1.0000** | FAIL (reversed) |

For Q 2, Q 7, Q 12, Q 55, #{L_perm ≤ L_canon} is extreme: 0 / 10,000 for the three "pass" surahs (shorter than every random perm); 10,000 / 10,000 for Q 55 (longer than every random perm). Q 36 has 45 / 10,000 permutations beating canonical (p = 0.0046).

**Directional summary**: 4 surahs strongly below null, 1 surah strongly above null.

### Secondary A — geodesic-optimality ratio

| Sura | L_canon | L_2opt (approx TSP) | L_canon / L_2opt |
|------|---------|---------------------|------------------|
| 2    | 104.302 | 85.719              | 1.217            |
| 7    | 65.805  | 54.297              | 1.212            |
| 12   | 32.795  | 27.654              | 1.186            |
| 36   | 19.129  | 15.802              | 1.211            |
| 55   | 13.639  | 5.476               | **2.491**        |

For Q 2/7/12/36, canonical verse-order path is within 18.6–21.7% of an approximate TSP optimum — comparable to [[h-new-111-fisher-rao-mushaf|H-NEW-111]]'s surah-level ratio of 1.107 (11% above optimum), though slightly looser at verse scale. For Q 55, canonical path is 149% longer than the TSP approximation, reflecting the refrain-clustering asymmetry.

### MW-5 positive control (Q 55, length-sorted verses)

Pre-committed: L_length_sorted > L_canon (length-sorting should be WORSE than canonical).

| Control variant                    | L     | Pass? |
|-----------------------------------|-------|-------|
| L_canon(55)                        | 13.639 | — |
| L_length_sorted_ascending_TOKENS   | 8.584  | **FAIL** (8.58 < 13.64) |
| L_length_sorted_ascending_CHARS    | 7.936  | **FAIL** (7.94 < 13.64) |

MW-5 FAILS in Q 55 for both operational definitions of "length". Mechanism: the 31 refrain verses in Q 55 are very nearly identical (same roots, same STEM composition) AND very nearly the same length; sorting by length clusters them, producing near-zero distance between consecutive refrain-verses and thus a shorter path than the alternating canonical order.

Per the pre-reg's failure-mode clause (explicitly pre-committed): **MW-5 fail → INSTRUMENT-BROKEN**. Primary family verdict is held in abeyance.

### Pre-committed family verdict

- n_pass = 4 of 5 at α_bon = 0.01.
- Pre-committed threshold for STRONG-REPLICATION: n_pass ≥ 3.
- Without the MW-5 override, this would be STRONG-REPLICATION.
- With the MW-5 override (as pre-committed in the pre-reg), verdict is **INSTRUMENT-BROKEN**.

---

## Interpretation

### The fractal signature (4 of 5 surahs)

For Q 2, Q 7, Q 12, Q 36 — four surahs spanning 83 to 286 verses, Medinan and Meccan, narrative and legal and prophetic-cycle — the canonical verse ordering is significantly closer to a Fisher-Rao geodesic than random permutations would produce. The z-scores (−2.82 to −10.26) and ratios (1.19 to 1.22) are in the same order of magnitude as the surah-level parent finding (z = −11.46, ratio = 1.11). This looks like a fractal signature: the same information-geometric principle appears at the within-surah scale as at the between-surah scale.

The mechanism is straightforward: consecutive verses tend to share vocabulary (roots, content) more than random pairings would, producing a "topical coherence" that maps naturally onto Fisher-Rao distance. This is observable in narrative surahs (Yūsuf's scene-by-scene plot), prophetic-cycle surahs (al-Aʿrāf's Noah/Hūd/Ṣāliḥ sequence), legal surahs (al-Baqara's ritual-then-regulation flow), and in Yā-Sīn's thematic block structure (parable → cosmology → eschatology).

### The Q 55 inversion (1 of 5 surahs)

Q 55 al-Raḥmān fires EXACTLY OPPOSITE to the fractal prediction. This is not noise: z = +5.39 is extreme, and 10,000 out of 10,000 random permutations are shorter than canonical. The mechanism is the refrain: "fa-bi-ayyi ālāʾi rabbikumā tukadhdhibān" appears as 31 of the 78 verses, interleaved (not clustered) with content verses. Because refrain-verses are near-identical in Fisher-Rao distance (d ≈ 0 among themselves), a path that CLUSTERS them is minimal, while the canonical alternating pattern MAXIMIZES distance between consecutive verses. Q 55 is thus information-geometrically ANTI-geodesic by design.

This is independently interesting. It means the Quran, at the verse level, DOES NOT uniformly minimize inter-verse distance — it uses the opposite principle in at least one surah. That same refrain structure is a well-known classical feature of al-Raḥmān (called a distinguishing rhetorical characteristic in tafsīr literature).

Two possibilities:
- **a.** The fractal-optimality principle applies to MOST surahs but is DELIBERATELY VIOLATED in refrain-heavy surahs for hymnic/liturgical purposes. This is the strongest reading and would be consistent with both [[h-new-111-fisher-rao-mushaf|H-NEW-111]] (surah-level optimality) and local violations at rhetorically-marked surahs.
- **b.** The fractal signal in 4/5 is an artifact (length-then-theme Uthmanic ordering heuristic applied at verse level too), and Q 55 is the normal case for refrain-heavy designs. Under this reading, "verse optimality" is really "length-sort optimality", which is partly ruled out by MW-1 but re-enters via correlated length-content.

### The MW-5 failure and what it means

The pre-committed MW-5 on Q 55 was "length-sort should be worse than canonical". This failed: length-sort produces a path 37% SHORTER than canonical. The failure is not random — it is caused by the exact same refrain-clustering mechanism. Length-sort clusters the 31 refrain verses; canonical does not.

This is a CONTENT-level failure of the MW-5 assumption, not a computational bug. The null permutation distribution itself (drawn from the same D matrix) is admissible; it correctly captures "what would random permutations of THESE distributions look like?". The MW-5 check was meant to ensure my null is not degenerate. On Q 55 specifically, length-sort is NOT a "known-worse" baseline because length-sort exploits the refrain structure.

For Q 2, Q 7, Q 12, Q 36, I did NOT run length-sort MW-5 (it was not pre-registered for them). [[h-new-111-fisher-rao-mushaf|H-NEW-111]] separately validated the same null construction at surah scale. So the primary results on those 4 surahs are NOT directly implicated by the Q 55 MW-5 failure.

But I pre-committed to INSTRUMENT-BROKEN on MW-5 failure, and I will honor it. The 4-of-5 replication stands as a strong SUGGESTIVE signal requiring a proper surah-specific MW-5 rerun to be CONFIRMED.

---

## Caveats / honest limits

1. **Pre-committed INSTRUMENT-BROKEN applies.** Per my own pre-reg, MW-5 failure forces verdict to INSTRUMENT-BROKEN. The 4-of-5 result is not promoted to STRONG-REPLICATION.

2. **Q 55 MW-5 choice was wrong FOR Q 55, possibly right for the others.** My pre-reg rationale ("length-sort ignores Fisher-Rao structure and should reliably score worse") was empirically violated in Q 55 precisely because its refrain-structure makes length strongly correlated with being-a-refrain. A proper MW-5 on Q 55 would need to permute refrain-positions vs content-positions separately, or use a different known-worse baseline (e.g., random-with-length-matched-pairs). This amounts to re-specifying MW-5 post-hoc, which I will NOT do — file as [[h-new-127-1-oq20-family-rerun|H-NEW-127.1]].

3. **K = 300 locked pre-hoc**. The verse-level version reduced K from 500 ([[h-new-111-fisher-rao-mushaf|H-NEW-111]]) to 300 for better small-support behavior. Robustness to K was NOT tested here.

4. **2-opt is approximate.** The ratio 1.19–1.22 for Q 2/7/12/36 is an UPPER bound on the true L_canon / L_min; the true optimum is at most L_2opt. So the "near-optimal" claim is conservative.

5. **Secondary A ratios are looser at verse scale than at surah scale.** Surah-level [[h-new-111-fisher-rao-mushaf|H-NEW-111]] had ratio 1.107; verse-level ratios here are 1.19–1.22. Two reasons: (a) verses have more noise per data-point (few root tokens per verse); (b) 2-opt with 80–280 nodes finds better local optima than 2-opt with 114 nodes, tightening the denominator.

6. **Selection of 5 surahs was NOT my choice.** Team-lead handed me the list. No cherry-picking on my part, but the list itself could be critiqued — it skews toward long and muqaṭṭāʿāt-opening surahs. Replication on a different 5-surah set (e.g., Q 1, Q 18, Q 28, Q 78, Q 112) belongs to [[h-new-127-2-oq20-family-rerun|H-NEW-127.2]].

7. **Bonferroni family was k=5.** With one surah going in the opposite direction, the family is heterogeneous. A mixed-effects meta-analysis of z-scores ({−10.26, −8.11, −6.72, −2.82, +5.39}) gives mean z ≈ −4.50, but this is descriptive — not pre-registered.

8. **The Q 55 reversal may itself be a FINDING, not a FAILURE.** Anti-geodesic canonical order in refrain-heavy hymnic surahs could be a deliberate rhetorical feature. A pre-registered follow-up on OTHER refrain-heavy surahs (Q 77 al-Mursalāt with "waylun yawmaʾidhin lil-mukadhdhibīn", Q 56 al-Wāqiʿa's dual-structure groups) would test whether anti-geodesic ordering is refrain-specific or Q-55-unique. File as H-NEW-128 candidate.

---

## Connections to prior findings

- **[[h-new-111-fisher-rao-mushaf|H-NEW-111]]** (parent): surah-level mushaf is Fisher-Rao-optimal at ratio 1.107, p < 10⁻⁴. The current verse-level 4-of-5 replication (if validated) would elevate [[h-new-111-fisher-rao-mushaf|H-NEW-111]] from surah-only to multi-scale signature.
- **[[h-new-58c-musabbihat-tense-split|H-NEW-58c]]** (musabbiḥāt cluster): identified lexical-thematic adjacency patterns. Q 55's refrain structure is a different kind of intra-surah structure and does not overlap with the musabbiḥāt finding.
- **T3 canonical-order-recovery**: verse-level recovery was attempted earlier in the project (check `canonical-order-recovery.md`). The Q 55 anti-geodesic behavior would explain why verse-level recovery cannot rely solely on minimum-distance heuristics.

---

## Files

- Pre-reg: `findings/phase-b-hypotheses/h-new-127-prereg.md`
- Script: `scripts/h_new_127_verse_fisher_rao.py`
- JSON: `findings/phase-b-hypotheses/csv/h-new-127.json`
- Journal: `journal/h-new-127-run-1.md`

---

## Verdict

**INSTRUMENT-BROKEN** per pre-committed MW-5 clause.

Substantive findings (reported with equal prominence to the INSTRUMENT-BROKEN verdict per DISCIPLINE §honesty):

- 4 of 5 surahs show Fisher-Rao-geodesic optimality at VERSE scale, z from −2.82 to −10.26, all p ≤ 0.0046 (Bonferroni-5 threshold 0.01). Ratios L_canon/L_2opt ∈ [1.19, 1.22].
- Q 55 al-Raḥmān shows anti-geodesic canonical order (z = +5.39, p = 1.0) — canonical ordering is LONGER than 100% of random permutations. Attributable to refrain interleaving (31 of 78 verses).
- MW-5 length-sort control failed in Q 55 (L_lensort < L_canon) due to refrain-length homogeneity, triggering the pre-committed INSTRUMENT-BROKEN verdict.

### Follow-up pre-reg candidates (not executed here)

- **[[h-new-127-1-oq20-family-rerun|H-NEW-127.1]]**: Re-run same test with a surah-specific MW-5 that is robust to refrain structure (e.g., greedy-NN-from-verse-1 "known-better" for the 4 non-refrain surahs; no MW-5 for Q 55 since length-sort provably doesn't work there, replace with reverse-canonical or shuffle-within-neighbor-windows).
- **[[h-new-127-2-oq20-family-rerun|H-NEW-127.2]]**: Replication on a DIFFERENT 5-surah set.
- **H-NEW-128**: Test anti-geodesic hypothesis on other refrain-heavy surahs (Q 56, Q 77).
- **[[h-new-129-joint-late-meccan-peak|H-NEW-129]]**: Connect [[h-new-111-fisher-rao-mushaf|H-NEW-111]] and [[h-new-127-verse-fisher-rao-fractal|H-NEW-127]]'s fractal signature to the meta-cluster network [[h-new-89-meta-cluster-network|H-NEW-89]].

### Ceiling

This finding does NOT elevate [[h-new-111-fisher-rao-mushaf|H-NEW-111]]'s PASS-DIRECTED ceiling. The 4-of-5 replication is strong, but the pre-committed MW-5 failure prevents a direct promotion. [[h-new-127-1-oq20-family-rerun|H-NEW-127.1]] (with a sound MW-5) is the cleanest path to elevation.
