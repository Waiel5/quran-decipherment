---
surah: 103
surah_name_ar: العصر
surah_name_translit: al-ʿAṣr
file_type: novel-findings
date_last_updated: 2026-05-30
phase: B+
verdict: Q103-F-01 — Arm A CONFIRMED (minimal-surah rā'-twin) + Arm B DIRECTIONAL (ṣād-iconicity, p_perm=0.07019, does NOT clear α=0.05) + Arm C CONFIRMED (minimal tripartite qasam skeleton)
seed: 20260509
n_perm: 10000
---

# Q 103 al-ʿAṣr — Pre-Registered Novel Findings


> **⛔ CORRECTION NOTICE — 2026-08-07.** This file locates this surah within the
> **compression-tail** and/or **iʿjāz anti-twin** framework. Both met a matched Arabic control
> on 2026-08-07 and **neither discriminates**. The anti-twin is **REVERSED** — this corpus sits
> at the **3rd percentile** of al-Jāḥiẓ and the 14th of al-Bukhārī, and pre-Islamic poetry under
> a matched partition reaches r = −0.872 against this corpus's −0.870. The compression-tail is
> **genre-shared and 91.5 % explained by unit size**: log(unit size) alone gives R² = 0.9147,
> and re-cutting this corpus's own verses to equal size collapses R² from 0.9887 to **0.3388**.
> UAS is a synthesis index with no null hypothesis.
>
> Positional statements below — "in the compression-tail", "iʿjāz-fawāṣil cell", a UAS rank —
> remain accurate as **descriptions of where this surah sits on those axes**. What is withdrawn
> is that the axes distinguish this corpus from ordinary Arabic. Nothing below is deleted.
>
> Evidence: `findings/phase-b-hypotheses/h-new-2720-genre-control-sweep.md`
> Summary: `findings/GENRE-CONTROL-CORRECTION-2026-08-07.md`.

One pre-registered three-arm test, finalized with seed 20260509 and 10,000 permutations (Arm B only),
pre-reg SHA-256 locked before computation and verified at runtime (fail-fast). Equal NULL/DIRECTIONAL
prominence per PRE-REG-STANDARD-04.

- **Pre-reg:** `surahs/Q103-al-asr/Q103-F-01-asr-minimal-prereg.md`
- **Pre-reg SHA-256:** `b6445946260ce8db4cbb424c8638ad5d5be030adbac6e47af6f9be130364037c` (verified at runtime; re-confirmed `shasum -a 256` on 2026-05-30)
- **Script:** `scripts/Q103_F_01_asr_minimal.py` (embeds the SHA as `EXPECTED_SHA`, fail-fast on mismatch)
- **JSON:** `surahs/Q103-al-asr/csv/Q103-F-01.json`
- **Rules-tuple:** `(no-tashkeel, orthographic-token, graphemes/letters, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)`

**Small-N design note.** Q 103 has only 3 verses, so NO within-surah verse-permutation can resolve (3! = 6
arrangements). As the protocol's small-N guidance requires, every arm here is either a **deterministic
corpus-rarity / exact-structural fact** (Arms A, C, B-H1) or a **corpus-level** (not within-surah)
length-matched permutation (Arm B-H2). No underpowered within-surah permutation was attempted.

---

## Q103-F-01 Arm A — minimal-surah rā'-monorhyme structural twin (CONFIRMED, deterministic)

**Hypothesis (pre-committed):** Within the corpus's 3-verse surahs, Q 103 belongs to a matched perfect-rā'-
monorhyme pair, and its closest such partner is also its Fisher-Rao nearest neighbour.

**Result (`csv/Q103-F-01.json`, arm_A):**

| Cell | Pre-committed | Observed | Pass |
|:--|:--|:--|:--|
| 3-verse surahs | {103, 108, 110} | **[103, 108, 110]** | — |
| A-H1: rā'-monorhyme 3-verse set = exactly {103, 108} | {103,108} | **[103, 108]** (Q 110 finals are ح/ا/ا — not rā') | ✓ |
| A-H2: Q 103's rank-1 FR neighbour = Q 108 | Q 108 | **Q 108**, FR **0.2399** | ✓ |

**Verdict: CONFIRMED (deterministic corpus-rarity).** Of the corpus's exactly three 3-verse surahs, exactly
two — Q 103 al-ʿAṣr and Q 108 al-Kawthar — are perfect rā'-monorhymes (every verse-final letter = ر), and
Q 108 is Q 103's single closest surah in Fisher-Rao root-distribution space (0.2399 of 113). The minimal-surah
twin is the **rā'-rhyming pair {103, 108}**, not the whole 3-verse cohort (Q 110 al-Naṣr, also 3 verses, is
only Q 103's rank-12 FR neighbour and is NOT a rā'-monorhyme). **Honest asymmetry:** the rank-1 tie is
one-directional — Q 103 is only rank-6 in Q 108's own FR list (Q 108's nearest neighbour is Q 106 al-Quraysh
at 0.2127). So the claim is "Q 108 is Q 103's nearest neighbour," not "they are mutual nearest neighbours."

