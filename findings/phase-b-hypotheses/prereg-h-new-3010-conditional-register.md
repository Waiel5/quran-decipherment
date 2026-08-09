---
id: H-NEW-3010
title: Realis vs irrealis conditionals are register-coded — PRE-REGISTRATION
date: 2026-08-09
phase: B
status: LOCKED-BEFORE-COMPUTATION
author: Waiel Al-Shujaa
seed: 20260509
n_perm: 10000
frontier_item: F-3 (HANDOFF/FRONTIER-MAP-2026-08-07.md, lines 199-205)
parents: [cross-finding-028-formal, H-NEW-2530, H-NEW-2500]
---

# PRE-REGISTRATION — H-NEW-3010 — Are realis (`in`) and irrealis (`law` / `lawlā`) conditionals register-coded?

**This file is locked BEFORE any computation of the outcome statistic (the irrealis
share), before any group contrast, and before any null. Its SHA-256 is embedded as a
literal in `findings/phase-b-hypotheses/scripts/h-new-3010.py` and verified at runtime
with `SystemExit` on mismatch, per Protocol §1.2.**

**What was inspected before this lock, and why it is not the outcome.** Only
*structural* facts were read: which QAC lemmas carry `TAG == COND` and with what
frequency (the census in §2.1); which POS tags each candidate lemma also carries (the
disambiguation table in §2.2); that the genre TSV covers all 114 surahs with a
non-empty `sinai_genre`; the coarse register group *sizes and memberships* under the
two mappings (§3.3); and per-surah word/verse counts from QAC (§5.1). **No irrealis
share, no group contrast, and no null was computed.** Every one of these inspections is
logged in the garden-of-forking-paths section (§9) with the reason it was needed to
write a runnable pre-registration.

---

## 0. The hypothesis

From `HANDOFF/FRONTIER-MAP-2026-08-07.md` §F-3:

> **`in`** (open / realis condition) concentrates in **legal-Medinan**;
> **`law` / `lawlā`** (counterfactual / irrealis) concentrates in **polemic** and
> **eschatological warning**. This is the missing fourth column of cross-finding-028.

cross-finding-028-formal established that Quranic discourse register is coded at the
function-word grain, on two layers: verse-onset particles (`idh` / `lammā` / `qālū`)
and person-iltifāt. Its own §"Open follow-ups" item 2 names the legal↔eschatological
blur as the law's soft edge (legal recovered only 8/20 in leave-one-out). The
conditional-modality axis is a candidate **fourth column**: a particle-grain feature
that is, on linguistic grounds, expected to split precisely the pair the existing
feature set cannot.

**This pre-registration tests the register claim only.** It does **not** test, and no
result here may be read as testing, whether the conditional axis improves
cross-finding-028's classifier — that would require re-running H-NEW-2530's pipeline
with a new feature and is a separate pre-registration.

---

## 1. DIRECTIONS — LOCKED AND JUSTIFIED BEFORE ANY COMPUTATION

### 1.1 The three locked directions

Let **irrealis share** be, for any group `G` of surahs,

```
share(G) = ( Σ_{s∈G} n_irrealis(s) )  /  ( Σ_{s∈G} [ n_irrealis(s) + n_realis(s) ] )
```

counted over QAC conditional-particle **segments** only (§2). Then:

| id | statement | LOCKED SIGN |
|:--|:--|:--|
| **H1** | `share(POLEMIC ∪ ESCHATOLOGICAL) − share(LEGAL)` | **> 0** |
| **H2** | `share(LEGAL) − share(all surahs not LEGAL)` | **< 0** |
| **H3** | `share(POLEMIC ∪ ESCHATOLOGICAL) − share(all surahs not in that group)` | **> 0** |

All three are **one-sided**. H1 is the primary. H2 and H3 decompose the frontier-map
claim into its two separate clauses (`in` concentrates in legal; `law`/`lawlā`
concentrates in polemic + eschatological), each against the rest of the corpus, so that
a result driven entirely by one clause cannot be reported as if both held.

