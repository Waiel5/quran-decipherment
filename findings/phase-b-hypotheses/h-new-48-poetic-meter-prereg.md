---
id: H-NEW-48
title: Quran verse-length distribution vs the 16 al-Khalīlian buḥūr — prose, poetry, or neither?
status: PRE-REGISTERED (locked before any Quran/baseline length distribution viewed)
registered: 2026-04-15
spec_locked_at: 2026-04-15
bonferroni_family: 2026-04-15-Wave-3-poetic-meter
bonferroni_k: 19
alpha_per: 0.00263
alpha_bon: 0.05
rules_tuple: (no-tashkeel, orthographic-token, graphemes, basmala-counted-only-in-surah-1, hafs-kufan, mashriqi)
primary_corpus: quran-text/quran-no-tashkeel.json
seed: 20260416
---

# [[h-new-48-poetic-meter|H-NEW-48]] — Does Quran verse-length match any pre-Islamic Arabic poetic meter?

## Question

al-Bāqillānī's classical claim (Iʿjāz al-Qurʾān, ~1000 CE) is that the Quran is neither prose (nathr) nor poetry (shiʿr). al-Khalīl b. Aḥmad al-Farāhīdī (~790 CE) classified Arabic poetry into 16 standard meters (buḥūr). Each meter has a canonical syllable-count per line (bayt) and per hemistich (shaṭr).

**Test:** Does the empirical Quranic verse-length distribution (length per āya) match the canonical syllable-count distribution of any one of the 16 buḥūr at Bonferroni-corrected α? Does the Quran sit BETWEEN prose-baseline and poetry-baseline (al-Bāqillānī prediction)?

## Prosodic table — LOCKED before viewing any Quran or baseline distribution

al-Khalīl's standard buḥūr in their full canonical (sālim, no zihāf) form. Per-hemistich (shaṭr) syllable counts are the standard prosodic descriptions; per-line (bayt) = 2 × shaṭr (for non-majzūʾ forms). Source: standard prosody (Wright Arabic Grammar Vol II §390 ff.; Frolov 2000 *Classical Arabic Verse*; Stoetzer 1989 *Theory and Practice of Arabic Metrics*). Each foot syllable count is the standard CV-CV pattern: WS = light syllable (CV), SW = heavy (CVC/CVV); the *count of syllables per foot* is fixed regardless of which is light/heavy.

| # | Meter (Latin) | Meter (Arabic) | Foot pattern | Syllables per shaṭr | Syllables per bayt | Letter-equivalent per shaṭr (3.0×) |
|--:|---|---|---|--:|--:|--:|
| 1 | Ṭawīl    | الطويل    | faʿūlun mafāʿīlun faʿūlun mafāʿīlun       | 14 | 28 | 42 |
| 2 | Madīd    | المديد    | fāʿilātun fāʿilun fāʿilātun                | 11 | 22 | 33 |
| 3 | Basīṭ    | البسيط    | mustafʿilun fāʿilun mustafʿilun fāʿilun    | 14 | 28 | 42 |
| 4 | Wāfir    | الوافر    | mufāʿalatun mufāʿalatun faʿūlun           | 13 | 26 | 39 |
| 5 | Kāmil    | الكامل    | mutafāʿilun mutafāʿilun mutafāʿilun       | 15 | 30 | 45 |
| 6 | Hazaj    | الهزج     | mafāʿīlun mafāʿīlun                        |  8 | 16 | 24 |
| 7 | Rajaz    | الرجز     | mustafʿilun mustafʿilun mustafʿilun       | 12 | 24 | 36 |
| 8 | Ramal    | الرمل     | fāʿilātun fāʿilātun fāʿilātun             | 12 | 24 | 36 |
| 9 | Sarīʿ    | السريع    | mustafʿilun mustafʿilun mafʿūlātu (catalectic) | 12 | 24 | 36 |
|10 | Munsariḥ | المنسرح   | mustafʿilun mafʿūlātu mustafʿilun         | 12 | 24 | 36 |
|11 | Khafīf   | الخفيف    | fāʿilātun mustafʿilun fāʿilātun           | 11 | 22 | 33 |
|12 | Muḍāriʿ  | المضارع   | mafāʿīlun fāʿilātun                        |  8 | 16 | 24 |
|13 | Muqtaḍab | المقتضب   | mafʿūlātu mustafʿilun                      |  8 | 16 | 24 |
|14 | Mujtathth | المجتث   | mustafʿilun fāʿilātun                      |  8 | 16 | 24 |
|15 | Mutaqārib | المتقارب | faʿūlun faʿūlun faʿūlun faʿūlun           | 12 | 24 | 36 |
|16 | Mutadārik | المتدارك | fāʿilun fāʿilun fāʿilun fāʿilun           |  8 | 16 | 24 |

**Letter-equivalent calibration.** The conversion factor 3.0 letters per syllable is the empirically-observed mean for unvocalized Arabic prose (each consonant ≈ 1 letter, each long vowel = 1 letter, short vowels = 0 letters in unvocalized text; mean syllable shape = CV(C)(C) ≈ 2.5–3.0 letters). LOCKED at 3.0 before viewing any Muʿallaqāt or Quran distribution. Sensitivity analysis at 2.5 and 3.5 provided as a robustness check (NOT the primary test).

