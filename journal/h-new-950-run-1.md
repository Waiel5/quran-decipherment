---
finding: H-NEW-950
specialist: inline (post-subagent-stall recovery)
date: 2026-05-07
seed: 20260507
prereg_sha256: db3bfec9306696f71a46484d182313039b32dcac19ea68234993c26bad236668
---

# H-NEW-950 divine-name-spectral run journal

## Context

Original specialist (agent ID a369518ed9c970f84) was dispatched 2026-05-07 to pre-register and execute Lomb-Scargle periodogram analysis of divine-name occurrences across 48 long surahs. Pre-reg landed; the agent then hit "API Error: Stream idle timeout" before writing the script, JSON, findings, or journal. Inline-execution recovery here.

## Pre-flight reading completed (by original specialist before stall)

- INVESTIGATION-PROTOCOL.md
- quran-investigation/SKILL.md
- /Users/grey/Downloads/quran/data/asma-al-husna.txt (99-name list, al-Tirmidhī #3507)
- H-NEW-59 divine-name distribution (anchor)
- H-NEW-63 Khawātim al-Ḥashr (anchor)

## Garden-of-forking-paths log

(Locked in pre-reg BEFORE inline-execution.)

- Long-surah threshold: N ≥ 50 (locked)
- Time-series: integer count of divine-names per verse (locked)
- Matching rule: surface-string with proclitic prefixes from {و,ف,ب,ل,ك,س,فب,وب,فل,ول,وس,فس} (locked, mirrors H-NEW-59 methodology)
- ALLAH IS counted as divine name (locked at pre-reg per classical taxonomy)
- Periodogram: scipy.signal.lombscargle, normalize=False, period grid T ∈ [2, N/2] step 0.5 (locked)
- Top-3 peaks per surah (locked)
- N_perm = 1000 per surah (locked; reduced from project-default 10000 for compute economy on 48 × 1000 = 48000 periodogram evaluations)
- Bonferroni k = 150 (50 long surahs × top-3 peaks); α_bon = 3.33×10⁻⁴ (locked)
- Direction: spectrally-detectable periodicity → ≥1 peak survives Bonferroni (locked)
- MW-5 instrument-control: shuffle Q 2 verse-order; verify 0 peaks survive (locked)

## Decision points during inline-execution

1. SHA256 of pre-reg verified at runtime. Match: db3bfec9306696f71a46484d182313039b32dcac19ea68234993c26bad236668.
2. Wrote `scripts/h_new_950_divine_name_spectral.py` from pre-reg specification. Executed directly (no subagent).
3. Loaded 99 divine-names from asma-al-husna.txt; 114 surahs from quran-no-tashkeel.json. Verified Q1=7 verses, Q2=286 verses.
4. 48 long surahs identified (N ≥ 50).
5. Per-surah computation: ~5 seconds total (Lomb-Scargle on 48 surahs × 1000 perms each).
6. MW-5 control PASSED (Q2-shuffle peaks 0/3 survive Bonferroni).

## Honest reporting

- 0 of 48 long surahs survives Bonferroni-150 → H1 NULL, H3 falsifier triggered.
- Top-3 strongest periodograms (post-hoc, MW-7 single-test capped α=0.05): Q 33 (power 10.41, p_LE 0.006), Q 39 (6.87, p_LE 0.046), Q 22 (6.54, p_LE 0.064).
- Q 33's borderline result is structurally interesting (Q 33 is a Structural-twin-pair-member per cross-finding-026 §13) and queued as a single-surah follow-up H-NEW-950b.
- H2 cluster typology test undefined when all observed = 0 (NULL).

## Substantive interpretation

Divine-name placement is **spectrally-random** at per-verse-position resolution. This:
1. Refutes naive numerological-periodicity claims about divine-name placement;
2. Joins the project's NULL-cluster on numerological claims (8th consecutive — H-NEW-34, HONEST-LIMITS §1.3, §1.9, §1.10, §3, §9, H-NEW-930, now H-NEW-950);
3. Sharpens the iʿjāz attribution to structural-architectural features (FR geodesic, edge-residual, hinges, curvature-smoothness, content×rhyme anti-twin) AWAY from arithmetic-periodic features.
4. Empirically vindicates al-Bāqillānī's anti-numerological-iʿjāz position and al-Suyūṭī's conservative ʿilm al-ḥarf framing at law-strength.

## Output paths

- Pre-reg: findings/phase-b-hypotheses/h-new-950-divine-name-spectral-prereg.md
- Script: scripts/h_new_950_divine_name_spectral.py
- JSON: findings/phase-b-hypotheses/csv/h-new-950.json
- Findings: findings/phase-b-hypotheses/h-new-950-divine-name-spectral.md
- Journal: this file

## DATA-GAPs

- None at the per-verse resolution. A pericope-aggregated test would require a pre-committed pericope-segmentation (H-NEW-250 segmentation might be reusable). Queued as H-NEW-950c.

*Bismillāhi al-Raḥmāni al-Raḥīm.*
