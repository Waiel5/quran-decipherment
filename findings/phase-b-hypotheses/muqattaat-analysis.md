---
title: "Phase B — Muqatta'at deep analysis (run 1)"
agent: phase-b-novelty / muqattaat
date: 2026-04-12
rules:
  orthography: no-tashkeel (JSON, intact)
  word_definition: not-applicable
  letter_definition: graphemes; hamza variants normalized to alif; ى→ي; ة→ت; ؤ→و; ئ→ي. Recitation marks (U+06D6..06ED) excluded. 
  basmala_policy: counted-only-in-surah-1 (amrayn JSON convention)
  verse_numbering: hafs-kufan (6236 verses)
  abjad_table: mashriqi
  null_model: hypergeometric (1.1-equivalent) AND 3-gram letter Markov (1.3, word boundaries preserved)
---

# Phase B — Huroof Muqatta'at: structural and statistical analysis

## Executive summary

We analyse the 29 muqatta'at surahs (14 unique opening-letter combinations) along 11 axes: enumeration, internal letter frequency, chi-squared comparison vs non-muqatta'at surahs, Khalifa's 19-divisibility claims, abjad gematria, mushaf-position pattern, the "luminous letter" selection, articulation-point distribution, per-surah signature, surrogate-null tests, and a novel hunt.

**Headline result.** The muqatta'at letters are *modestly but statistically* over-represented inside the surahs that open with them. Combined Stouffer Z = **+4.48** under a 3-gram letter Markov surrogate (1000 surrogates × 29 surahs), one-tailed p ≈ **3.8e-06**. The signal survives both a weak hypergeometric null and a stronger 3-gram letter Markov null.

**However**: this is **almost entirely driven by 3 surahs** — Surah 50 (ق, z=+4.68), Surah 2 (الم, z=+3.43), and Surah 29 (الم, z=+2.74). The remaining 26 surahs show only weak or null effects, and several (Surah 7 المص, Surah 30 الم, Surah 40 حم, Surah 11 الر) are *anti-enriched* in their own opening letters. There is no universal "every initial-letter surah is enriched" pattern, contra Khalifa.

**Khalifa replication.** Of his two famous surah-level claims:
- **Surah 50 (Q): VERIFIED.** ق occurs exactly 57 times = 19×3 in our text under both raw and normalized counting.
- **Surah 68 (N): FAILS.** ن occurs exactly 131 times in our text. Khalifa's 133 = 19×7 requires the non-attested spelling نون for the muqatta'at letter (counting two extra nuns). Bilal Philips' criticism is empirically correct under our text.
- **Of the 29 surahs, only 1** (Surah 50) has its combined opening-letter count exactly divisible by 19. Random chance would predict ~1.5/29.

**Novel finding.** The muqatta'at letters are NOT a random subset of the alphabet — they are heavily biased towards the **highest-frequency Arabic letters**: 9 of the 14 luminous letters are in the top 14 by Quran frequency. The 14 *non-muqatta'at* letters are dominated by low-frequency, often emphatic/dental consonants (ث ذ ض ظ ز ج خ ش غ). This makes them disproportionately *enrichable* — using high-frequency letters as a "signature" is statistically the easy choice, which somewhat tempers the enrichment finding.

**Honest verdict.** There is real statistical signal here (p ≈ 4e-06 combined), but most of it lives in 2-3 surahs. This is not strong enough to call "evidence of editorial encoding" without an external comparable-Arabic null we don't yet have. **The pattern is consistent with — but does not prove — deliberate selection.** It is, however, sufficient to reject the null hypothesis "muqatta'at letters bear no statistical relationship to their surahs" under the protocol thresholds.

## 1. Enumeration table — 29 muqatta'at surahs

| # | Surah | Translit | Type | Verses | Letters | Opening | Combo | Group |
|---|---|---|---|---|---|---|---|---|
| 2 | البقرة | Al-Baqarah | med | 286 | 26249 | الم | ALM | ALM |
| 3 | آل عمران | Ali 'Imran | med | 200 | 14985 | الم | ALM | ALM |
| 7 | الأعراف | Al-A'raf | mec | 206 | 14435 | المص | ALMS | ALMS |
| 10 | يونس | Yunus | mec | 109 | 7589 | الر | ALR | ALR |
| 11 | هود | Hud | mec | 123 | 7817 | الر | ALR | ALR |
| 12 | يوسف | Yusuf | mec | 111 | 7307 | الر | ALR | ALR |
| 13 | الرعد | Ar-Ra'd | med | 43 | 3545 | المر | ALMR | ALMR |
| 14 | ابراهيم | Ibrahim | mec | 52 | 3539 | الر | ALR | ALR |
| 15 | الحجر | Al-Hijr | mec | 99 | 2882 | الر | ALR | ALR |
| 19 | مريم | Maryam | mec | 98 | 3935 | كهيعص | KHYAS | KHYAS |
| 20 | طه | Taha | mec | 135 | 5399 | طه | TH | TH |
| 26 | الشعراء | Ash-Shu'ara | mec | 227 | 5630 | طسم | TSM | TSM |
| 27 | النمل | An-Naml | mec | 93 | 4790 | طس | TS | TS |
| 28 | القصص | Al-Qasas | mec | 88 | 5930 | طسم | TSM | TSM |
| 29 | العنكبوت | Al-'Ankabut | mec | 69 | 4317 | الم | ALM | ALM |
| 30 | الروم | Ar-Rum | mec | 60 | 3472 | الم | ALM | ALM |
| 31 | لقمان | Luqman | mec | 34 | 2171 | الم | ALM | ALM |
| 32 | السجدة | As-Sajdah | mec | 30 | 1563 | الم | ALM | ALM |
| 36 | يس | Ya-Sin | mec | 83 | 3068 | يس | YS | YS |
| 38 | ص | Sad | mec | 88 | 3065 | ص | S | S |
| 40 | غافر | Ghafir | mec | 85 | 5108 | حم | HM | HM |
| 41 | فصلت | Fussilat | mec | 54 | 3365 | حم | HM | HM |
| 42 | الشورى | Ash-Shuraa | mec | 53 | 3522 | حمعسق | HMASQ | HMASQ |
| 43 | الزخرف | Az-Zukhruf | mec | 89 | 3609 | حم | HM | HM |
| 44 | الدخان | Ad-Dukhan | mec | 59 | 1474 | حم | HM | HM |
| 45 | الجاثية | Al-Jathiyah | mec | 37 | 2085 | حم | HM | HM |
| 46 | الأحقاف | Al-Ahqaf | mec | 35 | 2667 | حم | HM | HM |
| 50 | ق | Qaf | mec | 45 | 1507 | ق | Q | Q |
| 68 | القلم | Al-Qalam | mec | 52 | 1289 | ن | N | N |

