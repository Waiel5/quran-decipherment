---
id: H-NEW-3120
title: "Asbāb al-nuzūl coverage as a chronology instrument — instrument audit, and a STEP-vs-GRADIENT test of the text's own retrospective marker"
status: PRE-REGISTERED 2026-08-09
author: Waiel Al-Shujaa
frontier_item: F-12 (HANDOFF/FRONTIER-MAP-2026-08-07.md)
spec_locked_at: 2026-08-09, BEFORE any phase-conditioned statistic on the ʾiḏ channel was computed
seed: 20260509
n_perm: 10000
bonferroni_family: h-new-3120-arm-a
bonferroni_k: 2
alpha_bon: 0.025
alpha_note: "k=2 over the two verdict-bearing hypotheses H1/H2. Rules-tuples are ROBUSTNESS, not multiplicity — the H-NEW-3070 precedent."
primary_text: quran-text/quran-no-tashkeel.json
morphology: data/morphology/quranic-corpus-morphology-0.4.txt
morphology_sha256: a1d12923815341face765083805d2148ed2d9f5cc3f7d6665219d887675d8c46
chronology: data/revelation-order.csv
asbab_source: data/literature/classical-tafsir/spa5k-tafsir-api/en-asbab-al-nuzul-by-al-wahidi/
method_parents:
  - findings/ABSENCE-CLAIMS.md
  - findings/PROXY-CLAIMS.md
  - findings/UNIT-DRIFT-DEFECT.md
  - findings/TIED-OUTCOME-DEFECT.md
  - findings/AUDIT-H-NEW-206-LENGTH-CONFOUND.md
  - findings/phase-b-hypotheses/cross-finding-029-the-deciding-parameter.md
shape_anchor: findings/phase-b-hypotheses/h-new-3070-deictic-gradient.md
---

# H-NEW-3120 — pre-registration

## 0. STEP-0 GREP — what already existed, run BEFORE any design

Mandated by the brief. Commands and results are recorded here because
[[ABSENCE-CLAIMS]] requires a claim about prior work to state its search.

```
grep -ril "asbab\|asbāb\|occasion.of.revelation" findings/
grep -ril "chronology instrument\|revelation.order\|noldeke\|al-Wahidi" findings/
grep -in "asbab\|chronolog\|noldeke\|egyptian standard" MASTER-FINDINGS-LEDGER.md
find /Users/grey/Downloads/quran -not -path "*/.git/*" -not -path "*/.claude/worktrees/*" \
  \( -iname "*asbab*" -o -iname "*wahidi*" -o -iname "*nuzul*" -o -iname "*lubab*" \)
```

**Prior asbāb work:** `findings/phase-b-hypotheses/asbab-nuzul.md` (2026-04-12), status
`exploratory`, claim_class historical-contextual. It states of itself: *"No pre-registered null was
defined for sabab-attribution itself."* Its contents are treated here as **hypotheses, not data**,
and every number taken from it is re-verified. **One is already refuted** — see §6.4.

**Prior chronology-instrument work, none of it on asbāb coverage:** `h-new-125` (15-axis Nöldeke
map), `h-new-212`/`h-new-222` (four chronologies under Fisher-Rao; carries a ⛔ pillar-2
correction), `h-new-46.1` (period stratification), `h-new-2350`, `h-new-267`, `h-new-224`,
`h-new-229`. Ledger §274 records the **MW-2 domain split** — Nöldeke chronology is a hidden-axis
pseudo-confound on structural/geometric axes but a genuine axis on lexical-content axes. The ʾiḏ
channel tested here is a lexical-content axis, which is the side of that split where the axis is
real.

**`PROXY-CLAIMS.md:192-243`: ρ(Nöldeke, Egyptian standard) = +0.7714, Kendall τ = +0.5771**,
independently confirmed by two harnesses, classed **PARTIAL** as a proxy. The two chronology
instruments this pre-registration uses as rules-tuples are therefore **not independent**, and are
not presented as such.

