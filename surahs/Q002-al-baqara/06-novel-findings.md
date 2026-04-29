---
surah: 2
surah_name_ar: البقرة
surah_name_translit: al-Baqara
file_type: novel-findings
date_last_updated: 2026-04-28
phase: B+
verdict: 5 pre-registered novel tests run; 1 VINDICATED, 1 DIRECTIONAL, 1 RULES-TUPLE-FRAGILE, 2 NULL.
---

# Q 2 al-Baqara — Novel Findings

This file logs novel investigations on Q 2 — patterns or signatures NOT explicitly highlighted in classical scholarship, OR refinements that go beyond the classical claim. Every test in this file was pre-registered before run; pre-reg files are SHA256-locked.

---

## Q002-F-01: Āyat al-Kursī divine-name-density rank

- Pre-reg: `Q002-F-01-ayat-al-kursi-divine-name-density-prereg.md` (SHA `e395b9bb...d679b2c`)
- Findings: `Q002-F-01-ayat-al-kursi-divine-name-density.md`
- JSON: `csv/Q002-F-01.json`

**Result**: NULL on density (rank 563/6236), VINDICATED on absolute count (rank 5/6236, distinct names rank 3/6236) — RULES-TUPLE-FRAGILE.

**Top finding**: Q 2:255 sits in a triumvirate with Q 59:23 and Q 59:24 as the corpus's three apex-density verses for asmāʾ al-ḥusnā by absolute distinct-name count.

---

## Q002-F-02: Khawātim al-Baqara 3-verse divine-name-density rank

- Pre-reg: `Q002-F-02-khawatim-baqara-divine-name-density-prereg.md` (SHA `3be0c7c6...35fa8bd`)
- Findings: `Q002-F-02-khawatim-baqara.md`
- JSON: `csv/Q002-F-02.json`

**Result**: NULL — rank 2839/6008 by total density and 3052 by distinct density. Hadith claim "kafatāhu" does NOT have a divine-name-density empirical correlate.

**Comparator (rank 2/6008)**: Q 59:22-24 retains its position as the highest-density 3-verse window per [[h-new-95]].

---

## Q002-F-03: Q 2 gravitational centrality / leave-one-out shift

- Pre-reg: `Q002-F-03-q2-centrality-test-prereg.md` (SHA `8d808886...b53d97`)
- Findings: `Q002-F-03-centrality.md`
- JSON: `csv/Q002-F-03.json`

**Result**: DIRECTIONAL. Q 2 is rank 6/114 by leave-one-out shift (just outside pre-committed top-5), but rank 103/114 by gravitational pull (LOW pull) and rank 104 by mean-distance (HIGH mean distance).

**Top finding**: The empirical medoid of the FR root distribution is **Q 112 al-Ikhlāṣ** (mean dist 0.759). Q 2 is a SCAFFOLD-AS-OUTLIER (rank-1 cohesion-anchor) rather than a SCAFFOLD-AS-CENTROID — refining al-Biqāʿī's intuition. Q 1 sits 4th-closest to centroid.

---

## Q002-F-04: Q 2 ring-structure detection (verse-token-level)

- Pre-reg: `Q002-F-04-ring-structure-prereg.md` (SHA `3eca733a...44ef44127`)
- Findings: `Q002-F-04-ring-structure.md`
- JSON: `csv/Q002-F-04.json`

**Result**: NULL — RESOLUTION-LIMITED. Verse-pair p = 0.93 (z = −1.45, mildly anti-ring), block-pair p = 0.61, Q 3 control p = 0.83. Verse-token-level chiastic mirroring is NOT empirically present. The thematic-ring claim (Farrin 2010, Cuypers 2015) survives because it operates at semantic-content level not lexical level.

---

## Q002-F-05: Q 2:282 (āyat al-dayn) length-extremity

- Pre-reg: `Q002-F-05-q2-282-longest-verse-prereg.md` (SHA `fb544168...3d60c817a`)
- Findings: `Q002-F-05-q2-282-length.md`
- JSON: `csv/Q002-F-05.json`

