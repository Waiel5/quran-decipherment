---
id: H-NEW-270
title: "Q11 Hud opener-template lattice"
status: PRE-REGISTERED 2026-04-18
date_prereg: 2026-04-18
seed: 20260418
bonferroni_family: h-new-270-hud-template-lattice
bonferroni_k: 3
alpha_bon: 0.0167
n_perm: 10000
match_k_nearest: 12
rules_tuple: "(quran-no-tashkeel; frozen Q11 narrative-chain opener verses 11:25/50/61/69/77/84/96; Arabic-token regex extraction; slot abstraction on prophet names and tribe ethnonyms only; statistic = max multiplicity of identical abstracted prefix among opener verses; matched null = within-surah nearest-12 by token count sampled without replacement; MW-5 = Q7 sibling prophet-cycle openers)"
prior_work_consulted:
  - findings/phase-c-structures/h-new-90-kahf-narrative-structure.md
  - HANDOFF/03-NEXT-MOVES.md
  - findings/phase-b-hypotheses/h-new-132-prophet-cycle-parallelism.md
verdict_ceiling: PASS-DIRECTED
---

# [[h-new-270-hud-template-lattice|H-NEW-270]] — Q11 Hūd opener-template lattice

## Question

Does the fixed Q11 Hūd narrative chain contain a **non-random repeated opener
template** of the visible `wa-ila [tribe] akhahum [prophet]` type, once we test
it against a bounded within-surah matched null rather than merely noticing the
surface repetition?

This is intentionally narrow. It does **not** ask whether Q11 is the unique
prophet-cycle surah, whether the whole Quran uses one prophet opener formula,
or whether the rhetorical mechanism is independent of narrative content. It
asks one local question about the opener verses of one frozen chain in Q11.

## Provenance disclosure

This is a **formal follow-up**, not a blind discovery study.

- [[h-new-90-kahf-narrative-structure|H-NEW-90]] already noted that Q11, not Q18, carried the strongest
  opener-formula signal in that run's small comparator set.
- HANDOFF NM-20 explicitly proposed a Q11 Hūd
  `wa-ila [tribe] akhahum [prophet]` follow-up.

Before locking this prereg I inspected the raw Arabic opener verses needed to
freeze the verse sets and confirm that the visible repeated family really is
present. I did **not** inspect the matched-null permutation p-values, the
within-surah candidate-list outcomes, or the final Bonferroni pass/fail table.

Because the family was already noticed qualitatively, the ceiling here is
**PASS-DIRECTED**, not stronger "discovery-confirmed" language.

## Frozen verse sets

### Target set: Q11 narrative-chain openers

Use the first verse of each frozen opener block in the Hūd narrative chain:

- 11:25 Nūḥ
- 11:50 Hūd
- 11:61 Ṣāliḥ
- 11:69 Ibrāhīm
- 11:77 Lūṭ
- 11:84 Shuʿayb
- 11:96 Mūsā

These seven verses are fixed as a set before execution. The design does **not**
permit post-hoc dropping the "non-fitting" entries (e.g. Ibrāhīm or Lūṭ) to
inflate homogeneity.

### MW-5 positive control: Q7 sibling prophet-cycle openers

Use the first verse of each frozen prophet block in Q7:

- 7:59 Nūḥ
- 7:65 Hūd
- 7:73 Ṣāliḥ
- 7:80 Lūṭ
- 7:85 Shuʿayb
- 7:103 Mūsā

Rationale: Q7 already serves in prior repo work as the nearest sibling
prophet-cycle surah, and it visibly contains the same `wa-ila [tribe] akhahum
[prophet]` triad for Hūd / Ṣāliḥ / Shuʿayb. If the template-extraction plus
matched-null machinery cannot recover this control at nominal level, the
instrument is mis-specified.

## Text and normalization

- Corpus: `quran-text/quran-no-tashkeel.json`
- Verse tokenization: Arabic-word regex over `ء..ي` plus `ٱ`
- Punctuation and waqf markers are ignored by construction because only Arabic
  word tokens are retained

### Slot abstraction

Each retained token is left unchanged **except**:

- prophet names -> `[PROPHET]`
- tribe ethnonyms `عاد / ثمود / مدين` -> `[TRIBE]`

No further abstraction is allowed:

- `قوم` remains literal
- speech verbs are not conflated
- other groups (`فرعون`, `الأيكة`, etc.) are not abstracted for the inferential
  target

This keeps the operationalization conservative and close to the visible family.

## Statistic family

For a set of opener verses and a fixed prefix depth `L`:

