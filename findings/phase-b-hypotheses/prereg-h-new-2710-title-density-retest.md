---
id: H-NEW-2710
title: Title-density re-test — does eponymy predict a surah's density rank in its own title root, against a topicality-matched null?
date: 2026-08-07
status: LOCKED-BEFORE-COMPUTATION (with a declared prior-knowledge exception, §1.2)
author: Waiel Al-Shujaa
family: TITLE-2026-08-07-A
replaces: H-NEW-1820 (Pillar 4, withdrawn 2026-08-07)
prior_art: H-NEW-2680 D4 (20-draw smoke, descriptive, third metric)
seed: 20260509
seed_replication: 20260519
n_permutations: 10000
tests_in_family: 6
alpha_bonferroni: 0.008333
corrected_novelty_gate: 0.005
raw_p_gate: 0.000833
---

# PRE-REGISTRATION — H-NEW-2710 — Title-density, with an actual null

Written before any null distribution has been generated. §1.2 declares exactly what I
already knew, because part of the observed statistic is **published prior art** and
pretending otherwise would be the same species of dishonesty this re-test exists to
correct. The final SHA-256 is embedded as a fixed literal in
`findings/phase-b-hypotheses/scripts/h-new-2710.py` and verified at runtime; the run must
abort with `SystemExit` on mismatch.

---

## 1. What is being re-tested, and what is already known

`h-new-1820-title-density-independence-formal.md` (Pillar 4) claims **title-density
independence**: that eponymy and density-rank-1 are "empirically independent at
p ≈ 50:50," on the evidence that **47 of 89** eponymous surahs are not rank-1 in their own
title root. It was withdrawn on 2026-08-07 for two reasons: a cross-metric "correction"
(reverted), and — the substantive one — **it has no null model**. A bare headcount cannot
support an independence claim, because rank-1-of-114 is a demanding bar and a bare
majority failing it may be entirely unremarkable.

### 1.1 Prior art — H-NEW-2680 D4, which already ran a version of the key null

`prereg-h-new-2680-pillar-conjunction.md` §D4 registered: *"replace each surah's
title-root with a root drawn uniformly at random from the roots actually attested in that
surah, matched to the observed title-root corpus-frequency band, 2 000 draws."* Its
result, in `runs/h-new-2680-SMOKE/20260807T011906Z/result.json`:

| | value |
|:--|--:|
| observed rank-1 | **43** |
| matched-null mean | **24.55** |
| sd | 3.47 |
| q05 / q50 / q95 | 19.9 / 25.0 / 30.05 |
| p | 0.0476 |
| draws | **20** |

**This is the single most important number available before this test runs, and it must
frame everything.** Under a topicality-matched null the expected rank-1 count is **~24.6
of 89, not ~0.8 of 89.** The uniform-null intuition (1/114) is wrong by a factor of ~30.
So the honest scale of the effect is roughly **1.75×**, not "astronomical" — and the
withdrawal notice's phrase "strongly ENRICHED," while directionally right, risks
overcorrecting into the opposite error from the one it is fixing.

**Why this test is still worth running, stated as four specific additions:**

1. **Power.** D4 used **20 draws**; its p = 0.0476 is exactly its Monte-Carlo floor
   (1/21). It cannot resolve anything below that. This uses 10,000.
2. **Metric discipline.** D4 ranks by *title-root count ÷ total STEM-root tokens*.
   H-NEW-1820's own JSON ranks by *per-word density*. Its prose §Computation says *raw
   count*. **Three different instruments are in play across two files**, which is exactly
   the confusion that produced the invalid correction. This test fixes **one** metric as
   primary and runs the others as declared tuples.
3. **The distribution, not the binary.** D4 reports only the rank-1 count. The rank-1
   binary discards nearly all the information; **median rank and the rank≤k curve are far
   more informative** and are registered here as co-primaries.
