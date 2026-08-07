---
id: H-NEW-2870
title: "Pre-registration — Is the fāṣila defined at PAUSAL phonology rather than citation form?"
date: 2026-08-07
author: Waiel Al-Shujaa
status: LOCKED — written and SHA-256'd BEFORE any test statistic was computed
family: RHYME-2026-08-07
frontier_item: F-16
parent_1: H-NEW-2240 (fāṣila assonance taxonomy — computed at pausal form only)
parent_2: H-NEW-2080 (rāwī-level rhyme scan — computed at min-tashkeel skeleton only)
method_parent_1: H-NEW-2690 (validated phonemiser / pausal reduction; 3/3 muʿallaqāt meters)
method_parent_2: H-NEW-2730 (within-corpus re-cut control — "no baseline text at all")
method_parent_3: findings/UNIT-DRIFT-DEFECT.md
seed: 20260509
seed_replication: 20260519
n_perm: 10000
n_recut: 2000
bonferroni_k: 6
alpha_bonferroni: 0.008333
---

# Pre-registration — H-NEW-2870

**Nothing here may be amended after the SHA-256 is embedded in `scripts/h-new-2870.py`.**
Directions are locked in §7, decision rules in §8, reporting order in §9, failure conditions
in §12. The runner's verdict logic must be diffed against §8 before any verdict is declared —
`STATE-OF-THE-PROJECT-2026-08-07.md` §4.4.

---

## 1. The question, and why it is being asked today

Classical Arabic recitation applies *waqf* (pausal) rules at a stopping place: the word-final
short vowel and the tanwīn drop, tanwīn fatḥ is realised as a long *ā*, tāʾ marbūṭa is heard as
*hāʾ*. **The hypothesis is that the Qurʾān's rhyme is defined at that pausal form and not at
the fully-vocalised citation (waṣl) form** — that verse-ends which do *not* rhyme when read
with full iʿrāb *do* rhyme once pausal reduction is applied.

### 1.1 Why this question and not another one

Every collapse recorded in `findings/UNIT-DRIFT-DEFECT.md` has the same shape: a **density
divided by a unit count**, compared across an ordering or grouping whose unit size drifts.
The measure defended here is **categorical, not a ratio**. Two adjacent verse-ends either fall
in the same rhyme class under a given phonological convention or they do not; there is no
denominator that can drift. Screen A of the unit-drift defect is not met, so the defect
cannot reach this statistic. That is the reason this target was chosen.

**This does not make the test safe.** It relocates the risk, and §1.2 names where it goes.

### 1.2 The confound that decides this finding, named before any computation

Pausal reduction **destroys information**. `ʿalīmun`, `ʿalīmin` and `ʿalīma` all become
`ʿalīm`. Fewer distinct verse-final forms means more coincidental matches **arithmetically**,
with no composition involved whatever. A rise in rhyme agreement under pausal reduction is
therefore the *expected* consequence of any lossy map, and by itself it is evidence of
nothing.

**The whole test is the control that holds the number of classes fixed** (§6.2, null N1). It
is built first and it is reported first (§9). If the observed pausal agreement sits inside
that null, the finding is that the gain is arithmetic, and that is what leads the write-up.

F-16 states the same warning in the frontier map: *"This is close to a definitional
restatement… The finding is only interesting as a magnitude and as a localisation of
residuals."* This pre-registration accepts that framing in full.

---

## 2. Relation to prior work — what is NOT being re-done

- **H-NEW-2240** built a 69-class fāṣila assonance taxonomy and established at law strength
  that surahs are rhyme-**homogeneous** (mean within-surah class entropy 1.071 nats, below the
  entire 10,000-permutation null). It computed **only at the pausal form**, on
  `quran-min-tashkeel.json`, and its own honest-limits §7 names this as an open choice:
  *"Pausal convention is a choice… a waṣl (continuous) definition would reclassify some
  endings."* **H-NEW-2870 is that limit, executed.** The homogeneity result is not re-tested.
- **H-NEW-2080** scanned the verse-final rāwī letter on the min-tashkeel skeleton (nūn+mīm =
  60.76 %, 18 perfect monorhymes). A consonantal skeleton **cannot** express the citation/pausal
  contrast, because the final short vowel is not written in it. Not re-tested; cited only.
