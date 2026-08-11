---
id: H-NEW-3170
title: "F-19 is not executable as specified — the muqaṭṭaʿāt 8/10 reads no corpus text; and the transliteration adds no phonology while merging 11 of 28 consonants. Pre-registered run VOID on its own alignment gate; three design defects reported."
date: 2026-08-09
phase: B
frontier_item: F-19
status: >-
  VOID — the pre-registered run failed hard gate S4 (9.73% of tokens excluded against a
  1% limit I set without computing it). No confirmatory cell is claimed. What is reported
  are (a) deterministic code and encoding facts that do not depend on the void gate, and
  (b) clearly-labelled post-hoc diagnostics.
verdict: VOID (gate S4); F-19 NOT EXECUTABLE AS SPECIFIED (deterministic, independent of the void)
author: Waiel Al-Shujaa
seed: 20260509
n_perms: 10000
k_confirmatory: 2
alpha_bonferroni: 0.025
prereg: prereg-h-new-3170-phoneme-level.md
prereg_sha256: 26f7807fc50df71195e2982bdb441dccf3f7ca22a1ea711d8dcb7a3d382fae16
run_dir: findings/phase-b-hypotheses/runs/h-new-3170/2026-08-09T110750Z
posthoc_dir: findings/phase-b-hypotheses/runs/h-new-3170-posthoc/2026-08-09T111240Z
rules_tuple: "(quran-full-tashkeel.json primary; quran-transliteration.json under test; surah keyed by `id` NOT list position; repaired h-new-2990 phonemiser incl. TANWIN_REMAP; al-Suyūṭī mustaʿliya + al-Khalīl ḥalq verbatim; Ḥafṣ-Kūfan; Mashriqī)"
parents: [H-NEW-165, H-NEW-165.2, H-NEW-232, H-NEW-252, H-NEW-301, H-NEW-910, H-NEW-2550, H-NEW-2870, H-NEW-2990]
---

# H-NEW-3170 — F-19: the transliteration, the phoneme layer, and a void run

## 0. Verdict, stated first

**The pre-registered run is VOID.** It failed hard gate **S4**: the token-level cells are
computed on verses where the Arabic and Latin token counts match, and that subset excludes
**7,570 of 77,800 tokens — 9.73%**, against a limit of 1% that I wrote into the
pre-registration **without computing what the actual exclusion would be**. The gate did its job:
the excluded verses average 20.2 tokens against a corpus mean of 12.5, so the omitted material is
systematically the long, vocative-heavy Medinan verses. **No confirmatory cell is claimed.**

Three further things are reported below at full prominence: **two of my own design defects**
(the C4 merger instrument, and a degenerate C5 control), and **one implementation-vs-prereg
mismatch** in D1.

What survives the void, because it does not depend on the alignment subset or on any null:

| # | finding | basis |
|--:|:--|:--|
| **1** | **F-19 is not executable as specified.** The muqaṭṭaʿāt singleton 8/10 statistic reads **no corpus text**; no representation can move it. | AST audit + manual inspection of three scripts |
| **2** | **`quran-transliteration.json`'s surah list is scrambled.** Positional iteration misaligns **102 of 114 surahs**. New data trap. | list order, reproduced |
| **3** | **The transliteration merges 11 of 28 consonants into 5 classes** — 18.92% of all consonant tokens. | counting-identity solve, post-hoc |
| **4** | **It adds no phonology.** The only information it carries beyond the vocalised Arabic is verse-initial capitalisation and 42 transcription typos. | H(T\|A), both case variants |
| **5** | **The tashkeel, not the transliteration, is what supplies F-19's "collapsed distinctions."** | 25,256 geminate pairs; 54,655 long vowels |

---

## 1. Step 0 — F-19 is not already answered

`quran-text/quran-transliteration.json` is read by **zero** scripts. Neither *phonemic* nor
*transliteration* occurs as a method term anywhere in the 7,514-line master ledger. The seven
named neighbours are all grapheme-level or codebook-level; the full table is in the
pre-registration §0. **Not stale. Not previously answered.**

