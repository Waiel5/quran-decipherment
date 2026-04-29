---
finding_id: h-new-127
title: "Fisher-Rao fractal extension: verse-level path optimality within 5 surahs"
specialist: h-new-127-specialist
parent_finding: h-new-111
date_prereg: 2026-04-17
seed: 20260417
bonferroni_k: 5
bonferroni_family: h-new-127-verse-fisher-rao-fractal
alpha_bon: 0.01
alpha_raw: 0.05
direction_primary: "canonical verse-order L_canon < L_random (one-sided lower-tail) for ≥3 of 5 surahs at α_bon=0.01"
direction_secondary: "L_canon / L_2opt ratio distribution across the 5 surahs (descriptive)"
K_top_roots: 300
dirichlet_alpha: 0.5
length_control: "MW-1 via L1-normalization of per-verse distributions"
rules_tuple: "(no-tashkeel, QAC-STEM root tokens, QAC v0.4, basmala-counted-only-in-surah-1, mushaf verse order, Hafs-Kufan)"
perms: 10000
surahs_locked:
  - 2    # al-Baqara   (286 verses, longest, Medinan, muqaṭṭāʿat ALM)
  - 7    # al-Aʿrāf    (206 verses, Meccan-long, muqaṭṭāʿat ALMS)
  - 12   # Yūsuf       (111 verses, Meccan narrative, muqaṭṭāʿat ALR)
  - 36   # Yā-Sīn      (83 verses,  Meccan, muqaṭṭāʿat YS)
  - 55   # al-Raḥmān   (78 verses,  Meccan, refrain-heavy)
verdict_ceiling: "STRONG-REPLICATION if ≥3 of 5 PASS; NULL if ≤2 of 5 PASS"
---

# [[h-new-127-verse-fisher-rao-fractal|H-NEW-127]] — Fisher-Rao fractal extension at verse level

## Relationship to parent finding

[[h-new-111-fisher-rao-mushaf|H-NEW-111]] established that the 114-surah mushaf ordering is Fisher-Rao
information-geodesic-shorter than random permutations, within ~11% of
a TSP-approximate optimum. Verdict: PASS-DIRECTED (p < 10⁻⁴), novel
test, ceiling until independent replication.

[[h-new-127-verse-fisher-rao-fractal|H-NEW-127]] tests whether **the same optimality signature appears at the
verse level within individual surahs**. If the mushaf's global
Fisher-Rao optimality is a FEATURE of the text (intentional design,
whether human or otherwise), it is plausible that verse-within-surah
orderings also minimize inter-verse information-geometric path length.
A FRACTAL signature (same property at two scales) is strong evidence
against the "Uthmanic committee heuristic" null, since any committee
heuristic applied at surah level cannot reach inside surahs to re-order
verses — verse ordering predates the mushaf compilation by tradition.

Conversely, if the fractal signature is absent (≤2 of 5 surahs PASS),
the [[h-new-111-fisher-rao-mushaf|H-NEW-111]] effect likely reflects a surah-level-only property, and
the "intentional-global-geodesic" reading weakens.

## Hypothesis

**Primary (H1) — pre-committed, directional REPLICATION of [[h-new-111-fisher-rao-mushaf|H-NEW-111]]**:
For each of the 5 locked surahs, the canonical (mushaf) verse ordering
has Fisher-Rao path length `L_canon` strictly less than that expected
under uniform random permutation of verses within the same surah.
Acceptance: **≥3 of 5 surahs** pass individual one-sided lower-tail
test at `α_bon = 0.01` (Bonferroni-5).

**Secondary A (descriptive)**: Per-surah ratio `L_canon / L_2opt`,
where `L_2opt` is greedy-NN + 2-opt approximation of verse-TSP within
that surah. Reported for all 5 surahs; no formal test.

**MW-5 positive control**: For ONE locked surah (Q 55 al-Raḥmān, chosen
because its refrain structure makes length a strong correlate of
position), construct a length-sorted verse ordering (ascending by
verse token-length, excluding basmala). Confirm `L_length-sorted > L_canonical`.
This is a standard MW-5 "known-worse" positive control: if length-sorted
is NOT worse than canonical, the null is broken or MW-1 normalization is
failing. (Note: MW-5 in [[h-new-111-fisher-rao-mushaf|H-NEW-111]] was greedy-NN-from-surah-1 "known-better";
here we use length-sorted "known-worse" because at verse scale, verses are
so short that greedy-NN may not be reliably shorter than canonical.)

