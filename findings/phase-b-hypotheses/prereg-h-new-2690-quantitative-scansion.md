---
id: H-NEW-2690
title: Pre-registration — Real quantitative scansion: does the Qurʾān occupy a distinct prosodic region, or merely a distinct length distribution?
date: 2026-08-07
author: Waiel Al-Shujaa
status: LOCKED — written and SHA-256'd BEFORE the scanner was ever applied to the Qurʾān
family: SCANSION-2026-08-07-A
seed: 20260509
seed_replication: 20260519
n_perm: 10000
bonferroni_k: 3
alpha_bonferroni: 0.016667
supersedes_scope_of: H-NEW-48
---

# Pre-registration — H-NEW-2690


> ## ⛔ CORRECTION NOTICE — 2026-08-07: the iʿjāz anti-twin is REVERSED under a matched control
>
> **The arithmetic reproduces** — an independent surface-instrument rebuild returns
> r = −0.8700 against the published −0.8643. What did not survive is the inference.
>
> - **Both prose baselines are *more* anti-twinned than this corpus.** Cut into 114
>   pseudo-surahs on this corpus's own verse-count and verse-length profile, al-Bukhārī
>   averages **r = −0.9107** (this corpus at the **14th percentile**, 172 of 200 cuts more
>   extreme) and al-Jāḥiẓ **−0.9311** (**3rd percentile**, 194 of 200). Pre-Islamic poetry
>   under a matched partition reaches **−0.8718**.
> - **H-NEW-740's Δ Fisher-z = −6.42 is an artefact of unmatched unit sizes.** It compared
>   equal 30-bayt poetry blocks to this corpus's unequal surahs (10 to 6,140 words).
>   r(d̄_content, log unit size) = **+0.956** and r(d̄_rhyme, log unit size) = **−0.838**, so a
>   *dispersed* size profile manufactures an anti-twin and equal blocks suppress it.
> - **About half the correlation is unit size.** Partialling out log unit size gives
>   **r = −0.432**; re-cutting this corpus's own verses to equal size gives **−0.338** — which
>   is indistinguishable from what H-NEW-740 measured for *poetry* (−0.48) and called the
>   genre baseline.
>
> **Honest limit, for this law specifically:** the baselines are arbitrary cuts of a
> continuous stream, not composed books, and for a **contiguity-sensitive** statistic like
> this one arbitrary cuts *preserve* local continuity and make the law *easier* for a
> baseline. The reversal is therefore **weaker evidence against the law than the percentile
> alone suggests**; the size decomposition, which uses no baseline at all, carries the weight.
>
> al-Bāqillānī's qualitative *iʿjāz al-fawāṣil* claim is **not** refuted — it was never a
> claim about correlation coefficients. What is withdrawn is its stated empirical vindication.
>
> Evidence: `findings/phase-b-hypotheses/h-new-2720-genre-control-sweep.md`
> Summary: `findings/GENRE-CONTROL-CORRECTION-2026-08-07.md`.

**Nothing here may be amended after the SHA-256 is embedded in `scripts/h-new-2690.py`.**
Directions are locked in §6. Failure conditions in §10. A reversed direction is a
pre-commit violation, published as NULL with equal prominence.

**Order of work, stated for the record.** The scanner was built and calibrated
**entirely on the poetry control corpus**, and its benchmark numbers (§4) were frozen into
this file, **before the scanner was applied to a single Qurʾānic verse**. At the time of
locking, no Qurʾānic scansion output existed.

---

## 1. The claim, and how it differs from H-NEW-48

al-Bāqillānī's *Iʿjāz al-Qurʾān* holds that the Qurʾān is **neither *nathr* (prose) nor
*shiʿr* (poetry)**.

**Prior art, stated precisely.** `h-new-48-poetic-meter.md` reports this claim as
confirmed. **It does not test it.** H-NEW-48 models each of the 16 *buḥūr* as a Gaussian
centred at μ = 1.6 × syllables_per_bayt (amendment 48-A calibrated
`LETTERS_PER_SYLLABLE = 1.6`) and compares it against **Qurʾānic verse letter-counts** by
Kolmogorov–Smirnov. Its own limitations section concedes: *"Letter-count is a proxy for
syllable-count"* and *"A more sophisticated reference would use the actual zihāf/ʿilal-
modified syllable-count distribution per meter, which requires foot-by-foot prosodic
counting beyond this test's scope."* **No CV template is ever extracted and nothing is
ever scanned.** H-NEW-48 is a comparison of *length distributions*.

