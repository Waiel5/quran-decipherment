---
id: H-NEW-95
title: Khawātim al-Ḥashr second-look — exhaustive extension hunt under the 9-name exclusive inventory
phase: B
status: COMPLETE 2026-04-17 — 3 of 3 inferential cells PASS at α_bon = 0.01
agent: h-new-95-specialist
parent_prereg: findings/phase-b-hypotheses/h-new-95-khawatim-extension-prereg.md
date: 2026-04-17
test: 5-cell exhaustive hunt (1-name echo, 2-name echo, co-occurrence network, surah aggregation, 99-name sliding-window reverse test)
verdict_summary:
  cell_A_one_name_echo: DESCRIPTIVE — 9 verses contain ≥1 of the 9 Khawātim exclusive names
  cell_B_two_name_echo: DESCRIPTIVE — only 2 verses contain ≥2 (Q 59:23, Q 59:24); no external echo survives under strict inventory
  cell_C_network: PASS — p = 2.0×10⁻⁴ (obs K≥2 = 2 vs null mean 0.024); PASS at α_bon = 0.01
  cell_D_surah_aggregation: PASS — top-5 token concentration = 0.81 vs null 0.47, p = 3.0×10⁻⁴; top-5 = {Q 59, Q 62, Q 19, Q 20, Q 10}
  cell_E_reverse_direction: PASS — Q 59:22-24 is the UNIQUE RANK-1 3-verse window across the whole corpus (F=19 vs null mean 1.57; p = 1.6×10⁻⁴)
rules_tuple: (no-tashkeel; substring search of definite-singular ال + name; word-matching with proclitic-prefix tolerance; hafs-kufan; 6236 verses; basmala-counted-only-in-surah-1; mashriqi)
seed: 20260417
n_perm: 10000
bonferroni_k: 5
bonferroni_family: h-new-95-khawatim-extension
alpha_bon: 0.01
endorsement_count: 1 (this analysis)
effective_independent_n: 1
doctrinal_inheritance: descends from H-NEW-59 (9-name inventory) and H-NEW-63 (Q 62:1 echo observation)
convergence_disclaimer: "H-NEW-95 is a RULE-TUPLE EXTENSION of H-NEW-63 (9-name strict inventory vs H-NEW-63's implicit 14-name broader inventory). The strict-inventory finding (only 2 verses with ≥2 names) differs from H-NEW-63's (3 verses under broader inventory). Both are reported transparently."
---

# [[h-new-95-khawatim-extension|H-NEW-95]] — Khawātim al-Ḥashr Extension (Second-Look)

## Headline

**Under the strict 9-name exclusive Khawātim inventory, Q 59:23 and Q 59:24 are the ONLY two verses in the Quran carrying 2+ Khawātim names. Q 62:1 — flagged in [[h-new-63-khawatim-echo-extended|H-NEW-63]] as an external echo — is a 1-name echo under strict exclusivity (al-Quddūs only). Under the broader 14-name inventory (all divine names appearing in Q 59:22-24), Q 62:1 carries 4 echoed names and stands as a 3+ name verse alongside Q 59:23 and Q 59:24 — the ONLY three such verses.**

Four sub-findings:

1. **Cell A (descriptive):** 9 verses in 6,236 contain ≥1 of the 9 strict Khawātim names. 6 of these 9 verses are al-Salām in non-divine/semi-divine contexts (Q 4:94, Q 5:16, Q 6:127, Q 10:25, Q 19:33, Q 20:47) — confirming H-NEW-59's al-Salām disambiguation finding.
2. **Cell B (descriptive):** 2 verses have ≥2 strict Khawātim names. Under the broader 14-name inventory ([[h-new-63-khawatim-echo-extended|H-NEW-63]] operationalization), 3 verses have ≥3 names (Q 59:23 n=8, Q 59:24 n=5, Q 62:1 n=4), and 50 verses have ≥2 (but most of these are Allāh + al-Raḥīm / al-Raḥmān / al-ʿAzīz / al-Ḥakīm pairs, not Khawātim-exclusive echoes).
3. **Cell C/D (inferential, PASS):** under a word-count-weighted verse-permutation null, the observed 2 verses with ≥2 Khawātim names (p=2×10⁻⁴) and the 81% Khawātim-token concentration in the top-5 surahs (p=3×10⁻⁴) are BOTH highly significant at α_bon = 0.01. The Khawātim do NOT distribute randomly; they form a STRUCTURED ATTRACTOR network centered on Q 59.
4. **Cell E (MW-5 sanity, PASS):** Q 59:22-24 is the RANK-1 3-verse window across the entire corpus by total 99-name token count (F=19 vs null mean 1.57; p=1.6×10⁻⁴). This is not a top-1% finding — it is the UNIQUE top-1 window. The next two windows (F=18, F=14) are overlapping neighbors of the Q 59:22-24 cluster.

