---
id: H-NEW-95
title: Khawātim al-Ḥashr second-look — exhaustive extension hunt for additional echo verses
phase: B
status: PRE-REGISTERED 2026-04-17
agent: h-new-95-specialist
spec_locked_at: 2026-04-17 (BEFORE running script; directions locked before viewing any result)
bonferroni_family: h-new-95-khawatim-extension
bonferroni_k: 5
alpha_bon: 0.01  # 0.05 / 5
rules_tuple: (no-tashkeel; substring search of definite-singular ال + name with proclitic-prefix tolerance; hafs-kufan; 6236 verses; basmala-counted-only-in-surah-1; mashriqi)
primary_data: /Users/grey/Downloads/quran/quran-text/quran-no-tashkeel.json (114 surahs, 6236 verses)
secondary_data: /Users/grey/Downloads/quran/quran-text/quran-min-tashkeel.json (used for manual-audit verification of borderline matches)
canonical_99_list: /Users/grey/Downloads/quran/data/asma-al-husna.txt
seed: 20260417
n_perm: 10000
direction_A-B: observed counts (descriptive)
direction_C-D: high-degree attractors non-random under verse-permutation null
direction_E: Q59:22-24 dense-rank in top 1% of all 3-verse windows
---

# [[h-new-95-khawatim-extension|H-NEW-95]] — Khawātim al-Ḥashr Extension (Pre-Registration)

## Question

[[h-new-63-khawatim-echo-extended|H-NEW-63]] established that Q 62:1 carries an exact 3-name subsequence of Q 59:23 ("al-Maliki al-Quddūsi al-ʿAzīz"), and that exactly 3 verses in the 6,236-verse corpus contain ≥2 Khawātim names (Q 59:23, Q 59:24, Q 62:1). That count used a specific operationalisation of "Khawātim name"; [[h-new-95-khawatim-extension|H-NEW-95]] does a second-look under the **9-name extended Khawātim inventory** (the 8 classical names plus al-Khāliq, which is Q 59-exclusive under substring rule per H-NEW-59 Cell 2):

> **Extended Khawātim inventory (N=9):** al-Quddūs, al-Salām, al-Muʾmin, al-Muhaymin, al-Jabbār, al-Mutakabbir, al-Khāliq, al-Bāriʾ, al-Muṣawwir.

The goal is to exhaustively hunt for additional echo verses, model the Khawātim as a bipartite graph of names × verses, test whether high-degree attractor verses are non-random, identify Khawātim-rich surahs, and reverse-direction-test Q 59:22-24 for total 99-name density among all 3-verse windows.

## Garden-of-forking-paths disclosure

Pre-existing knowledge before locking this pre-reg:
- H-NEW-59 already identified that 3 Khawātim names are surah-exclusive to Q 59, and al-Salām has 7 occurrences across 7 surahs (most as non-divine "peace/greeting").
- [[h-new-63-khawatim-echo-extended|H-NEW-63]] already identified Q 62:1 as the sole external 2+ Khawātim-name echo verse.
- The MW-5 positive control (Cell E: Q 59:22-24 being dense across ALL 99 names) is not novel — Q 59:23 is already known to be the densest verse ≥10 words per H-NEW-59 Cell 4. Cell E is a tighter 3-verse-window form of that result and functions as sanity.
- The direction of each inferential test (C, D, E) is locked BEFORE viewing any result. Cells A, B are purely descriptive.

Honest protection: writing the pre-reg BEFORE executing; directions in YAML frontmatter; Bonferroni k=5 with α_bon=0.01.

## Locked methodology

### The 9 extended Khawātim names (substring form)

```
KHAWATIM_9 = {
    'القدوس',   # al-Quddūs
    'السلام',   # al-Salām
    'المؤمن',   # al-Muʾmin
    'المهيمن',  # al-Muhaymin
    'الجبار',   # al-Jabbār
    'المتكبر',  # al-Mutakabbir
    'الخالق',   # al-Khāliq
    'البارئ',   # al-Bāriʾ
    'المصور',   # al-Muṣawwir
}
```

Matching uses the word-match-with-proclitic-prefix logic from H-NEW-59 (`scripts/h_new_59_divine_names_distribution.py`), loaded from `quran-no-tashkeel.json`. For al-Salām, all substring occurrences are retained (consistent with H-NEW-59); we report them transparently, flagging non-divine usages. A secondary rerun under "divine-only al-Salām" (= Q 59:23 only) is reported as a robustness check, not as a separate test.

### Muqaṭṭāʿāt set (locked from [[h-new-46-muqattaat-vs-surah-length|H-NEW-46]])

Same 29 surahs as H-NEW-59 / [[h-new-63-khawatim-echo-extended|H-NEW-63]]. (Kept here for reference; not directly used by cells A–E.)

## The 5 pre-registered cells

### Cell A — 1-name echo verses (descriptive)

Enumerate every verse in the corpus containing ≥1 Khawātim name. Report total count, per-name count, and the full verse list.

