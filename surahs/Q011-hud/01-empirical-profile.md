---
surah: 11
surah_name_ar: هود
surah_name_translit: Hūd
file_type: empirical-profile
date_last_updated: 2026-05-07
phase: B+
verdict: COMPLETE — Q 11 sits in iʿjāz-al-fawāṣil-leaning sub-cell (high rhyme entropy, NULL outlier-strength, low canonical-adjacency cost); UAS rank 88/114 (bottom-third); whole-surah architecture is internal block-variety not corpus-distinctness
---

# Q 11 Hūd — Empirical Profile


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

All metrics computed from canonical text variants under the project's
default rules-tuple `(no-tashkeel, orthographic-token, graphemes,
basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)`. Where rhyme/phoneme
analysis is run on min-tashkeel or full-tashkeel, that is flagged inline.
Numerical claims trace to JSON paths under `findings/phase-b-hypotheses/csv/`.

## 1. Snapshot table

| Metric | Q 11 value | Source |
|:--|:--|:--|
| n_verses | 123 | `quran-text/quran-no-tashkeel.json` |
| Word count (no-tashkeel) | 2,083 | computed |
| Letter count (no-tashkeel) | 7,954 | computed |
| Position s | 11 | canonical |
| Revelation order (al-Suyūṭī) | 52/114 | `data/revelation-order.csv` row 52 |
| **UAS** | **−1.4569**, rank **88/114** | `csv/h-new-840.json` `all_uas[surah=11]` |
| **Outlier-strength Δ_pct** | **−4.88 pp**, classification `NULL`, p_greater=0.2041 | `csv/h-new-590.json` `all_surahs_results[X=11]` |
| **iʿjāz sig_A** | +0.5935, **rank 46/114** | `csv/h-new-750.json` `per_surah[surah=11]` |
| **iʿjāz sig_B** | +1.1337, **rank 25/114** | same |
| z_rhyme_entropy | +1.7505 | same |
| z_mean_content_distance | +1.1570 | same |
| z_local_cohesion | −0.6168 | same |
| Mean FR-content distance to corpus | 1.0407 | same (`mean_content_distance`) |
| Local cohesion (intra-window) | 1.0654 | same (`local_cohesion`) |
| **Rhyme entropy (nats)** | **1.7365** | same |
| Top final letter | ن (nūn) | same |
| Top-letter fraction | 0.4553 (45.5%) | same |
| Q10→Q11 canonical-adjacency δ | 0.02992, fraction-residual 0.0036 (cheap) | `csv/h-new-720.json` `per_adjacency[s=10]` |
| Q11→Q12 canonical-adjacency δ | 0.03536, fraction-residual 0.0043 (cheap) | `csv/h-new-720.json` `per_adjacency[s=11]` |

## 2. UAS decomposition

`UAS = z(|outlier|) − w·z(max_neighbor_TSP_cost) + z(|sig_A|)` (per
[[h-new-840-unified-architectural-score|H-NEW-840]] §3 method).

For Q 11:
- `abs_outlier = 4.88` (small magnitude → low z; depresses UAS)
- `max_cost = 0.0354` (low magnitude → low z; depresses UAS)
- `abs_ijaz = 0.5935` (moderate magnitude → moderate z)

Composite: **UAS = −1.457**, **rank 88/114** (bottom third).

Q 11 fails to register in the "structural-iʿjāz" upper-tail (Q 33, Q 1, Q 2,
Q 9 are top). Q 11 is also far from "theological-iʿjāz" anchors (Q 112 the
FR-centroid). It sits in the **architectural middle-bottom** — the surah is
neither corpus-anchoring nor corpus-distinct. **The architectural signature
of Q 11 is INTERNAL** (per-block rhyme-pattern, per-block formula-templating,
narrative anthology structure — see Q011-F-01 and Q011-F-05 in 06-novel-findings.md)
**rather than whole-surah-distinctive**.

## 3. Outlier-strength spectrum (H-NEW-590) — null

Per [[h-new-590-outlier-spectrum|H-NEW-590]], Q 11's outlier-strength
**Δ_pct = −4.88 pp** with p_greater = 0.2041 (one-sided permutation upper),
classified `NULL`. Q 11 does NOT register as a corpus-significant outlier.

Comparison with the ALR cluster:
- Q 10: Δ_pct = +14.86 pp, classification `STRONG_OUTLIER`
- Q 11: Δ_pct = **−4.88 pp**, `NULL`
- Q 12: Δ_pct = +9.05 pp, `WEAK_OUTLIER`
- Q 14: Δ_pct = −4.28 pp, `NULL`
- Q 15: Δ_pct = +5.51 pp, `WEAK_OUTLIER`

**Within ALR-5, Q 11 is one of the two NULLs (alongside Q 14).** This is
itself an architectural fact: the ALR cluster contains two strong outliers
(Q 10, Q 12), two weak outliers (Q 14 marginal NULL, Q 15), and one
unambiguously NULL (Q 11). The **prophet-anthology** surah is not
corpus-distinct in its content-distance signature — it derives its identity
from internal narrative replication of a templated formula
(see Q011-F-01).