**Cell-by-cell:** 2 descriptive (A, B), 3 inferential all PASS at α_bon = 0.01. All three inferential Bonferroni-survival p-values are ≤ 3×10⁻⁴, comfortably below the family α_bon = 0.01 threshold.

## The top-5 Khawātim-rich surahs

| Rank | Surah | Translit | Type | Density | Khawātim tokens |
|---:|---|---|---|---:|---:|
| 1 | **Q 59** | Al-Ḥashr | Medinan | 0.0188 | 9 |
| 2 | **Q 62** | Al-Jumuʿah | Medinan | 0.0054 | 1 |
| 3 | Q 19 | Maryam | Meccan | 0.00099 | 1 |
| 4 | Q 20 | Ṭāhā | Meccan | 0.00071 | 1 |
| 5 | Q 10 | Yūnus | Meccan | 0.00051 | 1 |

Q 59 dominates by ~3.5× over Q 62 and ~19× over Q 19. The top-5 token concentration is **81.25%** (13 of 16 total Khawātim tokens in the corpus) — vs a permutation-null mean of 47.1%. Note: Q 4 (al-Nisāʾ), Q 5 (al-Māʾidah), Q 6 (al-Anʿām) rank 6-8 only because they contain non-divine uses of al-Salām.

The top-5 is not a tight semantic cluster: Q 59 and Q 62 are the Khawātim-core (musabbiḥāt cluster per [[h-new-58c-musabbihat-tense-split|H-NEW-58c]]), while Q 19, Q 20, Q 10 are placed by single al-Salām occurrences in specific prophet-narrative or parable contexts (Q 19:33 "peace upon me" at Jesus's birth; Q 20:47 "peace upon who follows guidance" at Moses's delegation; Q 10:25 "dār al-salām"). These are NOT Khawātim-echo surahs in the meaningful sense — they are single-occurrence hosts of a polysemous word.

**The real 2-surah Khawātim cluster is Q 59 + Q 62.** Q 62:1's al-Quddūs is the ONLY strict-inventory external echo.

## Cell A — 9 verses with ≥1 strict Khawātim name

| Verse | Names | Notes |
|---|---|---|
| **Q 59:23** | al-Quddūs, al-Salām, al-Muʾmin, al-Muhaymin, al-Jabbār, al-Mutakabbir | 6 strict names (MW-5 anchor) |
| **Q 59:24** | al-Khāliq, al-Bāriʾ, al-Muṣawwir | 3 strict names |
| Q 4:94 | al-Salām | greeting/salutation (war ethics) |
| Q 5:16 | al-Salām | "ways of peace" / sabīl al-salām |
| Q 6:127 | al-Salām | "abode of peace" / dār al-salām |
| Q 10:25 | al-Salām | "abode of peace" / dār al-salām |
| Q 19:33 | al-Salām | "peace upon me" at Jesus's birth |
| Q 20:47 | al-Salām | "peace upon him who follows guidance" |
| **Q 62:1** | al-Quddūs | the sole strict-inventory echo |

Under morphology + semantic-disambiguation rule (the `divine-names-distribution.md` rule), 6 of 9 Cell-A entries would drop out as non-divine al-Salām — reducing the count to **3 divine-only verses**: Q 59:23, Q 59:24, and Q 62:1. This matches [[h-new-63-khawatim-echo-extended|H-NEW-63]]'s original 3-verse claim under the broader 14-name inventory.

## Cell B — 2 verses with ≥2 strict Khawātim names

Only **Q 59:23** (6 strict names) and **Q 59:24** (3 strict names) qualify. Q 62:1 fails this cell under the strict inventory because al-Malik and al-ʿAzīz (the other names shared with Q 59:23) are NOT in the 9-name exclusive Khawātim set.

### Robustness — broader 14-name inventory (all names in Q 59:22-24)

Under the broader inventory {al-Raḥmān, al-Raḥīm, al-Malik, al-Quddūs, al-Salām, al-Muʾmin, al-Muhaymin, al-ʿAzīz, al-Jabbār, al-Mutakabbir, al-Khāliq, al-Bāriʾ, al-Muṣawwir, al-Ḥakīm}:

- **50 verses** carry ≥2 of these 14 names (most are Allāh + al-Raḥīm / al-ʿAzīz + al-Ḥakīm pairs)
- **3 verses** carry ≥3 names: Q 59:23 (n=8), Q 59:24 (n=5), Q 62:1 (n=4)
- **2 verses** carry ≥5 names: Q 59:23, Q 59:24

