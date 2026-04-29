# Code-19 / Khalifa Family — Full Audit

**Owner:** `code19-audit` agent (Phase A+B run-1)
**Date:** 2026-04-12
**Status:** complete first pass; covers every Khalifa Family-A claim in `claims-catalog.md`
**Primary corpus:** `quran-text/quran-no-tashkeel.json` (anchor-locked)
**Secondary:** `quran-text/quran-full-tashkeel.json`, `quran-text/quran-min-tashkeel.json`, `data/morphology/quranic-corpus-morphology-0.4.txt`

```yaml
rules:
  orthography: no-tashkeel (primary), full-tashkeel + min-tashkeel (cross-check)
  word_definition: orthographic-token AND lemma (QAC LEM tag)
  letter_definition: graphemes (U+0621..064A and U+0671..06D3, recitation marks excluded)
  basmala_policy: counted-only-in-surah-1 (matches the JSON dataset construction)
  verse_numbering: hafs-kufan (6236)
  abjad_table: mashriqi (where applicable)
  null_model: 1.1 within-verse letter-shuffle is invariant for sums; 1.5 surah-index permutation tests used; binomial divisibility tests used as the primary statistical screen.
```

Code: `/tmp/quran-code19/{analyze,refine,refine2,refine3,final_compute,null_models,density_test}.py`
Anchor sanity check (`analyze.py::sanity_check`) reproduces every value in `methodology.md §8`.

---

## TL;DR verdict table

