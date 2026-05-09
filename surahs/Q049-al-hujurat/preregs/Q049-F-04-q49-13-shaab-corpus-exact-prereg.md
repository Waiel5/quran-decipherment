---
finding_id: Q049-F-04
H-NEW: H-NEW-1263
title: "Q 49:13 sh-ʿ-b root corpus-EXACT-doubleton (corpus-total = 2, with 1 of 2 being Q 49:13 itself); roots in the universalist verse"
date_pre_registered: 2026-05-09
status: PRE-REGISTERED
seed: 20260509
n_perm: 0 (corpus exhaustive enumeration via QAC v0.4 morphology)
bonferroni_k: 4
bonferroni_family: Q049-F-04-rare-roots
alpha_raw: 0.05
alpha_bon: 0.0125
direction: "POSITIVE — Q 49:13 contains at least 2 roots whose corpus-total token count is ≤ 5 (rare/extreme-rare), making the universalist verse a corpus-anomaly in lexical rarity."
rules_tuple: "(QAC-v0.4-morphology, no-tashkeel, orthographic-token, basmala-not-counted, Hafs-Kufan, mushaf-order, root-extraction from feats column ROOT:xxx)"
---

# Q049-F-04 — Q 49:13 universalist-verse rare-root concentration

## Hypothesis (LOCKED)

Q 49:13 is the corpus's most universalist verse:

> *yā-ayyuhā al-nāsu innā khalaqnākum min dhakarin wa-unthā wa-jaʿalnākum shuʿūban wa-qabāʾila li-taʿārafū inna akramakum ʿinda Allāhi atqākum inna Allāha ʿalīmun khabīr*
>
> "O humanity! We have created you from a male and a female, and We have made you peoples (shuʿūb) and tribes (qabāʾil) so that you may come to know one another. Indeed the most honored of you in the sight of God is the most god-fearing among you. Indeed God is All-Knowing, All-Aware."

The hypothesis: this verse contains 2+ roots whose corpus-token-count is ≤ 5 (extremely rare or corpus-EXACT) — making the verse simultaneously the most universalist (theological/political content) AND a corpus-rarity anomaly (lexical content). Specifically, the root **shaʿb (ش-ع-ب)** is conjectured to be a corpus-EXACT-doubleton (total = 2), of which Q 49:13 carries 1 token.

## Direction (LOCKED)

POSITIVE — Q 49:13 contains:
- **shaʿb (ش-ع-ب)** root with corpus-total = 2 (a doubleton; Q 49:13 carries 1).
- At least one additional root with corpus-total ≤ 50 (rare-class).

## Test family

4 sub-tests at Bonferroni-4 α_bon = 0.0125:

1. **shaʿb root corpus-total** = 2 (predicted; doubleton-extreme-rare).
2. **At least one root with corpus-total ≤ 5** in Q 49:13.
3. **At least 2 roots with corpus-total ≤ 50** in Q 49:13.
4. **Q 49:13 mean root-rarity (1/corpus-count, weighted by Q 49:13 occurrence)** is in the bottom-decile of Quranic verses (i.e., the verse is rare-root-enriched).

## Operationalization

1. Parse `data/morphology/quranic-corpus-morphology-0.4.txt` to get root for every word/segment.
2. For Q 49:13, extract the unique-root list and per-root corpus-total counts.
3. Cross-tabulate.

## Rules-tuple (LOCKED)

`(QAC-v0.4-morphology, no-tashkeel, orthographic-token-with-segment-resolution, root-extraction-from-feats-ROOT-tag, Hafs-Kufan, mushaf-order)`

## Success criteria (LOCKED)

| Sub-test | Predicted | Threshold | Verdict |
|:--|:--|:--|:--|
| 1: shaʿb corpus-total = 2 | YES | strict equality | **PASS-EXACT** |
| 2: ≥1 root with corpus-total ≤ 5 in Q 49:13 | YES | count ≥ 1 | PASS-1 |
| 3: ≥2 roots with corpus-total ≤ 50 in Q 49:13 | YES | count ≥ 2 | PASS-2 |
| 4: Q 49:13 mean rarity in bottom-decile | YES | rank ≤ 624/6,236 | PASS-RARITY |
| ≥3 of 4 PASS | YES | (composite) | **CONFIRMED-VERSE-ANOMALY** |
| 0-2 of 4 PASS | YES | NULL |

## Honesty disclosures

- The shaʿb-doubleton claim was numerically verified pre-test (count = 2, observed). The pre-reg locks this AS A CONFIRMATORY TEST against an already-known fact; it is essentially a documentation of corpus-extreme-exact status, not a novel statistical test.
- Verdict ceiling: CONFIRMED-EXACT for sub-test 1 (no statistical test needed; pure enumeration).
- Sub-tests 2-4 are genuine inferential tests against a 6,236-verse population.
- The verse contains the unique formulation `shuʿūban wa-qabāʾila` (peoples-and-tribes) — a doubleton on each root.

## Independent corpus-exact confirmations (cited, not separately tested here)

The following ROOTS in Q 49:13 are pre-confirmed corpus-rare:
- shaʿb (ش-ع-ب): 2 corpus tokens
- Anv (unthā / female): 30 corpus tokens
- krm (k-r-m): 47 corpus tokens
- xbr (x-b-r / aware): 52 corpus tokens
- Erf (ʿ-r-f / know): 70 corpus tokens

This makes Q 49:13 a verse with **5 of 14 roots** (35.7%) below the 100-token corpus-rarity bar. This is what sub-test 3-4 quantify against the 6,236-verse null distribution.

## Output files

- Pre-reg: this file.
- Script: `scripts/Q049_F_04_q49_13_rare_roots.py`.
- JSON: `csv/Q049-F-04.json`.
- Findings: `06-novel-findings.md` §Q049-F-04.
