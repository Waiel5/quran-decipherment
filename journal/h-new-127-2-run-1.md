# H-NEW-127.2 run 1 journal

- Date: 2026-04-18
- Pre-reg: `/Users/grey/Downloads/quran/findings/phase-b-hypotheses/h-new-127-2-rerun-prereg.md`
- Pre-reg SHA-256: `d5fef06982648aa8a4cf35c470c67d9f34aae3b61597692b73736e25482f73a1`
- Script: `scripts/h_new_127_2_oq20_family_rerun.py`
- Output: `/Users/grey/Downloads/quran/findings/phase-b-hypotheses/csv/h-new-127-2.json`
- Family lock: Q1/Q18/Q28/Q78/Q112 uniform full-verse null

## Commands

```bash
python3 scripts/h_new_127_2_oq20_family_rerun.py
```

## Result

- `n_pass = 3 / 5`
- control bank pass = `True`
- family verdict = `POSITIVE`

## Locked per-surah results

| Sura | n_v | null model | L_canon | null μ | null σ | z | p | pass | L_greedy_best | L_2opt_best |
|------|-----|------------|---------|--------|--------|---|---|------|---------------|-------------|
| 1 | 7 | uniform_full_verse_permutation | 1.161789 | 1.218288 | 0.056468 | -1.000550 | 0.204779522048 | FAIL | 1.076481 | 1.076481 |
| 18 | 110 | uniform_full_verse_permutation | 32.416877 | 33.436290 | 0.211122 | -4.828546 | 0.000099990001 | PASS | 27.620872 | 26.817875 |
| 28 | 88 | uniform_full_verse_permutation | 27.251392 | 28.674068 | 0.190346 | -7.474145 | 0.000099990001 | PASS | 24.390358 | 23.666976 |
| 78 | 40 | uniform_full_verse_permutation | 5.738927 | 6.433836 | 0.103936 | -6.685926 | 0.000099990001 | PASS | 5.094744 | 5.070426 |
| 112 | 4 | uniform_full_verse_permutation | 0.468030 | 0.480444 | 0.031545 | -0.393525 | 0.505349465053 | FAIL | 0.428105 | 0.428105 |


## Control bank

- Greedy-NN shorter than canonical on all five surahs: `True`
- 2-opt shorter than canonical on all five surahs: `True`

## Immediate interpretation

The rerun keeps the same Fisher-Rao verse-path family as H-NEW-127.1, but
switches to the alternate locked five-surah family named in the parent note.
The geometric control bank passes, so the family verdict is determined by the
pre-registered `n_pass` rule.
