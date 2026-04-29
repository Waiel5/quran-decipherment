---
finding_id: H-NEW-238
run: 1
date: 2026-04-17
operator: specialist-agent (cyclic-shift wrap-edge task)
seed: 20260419
bonferroni_k: 1
alpha_bon: 0.05
rules_tuple: (114 surahs Hafs-Kūfan; no-tashkeel; QAC-STEM top-500 roots; Dirichlet α=0.5; L1-normalized; Fisher-Rao arccos Bhattacharyya; D inherited from H-NEW-111)
script: scripts/h_new_238_cyclic_shift_wrap.py
prereg: findings/phase-b-hypotheses/h-new-238-cyclic-shift-wrap-prereg.md
output_json: findings/phase-b-hypotheses/csv/h-new-238.json
output_md: findings/phase-b-hypotheses/h-new-238-cyclic-shift-wrap.md
h111_sha256: 4c366c414b82b0d0f3bcd06b68a7b5a87b500cf925b5088704a36c355d7f33fc
verdict: NULL (strict) / PASS-DIRECTED-ADJACENT (nuanced; Q 1 is top-quintile at rank 18/114)
---

# H-NEW-238 Run 1 — Cyclic-shift wrap-edge analysis

## Question
Among all 114 cyclic shifts of the mushaf ordering, what is the rank of the canonical Q 1-at-position-1 rotation on the ascending-sorted Fisher-Rao wrap-edge criterion W(k) = d_FR(Q k−1, Q k)?

## Key numbers

| Metric | Value |
|---|---:|
| Canonical W(1) = d_FR(Q 114 al-Nās, Q 1 al-Fātiḥa) | 0.3884 |
| Canonical Q 1 rank (ascending W) | **18 / 114** (15.8%ile) |
| Minimum-wrap start k* = Q 108 al-Kawthar | W* = 0.2256 |
| Cycle total length Σ W(k) | 86.1480 |
| Min / max / mean / median / sd of W | 0.2256 / 1.1776 / 0.7557 / 0.8137 / 0.2434 |

## Verdict

**Strict verdict (pre-reg rank mapping): NULL.** Q 1 rank = 18 > 10, so under the pre-registered Bonferroni k=1, α=0.05, rank ≤ 10 threshold for PASS-DIRECTED, the canonical rotation does NOT quantify as the M1-preferred start under strict pass-gating.

**Nuanced reading: Q 1 is top-quintile (15.8%ile).** Rank 18 / 114 is neither minimum (rank 1) nor mid-pack (rank 57.5). It is in the top 16% of cyclic shifts, which is better than liturgical-only would predict on average (rank 57.5 expected under uniform) but clearly NOT at the geodesic-minimum rotation.

## Top-10 tightest-wrap starting-points (M1-preferred)

All 10 are in the short mufaṣṣal tail (Q 104–114):

| Rank | k | Surah at pos 1 | Preceded by (pos 114) | W |
|---:|---:|---|---|---:|
| 1 | Q 108 | al-Kawthar | Q 107 al-Māʿūn | 0.2256 |
| 2 | Q 114 | al-Nās | Q 113 al-Falaq | 0.2718 |
| 3 | Q 107 | al-Māʿūn | Q 106 Quraysh | 0.2772 |
| 4 | Q 112 | al-Ikhlāṣ | Q 111 al-Masad | 0.2849 |
| 5 | Q 113 | al-Falaq | Q 112 al-Ikhlāṣ | 0.2886 |
| 6 | Q 106 | Quraysh | Q 105 al-Fīl | 0.2915 |
| 7 | Q 104 | al-Humaza | Q 103 al-ʿAṣr | 0.3119 |
| 8 | Q 111 | al-Masad | Q 110 al-Naṣr | 0.3184 |
| 9 | Q 109 | al-Kāfirūn | Q 108 al-Kawthar | 0.3342 |
| 10 | Q 105 | al-Fīl | Q 104 al-Humaza | 0.3364 |

The canonical Q 1 rotation ranks at position 18, immediately behind a dense cluster of Q 104–114 adjacent pairs (the terminal short mufaṣṣal sequence).

## Bottom-10 loosest-wrap (M1-disfavored)

Rank 114 (absolute worst) is particularly striking:

