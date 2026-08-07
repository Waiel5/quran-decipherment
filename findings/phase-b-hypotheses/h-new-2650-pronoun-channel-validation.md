---
id: H-NEW-2650
title: Validation and correction of the attached-object-pronoun channel
date: 2026-08-07
author: Waiel Al-Shujaa
status: "CHANNEL DEGRADED by the locked rule — triggered only by III→VI on an n=1 denominator. All five locked signs HELD; no arm lost significance; every correction ENLARGES the parent effects."
prereg: prereg-h-new-2650-pronoun-channel-validation.md
prereg_sha256: 4d7dbc76aa56e551c4dc38fcb6132c63e39884644344feb0e683c179481edacf
run: runs/h-new-2650/20260807T010445Z/
run_replication: runs/h-new-2650/20260807T010615Z/
seed: 20260509
validates: H-NEW-2540 §2b, H-NEW-2600 §5
eqtb_used: false
---

# H-NEW-2650 — The parser-free channel, broken open and rebuilt

**Verdict: CHANNEL DEGRADED** under the pre-registered decision rule (§6.1 of the pre-reg).
The rule fired on one arm — III→VI — where the false-negative rate difference is 0.109 vs
**1.000 on a denominator of one token**. Reported as locked, without override.

**The substantive result is the opposite of the fear that prompted this test.** The original
rule's error was **purely a miss error**: its false-hit rate is **0.0000 for every one of the
eight verb forms**. It never over-counted an object. Correcting the misses therefore *enlarges*
every claimed gap:

| pair | locked | gap RULE-OLD | **gap RULE-NEW** | p RULE-OLD | **p RULE-NEW** | sign |
|:--|:--:|--:|--:|--:|--:|:--|
| II → V | + | +0.2146 | **+0.2500** | 7.63×10⁻⁵ | **4.01×10⁻⁵** | HELD |
| I → VIII | + | +0.2120 | **+0.2309** | 1.40×10⁻⁶ | **7.66×10⁻⁷** | HELD |
| I → II | **−** | −0.1791 | **−0.1888** | 3.24×10⁻⁴ | 2.10×10⁻³ | HELD |
| I → IV | **−** | −0.0544 | **−0.0633** | 1.92×10⁻⁵ | **1.21×10⁻⁶** | HELD |
| III → VI | + | +0.0000 *(sign undefined)* | +0.0556 | 1.00 | 1.00 | HELD, no power |

The **LIVE THREAT FLAG** standing on H-NEW-2540 §2b and H-NEW-2600 §5 asked for the discards to
be decomposed into (a) legitimate subject markers and (b) genuine-object false negatives, and
warned that a form-correlated (b) would be fatal. **(b) is computed below. It is 0%–9% of
discards across forms, and it runs in the direction that makes the effects larger, not
smaller.** The flag can be resolved; the parent findings are not downgraded by this test.

---

## 1. A reproducibility failure, found before anything was computed

**The implementation under test did not exist on disk.** `scripts/h-new-2540.py` and
`scripts/h-new-2600.py` contain no `PRON` code at all; no run directory under
`runs/h-new-2540/` or `runs/h-new-2600/` holds it; a repository-wide search returns nothing.
The figures published in 2540 §2b and 2600 §5 came from code that was never saved. The
load-bearing evidence for two findings was, until now, unreproducible.

**This is substantially mitigated by what follows.** The heuristic was reimplemented from its
prose definition as `RULE-OLD`, and it reproduces **every published parent number exactly**:

| quantity | parent published | RULE-OLD here |
|:--|--:|--:|
| II→V sign test | 7.6×10⁻⁵ | **7.629×10⁻⁵** (18/1/4) |
| I→VIII sign test | 1.4×10⁻⁶ | **1.401×10⁻⁶** (30/3/6) |
| I→II sign test | 3.2×10⁻⁴ | **3.241×10⁻⁴** (6/27/4) |
| I→IV sign test | 1.9×10⁻⁵ | **1.917×10⁻⁵** (13/46/21) |
| II→V rates | 107/347, 24/256 | **107/347, 24/256** |
| III→VI rates (≥1 token) | 13/47, 0/33 | **13/47, 0/33** |
| threat-flag discard table | 8 rows | **all 8 rows reproduce exactly** |

The lost original is therefore recovered behaviourally, and the audit below is valid. The
script is now committed, so this cannot recur.

---

## 2. The five failure modes

### 2.1 nūn al-wiqāya — BENIGN, zero errors

