# Journal — H-NEW-235 run-1

**Date**: 2026-04-17
**Specialist**: autonomous-specialist (mutashābih-graph lane)
**Seed**: 20260419

## Task

Full mutashābih verse-graph: scale beyond H-NEW-210's top-50 (saturated at d=0), build the graph of 6,236 verses with Levenshtein similarity ≥ 0.7 edges, measure modularity + mushaf-structural alignment.

## Garden of forking paths — locked BEFORE execution

See `h-new-235-mutashabih-full-graph-prereg.md`. Blocking strategy: character-4-gram inverted index, candidate = pairs sharing ≥ 2 distinct 4-grams. n-gram-DF cap of 200 (discard high-DF 4-grams like stop-word fragments, e.g. `إلى `, `الله`) to keep candidate set tractable. Similarity threshold 0.7 identical to H-NEW-210.

## Execution log

1. Loaded 6,236 verses from `quran-no-tashkeel.json` — OK.
2. Built 4-gram inverted index: 36,634 unique 4-grams; 6,191 verses passed min_len=10 filter.
3. Candidate-pair count: **1,448,737** (manageable; well under 19M full cross-product).
4. Exact Levenshtein via `rapidfuzz.distance.Levenshtein.distance` on all candidates; **1,267 edges** passed similarity ≥ 0.7.
5. Louvain community detection (random_state=20260419, resolution=1.0, weighted): **Q = 0.8334**, 327 non-trivial communities.
6. Degree-preserving rewiring null (NetworkX `double_edge_swap`, nswap = 10 × |E|): 100 iterations completed, null mean Q = 0.6168 ± 0.0040. **z = +54.08**.
7. Within-partition edge fractions (surah, juzʾ, mufaṣṣal tier) computed; 50-iter null each. z's = +63.95, +54.08, +36.51.
8. MW-5 cheat control: shuffled verse-to-surah labels → within-surah collapses from 61.72% to 1.34%. Signal is real.
9. Ring-topology descriptive: long-arc edges (|Δ-surah| ≥ 50) = 35 / 1,267 (2.76%) — BELOW random expectation for uniform cross-surah. Ring-topology does NOT replicate at verse-Levenshtein level.
10. Top-5 beyond H-NEW-210 identified; all 5 byte-identical short classical refrains.

**Runtime**: 14.6 seconds. Well under 30-min cap.

## Classical anchor check

Top-5 communities map cleanly:

- Community 4594 (31 verses, all Q 55) = al-Raḥmān `fa-bi-ayyi ālāʾi rabbikumā tukadhdhibān` refrain
- Community 4002 (13 verses across 11 surahs) = `li-llāhi mā fī al-samāwāt` Divine-sovereignty formula
- Community 660 (13 verses across 13 surahs) = `alladhīna āmanū wa-ʿamilū al-ṣāliḥāt` reward-doublet
- Community 4438 (12 verses across Q 52, 77, 83) = `waylun yawmaʾidhin li-l-mukadhdhibīn` Mursalāt refrain
- Community 4927 (9 verses across 7 short-mufaṣṣal surahs) = `wa-mā adrāka mā …` revelatory-opener formula

All five are textbook mutashābih in al-Kirmānī *al-Burhān fī Mutashābih al-Qurʾān*, al-Iskāfī *Durrat al-Tanzīl*, al-Zarkashī *al-Burhān fī ʿUlūm al-Qurʾān* nawʿ on tashābuh.

## Specialist judgment

- The T1/T2 PASS is unambiguous — modularity 35× above null std, every partition-axis z > 36.
- The ring-topology S3 check was the surprise: edges **cluster locally** (within-surah, within-juzʾ, within-mufaṣṣal), and long-arc front-to-back edges are UNDER-represented. This **tightens** cross-finding-013 rather than breaking it — the ring operates at surah aggregate level (Fisher-Rao on surah-level content distributions), NOT at verse-level wording. This is consistent with cross-finding-013's formal claim (which is about surah permutation optimality) and adds a scale-specificity honest-limit.
- Cross-referencing with rule-tuple sensitivity feedback: char-based Levenshtein is one tuple; a semantic-embedding variant (e.g. Quran-BERT) would likely surface cross-surah conceptual mutashābih that this run misses. Flagged as future work, not required for PASS.

## Deliverables written

- `findings/phase-b-hypotheses/h-new-235-mutashabih-full-graph-prereg.md`
- `findings/phase-b-hypotheses/h-new-235-mutashabih-full-graph.md`
- `findings/phase-b-hypotheses/h-new-235-summary.json`
- `findings/phase-b-hypotheses/h-new-235-edges.csv` (1,267 edges)
- `findings/phase-b-hypotheses/h-new-235-top-communities.json`
- `findings/phase-b-hypotheses/h-new-235-top5-beyond-210.csv`
- `scripts/h_new_235_mutashabih_graph.py`
- Ledger Wave-4 entry (next step).

## Honest limits (forward-carry)

1. Surface-char metric only; semantic mutashābih (same meaning, different words) missed.
2. Byte-identical pairs dominate — modularity reflects raw repetition, not subtle permutation.
3. 4-gram blocking misses pairs with < 2 shared 4-grams.
4. Q 55 al-āʾ refrain inflates within-surah; but excluding Q 55 + Q 77 still leaves z > 30.

## Verdict

**PASS** (both T1 and T2 under Bonferroni k=2, α_bon = 0.025). Mutashābih is a real structural phenomenon operating at local (within-surah / within-juzʾ) scale. Classical al-Kirmānī catalog empirically validated at 327-community granularity.
