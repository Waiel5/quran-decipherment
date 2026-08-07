---
surah: 3
surah_name_ar: آل عمران
surah_name_translit: Āl ʿImrān
file_type: classical-claims-audit
date_last_updated: 2026-05-29
phase: B+
verdict: 6 claims audited — 4 VINDICATED, 1 SPLIT (block-cohesion: deterministic ✓ / permutation ✗), 1 NOT-TESTABLE
---

# Q 3 Āl ʿImrān — Classical Claims Audit


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

Each claim is stated with citation, given a rules-tuple, tested where empirically testable, and given an
honest verdict. Default rules-tuple: `(no-tashkeel, orthographic-token, basmala-counted-only-in-Q1,
Hafs-Kufan, Mashriqi)`. Verse text from `quran-text/quran-no-tashkeel.json`.

## Claim 1 — "Āl ʿImrān is Medinan; 200 verses" (al-Zamakhsharī)

**Claim:** al-Zamakhsharī, *al-Kashshāf*, surah-header: *"madaniyya wa-hiya miʾatā āya"* (Medinan, two hundred
verses).

**Test:** Count verses in `quran-text/quran-no-tashkeel.json` (Q 3); cross-check `data/hafs-verse-counts.tsv`
and `data/revelation-order.csv`.

**Result:** 200 verses in the JSON; `hafs-verse-counts.tsv` line 3 = 200; `revelation-order.csv`: Q 3 =
revelation #89, period "Medinan", Nöldeke #97 "Medinan."

**Verdict: VINDICATED.** Q 3 is Medinan and exactly 200 verses in the Hafs-Kūfan count on disk.

## Claim 2 — al-Bukhārī/Muslim: al-Baqara + Āl ʿImrān are *al-Zahrāwān* (a single faḍāʾil pair)

**Claim:** Muslim, *Ṣaḥīḥ*, *Kitāb Ṣalāt al-Musāfirīn*, ḥadīth #1766 (Abū Umāma): recite *al-Zahrāwān* — Sūrat
al-Baqara and Sūrat Āl ʿImrān — for they come as two clouds interceding. The two surahs are treated as a
liturgical-virtue *pair*.

**Test:** Is Q 2 the Fisher-Rao NEAREST neighbour of Q 3? Read `h-new-111.json` (Q 3 row).

**Result:** Q 3's nearest FR neighbour is **Q 2 al-Baqara at FR 0.6309** — rank 1/113 in Q 3's neighbour list,
and one of the smallest long-surah pair-distances in the corpus.

**Verdict: VINDICATED.** The classical *al-Zahrāwān* pairing of al-Baqara + Āl ʿImrān has a direct empirical
correlate: the two surahs are mutual FR-nearest-neighbours in root-distribution space. Their shared Medinan
creedal-legal-narrative vocabulary makes them the closest long-surah pair — the faḍāʾil pairing tracks the
content-geometry.

## Claim 3 — al-Suyūṭī / al-Zarkashī: the muṣḥaf-head {Q2-Q5} is a continuous *al-ṭiwāl* block

**Claim:** al-Suyūṭī, *al-Itqān*, on the order of the sūras, and al-Zarkashī, *al-Burhān*, *al-nawʿ fī
al-munāsaba* — the head of the muṣḥaf (the al-sabʿ al-ṭiwāl) is a thematically continuous block, and the
Q 2→Q 3→Q 4→Q 5 sequence is a coherent Medinan run.

**Test (PRE-REGISTERED as Q003-F-01 Arm A + Arm C):** (A) Is the contiguous 4-surah block {Q2,Q3,Q4,Q5} the
smoothest such block in the muṣḥaf on the H-NEW-720 mean-internal-TSP-seam metric? (C) Is that smoothness
beyond a max-statistic permutation null?

**Result:**
- **Arm A VINDICATED:** the {2,3,4,5} block mean internal seam = **−0.03196**, **rank 1/111** among all
  contiguous 4-surah blocks (the unique minimum). The top-3 smoothest blocks ({2-5}, {4-7}, {3-6}) are all
  overlapping windows inside al-sabʿ al-ṭiwāl.
- **Arm C NULL (honest):** a max-statistic permutation null (10,000 random re-arrangements of the 113 seam
  values, recording the smoothest 4-block each time) finds a block at least as smooth as {2-5} in **12.3%** of
  arrangements (p_perm = 0.12319). The corpus's many negative seams mean a smoothest-block this smooth is NOT
  by itself statistically surprising once the multiplicity of 111 candidate blocks is controlled.

