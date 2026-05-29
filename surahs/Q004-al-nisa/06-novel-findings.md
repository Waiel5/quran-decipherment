---
surah: 4
surah_name_ar: النساء
surah_name_translit: al-Nisāʾ
file_type: novel-findings
date_last_updated: 2026-05-29
phase: B+
verdict: Q004-F-06 — Arm A CONFIRMED (lone alif-rhyme ṭiwāl) + Arm B CONFIRMED (sig_A minimum) + Arm C NULL (not a length-stratified rhyme extreme)
seed: 20260509
n_perm: 10000
---

# Q 4 al-Nisāʾ — Pre-Registered Novel Findings

One pre-registered three-arm test, run with seed 20260509 and 10,000 permutations, pre-reg SHA-256 locked
before computation and verified at runtime.

- **Pre-reg:** `surahs/Q004-al-nisa/Q004-F-06-alif-monorhyme-prereg.md`
- **Pre-reg SHA-256:** `47eec58b703727e0acddd9b61bb60dac36b610d3850ebdcb08292e99af55cec6`
- **Script:** `scripts/Q004_F_06_alif_monorhyme.py` (verifies SHA at runtime, fail-fast — printed "SHA OK")
- **JSON:** `surahs/Q004-al-nisa/csv/Q004-F-06.json`
- **Rules-tuple:** `(min-tashkeel rhyme, orthographic-token, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)`

The test promotes the close-reading observation that al-Nisāʾ is the conspicuous alif-rhyme exception among
the otherwise-nūn-rhymed long surahs into three falsifiable, direction-locked claims.

---

## Q004-F-06 Arm A — Q 4 is the unique alif-rhyme long surah (CONFIRMED)

**Hypothesis (pre-committed):** among *al-sabʿ al-ṭiwāl* {Q2,Q3,Q4,Q5,Q6,Q7,Q9}, Q 4 al-Nisāʾ is the ONLY
surah whose dominant final-letter is alif (ا); the other six are nūn (ن).

- **A-H1 (direction-locked):** count of alif-dominant surahs in {2,3,4,5,6,7,9} = exactly 1 (= Q 4).

**Result:**
- al-ṭiwāl dominant final-letters: Q2 = ن, Q3 = ن, **Q4 = ا**, Q5 = ن, Q6 = ن, Q7 = ن, Q9 = ن.
- alif-members = **[4]** — **A-H1 PASS.** The other six are all nūn (others_all_nun = True).
- Robustness (MW-3): under the alternative ṭiwāl roster {2,3,4,5,6,7,8} (taking Q 8 al-Anfāl as the seventh
  instead of Q 9), Q 8 is also nūn-dominant — Q 4 remains the lone alif under either roster.

**Verdict: CONFIRMED (deterministic).** al-Nisāʾ is the unique alif-rhyme surah among the seven long surahs,
holding a near-monorhyme alif (96.0%, 169/176 verses) where every other long surah is nūn-dominant. This is a
clean deterministic corpus fact: a single 176-verse legal surah carrying the long-*qaṣīda* alif *rawī* in a
nūn-rhymed neighbourhood.

## Q004-F-06 Arm B — Q 4 is a structural-iʿjāz (fawāṣil-variety) minimum (CONFIRMED)

**Hypothesis (pre-committed):** the near-monorhyme suppresses fāṣila variety, so Q 4's al-Bāqillānī
structural-iʿjāz signature sig_A is among the corpus minima.

- **B-H1 (direction-locked):** Q 4's sig_A rank (descending) ≥ 112 (bottom-3 of 114) AND z_rhyme_entropy < 0.

**Result:**
- sig_A(Q4) = **−3.1463**, rank **113/114** (≥ 112) — only one surah scores lower.
- rhyme_entropy = 0.1989 nats; z_rhyme_entropy = **−1.0339** (< 0) — **B-H1 PASS.**

**Verdict: CONFIRMED.** Q 4 is a fawāṣil-variety minimum: its verse-endings are the second-least-varied in the
corpus (sig_A rank 113/114), driven by the 96% alif-monorhyme (rhyme entropy 0.199 nats, z −1.03). This
empirically grounds a refinement of al-Bāqillānī's *iʿjāz al-fawāṣil*: al-Nisāʾ's inimitability, whatever its
nature, is NOT on the verse-ending-variety axis — it is a deliberate near-monorhyme legal surah, the opposite
of a high-variety fawāṣil composition.

## Q004-F-06 Arm C — is the rhyme concentration extreme GIVEN the surah's length? (NULL)

**Hypothesis (pre-committed, direction-locked):** Q 4's `frac` (96.0%) is in the upper tail of the
length-stratified `frac` distribution (surahs with n_verses ≥ 100, excluding Q 4); a short oath-surah can hit
100% trivially, so the non-trivial claim is that a 176-verse surah at 96% is extreme.

- **C-H1 (direction-locked):** p_perm = (#{pool_frac ≥ obs} + 1)/(N+1) < 0.05 (Q 4 in the top ~5% of the
  long-surah distribution).

