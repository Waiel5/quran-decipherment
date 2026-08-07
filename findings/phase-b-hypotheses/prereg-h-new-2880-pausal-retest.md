---
id: H-NEW-2880
title: "Pre-registration — the pausal-fāṣila question re-tested against a null matched on class CONCENTRATION, not merely class COUNT"
date: 2026-08-07
author: Waiel Al-Shujaa
status: LOCKED — written and SHA-256'd BEFORE any null draw, any agreement-vs-null comparison, and any p-value of the new design
family: RHYME-2026-08-07
frontier_item: F-16
parent: H-NEW-2870 (verdict NULL by its locked grid; its §9 shows the null that produced that verdict was ill-posed)
method_parent_1: H-NEW-2870 §9 (the concentration diagnostic)
method_parent_2: findings/UNIT-DRIFT-DEFECT.md §4.1 ("a null that cannot draw the thing it compares against is not a comparison")
seed: 20260509
seed_replication: 20260519
n_perm: 10000
n_recut: 2000
bonferroni_k: 18
alpha_bonferroni: 0.00277778
---

# Pre-registration — H-NEW-2880

**Nothing here may be amended after the SHA-256 is embedded in
`scripts/h-new-2880.py`.** The null constructions are locked in §5, the anti-gaming gates in
§6, the directions in §7, the decision rules in §8, the reporting order in §9, the failure
conditions in §12. **The runner's verdict logic will be diffed against §8 and printed before
any verdict is declared** (`STATE-OF-THE-PROJECT-2026-08-07.md` §4.4).

---

## 1. The question, and what is actually unresolved

H-NEW-2870 asked whether the Qurʾān's fāṣila is defined at **pausal** phonology (*waqf*)
rather than at the fully-vocalised **citation** (*waṣl*) form. Its locked verdict is **NULL**
(p = 0.0058 against α_bon = 0.003125 on the arm that decided it). **That verdict stands. It is
not being overturned here, and this pre-registration does not treat it as a result to be
rescued.**

What H-NEW-2870 established *post-hoc*, in its §9, is that the arm which produced the NULL was
ill-posed:

| H-NEW-2870 §9, rime definition R2 | value |
|:--|--:|
| N1-a draws reaching or beating the observed A(P1) | 57 / 10,000 |
| **their own chance floor Σpᵢ², mean** | **0.2879** |
| all other draws' chance floor, mean | 0.2066 |
| **the real pausal partition's chance floor** | **0.1687** |
| share of winning draws MORE concentrated than the real partition | **57 / 57 = 100 %** |
| corr(A_null, floor_null) over all draws | **+0.6805** |

Under the tighter regime (R1) the same figures are 11/11 = 100 % and ρ = +0.7063.

**Matching a null on the class COUNT does not match it on class CONCENTRATION, and
concentration buys rhyme agreement for free.** Every draw that beat the observation did so by
being a coarser merge than *waqf* performs, not by being a better one. The question is
therefore genuinely open, and H-NEW-2880 exists to close it with a null that is correct by
construction.

### 1.1 The confound, stated exactly

Merging classes raises adjacent-verse agreement arithmetically. Under an independence model
the free gain is exactly the **chance floor** Σᵢpᵢ², where pᵢ is the verse share of class *i*.
A null that draws more concentrated partitions than the observed one therefore hands its own
draws extra agreement that the observation never received. **The floor is the nuisance
channel, and the requirement on any admissible null is that the floor be held at the observed
value — not approximately, and not on average.**

---

## 2. What is already known, and therefore what this pre-registration can and cannot lock

**Stated first, because pretending otherwise would be dishonest.** H-NEW-2870 is published.
The following quantities are already on the record and are *re-computed* here, not predicted:

| quantity (rime R2) | published value |
|:--|--:|
| A(C) citation agreement | 0.3484 |
| A(P1), A(P2) | 0.5353, 0.5364 |
| Δ(P1), Δ(P2) | +0.1869, +0.1880 |
| K(C) → K(P1) | 397 → 116 (collapse 3.42×) |
| chance floor, C / P1 | 0.1068 / 0.1687 |
| arithmetic share of Δ | 33.1 % |

**What is pre-registered here is the NULL, the anti-gaming gates, the primary statistic, the
locked direction and the decision rule — none of which has been computed.** No draw from any
null defined in §5 has been generated, and no agreement value has ever been compared against
any distribution under this design. §11 lists everything that *was* inspected before locking,
in full.

