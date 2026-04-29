# [[h-new-208-verse-position-structural|H-NEW-208]] — Verse-position within-surah structural analysis

**Pre-reg:** `[[h-new-208-verse-position-structural|h-new-208]]-verse-position-structural-prereg.md`
**Script:** `scripts/h_new_208_verse_position_structural.py`
**Data:** `findings/phase-b-hypotheses/analysis/h-new-208-band-data.csv`,
          `[[h-new-208-verse-position-structural|h-new-208]]-midpoint-anomalies.csv`
**Seed:** 20260419
**Bonferroni k:** 3 (α_bon = 0.01667, two-tailed)
**Ran:** 2026-04-17
**Surahs used (V ≥ 5):** 109 / 114

## Results (primary family)

| Test | Statistic | p | PASS |
|------|-----------|---|------|
| T1 Kruskal-Wallis verse-length × 5 bands | H = 43.71, df=4 | 7.36 × 10⁻⁹ | **PASS** |
| T2 Kruskal-Wallis #divine-names × 5 bands | H = 14.56, df=4 | 5.71 × 10⁻³ | **PASS** |
| T3 Mann-Whitney U MID vs non-MID (length) | U = 25751.5, r = +0.084 | 0.176 | **FAIL** |

### T1 band means (verse-length)
FIRST 29.3 · Q1 44.4 · **MID 47.1** · Q3 44.4 · LAST 55.2. Pattern is
non-monotone: FIRST short, body roughly flat, LAST longest. LAST verse is
~1.9× FIRST in mean length (43.3 graphemes ≈ one clause-pair longer).

### T2 band means (divine names per verse)
FIRST 0.459 · Q1 0.239 · MID 0.257 · Q3 0.339 · **LAST 0.532**. FIRST and
LAST are divine-name-enriched (the opening/closing signature); the interior
bands are depleted. MID is not the enriched band — FIRST and LAST are.

### T3 MIDPOINT vs rest
MID mean-length (47.1) marginally exceeds non-MID (43.3), but the effect is
small (r = +0.084) and non-significant at α_bon. **MIDPOINT is not globally
a distinguished band** at the verse-length level.

## Secondary

**S1 Structural-MIDPOINT surahs (|z| ≥ 2 for length or names at banded MID,
109 surahs):** 6 surahs, ranked:

| Surah | V | MID verse | z(length) | z(names) |
|-------|----|-----------|-----------|----------|
| Q 53 An-Najm | 62 | v32 | **+5.01** | −0.32 |
| Q 51 Adh-Dhāriyāt | 60 | v30 | +0.73 | **+3.84** |
| Q 39 Az-Zumar | 75 | v38 | +2.57 | +0.40 |
| Q 33 Al-Aḥzāb | 73 | v37 | +2.31 | +0.47 |
| Q 89 Al-Fajr | 30 | v16 | +2.15 | 0.00 |
| Q 22 Al-Ḥajj | 78 | v40 | +2.00 | +0.37 |

Q 53 An-Najm v32 stands out as an extreme structural midpoint (+5.01σ verse
length = 129 graphemes vs surah mean ≈29) — the single long verse
acknowledging divine forgiveness/knowledge; worth downstream follow-up.
Q 51:30 carries 2 divine names in a surah where the mean is ≈0.03 — a
divine-name spike exactly at midpoint.

**S2 Global position×length trend:** ρ = +0.040 (p = 1.4 × 10⁻³); per-surah
mean ρ = +0.104; 61.5% of surahs have positive ρ. Weak but real: verses
tend to get somewhat longer as the surah progresses, consistent with LAST
being the band peak in T1.

**S3 Sensitivity (drop Q 1-9 and V < 20, n=71 surahs):** T1′ p = 5.53 × 10⁻¹⁰
(still highly significant; band-effect is not driven by short or opener
surahs). T3′ p = 0.101, r = +0.126 — MID effect strengthens slightly but
still does not clear α_bon.

**Q 18 al-Kahf cross-check ([[h-new-90-kahf-narrative-structure|H-NEW-90]]):** V=110 → banded MID = **v56**, not
v50. Q 18:50 has length 111 (z = +1.59, noticeable but sub-threshold);
Q 18:56 has length 92 (z = +1.00). The [[h-new-90-kahf-narrative-structure|H-NEW-90]] v50 word-midpoint claim
is a word-count midpoint, not a verse-index midpoint, so it does not appear
in this verse-level test — consistent rather than contradictory.

## Interpretation

Position within a surah *does* statistically structure verse-length (T1 very
strong, p ≈ 10⁻⁹) and divine-name density (T2, p ≈ 6 × 10⁻³), but the
structure is a **FIRST-short / LAST-long / LAST-name-rich** envelope — a
khawātim-consistent signature (cf. `[[h-new-95-khawatim-extension|h-new-95]]-khawatim-extension`) — **not**
a MIDPOINT climax. T3 kills the global MIDPOINT hypothesis in its simple
form. Only ~6% of surahs (6 / 109) have a clearly anomalous banded-MID
verse, and those anomalies are heterogeneous (Q 53:32 length, Q 51:30
divine-name spike, etc.).

**Bottom line:** the Quran's within-surah position signal is dominantly an
**end-loaded** one; the MIDPOINT as a general structural device is not
supported at the verse-length/name-density level. Q 18 al-Kahf's v50
"midpoint" finding remains word-level and local, not a global pattern.

## Falsifier check

- T1, T2 significant but with LAST rather than MID as the enriched band.
- T3 non-significant → MIDPOINT hypothesis in its verse-length form falsified.
- S1 non-empty but small and heterogeneous → MIDPOINT specialness is a
  per-surah idiosyncrasy, not a corpus-wide device.

## Follow-ups

1. Per-surah MIDPOINT z-table (S1 table) is a seed list for narrative /
   tafsir cross-reference — e.g., Q 53:32 content analysis against
   Mawdūdī or Biqāʿī on the surah's pivot.
2. Re-run T2/T3 against **word-count** rather than verse-length, matching
   [[h-new-90-kahf-narrative-structure|H-NEW-90]]'s metric, to directly test the word-midpoint hypothesis at
   corpus scale.
3. The end-loading (Spearman ρ > 0; LAST > FIRST) connects to
   `[[h-new-95-khawatim-extension|h-new-95]]-khawatim-extension`; a joint model should be specified.
