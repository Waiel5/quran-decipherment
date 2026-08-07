---
prereg_id: H-NEW-2810
title: Re-deriving the hard-coded literals — every published baseline that circulates as a constant
author: Waiel Al-Shujaa
date: 2026-08-07
phase: C
status: PRE-REGISTERED — locked before any derived value was computed
method_parent: [H-NEW-2790]
rule_applied: findings/UNIT-DRIFT-DEFECT.md §6.3 (UNVERIFIABLE)
seeds: 20260509 primary / 20260519 replication
script: findings/phase-b-hypotheses/scripts/h-new-2810.py
run_dir: findings/phase-b-hypotheses/runs/h-new-2810/
---

# Pre-registration — H-NEW-2810

**Nothing in §§4–6 had been computed when this file was written.** What was known at lock time
is the *provenance inventory* of §2 — which literals exist, where they are consumed, and whether
a script or a result JSON exists for each. That is a filesystem fact, not a derived value, and it
is exactly what §6.3 of the rule document specifies as the cheap pre-screen. **No re-derived
number of any kind existed before this lock.**

---

## 0. The defect being audited

`findings/UNIT-DRIFT-DEFECT.md` §6.3 established a fourth screen outcome:

> **UNVERIFIABLE — the claim's headline numbers are not produced by any code in the repository.**

Such a number is worse than an unaudited one. It is consumed by downstream scripts as a fixed
input — sometimes as a *decision threshold* — so every result built on it inherits an unverified
constant while appearing corroborated by the citation. **This audit re-derives them.**

---

## 1. The generator — how the literals were found, not which ones I remembered

The inventory was produced by a **scan, not by recall**: every `.py` under `scripts/` and
`findings/phase-b-hypotheses/scripts/` was searched for a numeric literal bound to a key naming
*another* finding, on the pattern `["']?h[_-]new[_-]NNN…["']?\s*[:=]\s*<number>`. **Thirteen
matches; nine distinct literals; four of the nine I had not previously identified** (L6–L9).
One match — `h_new_900_cross_text.py:490` — is a comment recording a window count, not a claimed
value, and is excluded with the reason stated.

---

## 2. The nine literals, with provenance established before the lock

The §6.3 check is two questions: **does a script produce it, and does a result JSON contain it?**

| tag | literal | source claim | consumed at (file:line) | script? | result JSON? | pre-lock status |
|:--|--:|:--|:--|:-:|:-:|:--|
| **L1** | **0.759** | H-NEW-192 Ridge LOOCV R², mushaf position, 15 features | `h_new_233_ensemble_predictor.py:571`, `:532`; `h_new_250_equation_fit.py:670` | **NO** | **NO** | **UNVERIFIABLE** |
| **L2** | **0.817** | H-NEW-192 RF LOOCV R², same | `h_new_233_ensemble_predictor.py:572`, `:533`; `h_new_250_equation_fit.py:671` | **NO** | **NO** | **UNVERIFIABLE** |
| L3 | 0.836 | H-NEW-183 Ridge LOOCV R², Nöldeke rank | `h_new_233_…:573`; `h_new_250_…:674` | yes | yes — `0.8355931448330429` | verifiable |
| L4 | 0.7395 | H-NEW-233 Ridge, 29 features | `h_new_250_…:672` | yes | yes — `0.7395490015311565` | verifiable |
| L5 | 0.8485 | H-NEW-233 RF, 29 features | `h_new_250_…:673` | yes | yes — `0.848516936603147` | verifiable |
| L6 | 0.4138 | H-NEW-88 RF LOOCV top-1 | `h_new_179_alpha_beta_predictor.py:533` | yes | yes — `0.41379310344827586` | verifiable |
| L7 | 0.6552 | H-NEW-165 RF top-1 | `h_new_275_bukhari_opener_phonological_replication.py:385` | yes | yes — `0.6551724137931034` in `h-new-165-2.json` | verifiable |
| L8 | 136 | H-NEW-1710 total Mūsā mentions | `Q028_F_06_musa_density_rank.py:126` | **NO** | yes — `h-new-1710.json` `/prophet_name_distribution/Mūsā/total` | verifiable **from the corpus** |
| L9 | 0.9230 | H-NEW-1395 null uniform mean | `Q030_F_08_alm_cluster_fr_cohesion.py:184` | yes | yes — `0.9229932999809524` | verifiable |

