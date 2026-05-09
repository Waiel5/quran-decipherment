---
id: H-NEW-1300
title: Q 96 al-ʿAlaq *qrʾ*-imperative corpus-distribution
date_locked: 2026-05-09
date_run: 2026-05-09
verdict: NULL (per strict pre-reg) | DESCRIPTIVE-CLUSTERING (post-hoc note)
seed: 20260509
n_perm: 10000
prereg_sha: 201d8a26cb063b2bd2c4d277ed90f65402bb89a1a3a61675e48955bfd4e64395
prereg_path: findings/phase-b-hypotheses/h-new-1300-q96-iqra-corpus-distribution-prereg.md
script_path: findings/phase-b-hypotheses/scripts/h_new_1300_q96_iqra.py
output_json: findings/phase-b-hypotheses/csv/h-new-1300.json
---

# H-NEW-1300 — Q 96 al-ʿAlaq *qrʾ*-imperative corpus-distribution

## Result: NULL (by strict pre-reg)

The pre-registered direction-of-effect was: **"Q 96 has the maximum *qrʾ*-imperative count of any of the 114 surahs (rank #1 by absolute count of IMPV verb-segments with ROOT:qrA)."**

The empirical result: **Q 96 is TIED at rank 1 with Q 73 al-Muzzammil at 2 IMPV+qrA segments each.** The pre-reg required strict maximum (no ties). Therefore, by the locked pre-reg, this is **NULL**.

Per PRE-REG-STANDARD-01 / §1.8 Protocol direction-flip prohibition, this NULL is published with the same prominence as a PASS would have received.

## Observed values

| Surah | IMPV+qrA count | Verse | Word | Form |
|:--|:--:|:--:|:--:|:--|
| Q 17 al-Isrāʾ | 1 | 17:14 | 1 | `{qora>o` |
| Q 69 al-Ḥāqqa | 1 | 69:19 | 8 | `{qora'u` |
| Q 73 al-Muzzammil | 2 | 73:20 | 26, 49 | `{qora'u` (×2 in same verse) |
| Q 96 al-ʿAlaq | 2 | 96:1 word 1; 96:3 word 1 | `{qora>o` (×2 in two verses) |

**Total IMPV+qrA in entire Quran: 6 segments across 4 surahs.** 110 of 114 surahs have zero.

## Permutation null

Under random relocation of all 6 IMPV+qrA segments to surahs (weighted by total IMPV-segment count per surah, preserving the marginal):

- p_perm (joint: Q 96 ≥ 2 AND rank-1 ≥ 2): **0.00010** (1 / 10000)
- p (Q 96 ≥ 2 alone): **0.00010**
- p (any rank-1 ≥ 2 alone): 0.38320 (low because total = 6 distributed ≥114 surahs allows occasional 2-clusters)

So while Q 96's count of 2 is **per-surah-extreme** at p < 10⁻⁴, the joint condition with strict-rank-1 (no ties) is what fails the pre-reg.

## What survives the strict-NULL verdict

The IMPV-qrA inventory is **structurally clustered**: 4 of 114 surahs (3.5%) account for 100% of corpus IMPV-qrA segments. The 4 surahs split into two **classical-context pairs**:

### Pair 1 — Prophetic revelation imperatives (Q 73 + Q 96)
- **Q 96 al-ʿAlaq vv 1, 3**: "iqraʾ bismi rabbika alladhī khalaq" / "iqraʾ wa-rabbuka al-akram" — the FIRST imperatives revealed to the Prophet per Bukhārī Bad' al-Waḥy.
- **Q 73 al-Muzzammil v 20**: "fa-iqraʾū mā tayassara min al-qurʾān" (×2 within the same verse — the "long verse" of Q 73 v 20) — the night-prayer recitation imperative.

Both surahs are **classically among the very earliest revealed**: Q 96:1-5 first per Bukhārī; Q 73 ranks Nöldeke #3 (verify against `data/revelation-order.csv`).

### Pair 2 — Eschatological "read your record" imperatives (Q 17 + Q 69)
- **Q 17:14**: "iqraʾ kitābak, kafā bi-nafsika al-yawma ʿalayka ḥasībā" — second-person addressee in the Day of Judgment ledger-reading.
- **Q 69:19**: "fa-ammā man ʾūtiya kitābahū bi-yamīnih, fa-yaqūlu hāʾūmu iqraʾū kitābiyah" — third-person eschatological narration of the saved reading their record.

Both contexts feature *kitāb* + *iqraʾ* in eschatological-judgment registers — connecting to **cross-finding-008 muqaṭṭāʿat-as-book-introduction-markers** at the imperative-mood layer.

## Post-hoc-noticed observation (logged for future pre-reg)