## 4. iʿjāz signatures (H-NEW-750)

Q 11 has **moderately positive sig_A (+0.5935, rank 46/114)** — it sits
near the corpus median. The two contributing z-scores:
- z_rhyme_entropy = **+1.7505** (high — Q 11 is rhyme-diverse)
- z_mean_content_distance = +1.1570 (high — content-distinct from corpus mean)

These two z-scores are anti-correlated under the [[h-new-730-content-rhyme-anticorrelation|iʿjāz anti-twin lock]]
(window-level r ≈ −0.86). Q 11 violates the typical anti-correlation by
being elevated on BOTH simultaneously — this is a sign that Q 11 is
**multi-mode** rather than single-mode iʿjāz: high rhyme diversity from
multi-block narrative variety + high content distinctness from
prophet-anthology vocabulary.

sig_B = +1.1337, rank 25/114 — Q 11 is in the top quartile on sig_B.
sig_B captures pure rhyme-entropy + corpus-distance without the
anti-correlation correction; Q 11's high standing on sig_B confirms that
the corpus-positions of rhyme-diversity and content-distance are both
genuinely high (rather than averaging to median by sig_A's anti-correlation
correction).

## 5. Rhyme structure (H-NEW-700)

Final-letter distribution across Q 11's 123 verses (`csv/h-new-700.json`
`rhyme.rhyme_letter_diagnostics[surah=11]`, computed from
`quran-min-tashkeel.json`):

| Final letter | Count | % |
|:--|:-:|:-:|
| ن (nūn) | 56 | **45.5%** |
| د (dāl) | 23 | 18.7% |
| ب (bāʾ) | 13 | 10.6% |
| ر (rāʾ) | 11 | 8.9% |
| م (mīm) | 5 | 4.1% |
| Other 8 letters | 15 | 12.2% |

**Rhyme entropy = 1.7365 nats** (Shannon). Compare ALR cluster:
- Q 10: 0.358 (low — single-rāwī)
- Q 11: **1.7365** (highest in ALR-5)
- Q 12: 0.838
- Q 14: 1.058
- Q 15: 0.538

Q 11 is the **most rhyme-diverse ALR surah by a substantial margin**.
This is mechanistically consistent with Q 11's anthology structure:
each prophet-block carries its own characteristic fāṣila pattern
(Hūd-block: -ūd / -īd; Shuʿayb-block: -mīm / -nāḥ; Mūsā-coda:
back-to-nūn). The rhyme-entropy is INTERNAL DIVERSITY across blocks,
not corpus-distance.

## 6. Phoneme density (H-NEW-700, full-tashkeel)

Per [[h-new-700-phonological-compression-tail|H-NEW-700]], surahs at s=11
sit pre-kink (kink at s≈75 for phoneme); Q 11 should NOT be in the
phoneme-compression-tail. Q 11's mean phoneme distance to corpus is
near the head-mushaf baseline (≈ 0.001 floor); no phoneme-axis surprise.

## 7. Canonical-adjacency cost (H-NEW-720)

| Adjacency | δ_TSP | fraction-residual | Rank in 113 |
|:--|:--|:--|:--|
| Q 10 → Q 11 | 0.02992 | 0.0036 | rank 82/113 (cheap) |
| Q 11 → Q 12 | 0.03536 | 0.0043 | rank 77/113 (cheap) |

Both Q 11's mushaf-edges are **CHEAP** (low TSP-residual). This means
Q 10 → Q 11 → Q 12 is a **near-optimal sub-path** — the mushaf placed Q 11
in a position consistent with FR-cosine optimization. This contrasts with
expensive transitions (e.g., Q 32 → Q 33 at residual 4.4%, cross-finding-026
top-3). Q 11's mushaf-position is not a mushaf-residual contributor.

The CHEAPNESS of Q 11's both edges INSIDE the ALR cluster (Q 10, Q 12 are
both ALR siblings) is consistent with H-NEW-97's name-letter-joint finding
that ALR cluster is content-coherent at the local-adjacency scale.

## 8. ALR-cluster cohesion (Q011-F-03 finding) — NULL

[[Q011-F-03|Q011-F-03]] tested whether Q 11's mean FR distance to its 4
ALR-strict siblings {Q 10, Q 12, Q 14, Q 15} is strictly less than its
mean distance to the 20 nearest-length non-ALR surahs.

Pre-registered direction: Q 11 closer to ALR (T < 0). Result:
- Mean FR(Q 11, ALR-siblings) = **0.9043**
- Mean FR(Q 11, length-matched non-ALR-20) = **0.9548**
- T_obs = **−0.0505** (DIRECTION-MATCHED)
- Permutation p_lower (10,000 perms, seed 20260507) = **0.2448**

**Verdict: NULL** at α=0.05. Direction-matched (Q 11 IS closer to ALR
siblings on average) but the effect doesn't survive the length-matched
permutation null. The 00-overview §9 post-hoc t-test signal (Δ=0.142
ALR vs non-ALR) is **not corroborated** under the stronger
length-matched permutation framework. Honestly published.

