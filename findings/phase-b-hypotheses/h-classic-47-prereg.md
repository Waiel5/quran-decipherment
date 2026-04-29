---
finding_id: h-classic-47
phase: B
status: PRE-REGISTERED — computational-tester self-pre-reg per PRE-REG-STANDARD-04
pre_registered_by: computational-tester (2026-04-12)
registration_date: 2026-04-12
parent_task: #98
spec_source: findings/phase-b-hypotheses/h-classic-44-to-49-spec.md §H-CLASSIC-47
distinct_from: task #21 (cross-surah seam-Jaccard at the SURAH-pair scale; H-CLASSIC-47 is the verse-pair-WITHIN-surah scale)
rules_tuple: (no-tashkeel, root-level via QAC, hafs-kufan, mashriqi)
seed: 20260414
sided_test: one-sided positive (al-Biqāʿī Naẓm al-Durar explicit direction + general munāsaba literature concur)
direction_prereg_source: al-Biqāʿī Naẓm al-Durar fī tanāsub al-āyāt wa-l-suwar (LOCKED before run); seconded by al-Suyūṭī Itqān nawʿ 62 al-tanāsub bayna al-āyāt
priority_surahs: [2, 3, 4, 5]
negative_control_surahs: [TBD-matched-Meccan]
bonferroni_k: 6   # within H-CLASSIC-44..49 family
alpha_bon: 0.0083   # = 0.05 / 6
internal_k: 4   # 4 priority surahs; pass rule is ≥3 of 4 (absorbed by family Bonferroni per spec)
null_publishable: true
positive_publishable: true
---

# H-CLASSIC-47 — al-Biqāʿī verse-pair within-surah seam-Jaccard density

## Why this pre-registration exists

al-Biqāʿī's *Naẓm al-Durar fī tanāsub al-āyāt wa-l-suwar* is the
locus classicus of the *local-munāsaba* doctrine: every adjacent
verse pair is thematically and lexically linked, with the seam
between verses being where *munāsaba* operates most densely. He
distinguishes this verse-pair-level claim from the whole-surah
*tanāsub al-suwar* claim (which task #21 tested at the inter-surah
seam-Jaccard level and is logged in the effect-size inventory as
T-002 adjacent-pair seam-munāsaba PASS, z = +10.7).

H-CLASSIC-47 tests the **complementary spatial scale** — adjacent
verse pairs *within a single surah* — on the four longest Medinan
surahs (al-Baqara Q 2, Āl ʿImrān Q 3, al-Nisāʾ Q 4, al-Māʾida Q 5)
where al-Biqāʿī's commentary on verse-by-verse linkage is most
explicit and detailed. These four surahs are pre-committed before
script execution.

This is a **distinct test** from task #21:
- Task #21 / T-002: SURAH-pair adjacent-Jaccard. Each "pair" is two
  consecutive surahs (Q2↔Q3, Q3↔Q4, etc.); 113 surah-pairs total;
  found 17 surah-pair matches vs 2.01 null. Operationalized at the
  inter-surah level.
- H-CLASSIC-47: VERSE-pair within-surah Jaccard. Each "pair" is two
  verses of the SAME surah at distance k. We test at k=1 (adjacent)
  vs k≥3 (distant), within each of 4 specific surahs. Operationalized
  at the intra-surah level.

The two scales are theoretically orthogonal: T-002 PASS does not
imply H-CLASSIC-47 PASS, and vice versa.

## Pre-registered hypotheses

**H-CLASSIC-47-PRIMARY (locked, one-sided positive):** for at least
3 of the 4 al-Biqāʿī-priority surahs (Q 2, Q 3, Q 4, Q 5), the
observed mean root-Jaccard at distance k=1 (adjacent verse pairs)
exceeds the 99th percentile of the within-surah verse-order
permutation null. Per spec, **internal pass rule is ≥ 3/4 surahs**;
the family Bonferroni k=6 absorbs this internal multiplicity.

**H-CLASSIC-47-SECONDARY (descriptive bucket means):** for each
priority surah, report mean Jaccard by distance bucket
{1, 2, 3-5, 6-10, 11+} both **with** and **without** stopword-root
removal. Monotone decay (1 > 2 > 3-5 > 6-10 > 11+) is reported but
not used as a Bonferroni-counted gate.

**H-CLASSIC-47-TERTIARY (negative control):** repeat the primary
test on 4 matched-length Meccan surahs (verse-count ≥ 100, NOT
priority-surah). Pre-committed control selection: pick the 4 longest
non-priority surahs in mushaf order (Q 7 al-Aʿrāf 206 verses, Q 26
al-Shuʿarāʾ 227 verses, Q 37 al-Ṣāffāt 182 verses, Q 6 al-Anʿām
165 verses). These should NOT show the same effect if the signal is
specifically al-Biqāʿī-anchored Medinan munāsaba; if they DO, the
finding is partially generalized away from the priority surah claim.

