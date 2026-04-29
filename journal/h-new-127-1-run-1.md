# H-NEW-127.1 run 1 journal

- Date: 2026-04-18
- Pre-reg: `/Users/grey/Downloads/quran/findings/phase-b-hypotheses/h-new-127-1-rerun-prereg.md`
- Pre-reg SHA-256: `5f11a6995be0faf68a9b27f83d8799f824aa5f1c6172c034c481fe9be5525b6b`
- Script: `scripts/h_new_127_1_oq20_family_rerun.py`
- Output: `/Users/grey/Downloads/quran/findings/phase-b-hypotheses/csv/h-new-127-1.json`
- Family lock: Q2/Q7/Q12/Q36 uniform full-verse null; Q55 fixed-refrain-slot null

## Commands

```bash
python3 scripts/h_new_127_1_oq20_family_rerun.py
```

## Result

- `n_pass = 4 / 5`
- control bank pass = `True`
- family verdict = `POSITIVE`

## Locked per-surah results

| Sura | n_v | null model | L_canon | null μ | null σ | z | p | pass | L_greedy_best | L_2opt_best |
|------|-----|------------|---------|--------|--------|---|---|------|---------------|-------------|
| 2 | 286 | uniform_full_verse_permutation | 104.301933 | 108.497535 | 0.406264 | -10.327271 | 0.000099990001 | PASS | 87.676814 | 85.718611 |
| 7 | 206 | uniform_full_verse_permutation | 65.805001 | 68.270149 | 0.304785 | -8.088166 | 0.000099990001 | PASS | 55.818742 | 54.297138 |
| 12 | 111 | uniform_full_verse_permutation | 32.794547 | 34.265214 | 0.218188 | -6.740365 | 0.000099990001 | PASS | 28.503595 | 27.885987 |
| 36 | 83 | uniform_full_verse_permutation | 19.129451 | 19.519040 | 0.135554 | -2.874044 | 0.003999600040 | PASS | 16.370041 | 15.840863 |
| 55 | 78 | fixed-refrain-slot | 13.639165 | 13.693339 | 0.118168 | -0.458439 | 0.312168783122 | FAIL | 5.672339 | 5.501191 |


## Control bank

- Greedy-NN shorter than canonical on all five surahs: `True`
- 2-opt shorter than canonical on all five surahs: `True`
- Q55 refrain positions verified against H-NEW-83: `True`

## Immediate interpretation

The rerun keeps the original five surahs from H-NEW-127, but repairs the Q55
null with the H-NEW-280 fixed-refrain-slot construction. The geometric control
bank passes, so the family verdict is determined by the locked `n_pass` rule.
