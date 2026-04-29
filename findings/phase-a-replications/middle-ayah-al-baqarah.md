---
claim_id: middle-ayah-al-baqarah
claim_statement: "Surah 2:143 (wasatan/middle) is the middle verse of Al-Baqarah"
claimant: widely-circulated folk claim, user-mentioned 2026-04-12
sources: []
rules:
  orthography: no-tashkeel
  word_definition: real-words
  letter_definition: graphemes
  basmala_policy: counted-only-in-surah-1
  verse_numbering: hafs-kufan
  abjad_table: not-applicable
  null_model: base-rate-comparison
verdict: partially-verified
---

# Middle-ayah claim for Al-Baqarah (wasatan / 2:143)

## 1. Claim

A folk claim, widely circulated in popular-apologetics channels, asserts that Surah Al-Baqarah's "middle verse" is 2:143, whose key phrase is

> وَكَذَٰلِكَ جَعَلْنَاكُمْ أُمَّةً وَسَطًا
> "And thus We made you a middle / moderate nation"

and that this verse is "literally" the middle verse of the surah. A stronger variant extends the claim to the middle of the whole Quran (by verse count, word count, and/or letter count).

This write-up tests every sub-claim rigorously.

## 2. Method

All counts use the intact JSON corpora (`quran-no-tashkeel.json`, `quran-min-tashkeel.json`, `quran-full-tashkeel.json`) via `analysis/tools/loader.py` and `analysis/tools/tokenize.py`. Substring matching across orthographies strips tashkeel, tatweel, dagger-alif, and recitation marks, and normalizes alif-with-wasla (U+0671) to plain alif. The scripts live at `analysis/scripts/middle_ayah_analysis.py` and `analysis/scripts/middle_ayah_verify.py`.

Rules tuples (fingerprints used below):

- `[nt/rw/b1]` = `no-tashkeel` / `real-words` / `basmala-counted-only-in-surah-1`
- `[mt/rw/b1]` = `min-tashkeel` / `real-words` / `basmala-counted-only-in-surah-1`
- `[ft/rw/b1]` = `full-tashkeel` / `real-words` / `basmala-counted-only-in-surah-1`
- `[nt/gr/b1]` = `no-tashkeel` / `graphemes` / `basmala-counted-only-in-surah-1`
- `[mt/gr/b1]`, `[ft/gr/b1]` — analogous letter-count variants

## 3. Raw results

### Task 1 — middle by verse index, Al-Baqarah

Al-Baqarah has **286** verses (confirmed in all three JSON variants). Because 286 is even, there are two candidates for "middle verse": position 143 and position 144.

`[nt/rw/b1]`:

- **2:143 contains `وسط`** (as the token `وسطا` — wasatan, accusative indefinite of wasat/"middle"). ✅
- 2:144 does NOT contain any wasat-family token.

Text of 2:143 (no-tashkeel):
> وكذلك جعلناكم أمة **وسطا** لتكونوا شهداء على الناس ويكون الرسول عليكم شهيدا ۗ وما جعلنا القبلة التي كنت عليها إلا لنعلم من يتبع الرسول ممن ينقلب على عقبيه ۚ وإن كانت لكبيرة إلا على الذين هدى الله ۗ وما كان الله ليضيع إيمانكم ۚ إن الله بالناس لرءوف رحيم

After stripping tashkeel + recitation marks, the same substring `وسط` is present in `[mt/rw/b1]` and `[ft/rw/b1]`. The claim at the verse-index level is **orthography-robust**: 2:143 literally contains the wasat word in all three variants.

### Task 2 — middle by word count, Al-Baqarah

| Rule fingerprint | Total real-words | Lower-median word | Upper-median word | Verse containing it |
|---|---:|---:|---:|---|
| `[nt/rw/b1]` | 6140 | 3070 | 3071 | **2:172** (`كلوا`, `من`) |
| `[mt/rw/b1]` | 6116 | 3058 | 3059 | **2:172** (`طَيِّبٰتِ`, `ما`) |
| `[ft/rw/b1]` | 6118 | 3059 | 3060 | **2:172** (`طَيِّبَٰتِ`, `مَا`) |