A text can have a distinctive length distribution while being prosodically ordinary, and
can share a length distribution while being prosodically alien. **H-NEW-2690 measures the
thing itself**: the actual long/short syllable sequence, from the vocalised text, matched
against the al-Khalīlian foot inventory. It supersedes H-NEW-48's *scope*; it does not
re-run its test.

---

## 2. The instrument — quantitative scansion

### 2.1 Syllabification

Vocalised orthography → phoneme units → syllables, each **light `v`** (CV) or
**heavy `-`** (CVV or CVC). Locked rules:

1. Normalise NFC; delete Quranic waqf/recitation signs and tatweel
   (`U+0640`, `U+06D6`–`U+06DC`, `U+06DE`–`U+06E0`, `U+06E3`, `U+06E7`–`U+06E9`,
   `U+06EA`–`U+06ED`, `U+0653`–`U+0655`, `U+0656`–`U+065F` as listed in the script's
   `DROP` set).
2. `U+06E1` (small high dotless head of khāh) → sukūn. `U+06E5`/`U+06E6` (small wāw/yāʾ)
   → wāw/yāʾ. `U+0670` (superscript alef) → long *ā*. `آ` → hamza + *ā*. `ٱ` → alef.
3. **Encoding-variance normalisation** — three real defects found in the control corpus,
   each verified against codepoint dumps before locking:
   - `ALEF + FATḤA` → `FATḤA + ALEF` (vowel written after the alef of long *ā*).
   - `VOWEL + SHADDA` → `SHADDA + VOWEL` (shadda written after its vowel).
   - Bare unvowelled word-initial `و` / `ف` → `/wa/`, `/fa/` (proclitic conjunction
     written without its fatḥa).
4. Shadda = two consonants (gemination). Tanwīn = short vowel + `n`.
5. Matres lectionis: unvowelled `ا`/`ى` after *a*, `و` after *u*, `ي` after *i* → long vowel.
6. Syllable: C+VV → heavy; C+V+C(not followed by a vowel) → heavy; C+V → light.
7. **Final syllable of a unit forced heavy** — the standard ʿarūḍ convention at line end.

### 2.2 The 16 buḥūr

Hemistich (*miṣrāʿ*) patterns, in `v`/`-`:

| meter | pattern | meter | pattern |
|:--|:--|:--|:--|
| ṭawīl | `v--` `v---` `v--` `v-v-` | munsariḥ | `--v-` `---v` `--v-` |
| madīd | `-v--` `-v-` `-v--` | khafīf | `-v--` `--v-` `-v--` |
| basīṭ | `--v-` `-v-` `--v-` `-v-` | muḍāriʿ | `v---` `-v--` |
| wāfir | `v-vv-` `v-vv-` `v--` | muqtaḍab | `---v` `--v-` |
| kāmil | `vv-v-` ×3 | mujtathth | `--v-` `-v--` |
| hazaj | `v---` ×2 | mutaqārib | `v--` ×4 |
| rajaz | `--v-` ×3 | mutadārik | `-v-` ×4 |
| ramal | `-v--` ×3 | sarīʿ | `--v-` `--v-` `-v-` |

**This table is entered from the standard reference description of al-Khalīl's system.
No primary ʿarūḍ text is on disk to verify it against** (see §9). The positive control of
§4 is its empirical validation: if a pattern is wrong, the poets whose meter it is will
not match it.

### 2.3 Two derived measures

- **Meter identification.** Normalised Levenshtein distance between the observed string
  and each meter's hemistich pattern **doubled** (a full bayt); argmin over 16. Uniform
  substitution cost. Ties broken by the table order above. Normalised by
  `max(len(obs), len(canon))`.
- **Metricality `d_min`** — the new quantity, and the one H-NEW-48 has no analogue for.
  For a unit of length *L*, each meter's hemistich pattern is **tiled and truncated to
  exactly *L***, at **every phase** (every rotation of the pattern); `d_min` is the
  minimum normalised edit distance over all 16 meters × all phases. Tiling makes `d_min`
  **length-invariant by construction**, so it measures *pattern conformity* and cannot
  degenerate into the length proxy that H-NEW-48 measured. Verified flat across lengths
  in §4.

---

## 3. Corpora — and a severe data limitation, stated up front

**Scansion requires vocalisation. Most of the project's baseline corpora have none.**
Measured diacritics-per-Arabic-letter before locking:

