---
date: 2026-04-12
agent: prophet-chronology
task: Prophet-mention timing across Nöldeke chronology
run: 1
status: complete
script: scratch/prophet-chronology/analyze.py
output: scratch/prophet-chronology/results.json
finding: findings/phase-b-hypotheses/prophet-mention-chronology.md
---

# Run 1 — Prophet-mention timing across Nöldeke chronology

## Pre-registered setup (fixed before touching data)

- Rules tuple: `(no-tashkeel, orthographic-token & lemma, graphemes, counted-only-in-surah-1, hafs-kufan, mashriqi)`.
- 10 prophets: Mūsā, Ibrāhīm, Maryam, Yūsuf, ʿĪsā, Ādam, Iblīs, al-Masīḥ, Nūḥ, Lūṭ.
- 4 Nöldeke phases: Early Meccan (48 surahs), Middle Meccan (21), Late Meccan (21), Medinan (24).
- Three hypotheses: H1 sequential-introduction, H2 Medinan-shorter-surahs, H3 Mūsā-ʿĪsā Medinan rise.
- Nulls: N-A within-surah token shuffle (1000 draws, seed 20260412), N-B surah-phase-label shuffle (1000 draws, same seed), chi-squared complement (df=3).

## Workflow

1. Confirmed QAC LEM tags for all 10 prophets (grep). Confirmed no ambiguity:
   - Mūsā = `muwsaY``, Ibrāhīm = `<iboraAhiym`, Maryam = `maroyam`, Yūsuf = `yuwsuf`, ʿĪsā = `EiysaY`, Ādam = `A^dam`, Iblīs = `<iboliys`, al-Masīḥ = `masiyH`, Nūḥ = `nuwH`, Lūṭ = `luwT`.
2. Loaded `data/revelation-order.csv`; verified 114 rows and phase distribution: 48 + 21 + 21 + 24. Built `surah_phase` map.
3. Loaded `quran-text/quran-no-tashkeel.json`; verified 114 surahs / 6236 verses; built verse-count per surah.
4. Parsed QAC morphology line-by-line; extracted (surah, verse) location and PN lemma; built `verse_prophet_tokens[(s,v)]` as Counter of prophet→count.
5. Built 10×4 phase-prophet matrix. Computed chi-squared uniform and verse-weighted.
6. Extracted first-appearance by Nöldeke order. Found al-Masīḥ is Medinan-only (Q 3:45 = Nöldeke 97) — H1 counter-example.
7. Co-mention matrices per phase.
8. Surah-length per mention per phase.
9. Null model N-A (within-surah token shuffle): had to fix a bug. Initial implementation shuffled verse-bags which made co-occurrence invariant — detected zero-variance in draws, switched to independent-token-per-verse within surah. Also fixed a key-ordering mismatch (PAIRS were built in PROPHETS order but bag-derived keys were alphabetical; aligned both to alphabetical).
10. Null model N-B (surah-phase-label shuffle): implemented as a separate null because N-A is invariant for phase totals.
11. Computed p-values (two-sided empirical).

## Key numerical results

- 10×4 matrix (tokens, 4 + 41 + 67 + 24 = 136 for Mūsā; 0 + 5 + 0 + 29 = 34 for Maryam; 0/0/0/11 for al-Masīḥ).
- All 10 prophets reject flat-uniform chi-squared at α = 0.05; 9/10 reject verse-weighted chi-squared at α = 0.05 (Ādam does not).
- Bonferroni-surviving phase-total cells under N-B: 8 cells (Mūsā/Ibrāhīm/Nūḥ/ʿĪsā/Lūṭ Early deficit, Iblīs Middle excess, Maryam/ʿĪsā Medinan excess).
- Bonferroni-surviving co-mention pairs under N-A (family = 180): 6 pairs — 5 Medinan (ʿĪsā-Maryam, Maryam-al-Masīḥ, Ibrāhīm-Nūḥ, Ibrāhīm-ʿĪsā, Mūsā-ʿĪsā) + 1 Middle Meccan (Ādam-Iblīs).
- Mūsā-ʿĪsā Medinan co-mention: 4 observed / 0.50 null mean / p < 0.001 — H3 confirmed.
- Medinan surah-length per mention 173.9 > Meccan 123.6 — H2 reversed.
- al-Masīḥ first mention Q 3:45 (Nöldeke 97, Medinan), 0 Meccan attestations — H1 refuted by lemma counter-example.

## Sanity checks passed

- Phase verse count sums to 6236 (hafs-kufan anchor ✓).
- Mūsā lemma total 136, ʿĪsā 25, Maryam 34 — all match classical citations.
- Prophet lemma strings independently grep-verified in QAC file.

## Bugs caught & fixed

1. Initial null model preserved the verse-bag composition, making co-occurrence invariant (all null means identical to observed, p = 1). Fixed by switching to independent-token reassignment within surah.
2. PAIRS key-ordering mismatch: built from PROPHETS list but compared against alphabetical-sorted bag keys. Aligned both to alphabetical order.
3. Function-definition ordering: `two_sided_p` used before defined. Moved up.

## Runtime

~3 seconds for 1000×2 nulls + chi-squared + descriptive stats.

## Output

- `findings/phase-b-hypotheses/prophet-mention-chronology.md` — full write-up with YAML frontmatter, rules tuple, hypothesis verdicts, matrices, classical cross-reference, garden-of-forking-paths disclosure.
- `scratch/prophet-chronology/results.json` — all numerical results including null distributions summaries.
- `scratch/prophet-chronology/analyze.py` — deterministic reproduction script.

## Queued follow-ups (handed to downstream agents)

1. Bell / Blachère chronology sensitivity test.
2. List-formula-stripped H3 retest.
3. Prophet-verb-framing extension (qāla, arsala, naṣara + prophet).
4. Cross-reference Medinan ʿĪsā pericopes with Syriac-Christian subtext catalog (Reynolds).