**F-12's specific question — does asbāb coverage predict chronology — is unasked anywhere.** It is
also **instrument-blocked**, which §1 establishes and which is the finding.

---

## 1. THE INSTRUMENT AUDIT — established BEFORE this pre-registration, and it blocks the literal F-12

These measurements are **not hypotheses**. They are facts about the file tree, established and
machine-checked before any test was designed, and they are the reason Arm A is not a coverage test.

### 1.1 The source is truncated at surah 77

`en-asbab-al-nuzul-by-al-wahidi/` contains **surahs 1..77 exactly, gapless**, and **nothing from
78..114** (37 surahs absent). The absent block is **34 Meccan / 3 Medinan**, and by Nöldeke phase
**35 Early Meccan / 2 Medinan**.

**Two distinct absence-encodings coexist in the directory, and that is the proof it is a scrape
boundary and not an editorial judgement:**

| encoding | instances | meaning |
|:--|:--|:--|
| file present, zero entries | **Q 72, Q 77** | the source says "no occasion here" |
| **file absent entirely** | **Q 78–114** | ingestion never reached it |

Coverage inside the present block is **sparse and scattered — 1,089 entries against 5,672 verses
= 19%**, from Q 2 at 0.45 down to Q 67 at 0.07, with only Q 1 at full coverage. Selectivity is
expressed at verse level throughout. **A contiguous gapless surah-level cut sitting on top of
scattered verse-level selectivity is an ingestion boundary.**

**Comparator control:** `en-al-jalalayn`, `ar-tafsir-ibn-kathir` and `en-tafsir-ibn-abbas` each
carry **114** surah files from the same spa5k tree. Only the asbāb edition carries 77.

**Absence claim, with its search stated as [[ABSENCE-CLAIMS]] requires:** the `find` above returns
5 hits repo-wide, all accounted for; `editions.json` (27 editions) contains exactly one asbāb
edition (id 86, source altafsir.com). **No al-Wāḥidī coverage of surahs 78–114 exists on disk.**

### 1.2 The source is a blend — 72% is not al-Wāḥidī

`PROXY-CLAIMS.md:384-486` (census of 2026-08-08) established this directory is **al-Wāḥidī 28% +
a Persian Sufi commentary 72%**, refuted decisively by *Shaykh al-Islām Anṣārī* (d. 481) quoted at
`20/5` when al-Wāḥidī died 468. **Independently re-classified here rather than inherited:** of
1,089 non-empty entries, **353 (32.4%) carry al-Wāḥidī isnād/revelation formulae, 393 (36.1%) carry
the Sufi register, 2 both, 341 (31.3%) neither → ambiguous fraction 31.5%.** My classifier is more
permissive than the published one; both agree the directory is a blend. **All 7 verses of Q 1 are
the Sufi text.**

**Any per-verse "has a recorded occasion" flag built here is a PROXY with a 31.5% ambiguous
fraction**, declared per [[PROXY-CLAIMS]].

### 1.3 Coverage is a LENGTH instrument, not a chronology instrument

Per-surah coverage rate, Spearman. **All three length variables run; none locked.**

| channel | naive F-12 (all 114, absent = 0) | clean window (1–77) |
|:--|--:|--:|
| verse count | +0.4995 | **−0.0678** |
| word count | +0.7244 | +0.2571 |
| **mean verse length** | **+0.8206** | **+0.6394** |
| Nöldeke phase ordinal | +0.7350 | +0.5774 |
| Egyptian standard rank | +0.5187 | +0.3944 |
| **mushaf index** | **−0.7665** | −0.3237 |
| tie fraction | **0.3772** | 0.0779 |

**Mean verse length beats chronology in both windows.** The dominant length channel is **mean verse
length**; **verse count is the worst and in the clean window it is nothing at all (−0.0678)**.
This is the fourth independent confirmation of that channel ordering in this project, after
H-NEW-3010, H-NEW-3070 and the F-3 correction.