- **H-NEW-2690/2730** supply the phonemiser and pausal reduction reused here (§4). Their
  scansion claims are not touched.

**New here:** the citation (waṣl) form has never been computed in this repository, and no
delta between conventions has ever been measured.

---

## 3. Frozen inputs (SHA-256 verified at runtime; mismatch is fatal)

| path | SHA-256 | role |
|:--|:--|:--|
| `quran-text/quran-full-tashkeel.json` | `382a7341300602ec8b366316d4bbe2a44955c2bf984d395bdd82dae6110b6715` | primary text — the only on-disk copy carrying the final short vowels this test requires |
| `data/alt-text/quran-uthmani-txt.txt` | `e5e7e54988877d6164832d55435135a563b9cfc249e0c8efd73e9e7f23231db8` | Tanzil Uthmani v1.1 — independent encoding, used **only** for the orthography gate in §4.1 |
| `data/baseline-corpora/raw/muallaqa-imru-al-qais.txt` | `06f05f6a299d989fcaf330f43f7fba9116b373f94096d38ec07df71432f59c14` | positive control |
| `data/baseline-corpora/raw/muallaqa-zuhayr.txt` | `9a8aac1838323aaa65f916f597ec38c842b74eed77ce44f53c2932b52e6610c2` | positive control |
| `data/baseline-corpora/raw/muallaqa-amr-bin-kulthum.txt` | `d93a81bd2095c7db00417650f883c834077fac12668e50002c8b35f26e2ef720` | positive control |
| `data/baseline-corpora/raw/bukhari-noquran.txt` | `0169b60de7585a51fc340161488534c4d909370c3dcc8951ca2ae3818c44a100` | negative control (see §6.5 — **partially blocked**) |
| `data/baseline-corpora/raw/jahiz-hayawan.txt` | `419095484df4e315eba889d38a9c2f6edff55c2f10f481ed9ad024e07bbff0cd` | negative control (see §6.5 — **partially blocked**) |

---

## 4. The instrument

### 4.1 Orthography gate — RUN AND REPORTED BEFORE ANY TEST STATISTIC

`quran-full-tashkeel.json` does **not** encode tanwīn with the standard Unicode marks
throughout. It uses three codepoints whose Unicode *names* do not describe their function in
this text:

| codepoint | Unicode name | function in this text |
|:--|:--|:--|
| U+0657 (ٗ) | ARABIC INVERTED DAMMA | **tanwīn fatḥ** (single-mark idghām/ikhfāʾ form) |
| U+065E (ٞ) | ARABIC FATHA WITH TWO DOTS | **tanwīn ḍamm** |
| U+0656 (ٖ) | ARABIC SUBSCRIPT ALEF | **tanwīn kasr** |

These carry **6,643 marks corpus-wide against 1,911 for the standard doubled marks** — i.e.
**78 % of all tanwīn in this file is encoded in the non-standard set.** Since tanwīn is
precisely what pausal reduction removes, misreading these would silently void the entire test.

**Gate (must pass, else abort):** align the 6,236 verses 1:1 with the Tanzil Uthmani text and
verify that every word carrying U+0657 / U+065E / U+0656 carries the corresponding standard
mark (ً / ٌ / ٍ) in Tanzil, and vice-versa for the doubled marks. **Required: ≥ 99 % agreement
on each of the six marks, with the counts reported.** If the gate fails, report the instrument
as broken and stop.

> **Defect inherited from the method parent, recorded here because this test must not repeat
> it.** `scripts/h-new-2690.py`'s `normalize()` places U+0656, U+0657 and U+065E in its `DROP`
> set. That silently deletes **6,643 tanwīn** — 78 % of the corpus's tanwīn — before
> syllabification. H-NEW-2870 does **not** inherit that `DROP` set; it maps the three marks to
> their standard equivalents before phonemisation. This is a correction to the reused
> machinery, not a new modelling choice, and it is declared here rather than discovered later.

### 4.2 Phonemiser

