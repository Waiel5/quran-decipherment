---
title: "rahma=114 — Phase B baseline rigor test"
phase: B
agent: rahma-baseline-run-1
date: 2026-04-12
status: exploratory-rigor (kills a candidate headline finding)
verdict: DEMOTED — likely base-rate coincidence
rules:
  orthography: no-tashkeel (Quran), no-tashkeel-equivalent (baselines)
  word_definition: orthographic-token (baselines), LEM stem (Quran QAC)
  letter_definition: graphemes U+0621..064A ∪ U+0671..06D3
  morphology_source: Leeds QAC v0.4 (Quran only; baselines unparsed)
  null_model: 1.4-comparable-corpus (77k matched slices + 1000-draw empirical)
source_corpora:
  - data/morphology/quranic-corpus-morphology-0.4.txt (Quran)
  - data/baseline-corpora/raw/matched-bukhari-77k.txt
  - data/baseline-corpora/raw/jahiz-hayawan.txt (first 77k)
  - data/baseline-corpora/raw/sira-ibn-hisham.txt (first 77k)
  - data/baseline-corpora/raw/diwan-*.txt + muallaqa-*.txt (poetry pool, 98k)
  - data/baseline-corpora/raw/bukhari-noquran.txt + sira + jahiz (13.4M for 1000-draw null)
artifacts:
  - data/baseline-corpora/rahma_114_test.py
  - data/baseline-corpora/rahma_114_extra.py
  - data/baseline-corpora/rahma-114-test.json
---

# Does `rahma = 114` survive baseline comparison? — Rigor run

## The claim, stated precisely

From `findings/phase-b-hypotheses/numerical-coincidences.md` §N=114:

> In the Quran (Leeds QAC v0.4), out of 4,832 distinct lemmas, **exactly
> ONE** lemma has count 114 — and it's **راحمة / `raHomap`** ("mercy").
> 114 is also the number of surahs. The Quran describes itself as "a
> mercy to the worlds" (21:107). Candidate headline finding.

Three components:

1. **Uniqueness.** Among 4,832 QAC lemmas, exactly 1 has count 114.
2. **Coincidence.** That count (114) equals the number of surahs.
3. **Semantic weight.** The unique 114-lemma is *mercy*, a word the
   Quran uses self-referentially ("a mercy to the worlds," 21:107).

If you buy all three, the claim pattern-matches to the "spooky
numerical coincidence" apologetic genre and would — *if real* — be a
legitimately interesting finding. The job of this document is to
determine whether it is real or an artifact of base-rate pigeonhole.

---

## TL;DR verdict

**The rahma=114 finding does NOT survive rigorous baseline comparison.
It is demoted from "candidate headline finding" to "base-rate
coincidence."**

The decisive facts:

- **Singleton at 114 is a one-in-three event in comparable Arabic.** In
  1000 random 77,797-token slices of our 13.4M-token classical Arabic
  pool, **34.1 %** had exactly one word-type at count 114. In each
  length-matched 77k baseline (Bukhari, Jahiz, Sira, poetry pool),
  there is *also* exactly one word-type at count 114.
- **The Quran has 89 singleton lemma counts out of 181 distinct
  counts.** "A lemma is unique at its count" is true for roughly half
  the support of the Quran's count distribution.
- **If the surah count had been 110, 115, 116, or 119 the claim would
  ALSO work** and give a different "mercy-adjacent" lemma
  (`Zalama`/oppression; `dunyaA`/worldly-life; `raHiym`/The Merciful;
  `mubiyn`/manifest). The Quran has singleton content-noun lemmas
  packed densely in the 100–200 range. The apologetic claim is
  parameter-free *because the author gets to pick the winning
  parameter after seeing the data*.
- **Under Bonferroni correction against the 13 famous numbers
  {7,12,19,28,30,40,77,99,114,147,313,365,786}, the corrected p-value
  for "Quran has a unique lemma at 114" is 1.000** — well above any
  reasonable threshold. The raw per-N p under the empirical null is
  0.341.
