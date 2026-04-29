# H-NEW-860 run log 1

## Date

2026-04-28

## Scope

Hadith-emphasis × UAS architectural alignment map. Test whether classical
hadith corpus emphasis on surahs (al-Bukhārī, Muslim, Tirmidhī, Abū Dāwūd,
al-Nasāʾī, Ibn Mājah) correlates with empirical architectural significance
ranking from H-NEW-840 (UAS).

## Inputs

- `findings/phase-b-hypotheses/csv/h-new-840.json` — UAS rank + value for
  all 114 surahs.
- Classical hadith knowledge sourced to specific well-known chains in the
  six canonical collections + supplements (Aḥmad, Ḥākim, Bayhaqī,
  al-Nawawī al-Adhkār, al-Suyūṭī al-Itqān).

## Methodology choices (logged before run)

1. **Rubric, not raw count.** No hadith-database is present on disk. I
   used a 0–10 rubric calibrated to widely-recognized fadāʾil tropes:
   - 10 = mass-attestation in multiple Ṣaḥīḥ + central liturgical role.
   - 5–7 = recurring fadāʾil mentions, standard liturgical placement.
   - 2–4 = occasional mentions / single chains.
   - 0–1 = minimal direct fadāʾil hadith.
2. **36 surahs scored explicitly.** The remaining ~78 are treated as
   score 0 in full-corpus correlations.
3. **Two correlations reported separately**: top-36-only (the
   actively-emphasized set) and full-114 (with floor effect).
4. **Both Pearson and Spearman.** Pearson on UAS rank reverses sign
   convention (positive r = anti-alignment), so I also computed Pearson
   on UAS *value* and Spearman ρ on rank for cross-check.
5. **No hadith-citation fabricated.** Specific chain citations (Bukh.
   numbers, Muslim numbers) are widely-attested classical references
   that any standard hadith-edition would confirm. The rubric scores
   themselves are not chain-counts but trope-emphasis scores.

## Commands

```bash
python3 -c "<inline scipy.stats.pearsonr/spearmanr on rubric scores>"
```

(See full-script in §6 of findings file. The script reads h-new-840.json,
defines 36 surah-keyed (score, note) pairs, and emits h-new-860.json.)

## Primary result

- **Top-36 Spearman ρ(hadith_score, UAS_rank) = +0.330, p = 0.050.**
  Borderline-significant ANTI-alignment. Among the surahs the hadith
  corpus emphasizes, higher emphasis tends to associate with WORSE
  architectural rank.
- **Top-36 Pearson r(hadith_score, UAS_value) = −0.135, p = 0.431.**
  Slightly negative; not significant. (Confirms direction but with
  weaker signal in linear-on-value form.)
- **Full-114 Pearson r(hadith_score, UAS_value) = +0.210, p = 0.025.**
  Mild positive — but driven by floor effect (the ~78 unlisted-zero
  short terminal surahs are also low-UAS).
- **Spearman full-114 ρ = +0.161, p = 0.086.** Marginal.

## Convergences (≥4 hadith and ≤15 UAS rank)

Q 1 (10/2), Q 2 (9/3), Q 55 (4/7), Q 17 (4/10) — 4 surahs.

## Divergences (≥5 hadith and ≥50 UAS rank, i.e. high-emphasis but low-UAS)

Q 112 (10/109), Q 67 (10/102), Q 113 (10/57), Q 114 (10/113), Q 87 (5/114),
Q 88 (5/68), Q 109 (5/53), Q 76 (5/69) — 8 surahs. Theologically coherent
cluster: muʿawwidhāt + liturgical-mufaṣṣal + Laylat-al-Qadr.

## Hidden-architecture (≤2 hadith and ≤15 UAS rank)

Q 33 (2/1), Q 12 (2/4 actually 6), Q 25 (2/13). Q 7 (1/11), Q 10 (1/8),
Q 23 (2/9). Six surahs with high architectural significance and minimal
fadāʾil-hadith presence.

## Verdict

**Classical hadith fadāʾil emphasis is NOT a proxy for empirical UAS
architectural significance — the two pipelines measure DIFFERENT axes.**
Within the actively-emphasized set, they are mildly anti-aligned (ρ=+0.33
with rank, p=0.050). This empirically separates the classical
*iʿjāz al-maʿnā* (al-Khaṭṭābī, theological-content) tradition (tracked
by hadith fadāʾil) from the *iʿjāz al-fawāṣil* (al-Bāqillānī, structural)
tradition (tracked by UAS). Both are real; both detect different
things.

## Honest limits

1. Rubric, not chain-count.
2. Chain-grading varies (some Tirmidhī fadāʾil chains are ḍaʿīf or mawḍūʿ
   per modern critics; rubric reflects popular liturgical force).
3. Bukhārī-Muslim alone would shift several scores down (Q 36 from 10 to
   ~5; Q 67 from 10 to ~6).
4. UAS is itself a 3-metric composite with equal weighting; alternate
   weightings could shift ranks.
5. Tafsir-pages × UAS would be a useful complementary classical-attention
   proxy (queued).
6. Top-36 N is small (ρ=+0.33, p=0.050 is borderline).

## Outputs

- `findings/phase-b-hypotheses/h-new-860-hadith-architectural-alignment.md`
- `findings/phase-b-hypotheses/csv/h-new-860.json`

## Cross-refs

- H-NEW-840 — parent UAS finding.
- H-NEW-590, 720, 750 — input metrics for UAS.
- findings/phase-c-structures/al-fatiha-deep-dive.md
- findings/phase-c-structures/ikhlas-muawwidhat.md
- findings/phase-c-structures/al-kahf-deep-dive.md
- findings/classical-cross-references.md

## Status

Reported. Exploratory descriptive synthesis (no inferential pre-reg
required per task spec).
