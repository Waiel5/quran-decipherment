---
surah: 54
test_id: Q054-F-01
title: Dual-refrain 5-section architecture — Q 54's *yassarnā/muddakir* + *kayfa kāna ʿadhābī wa-nudhur* refrain monopoly + section-rhythm test
file_type: pre-registration
date_locked: 2026-05-09
seed: 20260509
bonferroni_k: 3
bonferroni_family: Q054-F-01-dual-refrain-architecture
alpha_bon: 0.0167
---

# Q054-F-01 — Pre-registration: Q 54 dual-refrain 5-section architecture

## 1. Hypothesis (locked before observation)

**H1a (one-tailed, locked direction; corpus-monopoly cell):** The 6 verses of Q 54 ending with the literal Arabic string `فهل من مدكر` (*fahal min muddakir* — "is there any who will remember?") account for ALL corpus instances of that ending phrase. Operationally: of all 6,236 verses corpus-wide, the count of verses whose normalised-no-tashkeel-text ends in `فهل من مدكر` is exactly 6, and all 6 are in Q 54 (vv 15, 17, 22, 32, 40, 51). **Locked share threshold: ≥ 95% of corpus instances are in Q 54.**

**H1b (one-tailed, locked direction; closure-rhythm cell):** The 4 *fahal min muddakir + ʿadhābī wa-nudhur* refrain pairs in Q 54 (post-Nūḥ vv 15-17 / post-ʿĀd vv 18-22 / post-Thamūd vv 30-32 / post-Lūṭ vv 39-40) close 4 of 5 prophet/nation pericopes in pre-committed sequence Nūḥ → ʿĀd → Thamūd → Lūṭ → Pharaoh. Locked: at least 4 of the 5 pre-committed pericope-closure positions match the refrain-occurrence verse-positions within ±1 verse (allowing the single yassarnā per pericope as the closure marker, OR the *fa-dhūqū ʿadhābī wa-nudhur* pair at vv 37+39 which substitutes for *kayfa kāna* in the Lūṭ pericope). **Locked threshold: ≥4/5 pericopes show structural closure by either refrain (yassarnā or ʿadhābī).**

**H1c (one-tailed, locked direction; compression cell):** Q 54's mean verses-per-pericope across the 5 pre-committed pericopes (Nūḥ vv 9-17, ʿĀd vv 18-22, Thamūd vv 23-32, Lūṭ vv 33-40, āl-Firʿawn vv 41-42) is strictly lower than Q 26 al-Shuʿarāʾ's mean verses-per-pericope across its 7 pre-committed pericopes (Mūsā vv 10-68, Ibrāhīm vv 69-104, Nūḥ vv 105-122, Hūd vv 123-140, Ṣāliḥ vv 141-159, Lūṭ vv 160-175, Shuʿayb vv 176-191). **Locked: Q54 mean < Q26 mean by ≥ 2× (i.e., compression ratio ≥ 2).**

**H0 (joint):** H1a fails OR H1b fails OR H1c fails.

**Direction:** Q 54 is a corpus-uniquely-saturated dual-refrain prophet-cycle surah with verses-per-pericope ≥ 2× compressed vs Q 26 (LOCKED).

## 2. Operational definition

- **Source text**: `quran-text/quran-no-tashkeel.json` (default rules-tuple).
- **Refrain A regex**: literal terminal substring `فهل من مدكر` (with leading whitespace boundary; the entire verse ENDS with this string after stripping any trailing whitespace).
- **Refrain B regex**: literal substring `فكيف كان عذابي ونذر` for the *kayfa kāna* form, OR `فذوقوا عذابي ونذر` for the *fa-dhūqū* substitute (Q 54:37 + Q 54:39 jointly close Lūṭ pericope).
- **Pericope boundaries** (pre-committed before observation, sourced from al-Ṭabarī + al-Rāzī classical commentary tradition; locked here):
  - Nūḥ: vv 9-17 (closure at v 17 yassarnā; v 15 is the "track-trace-sign" prelude)
  - ʿĀd: vv 18-22 (closure at v 22 yassarnā; v 21 is the *kayfa kāna*)
  - Thamūd: vv 23-32 (closure at v 32 yassarnā; v 30 is the *kayfa kāna*)
  - Lūṭ: vv 33-40 (closure at v 40 yassarnā; vv 37+39 are the *fa-dhūqū* substitute)
  - āl-Firʿawn: vv 41-42 (NO yassarnā; the surah pivots to the closing block at v 43)
