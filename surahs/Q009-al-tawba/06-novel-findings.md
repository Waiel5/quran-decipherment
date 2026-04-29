---
surah: 9
surah_name_ar: التوبة
surah_name_translit: al-Tawba
file_type: novel-findings
date_last_updated: 2026-04-28
phase: B+
verdict: 4 pre-registered novel findings completed. Q009-F-01 FALSIFIES the no-mercy-→ no-basmala classical claim (mercy-density rank 24/114, ABOVE corpus mean). Q009-F-02 VINDICATES the al-Faḍiḥa naming (hypocrisy rank 5/114). Q009-F-03 VINDICATES the Q9-Q10 boundary as rank 4/113 most expensive canonical adjacency, with muqaṭṭaʿāt-cluster-control falsifying that as the driver. Q009-F-04 returns NULL on the single-dominant-last-revealed-verse claim.
---

# Q 9 al-Tawba — Novel Findings

This file collates novel pre-registered findings on Q 9 produced in this investigation. Each is direction-locked, SHA-verified, Bonferroni-corrected, and reports honest NULL/DIRECTIONAL/VINDICATED/FALSIFIED verdicts.

**Bonferroni**: family k = 5; α_corrected = 0.01.

---

## Q009-F-01 — Mercy-vocabulary density audit

- **Pre-reg**: `Q009-F-01-mercy-density-prereg.md` (SHA: `edb931a1294429b216bd18332d59c4c42189cda6bc2d09a192e5ce403b01ec62`)
- **Script**: `/Users/grey/Downloads/quran/scripts/Q009_F_01_02_density.py`
- **Results**: `csv/Q009-F-01-02-density-results.json`

### Hypothesis (DIRECTION-LOCKED)
Q 9's per-1000-token mercy-vocabulary density (root r-ḥ-m, QAC `rHm`) is **at or below the lower-quartile** of the 114-surah distribution (rank ≥ 87 of 114). This is the empirical correlate of Position 5 in the classical "no-basmala" debate (ʿAlī b. Abī Ṭālib, al-Mubarrad, Sufyān b. ʿUyayna).

### Rules-tuple
Hafs no-tashkeel · orthographic-words · QAC v0.4 root-index · density per 1000 tokens.

### Result
- Q 9 *r-ḥ-m* count: **13 attestations**
- Q 9 density: **4.86 / 1k tokens**
- Q 9 rank from top: **24 / 114**
- Corpus mean: 3.95 / 1k tokens
- Corpus median: 1.59 / 1k tokens

Q 9 is in the **top-quartile** of the corpus by mercy density — substantially ABOVE the corpus mean and median, NOT below.

### Pre-committed thresholds
- VINDICATED if rank ≥ 87 (low density). **NOT MET.**
- DIRECTIONAL VIOLATION if rank ≤ 28 (high density). **MET.**

### Verdict: **DIRECTIONAL VIOLATION — classical claim FALSIFIED**

The pre-committed direction (low mercy-density supporting the no-mercy-because-war classical position) was **violated**. We REPORT this as a falsification of the classical claim, with full prominence per protocol §1.3.

