---
test_id: Q047-F-02
title: "War-vocabulary density — Q 47 in top-5 corpus-wide (qiṭāl, riqāb, asrā, fidāʾ)"
date_locked: 2026-05-08
seed: 20260508
n_perm: 10000
bonferroni_k: 1
bonferroni_family: Q047-F-02-war-vocab
alpha_bon: 0.05
direction_locked: true
rules_tuple: (no-tashkeel, orthographic-token, graphemes, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)
specialist: Q032-Q047-retry-specialist
parent_findings:
  - h-new-111 (FR distance matrix)
classical_anchors:
  - al-Bukhārī, *Ṣaḥīḥ*, kitāb al-tafsīr (Q 47 verses on jihād)
  - al-Wāqidī, *Maghāzī* — Q 47 contextualized as Medinan war-instruction surah
---

# Q047-F-02 Pre-registration — War-vocabulary density

## Hypothesis

Q 47 is widely characterized as a *qitāl-surah*: Q 47:4 (فاضربوا الرقاب — "strike the necks"), Q 47:35 (لا تهنوا وتدعوا إلى السلم — "do not weaken and call for peace"), Q 47:31 (نبلوكم حتى نعلم المجاهدين — "we will test until we know the strivers"). Hudaybiyya context per Bukhārī.

**Hypothesis**: Q 47 ranks in the top-5 corpus-wide for war-vocabulary density (per-100-words).

War-vocabulary stems (orthographic forms in no-tashkeel):
- قتل، قتال، قاتل، قاتلوا، قتلوا، يقاتل، يقاتلون (qitāl/qatl root forms)
- جهاد، جاهد، جاهدوا، يجاهد، يجاهدون، مجاهد، مجاهدون (jihād root forms)
- ضرب الرقاب، رقاب، الرقاب (riqāb forms)
- أسر، أسرى، أسارى (captive forms)
- فدا، فداء، فدية (ransom forms)
- حرب، الحرب (war forms)
- كفار، الكفار، كفروا، الذين كفروا (combatant disbelievers)
- وثاق، الوثاق (binding/bonds forms)

## Pre-committed prediction (DIRECTION LOCKED)

**Direction-locked**: Q 47 is in the top-5 corpus-wide for war-vocabulary density (per-100-words).

## Test (Bonferroni-1)

**T1**: rank(Q 47) ≤ 5 in the descending-density sorted list of all 114 surahs.

α = 0.05 (single test).

## Direction-of-effect lock

Predicted: Q 47 rank ≤ 5.
If Q 47 rank > 5: NULL.

## Success criteria

- VINDICATED: rank ≤ 3 (very high density).
- DIRECTIONAL: rank ≤ 5 (top-5 confirmed).
- NULL: rank > 5.

## Garden-of-forking-paths log

- BEFORE running: chose orthographic-stem matching (not lemmatized) for transparency. Some Q 9 (Tawba) forms will also match heavily.
- BEFORE running: predicted rank ≤ 5 because Q 9 (Tawba), Q 8 (Anfāl), Q 2 (Baqara — qitāl verses), and Q 4 (Nisāʾ — qitāl verses) are obvious competitors — Q 47 may rank #2 or #3.
- BEFORE running: included الذين كفروا as a war-vocabulary marker because in Q 47 it is consistently the OPPONENT in qitāl context (Q 47:4, 47:32). This is a generous inclusion that may inflate other Meccan surahs slightly.
- HONEST disclosure: this is a corpus-density test; Q 47's 38 verses ÷ ~538 words gives ~14 words per verse — short enough that war-stems concentrate.