**Result**: VINDICATED. Q 2:282 is rank 1/6236 by both word count AND letter count, z = +12.31, gap-to-second-longest = 4.33σ. The classical observation that 2:282 is "the longest verse" is empirically locked at maximum strength.

**Top-5 longest verses are all LEGAL/PROCEDURAL**: Q 2:282 (debt-contract), Q 4:12 (inheritance), Q 73:20 (night-prayer easing), Q 24:31 (modesty), Q 24:61 (hospitality). This empirically supports the al-sabʿ al-ṭiwāl content-class hypothesis.

---

## Other empirical observations (not pre-registered as separate tests)

These are descriptive-empirical findings drawn from Q 2 analysis. They are NOT inference tests; they are catalogue entries.

### Per-block content cohesion (8-block scheme from §00-overview)

Computed via `Q002_C_audit_helpers.py`:

| Block | Verses | Internal mean-cos | Mean-cos to other blocks |
|:--|:--|:--|:--|
| A (opening + Adam) | 1-39 | 0.0679 | 0.2308 |
| B (Banū Isrāʾīl) | 40-103 | 0.0951 | 0.2300 |
| C (Abrahamic + qibla) | 104-141 | 0.0892 | 0.2492 |
| D (qibla-change + ritual) | 142-176 | 0.0963 | 0.2335 |
| E (legal core) | 177-242 | **0.1120** (highest) | 0.2040 |
| F (faith narratives) | 243-260 | 0.1094 | 0.2185 |
| G (charity + ribā + debt) | 261-283 | 0.1117 | 0.2033 |
| H (khawātim) | 284-286 | 0.0883 | **0.1720** (lowest) |

**Observations**:
- **Block E (vv. 177-242, communal-legal)** has the highest internal cohesion (0.112) — legal verses cluster tightly.
- **Block A (vv. 1-39, opening)** has the lowest internal cohesion (0.068) — deliberately heterogeneous opening.
- **Block H (vv. 284-286, khawātim)** has the lowest mean-cos to other blocks (0.172) — distinctive closural function.
- **Block C (vv. 104-141, Abrahamic + qibla setup)** has the highest mean-cos to other blocks (0.249) — most "connected" to the rest, consistent with its bridge-function between Banū Isrāʾīl narrative and qibla-change.

### Q 2 vocabulary distinctness

- Q 2 unique surface-form vocabulary: **2,279** word forms.
- Corpus vocabulary: 14,870 unique forms.
- Q 2 vocab as % of corpus: 15.3%.
- **Hapax-Q2** (forms found ONLY in Q 2): **682** (29.9% of Q 2 vocab).

This is a striking concentration: nearly 1 in 3 of Q 2's vocabulary forms is unique to it. Combined with Q 2's 7.89% word-share of the corpus, this means Q 2 contributes ~5% of the corpus's unique vocabulary. The "scaffold" character is partly carried by Q 2 introducing terms that occur nowhere else.

### Cow-vocabulary concentration (claim 10 of audit)

- 67% of all "baqara" surface-forms occur in Q 2 (4 of 6 corpus-wide).
- 40% of all "ʿijl" surface-forms occur in Q 2 (4 of 10 corpus-wide).
- Q 2 contains 7.89% of corpus by word count, but **8.4× over-concentration of "baqara"** and **5.0× over-concentration of "ʿijl"**.

The cow-narrative occupies only 5/286 = 1.7% of Q 2 by verse count yet provides 67% of corpus "baqara" mentions — confirming the narrative's distinctive lexical fingerprint that justifies the surah's name.

### Q 2 final word: "al-kāfirīn"

Q 2:286 ends with "...فانصرنا على القوم الكافرين" — the final word is الكافرين. This is a specific instance of the cross-finding-008 pattern: muqaṭṭaʿāt-opened surahs reference "the Book" early. Q 2 + Q 3 together form a frame: both open with ALM and book-reference; both have communal-prayer closings; Q 2 closes on "al-kāfirīn" while Q 3 closes on "al-muḥsinīn" (the well-doers, Q 3:200 final 2 words).