QAC folds the protective nūn **into the 1S object segment** (`niY`, `n~iY`, `ni`, `niYa`); it is
never emitted separately. No miss, no false hit. Note that `ni`/`n~i` also occur as the
*energetic* nūn — QAC distinguishes them by TAG (`PRON` vs `EMPH`), so the two never collide.

### 2.2 Subject-agreement extraction — BENIGN, zero errors

The concern was that taking the **last** `[123][MF]?[SDP]` match might capture something other
than subject agreement. **All 19,356 verb feature strings contain exactly one such token.**
Last == only. The regex could not have gone wrong. (Verified with word-boundary guards; the
script aborts if any verb ever shows multiplicity ≠ 1.)

### 2.3 Duals, energetics, imperatives — ONE REAL LATENT BUG, not triggered

**The energetic nūn is a separate segment tagged `EMPH`, not part of the verb stem.** `EMPH`
immediately follows a verb **243** times, `REL` 4 times, and **101 object clitics are separated
from their verb by such a segment** (e.g. Q 11:46 `fa-lā tasʾalni`). Any implementation that
required the clitic to be *adjacent* to the verb, or that terminated its scan at the first
non-`PRON` segment, would silently lose all 101.

RULE-OLD as specified in 2540 §2b scans *any* `PRON` later in the word, so it escaped this.
**The bug was latent, not active.** RULE-NEW now skips `EMPH`/`REL` explicitly rather than by
luck. Duals and imperatives are handled by the closed lexicon (§3) — dual subject `-ā`/`-āni`
and object `-humā`/`-kumā` are distinct surface shapes.

### 2.4 Homographic clitics — THE REAL BUG

This was the item flagged as most important, and it is where the rule actually failed.

QAC tags **subject** pronouns as `PRON` as well: Q 2:152 `fa-udhkurūnī` = V(`2MP`) +
`PRON:2MP` (wāw al-jamāʿa, the subject) + `PRON:1S` (`-nī`, the object). Discarding a `PRON`
whose PGN equals the verb's agreement is therefore *usually* correct — it removes the subject
clitic. **But a genuine object sharing the subject's PGN is discarded too.** `khalaqa-hu`
(V 3MS + `-hu` 3MS) is an object, and RULE-OLD threw it away.

**305 genuine object clitics were discarded this way across Forms I–VIII.** The exploration also
exposed a trap in the naive fix: 22 tokens of `PRON:2FS` with surface `Y` are the *yāʾ
al-mukhāṭaba* (a subject), not the 1S object `-ī`, so an initial-letter test alone
mis-classifies them. RULE-NEW resolves clitics by **(surface shape × PGN × slot × verb
agreement × aspect)**, not by PGN comparison.

### 2.5 Non-object clitics — STRUCTURAL, UNRESOLVED, AND UNRESOLVABLE HERE

RULE-NEW identifies enclitic pronouns that are **not the verb's subject**. On a Qurʾānic verb
such a clitic is overwhelmingly a direct object, but the class also admits second objects of
ditransitives and clitics on verbs governing an oblique complement. **Separating those requires
syntactic annotation — which is exactly what this channel exists to avoid.** This limit applies
identically to RULE-OLD and RULE-NEW, so it does not affect the *comparison*, but it caps the
channel's absolute precision. Only the blinded human review of §6 can measure it. **No precision
figure is asserted anywhere in this file.**

---

## 3. RULE-NEW — the corrected classifier

Ordered, closed decision list over every post-verb `SUFFIX`-type `PRON` (pre-reg §4). `f` =
surface form stripped to bare letters, `p` = PGN, `s` = slot index, `g` = verb agreement,
`a` = aspect:

1. `f` starts `h` or `k` → **OBJECT** — no Arabic subject clitic has these shapes.
2. `f` starts `t`, `w`, `y`, `u` → **SUBJECT** — tāʾ al-fāʿil, wāw al-jamāʿa, yāʾ al-mukhāṭaba.
3. `p = 1S` → **OBJECT** — the `-nī`/`-ī` family; the 1S subject `tu` already left at step 2.
4. `p = 1P` → **SUBJECT** iff `s = 0` **and** `g = 1P` **and** `a = PERF`; else **OBJECT**.
5. otherwise → **SUBJECT** — nūn al-niswa, dual nūn and alif.

Step 4's condition was derived from the corpus and is exact: **1,262 subject cases, every one
`PERF`; zero `IMPF`/`IMPV` counterexamples**; 230 object cases.

**Coverage is asserted at runtime and is 100%**: all 12,496 post-verb `SUFFIX PRON` tokens
across 107 distinct (surface-form, PGN) pairs are classified by exactly one rule. The script
aborts otherwise. Zero `STEM`-type `PRON` follow a verb inside a word.

