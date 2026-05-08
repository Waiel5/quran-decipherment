# H-NEW-930 — Modular-arithmetic patterns in verse-count distribution

**Run 1** — 2026-05-07 — modular-arithmetic-specialist

## Timeline

- **t0**: Pre-flight reading: SKILL.md, INVESTIGATION-PROTOCOL §, HANDOFF/04-DISCIPLINE.md, MASTER-LEDGER (relevant prior NULL findings on numerology), effect-size-inventory.tsv (confirmed H-NEW-34 + 4 HONEST-LIMITS § prior NULLs on modular claims). Confirmed no existing H-NEW-930 file on disk; H-NEW-920 slot vacant; H-NEW-901 and H-NEW-910 are most recent neighbours.
- **t1**: Loaded `quran-text/quran-no-tashkeel.json`; verified 114 surahs, total 6236 verses, Q1=7, Q2=286, Q108=3 (Hafs-Kūfan numbering confirmed).
- **t2**: Pre-reg drafted at `findings/phase-b-hypotheses/h-new-930-modular-verse-counts-prereg.md`. Direction-locked: H1 = χ² goodness-of-fit on V mod m for m ∈ {7, 11, 13, 19}, Bonferroni-4 (α_bon = 0.0125). Garden-of-forking-paths log written BEFORE observation; moduli explicitly fixed at literature-prior choice.
- **t3**: Pre-reg SHA256 computed: `93ba966620068d10984923ea63b76aee8a8ec30adaa648da0e718b8ddd0ff390`. Embedded in run script as EXPECTED_SHA.
- **t4**: Run script `scripts/h_new_930_modular_verse_counts.py` written. Implements χ² stat + chi² CDF (no scipy dependency, regularized incomplete-gamma series), two-sided binomial p, multinomial-permutation sensitivity for m=19, mushaf-permutation invariance check.
- **t5**: Script executed. SHA verification passed. Results:
  - m=7:  χ²=6.597, df=6, p=0.3598 — NULL
  - m=11: χ²=17.614, df=10, p=0.0618 — NULL (closest to threshold; uncorrected α=0.05 narrowly missed)
  - m=13: χ²=9.386, df=12, p=0.6697 — NULL
  - m=19: χ²=8.667, df=18, p=0.9670 — NULL (strongly under-dispersed)
  - **0 of 4 reject at α_bon = 0.0125**
- **t6**: Multinomial-perm sensitivity for m=19: p_perm = 0.9741 (10000 perms, seed 20260507) — consistent with asymptotic 0.967.
- **t7**: H4(a) mushaf-permutation invariance empirically confirmed: 0 of 1000 random multiset-permutations produced a different χ² (multiset-invariant, as expected mathematically).
- **t8**: Cross-validated chi² + p against scipy.stats.chisquare — exact match to 4 decimal places.
- **t9**: Findings written at `findings/phase-b-hypotheses/h-new-930-modular-verse-counts.md`. Equal-prominence NULL headline; Khalifa-19 disavowal section; classical ʿilm al-ḥarf cross-reference.
- **t10**: 4 surahs with V≡0 mod 19 enumerated for descriptive transparency: Q 47 (Muḥammad, V=38), Q 82 (al-Infiṭār, V=19), Q 87 (al-Aʿlā, V=19), Q 96 (al-ʿAlaq, V=19). Count = 4 vs binomial-expected 6 — UNDER-represented (opposite of Khalifa prediction).
- **t11**: MASTER-FINDINGS-LEDGER.md updated with H-NEW-930 NULL entry inserted after H-NEW-920 slot.

## Key findings

1. **Family verdict: NULL** (0/4 reject). Quran's verse-counts are modularly random under {7, 11, 13, 19}.
2. **m=19 is strongly under-dispersed** (p=0.967): the 19 residue classes each contain 3–10 surahs (E=6), narrower than null sd would predict. Descriptive only — not pre-committed as a hypothesis.
3. **Khalifa-19 prediction REVERSED on its own terms**: residue-0 mod 19 has 4 surahs (Q 47, 82, 87, 96) vs expected 6 — **under-represented**, not over-represented.
4. **m=11 was the closest to significance** (p=0.062) — residue-0 over-represented (17 vs 10.36). Did NOT survive Bonferroni-4. Discipline holds.
5. **Multiset-invariance**: H4(a) is mathematically a no-op for χ²(V mod m); structural property of the test, documented.
6. **H4(b) DATA-GAP**: pre-Islamic-poetry per-poem-line-count tabulation not on disk in tabular form; not required for NULL verdict.

## Discipline check

- [x] Pre-reg SHA matches embedded
- [x] Direction-of-effect was locked BEFORE observation (one-sided χ² upper-tail per pre-reg)
- [x] Bonferroni-4 applied (α_bon = 0.0125)
- [x] Garden-of-forking-paths log locked BEFORE run
- [x] Equal NULL prominence written (§0 headline)
- [x] Honest limits section written (§5)
- [x] No moduli substituted post-observation
- [x] Khalifa-19 disavowal explicit (§6)
- [x] Cross-references to prior NULLs on numerology (§8)
- [x] Verdict: NULL (not CONFIRMED, not DIRECTIONAL)

## Reproducibility

- File hashes: pre-reg SHA `93ba966620068d10984923ea63b76aee8a8ec30adaa648da0e718b8ddd0ff390`
- Seed: 20260507
- Verse-count source: `quran-text/quran-no-tashkeel.json` (114 surahs, total 6236)
- Output: `findings/phase-b-hypotheses/csv/h-new-930.json`
- Run command: `python3 scripts/h_new_930_modular_verse_counts.py`
- Cross-validated against scipy.stats.chisquare: exact match.

## Closes

- Pre-registered Bonferroni-corrected χ² goodness-of-fit on verse-count mod {7, 11, 13, 19} — slot in project ledger filled.
- Adds 7th NULL to the project's modular/numerological-claims series (consistent with H-NEW-34 + HONEST-LIMITS §1.3, §1.9, §1.10, §3, §9).

*Bismillāhi al-Raḥmāni al-Raḥīm. Direction LOCKED. ONE text. Equal NULL prominence.*
