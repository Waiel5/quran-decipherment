---
title: "Pre-registration — H-NEW-2950: the sajdah loci, their glyph census, and whether they are textually marked"
author: Waiel Al-Shujaa
date: 2026-08-08
status: PRE-REGISTERED — locked before any comparison statistic was computed
frontier_item: F-8 (HANDOFF/FRONTIER-MAP-2026-08-07.md:234)
prior_work: [H-NEW-1330, H-NEW-1331, H-NEW-1510]
method_parents: [findings/UNIT-DRIFT-DEFECT.md, findings/ABSENCE-CLAIMS.md, findings/PROXY-CLAIMS.md]
script_path: findings/phase-b-hypotheses/scripts/h-new-2950.py
seed_primary: 20260509
seed_replication: 20260519
---

# H-NEW-2950 — pre-registration

## 0. What this pre-registration does and does not cover

This finding has **two deliverables of different epistemic kinds**, and they are separated here
deliberately.

**Deliverable 1 — the glyph census — is documentary, not inferential.** It counts a Unicode
codepoint in files on disk and enumerates where it occurs. It has no null model, no direction
and no p-value, because there is nothing to be uncertain about: the glyph is either in the file
or it is not. It was executed before this pre-registration was written and its result is not
conditioned on anything registered below. Registering a census would be theatre.

**Deliverable 2 — the textual-marking test — is inferential and is what this document locks.**
Everything in §§3–7 was fixed before any sajdah-verse feature value was compared against any
non-sajdah verse. The instrument strings in §4 were verified against the corpus beforehand
(that is calibration — confirming that `IMPV` is a string QAC actually emits — not peeking),
and the verification counts are recorded in §4.4 so the reader can see exactly what was looked
at before the direction was locked.

## 1. The question

Are the verses at which the muṣḥaf marks a prostration **textually distinguished** from
comparable verses, or are they marked purely by ritual assignment with no in-text correlate
beyond the naming of prostration itself?

## 2. The anti-circularity constraint — the single most important design decision here

The tradition did not select these loci at random. It selected them **because they speak of
prostration**. A test that asks "do the sajdah verses mention prostration?" is not an empirical
finding; it is the definition of the set restated as a result. Any finding that reports it as a
discovery has measured its own selection rule.

**Therefore every feature count in this pre-registration removes all QAC segments whose
`ROOT` is `sjd`.** The question then becomes non-trivial and worth asking: *setting aside the
prostration word itself, is the locus marked?*

This exclusion is **locked and is not optional**. A version of the same statistics without the
exclusion is registered in §7.3 as a **diagnostic** — reported to quantify how much of any
apparent signal is definitional — and is explicitly **not** part of the gated family and
**cannot** produce a PASS.

## 3. The unit-drift and proxy screens, applied to this design before it was built

Per `findings/UNIT-DRIFT-DEFECT.md` §3 and `findings/PROXY-CLAIMS.md` §3, applied to the
statistic and not to the prose:

| screen | status here |
|:--|:--|
| **Screen A — is the statistic a ratio with a unit count in the denominator?** | **No.** The statistic is a **sum of raw integer counts** over 15 verses. There is no density, no rate, no per-verse normalisation and no distance averaged over units of unequal size. This was chosen specifically so the defect cannot reach the result. |
| **Screen B — ordering or grouping with unit-size drift?** | Neutralised by construction: every comparison verse is drawn from the **same surah** as its sajdah verse and is one of the **nearest verses to it by word count** (§5). Length is matched at the level of the individual comparison, not adjusted for after the fact. |
| **Screen C (proxy) — is any quantity hand-assigned?** | **No.** The sajdah set comes from the in-corpus U+06E9 glyph, not from a hand-typed verse list. The three features are computed from QAC v0.4 morphological tags. Nothing in the pipeline is scored by hand. |

**The recurring failure this design is built to avoid** is testing whether sajdah verses are
*long*. Matching is on surah and word count jointly, and the statistic is a count rather than a
density, so verse length enters the null and the observation identically.

## 4. Instrument — QAC v0.4

Source: `data/morphology/quranic-corpus-morphology-0.4.txt` (Quranic Arabic Corpus, morphology
v0.4, Kais Dukes, GPL; text lineage Tanzil Uthmani 1.0.2). Rows are
`LOCATION \t FORM \t TAG \t FEATURES` with `LOCATION = (surah:verse:word:segment)`.

### 4.1 Word count (the matching variable)

> **w(v) = the number of distinct `word` indices appearing in QAC for verse v.**