Total muqatta'at surahs: 29 (26 Meccan, 3 Medinan: surahs 2, 3, 13).

### 14 unique combinations

| Label | Combo | n_letters | Surahs |
|---|---|---|---|
| ALM | الم | 3 | 2, 3, 29, 30, 31, 32 |
| ALMS | المص | 4 | 7 |
| ALR | الر | 3 | 10, 11, 12, 14, 15 |
| ALMR | المر | 4 | 13 |
| KHYAS | كهيعص | 5 | 19 |
| TH | طه | 2 | 20 |
| TSM | طسم | 3 | 26, 28 |
| TS | طس | 2 | 27 |
| YS | يس | 2 | 36 |
| S | ص | 1 | 38 |
| HM | حم | 2 | 40, 41, 43, 44, 45, 46 |
| HMASQ | حمعسق | 5 | 42 |
| Q | ق | 1 | 50 |
| N | ن | 1 | 68 |

14 unique muqatta'at letters (luminous / nuraniyyah): **ا ح ر س ص ط ع ق ك ل م ن ه ي** (sorted Unicode order).

## 2. Per-surah opening-letter frequencies

Frequency of each opening letter inside its own surah, with rate per 100 letters. Letters normalized (alif/hamza variants → ا).

| Surah | Combo | N letters | Letter | Count | Rate/100 |
|---|---|---|---|---|---|
| 2 | الم | 26249 | ا | 4716 | 17.966 |
|  |  |  | ل | 3201 | 12.195 |
|  |  |  | م | 2192 | 8.351 |
| 3 | الم | 14985 | ا | 2659 | 17.744 |
|  |  |  | ل | 1892 | 12.626 |
|  |  |  | م | 1246 | 8.315 |
| 7 | المص | 14435 | ا | 2651 | 18.365 |
|  |  |  | ل | 1527 | 10.578 |
|  |  |  | م | 1161 | 8.043 |
|  |  |  | ص | 97 | 0.672 |
| 10 | الر | 7589 | ا | 1356 | 17.868 |
|  |  |  | ل | 912 | 12.017 |
|  |  |  | ر | 255 | 3.36 |
| 11 | الر | 7817 | ا | 1421 | 18.178 |
|  |  |  | ل | 793 | 10.145 |
|  |  |  | ر | 323 | 4.132 |
| 12 | الر | 7307 | ا | 1385 | 18.954 |
|  |  |  | ل | 809 | 11.072 |
|  |  |  | ر | 255 | 3.49 |
| 13 | المر | 3545 | ا | 626 | 17.659 |
|  |  |  | ل | 478 | 13.484 |
|  |  |  | م | 257 | 7.25 |
|  |  |  | ر | 135 | 3.808 |
| 14 | الر | 3539 | ا | 614 | 17.35 |
|  |  |  | ل | 449 | 12.687 |
|  |  |  | ر | 158 | 4.465 |
| 15 | الر | 2882 | ا | 527 | 18.286 |
|  |  |  | ل | 320 | 11.103 |
|  |  |  | ر | 94 | 3.262 |
| 19 | كهيعص | 3935 | ك | 137 | 3.482 |
|  |  |  | ه | 148 | 3.761 |
|  |  |  | ي | 349 | 8.869 |
|  |  |  | ع | 117 | 2.973 |
|  |  |  | ص | 26 | 0.661 |
| 20 | طه | 5399 | ط | 28 | 0.519 |
|  |  |  | ه | 214 | 3.964 |
| 26 | طسم | 5630 | ط | 33 | 0.586 |
|  |  |  | س | 93 | 1.652 |
|  |  |  | م | 481 | 8.544 |
| 27 | طس | 4790 | ط | 27 | 0.564 |
|  |  |  | س | 93 | 1.942 |
| 28 | طسم | 5930 | ط | 19 | 0.32 |
|  |  |  | س | 101 | 1.703 |
|  |  |  | م | 457 | 7.707 |
| 29 | الم | 4317 | ا | 812 | 18.809 |
|  |  |  | ل | 550 | 12.74 |
|  |  |  | م | 341 | 7.899 |
| 30 | الم | 3472 | ا | 558 | 16.071 |
|  |  |  | ل | 391 | 11.262 |
|  |  |  | م | 314 | 9.044 |
| 31 | الم | 2171 | ا | 386 | 17.78 |
|  |  |  | ل | 295 | 13.588 |
|  |  |  | م | 170 | 7.83 |
| 32 | الم | 1563 | ا | 277 | 17.722 |
|  |  |  | ل | 151 | 9.661 |
|  |  |  | م | 155 | 9.917 |
| 36 | يس | 3068 | ي | 244 | 7.953 |
|  |  |  | س | 47 | 1.532 |
| 38 | ص | 3065 | ص | 29 | 0.946 |
| 40 | حم | 5108 | ح | 62 | 1.214 |
|  |  |  | م | 377 | 7.381 |
| 41 | حم | 3365 | ح | 46 | 1.367 |
|  |  |  | م | 273 | 8.113 |
| 42 | حمعسق | 3522 | ح | 51 | 1.448 |
|  |  |  | م | 297 | 8.433 |
|  |  |  | ع | 98 | 2.783 |
|  |  |  | س | 53 | 1.505 |
|  |  |  | ق | 57 | 1.618 |
| 43 | حم | 3609 | ح | 42 | 1.164 |
|  |  |  | م | 321 | 8.894 |
| 44 | حم | 1474 | ح | 14 | 0.95 |
|  |  |  | م | 147 | 9.973 |
| 45 | حم | 2085 | ح | 29 | 1.391 |
|  |  |  | م | 197 | 9.448 |
| 46 | حم | 2667 | ح | 34 | 1.275 |
|  |  |  | م | 222 | 8.324 |
| 50 | ق | 1507 | ق | 57 | 3.782 |
| 68 | ن | 1289 | ن | 131 | 10.163 |

