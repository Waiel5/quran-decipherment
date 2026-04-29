# H-NEW-890 — Journal, run 1

**Date**: 2026-04-28
**Agent**: specialist
**Seed**: 20260428
**N_iter**: 100,000

## Workflow

1. Surveyed the data layout. Found the FR distance matrix is encoded as a JSON-list (not nested string) inside `csv/h-new-111.json` under `D_matrix_upper_triangular` (initially decoded as string; corrected on first traceback).

2. Wrote the prereg with five pre-committed tests and Bonferroni-5 (α_bon = 0.01) before any computation. Hashed the prereg (0c0c7e8c…); the hash propagates to the output JSON.

3. Built the script in five disjoint test functions with shared loaders (`load_verse_counts`, `load_fr_distance_matrix`, `load_quran_text`).

4. First execution: T1, T2, T3, T4 ran cleanly; T5 originally used a too-narrow regex (\bالله\b only matches the bare token, not prefix-attached forms like لله, بالله, والله). The bare regex gave Q 1 only 1 Allah token (vs the classical claim of 5+ divine names). I replaced the primary metric with the broader catalog count from `divine-names-by-verse.csv` (Q 1 = 6 divine names → density 0.857 — the densest in the entire mushaf, matching the classical claim) and kept the bare regex as a sensitivity check. Both metrics give the same direction (ρ ≈ +0.60), so the NULL-with-reversal verdict is robust.

5. Re-ran. All five tests produced clean output.

## Findings (1 sentence each)

- **T1**: NULL with REVERSAL — d_FR(Q 8, Q 9) = 0.911, rank 81/113 among adjacent pairs (LARGER than typical). The bismillah-absence "two-as-one" intuition is *not* corroborated by FR-roots distance.
- **T2**: PASS-DISTINCTIVE — Quran's per-surah-gzip kink-50 fit gives R² = 0.766 vs Bukhari pseudo-mushaf R² = 0.498 (Δ = +0.268), with |β_Q| = 4.4× |β_B|. The compression-tail law is Quran-distinctive.
- **T3**: NULL — k_obs = 4 vs bootstrap null mean 4.01, p = 1.0. Code-19 is a chance-level pattern.
- **T4**: DESCRIPTIVE-NULL — 6236 = 2² × 1559, 1559 prime; no actual surah length is among 6236's divisors.
- **T5**: NULL with strong REVERSAL — Spearman ρ(div-name-density, d_FR(s, 1)) = +0.607, p ≪ 10⁻¹². Q 1's FR-neighbors are *short, low-density* tail surahs (Q108, Q110, Q112, Q106, Q100), not the divine-name-laden Medinan ṭiwāl.

## Mechanism notes

The T5 reversal is *physically* explained: FR-distance is partly length-driven, Q 1 is short (n=7), and so its FR-neighborhood is the mufaṣṣal-qiṣār tail. The *theological* prediction (Q 1 = umm al-kitāb seed) needs a length-residualized metric to test fairly; we pre-committed the simpler version and report it as NULL with explicit honest-limits.

The T1 result is more interesting: even at raw root-level, Q 8 and Q 9 are not FR-similar. Their thematic overlap (early Medinan polity, warfare, oath/treaty) does not translate into a shared root-frequency signature.

## Status of architectural findings

The architectural findings are *strengthened* by H-NEW-890: T2 controls for the obvious "is-it-just-Arabic-prose-property?" alternative, and the answer is no. Meanwhile, the four classical numerical claims fail under proper testing (3 of 4 in the *opposite* direction from prediction, 1 at exact null mean).

## Artifact hashes

- prereg: 0c0c7e8ce0774832df0f7bb56f1937cc6bc8bf87d347022f64d5a7cea2ff7885
- script: a884db8be3d2a4d6d7f0d12cc961dd690f29e871e4d45bdfb80fb867a817d1f4
- output JSON: 683e0f89d7f2326af60810f0ae06d0139a161785d503c70bf3430c6c00ec82e3

## Next steps (suggested but not auto-run)

1. Length-residualized FR-distance variant of T5 to test Q 1 = umm al-kitāb properly (pre-register separately).
2. Length-residualized FR-distance variant of T1 to test Q 8/Q 9 unity.
3. Extend T2 to additional control corpora (jahiz-hayawan.txt, mutanabbi-diwan.txt, sira-ibn-hisham.txt) to strengthen the genericity NULL.
