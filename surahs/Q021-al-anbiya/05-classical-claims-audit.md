---
surah: 21
surah_name_ar: الأنبياء
file_type: classical-claims-audit
date_last_updated: 2026-05-07
phase: B+
verdict: COMPLETE — 5 classical claims audited
---

# Q 21 al-Anbiyāʾ — Classical Claims Audit


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

Five classical claims about Q 21 are tested empirically with rules-tuple specification.

## Claim 1 — al-Bāqillānī: Q 21:30 is *iʿjāz al-mafāhīm* on cosmology

**Source**: al-Bāqillānī, *Iʿjāz al-Qurʾān* — the heavens-and-earth-were-joined-then-separated verse is cited as a Quranic statement of cosmological fact whose accuracy is itself an iʿjāz-marker. Cited in al-Suyūṭī *al-Itqān* nawʿ 65 (PENDING-VERIFICATION on specific page-number; the secondary literature uniformly attributes this position to al-Bāqillānī).

**Empirical correlate** — Q021-F-04 cosmological-cluster cohesion test. The classical claim has multiple sub-claims:
- Q 21:30 is a self-standing iʿjāz statement (theological/scientific).
- Q 21:30-33 form a 4-verse coherent cosmological unit (al-Biqāʿī's *naẓm* claim).

**Rules-tuple test**: `(QAC-v0.4-STEM-roots-per-verse, count-vector, cosine-similarity, no-tashkeel)`.

**Verdict**: **NULL / DIRECTIONAL-borderline** at the *naẓm* sub-claim. The 4-verse block has cosine sim 0.141 vs contig-null mean ~0.124 (p=0.127); against non-contig null (p=0.056). The al-Biqāʿī *naẓm*-coherence claim is not strongly empirically supported at QAC-roots level. The *theological/scientific* iʿjāz status of Q 21:30 itself is OUT-OF-SCOPE for this empirical test (theological-philosophical, not empirical-architectural).

## Claim 2 — al-Rāzī: Q 21:22 is the *burhān al-tamānuʿ* anchor

**Source**: al-Rāzī, *Mafātīḥ al-ghayb*, treatment of Q 21:22 (extensive *masāʾil* on the conditional-counterfactual *law kāna fī-himā āliha illā Allāh la-fasadatā*). al-Rāzī derives 4 sub-arguments (two-omnipotent-wills, joint-sovereignty-incoherence, cosmic-causation-singularity, no-corruption-confirms-unity).

**Empirical correlate**: This is a *theological-philosophical* claim about the verse's argumentative structure. It is **NOT-EMPIRICALLY-TESTABLE** in the Q021-F-NN test framework — there is no measurable architectural signature for the *burhān al-tamānuʿ*'s philosophical strength.

**Verdict**: **NOT-EMPIRICALLY-TESTABLE** in the project's rules-tuple framework. al-Rāzī's claim stands as a classical-theological position; the project's empirical methods cannot validate or falsify it.

## Claim 3 — al-Biqāʿī: Q 20 → Q 21 → Q 22 munāsabah triad

**Source**: al-Biqāʿī, *Naẓm al-durar fī tanāsub al-āyāt wa-l-suwar*, treatment of Q 20-Q 21-Q 22 connections. The triad: Q 20 closes "wait, then" (*fa-tarabbaṣū*), Q 21 opens "the reckoning has drawn near" (*iqtaraba*), Q 22 opens "fear your Lord" (*it-taqū rabbakum*). Eschatological tightening across three surahs.

**Empirical correlate**: 
- **Q 20-Q 21 canonical-adjacency cost**: 0.0544 (rank 64/113, modest = "easy boundary"). [[h-new-720-canonical-adjacency-cost|H-NEW-720]].
- **Q 21-Q 22 canonical-adjacency cost**: 0.1776 (rank 16/113, top-15 expensive boundary).

**Rules-tuple**: `(QAC-v0.4-STEM-roots, FR-distance, top-K=500, Dirichlet α=0.5, L1-normalize)`.

**Verdict**: **MIXED — DIRECTIONAL on Q 20→Q 21, FALSIFIED on Q 21→Q 22**.
- The Q 20→Q 21 *tartīb* is empirically smooth (rank 64/113 cost) — consistent with al-Biqāʿī's *fa-tarabbaṣū → iqtaraba* munāsabah.
- The Q 21→Q 22 *tartīb* is empirically expensive (rank 16/113 cost) — al-Biqāʿī's *iqtaraba → it-taqū rabbakum* munāsabah is **NOT** matched by FR-roots smoothness. The mushaf pays a cost here.

The classical *munāsabah* tradition often reads thematic-eschatological continuity onto FR-roots-distant pairs; this is the case for Q 21→Q 22. The al-Biqāʿī claim captures *thematic* tightening but not *root-vocabulary* smoothness.

## Claim 4 — al-Suyūṭī chronology: Q 21 is middle-Meccan, revelation #73

**Source**: al-Suyūṭī, *al-Itqān fī ʿulūm al-Qurʾān*, nawʿ 1 (chronology). The standard chronology places Q 21 as revelation 73 of 114 (middle-Meccan, prior to the Hijra).

**Empirical correlate**: 
- al-Suyūṭī's chronology has been *empirically locked* at the s=50 Hijra-kink ([[h-new-660-compression-tail-gradient|H-NEW-660]]); Meccan/Medinan boundary holds at perm p<10⁻⁴.
- For Q 21 specifically: middle-Meccan classification implies content-distance d̄ in the head-zone (d̄ ≈ 0.96 by the law). Q 21's observed d̄ = 1.010 is near-prediction (slight upward deviation = WEAK_ANCHOR, consistent with a middle-Meccan with modest content-distinctness).

**Rules-tuple**: `(QAC-v0.4-STEM-roots, FR-distance, K=15-window, Dirichlet α=0.5, L1-normalize)`.

**Verdict**: **VINDICATED**. al-Suyūṭī's chronological placement of Q 21 is consistent with the H-NEW-660 compression-tail law (Q 21 is in the head-zone, content-distance near corpus mean for s=21 position). No specific revelation-number test is performed (revelation-number assignment is itself a chronology-internal scheme, not an empirically-derivable invariant).

## Claim 5 — al-Bukhārī Ibn Masʿūd hadith: Q 17-Q 21 are "old property"

**Source**: al-Bukhārī, *al-Jāmiʿ al-ṣaḥīḥ* hadith #4533 and #4787 (Kitāb al-Tafsīr / Kitāb Faḍāʾil al-Qurʾān). Ibn Masʿūd states: "Banī Isrāʾīl, al-Kahf, Maryam, Ṭā-Hā, al-Anbiyāʾ are from the very old surahs which I learned by heart, and they are my first property." The implication: Q 17-Q 21 were among the earliest-revealed (and earliest-memorized) surahs, a *contiguous* mushaf-block of "old property".

**Empirical correlate**:
- The Q 17-Q 21 block crosses both al-sabʿ-al-ṭiwāl boundary (Q 17 last of the *ṭiwāl* tier in some classifications) and the **true-isolate boundary** (Q 21 enters true-isolate cluster).
- Q 17-Q 18 adjacency cost (H-NEW-720): rank ~95 (cheap).
- Q 18-Q 19: rank ~85 (cheap).
- Q 19-Q 20: rank ~70 (modest).
- Q 20-Q 21: rank 64 (modest).

The Q 17-Q 21 5-surah block is a relatively-cheap-internal-cost mushaf segment. This is **CONSISTENT** with the Ibn Masʿūd "memorized as a unit" claim — a unit with low internal *tartīb* friction.

**Rules-tuple**: `(QAC-v0.4-STEM-roots, FR-distance, top-K=500, Dirichlet α=0.5, L1-normalize)`.

**Verdict**: **VINDICATED**. The Bukhārī Ibn Masʿūd hadith identifying Q 17-Q 21 as a "first property" memorization-block is empirically consistent with low internal canonical-adjacency cost. The Q 21 boundary at the *outer* end of this block (Q 21→Q 22 cost rank 16) marks the transition out of the "old property" cluster into the al-Ḥajj/al-Muʾminūn middle-Medinan-tier zone (Q 22 is Medinan in some classifications).

## Audit summary

| # | Claim | Source | Verdict |
|:-:|:--|:--|:--|
| 1 | Q 21:30 cosmological iʿjāz / vv. 30-33 *naẓm* unit | al-Bāqillānī / al-Biqāʿī | DIRECTIONAL-borderline (NULL on contig-null; p=0.056 on non-contig) |
| 2 | Q 21:22 *burhān al-tamānuʿ* | al-Rāzī | NOT-EMPIRICALLY-TESTABLE |
| 3 | Q 20-Q 21-Q 22 munāsabah triad | al-Biqāʿī | MIXED (Q20→Q21 vindicated; Q21→Q22 FALSIFIED on root-smoothness) |
| 4 | Q 21 middle-Meccan chronology | al-Suyūṭī | VINDICATED |
| 5 | Q 17-Q 21 Ibn Masʿūd "old property" cluster | al-Bukhārī #4533, #4787 | VINDICATED |

**Net audit**: 2 VINDICATED, 1 MIXED, 1 DIRECTIONAL-borderline (effectively NULL), 1 NOT-EMPIRICALLY-TESTABLE.

The classical tradition's most-influential claims about Q 21 (cosmological-iʿjāz of v. 30, *burhān al-tamānuʿ* of v. 22) are theological-philosophical and not directly empirically-testable in the project's rules-tuple framework. The chronological placement (al-Suyūṭī) and the hadith-attested mushaf-cluster (al-Bukhārī Ibn Masʿūd) are vindicated. The al-Biqāʿī munāsabah triad is partly vindicated and partly falsified — the Q 21→Q 22 transition specifically pays a top-15 TSP-cost despite al-Biqāʿī's claim of thematic-eschatological tightening.

## Cross-references

- All 5 mufassirūn surveyed in `03-tafsir-survey.md`.
- Pre-registered novel tests: `Q021-F-04` (Claim 1), `Q021-F-05` (related to Claim 3).
- [[h-new-720-canonical-adjacency-cost|H-NEW-720]]: Q 20-Q 21 rank 64; Q 21-Q 22 rank 16.
- [[h-new-660-compression-tail-gradient|H-NEW-660]]: chronology kink at s=50 (al-Suyūṭī validation).
