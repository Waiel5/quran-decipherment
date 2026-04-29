# H-NEW-97 run 1 — 2026-04-17

Specialist: h-new-97-specialist
Task: NM-5 — Surah-name-class × muqaṭṭaʿāt letter-set JOINT distribution
Seed: 20260417
Bonferroni: k=4, α_bon=0.0125, family = h-new-97-name-letter-joint

## Chronology

1. Read HANDOFF (01, 03, 04) — confirmed task spec and PRE-REG-STANDARD-04.
2. Read H-NEW-49 findings and JSON — extracted locked 9-class name-class taxonomy and per-surah class assignments for the 29 muqaṭṭaʿāt surahs.
3. Read H-NEW-88 findings — extracted locked 14-set letter-set taxonomy.
4. Decided on 10-row collapse: keep ALM, ALR, HM, TSM as cluster rows; keep ALMS, ALMR, KHYAS, HMASQ as compound-singleton rows; pool SINGLE_SIMPLE = {Ṭāhā, Ṭāsīn, Yāsīn, Ṣād, Qāf, Nūn}. Locked BEFORE viewing joint.
5. Wrote pre-reg `findings/phase-b-hypotheses/h-new-97-name-letter-joint-prereg.md` with YAML frontmatter per PRE-REG-STANDARD-04.
6. Wrote script `scripts/h_new_97_name_letter_joint.py`. Monte-Carlo permutation test shuffles name-class labels over 29 surahs (preserves both marginals approximately — since we shuffle only one axis).
7. Ran script. Output:
   - Cell 1 (10×9 χ² independence): χ² = 69.66, df = 56, p_mc = 0.173 → FAIL-TO-REJECT at α_bon = 0.0125.
   - Cell 2a (ALR vs Uniform9): χ² = 25.60, p_mc = 0.0059 → **REJECT** at α_bon = 0.0125.
   - Cell 2b (ALM vs Uniform9): χ² = 9.00, p_mc = 0.458 → FAIL-TO-REJECT.
   - Cell 2c (HM vs Uniform9): χ² = 6.00, p_mc = 0.882 → FAIL-TO-REJECT.
   - Cell 3 (Cramer's V): 0.586 → LARGE effect.
   - Cell 4 (directional checks): 3/3 PASS.
8. Wrote findings and journal.

## Honest audit

- The global χ² (Cell 1) fails to reject. This is the PRIMARY pre-registered test and it is underpowered. I report this with equal prominence to the ALR sub-cell PASS.
- The ALR cluster's 4/5 PROPHET_PERSON is the main signal. This was foreshadowed by H-NEW-49 (Q 10–14 are the prophet-named Meccan cluster) and by general knowledge of Islamic tradition. The H-NEW-97 contribution is to **test** it under Bonferroni-4 Monte-Carlo null.
- Directional predictions in Cell 4 are deterministically derived from H-NEW-49 — they are pre-loaded and descriptive. Noted explicitly in findings.
- The 10-row collapse was a judgment call locked before the test. A 4-row collapse (ALM / ALR / HM / OTHER) would have more power; recommended as H-NEW-97.1 follow-up.
- I applied Monte-Carlo null with 10K perms per pre-reg. Seed 20260417. Reproducible.

## Lessons

- Global χ² on sparse contingency with many df is easily underpowered; per-cluster tests with uniform-null are more informative at N=29.
- Cramer's V as a secondary effect-size measure is useful — in this case V=0.586 "large" alongside non-rejection shows the test, not the pattern, is the limitation.
- Pre-registering both a PRIMARY and a set of SECONDARY tests, with explicit Bonferroni distribution, prevents post-hoc cherry-picking of the ALR sub-cell as the headline.

## Files produced

- `findings/phase-b-hypotheses/h-new-97-name-letter-joint-prereg.md`
- `scripts/h_new_97_name_letter_joint.py`
- `findings/phase-b-hypotheses/csv/h-new-97.json`
- `findings/phase-b-hypotheses/h-new-97-name-letter-joint.md`
- `journal/h-new-97-run-1.md` (this file)