This means: Q 11's ALR pull-in is real in direction but weak in magnitude.
It is not architecturally distinguishable from a length-matched non-ALR
draw at α=0.05. The H-NEW-97 PROPHET_PERSON name-class signature stands
(p_mc=0.006), but the **content-axis ALR cohesion** does NOT survive
length-controlled testing.

## 9. Architectural type classification

Per [[cross-finding-026-iʿjāz-architecture|cross-finding-026]] §5 typology:

- **Structural-twin-pair** (Bāqillānī-style): expensive adjacency neighbor + high outlier strength. **Q 11 fails** — both adjacencies cheap, outlier NULL.
- **iʿjāz-al-fawāṣil-pure** (al-Bāqillānī rhyme-architecture): high rhyme-entropy + corpus-distinct outlier. **Q 11 partial** — high rhyme-entropy YES (z=+1.75), but outlier NULL.
- **theological-iʿjāz** (al-Khaṭṭābī): low UAS + high *thuluth-al-Qurʾān* status. **Q 11 partial** — low UAS yes (rank 88), but no *thuluth* tradition associates Q 11.
- **anti-iʿjāz-by-iteration** (proposed sub-cell): high rhyme-entropy WITHOUT outlier-strength + cheap adjacencies + multi-block internal-templated-formula. **Q 11 full member**.

Q 11's distinctive architecture is **NOT corpus-anchoring (low UAS), NOT
corpus-disrupting (cheap adjacencies), but INTERNALLY-REPLICATED**
(formulaic-lattice via Q011-F-01). This is a **fourth type**: the surah's
*iʿjāz* is in its **internal compositional iteration**, not in its
relationship to corpus context.

This sub-classification is queued for cross-finding integration.

## 10. Position in compression-tail laws

Q 11 is at s=11 — **head-mushaf zone**, well before the s=50 kink for
content-compression and the s=75 kink for phoneme-compression.

| Law | Predicted at s=11 | Q 11 observed | Match |
|:--|:--|:--|:--|
| d̄_content (s) ≈ 0.96 (head-zone) | 0.96 | **1.0407** | head-elevated (z=+1.16) |
| d̄_rhyme (s) ≈ 0.36 (head-zone) | 0.36 | rhyme-entropy 1.7365 (multi-rhyme) | high (z=+1.75) |
| d̄_phoneme (s) ≈ 0.001 (head-zone) | 0.001 | head-baseline | matched |
| Verse-length kink-50 | head pre-kink | n=123 (long, head-zone) | matched |

Q 11 is HEAD-ZONE on length and phoneme. On content-distance and rhyme-entropy
it is **elevated above the head-zone baseline** — these are the dimensions
where Q 11 stands out internally (not by violation of compression-tail laws,
but by sitting in the upper tail of the head-zone distribution).

## 11. Honest limits

- The 00-overview §9 ALR-pull-in signal is post-hoc t-test; under
  Q011-F-03's pre-registered length-matched perm null, it does not
  survive at α=0.05. We declare ALR-cohesion as DIRECTIONAL but NOT
  CONFIRMED for Q 11.
- The 4-axis classification (anti-iʿjāz-by-iteration) is a synthetic label
  introduced in this profile; it requires cross-finding ratification before
  promotion. Status: NOMINATED for cross-finding follow-up.
- The Q 11 content-distance elevation (z=+1.16) is real but modest —
  not a "max" in any axis. It contributes to sig_A as a moderate-positive,
  but not as a corpus-anchoring signal.
- Q 11's high sig_B rank (25/114) is partly an artifact of high rhyme-entropy
  + high content-distance combined: sig_B doesn't apply the anti-correlation
  correction. The truer architectural-significance number is UAS rank 88.

## 12. Cross-references to per-finding files

- [[h-new-111-fisher-rao-mushaf|H-NEW-111]] — FR matrix used for §8 ALR test.
- [[h-new-590-outlier-spectrum|H-NEW-590]] — Q 11 NULL classification.
- [[h-new-700-phonological-compression-tail|H-NEW-700]] — rhyme + phoneme.
- [[h-new-720-canonical-adjacency-cost|H-NEW-720]] — Q10-Q11 + Q11-Q12 cheap.
- [[h-new-750-per-surah-iʿjāz-signature|H-NEW-750]] — sig_A=+0.594, sig_B=+1.13.
- [[h-new-840-unified-architectural-score|H-NEW-840]] — UAS rank 88.
- [[h-new-97-name-letter-joint|H-NEW-97]] — ALR PROPHET_PERSON 4/5 (Q 11 a member).
- [[h-new-270-hud-template-lattice|H-NEW-270]] — Q 11 wa-ilā-akhāhum lattice (depth-12 z=∞).
- [[h-new-940-prophet-order-conservation|H-NEW-940]] — Q 11's prophet-order in Hūd-narrative (Nūḥ → Hūd → Ṣāliḥ matches consensus τ=+1.0).
- [[Q011-F-01-wa-ila-akhahum-corpus-share|Q011-F-01]] — corpus-share of formula-lattice.
- [[Q011-F-03-alr-cluster-fr-cohesion|Q011-F-03]] — ALR-pull-in NULL.

*Bismillāhi al-Raḥmāni al-Raḥīm.*