---

## 3. Frozen inputs (SHA-256 verified at runtime; mismatch is fatal)

| path | SHA-256 | role |
|:--|:--|:--|
| `findings/phase-b-hypotheses/scripts/h-new-2870.py` | `9765a448256a93dc740ceb1dcd56ffbb58f33aa8a6192f855ad3579af07d2dde` | **the instrument, pinned.** §§0–6 of the parent runner (phonemiser, conventions, rime extractor, gates) are executed verbatim so the two findings cannot drift apart |
| `quran-text/quran-full-tashkeel.json` | `382a7341300602ec8b366316d4bbe2a44955c2bf984d395bdd82dae6110b6715` | primary text |
| `data/alt-text/quran-uthmani-txt.txt` | `e5e7e54988877d6164832d55435135a563b9cfc249e0c8efd73e9e7f23231db8` | Tanzil Uthmani v1.1 — orthography gate only |
| `data/baseline-corpora/raw/muallaqa-imru-al-qais.txt` | `06f05f6a299d989fcaf330f43f7fba9116b373f94096d38ec07df71432f59c14` | positive control |
| `data/baseline-corpora/raw/muallaqa-zuhayr.txt` | `9a8aac1838323aaa65f916f597ec38c842b74eed77ce44f53c2932b52e6610c2` | positive control |
| `data/baseline-corpora/raw/muallaqa-amr-bin-kulthum.txt` | `d93a81bd2095c7db00417650f883c834077fac12668e50002c8b35f26e2ef720` | positive control |
| `data/baseline-corpora/raw/bukhari-noquran.txt` | `0169b60de7585a51fc340161488534c4d909370c3dcc8951ca2ae3818c44a100` | negative control (delta blocked — §10) |
| `data/baseline-corpora/raw/jahiz-hayawan.txt` | `419095484df4e315eba889d38a9c2f6edff55c2f10f481ed9ad024e07bbff0cd` | negative control (delta blocked — §10) |

The parent pre-registration `prereg-h-new-2870-pausal-rhyme.md`
(`119753ad7862d66dfead2ff6de1032adee0a824cd7544cd8bc4d6688587508d4`) is verified as a
by-product of executing the pinned instrument, which checks it itself.

---

## 4. The instrument — inherited unchanged, and re-gated

No change is made to the phonemiser, the pausal conventions (C, P1, P2, P3), the rime
extractors (R1 as pre-registered by the parent, R2 the tanwīn-transparent repair), or the two
gates. **Gate A (orthography, ≥ 99 % on each of six tanwīn marks) and Gate B (6/6 against
H-NEW-2240) are re-run and printed before any statistic. If either fails, the run stops.**

### 4.1 Why R2 is the primary rime definition and R1 cannot carry the new nulls

Every null in §5 permutes the assignment of **citation types** to **pausal classes**. That
operation is defined only if the pausal partition is a *coarsening* of the citation partition —
i.e. if every citation type maps to exactly one pausal class. Measured before locking (§11):

| rime | citation types split across pausal classes | verses in split types | block sizes reconstruct exactly from type sizes |
|:--|--:|--:|:--|
| **R2** | **0** | **0 (0.00 %)** | **yes, exactly** |
| R1 | 2 | 1,059 (16.98 %) | **no** — max discrepancy 710 verses |

**Under R1 the operation is undefined and the null would be ill-posed by the parent's own
§12 failure condition.** R1 is therefore carried only for the controls that do not require
the map (the class-collapse magnitude, the re-cut control D3, the poetry control D4, the
per-surah table). **The new nulls are run under R2 only, and that is decided here, before any
of them is computed, on a structural fact and not on a result.**

---

## 5. The nulls — the whole point of this finding

### 5.1 The requirement, stated before any construction

> An admissible null draw must have **the same class-size multiset** as the real pausal
> partition — hence the same K, the same K_eff, the same maximum class size and the same
> chance floor Σpᵢ² — and must differ from the observation **only** in which citation endings
> are grouped together.

### 5.2 N-EXACT — three constructions, all exact, S2 primary

Let the citation form partition the 6,236 verse-ends into M = 397 types with verse-counts
s₁ … s_M, and let the observed pausal partition group those types into K blocks with verse-counts
n₁ … n_K (K = 116 for P1, 115 for P2). A draw assigns every citation type to a block so that
the achieved block verse-counts equal n₁ … n_K **exactly**.