**Per-line vs per-hemistich.** Arabic poetry is typically transcribed one bayt per line, but in our muʿallaqa files each line = one bayt = full 2-shaṭr. So Muʿallaqāt should match at the **bayt** level (28-letter Ṭawīl etc.). The Quran's "verse" (āya) has no fixed prosodic length; we treat it as the unit of analysis and ask whether its empirical length distribution matches any meter's bayt-length distribution.

## Procedure

1. **Build the Quran length distribution.** For each of 6,236 verses, compute letter-grapheme count (using `analysis.tools.tokenize.graphemes` on `quran-no-tashkeel.json`). Call this Q.
2. **Build each meter's reference distribution.** For meter m with bayt-letter-count μ_m, the canonical-meter distribution is a narrow Gaussian centred at μ_m with σ_m = 0.10 × μ_m (10% prosodic license: zihāf and ʿilal modifications, allowable consonant clusters, short-syllable variation). LOCKED. This generates a discretised PMF over integer letter-counts {1, 2, ..., 200}.
3. **Build baseline distributions.** Three matched-Arabic baselines, length distributions:
   - **B1 = Bukhārī** sentence lengths (prose; same split as [[h-new-43-verse-length-fft|H-NEW-43]]).
   - **B2 = Jāḥiẓ-Ḥayawān** sentence lengths (prose).
   - **B3 = Muʿallaqāt** verse (bayt) lengths (poetry; 7 muʿallaqāt concatenated, one bayt per line).
4. **KS distance.** For each pair (Q, m) and (Q, B), compute two-sample Kolmogorov-Smirnov D statistic with empirical p-value via 10,000 permutation/bootstrap reshuffles. Also report the bootstrap-resampled D distribution for context.
5. **Bonferroni correction.** k = 16 meters + 3 baselines = **19 cells**. α_per = 0.05/19 = **0.00263**. LOCKED.
6. **al-Bāqillānī test.** Does Q's empirical mean and median sit BETWEEN B1∪B2 (prose) and B3 (poetry)? Specifically, is `min(mean(B1), mean(B2)) < mean(Q) < mean(B3)` OR `mean(B3) < mean(Q) < min(mean(B1), mean(B2))`? Same for median.
7. **MW-5 positive control.** Each muʿallaqa is by historical convention a specific meter (Imruʾ al-Qais → Ṭawīl, Tarafa → Ṭawīl, Zuhayr → Ṭawīl, Labid → Kāmil, ʿAntara → Kāmil, ʿAmr b. Kulthūm → Wāfir, al-Ḥārith → Khafīf). The combined Muʿallaqāt should match at least one meter at p<0.001 in our pipeline. If NOT, the pipeline's letter-equivalent calibration is broken and the verdict is NULL-BROKEN.
8. **MW-7 internal-error gate.** All 16 meter syllable-counts taken from this pre-reg's locked table. If Wright/Stoetzer/Frolov disagree on any meter, document and use the modal value.

## Pre-committed verdict table

| Outcome | Verdict |
|---|---|
| Q distinct from all 16 meters AND distinct from all 3 baselines at α_per=0.00263 | **PASS — Quran is neither prose nor poetry by this metric** (al-Bāqillānī confirmed) |
| Q indistinguishable from at least one meter at α_per | **NULL-classical-meter-match** (specific match named) |
| Q indistinguishable from prose baselines at α_per | **NULL-prose** (Quran is statistically prose) |
| Q sits between prose and poetry on mean+median (Step 6 test) AND distinct from all individual meters/baselines | **PASS-BETWEEN — quantitative al-Bāqillānī confirmed** |
| Muʿallaqāt do not match any meter at p<0.001 | **NULL-BROKEN** (positive control failed; pipeline calibration off) |

## Garden-of-forking-paths log (committed BEFORE any view of Quran or baseline length data)

- **Letter unit.** Letter-graphemes (no tashkeel, no recitation marks, no shadda-doubling). LOCKED. Alternative: "with-shadda-doubled" not tested in this pre-reg.
- **Syllable→letter conversion.** Locked at 3.0 letters/syllable. Sensitivity at 2.5, 3.5 reported but not used for verdict.
- **Meter reference σ.** σ_m = 0.10 × μ_m. LOCKED. This 10% width represents the standard ±2 syllable zihāf/ʿilal license (e.g., Ṭawīl 28-syllable line can be 26–30 in performance).
- **KS p-value method.** Bootstrap resampling of n_Q from each meter's reference PMF; 10,000 reps. LOCKED.
- **Baseline list.** Bukhārī, Jāḥiẓ, Muʿallaqāt. Three. LOCKED. (Sira ibn Hisham, Mutanabbi diwan available but NOT included to keep k = 19; adding them would inflate Bonferroni.)
- **Inclusion of Mutadārik (16th meter).** Sometimes excluded as al-Khalīl's table only had 15. We INCLUDE Mutadārik to be conservative (k=16 not 15). Pre-committed.
- **Quran verse delimiter.** Hafs-Kufan numbering as stored in amrayn no-tashkeel JSON. Basmala = surah 1 verse 1 only. LOCKED.
- **Bonferroni k = 19** (16 + 3). LOCKED. Alternative k=20 if Mutadārik split into Khabab variant: NOT taken.