**The naive F-12 instrument would have returned ρ = +0.7350 against Nöldeke at p ≈ 1.3×10⁻²⁰.**
It would have been measuring where a scraper stopped and how long the verses are. Its tie fraction
of 0.3772 is 37 surahs tied at exactly zero — the 37 that were never ingested.

### 1.4 The circularity named in the brief, quantified

| | value |
|:--|--:|
| asbāb-covered verse entries: Medinan / Meccan | 536 / 553 |
| **fraction of covered verses that are Medinan** | **0.4922** |
| corpus baseline Medinan verse share | 0.2603 |
| **enrichment** | **1.89×** |
| **enrichment within the clean window 1–77** | **1.74×** |

The confound **survives removal of the truncation**. Instrument and outcome share the construct —
the [[AUDIT-H-NEW-206-LENGTH-CONFOUND]] defect. **Conclusion: the literal F-12 coverage test is
not run. It is not a test of chronology.**

---

## 2. WHAT IS ACTUALLY TESTED — Arm A, and why it is the faithful residue of F-12

F-12 asks what a *recorded occasion* predicts. The external roster cannot answer that. The
**text's own retrospective anchoring** can, and it needs no coverage variable, so it is immune to
both §1.1 and §1.2.

**Channel: the particle ʾiḏ (إذ)** — the narrative-past hinge that introduces retrospective
episodes, and the marker `asbab-nuzul.md` §2.1 identifies as *"the most pervasive internal
sabab-marker."*

**Extraction rule, LOCKED:** QAC segments with `LEM:<i*`. Verified before locking: **239 segments,
POS:T for all 239**, surface forms `<i*o` 224 / `<i*i` 12 / `<i*` 3. The distinct lemma `LEM:<i*aA`
(ʾiḏā, 409 segments) is **excluded by lemma, not by string** — the QAC lemma partition separates
them cleanly, avoiding the homograph trap that a string match on `إذ` incurs.

### 2.1 The validity limit, stated before the test and not after

**ʾiḏ marks retrospective narration generally, not Muhammadan-sīra occasions specifically.** A
large share of its tokens introduce Israelite and prophetic-past episodes that no asbāb report
attaches to. **This channel therefore measures retrospective-narrative deixis, and the inference
from it to "occasion of revelation" is an interpretive step this pre-registration does not
license.** It is named here so that the finding cannot be read as more than it is. Nothing below
calls ʾiḏ an occasion marker.

---

## 3. HYPOTHESES — directions LOCKED and justified from published anchors

**H1 — THE STEP (surah-level).** mean(ʾiḏ density | Medinan) − mean(ʾiḏ density | Meccan) > 0.
**Direction LOCKED POSITIVE.**

**H2 — THE GRADIENT (surah-level).** Spearman ρ(ʾiḏ density, Nöldeke phase ordinal ∈ {0,1,2,3}) > 0.
**Direction LOCKED POSITIVE.**

**Justification for the locked direction — three published anchors, not the frontier map's Prior line:**

1. `asbab-nuzul.md` §2.1 (2026-04-12) reports ʾiḏ per-verse Medinan 0.0308 vs Meccan 0.0230,
   **ratio 1.34× Medinan-enriched.** This is the eyeball and is declared as such in §6.
2. **H-NEW-3070** (2026-08-09) establishes that the corpus's registral shift is carried at the
   **Meccan→Medinan boundary** (Late→Medinan the only surviving step, distal share 0.677 → 0.847).
3. Ledger §274 **MW-2 domain split** — chronology is a genuine axis on lexical-content axes.

### 3.1 THE SHAPE PREDICTION — the novel, falsifiable part

H-NEW-3070's central methodological claim is that **"a binary beating a rank is the signature of a
step, not a slope."** That claim was made on the deictic channel. **This pre-registration tests it
as a prediction on an independent channel.**

**PREDICTED, before the run:**