### 1.2 Why these directions, and not the reverse

The justification is **grammatical**, drawn from the standard description of the
particles, and is fixed here before any measurement.

**`in` (إِنْ) al-sharṭiyya is an OPEN condition.** Its protasis is presented as
*possible* — neither asserted nor denied. It is the ordinary particle of the
`sharṭ / jazāʾ` apparatus: *if case C obtains, ruling R applies*. Legal discourse is
constitutively made of contingent rulings over cases that may or may not occur, so the
open conditional is the form a case-based ruling naturally takes. This is why the
prediction runs `in` → legal.

**`law` (لَوْ) is ḥarf imtināʿ li-imtināʿ — a COUNTERFACTUAL.** Its protasis is
presupposed **false**, and the apodosis therefore asserts what *would* have followed
from something that did not happen. That presupposition has two natural discourse
homes, and both are named in the hypothesis:

- **Polemic by reductio.** Asserting a counterfactual whose apodosis is absurd refutes
  the protasis. The argument form requires the protasis to be false and requires the
  audience to grant that it is.
- **Eschatological warning.** The `law tarā` / `wa-law tarā idh…` construction
  ("if you could see when…") presupposes that the addressee does *not* see, which is
  exactly the rhetorical situation of a warning about the unseen.

**`lawlā` (لَوْلَا) al-imtināʿiyya ("were it not for X, Y would have…")** is the
negative counterfactual and shares `law`'s presupposition structure and its polemical
use.

**Therefore, if register is coded in the conditional apparatus at all, the coding must
run in this direction.** A reversed result — legal-Medinan carrying *more*
counterfactual than polemic and eschatological — would not be a weaker version of this
hypothesis; it would contradict the grammatical description the hypothesis rests on,
and is pre-committed to be published as a **pre-commit violation, labelled NULL, with
full prominence** (Protocol §1.8).

### 1.3 Classical anchor — stated at exactly the strength it can be supported

The frontier map names *"the sharṭ / jazāʾ apparatus in al-Zarkashī *al-Burhān*"* and
notes the PDF is on disk at
`data/literature/classical-tafsir/zarkashi-al-burhan-fi-ulum-al-quran.pdf`.

**The PDF is image-only.** `pdftotext -f 1 -l 5` on it returns exit code 0 and **zero
extractable characters**, so no passage in it has been read and no *nawʿ* number can be
cited. Per the anti-hallucination rule (Protocol §2.11): **no al-Zarkashī citation is
made in this pre-registration, and none may be made in the finding**, beyond the fact
that the work is the classical locus for the `sharṭ` apparatus and that its text is not
machine-readable here. **The locked direction rests on the grammatical description of
the particles in §1.2, not on a located classical passage.** This is a real limitation
and is carried into the finding's limits section verbatim.

---

## 2. THE INSTRUMENT (LOCKED)

### 2.1 Source and extraction

Single source: `data/morphology/quranic-corpus-morphology-0.4.txt` (QAC v0.4). A
**token** is one morphological segment line whose `TAG` column equals exactly `COND`.
There are **1,049** such segments. Location is parsed as `(surah:verse:word:segment)`.

### 2.2 The disambiguation — why QAC lemma is mandatory here

Raw substring counting would be catastrophically wrong on this hypothesis. The full
POS cross-tab of the candidate lemmas, computed from the file before this lock:

| lemma | COND | other tags carried by the same lemma |
|:--|--:|:--|
| `<in` (in) | **578** | NEG 114, CERT 5 |
| `law` | **185** | SUB 16 |
| `lawolaA^` (lawlā) | **35** | **EXH 40** |
| `man` | 184 | REL 650, INTG 37 |
| `maA` | 23 | REL 1476, NEG 705, PREV 162, INTG 95, SUB 83, SUP 21 |
| `>am~aA` | 11 | EXL 44 |
| `<i*aA` (idhā) | 1 | T 405, SUR 3 |
| `<im~aA` | 1 | EXL 22 |
| `<iyn`, `<il~am` | 1 each | — |