**Stopword-root removal**: the rasm-frequent function-word roots
will be removed in the "without-stopwords" condition. Locked list:
{Alh (= Allāh), kwn (= kāna/yakūnu), qwl (= qāla/yaqūlu),
Eml (= ʿamala), Amn (= āmana), llh (= function l/li/la-),
xlq (= khalaqa), Erf (= ʿarafa)}. NB: Alh is the divine name proper
and is not a "stopword" in the usual sense, but it dominates Quranic
adjacent-pair Jaccard in narrative chains; the comparison
"with-Alh vs without-Alh" is informative and pre-committed here.

## Pre-registered acceptance matrix (Bonferroni k=6 within H-CLASSIC-44..49 family, α_bon = 0.0083)

| Outcome                                                                                                     | Verdict                       |
|-------------------------------------------------------------------------------------------------------------|-------------------------------|
| PRIMARY ≥ 3/4 priority surahs pass per-surah 99th pctile permutation null AND TERTIARY ≤ 1/4 control surahs pass | **PASS — al-Biqāʿī verse-pair seam-Jaccard confirmed** |
| PRIMARY ≥ 3/4 priority surahs pass AND TERTIARY ≥ 2/4 control surahs ALSO pass                              | **PARTIAL — verse-pair effect is real but generalizes beyond priority surahs (not specifically Medinan-Biqāʿī)** |
| PRIMARY ≤ 2/4 priority surahs pass                                                                          | **NULL — al-Biqāʿī adjacent-verse seam-density falsified at verse-pair scale** |
| PRIMARY ≥ 3/4 BUT only with stopwords (Alh dominates) AND not without stopwords                             | **PARTIAL-DECONFOUNDED — effect is driven by formulaic/divine-name repetition, not semantic munāsaba** |

## No-fork protections

1. **Priority surahs LOCKED** to {Q 2, Q 3, Q 4, Q 5} before script
   run. No swap to "Q 6 or Q 9" if Q 5 fails. The 4 surahs are the
   spec-named al-Biqāʿī-priority set.

2. **Control surahs LOCKED** to {Q 6, Q 7, Q 26, Q 37} (the 4
   longest non-priority Meccan surahs in mushaf order with
   n_verses ≥ 100). Pre-committed deterministically before script
   run.

3. **Distance-1 LOCKED as primary scale.** Bucket scales (2, 3-5,
   6-10, 11+) reported descriptively but cannot rescue a failed
   primary.

4. **Stopword list LOCKED** to {Alh, kwn, qwl, Eml, Amn, llh, xlq,
   Erf}. With-vs-without is a planned comparison, not a post-hoc
   selection.

5. **Permutation null seed**: 20260414, 10,000 within-surah verse-
   order permutations per surah. Seed locked.

6. **Pass rule LOCKED to ≥ 3/4 priority surahs** (per spec). No
   swap to "any surah with z > X" or "weighted mean across surahs".

7. **Root extraction LOCKED to QAC v0.4 STEM-only token roots**,
   matching H-NEW-29 token sequence convention. Re-uses the QAC
   loader pattern from `scripts/h_new_29_root_cv.py` (lines 24-49).

## Pre-registered operationalization

1. **QAC root loading**: parse
   `data/morphology/quranic-corpus-morphology-0.4.txt` line by line.
   For each line whose feat field contains `STEM`, extract the
   `(sid:vid:wid:seg)` location and the `ROOT:xxx` field if present.
   Build per-verse multisets: `verse_roots[(sid, vid)]` = set of
   root strings (ignore None / function-word-only words). Words
   without a root (proper nouns without root annotation, or function
   particles) are dropped.

2. **Per-surah verse-root-set list**: for each of 8 surahs (4
   priority + 4 control), build an ordered list `verse_sets[i]` of
   root sets in mushaf order, indexed 1..n_verses.

3. **Two stopword conditions**:
   - **with-stopwords**: the full per-verse root set.
   - **without-stopwords**: with the LOCKED stopword list removed
     before computing Jaccard.

4. **Pairwise Jaccard at distance k**: for each unordered pair
   (i, j) with j-i = k (where 1 ≤ i < j ≤ n_verses), compute
   |verse_sets[i] ∩ verse_sets[j]| / |verse_sets[i] ∪ verse_sets[j]|.
   If both verses have empty root sets, Jaccard is undefined and
   the pair is dropped.

