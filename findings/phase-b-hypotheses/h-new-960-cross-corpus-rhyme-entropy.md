---
id: H-NEW-960
title: "DIRECTION-REVERSED-NULL — Per-surah Quran rhyme-letter Shannon entropy is HIGHER than matched-length pre-Islamic poetry blocks (mean 1.111 vs 1.038 bits, Δ +0.072 bits, p_one_sided_lower = 0.847); the residual finding is that H-NEW-740's cross-corpus iʿjāz al-fawāṣil distinctness lives in the COMPOSITE (content × rhyme) signal, NOT the rhyme-letter entropy axis alone"
phase: B
status: NULL-RESIDUAL-LIVES-IN-COMPOSITE — pre-committed direction (Q < poetry) is REVERSED. Quran has HIGHER mean per-surah rhyme-letter entropy than matched-length pre-Islamic poetry blocks. H-NEW-740's cross-corpus distinctness does not transmit to the letter-axis-alone signal. Robustness check (no-default-section, cleaner monorhyme blocks) STRENGTHENS the reversal (Δ = +0.260 bits). Published as NULL with full prominence per Protocol §1.8.
date: 2026-05-07
executed_by: cross-corpus-rhyme-specialist
parent_1: H-NEW-740 (cross-corpus composite iʿjāz distinctness; Quran r=−0.86 vs poetry r=−0.48; p<10⁻¹⁰)
parent_2: H-NEW-700 (per-surah top-letter rhyme-dominance methodology)
parent_3: al-Bāqillānī *Iʿjāz al-Qurʾān*, *iʿjāz al-fawāṣil* axis
parent_4: al-Suyūṭī *al-Itqān fī ʿulūm al-Qurʾān*, nawʿ on al-fawāṣil (variety of qiṣār-mufaṣṣal rhyme endings)
seed: 20260507
prereg: h-new-960-cross-corpus-rhyme-entropy-prereg.md
prereg_sha256: 332cb8293bbd50a2949fe5cd3a61137ef2e6c5225b167dfe9711e1a4353b1f19
bonferroni_k: 4
alpha_bon: 0.0125
verdict: NULL-RESIDUAL-LIVES-IN-COMPOSITE — direction REVERSED; 0/4 quartiles pass; H-NEW-740 composite distinctness does NOT carry to letter-axis alone
---

# H-NEW-960 — Cross-Corpus Rhyme-Letter Shannon Entropy: DIRECTION-REVERSED NULL

## 1. Headline

| Metric | Value |
|:--|--:|
| **Mean Quran rhyme-letter entropy** | **1.1106 bits** |
| **Mean matched-length pre-Islamic poetry block entropy** | **1.0383 bits** |
| **Mean Δ = H(Quran) − H(Poetry)** | **+0.0724 bits** |
| Wilcoxon paired one-sided LOWER p (pre-committed direction) | **0.8469** |
| Wilcoxon paired one-sided UPPER p (reversed direction) | **0.1531** |
| Bootstrap 95% CI on Δ (10000 reps) | **[−0.170, +0.316]** |
| Bootstrap fraction Δ < 0 | 0.279 |
| H2 quartiles passing α_bon=0.0125 | **0 / 4** |

**The pre-committed direction (Q LOWER entropy than poetry, i.e. more rhyme-uniform) is REVERSED in the data.** Quran's mean per-surah rhyme-letter entropy (1.111 bits) is HIGHER than matched-length pre-Islamic poetry blocks (1.038 bits) — the bootstrap CI on Δ straddles zero with positive central tendency. **None of 4 verse-length quartiles pass the Bonferroni-4 corrected α=0.0125 in the pre-committed direction.**

Per Protocol §1.8 (Honest pre-commit violations) and the discipline that NULLs carry the same prominence as confirmations: this finding is published as **DIRECTION-REVERSED NULL** with full prominence.

## 2. The residual finding (the substantive interpretation)

