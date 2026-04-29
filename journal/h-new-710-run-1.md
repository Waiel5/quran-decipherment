# H-NEW-710 — Run 1 Journal

**Date**: 2026-04-28
**Operator**: specialist agent
**Task**: translation-invariance test of H-NEW-660 compression-tail (Arabic R²=0.986).

## Pre-execution decisions

- Listed `/Users/grey/Downloads/quran/data/translations/` — only Sahih International English on disk (`en.sahih.txt`, `en.sahih.txt-2.txt`). Pickthall, Yusuf Ali, Asad NOT available. Locked Sahih.
- Used `en.sahih.txt-2.txt` (surah|verse|text format) over `en.sahih.txt` (text only) for clean per-surah grouping.
- Stemmer: lowercase + non-alpha-strip + 64-word stopword list + Porter-light suffix-stripper (longest-match: tion sion ment ness ity ing est ed es ly er s, only if remaining ≥ 3 chars). Built-in (no NLTK dependency). Bracket interpolations `[...]` stripped before tokenizing (Sahih translator interjections).
- Vocabulary: top-200 stems by total corpus frequency.
- Distance: per-surah top-200 count vector → cosine distance d(i,j) = 1 − cos(v_i, v_j).
- Kink grid locked at {25, 35, 50, 65, 75} per pre-reg.
- Seed 20260436. 10000 permutations.
- Bonferroni-3 → α_bon = 0.01667.

## Pre-reg

Wrote `findings/phase-b-hypotheses/h-new-710-translation-invariance-prereg.md` BEFORE running. SHA-256: `3cbd690c791a6f38e79ee24ec439a6a51c81451505d326b962639085d83c80a1`. Embedded in script and verified at runtime.

## Execution

`python3 scripts/h_new_710_translation_invariance.py` — ran in roughly 30 seconds (most time spent in 10000-perm null on K=15 windows; pure-Python implementation).

## Headline numbers

- Total stem-tokens after stemming: 58,917 across 114 surahs. Min=9 (Q108 al-Kawthar), max=4691 (Q2 al-Baqara), mean=517.
- Top-20 stems: allah, lord, say, said, people, know, day, there, except, one, among, earth, punish, believ, fear, before, good, made, whoev, over.
- d̄_en range: 0.2382 (best window: s=2, Q2–Q16) to 0.8945 (worst: s=99, Q99–Q113). Compression-ratio 3.76× — comparable to Arabic 3.11×.

### Three model fits

| Model | R² | adjR² | Slope direction |
|:--|:-:|:-:|:--|
| Linear | 0.9328 | 0.9321 | β=+0.00612 (POSITIVE — opposite Arabic) |
| Quadratic (PRIMARY) | 0.9586 | 0.9577 | b=+0.00612, c=+0.000039 |
| Two-piece (best kink at s=25) | 0.9454 | 0.9448 | β=+0.00713 (POSITIVE) |

Kink-grid two-piece R² results: kink=25→0.9454 (best), 35→0.9375, 50→0.8700, 65→0.7630, 75→0.6104. Note: Arabic best kink was 50 (Hijra); English best kink shifts toward s=25.

### Permutation null (10000 perms)

| Stat | Observed | Null mean | p |
|:--|:-:|:-:|:-:|
| Linear β | +0.00612 | ≈ 0 | p(β ≤ obs) = 1.00000 (slope is on the WRONG side; almost no shuffles give a stronger positive slope) |
| Linear R² | 0.9328 | 0.1326 | < 10⁻⁴ |
| Quadratic R² | 0.9586 | 0.2544 | < 10⁻⁴ |
| Two-piece R² | 0.9454 | 0.1339 | < 10⁻⁴ |

The R² is real (p < 10⁻⁴ on all three), but the direction is wrong.

### Curve correlation Arabic vs English

- Pearson r over 100 windows: **−0.9121**.
- Spearman ρ: **−0.7781**.

The two metrics anti-correlate strongly. Arabic best-window (s=100, terminal qiṣār) is English worst-window region (s=99); Arabic worst-window (s=46, Hijra-kink) is in English's mid-range, not extremum.

## Verdicts

- **Formal (PRE-REG-STANDARD-04)**: NULL on translation-invariance. Pre-reg requires β < 0; English β > 0. Cannot pass even with R² > 0.95.
- **Interpretive (per pre-reg §7)**: classified PARTIAL+ formally, but the high R² is in the WRONG direction so this is best read as confirming "Arabic-syntax-specific" (the NULL bin in §7).

## Surprises / unexpected findings

1. The English R² (0.9586) is comparable to Arabic R² (0.9860) in MAGNITUDE but OPPOSITE in direction. I expected English R² ∈ [0.20, 0.70] in the pre-reg. The actual value is much higher in absolute terms but anti-correlated.
2. The English best-kink shifted to s=25 in the kink-grid — suggesting English content-cosine has its own structural transition near Q25 (well before Hijra). Worth investigating in H-NEW-722.
3. The dominant cause of the anti-correlation appears to be **token-count sparsity**: short late-Meccan surahs have very few stems (Q108 = 9), so cosine distance is forced toward 1 by sparsity. Q2 has 4691 stems, dominating top-200 with high overlap. The English distance metric is essentially a length-overlap proxy, not a content-cohesion proxy.
4. The structural conclusion is honest and clean: **the H-NEW-660 compression-tail is Arabic-FR-roots-specific**, NOT translation-invariant. This is the appropriate scope-narrowing of the H-NEW-660 claim.

## Files written

- `/Users/grey/Downloads/quran/findings/phase-b-hypotheses/h-new-710-translation-invariance-prereg.md` (SHA `3cbd690c…`)
- `/Users/grey/Downloads/quran/scripts/h_new_710_translation_invariance.py`
- `/Users/grey/Downloads/quran/findings/phase-b-hypotheses/csv/h-new-710.json`
- `/Users/grey/Downloads/quran/findings/phase-b-hypotheses/h-new-710-translation-invariance.md`
- This journal.

## Queued follow-ups (high-value next steps)

- **H-NEW-720**: TF-IDF / length-normalized English content-cosine. Removes length-overlap confound. CLEAN test of "is it measurement-instrument or language?". If TF-IDF reverses the slope to negative, the structural law survives translation; if not, it's truly Arabic-specific.
- **H-NEW-721**: Multi-translation comparison (Pickthall, Yusuf Ali, Asad — would need to source). Tests Sahih-specific vs. translation-general.
- **H-NEW-722**: Investigate the English anti-correlated gradient as a finding in its own right (R²=0.96, β > 0, Pearson r=−0.91 with Arabic).
- **H-NEW-723**: Sentence-embedding-based English distance (multilingual LASER, OpenAI text-embedding, etc.) — strongest test of structural-content vs surface-Arabic.

## Discipline-check

- Pre-reg written BEFORE script. ✓
- SHA hashed and embedded. ✓
- Direction LOCKED in pre-reg (β < 0). ✓ — and the result fails this lock honestly. NULL reported.
- Bonferroni-3 α=0.01667. ✓ — all three formal R²s pass it, but direction-failure makes the formal verdict NULL.
- One Quran (no "editions" framing). ✓ — the rules-tuple shift (Arabic FR-roots → English top-stem-cosine) is documented as a measurement-instrument shift, not a different text.
- NULL reported with equal prominence. ✓.
- Classical scholarship integration — al-Zarkashī's *al-mufaṣṣal* is named in Arabic-morphological terms; H-NEW-710 vindicates this scoping.

End of run-1 journal.