The IMPV-qrA inventory bifurcates cleanly into a **prophetic-revelation pair (Q 73 + Q 96)** and an **eschatological-record-reading pair (Q 17 + Q 69)**. Both pairs share *kitāb* + *iqraʾ* lexis but in distinct rhetorical settings.

This observation is **post-hoc** (emerged from looking at the rank-1 tie). It cannot be promoted from this pre-reg. It seeds H-NEW-1301 (next entry below).

## H-NEW-1301 follow-up pre-reg seed (NOT yet locked)

**Hypothesis (to be locked before viewing data)**: The 4 IMPV-qrA surahs {Q 17, 69, 73, 96} form a tight Fisher-Rao cluster relative to a length-matched random-surah baseline.

**Proposed test**: Compute mean intra-cluster pairwise FR distance for {17, 69, 73, 96}; permutation null = 10000 random length-matched 4-surah samples. Direction: intra-cluster mean ≤ permutation 5th percentile.

**Bonferroni**: k=1 single test. α = 0.05.

**Pre-commit attestation**: this pre-reg seed will be SHA-locked as `findings/phase-b-hypotheses/h-new-1301-impv-qra-cluster-prereg.md` BEFORE the FR matrix is loaded. NOT executed in this finding.

## Connections to existing findings

- **Cross-finding-008** (muqaṭṭāʿat as book-introduction markers, p ≤ 10⁻¹²): Q 96 references *qalam* explicitly at v 4, joining the H-NEW-56 extended-writing-cluster. But Q 96 is itself non-muqaṭṭāʿat. The IMPV-qrA inventory is orthogonal to muqaṭṭāʿat status: 0 of the 4 IMPV-qrA surahs are muqaṭṭāʿat-opened.
- **H-NEW-74** *qul* imperative count = 332. *iqraʾ* corpus inventory = 6. The contrast is structurally informative: *qul* is the dominant prophetic-mouth-piece imperative (frequency-saturated), *iqraʾ* is rare and ritualistically marked.
- **Cross-finding-012** Late-Meccan scripture-announcement apparatus: Q 96 is **Early-Meccan**, Q 73 is **Early-Meccan**, Q 69 is **Middle/Late-Meccan**, Q 17 is **Late-Meccan/early-Medinan**. The IMPV-qrA inventory spans the Meccan period without concentrating at Late-Meccan — orthogonal to cross-finding-012's qul/eschatology/loanword Pattern-B.

## Honest limits

- **Strict NULL by pre-reg**: the rank-1 tie kills the inferential claim. The descriptive 4-surah clustering is post-hoc and capped at single-test α=0.05 PASS-DIRECTED ceiling pending H-NEW-1301 replication.
- **Rules-tuple sensitivity**: tested under both root-filter (ROOT:qrA) and lemma-filter (LEM:qara>a). Same 6-segment inventory under both. Tested with QAC v0.4 morphological tags only; no cross-corpus replication of the IMPV identification.
- **Q 73 v 20 has 2 IMPV-qrA within ONE verse**: this could be interpreted as "Q 73 has only 1 imperative event with internal repetition" rather than "2 distinct imperative events." Under the verse-event count, Q 96 (2 imperative events in 2 verses) would strictly exceed Q 73 (1 imperative event with internal doubling). But this would be a **post-hoc rule change** to flip the verdict — explicitly forbidden. The segment-count rule was locked in the pre-reg's `word_definition: morphological-segment` field.

## Classical citations

- al-Bukhārī, *Ṣaḥīḥ*, Kitāb Bad' al-Waḥy, ḥadīth #3 (per on-disk `data/hadith/bukhari*`) — Q 96:1-5 first revealed.
- al-Ṭabarī, *Tafsīr* on Q 73:20 — connection of "fa-iqraʾū" to night-prayer length-relaxation post-revelation.
- al-Suyūṭī, *al-Itqān fī ʿulūm al-Qurʾān*, nawʿ on first-revealed surah (verify nawʿ-number against on-disk PDF before quoting).

## Verdict summary

| Cell | Status | p | Note |
|:--|:--|:--|:--|
| A — strict rank-1 by absolute count | NULL | tied at 2 with Q 73 | pre-reg violated by tie |
| A — joint Q 96 ≥ 2 AND rank-1 ≥ 2 | extreme | p_perm = 0.00010 | descriptive only, not the pre-reg |
| B — per-verse density | NULL | Q 96 not rank-1 by density | descriptive cell only |

**Final verdict: NULL by strict pre-reg.** Descriptive 4-surah {Q 17, 69, 73, 96} clustering noted; H-NEW-1301 follow-up pre-reg drafted but not yet locked or run.
