---
finding_id: H-NEW-3170
title: "PRE-REGISTRATION — Does the Buckwalter-style transliteration carry phoneme-level information the vocalised Arabic text does not?"
author: Waiel Al-Shujaa
date: 2026-08-09
phase: B
frontier_item: F-19
status: PRE-REGISTERED — NOT YET RUN
seed: 20260509
n_perms: 10000
k_confirmatory: 2
alpha_bonferroni: 0.025
binding_raw_gate: 0.001
rules_tuple: "(quran-text/quran-full-tashkeel.json as primary Arabic; quran-text/quran-transliteration.json as the F-19 channel under test; surah keyed by the JSON `id` field NOT list position; verse keyed by `id`; whitespace word tokenisation; repaired h-new-2990 phonemiser incl. TANWIN_REMAP for U+0656/0657/065E; al-Khalīl/al-Suyūṭī classical mustaʿliya and ḥalq sets; Hafs-Kufan; Mashriqi)"
data_source: "quran-text/quran-transliteration.json; quran-text/quran-full-tashkeel.json; quran-text/quran-no-tashkeel.json; scripts/h_new_165_phonological_predictor.py, scripts/h_new_232_oq1_singleton.py, scripts/h_new_301_minimal_2feature_singleton.py (read as SOURCE ARTEFACTS for the executability audit D1, not as data)"
---

# PRE-REGISTRATION — H-NEW-3170 (frontier item F-19)

## 0. Step-0 staleness check — DID THIS ALREADY EXIST?

Per the BINDING RULE at `HANDOFF/FRONTIER-MAP-2026-08-07.md` §"CALIBRATION", this check
precedes all design decisions and is logged here as the **first** forking-paths entry.

Commands run over `findings/`, `MASTER-FINDINGS-LEDGER.md`, `HANDOFF/`, `scripts/`:

```
grep -ril "buckwalter"                                  → 50+ files (all QAC root/lemma notation)
grep -ril "phoneme|phonological|makhraj|articulation"   → 100+ files (all GRAPHEME-based)
grep -ril "phonemic"                                    → 7 files
grep -in  "phonemic"      MASTER-FINDINGS-LEDGER.md     → 0 hits
grep -in  "transliterat"  MASTER-FINDINGS-LEDGER.md     → 0 hits
grep -rl  "quran-transliteration|quran_transliteration" scripts/ findings/  → 0 files
grep -ril "h-new-165|h-new-232|h-new-252|h-new-301|h-new-700|h-new-2870|h-new-2990"
```

**Result: NOT already answered.** `quran-text/quran-transliteration.json` is read by **zero**
scripts in the repository, and neither "phonemic" nor "transliteration" occurs anywhere in the
7,514-line master ledger as a method term. The map's "Read by 0 scripts" is confirmed.

The seven named neighbours, and why none of them is this:

| finding | what it does | why it is not F-19 |
|:--|:--|:--|
| **H-NEW-165** | 15-dim locked tajwīd codebook over the muq letter-sets; RF LOOCV 19/29 | **reads no corpus text at all** (see D1) |
| **H-NEW-165.2** | 4 codebook variants; ROBUST, 8/10 invariant | perturbs the codebook, not the representation |
| **H-NEW-232** | singleton nearest-centroid, **8/10**, p = 0.02498 | **reads no corpus text at all** (see D1) |
| **H-NEW-252** | phon ∪ (α,β) 17-dim; same 2 misses | consumes H-NEW-232's JSON; no text |
| **H-NEW-301** | all C(11,2) pairs; best 9/10, maxT p = 0.196 MARGINAL | **reads no corpus text at all** (see D1) |
| **H-NEW-700** | phoneme-density / rhyme compression tail | grapheme proxy; corrected 2026-08-07; not a representation contrast |
| **H-NEW-2870 / 2990** | pausal fāṣila phonology; the repaired phonemiser | builds the instrument this lane borrows; never contrasts representations |

**One published finding names this lane's remedy in its own words.**
`h-new-910-alif8-cluster.md` line 290, under "Honest limits and DATA-GAPS":

