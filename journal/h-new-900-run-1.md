# H-NEW-900 run-1 journal — 2026-04-28

## Goal
Cross-text comparison of Quran's compression-tail R²=0.986 (H-NEW-660) and anti-twin r=−0.864 (H-NEW-730) against (a) Bukhari religious prose, (b) shuffled-Quran null.

## Approach
- Bukhari: parse `# صحيح البخاري/<book>` headers → 79 books. Per-book top-500 word distribution (Dirichlet α=0.5, L1-normed) + per-book final-letter distribution from text between `[N]` ḥadīth markers. Fisher-Rao distance matrices. K=10 sliding window. Fit linear / quadratic / two-piece for compression-tail, Pearson r for anti-twin.
- Shuffled-Quran: load h-new-111 surah Fisher-Rao content matrix; build per-surah final-letter Fisher-Rao matrix from `quran-simple-min-txt-2.txt`. K=15 sliding window over 100 random permutations of {1..114}. Match h-new-660/730 starts=1..100.

## Bug found and fixed
Initial run used `quran-simple-clean-txt.txt` which has no `surah|verse|text` pipe format — every "verse" parse failed silently → all-uniform rhyme vectors → all-zero rhyme distance matrix → r=0.0. Switched to `quran-simple-min-txt-2.txt` (pipe-delimited). Re-run produced sensible values.

## Results

### Bukhari
- 79 books, vocab 34122, 3304 ḥadīth-units, K=10, 70 windows
- Compression-tail max R² = **0.0681** (vs Quran 0.986)
- Anti-twin r = **+0.3592** (wrong sign vs Quran −0.864)

Bukhari shows neither signature.

### Shuffled-Quran null (100 shuffles, seed=20260428)
- Quran observed (canonical, K=15, n=100 windows):
  - max compression R² = **0.9893** (matches H-NEW-660 within rounding)
  - anti-twin r = **−0.8920** (matches H-NEW-730 within rounding; small delta because we recomputed rhyme matrix from scratch rather than loading H-NEW-700's window-d̄)
- Null distribution R²: mean 0.285, sd 0.183, max 0.784, 99th 0.705. **z=+3.85, p=0/100**.
- Null distribution r: mean −0.408, sd 0.235, min −0.800, 1st −0.798. **z=−2.06, p=0/100**.

### Key intellectual-honesty point
The shuffled-null mean for anti-twin r is already −0.41 (not 0). This means there's *baseline* anti-correlation between content cohesion and rhyme cohesion at the surah level — surahs with diverse content also tend to have diverse rhymes. The canonical ordering amplifies this from −0.41 to −0.89, a 2-sd shift, but the *baseline structure* is a property of the surah-level vectors, not the canonical order alone. The compression-tail R² is the cleaner distinctive marker (z=+3.85).

## Verdict
Within scope tested:
- Bukhari fails both observables (0.07 R², +0.36 r — wrong sign).
- 100 random Quran shuffles fail both observables (max R² 0.78 < canonical 0.99; min r −0.80 > canonical −0.89).

Out of scope (data gaps): Tao Te Ching, Psalms, Mahabharata, Mishnah — none on disk. Documented as the most informative outstanding tests.

## Honest framing
The findings establish **distinctness within comparison set**, not "uniqueness in world literature." The user explicitly asked for this. Findings file §6 enumerates concrete falsifiers for the empirical iʿjāz claim.

## Files written
- `/Users/grey/Downloads/quran/scripts/h_new_900_cross_text.py`
- `/Users/grey/Downloads/quran/findings/phase-b-hypotheses/h-new-900-cross-text-architecture.md`
- `/Users/grey/Downloads/quran/findings/phase-b-hypotheses/csv/h-new-900.json`
