---
test_id: Q047-F-04
title: "Muḥammad-name corpus inventory — exact-attestation count + 4-verse identification"
date_locked: 2026-05-10
seed: 20260509
n_perm: 10000
bonferroni_k: 1
bonferroni_family: Q047-F-04-muhammad-inventory
alpha_bon: 0.05
direction_locked: true
rules_tuple: (no-tashkeel, orthographic-token, graphemes, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)
specialist: Q047-wave-J-specialist
parent_findings:
  - Q047-F-01 (Muhammad-naming density)
  - cross-finding-009 (prophet-named surahs)
classical_anchors:
  - al-Suyūṭī, *al-Itqān fī ʿulūm al-Qurʾān*, nawʿ 17 (asmāʾ al-Nabī fī al-Qurʾān)
  - al-Suyūṭī, *al-Itqān*, nawʿ 22 (asbāb al-nuzūl on Q 3:144, Q 33:40, Q 47:2, Q 48:29)
  - al-Qurṭubī, *al-Jāmiʿ li-aḥkām al-Qurʾān*, on Q 47:2 (naming significance)
---

# Q047-F-04 Pre-registration — Muḥammad corpus inventory

## Hypothesis

The proper name *Muḥammad* (محمد) appears as a standalone token in EXACTLY 4 verses of the Qurʾān (verified Hafs-Kufan, no-tashkeel orthographic-token tuple):

- Q 3:144 (Uḥud retreat: *wa-mā Muḥammadun illā rasūlun*)
- Q 33:40 (seal of prophets: *mā kāna Muḥammadun abā aḥadin min rijālikum*)
- Q 47:2 (those who believe in what was sent down to Muḥammad)
- Q 48:29 (the Conquest: *Muḥammadun rasūlu llāh*)

Additionally, the alternate name *Aḥmad* (أحمد) appears EXACTLY 1× at Q 61:6 (the ʿĪsā prophecy).

Q 47 is the only surah that takes Muḥammad's name as its title.

## Pre-committed prediction (DIRECTION LOCKED)

**Direction-locked**: count(Muḥammad, verse-internal, no-tashkeel) == 4 AND set of attesting (surah, verse) pairs == {(3,144), (33,40), (47,2), (48,29)} AND count(Aḥmad, verse-internal) == 1 AND that attestation is at (61,6).

## Test (Bonferroni-1)

**T1**: count_verses_with_Muhammad == 4 AND set_matches.

This is a corpus-EXACT prediction (not a permutation test): the result is either a perfect match (VINDICATED) or any deviation (NULL/RETRACTED).

α = 0.05 (Bonferroni-1, single corpus-exact prediction).

## Direction-of-effect lock

Pre-committed:
- 4 verse-internal Muḥammad attestations, at the 4 verses listed above.
- 1 verse-internal Aḥmad attestation, at Q 61:6.

If any deviation: NULL.

## Success criteria

- VINDICATED: exact match (count == 4 AND set == pre-listed set AND Aḥmad at (61,6)).
- DIRECTIONAL: ≥3 of 4 verses correct AND total count ∈ {3, 4}.
- NULL: any other outcome.

## Note on title-line

A 5th attestation appears in the title-line of Q 47 ("سورة محمد" / *sūrat Muḥammad*) but title-lines are paratext, not verse-text — they are NOT counted in this inventory (per the rules-tuple's "basmala-counted-only-in-Q1" convention extending to all paratext markers).

## Garden-of-forking-paths log

- BEFORE running: chose "standalone token" not "substring", because *Muḥammad* would otherwise spuriously match within other tokens.
- BEFORE running: chose no-tashkeel variant (default tuple) because tashkeel does not change orthographic identity of *محمد*.
- BEFORE running: confirmed Aḥmad spelling is *أحمد* (with hamza) in Q 61:6 verse text — token-equality test must match this exact form.
- ACKNOWLEDGED: this test largely DUPLICATES Q047-F-01's input verification step (which used 4 verses); the value here is making the EXACT-VERSE attestation set its own load-bearing pre-registered claim, useful for downstream classical-claim audits (al-Suyūṭī *Itqān* nawʿ 17 enumerates 5 names: Muḥammad, Aḥmad, ʿAbdullāh, Bashīr, Nadhīr — testing the *Muḥammad/Aḥmad* count is a discrete sub-claim of his enumeration).