All three constructions process the types in **descending size order** with uniform random
tie-breaking inside each equal-size group, and differ only in how the receiving block is chosen:

| tag | block choice | role |
|:--|:--|:--|
| **S2** | sampled from the blocks with remaining capacity ≥ sᵢ, **with probability proportional to remaining capacity** (if none has capacity, the block with the largest remainder) | **PRIMARY** |
| S1 | the block with the largest remaining capacity (random tie-break) | robustness |
| S5 | best fit — the block with the *smallest* remaining capacity that still admits sᵢ (random tie-break) | robustness |

**S2 is locked as primary on a property of the null, measured before locking and never on a
test statistic** (§11.4): over 200 trial draws of each construction all three reproduced the
target profile exactly (total-variation distance 0.0000, floor 0.168712 with standard
deviation 0.00000), and S2 produced the **least mutually structured** draws — mean pairwise
adjusted Rand index between independent draws 0.013, against 0.099 for S1 and 0.188 for S5.
S2 therefore explores the constraint set most fully and imposes the least construction
artefact. All three are reported.

**Exactness is enforced, not assumed.** Any draw whose achieved block-size multiset differs
from the target is **rejected and redrawn**; the rejection rate is reported. If it exceeds
1 % the construction is declared defective and no p-value is reported from it (§6, G1).

### 5.3 Why this null cannot be gamed by concentration — the argument, to be demonstrated

Every draw has, by construction, the identical block-size multiset, and therefore the
identical K, K_eff, maximum block size, Simpson index and chance floor Σpᵢ². **The nuisance
channel has exactly zero variance across the null distribution.** No draw can beat the
observation by being coarser, because no draw is coarser, finer, or differently shaped: the
only thing that varies between draws is *which citation endings share a class*, which is
precisely the phonological content the hypothesis is about.

This is stronger than conditioning on the floor within a band, and strictly stronger than
matching the class count (N1-a) or the per-block cardinality (N1-b). It is the answer to
§1.1's requirement, and §6 turns it into a gate rather than a claim.

### 5.4 N-A — the exact within-size-class permutation, reported as a bound, NOT gating

A second exact null: permute the block labels of the citation types **within each size class**
(all types of verse-count s exchange freely). Every block sum is preserved identically, so
this too is exactly matched.

**Its freedom was measured before locking and it is limited**: 370 of 397 types are movable
(93.2 %), but they carry only **1,538 of 6,236 verses — 24.7 %**. The four largest citation
types (1,656 / 1,065 / 295 / 253 verses) each have a unique size and are frozen. This is not
a defect of the implementation but a property of any exact-sum null under this size profile:
the largest citation type (1,656 verses) sits in the only block whose total (1,751) can hold
it, so **no exact-sum exchange can move it at all.**

**N-A is therefore pre-registered as a LOW-POWER BOUND. It is reported with its measured
freedom and it does not gate the verdict.** Its failure would be uninformative; its passing
would be additional evidence.

### 5.5 N-STEM — the lexical-repetition control, secondary and non-gating

*Waqf* merges the case-variants of a single stem (`-ūna` / `-ūnu` / `-ūni` → `-ūn`). A stem
recurs within a surah for lexical reasons, so part of any gain could be repetition rather than
composition. **Locked control:** restrict the statistic to adjacent cross-type pairs whose two
verse-ends fall in **different P3 classes** — P3 being the truncation-only tuple, which drops
the final vowel and the tanwīn without the compensatory *ā*. Two endings in different P3
classes cannot be merged by mere truncation of a shared skeleton; merging them requires the
transformational rule *−an → ā*. The observed merge rate on that sub-population is compared
against the same S2 null. Reported with a p-value; **does not gate.**

### 5.6 The primary statistic and the locked direction

