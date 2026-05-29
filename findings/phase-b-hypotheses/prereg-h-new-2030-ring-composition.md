---
finding_id: h-new-2030
title: "Within-surah ring-composition / chiastic-symmetry detection"
specialist: h-new-2030-ring-composition-specialist
date_prereg: 2026-05-29
seed: 20260509
perms: 10000
bonferroni_k: 114
bonferroni_family: h-new-2030-per-surah-chiasm-scan
alpha_raw: 0.05
alpha_bon: 0.000438596
rules_tuple: "(no-tashkeel, QAC v0.4 STEM-ROOT tokens, content-root Jaccard, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)"
parent_findings:
  - H-NEW-185 (mushaf-level ring; this is the WITHIN-surah analogue, never tested)
  - H-NEW-189 (Medinan first-last inclusio — a 1-pair special case of chiasmus)
verdict_ceiling: "PASS (not CONFIRMED); CONFIRMED requires replication on an independent feature space (char-n-gram) and survival of the section-block secondary test"
---

# H-NEW-2030 — Within-surah ring-composition / chiastic-symmetry detection

## Motivation

Ring composition (chiasmus / concentric ABCB'A' symmetry, "the meaning in the
middle") is a documented feature of ancient Near-Eastern and Biblical texts and
has been claimed for the Quran by:

- **Raymond Farrin**, "Surat al-Baqara: A Structural Analysis" (*The Muslim
  World* 100, 2010; PDF at `data/literature/farrin-cuypers/2010-farrin-surat-al-baqara-structural-analysis.pdf`):
  Q 2 al-Baqara is a single nine-section concentric ring with the qibla-change
  pericope (2:142–152, pivot ≈ 2:143 "a middle nation") at the centre, and
  sections 1↔9, 2↔8, 3↔7, 4↔6 mirroring.
- **Michel Cuypers**, *The Composition of the Qur'an: Rhetorical Analysis*
  (2015; PDF at `data/literature/farrin-cuypers/2015-cuypers-composition-of-the-quran-rhetorical-analysis.pdf`)
  and *Le Festin* (2007), applying "Semitic rhetoric" to argue Q 5 al-Māʾida is
  ring-structured.
- **Nicolai Sinai**, "Going Round in Circles" (*JQS* 19, 2017; PDF at
  `.../2017-sinai-going-round-in-circles-jqs.pdf`): a sceptical review arguing
  many proposed rings are loose / unfalsifiable.

The project has **never** tested ring-composition WITHIN surahs at verse
granularity. H-NEW-185 tested a ring at the mushaf (surah-ordering) level; this
is the within-surah analogue. H-NEW-189 found Medinan first↔last inclusio — that
is precisely the outermost (i=1) pair of a chiasm, so a corpus chiasm-scan is
the natural generalisation of H-NEW-189.

## Operationalisation (LOCKED before computation)

For each surah s with n verses:

1. **Verse content-root set** R_i = the set of QAC v0.4 STEM-level ROOT codes
   attested in verse i (from `data/morphology/quranic-corpus-morphology-0.4.txt`,
   field `ROOT:` on STEM segments only; particles / prefixes without ROOT are
   excluded). Basmala (Q 1:1 only, per rules-tuple) included for Q 1; the
   standalone pre-surah basmala of other surahs is NOT a numbered verse and is
   excluded.

2. **Verse-pair similarity** = Jaccard index
   J(R_i, R_j) = |R_i ∩ R_j| / |R_i ∪ R_j|, with J = 0 if both sets empty.

3. **Mirror pairs**: for a surah of n verses, the mirror of verse i is verse
   (n+1−i). The set of mirror pairs is {(i, n+1−i) : 1 ≤ i < n+1−i}, i.e.
   ⌊n/2⌋ disjoint pairs (the central verse of an odd-n surah pairs with itself
   and is excluded — self-Jaccard = 1 would inflate the score).

4. **Chiasm-score** C(s) = mean over the ⌊n/2⌋ mirror pairs of J(R_i, R_{n+1−i}).

## Hypothesis (DIRECTION LOCKED — one-sided)

**Primary H1**: For at least **3** surahs (of the 114), the observed
chiasm-score C(s) is GREATER than expected under within-surah verse-order
permutation, at the Bonferroni-corrected level α_bon = 0.05/114 = 4.386×10⁻⁴
(one-sided, mirror-pair similarity > permuted-order similarity).

**Direction**: C_observed > C_null (mirror pairs MORE similar than random
verse-order would produce). A result in the opposite direction (mirror pairs
LESS similar than random — "anti-chiasm") is a pre-commit-relevant outcome and
will be published as NULL with full prominence; it does NOT count toward H1.

**Targeted secondary tests (pre-specified, NOT part of the k=114 family)**:
- **S1 — Farrin's Q 2**: is C(Q2) significant at raw α=0.05? Reported with the
  honest caveat that Farrin's claim is *section-level* (9 thematic blocks), so a
  verse-level NULL does not by itself refute the block-level claim. A block-level
  variant (S3) is run to address this directly.
- **S2 — Cuypers' Q 5**: is C(Q5) significant at raw α=0.05? Same caveat.
- **S3 — block-level chiasm (Farrin/Cuypers fairness control)**: partition each
  surah into B equal contiguous blocks (B ∈ {5, 7, 9}, pre-specified), pool the
  root-set of each block, and test block-mirror Jaccard (block b ↔ block B+1−b)
  vs. block-order permutation. This is the granularity at which Farrin/Cuypers
  actually argue. Reported for Q 2, Q 5, and corpus-wide enrichment, at raw
  α=0.05 each cell (post-hoc-noticed-cap does not apply — S3 is pre-registered
  here). S3 is exploratory-confirmatory and reported separately from H1.

## Null distribution (MW-2)

For each surah, randomly permute the verse order (Fisher–Yates) and recompute
the chiasm-score under the SAME mirror-pairing rule; repeat **10,000** times;
seed **20260509** (numpy default_rng, surah-specific child seed = base_seed +
surah_id to guarantee independence and reproducibility). One-sided p-value =
(1 + #{C_perm ≥ C_obs}) / (10001). Permuting verse order destroys any
positional (chiastic) structure while exactly preserving the multiset of
verse-root-sets and the surah length — the correct null for "is the ORDER
chiastic". Surahs with n < 4 (Q 103, Q 108, Q 110) have ≤1 mirror pair and ≤2
distinct permutation outcomes; they are reported but flagged DEGENERATE and
excluded from the "significant" count.

## Success / failure criteria

- **PASS (H1 supported)**: ≥3 surahs with p_one-sided < α_bon = 4.386×10⁻⁴ in
  the chiastic direction.
- **PARTIAL**: 1–2 surahs below α_bon, OR ≥3 surahs below raw α=0.05 but <3
  below α_bon.
- **NULL**: 0 surahs below α_bon AND the corpus-wide distribution of chiasm
  z-scores is centred at ≈0 (no systematic chiastic tendency). Published with
  equal prominence.

## MW protections

- **MW-1 (instrument-prior)**: Jaccard on QAC STEM-ROOT sets, mirror-pair mean,
  fixed here before any computation.
- **MW-2 (corpus-prior)**: 10,000 within-surah verse-order permutations.
- **MW-3 (alternative-models)**: secondary block-level model S3 (B∈{5,7,9}) as
  an alternative aggregation; also report a cosine-on-root-count variant as a
  robustness check (does not change verdict).
- **MW-4 (over-fitting)**: no fitted free parameters in the primary test.
- **MW-5 (replication)**: re-run the top surahs on a char-4-gram feature space
  (independent of QAC roots) before any CONFIRMED upgrade; PASS-ceiling until then.
- **MW-6 (instrument-control)**: the permutation null IS the matched control
  (same verse-root multiset, order destroyed). Additionally, mean p across all
  114 surahs should be ≈0.5 under a true global null — reported as a sanity check.
- **MW-7 (post-hoc cap)**: any surah noticed as chiastic that was not in the
  pre-specified target set (Q 2, Q 5) carries the Bonferroni-corrected bar; no
  post-hoc α relaxation.

## Anti-confirmation commitment

The honest prior, given Sinai 2017, is that **most surahs are NOT chiastic** and
that verse-level chiasmus is a demanding bar most surahs will fail. The question
is strictly whether SOME surahs reach law-strength. A corpus-wide NULL is a
fully publishable, equal-prominence outcome and would empirically support
Sinai's scepticism over the strong Farrin/Cuypers ring program.