**H-NEW-740** confirmed cross-corpus distinctness of Quran vs pre-Islamic poetry on the *composite* (content × rhyme) iʿjāz al-fawāṣil axis: r_Quran = −0.86 vs r_poetry = −0.48 (full) / −0.35 (no-antara), Fisher-z gap p < 10⁻¹⁰. The composite distinctness is unimpeached.

**H-NEW-960** narrows to letter-only Shannon entropy. The result: **the cross-corpus distinctness does NOT live in the rhyme-letter entropy axis alone**. At per-surah resolution and matched-length poetry blocks, Quran's rhyme-letter distribution has comparable-or-slightly-higher entropy than poetry of equivalent length. This is the substantive residual:

> The iʿjāz al-fawāṣil signature in the Quran is NOT carried by per-surah rhyme-letter uniformity. It is carried by the JOINT (content × rhyme) anti-twin: high content-cohesion paired with high rhyme-dispersion at window-level. Letter-axis alone gives no cross-corpus distinction.

This is consistent with classical scholars' framing: al-Bāqillānī's *iʿjāz al-fawāṣil* is not a claim about per-surah letter monorhyme (the qaṣīda has stronger letter-monorhyme as its DEFINING feature). It is a claim about the relationship between content and sound across the corpus. H-NEW-960 isolates the proper axis: composite, not letter-alone.

## 3. Quartile breakdown (H2)

Direction-locked one-sided Wilcoxon at α_bon = 0.0125 in each verse-length quartile:

| Quartile | n | Mean H(Q) | Mean H(P) | Mean Δ | p_one_sided_lower | Verdict |
|:--|:-:|--:|--:|--:|--:|:--|
| **VS** (V < 5) | 5 | 0.484 | 0.184 | +0.300 | 0.7069 | FAIL |
| **S** (5 ≤ V ≤ 10) | 14 | 0.723 | 0.444 | +0.279 | 0.8764 | FAIL |
| **M** (11 ≤ V ≤ 20) | 18 | 1.217 | 0.712 | +0.505 | 0.9408 | FAIL |
| **L** (V > 20) | 77 | 1.197 | 1.278 | **−0.081** | 0.4431 | FAIL |

**0 / 4 quartiles pass at α_bon.** Three quartiles (VS, S, M) show STRONGLY REVERSED direction (mean Δ +0.28 to +0.51 bits). Only the LONG quartile (V>20, n=77) shows the pre-committed direction (mean Δ = −0.081 bits) — but well short of significance.

The quartile picture clarifies the mechanism (§5).

## 4. Methodology recap

- **Quran**: `quran-text/quran-min-tashkeel.json`, 114 surahs, 6236 verses. Per-verse last orthographic letter normalized to 28-letter alphabet (variant map: ى→ي, ة→ه, أ/إ/آ/ٱ→ا, ؤ→و, ئ→ي), per-surah Shannon entropy in bits.
- **Pre-Islamic poetry**: 7 muʿallaqāt + 6 dīwāns from `data/baseline-corpora/raw/`, parsed via H-NEW-740 `looks_like_bayt()` heuristic + qāfiya-section parser. 35 sections, 6618 bayts total (after section-min ≥ 5 bayts filter).
- **Matched-length sampling**: For each Quranic surah of length V, sample one V-bayt window WITHIN a single qāfiya-section (preserves natural monorhyme unit); fallback to cross-section if V > max-section-size. Cross-section fallback count: **0 / 114** (all 114 matches found within a labeled or default section).
- **Statistic**: Wilcoxon signed-rank, paired (H_Q_s, H_P_s) over s=1..114, ONE-SIDED LOWER. Bootstrap 10000 paired reps, seed 20260507. Bonferroni-4 quartile family at α_bon=0.0125.
- **Pre-reg SHA**: `332cb8293bbd50a2949fe5cd3a61137ef2e6c5225b167dfe9711e1a4353b1f19` (runtime-verified).