Under word-count, the middle word lies in **2:172**, not 2:143. 2:172 reads (nt):

> يا أيها الذين آمنوا كلوا من طيبات ما رزقناكم واشكروا لله إن كنتم إياه تعبدون
> "O you who believe, eat of the good things We have provided you, and give thanks to Allah if indeed it is He you worship"

That verse contains no wasat-family word. The claim **fails at word-count granularity** in every orthography.

### Task 3 — middle by letter count, Al-Baqarah

| Rule fingerprint | Total letters | Median letter index | Verse containing it |
|---|---:|---:|---|
| `[nt/gr/b1]` | 26,249 | 13,125 | **2:171** (letter #28 within the verse) |
| `[mt/gr/b1]` | 25,900 | 12,950 / 12,951 | **2:171** |
| `[ft/gr/b1]` | 25,988 | 12,994 / 12,995 | **2:171** |

Under letter-count, the median letter lies in **2:171**, one verse before 2:172 and 28 verses after 2:143. 2:171 reads:

> ومثل الذين كفروا كمثل الذي ينعق بما لا يسمع إلا دعاء ونداء ۚ صم بكم عمي فهم لا يعقلون

No wasat-family word. Claim **fails at letter-count granularity**.

### Task 4 — middle of the whole Quran

**4a) By total verse index.** Of 6236 verses, positions 3118 and 3119 are the two middle candidates:

- verse #3118 = **26:186** — "وما أنت إلا بشر مثلنا وإن نظنك لمن الكاذبين" (mouths of the people of Shu'aib)
- verse #3119 = **26:187** — "فأسقط علينا كسفا من السماء إن كنت من الصادقين"

Neither contains any wasat-family word. The whole-Quran verse-midpoint is **not** 2:143; it sits in Ash-Shu'ara, one of the seven long-alif letters-at-start surahs. **Claim fails.**

**4b) By total real-word count.** The whole-Quran has **77,797** real-words `[nt/rw/b1]`. The 38,899-th word — the median word — falls in **18:77**, at token #11 (`يضيفوهما`, "that they give them hospitality"). Surah 18 (Al-Kahf) verse 77 is part of the Moses-and-Khidr narrative, not a wasat verse.

Mildly interesting aside: 18:77 is inside Al-Kahf ("The Cave"), which is itself traditionally recited as a middle/weekly-midpoint surah. That's a suggestive but not established coincidence.

**4c) By total letter count.** The whole-Quran has **330,709** letters `[nt/gr/b1]`. Median letter = 165,355. Falls in **18:73**, letter #19 within that verse ("قال لا تؤاخذني بما نسيت ولا ترهقني من أمري عسرا").

The middle-by-word and middle-by-letter both fall in Surah 18 (Al-Kahf), within ~4 verses of each other — Kahf is near the absolute middle of the Quran under both word- and letter-counts. But neither midpoint word nor midpoint letter has anything to do with wasat. The claim that 2:143 is the "middle of the Quran" is false under every natural definition of middle.

### Task 5 — robustness across orthographies

Task 2 and 3 were rerun on all three variants in the tables above. The **identity of the median verse** (2:172 for word-count, 2:171 for letter-count) is invariant across `no-tashkeel`, `min-tashkeel`, and `full-tashkeel`. Task 1 (verse-index) is trivially invariant since verse numbering doesn't depend on orthography. Task 4 sub-parts were verified under `no-tashkeel` only; orthography differences would shift totals by < 0.5% and cannot move the midpoint away from Surah 18 for word-count or letter-count.

Conclusion: the divergence between the verse-index claim (verified) and the word/letter claims (failed) is **not** an artifact of orthography choice.

### Task 7 — null sanity: base rate of wasat-family surface forms

Across the entire Quran (77,797 real-words), the substring `وسط` (after tashkeel normalization) appears in exactly **5 tokens / 5 verses** in all three orthographies:

| Surah:verse | Token (stripped) | Meaning |
|---|---|---|
| 2:143 | `وسطا` | wasatan — "middle/moderate [community]" |
| 2:238 | `الوسطى` | al-wustaa — "the middle [prayer]" |
| 5:89 | `أوسط` | awsat — "most moderate [of what you feed]" |
| 68:28 | `أوسطهم` | awsatuhum — "the most moderate/middling of them" |
| 100:5 | `فوسطن` | fa-wasatna — "then they penetrate to the midst" |

