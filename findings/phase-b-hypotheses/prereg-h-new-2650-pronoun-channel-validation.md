---
id: H-NEW-2650
title: Validation and correction of the attached-object-pronoun channel
date_locked: 2026-08-07
author: Waiel Al-Shujaa
phase: B+
type: INSTRUMENT VALIDATION — adversarial, against my own parent findings
status: LOCKED before any by-form error rate or form-pair result was computed
seed_primary: 20260509
seed_replication: 20260519
bonferroni_k: 5
alpha_corrected: 0.01
parent_findings: H-NEW-2540 (§2b), H-NEW-2600 (§5)
frozen_input_sha256: a1d12923815341face765083805d2148ed2d9f5cc3f7d6665219d887675d8c46
---

# PRE-REGISTRATION — H-NEW-2650

## Hardening the attached-object-pronoun channel

**This document is locked before computation. Its SHA-256 is embedded in
`findings/phase-b-hypotheses/scripts/h-new-2650.py` and verified at runtime with `SystemExit`
on mismatch.**

---

## 0. Why this test exists, and the standard it is held to

[[h-new-2540-form-v-valency|H-NEW-2540]] §7.2 documents **confirmed** parser contamination: the
EQTB treebank's syntax was initially produced by a BiLSTM parser whose inputs included
morphological-feature embeddings, and EQTB carries `verb_form` among them. Consequently **both
H-NEW-2540 and H-NEW-2600 now rest on the EQTB-free attached-object-pronoun channel**
(2540 §2b, 2600 §5) rather than on the dependency edges.

That channel has never been validated. **If it is flawed, two findings collapse.** This
pre-registration is written adversarially against my own prior work. A result that weakens
H-NEW-2540 and H-NEW-2600 is the correct outcome if the channel is broken, and it will be
published as such.

**A robustness property must be computed, never asserted.** H-NEW-2560 H5 was demoted to
CIRCULARITY-DOMINATED tonight for exactly that failure. Every claim below is computed.

### 0.1 A reproducibility failure found before locking, reported here

**The implementation under test does not exist on disk.** `findings/phase-b-hypotheses/scripts/h-new-2540.py`
and `h-new-2600.py` contain **no `PRON` code whatsoever**; no run directory under
`findings/phase-b-hypotheses/runs/h-new-2540/` or `.../h-new-2600/` contains it; a repository-wide
search for the channel's implementation returns nothing. The numbers published in 2540 §2b and
2600 §5 were produced by code that was never saved.

**Consequence:** this pre-registration cannot audit the original code. It specifies the
heuristic from its prose definition in 2540 §2b — *"a verb carries one iff a `PRON` segment
follows it inside the same orthographic word and its person/gender/number differs from the
verb's own subject agreement"* — reimplements that as `RULE-OLD`, and reimplements a corrected
version as `RULE-NEW`. Any discrepancy between `RULE-OLD` as reconstructed here and the lost
original is itself unresolvable, and is recorded as a limitation.

---

## 1. Frozen inputs

| Input | SHA-256 |
|:--|:--|
| `data/morphology/quranic-corpus-morphology-0.4.txt` | `a1d12923815341face765083805d2148ed2d9f5cc3f7d6665219d887675d8c46` |
| `data/revelation-order.csv` | `74f52ec1518abf8ecbf67671ee1cdd8e4cfc553fc8c5ead8274cc7dae8916fb7` |
| `quran-text/quran-no-tashkeel.json` | `253f72f32f1dd4f6288c24be1b3b81b2e32c67aedd59aecb6e4a057dae35918a` |

The QAC hash is **byte-identical to the one recorded in the parent runs' manifests**, so results
are directly comparable to 2540/2600. Verified at runtime; abort on mismatch. **No EQTB file is
read by this test at any point** — that is the entire purpose of the channel.

---

## 2. Instrument characterisation performed BEFORE this lock

Disclosed in full (garden-of-forking-paths, §9). All of it is QAC segmentation convention, not
hypothesis-relevant outcome:

- 128,219 located segments; 19,356 `V`; 24,685 `PRON`.
- Verb form markers `|(II)|`…`|(XII)|`; **Form I is unmarked**. Counts: I 12,347, IV 3,487,
  II 1,300, VIII 963, V 414, X 369, III 334, VI 77, VII 51, XII 9, IX 5. `|PASS` on 1,140 verbs.