> *"Phoneme axis used grapheme proxy: the H5 phoneme density used emphatic/pharyngeal/sibilant/glottal
> grapheme counts as a phoneme proxy. **A proper phoneme analysis would use the IPA-aligned
> full-tashkeel transliteration.** The grapheme proxy is the project default but is admittedly coarse."*

That is a standing, self-declared, undischarged residual, and it is the anchor for this lane's
direction lock (§4). It is **not** the frontier map's `Prior.` line, which the CALIBRATION block
forbids citing as evidence and which is not cited here.

---

## 0.1 PRE-LOCK RECONNAISSANCE — declared in full, before any hypothesis is stated

The frontier map's F-19 entry contains a **named confound** and an explicit instruction:

> *"If the romanisation is derived from the same vocalised text, this adds no information — it is a
> re-encoding. **Must verify independence, and if it is derived, use the tashkeel directly instead.**"*

That instruction makes the derivation check a **pre-design gate**, not a result. I ran it before
writing this document. Everything I looked at is listed here. Nothing below is a hypothesis outcome;
all of it is structural fact about the encoding, of the same kind as counting tanwīn codepoints.

| # | what I looked at | what I found |
|--:|:--|:--|
| **R1** | order of the 114 surah objects in `quran-transliteration.json` | **SCRAMBLED.** The list runs `1..12, 14, 15, … 43, 93, 13, 32, 61, …`; surah 13 sits at **list position 39**. Only the first 12 entries are in id order. Any positional `zip()` against a normally-ordered file misaligns **102 of 114 surahs**. Keying by `id` restores a clean 114/114 surah and 6,236/6,236 verse alignment. |
| **R2** | word-token alignment of T against each Arabic file | T aligns best with **full-tashkeel**: 375 verses differ in token count (77,800 vs 77,429 tokens). Against min-tashkeel 2,771 verses differ; against no-tashkeel 2,723. |
| **R3** | the 375 mismatching verses | every inspected case is **vocative-*yā* splitting** — `يَٰبَنِيٓ` → `Ya banee`, `يَٰمُوسَىٰ` → `ya moosa`. This is the exact phenomenon of `AUDIT-REGISTER-PROXY-ORTHOGRAPHY-DEPENDENCE` §2.1, appearing here in a **third** file pair. |
| **R4** | character inventory of T | **45 characters**: 26 lowercase + 19 uppercase/`-`/space Latin. **No diacritics of any kind.** |
| **R5** | Latin word types mapping to >1 Arabic consonantal skeleton | 382 types, 11,655 of 70,230 aligned tokens (16.60%). Inspected examples include `baaad` ← {بعد, بعض}, `yuntharoona` ← {ينظرون, ينذرون}, `ohilla` ← {أهل, أحل}, `alghaytha` ← {ٱلغيظ, ٱلغيث}, `bastatan` ← {بسطة, بصطة}. |
| **D1-recon** | input calls in `h_new_165_phonological_predictor.py`, `h_new_232_oq1_singleton.py`, `h_new_301_minimal_2feature_singleton.py` | **zero corpus reads in all three.** Their only file I/O is writing their own output JSON. |

**What I did NOT look at before locking:** every quantity named in §3 and §4 — the conditional
entropies, the per-consonant merger matrix as a scored object, the mustaʿliya/ḥalq concentration
statistic, the surah-level correlations, any permutation p-value, any tie fraction, and every
number in the verdict table. Those are computed for the first time by the run.

**Honest statement of what this costs.** R5 makes the *direction* of D3 (loss) obvious before the
run. I am therefore **not** claiming D3 as a blind prediction, and D3 is **not** one of the two
confirmatory cells. The confirmatory cells C4 and C5 ask a different question — whether the loss is
*targeted* at the project's signal axes — whose answer R5's five examples do not determine, since
those examples were selected for legibility and not by any frequency or feature criterion.

---

## 0.2 F-19 AS SPECIFIED IS NOT EXECUTABLE — and the reason is auditable

The map's F-19 operationalisation is:

> *"…should improve or break the muqaṭṭaʿāt singleton ceiling that OQ-1 leaves open at 8/10."*

The 8/10 is `h_new_232_oq1_singleton.py`. Its features come from `letter_set_features(name)`, which
averages a hard-coded 14-row `LETTER_FEATURES` table over the 2–5 letters of a letter-set. **The
Quran's text is never opened.** There is consequently **no text representation in that pipeline to
replace with a phonemic one** — the statistic is a function of 14 letter names and a codebook, and
is invariant to every possible re-encoding of the corpus by construction.

This is recorded as cell **D1** and verified mechanically at runtime rather than asserted.

Because the specified test cannot run, this pre-registration tests **F-19's headline claim**
instead — *"Buckwalter transliteration enables a phoneme-level analysis that the orthographic text
does not support"* — which is executable, decisive, and untouched. The substitution is made **before
observation** and is itself the map's instruction (§0.1, "use the tashkeel directly instead").

---

## 1. Hypotheses

**Deterministic cells (measurements; no sampling model, therefore no p-value — see §5.3):**

- **D1 — EXECUTABILITY.** The muqaṭṭaʿāt singleton statistic reads no corpus text.
- **D2 — ADDITION.** `H(T | A) = 0` — the transliteration is a deterministic function of the
  vocalised Arabic word, i.e. it carries **no** information the tashkeel does not already carry.
- **D3 — LOSS.** `H(A | T) > 0` — the vocalised Arabic is **not** recoverable from the
  transliteration.
- **D6 — WHAT THE PHONEME LAYER ACTUALLY ADDS.** Gemination rate and long-vowel rate are computable
  under the phonemic representation and **undefined** under the grapheme representation. Reported
  descriptively, with their source named.

**Confirmatory cells (permutation-tested, k = 2, α_bon = 0.025):**

- **C4 (PRIMARY).** The contrast destroyed by the transliteration is **concentrated on the
  classical mustaʿliya ∪ ḥalq consonants** — the axes the project's own instrument treats as
  signal-bearing — relative to a frequency-matched null over alternative merger assignments.
- **C5 (SECONDARY).** At surah level, the transliteration preserves **sonorant** density better than
  **mustaʿliya** density: `Δρ = ρ_son(P,T) − ρ_must(P,T) > 0`, on the **worst** of three length
  channels.

---

## 2. Representations under test

| tag | representation | source | what it can see |
|:--|:--|:--|:--|
| **G** | grapheme | `quran-no-tashkeel.json` | consonantal skeleton only. Cannot see short vowels, vowel length, or gemination. The project default. |
| **P** | phonemic | `quran-full-tashkeel.json` through the **repaired h-new-2990 phonemiser** | C / V / VV stream; gemination emitted as a doubled C; tanwīn as consonantal `-n`; all 28 consonants distinct. |
| **T** | transliteration | `quran-transliteration.json` | the F-19 channel under test. |

**Phonemiser provenance (mandatory declaration).** P uses the phonemiser at
`findings/phase-b-hypotheses/scripts/h-new-2990.py` §1, ported **verbatim** — `normalize`,
`phonemes` and their constant tables — including

```python
TANWIN_REMAP = {"ٗ": FATHATAN, "ٞ": DAMMATAN, "ٖ": KASRATAN}   # U+0657, U+065E, U+0656
```

which **remaps** rather than drops the three Uthmānī tanwīn codepoints. Per
`AUDIT-TANWIN-DELETION-2690`, the unrepaired instrument (`h-new-2690.py`) deletes 6,643 of the
corpus's 8,554 tanwīn — 77.66% — by treating those codepoints as diacritics. **This lane uses the
repaired mapping, and the run asserts at startup that all three codepoints survive normalisation
as tanwīn.** That assertion is gate **S2** (§6). No new phonemiser is written.