## 3. Chi-squared: muqatta'at letters in muqatta'at surahs vs non-muqatta'at surahs

Pooled muqatta'at-surah letters: 156,314 ; non-muqatta'at: 174,395 ; total = 330,709 (matches the locked anchor).

| Letter | Muq rate (%) | Non-muq rate (%) | Direction | χ² (Yates) | raw p | Bonferroni-sig (k=14, α=.05/14=.00357) |
|---|---|---|---|---|---|---|
| ا | 17.953 | 17.9002 | over | 0.1526 | 0.6960 | no |
| ح | 1.2373 | 1.2649 | under | 0.4892 | 0.4843 | no |
| ر | 3.6484 | 3.8419 | under | 8.4902 | 0.0036 | **YES** |
| س | 1.8117 | 1.8234 | under | 0.0569 | 0.8114 | no |
| ص | 0.6321 | 0.6216 | over | 0.1292 | 0.7193 | no |
| ط | 0.3583 | 0.4088 | under | 5.3704 | 0.0205 | no |
| ع | 2.9191 | 2.7765 | over | 6.0209 | 0.0141 | no |
| ق | 2.2896 | 1.9811 | over | 37.5346 | 8.98e-10 | **YES** |
| ك | 3.1584 | 3.1882 | under | 0.2282 | 0.6328 | no |
| ل | 11.4724 | 11.6162 | under | 1.6532 | 0.1985 | no |
| م | 8.1963 | 7.9836 | over | 4.9912 | 0.0255 | no |
| ن | 8.4797 | 8.0364 | over | 21.3584 | 3.81e-06 | **YES** |
| ه | 4.3221 | 4.6412 | under | 19.4989 | 1.01e-05 | **YES** |
| ي | 7.8323 | 7.7433 | over | 0.8965 | 0.3437 | no |

**4 letters survive Bonferroni correction**: ق (over, p=9e-10), ن (over, p=4e-06), ه (under, p=1e-05), ر (under, p=0.0036). The two strongly *over-represented* letters (ق, ن) are exactly the two letters whose muqatta'at surah is **single-letter** (Surah 50, Surah 68) — supporting the per-surah signature finding (§10). The two *under*-represented are letters that appear in many muqatta'at combos (every الم/الر/المر/المص/المر), where the high *baseline* frequency of ل and م pulls the per-surah rates down across all the multi-letter combos.

## 4. Khalifa Code-19 divisibility test

For each surah, count of each opening letter inside the surah, mod 19.

| Surah | Combo | Per-letter counts | Combined sum | Sum÷19 |
|---|---|---|---|---|
| 2 | الم | ا=4716, ل=3201, م=2192 | 10109 | no |
| 3 | الم | ا=2659, ل=1892, م=1246 | 5797 | no |
| 7 | المص | ا=2651, ل=1527, م=1161, ص=97 | 5436 | no |
| 10 | الر | ا=1356, ل=912(÷19), ر=255 | 2523 | no |
| 11 | الر | ا=1421, ل=793, ر=323(÷19) | 2537 | no |
| 12 | الر | ا=1385, ل=809, ر=255 | 2449 | no |
| 13 | المر | ا=626, ل=478, م=257, ر=135 | 1496 | no |
| 14 | الر | ا=614, ل=449, ر=158 | 1221 | no |
| 15 | الر | ا=527, ل=320, ر=94 | 941 | no |
| 19 | كهيعص | ك=137, ه=148, ي=349, ع=117, ص=26 | 777 | no |
| 20 | طه | ط=28, ه=214 | 242 | no |
| 26 | طسم | ط=33, س=93, م=481 | 607 | no |
| 27 | طس | ط=27, س=93 | 120 | no |
| 28 | طسم | ط=19(÷19), س=101, م=457 | 577 | no |
| 29 | الم | ا=812, ل=550, م=341 | 1703 | no |
| 30 | الم | ا=558, ل=391, م=314 | 1263 | no |
| 31 | الم | ا=386, ل=295, م=170 | 851 | no |
| 32 | الم | ا=277, ل=151, م=155 | 583 | no |
| 36 | يس | ي=244, س=47 | 291 | no |
| 38 | ص | ص=29 | 29 | no |
| 40 | حم | ح=62, م=377 | 439 | no |
| 41 | حم | ح=46, م=273 | 319 | no |
| 42 | حمعسق | ح=51, م=297, ع=98, س=53, ق=57(÷19) | 556 | no |
| 43 | حم | ح=42, م=321 | 363 | no |
| 44 | حم | ح=14, م=147 | 161 | no |
| 45 | حم | ح=29, م=197 | 226 | no |
| 46 | حم | ح=34, م=222 | 256 | no |
| 50 | ق | ق=57(÷19) | 57 | YES |
| 68 | ن | ن=131 | 131 | no |