---

## 4. Differential error by form — the crux deliverable

RULE-OLD assessed against RULE-NEW as reference, over non-passive verbs with ≥1 post-verb
clitic. **FN** = objects RULE-OLD missed, as a share of RULE-NEW's objects. **FP** = RULE-OLD
objects that RULE-NEW calls subject-only, as a share of RULE-OLD's objects.

Every discard is split into **(a)** legitimate subject-marker discards and **(b)** genuine-object
false negatives. The classifier **never sees the verb's derivational form**, so it cannot
introduce a form-correlated bias by construction.

| form | verbs | w/ clitic | N_old | N_new | discards | **(a) subj** | **(b) obj** | **(b)/disc** | FN rate | **FP rate** |
|:--|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| I | 11,695 | 6,439 | 1,672 | 1,829 | 4,767 | 4,610 | 157 | 0.0329 | 0.0858 | **0.0000** |
| II | 1,160 | 724 | 381 | 412 | 343 | 312 | 31 | 0.0904 | **0.0752** | **0.0000** |
| III | 310 | 240 | 90 | 101 | 150 | 139 | 11 | 0.0733 | 0.1089 | **0.0000** |
| IV | 3,203 | 2,181 | 695 | 774 | 1,486 | 1,407 | 79 | 0.0532 | 0.1021 | **0.0000** |
| V | 404 | 226 | 30 | 35 | 196 | 191 | 5 | 0.0255 | 0.1429 | **0.0000** |
| VI | 77 | 55 | 0 | 1 | 55 | **54** | **1** | 0.0182 | 1.0000 *(1 of 1)* | — |
| VII | 51 | 22 | 0 | 0 | 22 | **22** | **0** | 0.0000 | — | — |
| VIII | 948 | 642 | 97 | 118 | 545 | 524 | 21 | 0.0385 | **0.1780** | **0.0000** |
| X | 354 | 255 | 45 | 51 | 210 | 204 | 6 | 0.0286 | 0.1176 | **0.0000** |

**Corpus total: (a) = 7,465 legitimate subject markers (96.0%), (b) = 311 genuine-object false
negatives (4.0%).** Forms IX (0 clitics) and XII (2, both subject) are omitted from the table.

**Three readings, in order of importance.**

1. **FP = 0.0000 everywhere.** RULE-OLD never manufactured an object. Whatever it reported was
   really there. The claimed effects cannot have been inflated by false hits — the failure mode
   that would have been fatal is absent.
2. **The threat flag's decomposition, answered.** Of the discards the flag tabulated,
   **(a) legitimate subject markers account for 91.0%–100%**, and **(b) genuine-object false
   negatives for 0.0%–9.0%**. The dramatic form-correlation in the *raw discard rate*
   (0.47 for Form II up to 1.00 for VI/VII) is almost entirely the (a) component — the wāw,
   tāʾ and nūn of subject agreement — exactly as the flag conjectured it might be.
3. **The residual (b)-correlation is real but small, and correcting it widens every gap.** FN
   rates across the four well-powered pairs: II→V Δ = 0.068, I→II Δ = 0.011, I→IV Δ = 0.016,
   **I→VIII Δ = 0.092 — close to the 0.10 threshold and flagged**. All four pooled gaps moved
   *further* in their locked direction under correction (§5), so the misses were, on net,
   suppressing the parents' effects rather than manufacturing them. A channel biased toward its
   own hypothesis would show the reverse.

   These global FN rates do **not** predict the gap change arithmetically — they are computed
   over every verb of a form, whereas each pair uses only its eligible paired roots. They are
   reported as the differential-error diagnostic the threat flag asked for; §5 is what settles
   the effect on the claims.

---

## 5. The five pairs, corrected

Within-root paired, ≥2 tokens per form per root, `PASS` excluded, two-sided exact sign test.
Bonferroni k = 5, α = 0.01. The parents' stricter 0.0005 gate is also shown.

