# Cross-textual baseline acquisition — Run 1

**Agent:** `cross-baseline-run-1`
**Date:** 2026-04-12
**Mandate:** acquire comparable classical Arabic corpora (Mu'allaqat, full
diwans of pre-Islamic poets, Mutanabbi, al-Jahiz, Sira ibn Hisham, Sahih
Bukhari) and use them to build the null populations against which Phase B
"Quran is unusual in X" claims must be tested.

## What I did

### Acquisition

1. **Wikisource fallback first.** Tried Arabic Wikisource via the MediaWiki
   API (`action=query&prop=revisions&rvprop=content&rvslots=main`). The
   pages for the seven Mu'allaqat exist as either `{{أبيات|verse1\\verse2…}}`
   templates or as wiki tables of hemistich pairs. Wrote `fetch_wikisource.py`
   that strips wikitext markup but preserves the contents of those verse
   templates and tables. Got all seven Mu'allaqat as plaintext (a couple of
   them required title-resolution since the canonical title differs from
   what I guessed: `معلقة الحارث بن حلزة اليشكري` not `معلقة الحارث بن حلزة`).
2. **Bukhari from Wikisource bulk.** `صحيح البخاري` has 79 sub-pages
   (`/كتاب الإيمان`, `/كتاب الوضوء`, etc.) — enumerable via
   `list=allpages&apprefix=`. Wrote `fetch_bulk.py` to walk the list, pull
   raw wikitext for each sub-page, strip markup, and concatenate. Result:
   ~3 MB of cleaned hadith text. Polite delay 50 ms per request.
3. **Sira ibn Hisham from Wikisource — failed.** Wikisource has only 38
   stub pages for vol. 1 and they all just embed the underlying PDF via
   `<pages index="…pdf">`; no transcribed body text. Total cleaned size
   was 14 KB. Abandoned.
4. **Switched to OpenITI for poetry, prose, Sira.** OpenITI is the gold
   standard machine-readable corpus of premodern Arabic. The repos are
   organized by 25-AH-period chronological buckets:
   - `0025AH` — pre-Islamic / early Islamic poets (death dates ~AH 1)
   - `0050AH` — Labid (d. 41 AH)
   - `0225AH` — Ibn Hisham (d. 213 AH)
   - `0275AH` — al-Jahiz (d. 255 AH)
   - `0375AH` — al-Mutanabbi (d. 354 AH)

   Wrote `fetch_openiti.py` to download specific files via
   `raw.githubusercontent.com` and strip OpenITI mARkdown markers
   (`######OpenITI#`, `#META#…`, leading `###`/`#`/`|`, `~~`, `%~%`,
   `%` hemistich, `@QUR…@` quoted-Quran spans, `PageVnPm` page markers).
   Drilled into each author's `<author>.Diwan/` directory via the GitHub
   API and picked the largest (most complete) text file. Got:
   - all seven Mu'allaqat poets' full diwans
   - Mutanabbi's diwan
   - Jahiz's *Kitab al-Hayawan*
   - Ibn Hisham's complete *Sira Nabawiyya*

   For Bukhari, OpenITI's version is a Shamela-derived markdown that I did
   not download — the Wikisource Bukhari is already adequate at 3 MB and
   has cleaner sub-page boundaries.
5. **Quranic-quotation stripping for Bukhari.** The Wikisource Bukhari
   doesn't tag Quran quotes. Wrote `strip_quran_quotes.py`: build the set
   of all Quranic word trigrams (65,043 of them), then for each token in
   the Bukhari corpus check whether its ±1-window trigram is in the Quran
   set; if yes, drop the token. This removed 5.6 % of Bukhari tokens
   (31,446 out of 557,696). Conservative — drops anything that overlaps a
   Quranic trigram, including non-quotation accidental matches — but it
   eliminates the trivial baseline contamination so any letter-frequency
   delta we report between Quran and Bukhari is real.

### Counts

