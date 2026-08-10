---
finding_id: H-NEW-3150
title: "PRE-REGISTRATION — Is ṣīghat al-mubālagha over-represented at the fāṣila beyond rhyme shape, divine-name presence and the hapax slot?"
author: Waiel Al-Shujaa
date: 2026-08-09
phase: B
frontier_item: F-7
status: PRE-REGISTERED — NOT YET RUN
seed: 20260509
n_perms: 10000
k_confirmatory: 6
alpha_bonferroni: 0.008333
binding_raw_gate: 0.001
rules_tuple: "(QAC morphology v0.4 segment-token, vocalised-Buckwalter LEM + ROOT, machine template-match wazn, verse-final = word index == max word index, basmala counted only in Q1, Hafs-Kufan, Mashriqi)"
data_source: "data/morphology/quranic-corpus-morphology-0.4.txt; data/asma-al-husna.txt; findings/classical-sources/99-names-wazn-classification.tsv (validation set only)"
---

# PRE-REGISTRATION — H-NEW-3150

## 0. Step-0 staleness check — DID THIS ALREADY EXIST?

Per the BINDING RULE at `HANDOFF/FRONTIER-MAP-2026-08-07.md` §"CALIBRATION", this check
precedes all design decisions and is logged here as the **first** forking-paths entry.

Commands run over `findings/`, `MASTER-FINDINGS-LEDGER.md`, `HANDOFF/`:

```
grep -rniE "mubalagha|mubālagha|mubalaghah|صيغ المبالغة"
grep -rniE "\bwazn\b|awzan|أوزان"
grep -rniE "H-NEW-23\b" ; "H-NEW-2070" ; "H-NEW-2300"
grep -rilE "fasila|fāṣila|fawasil|fawāṣil"
grep -rniE "Faʿīl|Faʿʿāl|Faʿūl|Fāʿil|fa'il|fa''al|fa'ul"
grep -rniE "verse-final (POS|part.of.speech|word class|adjective|noun)"
grep -rl "99-names-wazn" --include="*.py" .      → 0 files
grep -rl "ghazali-attribute-pairs" --include="*.py" .  → 0 files
```

**Result: NOT already answered.** No finding in the repository measures nominal-pattern
density at verse-final position. The six near neighbours, and what each does instead:

| finding | what it measures | why it is not this |
|:--|:--|:--|
| **H-NEW-23** | hapax *lexical rarity* → verse-final, z = +10.61 | rarity, not morphological pattern |
| **H-NEW-2070 / 2300 / 2400** | *divine-name* verse-final pairs, content↔seal matching, co-occurrence network | referent identity, not pattern |
| **H-NEW-2080 / 2240 / 2870 / 2880** | fāṣila *phonology* — rhyme class, rāwī letter, pausal collapse | sound, not morphology |
| **H-NEW-2560** | fāṣila *syntax* — clause seal at 8.1× | constituency, not morphology |
| **H-NEW-3130** (F-6) | *verb* derived forms I–X per surah; NULL 0/6 | verbs, different tagset, not positional |
| **H-NEW-30** / `khawatim-al-hashr-analysis.md` | the only prior use of the wazn TSV | self-labelled **"Descriptive observation (not inferential)"**; non-positional; no test statistic. `TEAM-AMENDMENTS-LOG.md` AMEND-21 records the inferential version as never executed |

Both idle assets named by the frontier map are confirmed idle: zero `.py` files in the
repository read either TSV.

## 1. Hypothesis

