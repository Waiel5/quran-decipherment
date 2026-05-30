---
surah: 103
surah_name_ar: العصر
surah_name_translit: al-ʿAṣr
file_type: prereg
test_id: Q103-F-01
date_locked: 2026-05-30
phase: B+
seed: 20260509
n_perm: 10000
status: LOCKED-BEFORE-COMPUTATION
---

# Q103-F-01 — Pre-Registration: al-ʿAṣr as a minimal qasam-architecture + emphatic-iconicity locus

**LOCKED BEFORE COMPUTATION.** This file is SHA-256 hashed; the hash is embedded in
`scripts/Q103_F_01_asr_minimal.py` and verified at runtime (fail-fast on mismatch).

## Motivation

Q 103 al-ʿAṣr is one of the three 3-verse surahs in the corpus (with Q 108 al-Kawthar and
Q 110 al-Naṣr). At only 14 words / 73 letters it is one of the shortest surahs, yet it has a
complete tripartite rhetorical skeleton: **oath (qasam)** `wa-l-ʿaṣr` → **answer-of-the-oath
(jawāb al-qasam)** `inna al-insāna la-fī khusr` → **exception (istithnāʾ)** `illā alladhīna
āmanū wa-ʿamilū al-ṣāliḥāti wa-tawāṣaw bi-l-ḥaqqi wa-tawāṣaw bi-l-ṣabr`. al-Shāfiʿī's famous
verdict (transmitted by Ibn Kathīr, *Tafsīr al-Qurʾān al-ʿaẓīm*, on Q 103: «لو تدبر الناس هذه
السورة لوسعتهم» — "if people pondered this surah it would suffice them") is precisely a claim
about maximal content compressed into minimal form.

Three on-disk empirical anchors converge on Q 103 and were noticed during close reading; this
pre-reg promotes them to direction-locked, falsifiable tests BEFORE any computation:

1. **H-NEW-2340** (`csv/h-new-2340.json`) ranks Q 103 **#2 in heavy-istiʿlāʾ (emphatic) letter
   density at 0.0959** — behind only Q 113 al-Falaq (0.1212). The istiʿlāʾ letters are
   {خ ص ض ط ظ غ ق} (Buckwalter x S D T Z g q).
2. **H-NEW-750** (`csv/h-new-750.json`) records Q 103 with `rhyme_entropy_nats = 0.0`
   (a **perfect monorhyme**, `top_final_letter = ر`, frac = 1.0) and `local_cohesion = 3.070`
   (`z_local_cohesion = +2.112`, very high).
3. **H-NEW-2210** (`csv/h-new-2210.json`) catalogs Q 103 as a wāw-qasam on a *temporal* sworn
   object (ʿaṣr), with the jawāb (inna/anna marker) at v 2 — `qasam_to_jawab_verse_distance = 1`.

## Rules-tuple

`(no-tashkeel, orthographic-token, graphemes/letters, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)`

Verse text from `/Users/grey/Downloads/quran/quran-text/quran-no-tashkeel.json` (surah index 102,
`id` 103). Letters = the 28-base Arabic-letter set + hamza/alif/tā'-marbūṭa variants
{ابتثجحخدذرزسشصضطظعغفقكلمنهوياءأإآؤئىة}; pause/sajda diacritic marks stripped. istiʿlāʾ set =
{خ ص ض ط ظ غ ق}. Roots from QAC v0.4
(`/Users/grey/Downloads/quran/data/morphology/quranic-corpus-morphology-0.4.txt`), surah-103 lines.
FR distances from `findings/phase-b-hypotheses/csv/h-new-111.json` (1-indexed). H-NEW values
re-read at runtime from their JSON artifacts and cross-checked against independent recomputation.

---

## Arm A — minimal-surah rā'-monorhyme structural twin (DETERMINISTIC, CONFIRMATORY)

**Hypothesis A (pre-committed):** Within the corpus's 3-verse surahs, Q 103 belongs to a matched
*perfect-rā'-monorhyme* pair, and its closest such partner is also its Fisher-Rao nearest neighbor.

- **A-H1 (direction-locked):** Of the exactly three 3-verse surahs {Q 103, Q 108, Q 110}, exactly
  two — **Q 103 and Q 108** — are perfect monorhymes whose every verse-final Arabic letter is **ر
  (rā')**; Q 110 is NOT (its finals are not a single rā' monorhyme).
- **A-H2 (direction-locked):** Q 108 al-Kawthar is Q 103's **rank-1 Fisher-Rao nearest neighbor**
  (smallest FR distance of all 113 other surahs), per `h-new-111.json`.