One published finding names this lane's remedy in its own words —
`h-new-910-alif8-cluster.md` line 290: *"the H5 phoneme density used … grapheme counts as a
phoneme proxy. A proper phoneme analysis would use the IPA-aligned full-tashkeel
transliteration."* That is the anchor this lane's directions were locked from. The frontier
map's `Prior.` line was not cited, per the CALIBRATION block.

---

## 2. Finding 1 — F-19's named target statistic reads no corpus text

F-19's operationalisation is *"should improve or break the muqaṭṭaʿāt singleton ceiling that
OQ-1 leaves open at 8/10."* That 8/10 is `h_new_232_oq1_singleton.py`. Its features come from

```python
def letter_set_features(letter_set_name: str):
    letters = SET_LETTERS[letter_set_name]        # 2 to 5 letters
    ...  np.mean([LETTER_FEATURES[L][fname] for L in letters])
```

— a hard-coded 14-row codebook averaged over the letters of a letter-set name. An AST walk over
all three scripts in the family finds **zero read-mode file calls**:

| script | read-mode calls | write calls | corpus path strings |
|:--|--:|:--|--:|
| `h_new_165_phonological_predictor.py` | **0** | `OUTPUT_JSON.open("w")` | 0 |
| `h_new_232_oq1_singleton.py` | **0** | `OUTPUT_JSON.open("w")` | 0 |
| `h_new_301_minimal_2feature_singleton.py` | 1 → `p.read_bytes()` at line 84, **its own pre-registration SHA lock** | `open(OUT_JSON,"w")` | 0 |

**The Quran's text is never opened.** There is therefore no text representation in that pipeline
to replace with a phonemic one: the statistic is a function of 14 letter names and a codebook, and
is invariant to every possible re-encoding of the corpus **by construction**.

A corollary worth recording, since it is visible in the same code and is arithmetic, not
inference: H-NEW-165's "structural ceiling" of **19/29 = 0.6552** is exactly the count of
multi-member surahs. Under LOOCV, surahs sharing a letter-set share an *identical* feature row, so
each multi-member surah is always predicted correctly and each of the 10 singletons never can be.
The ceiling is a property of duplicate rows under leave-one-out, and H-NEW-165.2's finding that it
is identical across four codebooks follows from that.

**This says nothing about whether the classical a-priori grouping H-NEW-232 tests is coherent.**
That question is untouched here. What is established is only that F-19's proposed instrument
cannot bear on it.

---

## 3. Finding 2 — a new data trap in the file F-19 names

The 114 surah objects in `quran-transliteration.json` are **not in `id` order**:

```
1 2 3 4 5 6 7 8 9 10 11 12 14 15 16 … 43 93 13 32 61 94 95 97 35 36 41 44 62 99 100 …
```

Only the first twelve are in order. **Surah 13 sits at list position 39.** Any code that iterates
the transliteration alongside a normally-ordered corpus file by position — the obvious
`zip(T, A)` — compares **102 of 114 surahs to the wrong surah**, and does so silently: the totals
still come to 114 surahs and 6,236 verses.

I hit this myself on the first probe. Keying by `id` restores a clean 114/114 and 6,236/6,236
alignment. Gate S1 in the run script asserts the list order is *not* sorted, precisely so that a
run cannot pass by accident under positional zip.

Related: the same file follows the **simple** orthography's vocative-*yā* segmentation
(`يَٰمُوسَىٰ` → `ya moosa`) against the Uthmānī rasm's joined form. This is
`AUDIT-REGISTER-PROXY-ORTHOGRAPHY-DEPENDENCE` §2.1's phenomenon appearing in a **third** file pair,
and it is the direct cause of the S4 failure that voided this run (§6).

---

## 4. Finding 4 — the transliteration adds nothing phonological (and my locked direction was still wrong)

**My locked direction for D2 was `H(T|A) = 0`. It is not zero, and I record that as a failed
prediction.** Measured over the 70,230 aligned tokens:

| variant | H(T\|A) | Arabic types with >1 Latin image | token mass |
|:--|--:|--:|--:|
| **V-case** (raw) | **0.1749 bits** | — | — |
| **V-fold** (`AA` sentinel-protected, then case-folded) | **0.0029 bits** | 42 | 1,561 |

But the *content* of the residual is the point, and none of it is phonology:

- **V-case** is entirely **verse-initial capitalisation**: `فِي` → `fee` ×1007 / `Fee` ×21;
  `مِن` → `min` ×667 / `Min` ×10; `إِنَّ` → `inna` ×339 / `Inna` ×196. This is a **verse-boundary**
  signal, and the corpus already carries verse boundaries explicitly.
- **V-fold**'s 0.0029 bits is **42 single-token transcription errors**, each a hapax against a
  form attested hundreds of times: `min`×342 / `mi`×1 · `kanoo`×199 / `kano`×1 ·
  `kuntum`×131 / `kutum`×1 · `alssalihati`×56 / `alsalihati`×1 · `alnnari`×47 / `alnari`×1.

So: **the substantive claim the lock encoded — that the transliteration carries no phonological
information the tashkeel lacks — holds. The lock as written does not.** Those are different
statements and I am not going to collapse them.

*(The 42 typos are recorded as a data-provenance note on this file. They are a hapax-vs-hundreds
pattern, so they are errors, not variants.)*

### 4.1 And it loses a great deal

`H(A|T) > 0` on all three declared Arabic reference forms, i.e. the vocalised Arabic is **not**
recoverable from the transliteration:

| reference form | H(A\|T) |
|:--|--:|
| A1 full tashkeel | **0.5689 bits** |
| A2 phonemic (repaired phonemiser) | **0.2206 bits** |
| A3 consonantal skeleton (most favourable to T) | **0.0295 bits** |

Because this is an **existence** claim, the 9.73% exclusion cannot overturn it: ambiguity observed
on 90.3% of the corpus is ambiguity in the corpus.

---

## 5. Finding 3 — which contrasts it destroys (POST-HOC, exact)

**This section is post-hoc and non-blind.** It was written after the void run's outcomes were
seen, and it exists because the void run's own merger instrument was defective (§7.1).

The transliteration's character map is recovered exactly by solving the counting identity that any
deterministic character-level transliteration must satisfy — for every token,
`count(latin char l) = Σ_s M[s][l]·count(s)` — over all 70,230 aligned tokens. Mean absolute
residual per cell: **0.033**.

| class | Latin image | consonant tokens | mustaʿliya/ḥalq members |
|:--|:--|--:|:--|
| **{ت, ط}** | `t` | 12,747 | ط |
| **{ث, ذ, ظ}** | `th` | 7,731 | ظ |
| **{د, ض}** | `d` | 8,386 | ض |
| **{س, ص}** | `s` | 9,120 | ص |
| **{ح, ه}** | `h` | 21,386 | ح, ه |

**11 of 28 consonants are merged, covering 59,370 of 313,777 consonant tokens — 18.92%.**
Preserved and distinct: ق `q` vs ك `k`; غ `gh` vs ع `AA`; خ `kh`; ش `sh`; and every sonorant
(م `m`, ن `n`, ل `l`, ر `r`, و `w`, ي `y`).

**The organising principle is not the emphatic axis — it is the Latin dental-alveolar series.**
Every merger pairs an emphatic with its *plain* counterpart, and the plain member is destroyed
just as thoroughly. Six of the eleven merged consonants are in mustaʿliya ∪ ḥalq; five are not.

Recomputing C4's statistic on this corrected partition (**descriptive only — post-hoc, and not
claimable**): `F_obs = 0.4717` against an exact frequency-stratified null over 36,015
configurations, mean 0.2299 — **percentile 91.1, p_exact = 0.089.** Directionally as locked, and
**not significant at α_bon = 0.025** even before the post-hoc discount.

> **A deciding parameter, in this lane's own work.** With the void run's defective 9-consonant
> partition, `F_obs = 0.1742, p = 0.830` — *anti*-concentrated. Adding the two consonants the
> defective instrument missed, ح and ه (21,386 tokens, both ḥalq), moves the statistic from the
> 17th to the **91st** percentile of its null. **The direction of the answer was decided entirely
> by whether two consonants were in the merger set.** This is a fourth anchor for
> [[cross-finding-029-the-deciding-parameter]].