1. abstract each verse token stream by the locked slot rules
2. truncate to the first `L` abstracted tokens
3. count how many opener verses share each exact truncated template
4. record

`T_L = max_template_multiplicity`

Interpretation: the size of the largest exact opener-template clique at depth
`L`.

Direction for every cell: **one-sided upper**.

## Bonferroni cells

Three nested cells are locked in advance:

### Cell A — bare slot-template stem

- `L = 4`
- target family:
  `wa-ila [TRIBE] akhahum [PROPHET]`

### Cell B — vocative-imperative continuation

- `L = 8`
- target family:
  `wa-ila [TRIBE] akhahum [PROPHET] qala ya qawm u'budu`

### Cell C — monotheism-clause continuation

- `L = 12`
- target family:
  `wa-ila [TRIBE] akhahum [PROPHET] qala ya qawm u'budu Allah ma lakum min`

The nesting is intentional and disclosed. Bonferroni treats them as three
separate inferential cells even though they are strongly correlated.

## Null model

The null is intentionally **local to Q11**.

For each cell separately:

1. Keep the target opener-count fixed (`n = 7` for Q11).
2. For each opener verse, compute its raw Arabic token count.
3. Among the **non-opener** verses of the same surah, rank candidates by:
   - absolute token-count difference
   - then absolute verse-index distance
   - then verse number
4. Keep the nearest `k = 12` candidate verses for that opener.
5. Draw one candidate for each opener slot **without replacement**, greedily
   filling the most constrained slot first.
6. Compute the same `T_L` statistic on the sampled 7-verse set.
7. Repeat `N_PERM = 10000`.

This null asks: if we take other Q11 verses of roughly the same lengths, do we
typically obtain a template clique as large as the frozen opener set?

### Why this null

- It stays local to Q11 instead of turning a narrow follow-up into a
  whole-Quran discovery hunt.
- It controls the most obvious nuisance variable: short formulaic verses are
  more likely to share prefixes.
- It avoids the stronger and shakier claim that Q11 must beat every other
  prophet-narrative surah to count as a real local lattice.

## MW-5 positive control rule

Run the exact same three cells and matched-null procedure on the frozen Q7
opener set.

**MW-5 passes** iff all three Q7 cells satisfy nominal `p_perm < 0.05`.

If MW-5 fails on any cell, overall verdict becomes `NULL-BROKEN`.

## Comparator disclosure

The following surahs may be reported descriptively on the same metric, but they
are **not** counted in the Bonferroni family and do not affect the verdict:

- Q26 Ash-Shu'ara
- Q54 Al-Qamar
- Q71 Nuh

These are included only to contextualize how "Q11 lattice" should be phrased
after the run. No inferential claim of Quran-wide uniqueness is made here.

## Decision rule

Per cell:

- PASS iff `p_perm < 0.0167`

Overall:

- MW-5 failure on any cell -> `NULL-BROKEN`
- 0/3 target cells PASS with MW-5 valid -> `NULL`
- 1-2/3 target cells PASS with MW-5 valid -> `PARTIAL-PASS`
- 3/3 target cells PASS with MW-5 valid -> `PASS-DIRECTED`

## What is frozen after lock

- the Q11 target verse set
- the Q7 MW-5 verse set
- the three prefix depths `L = 4, 8, 12`
- the abstraction vocabulary (`[PROPHET]`, `[TRIBE]` only)
- `T_L = max_template_multiplicity`
- nearest-12 within-surah token-count null
- `N_PERM = 10000`
- Bonferroni `k = 3`

Not allowed after lock:

- dropping Ibrāhīm / Lūṭ / Mūsā because they weaken the target
- widening the abstraction dictionary
- switching to longest-common-prefix length, edit distance, embeddings, or
  Jaccard after results
- promoting descriptive comparator ranks to inferential support

## Honest limits to report

- The visible family was already known qualitatively; this run formalizes it
  under a locked null rather than claiming first discovery.
- The three cells are nested and highly correlated; Bonferroni is conservative
  but does not create three independent discoveries.
- The null controls verse length, not all discourse or syntax variables.
- A PASS here would support a **local opener-template lattice in Q11**, not a
  uniqueness claim over the whole Quran.

## Deliverables

1. `scripts/h_new_270_hud_template_lattice.py`
2. `findings/phase-b-hypotheses/h-new-270-hud-template-lattice-prereg.md`
3. `findings/phase-b-hypotheses/h-new-270-hud-template-lattice.md`
4. `findings/phase-b-hypotheses/csv/h-new-270.json`
5. `journal/h-new-270-run-1.md`