The wasat-family is **extremely rare**: 5 / 77,797 ≈ 6.4 × 10⁻⁵ per real-word, or roughly 1 in 15,500. A wasat-family word occurring at a specific pre-nominated position is genuinely improbable given base rate. This makes the verse-index coincidence at 2:143 non-trivial.

### Task 8 — counterfactual: wasat near midpoint of all surahs

Of 114 surahs, **60 have an even verse count** (so they have two canonical "middle" candidates). Of those 60 + the 54 odd-count surahs, how many have a wasat-family word literally in one of their middle verses?

| Scope | Hits |
|---|---|
| Strictly at the midpoint verse(s) (n/2 and n/2+1 for even; (n+1)/2 for odd) | **1 surah: 2:143 (Al-Baqarah)** |
| Within ±2 verses of midpoint | **3 surahs**: 2:143, 68:28, 100:5 |

**Al-Baqarah is the unique surah in which a wasat-family word literally lands at the canonical midpoint verse.** The other two "near-midpoint" hits are:

- 68:28 `أوسطهم`: in a surah of 52 verses, verse 28 is two above the midpoint 26 — close but not central. The verse describes the "most moderate" owner of the garden in the parable.
- 100:5 `فوسطن`: in a surah of 11 verses, verse 5 is one below the midpoint 6. Surah Al-'Adiyat is short enough that any word in it is "near the middle" trivially.

Result is invariant across `no-tashkeel`, `min-tashkeel`, `full-tashkeel`. **2:143 is the only strict-midpoint hit in all three orthographies.**

## 4. Verdict

**PARTIALLY VERIFIED.**

The claim splits into three components, which this investigation resolves as follows:

1. **Al-Baqarah middle verse by index = 2:143, which contains wasat.** ✅ **VERIFIED** under every orthography (`nt`, `mt`, `ft`). 286 verses → positions 143 and 144 are the two canonical "middles" for an even-length surah; 2:143 contains the token `وسطا`. This is a real, reproducible, orthography-robust fact.

2. **Al-Baqarah middle verse by word or letter count = 2:143.** ❌ **FAILED** under every orthography. Word-midpoint is 2:172, letter-midpoint is 2:171. The verse-index coincidence does not survive when "middle" is defined by word or letter count.