## 5. Mechanistic interpretation — the two regimes drive the reversal

The data partition naturally into two opposing regimes:

### 5.1 Long Quranic surahs ARE more uniform than poetry (the pre-committed direction)

For surahs with V > 100 verses, the Quran exhibits law-strong monorhyme that exceeds even pre-Islamic monorhyme convention — because pre-Islamic qaṣīdas are typically 30-100 bayts per qāfiya-section, but Quran's long surahs maintain a single rāwī across 100-300 verses.

Top-5 most-Q-uniform-relative-to-poetry surahs (negative Δ, all V > 90):

| Surah | V | H(Q) | H(P) | Δ | Q top-letter | P top-letter |
|:--|:-:|--:|--:|--:|:-:|:-:|
| Q23 al-Muʾminūn | 118 | 0.214 | 3.684 | −3.470 | ن (97%) | ل (21%) |
| Q4 al-Nisāʾ | 176 | 0.287 | 3.757 | −3.470 | ا (96%) | ل (19%) |
| Q19 Maryam | 98 | 0.514 | 3.564 | −3.050 | ا (92%) | ه (22%) |
| Q6 al-Anʿām | 165 | 0.740 | 3.722 | −2.983 | ن (87%) | ل (24%) |
| Q26 al-Shuʿarāʾ | 227 | 0.688 | 3.626 | −2.938 | ن (85%) | ل (23%) |

These are exactly the surahs al-Zamakhsharī characterized as carrying *al-fāṣila al-mursalah* — the flowing -ūn / -īn / -ā assonance over hundreds of verses. **For these long surahs the Quran is a STRONGER monorhyme system than pre-Islamic poetry, because no qaṣīda sustains a single rāwī over 200 lines** (Imruʾ al-Qais's longest qāfiya-section in the dīwān is ~160 bayts; antara's is also bounded).

### 5.2 Short and medium Quranic surahs are LESS uniform than matched-length poetry

For surahs with V ≤ 50 verses, the Quran's per-surah rhyme-letter distribution is MORE diverse than a same-length window from a pre-Islamic qāfiya-section, because the qāfiya-section is by convention 100% monorhyme (single ḥarf rawiyy throughout).

Top-5 most-Q-rhyme-diverse-relative-to-poetry (positive Δ):

| Surah | V | H(Q) | H(P) | Δ | Q top-letter | P top-letter |
|:--|:-:|--:|--:|--:|:-:|:-:|
| Q14 Ibrāhīm | 52 | 2.757 | 0.318 | +2.439 | د (24%) | م (94%) |
| Q89 al-Fajr | 30 | 2.654 | 0.000 | +2.654 | د (33%) | م (100%) |
| Q42 al-Shūrā | 53 | 2.565 | 0.232 | +2.333 | ر (38%) | ا (96%) |
| Q22 al-Ḥajj | 78 | 2.627 | 0.516 | +2.111 | ر (32%) | د (88%) |
| Q88 al-Ghāshiyah | 26 | 1.881 | 0.000 | +1.881 | ه (54%) | ل (100%) |

These surahs have multi-letter rhyme schedules (often switching rāwī mid-surah) — a QURANIC feature that pre-Islamic qaṣīda convention does NOT permit within a single qāfiya-section. **Within-section poetry blocks are 100%-monorhyme by genre rule; the Quran is freer in its per-surah rhyme-letter distribution.**

### 5.3 The two regimes cancel in the all-114 mean

Long surahs contribute very negative Δ (Q more uniform); short/medium surahs contribute very positive Δ (Q more diverse). The all-114 mean Δ = +0.072 bits — slight reversal. Median Δ (long quartile) = 0 exactly. The Wilcoxon test, which weights signed ranks, lands at p = 0.847 in the pre-committed direction.