**H1.** Nominal tokens in Sībawayh's six *ṣiyagh al-mubālagha* (`Faʿʿāl, Faʿūl, Fuʿūl, Mifʿāl,
Faʿīl, Fuʿʿāl`; *al-Kitāb* i.110–115) occupy the verse-final slot more often than other nominal
tokens **matched on verse length, root rarity, divine-name status and rime shape**.

The four matching variables are the whole test. Unmatched, H1 is near-certain and uninformative:
it would restate that verses end on divine names (H-NEW-2070) which happen to be *faʿīl*.

## 2. Direction — LOCKED, one-sided POSITIVE

Derived from published anchors. **The frontier map's `Prior.` line is explicitly NOT used**: that
map's priors stand at 1-for-6 and every optimistic one has failed.

1. **H-NEW-23 / al-Zarkashī, *al-Burhān* nawʿ 59 §4 (*al-maqṣūda li-ghayrihā*)** — MASTER finding
   #7. Words are *selected into* the terminal slot at verse-construction time (z = +10.61 against
   a within-verse uniform null; register baseline z = +6.43 from the Muʿallaqāt positive control
   T-004). The established sign of terminal-slot selection for a rhetorically marked lexical class
   is **positive**.
2. **Ibn Abī l-Iṣbaʿ al-Miṣrī, *Badīʿ al-Qurʾān* nawʿ 87, *barāʿat al-maqṭaʿ*** — quoted verbatim
   in `findings/TEAM-AMENDMENTS-LOG.md` AMEND-8: *"an yakhtim al-kalām bi-lafẓa mustaḥsana lā
   yaʾtī baʿdahā shayʾ"* — seal the speech with a heightened word after which nothing comes. A
   *ṣīghat al-mubālagha* is by construction a heightened form of its base. Direction **positive**.

Two further anchors predict **decay down the control ladder but not reversal**, and are the reason
the ladder exists rather than a single test:

3. **H-NEW-2080 §B2** — verse-final letters are 60.76 % nūn+mīm against a 32.28 % generic
   word-final baseline (z = +48.1). *Faʿīl* surfaces as ‑īm/‑īr/‑īz, the dominant fāṣila rime. Predicts
   the raw effect is partly rhyme shape → should shrink under the rime-class stratum.
4. **H-NEW-2070** — 321 verses close on a divine-name pair. Predicts the raw effect is partly
   referent → should shrink under the divine-name stratum.

**A reversal is a live outcome and is pre-registered as an equally-prominent verdict** (§7), because
three CBM priors on this map have been refuted in the opposite direction from the one anticipated.

## 3. Population, instrument and unit

### 3.1 Frame

All QAC v0.4 **stem** segments with `POS ∈ {N, ADJ}`, a `LEM`, and a triliteral `ROOT`, whose
normalised vocalised Buckwalter lemma matches **exactly one** of 19 templates (§3.2).

- QAC segments: **128,219**. Verses: **6,236**.
- `POS:ADJ` = **1,961**, `POS:PN` = **3,911** — both counts verified against the map, exactly.
- Nominal (N+ADJ) stems with lemma+root: **26,730**.
- **Machine-labelled analysis frame: 9,383 tokens** (35.1 % of nominal stems).

### 3.2 Instrument — machine wazn, NOT the hand TSV

The wazn label is **computed**, not assigned. For root `(c₁,c₂,c₃)` the vocalised Buckwalter lemma
is matched against fixed templates: `Faʿīl = c₁+a+c₂+iy+c₃`, `Faʿʿāl = c₁+a+c₂+~aA+c₃`,
`Faʿūl = c₁+a+c₂+uw+c₃`, `Fāʿil = c₁+aA+c₂+i+c₃`, and 15 more (full list in the script). Two
normalisations, both locked:

- a `~` immediately after radical 1 with no intervening vowel is **sun-letter assimilation of the
  definite article** and is stripped (`r~aHiym` → `raHiym`); a `~` after radical 2 is the genuine
  gemination of *faʿʿāl* and is kept;
- for geminate roots (c₂ = c₃) the CVC-final templates carry a collapsed variant (`rab~` for
  *faʿl* of `rbb`).

A token is labelled only if **exactly one** template matches. Measured: **0 multi-template
collisions** across the frame.

**Why the TSV is not the instrument.** `99-names-wazn-classification.tsv` covers 99 names; the
frame is 9,383 tokens. The TSV is used **only as a validation set** for the machine labeller (§3.4)
and as sensitivity arm S4.

### 3.3 Proxy census of the hand-assigned TSV — per `findings/PROXY-CLAIMS.md`

100 data rows (99 names + *Allāh*). All figures machine-counted from the file:

| quantity | value |
|:--|--:|
| rows | 100 |
| confidence HIGH / MEDIUM / LOW | **95 / 3 / 2** |
| distinct `wazn` labels | 20 |
| distinct `wazn_family` buckets | 11 |
| rows where `wazn ≠ wazn_family` (fine label coarsened away) | **19** |
| rows in a **non-pattern** bucket (`Proper` 1 + `Substantive` 12 + `Compound` 2) | **15** |
| rows carrying an unambiguous single derived pattern | **85** |
| `is_mubalagha = 1` | **40** |
| …of which `Faʿīl`, which the TSV's own header calls *contested* | **27 (67.5 % of the flag)** |
| `is_mubalagha = 1` after dropping Faʿīl (TSV limitation #4) | **13** |
| notes-field keyword flags for contestation | 1 |

**The ambiguous fraction is 15 % structurally** (15 of 100 rows are not in a derived pattern at
all), **and the mubālagha flag itself is 67.5 % carried by a single pattern the source document
declares contested.** That is why the strict-5 arm (§7, S1) is pre-registered rather than optional.

### 3.4 Rater agreement — measured, not asserted

Two lanes have reported rater agreement at κ = 0.386 and κ = 0.468. A second classification of
these 99 names does **not** exist on disk; one is therefore **constructed** by applying the §3.2
machine labeller to the QAC lemma of each name, and agreement is measured against the hand TSV.
Join is by stripped Arabic surface with the dagger alif expanded both ways (ٰ → ا and ٰ → ∅), so
that defective Quranic rasm (`رَّحْمَٰن`) and plene TSV spelling both match.

| | value |
|:--|--:|
| TSV names joined to a QAC lemma | **72 / 100** |
| …of which the machine returns a unique wazn | **47** |
| hand = machine | **45 / 47 = 95.7 %** |
| **Cohen's κ, multi-class wazn** | **0.942** |
| **Cohen's κ, binary `is_mubalagha`** | **0.950** |

**This number must not be read as vindicating the TSV wholesale, and the pre-registration says so
before the run.** Three qualifications, all measured:

1. **The machine abstains on the hard cases.** Of 72 joined names it labels 47 and abstains on 25.
   The 25 are weak-rooted (*al-ʿAlī, al-Qawī, al-Walī, al-Ghanī, al-Ḥayy, al-Qayyūm, al-Nūr,
   al-Awwal*), hamzated (*al-Bāriʾ, al-Muʾmin*), quadriliteral (*al-Muhaymin*) or defectively
   written (*al-Raḥmān, al-Khāliq, al-Bāsiṭ*). **κ = 0.942 is measured on the transparent half; the
   TSV's contested calls remain unvalidated by anything.**
2. **Both "disagreements" are join failures, not analytic disagreements.** *al-Muʿizz* joined to
   `مَعْز` (*maʿz*, "goats", root `mEz`) and *al-ʿAfū* to `عَفْو` (*ʿafw*, the verbal noun). The TSV
   is right in both cases and the machine's *classification* never contradicted it where both
   spoke. Corrected agreement on correctly-joined names is 45/45.
3. **The two raters are not independent.** Both read the same surface form. This measures
   transcription fidelity, not the analytic judgement that κ = 0.386 and κ = 0.468 measured.

### 3.5 Outcome and the tie fraction — per `findings/TIED-OUTCOME-DEFECT.md`

`is_final` = 1 iff the token's word index equals the maximum word index of its verse.

| quantity | value |
|:--|--:|
| verse-final tokens in frame | **2,029 / 9,383 = 21.62 %** |
| **tie fraction of `is_final`** | **78.4 % tied at 0** |
| per-verse mubālagha **count** outcome | **66.8 % of verses tied at zero** |

**Both exceed 50 %, so a parametric p is not usable and the permutation null is primary** — this is
the standing requirement, discharged in the pre-registration as the rule demands. The parametric
normal-approximation z is computed and reported **alongside** every permutation p, because
TIED-OUTCOME-DEFECT §3.3 requires the disagreement to be visible where both are available.

### 3.6 Marginals (computed before locking; the cross-tab was NOT computed)

| wazn | n | mubālagha-6 | divine-name tokens |
|:--|--:|:--:|--:|
| Faʿl | 4,113 | 0 | 18 |
| **Faʿīl** | **2,205** | **1** | **962** |
| Faʿal | 901 | 0 | 92 |
| Fāʿil | 641 | 0 | 30 |
| **Faʿūl** | **492** | **1** | 103 |
| Afʿal | 376 | 0 | 0 |
| Mufʿil | 264 | 0 | 0 |
| **Fuʿūl** | **111** | **1** | 2 |
| Faʿil | 81 | 0 | 15 |
| **Faʿʿāl** | **69** | **1** | 38 |
| Mufaʿʿil | 42 | 0 | 1 |
| **Mifʿāl** | **28** | **1** | 0 |
| Muftaʿil | 22 | 0 | 4 |
| Mutafaʿʿil | 15 | 0 | 7 |
| **Fuʿʿāl** | **10** | **1** | 0 |
| Mufāʿil | 7 | 0 | 0 |
| Faʿlān | 4 | 0 | 0 |
| Fuʿʿūl | 2 | 0 | 2 |

- **mubālagha-6 tokens: 2,915.** Strict-5 (Faʿīl dropped): **710**.
- Divine-name tokens: **1,274**. Verses with ≥ 1: **927 / 6,236 = 14.9 %**.
- **962 of the 2,205 Faʿīl tokens (43.6 %) are divine names.** The confound in one number.
- **The mubālagha-6 class is 75.6 % Faʿīl by token — the contested pattern.** The headline test
  is, numerically, mostly a Faʿīl test, which is why S1 is confirmatory-adjacent and reported
  in the abstract.
- The three smallest patterns (Fuʿʿāl 10, Mifʿāl 28, Faʿʿāl 69) are too sparse for per-pattern
  inference and **no per-pattern claim will be made for them**.

**Explicitly NOT computed before this file was locked:** the cross-tabulation of `is_mubalagha`
against `is_final`, in any arm, stratified or not. Marginals of each variable separately, stratum
sizes, S_max and MDE are instrument properties (`h-new-3030` §3.5 line 102: *"Power and S\* are
functions of the null over the pools alone. Neither depends on the observation."*).

## 4. The three length channels — all run, worst is the headline

| channel | verse-length definition |
|:--|:--|
| **CH-W** | whitespace/QAC **word** count of the verse (this is H-NEW-23's channel) |
| **CH-S** | QAC **morphological segment** count of the verse |
| **CH-N** | count of **machine-labelled nominal tokens** in the verse — the eligible-slot count |

Corpus means: 12.42 words, 20.56 segments per verse. Tokens are stratified by **quintile** of their
verse's value on the channel. Locked at quintiles: MDE was computed at 2/3/4/5/10 bins and is flat
at 29–32 across all of them (§6), so bin count is **not** a deciding parameter here; deciles are
sensitivity arm S2.

## 5. Design — a stratified label-shuffle ladder

Statistic **S = number of mubālagha tokens at verse-final**, summed over informative strata.

Null: **shuffle the `is_mubalagha` label among tokens within each stratum**, 10,000 permutations,
`seed = 20260509`. A stratum is *informative* iff n ≥ 2 and both labels and both outcomes occur in
it; non-informative strata contribute zero to S and to the null by construction.

One-sided p = (1 + #{S_perm ≥ S_obs}) / (1 + 10,000). **Resolution floor: p ≥ 9.999 × 10⁻⁵.**

### 5.1 The ladder (descriptive — NOT confirmatory)

| arm | strata |
|:--|:--|
| A1 | none |
| A2 | length quintile |
| A3 | + rare root (root token count ≤ 3; n = 218) |
| A4 | + divine-name status |
| A5 | + rime class |

### 5.2 The confirmatory family, k = 6

| id | arm | frame | channel |
|:--|:--|:--|:--|
| C1 | A5 | full | CH-W |
| C2 | A5 | full | CH-S |
| C3 | A5 | full | CH-N |
| C4 | A5 minus the divine stratum | **verses containing zero divine-name nominal tokens** (6,671 tokens, 71.1 %) | CH-W |
| C5 | as C4 | as C4 | CH-S |
| C6 | as C4 | as C4 | CH-N |

**Rime class** is the pair (long vowel before the final consonant ∈ {ā, ū, ī, none}, final
consonant grouped into 13 classes + other) computed on the unvocalised lemma — 52 populated
classes. Raw two-letter rime is sensitivity arm S3.

## 6. Power — computed before the run

Per stratum with n tokens, m mubālagha and f verse-final, S is hypergeometric under the null:
E = Σ mf/n, Var = Σ mf(n−f)(n−m) / n²(n−1). S\* = E + z₀.₉₉₉·SD. S_max = Σ min(m,f).
MDE = (z₀.₉₉₉ + z₀.₈₀)·SD.

| arm | informative strata | tokens | E[S]ₙᵤₗₗ | SD | **S\*** | **S_max** | **MDE** |
|:--|--:|--:|--:|--:|--:|--:|--:|
| C1 CH-W | 50 | 2,496 | 286.7 | 7.85 | 310.9 | 452 | 30.9 |
| C2 CH-S | 49 | 2,299 | 289.3 | 7.82 | 313.4 | 454 | 30.7 |
| C3 CH-N | 44 | 2,621 | 284.3 | 8.04 | 309.1 | 462 | 31.6 |
| C4 CH-W | 45 | 1,967 | 252.5 | 7.47 | 275.6 | 402 | 29.4 |
| C5 CH-S | 45 | 1,796 | 260.5 | 7.43 | 283.4 | 409 | 29.2 |
| C6 CH-N | 47 | 2,134 | 258.5 | 7.53 | 281.7 | 411 | 29.6 |

**The UNTESTABLE-AT-THIS-N branch is evaluated and does not fire on any arm**: S\* < S_max
everywhere (worst margin C3, 309.1 vs 462). The design can reject in principle. What it can
reject against is an excess of **≈ 30 tokens on a null mean of ≈ 285 — a relative excess of about
11 %, at 80 % power.** An effect smaller than that will return NULL from this instrument and the
NULL will mean only that.

**The cost of the rime stratum is stated here, before the run, because it is large**: A5 retains
only ~2,500 of 9,383 tokens as informative. Rime shape and nominal pattern are close to collinear
— *faʿīl* is ‑īC by construction — so conditioning on rime removes most of the contrast. This is
a real limit on C1–C6 and is not a defect of the implementation.

## 7. Decision rule — LOCKED

Gate: an arm **passes** iff `direction is positive` **AND** `p_perm_one_sided ≤ 0.001` (binding raw
gate) **AND** `p_perm_one_sided ≤ 0.008333` (Bonferroni k = 6). Since 0.001 < 0.008333 the raw gate
binds; both are checked and both reported.

**HEADLINE = the worst (largest p) of C1–C6.** The dominant channel — the one whose p is furthest
from the others — is named in the abstract.

| verdict | condition |
|:--|:--|
| **CONFIRMED (PASS-RESIDUAL)** | all six of C1–C6 pass |
| **PASS-DIVINE-DEPENDENT** | C1–C3 all pass **and** at least one of C4–C6 fails → the effect does not survive removing divine-name verses. **This goes in the abstract, in the first three sentences.** |
| **PASS-PARTIAL** | at least one, but not all, of C1–C6 pass, and the C1–C3 / C4–C6 split is not clean |
| **NULL** | none of C1–C6 passes. Must report per-arm MDE, S\*, S_max and the UNTESTABLE branch evaluation |
| **REVERSED → EQUAL PROMINENCE** | any confirmatory arm has S_obs < E[S]ₙᵤₗₗ with two-sided p ≤ 0.008333. Reported with equal prominence in the abstract **regardless of the other arms' verdicts** |
| **UNTESTABLE-AT-THIS-N** | an arm with S\* > S_max is reported as untestable and does **not** count as a NULL |

`PASS-DIVINE-DEPENDENT` and `REVERSED` can co-occur with each other and with `PASS-PARTIAL`; all
applicable labels are emitted, not just the first that matches.

## 8. Sensitivity arms — reported, not confirmatory

| id | variation |
|:--|:--|
| S1 | **strict-5 mubālagha** (Faʿīl dropped; n = 710) on all six confirmatory arms |
| S2 | deciles instead of quintiles |
| S3 | raw two-letter rime instead of coarse rime class |
| S4 | hand-TSV wazn labels in place of machine labels, on the 47 doubly-labelled names |
| S5 | **`POS:ADJ` only** (the frontier map's stated instrument) vs `N+ADJ` |
| S6 | within-verse uniform-slot null (the H-NEW-23-comparable statistic) |

**S5 is not cosmetic.** The map specifies `POS:ADJ (1,961)`, but QAC tags the same lemma under both
`N` and `ADJ`: *ʿalīm* is ADJ 101× and N 62×; *ghafūr* is N 62× and ADJ 29×; *ʿazīz* is N 63× and
ADJ 38×. Restricting to ADJ discards 38 % of *ʿalīm* and 68 % of *ghafūr* — precisely the tokens
the hypothesis is about. H-NEW-2400 §115 already documented this as a matcher artefact. The frame
is therefore **N+ADJ**, and ADJ-only is run as sensitivity to quantify what the map's instrument
would have lost.

## 9. Garden-of-forking-paths log — every choice made before locking

1. **Step-0 staleness grep run before any design** (§0). Result: not already answered. Six near
   neighbours identified; two of them changed the design.
2. **Direction derived from H-NEW-23 + Ibn Abī l-Iṣbaʿ**, not from the map's `Prior.` line, which
   is discarded per the map's own calibration block.
3. **Rhyme-shape added as a confound the map did not name**, on the strength of H-NEW-2080 §B2.
   Without it the test cannot distinguish morphology from assonance.
4. **Instrument switched from the hand TSV to a machine template matcher**, because the TSV covers
   99 names and the frame is 9,383 tokens. The TSV became the validation set.
5. **Frame set to N+ADJ, not ADJ-only**, on measured evidence of QAC POS-splitting of the same
   lemma (§8). ADJ-only retained as S5.
6. **Quintiles locked** after computing MDE at 2/3/4/5/10 bins and finding it flat at 29–32.
7. **Rare-root threshold ≤ 3** (n = 218) rather than strict hapax (n = 82), because 82 positives
   across ~50 strata is mostly non-informative. Strict hapax noted as a further sensitivity.
8. **Verse-final defined as word index == max word index**, including tokens carrying an enclitic
   suffix, because the rhyme is carried by the whole word.
9. **Divine-name roster reused from H-NEW-2070** (`data/asma-al-husna.txt`, 97 single-token
   al-Tirmidhī names) with its published `strip_al` normalisation, rather than a new roster.
10. **Marginals computed, cross-tab not** (§3.6).
11. **10,000 permutations** with the resolution floor stated (§5), rather than raising n_perm to
    chase a smaller p.
12. **Both parametric and permutation p reported** on every arm, per TIED-OUTCOME-DEFECT §3.3.

## 10. Immutability

This file is hashed with SHA-256 and the digest embedded in
`findings/phase-b-hypotheses/scripts/h-new-3150.py` as `EXPECTED_PREREG_SHA`. The script verifies
it at runtime and exits non-zero on mismatch. **Per `findings/feedback`-established rule and the
four broken locks of commit `b76ec401f`: this file is never edited after the run. Corrections go
in the finding.**

Run directory: `findings/phase-b-hypotheses/runs/h-new-3150/<UTC>/`, created with
`os.makedirs(exist_ok=False)`, all artefacts written with `open(..., 'x')`. Never deleted.