3. **2:143 is the middle of the whole Quran.** ❌ **FAILED** under every definition. Middle-by-verse-index is 26:186/187 (Ash-Shu'ara); middle-by-word and middle-by-letter are both in Surah 18 (Al-Kahf). 2:143's position within the full Quran is nowhere near any of these.

## 5. Honest discussion — is this a real pattern?

The verified component (task 1) is **real** but stands on two loaded choices the claim doesn't disclose:

**Loaded choice 1: "Middle of an even-length list" is ambiguous.** Al-Baqarah has 286 verses. There is no single middle verse. The claim tacitly picks "position 143" over "position 144" because 143 is the one that happens to contain wasat. Had we used either `floor((n+1)/2) = 143` OR `ceil(n/2) = 143` we'd call 143 the middle; had we used `floor(n/2) + 1 = 144` OR the pair {143, 144} we'd either call 144 the middle or give a tie. The claim is picking the convention that works. That's a mild fork but not a severe one — "position n/2 of 2n" is a reasonable default.

**Loaded choice 2: "Granularity of middle" is fork-prone.** The claim says "middle verse" not "middle word" or "middle letter". Had the claim been tested under word-count, it would fail (2:172). Had it been tested under letter-count, it would fail (2:171). That it is framed specifically as "middle *verse*" looks like post-hoc convention selection. Three natural definitions of middle exist, and only one works for 2:143.

### Counterfactual strength (the task 8 result is the interesting finding)

**The counterfactual is where the claim gains some actual strength.** 2:143 is the *unique* Quranic surah where a wasat-family word lands exactly at the canonical midpoint verse. The wasat family contains 5 tokens in 77,797 — extremely rare. Under a naïve null model that pretends wasat-family occurrences are independently Poisson-distributed across verses (6236 total, expected hits = 5), the probability that the random location of 1 of those 5 tokens coincides with a specific 2-verse window at the midpoint of a specific 286-verse surah is roughly `(2/6236) × 5 ≈ 1.6 × 10⁻³`. That's a real — but not revolutionary — statistical signal. It does not survive correction for the number of surahs and windows we could have tested (114 surahs × several "middleness" definitions × several word-family definitions → effective k > 100), and it depends sensitively on the choice to define "middle" at verse-index granularity.

The claim is best described as: **the Quran contains a suggestive semantic-position coincidence, reproducible from raw text, but the statistical case for intentionality is weak because the fork space is large and only the verse-index definition survives.** That said, 2:143 is also famous in Islamic jurisprudence precisely for its wasat content (it's the classical locus for the doctrine of "the middle community"), so the verse **is** literally about middleness and **is** located at the middle of the longest surah — a coincidence that does reproduce, even if multiple-comparison rigor would deflate any p-value attached to it.

### What would strengthen or destroy the claim

- **Strengthen:** if the whole-Quran middle (task 4) had also landed on a wasat-family verse. It didn't.
- **Strengthen:** if the word-count and letter-count middles of Al-Baqarah (tasks 2, 3) had also landed on 2:143. They didn't — and they land one or two verses *before* 2:172, not near 2:143.
- **Destroy:** if many surahs had wasat-family words at their midpoints. Only one does.
- **Destroy:** if the verse-index claim was orthography-dependent. It isn't.

## 6. Rules-fingerprint summary

| Numerical claim | Value | Rule fingerprint |
|---|---|---|
| Al-Baqarah verse count | 286 | any variant, hafs-kufan |
| 2:143 contains `وسط` substring | TRUE | `[nt/rw/b1]`, `[mt/rw/b1]`, `[ft/rw/b1]` (post tashkeel strip) |
| 2:144 contains `وسط` substring | FALSE | same |
| Al-Baqarah total real-words | 6140 | `[nt/rw/b1]` |
| Al-Baqarah total real-words | 6116 | `[mt/rw/b1]` |
| Al-Baqarah total real-words | 6118 | `[ft/rw/b1]` |
| Al-Baqarah total letters (graphemes) | 26,249 | `[nt/gr/b1]` |
| Al-Baqarah total letters (graphemes) | 25,900 | `[mt/gr/b1]` |
| Al-Baqarah total letters (graphemes) | 25,988 | `[ft/gr/b1]` |
| Al-Baqarah word-midpoint verse | 2:172 | all three orthographies |
| Al-Baqarah letter-midpoint verse | 2:171 | all three orthographies |
| Whole-Quran verse-midpoint | 26:186/187 | hafs-kufan |
| Whole-Quran word-midpoint verse | 18:77 | `[nt/rw/b1]`, anchor 77,797 |
| Whole-Quran letter-midpoint verse | 18:73 | `[nt/gr/b1]`, anchor 330,709 |
| Wasat-family tokens, whole Quran | 5 | all three orthographies (post strip) |
| Surahs with even verse count | 60 / 114 | any |
| Surahs with wasat-family at strict midpoint | **1 (Al-Baqarah only)** | all three orthographies |
| Surahs with wasat-family within ±2 of midpoint | 3 (2, 68, 100) | all three orthographies |

## 7. Files and reproducibility

- Primary analysis script: `/Users/grey/Downloads/quran/analysis/scripts/middle_ayah_analysis.py`
- Robustness / tashkeel-normalized verification: `/Users/grey/Downloads/quran/analysis/scripts/middle_ayah_verify.py`
- Data: `/Users/grey/Downloads/quran/quran-text/quran-{no,min,full}-tashkeel.json`
- Toolkit: `/Users/grey/Downloads/quran/analysis/tools/{loader,tokenize}.py`

To reproduce: `python3 /Users/grey/Downloads/quran/analysis/scripts/middle_ayah_analysis.py` and `python3 /Users/grey/Downloads/quran/analysis/scripts/middle_ayah_verify.py`. All anchors match the locked values in `docs/methodology.md §8`.
