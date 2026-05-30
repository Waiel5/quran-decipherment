---
surah: 54
surah_name_ar: القمر
surah_name_translit: al-Qamar
file_type: novel-findings
date_last_updated: 2026-05-30
phase: B+
verdict: Q054-F-06 CONFIRMED (al-Muqtadir doubled closure-frame); F-01/F-02/F-04/F-05 CONFIRMED (PASS-DIRECTED ceilings); F-03 BRIEF-REFUTED-WITH-RHYME-SHIFT-CONFIRMED
seed: 20260509
n_perm: 10000
---

# Q 54 al-Qamar — Pre-Registered Novel Findings

Six pre-registered tests (Q054-F-01 … Q054-F-06), all SHA-256-locked before computation and verified at
runtime (fail-fast). The headline new test for this session is **Q054-F-06 (al-Muqtadir closure-concentration)**,
finalized below. All verdicts are reported with **equal NULL prominence** per PRE-REG-STANDARD-04.

- **Rules-tuple:** `(no-tashkeel, orthographic-token, verse-as-unit, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)`
- **Scripts:** `surahs/Q054-al-qamar/scripts/Q054_F_0{1..6}_*.py` (each verifies its pre-reg SHA at runtime)
- **JSON:** `surahs/Q054-al-qamar/csv/Q054-F-0{1..6}.json`

---

## Q054-F-06 — al-Muqtadir doubled closure-frame (CONFIRMED) ⭐ [this session]

- **Pre-reg:** `preregs/Q054-F-06-muqtadir-closure-concentration-prereg.md`
- **Pre-reg SHA-256:** `e76d3316f0bb61b670ad93b140778f46b8940f6b65f7c07a9dabcef992f87a98` (re-verified at runtime 2026-05-30:
  the script printed `SHA OK`)
- **Script:** `scripts/Q054_F_06_muqtadir_closure.py`; **JSON:** `csv/Q054-F-06.json`
- **Seed:** 20260509; **n_perm:** 10,000; **Bonferroni k = 2** (H6b + H6c); **α_bon = 0.025**.

**Provenance / forking-paths (disclosed in the pre-reg §0).** The *existence* of the two Q 54 *muqtadir*
tokens (vv 42, 55) was noticed during the 2026-05-09 deep-dive (overview §12), which also carried an
UNVERIFIED self-flagged "[check]" speculating Q 55:78 as a possible extra instance. This pre-reg LOCKED a
direction + permutation null and **re-verified the corpus-wide count from disk** (not assumed from the
overview). Because the two Q 54 instances were noticed pre-lock, the corpus-share cell (H6a) carries a
**PASS-DIRECTED ceiling**, not CONFIRMED; H6b (closure-position) and H6c (permutation null) are genuinely
novel and carry no post-hoc discount.

**Hypotheses (locked).**
- **H6a (PASS-DIRECTED ceiling):** Q 54 holds the corpus-MAXIMUM share of orthographic *muqtadir* (مقتدر)
  tokens; threshold Q 54 share ≥ 0.40.
- **H6b (closure-position):** BOTH Q 54 *muqtadir* instances are surah-closure-frame — pre-committed verse-set
  {(54,42) = final verse of the 5-pericope destruction-block vv 9-42; (54,55) = surah-final verse}.
- **H6c (permutation null):** Q 54's *muqtadir* count (=2) is elevated above a length-weighted multinomial
  redistribution of all corpus *muqtadir* tokens across 114 surahs; one-tailed perm-p < α_bon = 0.025.

**Result** (`csv/Q054-F-06.json`, re-run 2026-05-30):

| Cell | Statistic | Threshold | Outcome |
|:--|:--|:--|:--|
| **H6a** corpus-share | corpus *muqtadir* verses = **4** total: (18,45), (43,42), (54,42), (54,55); n_Q54 = **2**; share = **0.50**; corpus-max surah = **54** (count 2); `is_corpus_max = true` | ≥ 0.40 | **PASS** (ceiling: PASS-DIRECTED) |
| **H6b** closure-position | Q 54 *muqtadir* verses = {(54,42), (54,55)}; both ∈ committed closure-frame; n_closure = **2** | == 2 | **PASS** |
| **H6c** permutation null | observed Q 54 count = 2; **perm_p (length-weighted) = 0.0002**; perm_p (uniform, secondary) = 0.0011 | < 0.025 | **PASS** |

`pre_commit_violation_H6a = false` (Q 54 IS the corpus-max — locked direction held).

