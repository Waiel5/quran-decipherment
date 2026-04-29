# h-new-266-run-1

**Date**: 2026-04-18  
**Task**: land `H-NEW-266`, a formal per-surah phonological signature test  
**Outcome**: **PASS-DIRECTED**  
**Pre-reg**: `findings/phase-b-hypotheses/h-new-266-per-surah-phonological-signature-prereg.md`  
**Pre-reg SHA-256**: `e561b4c4e35502f93513add5f02c2684c32f3c3a084fd1831f06a73013ba8f5f`

## Scope kept tight

Per user steer, I kept this landing narrow:

- one locked prereg
- one executable script
- one JSON result
- one findings note
- one run journal

No exploratory follow-on cells were added after the prereg.

## Locked design

- Family: 1 omnibus + 4 class-specific density-dispersion cells
- Classes:
  - core emphatic `{ص ض ط ظ}`
  - strict throat `{ع ح خ غ}`
  - ṣafīr `{س ز ص}`
  - idghām-sonorant `{ي ر م ل و ن}`
- Null: exact surah-length-preserving random repartition of the normalized
  Quran letter inventory
- Bonferroni: `k=5`, `alpha_bon=0.01`
- MW-5: synthetic planted four-block control

## Execution

I implemented `scripts/h_new_266_per_surah_phonological_signature.py` and ran it
once after the prereg was written.

There was one concrete implementation bug on first execution:

- the sequential sampler incorrectly allowed earlier category leftovers to stay
  in the within-surah "bad" pool for later category draws
- this produced `ValueError: nbad < 0`
- I patched the sampler without changing the prereg, then reran successfully

No blocker remained after the fix.

## Result

| Cell | Observed | Null q95 | p_perm | Verdict |
|---|---:|---:|---:|---|
| Omnibus | **0.032127** | 0.022831 | **0.0002** | **PASS** |
| Core emphatic | 0.005073 | 0.004812 | 0.0142 | NULL |
| Strict throat | 0.007749 | 0.008104 | 0.1264 | NULL |
| Ṣafīr sibilant | **0.007480** | 0.006184 | **0.0002** | **PASS** |
| Idghām-sonorant | **0.026975** | 0.018135 | **0.0002** | **PASS** |

Overall verdict: **PASS-DIRECTED**.

Reason:

- primary omnibus cell passed strongly
- 2 of 4 localizer cells passed
- MW-5 passed

## MW-5

Synthetic positive control passed all 5 cells:

- omnibus `p=0.0010`
- emphatic `p=0.0010`
- throat `p=0.0010`
- ṣafīr `p=0.0010`
- idghām-sonorant `p=0.0010`

This clears the prereg rule (`omnibus + at least 3/4 localizers`), so the null
is not broken.

## Notes for ledger framing

- The safest summary is: **surahs carry non-random sound-signature dispersion on
  this locked family, especially on ṣafīr and idghām-sonorant densities**.
- Avoid overselling emphatic and throat structure; they did not survive the
  family correction.
- Keep the mechanism claim modest: this is a random-repartition null, not a
  content-controlled causal test.

## Files shipped

- `scripts/h_new_266_per_surah_phonological_signature.py`
- `findings/phase-b-hypotheses/h-new-266-per-surah-phonological-signature-prereg.md`
- `findings/phase-b-hypotheses/h-new-266-per-surah-phonological-signature.md`
- `findings/phase-b-hypotheses/csv/h-new-266.json`
- `journal/h-new-266-run-1.md`