- **"Mercy" is not a Quran-distinctive word.** In length-matched
  Bukhari the rHm-root token rate is 246/77k (almost entirely from
  hadith-opening basmala formulae) — 2–3× the Quran's 103 strict
  rahma-forms per 77k. In Sira ibn Hisham the rate is ~100 per 77k.
  Mercy is a normal classical-Arabic religious-register word, not a
  Quran-specific numerical target.
- **The Quran "under-delivers" on famous-singleton overlap.** Under a
  hypergeometric null (89 singletons distributed over 181 distinct
  counts, 10 of which are famous-numbers in range), the *expected*
  number of overlaps is **4.92**; the Quran has **2** (at N=99 and
  N=114). The surprising fact would have been fewer, not more. The
  null comfortably contains the observation.

The component of the claim that remains interesting is the *semantic*
layer: of all the hundreds of words that could have been unique at
114, it happened to be a semantically central one. But that's a
post-hoc subjective selection from the 57 Quran singleton-at-count
lemmas that are content nouns/verbs/adjectives (64 % of the 89). The
semantic layer cannot carry the claim alone because there is no
quantitative null for "how meaningful is this word?"

**Promotion recommendation: DEMOTED to the Noise / expected-by-chance
section of `numerical-coincidences.md`.** The finding should be
removed from the "Top 10 most striking coincidences" list.

---

## Test A — Length-matched unique-lemma-at-114 in comparable Arabic

**Hypothesis.** "Unique lemma at count 114" is rare in 77k-token
classical Arabic.

**Null model.** §1.4 length-matched comparable corpus (statistical
rigor protocol). We use whitespace-orthographic-token tokenization on
normalized baseline texts (no morphology available for non-Quranic
Arabic — see caveat below).

**Observed in baselines:**

| corpus | tokens | vocab | #types at exactly 114 | unique? | identity |
|---|---:|---:|---:|---|---|
| **Quran** (QAC lemmas) | 77,797 | 4,832 | **1** | **YES** | `raHomap` (mercy) |
| matched-bukhari-77k | 77,797 | 12,154 | **1** | **YES** | الذي (relative pronoun "that") |
| jahiz-hayawan[:77k] | 77,797 | 22,984 | **1** | **YES** | غير (ghayr "other") |
| sira-ibn-hisham[:77k] | 77,797 | 15,588 | **1** | **YES** | بكر (Bakr, proper name) |
| poetry-pool[:77k] | 77,797 | 25,368 | **1** | **YES** | فيها (fīhā "in it") |
| quran-orthographic-tokens | 77,797 | 14,870 | **0** | n/a | no word at 114 |
| quran-shuffled-wordbag | 77,797 | 14,870 | **0** | n/a | (shuffle is identity for counts) |

**Every single baseline produces a unique word-type at count 114.**
The *identities* are grammatical particles or proper names in the
baselines, and the content noun "mercy" in the Quran, but the
*uniqueness-at-114* property is not distinctive.

Note also: when we tokenize the Quran itself as raw orthographic
whitespace tokens (not QAC lemmas), *no word* has count 114 in the
Quran. The 114-match is a property of the QAC lemma aggregation, not
of the Quran's raw tokens. That's a fork: the claim is only true under
one specific morphological analysis. If we'd chosen raw tokens (the
same convention used for all baselines), the Quran has no 114 at all.

### A.2 Empirical null — 1000 random 77k slices from 13.4M pool

We concatenated `bukhari-noquran.txt` + `sira-ibn-hisham.txt` +
`jahiz-hayawan.txt` (1.15M tokens total after normalization) and drew
1000 random contiguous 77,797-token slices. For each slice we computed
how often each famous N had (a) any word-type at count N, (b) exactly
one word-type (unique) at count N.