**VERDICT: CONFIRMED** (H6a PASS-DIRECTED ceiling; H6b + H6c both pass at α_bon = 0.025). Q 54 carries
**2 of the corpus's 4 *muqtadir* tokens (50%)**, BOTH in surah-closure-frame position: *fa-akhadhnāhum akhdha
**ʿAzīz Muqtadir*** (v 42, sealing the destruction-block) and *fī maqʿadi ṣidqin ʿinda **Malīk Muqtadir***
(v 55, sealing the surah). The doubled al-Muqtadir frame brackets the surah's two terminal movements with the
same name-of-capacity. al-Qurṭubī independently glosses both as *qādir / yaqdiru ʿalā mā yashāʾ*
(`03-tafsir-survey.md` §4) — the classical anchor for the empirical frame. The frame is the **theological-
rhetorical axis** linking v 1's cosmic *qadar*-event and v 49's *innā kulla shayʾin khalaqnāhu bi-qadar* axiom:
every destruction and the believer's final seat alike rest on al-Muqtadir's *qadar*.

**Honest limits (anticipated in the pre-reg §6).**
- *muqtadir* is a **rare token (N=4 corpus-wide)**; with small N the length-weighted null is coarse and the
  perm-p is granular. A count of 2 reaches significance easily — so **H6b (closure-position), not the bare
  count, is the substantive discriminator.** H6a is arithmetically near-trivial once verified.
- This is a **single-surah descriptive-architectural fact** (a doubled power-name closure frame), **NOT a
  corpus-law.** It complements but does not depend on F-01…F-05.
- The corpus count includes the plural *muqtadirūn* form (Q 43:42); the bare-stem regex `مقتدر` matched both
  the singular and plural orthographic forms, as the pre-reg operationalised.

---

## Q054-F-01 — dual-refrain 5-section architecture (CONFIRMED 3/3, PASS-DIRECTED ceiling)

- Pre-reg SHA-256: `fd1e8281a0955f7c3b1e84082bcd521e22aa58841b1939bfd40bbf9735c33413`; `csv/Q054-F-01.json`.
- **H1a (corpus-share):** all **6/6** corpus *fa-hal min muddakir* terminal-phrase verses are in Q 54
  (vv 15, 17, 22, 32, 40, 51); share = **1.0000**; perm_p (length-weighted) = 0.0; perm_p (uniform) = 0.0.
  **Corpus-MONOPOLY.**
- **H1b (pericope closures):** 5/5 pre-committed pericopes (Nūḥ, ʿĀd, Thamūd, Lūṭ, āl-Firʿawn) close by a refrain.
- **H1c (compression):** Q 26 mean verses/pericope = 26.00; Q 54 mean = 6.80; ratio = **3.824 ≥ 2.0**.
- **VERDICT: CONFIRMED 3/3.** PASS-DIRECTED ceiling on H1a (corpus-monopoly noticed pre-lock).

**This is the H-NEW-2310 / H-NEW-1320 Q 54 refrain anchor at the surah level.** H-NEW-2310's runtime
`assert` re-derives Q 54's *yassarnā* refrain count = **4** (vv 17, 22, 32, 40); the two further isolated
*fa-hal min muddakir* terminals (vv 15, 51) bring the corpus-monopoly terminal-phrase total to 6.

---

## Q054-F-05 — *wa-laqad* opener density (CONFIRMED 2/2, PASS-DIRECTED ceiling)

- Pre-reg SHA-256: `88278d98f579d7742df1315c079548f606ae396f32aa386c5d04caa91deadd12`; `csv/Q054-F-05.json`.
- **H5a:** Q 54 has **11** *wa-laqad*-opener verses / 55 = **20.0 per 100 verses**, corpus **rank 1/114**;
  next-highest Q 15 al-Ḥijr at 7.07/100 (**2.83×** the runner-up); perm_p (length-weighted) = 0.0.
- **H5b:** 10/11 *wa-laqad*-openers are refrain-paired (threshold ≥6).
- **VERDICT: CONFIRMED 2/2.** PASS-DIRECTED ceiling (density noticed pre-lock).

---

## Q054-F-04 — perfect ر-monorhyme corpus-uniqueness (CONFIRMED 2/2, PASS-DIRECTED ceiling)

- Pre-reg SHA-256: `8c1331667d6123c9290da740786d4321971c885c7307da9e9b19b4cf977a67ec`; `csv/Q054-F-04.json`.
- **H4a:** top_final_letter_frac = **1.0000** (perfect 100% ر). **H4b:** rank_B = **114/114** (corpus minimum on
  the al-Sakkākī iqāʿ axis; sig_A rank 105/114). **H4c:** Q 54 is the **ONLY perfect-monorhyme surah with ≥ 50
  verses** (15 surahs are perfect-monorhyme, all others < 50 verses).