### Top-15 surface words in Q 2

Computed via `Q002_C_audit_helpers.py`:

| Word | Q 2 count | Corpus count | Q 2 share |
|:--|:--|:--|:--|
| من | 219 | 2,763 | 7.9% |
| الله | 216 | 2,153 | **10.0%** |
| ما | 86 | 1,010 | 8.5% |
| ولا | 83 | 658 | 12.6% |
| في | 78 | 1,185 | 6.6% |
| الذين | 73 | 810 | 9.0% |
| لا | 68 | 812 | 8.4% |
| إن | 60 | 966 | 6.2% |
| أن | 59 | 638 | 9.2% |
| على | 55 | 670 | 8.2% |
| وما | 52 | 646 | 8.0% |
| إلا | 43 | 664 | 6.5% |
| **والله** | 40 | 240 | **16.7%** |
| قال | 37 | 416 | 8.9% |
| **عليكم** | 33 | 164 | **20.1%** |

**Surprises**:
- **والله ("and Allāh")** appears 40× in Q 2 = 16.7% of all corpus instances (vs 7.89% baseline).
- **عليكم ("upon you" — second-person plural)** appears 33× = 20.1% of corpus instances. This 2.5× over-concentration reflects Q 2's communal-legal character — direct address to the Medinan community.
- Q 2 contains **10% of all "Allāh" tokens** in the corpus, just 1.27× over baseline.

The "you" (عليكم) over-concentration is a marker of Q 2's COMMUNAL-LEGAL register — fitting for the longest Medinan revelation.

---

## Summary of novel findings

| Finding | Status | Surprise rating |
|:--|:--|:--|
| Q 2:255 NULL on density, top-5 on absolute count (rules-tuple fragility) | RULES-TUPLE-FRAGILE | High |
| Khawātim al-Baqara NULL on divine-name density | NULL | Medium |
| Q 2 LOO-shift rank 6/114 (scaffold-as-anchor not centroid) | DIRECTIONAL | High (refines al-Biqāʿī) |
| Q 112 is the empirical centroid (medoid) of FR root distribution | DIRECTIONAL-DERIVATIVE | Medium |
| Q 2 verse-token chiastic mirroring NULL | NULL | Medium |
| Q 2:282 is rank 1 by length, z=+12.31, gap=4.33σ | VINDICATED | High |
| Block E (legal core) has highest internal cohesion | DESCRIPTIVE | Medium |
| Block H (khawātim) most distinctive (lowest mean-cos to others) | DESCRIPTIVE | Medium |
| Q 2 has 682 hapax words (30% of its vocab) | DESCRIPTIVE | Medium |
| Q 2 contains 67% of all "baqara" surface forms | DESCRIPTIVE | High (vindicates al-Rāzī) |
| Q 2's "you-plural" (عليكم) is 2.5× over-concentrated | DESCRIPTIVE | Medium |

## Honest limits

- Empirical analysis is at the surface-token level. Lemma- or root-level tests are pending (would use QAC).
- 5 pre-registered tests is below the 8-test family target for full Q 2 audit; future tests (e.g. iltifāt density, syntactic register, register-block fingerprints) are queued.
- The NULL on Farrin/Cuypers ring-structure is resolution-limited — DOES NOT falsify thematic-ring claim.
- All scripts use stdlib only (per investigation protocol).

## Cross-references

- All Q002-F-NN pre-reg + findings markdowns in `/Users/grey/Downloads/quran/surahs/Q002-al-baqara/`.
- Audit helpers script: `/Users/grey/Downloads/quran/scripts/Q002_C_audit_helpers.py`.
- Master test runner: `/Users/grey/Downloads/quran/scripts/Q002_F_master.py`.
- See `05-classical-claims-audit.md` for classical claims that gave rise to several of these tests.
- See `07-cross-references.md` for Q 2's role in larger network structure.
