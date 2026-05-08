---
finding_id: Q004-F-03
title: Q 4 inheritance-fraction structural coherence audit
status: PRE-REGISTERED
date: 2026-05-07
specialist: Q004-al-nisa-specialist
seed: 20260507
bonferroni_k: 5
bonferroni_family: Q004-novel-tests-2026-05-07
alpha_bon: 0.01
direction: COHERENT (the fraction set in Q 4:11-12 + Q 4:176 forms a closed algebraic system under classical farāʾiḍ; al-Suyūṭī ʿilm al-farāʾiḍ predicts an exhaustive case lattice)
acceptance_window: ≥ 6 distinct standard fractions attested AND every classical farāʾiḍ case sums shares ≤ 1 (no over-allocation)
---

# Q004-F-03 — Inheritance-fraction coherence: pre-registration

## Hypothesis

Q 4:11-12 plus Q 4:176 introduce six standard fractions: 1/2, 1/3, 1/4, 1/6, 1/8, 2/3. Classical *ʿilm al-farāʾiḍ* (al-Suyūṭī, *al-Itqān*; al-Bukhārī, *kitāb al-farāʾiḍ*) holds that these fractions form a *closed coherent system* — any inheritance scenario can be solved using only these six (with the additional "ʿawl" / "radd" balancing rules later codified by ʿUmar/Zayd).

## Operationalisation

- Pull the Arabic text of Q 4:11, 4:12, 4:176 from `quran-no-tashkeel.json`.
- Extract the explicit fraction-words: النصف, الثلث, الربع, الثمن, السدس, الثلثان (and فللذكر مثل حظ الأنثيين as the implicit 2:1 rule).
- Verify the 6-fraction-set membership: are all six attested in Q 4 alone? (corpus-distinctness test).
- Algebraic-coherence test: enumerate the 8 canonical inheritance scenarios cited by al-Suyūṭī (*al-Itqān*, nawʿ on farāʾiḍ) and the al-Bukhārī *kitāb al-farāʾiḍ* (book 85) traditions, and for each, compute the share-sum. Pre-commit: every scenario sums to ≤ 1 or invokes the explicit "ʿawl" rule.
- Cross-corpus distinctness: count fraction-lexemes in non-Q4 surahs; pre-commit: Q 4 is the LOCUS (>= 70% of corpus fraction-lexeme tokens in Q 4).

## Null model

- The "coherence" test is a classical-claim verification, not a frequentist statistical test. The null = "fractions are unrelated to classical farāʾiḍ rules."
- For the cross-corpus locus test: 10000 permutations of token-to-surah assignment; report Q 4's locus-percentile.

## Direction & alternative

- DIRECTION-LOCKED: COHERENT (≥ 6 fractions attested + scenarios close).
- INCOHERENT (< 6 fractions OR any scenario over-allocates without ʿawl): NULL of classical claim — would FALSIFY the Suyūṭī-Bukhārī tradition's reading.

## Bonferroni

- Family: Q004-novel-tests-2026-05-07, k=5; α_bon = 0.01 (applies to the locus-percentile test).

## Honest limits

- Classical *ʿawl* and *radd* doctrines are post-Quranic juristic developments (codified under ʿUmar via Zayd b. Thābit per al-Bukhārī ḥadīth #6738 and al-Tirmidhī #2092). The Quran itself does NOT spell out ʿawl; whether the system "closes" depends on whether ʿawl is permitted as an extra-textual rule. This test treats ʿawl as a permitted juristic completion, not as a Quranic claim.
- Some classical inheritance cases are over-determined (e.g. spouse + 2 daughters + parents = 3/12 + 8/12 + 4/12 = 15/12 > 1, requiring ʿawl). These are EXPECTED, not anomalies.
- Audit coverage: 8 canonical scenarios pulled from al-Bukhārī kitāb al-farāʾiḍ + al-Suyūṭī Itqān is non-exhaustive. The test does NOT prove "the system closes for all conceivable scenarios" — it tests "the 8 named classical scenarios are consistent with the 6-fraction set + ʿawl."