## Method (locked before any computation)

### Data

- Corpus: `/Users/grey/Downloads/quran/quran-text/quran-no-tashkeel.json`
  (Hafs-Kūfan, no tashkeel).
- Morphology: `/Users/grey/Downloads/quran/data/morphology/quranic-corpus-morphology-0.4.txt`
  (QAC v0.4 STEM segments with ROOT:XXX attributions).

### Locked surahs (5)

| # | Sura | Name       | Verses | Type    | Muqaṭṭāʿāt | Reason for inclusion |
|---|------|------------|--------|---------|-----------|----------------------|
| 1 | 2    | al-Baqara  | 286    | Medinan | الم       | longest sura; Medinan; legal–narrative hybrid |
| 2 | 7    | al-Aʿrāf   | 206    | Meccan  | المص      | Meccan-long; prophetic cycle narrative |
| 3 | 12   | Yūsuf      | 111    | Meccan  | الر       | Meccan narrative with a single-story arc |
| 4 | 36   | Yā-Sīn     | 83     | Meccan  | يس        | Meccan short-middle; "heart of Quran" trad. |
| 5 | 55   | al-Raḥmān  | 78     | Meccan  | —         | refrain-heavy (fa-bi-ayyi ālāʾi rabbikumā) |

These five span long/medium/short, Meccan/Medinan, narrative/legal/
hymnic, muqaṭṭāʿāt-opening and not. LOCKED BEFORE COMPUTATION.

### Feature space

- **K = 300 top roots** by global QAC-STEM frequency (across the ENTIRE
  Quran, not just per-surah). LOCKED. No post-hoc K tuning.
  - Rationale for K=300 vs [[h-new-111-fisher-rao-mushaf|H-NEW-111]]'s K=500: at verse scale, each
    verse has ≤ ~30 STEM tokens; K=300 is the max that still keeps
    per-verse support non-degenerate under Dirichlet smoothing
    without blowing up Dirichlet mass proportion.
- Each verse within a locked surah gets a raw STEM-root count vector
  over the K=300 roots.
- Dirichlet smoothing **α = 0.5** (Jeffreys prior) added to every
  count cell; THEN L1-normalized to get a probability vector on the
  K-simplex. MW-1 length-control is built in by normalization.
- Basmala policy: basmala appears only as verse 1 of surah 1 in the
  JSON (see loader.py docstring). None of the locked surahs is Q 1,
  so basmala is irrelevant here.

### Distance

Fisher-Rao angular distance (same as [[h-new-111-fisher-rao-mushaf|H-NEW-111]]):

    D_FR(p, q) = 2 · arccos( Σ_k sqrt(p_k · q_k) )

Clipped numerically to [0, π].

### Primary test (per surah)

For each locked surah s with n_s verses:

- `L_canon(s) = Σ_{i=1..n_s-1} D_FR(v_i, v_{i+1})`  in mushaf verse order.
- Null: 10,000 uniform random permutations of the n_s verses (seed
  20260417, same seed as [[h-new-111-fisher-rao-mushaf|H-NEW-111]]). `L_perm = Σ D_FR(π(v_i), π(v_{i+1}))`.
- `p(s) = (#{L_perm ≤ L_canon(s)} + 1) / (PERMS + 1)` (one-sided,
  lower-tail, +1 conservatism).
- Surah s **PASSes** iff `p(s) < α_bon = 0.01` (Bonferroni-5).

### Family verdict

- Count `n_pass = #{s : p(s) < 0.01}`.
- **STRONG-REPLICATION** if `n_pass ≥ 3`.
- **NULL** if `n_pass ≤ 2` (fractal hypothesis refuted at verse scale).

### Secondary A: geodesic-optimality ratio per surah

For each surah, compute `L_2opt(s)` via greedy-NN from each verse +
2-opt local search on the best greedy path (same algo as [[h-new-111-fisher-rao-mushaf|H-NEW-111]]).
Report `L_canon(s) / L_2opt(s)` descriptively; no formal test.

### MW-5 positive control

For Q 55 al-Raḥmān:
- Compute `L_length_sorted(55)` = path length of verses sorted by
  token-count (ascending).
- Require `L_length_sorted(55) > L_canon(55)`. If this fails, MW-5 is
  broken; report NULL-BROKEN and hold result in abeyance.
- Rationale: sorting verses by raw length ignores Fisher-Rao structure
  and should produce a path AT LEAST AS LONG AS canonical (typically
  longer). This is the "known-worse" direction; combined with the
  random-permutation null (which also should be longer than canonical
  on average), it gives a two-sided sanity check.