- **S1.** p_worst(H1, binary) < p_worst(H2, 4-phase rank).
- **S2.** The **Meccan-internal contrast** — Early/Middle/Late only, Medinan deleted — is **NULL**.
  Defined without ambiguity: two Meccan-internal statistics are computed, **H1m** =
  mean(density | Late Meccan) − mean(density | Early+Middle Meccan), and **H2m** =
  Spearman ρ(density, phase ordinal ∈ {0,1,2}) over Meccan surahs only. Both use the same
  seven length settings and the same worst-governs rule. **S2 holds iff BOTH H1m and H2m fail
  to clear α = 0.025 at their worst channel.** A single Meccan-internal survivor breaks S2.
- **S3.** The Egyptian-standard tuple (R2) is **weaker** than Nöldeke (R1), as in H-NEW-3070 §6.2.

If S1 and S2 both hold, the step-shape replicates on a second channel. **If S2 fails — if there is
a live Meccan-internal gradient in ʾiḏ — then H-NEW-3070's step claim does not generalise, and
that is the more interesting outcome.** Both directions are recorded as informative.

### 3.2 The unit check — [[UNIT-DRIFT-DEFECT]]

Both units reported; **the surah-level pair H1/H2 is verdict-bearing.**

- **U1 (token-level, reported, NOT verdict-bearing):** mean Nöldeke phase ordinal of the 239 ʾiḏ
  tokens, against the corpus mean phase ordinal weighted by verse count.

Reporting a token-level statistic without the surah-level one, or the reverse, is the unit-drift
defect. Both appear in the output table whatever they say.

---

## 4. NULL MODEL, LENGTH CONTROL, AND THE DECIDING PARAMETER

**Null:** permutation of phase labels across surahs, **seed 20260509, 10000 permutations**,
one-sided in the locked direction.

**Length control — three variables, none locked, WORST GOVERNS.** Seven settings:

| id | setting |
|:--|:--|
| L0 | unstratified |
| L1 | verse count · quintile / decile |
| L2 | word count · quintile / decile |
| L3 | **mean verse length** · quintile / decile |

Permutation is **within stratum**. **The worst (largest) p across all seven settings is the
verdict-bearing p for each hypothesis.** Every setting is reported whatever it says. Stratum
informativeness (fraction of strata containing ≥2 distinct phase labels) is computed and reported,
because a control with no permutation freedom is not a control.

**THE DECIDING PARAMETER** — declared a priori per [[cross-finding-029]] §3: **the length channel.**
§1.3 already shows this variable swinging a correlation from −0.0678 to +0.6394 on adjacent
channels of the same construct. The verdict is reported under all three and the dominant one named.

**Rules-tuples (ROBUSTNESS, not multiplicity):**

| tuple | definition |
|:--|:--|
| **R1** | Nöldeke phase ordinal / Nöldeke Meccan-Medinan — **PRIMARY** |
| **R2** | Egyptian standard (Tanzil) `period` and `revelation_order` |

**R1 and R2 are ρ = +0.7714 correlated and are not independent tests.** Reported as sensitivity.

**Tie fraction** of the per-surah ʾiḏ density is measured and reported per [[TIED-OUTCOME-DEFECT]].
**If it exceeds 0.50 the test is switched to an EXACT test.** The fraction of null draws exactly
equal to the observed statistic is reported for every verdict-bearing cell.

---

## 5. DECISION RULE — exact, and to be diffed line by line against the script before running

α = **0.025** (Bonferroni k = 2), one-sided, sign must match the locked direction.

```
PASS      := sign(H1) > 0 AND p_worst(H1) < 0.025
         AND sign(H2) > 0 AND p_worst(H2) < 0.025
PARTIAL   := exactly one of {H1, H2} satisfies its clause above
NULL      := neither satisfies its clause
```

A wrong-signed statistic **cannot** pass, whatever its p-value.

**Shape verdict, evaluated separately and only reported alongside the above:**

```
STEP-REPLICATED     := S1 holds AND S2 holds
GRADIENT-FOUND      := S2 fails (Meccan-internal contrast significant, correct sign)
SHAPE-INDETERMINATE := otherwise
```