- **Corpus-share** (H1a): N_total = corpus count of verses ending in `فهل من مدكر`; N_q54 = subset in Q 54; share_q54 = N_q54 / N_total.
- **Compression-ratio** (H1c): for each surah s ∈ {Q 26, Q 54}, mean_verses_per_pericope = sum(pericope_v_count) / number_of_pericopes; ratio = mean_q26 / mean_q54.

## 3. Permutation null

**Null model A (length-weighted, for H1a):** Under the null, the N_total terminal-string-match tokens are distributed across surahs proportional to verse-count (longer surahs ⇒ more chance to contain the rare terminal phrase). p-value = probability that a random length-weighted draw of N_total tokens places ≥ N_q54 in Q 54.

**Null model B (uniform-surah, for H1a):** N_total tokens distributed uniformly over 114 surahs.

**Null model C (rotation null for H1b):** Generate 10,000 rotations of the verse-position-vector of refrain occurrences within Q 54; for each rotation, compute number of pre-committed pericope-closure positions that hit. p-value = probability that ≥ 4/5 hit positions occur under random rotation.

n_perm = 10000, seed = 20260509.

## 4. Test statistic

- For H1a: share_q54.
- For H1b: count of pericopes structurally-closed by refrain (yassarnā OR ʿadhābī).
- For H1c: ratio = mean_verses_per_pericope_Q26 / mean_verses_per_pericope_Q54.

## 5. Success / Failure

- **CONFIRMED (joint)**: H1a + H1b + H1c all pass at α_bon = 0.0167.
- **PARTIAL**: 2 of 3 pass.
- **NULL**: ≤ 1 of 3 pass.
- **PRE-COMMIT VIOLATION**: any of the locked threshold quantities is < the locked direction (e.g., compression ratio < 1, share < 0.50).

## 6. Honest limits known a priori

- **Post-hoc origin disclosed**: the refrain-saturation finding is sourced from H-NEW-1230 + H-NEW-1320 (already-published landings). The 6-verse `فهل من مدكر` corpus monopoly was empirically observed during this specialist's pre-flight anchor extraction (see JOURNAL.md run-log step "extracting muddakir occurrences"). Per HANDOFF/04-DISCIPLINE.md "post-hoc-noticed protocol":
  - Single-test α=0.05 cap unless extreme p (e.g., < 1e-5) survives any conceivable Bonferroni.
  - Verdict ceiling = **PASS-DIRECTED** (NOT CONFIRMED) until INDEPENDENT REPLICATION on a distinct data dimension.
  - Independent-replication candidates: re-run on alternative orthographic conventions (Uthmani-consonantal, Mashriqi vs Maghribī); test the closure-rhythm via different operationalization (sentence-boundary detection vs literal-string matching).
- **Pericope-boundary specification is classical-tradition-anchored** (al-Ṭabarī + al-Rāzī + al-Biqāʿī all treat vv 9-17 / 18-22 / 23-32 / 33-40 / 41-42 as pericopes). Alternative boundary-specifications (e.g., the al-Suyūṭī *al-Itqān* nawʿ 16 *al-faṣl wa-l-waṣl* method) would produce slightly different pericope-counts but should not invert the compression ratio.
- **Q 54 has 5 pericopes, Q 26 has 7**; the pre-committed pericope counts are themselves classical/empirical. The compression-ratio is robust against minor pericope-boundary perturbations (within ±2 verses on either side).
- **The refrain analysis treats both *yassarnā* + *ʿadhābī* refrains as functioning together as a closure-marker pair** (yassarnā follows ʿadhābī in 3 of 4 cases: vv 16+17 ʿadhābī then yassarnā / vv 21+22 ʿadhābī then yassarnā / vv 30+32 ʿadhābī then yassarnā / vv 37+39+40 ʿadhābī twice then yassarnā). This empirical interleaving is the architectural feature being tested.

## 7. Rules-tuple

`(no-tashkeel, orthographic-token, regex-terminal-substring, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)`.

## 8. Bonferroni

k = 3 (H1a corpus-share + H1b closure-rhythm + H1c compression-ratio). α_bon = 0.0167.

## 9. Coordination

This is a Q 54-specific dual-refrain test. No other surah specialist has run a *muddakir* or *yassarnā* or *kayfa kāna ʿadhābī wa-nudhur* test. Q 26 al-Shuʿarāʾ specialist has not yet been written. Q 55 al-Raḥmān specialist has been written (see `surahs/Q055-al-rahman/`); Q 55 specialist did NOT run a Q 54-comparison cell. No duplication.

## 10. SHA256 lock

Computed at write-time, embedded into `scripts/Q054_F_01_dual_refrain_architecture.py`, verified at runtime.