**A success criterion:** A-H1 ∧ A-H2 both hold → Arm A CONFIRMED (deterministic corpus fact).
**A failure criterion:** either A-H1 (the 3-verse rā'-monorhyme pair is not exactly {103,108}) or
A-H2 (Q 108 is not Q 103's rank-1 FR neighbor) fails → Arm A NULL.

## Arm B — emphatic-iconicity concentration (PERMUTATION, DIRECTION-LOCKED)

**Hypothesis B (pre-committed):** Q 103's #2-in-corpus istiʿlāʾ density is not a uniform sprinkle
but is **concentrated in its ṣād (ص)-bearing content roots** — the surah's lexical spine
(ʿ-ṣ-r "time", ṣ-l-ḥ "righteous deeds", ṣ-b-r "patience") carries the emphatic load.

- **B-H1 (deterministic):** Q 103's independently recomputed istiʿlāʾ density equals the H-NEW-2340
  value 0.0959 (= 7 heavy letters / 73 total), and **ṣād is the dominant emphatic** (≥ half of the
  heavy-letter tokens).
- **B-H2 (permutation, direction-locked):** The observed istiʿlāʾ density of Q 103 (0.0959) is
  **HIGHER** than the corpus-wide null distribution of istiʿlāʾ density computed over **length-73
  contiguous letter-windows drawn at uniformly random start positions from the full mark-stripped
  Quran letter-stream** (seed 20260509, 10,000 draws). **Direction lock: obs > null (Q 103 is
  emphatic-DENSE relative to a random equal-length corpus window).** p_perm = (#{null ≥ obs}+1)/(N+1).

**B success criterion:** B-H1 ∧ (B-H2 p_perm < α_corrected) → Arm B CONFIRMED.
**B partial:** B-H1 holds but B-H2 not significant → DIRECTIONAL.
**B failure / pre-commit violation:** if observed density < null mean (B-H2 direction reversed) →
published as NULL with explicit pre-commit-violation flag.

## Arm C — minimal tripartite qasam→jawāb→istithnāʾ skeleton (DETERMINISTIC + WITHIN-CORPUS RANK)

**Hypothesis C (pre-committed):** Q 103 realises the full qasam→jawāb→istithnāʾ rhetorical arc
across its three verses with the **minimal possible qasam→jawāb distance (1 verse)**, and its
local self-cohesion sits in the corpus top decile.

- **C-H1 (deterministic):** Per `h-new-2210.json`, Q 103 is a wāw-qasam cluster with sworn object
  tagged *temporal* (ʿaṣr), jawāb marker inna at v 2, `qasam_to_jawab_verse_distance = 1`; and v 3
  opens with the exception particle *illā* (`<il~aA`, QAC POS:EXP) — confirming oath→answer→exception
  in three successive verses.
- **C-H2 (within-corpus rank, direction-locked):** Q 103's `local_cohesion` (H-NEW-750) places it in
  the **top 15 of 114** surahs by local self-cohesion (i.e. rank ≤ 15, descending). **Direction lock:
  Q 103 is HIGH-cohesion (small rank number), not low.**

**C success criterion:** C-H1 ∧ C-H2 → Arm C CONFIRMED.
**C failure:** C-H1 false, or C-H2 rank > 15 (direction reversed = pre-commit violation) → NULL.

---

## Null distributions

- **Null B (Arm B B-H2):** corpus length-matched random-window null. The full corpus mark-stripped
  letter-stream (concatenation of every surah's verses, marks stripped, Arabic letters only) is the
  pool; 10,000 contiguous windows of length 73 are drawn at uniformly random start indices (seed
  20260509); istiʿlāʾ density of each window forms the null. This is the MW-6 instrument-control:
  a same-length, same-corpus, content-blind baseline.
- Arms A and C are deterministic corpus facts (no permutation); they do not consume α.

## Bonferroni

Test family Q103-F-01 has **k = 1 permutation cell** (B-H2). α_corrected = 0.05 / 1 = 0.05.
The deterministic cells (A-H1, A-H2, B-H1, C-H1, C-H2) are not permutation tests and do not
consume α. Small-N note: with only 3 verses, NO within-surah verse-permutation can resolve
(3! = 6 arrangements); therefore every arm here is either a deterministic corpus-rarity claim or a
corpus-level (not within-surah) permutation, exactly as the small-N design requires.

## MW protections

- **MW-1 (instrument-prior):** rā'-monorhyme test, istiʿlāʾ set, FR-rank, root-spine, and qasam-cluster
  definitions all fixed in this pre-reg before any run.
- **MW-2 (corpus-prior):** Null B uses 10,000 length-matched random corpus windows.
- **MW-3 (alternative-models):** B-H1 reports the deterministic density + dominant-emphatic
  decomposition; B-H2 reports the random-window null. A and C report deterministic corpus facts and
  the within-corpus rank.
- **MW-5 (replication):** Arms A, B-H1, C are deterministic and fully replicable from the no-tashkeel
  JSON + QAC + the H-NEW artifacts; B-H2 seed-locked at 20260509.
- **MW-6 (instrument-control):** Null B's length-73 random corpus windows are the content-blind control.
- **MW-7 (post-hoc cap):** all three observations were noticed during close reading then promoted to
  direction-locked PRE-REGISTERED tests here before computation; the single permutation cell respects
  the α = 0.05 cap.

## Verdict mapping

| Arm | Pass condition | Verdict label |
|:--|:--|:--|
| A | A-H1 ∧ A-H2 | CONFIRMED (deterministic corpus-rarity) |
| B | B-H1 ∧ (B-H2 p < 0.05) | CONFIRMED |
| B | B-H1 only | DIRECTIONAL |
| B | B-H2 direction reversed | NULL (pre-commit violation, full prominence) |
| C | C-H1 ∧ C-H2 | CONFIRMED |
| C | C-H2 rank > 15 (reversed) | NULL (pre-commit violation) |

Final Q103-F-01 verdict = honest combination of Arms A, B, C, reported with equal NULL prominence.

*Locked 2026-05-30. Seed 20260509. Bismillāhi al-Raḥmāni al-Raḥīm.*