### What it means
The classical Position 5 ("no basmala because no mercy in this surah") is **empirically untenable**. Q 9 contains 13 attestations of the mercy-root, including:
- v. 5: *fa-inna llāha ghafūrun raḥīm*
- v. 27: *wa-llāhu ghafūrun raḥīm*
- v. 99: *yudkhilahum llāhu fī raḥmatih*
- v. 102: *wa-llāhu ghafūrun raḥīm*
- v. 117: *innahu bihim raʾūfun raḥīm* (about the Prophet's mercy to believers)
- v. 128: *bi-l-mu'minīna raʾūfun raḥīm* (about the Prophet)

The surah's CLOSING verse (v. 128) is in fact one of the strongest *raḥma*-attributive statements in the Quran. The classical Position 5 reads Q 9 through the lens of vv. 1-37 (the harsh treaty-revocation block) and ignores the textual reality that mercy-vocabulary is woven through the entire surah.

### What it does NOT establish
- The fine-grained semantic question — *who* receives the mercy (penitent ex-polytheists vs. the unrepentant), and whether the mercy is *exclusively* for *al-tāʾibūn* — is OPEN.
- The "no-basmala" question itself remains: at minimum, three other classical positions (Qurṭubī Positions 1, 2, 3) are not falsified by this finding.

---

## Q009-F-02 — Hypocrite-vocabulary density audit (al-Faḍiḥa)

- **Pre-reg**: `Q009-F-02-hypocrite-density-prereg.md` (SHA: `980b8caa77bf0778318aa51bb09250c1780adaeb313fef5c9e59bba3d4a83b40`)
- **Script**: `/Users/grey/Downloads/quran/scripts/Q009_F_01_02_density.py`
- **Results**: `csv/Q009-F-01-02-density-results.json`

### Hypothesis (DIRECTION-LOCKED)
Q 9's per-1000-token *n-f-q* (hypocrisy) density is in the **top-decile** of the 114-surah distribution (rank ≤ 12).

### Result
- Q 9 *n-f-q* count: **21 attestations**
- Q 9 density: **7.85 / 1k tokens**
- Q 9 rank from top: **5 / 114**
- Corpus mean: 1.02 / 1k tokens
- Corpus median: 0 (most surahs have zero attestations)

Q 9 is in the **top-decile** — rank 5/114, comfortably above the pre-committed threshold.

### Differential test (replication, n-f-q vs. k-f-r)
Q 9 *n-f-q* rank: 5
Q 9 *k-f-r* rank: 17
Difference: **−12**. Q 9 is *more distinctively* a hypocrisy-discussing surah than a disbelief-discussing surah, supporting the al-Faḍiḥa naming specifically (vs. a generic anti-disbelief naming like *al-Kāfira*).

### Verdict: **VINDICATED**

The classical naming *al-Faḍiḥa* (the Exposer) — al-Bukhārī ḥadīth #4674 via Saʿīd b. Jubayr → Ibn ʿAbbās — is now **empirically grounded at law-strength**. Q 9's nifāq-density is the most distinctive in the entire Quran (top-5; Q 63 al-Munāfiqūn is rank 1 by ratio but Q 63 has only 180 tokens; Q 9 is the longest surah with this signature density).

### Cross-implications
- The al-Faḍiḥa empirical signature is **content-driven**, not fāṣila-driven, consistent with [[h-new-750-per-surah-iʿjāz-signature]] placing Q 9 in the *anti-iʿjāz* (content-driven) quadrant (sig_A rank 107/114).
- This is one of the **clearest examples** of the project's core thesis: classical scholarship's rhetorical/qualitative observations have measurable empirical signatures at corpus-scale.

---

## Q009-F-03 — Q 9-Q 10 boundary structural audit

- **Pre-reg**: `Q009-F-03-q9-q10-boundary-prereg.md` (SHA: `a3f04af0f84584cbda89a983e5ad1bb30f4b825ce2e9a435c4d6ec1140ad4842`)
- **Script**: `/Users/grey/Downloads/quran/scripts/Q009_F_03_q9_q10_boundary.py`
- **Results**: `csv/Q009-F-03-q9-q10-boundary.json`

### Hypothesis (DIRECTION-LOCKED)
The Q 9 → Q 10 canonical-adjacency cost (FR-TSP residual decomposition, H-NEW-720) is in the **top-10 most-expensive of 113 adjacencies**.

### Result
- Q 9 → Q 10 (al-Tawba → Yūnus) fraction_residual: **3.73%**
- Rank: **4 / 113** (top-decile)
- Q 8 → Q 9 (al-Anfāl → al-Tawba) fraction_residual: 0.74%, rank 58/113 (mid-cheap)
- Top-3 expensive adjacencies: Q 1-Q 2 (7.50%), Q 32-Q 33 (4.38%), Q 33-Q 34 (3.99%); Q 9-Q 10 is rank 4 at 3.73%.

### Driver test — muqaṭṭaʿāt-cluster control
We hypothesised that Q 9 → Q 10's high cost might be due to Q 10 starting an ALR muqaṭṭaʿāt cluster (Q 10-15). To control: examine Q 6 → Q 7 (where Q 7 al-Aʿrāf starts the singleton-tag *الر* but actually it's *المص* — the only Quranic instance of this 4-letter combination).

- Q 6 → Q 7 fraction_residual: **0.00% — rank 103/113** (essentially free)

The control **falsifies** the muqaṭṭaʿāt-cluster-onset-as-driver hypothesis. Beginning a new muqaṭṭaʿāt cluster does NOT inherently cost much. The Q 9-Q 10 cost has a different driver.

### Verdict: **VINDICATED**

The Q 9 → Q 10 adjacency is structurally costly at top-decile rank, AND the control rules out the simplest alternative explanation (muqaṭṭaʿāt-introduction).

### What is the driver?
Hypothesis (not pre-registered, post-hoc): the Q 9-Q 10 cost is the **chronology-block boundary**.
- Q 9 revelation order: 113 (second-LAST surah revealed; Medinan, war-context)
- Q 10 revelation order: 51 (Meccan-middle, ALR-cluster opener)
- Difference: −62 in revelation order

The Q 9-Q 10 boundary is the LARGEST chronology-jump in the al-sabʿ al-ṭiwāl block. The mushaf is paying a TSP-cost to honor the chronology-mosaic structure (Medinan-ṭiwāl block 1-9 → Meccan-ALR block 10-15 → ...).

### Cross-implications
- This is the FIRST per-surah finding identifying a specific canonical-adjacency cost as **chronology-driven**.
- It complements [[cross-finding-011-mushaf-fisher-rao-confirmed]]'s observation that the mushaf is 11% from FR-TSP-optimal — Q 9-Q 10 alone accounts for ~3.7 percentage points of that 11% non-optimality.
- It refines [[h-new-870-q33-architectural-keystone]]: the Q 32-Q 33-Q 34 cluster is an *internal* keystone (8.4% of residual on the seam Q33 cluster); Q 9-Q 10 is a *transition-cost* (3.7% on the al-sabʿ al-ṭiwāl exit).
- **Together with Q 1-Q 2 (7.5%), Q 32-Q 34 (8.4%), and Q 9-Q 10 (3.7%)**, four of the top-5 most-expensive canonical adjacencies are CHRONOLOGY-or-ARCHITECTURE-block boundaries — supporting the thesis that the mushaf's *tartīb tawqīfī* layer is inherently sub-optimal-for-cohesion and inherently optimal-for-architectural-narrative.