- **MW-5 positive control:** under a shuffled-final-letter null on a Q-54-length surah (10,000 perms),
  P(perfect monorhyme) = **0.00000** — corpus-extreme.
- **VERDICT: CONFIRMED 2/2.** PASS-DIRECTED ceiling on the rules-tuple.

---

## Q054-F-02 — Q 54 vs Q 26 prophet-cycle compression (CONFIRMED 2/2, with known null-degeneracy)

- Pre-reg SHA-256: `b604bdb40233c539da7b0569ca14b732d6a18972b78e2e43cf4f404f1d8fc389`; `csv/Q054-F-02.json`.
- **H2a (verses):** compression ratio = **3.824 ≥ 2.0** PASS. **H2b (words):** ratio = **3.588 ≥ 2.0** PASS.
- **Honest limit (NULL-MODEL DEGENERACY, disclosed):** the random-partition permutation null produced
  perm_p = 1.0 for both axes, because random partitions of fixed total verses into fixed block-counts produce
  identical block-mean sizes regardless of cut placement — **the wrong null model**. The compression ratio
  (3.82× / 3.59×) stands as a **descriptive** finding; the perm-test is degenerate by construction. A proper
  null (Q 54 vs each of Q 7, Q 11, Q 19, Q 21, Q 26 individually) is queued (Q054-F-07).
- **VERDICT: CONFIRMED 2/2** on the descriptive ratios; perm-null flagged degenerate.

---

## Q054-F-03 — Q 53 → Q 54 seam (BRIEF-REFUTED-WITH-RHYME-SHIFT-CONFIRMED) — published NULL with full prominence

- Pre-reg SHA-256: `19909d279f1cf3059cbeb17b626404caf48a58e309ed4844e10d7d50bcbbd410`; `csv/Q054-F-03.json`.
- **H3a (brief-affirmation cell — locked in the brief's "clamped-zero seamless" direction):** the actual
  Q 53→Q 54 delta_raw = **+0.21006** (fraction_residual 0.0253, **rank 12/113 most-expensive** —
  `h-new-720.json`). The seam is **NOT clamped-zero; it is a TOP-12 expensive content-genre transition.**
  The locked direction is **REVERSED → published as a PRE-COMMIT VIOLATION**; the brief's hypothesis is
  empirically corrected.
- **H3b (rhyme-shift cell):** Q 53 top-final ى (0.855) vs Q 54 top-final ر (1.000); rhyme-letters NOT shared →
  **PASS** as locked.
- **H3c (thematic-continuity cell):** 4 shared destruction-narratives {Nūḥ, ʿĀd, Thamūd, Lūṭ} between Q 53:50-54
  and Q 54:9-42 → PASS (interpretive context).
- **VERDICT: BRIEF-REFUTED-WITH-RHYME-SHIFT-CONFIRMED.** 1/2 locked inferential cells (H3a reversed, H3b passed).
  The empirically-correct framing: the Q 53→Q 54 seam is a **structural content-genre transition that PRESERVES
  the Q 53-summary destruction-tetrad as the seed of Q 54's 5-pericope expansion** (al-Biqāʿī's
  expansion-from-summary munāsaba; 00-overview §11). **An honest NULL on the brief's prediction — full
  prominence.**

---

## Connection to the corpus refrain-architecture findings (H-NEW-2310 / -2470 / -1320)

Q 54 is one of the corpus's **5 strict-refrain surahs {Q 26, Q 37, Q 54, Q 55, Q 77}**. Its session-internal
F-01 (refrain corpus-monopoly) and F-06 (asmaic closure-frame) sit inside that corpus architecture:

- **H-NEW-2310 (refrain spacing-regularity) — Q 54 is a published NULL.** Q 54's *yassarnā* refrain
  (m=4, vv 17/22/32/40) is **direction-true** (gap-variance V_obs = 4.222 < null-median 40.67 — it IS spaced
  more regularly than chance) but **p = 0.0846 misses α**: with only 4 occurrences across 55 verses the test is
  **underpowered** (H-NEW-2310 §2.1). This NULL is reported with **equal prominence**: Q 54's refrain is a
  *content-boundary marker* (each closes a pericope) rather than a metronome like Q 55's 31× *fa-bi-ayyi ālāʾi*
  (V=0.116, p=0.0001 PASS) — the same discrimination H-NEW-2310 draws between Q 55/77/26-ring (PASS) and
  Q 54/37 (power-limited / story-marker NULL). **Q 54's refrain monopoly is a count/share fact (F-01,
  CONFIRMED), NOT a metronomic-spacing fact (H-NEW-2310, NULL).** The two are distinct and both are reported.