Two of these are decisive:

- **`in` is a negative particle 114 times** (`in` al-nāfiya, "not"). Substring counting
  would inflate the realis arm by ~20 %.
- **`lawlā` is exhortative (taḥḍīḍ, "why not…?") more often than it is conditional** —
  40 EXH against 35 COND. The taḥḍīḍ use carries **no counterfactual presupposition**
  and would directly corrupt the irrealis arm. QAC separates them; nothing else on disk
  does.

Restricting to `TAG == COND` is therefore not a convenience — it is the only route by
which this hypothesis is testable at all.

### 2.3 The particle sets — RULES-TUPLE AXIS 1 (LOCKED)

**Tuple T1 (primary) — the full conditional-particle pair.**

- irrealis = `{ law, lawolaA^ }`
- realis = `{ <in, <iyn, <il~am, <im~aA }`

`<iyn` is the orthographic variant of `in`; `<il~am` is `in` + `lam`; `<im~aA` is
`in` + `mā`. All three are open conditions built on `in`.

**Tuple T2 (second tuple) — the minimal pair only.**

- irrealis = `{ law }`
- realis = `{ <in }`

T2 drops `lawlā` entirely (because of the EXH/COND ambiguity documented in §2.2, even
though QAC resolves it) and drops the three rare `in`-compounds. It is the strictest
possible reading of the hypothesis: the bare `in` ↔ `law` minimal pair.

**Excluded from BOTH tuples, permanently and by rule:** `man`, `maA`, `>am~aA`,
`>ayon`, `Hayov2`, `mahomaA`, `>aY~`, `{l~a*iY`, `<i*aA`. These are *asmāʾ al-sharṭ*
(conditional nouns/relatives — "whoever", "whatever", "wherever") and the temporal
conditional. They are not marked for realis/irrealis modality, which is the entire
content of the hypothesis. Their exclusion is fixed here and may not be revisited.

### 2.4 Rules-tuple disclosure (Protocol §1.4)

- **Tashkeel level:** QAC's own Buckwalter lemma field, diacritised as QAC encodes it.
  The underlying text is Tanzil Uthmani v1.0.2 as bundled with QAC v0.4.
- **Token level:** QAC morphological **segment**, keyed by `LEM`, filtered to `TAG == COND`.
- **Counting unit:** conditional-particle **segments**. **The denominator is never a
  verse count, a word count, or any unit count** — see §4.1.
- **Basmala:** QAC carries the basmala as segments of `(1:1:*)` in Q 1 only. It contains
  no conditional particle, so it affects no numerator; it contributes 4 word positions
  to Q 1's word count, which is used only as a stratification variable.
- **Reading tradition:** Hafs-Kufan.
- **Script:** Mashriqi.

---

## 3. THE REGISTER LABELS (LOCKED)

### 3.1 Source

`findings/classical-sources/neuwirth-sinai-genre-labels.tsv` — Neuwirth (1981, 2010)
and Sinai (2017) genre labels, already read by 9 scripts in this repository. Verified
before this lock: **all 114 surahs are present and all 114 have a non-empty
`sinai_genre` field.** The `sinai_genre` column is the label used; `neuwirth_genre` is
not used (no fallback is ever needed).

### 3.2 The mapping problem, stated honestly

The labels are compounds — `legal-exhortative-polemical`, `polemical-legal`,
`oath-sworn-eschatological`, `scripture-reflective-polemical` — and **the compounds mix
the two classes the hypothesis contrasts**. Any coarse mapping is therefore a
researcher choice, and it is the single largest forking path in this design. It is
resolved by locking **two mechanical mappings** and running both as a rules-tuple axis.

### 3.3 The two mappings — RULES-TUPLE AXIS 2 (LOCKED)

Applied to the lower-cased `sinai_genre` string.

**Mapping M1 (primary) — LEGAL-PRECEDENCE CONTAINMENT.**

```
if "legal"      in label:                                  -> LEGAL
elif "eschatolog" in label or "polemic" in label:           -> IRR
else:                                                       -> OTHER
```