| pair | locked | RULE-NEW rates | gap | roots +/−/= | p (2-sided) | α=0.01 | 0.0005 gate |
|:--|:--:|:--|--:|:--|--:|:--|:--|
| **II → V** | + | 122/347 = 0.3516 vs 26/256 = 0.1016 | **+0.2500** | 19/1/3 | **4.01×10⁻⁵** | PASS | PASS |
| **I → VIII** | + | 448/1329 = 0.3371 vs 77/725 = 0.1062 | **+0.2309** | 31/3/5 | **7.66×10⁻⁷** | PASS | PASS |
| **I → II** | **−** | 90/1215 = 0.0741 vs 143/544 = 0.2629 | **−0.1888** | 7/25/5 | 2.10×10⁻³ | PASS | **fails** |
| **I → IV** | **−** | 356/1758 = 0.2025 vs 527/1983 = 0.2658 | **−0.0633** | 12/50/18 | **1.21×10⁻⁶** | PASS | PASS |
| III → VI | + | 1/18 = 0.0556 vs 0/15 = 0.0000 | +0.0556 | 1/0/3 | 1.00 | no power | no power |

**All five locked signs HELD. No pair lost significance at the registered α.** The causative
reversal — the falsification control that gives the lattice its force — survives intact and with
larger magnitudes in both arms.

### 5.1 The one genuine weakening, reported plainly

**I→II's sign test moves the wrong way: 3.24×10⁻⁴ → 2.10×10⁻³.** One root crossed from
`II > I` to `I > II` and another tied, taking the discordant count from 6/27 to 7/25. It still
clears α = 0.01, but it **no longer clears the parents' stricter 0.0005 gate**. Its pooled gap
simultaneously *strengthened* (−0.1791 → −0.1888). Both facts are true; the arm is more robust
in magnitude and less robust in root-level unanimity, and 2600 §5's `3.2×10⁻⁴` for this arm
should be updated to `2.1×10⁻³`.

### 5.2 III→VI, and why the locked rule fired

At the ≥2-token threshold this arm has 4 roots and no power under either rule — as H-NEW-2600 §4
already reported. RULE-OLD gives 0/18 vs 0/15, a gap of exactly zero, so its *sign is undefined*
and the arm was never evidence for anything. RULE-NEW gives 1/18 vs 0/15.

The **CHANNEL DEGRADED** verdict is triggered entirely by this arm's FN-rate difference,
0.1089 (III) vs **1.0000 (VI, being 1 out of 1)**. That denominator is a single token. The rule
was locked before the run and I am not overriding it, but the honest reading is that the trigger
is a degenerate-denominator artifact on an arm with no power, not evidence of a biased channel.

---

## 6. The Form VI "zero out of 33" claim — SURVIVES as written

H-NEW-2540 §2b states: *"No Form VI token **of any paired root** carries an object pronoun —
zero out of 33."* Evaluated at that claim's own eligibility (≥1 token per form per root):

| | RULE-OLD | RULE-NEW |
|:--|:--|:--|
| III | 13/47 | 16/47 |
| **VI** | **0/33** | **0/33** |
| sign test (2-sided) | 0.0625 | **0.0156** |

**The claim holds, and the arm strengthens under correction.** It must not be retracted.

**But one qualification must be added.** Corpus-wide, Form VI is **not** object-free: of 77
non-passive Form VI verbs, **one carries an object clitic** — Q 68:49 `tadārakahu`
(`(68:49:3:1)`, root *d-r-k*), *"had not a favour from his Lord **reached him**"*. It falls
outside the paired set because root *d-r-k* has **no Form III tokens at all** (6 × Form IV,
3 × Form VI). So the sentence as written is true, but any stronger reading — "Form VI never
takes an object pronoun" — is false, and 2540 §2b should carry that footnote.

### 6.1 The 100% discard rate of Forms VI and VII is grammar, not artifact

All 55 Form VI and all 22 Form VII clitic-bearing verbs were inspected individually
(`runs/h-new-2650/20260807T011152Z/discard-decomposition.json`, full listing with verse text).

- **Form VII: 22 of 22 discards are subject markers. Zero objects.** Every verb is
  *inqalaba* / *inṭalaqa* / *infaḍḍa* / *inṣarafa* — the canonical mediopassive *muṭāwiʿ* of
  Form I, and canonically intransitive. The clitics are plural wāw, dual alif and perfect tāʾ.
- **Form VI: 54 of 55 are subject markers**, on *tasāʾalūna*, *tanāzaʿtum*, *tawāṣaw*,
  *taʿāwanū*, *tanājaytum* — reciprocals, which take a plural or dual subject affix by
  definition and have no object to take. The single exception is Q 68:49.

**The 1.000 discard rate is therefore a real property of the Arabic, not an artifact of the
rule.** Forms VI and VII are reciprocal and mediopassive; their verbs carry subject clitics and
essentially never object clitics. The rule did not manufacture the zero — the grammar did. This
was the most alarming cell in the threat-flag table and it is the one that most clearly clears.

---