Reused from `scripts/h-new-2690.py` §2.1 (`normalize`, `phonemes`) — the machinery whose
scanner recovered **3/3 muʿallaqāt meters at 0.771 per-bayt accuracy**, with exactly two
changes, both declared here:

1. U+0656 → ٍ, U+0657 → ً, U+065E → ٌ **before** normalisation (§4.1).
2. U+0670 (superscript alef) and U+06E1 (small high dotless head of khah = sukūn) handled as
   in the parent.

Output is a list of items `('C', x)`, `('V', v)`, `('VV', v)`.

### 4.3 The rime extractor — the classical ridf / rawī / majrā, stated as an algorithm

Applied to the **unit-final orthographic word** only. Trailing standalone annotation tokens
(sajda sign ۩ and bare mark tokens) are dropped first.

Given the phoneme list `ph`:

1. **majrā** — if the last item is a *short* vowel, remove it and hold it as the majrā;
   otherwise majrā is empty.
2. **coda** — from what remains, take the maximal run of trailing consonants (may be empty).
3. **nucleus** — the item immediately preceding the coda. If the coda is empty (the word ends
   in a long vowel), the nucleus is that long vowel and the rime is **open**.
4. **RIME = nucleus + coda + majrā**, rendered as a string with vowel length marked.

Worked examples, locked (these are hand-checkable and are part of the §4.4 gate):

| word | convention | phonemes | RIME |
|:--|:--|:--|:--|
| ٱلۡعَٰلَمِينَ *al-ʿālamīna* | citation | a: l a m iː n a | **īna** |
| ٱلۡعَٰلَمِينَ | pausal | a: l a m iː n | **īn** |
| نَسۡتَعِينُ *nastaʿīnu* | citation | … ʕ iː n u | **īnu** |
| أَحَدٌ *aḥadun* | citation | a ħ a d u n | **un** |
| أَحَدٌ → *aḥad* | pausal | a ħ a d | **ad** |
| ٱلصَّمَدُ *al-ṣamadu* | citation | … m a d u | **adu** |
| ٱلصَّمَدُ → *al-ṣamad* | pausal | … m a d | **ad** |
| هُدٗى *hudan* | citation | h u d a n | **an** |
| هُدٗى → *hudā* | pausal | h u d aː | **ā** (open) |

This is the classical qāfiya skeleton (ridf/tawjīh + rawī + majrā) and it has **the same
structural depth under both conventions**, which is what makes the comparison fair. A
fixed-character-window definition would not: it would read three phonemes deep under one
convention and two under the other.

### 4.4 Instrument validation gate — REPORTED BEFORE ANY TEST STATISTIC

The pausal-form classes must reproduce H-NEW-2240's published, independently-derived,
hand-validated results. Required, all six:

| surah | H-NEW-2240 published | required here |
|:--|:--|:--|
| Q 18 al-Kahf | 110/110 open `-ā` | 110/110 open rime `ā` |
| Q 112 al-Ikhlāṣ | 4/4 `-ad` | 4/4 rime `ad` |
| Q 108 al-Kawthar | 3/3 `-ar` | 3/3 rime `ar` |
| Q 114 al-Nās | 6/6 `-ās` | 6/6 rime `ās` |
| Q 1 al-Fātiḥa | endings in `-īm`/`-īn` | all 7 rimes in {īm, īn} |
| Q 55 al-Raḥmān | dominated by `-ān` | modal rime = `ān` |

**If fewer than 6/6 pass, report the instrument as broken and stop.** No headline number is
computed before this gate is printed.

---

## 5. The conventions (rules-tuple)

Four, applied to the unit-final word. **All four are reported; the primary family is C vs P1
and C vs P2.**

| tag | name | rule |
|:--|:--|:--|
| **C** | citation / waṣl | as written, with the final short vowel and tanwīn realised in full |
| **P1** | pausal — minimal | drop the word-final short vowel; drop tanwīn ḍamm and tanwīn kasr entirely; realise **tanwīn fatḥ as long ā** (waqf bi-l-alif). Nothing else changes. |
| **P2** | pausal — full | P1 **plus** tāʾ marbūṭa → *h*, **plus** a word-final hamza preceded by a long vowel retained as a consonant coda (the *madd* + hamza ending) |
| **P3** | pausal — strict | P1 but tanwīn fatḥ dropped **without** the compensatory ā (bare consonant). Bracketing tuple: a deliberately *incorrect* account of Arabic waqf, included only to bound how much of the effect rests on the −an → ā rule. |