| corpus | ratio | scannable? |
|:--|--:|:--|
| `quran-text/quran-full-tashkeel.json` | **0.918** | yes |
| `muallaqa-zuhayr.txt` | 0.839 | **yes** |
| `muallaqa-imru-al-qais.txt` | 0.777 | **yes** |
| `muallaqa-amr-bin-kulthum.txt` | 0.722 | **yes** |
| `muallaqa-harith.txt` | 0.205 | **no** |
| `muallaqa-labid.txt` | 0.164 | **no** |
| `muallaqa-antara.txt` | 0.068 | **no** |
| `muallaqa-tarafa.txt` | 0.031 | **no** |
| `diwan-*.txt` (all 8), `mutanabbi-diwan.txt` | **0.000** | **no** |
| `baseline-corpora/raw/bukhari.txt` | 0.006 | **no** |
| `baseline-corpora/raw/jahiz-hayawan.txt` | 0.000 | **no** |

**Consequences, accepted before locking:**
- **Only 3 of the 7 muʿallaqāt can be scanned**, covering only **2 of the 16 meters**
  (ṭawīl ×2 poets, wāfir ×1). Kāmil and khafīf ground truth is lost with Labīd, ʿAntara
  and al-Ḥārith. The positive control is therefore a **2-meter** control, not a 16-meter one.
- **Every dīwān is useless for scansion.** Zero diacritics.
- **The prose baselines used by H-NEW-48 (Bukhārī `bukhari.txt`, Jāḥiẓ) cannot be
  scanned at all.**

**The prose baseline is therefore replaced**, and this is a deliberate, disclosed
substitution: `data/literature/hadith/ahmedbaset-json/db/by_book/the_9_books/darimi.json`
— Sunan al-Dārimī, 3,406 ḥadīth, **fully vocalised at ratio 0.866**, the best-vocalised
large prose corpus on disk.

**Locked corpora and units:**

| arm | source | unit | n |
|:--|:--|:--|--:|
| Qurʾān | `quran-text/quran-full-tashkeel.json` | verse | 6,236 |
| poetry | 3 vocalised muʿallaqāt | bayt (line), diacritic-ratio ≥ 0.55, ≥ 8 syllables | 240 |
| prose | Sunan al-Dārimī `hadiths[].arabic` | sentence, split on `[.؟!]`, ≥ 8 syllables | all |

---

## 4. Positive control — FROZEN BEFORE THE QURʾĀN WAS TOUCHED

**This is the gate. It is reported first in the finding, before any Qurʾānic number.**

Ground truth: Imruʾ al-Qais = **ṭawīl**, Zuhayr = **ṭawīl**, ʿAmr b. Kulthūm = **wāfir**.

| benchmark | locked value |
|:--|:--|
| per-bayt top-1 meter accuracy (16-way; chance 6.25%) | **77.1%** (185/240) |
| per-poem plurality meter correct | **3/3** |
| per-poet: Imruʾ al-Qais / Zuhayr / ʿAmr | 68% / 97% / 72% |
| median `d_min`, poetry | **0.1429** |
| median `d_min`, length-and-heaviness-matched random control | **0.2222** |
| poetry-vs-noise separation ratio | **1.56×** |
| `d_min` length-invariance (median at len ≈ 20 / 24 / 28) | 0.136 / 0.163 / 0.107 — flat |

Three opening baytss were additionally verified **by hand, syllable by syllable**, against
their textbook scansion, and all three match exactly:
Imruʾ al-Qais *qifā nabki* → `v--v---v--v-v-` (ṭawīl);
Zuhayr *a-min ummi awfā* → `v--v---v--v-v-` (ṭawīl);
ʿAmr *alā hubbī* → `v---v-vv-v--` (wāfir = mufāʿaltun[ʿaṣb] + mufāʿalatun + faʿūlun).

**Calibration choices, made on the control corpus only, and bounded in advance.**
Exactly two matcher variants were compared — uniform substitution cost, and a
ziḥāf-asymmetric cost making heavy→light cheaper. Uniform scored **equal or better**
(77.1% vs 77.1% at 0.75, 71.7% at 0.5), so **the unparameterised uniform matcher is
locked**; no free parameter is introduced. Vocalisation-threshold sensitivity was also
measured (0.45/0.55/0.65/0.75 → 76.8/77.1/78.3/84.9%); **0.55 is locked** as the primary
because it retains the most data, and the monotone rise with vocalisation completeness is
itself evidence that residual error is vocalisation-driven rather than scanner-logic-driven.

**GATE (locked):** if per-poem plurality accuracy is < 2/3, or per-bayt accuracy < 40%,
the scanner is declared **not fit for purpose**, the honest deliverable is
"the scanner does not work and here is why," and **no Qurʾānic result is reported at all.**
On the frozen benchmark the gate passes; the script re-asserts it at runtime.