- **Every one of the 19,356 verb feature strings contains exactly one agreement token**
  matching `[123][MF]?[SDP]` under word-boundary guards. (Failure mode 2 — "last match may not
  be the subject agreement" — is therefore empirically vacuous: last == only.)
- **QAC tags subject pronouns as `PRON` as well.** Q 2:152 `fa-udhkurūnī` segments as
  V(`2MP`) + `PRON:2MP` (wāw al-jamāʿa, the SUBJECT) + `PRON:1S` (`-nī`, the OBJECT).
- **`nūn al-wiqāya` is folded into the 1S object segment** (`niY`, `n~iY`, `ni`, `niYa`); it is
  never a separate segment. (Failure mode 1.)
- **The energetic nūn is a SEPARATE segment tagged `EMPH`**, not part of the verb: `EMPH`
  immediately follows a verb 243 times (`n~a`, `n~i`, `ni`, `A`), and `REL` 4 times.
  **101 object clitics are separated from their verb by such a segment.** Any implementation
  requiring adjacency loses them. (Failure mode 3.)
- **0 `STEM`-type `PRON` segments follow a verb inside a word**; all 12,496 post-verb `PRON`
  are `SUFFIX` clitics, across 107 distinct (surface-form, PGN) pairs.

---

## 3. RULE-OLD — the heuristic under test, reconstructed

A verb token carries an attached object pronoun iff **any** `PRON` segment occurring later in
the same orthographic word has a `PRON:` PGN value **different** from the verb's own agreement
token. (The "any … different" reading is taken from the parent findings' own threat-flag table,
which reports counts under "any post-verb PRON".)

## 4. RULE-NEW — the corrected heuristic, locked here

Every post-verb `SUFFIX`-type `PRON` segment in the same orthographic word is classified as
**SUBJECT-CLITIC** or **OBJECT-CLITIC** by the following ordered, closed decision list. `f` is
the segment's surface form with diacritic/pausal marks stripped and a leading `~` removed; `p`
is its `PRON:` PGN value; `s` is its 0-based index among post-verb `SUFFIX PRON` segments of
that verb; `g` is the verb's agreement token; `a` is the verb's aspect (`PERF`/`IMPF`/`IMPV`).
Non-`PRON` segments (`EMPH`, `REL`) are **skipped, not treated as terminators**.

1. `f` begins with `h` or `k` → **OBJECT**. *(No Arabic subject clitic has these shapes.)*
2. `f` begins with `t`, `w`, `y`, or `u` → **SUBJECT**. *(tāʾ al-fāʿil, wāw al-jamāʿa,
   yāʾ al-mukhāṭaba, and one `'uw` wāw variant.)*
3. `p == 1S` → **OBJECT**. *(What remains at this step is the `-nī` / `-ī` family; the 1S
   subject clitic `tu` was removed at step 2.)*
4. `p == 1P` → **SUBJECT** iff `s == 0` **and** `g == 1P` **and** `a == PERF`; otherwise
   **OBJECT**. *(Only the perfect suffixes a 1P subject; a `-nā` on any other verb is the
   object. Empirically: 1,262 subject cases, all `PERF`; **zero** `IMPF`/`IMPV` counterexamples.)*
5. Otherwise → **SUBJECT**. *(nūn al-niswa, dual nūn and alif, yāʾ al-mukhāṭaba.)*

A verb carries an attached object pronoun iff **at least one** of its post-verb `SUFFIX PRON`
segments is classified **OBJECT**.

**Runtime assertion (abort on failure):** every one of the 107 (form, PGN) pairs must be
classified by exactly one rule, and the union of OBJECT and SUBJECT classifications must equal
all 12,496 post-verb `SUFFIX PRON` tokens. Coverage must be 100%.

### 4.1 Failure mode 5 — non-object clitics — and the limit RULE-NEW does not clear

RULE-NEW identifies **enclitic pronouns that are not the verb's subject**. In Qurʾānic Arabic
such a clitic on a verb is overwhelmingly a direct object, but the class is not exclusively
direct objects: it also admits second objects of ditransitives, and clitics on verbs governing
a *bi-* or other complement. **RULE-NEW does not and cannot separate these from first direct
objects without syntactic annotation** — and syntactic annotation is precisely what this
channel exists to avoid. This is a permanent, structural limit of the channel, it applies
equally to RULE-OLD, and it is why the blinded human validation of §7 is required before any
precision claim is made. **No precision figure will be asserted from computation alone.**

---

## 5. Registered inferences — directions inherited, NOT re-locked

The five form pairs and their locked signs are inherited verbatim from the parent
pre-registrations; this test may not re-lock them. Statistic and eligibility are inherited from
H-NEW-2540/2600: within-root paired comparison, **≥2 tokens per form per root**, explicit
`PASS` verbs excluded, two-sided exact sign test over roots.

| # | pair | locked sign | parent-reported QAC-only gap |
|:-:|:--|:--:|--:|
| 1 | II → V | **+** | +0.215 (p = 7.6×10⁻⁵) |
| 2 | I → VIII | **+** | +0.212 (p = 1.4×10⁻⁶) |
| 3 | I → II | **−** | −0.179 (p = 3.2×10⁻⁴) |
| 4 | I → IV | **−** | −0.054 (p = 1.9×10⁻⁵) |
| 5 | III → VI | **+** | +0.277 (III 13/47; **VI 0/33**) |

**Bonferroni k = 5, α_corrected = 0.05/5 = 0.01.** The stricter parent gate (0.0005, H-NEW-2600
§0) is additionally reported for every pair. Each pair is run under **RULE-OLD and RULE-NEW on
identical token sets**, so the two are directly differenced.

---

## 6. The differential-error analysis — the crux

For each verb form F ∈ {I, II, III, IV, V, VI, VII, VIII}, computed over all non-`PASS` verbs of
that form having ≥1 post-verb `SUFFIX PRON`:

- `N_old(F)` — verbs RULE-OLD calls object-bearing.
- `N_new(F)` — verbs RULE-NEW calls object-bearing.
- **`FN(F)`** = verbs RULE-NEW calls object-bearing that RULE-OLD missed, **as a fraction of
  `N_new(F)`** — the miss rate.
- **`FP(F)`** = verbs RULE-OLD calls object-bearing that RULE-NEW calls subject-only, **as a
  fraction of `N_old(F)`** — the false-hit rate.

Both are reported per form, with raw numerators and denominators, for RULE-OLD assessed against
RULE-NEW as reference. **RULE-NEW is a corrected rule, not ground truth**; §7's blinded sample
is what can test RULE-NEW itself, and it is deliberately left unscored here.

### 6.1 Locked verdict rule

| Condition | Verdict |
|:--|:--|
| All 5 pairs keep their locked sign under RULE-NEW **and** every pair significant at α = 0.01 under RULE-OLD remains significant at α = 0.01 under RULE-NEW | **CHANNEL SOUND** |
| Signs and significance all hold, but `FN(F)` differs by **> 10 percentage points** between the two forms of any pair | **CHANNEL DEGRADED** — direction usable, magnitudes not |
| **Any** locked sign flips under RULE-NEW, **or** any pair significant at α = 0.01 under RULE-OLD falls below it under RULE-NEW | **CHANNEL COMPROMISED** — 2540 §2b and 2600 §5 must be amended and both parent findings downgraded |

A CHANNEL COMPROMISED verdict **requires** me to state plainly that H-NEW-2540 and H-NEW-2600
lose their load-bearing evidence. I commit to that here, before seeing the result.

### 6.2 The Form VI zero claim

H-NEW-2540 §2b asserts *"No Form VI token of any paired root carries an object pronoun — zero
out of 33."* The threat flag on both parents notes Form VI discards **100%** of its post-verb
`PRON` under RULE-OLD. **If RULE-NEW assigns any object clitic to any Form VI verb, that
sentence is false and must be retracted.** Registered as a separate binary outcome.

---

## 7. Blinded manual validation sample

Stratified by **verb form × RULE-NEW verdict (object-detected / not-detected)**, **≤10 rows per
cell**, sampled with seed 20260509 (replication 20260519). Forms I–VIII, both cells → up to 160
rows. Columns exactly as `runs/h-new-2540/.../validation-sample.tsv`:

`sample_id`, `verb_location`, `verb_surface`, `verse_text`, then **blank** review columns
`review_has_attached_object_pronoun`, `review_clitic_span`, `review_is_direct_object`,
`review_notes`.

The sample file carries **no form label, no rule verdict, and no clitic annotation**. A separate
`validation-key.json` holds the mapping. **The review columns are left blank — I will not fill
them in.** Until qualified reviewers return them, no precision or recall figure for RULE-NEW is
claimed anywhere.

---

## 8. Outputs and run discipline

Immutable run directory `findings/phase-b-hypotheses/runs/h-new-2650/<UTC-timestamp>/`
containing `manifest.json`, `result.json`, `validation-sample.tsv`, `validation-key.json`.

**No run directory is ever deleted**, including superseded or uncommitted ones (standing
correction; H-NEW-2540 §8.1 records a prior breach of exactly this clause by me). If a manifest
records a non-portable local path, the fix is to re-run into an **additional** directory and
retain both, recording why.

Replication: the complete analysis is re-executed at seed 20260519; the sample differs, every
rate and p-value must be identical (the pair statistics contain no randomness).

---

## 9. Garden-of-forking-paths log (written before the run)

Computed before this lock, all of it segmentation convention:

- Tag frequencies; verb form-marker counts; `PASS` count.
- Agreement-token multiplicity per verb feature string (uniformly 1).
- The complete inventory of 107 post-verb (surface-form, PGN) `SUFFIX PRON` pairs with counts,
  grouped by initial letter; `STEM`-`PRON`-after-verb count (0); `EMPH`/`REL` interposition
  counts (243 / 4; 101 clitics affected).
- Resolution of the two ambiguous cells: n-initial `PRON:1P` (1,262 subject / 230 object) and
  the single A-initial `PRON:1P` token at Q 12:11.
- Aggregate counts of post-verb clitics whose PGN equals the verb agreement but whose surface
  form is an object clitic: **305** at one-clitic verbs and **31** at multi-clitic verbs, before
  correcting for the 2FS `yāʾ al-mukhāṭaba` misclassification that this exploration exposed and
  that RULE-NEW step 2 fixes.

**Not computed before this lock:** any per-form false-negative or false-positive rate; any
form-pair object-pronoun rate, gap, sign count, or p-value under either rule; any Form VI object
count. Those are the outcomes and they are locked out.

---

*Locked 2026-08-07 by Waiel Al-Shujaa. Bismillāhi al-Raḥmāni al-Raḥīm.*
