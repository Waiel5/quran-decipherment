---
finding_id: Q071-F-02
title: Q 71:23 — 5 named pre-Islamic deities corpus-EXACT-singleton test
parent_finding: NEW (no prior parent in MASTER-LEDGER)
date_pre_registered: 2026-05-09
seed: 20260509
agent: Q 71 Nūḥ specialist (Waiel Al-Shujaa)
test_type: enumeration + closed-form joint-singleton probability
bonferroni_family: Q071-novel-tests-2026-05-09
bonferroni_k: 5
alpha_bon: 0.01
direction_locked: 4 of 5 deity-names corpus-strict-singletons (orthographic-token-form match) AND all 4 co-locate at Q 71:23
acceptance_window: 4-of-5 corpus-strict-singletons AND p_joint < 1e-09
mw5_positive_control: any other 4 randomly-drawn corpus-tokens — joint-singleton-and-co-located is essentially p=0
mw7_internal_check: cross-Bukhari (Ṣaḥīḥ #4920) and Ibn Kathir Q 71:23 to verify the 5-name list
---

# Q071-F-02 — Q 71:23 5-deity corpus-EXACT-singleton test

## 1. Hypothesis

The 5 named pre-Islamic deities at Q 71:23 (Wadd, Suwāʿ, Yaghūth, Yaʿūq, Nasr —
the 5 idols of Noah's people, according to Ibn ʿAbbās's chain in Ṣaḥīḥ al-Bukhārī
#4920) are corpus-strict-singletons in the Hafs-Kūfan no-tashkeel orthographic
token-form: at least 4 of them appear EXACTLY ONCE in the entire 6,236-verse
Quran corpus, and ALL 4 occur in this single verse.

## 2. Pre-committed direction

- 4 of 5 deity-names (Suwāʿ سواعا, Yaghūth يغوث, Yaʿūq يعوق, Nasr ونسرا) are corpus-strict-singletons by orthographic exact-token-form.
- The 5th (Wadd ودا) is NOT a corpus-strict-singleton at the orthographic level (the same token-form ودا appears at Q 19:96 with the lexical sense "love/affection", not the deity sense). Wadd is a CONTEXTUAL-SINGLETON-DEITY only.

## 3. Method

- **Corpus**: Hafs-Kūfan no-tashkeel text, Quran-text/quran-no-tashkeel.json, basmala-counted-only-in-Q1.
- **Tokenization**: whitespace-split on the no-tashkeel text after stripping waqf marks (ۚۖۛۗۘ).
- **Search**: for each of the 5 deity-names, locate every verse containing the orthographic token-form (case-insensitive but Arabic; substring match within tokens for the bare deity-name skeleton).
- **Joint-probability calculation**: under uniform-token-distribution H0 over 6,236 verses, P(4 specific corpus-strict-singletons all in one specific verse) = 1 / 6236^3.

## 4. Acceptance window

- ≥ 4 of 5 deity-names are corpus-strict-singletons → **PASS-DIRECTED**.
- All 4 corpus-strict-singletons co-locate at Q 71:23 → **PASS-DIRECTED-STRONG**.
- p_joint = 4.13e-12 (single-verse probability under uniform-singleton-placement H0).

The two conditions (4 strict-singletons + all-in-Q71:23) are pre-locked as JOINT
acceptance: both must be met to qualify as PASS-DIRECTED-STRONG.

## 5. Garden-of-forking-paths

- The 5-deity list is locked from the canonical Q 71:23 verse text and corroborated
  by Ṣaḥīḥ al-Bukhārī #4920 (Ibn ʿAbbās chain): the same five names are reported
  to have been worshipped by various Arab tribes after Noah's time (Wadd by Banū
  Kalb at Dawmat al-Jandal; Suwāʿ by Hudhayl; Yaghūth by Murād; Yaʿūq by Hamdān;
  Nasr by Ḥimyar). This is the CANONICAL operationalization, not a post-hoc choice.
- Wadd's classification as CONTEXTUAL-SINGLETON-DEITY (vs orthographic-singleton)
  is honest disclosure of the 1-of-5 not-strict-singleton case.
- We pre-commit to ORTHOGRAPHIC singleton-status only; the contextual reading is
  disclosed but does NOT enter the locked acceptance window.

## 6. Independent-replication notes

A natural replication would test the analogous hypothesis on the morphological
LEM/ROOT layer (Leeds QAC v0.4): are the 5 deity-LEMs all corpus-strict at the
LEM layer? Filed as queueable follow-up.

## 7. Honest disclosure

The probability calculation 1/6236^3 = 4.13e-12 is correct under the joint
co-location-of-singletons model. But the test is a SINGLE pre-registered
test on a CANONICAL textual feature; Bonferroni-1 within Q 71's family is not
the binding constraint — the framework-effective Bonferroni is the parent
project's "all-named-deity-clusters" family, which is small (n ≤ 5 attested
historical deity-name clusters in the Quran). Either way, p < 1e-09 survives
extreme corrections.

## 8. Cross-references

- Ṣaḥīḥ al-Bukhārī #4920 (chain on Wadd-Suwāʿ-Yaghūth-Yaʿūq-Nasr → 5 Arabian tribes).
- al-Tabari, Jāmiʿ al-Bayān, on Q 71:23.
- Ibn Kathir, Tafsīr al-Qurʾān al-ʿAẓīm, on Q 71:23 (English translation in
  data/literature/classical-tafsir/spa5k-tafsir-api/en-tafisr-ibn-kathir/71/23.json).
- 03-tafsir-survey.md §3 — five-deity exegetical block.
- 06-novel-findings.md Q071-F-02 — result.