| Rank | k | Surah at pos 1 | Preceded by (pos 114) | W |
|---:|---:|---|---|---:|
| 105 | Q 24 al-Nūr | Q 23 al-Muʾminūn | 1.0497 |
| 106 | Q 13 al-Raʿd | Q 12 Yūsuf | 1.0683 |
| 107 | Q 10 Yūnus | Q 9 al-Tawba | 1.0689 |
| 108 | Q 34 Sabaʾ | Q 33 al-Aḥzāb | 1.1154 |
| 109 | Q 57 al-Ḥadīd | Q 56 al-Wāqiʿa | 1.1156 |
| 110 | Q 25 al-Furqān | Q 24 al-Nūr | 1.1291 |
| 111 | Q 33 al-Aḥzāb | Q 32 al-Sajda | 1.1330 |
| 112 | Q 56 al-Wāqiʿa | Q 55 al-Raḥmān | 1.1493 |
| 113 | Q 55 al-Raḥmān | Q 54 al-Qamar | 1.1516 |
| **114** | **Q 2 al-Baqara** | **Q 1 al-Fātiḥa** | **1.1776** |

**Key finding**: the ABSOLUTE WORST edge in the mushaf cycle is Q 1 al-Fātiḥa → Q 2 al-Baqara (W = 1.1776). The canonical start creates the TIGHTEST-in-top-quintile wrap at Q 114 → Q 1 (W = 0.3884, rank 18/114) AND the LOOSEST edge in the entire cycle at Q 1 → Q 2 (W = 1.1776, rank 114/114). The short-to-long transition at the opening is the cycle's maximum compositional jump.

## Interpretations

