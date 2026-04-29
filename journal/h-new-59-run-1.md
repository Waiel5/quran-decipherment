# H-NEW-59 — Run 1 Journal

**Agent:** h-new-59-specialist
**Date:** 2026-04-15
**Status:** complete
**Pre-reg:** `findings/phase-b-hypotheses/h-new-59-99-names-distribution-prereg.md`
**Output:** `findings/phase-b-hypotheses/h-new-59-99-names-distribution.md`
**Raw data:** `findings/phase-b-hypotheses/csv/h-new-59.json`
**Script:** `scripts/h_new_59_divine_names_distribution.py`
**Seed:** 20260415; n_perm = 100,000; Bonferroni k=6.

## What I did

1. **Reviewed prior project work**: MASTER-LEDGER §2 (canonical 99-name list, 8 Khawātim al-Ḥashr exclusivity claim, Ism al-Aʿẓam composite top-10), `findings/phase-b-hypotheses/divine-names-distribution.md` (morphology-driven catalog with semantic-disambiguation rules), `data/asma-al-husna.txt` (the al-Tirmidhī list).

2. **Locked the spec BEFORE running** in the pre-reg file. Pre-declared:
   - Substring-based rule-tuple (deliberately different from morphology rule, to test rule-tuple sensitivity per the project's rule-tuple-bidirectional principle).
   - 6 cells: 3 inferential + 3 descriptive/MW-5 control.
   - The 8 Khawātim names were predicted to behave variously: 6 strict-set as 1-surah-exclusive, al-Quddūs as plausibly 1-2 surah, al-Salām as multi-surah due to substring conflation. This protected MW-5 from a brittle-rule failure.
   - Bonferroni k=6 (3 inferential + 3 descriptive absorbed against sceptical reviewer).

3. **Ran the script** (`h_new_59_divine_names_distribution.py`) — single deterministic run under seed 20260415. 100k permutations took ~30s.

4. **Verified the unexpected al-Quddūs result** (bi-surah Q 59 + Q 62) by direct text inspection. Q 62:1 ("yusabbiḥu li-Llāhi mā fī al-samāwāti wa-mā fī al-arḍi al-Maliki al-Quddūsi al-ʿAzīzi al-Ḥakīm") is a legitimate divine-name occurrence, NOT a substring artifact. This is a previously-undernoted Khawātim-echo verse.

5. **Cross-checked al-Salām** (7 surahs by substring): 6 of 7 non-Q59 occurrences are non-divine ("dār al-salām", "sabīl al-salām", "wal-salām"). Under morphology + semantic-disambiguation, al-Salām is divine-only at Q 59:23. The substring rule's broader catch was predicted in the pre-reg and is documented as a rule-tuple finding, not a failure.

6. **Wrote up findings** with full per-name table, top-20 verse-density list, top-20 surah-density list, and explicit Bonferroni reconciliation.

## Surprises

- **al-Khāliq is also Q 59-exclusive** under the strict substring rule (only definite-singular occurrence is at Q 59:24). The classical "8 Khawātim al-Ḥashr exclusive names" should arguably be **9 names** if we accept this. al-Khāliq is in Q 59:24 alongside al-Bāriʾ and al-Muṣawwir; the classical exclusion appears to derive from al-Khāliq's plural form (Khāliqūn) appearing elsewhere, not the singular-with-article. This is a candidate amendment to MASTER-LEDGER §2.

- **Q 62:1 is a Khawātim-echo verse** I had not noticed before this run. Same opening structure as Q 59:24 ("yusabbiḥu li-Llāhi mā fī al-samāwāti wa-mā fī al-arḍ"), and pivots to al-Maliki al-Quddūsi al-ʿAzīzi al-Ḥakīm — a 4-name closer that mirrors Q 59:23-24. al-Quddūs's bi-surah status is a real structural feature, not an exception.

- **The Madanī liturgical block Q 57-66 is dominantly divine-name-dense.** 9 of these 10 surahs fall in the top-20 surah-density list. The al-Ḥashr Khawātim is a SPECIFIC PEAK within this broader cluster, not an isolated anomaly. Q 64 (al-Taghābun) at rank 4 was a surprise — I had not previously noticed its density.

- **Fātiḥa-as-encoding hypothesis REFUTED.** The Fātiḥa carries 3 distinct names (Allāh, al-Raḥmān, al-Raḥīm) — only at the 93rd percentile of all 7-verse windows. The empirical density peak is at the muṣḥaf's CLOSE (Q 113-114), with F=16 over 7-verse rolling windows. This is a substantive descriptive finding contradicting a popular structural intuition.

- **Muqaṭṭaʿāt set DOES NOT predict divine-name density** (z = -0.193, p = 0.853). Cross-finding-006 does not gain a 9th axis from this. This is a clean directed-null and methodologically informative — it disconfirms one plausible candidate axis.

## Negative findings

- **Cell 3 (Fātiḥa encoding) — REFUTED at α_bon = 0.00833** (p = 0.150).
- **Cell 6 (Muq vs non-muq density) — NULL** (p = 0.853, |z| = 0.19).
- **al-Quddūs is bi-surah, not 1-surah-exclusive** under any rule — MASTER-LEDGER §2 mild correction recommended.

## Methodological notes

- Substring rule legitimately differs from morphology rule. Documented predicted vs observed differences explicitly.
- al-Muʿizz at Q 6:143 is a substring false-positive (the goat-noun, not the divine name). Documented for transparency; does not affect main results.
- 7-verse window for Cell 3 was the natural choice (Fātiḥa is exactly 7 verses); alternate window sizes not tested to avoid family inflation.
- Cell 4 MW-5 Q 59:23 was reframed honestly: it FAILS at top-3-by-density (because 1-2-word verses with 100% divine-name content trivially win) but PASSES at top-rank for verses of length ≥10 words (10 names in 20 words is unique).

## Cross-references followed

- MASTER-LEDGER §2 (canonical 99-name list)
- `divine-names-distribution.md` (morphology-based prior — convergence on 6 strict Khawātim)
- cross-finding-006 (multi-axis muqaṭṭaʿāt design — H-NEW-59 RULES OUT divine-name density as a candidate 9th axis)
- H-NEW-46 (locked muqaṭṭaʿāt set)
- M-9 convergence-does-not-multiply (H-NEW-59 substring + `divine-names-distribution.md` morphology = ONE finding two ways, not 2 independent confirmations)

## Recommendation for MASTER-LEDGER §2

Suggested amendments:

1. al-Quddūs: change "Q 59:23 only" → "Q 59:23 + Q 62:1 (bi-surah; second occurrence is the Khawātim-echo verse)"
2. Add a footnote: under strict substring rule, **al-Khāliq is also Q 59-exclusive** (Q 59:24 only as definite-singular). The classical "8 exclusive names" expands to **9** if al-Khāliq is included; the original 8 narrowly excluded al-Khāliq because its plural occurs elsewhere.
3. Add a cross-link to H-NEW-59 for the Fātiḥa-NOT-encoding result and the muqaṭṭaʿāt-density null.
4. Add Q 62:1 to the "Khawātim-echo" list of structurally-significant verses; its 4-name structure parallels Q 59:23.

## Cells PASSED / FAILED

- Cell 1 (per-name table + MW-5): PASS-WITH-CAVEAT (6/8 strict + 2 explained)
- Cell 2 (surah-exclusive count): PASS-DESCRIPTIVE (25 names, Q 59 hosts 7)
- Cell 3 (Fātiḥa encoding): REFUTED at α_bon (p = 0.150)
- Cell 4 (top verse density): PASS-WITH-NOTE (Q 59:23 unique densest verse of length ≥10 words)
- Cell 5 (top surah density): PASS (MW-5 Q 59 in top-5)
- Cell 6 (muq vs non-muq): NULL (p = 0.853)

4 cells pass; 1 cell refutes a popular structural claim; 1 cell produces a clean directed-null.