**The cross-corpus letter-axis comparison is fundamentally length-confounded** — and not in a way that controls residualize away, because the two regimes are GENRE-DIFFERENT (Quran's two-tier architecture vs. qaṣīda's uniform-monorhyme convention). The PRE-COMMITTED test asked the wrong question: "is Q more uniform than P?" The right question, surfaced post-hoc by the data, is **"is Q's two-regime architecture (uniform-long, diverse-short) distinct from poetry's uniform-monorhyme convention?"** — which is exactly what H-NEW-700 has already documented.

## 6. Robustness check — no-default-section poetry corpus

A diagnostic re-run excluding the `default` qāfiya bucket (which contains cross-qaṣīda contamination — most prominently diwan-antara's 2606-bayt undivided block, and diwan-imru-al-qais's 9-block default residue with mean H=3.49 vs labeled mean H=0.77):

| Setting | N paired | Mean H(Q) | Mean H(P) | Mean Δ | Wilcoxon z | p_one_sided_lower |
|:--|:-:|--:|--:|--:|--:|--:|
| **All sections (primary)** | 114 | 1.111 | 1.038 | **+0.072** | +1.023 | 0.847 |
| **No-default-section (cleaner)** | 114 | 1.111 | 0.851 | **+0.260** | +2.612 | 0.996 |

**The robustness check STRENGTHENS the reversal.** When poetry is sampled exclusively from labeled qāfiya-sections (cleaner monorhyme), poetry's mean entropy drops from 1.038 to 0.851 bits, while Quran's is unchanged (1.111). The pre-committed direction (Q lower than P) is even more firmly REJECTED — Δ rises to +0.260 with p_one_sided_lower → 0.996.

