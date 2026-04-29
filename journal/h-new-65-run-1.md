---
hypothesis: H-NEW-65
run: 1
agent: h-new-65-specialist (re-dispatch after rate-limit)
date: 2026-04-15
seed: 20260416
script: /Users/grey/Downloads/quran/scripts/h_new_65_fatiha_as_dna.py
prereg: /Users/grey/Downloads/quran/findings/phase-b-hypotheses/h-new-65-fatiha-as-dna-prereg.md
verdict: REFUTED-WEAK (1 of 6 axes Bonferroni-significant; threshold ≥ 2)
---

# H-NEW-65 — Run 1 journal

## Goal
Test the classical "Fātiḥa is microcosm of the Quran" claim across 6 pre-locked axes with sliding-window 7-verse null and Bonferroni k=6 (α_bon=0.00833). Pre-committed PASS = ≥ 2 of 6 Bonferroni-significant.

## Rules tuple
(no-tashkeel; word-segment substring + first-letter-of-token; hafs-kufan; 6236 verses; basmala-counted-only-in-surah-1; mashriqi). Same rules-tuple as the locked spec; not modified.

## Steps
1. Read pre-reg `/Users/grey/Downloads/quran/findings/phase-b-hypotheses/h-new-65-fatiha-as-dna-prereg.md` end-to-end.
2. Loaded `quran-no-tashkeel.json`; verified 114 surahs / 6236 verses / Fātiḥa = first 7 verses (basmala = Q 1:1).
3. Confirmed Fātiḥa word-counts (4,4,2,3,4,3,9) match spec exactly.
4. Confirmed Fātiḥa verse-final letters: م,ن,م,ن,ن,م,ن.
5. Implemented all 6 axes per pre-reg specifications; all directions and PASS criteria pre-locked.
6. Sliding-window null = 6230 contiguous 7-verse windows (axes 1–4, 6 use full sliding null; axis 5 uses 1000 random sliding-window indices sampled under seed 20260416 per pre-reg compute-budget concession).
7. Computed MW-5 sanity controls: Q 59:22-anchored window (axes 1, 2) + Q 26:1-anchored window (axis 4).
8. Wrote raw JSON + findings file + this journal.

## Per-axis results

| Axis | Fātiḥa | Null median | p (1-sided) | Pass? |
|------|--------|-------------|-------------|-------|
| 1 lexical mean log-freq (↑) | 3.023 | 3.190 | 0.657 | NO |
| 2 semantic theme cov (↑) | 5/5 | 1 | **0.00144** | **YES** |
| 3 phonetic LL (↑) | −9.480 | −9.870 | 0.491 | NO |
| 4 structural KS (↓) | 0.679 | 0.470 | 0.847 | NO |
| 5 compression gain (↑) | 0.000500 | 0.0007 | 0.740 | NO |
| 6 phar/glot first-letter (↑) | 2/4 | 3 | 0.950 | NO |

## Key observations

- **Axis 2 PASS** is the meaningful positive result: Fātiḥa hits all 5 pre-locked theme classes (praise/mercy/judgment/guidance/supplication) — only 9 of 6230 sliding windows reach 5/5 (0.144%, comfortably below α_bon=0.0083).
- **Axis 1 (lexical) is below median**: Fātiḥa's distinct types are slightly less common than typical, partly because of low-frequency definites like ـ"الصراط"ـ.
- **Axis 4 (structural KS) is WORSE than typical** (85th percentile of distance from corpus CDF): the 9-word verse 7 plus the 2-word verse 3 push Fātiḥa's word-count distribution far from the corpus norm.
- **Axis 5 (compression) shows essentially no advantage**: Fātiḥa is a mediocre gzip dictionary for the rest of the Quran (27th percentile).
- **Axis 6 (pharyngeal/glottal) is below median**: Fātiḥa covers only ا and ع as token-initial pharyngeal/glottal letters; ه and ح never appear in token-initial position. The H-NEW-44.2.1 muqaṭṭaʿāt-class saturation pattern does NOT extend to Fātiḥa.

## MW-5 controls (non-blocking per pre-reg)
- Q 59:22 window axis-1: 3.138 (mid-range, expected — divine-name density ≠ lexical commonness).
- Q 59:22 window axis-2: 2 (below median — Khawātim are name-dense not theme-diverse).
- Q 26:1 window axis-4: 0.465 (near corpus median).

These match pre-reg expectations: MW-5 anchor verses are not necessarily extreme on the *specific* statistics chosen for these axes (pre-reg explicitly flagged this).

## Unsurprises / surprises

- **Surprise**: Fātiḥa is *worse than typical* on 4 of 6 axes (axes 1, 4, 5, 6). The microcosm intuition has been quite literally backwards on lexical and structural and letter-class dimensions.
- **Unsurprise**: The semantic-theme axis is the only one to pass — that matches the strongest historical-exegetical reading of the Umm al-Kitāb claim (the integrating thematic kernel).

## Bonferroni & pre-committed PASS
- α_bon = 0.05 / 6 = 0.00833.
- Required ≥ 2 of 6 Bonferroni-significant for PASS.
- Got 1 of 6 → REFUTED-WEAK.

## Follow-on
- Per M-9, H-NEW-59 + H-NEW-65 → effective N ≈ 2 for the broader Fātiḥa-microcosm hypothesis. Both are negative on the strong reading. No further compounding tests warranted unless a genuinely new axis is identified.
- The axis 2 (theme-coverage) result deserves a single-axis follow-up *only* if a question-specific MW-5 control can be constructed (e.g., the Khawātim al-Ḥashr window scored 2/5, demonstrating that even a famously dense-divine-names cluster does NOT exhibit Fātiḥa's thematic saturation).

## Reproducibility
- Seed 20260416. Sliding-window null is deterministic; axis-5's 1000-window subsample is RNG-driven — re-run from clean Python yields bit-identical numbers.
- No tooling changes required; all logic in the single script.

## Files
- Script: `/Users/grey/Downloads/quran/scripts/h_new_65_fatiha_as_dna.py`
- JSON: `/Users/grey/Downloads/quran/findings/phase-b-hypotheses/csv/h-new-65.json`
- Findings: `/Users/grey/Downloads/quran/findings/phase-b-hypotheses/h-new-65-fatiha-as-dna.md`
- Journal: this file.
