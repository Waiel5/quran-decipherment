# [[h-new-197-prophet-cycle|H-NEW-197]] Pre-registration: Prophet-narrative parallelism across surahs

**Date:** 2026-04-17
**Seed:** 20260419
**Bonferroni k:** 2 (Moses cycle, Abraham cycle)
**Author:** autonomous agent ([[h-new-197-prophet-cycle|H-NEW-197]])

## Question

Are the same prophet-stories (Moses, Abraham) told in *syntactically parallel* ways across multiple surahs? Does the Quran's multi-telling strategy follow a common *sequential* narrative template?

## Data

Text source: `/Users/grey/Downloads/quran/quran-text/quran-min-tashkeel.json` (verse-indexed canonical corpus — one text, one numbering).

### Moses cycle surahs (pre-registered)
Q 7, 10, 11, 20, 26, 28, 79.

### Abraham cycle surahs (pre-registered)
Q 14, 19, 21, 26, 37.

## Operationalisation

### Step 1 — narrative events (atoms)

For each narrative we pre-register a fixed ordered list of *event-atoms*, each detected by a surface-form regex on min-tashkeel verse text. An atom "fires" in verse v if its regex matches.

**Text normalisation (frozen before analysis):** strip all combining marks (U+0610–U+061A, U+064B–U+065F, U+0670, U+06D6–U+06ED); merge alef-variants (أ إ آ ٱ → ا); merge alef-maqsura (ى → ي); merge ta marbuta (ة → ه). Apply same normalisation to needle and haystack.

**Moses atoms** (ordered canonically as commonly narrated):

| code | description | regex terms (min-tashkeel, substring OR) |
|---|---|---|
| MU | Moses named | موسى |
| FR | Pharaoh named | فرعون |
| RB | "your/our lord" invocation near Moses | ربك\|ربنا\|ربي |
| SG | signs / āyāt | ءاي\|اٰي\|بِآي |
| ST | staff/rod / serpent | عصا\|حية\|ثعبان\|حيّ |
| HA | hand (white hand) | يد\|بيضاء |
| SO | sorcerers / magicians | سحر\|ساحر\|سحرة |
| SE | sea / drowning | بحر\|غرق\|يم |
| CH | children of Israel | بني اسر\|بنى اسر\|اسراءيل |
| CA | calf | عجل |
| MT | mountain / Tur / tablets | طور\|الواح |

**Abraham atoms** (ordered canonically):

| code | description | regex terms |
|---|---|---|
| IB | Abraham named | ابرٰه\|إبراهيم\|ابراهيم |
| FT | father / Azar | ابي\|أبي\|ابيه\|اباه\|ءازر |
| ID | idols / images | اصنام\|تماثيل\|وثن |
| ST | stars / sun / moon | نجم\|شمس\|قمر\|كوكب |
| FI | fire / burning | نار\|حرق |
| SC | son / sacrifice / Isma/Ishaq | اسمٰع\|اسحٰق\|ذبح\|غلٰم\|ذِبْح |
| GU | guests / visitors | ضيف\|رسلنا\|المرسلون |
| PR | prayer / station of Abraham | مقام\|دعاء\|ادع |
| HA | Hajj / house / Ka'ba | بيت\|حج\|كعب\|قبل |
| LO | Lot / overthrown cities | لوط\|مؤتفك |

### Step 2 — extract per-surah event sequence

For each target surah S, iterate over its verses in order. For verses that contain the prophet-anchor (MU for Moses; IB for Abraham), record the ordered sequence of *atom codes that appear in the local window* (the verse itself plus previous/next verse). Collapse repeats of the same atom if adjacent (ABA stays ABA; AAB becomes AB). This yields an ordered string per surah, e.g. `MU FR SG ST SO CH SE` .

We only keep verses that contain the anchor OR are within ±1 verse of an anchor verse, to stay inside the narrative block.

### Step 3 — inter-surah alignment score

For each pair (S_i, S_j) of the pre-registered surahs, compute normalised Levenshtein similarity on their atom-code strings:

`sim(i,j) = 1 - edit_distance(s_i, s_j) / max(|s_i|,|s_j|)`

Cycle score = mean sim over all pairs.

### Step 4 — null distribution

Null model A (primary): within each surah, shuffle the *verse-level atom bags* (i.e. keep which atoms fire in each verse but randomly reorder the kept verses). Recompute per-surah sequence and mean pairwise sim. Repeat 2000 times.

Null model B (sanity): shuffle atom codes uniformly within each surah's string (permuting letters). Repeat 2000 times.

Primary test uses Null A. p-value = (1 + #null ≥ observed) / (1 + 2000).

### Step 5 — decision rule

With Bonferroni k=2: reject null for a cycle iff p_A < 0.025.

- **STRONG**: both cycles p_A < 0.025 AND observed mean sim ≥ 0.50.
- **MODERATE**: one cycle passes with observed mean sim ≥ 0.50.
- **NULL**: neither cycle passes, OR both pass but observed sim < 0.40 (significance without substantive effect).

## Garden of forking paths

Alternatives considered & locked-out:
- **Window size** pre-registered at ±1 verse; no post-hoc widening.
- **Collapsing policy**: only *adjacent* repeats collapsed; non-adjacent repeats preserved.
- **Similarity metric**: normalised Levenshtein locked in; not switching to LCS or n-gram after seeing result.
- **Atom list**: frozen above; no additions post-hoc.
- **Surah lists**: frozen above. Q 79 retained for Moses despite being short.
- Null A is primary (more conservative); Null B reported for diagnostics.

Seed: `numpy.random.default_rng(20260419)` for both nulls.

## Outputs

- `findings/phase-b-hypotheses/h-new-197-prophet-cycle.md` — findings doc
- `findings/phase-b-hypotheses/h-new-197-work/moses_sequences.tsv`, `abraham_sequences.tsv`, `pairwise_sim.tsv`
- `scripts/h_new_197_prophet_cycle.py`
