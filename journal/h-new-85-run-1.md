---
agent: h-new-85-specialist
date: 2026-04-15
hypothesis: H-NEW-85 — comprehensive oath-opening surah analysis
status: completed
prior: H-NEW-61 (locked 21 OATH_PARTICLE surahs, 21/21 Meccan)
---

# H-NEW-85 run 1 — Oath-opening surahs

## Workflow

1. Loaded H-NEW-61 OATH_PARTICLE class from
   `findings/phase-b-hypotheses/csv/h-new-61.json` → 21 surahs:
   {36, 37, 38, 43, 44, 50, 51, 52, 53, 68, 77, 79, 85, 86, 89, 91, 92,
   93, 95, 100, 103}. Frozen as the H-NEW-85 input set.
2. Drafted prereg with 5 cells, k=5 Bonferroni, α_bon = 0.010.
3. Wrote `scripts/h_new_85_oath_openers.py`:
   - Loads QAC morphology rows.
   - Walks each oath surah from its first non-muqaṭṭaʿāt word.
   - Identifies head-NPs by the locked rule (wCONJ/wP/fCONJ + GEN-noun,
     optionally with intervening DET/Al or DEM modifier).
   - Categorizes each head-NP via locked root → 9-category dictionary.
   - Runs χ² and Mann-Whitney tests as per prereg.

## Bug-fixes during run

- **Bug 1 (`get_prefix_kind`)**: the function early-returned None on any
  `|`-containing feature, but PREFIX rows ALSO contain `|` (e.g.,
  `PREFIX|w:P+`). Fixed by checking `feat.startswith("PREFIX")` first.
  Effect: pre-fix walker was treating ALL waw prefixes as STEM and
  bottoming out at 1 head-NP per surah. Post-fix walker correctly
  identifies the multi-NP clusters.
- **Bug 2 (DEM modifier)**: Q 95:3 (*wa-hādhā l-balad al-amīn*) starts
  with wCONJ+DEM, then Al+N-GEN. The original rule only checked the
  first stem; missed v3. Patched `is_oath_head` to peek at next_word for
  the wCONJ+DEM pattern, per the locked extractor's "optionally with
  intervening DET (Al+) or DEM" clause.
- **Bug 3 (surah verses field)**: assumed `array`/`verses` keys; actual
  JSON uses `total_verses`. Fixed and added asserts on Q 91=15v, Q 103=3v.
- **Category dictionary additions** (post-pilot): added qsm, lqy, wry, ESr
  to the locked categories per documented amendment in the prereg.

## Cell-by-cell results

| Cell | Result |
|---|---|
| 1 | 21/21 with ≥1 head, 21/21 Meccan — PASS |
| 2 (max verses) | Q 91 = 7, next = 5 (Q 77, Q 79) — UNIQUE PASS |
| 2b (max items) | Q 91 = 8, next = 5 (Q 77, Q 79, Q 89) — UNIQUE PASS |
| 3 (cat χ²) | χ² = 24.95, df = 8, p = 0.0016 — PASS |
| 4 (length MW) | U = 769, p = 0.79, dir = LONGER — NULL |
| 5 (theme χ²) | χ² = 1.67, df = 3, p = 0.65 — NULL |

## Key empirical findings

- Q 91 al-Shams holds STRICT MAXIMUM on three independent axes:
  verse-block length (7), head-NP count (8), category-diversity (4).
- Total 62 head-NPs across 21 oath-openers.
- Sworn-by repertoire dominated by KINETIC_AGENTIVE (n=14) and
  TEMPORAL (n=12). PSYCHOLOGICAL category appears EXACTLY ONCE
  (Q 91:7's nafs).
- Length distribution NOT distinct from non-oath Meccan; theme distribution
  remarkably balanced. The oath form is theologically generic.
- Form-content coupling: INSTRUMENTAL_SCRIPTURAL → PROPHETHOOD/QURAN_STATUS;
  KINETIC_AGENTIVE → ESCHATOLOGY (corroborates Farahi).

## Output files

- Prereg: `findings/phase-b-hypotheses/h-new-85-oath-openers-prereg.md`
- Finding: `findings/phase-b-hypotheses/h-new-85-oath-openers.md`
- Script:  `scripts/h_new_85_oath_openers.py`
- JSON:    `findings/phase-b-hypotheses/csv/h-new-85.json`
- Per-head CSV: `findings/phase-b-hypotheses/csv/h-new-85-oath-items.csv`
- Per-surah CSV: `findings/phase-b-hypotheses/csv/h-new-85-per-surah.csv`

## Honest limitations

- Q 52 mechanical-walker count (2 head-NPs) undercounts the classical
  6-item Ṭūr cluster because the v3 *fi raqqin manshūr* phrase is a PP,
  not wCONJ+GEN. Faithful to the locked rule.
- Cell 5 hand-classifies jawāb themes per oath-clusters.md §4 taxonomy.
  Borderline re-classification (Q 86, Q 38) could shift counts by 1–2,
  but χ² p = 0.65 is so far from significance that no re-classification
  rescues it.