**Only L1 and L2 fail both checks.** The other seven are re-derivable against an existing
artifact; they are audited anyway, because a literal can be a *wrong rounding* of a real number
and that is a correction worth making.

---

## 3. What each derivation is, method by method

### 3.1 L3–L7, L9 — literal-against-artifact
Read the value the producing script actually emitted, from its frozen result JSON. Compare the
circulating literal to it. **This tests the transcription, not the computation** — the
computation is already reproducible by definition of having a script — and the finding will say
so rather than claim more.

### 3.2 L8 — re-derive from the corpus
`h-new-1710.json` records 136 but no script produces that file. The literal is therefore
re-derived **from the Leeds QAC morphology directly**: count tokens whose lemma is the proper
noun *Mūsā*, over the whole corpus, under the rules-tuple `Q028-F-06` declares
(`QAC-PN-lemma + no-tashkeel-orthographic, basmala-counted-only-in-Q1, Ḥafṣ-Kūfan`).
**A useful internal control exists and is registered here:** `Q028-F-06` independently computes
`corpus_total_musa_qac` in the same run that hard-codes 136, so its own output already contains a
second opinion. Both are reported.

### 3.3 L1, L2 — the exhaustive feature-set search

This is the substance of the audit. H-NEW-192 has **no script**, and names only **10** of the
**15** features it claims. H-NEW-2790 tried two hand-built reconstructions and neither reproduced
the Ridge literal (0.8026 and 0.8041 against 0.759). **Two reconstructions failing is not
evidence that no reconstruction succeeds.** So the question is asked exhaustively:

> **Is there ANY 15-feature set, containing the ten features H-NEW-192 names, drawn from the
> feature pool available in this repository, that yields Ridge LOOCV R² = 0.759?**

**The pool** is H-NEW-233's 29 columns (`BASE_FEATURES` + `EXPANSION_FEATURES`) plus
`divine_name_density` and `legal_term_density` from H-NEW-125 — **31 columns**, being every
per-surah feature this repository can build from frozen artifacts.

**The ten named features are fixed in every candidate**, mapped to columns as:
`verse_count`, `mean_verse_len`, `eschat_density`, `type_token_ratio`, `divine_name_density`,
`loanword_density`, `qul_density`, `legal_term_density`, `muq_cardinality`, `refrain_score`.

**The remaining five are chosen from the other 21** → **C(21,5) = 20,349 candidate sets**, each
scored by Ridge LOOCV R² using H-NEW-183's frozen `loocv_ridge` verbatim. This is exhaustive over
the stated space, not a sample.

**A second, independent recovery channel is registered**, because H-NEW-192 publishes an RF
importance vector as well as an R²:

| rank | feature | published importance |
|--:|:--|--:|
| 1 | verse_count | 0.416 |
| 2 | mean_verse_length | 0.173 |
| 3 | eschatological_density | 0.125 |
| 4 | type-token ratio | 0.095 |
| 5 | divine_name_density | 0.053 |
| 6 | loanword_density | 0.048 |
| 7 | qul_density | 0.039 |
| 8 | legal_density | 0.012 |
| 9 | muq_cardinality | 0.010 |
| 10 | refrain_score | 0.009 |

**These sum to 0.980**, so the five unnamed features together carry **0.020** — a strong
constraint registered in advance: any genuine reconstruction must place ~2 % of total importance
on its five extra columns, and must rank the named ten in exactly this order.

RF is too expensive to run on all 20,349 sets. **Locked two-stage design:** Channel A (Ridge)
runs exhaustively; Channel B (RF importances, 200 trees) runs on the **50 candidates closest to
0.759 on Ridge**, plus **50 uniformly-sampled controls** at seed 20260509 so the Channel-B
statistic has a null to be read against.

---

## 4. LOCKED tolerances

