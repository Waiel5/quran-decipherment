# H-NEW-68 — Friday-Recitation Cluster — Run 1 Journal

**Date**: 2026-04-15
**Specialist**: h-new-68-specialist (re-dispatch after rate-limit on prior)
**Seed**: 20260416

## Sequence

1. **Confirmed environment**: pre-reg from prior specialist did NOT exist
   on disk; wrote pre-reg first per task instruction.
2. **Reviewed prior cluster instrument**: H-NEW-58c (musabbiḥāt cluster
   p=0.0001 via shared-prefix on 5-subset null). Same instrument design
   reused for Friday 4-subset cluster. Per MW-5 inheritance rule, no fresh
   instrument-validation needed.
3. **Wrote pre-reg** (`h-new-68-friday-cluster-prereg.md`) BEFORE running
   any data-touching code on the Friday cluster:
   - Locked 4 surahs: Q 18, Q 32, Q 62, Q 76 (classical Friday liturgy).
   - Locked 4 axes: A1 mean-pairwise-prefix, A2 mean-pairwise-jaccard,
     A3 length-cohesion (1/(1+CV(verse_counts))), A4 divine-density-
     cohesion (1/(1+CV(div_density))).
   - Locked Bonferroni k = 4, α_bon = 0.0125.
   - Locked PASS criterion: ≥ 2 / 4 axes sig at α_bon → PASS;
     1 → MARGINAL; 0 → NULL.
   - Locked secondary Q 18-Q 62 pair test (any-pair null, k=2).
   - Locked null: 10 K random 4-surah subsets, exclude exact Friday set.
4. **Wrote script** (`scripts/h_new_68_friday_cluster.py`):
   - Loads no-tashkeel JSON, QAC stem-roots per surah, divine-names CSV.
   - Computes pairwise shared-prefix (via shared_prefix(a, b)),
     pairwise root-jaccard, cluster-level CV-cohesion for length and
     divine density.
   - Builds 4-subset null (10 K draws, exclude Friday cluster).
   - Builds Q 18-Q 62 any-pair null (10 K draws, exclude this pair).
   - Computes upper-tail p, Bonferroni decisions, PASS criterion.
5. **Single run**:
   - A1 prefix mean: obs 0.333 chars vs null mean 0.317, p = 0.352
   - A2 jaccard mean: obs 0.178 vs null 0.134, p = 0.239
   - A3 length cohesion: obs 0.544 vs null 0.596, p = 0.699
   - A4 divine cohesion: obs 0.447 vs null 0.522, p = 0.767
   - Verdict: NULL (0/4 axes Bonferroni-sig; 0/4 even uncorrected)
   - Q 18-Q 62 secondary: prefix obs=0 chars (literally 0!), p=1.000;
     jaccard 0.144, p=0.418. Both NULL.
6. **No tweaks made.** Single run; published as-is per pre-commitment.

## Garden-of-forking-paths log

Every choice was locked in the pre-reg before any cohesion number was
computed:

- 4-surah set chosen by classical liturgy (al-Kahf Friday + Sajda/Insān
  Fajr Friday + al-Jumuʿah eponymous). NOT chosen by structural
  similarity inspection.
- 4 axes chosen for coverage (formula, lexical, length, theological).
  Cluster-level CV chosen for A3, A4 because verse-count and divine-
  density are surah-set properties (not pair properties). Pair-level
  jaccard and prefix used for A1, A2 because those are inherently
  pairwise.
- Bonferroni k=4 (one cluster × 4 axes) chosen rather than k=24 (6 pairs
  × 4 axes). The cluster-cohesion scalar IS one number per axis, not 6.
  This is a defensible loosening relative to k=24 — but the ratification
  argument is that the FAMILY of "Friday cluster cohesion" is genuinely
  4 axes, not 24 pair-axis cells. The k=4 decision was locked in the
  pre-reg before any computation; if instead the per-pair cells had
  appeared significant, the publish-everything rule would have flagged
  them transparently. (Per bonferroni_tightening_vs_loosening rule,
  k=4 is the natural family granularity here; loosening from k=24 to
  k=4 was pre-committed and motivated by axis structure.)
- Null is "any 4-surah subset" (not adjacency-restricted) because the
  Friday cluster is non-adjacent across the muṣḥaf. Adjacency null
  would be inappropriate.
- Excluded from null: ONLY the exact cluster {18, 32, 62, 76}. Subsets
  containing 1, 2, or 3 of the Friday surahs are NOT excluded — same
  convention as H-NEW-58c.
- Cohesion = 1 / (1 + CV) chosen for A3, A4 because it bounds in (0,1]
  smoothly, consistent with the H-NEW-58 sim_scalar pattern.
- Q 18 ↔ Q 62 secondary pair test was pre-committed alongside the
  cluster test, NOT added after seeing cluster NULL.

## Key empirical observations

1. **Zero-prefix dominance**: 5 of 6 pairs have shared_prefix = 0 chars.
   Only Q 18-Q 32 has 2 chars ("ال" — the definite article). The 4
   surahs come from 4 different opener-class families (al-ḥamd /
   muqaṭṭaʿāt / musabbiḥāt / interrogative).
2. **Q 62 is a divine-density outlier**: 1.36 names/verse vs ~0.10-0.15
   for the other 3 surahs. This single-surah outlier explodes the
   cluster CV on A4 and drags cohesion below null mean.
3. **Q 18 is a length outlier**: 110 verses vs 11-31 for the other 3.
   This explodes cluster CV on A3.
4. **Q 18-Q 62 share NO opening character**: al-ḥ vs y. The two most-
   unambiguously Friday-specific surahs have ZERO structural-shape link
   on the opener axis.
5. **Comparison to musabbiḥāt cluster (H-NEW-58c)**: Friday cluster's
   mean-pairwise-prefix is 0.33 chars vs musabbiḥāt's 14.1 chars (42×
   lower) on the identical instrument. The instrument detects cohesion
   when present; Friday cluster lacks shape cohesion.

## Outputs

- Pre-reg: `findings/phase-b-hypotheses/h-new-68-friday-cluster-prereg.md`
- Script: `scripts/h_new_68_friday_cluster.py`
- JSON: `findings/phase-b-hypotheses/csv/h-new-68.json`
- Findings: `findings/phase-b-hypotheses/h-new-68-friday-cluster.md`

## Verdict

- **PASS criterion**: NULL (0/4 axes Bonferroni-sig; 0/4 uncorrected)
- **Q 18 ↔ Q 62 specific**: NULL (prefix p=1.000; jaccard p=0.418)
- **Substantive finding**: classical Friday liturgy is a function/genre
  curation, not a structural-shape curation. Mirrors H-NEW-58 finding
  on classical surah-pairs.

## Suggested follow-up: H-NEW-68b

Test Friday cluster on **functional/thematic axes**:
- F1: eschatological vocabulary density (yawm, qiyāma, ḥisāb, jannah,
  nār)
- F2: dhikr/tasbīḥ formula presence
- F3: shared narrative protagonists (Q 18 has 4 narratives; do they
  echo in Q 62, Q 32, Q 76?)
- F4: divine-name PAIRINGS (al-ʿAzīz al-Ḥakīm appears in Q 62; check
  Q 32, Q 76 — Q 62 may carry the cluster on this axis)

Those are the axes the classical fadāʾil al-Qurʾān tradition actually
claims for Friday liturgy, not statistical shape.