Rationale for putting the −an → ā rule inside the *minimal* tuple: dropping tanwīn fatḥ
without its alif is not what waqf does in any reading. P3 exists so that the reader can see
what the answer would have been under the wrong rule, per the standing finding that **the
rules-tuple can decide the answer** and that variants can rehabilitate as readily as demote.

---

## 6. Statistics, nulls and controls

### 6.1 The observable

For a text partitioned into ordered units within blocks (surahs / poems / matched cuts), over
all **adjacent within-block unit pairs**:

- **A(conv)** = (adjacent pairs whose two units share a RIME class under `conv`) / (all
  adjacent pairs). For the Qurʾān: 6236 − 114 = **6122 pairs**.
- **Δ(P) = A(P) − A(C)** — *the headline statistic.*
- **K(conv)** = number of distinct RIME classes. **K_eff(conv)** = exp(Shannon entropy of the
  class distribution) — the effective class count, which is the honest one because it is
  insensitive to singleton classes.
- **collapse factor** = K(C)/K(P) and K_eff(C)/K_eff(P).

### 6.2 N1 — the matched-collapse null. **THE DECISIVE CONTROL. BUILT FIRST.**

*Question:* does pausal reduction raise agreement for any text simply because it collapses
distinctions?

*Construction:* let the citation form partition the units into `M` distinct RIME types with
verse-counts `m_1 … m_M`, and let the observed pausal form have `K` classes with verse-counts
`n_1 … n_K`. Draw a **random surjection** ψ from the M citation types onto K blocks such that
the induced block verse-counts match `n_1 … n_K` as closely as a randomised greedy fill
against those targets allows. Compute A(ψ). Repeat **10,000** times, seed 20260509.

This null holds **fixed**: the number of classes, the class-size profile in verses, and every
agreement the citation form already produces (two units with the same citation type always
land in the same block). It destroys **only** the phonological identity of the merges — which
citation endings the waqf rules actually put together.

- If **A(P) > null** → the specific mergers waqf performs are the ones that create rhyme.
- If **A(P) inside the null** → the gain is arithmetic. *That is the finding, and it leads.*

Reported alongside: the **chance floor** Σᵢpᵢ² under the pausal marginals (analytic), and the
**map-violation rate** — the fraction of units whose pausal class is not a function of their
citation class (waqf can *split* a citation class: citation `an` goes to pausal `ā` for
*hudan* but stays `an` for *ʿan*). If that rate is large the null is ill-posed and must be
reported as such.

### 6.3 N2 — pseudo-fāṣila re-cut. Within-corpus, no baseline text.

The H-NEW-2730 move: *re-cut this corpus's own material and use no baseline text at all.*

Within each surah, concatenate all words into a stream and re-cut it into the **same number of
units** whose lengths are a **random permutation of that surah's own verse lengths**. The
length profile, the unit count, the vocabulary, the orthography and the vocalisation are
identical to the real text; **only the boundary positions are not composed.** Compute Δ on the
re-cut. **2,000** re-cuts, seed 20260509. Report the rate at which a re-cut boundary
coincidentally lands on a true verse end.

### 6.4 Positive control — pre-Islamic poetry

The three muʿallaqāt whose **line-final** words are vocalised at ≥ 0.9 (measured before
locking; see §11): Imruʾ al-Qays 0.963, Zuhayr 0.939, ʿAmr b. Kulthūm 0.924. The other four
are 0.000–0.494 and are **excluded by this pre-declared threshold**, not by inspection of any
result. These are the same three H-NEW-2690 used.

Poetry is monorhymed by construction, so it should **already rhyme at the citation form**:
pausal reduction should not need to rescue it. Prediction locked in §7.