4. **Dispersion matching.** D4 matched control roots on **frequency band only**. A root
   attested in few surahs will rank those surahs highly regardless of naming, so
   **dispersion is the more important of the two controls** and is added here.
   D4's own status is *"descriptive and is reported whatever it shows"*, with no locked
   direction and no gate; this test gates.

The main `runs/h-new-2680/20260807T011917Z/` directory is **empty** — the full-power run
produced no output. Nothing here overwrites or touches it.

### 1.2 Declared prior knowledge — this direction lock is NOT blind

**I knew the observed rank vector before writing this file**, because it is published in
`findings/phase-b-hypotheses/csv/h-new-1820.json` and the brief required me to read
H-NEW-1820 first. I also knew D4's approximate null expectation (§1.1). Specifically, I
had already computed from the published data:

- 42 of 89 at rank 1; **median rank 2**; rank ≤2: 52; ≤3: 57; ≤5: 63; ≤10: 75.

**Therefore the direction locked in §4 is a formality, not a prediction, and no credit is
claimed for it.** What is genuinely pre-registered — decided before any null distribution
existed — is: the null specifications, the statistic set, the tie convention, the metric
hierarchy, the matching bands, the family size, and the decision rule. **The value of
this test lies entirely in the null, and the pre-registration protects the null, not the
direction.** Any reader should discount the direction lock accordingly.

This declaration is itself the point: a pre-registration that quietly claimed a blind
lock here would be false.

---

## 2. What was inspected before this lock — exhaustive

1. `h-new-1820-title-density-independence-formal.md` in full, including both withdrawal
   notices; `cross-finding-027-formal-eponymy-independence-law.md` withdrawal line.
2. `h-new-1820.json`: 89 entries, fields `sid, title, root, title_surah_count,
   title_density_rank, is_rank_1, rank_1_surah, rank_1_count`. The 42/89 rank-1 count
   reproduces internally three ways.
3. The published rank distribution (§1.2).
4. **Reproduction check under per-word density: 87 of 89 published ranks reproduce
   exactly.** Two do not, and both are reported in §3.4 — including a **third
   arithmetic error in H-NEW-1820 that nobody has caught**.
5. `prereg-h-new-2680-pillar-conjunction.md` §D4 and §L4; the D4 smoke result of §1.1;
   the empty main 2680 run directory.
6. QAC root inventory: 1,642 roots. Title-root corpus frequency median 21 (min 1, max
   660); title-root dispersion median 14 surahs. **All 89 title roots are attested in
   QAC.**
7. Control-matching feasibility (§4.2): at ±×2 on both frequency and dispersion, 63 of 89
   pairs have ≥5 candidate control roots; 12 need ×4, 6 need ×8, 8 fall through to
   unrestricted; median candidate pool 16, min 3.

No null distribution was generated. No statistic under any null model was computed.

---

## 3. Metric, eponymous set, and tie convention

### 3.1 Frozen inputs (SHA-256, verified at runtime; any mismatch aborts)

| # | path | SHA-256 |
|:-:|:--|:--|
| 1 | `findings/phase-b-hypotheses/csv/h-new-1820.json` | `1a6282e451c1ff1d1cb5c0362fdfa22b6145a06bb286f66aa02a600987ea0842` |
| 2 | `data/morphology/quranic-corpus-morphology-0.4.txt` | `a1d12923815341face765083805d2148ed2d9f5cc3f7d6665219d887675d8c46` |
| 3 | `quran-text/quran-no-tashkeel.json` | `253f72f32f1dd4f6288c24be1b3b81b2e32c67aedd59aecb6e4a057dae35918a` |

### 3.2 THE metric — one, stated, primary

**Per-word density.** For surah `s` and root `R`:

```
density(R, s) = (QAC ROOT:R token count in s) / (orthographic word count of s)
```

Word counts from input 3; root counts from input 2 via the `ROOT:` feature on any
segment. **This is H-NEW-1820's own instrument** — it is what `h-new-1820.json`'s ranks
actually encode (§2.4), whatever that file's prose says.