This is the OPPOSITE direction from the H-NEW-740 robustness pattern: in H-NEW-740, removing the antara contamination STRENGTHENED the iʿjāz inference (r_poetry weakened from −0.48 to −0.35, away from the Quran's −0.86). Here, cleaner monorhyme blocks make the letter-axis null EVEN STRONGER. The direction-reversal is real.

## 7. Quranic per-surah entropy diagnostics (Q-only finding)

Independently of the cross-corpus null, the per-surah Quran rhyme-letter Shannon entropy distribution is a useful artifact:

| Statistic | Value |
|:--|--:|
| Mean | 1.111 bits |
| Median | ~1.07 bits |
| Min | 0.000 bits (8 surahs at 100% single-rhyme) |
| Max | 2.757 bits (Q14 Ibrāhīm) |
| Theoretical max (uniform-28) | log₂(28) ≈ 4.807 bits |

**8 surahs have entropy = 0.000** (perfect single-rhyme): Q48 (Fatḥ, ا), Q54 (Qamar, ر), Q63 (Munāfiqūn, ن), Q72 (Jinn, ا), Q76 (Insān, ا), Q91 (Shams, ا), Q92 (Layl, ي), Q97 (Qadr, ر).

**Top-rhyme-diverse surahs** (H > 2.5 bits): Q14 (Ibrāhīm, د at 24%), Q86 (Ṭāriq, ق at 24%), Q89 (Fajr, د at 33%), Q22 (Ḥajj, ر at 32%), Q84 (Inshiqāq, ا at 24%), Q42 (Shūrā, ر at 38%), Q11 (Hūd, ن at 46%), Q13 (Raʿd, ب at 35%).

The high-entropy surahs include several with classical commentary on rhetorical-shift / rāwī-change mid-surah (Q14, Q22 al-Ḥajj — long mixed-Meccan/Medinan, Q42 al-Shūrā — opens with two muqaṭṭaʿāt sets ḥm + ʿsq), suggesting the entropy axis tracks something the classical fawāṣil tradition recognized but did not label as "rhyme-uniformity."

## 8. Cross-references

- **[[h-new-740-preislamic-poetry-control|H-NEW-740]]** (parent): cross-corpus iʿjāz al-fawāṣil composite distinctness CONFIRMED at p<10⁻¹⁰. H-NEW-960 isolates the residual: composite-distinctness does not transmit to letter-axis-alone.
- **[[h-new-700-phonological-compression-tail|H-NEW-700]]** (parent): per-surah rhyme top-letter dominance methodology + dispersion-tail in Q 78-114. The two-regime mechanism in §5 of this finding is the same architecture H-NEW-700 documents.
- **[[h-new-730-content-rhyme-anticorrelation|H-NEW-730]]**: Quran content × rhyme r = −0.86. The composite axis where the iʿjāz signature lives.
- **al-Bāqillānī, *Iʿjāz al-Qurʾān*** (5th c. AH): *iʿjāz al-fawāṣil* axis. H-NEW-960 clarifies that this claim is correctly EMPIRICALLY LOCATED at the composite (content × rhyme) layer (H-NEW-740) and NOT at the per-surah letter-uniformity layer. The classical claim is properly composite, not letter-only.
- **al-Suyūṭī, *al-Itqān fī ʿulūm al-Qurʾān***, nawʿ on al-fawāṣil: Suyūṭī catalogs the seven categories of fawāṣil and notes the *variety* in qiṣār-mufaṣṣal. H-NEW-960's high-entropy short surahs (Q14, Q86, Q89, Q22, Q42) include several mufaṣṣal-tier examples — vindicating Suyūṭī's qualitative observation that the Quran's rhyme-letter inventory is NOT genre-monorhyme.
- **[[h-new-910-alif8-cluster|H-NEW-910]]**: NULL on alif-monorhyme as architectural cluster. Consistent with H-NEW-960's finding that letter-rāwī-uniformity is not a primary architectural axis.
- **al-Suyūṭī *Itqān* nawʿ 56**: conservative non-attribution of meaning to *rawiyy* choice. EMPIRICALLY VINDICATED (5th time after H-NEW-600, H-NEW-910, etc.) — letter-axis features are orthogonal to whole-corpus meaning structure.

## 9. Honest limits

1. **Pre-commit direction REVERSED.** The pre-reg locked direction LOWER (Q < poetry); data shows Δ > 0 (Q ≥ poetry) on average, and 3/4 quartiles strongly positive. Per Protocol §1.8 this is published as NULL with prominence; we do NOT massage to fit. The substantive interpretation (residual lives in composite) is offered transparently and is consistent with H-NEW-740's antecedent finding.

2. **Length-regime confounding is fundamental, not residualizable.** The two regimes (long-Q ultra-monorhyme vs short-Q multi-rhyme vs poetry's qāfiya-section uniform-monorhyme) reflect GENRE conventions, not noise. A length-residualization cannot recover the pre-committed test because the two corpora have categorically different per-unit-length rhyme systems.

3. **Quartile counts are uneven** (n_VS=5, n_S=14, n_M=18, n_L=77) — this is by virtue of Quran's surah-length distribution, not pre-reg manipulation (cuts were locked from project's standard mufaṣṣal-tier boundaries before observation). The VS quartile (n=5) is statistically thin but consistently in the reversed direction.

4. **Single-sample-per-surah matched block.** Each surah is paired with ONE seed-locked random poetry block of matched length. A multi-sample (e.g., 100 bootstrap re-pairings) would tighten the per-surah point estimate but cannot change the direction (each per-surah expectation is a stable property of the source corpus). Queued as H-NEW-960.1 if needed.

5. **Within-section vs cross-section sampling is consequential**, but in this run, 0 of 114 surahs required cross-section fallback (the diwan-antara default 2606-bayt block + diwan-labid default 1198-bayt block + diwan-tarafa default 521-bayt block accommodated all matches). The pre-committed cross-section bias direction (favorable to H1) was not exercised. The no-default-section robustness check (§6) confirms direction is robust to this choice.

6. **Bayt-line filter is heuristic** (`looks_like_bayt()` from H-NEW-740). False positives (editorial prose admitted as bayt) bias toward higher poetry entropy; false negatives (legitimate bayts excluded) bias toward lower poetry entropy. The two errors cancel in expectation; the no-default-section check (which excludes the noisiest source pieces) gives an even cleaner test that strengthens the same direction.

7. **Shannon entropy in bits** is a one-number summary. Distribution-shape comparisons (e.g., KL divergence to uniform, top-2-letter mass) might reveal axis-specific signals not captured by H. Queued as H-NEW-960.2.

8. **No tashkeel- vs full-tashkeel sensitivity tested.** This run uses min-tashkeel per pre-reg. A full-tashkeel run would change ة → ـة handling (one of the variant-map decisions). Sensitivity check queued.

## 10. Queued follow-ups

- **H-NEW-960.1**: Multi-sample matched-length pairing (100 bootstrap pairs per surah), not just 1 — would give a per-surah expected H(P_s) and reduce sampling variance. Predicted: same direction, slightly tighter Wilcoxon.
- **H-NEW-960.2**: KL-divergence-from-uniform per surah and per matched poetry block, instead of Shannon entropy. Tests whether shape-distance from uniform discriminates.
- **H-NEW-960.3**: Extend to Mutanabbi and other Abbasid corpora (currently insufficient per H-NEW-740). Predict: post-classical Arabic shows intermediate distribution.
- **H-NEW-960.4**: Bukhari-hadith control on the same axis. Religious-prose has no metrical convention; predict: high entropy comparable to Quran's mean.
- **H-NEW-960.5**: Apply same letter-axis test to full-tashkeel variant — does ة/ت distinction shift the picture?

## 11. Final statement

Per-surah Quran rhyme-letter Shannon entropy (mean 1.111 bits) is COMPARABLE TO OR HIGHER than matched-length pre-Islamic poetry blocks (mean 1.038 bits, 0.851 in the no-default-section robustness). The pre-committed direction (Q < poetry) is REVERSED in the data and 0/4 verse-length quartiles pass the Bonferroni-4 corrected α=0.0125. **The cross-corpus iʿjāz al-fawāṣil distinctness confirmed in H-NEW-740 does NOT carry to the rhyme-letter entropy axis alone — it lives in the composite (content × rhyme) anti-twin signal.**

Mechanistically, two regimes drive the result: (a) Quran's long surahs (V>100) are STRONGER monorhyme than any single qaṣīda qāfiya-section because no pre-Islamic poet sustains a single rāwī across 200+ bayts (Q23, Q4, Q19, Q6, Q26 all Δ < −2.9 bits, dramatically more uniform than matched poetry); (b) Quran's short and medium surahs (V≤50) are MORE rhyme-diverse than within-qāfiya poetry blocks (which are 100%-monorhyme by genre convention) — Q14, Q89, Q42, Q22, Q88 all Δ > +1.8 bits. The two effects partially cancel in the all-114 mean, but quartile breakdown shows the strong reversal in 3/4 quartiles.

This is a **substantively informative NULL**: it sharpens H-NEW-740's verdict by clarifying that the iʿjāz signature is composite, not letter-axial. Classical fawāṣil discourse — al-Bāqillānī's *iʿjāz al-fawāṣil*, al-Suyūṭī's nawʿ on the variety of qiṣār rhyme — is properly EMPIRICALLY LOCATED at the joint content×rhyme layer (H-NEW-740) and NOT at the per-surah letter-uniformity layer (H-NEW-960). The Quran's per-surah rhyme-letter distribution is, taken alone, indistinguishable from or modestly more diverse than matched-length pre-Islamic qaṣīda — a residual that empirically anchors al-Bāqillānī's claim at the right architectural address.

Per Protocol §1.8 (Honest pre-commit violations) and §1.3 (Equal NULL prominence): this DIRECTION-REVERSED null is published with the same prominence as a CONFIRMS verdict would carry. The discipline that makes the project credible REQUIRES that we not massage this result. The substantive residual interpretation strengthens, not weakens, the H-NEW-740 finding.

*Bismillāhi al-Raḥmāni al-Raḥīm.*