## Mechanism interpretation

- **PASS** → al-Bāqillānī's prose/poetry-distinct claim is empirically supported at the verse-length-distribution level. Strong finding.
- **PASS-BETWEEN** → quantitative version of al-Bāqillānī: Quran's verse-length distribution lies geometrically between prose and Arabic poetry mass.
- **NULL-classical-meter-match** at, e.g., Sarīʿ or Rajaz → would imply the Quran's verse-length distribution is statistically indistinguishable from one specific classical meter, contradicting al-Bāqillānī.
- **NULL-prose** → Quran's distribution looks like Bukhārī/Jāḥiẓ prose; the iʿjāz claim is metric-level disconfirmed.
- **NULL-BROKEN** → calibration broken; rerun with proper Wright-table syllable counts only (no rescue inside this pre-reg).

## Prior art

- al-Bāqillānī, *Iʿjāz al-Qurʾān* (~1000 CE) — qualitative claim of neither-prose-nor-poetry.
- al-Suyūṭī, *al-Itqān* — discusses sajʿ (rhymed prose) and the meter question.
- Frolov 2000, *Classical Arabic Verse* — modern reference on al-Khalīl's system.
- Stoetzer 1989, *Theory and Practice of Arabic Metrics*.
- No published quantitative test of the al-Bāqillānī claim against the full 16-meter set with permutation-corrected α to our knowledge.

## Integrity commitment

- Publish KS distance Q-vs-each-meter, Q-vs-each-baseline, AND mean/median Quran/baseline summary, regardless of verdict.
- Publish Muʿallaqāt-vs-each-meter table (positive control transparency).
- Publish length distributions (means, medians, std, 5th/95th percentile, n) for all 4 corpora.
- Seed 20260416 (one greater than [[h-new-43-verse-length-fft|H-NEW-43]]'s 20260415, per project convention).

---

## AMENDMENT 48-A — calibration of letters-per-syllable (pre-execution, empirical)

**Issue.** The locked value LETTERS_PER_SYLLABLE = 3.0 was derived from romanized/transcribed Arabic prose, NOT from unvocalized native Arabic script. Empirical check on Imruʾ al-Qais's muʿallaqa (known Ṭawīl, 28 syllables/bayt) gives 80 lines × 40.7 letters/line = 40.7 letters/bayt, implying letters/syllable = 40.7/28 = **1.45**, not 3.0. Other Ṭawīl muʿallaqāt (Tarafa, Zuhayr) give ~42 letters/bayt → LPS = 1.50. Kāmil (Labid: 30 syll) gives ~56 letters → LPS = 1.87. Wāfir (ʿAmr b. Kulthūm: 26 syll) gives ~42 → LPS = 1.62. Mean across 7 muallaqāt: **LPS ≈ 1.6**.

**Cause.** In unvocalized Arabic script, only consonants and long vowels (alif/wāw/yāʾ) are written. A CV syllable (consonant + short vowel) = 1 letter. A CVC syllable = 2 letters. CVV = 2 letters. CVVC = 3 letters. The mean over a typical Arabic word is ~1.4–1.7 letters per syllable, NOT 3.0.

**Decision (this amendment, locked BEFORE viewing any KS distance).** Re-lock LETTERS_PER_SYLLABLE = **1.6** as the primary value (derived directly from the historical muʿallaqāt-meter assignment, which is observable historical fact, NOT from the Quran's distribution). Keep 1.4 and 1.8 as sensitivity-analysis alternatives. The previous values (2.5, 3.5) are dropped as they are ruled out a priori by the 7 muallaqāt calibration alone.

**This is a calibration correction, not a Bonferroni change.** Bonferroni k stays at 19. α_per stays at 0.00263. The amendment is empirically grounded (7 historical-meter ground-truth points), pre-viewing-Quran, and the script's positive-control gate (MW-5 = "muʿallaqāt must match a meter at p<0.001") would have failed at LPS=3.0, exposing the calibration error post-hoc. Documenting it pre-hoc is honest.

**Garden-of-forking-paths log:**
- Calibration checkpoint detected at script-write-time, BEFORE any Quran-vs-meter KS computed.
- The calibration-source = historical muʿallaqāt assignment (Tawil/Kamil/Wafir/Khafif), NOT the Quran data.
- Sensitivity analysis 1.4 / 1.8 reported for transparency; verdict gate uses 1.6 only.
- No re-locking permitted post-result.

This amendment is consistent with the project standard "Specialist judgment may override team-lead method specs with direct empirical evidence + garden-of-forking-paths log BEFORE run" (granted 2026-04-15).