---

## 6. Finding 5 — what actually supplies the "collapsed distinctions"

F-19's premise is that a phoneme-level representation "would distinguish long/short vowels and
gemination that the grapheme layer collapses." It would — and the source of that information is
the **tashkeel**, not the transliteration. Under the repaired h-new-2990 phonemiser on
`quran-full-tashkeel.json`:

| quantity | value | computable under the grapheme layer? |
|:--|--:|:--|
| consonant tokens | 313,777 | yes |
| **geminate pairs** | **25,256** (0.0805 per consonant) | **no** |
| **long vowels** | **54,655** (0.2407 of all vowels) | **no** |
| short vowels | 172,407 | no |

Both new variables are real, both are per-surah computable, and both come from the vocalised
Arabic file the project already has. **The frontier map's own instruction — *"if it is derived,
use the tashkeel directly instead"* — is the correct one, and the transliteration is not needed
for any of it.** H-NEW-910's H5 residual can be discharged from the tashkeel alone.

Instrument note: the phonemiser is the **repaired** one. Gate S2 confirmed **8,554 tanwīn survive
normalisation** — matching `AUDIT-TANWIN-DELETION-2690`'s corpus figure exactly, against the 1,911
the defective `h-new-2690.py` mapping yields. The three Uthmānī codepoints U+0656/0657/065E are
remapped, not dropped.

---

## 7. What I got wrong

### 7.1 The C4 merger instrument was defective — and my own gate for this failed to fire

The pre-registered merger test asked, for each consonant pair {x,y}, whether Arabic skeleton
minimal pairs on x/y map to **identical whole Latin word forms**. That is not the same question as
*does T distinguish x from y*, because **the vowels can disambiguate two words whose consonants
merged**. The instrument therefore scored contrasts as PRESERVED that are in fact totally
destroyed:

| pair | minimal-pair instrument | truth (character map) |
|:--|--:|:--|
| {س, ص} | destroyed fraction **0.202** | both → `s`, **fully merged** |
| {ت, ط} | 0.261 | both → `t`, **fully merged** |
| {ذ, ظ} | 0.308 | both → `th`, **fully merged** |
| {ح, ه} | **0.050** | both → `h`, **fully merged** |
| {د, ض} | 0.623 | both → `d`, fully merged — the only one it caught |

This is `cross-finding-030` **mechanism 1** — *the control does not discriminate; its strata are
not homogeneous in the thing it claims to hold fixed* — occurring in the design of a lane that had
read that file and written a gate against it. **Gate S5 was the wrong check**: it tested whether
the two members of a declared-merged pair had homogeneous *recoverability*, not whether the
quantity being measured was the consonant contrast at all. S5 excluded 0 pairs and never fired.

### 7.2 The C5 control was degenerate and could only ever return 1.0

C5 contrasted how well the transliteration preserves **sonorant** density against **mustaʿliya**
density across 114 surahs. **No sonorant is merged by the transliteration** — م ن ل ر و ي all have
distinct Latin images. So the T-side sonorant count is *identically equal* to the P-side count, and
`ρ_son(P,T) = 1.0000` exactly, in all nine (θ × channel) cells. The control arm was not a
comparison; it was an identity.

Gate S7 checked the wrong property here too: it verified that sonorant and mustaʿliya densities are
different variables (ρ = 0.1196, well under the 0.8 limit) — which is true and irrelevant. It never
checked that the control arm was **non-degenerate**.

### 7.3 D1's implementation was stricter than its pre-registration

The prereg says D1 passes on *"zero **corpus-text** reads."* The implementation counted **any**
read-mode call, and so flagged `h_new_301`'s `p.read_bytes()` — which reads *its own
pre-registration* to compute its SHA lock. Under the implementation D1 returned FAIL; under the
prereg's wording it passes. The substantive fact (no corpus text is read by any of the three) is
unaffected and is verified two ways. **This is a mismatch I should have caught: I diffed the
verdict function against §5.2 line by line, but did not diff each cell's *definition* against its
implementation.**

