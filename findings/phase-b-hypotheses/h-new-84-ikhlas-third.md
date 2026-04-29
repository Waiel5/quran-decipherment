---
id: H-NEW-84
title: Sūrat al-Ikhlāṣ "1/3 of the Quran" — quantitative test
phase: B
status: COMPLETED 2026-04-15
verdict: REFUTED-STRONG (0 / 7 axes PASS by locked criterion)
notable_finding: Axis 5 (al-Ghazālī's theology-fraction = 1/3) at ratio 0.3725, JUST outside locked band [0.30, 0.37] by 0.0025 — borderline support for the symbolic interpretation
agent: h-new-84-specialist
seed: 20260417
prereg: h-new-84-ikhlas-third-prereg.md
---

# [[h-new-84-ikhlas-third|H-NEW-84]] — Sūrat al-Ikhlāṣ "1/3 of the Quran" — quantitative test

## Verdict

Per the locked PASS criterion (per-axis ratio ∈ [0.30, 0.37]; overall ≥ 3 of 7 axes for PASS-WEAK):
**REFUTED-STRONG (0 / 7 axes PASS).**

The ḥadīth's literal reading (Q 112 = 1/3 of the Quran) fails by **3+ orders of magnitude** on every direct-content operationalization. However, **al-Ghazālī's symbolic interpretation** (theology = 1/3 of corpus content) comes **strikingly close** at ratio **0.3725**, only 0.0025 outside the locked tolerance band — this is the **honest borderline finding**.

## Per-axis results

| Axis | Operationalization | Q112 / corpus ratio | Off by factor | PASS [0.30, 0.37]? |
|------|---------------------|---------------------|---------------|--------------------|
| 1 | Letter graphemes | 47 / 330,709 = **0.000142** | 2,345× too small | NO |
| 2 | Word tokens | 15 / 82,375 = **0.000182** | 1,830× too small | NO |
| 3 | Shannon information bits | 195.5 / 1,450,720 = **0.000135** | 2,473× too small | NO |
| 4 | Distinct roots covered | 7 / 1,642 = **0.00426** | 78× too small | NO |
| 5 | Theology-dominant verses (al-Ghazālī) | 2,322.8 / 6,236 = **0.3725** | 1.12× too high | **NO (borderline)** |
| 6 | Theology concentration factor (inverse) | 1 / 6.55 = **0.1526** | 2.2× too small (i.e., concentration factor 6.55× vs target 3×) | NO |
| 7 | Divine-names coverage (99 names) | 2 / 99 = **0.0202** | 16.5× too small | NO |

## Best-matching interpretation

**Axis 5 — al-Ghazālī's 3-category schema (theology / narratives / commandments)**:
- 2,322.8 of 6,236 verses (37.25%) are dominantly theological per the locked keyword schema.
- This is **very close** to 1/3 (33.3%) — within ~12% relative error, but **outside** the pre-locked ±10% band.
- Of the 6,236 verses, 3,204 (51.4%) are **uncategorized** (none of the keyword classes hit). Of the 3,032 categorized, **76.6% are theology-dominant** — much higher than the implied 1/3.
- The classical 3-category schema therefore has **partial empirical support**: theology IS the largest category by the chosen keyword schema, but the ratio is closer to **3/8 of all verses** or **3/4 of categorized verses** than to **1/3**.

## Q 112 quantitative profile

- 4 verses, 15 word-tokens, 12 distinct types, 47 Arabic letter-graphemes
- 7 distinct roots: q-w-l, ʾ-l-h, ʾ-ḥ-d, ṣ-m-d, w-l-d, k-w-n, k-f-w
- True hapax: **الصمد** (al-Ṣamad) — only 1 occurrence in entire Quran
- Form-hapax: يلد, يولد (both root w-l-d, but these specific surface forms occur only here)
- Divine-name coverage (out of 99 attribute names): **1 explicit (الصمد) + 1 stem-form proxy (أحد → الأحد)** = 2

## MW-5 sanity controls

All passed:
- **Q 1 al-Fātiḥa**: theology-dominant per schema (theology=6, narratives=0, commandments=0).
- **Q 2:255 āyat al-kursī**: theology-dominant (theology=4, narratives=0, commandments=0).
- **Q 59:22-24 khawātim al-ḥashr**: contains **14 of the 99 divine attribute names** (the densest divine-name region in the Quran, as classically claimed).

## Interpretation of best-matching axis (Axis 5)

The al-Ghazālī interpretation reads the 1/3 ḥadīth as:
> "The Quran reduces to three thematic categories — doctrines (about God), narratives, and commandments — and Sūrat al-Ikhlāṣ exhausts the doctrinal category, hence equals 1/3 of the Quran's content."

This interpretation produces a **theology-dominant fraction of 0.3725** of all corpus verses — within 12% of the 1/3 target, but **outside the ±10% pre-locked tolerance band**. This is a striking near-hit, but per the locked criterion, it does NOT formally PASS.

A NULL result for the literal length / token / root / Shannon interpretations is fully expected and confirms that Bukhārī #5013 cannot be read as a quantitative-content claim. The ratio 0.3725 for theological-category verses suggests that **a thematically-defined "1/3 of the Quran is doctrine about God" reading is ~12% from being literally true** — close enough to be theologically resonant, far enough that the strict ±10% band rejects it.

## Honest framing

- The ḥadīth is **best read as a spiritual/devotional valuation statement** ("reciting al-Ikhlāṣ has the reward-equivalent of reciting 1/3 of the Quran"), not a statistical content-equivalence claim.
- The al-Ghazālī interpretation has **partial empirical resonance** (theological verses ≈ 37% of corpus, vs ideal 33%) but does not formally pass the ±10% tolerance.
- The al-Ghazālī interpretation could be **rehabilitated** under a slightly looser tolerance (±15% gives band [0.283, 0.383], which Axis 5's 0.3725 enters). But per the project's "Bonferroni tightening self-verifies; loosening requires ratification" rule, we DO NOT relax the locked tolerance post hoc. The result stands as REFUTED-STRONG.
- The keyword-list operationalization is one of many possible operationalizations of "theology category". A different keyword schema might shift Axis 5 substantively. We pre-locked our schema to avoid this degree of freedom.
- The classical 3-category schema is empirically **NOT a balanced trichotomy**: theology (37.25%) ≫ narratives (8.25%) > commandments (3.12%); 51.4% of verses are uncategorized by the schema. This itself is a **substantive empirical finding** that complicates the al-Ghazālī interpretation.

## Cross-references

- **Bukhārī #5013-5015**, **Muslim #811-812**, **Tirmidhī #2901**, **Abū Dāwūd #1461**, **Nasāʾī #995**: the source ḥadīth corpus.
- **al-Ghazālī, Iḥyāʾ, ch. on faḍāʾil al-Qurʾān**: the 3-category schema interpretation.
- **al-Suyūṭī, al-Itqān**: faḍāʾil al-suwar.
- **Ibn Taymiyya, Tafsīr Sūrat al-Ikhlāṣ**: theological tafsīr.
- **[[h-new-65-fatiha-as-dna|H-NEW-65]] (Fātiḥa-as-DNA)**: methodologically parallel "single surah encodes corpus" test (REFUTED-STRONG by similar methodology).
- **H-NEW-59 (divine-names-distribution)**: relevant to Axis 7.
- **MASTER-FINDINGS-LEDGER**: classical valuation claims about specific surahs.
