---
finding_id: h-new-38
phase: B
status: PRE-REGISTERED — execution authored same-session, computational-tester self-pre-reg per PRE-REG-STANDARD-04
pre_registered_by: computational-tester (2026-04-13)
registration_date: 2026-04-13
parent_task: #75
rules_tuple: (no-tashkeel, character-level, 28-letter-rasm, hamza→alif normalize, ى→ي, ة→ه, mushaf order, leave-one-out via per-verse subtraction)
n_gram_order: 5
seed: 20260414
sided_test: one-sided POSITIVE for primary (sign(G) > 0 majority); one-sided positive for secondary (Quran G-fraction > baseline G-fraction)
direction_prereg_source: al-Rāzī Mafātīḥ al-Ghayb linear-progression thesis (verses cohere forward); MW-1-GATE-A H-NEW-20 PASS already shows verse-similarity autocorrelation positive at lag-1 → directional sign committed BEFORE script write
baselines: [bukhari-noquran, jahiz-hayawan, mutanabbi-diwan]
bonferroni_k: 2   # primary sign-test + secondary cross-corpus comparison; per-baseline secondary contributes 1 worst-baseline-wins line
alpha_bon: 0.005   # = 0.01 / 2
null_publishable: true
positive_publishable: true
---

# [[h-new-38-directed-pmi|H-NEW-38]] — Directed verse-to-verse pointwise predictability asymmetry

## Why this pre-registration exists

H-NEW-20 (al-Rāzī verse-similarity autocorrelation, MW-1-GATE-A) PASSED a
**symmetric** lag-1 cohesion test. [[h-new-38-directed-pmi|H-NEW-38]] deepens it by asking the
**directed** question: is the predictability gain from v_i → v_{i+1} a
property of the directional dependency, or merely shared topical
vocabulary that would be measured equally by a symmetric metric?

The directed quantity is

  G(v_i → v_{i+1}) = H(v_{i+1}) − H(v_{i+1} | v_i)

where both H values are character-level cross-entropies of v_{i+1}
under a 5-gram model. A POSITIVE G means knowing v_i reduces the
character-level surprise of v_{i+1}, i.e., v_i carries forward
predictive information about v_{i+1}. The aggregate sign-test asks
what fraction of the 6,122 adjacent verse-pairs (6,236 verses − 114
surah-initial gaps where i is the last verse of a surah and i+1 is
the first verse of the next surah, EXCLUDED) has G > 0.

**Classical anchoring (positive direction):**
- al-Rāzī's *Mafātīḥ al-Ghayb* linear-progression thesis (`al-tartīb`):
  consecutive verses build cumulatively on the preceding context.
- al-Biqāʿī's *Naẓm al-Durar* munāsaba al-āyāt (verse-pair coherence)
  similarly predicts forward predictability.

**Counter-prediction (al-Sakkākī iltifāt):** *some* adjacent pairs are
deliberately interruption-points (mood pivots, addressee shifts,
rhetorical questions), where G should go negative. The PRIMARY test is
the global sign-fraction; this LOCAL pattern would emerge in subsetted
exploratory analysis, not the primary.

## Pre-registered hypotheses

**[[h-new-38-directed-pmi|H-NEW-38]]-PRIMARY (locked sign):** the fraction f₊ = |{i : G(v_i → v_{i+1}) > 0}| / 6122
exceeds 0.5 by a margin large enough to reject H₀ (one-sided exact
binomial p < α_bon = 0.005).

**[[h-new-38-directed-pmi|H-NEW-38]]-SECONDARY (cross-corpus):** Quran's f₊ exceeds the f₊ of
each of three matched-Arabic baselines (Bukhari-noquran, Jāḥiẓ Ḥayawān,
Mutanabbī Dīwān). Each baseline corpus is split into "verses"
(line-units; defined operationally below), and the same G computation
runs over its line-adjacent pairs. Worst-baseline gap wins the
secondary verdict (must exceed all 3 to pass). One-sided
two-proportion z-test, α_bon = 0.005.

## Pre-registered acceptance matrix (Bonferroni k=2, α_bon = 0.005)