### 7.4 The pre-registration miscounts its own target set

Pre-registration §3.3 states the mustaʿliya ∪ ḥalq union is *"13 distinct letters."* **It is 11.**
mustaʿliya (خ ص ض ط ظ غ ق) is 7 and ḥalq (ء ه ع ح غ خ) is 6, and they overlap on **two** letters,
غ and خ — I subtracted neither. **No computation is affected**: the script builds
`TARGET = MUSTALIYA | HALQ` as a set union, so every statistic used the correct 11. Only the prose
count was wrong. Under the declared hamza normalisation (ء → ا, prereg §7 and the script's
`CARRIER_NORM`) the **scoreable** target set inside the 28-letter inventory is **10**: ح خ ص ض ط ظ
ع غ ق ه.

Per the immutability rule the pre-registration is **not edited**; the error is recorded here.

### 7.5 The S4 threshold was locked without being computed

1% was a guess. The true figure is 9.73%, and it was knowable before locking — the reconnaissance
had already found the 375 divergent verses; I did not convert verses to token mass. **The gate is
right and the threshold was wrong, and per the immutability rule the pre-registration is not
edited.** The run stands as VOID.

---

## 8. The three length channels, reported as required

C5 was run on all three, at all three merger thresholds. Every cell is in `result.json`; the
headline is the **worst** (smallest Δρ). All nine are uninterpretable for the reason in §7.2, and
are printed here only because the protocol requires the channel table regardless of outcome.

| θ | L1 verse count | L2 word count | L3 mean verse length |
|:--|--:|--:|--:|
| 0.25 | Δρ = +0.0158, p = 0.342 | **Δρ = +0.3150, p = 0.0092** | Δρ = +0.0050, p = 0.400 |
| 0.50 | +0.0088, p = 0.420 | +0.1585, p = 0.119 | +0.0023, p = 0.470 |
| 0.75 | +0.0000, p = 0.496 | −0.0000, p = 0.502 | −0.0000, p = 0.496 |

**Headline (worst of nine): θ=0.75 / L2, Δρ = −0.0000, p = 0.502 — FAIL.**
**Dominant channel: L2 word count** (|ρ| = 0.9946 against the grouping variable, versus 0.9036 for
L1 and 0.7552 for L3).

The swing across channels at θ=0.25 is **p = 0.0092 → 0.400, a 44× swing**, and the dominant
channel is the one that would have produced the significant result. Under a single-channel design
locking L2 this cell would have read as a pass at α_bon; under L3 it would not. That is
`AUDIT-LENGTH-CHANNEL-EXPOSURE`'s standing correction working exactly as intended — and here it is
moot only because the cell is degenerate anyway.

**Tie fractions were measured on every cell.** C4: 0.0003 (permutation), 0.0001 (exact). C5: 0.000
in all nine cells. **None exceeded the 50% trigger, so no exact-test branch was required by ties**;
C4's exact enumeration was run anyway because it was feasible (8,575 and 36,015 configurations).

---

## 9. Power, MDE, and the S\* vs S_max branch

Computed unconditionally, per method `h-new-3030` §3.3 and §3.5, from the realised nulls:

| cell | S\* (smallest value rejecting at α_bon) | S_max | branch | MDE (80% power, exponential tilt) |
|:--|--:|--:|:--|--:|
| **C4** | 0.8182 | 1.0 | **not** UNTESTABLE | **F ≥ 0.881** |
| **C5** | 0.2619 | 2.0 | **not** UNTESTABLE | **Δρ ≥ 0.379** |

**The `UNTESTABLE-AT-THIS-N` branch did not fire for either cell** — both designs *could* have
rejected. But the MDEs are severe and should be read as the honest limit:

- **C4** needed the merged consonants to be **88% mustaʿliya/ḥalq by token mass** for 80% power.
  The corrected observed value is 47.2%. With only 10 of 28 consonants in the scoreable target set
  (§7.4) and a frequency-stratified null whose mean is 0.230, this design cannot resolve a moderate
  concentration — it can only detect a near-total one. **A negative C4 would have been weak
  evidence, and the corrected post-hoc value at percentile 91.1 with p = 0.089 is exactly the sort
  of moderate effect it is not built to see.**
- **C5**'s MDE of Δρ ≥ 0.379 is moot: with a control arm pinned at 1.0000 the cell has no
  operating characteristic at all.

---

## 10. What this does not claim

- It does **not** claim the muqaṭṭaʿāt 8/10 is wrong. It claims only that it reads no text.
- It does **not** claim `quran-transliteration.json` is defective *as a romanisation*. A
  reader-facing transliteration is entitled to merge ص with س. The finding is about what it can
  then be **used for** — and it cannot be used for any analysis touching the emphatic, interdental
  or pharyngeal contrasts, which is the project's entire OQ-1 signal axis (H-NEW-301's best
  2-feature subset is `mean_emphatic + mean_pharyngeal`).
- It does **not** discharge H-NEW-910's H5 grapheme-proxy residual. It establishes that the
  residual should be discharged **from the tashkeel**, and the transliteration is not required.
- It asserts **nothing about the Quran**. Every measurement here is a property of an encoding or
  of three Python files.

## 11. What a repaired lane must fix

1. **Alignment.** Either align at verse level on character streams (no token-count gate needed), or
   set the exclusion limit from a computed figure. The vocative-*yā* verses are 9.73% of tokens and
   are not a random 9.73%.
2. **Merger detection.** Use the counting-identity solve (§5), not whole-word confusability. Note
   the 1-decimal image-vector equality rule still misses {ح, ه}, because `h` is shared with the
   `th`/`kh`/`gh`/`sh` digraphs; that class was confirmed by an independent character-presence
   diagnostic and any repaired instrument must handle digraph-shared images explicitly.
3. **A non-degenerate control.** Any contrast arm must be checked for *variation*, not only for
   *independence from the treatment*. Add the check to the S-gate family: **a control that can
   only return one value is not a control.**
4. **Blindness.** §5 and the corrected C4 are post-hoc. A repaired lane must pre-register against
   them, and cannot claim them.

---

## 12. Artefacts

- `runs/h-new-3170/2026-08-09T110750Z/` — the pre-registered run: `result.json`,
  `pair-contrast-table.json` (all 378 consonant pairs), `surah-profiles.json` (114 surahs),
  `run.log`, `prereg.sha256`.
- `runs/h-new-3170-posthoc/2026-08-09T111240Z/` — the post-hoc character-map recovery:
  `result.json`, `addendum-full-partition.json`.
- `runs/h-new-3170-posthoc/2026-08-09T111218Z/` — **empty**. The first post-hoc attempt created
  its directory and then crashed on a name error before writing anything. **It is retained, not
  deleted**, per the standing rule that no run directory is ever removed.
- Every number in this document was machine-checked against these artefacts before publication.
  Two were wrong on the first pass and are corrected here: the short-vowel count (172,435 →
  **172,407**) and the length-channel p-swing (43× → **44×**).
- `scripts/verify-prereg-locks.sh` — 25 locks checked, 0 broken, including this lane's.

Related: [[cross-finding-029-the-deciding-parameter]] · [[cross-finding-030-three-ways-a-control-fails]] ·
[[AUDIT-TANWIN-DELETION-2690]] · [[AUDIT-WAQF-MARK-INVENTORY-DIVERGENCE]] ·
[[AUDIT-REGISTER-PROXY-ORTHOGRAPHY-DEPENDENCE]] · [[AUDIT-LENGTH-CHANNEL-EXPOSURE]] ·
[[h-new-165-phonological-predictor]] · [[h-new-232-oq1-singleton-nearest-neighbor]] ·
[[h-new-301-minimal-2feature-singleton]] · [[h-new-910-alif8-cluster]] ·
[[h-new-2990-verse-profile]] · [[PROXY-CLAIMS]]