## Q103-F-01 Arm B — emphatic (istiʿlāʾ) iconicity concentration (DIRECTIONAL — does NOT clear α=0.05)

**Hypothesis (pre-committed):** Q 103's #2-in-corpus istiʿlāʾ density is ṣād-concentrated in its lexical spine,
and is higher than a length-matched corpus-window null. **Direction lock: obs > null.**

**Result (`csv/Q103-F-01.json`, arm_B):**

| Cell | Value |
|:--|:--|
| Q 103 total letters | 73 |
| Heavy (istiʿlāʾ) letter count | 7 |
| **Observed istiʿlāʾ density** | **0.0959** (= 7/73; exact match to H-NEW-2340 = #2/114, behind Q 113's 0.1212) |
| Heavy-letter breakdown | **ص ×5**, خ ×1, ق ×1 |
| ṣād dominant (≥ half) | YES (5 of 7) → **B-H1 PASS** |
| Null (10,000 length-73 corpus windows, seed 20260509) | mean **0.05005**, std **0.02510** |
| **z** | **+1.827** (direction obs > null — locked direction holds) |
| **p_perm** | **0.07019** ( = (701+1)/(10000+1) ) |
| α_corrected (k=1) | 0.05 |

**Verdict: DIRECTIONAL.** B-H1 passes deterministically: Q 103 is the corpus's 2nd-densest surah in emphatic
letters, and the load is **overwhelmingly ṣād** (5 of 7 heavy tokens) — carried by the lexical spine al-ʿa**Ṣ**r
(time), al-**Ṣ**āliḥāt (righteous deeds), al-**Ṣ**abr (patience). The permutation direction is in the locked
sense (obs 0.0959 > null-mean 0.0500, z = +1.83), so this is **NOT a pre-commit violation**. But it **does not
clear α = 0.05** (p_perm = 0.07019). Honest reading: Q 103 is emphatically heavy, ṣād-driven, and *suggestively*
above a content-blind length-matched corpus window — but not at significance. With 73 letters the window is
small and the null is wide (std 0.025), so a single-cell permutation is genuinely underpowered; the DIRECTIONAL
label is the correct, non-inflated verdict.

**What the non-significance teaches.** The corpus-level emphatic-iconicity hypothesis (heavy-letter density ↔
ʿadhāb/punishment vocabulary) was itself **NULL** in H-NEW-2340 (ρ = 0.0232, p = 0.40516; `csv/h-new-2340.json`,
primary), and Q 103's own `adhab_density` is **0.0**. So even at #2 corpus density, Q 103's emphasis is
**lexical-spine-driven, not punishment-theme-driven** — it is heavy because its three thematic anchor-words
happen to carry ṣād, not because the surah is "about" punishment. The DIRECTIONAL p = 0.070 is consistent with
that: a real but modest, content-incidental heaviness.

## Q103-F-01 Arm C — minimal tripartite qasam→jawāb→istithnāʾ skeleton (CONFIRMED)

**Hypothesis (pre-committed):** Q 103 realises the full oath→answer→exception arc across its three verses with
the minimal qasam→jawāb distance (1 verse), and its local self-cohesion is in the corpus top decile.

**Result (`csv/Q103-F-01.json`, arm_C):**

| Cell | Pre-committed | Observed | Pass |
|:--|:--|:--|:--|
| C-H1: wāw-qasam, temporal object, jawāb *inna* at v 2, distance = 1, v 3 *illā* (QAC EXP at 103:3:1:1) | all hold | kinds=["waaw"], obj=ʿaṣr "temporal", jawāb v 2 (*inna/anna*), **distance 1**, v3 EXP ✓ | ✓ |
| C-H2: local_cohesion rank ≤ 15 (top decile), direction HIGH | rank ≤ 15 | **rank 10/114** (local_cohesion 3.0697; rhyme_entropy 0.0) | ✓ |

**Verdict: CONFIRMED.** Q 103 is a textbook minimal qasam: a single wāw-oath on a temporal object (*wa-l-ʿaṣr*),
answered one verse later by *inna al-insāna la-fī khusr* (qasam→jawāb distance = **1**, the minimal value; 11 of
the corpus's 44 qasam-clusters share distance 1 per H-NEW-2210), then qualified by the exception particle *illā*
opening v 3 (QAC POS:EXP at 103:3:1:1). Its local self-cohesion is **rank 10/114** (top decile, descending) and
its rhyme entropy is the **corpus floor (0.0** — perfect rā'-monorhyme). The full oath→jawāb→istithnāʾ rhetorical
arc is realised in exactly three verses — the empirical correlate of al-Shāfiʿī's "if people pondered this surah
it would suffice them" and al-Rāzī's use of al-ʿAṣr as a taḥaddī test-case (`03-tafsir-survey.md`).

---

## Bonferroni / family summary

Q103-F-01 has **one permutation cell** (Arm B B-H2); α_corrected = 0.05/1 = 0.05. The deterministic cells
(A-H1, A-H2, B-H1, C-H1, C-H2) are exact corpus facts / within-corpus ranks and do not consume α.

| Arm / cell | Type | Result | Verdict |
|:--|:--|:--|:--|
| A (A-H1 ∧ A-H2) | deterministic | {103,108} rā'-pair; Q108 = rank-1 FR (0.2399) | **CONFIRMED** |
| B-H1 | deterministic | 0.0959 (#2/114), ṣād 5/7 dominant | PASS |
| B-H2 | permutation (α=0.05) | z=+1.827, **p_perm=0.07019**, direction obs>null | **DIRECTIONAL** (not significant) |
| **B overall** | — | B-H1 ✓, B-H2 directional-not-sig | **DIRECTIONAL** |
| C (C-H1 ∧ C-H2) | deterministic + rank | distance 1, local_cohesion rank 10/114 | **CONFIRMED** |

**Net Q103-F-01: Arm A CONFIRMED + Arm B DIRECTIONAL + Arm C CONFIRMED.**

## MW protections applied

- **MW-1 (instrument-prior):** rā'-monorhyme test, istiʿlāʾ set {خ ص ض ط ظ غ ق}, FR-rank, root-spine, and
  qasam-cluster definitions all fixed in the pre-reg before any run.
- **MW-2 (corpus-prior):** Arm B null = 10,000 length-73 random contiguous windows from the mark-stripped
  whole-corpus letter-stream (seed 20260509).
- **MW-3 (alternative-models):** B reports both the deterministic decomposition (B-H1) and the random-window
  null (B-H2); A and C report exact corpus facts + within-corpus rank.
- **MW-5 (replication):** Arms A, B-H1, C are deterministic and fully replicable from the no-tashkeel JSON +
  QAC + H-NEW artifacts; B-H2 seed-locked (re-ran 2026-05-30, p_perm reproduces at 0.07019).
- **MW-6 (instrument-control):** Arm B's length-73 random corpus windows are the content-blind control.
- **MW-7 (post-hoc cap):** all three observations were noticed during close reading then promoted to
  direction-locked PRE-REGISTERED tests before computation; the single permutation cell respects the α=0.05 cap.

## Cross-finding integration

- **H-NEW-2340** (emphatic-iconicity) — Q 103 is the data-point at rank #2; Arm B's DIRECTIONAL result is fully
  consistent with the corpus-level NULL of the heavy↔ʿadhāb hypothesis (Q 103's adhab_density = 0).
- **H-NEW-2210** (qasam→jawāb inventory) — Arm C lands Q 103 as a distance-1 minimal wāw-qasam (1 of 11 such).
- **H-NEW-111 / H-NEW-750** — Arm A (FR rank-1 = Q 108) and Arm C (rhyme entropy 0.0, local_cohesion rank 10)
  are read directly from these artifacts.
- **Minimal-surah twin candidate (corpus-wide):** the {Q 103, Q 108} rā'-monorhyme + FR-rank-1 pairing is a
  candidate for promotion to a corpus-wide "minimal-surah twin" H-NEW finding (cf. the Q 066-F-01 verbatim-twin
  roster precedent); queued as Q103-F-03.

## Honest limits

- Arm B's DIRECTIONAL (not CONFIRMED) status is the headline honesty point: at p_perm = 0.070, Q 103's emphatic
  heaviness is suggestive but unproven against a content-blind null. It must NOT be reported as a confirmed
  iconicity effect. The 73-letter window + the corpus-level NULL of the underlying hypothesis both caution against
  over-reading it.
- Arm A's "rank-1 FR neighbour" is direction-asymmetric (Q 103→Q 108 rank 1; Q 108→Q 103 rank 6); the claim is
  one-directional and is stated as such.
- The 4-dim phoneme channel labels (`h-new-700.json`) are not schema-annotated; the istiʿlāʾ-channel identification
  rests on numerical equality (0.0959) with H-NEW-2340, not a documented label (noted in `01-empirical-profile.md`).
- FR distances are over QAC-STEM root distributions; with only 9 distinct roots Q 103's FR vector is sparse, so
  neighbour ranks are sensitive to top-K coverage (0.9 for Q 103 per `h-new-111.json`).

---

*Computed/finalized 2026-05-30, seed 20260509, 10,000 perms, SHA-locked pre-reg verified at runtime.
Script: `scripts/Q103_F_01_asr_minimal.py`; JSON: `csv/Q103-F-01.json`.*