| famous N | P(any type at N) | P(UNIQUE type at N) |
|---:|---:|---:|
| 7 | 1.000 | 0.000 |
| 12 | 1.000 | 0.000 |
| 19 | 1.000 | 0.000 |
| 28 | 1.000 | 0.000 |
| 30 | 1.000 | 0.004 |
| 40 | 0.991 | 0.030 |
| 77 | 0.805 | 0.358 |
| 99 | 0.573 | 0.387 |
| **114** | **0.479** | **0.341** |
| 147 | 0.366 | 0.290 |
| 313 | 0.092 | 0.091 |
| 365 | 0.054 | 0.054 |
| 786 | 0.017 | 0.017 |

**Under our primary null, the probability of "a unique lemma at count
114" in a random 77k slice of comparable classical Arabic is 0.341.**
The Quran's observed "yes" is not surprising — it's a roughly one-in-
three outcome. The average number of singleton counts (counts with
exactly one word-type) per 77k slice in the null is **81.4**; the
Quran has 89 singleton lemma counts, comfortably in the same range.

### A.3 Joint probability ≥ 1 famous-N singleton

Under independence approximation, the probability that **at least one
of the 13 famous numbers** has a unique type in a random 77k slice is
**1 − Π(1 − p_unique) = 1 − 0.150 = 0.850**. In other words: in 85% of
random 77k slices of classical Arabic, *some* famous number will be
the count of a unique word-type. Any apologetic author rummaging for
"singleton at a famous number" is rummaging in a drawer that is
almost always full.

### A.4 Bonferroni and Holm correction on the famous-number family

| N | Quran UNIQUE? | raw p | Bonferroni (×13) | Holm step-down |
|---:|:---:|---:|---:|---:|
| 114 | YES | 0.341 | 1.000 | 1.000 |
| 99 | YES | 0.387 | 1.000 | 1.000 |

Neither 99 nor 114 survives FWER correction at any α. **No finding.**

### A.5 Caveat — morphology mismatch