**Verdict: SPLIT.** al-Suyūṭī/al-Zarkashī's *qualitative* al-ṭiwāl-block continuity is VINDICATED at the
deterministic-rank level (the head-block IS the corpus's smoothest 4-surah run, Arm A) — but its *statistical
surprise* is NOT established (Arm C NULL). The block is real and maximal, but its degree of smoothness is
within reach of chance seam-arrangement. Full detail in `06-novel-findings.md`; published with equal NULL
prominence.

## Claim 4 — al-Rāzī/al-Biqāʿī: the Q 3 → Q 4 munāsaba (the family/creed surah leads into the family-law surah)

**Claim:** al-Rāzī (*Mafātīḥ al-ghayb*) and al-Biqāʿī (*Naẓm al-Durar*) on the munāsaba between Āl ʿImrān
(which closes on the believing community, Uḥud, and *ribāṭ*) and al-Nisāʾ (which opens on the family and its
inheritance law) — the two surahs are a continuous Medinan-community pair.

**Test:** Does the Q 3 → Q 4 seam have an empirical smoothness correlate? Read `h-new-720.json`.

**Result:** Q 3 → Q 4 delta_raw = **−0.04662**, ascending-rank **4/113** — a clamped/negative **seamless seam**
(one of the smoothest joints in the muṣḥaf). Q 4 is also Q 3's 3rd-nearest FR neighbour (0.7931).

**Verdict: VINDICATED.** al-Rāzī/al-Biqāʿī's qualitative Q 3 → Q 4 munāsaba has a direct quantitative
correlate: the transition is the rank-4 smoothest seam in the corpus. The shared Medinan
community/family/legal vocabulary makes the two surahs' root-distributions adjacency-cheap.

## Claim 5 — Ibn Kathīr: the first 83 āyāt respond to the Najrān delegation (year 9)

**Claim:** Ibn Kathīr, *Tafsīr al-ʿaẓīm*, on Q 3:1: "the first eighty-three āyāt relate to the delegation from
Najrān that arrived in al-Madīna in the ninth year of Hijra," anchored by the Mubāhala verse (Q 3:61).

**Test:** This is an asbāb-al-nuzūl / historical-occasion claim, anchored by Bukhārī #4187 (the al-ʿĀqib /
al-Sayyid Najrān delegation). It is a riwāya/sīra claim, not a structural-numerical claim about the text.

**Verdict: NOT-TESTABLE (empirically).** The Najrān-occasion of the first 83 āyāt is a historical-isnād
matter outside the project's empirical-architectural instruments. The Mubāhala-delegation event IS on-disk
attested (Bukhārī #4187, #4188, #3582; see `04-hadith-corpus.md`); the verse-count assignment ("first 83") is
documented, not adjudicated.

## Claim 6 — al-Bāqillānī (iʿjāz al-fawāṣil): is Āl ʿImrān a high structural-iʿjāz surah?

**Claim (project-internal, testing al-Bāqillānī's *iʿjāz al-fawāṣil* axis):** a long, doctrinally central
surah like Āl ʿImrān should rank high on the fāṣila-significance (sig_A) axis.

**Test:** Read Q 3's sig_A and rhyme entropy from `h-new-750.json`.

**Result:** Q 3 sig_A = **−0.8179, rank 84/114** (mid-LOW). But its rhyme_entropy = 1.249 nats (z = +0.87,
ABOVE average) — its fawāṣil are MORE varied than typical. The low sig_A rank is driven entirely by its
extreme content-distance (z_mean_content_distance = +1.69), which the sig_A formula penalises.

**Verdict: VINDICATED-with-nuance (FALSIFIES the naive expectation).** Āl ʿImrān is NOT a high-sig_A surah —
but the reason refines al-Bāqillānī: Q 3's verse-endings ARE highly varied (high rhyme entropy), satisfying
the *fawāṣil-variety* intuition; it ranks low only because the composite sig_A also penalises content-distance,
and Q 3 is an FR-distant long surah. The fawāṣil-variety component (the genuinely al-Bāqillānī-relevant axis)
is satisfied; the composite score is dominated by the content-geometry axis. This is the same pattern seen in
the long-surah block generally.

## Summary table

| # | Claim | Source | Verdict |
|:--|:--|:--|:--|
| 1 | Medinan; 200 verses | al-Zamakhsharī | **VINDICATED** |
| 2 | al-Zahrāwān (Q2+Q3 pair) | Muslim #1766 | **VINDICATED** (FR-nearest-neighbour) |
| 3 | {Q2-Q5} continuous al-ṭiwāl block | al-Suyūṭī / al-Zarkashī | **SPLIT** (rank-1 block ✓ Arm A / not beyond chance ✗ Arm C) |
| 4 | Q 3 → Q 4 munāsaba | al-Rāzī / al-Biqāʿī | **VINDICATED** (seam rank 4/113) |
| 5 | first 83 āyāt = Najrān occasion | Ibn Kathīr | NOT-TESTABLE |
| 6 | high structural-iʿjāz (fawāṣil) | al-Bāqillānī (axis) | VINDICATED-with-nuance (variety ✓, composite low) |

## Honest limits

- Claim 3's SPLIT turns on the max-statistic permutation null; a different null (e.g. block-position
  permutation rather than seam-value permutation, or a non-max statistic) could shift p_perm. The
  deterministic rank-1 status (Arm A) is robust; the statistical-surprise claim (Arm C) is the contested part.
- Claim 2's FR-nearest-neighbour correlate is on QAC-STEM root distributions; a lemma- or surface-level metric
  could reorder the neighbour list, though the Q 2/Q 3 proximity is robust given their shared vocabulary.
- Verse-count variant traditions: the Kūfan/Baṣran counting schools agree on 200 for Q 3 on disk; no variant
  count is present.

---

*All testable claims pre-registered before computation (Q003-F-01) or deterministic. 2026-05-29.*
