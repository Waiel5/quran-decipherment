---
run_id: h-new-172-run-1
agent: autonomous-agent
parent_hypothesis: H-NEW-172
date: 2026-04-17
seed: 20260419
rules_tuple: (no-tashkeel, orthographic-token, graphemes, basmala-counted-only-in-surah-1, hafs-kufan, mashriqi)
inputs:
  - /Users/grey/Downloads/quran/quran-text/quran-no-tashkeel.json
  - /Users/grey/Downloads/quran/data/baseline-corpora/raw/bukhari-noquran.txt
  - /Users/grey/Downloads/quran/data/revelation-order.csv
outputs:
  - /Users/grey/Downloads/quran/findings/phase-b-hypotheses/h-new-172-zipf-per-chapter.md
  - /Users/grey/Downloads/quran/findings/phase-b-hypotheses/csv/h-new-172.json
  - /Users/grey/Downloads/quran/findings/phase-b-hypotheses/csv/h-new-172-per-surah.csv
  - /Users/grey/Downloads/quran/findings/phase-b-hypotheses/csv/h-new-172-per-bab.csv
---

# H-NEW-172 — run-1 log

**Task**: per-surah Zipf α for Quran vs 114 longest Bukhārī bab-segments; correlate with muq / period / length / H-NEW-163 dispersion; synthesize with H-NEW-159 β.

**MW-5 check**: synthetic Zipfian(α_true=1.0, N=10000, V=1000) → α_hat = 0.979. Within ±0.1 tolerance. Method working.

**Results**:
- Quran: n=93 surahs (≥50 tokens), mean α 0.543, SD 0.174, range [0.00, 0.925]
- Bukhārī: n=114 babs, mean α 0.705, SD 0.076, range [0.489, 0.853]
- P1 (means): t=−8.36, p≈0 → PASS (α_bon=0.0167)
- P2 (variances, Brown-Forsythe): t=+4.83, p=1.4e-6 → PASS
- S1 (correlates, sub-Bonferroni α=0.00417): ALL FOUR AXES PASS
  - Strongest: log(length), ρ=+0.810
  - dispersion: ρ=−0.752
  - muq-status: d=+0.74, p=1.5e-4
  - Medinan vs Meccan: d=+0.63, p=3.6e-3
- Synthesis with H-NEW-159: Spearman ρ(α_s, β_s) = −0.453, p=8e-6. Negatively correlated: short surahs have LOW α + HIGH β.

**Verdict**: PASS (3/3 pre-reg cells, 4/4 secondary axes). Quran shows heavier-tailed, more variable rank-frequency structure than Bukhārī, driven by a length gradient spanning 3 orders of magnitude vs Bukhārī's 1.

**Garden-of-forking-paths disclosure**: α fitted on ranks with f≥2 (hapax-truncation, standard practice). If we include hapaxes the fit extends further into the tail; signs preserve, effect sizes slightly shrink. The primary verdict (Quran ≠ Bukhārī in mean AND variance) is robust.
