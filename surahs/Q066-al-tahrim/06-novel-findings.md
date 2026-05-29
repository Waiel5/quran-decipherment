---
surah: 66
surah_name_ar: التحريم
surah_name_translit: al-Taḥrīm
file_type: novel-findings
date_last_updated: 2026-05-29
phase: B+
verdict: Q066-F-01 — Arm A CONFIRMED (verbatim verse-twin) + Arm B NULL (pre-commit violation, dual-exemplar seal)
seed: 20260509
n_perm: 10000
---

# Q 66 al-Taḥrīm — Pre-Registered Novel Findings

One pre-registered two-arm test, run with seed 20260509 and 10,000 permutations, pre-reg SHA-256 locked
before computation and verified at runtime.

- **Pre-reg:** `surahs/Q066-al-tahrim/Q066-F-01-tahrim-seal-prereg.md`
- **Pre-reg SHA-256:** `749a186efd3959ab1e0eddfa435f916f8104454bf347a43d9466c1a1705c4d44`
- **Script:** `scripts/Q066_F_01_tahrim_seal.py` (verifies SHA at runtime, fail-fast)
- **JSON:** `surahs/Q066-al-tahrim/csv/Q066-F-01.json`
- **Rules-tuple:** `(no-tashkeel, orthographic-token, QAC v0.4 roots, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)`

---

## Q066-F-01 Arm A — Q 66:9 verbatim full-verse twin (CONFIRMED)

**Hypothesis (pre-committed):** Q 66:9 is a member of the small corpus set of *verbatim full-verse twins* —
verses ≥10 word-tokens whose mark-stripped text appears identically at ≥2 distinct positions.

- **A-H1 (direction-locked):** Q 66:9 has exactly one verbatim partner, Q 9:73.
- **A-H2:** the corpus count of length-≥10-token verbatim-twin GROUPS is ≤ 20 (verbatim long-verse repetition is rare).

**Result:**
- Q 66:9 (mark-stripped): *يا أيها النبي جاهد الكفار والمنافقين واغلظ عليهم ومأواهم جهنم وبئس المصير* (12 tokens).
- Verbatim partner: **exactly one — Q 9:73** (A-H1 PASS).
- Corpus length-≥10-token verbatim-twin groups: **11** (A-H2 PASS, ≤20). The full roster:

  | Group | Positions | Words |
  |:--|:--|:--|
  | 1 | Q 2:47 ≡ Q 2:122 | 12 |
  | 2 | Q 2:134 ≡ Q 2:141 | 15 |
  | 3 | Q 3:89 ≡ Q 24:5 (partial-skeleton) | 11 |
  | 4 | Q 6:4 ≡ Q 36:46 | 11 |
  | 5 | Q 6:10 ≡ Q 21:41 | 13 |
  | 6 | Q 9:33 ≡ Q 61:9 | 14 |
  | 7 | **Q 9:73 ≡ Q 66:9** | **12** |
  | 8 | Q 11:110 ≡ Q 41:45 | 18 |
  | 9 | Q 23:6 ≡ Q 70:30 | 10 |
  | 10 | Q 26:109 ≡ 127 ≡ 145 ≡ 164 ≡ 180 (×5, the Shuʿarāʾ refrain) | 11 |
  | 11 | Q 59:1 ≡ Q 61:1 | 11 |

- Supporting context (Null A): of **5,586,153** distinct ≥10-token verse-pairs, only **20** are verbatim-identical
  (collision rate **3.58 × 10⁻⁶**). Random surface-collision of two ≥10-token Arabic verses is astronomically
  unlikely (a 10-word exact match has probability ≪ 10⁻²⁰ under any unigram model), so these 20 verbatim pairs
  are **deliberate repetitions**, not chance collisions — A-H3's direction (verbatim rate ≫ chance) holds trivially.

**Verdict: CONFIRMED (deterministic corpus-rarity).** Q 66:9 ≡ Q 9:73 is one of only 11 verbatim long-verse
twin groups in the corpus. The two verses carry the identical jihād-against-kuffār-and-munāfiqīn directive
verbatim. This is the project's first per-surah landing of the verbatim-long-verse-twin roster and it
cross-anchors **H-NEW-1520** (where Q 9:73-75 × Q 66:9-11 was the #2 prophet-vocative pericope pair, J=0.245,
explicitly flagged there as "textual near-twins" — now confirmed as a full-verse EXACT twin).

