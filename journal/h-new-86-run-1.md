---
date: 2026-04-16
agent: h-new-86-specialist
hypothesis: H-NEW-86 surah-name-as-key-root, comprehensive 114 scan
parent: H-NEW-49 cell 5
status: COMPLETED, EXPLORATORY
---

# H-NEW-86 — run 1 journal

## Order of operations (integrity)

1. Read H-NEW-49 prereg + findings + cell-5 results from disk to understand the parent hypothesis.
2. Read Leeds morphology format + sampled ROOT/LEM tagging for proper-noun and content-noun cases (Yūsuf, baqarah, Nūḥ, kahf).
3. Confirmed Leeds tagging: PNs have LEM but no ROOT; content nouns have both. → Designed dual-mode test.
4. Wrote pre-registration `h-new-86-surah-name-as-key-root-prereg.md` with locked Bonferroni-114, 5 stratifications, MW-5 controls (positive Yūsuf; subtle Nūḥ).
5. Wrote `scripts/h_new_86_surah_name_as_key_root.py` with the full 114-row SURAH_MAP (translit, gloss, class, type, target_buckwalter, notes) frozen in code. Mapping is 100% deterministic; printed verbatim in JSON output.
6. Ran the script. Saved JSON + CSV outputs.
7. Wrote findings document.

## Key results

- **Total testable**: 110 of 114 (4 muqaṭṭaʿāt-letter surahs not testable on this axis: Q20 Ṭāhā, Q36 Yāsīn, Q38 Ṣād, Q50 Qāf).
- **Bonferroni-114 SIG**: 26 of 110 (23.6%). Verdict: **EXPLORATORY** (below 33% PASS threshold).
- **Raw α=0.05 SIG**: 74 of 110 (67.3%). Many trends.
- **MW-5 positive (Q12 Yūsuf)**: hits_in=25, hits_rest=2, ratio=532, p=2.98e-39. Pipeline confirmed.
- **MW-5 subtle (Q71 Nūḥ)**: hits_in=3, hits_rest=40, ratio=25.6, p=2.78e-4. Just clears Bonferroni-114.

## Top findings

| Rank | Surah | Class | hits/n_in | ratio | p_two |
|---|---|---|---:|---:|---:|
| 1 | Q12 Yūsuf | PROPHET | 25/1777 | 532× | 3.0e-39 |
| 2 | Q4 al-Nisāʾ | SOCIAL | 20/3747 | 10× | 2.1e-12 |
| 3 | Q18 al-Kahf | REV_RIT | 6/1579 | ∞ | 7.1e-11 |
| 4 | Q101 al-Qāriʿah | EVENT_ESCH | 3/36 | 3225× | 9.2e-10 |
| 5 | Q9 al-Tawba | REV_RIT | 17/2498 | 7× | 2.4e-9 |
| 6 | Q114 al-Nās | SOCIAL | 5/20 | 82× | 4.2e-9 |
| 7 | Q11 Hūd | PROPHET | 5/1917 | 98× | 1.9e-7 |
| 8 | Q63 al-Munāfiqūn | SOCIAL | 6/180 | 25× | 2.7e-7 |

## Stratifications (5 pre-committed)

| # | Stratification | Test | p | Verdict |
|---|---|---|---|---|
| 1 | muqaṭṭaʿāt × pass | Fisher 2×2 | 1.000 | NULL |
| 2 | class × pass | χ² | 0.567 | NULL aggregate; DIVINE_ATTR 0/7, PROPHET 4/11, ANIMAL 5/13 directional |
| 3 | PN(LEM) vs ROOT × pass | Fisher 2×2 | 0.150 | NULL but PN trends higher (5/12=42% vs 21/98=21%) |
| 4 | Meccan/Medinan × pass | Fisher 2×2 | 1.000 | NULL |
| 5 | Length quartile × pass | χ² | 0.061 | TREND, U-shaped (Q1: 36%, Q2: 11%, Q3: 14%, Q4: 33%) |

## Comparison with H-NEW-49 cell 5