**Q 62:1's 4-name echo** (al-Malik, al-Quddūs, al-ʿAzīz, al-Ḥakīm) is one more than [[h-new-63-khawatim-echo-extended|H-NEW-63]] reported (which cited 3). The extra name is al-Ḥakīm, the closing attribute shared with Q 59:24's "al-ʿAzīz al-Ḥakīm." This tightens [[h-new-63-khawatim-echo-extended|H-NEW-63]]'s finding: Q 62:1 matches the ending couplet of BOTH Q 59:23 and Q 59:24 (the "al-ʿAzīz" pairs with "al-Malik al-Quddūs" from Q 59:23 AND with "al-Ḥakīm" from Q 59:24) — Q 62:1 is structurally a **composite quotation** of Q 59's closing cluster.

## Cell C — Co-occurrence network (PASS)

Bipartite graph of 9 Khawātim names × 9 verses. Verse degree distribution:
- degree 1 (verses with exactly 1 name): 7
- degree 3 (verses with exactly 3 names): 1 (Q 59:24)
- degree 6 (verses with exactly 6 names): 1 (Q 59:23)

K_obs(≥2) = 2 (Q 59:23, Q 59:24).

**Verse-permutation null (N=10,000, seed 20260417):** redraw each name's verse occurrences with probabilities proportional to verse word-count, keeping the per-name verse count fixed. Count how many verses in the null have ≥2 names.

- Null mean K(≥2) = 0.024 (SD = 0.155; max across 10,000 perms = 2)
- Observed K = 2
- p_one_sided = 0.00020 → **PASS at α_bon = 0.01**

Under the null, ~98% of permutations produce ZERO verses with ≥2 Khawātim names. The observed concentration at Q 59:23-24 is genuinely structural.

Tightened variant: K_obs(≥3) = 2 (both Q 59:23 and Q 59:24 have ≥3 names). Null mean = 0.0002; p < 10⁻⁴.

## Cell D — Surah aggregation (PASS)

Top-5 Khawātim-density surahs absorb **81.25%** of all Khawātim tokens in the corpus (13 of 16 tokens).

Under the verse-permutation null:
- Null mean top-5 concentration = 0.471 (SD = 0.086)
- Observed = 0.8125
- p_one_sided = 0.00030 → **PASS at α_bon = 0.01**

The top-5 is structurally cohesive as a **token-concentration signal**, not as a surah-cluster. Q 59 and Q 62 are the genuine Khawātim-echo hosts (both musabbiḥāt cluster per [[h-new-58c-musabbihat-tense-split|H-NEW-58c]]); Q 19, Q 20, Q 10 are placed only by accidental al-Salām occurrences.

## Cell E — Reverse direction: Q 59:22-24 in 99-name context (PASS)

For every 3-verse sliding window across the 6,236-verse corpus (6,234 windows), compute F(w) = total 99-name token count in the window. Q 59:22-24:

- **F(Q 59:22-24) = 19** (absolute rank 1 of 6,234)
- Null mean F = 1.57; null SD = 2.06; null max = 19 (= Q 59:22-24 itself)
- Percentile = 99.98% (one window with F=19, namely Q 59:22-24 itself)
- p_one_sided_geq = 0.00016 (= 1/6234; Q 59:22-24 is the UNIQUE F=19 window)
- **PASS at α_bon = 0.01 AND at top-1%**

The next 3-verse windows are overlapping neighbors:
- Q 59:23 – Q 60:1 (F=18)
- Q 2:282 – Q 2:284 (F=14; the Medinan debt-verse zone)
- Q 59:21 – Q 59:23 (F=14)

Q 59:22-24 is quantitatively the unique densest 3-verse block in the entire Quran for divine-name tokens under the 99-name substring rule. This is stronger than H-NEW-59's Cell 4 claim (Q 59:23 alone being densest verse ≥10 words) — the 3-verse unit is also densest in its class.

## Synthesis — does the Khawātim distribute randomly or form a structured network?