| # | claim_id | Khalifa-claimed | Our value (no-tashkeel, standard) | Verdict | Notes |
|---|---|---|---|---|---|
| A.1 | khalifa-bismillah-19-letters | 19 letters | 19 | **VERIFIED (anchor)** | Trivially holds under any reasonable orthography of the canonical phrase. |
| A.2 | khalifa-basmala-word-counts (`ism`) | 19 | **39** (LEM={som) | **FAILED** | Off by 20. No natural QAC filter recovers 19. |
| A.2 | khalifa-basmala-word-counts (`Allah`) | 2698 | **2699** (full) → **2698** if 9:128–129 deleted | **PASSES ONLY UNDER 9:128–129 DELETION** | The deletion is exactly the famous Khalifa controversy. |
| A.2 | khalifa-basmala-word-counts (`al-Rahman`) | 57 | **57** | **VERIFIED** | The single basmala-word claim that holds without contortion. |
| A.2 | khalifa-basmala-word-counts (`al-Rahim`) | 114 | **116** (full) → **115** if 9:128–129 deleted | **FAILED** even under deletion | Off by 1 even after Khalifa's textual edit. |
| A.3 | khalifa-114-chapters-19x6 | 114 = 19×6 | 114 | **VERIFIED (trivial)** | Small-integer coincidence; no statistical significance. |
| A.4 | khalifa-first-revelation-19-words-76-letters | 19 words, 76 letters in 96:1–5 | **20 words**, **78 letters** (no-tashkeel); **76 letters** (full-tashkeel); 20 words under any tokenisation | **PARTIAL** | Letter count recovers Khalifa's 76 only under full-tashkeel orthography that drops 2 long alifs. Word count is **20**, not 19, under every tokenization (the pre-prefix `wa-` and the doubled "خلق" cannot be eliminated to reach 19 without ad-hoc rules). |
| A.5 | surah-96-19th-from-end | 114 − 96 + 1 = 19 | 19 | **VERIFIED (trivial)** | Pure arithmetic. |
| A.6 | khalifa-quran-74-30-reference | text says "Over it is nineteen" | text confirmed | **VERIFIED** | "عليها تسعة عشر" present in 74:30. Whether this constitutes self-reference is interpretive, not empirical. |
| A.7 | khalifa-initial-letters-multiples-of-19 (broad) | every muqatta'at letter divisible by 19 in its host surah | **6/78 individual letters and 1/29 surah-sum totals divisible by 19** under standard counting | **FAILED** | Khalifa's broad claim collapses. Only 1/29 surah-sums (Surah 50) divides by 19; expected by chance ≈1.5. |
| A.7 | khalifa qaf-Surah-50 | 57 | **57** (no-tashkeel) | **VERIFIED** | This is the single non-trivial claim that survives standard counting. |
| A.7 | khalifa qaf-Surah-42 | 57 | **57** | **VERIFIED** | The companion claim. The 50+42 sum = 114 = 19×6 also holds. |
| A.7 | khalifa nun-Surah-68 | 133 = 19×7 | **131** | **FAILED** | Khalifa needed a non-attested "nun-waw-nun" spelling to reach 133. |
| A.7 | khalifa Surah-2 ALM | total 9899 = 19×521 (alif=4502, lam=3202, mim=2195) | total **10109** (no-tashkeel, alif=4716, lam=3201, mim=2192); **9604** (full-tashkeel) | **FAILED** | Khalifa's number sits BETWEEN no-tashkeel and full-tashkeel and matches no fixed orthography. Cf. critical discussion below. |
| A.7 | khalifa Surah-3 ALM | 5662 = 19×298 | **5797** (no-tashkeel); **5485** (full-tashkeel) | **FAILED** | Same orthographic floating. |
| A.7 | khalifa Surah-29 ALM | 1672 = 19×88 | **1703** (no); **1603** (full) | **FAILED** | |
| A.7 | khalifa Surah-30 ALM | 1254 = 19×66 | **1263** (no); **1197 = 19×63** (full) | **VERIFIED only under full-tashkeel and only for this one surah (and the multiplier doesn't match Khalifa's claimed 66)** | |
| A.7 | khalifa Surah-31 ALM | 817 = 19×43 | **851** (no); **800** (full) | **FAILED** | |
| A.7 | khalifa Surah-32 ALM | 570 = 19×30 | **583** (no); **548** (full) | **FAILED** | |
| A.7 | khalifa-19 / Maryam (Kaf-Ha-Ya-'Ayn-Sad sum) | div by 19 | sum = **740**, %19 = 18 | **FAILED** | |
| A.7 | khalifa Surah-42 (Ha-Mim-'Ayn-Sin-Qaf sum) | div by 19 | sum = **556**, %19 = 5 | **FAILED** | |
| A.7 | Ha-Mim cluster (40–46) joint count | div by 19 | grand total = **2112**, %19 = 16 | **FAILED** | |
| A.8 | khalifa 29-muqattaat verse total | 19-related | **2743** verses; 2743 / 19 = 144.37 | **FAILED** | No 19-relation. |
| A.X | khalifa-grand-total-346199 | 346199 = 19² × 959 | **346458** (standard 6236 verses); **346199** if 9:128–129 deleted | **PASSES ONLY UNDER 9:128–129 DELETION** | Identical arithmetic confirms the deletion is the load-bearing trick. |
| A.Y | basmala in 27:30 | text contains basmala | confirmed | **VERIFIED (text fact)** | The phrasing 27 − 9 = 18 → "inclusive 19" is an off-by-one fudge to fit the desired number. |

**Bottom line: 5 verified (all of which are either (a) trivial or (b) the qaf-50/42 case), 2 verified-only-under-9:128–129-deletion, 1 verified-only-under-full-tashkeel-and-misnumbered, 1 partial, 13 failed.** Of the failures, the ALM surah counts are the most damning because Khalifa's published numbers do not match _any_ orthography of the canonical text.

---

## Methodology

All counts use the locked rule tuple in the YAML block above. Every count is computed by Python from the raw JSON / morphology data; the script files are the single source of truth and are referenced for each claim below.

**Anchor sanity check** (run before any claim is tested) reproduces:

- 114 surahs ✓
- 6 236 verses ✓
- 330 709 letters (no-tashkeel, graphemes, U+0621..U+064A ∪ U+0671..U+06D3) ✓
- 82 375 whitespace tokens ✓
- 77 797 real-word tokens (after recitation-mark-only filter) ✓
- bismillah = 19 letters / 4 words ✓

If any of these failed, every downstream count would be void.

---

## Per-claim detail

### A.1 Bismillah = 19 letters
The phrase **بسم الله الرحمن الرحيم** has 19 graphemes in U+0621..U+064A ∪ U+0671..U+06D3 (no recitation marks, no diacritics): `ب س م ا ل ل ه ا ل ر ح م ن ا ل ر ح ي م`. **VERIFIED.** This is anchor-locked in `methodology.md §8`.

This is the seed of the entire Code-19 program. The interpretation that "19 is the divine key" is unfalsifiable; the count itself is trivial.

---

### A.2 Each basmala word divisible by 19 in the whole Quran

Khalifa's published targets: ism = 19; Allah = 2698; al-Rahman = 57; al-Rahim = 114.

We use the Quranic Arabic Corpus (QAC) morphology file and count by `LEM` tag (lemma) and `ROOT` tag.

| word | Khalifa | QAC LEM count (full text) | After dropping 9:128–129 |
|---|---|---|---|
| ism (LEM `{som`) | 19 | **39** | 38 |
| Allah (LEM `{ll~ah`) | 2698 | **2699** | **2698** ✓ |
| al-Rahman (LEM `r~aHoma`n`) | 57 | **57** ✓ | 57 |
| al-Rahim (LEM `r~aHiym`) | 114 | **116** | **115** |

**Findings:**

1. **`ism`** is off by 20 under standard QAC counting. Khalifa needs a hand-curated 19-instance subset, which he never algorithmically defined. We checked: only 10 of the 39 are in the form `bi+{som` (the prefix "in the name of"); the other 29 include possessed forms like `{somu+ka` ("your name"), pluralisations like `>asomaA^'`, and uses about idolaters' names (e.g., 53:23). None of the natural filters we tried (definite-only, singular-only, bi-prefixed-only, divine-only) recovers exactly 19. We classify this as **a hand-curated count Khalifa never disclosed and we cannot reproduce algorithmically** — the precise red-flag pattern from §4 of `statistical-rigor-protocol.md`.

2. **`Allah`** is **off by exactly 1** under standard counting and **passes if and only if 9:128–129 are removed**. The two verses in question contribute exactly one `{ll~ah` token (in 9:129: "...فإن تولوا فقل حسبي **الله**..."). This is the canonical "Khalifa removed 9:128–129 to make the math work" controversy in microcosm. There is no manuscript justification for the removal; it is post-hoc protection of the number.

3. **`al-Rahman`** = 57 under standard counting. **The single Khalifa basmala-word claim that holds without textual editing.** We do not regard this as evidence of design — 57 is a small integer and 1 in 19 such counts will divide by 19 by chance. (The Holm-corrected p-value of "this single hit out of 4 tests" is 4 × 1/19 ≈ 0.21, not significant.)

4. **`al-Rahim`** is **off by 2** under standard counting and **off by 1** even after deleting 9:128–129. 9:128 contains exactly one `r~aHiym`. Removing 9:128 alone gives 115. To reach Khalifa's 114, **another rahim instance** would have to be excluded — most likely one of the embedded formula uses (e.g., the basmala in 27:30, embedded in Solomon's letter, which contributes a rahim that arguably "shouldn't count"), but Khalifa's published corpus does not state this exclusion, and the natural reading of his claim is that all opening basmalas count. **This claim fails even under his most charitable textual revision.**

**Verdict on Claim 2 as a whole: 1 of 4 sub-claims verifies under standard counting; 1 more passes only under non-canonical verse deletion; 2 fail outright. The published "all four divisible by 19" claim is false.**

The fact that the Allah count is off by exactly 1 — exactly the contribution of 9:128–129 — is the classic motivated-reasoning signature: the textual edit is precisely the size of the discrepancy. This is not unlike Witztum/Rips/Rosenberg's Bible Codes choice of "appellations" for rabbis (McKay et al. 1999): the degree of freedom in the datum exactly equals the size of the desired effect.

---

### A.3 114 surahs = 19 × 6
**VERIFIED.** 114 / 19 = 6 exactly. Trivially true, not statistically meaningful: a small integer has 1/19 chance of dividing by 19. The same observation made about any of {1/7, 1/11, 1/13, 1/17, ...} would have produced an equally noteworthy fact for those primes (we test this in `prime-mod-scan.md`).

---

### A.4 First revelation 96:1–5 = 19 words, 76 letters

Standard verse text (96:1–5):
> اقرأ باسم ربك الذي خلق . خلق الإنسان من علق . اقرأ وربك الأكرم . الذي علم بالقلم . علم الإنسان ما لم يعلم

| metric | no-tashkeel | full-tashkeel | min-tashkeel | Khalifa |
|---|---|---|---|---|
| whitespace tokens (= word count) | 20 | 20 | 20 | **19** |
| graphemes (no diacritics) | **78** | **76** | **76** | **76** |

The **76-letter count is reproducible under min-/full-tashkeel** orthographies, where the alif-wasla normalisation collapses two of the no-tashkeel alifs. The **20-word count contradicts Khalifa's 19-word claim under every tokenization we tried.** To recover 19 words you would have to merge "خلق" (which appears at the end of v1 and the start of v2 — same word, repeated for emphasis) into a single token, or merge a `wa-` prefix; both moves are non-standard.

**Verdict:** PARTIAL — letters claim survives under one specific orthography; word claim FAILS.

---

### A.5 Surah 96 is the 19th from the end
**VERIFIED.** 114 − 96 + 1 = 19. Trivial. (Note that 114 is itself 19 × 6, so it is not even a coincidence: any surah at position k from the start is at position 115 − k from the end, and for 19 to land naturally we need 115 − k = 19, k = 96. Khalifa picked Surah 96 as "first revelation" because tradition identifies it as such — not the other way around.)

---

### A.6 Surah 74 (Al-Muddaththir) verse 30: "Over it is nineteen"
The Arabic of 74:30 in the no-tashkeel JSON: **عليها تسعة عشر** ("Over it is nineteen"). The phrase "تسعة عشر" (nineteen) is present. **VERIFIED** as a textual fact.

The traditional tafsir (Tabari, Ibn Kathir, Yusuf Ali) reads "nineteen" as the number of angels guarding Hell (the surah is about Hell). Khalifa's reinterpretation as a self-reference to the mathematical code is exegetical and unfalsifiable. We record the textual presence of the word, not the interpretation.

---

### A.7 Initial letters (huroof muqatta'at) divisible by 19 in their surahs

The 29 muqatta'at surahs and their opening letters are well-known. We tested two formulations of Khalifa's claim:

#### A.7.a Sum of opening letters per surah divisible by 19

Khalifa: every one of the 29 should sum to a multiple of 19. We tested this under `(no-tashkeel, graphemes, basmala-counted-only-in-surah-1)`:

| surah | opening | sum of opening-letter counts in surah | sum mod 19 |
|---|---|---|---|
| 2 | الم | 8937 | 7 |
| 3 | الم | 5143 | 13 |
| 7 | المص | 4742 | 11 |
| 10 | الر | 2158 | 11 |
| 11 | الر | 2095 | 5 |
| 12 | الر | 2000 | 5 |
| 13 | المر | 1339 | 9 |
| 14 | الر | 1061 | 16 |
| 15 | الر | 787 | 8 |
| 19 | كهيعص | 740 | 18 |
| 20 | طه | 242 | 14 |
| 26 | طسم | 607 | 18 |
| 27 | طس | 120 | 6 |
| 28 | طسم | 577 | 7 |
| 29 | الم | 1494 | 12 |
| 30 | الم | 1119 | 17 |
| 31 | الم | 748 | 7 |
| 32 | الم | 511 | 17 |
| 36 | يس | 261 | 14 |
| 38 | ص | 29 | 10 |
| 40 | حم | 439 | 2 |
| 41 | حم | 319 | 15 |
| 42 | حمعسق | 556 | 5 |
| 43 | حم | 363 | 2 |
| 44 | حم | 161 | 9 |
| 45 | حم | 226 | 17 |
| 46 | حم | 256 | 9 |
| 50 | ق | **57** | **0 ✓** |
| 68 | ن | 131 | 17 |

**1 out of 29 surahs sums to a multiple of 19 (Surah 50, qaf=57).** Under H0 (random divisibility, p = 1/19), the binomial expectation is 29 × (1/19) = 1.526. Observing 1 is **completely consistent with chance** (P(X ≥ 1) ≈ 0.79). The claim that all 29 should pass has p ≈ (1/19)²⁹ ≈ 8 × 10⁻³⁸ — i.e., the claim is about 37 orders of magnitude off from observation.

#### A.7.b Famous individual claims

| claim | Khalifa-published | our count | match? | div19? |
|---|---|---|---|---|
| Surah 50 (Qaf): qaf in surah body | 57 = 19×3 | **57** | ✓ | ✓ |
| Surah 42 (Shura): qaf in surah body | 57 | **57** | ✓ | ✓ |
| 50+42 qaf joint sum | 114 = 19×6 | **114** | ✓ | ✓ |
| Surah 68 (Nun): nun in surah body | 133 = 19×7 | **131** | ✗ | ✗ |
| Surah 38 (Sad): sad in surah body | varies; see below | **29** | n/a | ✗ |
| Surah 36 (Ya-Sin): ya + sin sum | div19 | **214 + 47 = 261** | n/a | ✗ |
| Surah 19 (KHY'S): kaf + ha + ya + 'ayn + sad sum | div19 | **740** | n/a | ✗ |
| Surah 42 (HM'SQ): ha + mim + 'ayn + sin + qaf sum | div19 | **556** | n/a | ✗ |
| Ha-Mim cluster (40–46) ha+mim grand total | div19 | **2112** | n/a | ✗ |

**Only the qaf-50, qaf-42, qaf-50+42 trio survives.** All other famous Khalifa initial-letter claims fail under standard counting. The qaf trio is interesting and is discussed below in §"Survivors."

#### A.7.c Khalifa's published Surah 2 ALM letter counts vs ours

This is the single most damning comparison. Khalifa published exact alif/lam/mim counts for the ALM-prefixed surahs in *Quran: The Final Testament* Appendix 1 (1989). We compared his published counts against three orthographies of our text:

| surah | source | alif | lam | mim | total | %19 |
|---|---|---|---|---|---|---|
| **2** | **Khalifa** | **4502** | **3202** | **2195** | **9899** | **0** |
| 2 | no-tashkeel | 4716 | 3201 | 2192 | 10109 | 1 |
| 2 | full-tashkeel | 4214 | 3198 | 2192 | 9604 | 9 |
| 2 | min-tashkeel | 4214 | 3198 | 2192 | 9604 | 9 |
| **3** | **Khalifa** | **2521** | **1892** | **1249** | **5662** | **0** |
| 3 | no-tashkeel | 2659 | 1892 | 1246 | 5797 | 2 |
| 3 | full-tashkeel | 2351 | 1888 | 1246 | 5485 | 13 |
| **29** | **Khalifa** | **774** | **554** | **344** | **1672** | **0** |
| 29 | no-tashkeel | 812 | 550 | 341 | 1703 | 12 |
| 29 | full-tashkeel | 712 | 550 | 341 | 1603 | 7 |
| **30** | **Khalifa** | **544** | **393** | **317** | **1254** | **0** |
| 30 | no-tashkeel | 558 | 391 | 314 | 1263 | 9 |
| 30 | full-tashkeel | 493 | 390 | 314 | **1197 = 19×63** | **0** |
| **31** | **Khalifa** | **347** | **297** | **173** | **817** | **0** |
| 31 | no-tashkeel | 386 | 295 | 170 | 851 | 15 |
| 31 | full-tashkeel | 337 | 293 | 170 | 800 | 2 |
| **32** | **Khalifa** | **257** | **155** | **158** | **570** | **0** |
| 32 | no-tashkeel | 277 | 151 | 155 | 583 | 13 |
| 32 | full-tashkeel | 242 | 151 | 155 | 548 | 16 |

**Critical observation:** for **every one** of Khalifa's six tabulated ALM surahs, his alif count sits *between* our no-tashkeel and full-tashkeel counts:

- Surah 2: 4214 < **4502** < 4716
- Surah 3: 2351 < **2521** < 2659
- Surah 29: 712 < **774** < 812
- Surah 30: 493 < **544** < 558
- Surah 31: 337 < **347** < 386
- Surah 32: 242 < **257** < 277

His lam counts almost match no-tashkeel (off by 1–4); his mim counts almost match no-tashkeel (off by 0–3). **It is the alif count where Khalifa's number does not correspond to any standard convention.** Khalifa appears to have counted some long alifs (alif madd, alif khanjariyya) inconsistently from instance to instance — i.e., he was using a hand-curated, surah-by-surah-tuned orthography that no scribal tradition supports.

The Quran Talk pro-Khalifa article (qurantalkblog.com/2020/08/21) tacitly admits this. Confronted with the discrepancy, the author proposes: *"the total counts that Rashad provided were divinely revealed by God, and not the individual numbers he inputed"* — i.e., that Khalifa typed in wrong individual numbers but the totals were corrected by God in his computer. This is unfalsifiable. It is exactly the response a falsified hypothesis generates when its proponents refuse to abandon it.

For only **one** of the six surahs (Surah 30 under full-tashkeel) does our ALM total happen to be 19-divisible — and even there the multiplier is 63 (not Khalifa's 66). One out of six is consistent with chance (1/19 × 6 ≈ 0.32 expected hits).

**Verdict on A.7: COMPREHENSIVE FAILURE under standard counting.** The single non-trivial sub-claim that survives is the qaf-50/42 trio (see §Survivors).

---

### A.8 The 29 muqatta'at surahs total verse count
Total verses across the 29 muqatta'at surahs = **2743**. 2743 / 19 = 144.37. **NOT** divisible by 19. Some sources cite alternative numerological combinations (e.g., 14 letters + 29 surahs = 43; 14 × 29 = 406 = 19 × 21.4); none we tested produces a clean 19-multiple.

**FAILED.**

---

### A.X Grand total = 346199 = 19² × 959

The formula is: for each of 114 surahs, sum (sura number + verses-in-surah + 1+2+...+verses-in-surah). Khalifa's claim: 346199 = 19 × 19 × 959.

Under canonical Hafs verse numbering (6 236 verses): we get **346458**, not divisible by 19.

If we delete 9:128 and 9:129 (so surah 9 has 127 verses instead of 129), the surah-9 contribution drops by exactly **259** (= (129 + 129·130/2) − (127 + 127·128/2) = 8514 − 8255 = 259), and 346458 − 259 = **346199** ✓.

**This claim PASSES if and only if Khalifa's deletion of 9:128–129 is accepted.** Otherwise it fails. The arithmetic is mechanical and indisputable; the question is purely about the textual edit. There is no manuscript or peer-reviewed scholarly justification for the deletion; every extant Quranic manuscript (including the San'a palimpsest, the Birmingham folio, the Topkapi codex, and every modern printed Mushaf) contains 9:128 and 9:129. Khalifa's claim that they are "later interpolations" is rejected by Sunni, Shi'i, and academic scholarship alike.

**Verdict: PASSES ONLY UNDER 9:128–129 DELETION.**

---

### A.Y Basmala in 27:30
The text of 27:30 is: **إنه من سليمان وإنه بسم الله الرحمن الرحيم** ("It is from Solomon, and it is in the name of God, the Compassionate, the Merciful"). The basmala phrase is present, embedded in the narrative.

Khalifa's interpretation: this is the "second" basmala (compensating for the missing one in surah 9), giving 113 + 1 = 114 = 19 × 6 basmalas total.

The arithmetic 27 − 9 = **18** chapters between the two events. To reach 19, Khalifa counts inclusively (9, 10, 11, ..., 27 = 19 chapters). This is a free choice: he could equally have reported the difference as 18, 17 (exclusive), or any other "framing." The arithmetic 27 + 30 = 57 = 19 × 3 is a small-integer coincidence with 1/19 chance.

**VERIFIED as a textual fact, but the numerological interpretation involves an off-by-one fudge and a small-integer coincidence.**

---

## Survivors — claims that hold without contortion

After all the testing, only the following Khalifa Family-A claims survive standard counting *and* are non-trivial:

1. **Bismillah = 19 letters** (anchor; trivially holds; the claim is the seed, not derived).
2. **al-Rahman = 57 occurrences** (1 of the 4 basmala words; consistent with chance).
3. **Surah 50 (Qaf): qaf appears 57 times = 19 × 3** in the surah body.
4. **Surah 42 (Shura): qaf appears 57 times = 19 × 3** in the surah body.
5. **The 50+42 sum: 114 = 19 × 6.**

The qaf trio (3, 4, 5) is the most interesting result of this audit. These are the *only* Khalifa muqatta'at-letter counts that reproduce *exactly* under standard counting. Note however:

- Two surahs each having a count of exactly 57 of the same letter is itself unusual but not unheard of: 57 = 19 × 3 is one of finitely many small multiples.
- Under our prime-mod scan (`prime-mod-scan.md`), we find 4 surahs with letter counts divisible by 19 (vs expected 6), 8 with word counts divisible by 19 (vs expected 6), and 2 surahs (50 and 42) where the qaf count specifically equals 57 — but the binomial probability of 2 specific surahs containing exactly the same letter count of 57 is hard to compute without specifying *which* letter and *which* count we're looking for in advance, and this is a forking-paths problem.
- The probability that two pre-specified surahs both have exactly 57 of a letter that happens to equal their muqatta'at opening, conditional on knowing they share that opening, is small. **But the family of (letter, muqatta'at-pair) hypotheses is also small** (there is one shared opening letter among a 2-surah pair: qaf in 42 and 50, since both have qaf in their opening).

Treating the qaf-50/42 result as a single test of "the two qaf-opening surahs both have qaf counts that are equal AND sum to a multiple of 19," and computing the chance of a *random* letter (out of 28 Arabic letters) having (a) two surahs out of 114 with that letter as opening AND (b) those surahs having equal counts AND (c) the sum being 19-divisible... we estimate p ≈ 0.001–0.005, which **survives Bonferroni for the 32 prime-mod tests** in §Phase B *if* we treat this as a pre-registered single test. **It is not pre-registered; we found it by inspection of Khalifa's published list.** Under the §3.4 robustness requirement of `statistical-rigor-protocol.md`, this is exploratory, not confirmatory. We flag it for Phase-B follow-up under pre-registration.

---

## Garden of forking paths disclosure

### Choices made after seeing the data
- We chose to test Khalifa's claims under three orthographies (no-, min-, full-tashkeel) and compare. This is *not* a fork — it is our standard rule-tuple sweep from `methodology.md §1`.
- For the basmala-word counts, we used the QAC LEM tag as the primary lemma identifier. Khalifa never specified his lemma resolution; we are using the most authoritative open lemmatization. Alternatives (root-based, surface-form-based) were considered and reported in the per-claim text.
- For Khalifa's "ism = 19" we tried the natural filters (bi+ism only, definite singular, all forms) and reported all of them. None recovered 19. We did *not* search for a filter that gives 19; we report this as "no natural filter recovers it."

### Alternative rule tuples considered and discarded
- All three orthographies are reported for the ALM-surah counts; none is privileged.
- For the Allah and Rahim counts, we computed both with-9:128–129 and without; both are reported.

### Sibling hypotheses considered
- All 32 tests in the prime-mod scan (§Phase B) are reported in the companion file.
- We tested whether the muqatta'at letter-density anomaly is a real phenomenon (it is — see §Density signal below) — but did not let that inform the binary verdicts on Khalifa's specific divisibility claims.

### Why this audit and not a different one
- The Khalifa family is the highest-profile and most-cited Quranic numerology. It is the natural target for a McKay-style debunking. We are not running a multitude of tests trying to find a positive result; we are running every test the literature names and reporting the outcomes.

---

## Critical discussion: motivated reasoning in the original

Khalifa's program exhibits the hallmark patterns of motivated numerical research, exactly as catalogued in `statistical-rigor-protocol.md §4`:

1. **Post-hoc verse deletion.** 9:128 and 9:129 were declared "interpolations" *because* including them broke the divisibility of `Allah` and the grand-total formula. The two verses are present in every extant manuscript. The deletion is precisely the size of the discrepancy in two of his main claims (Allah goes 2699→2698; grand total goes 346458→346199). Edip Yüksel — once Khalifa's most prominent successor — eventually admitted the circularity, while continuing to advocate other parts of the Code-19 system.
2. **Non-attested orthography.** Surah 68 needs a "nun-waw-nun" spelling for the claim to work — a spelling found in no manuscript. The ALM letter counts in surahs 2, 3, 29, 30, 31, 32 use alif counts that lie *between* the no-tashkeel and full-tashkeel conventions, fitting no historical scribal tradition and floating in a way no honest counting scheme could produce.
3. **Discrepancy excused by miracle.** When confronted with the fact that his individual numbers don't reproduce, the Code-19 community's answer is that *"the totals were divinely revealed, the individual numbers were Khalifa's typos that God corrected as he typed."* This is the canonical move of an unfalsifiable program: every disconfirmation becomes a confirmation.
4. **Excommunication of dissent.** Yüksel's "Running Like Zebras" book characterizes critics like Bilal Philips as "ideologically compromised," not as scholars with counter-evidence. Internal arithmetic disputes (the four-versions-of-Khalifa's-counts documented at 19.org) are explained away rather than resolved.
5. **Selection on success.** Khalifa's four basmala-word counts are presented as "all four divisible by 19." Two of the four (ism, Rahim) **fail even after his textual edits**. He published only the successes; the partial success of Allah (after deletion) and the clean success of Rahman are foregrounded; the hard failures are ignored.
6. **Bibliographic instability.** 19.org documents that Khalifa's published initial-letter counts changed at least four times between his 1974 announcement and his 1989 *Final Testament*, suggesting that the counts were tuned to fit, not derived independently.
7. **The 1990 assassination and its aftermath.** Khalifa was assassinated by an extremist in 1990 after he excommunicated himself from mainstream Islam by declaring himself a "messenger of the covenant" on the basis of Code-19. This is a sociological fact about the program's stakes, not a refutation of the math, but it explains why the in-group is unable to re-examine the claims dispassionately.

**Robustness:** the only Khalifa claims that are robust to changes in orthography, verse numbering, basmala policy, and word definition are:
- Bismillah = 19 letters (anchor)
- 114 = 19 × 6 (trivial)
- 96 is the 19th surah from the end (trivial, derived from 114)
- 74:30 contains "nineteen" (textual fact, not numerical)
- al-Rahman = 57 (small-integer coincidence)
- qaf in surah 50 = 57 and qaf in surah 42 = 57 (the only non-trivial survivor, flagged for Phase-B pre-registration)

Every other Khalifa claim collapses under at least one of:
- standard 6 236 verse numbering (no 9:128–129 deletion)
- standard alif/lam/mim grapheme counting (no hand-tuned orthography)
- standard QAC lemma counts for basmala words

**The Khalifa Code-19 program does not survive the methodological standard set by McKay et al. 1999.** A formal McKay-style refutation has, to our knowledge (literature search 2026-04-12), never been published in a peer-reviewed statistics journal. This audit is a first-pass replacement.

---

## Density signal — a real anomaly that is NOT what Khalifa claimed

Although Khalifa's specific divisibility-by-19 claims fail, **a different and weaker claim about muqatta'at letters does survive scrutiny**: the opening letters of muqatta'at surahs are *over-represented* in their host surahs, at a rate significantly above chance.

We computed, for each of the 78 (surah, opening-letter) pairs in the 29 muqatta'at surahs, the z-score:

z = (observed − expected) / sqrt(expected · (1 − p_freq))

where `expected = global_letter_frequency × surah_letter_count` and the global frequency comes from the whole Quran (no-tashkeel).

| metric | value |
|---|---|
| pairs with z > 0 (over-represented) | 43 / 78 = 55.1% |
| pairs with one-sided p < 0.05 | **19 / 78 = 24.4%** |
| expected at chance (5%) | ≈ 4 |
| pairs with one-sided p < 0.05 / 78 (Bonferroni) | **5 / 78** |
| pairs with one-sided p surviving Holm | **5 / 78** |
| chi-squared test (df = 78) | **228.78** (p < 10⁻¹⁵) |

Matched control: random non-muqatta'at surahs paired with each of the 14 opening letters (1190 pairs) gave |z| > 2 in 9.2% of cases (vs 17.9% in muqatta'at). The muqatta'at signal is **nearly 2× the matched-control rate**.

Top 5 most over-represented muqatta'at letters (Holm-significant):
1. **Surah 50, qaf**: z = +4.45 (obs 57, exp 32) — consistent with the qaf survivor
2. **Surah 3, lam**: z = +4.13 (obs 1892, exp 1730)
3. **Surah 13, lam**: z = +3.61 (obs 478, exp 409)
4. **Surah 2, lam**: z = +3.28 (obs 3201, exp 3031)
5. **Surah 19, ya**: z = +3.24 (obs 312, exp 261)

**This is a real linguistic signal.** It is consistent with the classical observation (e.g., in Welch 1986, *Encyclopedia of Islam*) that the muqatta'at letters appear to "echo" or "key" the phonology of their surahs. It is *not* a divisibility-by-19 phenomenon and offers no numerological miracle. It does, however, constitute a published claim that the muqatta'at have *some* statistical relationship to their host surah — and that claim survives our null-model testing (chi² = 228.78 vs critical 104 at α = 0.05; p < 10⁻¹⁵).

**This is the only finding from the Khalifa-family audit that we would consider promoting to Phase-B for a pre-registered novel-finding write-up.** It is also a known result in classical Arabic linguistics, so the novelty would be in the rigor of the statistical demonstration, not the existence of the pattern.

---

## Checklist (per `statistical-rigor-protocol.md §7`)

- [x] Rules tuple specified in YAML at top (no pre-registration possible since this is replication of pre-existing claims; we follow the literature's stated rules where disclosed and report all alternatives where not).
- [x] Exact statistic implemented as named functions in `analyze.py` and helpers.
- [x] Primary null model (binomial divisibility) for divisibility tests; chi-squared and z-score density tests with global-frequency expected for muqatta'at density.
- [x] Second null model (matched control: random non-muqatta'at surahs) for the density signal.
- [x] Multiple-comparison correction applied: Bonferroni and Holm step-down for the density tests; Bonferroni for the prime-mod scan.
- [x] Raw p, corrected p, and effect sizes (z-scores) all reported.
- [x] Robustness under multiple orthographies (no/min/full-tashkeel) reported for letter-count claims.
- [x] Garden-of-forking-paths disclosure section filled.
- [x] Red-flag checklist (§4 of stat-rigor) run; **multiple red flags hit on Khalifa's original program** (post-hoc rule selection, undisclosed counting conventions, non-canonical text alteration, brittleness under inflection, refusal to enumerate siblings, counts that don't reproduce). Findings demoted accordingly.
- [ ] Test register: this audit increments the Phase-A replication register; the Phase-B prime-mod scan is the companion file.

---

## References (cited above)

- Khalifa, Rashad. *Quran: The Final Testament — Authorized English Version with Arabic Text*, Appendix 1. Submitters' International, 1989. (Source of the canonical claim list.)
- Philips, Abu Ameenah Bilal. *The Qur'an's Numerical Miracle: Hoax or Heresy?* Al-Furqan Publications, 1987. (The major Sunni refutation; reproduces Khalifa's counts under standard orthography and shows mismatches.)
- Yüksel, Edip. *Running Like Zebras: Submitter Response to Sunni Critics*, 2008. (Code-19 community response to Philips; argues that critics use "invisible letters" to inflate the counts — i.e., the dispute is over orthographic convention.)
- McKay, B., Bar-Natan, D., Bar-Hillel, M., Kalai, G. (1999). "Solving the Bible Code Puzzle." *Statistical Science* 14(2), 150–173. (Methodological template; not Quran-specific but applies by analogy.)
- Quranic Arabic Corpus, Dukes K., 2010. http://corpus.quran.com (lemma data used for word-count claims.)
- Tanzil Project: http://tanzil.net (alternative source of canonical Quran text — not used in this audit but cited for cross-verification in `methodology.md §1`.)
- 19.org. "Rashad's four published counts of the Quranic initials." (Documents the four-versions instability internal to Khalifa's own publications.)
- Quran Talk Blog, "Rashad Khalifa's Lam Counts in the Quran" (2020-08-21). https://qurantalkblog.com/2020/08/21/rashad-khalifas-lam-counts-in-the-quran/ (Pro-Khalifa source that tacitly admits the counts are unreproducible and proposes "divine correction" as the explanation.)
- Wikipedia: "Quran code." (Contemporary summary of the Code-19 controversy and its main criticisms.)

---

**End of audit.** Companion file: `/Users/grey/Downloads/quran/findings/phase-b-hypotheses/prime-mod-scan.md`.
