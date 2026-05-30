---
surah: 102
surah_name_ar: التكاثر
surah_name_translit: al-Takāthur
file_type: novel-findings
date_last_updated: 2026-05-30
phase: B+
verdict: Q102-F-01 — Arm A CONFIRMED (corpus-unique triple-kallā run) + Arm B DIRECTIONAL (bare-threat singleton ✓; thumma-refrain a 3-member family, pre-commit violation on B-H1)
seed: 20260509
n_perm: 10000
---

# Q 102 al-Takāthur — Pre-Registered Novel Findings

One pre-registered two-arm test, run with seed 20260509 and 10,000 permutations (Arm B-H3 supporting
context only); pre-reg SHA-256 locked before computation and verified at runtime (printed "SHA OK").

- **Pre-reg:** `surahs/Q102-al-takathur/Q102-F-01-kalla-reduplication-prereg.md`
- **Pre-reg SHA-256:** `87433a4dd51b12605a09e63140437f480ac2e551b05014137837b0d31046acf4`
  (re-verified 2026-05-30: computed SHA of the pre-reg file == embedded EXPECTED_SHA in the script == `prereg_sha` in the JSON)
- **Script:** `scripts/Q102_F_01_kalla_reduplication.py` (verifies SHA at runtime, fail-fast)
- **JSON:** `surahs/Q102-al-takathur/csv/Q102-F-01.json`
- **Rules-tuple:** `(no-tashkeel, orthographic-token, QAC v0.4 POS:AVR LEM kal~aA, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)`

---

## Q102-F-01 Arm A — the corpus-UNIQUE 3-consecutive-verse rebuke-*kallā* run (CONFIRMED)

**Hypothesis (pre-committed):** Among all 114 surahs, Q 102 is the UNIQUE carrier of a run of **3
consecutive verses** each bearing a genuine rebuke-*kallā* (POS:AVR LEM `kal~aA`); every other surah's
maximum consecutive-*kallā* run is ≤ 2.

- **A-H1 (verification):** Q 102 has exactly 3 rebuke-*kallā* tokens, at verses 3, 4, 5 (run length 3).
- **A-H2 (corpus-census):** total corpus rebuke-*kallā* = 33 (replicating al-Dānī via H-NEW-2230); none
  in Q 1–18 (homograph-clean).
- **A-H3 (direction-locked, gating):** Q 102's max consecutive-verse run (= 3) STRICTLY EXCEEDS every
  other surah's (≤ 2).

**Result (from `csv/Q102-F-01.json`):**

| Cell | Outcome |
|:--|:--|
| **A-H1** Q 102 *kallā* verses = [3, 4, 5], run = 3 | **PASS** |
| **A-H2** total rebuke-*kallā* = **33**; first-half (Q 1–18) rebuke-*kallā* surahs = **[]** (none) | **PASS** |
| **A-H3** Q 102 max-run = **3**; max over all other surahs = **2**; Q 102 sole maximum | **PASS** |

The full per-surah rebuke-*kallā* verse map (15 surahs carry the rebuke particle): Q 19 [79,82],
Q 23 [100], Q 26 [15,62], Q 34 [27], Q 70 [15,39], Q 74 [16,32,53,54], Q 75 [11,20,26], Q 78 [4,5],
Q 80 [11,23], Q 82 [9], Q 83 [7,14,15,18], Q 89 [17,21], Q 96 [6,15,19], **Q 102 [3,4,5]**, Q 104 [4].
Per-surah max consecutive run: Q 74 = 2 (vv 53-54), Q 78 = 2 (vv 4-5), Q 83 = 2 (vv 14-15),
**Q 102 = 3 (vv 3-4-5)** — every other surah ≤ 2.

**Verdict: CONFIRMED (deterministic corpus-singleton).** Q 102 is the SOLE surah in the corpus with a run
of three consecutive rebuke-*kallā* verses. The census (33) and homograph-cleanliness replicate
al-Dānī / al-Suyūṭī *Itqān* nawʿ 40 at QAC-lemma strictness (H-NEW-2230 claim 7). This anchors the
classical *kallā* census to a per-surah deterministic extreme. **It also corrects the task-brief working
figure of "×2 *kallā*": the morphological ground-truth is 3 (POS:AVR), not 2.**

---

## Q102-F-01 Arm B — the single-particle near-verbatim adjacent refrain (DIRECTIONAL — pre-commit violation on B-H1)