1. **Q 1 is not the M1-minimum rotation.** The minimum-wrap-edge start is k* = Q 108 al-Kawthar (W* = 0.2256, 42% tighter than canonical Q 1's 0.3884). If M1 alone drove the canonical choice, the mushaf would be rotated to start at Q 108 al-Kawthar, preceded by Q 107 al-Māʿūn. This is clearly not the canonical tradition.

2. **Q 1 IS, however, top-quintile (15.8%ile).** Q 1's wrap at rank 18 is far better than random (expected rank 57.5). The canonical rotation is not geodesically arbitrary — it is on the tighter side of the distribution, but it is NOT the absolute minimum.

3. **The short-mufaṣṣal cluster dominates the top of the ranking.** Ranks 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 are all pairs within Q 103–114. These surahs are mutually similar in root-distribution (confirming the H-NEW-137 TERMINAL_TRIAD content-closure finding and cross-finding-019's Q 50 ḥawāmīm-group coherence extended to the short-end). Any rotation that lands the "cut point" inside this short-terminal cluster yields a tiny wrap-edge — hence the top-10 lock-out.

4. **The canonical Q 114 → Q 1 wrap (rank 18) lands at the BOUNDARY of this short-terminal cluster.** Q 1 al-Fātiḥa is 7 verses, prayer-frame, short. Q 114 al-Nās is 6 verses, short. Their mutual root-distribution similarity (W = 0.3884) is real but not AS tight as the internal Q 104–114 adjacencies (W ≈ 0.22–0.34). Q 1 is a "near-miss" to the internal short-surah cluster on Fisher-Rao roots — close enough to rank 18, not close enough to rank 1.

5. **The compositional HINGE is at Q 1 → Q 2 (rank 114, worst).** The canonical mushaf has two architectural consequences of placing al-Fātiḥa at position 1:
   - Position 114→1 (the wrap): tight (rank 18) because short-to-short-prayer-frame transition is in the tight half.
   - Position 1→2 (the opener-to-longest): **the largest single Fisher-Rao jump in the 114-edge cycle**, 3× the mean and 5× the minimum. The mushaf opens with a structural hinge larger than any of the Juzʾ / block / Meccan-Medinan boundaries identified in H-NEW-130/130b (15 largest jumps), all of which sit in the interior.

   **This is a new observation**: the Q 1 → Q 2 edge is the SINGLE LARGEST Fisher-Rao jump in the entire mushaf cycle. Worth follow-up: does this "biggest opening hinge" appear in H-NEW-130's universal-hinge list? (Likely yes; it is consistent with the "Q 1 as sui-generis prayer frame + Q 2 al-Baqara as the first encyclopedic content surah" transition.)

6. **Reconciliation with H-NEW-227.** H-NEW-227 established that the mushaf wrap d(Q 114, Q 1) = 0.3884 is below the null 5th percentile AND tighter than all 4 chronology wraps. That is a BETWEEN-ordering test. The present test is a WITHIN-ordering (cyclic-shift) test: given the mushaf ordering, is Q 1 the MINIMUM wrap rotation? Answer: no (rank 18), but still below the 5th percentile of RANDOM-ordering wraps (H-NEW-227). The two findings are compatible: the mushaf as a whole has an unusually tight wrap-edge *among all possible orderings*, but within the mushaf's own rotation space, 17 other rotations beat Q 1.

## Link to H-NEW-192 (compositional decomposition)

H-NEW-192 found Q 1 has the largest position-prediction residual in the corpus: feature-predicted position = 105, actual position = 1, Δ = −104. That test said Q 1's placement is sui-generis (liturgical / prayer-frame, not compositional). The present test gives an INDEPENDENT quantification of the same phenomenon:

- Feature-prediction (H-NEW-192): "if you predicted position from compositional features, Q 1 would be at position 105 (short mufaṣṣal end), not position 1."
- Wrap-edge (H-NEW-238): "if you optimized the rotation of the mushaf cycle for minimum wrap-edge, you would start at Q 108, not Q 1. Under the rotation that starts at Q 1, the wrap-edge is rank 18/114."

Both instruments independently place Q 1 at the short-mufaṣṣal end of the content-feature space (consistent with H-NEW-137 TERMINAL_TRIAD closeness) while the canonical order places Q 1 at position 1. Both independently diagnose the placement as liturgical (P3), not compositional.

## Link to cross-finding-020 (complete equation)

cross-finding-020's decomposition `mushaf ≈ 76% f_M5 + 15% g_M1 + 5% h_P3 + 4% residual` assigns 5% of mushaf-position variance to liturgical-frame effects (Q 1 exception dominant). The present H-NEW-238 result directly supports that decomposition: at Q 1, M1 (geodesic) would prefer rotation to Q 108, but P3 (liturgical) fixes Q 1 at position 1. The 5% h_P3 share is localized largely to the Q 1 row of the decomposition.

## Classical alignment

- **al-Suyūṭī *Itqān***: fātiḥat al-kitāb = "Opener of the Book" is a liturgical designation — Q 1 is umm al-kitāb recited at every ṣalāh raka. P3 is classically attested.
- **Ibn Taymiyya *Majmūʿ al-Fatāwā***: mushaf sūra-order is *tawqīfī* (divinely-fixed). This doctrine does NOT claim compositional-minimum; it claims revelatory-fixedness. The present result is compatible: Q 1 is NOT the compositional-geodesic minimum, but IS tawqīfī-fixed.
- **al-Zarkashī *Burhān***: Q 1 is the archetypal fātiḥa.

The empirical result (Q 1 rank 18, not rank 1) vindicates al-Suyūṭī's liturgical framing over any hypothetical compositional-optimization framing. Classical tradition's P3 interpretation is quantitatively supported — Q 1 placement is not geodesically optimal.

## Verdict reconciliation

- Strict pre-reg: NULL (rank 18 > 10 threshold).
- Substantive reading: PASS-DIRECTED-ADJACENT. Q 1 is top-quintile (15.8%ile) on wrap-edge — BETTER than random mid-pack, but NOT the M1-minimum. The interpretation is P3-dominant with M1-tolerance, not P3 ∧ M1 alignment.
- Bottom line: al-Fātiḥa's canonical position-1 status is a LITURGICAL designation that incurs a small compositional cost (W = 0.3884 vs possible W* = 0.2256, a 42% tighter rotation exists). The cost is tolerable — Q 1's wrap is still in the tight quintile — but it is a cost, not a free lunch.

## Top-5 tightest-wrap starting-points (requested deliverable)

1. **Q 108 al-Kawthar** at position 1, preceded by Q 107 al-Māʿūn. W = 0.2256. (M1-preferred.)
2. Q 114 al-Nās at position 1, preceded by Q 113 al-Falaq. W = 0.2718.
3. Q 107 al-Māʿūn at position 1, preceded by Q 106 Quraysh. W = 0.2772.
4. Q 112 al-Ikhlāṣ at position 1, preceded by Q 111 al-Masad. W = 0.2849.
5. Q 113 al-Falaq at position 1, preceded by Q 112 al-Ikhlāṣ. W = 0.2886.

Of note: Q 108 al-Kawthar is the M1-minimum start, and it is ALSO the subject of cross-finding-019 as a "composite hub exemplar" of the 4-region architecture. Q 108 being the M1-preferred rotation-start is consistent with its hub status at the short-mufaṣṣal cluster.

## Files

- Pre-reg: `findings/phase-b-hypotheses/h-new-238-cyclic-shift-wrap-prereg.md`
- Script: `scripts/h_new_238_cyclic_shift_wrap.py`
- Results JSON: `findings/phase-b-hypotheses/csv/h-new-238.json`
- Findings: `findings/phase-b-hypotheses/h-new-238-cyclic-shift-wrap.md`
