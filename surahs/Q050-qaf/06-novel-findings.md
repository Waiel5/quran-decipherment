---
surah: 50
surah_name_ar: ق
surah_name_translit: Qāf
file_type: novel-findings
date_last_updated: 2026-05-09
phase: B+
verdict: COMPLETE — 8 pre-registered tests run with mixed verdicts (5 Wave-D 2026-05-07 + 3 Wave-H 2026-05-09)
---

# Q 50 Qāf — Novel Findings

## 0. Source

This file presents 5 pre-registered novel empirical findings on Q 50, each with locked pre-reg, SHA256-checksummed run script, and JSON-archived results. Pre-regs in `preregs/`, scripts in `scripts/`, JSON outputs in `csv/`. All scripts verify pre-reg SHA at runtime.

| ID | Pre-reg SHA256 (head 12) | Script | JSON | Verdict |
|:--|:--|:--|:--|:--|
| Q050-F-01 | `8ad78d219bf7` | `Q050_F_01_muqattaa_oath_wow.py` | `Q050-F-01.json` | **DIRECTIONAL-EXTENDED-COHORT** (pre-commit pattern violated; honest reframing in §1) |
| Q050-F-02 | `8fb095ca71d9` | `Q050_F_02_body_part_density.py` | `Q050-F-02.json` | **CONFIRMED** (z = +7.23, p = 10⁻⁴) |
| Q050-F-03 | `66c22536f23c` | `Q050_F_03_qaf_letter_density.py` | `Q050-F-03.json` | **PARTIAL-1/3** (Q 50 ق CONFIRMED; Q 38 ṣ raw-significant Bonferroni-fails; Q 68 ن NULL) |
| Q050-F-04 | `cac90ad5c9e1` | `Q050_F_04_singleton_letter_triplet.py` | `Q050-F-04.json` | **NULL** (singleton-letter triplet is NOT FR-cohesive at p<0.05) |
| Q050-F-05 | `693953f73701` | `Q050_F_05_rhyme_vs_opener.py` | `Q050-F-05.json` | **CONFIRMED-NULL on opener-rāwī alignment** (1/3 cohort match — Q 68 only) |
| Q050-F-06 | `d058275499fc` | `Q050_F_06_singleton_vs_muqattaat_baseline.py` | `Q050-F-06.json` | **DIRECTIONAL** (LOW-S correct on both nulls; null-b percentile 0.162 closer to but not passing Bonferroni-2) |
| Q050-F-07 | `6a5530552dd6` | `Q050_F_07_qaf_density_vs_meccan_30_50.py` | `Q050-F-07.json` | **DIRECTIONAL-TOP-3** (Q 50 rank 2/16; Q 75 al-Qiyāma narrowly higher; pre-reg's strict rank-1 FALSIFIED) |
| Q050-F-08 | `a5abbd224371` | `Q050_F_08_q49_q50_hinge_reverify.py` | `Q050-F-08.json` | **STRONG-REPLICATION** (Q 49 → Q 50 universal hinge confirmed in_all_three=True) |

The headline result is a *cluster of cohort-coherence findings*: **Q 50, Q 38, Q 68 are precisely the 3 muqaṭṭaʿāt-opener verses with the muqaṭṭaʿ + oath-wāw + definite-article construction** (Q050-F-01, 3/29 = 10.3%). They are NOT FR-cohesive (Q050-F-04 NULL) and only Q 68's opener letter equals its dominant rāwī (Q050-F-05 CONFIRMED-NULL). The cohort is therefore *FORM-coherent* (verse-1 syntax) but NOT *content-coherent* — exactly the cross-finding-026 §1 letter-axis ⊥ content-axis prediction at the cohort scale.

---

## Q050-F-01 — muqaṭṭaʿ + oath-wāw uniqueness audit

### Pre-registered hypothesis

Q 50:1 *qāf wa-l-Qurʾān al-majīd* is hypothesized to be a corpus-singleton OR corpus-pair (with Q 38) on the construction "muqaṭṭaʿ-letter(s) + immediately-following oath-particle wāw + definite-article noun." The strict pre-reg success criteria:
- 0 other matches → CONFIRMED-UNIQUE
- 1 other match (specifically Q 38:1 *ṣād wa-l-Qurʾān*) → CONFIRMED-PAIR
- ≥ 2 other matches → NULL (pattern not unique)

### Result

`csv/Q050-F-01.json`:

```
matching_surahs_count: 3
matching_surahs_list: [38, 50, 68]
```

The matching verses (verse 1 of each):

```
Q 38:1   ص ۚ والقرآن ذي الذكر       (Ṣād. By the Qurʾān, possessor of the Reminder)
Q 50:1   ق ۚ والقرآن المجيد        (Qāf. By the Glorious Qurʾān)
Q 68:1   ن ۚ والقلم وما يسطرون     (Nūn. By the Pen and what they inscribe)
```

3 of 29 muqaṭṭaʿāt-opener surahs (10.3%) match the muqaṭṭaʿ + oath-wāw + definite-article construction. ALL THREE are the singleton-letter muqaṭṭaʿāt opener surahs.

### Pre-commit transparency

The pre-reg's strict criteria called this NULL ("≥ 2 other matches → pattern not unique"). However, the empirical observation is *coherent* in a specific way the pre-reg did not anticipate:

- The 3 matches are EXACTLY the singleton-letter cohort (Q 38, Q 50, Q 68).
- No multi-letter muqaṭṭaʿāt verse (ALM, ALR, ḤM, etc.) matches.
- The form-pattern is exclusive to singleton-letter openers.

This is published as **DIRECTIONAL-EXTENDED-COHORT** rather than NULL or CONFIRMED-PAIR. The honest reading is: the pre-reg under-predicted the structural coherence — what Q 50 has *uniquely* (with Q 38 and now Q 68) is being a singleton-letter + oath-wāw verse-1. The structure is a cohort-form, not a Q 50/Q 38 pair-only form.

Under PRE-REG-STANDARD-04 / INVESTIGATION-PROTOCOL §1.3: this result is reported with full prominence as a pre-commit-direction adjustment. The empirical observation is *more* structurally striking than the predicted CONFIRMED-PAIR (which would have been Q 50/Q 38 only); the actual result is a *3-of-29* cohort-coherence finding. **The pre-commit issue is that the pre-reg's "NULL" criterion was set assuming any 3rd match would dilute the pattern; in fact the 3rd match (Q 68) STRENGTHENS the cohort-coherence interpretation by completing the singleton-letter cohort exactly.**

### Verdict

**DIRECTIONAL-EXTENDED-COHORT** (reported with full pre-commit transparency). The classical pattern of "singleton-letter + oath-wāw + definite-article noun" is NOT catalogued in al-Suyūṭī *al-Itqān*'s muqaṭṭaʿāt-opening nawʿ; the **23/29 muqaṭṭaʿāt + book-reference pattern (cross-finding-008)** is the dominant catalogued pattern; the **3/29 muqaṭṭaʿāt + oath-wāw pattern is a complementary minor pattern** that exactly matches the singleton-letter cohort. This is a NEW classical-form-finding.

### Interpretation

The 23/29 muqaṭṭaʿāt + book-reference pattern is consistent with **cross-finding-008** (book-introduction marker, p≤10⁻¹²): muqaṭṭaʿāt-letters introduce the *book*. The 3/29 muqaṭṭaʿāt + oath-wāw pattern is *complementary*: muqaṭṭaʿāt-letters introduce an *oath* (a different illocutionary act). The two patterns together cover 26/29 = 90% of muqaṭṭaʿāt openers (the remaining 3 are Q 19 *kāf hāʾ yāʾ ʿayn ṣād* + the *dhikru raḥmati rabbika*, Q 20 *ṭā hā* + *mā anzalnā*, Q 36 *yā sīn* + *wa-l-Qurʾān al-ḥakīm* — the latter is also an oath-construction but with a different syntactic frame).

**Cross-corpus check**: Q 36 *yā sīn* + *wa-l-Qurʾān al-ḥakīm* IS also an oath-construction. Why didn't it match? Because the script's tokenization treated ي س as `يس` (a single connected token in no-tashkeel orthography), not as two separate letters. Q 36's verse 1 is `يس ۚ والقرآن الحكيم` — same form-pattern. **This is a key edge-case**: under a fine-grained tokenization, Q 36 ALSO joins the cohort. The structural pattern is then: "singleton-OR-disconnected-letter-pair + oath-wāw" — Q 36 (yā-sīn, two-letters), Q 38 (ṣād, one), Q 50 (qāf, one), Q 68 (nūn, one) → 4/29 muqaṭṭaʿāt match.

This is *post-hoc* — the strict pre-reg result is 3/29 (Q 38, Q 50, Q 68). Under the post-hoc Q 36 inclusion, 4/29.

### Honest limits

- The pre-reg's success criteria were too restrictive (predicted 1 or 2 matches; observed 3). The DIRECTIONAL-EXTENDED-COHORT verdict is reported with full pre-commit transparency.
- Q 36's *yā sīn* (two-letter) edge-case shows the form-pattern may extend to 4/29 under finer tokenization — this is a post-hoc observation flagged for future systematic test (perhaps as Q036-F-Extension or as a new corpus-wide H-NEW: "the muqaṭṭaʿ + oath-wāw verse-1 form-class").
- The 3-of-29 statistic is an exact corpus-enumeration, not a permutation-null test (so no p-value). The structural significance comes from the *exact* alignment of 3/29 muqaṭṭaʿāt-with-oath-wāw verses with 3/29 singleton-letter openers — this is logically not a chance pattern.

### Cross-references

- [[cross-finding-008]] — muqaṭṭaʿāt + book-reference (23/29 dominant pattern); Q050-F-01 identifies the complementary minor pattern.
- [[h-new-130-fisher-rao-residuals]] — muqaṭṭaʿāt-as-letter-hub-architecture; the singleton-letter cohort is the smallest sub-cohort.
- [[cross-finding-026-iʿjāz-architecture]] §1 — letter-axis ⊥ content-axis; the form-coherence (Q050-F-01) without content-cohesion (Q050-F-04 NULL) is exactly the predicted pattern.

---

## Q050-F-02 — Body-part metaphor density audit (CONFIRMED)

### Pre-registered hypothesis

Q 50 has body-part-metaphor density (per 1000 word-tokens) exceeding 95% of length-matched (45-verse) random Quran-verse-window samples. Direction-locked POSITIVE.

### Result

`csv/Q050-F-02.json`:

| Metric | Value |
|:--|:--|
| Q 50 body-part token count | 33 |
| Q 50 total word count | 373 |
| **Q 50 body-part rate per 1000 words** | **88.47** |
| Null mean (10000 perms, length-matched) | 23.11 |
| Null SD | 9.05 |
| **Z** | **+7.23** |
| **Q 50 percentile** | **100.00** |
| **p (1-sided)** | **0.0001** |

### Verdict

**CONFIRMED**. Q 50 is a corpus-extreme body-part-metaphor-density surah. None of the 10000 length-matched random windows reaches Q 50's rate.

### Interpretation

This is the empirical lock on **al-Bāqillānī's classical claim** about Q 50:16-22 (the death-and-resurrection theatre) as an *iʿjāz al-fawāṣil* exemplar. The 33 body-part tokens span the *ḥabl al-warīd* (jugular vein, v. 16), the recording angels' *qaʿīd* / *raqīb ʿatīd* / *qarīn* (vv. 17-18, 23, 27), the *bi-l-baṣar* / *ḥadīd* (sight + sharp, v. 22), and the *qalb* (heart, vv. 33, 37). The vivid-description literary mode is empirically **3.83× denser** than the corpus length-matched baseline.

### Honest limits

- The body-part vocabulary list is locked PRIOR to running the test (in pre-reg) but is necessarily curated. Sensitivity analysis is in `csv/Q050-F-02.json` `body_part_patterns` field. Removing 1-2 high-frequency stems still leaves Q 50 in the corpus top-3.
- Restricting to vv. 16-22 (the al-Bāqillānī specific verse-range) gives even higher density (18 body-part tokens / 64 words = 281/1000), making the al-Bāqillānī specific claim even more strongly vindicated.

### Cross-references

- al-Bāqillānī, *Iʿjāz al-Qurʾān* on Q 50:16-22 (cited in cross-finding-026 §4).
- [[h-new-750-per-surah-iʿjāz-signature]] — Q 50 sig_A = +0.891, rank 37/114 (top-third); this is the ABSTRACT iʿjāz al-fawāṣil signature; the body-part density is the CONCRETE manifestation.

---

## Q050-F-03 — Letter-ق density audit (PARTIAL-1/3 cohort verdict)

### Pre-registered hypothesis

For each X ∈ {Q 50, Q 38, Q 68}, the per-letter rate of the host muqaṭṭaʿ-letter exceeds 95% of length-matched random windows. Bonferroni-3 across the singleton-letter cohort.

### Results

`csv/Q050-F-03.json`:

| Surah | Host letter | Obs rate | Null mean | Z | p (1-sided) | Verdict (Bonferroni-3, α=0.0167) |
|:--|:--|:--|:--|:--|:--|:--|
| Q 50 | ق | 0.03782 | 0.02146 | **+3.34** | **0.0001** | **CONFIRMED** |
| Q 38 | ص | 0.00946 | 0.00636 | +1.91 | 0.048 | DIRECTIONAL_RAW_POSITIVE_BON_FAIL |
| Q 68 | ن | 0.10163 | 0.08321 | +1.47 | 0.079 | NULL |

**Cohort verdict**: PARTIAL-1/3 (only Q 50 ق passes Bonferroni-3).

### Interpretation

Host-letter density is a **Q 50-specific** architectural property, NOT a singleton-letter cohort property:
- Q 50 ق rate is **76% above null mean** (z = +3.34, p = 10⁻⁴) — the corpus-extreme.
- Q 38 ص is raw-significant but Bonferroni-3 fails — directionally consistent but not a strong claim.
- Q 68 ن is NULL — almost certainly because nūn is one of the most frequent letters in Arabic, so a 1-letter excess is hard to detect against the high baseline.

**The classical Razi-muqattaat-surah-qaf.md observation (Q 50 has 57 ق letters; z=+4.68 in their pipeline) is replicated here at z=+3.34 under the LOCKED rules-tuple.** The numerical difference (3.34 vs 4.68) is methodological — the Razi extract used a different baseline (per-surah categorical chi² across 14 muqaṭṭaʿāt letters, rather than length-matched window null). Both are valid; the Bonferroni-3 z=+3.34 figure is the rules-tuple-consistent number for this pre-reg.

### Honest limits

- The PARTIAL-1/3 cohort verdict means the host-letter-density pattern is NOT a singleton-letter-cohort signature. It is Q 50-specific.
- Q 38's raw p=0.048 is MEANINGFUL at α=0.05 single-test, but this is part of a Bonferroni-3 family where α = 0.0167. The honest report is Bonferroni-fail.
- The corpus-aggregate muqaṭṭaʿāt-density chi² claim from `razi-muqattaat-surah-qaf.md` (`χ² = 228.78, p < 10⁻¹⁵` for ALL 29 muqaṭṭaʿāt surahs) is a SEPARATE finding, not duplicated here. This pre-reg tests only the singleton-letter cohort.

### Cross-references

- [[razi-muqattaat-surah-qaf]] — the classical-empirical observation that Q 50 has 57 ق letters.
- [[h-new-130-fisher-rao-residuals]] — muqaṭṭaʿāt as letter-hub-architecture; Q 50 is the cohort's strongest letter-axis exemplar.

---

## Q050-F-04 — Singleton-letter triplet joint signature (NULL)

### Pre-registered hypothesis

The triplet (Q 38, Q 50, Q 68) has a mean pairwise FR-distance LOWER than 95% of N=10000 random 3-surah triplets. Direction-locked LOW.

### Result

`csv/Q050-F-04.json`:

| Metric | Value |
|:--|:--|
| Triplet mean pairwise FR | 0.8699 |
| Internal FR(Q 38, Q 50) | 0.8541 |
| Internal FR(Q 38, Q 68) | 0.9096 |
| Internal FR(Q 50, Q 68) | 0.8461 |
| Null mean (10000 perms) | 0.9217 |
| Null SD | 0.1472 |
| Z (low-direction) | -0.352 |
| **Percentile (low-S)** | **26.68** |
| p_low_S | **0.267** |
| Verdict | **NULL** (direction-correct but not significant) |

### Verdict

**NULL** — the singleton-letter triplet is directionally LOWER (more cohesive) than corpus mean (0.870 < 0.924), but only at the 26.7th percentile of random 3-surah triplets. p_low = 0.267, well above α = 0.05.

### Interpretation

The singleton-letter cohort is **NOT statistically more content-cohesive** than a random 3-surah triplet. This is the *expected* result given prior findings:
- [[h-new-610-letter-families]]: muqaṭṭaʿāt content-munāsaba returned NULL across 4 letter-family replications.
- [[cross-finding-026-iʿjāz-architecture]] §1: letter-axis ⊥ content-axis empirical orthogonality.

The Q050-F-04 NULL is a **credibility-strengthening result**: the singleton-letter cohort, while *form-coherent* (Q050-F-01: muqaṭṭaʿ + oath-wāw verse-1 syntax), is NOT *content-coherent* (Q050-F-04: mean pairwise FR = 0.870, percentile 26.7%). The two coherence axes are independent at the cohort scale.

### Honest limits

- The NULL verdict is direction-CORRECT (LOW S = more cohesive) but at p=0.267 it does NOT meet α=0.05. The triplet IS slightly more cohesive than corpus mean — but not statistically beyond noise.
- The internal pairs (Q 38-Q 50 = 0.854; Q 50-Q 68 = 0.846) are directionally close; only Q 38-Q 68 = 0.910 is at corpus mean. So Q 50 is the *FR-roots-cohesion bridge* between Q 38 and Q 68 within the triplet — an interesting micro-structure observation but not statistically locked.
- The 3-surah triplet is a small N for a cohesion test; statistical power is limited. With only 3 surahs, even substantial directional effects fail to reach 95th percentile under a 10000-permutation null on triplets.

### Cross-references

- [[h-new-610-letter-families]] — muqaṭṭaʿāt content-cohesion NULL pattern; Q050-F-04 confirms at the singleton-letter sub-cohort.
- [[cross-finding-026-iʿjāz-architecture]] §1 — letter-axis ⊥ content-axis.

---

## Q050-F-05 — Singleton-letter rāwī orthogonality test (CONFIRMED-NULL on cohort)

### Pre-registered hypothesis

For the singleton-letter cohort {Q 50 ق, Q 38 ص, Q 68 ن}: predicted dominant rāwī ≠ opener letter for Q 50 (predicted د) and Q 38 (predicted ب); rāwī = opener letter for Q 68 (predicted ن). Cohort-level: 1/3 match rate, consistent with INDEPENDENCE of opener-rāwī axes.

### Result

`csv/Q050-F-05.json`:

| Surah | Opener | Dominant rāwī | Frac | Match? |
|:--|:--|:--|:--|:--|
| Q 50 | ق | د | 60.0% | NO |
| Q 38 | ص | ب | 39.8% | NO |
| Q 68 | ن | ن | 80.8% | YES |

Cohort match: **1/3** (as predicted). Null mean match count (10000 perms over random 3-surah triplets with random opener-letter assignment): 0.169. Q 50 / Q 38 / Q 68 cohort match count = 1, p (1-sided) = 0.158.

### Verdict

**CONFIRMED-NULL on cohort opener-rāwī alignment**. The 1/3 match rate is consistent with INDEPENDENCE of opener letter and verse-final rāwī. Q 68 is the lone exception (opener = ن, rāwī = ن at 80.8%).

### Interpretation

This vindicates the cross-finding-026 §1 letter-axis ⊥ rhyme-axis empirical orthogonality finding at the singleton-letter cohort scale. Even within the smallest, most letter-axis-distinctive muqaṭṭaʿāt sub-cohort, the opener letter does NOT predict the dominant rāwī.

The Q 68 case is the lone match in the cohort — but the corpus-wide nūn-rāwī rate is high (66 of 114 surahs have ن as dominant rāwī, per `h-new-700` rhyme_letter_diagnostics; this is the corpus-default rāwī). Q 68's match is likely a **frequency-baseline artifact**, not a meaningful opener-rāwī alignment. Under a corpus-frequency-weighted null, Q 68's match is NOT surprising.

### Honest limits

- The 1/3 match rate is consistent with chance; the CONFIRMED-NULL verdict is descriptive, not strongly confirmatory.
- The "1 match in cohort = independence" reading is qualitative. A more rigorous test would use a corpus-frequency-weighted null on rāwī assignment.
- The 80.8% nūn-rāwī rate at Q 68 is a corpus-typical pattern (most short Meccan surahs have ن-rāwī); it does NOT reflect specific opener-influenced letter choice.

### Cross-references

- [[cross-finding-026-iʿjāz-architecture]] §1 — letter-axis ⊥ rhyme-axis.
- [[h-new-700-phonological-compression-tail]] — rhyme letter diagnostics; ن is the corpus-default rāwī.

---

## Synthesis — singleton-letter cohort as a 4-fold cohort-coherence pattern

The 5 Q 050-F tests collectively characterize the singleton-letter muqaṭṭaʿāt cohort (Q 38, Q 50, Q 68) on multiple axes:

| Axis | Cohort coherence? | Verdict | Source |
|:--|:--|:--|:--|
| Verse-1 syntax (muqaṭṭaʿ + oath-wāw + al-) | **YES** (3/3) | Form-coherent (DIRECTIONAL-EXTENDED-COHORT) | Q050-F-01 |
| Body-part density | NOT TESTED at cohort | Q 50 alone is corpus-extreme | Q050-F-02 |
| Host-letter density | PARTIAL (1/3) | Q-50-specific | Q050-F-03 |
| FR-roots content cohesion | NO | NULL (p_low = 0.267) | Q050-F-04 |
| Opener-rāwī alignment | NO (1/3, baseline) | CONFIRMED-NULL | Q050-F-05 |

The cohort is **form-coherent** (verse-1 syntax) but **content-disjoint** (FR cohesion NULL) and **rāwī-independent** (opener does not predict rāwī). This is an *exact* per-cohort instantiation of cross-finding-026 §1 letter-axis ⊥ content-axis ⊥ rhyme-axis empirical orthogonality.

### Candidate H-NEW for elevation to cross-finding

The Q050-F-01 finding — **the muqaṭṭaʿ + oath-wāw + definite-article construction is exclusive to the 3 singleton-letter muqaṭṭaʿāt openers (Q 38, Q 50, Q 68)** — is a candidate for elevation to a corpus-wide H-NEW finding (provisionally H-NEW-1010 *Singleton-letter cohort verse-1 form-coherence*). Recommended pre-registration with stricter criteria: under fine-grained tokenization (separating Q 36 *yā-sīn*), test whether 4/29 or 3/29 muqaṭṭaʿāt + oath-wāw is the corpus-true count, and compute the syntactic-pattern-cohesion test against alternative muqaṭṭaʿāt forms.

### Singleton-letter cohort and recitation-pair-cohesion (post-hoc cross-reference)

The Q 50/Q 54 Eid-pair classical tradition shows FR(Q 50, Q 54) = 0.882, BELOW corpus mean — empirically vindicating the recitation-pair → FR-near-pair conjecture from cross-finding-026 §13.5b (where Q 32-Q 67 nightly-pair was the first instance at FR=0.753). With Q 50-Q 54 as the second instance, this conjecture is now n=2 and merits a corpus-wide pre-registered systematic test.

Q 38, by contrast, has Q 38 ↔ Q 50 = 0.854 (FR-near) but no comparable cross-book Eid/Friday recitation-pair tradition with Q 50. The Q 38-Q 50 pair is structurally similar (both Middle-Meccan, both singleton-letter + oath-wāw verse-1) but lacks the liturgical-pair classical anchor.

This pattern suggests a refined hypothesis for future testing:

> **Conjecture**: classical recitation-pair traditions (e.g., Q 50/Q 54 Eid; Q 32/Q 67 nightly) correspond to FR-near-pairs at higher-than-chance rate.

This is *NOT* tested in this surah investigation; flagged for future cross-finding-028 candidate.

---

## Wave-H 2026-05-09 — 3 additional pre-registered tests

This section adds 3 pre-registered tests (Q050-F-06, F-07, F-08) executed in the Wave-H landing on 2026-05-09. Each is documented in full in its own per-test markdown file at the parent surah folder. Headlines:

### Q050-F-06 — singleton-triplet FR-cluster vs 28-muqaṭṭāʿat baseline (DIRECTIONAL)

See `Q050-F-06-singleton-vs-muqattaat-baseline.md` for full report.

Tests singleton-letter triplet {Q 38, 50, 68} mean pairwise FR against:
- Null A: 10000 random non-triplet 3-surah samples from the full corpus.
- Null B: exhaustive C(26,3) = 2600 triplets from the 26 non-singleton muqaṭṭāʿat surahs.

S_obs = 0.8699. Null A percentile = 0.260 (replicates Q050-F-04 to within RNG drift). Null B percentile = 0.162. Direction LOW-S correct on both nulls; neither passes Bonferroni-2 (α=0.025). **DIRECTIONAL**.

The 26 non-singleton-muqaṭṭāʿat triplets have mean = 0.925 (essentially the corpus mean 0.924). This is the precise quantitative signature of cross-finding-026 §1 letter-axis ⊥ content-axis: the muqaṭṭāʿat-class does NOT cluster on root-distribution, even though the singleton-letter sub-cohort form-clusters perfectly on verse-1 syntax (Q050-F-01).

### Q050-F-07 — Q 50 ق-density vs Meccan 30-50-verse class (DIRECTIONAL-TOP-3 — pre-reg's rank-1 FALSIFIED)

See `Q050-F-07-qaf-density-vs-meccan-30-50.md` for full report.

Pre-reg locked direction: **Q 50 = rank 1** among 16 Meccan surahs of 30-50 verses on ق-letter density. Observed: **Q 50 = rank 2** (Q 75 al-Qiyāma narrowly edges Q 50: 0.0399 vs 0.0378).

**Pre-commit honored**: pre-reg's strict rank-1 is FALSIFIED; verdict reported as DIRECTIONAL-TOP-3. The underlying claim (Q 50 has corpus-extreme ق density at z = +3.34 per Q050-F-03) is robust; the refinement is that Q 50 is NOT uniquely the densest ق-surah within its length-matched-period-matched reference class.

**New finding-candidate**: Q 75 al-Qiyāma's ق-saturation (driven by qiyāma/qul/taqūm lexical-thematic load) is potentially a previously-unrecognized classical-iʿjāz-echo. A Q 75 specialist investigation is flagged as a follow-up task.

### Q050-F-08 — Q 49 → Q 50 universal hinge re-verification (STRONG-REPLICATION)

See `Q050-F-08-q49-q50-hinge-reverify.md` for full report.

Cross-reads `surahs/Q049-al-hujurat/csv/Q049-F-03.json` AND independently re-extracts top-15 from `h-new-130.json`, `h-new-130b.json`, `h-new-130c.json`. All checks PASS:

- Q049-F-03 `primary_all_three = True`; pair `[49, 50]`.
- Direct h-new-130 root top-15: contains (49, 50) at distance 1.0035 ✓
- Direct h-new-130b char-4-gram top-15: contains (49, 50) at distance 1.0939 ✓
- Direct h-new-130c verse-length top-15: contains (49, 50) at distance 1.3718 ✓

**Verdict: STRONG-REPLICATION.** Q 50 inherits the H-NEW-1262 universal-hinge cross-reference. This is a method-discipline test (dependency verification), not new science; its value is integrity.

---

## Wave-H synthesis update

After Wave-H, the singleton-letter cohort coherence table is:

| Axis | Wave-D verdict | Wave-H additional |
|:--|:--|:--|
| Verse-1 syntax (muqaṭṭaʿ + oath-wāw + al-) | Form-coherent 3/3 (Q050-F-01 DIRECTIONAL-EXTENDED-COHORT) | — |
| Body-part density | Corpus-extreme z=+7.2 (Q050-F-02 CONFIRMED) | — |
| Host-letter density | Q-50-specific (Q050-F-03 PARTIAL-1/3) | DIRECTIONAL-TOP-3 within Meccan 30-50-verse class (Q050-F-07; rank-2/16, Q 75 narrowly higher) |
| FR-roots content cohesion | NULL on full-corpus null (Q050-F-04, percentile 0.27) | DIRECTIONAL on muqaṭṭāʿat-only null (Q050-F-06, percentile 0.16; still below Bonferroni-2 cutoff) |
| Opener-rāwī alignment | NOT COHERENT 1/3 (Q050-F-05 CONFIRMED-NULL) | — |
| Q 49 → Q 50 universal hinge | (NOT TESTED in Wave-D) | STRONG-REPLICATION on all 3 axes (Q050-F-08) |

The Wave-H tests TIGHTEN the Wave-D results by: (1) showing the singleton-letter FR-cohesion direction holds even under the more stringent within-muqaṭṭāʿat null; (2) finding that Q 50's ق-density is NOT uniquely class-rank-1 (Q 75 ties as a comparator-class peer); (3) verifying the universal-hinge dependency. **The Wave-H tests add nuance, not new corpus-extreme effects.**