**If the verdict is NULL, an MDE at 80% power is computed and published, including the
UNTESTABLE-AT-THIS-N branch** (h-new-3030 §3.5): if the maximum attainable statistic is below the
critical value, the design could not have detected any effect and the null is reported as
UNTESTABLE, not as evidence of absence.

---

## 6. GARDEN-OF-FORKING-PATHS LOG

**6.1 — The Step-0 grep is logged in §0**, as the brief requires. Its result changed the design:
F-12's coverage framing was abandoned on the evidence in §1, not on preference.

**6.2 — ARM B IS DEMOTED TO DESCRIPTIVE, AND THIS IS AN ERROR I MADE.** The brief mandated a
circularity assessment before testing. Carrying it out required computing
ρ(coverage rate, Nöldeke phase) inside the clean window — **which is the outcome of the very test
a bounded Arm B would have run.** I saw it before I could pre-register it: **+0.5774 within 1–77.**
Arm B is therefore **not pre-registrable and is reported as descriptive only**, explicitly
non-pre-registered, in the finding. It is not counted in the Bonferroni family and carries no
verdict. **The mandated confound check and the bounded test were the same computation, and I did
not notice that until after I had run it.**

**6.3 — The direction lock uses a prior I had already read.** `asbab-nuzul.md`'s 1.34× ratio was
read during Step 0, before H1's direction was fixed. The lock is *from* that anchor, declared, not
independent of it. The **shape** prediction (§3.1) is the part not anchored in any prior
measurement of this channel.

**6.4 — A prior number is refuted, and it is the one I locked direction from.**
`asbab-nuzul.md` §2.1 reports **156 ʾiḏ tokens** (106 Meccan + 50 Medinan) from a string match
requiring word-initial space-preceded `إذ`. **QAC gives 239** for `LEM:<i*`. That is a **35%
undercount**, consistent with the string rule missing prefixed forms (وإذ, فإذ). The 1.34× ratio
therefore rests on 65% of the tokens and **its phase split may not survive recount** — which is
precisely why the direction is locked as a *prediction to be tested*, not as an established fact.
The re-count is reported whatever it does to the ratio.

**6.5 — Channel choice.** ʾiḏ was chosen over *yasʾalūnaka*/*yastaftūnaka* on **power, before
seeing any phase-conditioned result**: the question-formula family has ~15 tokens corpus-wide,
which cannot support a surah-level test. ʾiḏ has 239. The trade is stated in §2.1: the
question-formula is the *cleaner* occasion marker and the weaker instrument; ʾiḏ is the reverse.
**Had ʾiḏ been chosen after seeing that it worked, this entry would be the tell. It was chosen on
token count.**

**6.6 — Length was not locked to one variable.** All three run; worst governs; dominant named.
§1.3 shows why this matters here specifically: on the coverage channel, verse count and mean verse
length disagree in sign.

**6.7 — No hand-assigned list is used in Arm A.** The extraction is a QAC lemma match, machine-
reproducible from a hash-verified file. The only proxy in this finding is the al-Wāḥidī/Sufi
classifier of §1.2, whose ambiguous fraction (31.5%) is declared, and which is used **only
descriptively**.

**6.8 — Register labels are NOT used.** Per `AUDIT-REGISTER-PHASE-COLLINEARITY.md`, legal is 0
Meccan/15 Medinan and 37–57% of surahs contribute zero permutable information against phase. **No
arm of this pre-registration stratifies on register**, so the coarsening deciding-parameter does
not arise. The declared deciding parameter is the length channel (§4).

---

## 7. WHAT WOULD FALSIFY THIS

- H1 or H2 wrong-signed → **NULL**, and the anchors in §3 are wrong about this channel.
- S2 failing (a live Meccan-internal gradient) → **H-NEW-3070's step claim does not generalise.**
- Both H1 and H2 passing *only* at L0 and failing at L3 → the effect is mean-verse-length, and
  §1.3's diagnosis of the coverage channel extends to the textual channel too.
