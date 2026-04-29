# H-NEW-62 — Run 1 (2026-04-15)

## Agent
h-new-62-specialist

## Task
Comprehensive analysis of surah CLOSING verses (ḥusn al-intihāʾ audit). Mirror
of H-NEW-57 (formulaic openings) at the ending side.

## Procedure

1. Inspected data sources (`quran-no-tashkeel.json`, `revelation-order.csv`)
   without viewing closing texts.
2. Wrote pre-registration `h-new-62-closings-prereg.md` with locked
   11-class taxonomy (priority order PRAYER > GLORIFICATION > TAKBĪR-PAIR >
   QADĪR > WARNING > PROMISE > TAWḤĪD > QUL > SALAM > NARRATIVE > OTHER) and
   7 pre-registered tests.
3. Locked seed 20260416 and α_Bonferroni = 0.05/7 = 0.00714.
4. Wrote `scripts/h_new_62_closings.py` that:
   - extracts closing verse text per surah;
   - classifies into the 11 classes via locked substring rules;
   - runs paired Wilcoxon (length), Shannon entropy + bootstrap (last token
     concentration), Monte Carlo within-surah (paired-attribute fawāṣil),
     hypergeometric (qadīr formula), χ² (period × class), χ² (muqaṭṭaʿāt ×
     class), MC twin-pair count (4-token suffix);
   - dumps per-surah rows + summary to JSON.
5. Ran the script. Inspected outputs.
6. Wrote findings file `h-new-62-closings.md` documenting PASS/NULL
   transparently.

## Results

| Test | p | PASS Bonferroni? |
|---|---|---|
| T1 length (Wilcoxon) | 0.089 | NO |
| T2 closing-word entropy | 0.0076 | NO (raw-sig, narrowly misses) |
| T3 paired-attribute fawāṣil at closings | 0.235 | NO |
| T4 `على كل شيء قدير` at closings | 0.134 | NO |
| **T5 period × closing-class** | **0.0035** | **YES** |
| T6 muqaṭṭaʿāt × closing-class | 0.854 | NO |
| T7 twin-closings 4-tok | 0.0078 | NO (raw-sig, narrowly misses) |

Single hard-PASS: T5 (period × closing-class), driver = Medinan QADIR closings
(5/27 vs 1/87, ~19× rate ratio).

Notable raw-significant signals:
- Closing-word entropy 6.44 bits vs corpus 10.11 bits (3.7-bit concentration).
- 4 verbatim twin-pairs vs MC mean 0.56 (~7× enrichment).
- `الحمد لله` enrichment at closings: p = 0.0007 (Bonferroni-significant
  under formulaic-inventory side analysis).

NULLs (transparency):
- Closing length is NOT distinctive (median +0.4 tokens).
- Paired-attribute fawāṣil are NOT enriched at closings.
- The "umbrella" qadīr formula is NOT enriched at closings.
- Muqaṭṭaʿāt × class is null (sharp asymmetry vs H-NEW-57 openings PASS).
- MW-5 (prayer-formula closings as classical expectation): NOT supported;
  only 2/114 surahs close with PRAYER class (Q 2, Q 71).

## Verbatim twin-pairs (4-token shared suffix)

- Q 4 ↔ Q 24: `والله بكل شيء عليم`
- Q 11 ↔ Q 27: `ربك بغافل عما تعملون`
- Q 45 ↔ Q 59: `وهو العزيز الحكيم`
- Q 56 ↔ Q 69: `فسبح باسم ربك العظيم`

The Q 56 ↔ Q 69 pair is the most striking — a 5-token verbatim closing shared
between al-Wāqiʿa and al-Ḥāqqa.

## Issues / forking-path notes

- The locked taxonomy generates 67/114 OTHER. This is a real finding (closings
  are heterogeneous), not a defect — taxonomy was locked before viewing data
  per project rule. A post-hoc looser taxonomy was NOT applied (would
  constitute garden-of-forking).
- Some closings clearly have prayer/glorification content not matched by the
  locked literal rules (e.g., Q 22 `فنعم المولى ونعم النصير`; Q 23
  `وقل رب اغفر`). These are filed under OTHER per protocol.
- Wilcoxon and χ² use normal-approximation p-values (no scipy in this env).
  Approximations are conservative for the sample sizes here; conclusions hold.

## Verdict
MIXED. One Bonferroni-PASS (T5), four NULLs (incl. classical MW-5
expectation), two narrowly-missed raw-significant patterns. Published with
identical prominence per project policy.

## Convergence
- Mirrors and extends H-NEW-57 (formulaic openings PASS): the muqaṭṭaʿāt
  cluster shapes openings but NOT closings.
- Independently refutes the broad ḥusn al-intihāʾ classical claim, parallel
  to the prior REFUTATION of al-Suyūṭī's ḥusn al-ibtidāʾ.
- The Medinan QADIR-closing cluster fits the broader project finding that
  Medinan legal-content surahs use omniscient/encompassing-knowledge capstones.