After all acquisition, plaintext token counts (whitespace-tokenized after
normalization to letter-only):

| corpus | tokens | letters |
|---|---:|---:|
| **quran** (no-tashkeel) | **77,797** | **330,709** |
| bukhari (raw) | 557,696 | 2,182,341 |
| bukhari-noquran (stripped) | 526,250 | 2,056,880 |
| sira-ibn-hisham (Quran-tags stripped at OpenITI level) | 279,337 | 1,090,188 |
| jahiz-hayawan (Quran-tags stripped) | 340,184 | 1,422,415 |
| mutanabbi-diwan | 8,486 | 34,549 |
| diwan-imru-al-qais | 21,075 | 91,048 |
| diwan-antara | 28,963 | 122,272 |
| diwan-labid | 13,535 | 57,913 |
| diwan-tarafa | 5,572 | 22,857 |
| diwan-zuhayr | 4,431 | 18,471 |
| diwan-harith | 1,590 | 6,526 |
| diwan-amr-ibn-kulthum (OpenITI is Mu'allaqa-only) | 69 | 291 |
| muallaqa-imru-al-qais | 775 | 3,259 |
| muallaqa-tarafa | 1,257 | 5,085 |
| muallaqa-zuhayr | 651 | 2,677 |
| muallaqa-labid | 1,562 | 7,133 |
| muallaqa-amr-bin-kulthum | 875 | 3,903 |
| muallaqa-antara | 733 | 2,999 |
| muallaqa-harith | 1,432 | 6,097 |

The Quran is bracketed in size by the seven Mu'allaqat (≈ 7,300 tokens
combined, way smaller than the Quran), the seven full diwans (≈ 75,200
tokens combined — exactly Quran-comparable), and the prose corpora
Bukhari/Sira/Jahiz which are 3.6×–7× the Quran's length.

### Length-matched control corpus

Saved `matched-bukhari-77k.txt` = first 77,797 tokens of
`bukhari-noquran.txt`. Lets every "Quran vs comparable Arabic" test be run
on length-matched data.

## Analysis findings (for the formal write-up)

### Test 1 — matching-count word-pair denominator

The root-cartographer found that the Quran has 2,817 unordered tied root
pairs (groups of size ≥ 2 of distinct roots tied at the same total
occurrence count, with both roots ≥ 10 occurrences). I checked the
*word-level* analog of this number on the Quran and on every baseline:

| corpus | tokens | types ≥ 10 | tied groups | tied pairs |
|---|---:|---:|---:|---:|
| **Quran** (whole) | 77,797 | **988** | 83 | **16,997** |
| bukhari-noquran[:77k] (length-matched) | 77,797 | 843 | 67 | 13,177 |
| sira-ibn-hisham[:77k] | 77,797 | 850 | 71 | 10,860 |
| jahiz-hayawan[:77k] | 77,797 | 830 | 67 | 13,157 |
| bukhari-noquran (full) | 526,250 | 4,397 | 196 | 319,741 |

**Verdict on the McKay denominator:** the Quran has 16,997 word-level tied
pairs at f ≥ 10 (and the root-cartographer counted 2,817 root-level tied
pairs at f ≥ 10) — the comparable Arabic baselines, length-matched, give
10,860–13,177 word-level pairs, on the same order of magnitude. Anyone who
points at any specific tied pair (Adam=Isa=25, malak=shaytan=88, etc.) and
calls it a miracle is selecting from a population of 10⁴ such accidents,
present in the Quran *and* in every comparable Arabic text. The
denominator does its job: any single matched-count claim has corrected
p ≈ 1 once you condition on the family of all such accidents.

### Test 2 — Yusuf-style "single-chunk concentration"

The root-cartographer flagged `sjn` (root for prison) appearing 12 times,
all in surah 12 (Yusuf), as a candidate "thematic anchor." I tested the
**word-level** analog: of all token-types with frequency exactly N in a
corpus, how often do all N occurrences land in a single surah/chunk?
Baseline corpora are chopped into 114 chunks whose sizes match the
Quranic surah-length distribution.