**Source-file declaration (mandatory, per `AUDIT-WAQF-MARK-INVENTORY-DIVERGENCE`).** The primary
Arabic file is `quran-full-tashkeel.json`, which that audit shows is a **singleton** on waqf-mark
inventory (0 × U+06D9 *lā*, where twelve other files carry 68). It is chosen because it is the only
vocalised file, and vocalisation — not pause marking — is the entire subject of this test; and
because R2 shows it is the file T word-aligns with (375 mismatching verses against 2,771 and 2,723).
**The waqf divergence does not bind here:** every waqf codepoint is in the ported phonemiser's
`DROP` set and is removed before any phoneme exists. Gate **S3** verifies that the count of waqf
codepoints surviving into any P or T stream is zero.

**Orthographic-alignment declaration (mandatory, per `AUDIT-REGISTER-PROXY-ORTHOGRAPHY-DEPENDENCE`).**
The 375 vocative-*yā* verses (R3) are where T's segmentation diverges from the Uthmānī rasm. All
token-level cells (D2, D3, C4) are computed on the **token-count-matched subset only**; the count of
excluded verses and their token mass is reported, and gate **S5** requires it to be ≤ 1% of tokens.
Surah-level cells (C5) use whole-surah character streams and are unaffected by segmentation.

---

## 3. Statistics — exact definitions

### 3.1 D2 — addition
Over aligned token pairs `(a, t)` where `a` is the **full-tashkeel** Arabic word:
`A_add` = number of distinct `a` types mapping to ≥ 2 distinct `t` forms, and the token mass thereof.
`H(T|A)` in bits, computed over the empirical joint. **D2 holds iff `H(T|A) = 0`.**

**Case is a deciding parameter and is declared as such** (`cross-finding-029`). The scheme uses
uppercase both phonemically (`AA` = ʿayn) and positionally (verse-initial capital). Two variants are
run and **both reported**:
- **V-case** — raw, case-sensitive.
- **V-fold** — `AA` protected by a sentinel, then case-folded.
The **worse** (larger `H(T|A)`) is the headline for D2. If they disagree on whether `H(T|A) = 0`,
the disagreement is the result and is reported as such.

### 3.2 D3 — loss
`A_loss` = number of distinct `t` types mapping to ≥ 2 distinct Arabic forms; token mass; `H(A|T)`.
The Arabic reference form is itself a **deciding parameter**, declared, with three variants run and
**all three reported**, worst as headline:
- **A1** full-tashkeel word (finest)
- **A2** phonemicised word from P (the phonological object of interest)
- **A3** consonantal skeleton (coarsest)

**Per-consonant merger matrix.** For each of the 28 Arabic consonants, the distribution of Latin
images over aligned tokens, and the resulting partition of the 28 into T-distinguishable classes.
A consonant is **merged** iff it shares a Latin image class with a different consonant at ≥ `θ` of
its token mass. **θ = 0.50 is a coarsening parameter, declared, and swept over {0.25, 0.50, 0.75};
all three reported, worst as headline.**

### 3.3 C4 — targeted loss (PRIMARY)

The two classical sets, taken verbatim from the sources already used by H-NEW-165 and H-NEW-2550,
with **zero new hand assignment**:

- **mustaʿliya** (al-Suyūṭī, *al-Itqān*, ḥurūf al-istiʿlāʾ): خ ص ض ط ظ غ ق — 7 letters
- **ḥurūf al-ḥalq** (al-Khalīl, *Kitāb al-ʿAyn*): ء ه ع ح غ خ — 6 letters
- **union** (13 distinct letters) = the C4 target set
- **sonorants** (H-NEW-69's axis, and H-NEW-165's `sonorant` feature): م ن ل ر و ي — the C5 contrast set

**Statistic.** `F_obs` = (token mass of merged consonants that are in the target set) ÷ (token mass
of all merged consonants). Merged as defined in §3.2.

**Null.** 10,000 permutations, seed **20260509**. Each permutation holds the observed **merger
partition shape** fixed — the multiset of class sizes — and reassigns which consonants occupy which
class, sampling **frequency-stratified**: consonants are binned into quartiles of corpus token
frequency and permuted within bin, so a null merger set matches the observed one in both partition
shape and frequency profile. `p = (1 + #{F_null ≥ F_obs}) / (1 + n_perm)`.