Locked for this reason: QAC tokenises words, not orthographic marks. The sajdah glyph U+06E9
and the waqf marks are **not** QAC tokens, so this length measure is by construction immune to
being inflated by the very glyph that defines the test set. A whitespace-token count over the
text files would not have been — U+06E9 is a separate whitespace-delimited token in the source
text, which would have added exactly one to the length of exactly the 15 verses under test.

### 4.2 The three features (all computed after removing every `ROOT:sjd` segment)

| id | feature | definition on the QAC `FEATURES` field |
|:--|:--|:--|
| **F1** | **imperative count** (PRIMARY) | segments with `POS:V` **and** `IMPV` matched as a whole `\|`-delimited field |
| F2 | second-person-address count | segments matching `(?:^\|\|)(?:PRON:)?2(?:MS\|MP\|FS\|FP\|D)(?:$\|\|)` |
| F3 | divine-name count | segments whose `LEM` is one of `{ll~ah`, `r~aHoma\`n`, `rab~` |

### 4.3 Exclusion

A segment is dropped from **all three** feature counts iff its `FEATURES` field contains
`ROOT:sjd` as a whole `|`-delimited field. Dropped segments still count toward **nothing** —
they do not affect w(v), which is computed over word indices independently of the exclusion.

### 4.4 Calibration counts verified before the direction was locked

These were checked to confirm the tag strings exist and are non-degenerate. They are
corpus-wide totals over all 114 surahs and carry no information about the sajdah/non-sajdah
contrast.