5. **Bucket means (descriptive)**: for distance buckets {1, 2, 3-5,
   6-10, 11+}, compute the mean Jaccard across pairs falling in
   each bucket, separately for each surah and each stopword
   condition.

6. **Within-surah permutation null (PRIMARY)**: for each priority
   and control surah:
   - Compute observed mean Jaccard at distance k=1.
   - Permute the verse-root-set order uniformly within the surah
     10,000 times (seeded). For each permutation, recompute
     mean Jaccard at distance k=1.
   - Take the 99th percentile of the 10,000 null values.
   - The surah PASSES if observed > 99th percentile (one-sided
     positive).

7. **Pass count**: count how many of the 4 priority surahs PASS
   under the with-stopwords condition AND under the
   without-stopwords condition. Also count for the 4 control surahs.

8. **Verdict routing**: per the acceptance matrix above. Both
   stopword conditions must show ≥ 3/4 priority pass for the full
   PASS verdict. If only with-stopwords passes, route to
   PARTIAL-DECONFOUNDED.

## Outputs

- **JSON**: `findings/phase-b-hypotheses/csv/h-classic-47.json`
- **Narrative**: `findings/phase-b-hypotheses/h-classic-47.md`
- **Script**: `scripts/h_classic_47_biqai_seam.py`

## Compute estimate

- QAC parse: ~2 sec.
- Per-surah pairwise Jaccard:
  - Q2 (286 verses): 40,755 pairs.
  - Q3 (200): 19,900 pairs.
  - Q4 (176): 15,400 pairs.
  - Q5 (120): 7,140 pairs.
  - Q6 (165), Q7 (206), Q26 (227), Q37 (182): similar magnitudes.
  - Total: ~150k pairs × 2 stopword conditions = 300k Jaccard
    computations. Trivial: < 1 sec.
- Per-surah permutation null:
  - 10,000 permutations × 8 surahs × 2 conditions × ~280 distance-1
    pairs per perm × O(set ops) ~ a few seconds per surah.
  - Estimated total: ~60-90 seconds.
- **Total wall time**: ~2-3 minutes.

## Seed

`20260414` (consistent with the H-NEW-35 / [[h-new-38-directed-pmi|H-NEW-38]] / H-CLASSIC-48
family). Sub-seeds: SEED+0 for Q 2 perm, SEED+1 for Q 3 perm, etc.
(deterministic per-surah sub-streams).

## Bonferroni accounting

- **k = 6** within H-CLASSIC-44..49 family per spec.
- **α_bon = 0.0083** (= 0.05 / 6).
- **Internal k=4 absorbed** by family-level Bonferroni per spec.
  The pass rule "≥ 3/4 surahs exceed per-surah 99th pctile" has
  binomial null probability of P(≥3 of 4 successes when p=0.01) =
  binom.sf(2, 4, 0.01) = 5.96e-6, well below α_bon = 0.0083 and
  Bonferroni-budget-respecting.

## Reverse-finding routing

H-CLASSIC-47 is one-sided. A PRIMARY ≤ 2/4 result is **NULL**, not
REVERSE — there is no "reverse finding" because root-Jaccard at
distance 1 cannot be meaningfully NEGATIVE (Jaccard is bounded
[0, 1]). A counter-prediction would be something like "adjacent
verses have systematically LOWER Jaccard than distant ones",
indicating *anti-munāsaba* — but this is not a classical claim and
is not pre-registered.

## Dispatch chain

1. computational-tester → authors this pre-reg (this file). **DONE.**
2. computational-tester → authors `scripts/h_classic_47_biqai_seam.py`
   per the operationalization above.
3. computational-tester → executes the script, writes JSON +
   narrative.
4. skeptical-auditor → audits compliance with this pre-reg.
5. integrator → integrates verdict into MASTER ledger.

## Pre-execution lock confirmation

This file is committed BEFORE the script is written. Any subsequent
deviation must be documented as a disclosed-not-amended deviation in
the narrative, NOT a silent post-hoc edit to this pre-reg. The seed,
priority surahs, control surahs, distance-1 primary scale, stopword
list, pass rule (≥ 3/4 with both stopword conditions), and
Bonferroni accounting are LOCKED.

## Data reuse disclosure

- Reuses QAC morphology loader pattern from
  `scripts/h_new_29_root_cv.py` (LOC_RE, ROOT_RE, STEM filter).
- Reuses `quran-text/quran-no-tashkeel.json` for verse counts /
  surah ordering reference.
- Does NOT reuse any T-002 / task #21 statistical machinery
  (different scale: verse-within-surah vs surah-pair-cross-surah).
- Does NOT reuse H-NEW-20 cached results.
- KS test, scipy not needed for this test (permutation null is
  pure-Python).