**Tie handling.** The tie fraction of the null distribution — `#{F_null = F_obs} / n_perm` — is
**measured and reported**. The 28-consonant space is small and heavy ties are expected. **If the tie
fraction exceeds 50%, the permutation p is discarded and replaced by an EXACT enumeration** over all
distinct frequency-stratified assignments (or, if that exceeds 10⁷, by an exact conditional
hypergeometric on target-set membership among merged consonants). The exact result then governs the
verdict. This branch is decided by the measured tie fraction, not by the p-value.

### 3.4 C5 — surah-level consequence (SECONDARY), three length channels

For each of 114 surahs, and for each representation in {P, T}, compute the density of
(a) mustaʿliya consonants and (b) sonorants. Under T a consonant is counted via its Latin image, so
a merged consonant's density is necessarily contaminated by its merge-partner — that contamination
is the effect under test.

**Three length channels, all run, worst as headline, dominant named** (standing correction,
`AUDIT-LENGTH-CHANNEL-EXPOSURE` §6):

| channel | denominator |
|:--|:--|
| **L1** | verse count |
| **L2** | word count |
| **L3** | mean verse length (words per verse) |

The **dominant** channel is named by the largest \|Spearman ρ\| between the channel variable and the
grouping variable (per-surah mustaʿliya count), computed and reported.

**Statistic.** `Δρ = ρ_son(P,T) − ρ_must(P,T)`, Spearman, across 114 surahs, per channel.
**Headline = the channel with the smallest Δρ** (the worst case for the locked direction).

**Null.** 10,000 permutations, seed 20260509: permute the surah pairing between the P profile and
the T profile, recompute both ρ, recompute Δρ. One-sided in the locked direction.
`p = (1 + #{Δρ_null ≥ Δρ_obs}) / (1 + n_perm)`. Tie fraction measured; > 50% ⇒ exact branch as §3.3.

---

## 4. DIRECTIONS — LOCKED, AND JUSTIFIED FROM PUBLISHED ANCHORS

The frontier map's `Prior.` line is **not** cited. Per the CALIBRATION block its priors are 1-for-7
and every optimistic one has failed; it is treated as an unscored guess.

| cell | locked direction | anchors |
|:--|:--|:--|
| **D2** | `H(T|A) = 0` — T adds nothing | The map's own confound clause states the mechanism; R4 shows T has a 45-character diacritic-free alphabet against the Arabic file's vocalised inventory. A strictly coarser alphabet over the same token sequence cannot add information. |
| **D3** | `H(A|T) > 0` — T loses | Same. **Declared non-blind** (§0.1) and excluded from the confirmatory family. |
| **C4** | destroyed mass **CONCENTRATED** on mustaʿliya ∪ ḥalq, above null | (i) **H-NEW-301**: over all C(11,2) = 55 feature pairs the best-performing subset is exactly `mean_emphatic + mean_pharyngeal` at 9/10 — these two axes, and no others, carry the project's OQ-1 signal. (ii) **H-NEW-165 / 165.2**: `emphatic` and `pharyngeal` are the discriminating ṣifāt in the locked codebook, invariant across 4 codebook variants. (iii) **H-NEW-2550**: the muq-14's one genuinely non-random axis is **sonority**, which is *not* an emphatic axis — so a scheme that preserves sonorants while destroying emphatics destroys the signal-bearing axis and spares the other. (iv) Structural: the Latin alphabet has neither an emphatic nor a pharyngeal series, so a reader-facing romanisation must merge them, while m/n/l/r have direct Latin counterparts. |
| **C5** | `Δρ > 0` — sonorants preserved better than mustaʿliya | Same anchors, at surah granularity. |

---

## 5. DECISION RULE — verdict is a function of these cells and nothing else

### 5.1 Cell outcomes

- **D1 PASSES** iff the runtime audit finds **zero** corpus-text reads in all three of
  `h_new_165_phonological_predictor.py`, `h_new_232_oq1_singleton.py`,
  `h_new_301_minimal_2feature_singleton.py`.