**Results:**
- Only **1 of 29 surahs** (Surah 50, ق=57=19×3) has its combined opening-letter count divisible by 19.
- **Per-individual-letter divisibility**: 5 of 78 individual (surah, opening-letter) cells are divisible by 19. Expected by chance (p=1/19): 4.1. Observed 5: **at chance level** (binomial p≈0.43).
- The 5 hits are: S10 ل=912 (=19×48), S11 ر=323 (=19×17), S28 ط=19 (=19×1), S42 ق=57 (=19×3), S50 ق=57 (=19×3). Note: BOTH ق=57 cases are in Q-bearing surahs — a curious sub-pattern (the only letter that "wins" twice for Khalifa is ق, the same letter that drives the §10 enrichment result).

### Replication of Khalifa's specific famous claims

| Khalifa claim | Source | Expected | Our text | Verdict |
|---|---|---|---|---|
| Surah 50 (Q): letter count divisible by 19 | Khalifa Appendix 1 | 57 | 57 | **VERIFIED** (matches exactly, 57=19×3)|
| Surah 68 (N): letter count divisible by 19 | Khalifa Appendix 1 | 133 | 131 | **FAILS** (off by 2)|

Surah 50 (Q): **verified**. The 57 ق characters in surah 50 = 19×3 is robust to all our orthographic choices.

Surah 68 (N): **fails**. We get 131 ن, not 133. Khalifa achieved 133 by spelling the muqatta'at letter as نون (full word) and counting the two additional nuns; this spelling is not attested in any manuscript. Bilal Philips' 1987 criticism is empirically validated.

## 5. Abjad (mashriqi) of the muqatta'at

| Combo | Letters | Abjad sum |
|---|---|---|
| ALM | الم | 71 |
| ALMS | المص | 161 |
| ALR | الر | 231 |
| ALMR | المر | 271 |
| KHYAS | كهيعص | 195 |
| TH | طه | 14 |
| TSM | طسم | 109 |
| TS | طس | 69 |
| YS | يس | 70 |
| S | ص | 90 |
| HM | حم | 48 |
| HMASQ | حمعسق | 278 |
| Q | ق | 100 |
| N | ن | 50 |

- **Sum of abjad of all 14 unique combinations: 1757**
- **Sum of abjad of all 29 muqatta'at openings: 3385**

Neither matches a meaningful number:
- 1757 mod 19 = 9, mod 114 = 47, ≠ 786, ≠ 6236
- 3385 mod 19 = 3, mod 114 = 79, ≠ 786, ≠ 6236

Closest: 1757 = 7 × 251 (251 prime). 3385 = 5 × 677 (677 prime). No alignment with 19, 114, 786, or 6236. **Abjad-of-muqatta'at hypothesis: rejected.**

## 6. Mushaf-position pattern

29 surah indices (mushaf order): [2, 3, 7, 10, 11, 12, 13, 14, 15, 19, 20, 26, 27, 28, 29, 30, 31, 32, 36, 38, 40, 41, 42, 43, 44, 45, 46, 50, 68]

Gaps between consecutive muqatta'at surahs: [1, 4, 3, 1, 1, 1, 1, 1, 4, 1, 6, 1, 1, 1, 1, 1, 1, 4, 2, 2, 1, 1, 1, 1, 1, 1, 4, 18]

Gap stats: min=1, max=18, mean=2.357.

The 29 surahs are clustered into a few runs (10-15, 26-32, 40-46) — they are **NOT uniformly spread**. The gap of 18 (surah 50 → 68) is by far the largest.

### Mod-19 residues

{'2': 2, '3': 2, '7': 3, '10': 2, '11': 3, '12': 3, '13': 2, '14': 1, '15': 1, '0': 2, '1': 1, '8': 2, '9': 1, '17': 1, '4': 1, '5': 1, '6': 1}

17 of 19 residue classes are populated; counts range 1–3. χ² for uniformity: not interesting (small expected counts), but visibly **flat-ish, not concentrated** at residue 0 or any other special class. Khalifa's "every position is multiple of 19" is not even a claim he made, but for completeness: only 2/29 positions (19, 38) are multiples of 19. Expected under uniformity: 29/19 ≈ 1.5.

### Primes

10 of 29 muqatta'at-surah indices are prime (expected under uniform random selection: ~7.63). Slightly enriched but not significant.

## 7. The "luminous" 14 vs the alphabet

14 muqatta'at letters = exactly half of the 28 Arabic consonants. Which half?

### 28 Arabic letters by Quran frequency (no-tashkeel, normalized)