**Mapping M2 (second tuple) — FIRST-TOKEN DOMINANCE.**

```
t = label.split("-")[0]
if t == "legal":                                            -> LEGAL
elif t in {"polemical", "eschatological"}:                  -> IRR
else:                                                       -> OTHER
```

**Why M1 is primary, and why its tie-break is the conservative one.** M1 sends every
mixed compound — `polemical-legal` (Q 9), `legal-exhortative-polemical` — into
**LEGAL**, the group predicted to have the *lowest* irrealis share. If those surahs
genuinely carry polemical counterfactuals, M1 loads them onto the group that is
supposed to lack them, **shrinking the effect it is testing for**. A locked tie-break
that runs against the hypothesis is the correct one to make primary.

M2 reverses that tie-break for exactly those surahs, and additionally demotes compounds
whose first token is neither (`scripture-reflective-polemical` → OTHER). The two
mappings disagree on **21 surahs**, which is what makes this a real sensitivity axis
rather than a cosmetic one.

**Group memberships, fixed by the rules above (inspected before lock; these are label
facts, not outcome facts):**

| mapping | LEGAL | IRR | OTHER |
|:--|--:|--:|--:|
| **M1** | **17** — Q 2, 3, 4, 5, 8, 9, 24, 33, 47, 49, 58, 59, 60, 62, 65, 66, 98 | **36** — Q 6, 16, 25, 44, 50, 51, 52, 54, 56, 63, 67, 68, 69, 70, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 88, 89, 97, 99, 101, 104, 107, 109, 111 | 61 |
| **M2** | **13** — Q 2, 3, 4, 5, 8, 24, 33, 49, 58, 60, 62, 65, 66 | **25** — Q 9, 44, 47, 50, 54, 56, 63, 68, 69, 70, 75, 76, 78, 81, 82, 83, 84, 88, 98, 99, 101, 104, 107, 109, 111 | 76 |

**NARRATIVE is not in the contrast.** The hypothesis makes no directional prediction
for narrative/qaṣaṣ. It is reported descriptively in the finding and **may not be
promoted into any test post hoc.**

### 3.4 The four cells

`cells = { (M1,T1) [PRIMARY], (M1,T2), (M2,T1), (M2,T2) }`

---

## 4. THE NAMED CONFOUND: LENGTH

`AUDIT-H-NEW-206-LENGTH-CONFOUND.md` documents a finding demoted for letting length
leak into the very thing it predicted: `surah_length` was a clustering feature and the
clusters were then tested against a label (muqaṭṭaʿāt) that is 3.3× longer at the
median. Its transferable rule — *"if the thing you are predicting is already one of the
features you clustered on, the association you find is partly your own construction"* —
and `UNIT-DRIFT-DEFECT.md` §3 Screen B (groupings, not only orderings) govern this
design. The legal register lives in long surahs. Three separate protections are locked
below.

### 4.1 Protection 1 — the statistic has NO unit count in its denominator

`UNIT-DRIFT-DEFECT.md` §3 Screen A asks whether the headline statistic is a ratio with
a **unit count** in the denominator. **It is not.** The denominator of `share(G)` is
the number of *conditional-particle tokens* in `G`. A longer surah contributes more of
both numerator and denominator. This is the entire reason the irrealis **share** was
chosen over a per-verse or per-word conditional **density**, which would have been a
textbook instance of the defect.

**A per-verse or per-100-verse conditional density is forbidden as a primary statistic
in this test.** It may appear in the finding only as a descriptive figure, explicitly
labelled as unit-drift-exposed.

### 4.2 Protection 2 — MANDATORY pre-test length diagnostic, REPORTED whatever it shows

Before the primary test, and reported in the finding regardless of outcome:

1. For each mapping (M1, M2) and each group (LEGAL, IRR, OTHER): **median and mean of
   surah word count, verse count, and mean verse length** (words per verse), all from
   QAC.