Output: `cell_A_one_name_echo_verses` JSON block. No inferential test; no Bonferroni slot consumed beyond the family cap.

### Cell B — 2-name echo verses (descriptive, [[h-new-63-khawatim-echo-extended|H-NEW-63]] extension)

Enumerate every verse containing ≥2 Khawātim names. [[h-new-63-khawatim-echo-extended|H-NEW-63]] found 3 such verses under the 8-name inventory (Q 59:23, Q 59:24, Q 62:1). Under the 9-name inventory (adding al-Khāliq), the same verses survive — and any new verse containing ≥2 of the 9 names is newly logged.

Output: `cell_B_two_name_echo_verses` — verse list with names found, per verse.

### Cell C — Co-occurrence network (bipartite + degree)

Build the bipartite graph G = (Khawātim names ∪ verses, edges). Each edge connects a name n to a verse v iff n appears in v. Compute:
- **Verse-degree distribution** (verses × number of distinct Khawātim names in them).
- **High-degree attractor verses**: verses with degree ≥ 2.

**Inferential test (Cell C primary):** under the null H0 that Khawātim-name occurrences are independently scattered across verses proportional to verse word-count, the expected number of verses with ≥2 Khawātim-name occurrences is small but positive. We generate a **verse-permutation null** — for each of the 9 names, re-draw its verse occurrences at random, keeping the per-name token count fixed, with probabilities proportional to verse word-count — and count how many permutation runs produce ≥ K_obs verses with degree ≥ 2.

- Direction: LOCKED — observed number of degree-≥2 verses is higher than null mean (attractor verses are a genuine structural feature).
- N perms = 10,000, seed = 20260417.
- PASS at α_bon = 0.01 if p_one_sided < 0.01.

### Cell D — Surah-level aggregation

Compute per-surah Khawātim-name density d(s) = (total Khawātim-name tokens in surah s) / (total words in s). Rank all 114 surahs. Report top-5.

**Inferential test (Cell D primary):** is the top-5 cluster cohesive under a sensible metric? We operationalize "coherence" as: the top-5's combined Khawātim-name token count as a fraction of the total Khawātim-name token count in the corpus. We compare to a verse-permutation null (same mechanism as Cell C, aggregated to surah).

- Direction: LOCKED — observed top-5 concentration is higher than null.
- N perms = 10,000, seed = 20260417.
- PASS at α_bon = 0.01 if p_one_sided < 0.01.

### Cell E — Reverse direction: Q 59:22-24 density across ALL 99 names (MW-5 sanity)

Compute F(w) for every 3-consecutive-verse sliding window w across the corpus, where F(w) = total distinct 99-name occurrences (token count, summed over all 99 names) in w. Report Q 59:22-24's percentile.

- Direction: LOCKED — Q 59:22-24 is in the top 1% (p < 0.01).
- This is an MW-5 positive control (Khawātim cluster SHOULD fire on total-divine-name density).

## Bonferroni family

- k = 5 (cells A, B, C, D, E)
- α_bon = 0.05 / 5 = 0.01
- Cells A, B are descriptive (no Bonferroni slot strictly consumed, but counted toward k=5 per audit-034 strict policy).
- Cells C, D, E are inferential.

## Pre-committed honesty controls

- Seed = 20260417. Re-run must be bit-identical.
- NULL cells (if C, D, or E fail) published with same prominence as PASS.
- All raw verse lists, degree distributions, and sliding-window histograms published in `csv/h-new-95.json`.
- Ratification rule: any mid-run change to k, α, or direction requires documentation in journal AND is only legitimate if it TIGHTENS α (per Bonferroni asymmetry).

## Outputs

1. `/Users/grey/Downloads/quran/scripts/h_new_95_khawatim_extension.py`
2. `/Users/grey/Downloads/quran/findings/phase-b-hypotheses/csv/h-new-95.json`
3. `/Users/grey/Downloads/quran/findings/phase-b-hypotheses/h-new-95-khawatim-extension.md`
4. `/Users/grey/Downloads/quran/journal/h-new-95-run-1.md`

## Cross-references

- H-NEW-59 (99-names substring catalog)
- [[h-new-63-khawatim-echo-extended|H-NEW-63]] (4-verse extended Khawātim structure via Q 62:1)
- MASTER-LEDGER §2 (canonical 8-name claim; amended to 9 per H-NEW-59)
- [[cross-finding-009-meta-cluster-network|cross-finding-009]] (META-cluster network: Q 62 as 4-cluster meta-hub)
- [[h-new-46-muqattaat-vs-surah-length|H-NEW-46]] (locked muqaṭṭāʿāt set)
- MW-5 (positive-control principle; Cell E sanity on Q 59:22-24)
- M-9 convergence-does-not-multiply: [[h-new-95-khawatim-extension|H-NEW-95]] is a RULE-TUPLE EXTENSION of [[h-new-63-khawatim-echo-extended|H-NEW-63]] (9-name inventory vs 8-name), NOT an independent replication; all findings are co-dependent with H-NEW-59 and [[h-new-63-khawatim-echo-extended|H-NEW-63]].