- **D2 PASSES** iff `H(T|A) = 0` under the **worse** of V-case / V-fold.
- **D3 PASSES** iff `H(A|T) > 0` under the **best** (most favourable to T) of A1 / A2 / A3.
- **C4 PASSES** iff `p_C4 < 0.025` **and** `F_obs > median(F_null)`.
- **C5 PASSES** iff `p_C5 < 0.025` **and** `Δρ_head > 0`, where `Δρ_head` is the **minimum** Δρ over
  channels L1, L2, L3.

### 5.2 Overall verdict — exhaustive enumeration

1. `D1 and D2 and D3` → **`PREMISE-REFUTED`.** F-19's headline claim is false in both directions:
   the transliteration adds nothing the vocalised text lacks, and destroys what the vocalised text
   has; and F-19's named target statistic could not have been moved by any representation.
2. `PREMISE-REFUTED and C4 and C5` → **`PREMISE-REFUTED-LOSS-TARGETED`.** The strongest outcome:
   the loss is not merely present but concentrated on the project's signal axes.
3. `PREMISE-REFUTED and (C4 xor C5)` → **`PREMISE-REFUTED-LOSS-PARTIAL`**, naming which cell failed.
4. `PREMISE-REFUTED and not C4 and not C5` → **`PREMISE-REFUTED-LOSS-UNTARGETED`.** The loss exists
   but is spread across the inventory; the transliteration is coarse, not adversarial.
5. `not D2` → **`PREMISE-SURVIVES-ADDITION`.** T carries something the tashkeel does not; the run
   must enumerate what, and C4/C5 are reported but do not decide.
6. `not D3` → **`PREMISE-SURVIVES-LOSSLESS`.** T is a lossless recoding; F-19's phoneme claim
   reduces to the tashkeel's own content and is reported as such.
7. `not D1` → **`SPECIFIED-TEST-EXECUTABLE`.** The 8/10 does read text after all; this
   pre-registration is void on its substitution and the specified test must be run instead.

### 5.3 Why the deterministic cells carry no p-value — stated before the run

D1, D2, D3 and D6 are **measurements of a fixed pair of files**, not estimates from a sample.
There is no population, no resampling unit, and therefore no null distribution: the transliteration
either is or is not a function of the vocalised text, exactly as the tanwīn codepoint count in
`AUDIT-TANWIN-DELETION-2690` either is or is not 6,643. Attaching a permutation p-value to them
would be decoration. The permutation machinery is spent where a null exists — C4 and C5 — and the
Bonferroni family is **k = 2** for that reason.

### 5.4 If a confirmatory cell returns NULL — MDE and power are mandatory

Per method `h-new-3030` §3.3 and §3.5, any NULL reported here must state:

1. **MDE** — the smallest true concentration `F` (C4) or `Δρ` (C5) this design detects at 80% power,
   computed by exponential tilting of the realised null (`p_θ(x) ∝ p_0(x)·e^{θx}`, bisecting θ to
   80% power), **not** asserted.
2. **The S\* vs S_max branch.** `S*` = the smallest observed statistic that would reject at α_bon
   given the realised null; `S_max` = the largest value the statistic can attain under any
   configuration of the corpus (for C4, `F = 1.0`; for C5, `Δρ = 2.0`). If **`S* > S_max`** the
   verdict is **`UNTESTABLE-AT-THIS-N`** — the design could not have rejected under any data — and
   that says *nothing whatever about the signal*. Both quantities are functions of the null alone,
   are computed unconditionally whatever the outcome, and are written to `result.json`.
3. **Power against a uniform alternative**, reported alongside the MDE.

---

## 6. SELF-CHECKS — hard gates. A failed gate VOIDS the run.

