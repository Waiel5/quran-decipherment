---
surah: 39
test_id: Q039-F-04
title: Q 39 — corpus-UNIQUE self-ring (tanzīl-opener + hamd-closer + rabb-al-ʿālamīn echo)
file_type: pre-registration
date_locked: 2026-05-09
seed: 20260509
n_perm: 10000
bonferroni_k: 4
bonferroni_family: Q039-novel-tests
alpha_bon: 0.0125
direction: q39_self_ring_corpus_unique
---

# Q039-F-04 — Pre-registration: Q 39 self-ring composition formal test

## 1. Hypothesis (locked before observation)

MASTER-LEDGER §10.27 establishes that Q 39 is the ONLY surah from the H-NEW-1100 tanzīl-opener cluster {Q 32, 39, 40, 41, 45, 46} that ALSO appears in the hamd-closer cluster {Q 17, 27, 37, 39}. This is identified by the ledger as a **corpus-unique self-ring composition signature**.

Q 39:1: *tanzīl al-kitāb min Allāh al-ʿAzīz al-Ḥakīm*
Q 39:75: *...wa-qīla al-ḥamdu li-llāhi rabb al-ʿālamīn*

The phrase *al-ḥamdu li-llāhi rabb al-ʿālamīn* is the verbatim closure of Q 1:2 (*al-Fātiḥa*'s opener). Q 39 closes by speaking the formula that opens al-Fātiḥa.

**Question pre-registered:** Is the Q 39 self-ring corpus-UNIQUE under a formal cross-set test? Specifically:

**H1 (direction-locked):** The intersection |tanzīl-cluster ∩ hamd-closer-cluster| = 1 (only Q 39); under permutation null where 6 random surahs are drawn for "set-A" and 4 random surahs are drawn for "set-B" both from {1...114}, the expected intersection is 6×4/114 = 0.21. Q 39 is corpus-UNIQUE if the |intersection| ≥ 1 with cardinality EXACTLY = 1. Test: perm-p that random-A ∩ random-B has intersection ≥ 1 AND ≤ 1 (i.e., exactly-1 or zero). One-tailed by p(observed exactly-1 OR more) at α_bon = 0.0125.

(This is a test of the JOINT structural claim, not the "exactly-1" edge case. Better operationalization → see H2.)

**H2 (direction-locked, primary):** Define `self_ring_score(s)` = `tanzil_opener_member(s)` × `hamd_closer_member(s)`, returning 1 if surah s is in BOTH sets, 0 otherwise. The Q 39 score is 1. The corpus-wide sum is 1. Under null where surah indices are shuffled 10,000 times for the hamd-closer set (4 random surahs), p = fraction of shuffles where the random-4 hamd-set intersects the FIXED tanzīl-set {32, 39, 40, 41, 45, 46} at least once. Q 39's UNIQUE membership in both is "1 of 6 tanzīl members landing in 1 of 4 hamd-closer slots".

**H3 (direction-locked, secondary, corpus-UNIQUE rabb-al-ʿālamīn-echo):** Beyond set-membership, test whether Q 39 is the ONLY surah where the closing verse echoes verbatim the *al-ḥamdu li-llāhi rabb al-ʿālamīn* of Q 1:2. Operationalized: Q 39:75 contains the exact phrase. Other 113 surahs' last verses tested for inclusion; expected count for hamd-closer set is 4 surahs with closing al-ḥamdu, but only Q 37:182 also has *rabb al-ʿālamīn*. Then Q 39 + Q 37 are the 2 surahs with this exact echo at last verse. Q 39's specific tanzīl-opener + rabb-al-ʿālamīn-closer is the SELF-RING that Q 37 lacks (Q 37 is NOT in tanzīl cluster).

**Pre-commit violation conditions:**
- H2 reverse: random-4 hamd-set intersects tanzīl-set EVERY shuffle → self-ring is statistical noise.

**H0:** Q 39 is one of many possible tanzīl ∩ hamd-closer overlaps; no architectural significance.

## 2. Operational definitions

- tanzīl-cluster (H-NEW-1100): T = {32, 39, 40, 41, 45, 46} (locked).
- hamd-closer cluster (MASTER §10.27): H_close = {17, 27, 37, 39} (locked).
- rabb-al-ʿālamīn-closer cluster: H_close_rba = {s : last verse of s contains the orthographic-string رب العالمين as final 2 words}, computed at runtime.

### Test 1 (H1) — set-membership intersection significance
- T ∩ H_close (observed) = {39}, |intersection| = 1.
- Null: 10,000 random 4-subsets H_random of {1,...,114}; record |T ∩ H_random|.
- p = fraction with |intersection| ≥ 1.

### Test 2 (H2) — equivalent perm test on hamd-closer set
- Same as H1 but null permutes T instead. Symmetric check.
- Direction-locked: Q 39 is in both sets, so observed intersection ≥ 1.

### Test 3 (H3) — verbatim rabb-al-ʿālamīn-closer
- For each of 114 surahs, take last verse, check if it ends with `رب العالمين` (after waqf strip).
- Count surahs satisfying.
- Per Q 39:75 final 2 words: `العالمين` is final word; preceded by `رب`. Q 37:182 ends similarly.
- Direction-locked: this set should be small (≤ 5).
- Test: under a null where last-verse text is replaced by random within-surah verse, fraction with rabb-al-ʿālamīn closer.

### Combined verdict
H1, H2, H3 each at α_bon = 0.0125. Multi-test pass = STRONG self-ring; single = PASS-DIRECTED.

## 3. Empirical anchors (verified pre-reg)

- Q 39:1 first 6 words: *tanzīl al-kitāb min Allāh al-ʿAzīz al-Ḥakīm* (verified from JSON).
- Q 39:75 final 4 words: *al-ḥamdu li-llāhi rabb al-ʿālamīn* (verified).
- Q 1:2 in full: *al-ḥamdu li-llāhi rabb al-ʿālamīn* (verbatim match).
- Q 37:182 (verified): *wa-l-ḥamdu li-llāhi rabb al-ʿālamīn*.
- The full tanzīl-cluster T = {32, 39, 40, 41, 45, 46}: verified opener forms in MASTER-LEDGER §10.24.
- The hamd-closer cluster H_close = {17, 27, 37, 39}: per MASTER-LEDGER §10.27.

## 4. Success / Failure

- **CONFIRMED-DIRECTED**: H1, H2, H3 all pass at α_bon = 0.0125.
- **PASS-DIRECTED**: ≥1 of H1/H2/H3 passes.
- **NULL**: All fail.

## 5. Honest limits

- This test is REPLICATIVE of MASTER-LEDGER §10.24 + §10.27 structural-form-cluster work; it is not finding NEW structure but pre-registering a formal verification. Confirmation strengthens the §10.27 self-ring claim; rejection would refute it.
- The H1, H2, H3 tests are statistically dependent (same T set, similar H sets). Bonferroni-3 within this prereg WAS NOT applied — H1, H2 are essentially the same test, and H3 is on a different operationalization. The reported p-values should be interpreted as joint evidence, not 3 independent tests.
- Self-ring composition is a known classical-balāgha concept (al-Biqāʿī *Naẓm al-Durar*: *iʿādat al-ʿajz ʿalā al-ṣadr* / *radd al-ʿajz ʿalā al-ṣadr*); this test is the formal-empirical verification at the surah scale.

## 6. Bonferroni & rules-tuple

- Family `Q039-novel-tests`, k=4 (counted at family level: H1+H2+H3 collectively count as 1 cell of the family of 4 tests; α_bon = 0.0125 applies to the most-stringent passed cell).
- Rules-tuple: (no-tashkeel, orthographic-token, graphemes, basmala-counted-only-in-Q1, Hafs-Kufan).
- Seed 20260509.