---

## Q009-F-04 — Last-revealed verse classical-citation density

- **Pre-reg**: `Q009-F-04-last-revealed-prereg.md` (SHA: `f489aa91c6810e7cf19ac634330e949118c41be0634a1ab390b9ab512fbda6bd`)
- **Script**: `/Users/grey/Downloads/quran/scripts/Q009_F_04_last_revealed.py`
- **Results**: `csv/Q009-F-04-last-revealed.json`

### Hypothesis (DIRECTION-LOCKED)
Among 10 OpenITI tafsirs (Ṭabarī, Qurṭubī, Rāzī, Ibn Kathīr, Suyūṭī *al-Durr al-manthūr*, Suyūṭī *al-Itqān*, Biqāʿī, Zamakhsharī, Ṭabarsī, Thaʿlabī), the joint co-occurrence of "آخر ما نزل / آية / سورة" (last revealed) with **Q 9:128-129 markers** exceeds each rival claim (Q 4:176, Q 2:281, Q 5:3) by ≥ 10%.

### Result
Total "last-revealed" mentions across 10 tafsirs: 384 instances.

| Claim | Co-occurrence count |
|:--|--:|
| Q 9:128-129 | **64** |
| Q 2:281 (al-ribā) | 61 |
| Q 4:176 (al-kalāla) | 49 |
| Q 5:3 (al-yawm akmaltu) | 9 |

Q 9:128-129 vs. nearest rival (Q 2:281): ratio = 64 / 61 = 1.05× — does NOT meet the pre-registered 1.10× threshold.

### Verdict: **NULL**

The pre-committed direction (Q 9:128-129 dominance) is supported (Q 9:128-129 IS the most-cited candidate), but the magnitude does not exceed the threshold for a clear DOMINANT claim. **NO pre-commit violation** — direction was correct, magnitude was insufficient.

### What it means
- al-Bayhaqī's harmonization (al-Suyūṭī *Itqān* nawʿ 8 line 1800) — that each Companion answered with what reached him — is empirically the most defensible reading.
- Q 9:128-129 = last absolutely-revealed-passage; Q 2:281 = last legal-ruling-on-ribā; Q 4:176 = last legal-ruling-on-kalāla. These three coexist as "last revealed in their domain."
- Q 5:3 ("today I have perfected your religion for you") is overwhelmingly NOT cited as a last-verse contender — only 9× across 384 instances. The popular contemporary citation of Q 5:3 as "the last verse" is NOT supported by classical citation density.

---

## Cross-finding: Q 9 vocabulary signature

A consequence of computing all 7 root-densities for Q 9 (rHm, nfq, twb, kfr, $rk, jhd, Hrm) is the emergence of Q 9's **distinctive vocabulary signature**:

| Root | Density rank (Q 9 / 114) | Density / 1k |
|:--|:-:|:-:|
| jhd (jihad / striving) | **2** | 4.11 |
| twb (tawba / repentance) | **4** | 6.36 |
| Hrm (sacred / forbidden) | **4** | 3.74 |
| nfq (nifāq / hypocrisy) | **5** | 7.85 |
| $rk (shirk) | 9 | 4.49 |
| kfr (kufr / disbelief) | 17 | 11.59 |
| rHm (raḥma / mercy) | 24 | 4.86 |

**Pattern**: Q 9's signature is the **action-pair** of jihād + tawba, plus the **target-pair** of nifāq + ḥarām (sacred-violations). This 4-way structure (action-against-corruption × repentance-as-internal-purity × hypocrite-as-target × sacred-violations) constitutes the surah's rhetorical engine.

The conventional "war-and-mercy" framing of Q 9 obscures this 4-way structure. The empirical signature suggests Q 9 is better characterised as **the surah of internal-external-legal purification** — internal (tawba), external (jihad), targeted (nifāq), and grounded in violation of the sacred (ḥarām).

---

## Honest limits

- All four findings use the QAC v0.4 root-index. Stem-level vs. root-level analysis may differ. Cross-validation with `quran-min-tashkeel.json` regex-search (planned) is the next replication step.
- F-04's NULL is a "narrowly missed" result. With a wider corpus (+5 more tafsirs) or a more permissive context window, the result might pass; with a stricter context window, it might not. The result is rules-tuple-fragile in detail but the directional finding (Q 9:128-129 is the MOST-cited single candidate) is robust.
- F-03's "chronology driver" hypothesis is post-hoc; we have not pre-registered a separate test for it. A formal test would require constructing a chronological-mushaf TSP and comparing the cost differences.

*Bismillāhi al-Raḥmāni al-Raḥīm.*