Declared secondary tuples, reported in full, **never mixed into a single claim**:

- **T2 — raw count**: `count(R, s)`, no denominator.
- **T3 — per-verse**: `count(R, s) / verse count of s`.

**Only T1 (per-word density) is gated.** T2 and T3 carry no gate and cannot rescue or
overturn T1. Cross-metric substitution is the error being corrected here and is forbidden
by construction.

### 3.3 Tie convention — stated, because it is load-bearing

```
rank(R, s) = 1 + #{ s' : density(R, s') > density(R, s) }
```

Competition ranking on strict inequality: all surahs tied at a density share the same
(minimum) rank. This matters because **two eponymous surahs contain zero attestations of
their own title root** — Q 1 al-Fātiḥa (*ftH*) and Q 112 al-Ikhlāṣ (*xlS*) — and are
therefore tied with every other zero-count surah.

### 3.4 The eponymous set — taken verbatim, and audited

**The 89 (surah, title-root) pairs are read verbatim from input 1**,
`title_density_results[].{sid, root}`. They are **not re-derived**. H-NEW-1820 states
they came from al-Suyūṭī *al-Itqān* nawʿ 22 (*fī asmāʾ al-suwar*) with three exclusion
classes: personal names (12), muqaṭṭaʿāt (4), and roots not uniquely mappable.

**The 25 excluded surahs, enumerated here so the set is reproducible:**
5, 10, 11, 12, 14, 19, 20, 21, 23, 29, 30, 31, 34, 36, 38, 47, 50, 71, 72, 78, 80, 88,
93, 106, 114.

**Audit finding, disclosed before the run and NOT acted on.** 12 + 4 = 16, leaving 9
exclusions attributed to "could not be uniquely mapped," which H-NEW-1820 does not
itemise. I therefore **cannot fully reproduce the selection rule**, only the resulting
list. Because the brief requires the set be reused rather than silently re-derived, I use
it as given and record this as a limit (§8.2). Changing the set would make this
incomparable to the law it re-tests.

**Two published ranks do not reproduce**, and one is a genuine error:

| surah | root | published rank | recomputed | assessment |
|:--|:--|--:|--:|:--|
| Q 112 al-Ikhlāṣ | *xlS* | **112** | **18** | **ERROR in H-NEW-1820.** Q 112 has 0 *xlS* tokens; under the same convention Q 1 (also 0 tokens) was ranked 26. 17 surahs have *xlS* density > 0, so 18 is correct. This is a **third** uncaught error in that file, and it inflates the mean rank. |
| Q 77 al-Mursalāt | *rsl* | 20 | 19 | off-by-one, tie handling |

**This test uses the recomputed ranks under the single stated convention of §3.3**, and
reports both discrepancies. Note the direction: correcting Q 112 makes the eponymous
surahs look **better**, i.e. it strengthens the enrichment this test is evaluating. It is
recorded because it is true, not because it helps.

---

## 4. Registered statistics, nulls, and locked directions

Let `rank_i` be the rank of eponymous surah `i` in its own title root, `i = 1…89`.

### 4.1 Statistics — all three registered, the distribution first

- **S1 — rank-1 count**: `#{i : rank_i = 1}`. The law's own statistic. Locked
  **higher** than null.
- **S2 — median rank**: `median(rank_i)`. Locked **lower** than null. *(One-sided
  p = P(null median ≤ observed median).)*
- **S3 — mean reciprocal rank**: `MRR = (1/89) Σ 1/rank_i`. **The primary**, because it
  uses the whole distribution rather than thresholding it, is bounded in (0,1], and is
  sensitive to movement anywhere in the ranking. Locked **higher** than null.

The full **rank≤k curve** for k = 1,2,3,5,10,20,50 is reported for observed and null,
descriptively.

### 4.2 Null B — topicality-matched control roots (THE LOAD-BEARING NULL)