**Ceiling caveat, stated before running:** if A(C) for poetry is near 1.0 then Δ cannot be
large for arithmetic reasons, and a small Δ is not independent evidence. The **level** A(C) is
therefore the primary reportable for this arm and the delta is secondary.

### 6.5 Negative control — prose. **PARTIALLY BLOCKED, DECLARED BEFORE RUNNING.**

Measured before locking: `bukhari-noquran.txt` carries **0** harakāt over 2,056,880 Arabic
characters; `jahiz-hayawan.txt` carries **0** over 1,422,487. `bukhari.txt` carries 13,204
over 2,182,373 (0.6 %, scattered).

**Consequence: the citation form is not recoverable for either prose baseline, so Δ is not
computable for prose.** No amount of method can extract a final short vowel that was never
written, and automatic vocalisation would substitute a model's output for data.

This is stated now, in advance, so it cannot later be presented as a result. What **is**
computable and will be reported:

- **A(written)** for prose, on units length-matched to the Qurʾān's verse-length profile, as a
  *level* comparison against the Qurʾān's A(P1). The unvocalised written form is
  approximately the pausal skeleton, so this is the nearest available analogue.
- It is **not** a control on the delta, and will not be described as one.

Prose units: split on `[.؟!\n]`, keep units of ≥ 3 words, then draw units matching the
Qurʾān's per-surah verse-count and verse-length profile (H-NEW-2730's matched-partition
construction), 200 cuts, seed 20260509.

---

## 7. Directions — LOCKED

| # | direction | locked prediction |
|:--|:--|:--|
| **D1** | Δ(P1) > 0 and Δ(P2) > 0 for the Qurʾān | pausal reduction **increases** adjacent rhyme agreement |
| **D2** | **A(P) > N1 matched-collapse null** | the gain is **not** explained by class collapse alone |
| **D3** | Δ(Qurʾān) > Δ(pseudo-fāṣila re-cut) | the gain is a property of the **composed** boundaries |
| **D4a** | A(C) for poetry > A(C) for the Qurʾān | poetry already rhymes at citation form |
| **D4b** | Δ(Qurʾān) > Δ(poetry) | poetry does not need pausal reduction to rhyme |
| **D5** | K(C) > K(P) | pausal reduction collapses classes (near-certain; stated so its **magnitude** is on the record before the delta) |

**A reversal of D1 or D4a would be a major negative and is reportable as such.**

---

## 8. Decision rules

Primary family: **{D2, D3, D4b} × {P1, P2} = 6 tests.** Bonferroni **k = 6**,
**α = 0.05/6 = 0.008333**, one-sided in the locked direction.