**Hypothesis (pre-committed):**
- **B-H1 (corpus-exclusivity):** the ordered adjacent verse-pair (v_n = *kallā sawfa taʿlamūn*,
  v_{n+1} = *thumma kallā sawfa taʿlamūn*) — identical except a single prefixed connective particle — is
  corpus-EXCLUSIVE to Q 102:3-4. **Direction lock: count of such single-particle adjacent refrain pairs
  in the corpus = 1.**
- **B-H2 (bare-threat singleton):** the whole rebuke-verse whose entire post-particle content is the bare
  threat *sawfa taʿlamūn* (i.e. verse text ∈ {*kallā sawfa taʿlamūn*, *thumma kallā sawfa taʿlamūn*})
  occurs corpus-wide only at Q 102:3 and Q 102:4. **Direction lock: count = 2, both in Q 102.**
- **B-H3 (supporting context, non-gating):** length-stratified random re-pairing null (seed 20260509,
  10000 perms) on single-particle adjacent near-twins.

**Result (from `csv/Q102-F-01.json`):**

| Sub-hypothesis | Outcome |
|:--|:--|
| **B-H1** single-particle adjacent refrain pair corpus-exclusive to Q 102 | **FAIL (pre-commit violation)** |
| **B-H2** bare-threat whole-verse corpus-exclusive to Q 102 | **PASS** |
| **B-H3** observed near-twin count vs random re-pairing null | supporting context (rare) |

- **B-H1 FAIL (count = 3, not 1).** The single-particle adjacent near-twin pairs in the corpus are
  **three**, all *thumma*-led: **(Q 75:34-35, *thumma*), (Q 78:4-5, *thumma*), (Q 102:3-4, *thumma*)**.
  Q 102:3-4 IS present (`B_H1_q102_3_4_present = true`), but it is NOT a singleton — the locked direction
  (count = 1) is violated. **Published as the pre-commit violation, with full prominence.**
  - Q 75:34-35: *awlā laka fa-awlā* → *thumma awlā laka fa-awlā*.
  - Q 78:4-5: *kallā sa-yaʿlamūn* → *thumma kallā sa-yaʿlamūn*.
  - Q 102:3-4: *kallā sawfa taʿlamūn* → *thumma kallā sawfa taʿlamūn*.

- **B-H2 PASS (count = 2, both Q 102).** The bare-threat whole-verse (the entire post-*kallā* content being
  just *sawfa taʿlamūn*) occurs at exactly **Q 102:3 and Q 102:4** (`bare_threat_locs = [[102,3],[102,4]]`).
  The bare-threat reduplicated form is a Q 102 singleton — the 9 other *sawfa/sa-taʿlamūn*-bearing verses
  embed the threat in longer clauses; only Q 102 leaves it bare and doubled.

- **B-H3 (supporting context, non-gating per pre-reg §B-H3).** observed single-particle adjacent near-twin
  count = **3**; null_mean = **0.183**; p_perm = **0.0002** (≈ (1/10001)·(1+1)). Under random
  within-surah re-pairing, such adjacent single-particle near-twins essentially never co-occur 3 times —
  the corpus's adjacent refrains are deliberate, not chance collisions. (This is descriptive context; it
  does not consume α and does not change the deterministic B verdict.)

**Verdict: DIRECTIONAL.** Exactly one of the two gating deterministic cells passed: B-H2 (bare-threat
Q 102 singleton ✓), B-H1 (*thumma*-refrain Q 102 exclusivity ✗ — it is a **3-member family**). Per the
pre-reg verdict map (B partial = exactly one of B-H1/B-H2 holds → DIRECTIONAL), Arm B is **DIRECTIONAL**,
with the B-H1 pre-commit violation published at full prominence.

**What the partial-NULL teaches (a first-class finding).** al-Ṭabarī's *takrīr li-l-taghlīẓ* device
(Arabs double a word to intensify a threat) is real and cross-corpus — but it is **not unique to Q 102**.
The *thumma*-doubled adjacent threat-refrain is a small **corpus micro-family of three** {Q 75, Q 78,
Q 102}. Q 102 and Q 78 form a striking **2nd/3rd-person minimal pair**: Q 102 *kallā sawfa **taʿlamūn***
("you will know") vs Q 78 *kallā sa-**yaʿlamūn*** ("they will know"), both *thumma*-doubled. Q 102's
genuine singleton is finer-grained than the pre-reg's first guess: it is the **bare-threat reduplication**
(B-H2), not the *thumma*-doubling per se. This is exactly the kind of correction that pre-registration
discipline is designed to surface — the locked direction on B-H1 was wrong, and the honest report
upgrades the finding from "Q 102 has a unique refrain" to "Q 102 belongs to a 3-member *thumma*-threat
family AND uniquely strips the threat bare."