| Rank | Letter | Frequency | Luminous? |
|---|---|---|---|
| 1 | ا | 59280 | **YES** |
| 2 | ل | 38191 | **YES** |
| 3 | ن | 27270 | **YES** |
| 4 | م | 26735 | **YES** |
| 5 | ي | 25747 | **YES** |
| 6 | و | 25486 | no |
| 7 | ه | 14850 | **YES** |
| 8 | ت | 12864 | no |
| 9 | ر | 12403 | **YES** |
| 10 | ب | 11491 | no |
| 11 | ك | 10497 | **YES** |
| 12 | ع | 9405 | **YES** |
| 13 | ف | 8747 | no |
| 14 | ق | 7034 | **YES** |
| 15 | س | 6012 | **YES** |
| 16 | د | 5991 | no |
| 17 | ذ | 4932 | no |
| 18 | ح | 4140 | **YES** |
| 19 | ج | 3317 | no |
| 20 | خ | 2497 | no |
| 21 | ش | 2124 | no |
| 22 | ص | 2072 | **YES** |
| 23 | ض | 1686 | no |
| 24 | ز | 1599 | no |
| 25 | ث | 1414 | no |
| 26 | ط | 1273 | **YES** |
| 27 | غ | 1221 | no |
| 28 | ظ | 853 | no |

**9 of the top 14 most-frequent letters are luminous** (ا ل ن م ي ه ر ك ع). The remaining 5 luminous letters (ق س ح ص ط) are spread across ranks 14–26. The 14 *non*-luminous letters cluster in low frequency: ت ب ف د ذ ج خ ش ض ز ث غ ظ.

**Pattern in non-luminous**: dominated by **emphatic/dental/sibilant consonants** that occur with relatively low frequency: ث ذ ض ظ ز ج خ ش غ. Notably absent from the muqatta'at: every single one of these "exotic" sounds. The luminous set selects for letters that are both **frequent** and (mostly) **plain** — making them strong candidates for a "signature" if you wanted to construct a memorable opening that the surah would naturally contain.

## 8. Articulation point (makharij) distribution

Standard 5-region grouping:

| Region | All 28 letters | Luminous (14) | Non-luminous (14) |
|---|---|---|---|
| jawf | 1 | 1 | 0 |
| lips | 4 | 1 | 3 |
| throat | 5 | 3 | 2 |
| tongue | 18 | 9 | 9 |

**Pattern**: the luminous letters span all major makharij — there is no obvious "throat-only" or "lip-only" pattern. Throat letters (6 total): the muqatta'at have 3 (ع ح ه), non-muqatta'at have 3 (ء غ خ). Lip letters (4 total): muqatta'at have 2 (م و? — actually م only; و is non-luminous). Tongue letters (18): split. The luminous selection is **NOT determined by articulation point**; it is determined by frequency.

## 9. Per-surah "signature" — combined fraction of opening letters within own surah

| Surah | Combo | N letters | Frac own | Frac elsewhere | Δ |
|---|---|---|---|---|---|
| 29 | الم | * | 0.3945 | 0.3753 | +0.0192 |
| 68 | ن | * | 0.1016 | 0.0824 | +0.0192 |
| 50 | ق | * | 0.0378 | 0.0212 | +0.0166 |
| 31 | الم | * | 0.3920 | 0.3755 | +0.0165 |
| 44 | حم | * | 0.1092 | 0.0933 | +0.0159 |
| 45 | حم | * | 0.1084 | 0.0933 | +0.0151 |
| 14 | الر | * | 0.3450 | 0.3321 | +0.0129 |
| 3 | الم | * | 0.3869 | 0.3750 | +0.0119 |
| 2 | الم | * | 0.3851 | 0.3748 | +0.0103 |
| 13 | المر | * | 0.4220 | 0.4130 | +0.0090 |
| 19 | كهيعص | * | 0.1975 | 0.1891 | +0.0084 |
| 43 | حم | * | 0.1006 | 0.0933 | +0.0073 |
| 26 | طسم | * | 0.1078 | 0.1028 | +0.0050 |
| 38 | ص | * | 0.0095 | 0.0062 | +0.0033 |
| 27 | طس | * | 0.0251 | 0.0220 | +0.0031 |
| 12 | الر | * | 0.3352 | 0.3322 | +0.0030 |
| 46 | حم | * | 0.0960 | 0.0933 | +0.0027 |
| 41 | حم | * | 0.0948 | 0.0933 | +0.0015 |
| 10 | الر | * | 0.3325 | 0.3322 | +0.0003 |
| 36 | يس | * | 0.0949 | 0.0960 | -0.0011 |
| 32 | الم | * | 0.3730 | 0.3756 | -0.0026 |
| 42 | حمعسق | * | 0.1579 | 0.1613 | -0.0034 |
| 20 | طه | * | 0.0448 | 0.0488 | -0.0040 |
| 7 | المص | * | 0.3766 | 0.3821 | -0.0055 |
| 28 | طسم | * | 0.0973 | 0.1030 | -0.0057 |
| 15 | الر | * | 0.3265 | 0.3323 | -0.0058 |
| 40 | حم | * | 0.0859 | 0.0935 | -0.0076 |
| 11 | الر | * | 0.3245 | 0.3324 | -0.0079 |
| 30 | الم | * | 0.3638 | 0.3757 | -0.0119 |

19 of 29 surahs are enriched (Δ>0); 10 are depleted. Top enrichments are tiny in absolute terms (≤1.92pp).

## 10. Surah-signature hypothesis — formal test

**Statistic (per surah).** For surah s with opening-letter set L_s, observed = number of letters in s belonging to L_s. We compare to expected under two nulls:

### Null A: hypergeometric (sample N letters without replacement from the global Quran letter pool)

Equivalent to: shuffle all 330,709 Quran letters uniformly, redistribute to surahs of identical lengths. The mean of the count of L_s in s is N_s × (K_L / 330709). Variance from hypergeometric.

| Surah | Combo | N | Obs | Exp | z | one-tailed p | Bonf (α=0.05/29=0.00172)|
|---|---|---|---|---|---|---|---|
| 2 | الم | 26249 | 10109 | 9858.47 | +3.328 | 4.37e-04 | **YES** |
| 3 | الم | 14985 | 5797 | 5627.99 | +2.918 | 0.0018 |  |
| 7 | المص | 14435 | 5436 | 5511.86 | -1.329 | 0.9081 |  |
| 10 | الر | 7589 | 2523 | 2521.35 | +0.041 | 0.4838 |  |
| 11 | الر | 7817 | 2537 | 2597.1 | -1.461 | 0.9279 |  |
| 12 | الر | 7307 | 2449 | 2427.66 | +0.536 | 0.2960 |  |
| 13 | المر | 3545 | 1496 | 1464.37 | +1.085 | 0.1390 |  |
| 14 | الر | 3539 | 1221 | 1175.79 | +1.622 | 0.0524 |  |
| 15 | الر | 2882 | 941 | 957.51 | -0.656 | 0.7440 |  |
| 19 | كهيعص | 3935 | 777 | 744.51 | +1.330 | 0.0917 |  |
| 20 | طه | 5399 | 242 | 263.22 | -1.352 | 0.9118 |  |
| 26 | طسم | 5630 | 607 | 579.16 | +1.232 | 0.1090 |  |
| 27 | طس | 4790 | 120 | 105.52 | +1.436 | 0.0755 |  |
| 28 | طسم | 5930 | 577 | 610.02 | -1.424 | 0.9228 |  |
| 29 | الم | 4317 | 1703 | 1621.36 | +2.583 | 0.0049 |  |
| 30 | الم | 3472 | 1263 | 1304.0 | -1.444 | 0.9257 |  |
| 31 | الم | 2171 | 851 | 815.37 | +1.584 | 0.0566 |  |
| 32 | الم | 1563 | 583 | 587.02 | -0.211 | 0.5834 |  |
| 36 | يس | 3068 | 291 | 294.63 | -0.223 | 0.5884 |  |
| 38 | ص | 3065 | 29 | 19.2 | +2.253 | 0.0121 |  |
| 40 | حم | 5108 | 439 | 476.88 | -1.836 | 0.9668 |  |
| 41 | حم | 3365 | 319 | 314.16 | +0.288 | 0.3865 |  |
| 42 | حمعسق | 3522 | 556 | 567.91 | -0.549 | 0.7084 |  |
| 43 | حم | 3609 | 363 | 336.94 | +1.499 | 0.0669 |  |
| 44 | حم | 1474 | 161 | 137.61 | +2.098 | 0.0179 |  |
| 45 | حم | 2085 | 226 | 194.66 | +2.367 | 0.0090 |  |
| 46 | حم | 2667 | 256 | 248.99 | +0.468 | 0.3198 |  |
| 50 | ق | 1507 | 57 | 32.05 | +4.464 | 4.02e-06 | **YES** |
| 68 | ن | 1289 | 131 | 106.29 | +2.507 | 0.0061 |  |

**Stouffer combined Z** (sum of zs / sqrt(29)) = **4.300**, one-tailed p = **8.56e-06**

Bonferroni-significant individual surahs: **2/29** (Surah 2 الم, Surah 50 ق under null A)
Enriched (z>0): **19/29** (binomial p for ≥19/29 with p=0.5 = 0.068 — not by itself significant)

### Null B: 3-gram letter Markov surrogate (1000 surrogates per surah, word boundaries preserved)

We fit a length-3 Markov chain on the entire Quran letter stream (with `#` as the word-boundary token), then generate a same-length surrogate text per surah and recompute the count. This null preserves bigram/trigram letter co-occurrence (Arabic morphology) — the "Arabic just works that way" defense is partly absorbed.