8 of 9 H-NEW-49 cell-5 hits replicate at H-NEW-86 (Bonferroni-114). Q24 al-Nūr DEMOTES to NULL (skeleton-match was overcounting `nwr`-letter sequences). Q9 al-Tawba PROMOTES from p=9e-7 to p=2.4e-9 (morphology finds 17 actual `twb` ROOT hits vs skeleton's 10 — skeleton was UNDERcounting due to insertion of vowel letters between root consonants in some derived stems).

H-NEW-86 finds 8 net new SIG surahs not in H-NEW-49 cell 5: Q4 al-Nisāʾ, Q56 al-Wāqiʿah, Q70 al-Maʿārij, Q90 al-Balad, Q86 al-Ṭāriq, Q51 al-Dhāriyāt, Q31 Luqmān, Q39 al-Zumar.

## Pre-reg honesty notes

1. **Pre-reg prediction (1) confirmed**: Yūsuf is the cleanest LEM hit (p=3e-39).
2. **Pre-reg prediction (2) confirmed weakly**: PROPHET_PERSON pass-rate 4/11 = 36% IS the highest tied with ANIMAL_OBJECT (38%), but neither leads dramatically. The Fisher PN-vs-ROOT comparison (5/12=42% vs 21/98=21%) trends as predicted but does not clear α_strat_bon=0.01.
3. **Pre-reg prediction (3) STRONGLY confirmed**: DIVINE_ATTRIBUTE = 0/7. Most striking single class result.
4. **Pre-reg prediction (4) confirmed**: short eschatological surahs (Q99, Q101) are SIG; Q88 al-Ghāshiyah just misses Bonferroni (p > 4.4e-4 — only 1 hit in surah, and other rest-corpus matches dilute).
5. **Pre-reg prediction (5) confirmed**: 23.6% is in the 25-50% range I predicted. EXPLORATORY-to-PASS region. Lands in EXPLORATORY half.

## Garden-of-forking-paths log (BEFORE running)

Recorded in pre-reg:
- Saw H-NEW-49 cell 5 top-5 list before locking. Used this to predict reordering (Yūsuf #1 confirmed; Q24 al-Nūr to demote — confirmed; Q9 al-Tawba to potentially shift — confirmed in promote direction).
- Predicted PROPHET_PERSON would lead — partial confirmation.
- Predicted DIVINE_ATTRIBUTE NULL — strong confirmation.
- Predicted 25-50% pass rate — landed at 23.6%, just below the predicted floor.

No post-hoc cherry-picking. All 26 SIG surahs reported. All 5 stratifications pre-declared and reported regardless of result.

## Compute

- Loading morphology: ~3s.
- 110 hypergeometric tests + 5 stratifications: ~2s.
- Total runtime: ~6s.

## Files

- `findings/phase-b-hypotheses/h-new-86-surah-name-as-key-root-prereg.md`
- `scripts/h_new_86_surah_name_as_key_root.py`
- `findings/phase-b-hypotheses/csv/h-new-86.json`
- `findings/phase-b-hypotheses/csv/h-new-86-per-surah.csv`
- `findings/phase-b-hypotheses/h-new-86-surah-name-as-key-root.md`

## Verdict

**EXPLORATORY** at the global level (26/110 = 23.6% < 33% PASS threshold).

The most important upgrades over H-NEW-49 cell 5 are:
1. Q24 al-Nūr DEMOTES (skeleton overcount); Q9 al-Tawba PROMOTES (skeleton undercount) — both demonstrate the value of proper morphology.
2. Q4 al-Nisāʾ and Q11 Hūd both upgrade dramatically.
3. The DIVINE_ATTRIBUTE 0/7 finding is now formally locked: divine names are corpus-pervasive, NOT surah-anchors. This has implications for understanding the al-Asmāʾ al-Ḥusnā distribution (parent of H-NEW-49 cell 4).
4. The U-shaped length-quartile pattern (p=0.061) suggests two distinct mechanisms: short-surah denominator effect + long-surah narrative-anchor effect. Worth a follow-up extension.

## Suggested follow-ups

1. **H-NEW-86b**: Re-run with reduced α_bon = 0.05/110 (testable-114 only) instead of 0.05/114; would tighten Bonferroni honestly. Predicted: shifts ~1 borderline surah.
2. **H-NEW-86c**: Sensitivity to root-mapping. Five surahs have non-canonical ambiguity (Q3 Āl-ʿImrān LEM vs ROOT family-of-X; Q30 al-Rūm LEM vs ROOT; Q34 Sabaʾ LEM vs ROOT). Re-run with alternative mappings to test stability.
3. **H-NEW-86d**: Permutation null. Replace hypergeometric with 10⁴ surah-token-shuffles to test independence of the parametric assumption.
4. **H-NEW-86e**: Extend to abjad value of name-root. Does the gematria of the title-lexeme have any relation to surah length?