---

## 5. THE PAUSAL CONFOUND

Classical scansion applies *waqf* at line end: final short vowels and tanwīn are dropped.
Naive scansion of fully-vocalised text mis-weights **every unit-final syllable**. This is
handled as the primary rules-tuple axis, not as an afterthought:

- **T1 (PRIMARY) — pausal.** Unit-final short vowel and tanwīn dropped; final syllable
  then forced heavy (standard ʿarūḍ convention, and what the control calibration used).
- **T2 — non-pausal.** Full vocalisation retained verbatim to unit end, no forced heavy.

Every registered statistic is computed under **both** and both are reported in the same
tables. A verdict that holds only under one tuple is **RULES-TUPLE-FRAGILE**.

**T3 — matn sensitivity.** Ḥadīth text is *isnād* + *matn*; the isnād is a stereotyped
transmission chain, not representative prose. T3 recomputes the prose arm on text after
the last `قَالَ` (approximate matn extraction). Prose-arm results are reported under both.

---

## 6. Registered inferences and LOCKED directions

Bonferroni **k = 3**, **α_bon = 0.05/3 = 0.016667**. 10,000 permutations, seed 20260509,
replication 20260519.

### H1 — the Qurʾān occupies a distinct prosodic region
Statistic: median `d_min` per arm. **Conjunctive gate — both parts must hold:**
- (a) median `d_min`(Qurʾān) > median `d_min`(poetry), and
- (b) median `d_min`(Qurʾān) < median `d_min`(prose),

each at permutation p < 0.016667 (labels shuffled between the two arms compared).
*Justification:* al-Bāqillānī's claim on the metricality axis is that the Qurʾān is less
metrical than poetry and more metrical than ordinary prose. Unlike H-NEW-48's length
"between" predicate — which that finding itself reports as ill-defined because prose is
bimodal in length — "between" on `d_min` is well-defined, because `d_min` has a
meaningful floor (perfect metre = 0) and is length-invariant by construction.
**Falsifiable in both directions:** if the Qurʾān is *more* metrical than the muʿallaqāt,
or *less* metrical than ḥadīth prose, H1 fails and is published as failed.

### H2 — no single baḥr matches (a locked-NULL prediction)
Statistic: for each of the 16 meters, the median tiled distance `d_m`(Qurʾān) compared
against a **length-and-heaviness-matched random-string control** (seed-locked, one
matched string per verse). A meter "matches" if Qurʾānic conformity to it is
significantly better than the matched-noise control at Bonferroni α over 16 meters
(0.05/16 = 0.003125).
**Locked direction: NO meter matches.** Confirming al-Bāqillānī requires H2 to **fail to
find a match**. If one or more buḥūr do match, that is a **falsification of the classical
claim on this axis** and will be published as such with full prominence.
*The matched-random control is mandatory:* without it, "the Qurʾān is close to rajaz"
could be trivially true of any string with the same heaviness.

### H3 — sajʿ-dense mufaṣṣal sits closer to rajaz/sarīʿ than long Medinan material
Groups, defined objectively from `data/revelation-order.csv` (`period` column):
- **A = mufaṣṣal-qiṣār**: mushaf order ≥ 78.
- **B = long Medinan**: `period == Medinan` and ≥ 100 verses.

**Conjunctive gate:**
- (a) median `d_min`(A) < median `d_min`(B) at permutation p < 0.016667, and
- (b) the modal best-meter of group A is **rajaz or sarīʿ**.
*Justification:* rajaz and sarīʿ are the shortest-footed, most stichic meters, and the
juzʾ-ʿamma material is short-verse and rhyme-dense. Part (b) is a genuinely risky lock —
it names two of sixteen meters in advance.

---

## 7. Nulls, seeds, controls

- **Permutation null:** arm-label shuffle between the two arms under comparison,
  preserving arm sizes. 10,000 perms, seed 20260509.
- **MW-6 matched-noise control (mandatory):** for every unit, one random syllable string
  of identical length and identical heavy-fraction, seed 20260509. Reported for every arm.
- **MW-5 replication:** every statistic re-run at seed 20260519.
- **MW-3 alternative:** all statistics reported on the mean as well as the median.
- **MW-7:** anything not in the k=3 family is descriptive, single-test α = 0.05 ceiling,
  and labelled as such.

## 8. Frozen inputs (SHA-256, verified at runtime; mismatch = SystemExit)