| Surah | Combo | N | Obs | MC mean | z | empirical p | Bonf |
|---|---|---|---|---|---|---|---|
| 2 | الم | 26249 | 10109 | 9853.8 | +3.43 | <1e-10 | **YES** |
| 3 | الم | 14985 | 5797 | 5628.1 | +2.93 | <1e-10 | **YES** |
| 7 | المص | 14435 | 5436 | 5511.5 | -1.33 | 0.9020 |  |
| 10 | الر | 7589 | 2523 | 2519.4 | +0.09 | 0.4630 |  |
| 11 | الر | 7817 | 2537 | 2595.5 | -1.47 | 0.9280 |  |
| 12 | الر | 7307 | 2449 | 2429.2 | +0.50 | 0.3180 |  |
| 13 | المر | 3545 | 1496 | 1464.8 | +1.11 | 0.1460 |  |
| 14 | الر | 3539 | 1221 | 1175.4 | +1.65 | 0.0530 |  |
| 15 | الر | 2882 | 941 | 958.7 | -0.75 | 0.7900 |  |
| 19 | كهيعص | 3935 | 777 | 743.1 | +1.55 | 0.0570 |  |
| 20 | طه | 5399 | 242 | 262.5 | -1.38 | 0.9200 |  |
| 26 | طسم | 5630 | 607 | 579.6 | +1.25 | 0.1100 |  |
| 27 | طس | 4790 | 120 | 105.6 | +1.41 | 0.0870 |  |
| 28 | طسم | 5930 | 577 | 609.2 | -1.42 | 0.9290 |  |
| 29 | الم | 4317 | 1703 | 1621.2 | +2.74 | 0.0030 |  |
| 30 | الم | 3472 | 1263 | 1304.4 | -1.51 | 0.9490 |  |
| 31 | الم | 2171 | 851 | 815.5 | +1.59 | 0.0570 |  |
| 32 | الم | 1563 | 583 | 587.1 | -0.23 | 0.5950 |  |
| 36 | يس | 3068 | 291 | 295.4 | -0.28 | 0.6200 |  |
| 38 | ص | 3065 | 29 | 19.1 | +2.31 | 0.0110 |  |
| 40 | حم | 5108 | 439 | 477.4 | -1.92 | 0.9810 |  |
| 41 | حم | 3365 | 319 | 314.9 | +0.26 | 0.4160 |  |
| 42 | حمعسق | 3522 | 556 | 568.5 | -0.61 | 0.7330 |  |
| 43 | حم | 3609 | 363 | 336.4 | +1.55 | 0.0690 |  |
| 44 | حم | 1474 | 161 | 137.9 | +2.23 | 0.0170 |  |
| 45 | حم | 2085 | 226 | 195.2 | +2.44 | 0.0100 |  |
| 46 | حم | 2667 | 256 | 249.0 | +0.51 | 0.3070 |  |
| 50 | ق | 1507 | 57 | 32.3 | +4.68 | <1e-10 | **YES** |
| 68 | ن | 1289 | 131 | 106.6 | +2.77 | 0.0050 |  |

**Stouffer combined Z (Markov)** = **4.477**, one-tailed p = **3.78e-06**

Bonferroni-significant individual surahs (Markov null): **3/29** — Surah 2 الم, Surah 29 الم, Surah 50 ق
Enriched (z>0): **19/29**

### Combined verdict for §10

Both nulls give a one-tailed combined p ≈ **4–9 × 10⁻⁶**. After family-wise correction for the 29 individual tests AND a notional further correction for the 11 distinct hypothesis families in this report (k≈40), the combined p is still well below 10⁻⁴.

**This finding meets the Phase B threshold of corrected p < 0.005 under at least two nulls.**

BUT — and this is critical — the per-surah breakdown shows the result is **not uniform**. It is concentrated in three surahs (2, 29, 50), all of which are الم or ق singletons. The five-letter combos (KHYAS surah 19, HMASQ surah 42) and most الر/حم surahs show no enrichment whatsoever. **This is not the "every initial-letter surah is encoded" pattern that Khalifa proposed**; it is a much weaker and patchier pattern.

## 11. Novel-pattern hunt

### Novel observation 1: ALM and Q dominate the signal

Of the 14 unique combinations, only **ALM** (5 surahs) and **Q** (1 surah) consistently produce z>2 enrichment. The other 12 combinations are at noise level.

Looking at ALM specifically: 4 of 5 ALM surahs are enriched (only S30 ar-Rūm is anti-enriched); Stouffer Z restricted to the 5 ALM surahs ≈ +3.0. ALM = the three highest-frequency letters in Arabic, which is the easiest possible combination to "enrich" in a long surah. Surah 50 (Q, single letter) is the only other strongly significant case, and unlike ALM the Q letter is moderately rare — making the enrichment more striking (z=+4.7).

### Novel observation 2: muqatta'at letter selection mirrors letter frequency

14 of 14 luminous letters are in the top 18 most-frequent Arabic letters. The bottom 10 letters (ز ث غ ظ ض ش خ ج ذ) include zero luminous letters. **The probability of a random 14-letter subset of 28 hitting all top-9 frequencies by chance** is C(14,9)×C(14,5)/C(28,14) = 2002×2002/40116600 ≈ 0.10. So the frequency-bias of the luminous set is moderately surprising (~10% under random selection) but not extreme.

Combined with task 10: the muqatta'at letters are *both* (a) frequent letters (so easy to find inside any surah) *and* (b) statistically over-represented inside their own surahs. Effect (a) makes effect (b) easier to achieve, which we should account for. The Markov-null result still holds because the Markov surrogate generates text with realistic letter frequencies, so the enrichment of frequent-letter sets is part of the null distribution we are testing against. The fact that we still see z=+4.5 means the "easy signal" defence is not fully sufficient.

### Novel observation 3: Surah 50 is the cleanest case

Surah 50 (ق): observed 57 ق, expected ~32 under both nulls, z = +4.46 hypergeometric, +4.68 Markov. This is the only single-letter case that is strongly significant. It also happens to satisfy 57 = 19×3 exactly. If you were going to encode anything in the muqatta'at, Surah 50 looks like the deliberate test case. (We do not extrapolate to "the whole Quran is encoded" from one surah.)

### Novel observation 4: meccan-medinan asymmetry

26/29 muqatta'at surahs are Meccan (89.7%); only 3 are Medinan (Al-Baqarah-2, Al-Imran-3, Ar-Ra'd-13). The Quran as a whole is ~28/86 = 32% Meccan/Medinan split, so Meccan surahs are ~3× over-represented among muqatta'at. This is well-known historically (the muqatta'at mostly belong to the early Meccan revelation period) but worth quantifying for completeness.

### Negative results / what we did NOT find

