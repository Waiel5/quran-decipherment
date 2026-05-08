---
finding_id: Q050-F-02
title: "Q 50 body-part metaphor density vs corpus null"
date_pre_registered: 2026-05-07
status: PRE-REGISTERED
seed: 20260507
n_perm: 10000
bonferroni_k: 1
bonferroni_family: Q050-F-02-bodyparts
alpha_raw: 0.05
alpha_bon: 0.05
direction: "POSITIVE — Q 50 has a body-part-metaphor density (token-rate per 1000 word-tokens) higher than the corpus mean and higher than ≥ 95% of length-matched random Quran-verse samples."
rules_tuple: "(no-tashkeel, orthographic-token, exact-substring root-match against pre-locked vocab list, basmala-not-counted-in-Q50, Hafs-Kufan, mushaf-order)"
---

# Q050-F-02 — Body-part metaphor density audit

## Hypothesis (LOCKED)

Q 50 contains the famous Q 50:16 *naḥnu aqrabu ilayhi min ḥabli al-warīd* ("we are closer to him than his jugular vein") and other body-part-anchored verses (Q 50:33 *bi-l-ghaybi*, Q 50:37 *qalb*, Q 50:18 *qawl* + verbal-tongue, Q 50:41 *yawma yunādī al-munādi min makānin qarīb*). The hypothesis: Q 50 has a per-token rate of body-part-vocabulary that exceeds 95% of length-matched random Quran-verse samples.

## Locked vocabulary (BODY-PART ROOTS, FROM CLASSICAL TAFSIR)

The body-part vocabulary is locked by reading classical tafsir on Q 50 (al-Ṭabarī, al-Qurṭubī, al-Rāzī) PRIOR to running the test. The list:

| Arabic root/lemma | English | Source |
|:--|:--|:--|
| ورد (ḥabl al-warīd) | jugular vein | Q 50:16 |
| قلب | heart | Q 50:37 |
| لسن (lisān) / قول | tongue / speech | (general) |
| نفس | soul | Q 50:16 |
| عين | eye | (general) |
| سمع (samʿ) | hearing | Q 50:37 |
| بصر | sight | (general) |
| جلد (jild) | skin | (general) |
| روح (rūḥ) | spirit | (general) |
| دم (damm) | blood | (general) |
| لحم (laḥm) | flesh | (general) |
| عظم (ʿaẓm) | bone | (general) |
| رأس (raʾs) | head | (general) |
| يد (yad) | hand | (general) |
| رجل (rijl) | foot/leg | (general) |
| فم (fam) | mouth | (general) |
| اذن (ʾudhun) | ear | (general) |

The exact substring patterns (no-tashkeel, root-stem prefixes/suffixes allowed) are locked in the run script.

## Direction (LOCKED)

POSITIVE — Q 50's body-part token-rate per 1000 words is hypothesized to exceed the 95th percentile of a length-matched random-window null distribution.

## Null model

For each of N=10000 permutation iterations:
1. Pick a random contiguous window of K=45 verses from the Quran (Q 50 has 45 verses; matched window length).
2. Count the body-part-vocabulary tokens in that window using the LOCKED vocabulary list.
3. Compute body-part rate per 1000 word-tokens.

The null distribution is the 10000 random-window rates; Q 50's rate is compared.

## Rules-tuple (LOCKED)

`(no-tashkeel, orthographic-token, exact-substring root-match against pre-locked vocab list, basmala-not-counted-in-Q50, Hafs-Kufan, mushaf-order)`

Substring match is performed on token-stripped text (Quranic mushaf marks removed). Exact substring matching of root-stems (not full inflectional matches) — the locked vocabulary is searched as a substring within token-text.

## Success criteria

| p-value | Verdict |
|:--|:--|
| p < 0.05 (1-sided) | **CONFIRMED** (Q 50 is body-part-dense) |
| 0.05 ≤ p < 0.10 | DIRECTIONAL |
| p ≥ 0.10 | NULL |

## Failure criteria

If Q 50's rate is BELOW the 50th percentile → NULL on body-part-density claim. (Pre-commit violation if so.)

## Output files

- Pre-reg: this file (`preregs/Q050-F-02-body-part-density-prereg.md`).
- Script: `scripts/Q050_F_02_body_part_density.py`.
- JSON: `csv/Q050-F-02.json`.
- Findings: `06-novel-findings.md` §Q050-F-02.