> **Primary statistic: E = A(P) − Σpᵢ²(P)**, the excess of adjacent-verse rhyme agreement over
> the chance floor of its own partition. **Locked direction: E_observed > E_null, one-sided.**
> p = (1 + #{null E ≥ observed E}) / (1 + 10,000).

E is pre-registered as primary **here**, before any output, rather than reached for after a
failure — which is the difference between a repair and a result. Under N-EXACT the floor is
constant across draws, so E and the raw agreement A are the same test and must return
identical p-values; **that identity is itself checked and reported** (§6, G1). A is reported
alongside E throughout.

### 5.7 The nulls of H-NEW-2870, re-measured here as diagnostics only

N1-a (verse-count-profile-matched) and N1-b (cardinality-matched) are re-implemented verbatim
and run, **not to produce a verdict, but to measure their floor distributions** against the
observed 0.1687 and to supply the instrument positive control of §6, G2. They gate nothing.

---

## 6. Anti-gaming gates — printed BEFORE any p-value, and each one can stop the run

| gate | requirement | consequence of failure |
|:--|:--|:--|
| **G1 — exactness** | for every retained draw of N-EXACT (S2, S1, S5) and N-A: achieved block-size multiset **identical** to the observed; hence \|floor_null − floor_obs\| = 0, and K, K_eff, max block size identical. Redraw rate < 1 %. The p-value on E and the p-value on A must be **equal**. | the null is declared defective; **no p-value is reported from it** |
| **G2 — the diagnostic has teeth** | re-implement H-NEW-2870's N1-a verbatim and measure corr(A_null, floor_null). **Required ≥ +0.50** (the parent reports +0.6805 under R2). | the diagnostic is not detecting a defect that is known to be present, so it is measuring nothing — **stop the run** |
| **G3 — non-degeneracy** | mean adjusted Rand index between each N-EXACT draw and the real pausal partition **< 0.10**, and sd(A_null) **> 0.001** | the null is a copy of the observation, or has no variance; **no p-value is reported** |
| **G4 — can the null draw the observed thing?** | report, for every null including N1-a and N1-b, the share of draws whose chance floor lies within ±2 % of 0.1687. For N-EXACT this must be **100.0 %**. | reported as the decisive descriptive diagnostic either way (`UNIT-DRIFT-DEFECT.md` §4.1) |

**In addition, and reported whether or not it is degenerate:** corr(A_null, floor_null) for
every null. For N-EXACT the floor has zero variance, so the correlation is *undefined*; the
finding must say so explicitly and print the measured variance rather than quoting a
convenient zero. The §9 upper-tail diagnostic of the parent — the mean floor of the draws that
reach or beat the observation — is reported for every null as well.

---

## 7. Directions — LOCKED

| # | direction | locked prediction |
|:--|:--|:--|
| **D1** | Δ(P1) > 0 and Δ(P2) > 0 | pausal reduction increases adjacent rhyme agreement |
| **D2** | **E(P) > N-EXACT null**, under S2, S1 and S5, for P1 and P2 | the specific mergers *waqf* performs create rhyme agreement beyond what **any** regrouping of identical coarseness achieves |
| **D2ᴀ** | E(P) > N-A null | secondary; low power, non-gating |
| **D2ˢ** | merge rate on non-truncation pairs > N-EXACT null | secondary; non-gating |
| **D3** | Δ(Qurʾān) > Δ(pseudo-fāṣila re-cut) | the gain is a property of the **composed** boundaries |
| **D4a** | A(C) poetry > A(C) Qurʾān | poetry already rhymes at citation form and does not need pausal reduction |
| **D4b** | Δ(Qurʾān) > Δ(poetry) | as above, on the delta |

**A reversal of D1 or D4a is a major negative and is reportable as such.**

**What a D2 PASS would and would not mean, locked before the result.** It would mean that
*waqf*'s merges group citation endings that actually stand next to one another in the mushaf,
where a random regrouping of identical coarseness does not. It would **not** by itself
exclude lexical repetition of a shared stem — which is why D2ˢ exists and is reported
whatever D2 returns.

---

## 8. Decision rules

**Registered inference family — 18 tests, enumerated so the count is auditable:**

| # | test |
|:--|:--|
| 1–2 | D2 under **S2** (primary null) × {P1, P2}, rime R2 |
| 3–4 | D2 under S1 × {P1, P2}, rime R2 |
| 5–6 | D2 under S5 × {P1, P2}, rime R2 |
| 7–8 | D2ᴀ under N-A × {P1, P2}, rime R2 — non-gating |
| 9–10 | D2ˢ under S2, non-truncation pairs × {P1, P2}, rime R2 — non-gating |
| 11–14 | D3 re-cut × {P1, P2} × {R1, R2} |
| 15–18 | D4b poetry × {P1, P2} × {R1, R2} |

**Bonferroni k = 18, α = 0.05 / 18 = 0.00277778, one-sided in the locked direction.**
This is stricter than the parent's α = 0.003125. Resolution: 1/10,001 = 0.0001 for the
permutation tests and 1/2,001 = 0.0005 for the re-cut — both below α. ✔

**Verdict grid, locked:**

| outcome | verdict |
|:--|:--|
| Gate A, Gate B, or any of G1–G3 fails | **INSTRUMENT BROKEN / NULL DEFECTIVE** — no verdict, and the reason is the finding |
| D1 reverses | **REVERSED** — major negative |
| **D4a reverses** (poetry does not out-rhyme the Qurʾān at citation form) | **CONTROL FAILED** — the positive control does not behave, and no D2 result may be cited |
| **any of tests 1–6 fails at α** | **NULL — the gain is arithmetic even at matched concentration.** This leads the write-up regardless of every other result |
| tests 1–6 all pass **and** D3 passes under both tuples at R2 | **PASS** — the fāṣila is materially better defined at pausal phonology, and the effect is compositional |
| tests 1–6 all pass but D3 fails | **PARTIAL** |

Tests 7–10 (N-A, N-STEM), the R1 arms, P3, the prose level comparison, the per-surah table and
the class-collapse magnitude are **descriptive and gate nothing**. They are all reported.

**The runner's verdict logic will be diffed against this section, printed, before any verdict
is declared.**

---

## 9. Reporting order — LOCKED

1. Gate A (orthography) and Gate B (instrument).
2. **The class-collapse magnitude** — K(C), K(P), K_eff, the collapse factor, the chance-floor
   rise and the free arithmetic gain. **Before any headline number**, exactly as H-NEW-2870 did.
3. **The anti-gaming audit** — G1–G4, the floor distribution of every null including the
   parent's two, and corr(A_null, floor_null) for each.
4. Only then the **N-EXACT result** for S2, S1, S5, and then N-A and N-STEM.
5. The three control texts, with the prose blocker stated in the prose row itself.
6. The per-surah table and the exceptions.

---

## 10. Controls retained from H-NEW-2870, and one that remains blocked

- **Both pausal tuples** — P1 (minimal: final short vowels and tanwīn; tanwīn fatḥ → *ā*) and
  P2 (full: P1 plus tāʾ marbūṭa → *hāʾ*). P3, the deliberately-wrong truncation tuple, is
  retained descriptively and drives N-STEM.
- **Positive control — pre-Islamic poetry.** The same three muʿallaqāt selected by the parent's
  pre-declared ≥ 0.9 line-final vocalisation threshold, primary arm on readable pairs.
  Monorhymed by construction, so it should already rhyme at the citation form (D4a) and should
  not need pausal reduction (D4b).
- **Negative control — prose. THE DELTA REMAINS NOT COMPUTABLE, and this is declared again
  before running.** Re-measured before locking (§11.5): every prose text on disk carries
  **zero** ḥarakāt (`bukhari-noquran.txt` 0 over 2,056,880 Arabic characters;
  `jahiz-hayawan.txt` 0 over 1,422,374; `sira-ibn-hisham.txt` 0 over 1,090,188), and
  `bukhari.txt` carries 0.61 % scattered. **The citation form cannot be recovered from a text
  that never wrote its final short vowels.** Automatic vocalisation would substitute a model's
  output for data and will not be used. The **level** comparison on the skeleton instrument,
  length-matched, is retained and is **not** described as a control on the delta.
- **The within-corpus re-cut control (D3)**, which needs no baseline text and is the effective
  negative control on the delta.
- **The class-collapse magnitude reported before any headline number.**

---

## 11. Garden of forking paths — everything inspected before this pre-registration was locked

Declared in full, per `feedback_specialist_judgment_overrides_team_lead_method`.

1. Read `STATE-OF-THE-PROJECT-2026-08-07.md` (standing warning and §§0, 4),
   `findings/UNIT-DRIFT-DEFECT.md` in full, `h-new-2870-pausal-rhyme.md` in full,
   `prereg-h-new-2870-pausal-rhyme.md`, `scripts/h-new-2870.py` and
   `scripts/h-new-2870-posthoc.py`, and `runs/h-new-2870/20260807T131820Z/result.json`.
2. **All of H-NEW-2870's published values are known to me** — its agreements, deltas, class
   counts, chance floors, null means and p-values, including the fact that its N1-b returned
   0/10,000. §2 states this. **No value of any null defined in §5 is known.**
3. **Structural inspection of the partition, which was needed to know whether an exact null is
   constructible at all.** Measured: M = 397 citation types; K = 116 (P1) / 115 (P2) pausal
   blocks under R2 with **zero** split types and block sizes reconstructing exactly; under R1,
   2 split types covering 1,059 verses and reconstruction failing by 710 verses (§4.1). Block
   size profile 1751, 1293, 1192, 551, 178, … ; type size profile 1656, 1065, 295, 253, … ;
   51 distinct size classes, the largest being 165 types of size 1. Within-size-class freedom
   370/397 types but only 24.7 % of verses (§5.4), and the largest type provably frozen under
   any exact-sum exchange.
4. **Proposal-fidelity comparison of five candidate constructions**, 200 draws each, measuring
   *only* total-variation fidelity to the target profile, the induced chance floor, and
   adjusted Rand indices. **No agreement value, no delta and no p-value was computed for any
   of them.** Result: S1, S2, S3 (capacity² weighting) and S5 all achieved TV = 0.0000 and
   floor 0.168712 with zero variance; a uniform-random processing order — which is what the
   parent's N1-a uses — achieved TV = 0.1918 and floor 0.2657. S2 was selected on the
   least-structured criterion of §5.2; S3 is dropped as a near-duplicate of S2 and is not
   reported. This is the one design choice made after measurement, it was made on a property
   of the null and not on a result, and it is declared here.
5. **Vocalisation census of every baseline corpus on disk** (36 files), which re-established
   the prose blocker of §10. This is an encoding fact, not a test statistic.
6. **No draw from N-EXACT, N-A or N-STEM has been generated, and no agreement value has been
   compared against any distribution under this design.**

---

## 12. Failure conditions — what makes this finding wrong

- **Gate A < 99 %, or Gate B < 6/6** → instrument broken; stop.
- **G1 fails** (any draw not exactly matched, or redraw rate ≥ 1 %, or the E-test and A-test
  p-values differ) → the null is defective by the very criterion this finding was written to
  enforce; **report that and no p-value.** It would be the same error as the parent's, one
  level up, and it must be stated as such.
- **G2 fails** → the concentration diagnostic cannot see a defect known to be present; stop.
- **G3 fails** → the null is degenerate; no p-value.
- **E(P) inside the N-EXACT null** → the gain is arithmetic even at matched concentration.
  **NULL verdict, and the question is closed.** That is a real answer and it leads the
  write-up.
- **D4a reverses** → the positive control has failed and nothing else may be cited.
- **The re-cut reproducing Δ** → the delta is a property of Arabic word-final morphology, not
  of the fāṣila.
- Residual limits that no available data can remove: the prose delta (§10); the absence of a
  citable classical *waqf* anchor on disk (H-NEW-2870 §12 — al-Suyūṭī's Itqān PDF is a partial
  translation lacking the *waqf* nawʿ, al-Zarkashī's Burhān is a scan with no text layer, and
  no Ibn al-Jazarī is on disk); and the fact that the "citation form" is the Ḥafṣ mushaf's
  written iʿrāb, itself a recitational tradition and not a neutral baseline.
- **A limit this design cannot remove**: N-EXACT holds the class-size multiset fixed but
  cannot separate "*waqf* merges endings that stand next to each other because the text was
  composed to rhyme in pause" from "*waqf* merges case-variants of a stem that recurs within a
  surah for lexical reasons". N-STEM (§5.5) bounds that, it does not eliminate it, and the
  finding must say so in its honest limits whatever the verdict.

---

## 13. Run discipline

Immutable run directory `runs/h-new-2880/<UTC>/`, created with
`os.makedirs(..., exist_ok=False)`; every output opened with mode `'x'`; manifest paths
repo-relative; **checkpoints written OUTSIDE the run directory** (`UNIT-DRIFT-DEFECT.md` §7 —
a script must never overwrite a file inside its own run directory). **No run directory is ever
deleted.** This pre-registration's SHA-256 is embedded as a literal in the runner and verified
at runtime; all frozen inputs are SHA-256 verified. Every permutation test is replicated at
seed 20260519.

*Bismillāhi al-Raḥmāni al-Raḥīm.*