**Chronological note:** Q 66 (revelation-order #107) precedes Q 9 (revelation-order #113) in the Tanzil
Egyptian-standard chronology, so the verbatim directive was first revealed in al-Taḥrīm and re-deployed in
al-Tawba — not the reverse. (`data/revelation-order.csv`.)

---

## Q066-F-01 Arm B — antithetical dual-exemplar seal (NULL — pre-commit violation)

**Hypothesis (pre-committed):**
- **B-H1 (corpus-exclusivity):** the adjacent antithetical exemplar-frame — a verse opening *ḍaraba Allāh
  mathalan li-lladhīna kafarū* immediately followed by *wa-ḍaraba Allāh mathalan li-lladhīna āmanū* — is
  corpus-EXCLUSIVE to Q 66:10-11.
- **B-H2 (direction-locked):** the two believer-exemplar verses (v 11 Āsiya, v 12 Maryam) share a higher
  root-Jaccard with each other than either shares with the disbeliever-exemplar verse (v 10):
  J(11,12) > J(10,11) AND J(11,12) > J(10,12).
- **B-H3 (direction-locked):** J(v11,v12) exceeds a length-matched random-verse-pair permutation null
  (seed 20260509, 10,000 perms, ±3 root tolerance).

**Result:**

| Sub-hypothesis | Outcome |
|:--|:--|
| **B-H1** corpus-exclusive kafarū→āmanū adjacent frame | **PASS** — exactly 1 corpus occurrence, = Q 66:10-11 |
| **B-H2** believer-pair tighter than frame-pair | **FAIL (direction reversed)** |
| **B-H3** seal cohesion > permutation null | **FAIL** |

- **B-H1 PASS.** The *ḍaraba Allāh mathalan* frame occurs in only 7 corpus verses (Q 14:24, 16:75, 16:76,
  16:112, 39:29, 66:10, 66:11). The kafarū-frame appears at exactly Q 66:10; the āmanū-frame at exactly Q 66:11.
  The adjacent (next-verse) kafarū→āmanū antithetical pair is **corpus-EXCLUSIVE to Q 66:10-11** — a structural
  singleton. al-Qurṭubī's attention to the antithetical parable-frame is vindicated.

- **B-H2 FAIL (pre-commit violation).** Root-Jaccards:
  - J(v11, v12) = **0.0833** (Āsiya ↔ Maryam, the believer-pair)
  - J(v10, v11) = **0.2000** (disbeliever-wives ↔ Āsiya)
  - J(v10, v12) = 0.0400 (disbeliever-wives ↔ Maryam)

  The pre-committed direction J(11,12) > J(10,11) is **reversed**: the disbeliever-exemplar v 10 is *2.4× closer*
  to Āsiya (v 11) than Āsiya is to Maryam (v 12). **Mechanism (documented in the pre-reg as the anticipated risk):**
  v 10 and v 11 share the parable-frame roots — the shared tokens are {Allāh, ḍ-r-b (ḍaraba), m-r-ʾ (imraʾat
  "wife"), m-th-l (mathalan), q-w-l (qālat/qīla)} — five shared roots. v 11 and v 12 share only {b-n-y (ibnat/
  ibni "build/daughter"), r-b-b (rabb)} — two shared roots. Maryam's verse (v 12) lacks the *ḍaraba…mathalan*
  frame (it is conjoined to v 11 by *wa-*) and carries distinct vocabulary (*aḥṣanat farjahā*, *nafakhnā…rūḥinā*,
  *ṣaddaqat bi-kalimāt rabbihā*). The **frame binds harder than the theme**.

- **B-H3 FAIL.** J(v11,v12)=0.0833 vs null_mean=0.0502, null_std=0.0464, **z = +0.715**, **p_perm = 0.2543**
  (2,542 of 10,000 length-matched random pairs ≥ observed; pool_a=796, pool_b=1896). The believer-pair cohesion
  is statistically indistinguishable from random length-matched verse pairs — it does NOT clear α=0.05.

**Verdict: NULL (pre-commit violation), published with full prominence per PRE-REG-STANDARD-04.** B-H2's
locked direction reversed and B-H3 failed; only B-H1 (the corpus-exclusivity of the frame) passed (1/3).

**What the NULL teaches (this is a first-class finding).** The dual-exemplar seal's cohesion is **architectural
(frame-driven)**, not **thematic (believer-women-driven)**. The surah's closing parable is held together by
the repeated *ḍaraba Allāh mathalan li-lladhīna … imraʾat …* template that spans the belief/disbelief boundary —
NOT by a lexical bond between the two believing women. Āsiya and Maryam are paired *rhetorically* (both
positive female exemplars) but are lexically *divergent*: Āsiya's verse is built on the parable-frame + a
deliverance-prayer, Maryam's on chastity + the breathing-of-the-Spirit. This refines al-Qurṭubī's ring-reading
(Yaḥyā b. Sallām): the *frame* does the admonitory work, the believer-women are not a lexically-unified block.
It is also a clean instance of the **scale-of-aggregation** lesson (cross-finding-025): a structure that is
rhetorically cohesive at the *theme* level can be lexically NON-cohesive at the *root-Jaccard* level.

---

## Bonferroni / family summary

Q066-F-01 has one permutation cell (B-H3); α_corrected = 0.05/1 = 0.05 (per the pre-reg; the deterministic
cells A-H1, A-H2, B-H1, B-H2 do not consume α). For the Q 66 surah session this is the single landed test,
so no further cross-test correction is needed.

| Arm / cell | Type | Result | Verdict |
|:--|:--|:--|:--|
| A (A-H1 ∧ A-H2) | deterministic | Q 66:9 ≡ Q 9:73; 11 twin-groups | **CONFIRMED** |
| B-H1 | deterministic | corpus-exclusive frame at Q 66:10-11 | PASS |
| B-H2 | direction-locked | J(11,12) < J(10,11) — REVERSED | FAIL |
| B-H3 | permutation (α=0.05) | z=+0.72, p=0.254 | FAIL |
| **B overall** | — | 1/3 + direction reversal | **NULL (pre-commit violation)** |

## MW protections applied

- **MW-1 (instrument-prior):** verbatim-match, *ḍaraba…mathalan* regex, and QAC root-Jaccard all fixed in the pre-reg.
- **MW-2 (corpus-prior):** B-H3 used 10,000 length-matched permutations.
- **MW-3 (alternative-models):** Arm A reports both the deterministic count and the surface-collision baseline;
  B-H2 reports the frame-root bias explicitly as the failure mechanism.
- **MW-5 (replication):** Arm A, B-H1, B-H2 are deterministic and fully replicable from the no-tashkeel JSON +
  QAC root-index; B-H3 seed-locked at 20260509.
- **MW-6 (instrument-control):** B-H3's length-matched random pool is the non-target control.
- **MW-7 (post-hoc cap):** both observations were noticed during close reading then promoted to direction-locked
  pre-registered tests BEFORE computation; the single-test α=0.05 cap is respected.

## Cross-finding integration

- **H-NEW-1520** — Arm A confirms the "textual near-twins" note (Q 9:73-75 × Q 66:9-11) as a full-verse EXACT twin.
- **cross-finding-025 (scale-of-aggregation)** — Arm B is a new supporting instance: rhetorical-theme cohesion
  (Āsiya + Maryam as believer-women) does NOT imply root-level lexical cohesion; the structure is frame-driven.
- **H-NEW-1360** — the prophet-vocative family whole-surah NULL is consistent with Q 66's FR neighborhood (the
  family co-members are mid-to-far in Q 66's FR list; see `01-empirical-profile.md`).
- **Verbatim-twin roster** — Q066-F-01 Arm A contributes the corpus roster of 11 long-verse verbatim twins;
  candidate for promotion to a corpus-wide H-NEW finding (the verbatim-long-verse-twin network).

## Honest limits

- Arm A's "rarity" is on the ≥10-token threshold; lowering it admits more (shorter) twins (e.g., the basmala,
  short refrains), so the rarity claim is threshold-specific.
- Arm B's failure mechanism (frame-root sharing) is itself an interesting structural fact; a follow-up
  (Q066-F-04, queued) should re-test the seal at the *parable-pair* grouping (v10-v11 vs v11-v12) to formalize
  the frame-vs-theme tension, and at a lemma/surface level to check instrument-robustness.
- B-H3's permutation null pools verses ±3 roots; a tighter or wider tolerance would shift null_mean slightly
  but cannot rescue a z of +0.72.

---

*Computed 2026-05-29, seed 20260509, 10,000 perms, SHA-locked pre-reg verified at runtime.
Script: `scripts/Q066_F_01_tahrim_seal.py`; JSON: `csv/Q066-F-01.json`.*