| quantity | tolerance for a match | reason |
|:--|:--|:--|
| Ridge LOOCV R² vs 0.759 | **\|Δ\| ≤ 0.0005** | the literal is quoted to 3 dp, so anything rounding to 0.759 |
| RF LOOCV R² vs 0.817 | **\|Δ\| ≤ 0.005** | RF is seeded but library-sensitive; ten times looser than Ridge |
| literal vs artifact (L3–L9) | the literal must be the correct **round-half-up** of the artifact value at the literal's own precision | a transcription test, not a tolerance |
| RF importance vector | max abs deviation ≤ 0.02 across the ten, **and** identical rank order | 0.02 is the total mass the five unnamed features carry |

---

## 5. LOCKED decision rule — diff the runner against this section

```
CONFIRMS       the derived value equals the circulating literal within §4

CORRECTS       the derived value exists and differs from the literal beyond §4
               -> report BOTH values and enumerate every downstream consumer

IRRECOVERABLE  the intended computation cannot be reconstructed from what is on disk.
               For L1/L2 specifically this requires the EXHAUSTIVE search to return
               ZERO candidates within tolerance -- a failure of two hand-built
               reconstructions is NOT sufficient and does not license this label.
```

**IRRECOVERABLE is a positive finding, not a shrug**, and it is only earned by the exhaustive
arm completing. If the search returns zero matches, the finding reports the **closest achievable
value** and the **full distribution over all 20,349 sets**, so a reader can see how far the
literal sits from anything this repository can produce.

**Registered in advance as the most likely outcome for L1/L2 and the reason it matters:** if the
20,349-set minimum distance to 0.759 is large, then 0.759 is not merely unverified — it is
**unreachable** by any combination of this repository's own features containing the ten it names,
which is a much stronger statement and the one worth publishing.

---

## 6. Directions locked before the run

| # | prediction | rationale |
|:-:|:--|:--|
| D1 | L3, L4, L5, L6, L7, L9 all **CONFIRM** | each has a script and a JSON carrying the value; a transcription error is possible but unlikely |
| D2 | L8 **CONFIRMS** | its own consuming script independently recomputes the same quantity in the same run |
| D3 | **L1/L2 return zero exhaustive matches** | H-NEW-2790 already showed both hand-reconstructions land ~0.80 while the literal is 0.759, and adding features to a Ridge at n=114 moves R² by hundredths, not by 0.04 |
| D4 | the **minimum** over all 20,349 sets still exceeds 0.759 | every 15-column Ridge tested so far sits above it |

**If D4 fails — if some set reaches 0.759 — that is a recovery and it will be reported as one**,
with the recovered feature set named, its RF checked against 0.817, and its importance vector
checked against the published ten. An audit that can only find fault is not an audit.

---

## 7. Frozen inputs (SHA-256, runtime-verified; mismatch ⇒ `SystemExit`)