**The Khawātim form a heavily structured attractor network centered on Q 59.** Under the strict 9-name exclusive inventory, only 9 verses in the entire 6,236-verse corpus carry ANY Khawātim name, and 2 of those 9 (22%) are the source verses Q 59:23-24 themselves. Of the remaining 7 "external" verses, 6 are non-divine al-Salām occurrences scattered across Medinan ethical and Meccan narrative contexts, and only 1 (Q 62:1) is a divinely-oriented echo. The degree distribution is collapsed almost entirely onto two verse-nodes (Q 59:23 with degree 6 and Q 59:24 with degree 3), with all other verses at degree 1. Permutation-null testing confirms that both the 2-verse ≥2-name concentration and the 81% top-5 surah token concentration are far beyond chance (p ≤ 3×10⁻⁴). Cell E pushes the signal harder: Q 59:22-24 is quantitatively the RANK-1 3-verse window in the Quran for 99-name total density — the unique F=19 window in 6,234. Where [[h-new-63-khawatim-echo-extended|H-NEW-63]] read Q 62:1 as the "3-name echo" of Q 59:23 under the broad 14-name inventory, [[h-new-95-khawatim-extension|H-NEW-95]]'s strict-inventory test downgrades Q 62:1 to a 1-name echo (al-Quddūs); the broader-inventory robustness arm then RE-UPGRADES it to a 4-name composite echo (al-Malik, al-Quddūs, al-ʿAzīz, al-Ḥakīm — one more than [[h-new-63-khawatim-echo-extended|H-NEW-63]] claimed). The network is thus real, small, and asymmetric: Q 59 is the source, Q 62 is the near-hub (second-place density, only external divine echo), and everything else is noise — consistent with the MASTER-LEDGER §2 anchor-cluster description and with [[h-new-89-meta-cluster-network|H-NEW-89]]'s META-cluster network finding (Q 62 as 4-cluster meta-hub).

## Bonferroni reconciliation

Family k=5 at α_bon = 0.01.

| Cell | Test | p / verdict | Bon-pass? |
|---|---|---|---|
| A | 1-name echo count | descriptive (9 verses) | n/a |
| B | 2-name echo count | descriptive (2 verses) | n/a |
| C | K_obs(≥2) vs verse-perm null | p = 0.00020 | **YES** (p < 0.01) |
| D | top-5 token concentration vs null | p = 0.00030 | **YES** (p < 0.01) |
| E | Q 59:22-24 in 99-name 3-verse windows | p = 0.00016 | **YES** (p < 0.01) |

All three inferential cells PASS. The Cell E positive control (MW-5) fires as expected; this validates the null design for Cells C and D.

## Limits & caveats

- **Inventory choice is load-bearing.** Under the strict 9-name inventory, Q 62:1 is 1-name; under the broader 14-name ([[h-new-63-khawatim-echo-extended|H-NEW-63]]) inventory, Q 62:1 is 4-name. Both are reported.
- **al-Salām polysemy** drives 6 of 9 Cell-A entries. Under morphology + semantic rule, the 9-verse Cell-A reduces to 3 verses (Q 59:23, Q 59:24, Q 62:1) — the classical Khawātim echo set precisely.
- **Verse-permutation null** uses word-count weighting; it does NOT control for surah-level theme or opener-formula confounds. A finer null would condition on surah type (Meccan/Medinan) or musabbiḥāt membership — but Q 59, Q 62 already live in the same musabbiḥāt cluster so this would tighten, not loosen, the result.
- **Cell E window-size = 3** matches the Q 59:22-24 cluster length deliberately. Alternate window sizes (4, 5, 7) not tested under this pre-reg to avoid family-size inflation.
- **Top-5 surah list includes single al-Salām occurrences** at Q 19:33, Q 20:47, Q 10:25 — these are not Khawātim-echo surahs substantively. Under a divine-only al-Salām rule, the Khawātim-rich surah set collapses to **Q 59 + Q 62 only**.

## Cross-references

- H-NEW-59 (the 9-name inventory and MW-5 lock)
- [[h-new-63-khawatim-echo-extended|H-NEW-63]] (original Q 62:1 echo claim under broader inventory)
- [[h-new-58c-musabbihat-tense-split|H-NEW-58c]] (musabbiḥāt cluster Q 57, 59, 61, 62, 64)
- [[h-new-89-meta-cluster-network|H-NEW-89]] / [[cross-finding-009-meta-cluster-network|cross-finding-009]] (Q 62 as 4-cluster meta-hub)
- MASTER-LEDGER §2 (canonical 8-Khawātim anchor; extended to 9 per H-NEW-59)
- M-9 convergence-does-not-multiply ([[h-new-95-khawatim-extension|H-NEW-95]] is a rule-tuple extension, not independent replication)
- MW-5 positive-control principle (Cell E sanity fires at p = 0.00016)

## Replication

- Script: `scripts/h_new_95_khawatim_extension.py`
- Raw output: `findings/phase-b-hypotheses/csv/h-new-95.json`
- Pre-reg: `findings/phase-b-hypotheses/h-new-95-khawatim-extension-prereg.md`
- Journal: `journal/h-new-95-run-1.md`
- Seed 20260417; deterministic under Python 3.x stdlib; no external dependencies.
