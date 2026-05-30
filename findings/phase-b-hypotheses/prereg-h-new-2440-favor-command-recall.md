---
finding: H-NEW-2440
title: Favor→Command lexical-recall census — does a divine-favor root re-surface in a later command/prohibition within the same surah more than chance?
type: pre-registration (direction-locked, written BEFORE computation)
date: 2026-05-30
author: Waiel Al-Shujaa
seed: 20260509
nperm: 10000
status: LOCKED
---

# H-NEW-2440 — Favor→Command Lexical-Recall Census

## 0. Provenance of the seed

Q093-F-01 Arm B (MASTER-FINDINGS-LEDGER §10.116): in al-Ḍuḥā the root **ytm** ("orphan")
uniquely bridges the favor-block (v6: *a-lam yajidka yatīman* — "did He not find you an
orphan…") and the command-block (v9: *fa-ammā l-yatīma fa-lā taqhar* — "so as for the
orphan, do not oppress [him]"). Ibn Kathīr (*Tafsīr al-Qurʾān al-ʿaẓīm*, ad Q 93) maps
the favor verses to the command verses pairwise (v6↔v9 / v7↔v10 / v8↔v11), but **only
the orphan pair is lexically (root-) realized** — the v7↔v10 (*ḍāll*↔*sāʾil*) and
v8↔v11 (*ʿāʾil/aghnā*↔*niʿma*) pairs are conceptual, not lexical.

**This file generalizes that single observation into a corpus-wide GENERATOR + null test.**
A recurring Quranic rhetorical device — call it **favor→command lexical recall** — is
hypothesized: God recounts a past benefaction (the *taʿdīd al-niʿam* register, e.g.
*wajadaka / ātaynā / hadā / anʿamnā*), then issues a command/prohibition whose object or
key content word **re-uses a root from the favor block**, so that the command is lexically
anchored in the grace it answers. al-Ḍuḥā's *ytm* is the seed; the test asks whether the
device is a real, non-random structural feature of the corpus.

## 1. Hypothesis (DIRECTION-LOCKED)

**H1 (LOCKED, one-sided, positive):** Within surahs, the number of *favor→command lexical
recall pairs* — a content root that appears in an earlier **favor verse** (carrying a
past-tense divine-favor verb) and **re-appears** in a later **command verse** (imperative
or prohibition) within a bounded verse window — **EXCEEDS** the count produced by a
within-surah verse-order shuffle null.

Locked direction: **observed recall-count > null recall-count** (one-sided upper tail).
A reversed result (observed < null, i.e. canonical verse order *suppresses* favor→command
recall relative to shuffle) is a **pre-commit violation**, published as NULL with full
prominence.

**H2 (descriptive, no direction):** Report the full roster of favor→command recall pairs.
**al-Ḍuḥā ytm (93: v6→v9) MUST appear** in the roster, else the operationalization has
failed to capture its own seed (a validity check, not a hypothesis test).

## 2. Operationalization (LOCKED before computation)

### 2.1 Data & rules-tuple
- Text: `quran-text/quran-no-tashkeel.json` (verse inventory, region label).
- Morphology: `data/morphology/quranic-corpus-morphology-0.4.txt` (QAC v0.4).
- Rules-tuple: `(no-tashkeel, QAC-root + QAC-POS/aspect/mood, segment-level, basmala-not-counted, Hafs-Kūfan, Mashriqi)`.
- All roots = QAC `ROOT:` field of STEM segments. POS/aspect/mood = QAC `POS:`, `PERF/IMPF/IMPV`, `MOOD:JUS`, person tags (`1S,1P,3MS,3MP,2MS,2MP,…`), `PASS`.

### 2.2 Favor verse (past-tense divine action)
A verse V is a **favor verse** iff it contains ≥1 STEM verb segment that is:
- `POS:V`, aspect `PERF`, NOT `PASS`, AND
- person ∈ {`1S`,`1P`,`3MS`,`3MP`} (divine subject: "I/We/He did" — the register of
  *anʿamtu / ātaynā / wajadaka / hadā*), AND
- root ∈ **FAVOR_LEXICON** (locked below).

**FAVOR_LEXICON** (locked, 28 roots — the *taʿdīd al-niʿam* benefaction verbs;
each gloss is the divine-act sense):

| root | verb | gloss |
|---|---|---|
| wjd | wajada | found (you an orphan…) |
| Aty | ātā | gave/granted |
| nEm | anʿama | bestowed favor |
| hdy | hadā | guided |
| jEl | jaʿala | made/appointed |
| xlq | khalaqa | created |
| rzq | razaqa | provided sustenance |
| nzl | anzala/nazzala | sent down |
| swy | sawwā | fashioned/proportioned |
| Elm | ʿallama | taught |
| Erf | ʿarrafa | made known |
| fDl | faḍḍala | favored/preferred |
| whb | wahaba | granted (a gift) |
| njw | najjā | delivered/saved |
| njy | anjā | rescued |
| fkk | fakka | freed (a neck) |
| $rH | sharaḥa | expanded (the breast) |
| rfE | rafaʿa | raised |
| Hml | ḥamala | carried/bore |
| wDE | waḍaʿa | laid down (the burden) |
| xff | khaffafa | lightened |
| Awy | āwā | sheltered |
| gny | aghnā | enriched |
| ktb | kataba | prescribed/decreed (as mercy) |
| byn | bayyana | made clear |
| sbg | asbagha | lavished (favors) |
| msk | amsaka | held back (the sky) |
| Hyy | aḥyā | gave life |

Rationale for a *locked lexicon* (rather than "any PERF divine-person verb"):
a blanket past-divine-person rule is dominated by **qāla** "he/they said" (892),
**kāna** (792), **kafara/āmana/jāʾa** (human/disbeliever/event verbs) which are NOT
benefactions; including them would manufacture noise unrelated to the *favor* register.
The lexicon is fixed here, before the count, and is **not tuned after seeing results**.
The al-Ḍuḥā seed verbs (wjd, hdy, Awy, gny) are all members.

### 2.3 Command verse (imperative / prohibition)
A verse V is a **command verse** iff it contains ≥1 STEM verb segment that is either:
- `POS:V` + `IMPV` (imperative: *qul, ḥaddith, iʿbudū…*), OR
- `POS:V` + `IMPF` + `MOOD:JUS`, 2nd-person (`2MS/2MP/2FS/2FP/2MD`), immediately
  preceded (within the prior 2 segments of the same verse) by a `POS:PRO` segment — the
  prohibitive **lā al-nāhiya** (*lā taqhar, lā tanhar*).

### 2.4 Recall pair
For an ordered pair of verses (V_f, V_c) **in the same surah** with V_f a favor verse,
V_c a command verse, and **V_f's verse-number < V_c's verse-number** and
**(V_c − V_f) ≤ W** (window), a **recall** occurs for every content root R such that:
- R appears (as a STEM `ROOT:`) in V_f AND in V_c, AND
- R is **content-bearing**: POS ∈ {N, PN, ADJ, V, DER-noun} — excludes particles, and
- R ∉ **STOPROOTS** (locked: `kwn` "to be", `qwl` "to say", function-heavy roots that
  co-occur trivially): {kwn, qwl, llh-particles}. (The divine-name root `Alh` is NOT a
  stop-root — but it is a PN that recurs everywhere; reported but flagged.)

**Window W = 8 verses** (locked primary). al-Ḍuḥā v6→v9 = gap 3, well inside W=8.
A pericope-internal device should operate at short range; W=8 is a generous pericope.
MW-3 robustness variants: W=4 (tight pericope) and W=∞ (whole-surah), reported.

**Recall-pair count** = number of distinct (surah, R, V_f, V_c) tuples meeting all
conditions. A surah-level secondary count = distinct (surah, R) with ≥1 qualifying
(V_f,V_c) — the "recall-event" count (deduplicates a root recalled across many verse
pairs). **Primary test statistic = total recall-event count (surah, R) over the corpus.**

### 2.5 Null model (LOCKED)
**Within-surah verse-order shuffle.** For each surah, the multiset of verses (each verse
keeps its exact content = its set of {favor-flag, command-flag, content-roots}) is
randomly **re-ordered**; verses are then re-numbered 1..n in the shuffled order, and the
recall-event count is recomputed under the SAME window/direction rules. This destroys the
**favor-before-command ordering** and the **adjacency window** while exactly preserving
each surah's verse contents, its number of favor verses, command verses, and root
inventory. 10,000 permutations, seed = 20260509. Corpus null statistic = sum over surahs
of recall-events per permutation.

p_value = (#{null ≥ observed} + 1) / (NPERM + 1), one-sided upper tail (locked direction).
z = (observed − mean_null) / sd_null.

### 2.6 Success / failure criteria
- **CONFIRMED:** observed > null, p < 0.05 (single locked test, k=1; no Bonferroni family —
  but the 3 window variants are reported as MW-3 robustness, with the W=8 primary carrying
  the verdict), AND the al-Ḍuḥā ytm pair is present in the roster (validity check passes).
- **NULL / PRE-COMMIT VIOLATION:** observed ≤ null (reversed or no excess) → published as
  NULL with full prominence; the favor→command recall device is then a *post-hoc
  showcase* (al-Ḍuḥā is real but does not generalize as an above-chance corpus device).
- **DIRECTIONAL:** observed > null but 0.05 ≤ p, or validity check fails.

### 2.7 Replication (MW-5)
Re-run the null with seed = 20260601; require the same verdict sign.

### 2.8 Controls / threats
- **MW-6 (instrument-control):** a *command→favor* (reverse-order) recall count is also
  computed (favor verse AFTER command verse, same window). This is the locked-direction
  control: the device predicts forward (favor→command) recall should beat the null by
  MORE than the reverse-order recall does (the asymmetry is the signature). Reported, not
  the primary verdict.
- The null preserves favor-count, command-count, and root inventory per surah, so the test
  isolates the **ordering+window** structure, not lexical richness.
- **STOPROOTS** locked above to prevent trivial co-occurrence (the copula/“said” roots).

## 3. What would falsify the hypothesis
- Observed recall-events ≤ null mean (the canonical order does not place favor roots before
  commands more than a shuffle): NULL.
- al-Ḍuḥā ytm absent from roster: operationalization invalid → DIRECTIONAL at best.
- Effect vanishes under W=4 AND W=∞: window-fragile, demote.

## 4. Pre-registered roster expectation
al-Ḍuḥā (93) ytm v6→v9 present. Other expected candidates (NOT locked, exploratory):
Banī-Isrāʾīl favor-and-covenant passages (Q 2), the *udhkurū niʿmata* formulae, al-Balad
(Q 90) *fakk raqaba*, al-Sharḥ (Q 94) *sharaḥ*. The roster is descriptive output.

*Bismillāhi al-Raḥmāni al-Raḥīm.*