For each eponymous pair `(s, R)`: draw a control root `R'` uniformly from roots
**attested in s**, matched to `R` on **both** corpus frequency and dispersion:

```
freq(R)/m ≤ freq(R') ≤ freq(R)·m    and    disp(R)/m ≤ disp(R') ≤ disp(R)·m
```

where `freq` = total corpus token count, `disp` = number of surahs attested, and `m`
widens deterministically through **2 → 4 → 8** until at least **5** candidates exist,
falling back to all roots attested in `s` if 8 is insufficient. `R' ≠ R`. The widening
tier used per pair is recorded.

Then recompute all three statistics on the control ranks. 10,000 draws,
`random.Random(20260509)`.

**What this null does and does not rule out — stated now.** It conditions on the two
things that would otherwise manufacture the effect: *the root occurs in this surah at
all* (topicality), and *the root has this frequency and this concentration* (rarity and
peakedness). **It therefore cannot be beaten by the observation that "a root concentrates
where its topic is discussed" — that is built into it.** What it cannot rule out is that
surah titles were *chosen* by later transmitters precisely because the word is salient
there; this test cannot distinguish a compositional fact from a naming convention, and
§8.1 says so.

### 4.3 Null A — eponymy-pairing permutation (the weak null, reported for completeness)

Permute the 89 title roots across the 89 eponymous surahs, preserving both multisets.
10,000 draws, `random.Random(20260510)`.

**This null is expected to be trivially significant** and is registered as such in
advance: it destroys topicality entirely, so it answers only "does the specific pairing
matter," a question whose answer is not in doubt. It is reported because it is the
natural reading of "independence" and because refusing to report it would look like
concealment. **No claim in the finding may rest on Null A alone.**

### 4.4 Locked directions

| | direction |
|:--|:--|
| S1 rank-1 count | observed **>** null |
| S2 median rank | observed **<** null |
| S3 MRR | observed **>** null |

Per §1.2 these are informed by published prior art and are **not blind predictions**.

Replications of all six inferences at seed +10 (20260519, 20260520).

---

## 5. Decision gates

Family = **6 registered inferences**: {S1, S2, S3} × {Null A, Null B}.

- Bonferroni α = 0.05 / 6 = **0.008333**.
- Project novelty rule (`docs/statistical-rigor-protocol.md` §170) is stricter: corrected
  p < 0.005. **Raw decision gate = 0.005 / 6 = 0.000833**, i.e. `min(1, 6p) < 0.005`.

**A statistic PASSES iff its observed direction matches the lock AND both of its raw
p-values are < 0.000833.** Direction reversed, or either null failing, ⇒ NULL. No rescue
by threshold change, by dropping a null, or by substituting a secondary tuple.

**The runner must implement exactly this rule, and the script's verdict logic is to be
diffed against this section line by line before any verdict is published.**

### 5.1 Effect size is required, not optional

A p-value here is nearly meaningless — with 10,000 draws and a large sample the gate will
be trivially cleared if the effect is real. **The finding must lead with the effect
size**: observed S1 against the Null-B expectation, as a **rate ratio with a 95 %
interval** taken from the Null-B draw distribution, plus the observed and null median
ranks. Per §1.1 the expected ratio is around 1.75, and **a result near that value must be
reported as a modest enrichment, not as a vindication of either extreme.**

---

## 6. Verdict language, fixed now

Three claims must be kept apart, because H-NEW-1820 conflated them:

- **(a) "Eponymous surahs are usually not rank-1."** A descriptive fact. 47/89 stands
  regardless of any null, and this test does not challenge it.
- **(b) "Eponymy is independent of density rank."** The **law**. This is the claim a null
  can test, and it is false if S1/S3 pass.
- **(c) "Eponymy strongly predicts density rank."** The opposite overcorrection. Only
  supportable if the Null-B rate ratio is large; ~1.75× is **not** "strongly."

Outcomes:

- **S3 PASS under Null B** → **`PILLAR 4 RETIRED — independence is FALSE`**. The
  replacement statement must give the rate ratio and must say explicitly that (a) remains
  true while (b) is refuted, and must not assert (c) unless the ratio supports it.
- **S3 NULL under Null B** → **`INDEPENDENCE SURVIVES A TOPICALITY-MATCHED NULL`**. The
  law is reinstated *as a statement about the matched null only*, never as "titles are not
  chosen for density."
- **Null A passes, Null B fails** → the effect is topicality, not eponymy. Report as
  `TOPICALITY-EXPLAINED`, and the law survives in its useful form.
- Any T1/T2/T3 disagreement → `METRIC-FRAGILE`, reported with all three side by side.

**I am explicitly permitted to retire a pillar law and explicitly forbidden to
overcorrect.** Neither protecting H-NEW-1820 nor maximising the reversal is acceptable;
the rate ratio decides the wording.

---

## 7. Robustness (reported; never replaces §4)

1. **Zero-attestation cases.** Q 1 and Q 112 have no token of their own title root. All
   statistics are recomputed with those two excluded; reported as a sensitivity.
2. **Widening-tier breakdown** for Null B, with the statistics recomputed on the 63 pairs
   that matched at ×2 only — the strictest matching.
3. **Full rank≤k curves**, observed vs Null-B mean, k ∈ {1,2,3,5,10,20,50}.
4. **Per-surah table**: sid, title, root, frequency, dispersion, observed rank under all
   three metrics, and Null-B mean rank.
5. **Frequency and dispersion strata**: S1 and median rank split by title-root frequency
   tertile, to show whether the effect is carried by rare roots.
6. **The 42 rank-1 and 47 non-rank-1 sets** reported explicitly so the descriptive claim
   (a) remains checkable.

---

## 8. Honest limits, written before the result exists

### 8.1 The limit that no null in this design can address

A surah's title is, for most surahs, a **later transmitted convention**, not part of the
revealed text — the same editorial-layer problem as the waqf marks. If transmitters named
a surah after a word *because* it is salient there, then enrichment is a fact about
**naming practice**, not about the text's composition. **This test cannot separate the
two**, and no permutation over roots can. Every result must be worded as a statement
about the relationship between the received titles and the text, not about authorial
design.

### 8.2 Others

1. **The eponymous set's selection rule is not fully reproducible** (§3.4): 9 of 25
   exclusions are unexplained. The set is reused as given for comparability.
2. **H-NEW-1820 contains at least three arithmetic/consistency errors** (the reverted
   48/89, the 42+48=90 arithmetic break, and the Q 112 rank of 112). Its JSON is used
   only as the **eponymous-set source**; every rank is recomputed here.
3. **Titles map to roots one-to-one by assumption.** Compound and phrasal titles
   (*Āl ʿImrān*, *al-Muṭaffifīn*) are reduced to a single root by H-NEW-1820's mapping,
   which I did not audit item by item.
4. **Null B draws control roots from a surah's own attested roots**, so surahs with few
   distinct roots have small candidate pools (min 3). Recorded per pair.
5. **QAC root assignment is itself an annotation**, and roots are not senses.
6. **The direction lock is not blind** (§1.2).
7. **No cross-corpus control.** No other corpus has an equivalent eponymous-title system,
   so nothing here can be shown to be Quran-specific.

---

## 9. Required immutable run record

The run creates `findings/phase-b-hypotheses/runs/h-new-2710/<UTC timestamp>/` containing
`result.json` and `manifest.json` (command, git commit, prereg/script/input SHA-256,
Python version, seeds, platform). **Paths recorded in the manifest must be relative to
the repository root** so the run is committable as-is.

**Nothing in any run directory may ever be overwritten or deleted, including an
uncommitted or superseded one** — the standing correction at
`h-new-2540-form-v-valency.md` §8.1. This explicitly includes the empty
`runs/h-new-2680/20260807T011917Z/`, which is another test's record and is not touched.

The runner emits no interpretive prose.
