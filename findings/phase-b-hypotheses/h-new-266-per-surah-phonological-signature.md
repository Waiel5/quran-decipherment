# [[h-new-266-per-surah-phonological-signature|H-NEW-266]] — Per-surah phonological signature test

**Finding ID**: [[h-new-266-per-surah-phonological-signature|h-new-266]]  
**Date**: 2026-04-18  
**Pre-reg**: `findings/phase-b-hypotheses/h-new-266-per-surah-phonological-signature-prereg.md`  
**Pre-reg SHA-256**: `e561b4c4e35502f93513add5f02c2684c32f3c3a084fd1831f06a73013ba8f5f`  
**Seed**: `20260418`  
**Rules tuple**: `(quran-no-tashkeel, 28-letter orthographic normalization, exact surah letter counts preserved, 114 surahs, Hafs-Kufan)`  
**Bonferroni**: `k=5`, `alpha_bon=0.01`, `N_perms=5000`  
**Verdict**: **PASS-DIRECTED**

## Headline

On the locked 4-class family, the Quran's surahs show **more phonological
signature dispersion than expected under a length-matched random repartition
null**. The omnibus per-surah signature statistic passes strongly, and 2 of the
4 preregistered localizer cells also pass after Bonferroni correction:

- **Omnibus**: PASS
- **Ṣafīr sibilant density**: PASS
- **Idghām-sonorant density**: PASS
- **Core emphatic density**: NULL
- **Strict throat density**: NULL

This is a **bounded positive result**. It supports non-random surah-level
sound-signature structure on this small locked family, but it does **not**
license a stronger claim that every classical phonological class is structured
or that the signal is independent of lexical content.

## Primary numbers

### Bonferroni family (5 cells, alpha_bon = 0.01)

| Cell | Statistic | Observed | Null mean | Null q95 | p_perm | Verdict |
|---|---:|---:|---:|---:|---:|---|
| A | Omnibus mean L2 signature radius | **0.032127** | 0.020705 | 0.022831 | **0.0002** | **PASS** |
| B | Core emphatic mean abs deviation | 0.005073 | 0.004178 | 0.004812 | 0.0142 | NULL |
| C | Strict throat mean abs deviation | 0.007749 | 0.007015 | 0.008104 | 0.1264 | NULL |
| D | Ṣafīr sibilant mean abs deviation | **0.007480** | 0.005323 | 0.006184 | **0.0002** | **PASS** |
| E | Idghām-sonorant mean abs deviation | **0.026975** | 0.015729 | 0.018135 | **0.0002** | **PASS** |

Interpretation:

- The omnibus signal is decisive: observed surah signatures are about **55%**
  above the null mean (`0.032127 / 0.020705 ≈ 1.55`).
- The strongest localizer is **idghām-sonorant dispersion**, followed by
  **ṣafīr dispersion**.
- **Core emphatic** dispersion trends positive but misses Bonferroni.
- **Strict throat** dispersion does not survive even nominally strong
  correction; on this null, throat-density heterogeneity is not unusually high
  at the family threshold.

## MW-5 positive control

The preregistered synthetic four-block control **passed cleanly**, so the null
is not broken.

| Cell | Observed | Null q95 | p_perm | Verdict |
|---|---:|---:|---:|---|
| Omnibus | 0.055027 | 0.024682 | 0.0010 | PASS |
| Core emphatic | 0.019996 | 0.006664 | 0.0010 | PASS |
| Strict throat | 0.023917 | 0.009287 | 0.0010 | PASS |
| Ṣafīr sibilant | 0.020355 | 0.007829 | 0.0010 | PASS |
| Idghām-sonorant | 0.029319 | 0.018244 | 0.0010 | PASS |

MW-5 rule required omnibus PASS plus at least 3 of 4 class cells PASS.
Observed: **5/5 PASS**.

## Descriptive outliers

These are descriptive only; they were not separate inferential cells.

- **Q 114 al-Nās** is the most extreme positive ṣafīr-surah in the corpus on
  this pipeline: density `0.1375` vs null mean `0.02866`, `z = +5.884`.
- **Q 26 al-Shuʿarāʾ** is the strongest positive idghām-sonorant outlier:
  density `0.501514` vs null mean `0.473478`, `z = +4.307`.
- **Q 55 al-Raḥmān** is descriptively low on both strict throat and
  idghām-sonorant density in this normalization:
  throat `z = -3.921`, sonorant `z = -6.168`.
- **Q 18 al-Kahf** is the most negative idghām-sonorant outlier:
  density `0.433390` vs null mean `0.473571`, `z = -6.651`.

These rows are useful for texture, but the finding itself rests on the
pre-registered family table above.

## Interpretation

The cleanest reading is:

- **Surah boundaries are not phonologically interchangeable** under this locked
  family.
- The excess structure is carried mainly by **sibilant** and
  **sonorant/idghām** concentration patterns, not by a broad "all guttural/all
  emphatic" effect.
- The result is compatible with a mixed literary mechanism: lexical and
  rhetorical concentration, sajʿ texture, and recurring recitational templates
  can all generate surah-level class-density signatures relative to a random
  repartition null.

So `[[h-new-266-per-surah-phonological-signature|H-NEW-266]]` should be framed as a **real but narrow** positive: surahs have
non-random sound-signature structure on this small classical-tajwid-relevant
family, but the family is selective and the mechanism remains open.

## Honest limits

- This is an **orthography-derived** phonological proxy, not a full recitation
  or IPA model.
- The null preserves length and global inventory, but it intentionally destroys
  lexical, morphological, and semantic structure. A PASS therefore shows
  non-random concentration relative to random repartition, not independence from
  vocabulary.
- Equal weighting across the 114 surahs gives short surahs the same weight as
  long surahs in the dispersion statistic. That is appropriate for a per-surah
  question but makes the statistic sensitive to the short tail.
- The 4 class cells are correlated. Bonferroni is conservative; no effective-k
  reduction is claimed.
- Glottal handling was intentionally excluded from the locked family because
  the 28-letter normalization used here is less stable for a glottal-class test.

## Bottom line

`[[h-new-266-per-surah-phonological-signature|H-NEW-266]]` lands as **PASS-DIRECTED**:

- omnibus per-surah phonological signature dispersion: **PASS**
- localizers: **2/4 PASS** (`ṣafīr`, `idghām-sonorant`)
- MW-5 positive control: **PASS**

The result is publishable as a conservative surah-level sound-signature finding
with explicit limits.