| string | corpus-wide segment count |
|:--|--:|
| `ROOT:sjd` | 92 |
| `POS:V` + `IMPV` | 1,876 |
| second-person regex (F2) | 11,480 |
| `LEM:{ll~ah` | 2,699 |
| `LEM:rab~` | 975 |
| ``LEM:r~aHoma`n`` | 57 |
| total QAC segment rows | 128,219 |

## 5. The candidate set — locked, single rule, no forking paths

For each sajdah verse *i* in surah *s* with word count *w<sub>i</sub>*:

> **P<sub>i</sub> = { verse i } ∪ { the K non-sajdah verses of surah s that minimise
> |w(v) − w<sub>i</sub>|, ties broken by ascending verse number }**

with **K = 15** for the primary arm, giving **m<sub>i</sub> = 16** for every locus.

Locked clauses:

1. **All 15 sajdah verses are excluded from every pool.** Q 22 carries two loci; neither may
   enter the other's pool. This keeps the 15 draws independent.
2. **Pools never cross a surah boundary.** Surah is matched exactly.
3. **Tie-break is deterministic** (ascending verse number), so the pools are a function of the
   data alone and contain no randomness.
4. **Feasibility gate.** The smallest surah in the set is Q 96 (19 verses, 18 non-sajdah), so
   K = 15 is attainable at every locus. If any pool cannot be filled the run **aborts before a
   run directory is created**.

**One rule, stated once.** No window-then-widen fallback, because a two-branch matching rule is
a forking path and the branch taken would be chosen after seeing the data.

## 6. The null, and why it is exact

**H0.** A sajdah verse is exchangeable, on feature *f*, with the K nearest-length non-sajdah
verses of its own surah.

Under H0 the observed verse is a **uniform draw from P<sub>i</sub>**, independently across the
15 loci. So:

- **Statistic:** S = Σ<sub>i=1..15</sub> f(V<sub>i</sub>), where V<sub>i</sub> ∈ P<sub>i</sub>.
- **Observed:** S<sub>obs</sub> = Σ f(sajdah verse i).
- **Null distribution:** the **exact 15-fold convolution** of the 15 pool empirical pmfs of f.
  Since f is a small non-negative integer, this is computed exactly by integer dynamic
  programming — **no Monte Carlo, no asymptotic approximation, no normal reference.**
- **p (one-sided, upper):** p = P(S ≥ S<sub>obs</sub>).

**Ties are handled natively** because the convolution is over the *empirical pmf of the feature
value*, not over ranks. A pool in which 14 of 16 verses have zero imperatives contributes its
actual point mass at 0; nothing is smoothed and nothing is mid-ranked.

**Why "exact" is the honest word here.** The p-value is the exact probability of the observed or
a more extreme sum under the stated exchangeability, computed by enumeration of the full product
space 16<sup>15</sup> ≈ 1.2 × 10<sup>18</sup> via convolution. It is not a sampled approximation
to that probability.

### 6.1 The power statement, registered in advance

**n = 15. This test is underpowered and the finding will say so in its verdict line regardless
of outcome.**

Three floors will be reported:

1. **The design's realised floor**, p<sub>min</sub> = ∏<sub>i</sub> (c<sub>i</sub>/16) where
   c<sub>i</sub> is the number of pool members attaining that pool's maximum of f. This is the
   smallest p the test could return **on these pools** and is computed per axis.
2. **The tie-free floor**, 16<sup>−15</sup> = 1.16 × 10<sup>−19</sup>, attained only if every
   pool has a unique maximum and the sajdah verse is it.
3. **The sign-test floor**, 2<sup>−15</sup> = 3.05 × 10<sup>−5</sup> — the p from the weaker
   statement "all 15 loci exceed their pool median".

**The binding constraint at n = 15 is power, not p-resolution.** The floors above are small; what
is scarce is the ability to detect a modest effect. A NULL here is therefore *not* evidence of
absence of marking — it is evidence that any marking is not large enough for 15 verses to reveal.
This sentence is registered now so it cannot be softened later.

### 6.2 Monte Carlo cross-check (correctness, not inference)

Seed **20260509**, 200,000 draws from the same product-uniform null, used only to confirm the
convolution DP is implemented correctly. The run **aborts** if |p<sub>exact</sub> − p<sub>MC</sub>|
exceeds 5 Monte-Carlo standard errors. This is a unit test of the code and contributes no
inference.

## 7. Direction, family, and the decision gate — locked

### 7.1 Direction

**All three axes are locked one-sided UPPER: sajdah verses score HIGHER than matched controls.**

**Justification, written before the numbers were seen.** The classical account of *sujūd
al-tilāwa* is that the reciter is **commanded to act** at these points — al-Suyūṭī's masʾala
frames it as `يسن السجود عند قراءة آية السجدة` ("it is *sunna* to prostrate on reciting the
sajdah verse"). If the loci carry a textual signal beyond the prostration word itself, that
signal should be *heightened directive address to the hearer*: more imperatives (F1), more
second-person address (F2), and a denser invocation of the addressee's object of obedience
(F3). A locus that is textually marked but marked by *less* directive force would falsify the
mechanism, not support it — so a two-sided test would blur exactly the distinction of interest.

**Reversals will be reported.** If S<sub>obs</sub> < E[S] on any axis the finding records it as
a reversal against the locked direction and does **not** convert it into a two-sided pass.

### 7.2 Family and gate

Family size **k = 3** (F1, F2, F3). F1 is the **primary**; F2 and F3 are secondary.

| gate | threshold |
|:--|:--|
| Bonferroni significance | p < 0.05 / 3 = **0.0166667** |
| project novelty gate | min(1, 3p) < **0.005**, i.e. raw p < **0.00166667** |

**Verdict logic, locked:**

- An axis is **PASS-DIRECTED** iff `p_exact < 0.0166667` **and** `S_obs > E[S]`.
- An axis is **PASS-NOVELTY** iff `min(1, 3p) < 0.005` **and** `S_obs > E[S]`.
- **If F1 (primary) does not clear its Bonferroni gate, the headline verdict is NULL**, whatever
  the secondaries do. A secondary axis passing while the primary fails is reported as a
  descriptive observation requiring its own prospective pre-registration, not as support for F-8.
- An axis with `S_obs < E[S]` is recorded as **REVERSED**.

### 7.3 Registered diagnostic — NOT gated, cannot produce a PASS

The same three statistics computed **without** the `ROOT:sjd` exclusion. Reported to quantify
how much of the contrast is definitional (§2). Registered here so it cannot be presented later
as if it were a result: **no verdict may cite it as support.**

### 7.4 Registered replication arm

Seed **20260519**, **K = 10** (m<sub>i</sub> = 11) — a *tighter* length match, which is the more
demanding direction. Same three axes, same exact convolution, same gates. Reported in full
regardless of outcome. **This is a robustness check, not a second attempt at significance:** if
the primary arm NULLs and the replication arm passes, the registered reading is *unstable under
pool width*, not *PASS*.

## 8. Run discipline

- Prereg SHA-256 embedded as a literal in the script and **verified at runtime**; mismatch aborts.
- SHA-256 of QAC and of `quran-text/quran-no-tashkeel.json` likewise embedded and verified.
- **All integrity gates abort before a run directory exists.**
- Run directory `findings/phase-b-hypotheses/runs/h-new-2950/<UTC-timestamp>/`, created with
  `exist_ok=False`; every artefact written with mode `'x'`. **Run directories are never deleted.**
- Manifest records repo-relative paths, git commit, git status, both seeds, platform, and all hashes.
- **The finding file is not written to its final path before the run directory exists.**

## 9. What is out of scope

- Rules-tuple variants beyond the documentary comparison (Imāmī 4, Mālikī 11/13). The census
  reports which loci the glyph marks; it does not re-test H-NEW-1330/1331 under alternative
  inventories.
- Pericope-scale analysis. That is H-NEW-1510's unit and is not re-run here.
- Any claim about recitation practice, which is not measurable from this corpus.
