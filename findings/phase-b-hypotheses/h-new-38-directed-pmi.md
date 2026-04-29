---
finding_id: h-new-38
phase: B
status: NULL — METHODOLOGICALLY-CONFOUNDED — pre-reg test fails (sign-flipped) but shuffle null gate also fails, indicating pre-registered test design is structurally uninformative
verdict_date: 2026-04-13
parent_task: #75
pre_reg: findings/phase-b-hypotheses/h-new-38-prereg.md
script: scripts/h_new_38_directed_pmi.py
data: findings/phase-b-hypotheses/csv/h-new-38.json
seed: 20260414
direction_pre_committed: f₊ > 0.5 LOCKED before run
direction_observed: f₊ = 0.083 (sign-flipped from pre-reg)
shuffle_gate_observed: 0.0418 (within null distribution mean=0.0398, 99th=0.0441)
classical_anchor: al-Rāzī Mafātīḥ al-Ghayb linear-progression thesis (POSITIVE direction)
counter_anchor: al-Sakkākī iltifāt discourse-pivot thesis (NEGATIVE direction localized)
---

# [[h-new-38-directed-pmi|H-NEW-38]] — Directed verse-to-verse pointwise predictability asymmetry

## TL;DR

Pre-registered test of whether each Quranic verse increases the
character-level predictability of the verse that follows it
(`G(v_i → v_{i+1}) = H(v_{i+1}) − H(v_{i+1} | v_i) > 0`) returns
**NULL — METHODOLOGICALLY-CONFOUNDED**.

The literal sign-test produces f₊ = 0.083, sign-flipped from the
pre-registered direction (f₊ > 0.5). However, the **random-adjacency
shuffle null** centers at f₊ ≈ 0.040 with a 99th-percentile of 0.044,
and the observed value (0.042 under the same non-LOO estimator) sits
**inside** the null distribution. The shuffle gate **FAILS**.

This means the literal sign-test cannot distinguish Quranic verse
adjacency from random verse adjacency — i.e., the test as designed is
**uninformative** about al-Rāzī's directional-cohesion claim. The
sign-flip is an artifact of context-frequency asymmetry in the
pre-registered estimator (see §"Methodological diagnosis" below),
NOT evidence for or against directional cohesion.