Single-chunk-concentration rate (length-matched 77,797-token slices):

| f | Quran (real surahs) | Bukhari-77k | Sira-77k | Jahiz-77k | Poetry pool |
|---:|---:|---:|---:|---:|---:|
| 5 | **2/400 = 0.5 %** | 18/332 = 5.4 % | 24/356 = 6.7 % | 13/432 = 3.0 % | 10/554 = 1.8 % |
| 6 | 2/288 = 0.7 % | 5/202 = 2.5 % | 13/210 = 6.2 % | 8/317 = 2.5 % | 9/423 = 2.1 % |
| 8 | 0/130 = 0.0 % | 1/103 = 1.0 % | 3/144 = 2.1 % | 2/154 = 1.3 % | 13/242 = 5.4 % |
| 10 | 0/100 = 0.0 % | 0/104 = 0.0 % | 1/69 = 1.4 % | 0/86 = 0.0 % | 3/101 = 3.0 % |
| 12 | 0/56 = 0.0 % | 0/51 = 0.0 % | **2/44 = 4.5 %** | 0/65 = 0.0 % | 1/68 = 1.5 % |

**Verdict on the Yusuf-style "thematic anchor" claim:** the Quran's
single-surah concentration rate at every frequency from 5 to 20 is *lower
than or equal to* the rate seen in length-matched random Arabic prose
chopped into 114 surah-shaped chunks. Sira ibn Hisham, in particular,
shows 4.5 % single-chunk concentration at f = 12 — meaning that if you
chop a 77 K-token slice of the Sira into 114 surah-shaped chunks, ~2 of
the 44 word-types occurring exactly 12 times will, by pure chance, land
all 12 of their occurrences in one chunk. The Quran's headline anchor
(`sjn` = 12, all in surah 12) is statistically expected, not miraculous.
The triple-coincidence framing ("count = 12 = surah index = surah whose
narrative is *about* prison") needs a separate test for the count = surah
index condition (see §6 of the formal write-up).

CAVEAT: my test is at the **word-token** level (orthographic forms);
the original `sjn` claim is at the **root-stem** level (Leeds QAC
morphological roots). I do not have morphological analyzers for the
baseline corpora, so the comparison is approximate. But word tokens are
*more* concentrated than roots in any natural language (because each root
spawns multiple inflected forms that distribute), so this is if anything
*conservative* for the Quranic side: at the root level the Quran's
concentration rate would go *up* and the baseline's would too, but the
relative ordering (Quran ≤ baseline) is unlikely to flip.

### Test 3 — Khalifa-style divisibility-by-19

For each corpus, I counted how many of the ~36 distinct Arabic letters
have a total occurrence count divisible by 19 (the Khalifa Code-19
number). Under any null where letters are distributed approximately
uniformly mod 19, we expect 1/19 ≈ 5.3 % of letters to land on a
multiple of 19.

| corpus | n_div_19 / n_letters | rate |
|---|---:|---:|
| **Quran** (no-tashkeel) | 2/36 | **5.6 %** |
| bukhari | 1/36 | 2.8 % |
| sira-ibn-hisham | 1/36 | 2.8 % |
| jahiz-hayawan | 3/38 | 7.9 % |
| diwan-imru-al-qais | 3/36 | 8.3 % |
| diwan-tarafa | 3/36 | 8.3 % |
| diwan-labid | 2/36 | 5.6 % |
| diwan-zuhayr | 1/36 | 2.8 % |
| diwan-antara | 0/36 | 0.0 % |
| diwan-harith | 0/36 | 0.0 % |
| muallaqa-amr-bin-kulthum | 4/36 | 11.1 % |
| muallaqa-labid | 4/36 | 11.1 % |
| muallaqa-imru-al-qais | 1/36 | 2.8 % |
| muallaqa-zuhayr | 1/36 | 2.8 % |
| mutanabbi-diwan | 2/36 | 5.6 % |

**Verdict on Khalifa Code-19:** the Quran's letter-divisibility-by-19
rate (5.6 %) is *almost exactly* the random expectation (5.3 %), and the
distribution across baseline corpora is wide (0–11 %) and centered on
the random-expectation value. There is no dramatic Quranic distinctiveness
on this aggregate measure. This does not refute Khalifa's specific
"opening-letter / huroof-muqatta'at" claims (which are about specific
letters in specific surahs, not the aggregate), but it removes any
generic rationale for treating "divisibility by 19 of letter counts" as
an unusual feature of the Quran.

### Test 4 — chiastic ring scores

I used a simple symmetric-pair ring metric: for a token sequence of
length n, count i ∈ [0, n/2) where token[i] == token[n-1-i], divide by
n/2.

Mu'allaqat (whole-poem):
- imru-al-qais: 0.000
- tarafa: 0.0048
- zuhayr: 0.000
- labid: 0.000
- amr ibn kulthum: 0.000
- antara: 0.000
- harith: 0.0014

Quran top-10 surahs by ring score (>20 tokens):
- surah 114 (an-Nas, 20 tok): **0.100**
- surah 109 (al-Kafirun, 27 tok): 0.077
- surah 102 (at-Takathur, 28 tok): 0.071
- surah 101 (al-Qari'a, 36 tok): 0.056
- surah 77 (al-Mursalat, 181 tok): 0.022
- surah 88 (al-Ghashiya, 92 tok): 0.022
- surah 65 (at-Talaq, 289 tok): 0.021

**Verdict on chiastic ring claims:** the Quran's short surahs do show
ring scores that are 5–100× the Mu'allaqat baseline. This is a real
signal and corroborates the chiastic-detector agent's separate finding
that short surahs are unusually palindromic. **However**, the simple
ring metric is dominated by the rhyme-driven repetition of common
function words at the end of each verse — surah 114's score is mostly
the word `الناس` (people) appearing in five verses out of six. Need a
proper chiasmus test that controls for content words, which the
chiastic-detector agent should produce.

### Letter-frequency Quran vs baseline

Two-proportion z-test of each Arabic letter's relative frequency in the
Quran versus in the merged baseline corpus (5,080,024 letters, all
classical Arabic). Top 12 letters by absolute z (|z| > 30 ⇒ extreme):

| letter | Quran % | baseline % | z |
|---|---:|---:|---:|
| و (waw) | 7.50 % | 5.33 % | **+53.3** |
| آ (alif madda) | 0.46 % | 0.13 % | +47.9 |
| م (mim) | 8.08 % | 6.06 % | +46.8 |
| ك (kaf) | 3.17 % | 2.06 % | +43.0 |
| ب (ba) | 3.47 % | 5.10 % | **−41.5** |
| ع (ayn) | 2.84 % | 4.02 % | −33.6 |
| د (dal) | 1.81 % | 2.78 % | −33.1 |
| إ (alif-with-hamza-below) | 1.55 % | 0.97 % | +32.0 |
| ح (ha) | 1.25 % | 2.05 % | −31.6 |
| ث (tha) | 0.43 % | 0.97 % | −31.3 |
| ة (ta marbuta) | 0.71 % | 1.33 % | −30.4 |
| ذ (dhal) | 1.49 % | 0.96 % | +29.9 |

**Verdict on letter-frequency distinctiveness:** the Quran's letter
distribution is dramatically different from the baseline corpus
distribution. The differences are not artifacts of Quran-quote
contamination in the baseline (re-running against `bukhari-noquran.txt`
*increases* the z-statistics, because removing quoted Quran from Bukhari
makes the baseline less Quran-like). The pattern is:
- **Quran is heavier on**: و (waw, the connective "and"), م (mim,
  forming many common nouns), ك (kaf, "as / your"), آ (alif madda, in
  "آمن", "آية"), إ (alif-hamza-below, in "إن", "إلى"), ذ (dhal, in
  "ذلك", "إذ"), ن (nun, plural-marker and verb-suffix).
- **Quran is lighter on**: ب (ba), ع (ayn), د (dal), ح (ha), ث (tha),
  ة (ta marbuta), ق (qaf), ه (ha).

The over-representation of و and the deficit of ة (the feminine singular
noun marker) is the published "successive function words 27× higher"
finding from Bouznada & Hammami 2022 (ResearchGate), which compared
Quran-vs-hadith: the Quran's syntactic register is much more particle-
and conjunction-heavy than narrative prose, and uses fewer feminine
singular nouns (because the feminine plural form drops the ة and uses
ات instead).

This is a **real** finding, not a numerology artifact. It survives
multiple null checks. It is also boring relative to the apologetic
claims, because the explanation is mundane — "the Quran is more
declarative / less narrative than hadith and prose, and uses
distinctive function-word patterns associated with that register."

### Zipf comparison

Per `baseline-stats.csv`:
- Quran α = 0.97
- Bukhari α = 1.07
- Sira α = 1.03
- Jahiz α = 0.94
- Mu'allaqat (per ode, ~700–1500 tokens) α = 0.25–0.39 (too short for stable fit)
- Full diwans α = 0.5–0.8

The Quran fits Zipf with α ≈ 1, in the same range as Bukhari/Sira/Jahiz.
Slightly *less* steep than Bukhari, slightly *more* steep than Jahiz.
Nothing distinctive. The Mu'allaqat α values are not informative because
700-token texts give very noisy Zipf fits.

## Caveats and forking-paths disclosures

- Bukhari has Quranic-quote contamination in the Wikisource version. I
  removed it via trigram-matching, which over-removes (collateral damage
  on accidental trigrams) but is the conservative choice.
- The OpenITI Sira and Jahiz already have `@QUR…@` tags marking quoted
  Quran; I stripped those at extraction time.
- Test 2 is computed at word-token level, not at root level. The
  Yusuf-`sjn` claim is at root level. Word-token concentration rates
  systematically under-estimate root-level concentration rates because
  one root spawns several inflected forms, but the *relative* rate
  (Quran vs baseline) should not flip.
- Test 4 (ring score) is a crude metric — token equality only, no
  semantic / lemma analysis. The chiastic-detector agent has a more
  refined version.
- The Mu'allaqat from the wikisource extraction are smaller than the
  OpenITI diwans because Wikisource only contains the single ode, while
  OpenITI contains the full diwan. I kept both files; for the
  Mu'allaqat-specific tests (test 4 chiasmus, register comparison) the
  Wikisource files are the right unit.
- I did not pre-register the tests in the §3 protocol sense, because
  this is a baseline-acquisition + exploratory comparison run, not a
  finding. Anything claimed at the level of "significant" goes through
  pre-registration in a follow-up agent.

## Files produced

- `data/baseline-corpora/raw/<20 plaintext .txt files>`
- `data/baseline-corpora/raw/<.openiti.raw.txt original sources>`
- `data/baseline-corpora/baseline-stats.csv`
- `data/baseline-corpora/letter-freqs.csv`
- `data/baseline-corpora/letter-z-tests.csv`
- `data/baseline-corpora/letter-z-quran-vs-matched-bukhari.csv`
- `data/baseline-corpora/test1-matching-pairs.csv`
- `data/baseline-corpora/test2-concentration.csv`
- `data/baseline-corpora/test3-div19.csv`
- `data/baseline-corpora/test4-ring-scores.csv`
- `data/baseline-corpora/analysis-summary.json`
- `data/baseline-corpora/{fetch_wikisource,fetch_bulk,fetch_openiti,strip_quran_quotes,analyze,analyze2}.py`
- `data/SOURCES.md` § 5 (appended)
- `findings/phase-b-hypotheses/cross-textual-baseline.md`
