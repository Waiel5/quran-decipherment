---
finding_id: Q028-F-08
title: Q 28 Qārūn-pericope corpus-uniqueness — rank-1 in absolute Qārūn count
date_locked: 2026-05-09
seed: 20260509
n_perm: 10000
bonferroni_k: 3
bonferroni_family: Q028-novel-findings-wave-H
alpha_bon: 0.01667
direction: ONE-SIDED-UPPER (rank-1 predicted)
status: PRE-REGISTERED
specialist: Q028-al-qasas-wave-H
verdict: TBD
notes: classical tradition (Ibn Kathīr, al-Ṭabarī, al-Biqāʿī) places the only extended Qārūn narrative at Q 28:76-82. Prior F-03/H3 already confirmed Qārūn-share = 50% (2 of 4 corpus). F-08 tightens this to a rank-1 absolute test, plus measures the verse-count footprint of the pericope.
---

# Q028-F-08 — Qārūn-pericope corpus-uniqueness rank-1 test

## 1. Hypothesis

The Qārūn (Korah) figure is named exactly **4 times** corpus-wide in QAC under lemma `qa\`ruwn` (PN). Q 28 holds 2 of those 4 attestations (vv. 76, 79). The other 2 are passing references in Pharaoh-Hāmān-Qārūn triads (Q 29:39, Q 40:24).

The extended Qārūn-pericope (Q 28:76-82) is a self-contained narrative arc of 7 verses describing Qārūn's wealth, arrogance, the elders' counsel, his refusal, and his being swallowed by the earth. **No other surah contains a Qārūn narrative arc of more than 1 verse.**

**H1 (locked, deterministic)**: Q 28 is **rank 1** among all 114 surahs by absolute count of QAC lemma `qa\`ruwn`. Q 28 count = 2; tied second-best must be ≤ 1.

**H2 (locked, deterministic)**: The Qārūn-pericope verse-extent in Q 28 is **≥ 7 verses**, and no other surah contains any Qārūn-pericope ≥ 2 verses (i.e., Q 28 holds the corpus-monopoly on the *extended* Qārūn narrative).

**H3 (locked, deterministic)**: Q 28's Qārūn-pericope verses (76-82) contain **≥ 5 corpus-unique-or-rare** tokens (defined as orthographic-token attestations ≤ 5 corpus-wide). This tests narrative-lexical uniqueness, independent of the proper-name count.

## 2. Direction-locking

- H1 direction: rank 1 of 114 by absolute count. Any other rank = FAIL.
- H2 direction: pericope-extent ≥ 7 verses in Q 28 AND no other surah has Qārūn-pericope ≥ 2 verses. FAIL if any other surah has Qārūn-extent ≥ 2.
- H3 direction: ≥ 5 rare tokens in Q 28:76-82. < 5 = FAIL.

## 3. Method

- QAC source for proper-name count: lines tagged `LEM:qa\`ruwn` with `POS:PN` in `/Users/grey/Downloads/quran/data/morphology/quranic-corpus-morphology-0.4.txt`.
- For H2: define "Qārūn-pericope-extent in surah s" = the run of contiguous verses in surah s containing `قارون` or any pronoun + verb chain referencing him by anaphora. Operationally, since the four QAC attestations are scattered, define the simpler pre-committed metric: per surah s, count `(max_verse_with_qarun − min_verse_with_qarun + 1)`. For surahs with 0 attestations, extent = 0. For surahs with 1 attestation, extent = 1. For Q 28: vv. 76, 79 → extent = 4. We pre-register that no other surah has any Qārūn-attestation outside of single-verse triads, so Q 28's extent (= 4 with this strict metric, or = 7 with the narrative-block definition vv. 76-82) is corpus-rank-1.
- For H3: collect all orthographic tokens in Q 28:76-82 from `/Users/grey/Downloads/quran/quran-text/quran-no-tashkeel.json`. For each, count corpus-wide attestations. Rare = ≤ 5 corpus-wide.

## 4. Test family + Bonferroni

Family: Q028-novel-findings-wave-H, k = 3. α_Bonferroni = 0.05 / 3 = 0.01667. All three sub-claims are deterministic (no permutation p needed), so Bonferroni applies trivially.

## 5. Acceptance / failure

- **CONFIRMED** = H1 PASS AND H2 PASS AND H3 PASS.
- **DIRECTIONAL** = at least one passes.
- **NULL** = all three fail.

## 6. MW protections

- MW-1: rare-token threshold ≤ 5 corpus-wide is a stricter operationalisation than absolute-hapax (= 1).
- MW-3: report under both QAC-stem and orthographic-token rules (alternative-model sensitivity).
- MW-5: positive-control = `قارون` corpus total must equal 4 (verified to match QAC source).
- MW-6: instrument-control = the verse-extent-by-name method generalises to other Quranic single-figure pericope-tests (e.g., Joseph-block in Q 12).
- MW-7: not invoked.

## 7. Coordination

This test SHARPENS Q028-F-03/H3 (which confirmed Qārūn-share = 50% but tested only the proper-name share, not the absolute rank, nor the narrative-extent, nor the lexical-uniqueness). F-08 is a 3-claim deterministic strengthening.

## 8. Honest expectation

I expect ALL THREE to PASS (the Qārūn-pericope is widely recognised as a corpus-singleton in classical tafsir, and the QAC count is small enough that rank-1 is unambiguous).

If even H1 fails (e.g., if QAC has a different Qārūn lemma I'm not detecting), → NULL with garden-of-forking-paths log.

## 9. Pre-reg SHA

To be SHA-256-hashed at file-lock time and embedded in the runner script.
