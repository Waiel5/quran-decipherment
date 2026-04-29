# H-NEW-270 Run 1 — Q11 Hūd opener-template lattice

**Date**: 2026-04-18  
**Agent**: codex  
**Seed**: 20260418  
**N_PERM**: 10,000  
**Bonferroni**: `k = 3`, `alpha_bon = 0.0167`  
**Verdict**: `PASS-DIRECTED`  
**Pre-reg SHA-256**: `b448899915e10c355e2d7446543a897d5ff8b74a6e0a96434d3fdc385bfb3767`

## Task

Land a formal H-NEW-270 follow-up around the already-noticed Q11 opener family
`wa-ila [tribe] akhahum [prophet]`, but keep it narrow and conservative:

- only a local Q11 claim
- explicit Bonferroni family
- positive control if feasible
- no uniqueness overclaim if Q7 also lights up

## Locked design that was actually run

### Target set

Frozen Q11 narrative-chain opener verses:

- `11:25`
- `11:50`
- `11:61`
- `11:69`
- `11:77`
- `11:84`
- `11:96`

### Statistic

For a fixed abstracted prefix depth `L`:

- abstract prophet names to `[PROPHET]`
- abstract tribe ethnonyms `عاد / ثمود / مدين` to `[TRIBE]`
- leave everything else literal
- compute `T_L = max multiplicity of an identical abstracted prefix among the
  opener set`

Three locked cells:

1. `L = 4`
2. `L = 8`
3. `L = 12`

### Null

Within the same surah:

- for each opener verse, find the nearest 12 non-opener verses by token count
- sample one matched verse per opener slot without replacement
- compute the same `T_L`
- repeat 10,000 times

### MW-5 positive control

Frozen Q7 sibling prophet-cycle opener verses:

- `7:59`
- `7:65`
- `7:73`
- `7:80`
- `7:85`
- `7:103`

MW-5 pass rule: all three cells nominal `p < 0.05`.

## Implementation

Created:

1. `scripts/h_new_270_hud_template_lattice.py`
2. prereg markdown
3. results markdown
4. `findings/phase-b-hypotheses/csv/h-new-270.json`
5. this journal

No non-owned files touched.

## Execution result

### Q11 target

| Cell | Prefix depth | Observed clique | Null mean | Null q95 | p_perm | z | Verdict |
|---|---:|---:|---:|---:|---:|---:|---|
| A | 4 | **3** | 1.0165 | 1 | **0.00010** | **15.57** | PASS |
| B | 8 | **3** | 1.0135 | 1 | **0.00010** | **17.21** | PASS |
| C | 12 | **3** | 1.0000 | 1 | **0.00010** | n/a | PASS |

`3/3` target cells pass Bonferroni.

Cell-C note:

- all `10,000 / 10,000` matched null draws had clique size `1`
- so the observed `3` is completely separated from the null tail
- z is not useful because `sd = 0`

### Winning Q11 clique

The same three verses define the target family in every cell:

- `11:50`
- `11:61`
- `11:84`

Winning abstracted prefixes:

- Cell A:
  `وإلى [TRIBE] أخاهم [PROPHET]`
- Cell B:
  `وإلى [TRIBE] أخاهم [PROPHET] قال يا قوم اعبدوا`
- Cell C:
  `وإلى [TRIBE] أخاهم [PROPHET] قال يا قوم اعبدوا الله ما لكم من`

## MW-5 positive control

| Cell | Observed clique | Null mean | p_perm | Verdict |
|---|---:|---:|---:|---|
| A | **3** | 1.0067 | **0.00010** | PASS |
| B | **3** | 1.0000 | **0.00010** | PASS |
| C | **3** | 1.0000 | **0.00010** | PASS |

MW-5 is clean. The instrument is responsive on the sibling Q7 cycle.

## Descriptive context

I also ran the same metric descriptively on three frozen comparator surahs:

| Surah | A | B | C |
|---|---|---|---|
| Q26 Ash-Shu'ara | `2 / 0.3394` | `2 / 0.3325` | `2 / 0.3362` |
| Q54 Al-Qamar | `1 / 1.0000` | `1 / 1.0000` | `1 / 1.0000` |
| Q71 Nuh | `1 / 1.0000` | `1 / 1.0000` | `1 / 1.0000` |

And Q7, the MW-5 control, ties Q11 on the target profile:

- `3 / 0.00010` in all three cells

So the final phrasing in the findings file needed to be:

- real Q11 local lattice
- not a uniqueness win over Q7

## Interpretation note

The run does what it was meant to do:

- it upgrades the visible Q11 formula family into a locked matched-null result
- it avoids the much stronger and less defendable claim that Q11 must be
  uniquely best over the whole Quran

The right close-out is therefore `PASS-DIRECTED`, with an explicit note that
Q7 matches the same family under the same instrument.

## Files written

1. `scripts/h_new_270_hud_template_lattice.py`
2. `findings/phase-b-hypotheses/h-new-270-hud-template-lattice-prereg.md`
3. `findings/phase-b-hypotheses/h-new-270-hud-template-lattice.md`
4. `findings/phase-b-hypotheses/csv/h-new-270.json`
5. `journal/h-new-270-run-1.md`