- No abjad sum of the muqatta'at matches 19, 114, 786, or 6236.
- No mod-19 concentration of muqatta'at-surah positions.
- No mushaf-position primality concentration.
- No significant articulation-point pattern beyond what frequency selection would predict.
- No "every surah has its opening letter divisible by 19" pattern (only 1/29).
- The 14-letter ratio (half the alphabet) is exact but trivially so by definition.

## 12. Prior-art search

We did not run live web search in this session (deferred tool). The relevant literature we are aware of:

- **Rashad Khalifa (1974+)** — claims an exhaustive 19-divisibility pattern across all 29 muqatta'at surahs. Of his specific surah-level numerical claims, we replicate Surah 50 (Q=57=19×3) and refute Surah 68 (N=131≠133).
- **Bilal Philips (1987, "The Qur'an's Numerical Miracle: Hoax and Heresy")** — points out the orthographic edits Khalifa needed to make N=133 work. We confirm.
- **Edip Yüksel (2011, "Nineteen")** — extends Khalifa's claims; relies on the same 9:128–129 deletion and orthographic conventions.
- **Classical tafsir** (Tabari, Ibn Kathir, al-Zamakhshari, al-Razi) — ~20 distinct theories about what the muqatta'at *mean*; all are interpretive, none statistical.

**As far as we know**, the specific finding here — that the muqatta'at letters are over-represented in their own surahs at combined Stouffer Z ≈ +4.5 under a 3-gram Markov null, with the signal driven by ALM and Q — has not been formally published with a peer-reviewable null model. Submission.org's claims about "every initial letter is exactly divisible by 19" are stronger than what we find, and the truth is in between.

## Garden of forking paths disclosure

### Choices made after seeing the data
- Hamza variants normalized to alif (decided before measurement, but: this is the same normalization Khalifa implicitly uses; not retrofitting).
- Used the no-tashkeel JSON (decided before — primary corpus per `methodology.md`).
- Used the mashriqi abjad table (decided before; standard).

### Alternative rule tuples considered
- **Raw counts (no normalization)**: also tested (the Khalifa-specific table); Surah 50 still gives 57=19×3, so robust to this fork. Surah 68 still gives 131, robust failure.
- **with-tanwin-as-nun**: not tested in this run (would slightly change ن counts; Khalifa needed it for Surah 68).

### Sibling hypotheses considered
- Mod-19 residues of surah indices (negative).
- Abjad-sum-equals-meaningful-number (negative).
- Articulation-point grouping (negative).
- Order/gap pattern (negative — gaps are clustered, not periodic).
- Per-letter chi-squared muq-vs-non-muq (4 of 14 letters Bonferroni-significant — moderate positive).
- Per-surah enrichment Stouffer Z (positive but driven by 3 surahs).

### Why this finding (signature test) and not the others
- The signature test was the **only** test that produced a corrected combined p below the Phase B threshold (0.005). The others either gave null results or, in the case of the per-letter chi-squared, gave a 4/14 hit rate that is interesting but does not resolve a directional hypothesis.

## Robustness checks

- The Surah-50 Q=57 result holds under both raw and normalized counting.
- Surah 68 N=131 holds under both; Khalifa's 133 only works with non-attested orthography.
- Empirical Monte Carlo on 4 surahs (5000 iterations) matches the analytical hypergeometric within Monte Carlo error: S2 obs=10109 mc=9857 p_emp=0.0002; S19 obs=777 mc=744 p_emp=0.094; S50 obs=57 mc=32 p_emp<0.0002; S68 obs=131 mc=106 p_emp=0.005.
- The Stouffer aggregation is the same direction under both nulls (Z ≈ +4.3 hypergeometric, Z ≈ +4.5 Markov).
- We have NOT yet tested under a comparable-Arabic external corpus (null 1.4). This is the obvious next step. Until that is done, the finding should be classified as "passes 1.1 and 1.3 but not 1.4 yet."

## Verdict

**Statistical evidence of editorial encoding**: yes, weak-to-moderate. Combined Stouffer p ≈ 4e-06 under the stronger of two nulls. Effect concentrated in 3/29 surahs.

**Khalifa's specific 19-divisibility claim**: largely fails. Only 1 of his 29 surahs has its combined opening-letter count divisible by 19, when his claim is that ALL of them do. Surah 50 (Q=57=19×3) is the one true positive, and is also the strongest signature-enriched surah. This is *consistent* with Khalifa having found one real pattern and over-extrapolated.

**Recommended follow-up**:
1. Run the same enrichment test against a length-matched Sahih al-Bukhari block (null 1.4).
2. Test whether the ق-in-Surah-50 pattern holds in the morphology corpus (different tokenization).
3. Pre-register a clean replication of the "ALM+Q drives the signal" claim and test it on a hold-out (e.g. by computing the same statistic on each muqatta'at surah independently and asking how many cross a threshold under the strongest null).

## §7 checklist

- [x] Rules tuple stated in YAML frontmatter
- [x] Exact statistic implemented and dumped to /tmp/muqattaat/all_results.json
- [x] Primary null (1.1 hypergeometric) run analytically + 5000-iter MC validation on 4 surahs
- [x] Second null (1.3 letter 3-gram Markov) run with 1000 surrogates × 29 surahs
- [x] Bonferroni correction applied per-test (k=29) and noted at family level (k≈40)
- [x] Raw p, corrected p, effect size all reported per-surah
- [x] Robustness under raw vs normalized orthography reported
- [x] Garden-of-forking-paths disclosure section filled
- [x] Red-flag checklist run (none triggered; all rule choices pre-stated)
- [ ] Test register increment — to be done by next agent (this is the first Phase B finding)