| gate | requirement |
|:--|:--|
| **S1 — keying** | Surahs and verses are joined by their `id` fields, never list position. The run asserts the transliteration list order is **not** sorted (R1) and that id-keyed joining yields 114 surahs and 6,236 verses on both sides. **A run that silently succeeds under positional zip is void.** |
| **S2 — tanwīn repair** | After `normalize`, the three Uthmānī tanwīn codepoints U+0656/0657/065E survive as tanwīn. Asserted by round-tripping a probe string and by requiring the corpus-wide tanwīn total to be ≥ 8,000 (the audit's figure is 8,554; the defective instrument yields 1,911). |
| **S3 — waqf** | Zero waqf codepoints (U+06D6–U+06DC) survive into any P or T stream. |
| **S4 — alignment loss** | Token-level cells use only token-count-matched verses; the excluded token mass is reported and must be ≤ 1%. |
| **S5 — strata homogeneity** (`cross-finding-030` mech. 1) | Before C4 trusts the "merged" class, every consonant assigned to it must have ≥ θ of its token mass in the shared Latin class **and** the class must not pool a consonant that is ≥ 95% uniquely recoverable with one that is ≤ 5%. Any inhomogeneous class is reported and excluded, and the exclusion is listed. This is the check whose absence merged long-*ī* with the *ay* diphthong in H-NEW-3150. |
| **S6 — control applies** (`cross-finding-030` mech. 2) | The C4 null must be able to produce values both above and below `F_obs`; if `F_null` is constant, or if the target set is a superset of every consonant that can be merged, the control is **inapplicable** and C4 is void rather than passing. |
| **S7 — control ≠ treatment** (`cross-finding-030` mech. 3) | Spearman ρ between the C5 contrast axis (sonorant density) and the treatment axis (mustaʿliya density) across 114 surahs is computed and reported. If \|ρ\| > 0.8 the two axes are the same variable and C5 is void rather than passing. |
| **S8 — prereg lock** | `EXPECTED_PREREG_SHA` in `scripts/h-new-3170.py` matches this file's SHA-256 at runtime; mismatch ⇒ `SystemExit`. |
| **S9 — immutable run dir** | `os.makedirs(..., exist_ok=False)`; every artefact written with `open(..., 'x')`. No run directory is ever deleted. |

---

## 7. Garden of forking paths — every choice, fixed here

| choice | fixed value | alternatives NOT taken |
|:--|:--|:--|
| primary Arabic file | `quran-full-tashkeel.json` | min-tashkeel, no-tashkeel (both align far worse, R2) |
| surah/verse join | by `id` | positional (would misalign 102/114 surahs) |
| tokenisation | whitespace | QAC segment tokens |
| case handling | both V-case and V-fold run, worse reported | picking one |
| Arabic reference form for D3 | A1/A2/A3 all run, worst reported | picking one |
| merger threshold θ | 0.50, swept {0.25, 0.50, 0.75}, worst reported | a single unswept value |
| length channel | L1/L2/L3 all run, **worst** reported, dominant named | one channel |
| classical sets | al-Suyūṭī mustaʿliya, al-Khalīl ḥalq, verbatim | any hand-built feature table for the 14 non-muq consonants — **explicitly refused** as a `PROXY-CLAIMS` violation |
| null shape | partition-shape-preserving, frequency-stratified | unstratified shuffling (would confound merger with frequency) |
| n_perm | 10,000 | — |
| seed | 20260509 | — |
| confirmatory family | C4, C5 only; k = 2, α_bon = 0.025 | including D2/D3 (no sampling model) |
| tie policy | measured; > 50% ⇒ exact test governs | trusting the permutation p regardless |

---

## 8. What this pre-registration does NOT claim

- It does **not** claim the muqaṭṭaʿāt 8/10 result is wrong. D1 says only that it is a function of
  14 hard-coded letters and a codebook, so **no** text representation can move it. Whether the
  classical a-priori grouping it tests is coherent is a separate question this lane does not reopen.
- It does **not** claim the transliteration file is defective. A reader-facing romanisation is
  entitled to merge contrasts; the finding, if it lands, is about what it can then be **used for**.
- It does **not** rehabilitate H-NEW-910's H5 residual. It establishes which representation could
  discharge it; discharging it is a separate run.
- It asserts nothing about the Quran. Every cell here is a property of an **encoding**.

---

**LOCKED.** SHA-256 of this file is embedded as `EXPECTED_PREREG_SHA` in
`findings/phase-b-hypotheses/scripts/h-new-3170.py` and verified at runtime.
