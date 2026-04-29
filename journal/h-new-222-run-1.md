# Journal — H-NEW-222 run 1

**Date**: 2026-04-17
**Seed**: 20260419
**Bonferroni k=4, α_bon=0.0125**

## Task
Test 4 additional chronologies against Fisher-Rao D-matrix (H-NEW-111):
Ibn ʿAbbās, al-Suyūṭī Itqān, Tanzil (verify), Watt-Bell 1970.

## Result summary (shortest-first)
1. mushaf            L=85.7597  p=1e-4
2. watt_bell_1970    L=87.2321  p=1e-4  PASS
3. suyuti_itqan      L=89.5297  p=1e-4  PASS  (= Tanzil)
3. tanzil_egyptian   L=89.5297  p=1e-4  PASS  (replicates H-212 exactly)
5. ibn_abbas_abd_kafi L=89.8953 p=1e-4  PASS

All 4 PASS Bonferroni k=4 α_bon=0.0125. Mushaf rank 1/5. Mushaf still wins.

## Two historiographic side-findings

1. **Watt-Bell (1970) ch.7 list = Nöldeke 1860 list** (114/114 positional match).
   Watt explicitly says he uses Nöldeke's scheme. L identical to 4 decimals.
   Thus Watt-Bell does NOT contribute a distinct reconstruction — it is an
   analytical commentary on Nöldeke's framework.

2. **Suyūṭī Itqān (Jābir b. Zayd transmission) = Tanzil list**. Al-Zanjānī's
   tabulation (Tanzil's source) is the Jābir b. Zayd transmission which
   Suyūṭī endorses in Itqān nawʿ 7. The Cairo 1924 edition thus embeds
   Suyūṭī's preferred classical chain verbatim.

## Ibn ʿAbbās difference from Tanzil
70 positional differences. Single largest: al-Fātiḥa placed at rank 61
(not 5). Spearman ρ(ibn_abbas, tanzil) = +0.9864 — near-identical.
Ibn ʿAbbās is ~0.22 null-SDs LONGER than Tanzil — small penalty for the
late-Fātiḥa rearrangement.

## Instrument sanity
L_tanzil(H-222) = L_egyptian(H-212) = 89.5297 exactly. Instrument intact.

## Files
- prereg: findings/phase-b-hypotheses/h-new-222-more-chronologies-prereg.md
- script: scripts/h_new_222_more_chronologies.py
- JSON:   findings/phase-b-hypotheses/csv/h-new-222.json
- MD:     findings/phase-b-hypotheses/h-new-222-more-chronologies.md