| path (repo-relative) | SHA-256 |
|:--|:--|
| `quran-text/quran-no-tashkeel.json` | `253f72f32f1dd4f6288c24be1b3b81b2e32c67aedd59aecb6e4a057dae35918a` |
| `data/revelation-order.csv` | `74f52ec1518abf8ecbf67671ee1cdd8e4cfc553fc8c5ead8274cc7dae8916fb7` |
| `data/morphology/quranic-corpus-morphology-0.4.txt` | `a1d12923815341face765083805d2148ed2d9f5cc3f7d6665219d887675d8c46` |
| `findings/phase-b-hypotheses/csv/h-new-123.json` | `33bbeec06c1187b1a96448ecf87720a4915a49a827cf110685d4d277aa449f46` |
| `findings/phase-b-hypotheses/csv/h-new-125.json` | `8b2f7f1cf217562dd34be75519c80d29ceaebcc40b2b0c6fbe95bebb5d0442e1` |
| `findings/phase-b-hypotheses/csv/h-new-168-per-surah-dispersion.csv` | `7778d07f620d68b3a3fefbf5903c0e9e30665e25b58fe1f766d7f08cf6a07594` |
| `findings/phase-b-hypotheses/csv/h-new-182-surah-vectors.csv` | `30571ef0ee37f32881033ca22fcb368cffbaaf986d040491ed4396b2cb2b8acc` |
| `findings/phase-b-hypotheses/csv/h-new-187-per-surah.csv` | `7eee6ba49222e3fcd989ca2521114503fd5dcb3f907de6f1d343950970ed32ec` |
| `findings/phase-b-hypotheses/csv/h-new-183.json` | `246af4b198c2c7d5d4e2edf86d5d1924c37a35f5d4e6a5292b0e12291787a16f` |
| `findings/phase-b-hypotheses/csv/h-new-233.json` | `28715441baab9bef58735acb8fa7b63bd58686844fed25ee0f162ccfe67236a0` |
| `findings/phase-b-hypotheses/csv/h-new-88.json` | `3c3933a84e1a8b1d646ffd04e92b631514dd51a24d5826cebfaa53b0c440ae4b` |
| `findings/phase-b-hypotheses/csv/h-new-165-2.json` | `57de33891f8fc6528ec7ad9a26e898cd0eb1d77951245b6554fc87310e1b4657` |
| `findings/phase-b-hypotheses/csv/h-new-1395.json` | `6220fb2bcc9aa5bb02ea1d06fa82245e11945790fd6e4e6216ad29e142c542d7` |
| `findings/phase-b-hypotheses/csv/h-new-1710.json` | `78443356452b34fd0251ab4b8ea24df21a9a96664b22b2a13613ac987b313e60` |
| `surahs/Q028-al-qasas/csv/Q028-F-06.json` | `11bfae66abecb608d10576bfc2b9eefd2d259d290909f28d99d09fb900af0368` |
| `scripts/h_new_183_chronology_predictor.py` | `a30666c03c8bbdc0fa618099497ebe6962306cf7c712d5abf1b7adbbd025db2b` |
| `scripts/h_new_233_ensemble_predictor.py` | `ad69720a10159c43094336fab9890671743b545fbcfef5c53db1bbcb3478edd7` |

---

## 8. Run hygiene — the write-once rule this audit is paired with

This runner is the first written under the corrected rule (`UNIT-DRIFT-DEFECT.md` §7, which
H-NEW-2790's own defect produced):

> **A run script must never overwrite a file inside its own run directory.**

Accordingly: **`results.json` is written exactly once, at completion.** Progress checkpoints — and
a 20,349-cell exhaustive search needs them — go to `progress/NNNNNN.json` files **outside** the run
directory, each written once and never rewritten. **This is a locked property of the runner and
is verified by inspection in the finding**, because a rule whose first application violates it is
not a rule.

---

## 9. Garden of forking paths

- **Known at lock time:** the nine literals, their consumption sites, and the script/JSON
  existence table of §2 — all filesystem facts. The published importance vector and its 0.980
  sum. H-NEW-2790's two failed reconstructions (0.8026, 0.8041), which is *why* the exhaustive
  arm was designed.
- **Not computed at lock time:** every re-derived value, every one of the 20,349 Ridge R², every
  RF importance vector, and every classification.
- **The search space was fixed before it was run** — 31 columns, ten fixed, C(21,5) — and it is
  exhaustive over that space, so there is no stopping rule to abuse.
- **IRRECOVERABLE was defined so it cannot be reached lazily**: only the completed exhaustive arm
  earns it, which is the clause that stops "I could not reconstruct it" from becoming a verdict.

---

## 10. Honest limits, stated in advance

1. **The pool is what this repository can build, not what H-NEW-192 could have used.** If it used
   a feature that exists in no frozen artifact, the search cannot find it, and IRRECOVERABLE
   would then be correct for a reason the search cannot distinguish from the others. **The
   finding must state this rather than imply the literal is refuted.**
2. **Ridge LOOCV is deterministic; RF is not.** RF-based conclusions carry the library-version
   caveat, and any RF claim is reported with the tolerance it was judged at.
3. **A confirmed literal is a confirmed *transcription*, not a validated claim.** L3–L9 confirming
   says the constant matches its source artifact. It says nothing about whether the source
   computation was correct, and the finding will not let those be conflated.
4. **L8's rules-tuple is inherited, not re-derived.** The Mūsā count depends on the lemma
   convention and on the basmala rule; both are taken from `Q028-F-06`'s declaration and are not
   independently adjudicated here.

---

*Locked 2026-08-07 by Waiel Al-Shujaa, before any derived value was computed. A constant that no
code produces is not a result; it is a rumour with a decimal point.
Bismillāhi al-Raḥmāni al-Raḥīm.*