| Outcome                                                                                                     | Verdict                       |
|-------------------------------------------------------------------------------------------------------------|-------------------------------|
| PRIMARY exact binomial p < 0.005 AND SECONDARY worst-baseline-z > +2.576                                    | **PASS — DIRECTED COHESION CONFIRMED** |
| PRIMARY p < 0.005 AND SECONDARY fails on ≥ 1 baseline                                                       | **PARTIAL — Quran has internal directed cohesion but not specifically more than baseline** |
| PRIMARY p ≥ 0.005 (f₊ ≈ 0.5 or below)                                                                       | **NULL — no global directed cohesion** |
| PRIMARY p < 0.005 with f₊ < 0.5 (sign-flipped from pre-reg)                                                 | **REVERSE — file as [[h-new-38-directed-pmi|h-new-38]]-reverse.md, NOT primary** |
| Random-pair shuffle null (10k shuffles of i↔j adjacency) shows observed f₊ NOT in upper 99th percentile      | **NULL — observed f₊ within random-adjacency expectation** |

The **random-pair shuffle null** is a SEPARATE GATE additional to the
binomial test. It controls for the possibility that the model bias and
finite-sample structure inflate f₊ on any adjacency assignment. If the
binomial test rejects but the shuffle null does not, the verdict is
NULL (the shuffle null is the more conservative gate).

## No-fork protections

1. **Sign LOCKED to f₊ > 0.5** before any script execution. If the
   observation is f₊ < 0.5 with binomial-significant departure, file
   under `[[h-new-38-directed-pmi|h-new-38]]-reverse.md` as a separate finding — NOT as primary
   PASS with a sign-flip narrative. The two findings are distinct
   theoretical claims.

2. **n-gram order LOCKED to 5.** No post-hoc sweep over n ∈ {3, 4, 5,
   6, 7}. If a sensitivity analysis is desired post-verdict, it runs as
   ROBUSTNESS, not as primary substitute.

3. **Smoothing LOCKED to add-one Laplace** (consistent with H-NEW-25
   estimator family used in this project). No post-hoc swap to
   modified Kneser-Ney or stupid-backoff.

4. **Surah-initial gaps EXCLUDED.** The 6,122 = 6,236 − 114 figure is
   pre-committed. The 114 surah-boundary "transitions" are NOT included
   in the global sign-test (they are between surahs, not between
   adjacent verses of a coherent unit).

5. **No baseline swap.** The three baselines (Bukhari, Jāḥiẓ,
   Mutanabbī) are LOCKED. If a baseline returns degenerate G
   distribution (numerical underflow / identical model collapse), it
   is reported as DEGENERATE and the secondary verdict runs on the
   remaining baselines with k_secondary updated to match — but this
   path requires the degeneracy to be visible in the script's
   diagnostic output, not a post-hoc judgment.

6. **LOO model evaluation.** For each verse v_{i+1}, the global 5-gram
   model is evaluated AS IF it had not seen v_{i+1}. Implementation:
   subtract v_{i+1}'s n-gram counts from the global counts before
   computing both H(v_{i+1}) and H(v_{i+1} | v_i). The model is
   trained ONCE on the full Quran. Per-verse LOO is mathematically
   equivalent to retraining-without-v_{i+1} under add-one Laplace.

7. **Shuffle null seed:** 10,000 random shuffles of the 6,122 adjacency
   pairs (i.e., random permutation of v_{i+1} relative to v_i across
   all pairs simultaneously). Seed 20260414. Computes f₊ for each
   shuffle. Observed f₊ must exceed 99th percentile (one-sided right
   tail) to pass the shuffle gate.

## Pre-registered operationalization

1. **Tokenization:** character-level over the 28-letter rasm-normalized
   Arabic consonant set. Reuse normalization from
   `scripts/h_new_25_trigram_entropy.py` (hamza variants → alif, ى → ي,
   ة → ه, strip non-letters). Word boundaries collapsed to nothing
   (so `بسم الله` becomes `بسمالله` for the n-gram model). This is the
   same convention as H-NEW-25.

2. **Verse extraction:** load `quran-text/quran-no-tashkeel.json`,
   iterate surahs in mushaf order, normalize each verse text via
   `clean_consonants`. Each verse → one character string.

3. **Global model training:** concatenate all 6,236 verses into one
   stream WITH a sentinel separator (single `|` mapped to its own
   symbol so n-grams cannot cross verse boundaries). Build counts of
   n-grams of length n=1..5. Add-one Laplace smoothing.

4. **Per-verse LOO subtraction:** for each verse v, before computing
   its cross-entropy, subtract v's own n-gram counts from the global
   counts. After computation, re-add. (Implementation can avoid
   re-add if processing is carefully ordered.)