---

## Bonferroni / family summary

Per the pre-reg, Q102-F-01 has **k = 0 gating permutation cells** (both arms are deterministic corpus
censuses; B-H3 is supporting context only and does not consume α). No permutation-α is consumed. For the
Q 102 surah session this is the single landed test, so no cross-test correction is needed.

| Arm / cell | Type | Result | Verdict |
|:--|:--|:--|:--|
| A-H1 ∧ A-H2 ∧ A-H3 | deterministic | Q 102 sole 3-consecutive-*kallā* run; census 33; homograph-clean | **CONFIRMED** |
| B-H1 | deterministic (direction-locked) | count = 3 (3-member *thumma* family), not 1 | **FAIL (pre-commit violation)** |
| B-H2 | deterministic (direction-locked) | bare-threat count = 2, both Q 102 | **PASS** |
| B-H3 | supporting context (non-gating) | obs 3 vs null_mean 0.183, p_perm ≈ 0.0002 | context only |
| **B overall** | — | 1 of 2 gating cells | **DIRECTIONAL** |

## MW protections applied

- **MW-1 (instrument-prior):** the run-length over POS:AVR *kallā*, the single-particle near-twin rule
  (closed particle set {ثم, و, ف, بل, او}), and the bare-threat string set were all fixed in the pre-reg.
- **MW-2 (corpus-prior):** B-H3 used 10,000 length-stratified within-surah re-pairing permutations.
- **MW-3 (alternative-models):** Arm A reports the FULL per-surah run-length distribution (not just
  Q 102); Arm B reports both the strict *thumma*-refrain count and the bare-threat count.
- **MW-5 (replication):** A-H1/A-H2/A-H3, B-H1, B-H2 are deterministic and fully replicable from the
  no-tashkeel JSON + QAC morphology; B-H3 seed-locked at 20260509. Re-run 2026-05-30 reproduced the JSON
  exactly (SHA OK; A CONFIRMED; B DIRECTIONAL; B-H1 count 3; bare-threat [[102,3],[102,4]]).
- **MW-6 (instrument-control):** Arm A's 113 non-Q102 surahs are the non-target control; B-H3's
  re-pairing is the non-target control.
- **MW-7 (post-hoc cap):** both observations were noticed during close reading of Q 102 and promoted to
  direction-locked pre-registered tests BEFORE computation; the single-test cap is respected.

## Cross-finding integration

- **H-NEW-2160 / H-NEW-2230 (§10.80)** — Arm A replicates the rebuke-*kallā* census (33, homograph-clean,
  none in Q 1–18) at QAC-lemma strictness, and pins Q 102's 3 tokens to a per-surah deterministic extreme
  (the corpus-unique 3-consecutive run).
- **H-NEW-2310 (refrain / exact-repeated-verse structure)** — Arm B contributes a new supporting instance
  to the refrain/reduplication axis and surfaces a **3-member *thumma*-doubled adjacent threat-refrain
  micro-family** {Q 75:34-35, Q 78:4-5, Q 102:3-4}; candidate for promotion as a corpus-wide sub-finding.
- **Q 78 al-Nabaʾ (Q078-F-03)** — Q 102:3-4 is the 2nd-person minimal-pair twin of Q 78:4-5 (3rd-person);
  both *thumma*-doubled.
- **H-NEW-1820** — orthogonal but co-located: Q 102 is rank-2 in its own title-root *kvr*
  (`05-classical-claims-audit.md` Claim 5).

## Honest limits

- Arm A's "run" is over the QAC POS:AVR *kallā* token set; a raw-substring count (38) would over-count by
  conflating *kullan/kilā* homographs and could spuriously inflate run lengths — the rules-tuple (POS:AVR
  LEM `kal~aA`) is load-bearing and specified.
- Arm B's single-particle near-twin rule uses a closed leading-particle set {ثم, و, ف, بل, او} and exact
  mark-stripped string identity; a looser edit-distance definition would admit near-misses and change the
  count of 3. The *thumma*-only result (all 3 family members use *thumma*) is itself a clean sub-finding
  but is rule-definition-dependent.
- B-H3 is supporting context (non-gating); the p_perm ≈ 0.0002 is reported for completeness and does not
  upgrade the deterministic B verdict.

---

*Computed 2026-05-30, seed 20260509, 10,000 perms (B-H3 context), SHA-locked pre-reg verified at runtime.
Script: `scripts/Q102_F_01_kalla_reduplication.py`; JSON: `csv/Q102-F-01.json`.*
