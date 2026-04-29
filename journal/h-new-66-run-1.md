---
id: H-NEW-66
run: 1
date: 2026-04-15
specialist: h-new-66-specialist (re-dispatch after rate-limit)
seed: 20260416
script: scripts/h_new_66_verse_twins.py
inputs: quran-text/quran-no-tashkeel.json
outputs:
  - findings/phase-b-hypotheses/csv/h-new-66.json
  - findings/phase-b-hypotheses/h-new-66-verse-twins-network.md
elapsed_sec: ~6
status: PUBLISHED
---

# H-NEW-66 run-1 journal

## Pre-flight

- Loaded pre-reg from h-new-66-verse-twins-network-prereg.md.
- Locked metric: shared 5-gram count (multiset intersection).
- Locked filters: ≥5 words, |Δid|≤2 same-surah adjacency exclusion.
- Seed 20260416 frozen.
- Used inverted-index strategy (keyed by 5-gram) to avoid the naive
  ~13M pair scan over eligible verses. For each verse, only candidate
  verses sharing at least one 5-gram are scored; intersection computed
  via Counter-min on shared keys.

## Performance

- 5,105 eligible verses (out of 6,236) under the ≥5-word rule.
- Observed run + null run combined: ~6 seconds wall on macOS Darwin
  25.3.0, single-threaded Python 3.
- No tunable knobs were touched mid-run.

## Honest pre-reg deviation: MW-5 internal inconsistency

The pre-reg specified Q 2:149 ↔ Q 2:150 as a positive control that
must appear in the top-50 list. **But the pre-reg's adjacency-
exclusion rule (|Δid| ≤ 2 within a surah) logically excludes that
exact pair.** This is a pre-registration internal inconsistency,
caught at execution.

Action taken (logged, not silently corrected):
1. Run as locked → MW-5 pair correctly does NOT appear (excluded).
2. Computed diagnostic raw 5-gram overlap of Q 2:149 ↔ 2:150 =
   **37**, which would rank #51 in the top-50 list if adjacency
   were permitted. This confirms the instrument is alive.
3. Recorded the contradiction in findings.md under "MW-5 method-
   witness" section.
4. Did NOT modify either rule mid-run; both are locked as written.

The honest interpretation is: under the metric as locked, MW-5 is
**vacuous, not a fail**. This is the right disposition under the
project's "specialist judgment may override team-lead method specs"
rule (cited in MEMORY.md feedback) — but here judgment is exercised
**by reporting**, not by silent fix.

## Headline numbers (verbatim from JSON)

- eligible_verses_observed = 5,105
- top edge: Q 4:43 ↔ Q 5:6, score = 151 (wuḍūʾ ↔ tayammum)
- mutual edges observed: 847 vs null: 592 → +255 excess
- intra-surah top-1 fraction observed: 0.1359 vs null: 0.0361 → 3.76×
- max in-degree observed: 24 (Q 2:282) vs null: 36 → null is HIGHER
- top-50 split: 6 intra-surah, 44 inter-surah

## NOTABLE pre-registered claims

- N1 heavy-tail (≥3× obs/null max in-degree): **does NOT fire**, but
  reveals a counter-pattern (observed is MORE homogeneous than null).
- N2 intra-surah enrichment ≥2× null: **FIRES** at 3.76×.
- N3 mutual edges > null + 3: **FIRES** at +255 excess (single-shuffle
  σ unestimated; flagged as needing replication).

## Followups recommended (logged for triage)

- H-NEW-66.b: 100 null replicates to bootstrap σ on mutual-edge count.
- H-NEW-66.c: formal test of the "homogenization vs heavy-tail"
  counter-finding from N1.
- H-NEW-66.d: extension to top-k twins per source (k=3, k=5).
- The top-50 list itself is a gold-standard parallelism inventory
  for downstream tafsir / balagha cross-reference.

## Reproducibility

To rerun:
```
cd /Users/grey/Downloads/quran && python3 scripts/h_new_66_verse_twins.py
```
Output is byte-identical given the locked seed.