**Result:**
- frac(Q4) = 0.9602 (176 verses); long-surah pool (n_verses ≥ 100, excluding Q4) size = 17.
- null (10,000 length-stratified resamples): mean = 0.8112, std 0.148; **z = +1.007**; **p_perm = 0.17838**
  (1,783 of 10,000 draws ≥ Q4's frac) — **C-H1 FAIL** (does not clear α = 0.05).
- long surahs EXCEEDING Q 4: **Q 17 al-Isrāʾ (0.9910), Q 18 al-Kahf (0.9909), Q 23 al-Muʾminūn (0.9661)** —
  exactly the three named in the pre-reg as the pre-committed honest-limit.

**Verdict: NULL, published with full prominence per PRE-REG-STANDARD-04.** Q 4's 96.0% rhyme concentration is
NOT a length-stratified extreme: ~18% of the long-surah `frac` distribution is ≥ Q4's value, and three
comparable-length surahs (Q 17, Q 18, Q 23) hold TIGHTER monorhymes. **This does NOT retract Arm A** — Q 4 IS
the unique alif-rhyme surah among al-ṭiwāl (deterministic). What Arm C shows is that the *degree* of its
concentration, relative to all long surahs, is unremarkable: the alif-monorhyme is notable for its LETTER
(alif in a nūn neighbourhood) and its CONTEXT (the only such long-Medinan-legal surah), not for being the
corpus's tightest long-surah rhyme.

**What the NULL teaches (this is a first-class finding).** The pre-committed honest-limit (Q17/Q18/Q23 named
in advance) fired exactly as anticipated. al-Nisāʾ's rhyme distinctiveness is **categorical** (the alif vs the
ṭiwāl nūn) and **structural-iʿjāz-floor** (sig_A rank 113/114), but NOT **distributional-extreme** (its 96% is
mid-pack among long monorhymes). This separates three distinct senses of "monorhyme distinctiveness" — letter
identity (Arm A), fawāṣil-variety floor (Arm B), and length-stratified concentration (Arm C) — and shows
al-Nisāʾ is extreme on the first two and null on the third. It is a clean instance of the discipline that a
single qualitative observation ("al-Nisāʾ is a striking alif-monorhyme") decomposes into separately-testable
claims with separate verdicts.

---

## Bonferroni / family summary

Q004-F-06 has one permutation cell (Arm C); α_corrected = 0.05/1 = 0.05. The deterministic cells (A-H1, B-H1)
do not consume α.

| Arm / cell | Type | Result | Verdict |
|:--|:--|:--|:--|
| A (A-H1) | deterministic | Q 4 unique alif in ṭiwāl; others all nūn | **CONFIRMED** |
| B (B-H1) | deterministic | sig_A rank 113/114, z_rhyme_entropy −1.03 | **CONFIRMED** |
| C (C-H1) | permutation (α=0.05) | z=+1.01, p=0.178; Q17/Q18/Q23 exceed | **NULL** |
| **overall** | — | 2 deterministic CONFIRMED + 1 length-stratified NULL | **SPLIT (honest)** |

## MW protections applied

- **MW-1 (instrument-prior):** alif-vs-nūn definition, sig_A rank threshold, and length-stratified `frac` null
  all fixed in the pre-reg before any run.
- **MW-2 (corpus-prior):** Arm C used 10,000 length-stratified resamples.
- **MW-3 (alternative-models):** Arm A tested both ṭiwāl rosters ({…,9} and {…,8}); Arm B used an independent
  instrument (sig_A) from Arm A's letter-count.
- **MW-5 (replication):** Arms A, B deterministic and fully replicable from the on-disk JSON; Arm C seed-locked
  at 20260509.
- **MW-6 (instrument-control):** Arm C's length-stratification (n_verses ≥ 100) is the explicit control against
  the trivial short-surah-monorhyme confound — this is what made the NULL honest (it excluded the trivial
  100%-on-3-verses surahs).
- **MW-7 (post-hoc cap):** the alif-rhyme observation is from close reading; promoted to direction-locked
  pre-registered tests before computation. Arm C's honest-limit (Q17/Q18/Q23 named in advance) capped the
  over-claim and fired exactly as pre-committed.

## Cross-finding integration

- **H-NEW-700 (phonological dispersion-tail)** — Arm A adds the result that al-Nisāʾ is the lone alif-rhyme
  long surah; the long-Medinan fāṣila is otherwise nūn-uniform.
- **H-NEW-750 (iʿjāz signature)** — Arm B confirms Q 4 as a fawāṣil-variety minimum (sig_A rank 113/114),
  refining the al-Bāqillānī axis.
- **Decomposition of a qualitative observation** — Q004-F-06 is a model case: "al-Nisāʾ is a striking
  alif-monorhyme" decomposes into letter-identity (extreme), variety-floor (extreme), and length-concentration
  (null). Flagged for the methodology handoff alongside Q003-F-01.

## Honest limits

- Arm A's `frac` is on the min-tashkeel final-letter; a fuller *rawī*+*waṣl* rhyme model could shift the exact
  percentages (though alif-dominance is robust).
- Arm C's NULL is length-threshold-dependent (n_verses ≥ 100): a tighter stratum (≥ 150) would shrink the pool
  and could raise Q 4's rank, but the pre-committed threshold is ≥ 100 and the result is reported as such.
- The UAS rank 26/114 (`01-empirical-profile.md`) uses |sig_A|, so Q 4's high UAS reflects the MAGNITUDE of its
  negative sig_A (the variety-floor), not high structural-iʿjāz — a sign-ambiguity flagged in the profile.

---

*Computed 2026-05-29, seed 20260509, 10,000 perms, SHA-locked pre-reg verified at runtime.
Script: `scripts/Q004_F_06_alif_monorhyme.py`; JSON: `csv/Q004-F-06.json`.*
