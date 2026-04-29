---
id: H-NEW-270
title: "Q11 Hud opener-template lattice"
status: PASS-DIRECTED — 3/3 Bonferroni cells PASS; Q7 MW-5 positive control valid on all 3 cells
date: 2026-04-18
agent: codex
prereg: findings/phase-b-hypotheses/h-new-270-hud-template-lattice-prereg.md
script: scripts/h_new_270_hud_template_lattice.py
json: findings/phase-b-hypotheses/csv/h-new-270.json
journal: journal/h-new-270-run-1.md
seed: 20260418
n_perm: 10000
bonferroni_family: h-new-270-hud-template-lattice
bonferroni_k: 3
alpha_bon: 0.0167
rules_tuple: "(quran-no-tashkeel; frozen Q11 opener verses 11:25/50/61/69/77/84/96; prophet-name + tribe slot abstraction only; statistic = max multiplicity of identical abstracted prefix; within-surah nearest-12 token-count matched null)"
---

# [[h-new-270-hud-template-lattice|H-NEW-270]] — Q11 Hūd opener-template lattice

## Headline

Q11 Hūd does contain a **real local opener-template lattice** under the locked
[[h-new-270-hud-template-lattice|H-NEW-270]] design.

Across all three preregistered prefix depths, the frozen Q11 narrative-chain
openers produce the same three-verse clique:

- **11:50** Hūd
- **11:61** Ṣāliḥ
- **11:84** Shuʿayb

Those three verses share the exact abstracted opener family
`wa-ila [TRIBE] akhahum [PROPHET]`, and the clique survives unchanged when the
prefix is extended through:

- `qala ya qawm u'budu`
- `Allah ma lakum min`

Against the within-Hūd length-matched verse-set null, **all 3 Bonferroni cells
pass**.

This is a **PASS-DIRECTED** result, not a uniqueness claim. The same instrument
also lights up the sibling Q7 control; so the honest reading is:

**Q11 really has the lattice, but Q11 is not uniquely alone in having it.**

## Locked target result

Statistic in every cell:

- `T_L = max multiplicity of an identical abstracted prefix among the 7 frozen
  Q11 opener verses`
- one-sided upper test against 10,000 within-surah matched 7-verse draws

### Bonferroni family (`k = 3`, `alpha_bon = 0.0167`)

| Cell | Prefix depth | Observed max clique | Null mean | Null q95 | p_perm | z vs null | Verdict |
|---|---:|---:|---:|---:|---:|---:|---|
| A | 4 | **3** | 1.0165 | 1 | **0.00010** | **15.57** | **PASS** |
| B | 8 | **3** | 1.0135 | 1 | **0.00010** | **17.21** | **PASS** |
| C | 12 | **3** | 1.0000 | 1 | **0.00010** | n/a | **PASS** |

Cell-C note: the matched null is degenerate at depth 12 (`10,000 / 10,000`
null draws had max clique = 1), so a standard z-score is not informative. The
cell passes because **no** null draw reached the observed three-verse clique.

## What the winning template actually is

The winning abstracted prefixes are:

- **Cell A, 4 tokens**:
  `وإلى [TRIBE] أخاهم [PROPHET]`
- **Cell B, 8 tokens**:
  `وإلى [TRIBE] أخاهم [PROPHET] قال يا قوم اعبدوا`
- **Cell C, 12 tokens**:
  `وإلى [TRIBE] أخاهم [PROPHET] قال يا قوم اعبدوا الله ما لكم من`

The same three target verses carry the clique in all cells:

1. `11:50`
2. `11:61`
3. `11:84`

The other frozen Q11 chain-openers were retained in the target set and did
**not** need to be dropped post hoc:

- `11:25` Nūḥ
- `11:69` Ibrāhīm
- `11:77` Lūṭ
- `11:96` Mūsā

That matters. [[h-new-270-hud-template-lattice|H-NEW-270]] is not just counting the three visibly matching verses
in isolation; it asks whether the full frozen chain contains a clique unusually
large for other Hūd verses of similar lengths.

## MW-5 positive control

MW-5 used the fixed Q7 sibling prophet-cycle opener set:

- `7:59, 7:65, 7:73, 7:80, 7:85, 7:103`

Pass rule: all three cells must satisfy nominal `p < 0.05`.

### Q7 MW-5 results

| Cell | Observed max clique | Null mean | p_perm | Verdict |
|---|---:|---:|---:|---|
| A | **3** | 1.0067 | **0.00010** | PASS |
| B | **3** | 1.0000 | **0.00010** | PASS |
| C | **3** | 1.0000 | **0.00010** | PASS |

So the extractor and null are responsive on the nearest sibling surah. This is
not a broken pipeline accidentally returning positives.

## Descriptive comparator context

These rows are contextual only; they were not Bonferroni-counted.

| Surah | Opener set size | Cell A clique / p | Cell B clique / p | Cell C clique / p |
|---|---:|---|---|---|
| **Q7 Al-A'raf** | 6 | **3 / 0.00010** | **3 / 0.00010** | **3 / 0.00010** |
| **Q11 Hud** | 7 | **3 / 0.00010** | **3 / 0.00010** | **3 / 0.00010** |
| Q26 Ash-Shu'ara | 7 | 2 / 0.3394 | 2 / 0.3325 | 2 / 0.3362 |
| Q54 Al-Qamar | 5 | 1 / 1.0000 | 1 / 1.0000 | 1 / 1.0000 |
| Q71 Nuh | 1 | 1 / 1.0000 | 1 / 1.0000 | 1 / 1.0000 |

This is the key scope note:

- Q11 does **not** stand alone; Q7 ties it under this instrument.
- But Q11 also does **not** collapse into a generic prophet-narrative effect,
  since Q26 / Q54 / Q71 do not show the same template-clique profile here.

## Interpretation

The conservative reading is:

- **Yes**: Q11 Hūd contains a formally recoverable opener-template lattice.
- **No**: [[h-new-270-hud-template-lattice|H-NEW-270]] does not justify saying Q11 is uniquely the Quran's lone
  holder of that lattice.

The result therefore sharpens the handoff note rather than overturning it. The
visible `wa-ila [tribe] akhahum [prophet]` triad in Q11 is not just a casual
eyeballing artifact; it remains statistically exceptional relative to other
Hūd verses of the same approximate lengths. But the same local pattern also
appears in the sibling Q7 prophet-cycle, so the best label is **real local
lattice, not uniqueness win**.

## Honest limits

1. This is a **post-hoc formalization** of an already-noticed visible family.
   The prereg locks the null and the decision rule, but it does not erase that
   the family was first seen qualitatively.

2. The null is **within-surah** and **length-matched**, which is appropriate
   for a local Q11 claim. It does not prove that Q11 beats every possible
   Quran-wide comparator under every alternative metric.

3. The three Bonferroni cells are nested and highly correlated. They show depth
   stability of one family, not three independent discoveries.

4. The abstraction is intentionally minimal: only prophet names and tribe names
   were slotted. Different abstraction rules could change cross-surah
   comparators, which is exactly why they were frozen here and not widened
   after the fact.

## Verdict

**PASS-DIRECTED.** Under the locked within-Hūd matched-null design, the frozen
Q11 narrative-chain openers contain a stable three-verse
`wa-ila [TRIBE] akhahum [PROPHET]` lattice that survives at all three
pre-registered prefix depths (`p = 0.00010` in each cell), with a clean Q7
positive control and clear disclosure that the effect is **not unique to Q11**.