2. **Spearman ρ between the binary LEGAL indicator and each of the three channels**,
   and likewise for the binary IRR indicator, over all 114 surahs. This is the
   §5-mandated ranking of candidate nuisance channels *measured on the data*.
3. **Spearman ρ between the per-surah irrealis share and each of the three channels**,
   over surahs with ≥ 3 conditional tokens under T1. This is the leak channel proper:
   it measures whether the *outcome* is length-correlated, which is what would let a
   length-correlated grouping manufacture the result.

**This is a report, not a gate.** The stratified nulls of §5 are primary **regardless
of what the diagnostic shows** — the design does not become length-controlled
conditionally on the diagnostic, because a diagnostic that gates the design is a
forking path. The unstratified null is computed and reported **for contrast only and is
never the gate**.

### 4.3 Protection 3 — length is held fixed twice, in two different places

- **In the null** (§5.2): the register label is permuted only *within* surah-length
  strata, on **all three** channels and at **two** bin widths — six nulls, and the test
  must clear the **worst** of them.
- **In the statistic** (§5.3): a second statistic, `D_V`, is computed inside fixed
  **host-verse-length quintiles**, which holds *verse* length fixed by construction —
  the other half of the named confound.

---

## 5. THE TEST

### 5.1 Length channels (LOCKED)

All derived from `data/morphology/quranic-corpus-morphology-0.4.txt` itself, so the
length variables and the outcome come from one file with no join risk:

- `word_count(s)` = number of distinct `(verse, word)` positions in surah `s`
  (corpus total 77,429).
- `verse_count(s)` = number of distinct verses in surah `s` (corpus total 6,236;
  verified equal to `data/hafs-verse-counts.tsv` for **all 114** surahs).
- `mean_verse_length(s)` = `word_count(s) / verse_count(s)`.

Channels: `C = { log(word_count), verse_count, mean_verse_length }`.
Bin widths: `B = { 5, 10 }`.
Strata: the 114 surahs are ranked on the channel (ties broken by ascending surah
number, deterministic) and cut at ranks `floor(i·114/B)` for `i = 1…B−1`.