- **D2** — p = (1 + #{null A ≥ observed A(P)}) / (1 + 10000).
- **D3** — p = (1 + #{re-cut Δ ≥ observed Δ}) / (1 + 2000). Resolution 0.0005 < α. ✔
- **D4b** — p from a 10,000-permutation label-exchange test on the pooled pair set.

**Verdict grid, locked:**

| outcome | verdict |
|:--|:--|
| D2 passes under **both** P1 and P2, **and** D3 passes under both | **PASS** — the fāṣila is defined at pausal phonology and the effect is compositional |
| D2 passes under both but D3 fails | **PARTIAL** — the merges are phonologically specific but not localised to composed boundaries |
| **D2 fails under either P1 or P2** | **NULL — the gain is arithmetic.** This is the headline and it leads the write-up regardless of every other result |
| D1 reverses | **REVERSED** — report as a major negative |

D5, the prose level comparison, P3, and the per-surah table are **descriptive** and gate
nothing.

**The runner's verdict logic will be diffed against this section, printed, before any verdict
is declared.**

---

## 9. Reporting order — LOCKED

The write-up must present, in this order:

1. The **orthography gate** (§4.1) and the **instrument gate** (§4.4).
2. The **class-collapse magnitude** — K(C), K(P), K_eff, the collapse factor (§6.1, D5).
3. The **N1 matched-collapse null** and D2 (§6.2).
4. Only then the headline Δ.
5. The three control texts, with §6.5's blocker stated in the prose row itself.
6. The per-surah table and exceptions.

This order is locked because presenting Δ before the collapse magnitude would misrepresent an
arithmetic effect as a compositional one.

---

## 10. Classical anchor — **UNVERIFIED ON DISK, declared before running**

The brief for this test named `data/literature/classical-tafsir/suyuti-al-itqan-fi-ulum-al-quran-english.pdf`
(nawʿ 27, waqf) as the anchor. **It is not there.** Checked before locking:

- The Itqān PDF is Muneer Fareed's **partial** translation — its own introduction describes it
  as *"some twenty chapters of excerpts."* Full-text extraction yields 18,853 lines; a search
  for the waqf technical vocabulary (*waqf tāmm*, *kāfin*, *ḥasan*, *ibtidāʾ*) returns **no
  section on pauses**. The nawʿ is absent from this translation.
- `zarkashi-al-burhan-fi-ulum-al-quran.pdf` (1,568 pp.), which contains al-Zarkashī's own nawʿ
  on *al-waqf wa-l-ibtidāʾ*, is a **scanned image with no text layer** — `pdftotext` returns 0
  characters. No page can be cited from it.
- No primary waqf source (Ibn al-Jazarī *al-Nashr*, al-Dānī) exists on disk in citable form.

**Therefore no page citation is given for the waqf tradition in this finding.** The *waqf*
rules are stated as the standard recitational convention and the claim is carried by the
measurement, not by an authority. The anchor is recorded as an acquisition need. **No citation
will be invented.**

---

## 11. Garden of forking paths — everything inspected before this pre-reg was locked

Declared in full, per `feedback_specialist_judgment_overrides_team_lead_method`:

1. Read `STATE-OF-THE-PROJECT-2026-08-07.md`, `findings/UNIT-DRIFT-DEFECT.md`, FRONTIER-MAP
   F-16, H-NEW-2690, H-NEW-2730, H-NEW-2240, H-NEW-2080 and the 2240/2690 scripts.
2. **Corpus character census** of `quran-full-tashkeel.json` — all codepoints, and the
   marks appearing in verse-final words. Established the U+0657/065E/0656 problem (§4.1).
3. **Tanwīn mark verification** against Tanzil, 1:1 verse alignment. This became the §4.1 gate.
   Its result was seen before locking and is stated in §4.1; it is an **encoding fact**, not a
   test statistic, and no direction depended on it.
4. **Tashkeel density** of all 39 baseline-corpus files. This produced the §6.5 blocker and the
   §6.4 ≥ 0.9 line-final-vocalisation threshold. **The three poems were selected by that
   threshold, which was fixed before any rhyme statistic was computed**, and they are the same
   three the method parent used.
5. Searched the Itqān and Burhān PDFs for the waqf nawʿ (§10).
6. **No rhyme-class, agreement, delta, or null value of any kind has been computed.** The
   RIME extractor of §4.3 has not been run on any text.

---

## 12. Failure conditions — what makes this finding wrong

- **The orthography gate (§4.1) below 99 %** → instrument broken, stop.
- **The instrument gate (§4.4) below 6/6** → instrument broken, stop.
- **A(P) inside the N1 null** → the effect is arithmetic; NULL verdict, reported first.
- **Map-violation rate high** → N1 is ill-posed; report the null as uninterpretable rather
  than reporting a p-value from it.
- **The pseudo-fāṣila re-cut reproducing Δ** → the delta is a property of Arabic word-final
  morphology, not of the fāṣila.
- Residual limits that no available data can remove: the prose delta (§6.5); the absence of a
  citable classical anchor (§10); the fact that the "citation form" here is the Ḥafṣ mushaf's
  written iʿrāb, which is itself a recitational tradition and not a neutral baseline.

---

## 13. Run discipline

Immutable run directory `runs/h-new-2870/<UTC>/`, `os.makedirs(exist_ok=False)`, every output
opened with mode `'x'`, manifest paths repo-relative, checkpoints written **outside** the run
directory. **No run directory is ever deleted.** Pre-reg SHA-256 embedded as a literal in the
runner and verified at runtime. Replication at seed 20260519 for every permutation test.

*Bismillāhi al-Raḥmāni al-Raḥīm.*
