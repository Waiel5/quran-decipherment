---
surah: 35
test_id: Q035-F-02
title: Corpus-uniqueness of the Q 35:32 3-fold hierarchy {ẓālim li-nafsih, muqtaṣid, sābiq bi-l-khayrāt}
file_type: pre-registration
date_locked: 2026-05-09
seed: 20260509
bonferroni_k: 2
bonferroni_family: Q035-F-02-3fold-hierarchy
alpha_bon: 0.025
---

# Q035-F-02 — Pre-registration: Q 35:32 3-fold hierarchy corpus-uniqueness test

## 1. Hypothesis (locked before observation)

**H1a (one-tailed, locked direction):** Q 35:32 is the **SOLE corpus location** where all three terms — *ẓālim li-nafsih* (or close substring *ظالم* + *لنفسه*), *muqtaṣid* (*مقتصد*), *sābiq* combined with *al-khayrāt* (*سابق* + *الخيرات*) — co-occur in a single verse.

**H1b (one-tailed, locked direction):** No other surah-level co-occurrence of all three terms exists in the corpus (i.e. the 3-tuple does not co-occur in any other surah even allowing inter-verse separation).

**H0 (joint):** there exists at least one OTHER verse OR surah in which all three terms appear together.

**Direction:** Q 35 is the corpus-UNIQUE location for the 3-tuple at the verse-level (H1a) and surah-level (H1b).

## 2. Operational definition

- **Source**: `quran-text/quran-no-tashkeel.json`.
- **Term 1**: *ẓālim* (root z-l-m, surface form ظالم) **AND** *li-nafsih* (لنفسه or نفسه) — the wronger-of-self.
- **Term 2**: *muqtaṣid* (مقتصد) — the moderate.
- **Term 3**: *sābiq* (سابق) **AND** *bi-l-khayrāt* (الخيرات) — the foremost.

## 3. Test statistic

- N_verse: number of corpus verses containing all three terms (1 = Q 35:32 expected).
- N_surah: number of corpus surahs containing all three terms (allowing inter-verse separation; 1 = Q 35 expected).

## 4. Permutation null

Not strictly needed for a counting test, but for rigor:
- Randomly relabel verse-locations of the 3 terms (preserving total counts) and check the probability of all 3 co-occurring in a single verse.
- Each term has a known total count in the corpus: count occurrences of each, distribute 10000 random permutations. 
- Compare expected vs observed verse-co-occurrence count.

For surah-level: randomly distribute the term occurrences across the 114 surahs (length-weighted) and compute the rate at which all 3 terms land in the same surah.

n_perm = 10000, seed = 20260509.

## 5. Success / Failure

- **CONFIRMED**: N_verse = 1 (only Q 35:32) AND N_surah = 1 (only Q 35).
- **DIRECTIONAL**: only one of H1a/H1b passes.
- **NULL**: N_verse > 1 OR N_surah > 1 with comparable matches elsewhere.

## 6. Honest limits known a priori

- **Pre-flight observation**: during pre-flight phrase-search at session start, I empirically confirmed Q 35:32 is the SOLE corpus verse with all three terms (1 surah out of 114, 1 verse out of 6,236). Per HANDOFF/04-DISCIPLINE.md "post-hoc-noticed protocol": this finding was observed BEFORE pre-reg lock; verdict ceiling = **PASS-DIRECTED** until INDEPENDENT REPLICATION on a distinct data dimension.
- **Independent replication question**: does the 3-tuple uniqueness hold under different orthographic conventions (Uthmani-consonantal? Maghribī)? Under different morphological resolutions (e.g., looking only at root-level rather than surface form)?
- **Alternative roots**: there are partial matches elsewhere — Q 5:66 has *muqtaṣid* alone, Q 31:32 has *muqtaṣid* alone, Q 23:61 has *yusāriʿūn fī al-khayrāt* (similar verbal form). But the FULL 3-tuple (all three terms together) is corpus-unique to Q 35:32. The verdict is on the FULL 3-tuple co-occurrence.
- **Term-form variance**: *ẓālim li-nafsih* is the surface-form pattern. The PHRASE *ẓālim li-nafsih* is also corpus-unique (verified — search for that combined string).
- **PROMOTION threshold**: if N_verse = 1 AND the closest competing verse has at most 1/3 of the terms, the verdict is robust to alternative operationalizations.

## 7. Rules-tuple

`(no-tashkeel, orthographic-token, regex-substring, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)`.

## 8. Bonferroni

k = 2 (H1a verse-level + H1b surah-level). α_bon = 0.025.

## 9. Coordination

- This is a Q 35-specific 3-fold hierarchy test. No other specialist has tested this.
- Companion test Q 56 al-Wāqiʿah's 3-fold judgment-day classification (*sābiqūn / aṣḥāb al-yamīn / aṣḥāb al-shimāl*) is THEMATICALLY parallel but uses DIFFERENT vocabulary; not in scope here.

## 10. SHA256 lock

Computed at write-time, embedded into `scripts/Q035_F_02_3fold_hierarchy.py`, verified at runtime.
