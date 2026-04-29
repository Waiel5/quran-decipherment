---
agent: h-new-84-specialist
hypothesis_id: H-NEW-84
run: 1
date: 2026-04-15
seed: 20260417
status: COMPLETED
verdict: REFUTED-STRONG (0/7 axes PASS by locked criterion); Axis 5 borderline (0.3725 vs band [0.30, 0.37])
---

# H-NEW-84 run 1 journal — Sūrat al-Ikhlāṣ "1/3 of the Quran"

## Procedure

1. **Pre-registration locked** at `findings/phase-b-hypotheses/h-new-84-ikhlas-third-prereg.md`
   - 7 axes, Bonferroni k=7, α_bon = 0.00714
   - PASS criterion: per-axis ratio ∈ [0.30, 0.37] (±10% around 1/3)
   - Overall: ≥3 PASS for PASS-WEAK, ≥5 for PASS-STRONG, 1-2 REFUTED-WEAK, 0 REFUTED-STRONG
   - Garden-of-forking-paths log committed BEFORE running script
   - Disclosure: literal length-ratio (Axis 1) is 0.000142 (1/7,038), known a priori to fail catastrophically; included for completeness

2. **Script written**: `scripts/h_new_84_ikhlas_third.py`
   - Loads `quran-text/quran-no-tashkeel.json` (114 surahs, 6236 verses)
   - Loads Leeds Quranic Arabic Corpus 0.4 morphology (128,219 segment rows)
   - 7 operationalizations computed in single pass
   - MW-5 sanity controls: Q 1, Q 2:255, Q 59:22-24
   - Output JSON to `findings/phase-b-hypotheses/csv/h-new-84.json`

3. **Bug fix**: initial NAMES_99 list had 100 entries because الله is included as the proper Name; canonical Tirmidhī list has 99 attributes excluding الله. Filter to NAMES_99_ATTR (without الله) so denominator = 99 strictly.

4. **Run results**:

| Axis | Ratio | PASS? |
|------|-------|-------|
| 1 LENGTH | 0.000142 | NO |
| 2 TOKEN_COUNT | 0.000182 | NO |
| 3 SHANNON_BITS | 0.000135 | NO |
| 4 ROOT_COVERAGE | 0.00426 | NO |
| 5 THEOLOGY_GHAZALI | **0.3725** | **NO (borderline)** |
| 6 THEOLOGY_CONCENTRATION | 0.1526 | NO |
| 7 DIVINE_NAMES_99 | 0.0202 | NO |

5. **MW-5 sanity**: all passed.
   - Q 1 al-Fātiḥa: theology-dominant ✓
   - Q 2:255 āyat al-kursī: theology-dominant ✓
   - Q 59:22-24 khawātim al-ḥashr: 14/99 names ✓ (most divine-name-dense corpus region)

## Key empirical findings

1. **Length-based interpretations**: vacuous. Q 112 is 1/7,038 of corpus by letter, 1/5,492 by token, 1/235 by root-coverage. The hadith CANNOT be a literal length-equivalence claim.

2. **al-Ghazālī's 3-category schema (Axis 5)**: theology-dominant verses are **2,322.8 / 6,236 = 37.25%** of the corpus by the locked keyword schema. This is **within ~12% of the 1/3 target** but **outside the ±10% pre-locked tolerance band [0.30, 0.37]**. Per the locked criterion, Axis 5 FAILS. But the ratio is **strikingly close** to 1/3, which is the most empirically supportive single result in the test.

3. **Theology concentration (Axis 6)**: Q 112's theological-keyword density is **6.55× the corpus average**, vs the predicted 3× under a literal "1/3 of theology in 1/3 of length" reading. This is over-saturated by 2.2×.

4. **Divine-name coverage**: Q 112 contains only **2 of the 99 attribute names** (الصمد + أحد→الأحد stem proxy). 23 of 99 names appear nowhere in the Quran by exact substring match (a separate finding worth checking elsewhere). Q 59:22-24 contains 14 names — 7× more than Q 112 and the densest single region.

5. **Category breakdown of corpus** (substantive sub-finding):
   - Theology-dominant: 2,322.8 verses (37.25%)
   - Narrative-dominant: 514.8 verses (8.25%)
   - Commandment-dominant: 194.3 verses (3.12%)
   - **Uncategorized: 3,204 verses (51.4%)**
   The al-Ghazālī 3-category schema does NOT cover ~half the Quran by these keyword lists. This complicates the symbolic interpretation: a balanced trichotomy is not empirically realized.

## Decisions made during run

1. The 100-vs-99 names question was resolved by filtering to NAMES_99_ATTR (excluding الله). This is consistent with classical scholars who treat الله as al-Ism al-Aʿẓam (the Greatest Name, separate from the 99 attributes). Pre-reg explicitly cited 99 names; this fix preserves the pre-reg semantics.

2. Axis 5 result of 0.3725 was NOT post-hoc rehabilitated by widening the band. Per project rule "Bonferroni tightening self-verifies; loosening requires ratification", post-hoc band-loosening is forbidden. The result is reported transparently as borderline outside the locked band.

3. The keyword-list operationalization for the 3 categories is admittedly one of many possible. Pre-locking the lists prevents garden-of-forking-paths abuse, but a different keyword schema could shift the ratio. This degree-of-freedom is acknowledged transparently in the findings.

## Files written

- `findings/phase-b-hypotheses/h-new-84-ikhlas-third-prereg.md`
- `findings/phase-b-hypotheses/h-new-84-ikhlas-third.md`
- `findings/phase-b-hypotheses/csv/h-new-84.json`
- `scripts/h_new_84_ikhlas_third.py`
- `journal/h-new-84-run-1.md` (this file)

## Reproducibility

```
cd /Users/grey/Downloads/quran
python3 scripts/h_new_84_ikhlas_third.py
# Reads: quran-text/quran-no-tashkeel.json, data/morphology/quranic-corpus-morphology-0.4.txt
# Writes: findings/phase-b-hypotheses/csv/h-new-84.json
# Seed: 20260417 (only used for hypothetical sampling — none triggered in current axes; deterministic)
```

## Cross-references

- H-NEW-65 (Fātiḥa-as-DNA): parallel structural test — REFUTED-STRONG
- H-NEW-59 (divine-names-distribution): relevant to Axis 7
- M-9 (convergence-does-not-multiply): H-NEW-84 is FIRST quantitative test of 1/3 claim