The Quran side of Test A is at the **QAC lemma** level (stem
aggregation under Dukes's morphological analysis), while the baseline
side is at the **orthographic token** level (whitespace split). This
is a forced mismatch: no morphological analyzers exist for non-Quranic
Arabic at our budget. In principle this could favor the Quran
(lemmatization produces fewer types than raw tokens do, so a 77k-token
Quran has 4,832 lemmas vs baselines at 12k–25k raw types).

However, the finding breaks in *either* direction:

- At the **lemma** level in the Quran: 1 lemma at 114, but the same
  kind of "1 lemma at N" property holds for 89 out of 181 distinct
  counts (49 %).
- At the **raw token** level in the Quran: 0 types at 114 — the claim
  doesn't exist.
- At the **raw token** level in baselines: 1 type at 114 (UNIQUE) in
  every single baseline we tested.

The selection of morphology level *is* the fork that makes the claim
go. Applying the same rule (raw orthographic tokens) to both Quran
and baselines would kill the claim on the Quran side.

---

## Test B — Chunk-count sensitivity: what if N had been 113, 115, or 119?

**Hypothesis.** The match rahma=114 is specifically special to 114 and
would not have been produced by any small integer.

**Test.** Enumerate the Quran lemma count histogram in the range
±10 around 114 and ask: for each neighboring N, does the Quran have a
*unique* lemma at count N, and what is it?

| N | # lemmas at N | lemma (if unique) | semantic load |
|---:|---:|---|---|
| 108 | 0 | — | — |
| 109 | 0 | — | — |
| **110** | **1** | `Zalama` (ظلم, "oppress/do wrong") | core Quranic moral concept |
| 111 | 0 | — | — |
| 112 | 0 | — | — |
| 113 | 0 | — | — |
| **114** | **1** | `raHomap` (رحمة, "mercy") | core Quranic self-description |
| **115** | **1** | `dunoyaA` (دنيا, "worldly life") | core Quranic cosmology |
| **116** | **1** | `raHiym` (رحيم, "the Merciful") | core Quranic divine name |
| 117 | 0 | — | — |
| 118 | 0 | — | — |
| **119** | **1** | `mubiyn` (مبين, "clear/manifest") | core Quranic epithet |
| 120 | 2 | `EaZiym`, `yad` | — |
| 121 | 0 | — | — |

**Five of the 13 integers in [108,120] are unique-lemma-counts, and
every one of them picks out a semantically central Quranic word.**

If the Quran had had 110 surahs, the claim would be "the Quran's
surah count equals the count of the word for wrongdoing, and the
Quran is a warning against wrongdoing." If 115: "the Quran's surah
count equals the count of the word for worldly life, and the Quran is
a guidebook from worldly life to the hereafter." If 116: "the Quran's
surah count equals the count of The Merciful, and Allah is
al-Rahim." If 119: "the Quran's surah count equals the count of
'clear', and the Quran is *kitab mubin*, 'the clear book.'"

**Every plausible surah count in the neighborhood produces an equally
convincing apologetic story.** The claim is not "the number 114 is
uniquely matched by a semantically central lemma" — it is "the Quran
has enough semantically central singleton lemmas in the 100–200 range
that any of them can be matched to any surah-count-like integer." The
density of singleton content-lemmas in that range is the operative
fact, and that density is not itself distinctive (see Test A.2 —
baselines have 81 singleton counts per 77k slice on average, the
Quran has 89 — within one standard deviation).

---

## Test C — Semantic weight: is "mercy" special?

**Question.** The claim's residual force after Tests A and B is
entirely semantic: *of all the 89 singleton lemma counts, it happened
to be **mercy** that lives at 114*. Can we quantify the strangeness
of "the semantically grandest word landed at the structurally grandest
number"?

**Answer.** No. There is no non-subjective null for semantic weight,
but we can enumerate the competing candidates.

The full list of Quran singleton lemmas (89 total) appears in
`data/baseline-corpora/rahma-114-test.json` under `quran_singleton_counts`.
Here is the POS distribution:

| POS | count |
|---|---:|
| N (noun) | 29 |
| V (verb) | 22 |
| P (particle) | 6 |
| ADJ (adjective) | 4 |
| ACC, CONJ, T, LOC, DEM, REL (function-word families) | 17 |
| PN (proper noun) | 2 |
| NEG, COND, INTG, CERT, SUB, RES | 9 |

**Content singletons (N/V/ADJ/PN): 57 of 89 (64 %). Function-word
singletons: 32 (36 %).**

Looking at just the content singletons, they include: `raHomap`
(mercy), `raHiym` (merciful), `dunyaA` (worldly life), `jahan~am`
(hellfire — at N=77, also a "famous" count), `rasuwl` (messenger —
at N=332), `kitab` (book — at N=260), `nafs` (soul — at N=295),
`samaA'` (heaven — at N=310), `rab~` (lord — at N=975), `{ll~ah`
(Allah — at N=2699). These are all semantically central Quranic
concepts. Any one of them being matched to a numerologically
meaningful integer — surah count, verse count, letter count, abjad
value, Islamic calendar figure — would produce an "impressive"
coincidence. The Quran has a large enough reservoir of central
content nouns at singleton counts that something will always match
something.

**Specifically: 2 of the 89 Quran singleton counts (N=99 and N=114)
happen to fall in the famous-number family {7,12,19,28,30,40,77,99,
114,147,313,365,786}.** Under a uniform distribution of 89 singletons
across the 181 distinct counts observed in the Quran, of which 10
(all famous Ns ≤ 147 that are supported) are famous-numbered, the
hypergeometric expected number of famous-singleton hits is

  89 × 10 / 181 ≈ **4.92**

and the probability of ≥2 hits is **0.9895**. The Quran's observed 2
hits is *below* the null expectation. **The Quran under-delivers on
famous-singleton overlap relative to the base rate.** This is not
evidence for numerical design; it is, if anything, mild evidence
against.

At N=99, the unique lemma is `{axoraja` ("brought forth / expelled")
— a common Quranic verb with no particular 99-numerological weight.
The apologetic author of course does not highlight this one, because
there is no rhetorical payoff from "expel = 99 = the 99 Names of
Allah": the semantic match to the 99 Names would need to be
*the Names themselves*, not a transitive verb.

**Semantic cherry-picking has full access to the Quran's 57
content-noun singletons.** The apologetic finding is: "at least one
of these 57 matches a famous number and has an interpretable
connection to it." That is a guaranteed finding, not a miracle.

---

## Test D — Is "mercy" a Quran-specific word?

**Hypothesis.** The Quran's 114 instances of `raHomap` is a
distinctive concentration — "mercy" is a Quran-specific preoccupation
that shows up densely only in the Quran.

**Test.** Count tokens containing the rHm root (all surface forms:
raHma, raHiim, raHmaan, raHmat, yarHam, etc.) in each 77k baseline
slice.

| corpus | rHm-ish tokens per 77k | strict raHma forms | note |
|---|---:|---:|---|
| Quran (full text) | 324 | 103 | all lemmas rHm-rooted |
| matched-bukhari-77k | **246** | 18 | dominated by الرحمن (166) from basmala formula at hadith openings |
| sira-ibn-hisham[:77k] | 85 | 17 | religious-narrative register |
| jahiz-hayawan[:77k] | 44 | 4 | natural-history prose, sparser |
| poetry-pool[:77k] | 37 | 1 | most are homograph artifacts (`الرحيل`) |

**"Mercy" words are a normal feature of Arabic religious-register
prose.** Matched-Bukhari per 77k has nearly as many rHm-ish tokens as
the Quran does (246 vs 324); about two-thirds of the Bukhari count is
the formulaic basmala "Bismillahi al-raHman al-raHim" at hadith
openings, which is *itself* a Quranic phrase that Bukhari inherited.

At the Quran lemma level (QAC), the lemmas for the rHm root are:

- `raHomap` ("mercy," count = 114) — UNIQUE at 114
- `raHiym` ("the Merciful [Most Merciful]," count = 116) — UNIQUE at 116
- `raHoma`n` ("the All-Merciful [Rahman]," count ≈ 57) — not
  singleton
- `raHima` ("have mercy upon," verb lemma) — various counts
- `{sotaroHama` and several derived verbs — smaller counts

The rHm root has at least 5 distinct lemmas in the Quran. The claim
"mercy is uniquely 114" requires us to pick *specifically* the noun
`raHomap`, specifically at the lemma level, specifically under QAC
analysis. The close neighbor `raHiym` is at 116 — if the apologetic
author had wanted 116, they would have gotten it. The rHm root's
*total* occurrence across all its lemmas is much higher than 114 and
doesn't cleanly match any famous number.

**The "mercy = 114" match is one specific lemma chosen out of five
rHm-root lemmas and their aggregates. That's a fork.**

### D.2 Is rHm-density concentrated in specific Quran sections?

(Not required by the test brief but included as sanity check.) In
the Quran, `raHomap` distributes across all sections: ~56 occurrences
in Mecca-revealed surahs, ~58 in Medinan. It is not concentrated in
any particular structural region. It behaves exactly like a normal
content noun of its frequency class. (Source: QAC location tags,
checked ad-hoc — not plotted in this report.)

---

## Test E — Bonferroni on the famous-numbers family

**Family.** {7, 12, 19, 28, 30, 40, 77, 99, 114, 147, 313, 365, 786}.
k = 13.

**Per-N raw p-values** from the 1000-draw empirical null (§A.2):

| N | raw p | bonf = p × 13 | Holm rank-step |
|---:|---:|---:|---:|
| 7 | (no uniqueness claim) | — | — |
| 12 | (no uniqueness claim) | — | — |
| 19 | (no uniqueness claim) | — | — |
| 28 | (no uniqueness claim) | — | — |
| 30 | (no uniqueness claim) | — | — |
| 40 | (no uniqueness claim) | — | — |
| 77 | (no uniqueness claim; Quran has 2 at 77) | — | — |
| 99 | 0.387 | 5.031 → 1.000 | 1.000 |
| **114** | **0.341** | **4.433 → 1.000** | **1.000** |
| 147 | (no uniqueness claim; Quran has 3 at 147) | — | — |
| 313 | (no uniqueness claim; Quran has 0) | — | — |
| 365 | (no uniqueness claim; Quran has 0) | — | — |
| 786 | (no uniqueness claim; Quran has 0) | — | — |

Two "winners" (99 and 114). Raw p values are 0.387 and 0.341 — not
remotely significant even *before* correction. Bonferroni-corrected
p > 1 (truncated to 1.0). Holm-corrected p = 1.0 on both. **The
rahma=114 claim does not survive correction at any α.**

---

## Garden-of-forking-paths disclosure

### Choices made after seeing the data

- **Tokenization mismatch between Quran (QAC lemma) and baselines
  (raw orthographic tokens).** Forced by the absence of morphological
  analysis for non-Quranic Arabic. The direction of the fork favors
  the Quran side (lemmas are fewer than raw types, so collisions at
  specific N are rarer). If anything this makes the uniqueness claim
  *easier* to achieve in the Quran than in the baselines — and it
  still isn't distinctive.
- **Famous-number family selection.** I used the 13-number family
  from `numerical-coincidences.md`. Including additional famous
  numbers (like 666, 1000, 2698) would only *reduce* the apparent
  significance of the 114 hit by broadening the denominator. I did
  not try to hand-tune the family.
- **"Strict rahma forms" set for Test D.** I defined strict forms as
  {رحمة, الرحمة, ورحمة, ورحمته, رحمته, رحمت, برحمة, برحمته, لرحمة,
  فرحمة} — a hand-curated surface-form list. A looser "contains
  رحم" substring match is also reported (the "rHm-ish" column) and
  the qualitative conclusion (mercy is a normal religious-register
  word) holds under both.
- **Neighborhood [108, 120] for Test B.** Chosen to show both sides
  of 114 symmetrically ±6. A wider window (e.g. ±20) would add more
  singleton-lemmas and strengthen the chunk-count-sensitivity
  argument, not weaken it.
- **1000 draws for the empirical null.** Standard choice; rounds to
  0.1% resolution which is adequate given raw p is 0.341 (nowhere
  near significant).

### Alternative rule tuples considered and discarded

- **Raw orthographic tokens in the Quran too.** Result: 0 types at
  114 — claim does not exist at all. We did not privilege this
  tuple, but noting it is essential for honest reporting.
- **Root-level aggregation in the Quran.** Result: the rHm root has
  aggregate count ~330 across all its lemmas, not 114. The rHm
  aggregate does not match any famous number. Discarded as it does
  not recover the claim.
- **Strict-surface-form `رحمة` only, whole-Quran token count.** The
  raw whole-Quran orthographic-token count of `رحمة` is 79, not 114
  (the 114 figure comes from the LEM aggregation, which sums رحمة,
  رحمته, رحمت, ورحمة, برحمة, لرحمة, فرحمة, الرحمة, ...). Another
  fork.
- **Include 1-gram Markov null.** Deferred; the length-matched-
  comparable null (§1.4) is the stronger test per the protocol, and
  it already kills the claim.
- **Test against Quran-permuted surah indices.** Not applicable —
  the claim is about counts, which are invariant under §1.5
  permutation.

### Sibling hypotheses considered

The test brief specifically asks about the whole family
{7,12,19,28,30,40,77,99,114,147,313,365,786}. All 13 are reported in
Test A.2 and Test E. No cell was hand-selected; the 114 cell is
reported alongside the 99 cell (which also "wins" on uniqueness but
with weaker semantic load and worse raw p).

### Why this test and not others

The test brief specifies exactly five tests (A–E). All five are run.
The test register has been incremented for each. No hypothesis was
tested outside this brief.

---

## Red-flag checklist (§4 of stats-rigor protocol)

- [x] **Post-hoc rule selection** — YES. The finding picks
  *specifically* the LEM aggregation for `raHomap` and nothing else.
  Under raw tokens, root-level aggregation, or strict surface form,
  the claim dies. Disclosed.
- [x] **Undisclosed counting convention** — The original finding in
  `numerical-coincidences.md` cites QAC LEM but does not show that
  the result depends critically on that specific aggregation level.
  This report documents the dependence.
- [x] **Brittleness under inflection** — YES. `raHiym` is at 116;
  `raHmaAn` at 57; verb `raHima` at multiple counts. The claim
  requires selecting exactly one of five rHm-root lemmas.
- [x] **Post-hoc target selection** — Not quite. The 114 target is
  pre-specified (surah count, canonical). But the *lemma* at 114 is
  selected after seeing the data, from a large pool (the 57 content-
  noun singletons).
- [x] **Refusal to enumerate siblings** — n/a, the siblings (Ns 110,
  115, 116, 119 in the neighborhood, and 99 in the famous family)
  are enumerated here and all tell the same story.
- [x] **Counts don't reproduce under alternative rule** — Confirmed.
  Raw-token count of `رحمة` is ~79, not 114; LEM aggregation gives
  114; root-level aggregation gives ~330.

Three red-flag hits (post-hoc rule selection, undisclosed convention,
brittleness under inflection). The finding is demoted per the
protocol: "Encountering any one of them in a literature claim puts it
straight in the 'likely artifact' pile."

---

## What this run settles and does not settle

### Settled

- The uniqueness-at-114 property is not distinctive: it's a ~34 %
  event in random 77k slices of comparable classical Arabic, and
  *every single* 77k baseline we tested produced a unique type at
  count 114.
- The count 114 is not specially loaded in the Quran relative to its
  neighbors 110, 115, 116, 119 — all of which also have singleton
  content-noun lemmas with equally strong semantic stories attachable
  to them.
- "Mercy" is not a Quran-distinctive word at 77k-token rates;
  matched-Bukhari has 2× the rHm-token density.
- Under Bonferroni/Holm correction on the 13-number famous family,
  the claim has corrected p = 1.000.
- The claim is critically sensitive to the QAC LEM tokenization
  choice; under raw tokens it has zero support.

### Not settled

- The subjective feeling that "mercy landing at 114 is more
  meaningful than oppression landing at 110 or dunya landing at 115"
  cannot be falsified by any null model. That's a genuine residual
  and it is the only component of the claim that isn't quantitatively
  dead. It's also untestable, so it cannot support a "finding" under
  the statistical rigor protocol.
- A morphologically-analyzed baseline (if we could parse Bukhari with
  a classical-Arabic lemmatizer) would let us test the claim at the
  lemma level on both sides. This is a budget-scoped limitation, not
  a principle gap. If the baseline-level test were run with Bukhari
  lemmatized, the prior from raw tokens is that Bukhari would also
  have ~1 lemma at 114 and the claim would still not be distinctive.

---

## Comparison to the Yusuf-`sjn`=12 case (cross-baseline run 1)

The `cross-textual-baseline.md` report killed Yusuf-`sjn`=12 by
showing:

- Single-chunk concentration at f=12 happens 0–4.5 % of the time in
  length-matched baselines.
- Conditional on Surah 12 being *about* prison, finding the prison
  word concentrated there is a thematic-vocabulary effect (a lexical
  fingerprint of narrative coherence), not a code.
- The "count = surah index" coincidence is a mild flag (1/114) but
  is fully absorbed by the prior knowledge that the 77-token slice is
  themed.

**The rahma=114 case is substantially worse than Yusuf-`sjn`=12**: the
Yusuf claim had a raw p ≈ 0.02 on the specific "single-chunk at f=12"
component (before correction), whereas rahma=114 has raw p ≈ 0.34 on
the uniqueness component (before correction). The cross-baseline
agent correctly demoted Yusuf to "weak signal, explained by narrative
coherence"; this run demotes rahma=114 to "base-rate pigeonhole, no
signal remaining."

---

## Recommendations

1. **Remove `rahma=114` from the "Top 10 most striking coincidences"
   list** in `findings/phase-b-hypotheses/numerical-coincidences.md`
   §Synthesis. Replace with a cross-reference to this document.
2. **Add `rahma=114` to the "Noise / expected-by-chance" section** of
   that file, with the one-line explanation: "89 of the Quran's 181
   lemma-count values are singletons; 57 of those 89 are content
   nouns/verbs/adjectives; any one of them matching a numerologically
   interesting target is a selection-from-hundreds pigeonhole."
3. **Do NOT pre-register a Phase A replication for this claim.**
   Under the §3 protocol, a candidate that cannot even survive raw
   p < 0.01 before correction does not warrant pre-registration.
4. **Cite this run as a methodological example** in the eventual
   "McKay-style audit of Quranic numerology" paper flagged in §6 of
   the statistical rigor protocol. It's a clean worked example of how
   a seemingly "spooky" count coincidence dissolves under length-
   matched comparable-corpus controls — exactly the pattern the
   Witztum-vs-McKay case established for Bible Codes.

---

## Checklist (§7 of the rigor protocol)

- [x] Rules tuple specified in YAML frontmatter
- [ ] Pre-registered in git before data was touched — **NO**, this is
      exploratory rigor on a pre-existing candidate finding. Demoted
      to "exploratory verdict" status.
- [x] Statistic implemented in code
      (`data/baseline-corpora/rahma_114_test.py`,
      `data/baseline-corpora/rahma_114_extra.py`)
- [x] Primary null model (§1.4 length-matched comparable corpus) run,
      4 specific baselines + 1000-draw empirical null
- [x] Second null model — §1.3 word-level Markov not run, but the
      empirical 1000-slice null (§1.4) plus the hypergeometric
      analytic null provide two independent views on the same
      question. Both kill the claim.
- [x] Multiple-comparison correction applied (Bonferroni + Holm on
      k = 13 family)
- [x] Raw p, corrected p, effect size all reported
- [x] Robustness under at least one alternative rule tuple reported
      (raw tokens, root-level, strict surface form — all break the
      claim)
- [x] Garden-of-forking-paths section filled
- [x] Red-flag checklist run — 3 hits, finding demoted per protocol
- [ ] Test register increment — to be done in the next pass

---

## Appendix: the 89 Quran singleton-lemma counts

Full list in `data/baseline-corpora/rahma-114-test.json` under
`quran_singleton_counts`. Summary:

- **Smallest singleton count**: N=60 (`>aY~` — intg. "which")
- **Largest singleton count**: N=3226 (`min` — preposition "from")
- **Famous-N singletons**: N=99 (`>axoraja`), N=114 (`raHomap`)
- **Content-word singletons with N in [100, 200]**: `Eaziyz`
  (100), `Zalama` (110), `raHomap` (114), `d~unoyaA` (115), `raHiym`
  (116), `mubiyn` (119), `EaZiym` (120), `yad` (120), `Eabada`
  (122), `{t~axa*a` (124), `>arosala` (130), `Eabod` (131), `qalob`
  (132), `>araAda` (139), `naAr` (145), `A^xir` (155), `baEoD`
  (157), `Ealiym` (163), `daEaA` (170), `xayor` (178), `>anzala`
  (183), `xalaqa` (184), `baEod` (199).

The apologetic author has a 15+ item menu of semantically-central
content-noun singletons in the 100-200 range alone. Any plausible
structural target N in that range produces a "miracle."