- **H-NEW-1320 (refrain saturation rank):** Q 54 ranks **5/114** (count 4, saturation 0.073) — tier-2 boundary
  of the {Q 55, Q 77, Q 26} 3-tier cluster.
- **H-NEW-2470 (ordering-by-dispersion):** Q 54 carries 13 similar-verse pairs and **disperses directionally**
  (depletion +0.47) but is far weaker than the Q 55 engine (+11.95). The corpus law is **Q55-anchored, not
  every-surah** — Q 54 is a directional-only contributor. Honest qualified placement.

**Net refrain-architecture reading of Q 54.** Its refrain distinction is **lexical-monopoly + saturation-rank**
(F-01 CONFIRMED, H-NEW-1320 rank 5), NOT **metronomic spacing** (H-NEW-2310 NULL) and NOT **decisive
dispersion** (H-NEW-2470 directional-only). The doubled al-Muqtadir asmaic frame (F-06 CONFIRMED) is the
surah's *non-refrain* closure device — the āl-Firʿawn pericope (v 42) and the surah finale (v 55) substitute the
name-of-power for the remembrance-refrain, which is precisely why those two pericopes/blocks lack the
*yassarnā* seal (`02-content-analysis.md` §3).

## Bonferroni / family summary

| Test | Cells (inferential) | α_bon | Permutation result | Verdict |
|:--|:--|:--|:--|:--|
| F-01 dual-refrain | 3 (H1a/b/c) | 0.0167 | H1a perm_p = 0.0 | **CONFIRMED 3/3** (PASS-DIRECTED ceiling) |
| F-02 compression | 2 (H2a/b) | — | degenerate null (p=1.0) | **CONFIRMED 2/2** descriptive (null flagged) |
| F-03 Q53→Q54 seam | 2 (H3a/b) | — | deterministic | **BRIEF-REFUTED + RHYME-SHIFT-CONFIRMED** (NULL on H3a) |
| F-04 monorhyme | 2 (H4a/b) | — | MW-5 perm_p = 0.0 | **CONFIRMED 2/2** (PASS-DIRECTED ceiling) |
| F-05 *wa-laqad* density | 2 (H5a/b) | — | H5a perm_p = 0.0 | **CONFIRMED 2/2** (PASS-DIRECTED ceiling) |
| **F-06 muqtadir closure** | **2 (H6b/c)** | **0.025** | **H6c perm_p = 0.0002** | **CONFIRMED** (H6a PASS-DIRECTED ceiling) |

## MW protections applied (F-06)

- **MW-1 (instrument-prior):** the `مقتدر` regex, closure-frame verse-set, and length-weighted multinomial null
  were all fixed in the pre-reg before computation.
- **MW-2 (corpus-prior):** H6c used 10,000 length-weighted multinomial permutations (seed 20260509).
- **MW-3 (alternative-models):** uniform-weighted null reported as a secondary diagnostic (perm_p = 0.0011).
- **MW-5 (replication):** H6a/H6b are deterministic and fully replicable from `quran-no-tashkeel.json`;
  H6c seed-locked. The 2026-05-30 re-run reproduces the JSON exactly (perm_p 0.0002 / 0.0011).
- **MW-6 (instrument-control):** the length-weighted redistribution across all 114 surahs is the non-target
  control — it asks whether Q 54's count exceeds what its verse-length alone predicts.
- **MW-7 (post-hoc cap):** the bare-count existence was noticed pre-lock → H6a capped PASS-DIRECTED; the novel
  closure-position + permutation cells (H6b/c) carry the inferential weight.

## Honest limits (family-wide)

- Four of the six tests (F-01, F-04, F-05, plus F-06's H6a) carry **PASS-DIRECTED ceilings** because the headline
  observation was noticed during the 2026-05-09 close-read before locking — promotion to CONFIRMED-FULL requires
  independent replication on a distinct dimension (alt-orthography, alt-operationalization), queued in JOURNAL.
- F-03 is an honest **pre-commit violation** on the dispatch-brief's seam prediction — the most important NULL of
  the family, reported with full prominence.
- F-02's permutation null is degenerate by construction; only the descriptive compression ratio is load-bearing.
- F-06's significance is easy to reach given N=4; **H6b (closure-position) is the substantive content**, and the
  finding is a single-surah descriptive fact, not a corpus-law.

---

*Computed 2026-05-30 (F-06 re-run; SHA verified `SHA OK`), seed 20260509, 10,000 perms. F-01…F-05 results
carried from the 2026-05-09 session JSON. All values traced to `csv/Q054-F-0{1..6}.json`.*