## 7. Verdict on whether the channel can carry the parents

**It can, for the four well-powered arms, and this test strengthens rather than weakens them.**

- All five locked signs held; none flipped.
- No arm lost significance at the registered α.
- The false-hit rate is zero for every form — no claimed object was ever fabricated.
- Genuine-object false negatives are 0%–9% of discards, and correcting them **widens** every
  gap. The inflation mechanism the threat flag feared does not operate.
- The **LIVE THREAT FLAG** on 2540 §2b and 2600 §5 can be resolved. The numbers in those
  sections should be updated to the RULE-NEW values of §5 (all of which are stronger except
  I→II's sign test), the Form VI footnote of §6 added, and I→II's p corrected.

**What is not settled.** RULE-NEW is a corrected rule, **not ground truth**. It cannot separate
direct objects from second objects or oblique-governed clitics (§2.5). The blinded sample below
is what tests RULE-NEW itself, and until it is scored, the channel's absolute precision is
unmeasured. The parents' *comparative* claims do not depend on that precision — both forms in
each pair are measured by the identical instrument — but their *absolute* rates do.

## 8. Blinded validation sample

`runs/h-new-2650/20260807T010445Z/validation-sample.tsv` — **141 rows**, stratified by
verb form × RULE-NEW verdict, ≤10 per cell, seed 20260509. Cells: 10 each except
(VI, detected) = 1 and (VII, detected) = 0, which is all the corpus contains.

Columns: `sample_id`, `verb_location`, `verb_surface`, `verse_text`, then
`review_has_attached_object_pronoun`, `review_clitic_span`, `review_is_direct_object`,
`review_notes`. **The review columns are blank and I have not filled them in.** The file carries
no form label and no rule verdict; the mapping is in `validation-key.json`.

## 9. Provenance and run discipline

- Pre-reg SHA-256 `4d7dbc76aa56e551c4dc38fcb6132c63e39884644344feb0e683c179481edacf`,
  verified at runtime with `SystemExit` on mismatch.
- Frozen inputs verified at runtime. QAC `a1d12923…8c46` is **byte-identical to the hash in the
  parent runs' manifests**, so every comparison above is against the same corpus the parents used.
- **No EQTB file is opened by this script.** That is the point of the channel.
- Two run directories, **both retained**: `20260807T010445Z` (primary) and `20260807T010615Z`
  (determinism re-run). `result.json` and `validation-sample.tsv` are **byte-identical** across
  both (`df015fdb…de1c`, `c5bed95d…0bd3`). The pair statistics contain no randomness.
- **No run directory was deleted.** H-NEW-2540 §8.1 records a prior breach of this clause by me;
  it is not repeated here.

## 10. Honest limits

1. **The original code is gone.** RULE-OLD reproduces every published parent figure exactly,
   which is strong evidence the reconstruction is faithful — but it is evidence, not proof. A
   discrepancy between the lost original and RULE-OLD in some untested corner is unfalsifiable.
2. **RULE-NEW is not ground truth** (§2.5, §7). Its own error rate is unmeasured until the
   blinded sample is scored.
3. **The DEGRADED verdict rests on n = 1.** Locked and reported as such; a threshold rule on a
   single-token denominator is not informative, and a better-designed rule would have required a
   minimum denominator. That is a defect in my pre-registration, not in the channel.
4. **I→VIII's FN-rate gap is 0.092**, just inside the 0.10 threshold. Had the threshold been
   0.09 the verdict would name that arm too. The threshold was locked before the run, but it was
   arbitrary and the arm should be watched.
5. **Forms IX–XII are excluded** from the differential table (23 verbs total, none in a tested
   pair).
6. **This validates the channel, not the parents' interpretation.** Whether "attached object
   pronoun" is a good proxy for valency is a separate question that neither this test nor the
   parents' design addresses.

## 11. Files

- Pre-reg: `findings/phase-b-hypotheses/prereg-h-new-2650-pronoun-channel-validation.md`
- Script: `findings/phase-b-hypotheses/scripts/h-new-2650.py`
- Runs (both retained): `findings/phase-b-hypotheses/runs/h-new-2650/20260807T010445Z/`,
  `findings/phase-b-hypotheses/runs/h-new-2650/20260807T010615Z/`
- Parents: `h-new-2540-form-v-valency.md` §2b, `h-new-2600-mutawaa-lattice.md` §5

---

*H-NEW-2650 logged 2026-08-07 by Waiel Al-Shujaa. The rule only ever missed; it never invented.
Bismillāhi al-Raḥmāni al-Raḥīm.*