5. **H(v_{i+1}) computation:** sum −log₂ p(c_t | c_{t-4}..c_{t-1})
   over the characters of v_{i+1}, using the LOO-adjusted model.
   Padding for the first 4 characters: prepend the begin-of-verse
   sentinel × 4. Divide by length(v_{i+1}) to get per-character entropy.

6. **H(v_{i+1} | v_i) computation:** identical, except the context for
   the first 4 characters of v_{i+1} comes from the LAST 4 characters
   of v_i (no sentinels). The model is the same LOO-adjusted model.
   Per-character entropy over v_{i+1}'s length.

7. **G computation:** G_i = H(v_{i+1}) − H(v_{i+1} | v_i). Positive
   means v_i → v_{i+1} is more predictable than v_{i+1} alone.

8. **Sign test:** count |{i : G_i > 0}| / 6122. Exact one-sided
   binomial p-value vs H₀ = 0.5.

9. **Random-pair shuffle null:** for each of 10,000 shuffles, randomly
   re-pair each v_{i+1} with a different v_i drawn from the full Quran
   verse pool (uniform without replacement, paired up). Recompute
   H(v_{i+1} | v_i_shuffled) and G_shuffled. Compute f₊_shuffled.
   Observed f₊ must exceed the 99th percentile of the shuffle
   distribution.

10. **Baseline corpora:** load each of {bukhari-noquran, jahiz-hayawan,
    mutanabbi-diwan} from `data/baseline-corpora/raw/`. Split into
    "verses" by newline. Apply identical normalization. Train SAME
    type of model on EACH baseline corpus separately. Compute f₊
    for each baseline's adjacency pairs. Two-proportion z-test for
    each baseline pair (Quran vs baseline).

## Outputs

- **JSON:** `findings/phase-b-hypotheses/csv/h-new-38.json`
- **Narrative:** `findings/phase-b-hypotheses/h-new-38-directed-pmi.md`
- **Script:** `scripts/h_new_38_directed_pmi.py`

## Compute estimate

Char-level 5-gram with 6,236 verses × ~30 chars avg = ~190k chars.
Building counts: O(N). Per-verse LOO eval: O(N) per verse → O(N²) total
~ 36 billion ops. **TOO SLOW with naive impl.** Optimization: keep
ONE global Counter, subtract a verse's contribution (O(verse_length))
before each eval, re-add after. Total: O(N) for build + O(N) for all
LOO evals = O(N) overall. Estimated **< 60 seconds** on cold start for
full Quran. Baselines: similar. Shuffle null: 10,000 × O(N) ≈ 30 sec.
Total wall time: < 5 minutes.

## Seed

`20260414` for the shuffle null. (NB: parent task #75 spec mentioned
20260413 for sister H-NEW-17; [[h-new-38-directed-pmi|H-NEW-38]] uses 20260414 to avoid seed
collision and document its independent execution.)

## Bonferroni accounting

- k = 2: PRIMARY (binomial sign test) + SECONDARY (worst-baseline
  cross-corpus z-test).
- α_bon = 0.005.
- The shuffle null is a SEPARATE GATE, not in the Bonferroni family
  (it is a sanity check, not a hypothesis test).

## Reverse-finding routing

If the test produces a sign-flipped result (f₊ < 0.5) with
binomial-significant departure, this is filed as
`[[h-new-38-directed-pmi|h-new-38]]-reverse-suppression.md` as a SEPARATE hypothesis-generating
finding ("Quranic adjacent verses are LESS predictable than expected;
candidate mechanism = al-Sakkākī iltifāt-style discourse pivots").
This is NOT the primary verdict; the primary remains a NULL on the
positive direction.

## Dispatch chain

1. computational-tester → authors this pre-reg (this file). **DONE.**
2. computational-tester → authors `scripts/h_new_38_directed_pmi.py`
   per the operationalization above.
3. computational-tester → executes the script, writes JSON + narrative.
4. skeptical-auditor → audits compliance with this pre-reg.
5. integrator → integrates verdict.

## Pre-execution lock confirmation

This file is committed BEFORE the script is written. Any subsequent
deviation from this pre-reg in the script must be documented as an
amendment with explicit team-lead approval. The seed, n-gram order,
smoothing, baselines, sign direction, Bonferroni k, and α_bon are all
LOCKED.