**All three channels are used; none is selected.** `UNIT-DRIFT-DEFECT.md` §5 requires
ranking channels on the data and controlling on the strongest. Selecting the strongest
*after* measuring it is itself a degree of freedom, so this design removes the choice:
the test must clear **every** channel. That is strictly stronger than controlling on
the strongest, and it cannot be gamed by a mis-ranked table (the failure mode recorded
in `UNIT-DRIFT-DEFECT.md` §3's own warning box).

Both bin widths are reported and the **stricter (larger) p is taken**, per
`UNIT-DRIFT-DEFECT.md` §6.1 requirement 2. Requirement 3 of that section asks which
regime the claim is in: **this statistic is a group contrast, not a fitted model
containing the stratifying variable**, so stratified permutation is decisive for it
(§6.1's own qualification applies only to regressions containing the stratifier).

### 5.2 The null (LOCKED)

**Permutation. 10,000 permutations. Seed 20260509.** `random.Random(20260509)` is
re-instantiated for each null configuration, so every configuration is independently
reproducible from the stated seed.

The permuted quantity is the **surah-level register label vector**, shuffled **within
each length stratum**. Surah is the exchangeable unit because the register label is a
surah-scale label; permuting at verse or token level would be pseudo-replication.

**No parametric p-value is computed anywhere in this test.** Not χ², not a
proportion z-test, not Fisher's exact. `AUDIT-H-NEW-206-LENGTH-CONFOUND.md` §1
established that a χ² *statistic* with a permutation null is legitimate while a χ²
*p-value* is not; this design uses neither.

One-sided p, with the direction locked in §1.1:

```
positive direction (H1, H3):  p = (1 + #{ perm >= obs }) / (1 + n_perm)
negative direction (H2):      p = (1 + #{ perm <= obs }) / (1 + n_perm)
```

Floor = 1/10001 = 9.999 × 10⁻⁵.

### 5.3 The two statistics (LOCKED)

**`D_pooled(G_a, G_b) = share(G_a) − share(G_b)`** — the primary statistic, defined in
§1.1.

**`D_V(G_a, G_b)` — the host-verse-length-matched statistic.** Every conditional token
has a host verse; `L(t)` is that verse's QAC word count. Quintile boundaries on `L` are
computed **once**, from **all** conditional tokens of the tuple's particle set across
all 114 surahs, and are **held fixed across every permutation** (so the strata are not
re-derived under the null). Then

```
D_V = Σ_q  w_q · [ share_q(G_a) − share_q(G_b) ]
```

over quintiles `q` in which **both** groups have ≥ 1 token, with
`w_q = (n_q(G_a) + n_q(G_b)) / Σ_{q'} (n_{q'}(G_a) + n_{q'}(G_b))` renormalised over
the included quintiles. If **no** quintile contains tokens from both groups, `D_V` is
**undefined** and the test is treated as **failing** (conservative).

### 5.4 Per-test p-value (LOCKED)

For each of the 12 tests (3 hypotheses × 4 cells), 12 permutation p-values are
computed — 2 statistics × 3 channels × 2 bin widths — and

```
p_test = MAX over those 12
```

The maximum, not the minimum and not the primary: a claim that survives its weakest
control is established; a claim that survives only its most favourable one is not.

### 5.5 Power guard (LOCKED)

A test is **computable** only if, under its tuple, **each** of the two groups being
contrasted carries **≥ 20** conditional-particle tokens, **and** `D_V` is defined.
Otherwise the test is `NOT-POWERED` and **counts as failing**. The threshold 20 is
fixed here without having counted the per-group tokens.

---

## 6. DECISION RULE (LOCKED — the script's verdict function must match this LINE BY LINE)

```
k          = 12                      # 3 hypotheses x 4 cells
alpha_bon  = 0.05 / 12               # = 0.0041666666...
PRIMARY    = (H1, M1, T1)

for each test in the 12:
    computable = (tokens(G_a) >= 20) and (tokens(G_b) >= 20) and D_V is defined
    sign_ok    = sign(D_pooled) matches the direction locked in Sec 1.1
    p_test     = max over the 12 (statistic x channel x bins) one-sided permutation p
    clears     = computable and sign_ok and (p_test < alpha_bon)

n_clear = count of tests with clears == True

VERDICT:
  if PRIMARY is computable and D_pooled(PRIMARY) < 0:
        "NULL — PRE-COMMIT VIOLATION (direction reversed)"
  elif n_clear == 12:
        "PASS"
  elif clears(PRIMARY) and n_clear >= 8:
        "DIRECTIONAL"
  elif clears(PRIMARY):
        "WEAK-DIRECTIONAL"
  else:
        "NULL"
```

**Note the asymmetry, which is deliberate.** `D_pooled(PRIMARY) < 0` triggers the
pre-commit-violation branch **at any magnitude, significant or not**, because the
direction — not its significance — is what was locked in §1.1. `D_pooled(PRIMARY) == 0`
falls through to the ordinary ladder and ends at NULL, since a zero difference fails
`sign_ok`.

**Both raw and Bonferroni-corrected significance are reported** for every test
(Protocol §1.5). The verdict uses `alpha_bon` only.

**Equal NULL prominence.** A NULL here is as publishable as a PASS and will be written
with the same prominence and the same detail. It would establish that the modality
distinction in the conditional apparatus is **not** register-coded — which directly
bounds cross-finding-028's "register lives in the function words" claim by naming a
function-word axis that does not carry register. That is a first-class result.

---

## 7. WHAT WOULD FALSIFY THIS

- `share(LEGAL) ≥ share(POLEMIC ∪ ESCHATOLOGICAL)` → pre-commit violation, published as
  NULL.
- The contrast surviving unstratified permutation but dying under any of the six
  length-stratified nulls → the effect was length, and is published as such.
- The contrast surviving `D_pooled` but dying under `D_V` → the effect was *verse*
  length, and is published as such.
- Any cell falling below the 20-token power guard → that cell is `NOT-POWERED` and the
  finding says so rather than quietly dropping it.

---

## 8. OUTPUTS

- Run directory: `findings/phase-b-hypotheses/runs/h-new-3010/<UTC timestamp>/`, created
  with `os.makedirs(..., exist_ok=False)`; every file opened with mode `'x'`.
  **Write-once — the script never overwrites a file inside its own run directory**
  (`UNIT-DRIFT-DEFECT.md` §7). No checkpointing is performed.
- `manifest.json` — prereg path + SHA-256, script path + SHA-256, frozen input SHA-256s,
  seed, n_perm, UTC timestamp, Python version.
- `results.json` — every statistic, every one of the 144 permutation p-values, the
  length diagnostic, the descriptive tables, and the verdict.
- `verdict.txt` — the verdict line and the 12-test clearance table.
- Finding: `findings/phase-b-hypotheses/h-new-3010-conditional-register.md`.

**No run directory is ever deleted**, including a superseded or erroneous one. A
corrected run goes to an additional directory and both are retained
(`CONTINUE-PROMPT.md` STANDING RULES §2).

---

## 9. GARDEN OF FORKING PATHS — every choice considered, and why it was resolved as it was

Each entry records an alternative that was genuinely available and is hereby closed.

**9.1 Unit of analysis.** Surah (chosen) / verse / pericope. The register label is a
surah-scale label, so the surah is the exchangeable unit; permuting labels at verse or
token level would be pseudo-replication against a label that has no verse-level
variation. Pericope-scale is the natural sharpening (cross-finding-025) but no
pericope-scale register labelling exists on disk, and building one here would be a
hand-assigned proxy — the defect class `findings/PROXY-CLAIMS.md` exists to prevent.
**Recorded as the single largest limitation of this design.**

**9.2 The outcome statistic.** Irrealis *share* among conditionals (chosen) /
conditionals per verse / conditionals per 100 words / a log-odds ratio. The share was
chosen specifically because its denominator is not a unit count (§4.1). The two density
forms were rejected as textbook unit-drift. Log-odds was rejected because it is
undefined for a zero cell and the corpus is certain to contain groups with zero
irrealis tokens at some strata.

**9.3 Pooled vs unweighted-mean share.** Pooled over tokens (chosen for `D_pooled`) /
mean over surahs of the per-surah share. Pooling lets a few conditional-dense surahs
dominate; a surah-mean is noisy for surahs with 1–2 conditionals and needs an arbitrary
minimum-token cutoff, which is a free parameter. Pooling was chosen because the
permutation null naturally absorbs the which-surah-lands-where variance. **The
surah-unweighted mean is nonetheless computed and reported as a declared secondary
descriptive arm, and is not in the decision rule.**

**9.4 The register mapping.** Legal-precedence containment (M1) / first-token dominance
(M2) / hand assignment / restricting to unambiguous single-token labels only. Hand
assignment was rejected outright (proxy defect). Restricting to unambiguous labels was
rejected because it would silently delete Q 9 and Q 2 — the two heaviest legal surahs —
and a filter that removes the strongest members of a group is not a control. M1 and M2
are both run, as the second rules-tuple axis; M1 is primary because its tie-break runs
*against* the hypothesis (§3.3).

**9.5 The particle sets.** T1 (full pair) / T2 (bare minimal pair) / including
`man` and `maA` / including `idhā`. The conditional nouns and the temporal conditional
were excluded permanently (§2.3) because they carry no realis/irrealis marking, which is
the whole content of the hypothesis. Including `idhā` was specifically considered and
rejected: cross-finding-028 already uses the *idhā*-cascade as an eschatological
feature, so including it would import a known-eschatological marker into a test of
whether eschatological surahs differ — the AUDIT-H-NEW-206 circularity, exactly.

**9.6 Whether to include `lawlā` in the irrealis arm.** Yes in T1, no in T2. The
EXH/COND split (40/35) makes it the single most ambiguous member; QAC resolves it, but
the resolution is an annotation judgement, so both readings are run.

**9.7 The comparison group for H2/H3.** All non-members among the 114 (chosen) / only
the OTHER group / only the opposite contrast group. Using all non-members keeps the
denominator fixed and interpretable and avoids a second arbitrary grouping decision.

**9.8 The length control.** Stratified permutation on three channels × two bin widths
plus a verse-length-matched statistic (chosen) / OLS residualisation of the share on log
length / dropping long surahs / matching on propensity. OLS residualisation was rejected
because it introduces a fitted model into a design whose whole point is to avoid one,
and `AUDIT-H-NEW-206` demotes exactly the pattern where a length feature enters the
machinery. Dropping long surahs was rejected because it would delete the legal register.
Propensity matching was rejected as a hand-tuned instrument with free parameters.

**9.9 Which length channel to control on.** Strongest-by-ρ (the
`UNIT-DRIFT-DEFECT.md` §5 default) / all three (chosen). All three, because selecting
after measuring is a degree of freedom and because §3 of that same document records its
own drift table naming the *wrong* primary channel for months. Requiring every channel
is strictly stronger and removes the choice.

**9.10 Bin width.** 5 / 10 / both with the max taken (chosen), per
`UNIT-DRIFT-DEFECT.md` §6.1 requirement 2 — a single *k* is an undeclared researcher
degree of freedom.

**9.11 One-sided vs two-sided.** One-sided, because §1.2 gives a grammatical reason the
effect must run one way if it exists at all, and because a two-sided test would let a
reversal be reported as a success. The cost — a reversal cannot "pass" — is the
intended cost.

**9.12 Aggregating the 12 nulls per test.** Max (chosen) / min / the primary
configuration / Fisher combination. Max, because a claim should be reported at the
strength of its weakest control.

**9.13 Family size and α.** k = 12 over the full 3 × 4 grid (chosen) / k = 4 counting
only the primary hypothesis across cells / k = 1 for the primary cell alone. k = 12
counts every test whose result will be reported, which is the honest family. It is a
tightening relative to the alternatives and therefore self-verifying.

**9.14 Verdict ladder.** The four-rung ladder of §6 (chosen) / a binary PASS/NULL. The
ladder exists so that a partial result cannot be written up as a PASS; the
`DIRECTIONAL` and `WEAK-DIRECTIONAL` rungs are named failures of the full gate, not
softened passes.

**9.15 Narrative as a third contrast.** Considered and rejected. The hypothesis makes
no directional prediction for narrative, and a post-hoc direction would be a
Protocol §1.2 violation. Narrative is descriptive only.

**9.16 Structural inspections performed before this lock.** The lemma × POS cross-tab
(§2.2) — needed to know which lemmas exist and which tags to filter, without which no
particle set could be specified. TSV coverage (§3.1) — needed to know whether a fallback
column was required. Group memberships and sizes (§3.3) — needed to state the power
guard and to know whether the mappings differ enough to constitute a real axis. Per-surah
word/verse counts (§5.1) — needed to specify the stratification and to verify the QAC
verse counts against `data/hafs-verse-counts.tsv`. **None of these touches the irrealis
share, the group contrast, or any null.** The verse-count cross-check returned 0
mismatches across all 114 surahs.

---

## 10. FROZEN INPUTS

SHA-256 recorded in `manifest.json` at run time for:

- `data/morphology/quranic-corpus-morphology-0.4.txt`
- `findings/classical-sources/neuwirth-sinai-genre-labels.tsv`
- `data/hafs-verse-counts.tsv`
- `data/revelation-order.csv` (used **only** for the descriptive Meccan/Medinan
  cross-tab in the finding; it enters no test statistic and no null)

---

*Pre-registration H-NEW-3010 locked 2026-08-09 by Waiel Al-Shujaa, before any
computation of the outcome. A rate is a ratio and the divisor is part of the claim —
so this claim has no unit count in its divisor at all. Bismillāhi al-Raḥmāni al-Raḥīm.*