### MW-1 length residualization

Built into Dirichlet-smoothed L1 normalization: each verse's
probability vector sums to 1, regardless of verse token count. Total
verse length drops out.

## Pre-committed acceptance window

- **PER-SURAH PASS**: `p(s) < 0.01` (Bonferroni-5 of primary family).
- **FAMILY STRONG-REPLICATION**: n_pass ≥ 3 of 5.
- **FAMILY NULL**: n_pass ≤ 2 of 5.
- **Secondary A**: descriptive; report all 5 ratios.

## Garden of forking paths

- **Post-hoc origin disclosure**: This is a FRACTAL EXTENSION of
  [[h-new-111-fisher-rao-mushaf|H-NEW-111]], directionally pre-committed to REPLICATE (same direction:
  canonical < random). I have already VIEWED the [[h-new-111-fisher-rao-mushaf|H-NEW-111]] result
  (which passed at p<10⁻⁴). This is not post-hoc eyeballing of verse
  data — verse-level data has NOT been computed yet — but it is
  correlated-direction-to-parent. Per DISCIPLINE §post-hoc-noticed,
  the test is family-locked BEFORE the null runs; I apply
  Bonferroni-5 within this family; the PARENT-to-CHILD correlation
  does NOT inflate verse-level p-values because the feature space is
  different (verse-distributions ≠ surah-distributions) and the null
  is drawn independently (verse-perms ≠ surah-perms).
- **K=300 locked at pre-reg time**. Alternatives considered and
  rejected pre-result: K ∈ {100, 200, 500, 1000}. Chose 300 because:
  (i) at K=100, per-verse support is too sparse (median verse ~6
  STEM tokens post-top-K); (ii) at K=500, Dirichlet mass α·500 = 250
  overwhelms raw counts for short verses; (iii) K=300 gives α·K = 150
  which is in the same regime as the parent's α·K = 250 for K=500,
  scaling appropriately for the smaller per-verse token count.
- **5 surahs locked at pre-reg time**. The 5-surah selection was
  handed to me by team-lead; I accept it without modification. The
  surahs span length (78–286), type (Meccan/Medinan), muqaṭṭāʿāt
  presence, and genre (narrative/legal/hymnic) — no cherry-picking
  possible since I did not pick them.
- **Dirichlet α = 0.5** (Jeffreys): same as parent. Accepted, no
  tuning.
- **Distance = Fisher-Rao angular**: same as parent. Accepted.
- **PERMS = 10,000**: same as parent. Accepted.
- **Seed 20260417**: same as parent, ensures reproducibility.
- **MW-5 choice**: length-sorted "known-worse" rather than greedy-NN
  "known-better". Rationale: at verse-scale, greedy-NN may produce
  L_greedy < L_canon routinely (since verses are much shorter than
  surahs and distances are noisier), which would NOT validate the
  null — we need a CERTAINLY-WORSE control. Length-sorted ignores
  Fisher-Rao geometry entirely and should reliably score worse.

## Failure modes and how they would be reported

- MW-5 positive control fails on Q 55 → INSTRUMENT BROKEN, primary
  family result held in abeyance; publish null-broken finding.
- n_pass = 0 → STRONG NULL: fractal signature definitively absent;
  [[h-new-111-fisher-rao-mushaf|H-NEW-111]] is a surah-scale-only phenomenon.
- n_pass ∈ {1, 2} → WEAK NULL: fractal hypothesis refuted at
  pre-registered threshold; note which surah(s) passed and
  characterize them descriptively.
- n_pass ∈ {3, 4} → STRONG-REPLICATION: fractal hypothesis supported;
  [[h-new-111-fisher-rao-mushaf|H-NEW-111]] elevated from surah-only to multi-scale signature.
- n_pass = 5 → STRONG-REPLICATION+: fractal signature universal
  across the sampled 5 surahs.

## Deliverables

1. Pre-reg (this file).
2. Script `scripts/h_new_127_verse_fisher_rao.py` (seed 20260417, deterministic).
3. JSON `findings/phase-b-hypotheses/csv/h-new-127.json` with per-surah:
   L_canon, L_null_mean, L_null_quantiles, p-value, L_2opt, ratio.
4. Findings `findings/phase-b-hypotheses/h-new-127-verse-fisher-rao-fractal.md`.
5. Journal `journal/h-new-127-run-1.md`.