| file | SHA-256 |
|:--|:--|
| `quran-text/quran-full-tashkeel.json` | `382a7341300602ec8b366316d4bbe2a44955c2bf984d395bdd82dae6110b6715` |
| `data/revelation-order.csv` | `74f52ec1518abf8ecbf67671ee1cdd8e4cfc553fc8c5ead8274cc7dae8916fb7` |
| `…/the_9_books/darimi.json` | `45ec3ac92b072287e6c7451084f55f50a2676e0eab2ec165c4ffecfa57f41d2a` |
| `…/raw/muallaqa-imru-al-qais.txt` | `06f05f6a299d989fcaf330f43f7fba9116b373f94096d38ec07df71432f59c14` |
| `…/raw/muallaqa-zuhayr.txt` | `9a8aac1838323aaa65f916f597ec38c842b74eed77ce44f53c2932b52e6610c2` |
| `…/raw/muallaqa-amr-bin-kulthum.txt` | `d93a81bd2095c7db00417650f883c834077fac12668e50002c8b35f26e2ef720` |

**Run immutability.** Output to `findings/phase-b-hypotheses/runs/h-new-2690/<UTC>/` with
`result.json` + `manifest.json`. **No run directory may ever be deleted or overwritten,
including uncommitted or superseded ones.** A non-portable path is remedied by re-running
to an **additional** directory and retaining both. No exception.

## 9. Classical anchoring — and what is NOT available

- **al-Khalīl b. Aḥmad**, *Kitāb al-ʿAyn* / the ʿarūḍ system: **NOT on disk.** No passage
  is cited. The 16-meter table of §2.2 is external reference knowledge, and its only
  on-disk validation is the positive control of §4. **This is a real limitation of the
  whole test and is stated as such, not buried.**
- **al-Bāqillānī**, *Iʿjāz al-Qurʾān*: `KNOWLEDGE-GRAPH.md` maps al-Bāqillānī only for the
  *iʿjāz al-fawāṣil* claim (→ h-new-730/740). **The primary text is not on disk.** The
  "neither nathr nor shiʿr" claim is therefore engaged as a *thesis attributed in the
  secondary framing of H-NEW-48*, **not** as a quoted passage. No passage will be quoted.
- Any citable passage found on disk during the run will be cited with file path and page;
  none will be invented.

## 10. Failure conditions (locked)

- Positive-control gate fails (§4) → **no Qurʾānic result reported**; the deliverable is
  the scanner post-mortem.
- p ≥ 0.016667 on a registered inference → that inference is **NULL**.
- Direction reversed — Qurʾān more metrical than poetry, or less than prose, or a baḥr
  matches, or mufaṣṣal less metrical than Medinan, or A's modal meter is neither rajaz nor
  sarīʿ → **pre-commit violation**, published as REVERSED/NULL with full prominence.
- Holds under T1 but not T2 → **RULES-TUPLE-FRAGILE**, never CONFIRMED.
- **CONFIRMED** requires all three inferences to pass under both pausal tuples.

## 11. Honest limits, stated in advance

1. **2-meter positive control.** Only ṭawīl and wāfir have vocalised ground truth. The
   scanner is unvalidated on the other 14 meters, including rajaz and sarīʿ — **which H3
   names**. H3 is therefore the weakest inference here and must be read as such.
2. **The meter table is unverifiable on disk** (§9).
3. **23% per-bayt error** on known-meter poetry. Every Qurʾānic number inherits it.
4. **Differential vocalisation completeness** — Qurʾān 0.918 vs ḥadīth 0.866 vs
   muʿallaqāt 0.72–0.84. The Qurʾān is the best-vocalised arm; if incomplete vocalisation
   inflates `d_min`, the poetry and prose arms are inflated *relative to* the Qurʾān.
   **This biases toward finding the Qurʾān more metrical than it is, i.e. toward H1(a)
   failing and H2 finding a spurious match.** Direction of bias stated before running.
5. **Prose arm is ḥadīth, not the H-NEW-48 baselines** — a different genre from Jāḥiẓ's
   literary prose, and isnād-contaminated (T3 addresses this only approximately).
6. **Qurʾānic recitation is not metre.** Tajwīd durations (madd) are not modelled; the
   scanner reads orthography, not performance.
7. **Verse ≠ bayt.** The unit comparison across arms is a genuine incommensurability;
   `d_min`'s length-invariance mitigates but does not remove it.

---

*Locked 2026-08-07 by Waiel Al-Shujaa, after control calibration and before any Qurʾānic
scansion. Bismillāhi al-Raḥmāni al-Raḥīm.*