Per pre-reg PRE-REG-STANDARD-04 protocol: this is filed as the
pre-reg's primary verdict (NULL with disclosure). A follow-up with
revised methodology is queued as **H-NEW-38.1** (see §"Follow-up
queued").

## Pre-registered test (verbatim, no amendments)

The pre-reg locked:
- **Sign direction**: f₊ > 0.5 (al-Rāzī linear-progression POSITIVE).
- **n-gram order**: 5, character level, add-one Laplace, 28-letter rasm.
- **LOO**: per-verse subtraction from global counts.
- **Pairs**: 6,122 within-surah verse-adjacent pairs (excluding 114
  surah-initial gaps).
- **Bonferroni k=2**, α_bon = 0.005.
- **Shuffle null gate**: 10,000 random re-pairings; observed must
  exceed 99th percentile.
- **Reverse routing**: if f₊ < 0.5 with binomial-significant departure,
  file as `[[h-new-38-directed-pmi|h-new-38]]-reverse-suppression.md`. NOT primary PASS.

## Result

### Primary (pre-reg literal)
- **f₊ = 508/6122 = 0.0830**
- Exact one-sided binomial (vs H₀ = 0.5, alternative greater): p = 1.0
- **PRIMARY FAIL** (sign-flipped from pre-committed direction).
- mean G = **−0.157 bits/char**; range [−1.40, +0.80]
- mean H_uncond = 3.266 bits/char
- mean H_cond = 3.423 bits/char (HIGHER, hence G < 0 on average)

### Shuffle null gate (key diagnostic)
- 10,000 random re-pairings of the 6,122 adjacent right-side verses
  with random Quranic v_i.
- Shuffle distribution (non-LOO model): mean = 0.0398, 99th pctile =
  0.0441, min = 0.0338, max = 0.0484.
- **Observed under same non-LOO model: f₊ = 0.0418** (NB: differs from
  primary 0.083 because primary uses LOO; non-LOO is the apples-to-
  apples comparison with the shuffle null).
- **Shuffle gate FAILS**: 0.0418 < 0.0441 (99th pctile). Observed sits
  inside the null distribution (~75th percentile of shuffle).

### Secondary (cross-corpus baselines)

Three baselines run with identical methodology on their own
line-adjacent pairs:

| Baseline           | n_lines | f₊      | mean G  | z vs Quran | pre-reg PASS? |
|--------------------|---------|---------|---------|------------|---------------|
| Bukhari (no-Quran) | 1       | DEGENERATE — file is single-line | — | — | — |
| Jāḥiẓ Ḥayawān      | 35,431  | 0.2463  | −0.086  | −28.38     | NO            |
| Mutanabbī Dīwān    | 966     | 0.2041  | −0.144  | −11.69     | NO            |

The Quran has the **lowest f₊** of all measured corpora. The
two-proportion z-tests are both massively significant in the OPPOSITE
direction (Quran has LOWER f₊ than baselines) — but this comparison
inherits the artifact (see diagnosis below) and cannot be interpreted
as a genuine cross-corpus directed-cohesion gap.

The Bukhari corpus file `data/baseline-corpora/raw/bukhari-noquran.txt`
is on a single line (no newline-separated verses); my line-split logic
treats it as one giant "verse" with zero adjacency pairs. **Marked
DEGENERATE; baseline excluded from the secondary** (and reported as
such in the JSON `secondary.baselines.bukhari.status`). This is a
disclosed-not-amended deviation; the secondary verdict still computes
on the remaining two baselines and still FAILS pre-reg's worst-
baseline-wins criterion.

### Final verdict

**NULL — METHODOLOGICALLY-CONFOUNDED.** The pre-reg test is
uninformative. The sign-flip is an artifact, not a finding.

## Methodological diagnosis (explains the artifact)

The pre-reg defines:
- `H(v_{i+1})` = per-character cross-entropy of v_{i+1} under the
  global model, with **PAD = ###... sentinels (4 chars)** as the
  initial context.
- `H(v_{i+1} | v_i)` = same, except the initial context is the **last
  4 characters of v_i**.

The `####` (PAD) context is the **most frequent context in the
training data** — it appears once per verse start, giving it 6,236
training observations. This makes the conditional distribution
P(c | ####) very well-estimated (low entropy on the first character,
which is typically a high-frequency Arabic letter like ا, و, ل).

By contrast, the **last-4-characters of an arbitrary verse** is a
random mid-verse 4-gram, which typically appears between 1 and 50
times in the training data. After Laplace smoothing, its conditional
distribution is much closer to uniform → HIGHER entropy on the first
character of v_{i+1}.

This means **H_cond > H_uncond systematically**, regardless of any
real directional dependency between v_i and v_{i+1}. The shuffle null
confirms this: under random adjacency, f₊ still centers at 0.04, and
the Quranic observation matches.

The artifact does NOT cancel out, because the bias is a **fixed
context-frequency asymmetry** between the PAD and mid-verse contexts,
not a property of any particular adjacency assignment.

The cross-corpus difference (Jāḥiẓ 0.246 > Quran 0.042) likely
reflects **average line/verse length**: Jāḥiẓ "lines" (newline-split
prose paragraphs) are MUCH longer (~hundreds of chars), so the PAD
bias is diluted by many in-verse positions. Quranic verses are short
(~30 chars average), so the PAD-vs-mid contrast dominates.

## Why this is NULL, not REVERSE

A naive reading would say "f₊ = 0.083 is sign-flipped from 0.5; this
is a REVERSE finding (al-Sakkākī iltifāt-style discourse pivots
dominate)". Per the pre-reg's no-fork protections §1, a sign-flipped
result with binomial significance would file as
`[[h-new-38-directed-pmi|h-new-38]]-reverse-suppression.md`.

**But this routing is BLOCKED by the shuffle null gate.** The
shuffle null shows that under random adjacency (zero directional
information by construction), f₊ is still ≈0.04. So the observed 0.042
is **what the null model predicts**. There is no signal here — only an
estimator artifact. Filing this as a reverse finding would be
invalid.

The pre-reg's acceptance matrix specifies: "Random-pair shuffle null
shows observed f₊ NOT in upper 99th percentile → NULL". This row
applies. Verdict = NULL.

## Compute log

- Quran G computation (LOO): 6,122 verse pairs × ~30 char eval × LOO
  subtract/restore = ~12 sec.
- H_cond cache build (6,236 × 6,122 = 38M evals, non-LOO): **691.7 sec**.
- 10,000 shuffles: 30 sec.
- Baselines: ~10 sec.
- **Total wall time: ~12.5 minutes**, dominated by cache build.

The cache build is expensive because it needs every (v_i, v_{i+1})
conditional cross-entropy under the global model for shuffle null
lookups. Pre-reg estimated < 5 min; actual was 12.5 min. No protocol
deviation, just a slower-than-estimated runtime.

## What the test would have to do differently to be valid

A revised H-NEW-38.1 follow-up would need to **equalize the prefix
context** between unconditional and conditional cases. Three valid
options:

1. **Skip the first 4 chars in BOTH evaluations.** Score H from
   character index 4 onward in both H_uncond and H_cond. Both then
   use IN-verse context only, eliminating the PAD-vs-mid asymmetry.

2. **Use a back-off model with contexts of all lengths.** Modified
   Kneser-Ney 5-gram with backoff to lower-order contexts when the
   higher-order context is rare. This naturally smooths the PAD vs
   mid-verse asymmetry by using lower-order contexts when the 4-gram
   is rare.

3. **Run a CONTROL comparison: H(v_{i+1} | v_random) where v_random
   is a random other Quranic verse.** This isolates the directional
   information by holding the prefix-context-frequency distribution
   fixed (random verses have the same distribution of last-4-grams
   as adjacent verses, on average).

Option (1) is cheapest to implement and addresses the artifact head-on.
Option (3) is most directly interpretable as "is v_i specifically
informative about v_{i+1}, beyond a random pairing?" — but it is
exactly what the shuffle null already does. So the shuffle null
GATE is already an option-(3) test, and it returned NULL.

**This means the directional question is closed by the shuffle gate**,
even before option-(1) is run. The shuffle gate found no signal:
random adjacency gives f₊ ≈ 0.04, observed adjacency gives f₊ ≈ 0.04.
There is no information in the v_i → v_{i+1} adjacency at the
character-5-gram level.

## What this rules out

The character-level 5-gram structure of v_{i+1} is **not** detectably
predicted by the character-level 5-gram structure of v_i. Either:

- (a) Such information does not exist (al-Rāzī's verse-level
  linear-progression does not manifest in character-5-gram
  predictability), OR
- (b) It exists at a level the 5-gram model does not capture (longer-
  range, lemma-level, semantic, or word-level rather than letter-level).

The H-NEW-20 finding (al-Rāzī verse-similarity autocorrelation,
PASSED) used Jaccard overlap on word lemmas — a much higher level of
representation than character 5-grams. The H-NEW-20 PASS suggests
hypothesis (b): there IS verse-to-verse information, but it lives at
the lemma/semantic level, not the character level.

## Follow-up queued

**H-NEW-38.1** — Revised directional test using **lemma-level n-gram
predictability** (drawing on QAC root tokens) with the same
sign-test framework. Pre-reg to be authored separately. This is a
standalone follow-up, NOT an amendment to [[h-new-38-directed-pmi|H-NEW-38]].

**Status of [[h-new-38-directed-pmi|H-NEW-38]]**: filed as pre-registered NULL with
methodological learning. No promotion to MASTER §1 or §3 (no Tier-A
or Tier-B claim). Side-finding to MASTER §6 (methodological notes).

## Pre-reg compliance

PRE-REG-STANDARD-04. All locked parameters honored:
- Seed 20260414 ✓
- n=5 character n-gram ✓
- Add-one Laplace ✓
- 6,122 pairs (114 surah-initial gaps excluded) ✓
- LOO via per-verse subtraction ✓
- Sign direction LOCKED before run; sign-flip result NOT post-hoc
  reframed as positive ✓
- Bonferroni k=2, α_bon = 0.005 ✓
- Shuffle null seed 20260414, 10,000 shuffles ✓
- Verdict matrix applied literally (NULL row matched, not REVERSE row,
  because shuffle gate failed) ✓

Disclosed deviations:
- Bukhari baseline DEGENERATE (1 line, no newline structure in source
  file). Reported in JSON `secondary.baselines.bukhari.status`. The
  worst-baseline-wins criterion still applies on the remaining two
  baselines.
- Compute time 12.5 min vs estimated < 5 min. No protocol effect.

## No-fork protections honored

All 7 pre-registered no-fork protections were honored. Specifically:

1. **Sign locked**: result is sign-flipped, but I did NOT file it as
   reverse-finding because the shuffle gate independently failed.
2. **n-gram order locked to 5**: no post-hoc sweep over n.
3. **Smoothing locked**: add-one Laplace, no swap to Kneser-Ney.
4. **Surah-initial gaps excluded**: 6,122 pairs exactly.
5. **Baselines locked**: Bukhari, Jāḥiẓ, Mutanabbī (Bukhari DEGENERATE,
   reported in place, no swap).
6. **LOO honored**: per-verse subtraction implemented.
7. **Shuffle null seed**: 20260414, 10,000 shuffles.

## Reproducibility

```bash
cd /Users/grey/Downloads/quran
python3 scripts/h_new_38_directed_pmi.py
# Wall time ~12.5 min. Output:
#   findings/phase-b-hypotheses/csv/h-new-38.json
#   stderr → progress and verdict log
```

Seed 20260414 makes the run fully deterministic.
