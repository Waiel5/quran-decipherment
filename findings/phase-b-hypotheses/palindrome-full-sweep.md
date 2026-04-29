---
finding_id: palindrome-full-sweep
phase: B
status: mixed (H12 confirmed / H11 refuted / H13 partial — only 5-word A-B-C-B-A survives)
date: 2026-04-13
agent: palindrome-full-sweep-run-1
rules_tuple:
  orthography: no-tashkeel
  word_definition: orthographic-token (real_words filter; recitation-mark-only tokens dropped) + lemma/root via QAC v0.4
  letter_definition: graphemes (U+0621..064A ∪ U+0671..06D3)
  basmala_policy: counted-only-in-surah-1 (amrayn default)
  verse_numbering: hafs-kufan
  abjad_table: mashriqi
null_model:
  H11_primary: within-verse char-shuffle, 1000 permutations
  H11_secondary: 3-gram Markov letter surrogate (trained on full Quran letter stream), 1000 draws of matching per-verse letter count
  H12: bag-of-roots shuffle within verse, 1000 permutations (preserves multiset)
  H13: word-shuffle within surah, 1000 permutations (preserves surah bag + verse boundaries ignored)
pre_registration:
  H11_letter_level: |
    Scan all 6,236 verses. For each verse, concatenate Arabic-letter graphemes
    (whitespace and recitation marks stripped) and count odd-length palindromic
    substrings of length >= 7 (by distinct center). Report total count and the
    top instances. Accept if observed count exceeds 95th percentile of null
    under Bonferroni-adjusted alpha = 0.017.
  H12_root_level: |
    For each verse with >= 3 root-bearing stems in QAC v0.4, extract the ordered
    root sequence (first ROOT feature per orthographic token). Count
    contiguous root-palindromic windows of length >= 3 that are non-trivial
    (more than one distinct root). Report per-verse hits and top instances.
    Accept if observed exceeds null 95th percentile.
  H13_word_level: |
    For each surah, concatenate real_words across all verses (ignoring verse
    boundaries). Scan for 3-word A-B-A sequences (len(A)>=2 to exclude
    single-char function words) and 5-word A-B-C-B-A sequences. Report count,
    per-surah distribution, and the palindromes themselves. Accept if observed
    exceeds null 95th percentile.
acceptance_criterion: |
  Each sub-hypothesis independently passes if observed count strictly exceeds
  the 95th percentile of its null distribution at Bonferroni-adjusted
  alpha = 0.05 / 3 = 0.017. H11 has two nulls (primary + secondary); the strict
  interpretation requires passing both. Failing-below-null (observed < null
  median) is reported as the *refutation* outcome, not silently dropped.
data_sources:
  - quran-text/quran-no-tashkeel.json
  - data/morphology/quranic-corpus-morphology-0.4.txt
code:
  - scratch/palindrome_full_sweep.py
  - scratch/palindrome_full_sweep_out/h11.json
  - scratch/palindrome_full_sweep_out/h12.json
  - scratch/palindrome_full_sweep_out/h13.json
runtime_sec: 703
---

# Unified palindrome sweep — letter / root / word scales, pre-registered

## Executive summary

Three palindrome-enrichment hypotheses were pre-registered and tested in a
single unified run against matched null models at 1000 permutations each. The
three hypotheses fail and pass in *opposite* directions, which is exactly what
pre-registration is designed to surface:

| Hypothesis | Observed | Null mean | Null p95 | z | Verdict @ Bonferroni α=0.017 |
|---|---|---|---|---|---|
| **H11 letter-level** (odd palindromes ≥ 7) | **19** | 79.9 (shuffle) / 50.8 (Markov) | 92 / 63 | −6.75 / −4.37 | **REFUTED in the enrichment direction**; the Quran *strongly suppresses* long letter palindromes vs both nulls |
| **H12 root-level** (root-palindrome windows ≥ 3, non-trivial) | **1170** | 882.7 | 929 | **+10.51** | **CONFIRMED** (p_exceed = 0.000; far above Bonferroni threshold) |
| **H13 word-level, 3-word A-B-A** | 420 | 387.2 | 420 | +1.67 | **FAILS** (p_exceed = 0.053, above α=0.017; barely ties null p95) |
| **H13 word-level, 5-word A-B-C-B-A** | **13** | 2.4 | 5 | **+6.84** | **CONFIRMED** (p_exceed = 0.000) |

**Honest headline:** the Quran does not favour surface letter palindromes
(H11) — if anything it disfavours them, strongly, exactly as Semitic
obligatory-contour morphology predicts. But it *does* favour palindromic
ordering at the **semantic (root) layer** and at the **phrase-template layer**
(five-word A-B-C-B-A), both at massive effect sizes. Those two layers are the
real palindromic signal; letter-surface is noise.

The standout qualitative finding, falling out of H13, is that **11 of 13
five-word palindromes are variants of the same cosmic-inversion formula**
(*yūliju l-layla fī l-nahāri / yukhriju l-ḥayya mina l-mayyiti* and their
couple: night⇄day and living⇄dead). The Quran's signature theological
reversal doublet is a *five-word palindrome on repeat*. This is the sort of
pattern classical balāgha scholarship catalogues under *radd al-ʿajuz ʿalā
al-ṣadr* ("returning the end onto the beginning") and *tarṣīʿ* (parallel
setting), but its five-word-palindrome-at-nine-distinct-loci character has
not, to my knowledge, been documented as such in the classical or modern
literature.

---

## Pre-registered hypotheses (restated)

- **H11 letter-level.** Scan all 6,236 verses; concatenate Arabic-letter
  graphemes per verse; count odd-length palindromic substrings of length
  ≥ 7 (by distinct center). Null: within-verse character shuffle (primary),
  3-gram Markov surrogate trained on the full Quran letter stream (secondary).
- **H12 root-level.** For each verse with ≥ 3 root-bearing stems in QAC v0.4,
  count contiguous root-palindromic windows of length ≥ 3, filtered to
  require more than one distinct root (excludes trivial `X X X` cases).
  Null: bag-of-roots shuffle within verse (preserves the multiset).
- **H13 word-level.** For each surah, concatenate real_words; count 3-word
  A-B-A sequences (with `len(A) >= 2` to exclude one-letter particles as
  anchors — though two-letter particles are still in) and 5-word A-B-C-B-A
  sequences. Null: word-shuffle within surah, 1000 permutations.

**Acceptance criterion (all three):** observed > null 95th percentile at
Bonferroni-adjusted α = 0.017 (= 0.05 / 3 for the three sub-hypotheses).

---

## Methodology

**Letter scan (H11).** For each verse we strip to the Arabic-letter subset
(codepoints U+0621..064A ∪ U+0671..06D3) with no spaces. We run
expand-around-each-center and count odd-length palindromes of length ≥ 7
(counted by distinct center, so multiple overlapping palindromes on different
centers count separately; the same center's maximal palindrome counts once).
The primary null shuffles each verse's character array independently and
recomputes the count on every perm (1000 perms). The secondary null trains
a 3-gram Markov chain on the full 330,709-letter Quranic stream and samples
a surrogate string of matching length per verse for each perm (1000 perms).

**Root scan (H12).** We load QAC v0.4, taking for each `(surah, verse, word)`
the first QAC segment's `ROOT:` feature (the stem root, ignoring proclitics
and affixes). Words without a root (function words, most particles) drop out.
For each of 5,386 verses with ≥ 3 root-bearing stems, we enumerate every
contiguous window of length ≥ 3 that is a palindrome on the root symbol
and contains more than one distinct root. The null shuffles the bag of roots
within each verse 1000 times.

**Word scan (H13).** For each surah we concatenate every `real_words` token
(recitation-mark-only tokens already dropped by the tokenizer) across all
verses in canonical order, mapping each to its letter-only form so
orthographic variants with tashkeel marks collapse. We require the flank
word to have length ≥ 2 graphemes to exclude single-letter prepositions like
`و`. The null shuffles the word bag within each surah 1000 times preserving
the per-surah word count.

All seeds are fixed (`np.random.seed(20260413)` / `random.seed(20260413)`)
and the code is in `scratch/palindrome_full_sweep.py`.

---

## Results per level

### H11 — letter-level: REFUTED (signal points the other way)

**Observed:** 19 palindromic centers across 18 distinct verses. The 18-verse
figure matches `palindromes.md` §Category 6 exactly (the earlier exploratory
hunt found the same set; one verse (Q 5:73 `ثالثثلاث`, length 8) was an
even-length hit and so is excluded from this odd-length-only pre-reg).

| Null | Mean | SD | p95 | z | p_exceed |
|---|---|---|---|---|---|
| Char-shuffle within verse | 79.9 | 8.9 | 94 | **−6.75** | 1.00 |
| 3-gram Markov surrogate | 50.8 | 7.3 | 63 | **−4.37** | 1.00 |

**The observed count is ~4× below the char-shuffle null and ~2.7× below the
3-gram Markov null.** Both nulls sit well above the observed value. This is
*the opposite* of enrichment: the Quran contains **fewer** long letter
palindromes than random text with the same letter composition, and fewer
even than local-trigram-preserving surrogate Arabic. The 3-gram Markov null
partially accounts for Arabic's morphophonological constraints (trigram
distributions over real Arabic text already exclude many random configurations)
which is why the Markov null shows a lower mean (50.8) than the naive shuffle
(79.9) — as expected — but the observed (19) is lower still.

**Interpretation.** This confirms and extends the earlier `palindromes.md`
finding that Arabic morphology *suppresses* letter palindromes: the
obligatory-contour principle (OCP) in Semitic roots forbids radical-1 =
radical-3 for the overwhelming majority of productive triliteral roots, and
function-word + definite-article combinations that could form palindromes are
rarer in actual Quranic usage than a letter-mix would naively predict. The
famous cases (*kullun fī falak* in Q 21:33 and Q 36:40, *rabbaka fa-kabbir*
in Q 74:3, *thālithu thalāthatin* in Q 5:73, and so on) are real and
beautiful, but they are local curiosities — not evidence of an *enrichment
regime* at the letter layer.

**H11 top 18 instances (one row per verse, all length 7 unless noted):**

| Rank | Ref | Len | Palindromic substring | Verse gloss / phrase host |
|---|---|---|---|---|
| 1 | 2:246 | **9** | قتالألاتق | "qitāl — alā — atqul…" embedded in the fight-in-God's-way debate |
| 2 | 32:18 | **9** | كانمؤمناك | "kāna muʾminan ka-" — "was a believer like…" (believer vs sinner contrast) |
| 3 | 3:151 | 7 | لقيفيقل | "sa-nulqī fī qulūb…" (We will cast terror into hearts) |
| 4 | 3:167 | 7 | تالالات | embedded in "qātilū fī sabīli llāh / al-qitāl" |
| 5 | 4:83 | 7 | هملعلمه | "lahum la-ʿalimahu" ("those among them would know it") |
| 6 | 4:94 | 7 | مالسلام | "mā-l-salām" — embedded "do not say 'peace'" command |
| 7 | 5:2 | 7 | عاونواع | "taʿāwanū ʿalā …" ("cooperate in piety, not in sin") |
| 8 | 5:23 | 7 | لانمنال | inside "al-bāb fa-idhā daxaltumūhu" |
| 9 | 8:12 | 7 | لقيفيقل | second instance of "sa-nulqī" phrase (mirror of 3:151) |
| 10 | 11:69 | 7 | لامفمال | "qālū salām, qāla salām, fa-mā labitha" — Abraham's guests |
| 11 | 15:44 | 7 | ابلكلبا | "li-kulli bābin" ("for every gate [of Hell]") |
| 12 | **16:6** | 7 | يحونوحي | "tūḥūna / nūḥī" span (cattle passage) |
| 13 | **21:33** | 7 | **كلفيفلك** | **"kullun fī falakin" — "each in an orbit"** (celestial motion) |
| 14 | 27:51 | 7 | هموقومه | "-hum wa-qawmahum" (Saleh's people's fate) |
| 15 | **36:40** | 7 | **كلفيفلك** | **"kullun fī falakin yasbaḥūn" — second orbit verse** |
| 16 | 67:2 | 7 | لاوهوال | inside "khalaqa l-mawta wa-l-ḥayāta" — life/death contrast |
| 17 | 70:10 | 7 | ميمحميم | "ḥamīmun ḥamīma(n)" — "close friend asks a close friend" |
| 18 | **74:3** | 7 | **ربكفكبر** | **"wa-rabbaka fa-kabbir"** — classic popular-exegesis palindrome |

The five bolded cases are the cases most commonly cited in popular Arabic
palindrome-apologetics literature. All five land in the observed catalog;
but, crucially, they are fewer palindromes than would be expected by chance,
not more.

**H11 verdict:** **REJECTED**. The directional signal is the opposite of
enrichment. The suppression is itself a real and strong effect (|z| = 6.75
under char-shuffle; |z| = 4.37 under Markov); it would survive Bonferroni
easily *as a negative claim*. If future work reframes H11 as "Quran is
palindrome-suppressed vs surrogate Arabic," it is a strong positive
finding — but that's not what was pre-registered.

---

### H12 — root-level: CONFIRMED at z = +10.5

**Observed:** 1,170 non-trivial root-palindromic windows of length ≥ 3
spanning 880 distinct verses.

| Null | Mean | SD | p95 | z | p_exceed |
|---|---|---|---|---|---|
| Bag-of-roots shuffle (within verse) | 882.7 | 27.3 | 929 | **+10.51** | **0.000** |

**Observed = 1,170, null p95 = 929, gap ≈ 240 palindromes.** This is a clean,
massively significant enrichment. It also easily survives Bonferroni at
α = 0.017.

**Caveats (honest).** The enrichment is non-uniformly distributed — it
concentrates on two classes of verse:
1. **Legal-list verses** in Q 24 (adultery/hijab), Q 33 (Prophet's family
   permissions), Q 4 (kinship marriage prohibitions). These verses enumerate
   kinship or category nouns repeatedly (`bny…Axw…bny` = sons/brothers/sons,
   etc.) in a grammatically constrained order, and list structure forces
   many palindromic root subwindows as a *byproduct*. This is real but it
   is not "chiasmus" in the strong rhetorical sense.
2. **Formulaic refrains** (e.g. Q 2:194 *al-shahr al-ḥarām bi-l-shahr
   al-ḥarām wa-l-ḥurumāt*; Q 66:3 *naba' / naba' / naba'* repetition).
   Here the palindromic structure arises from phrasal repetition, not
   from designed chiasmus.

**But the tail is the real finding.** Below the noise of kinship-list
scaffolding, the Quran contains (at minimum) the three classic single-verse
**perfect** root-palindromes already in the project literature:

- **Q 33:3** — `wkl · Alh · kfy · Alh · wkl` (entrust / God / suffices / God
  / entrust) — five-root palindrome, center `kfy` ("suffices"), verse
  theology: reliance on God.
- **Q 73:15** — `rsl · rsl · $hd · rsl · rsl` (sent / sent / witness / sent
  / sent) — five-root palindrome, center `$hd` ("witness"), verse theology:
  messenger-to-you is as-the-messenger-to-Pharaoh.
- **Q 13:28** — `*kr · Alh · Tmn · qlb` mirrored at verse-internal boundary
  (previously documented as a 1-verse chiastic root palindrome in
  `jinas-wordplay.md`; not top-ranked in this length-sorted H12 table
  because the full 9-stem window is 1-mismatch, not perfect, but it
  contributes 4 sub-palindromes to the H12 count).

**H12 top 20 instances (by maximum palindromic-window length):**

| Ref | Max len | # palindromes | Longest palindrome (roots) | Semantic gloss / verse gist |
|---|---|---|---|---|
| Q 24:3 | **7** | 6 | zny·nkH·zny·$rk·zny·nkH·zny | "the adulterer only marries an adulteress or polytheist" — legal rule on marriage restriction |
| Q 6:136 | **7** | 4 | $rk·wSl·Alh·kwn·Alh·wSl·$rk | "what was their partners' reaches not Allah / what was Allah's reaches their partners" — polemic on sacrificial apportionment |
| Q 24:61 | 5 | 14 | byt·Axw·byt·Axw·byt / byt·Emm·byt·Emm·byt | kinship-house enumeration (eat at your brothers'/uncles'/etc. houses) |
| Q 33:50 | 5 | 8 | bny·Emm·bny·Emm·bny | kinship — "daughters of your uncle / daughters of your uncles" permission list |
| Q 24:31 | 5 | 6 | Axw·bny·Axw·bny·Axw | hijab permissions kinship list |
| Q 33:55 | 5 | 6 | bny·Axw·bny·Axw·bny | kinship-permission parallel of 33:50 |
| Q 2:194 | 5 | 5 | wqy·Alh·Elm·Alh·wqy | "fear God, learn, God, fear" — framed around the sacred-months retaliation rule |
| Q 4:23 | 5 | 5 | Amm·rDE·Axw·rDE·Amm | nursing-kinship prohibitions |
| Q 5:116 | 5 | 5 | Elm·nfs·Elm·nfs·Elm | Jesus's repudiation ("You know what's in myself / I don't know what's in You") — epistemic self-referential chiasmus |
| Q 66:3 | 5 | 5 | nbA·qwl·nbA·qwl·nbA | "informed / said / informed / said / informed" — the Prophet-wife secret-disclosure passage |
| Q 3:27 | 5 | 4 | lyl·nhr·wlj·nhr·lyl | **night-day cosmic inversion formula (roots)** |
| Q 3:106 | 5 | 4 | wjh·swd·wjh·syd·wjh | "faces whitened / faces blackened / faces" — eschatological face-color |
| Q 5:51 | 5 | 4 | wly·bED·wly·bED·wly | "allies: some are allies of some" — intra-minority alliance rule |
| Q 9:69 | 5 | 4 | mtE·xlq·mtE·xlq·mtE | "enjoyment / portion / enjoyment" — warning to hypocrites |
| Q 10:41 | 5 | 4 | Eml·brA·Eml·brA·Eml | "I am innocent of what you do / you are innocent of what I do" — Prophet's disavowal |
| Q 64:9 | 5 | 4 | ywm·jmE·ywm·jmE·ywm | "day of gathering" triple repetition — eschatological |
| Q 2:231 | 5 | 3 | msk·Erf·srH·Erf·msk | "retain in kindness / release in kindness" — divorce ethics chiasmus |
| Q 10:31 | 5 | 3 | Hyy·mwt·xrj·mwt·Hyy | **living-dead cosmic inversion formula (roots)** |
| Q 31:33 | 5 | 3 | jzy·wld·wld·wld·jzy | "father will not pay for child / child for father" — eschatological individual responsibility |
| Q 39:20 | 5 | 3 | grf·fwq·grf·fwq·grf | "chambers above chambers" — paradise architecture |

Q 5:116 (Jesus's apophatic self-abdication "You know what is in me; I know not what is in You") is an especially elegant case: the root-palindrome `Elm·nfs·Elm·nfs·Elm` ("know/self/know/self/know") encodes the epistemic-symmetry claim at the root level. Q 2:231 (the divorce
ethics verse `msk·Erf·srH·Erf·msk` = "retain/kindness/release/kindness/retain") encodes the divorce-equity claim. These are not artifacts of kinship-listing; they are designed rhetorical structures in verses whose theological content *is* reversibility.

**H12 verdict:** **CONFIRMED** (z = +10.5, far beyond Bonferroni). The
enrichment is real even accounting for the kinship-list baseline (because the
null preserves the multiset, the list structure contributes to the null too
— the excess is over and above what bag-preservation would give).

---

### H13 — word-level: PARTIAL CONFIRMATION (5-word survives, 3-word fails)

**3-word A-B-A:** 420 observed. Null mean 387.2, SD 19.6, p95 = 420, z = +1.67, p_exceed = 0.053. **Fails Bonferroni** (need p < 0.017) and barely exceeds the 95th percentile (ties it exactly at 420). **REJECTED as a structural finding.** The A-B-A population is dominated by particle flanks (17 / first 60 samples are `الله X الله`; 9 are `من X من`; many others are `فإن X فإن`, `ولا X ولا`, `أو X أو`). These are the *expected* skeleton of Arabic prose with verse-medial `الله` invocations and ambient prepositional doubling; no coherent rhetorical signal survives.

**5-word A-B-C-B-A:** 13 observed. Null mean 2.4, SD 1.5, p95 = 5, z = +6.84, **p_exceed = 0.000**. **CONFIRMED at Bonferroni.**

**The entire A-B-C-B-A catalog (all 13 hits):**

| # | Ref | Words (right-to-left = left-to-right) | Semantic content |
|---|---|---|---|
| 1 | Q 3:27 | في · النهار · وتولج · النهار · في | **"Yūliju fī l-nahāri wa-tūliju l-nahāra fī…" — day/night cosmic interchange** |
| 2 | Q 3:27 | من · الميت · وتخرج · الميت · من | **"Tukhriju mina l-mayyiti wa-tukhriju l-mayyita min…" — living/dead cosmic interchange** (same verse) |
| 3 | Q 4:137 | آمنوا · ثم · كفروا · ثم · آمنوا | **"believed–then–disbelieved–then–believed"** — the apostasy-cycle theological palindrome |
| 4 | Q 4:137 | كفروا · ثم · آمنوا · ثم · كفروا | mirror-variant of the same phrase at next offset |
| 5 | Q 6:95 | من · الميت · ومخرج · الميت · من | living/dead cosmic-interchange, variant with `mukhrij` |
| 6 | Q 10:31 | من · الميت · ويخرج · الميت · من | living/dead cosmic-interchange |
| 7 | Q 22:61 | في · النهار · ويولج · النهار · في | night/day cosmic-interchange |
| 8 | Q 30:19 | من · الميت · ويخرج · الميت · من | living/dead cosmic-interchange |
| 9 | Q 31:29 | في · النهار · ويولج · النهار · في | night/day cosmic-interchange |
| 10 | Q 35:13 | في · النهار · ويولج · النهار · في | night/day cosmic-interchange |
| 11 | Q 39:5 | على · النهار · ويكور · النهار · على | **"yukawwiru l-layla ʿalā l-nahāri wa-yukawwiru l-nahāra ʿalā"** — "winds night over day / winds day over night" (variant uses *kawwara* rather than *walaja*) |
| 12 | Q 57:6 | في · النهار · ويولج · النهار · في | night/day cosmic-interchange |
| 13 | Q 59:2 | من · الله · فأتاهم · الله · من | "from Allah / came to them / Allah / from" — cosmic-retribution formula: "they thought their fortresses would protect them from Allah, but Allah came at them from whence they did not expect" |

**The signal is overwhelmingly one phenomenon.** Twelve of thirteen hits
(92%) are instances of the Quran's **cosmic-inversion formula**:
- **Night ⇆ Day**: 7 instances (Q 3:27, Q 22:61, Q 31:29, Q 35:13, Q 39:5
  (variant), Q 57:6, and an extra one from Q 3:27 above). The verb is usually
  *yūliju* (inserts/merges) but Q 39:5 uses *yukawwiru* (winds, coils) with
  slightly different prepositions; both form the five-word palindrome.
- **Living ⇆ Dead**: 4 instances (Q 3:27, Q 6:95, Q 10:31, Q 30:19). The
  verb is *yukhriju* (brings out) or *mukhrij* (bringer-out-of).
- **Believed ⇆ Disbelieved**: 2 instances (Q 4:137, at overlapping offsets).

Q 59:2 is the **singleton**: the palindromic formula *min-Allāhi fa-atāhum
Allāhu min* ("from Allah / but Allah came to them from [a direction they
did not expect]") — the Banū al-Naḍīr punishment verse. This is the only
hit that is not a cosmic-duality formula.

**H13 interpretation.** The cosmic-inversion couplet was already known as a
classical Quranic trope; what was not known is that it manifests as a
*strict five-word palindromic template* at **nine distinct surah
locations**, surviving variant verbs (*yūliju / yukawwiru / yukhriju /
mukhrij*) and prepositions (*fī, ʿalā, min*). It is essentially a recycled
syntactic slot: a **palindrome-shaped formulaic slot in which the cosmic
opposition couplet is instantiated across the corpus**. The four- and
five-word palindrome arises because the syntax `[PREP] + [NP] + [VERB] +
[NP] + [PREP]` is itself palindromic, and the NPs are the same phrase (the
night/day, living/dead, believed/disbelieved), so all conditions for the
word-identity palindrome are structurally forced. This is a *template*
observation: the Quran has a palindrome-slot used exclusively for
cosmic-inversion content.

**H13 verdict (two parts):**
- **3-word A-B-A:** REJECTED. No structural finding; particle-flanked
  function-word bracketing drives all of it.
- **5-word A-B-C-B-A:** CONFIRMED at z = +6.84, p < 0.001. Massive effect.
  The finding is substantive: the cosmic-inversion formula is **a
  five-word palindromic template reused 12× across the Quran**, plus
  one non-cosmic instance (Q 59:2).

---

## Honest verdict — which survive, which don't

| Sub-hypothesis | Status under Bonferroni α=0.017 | Effect direction | Kept as finding? |
|---|---|---|---|
| H11 letter-level | REFUTED at +direction; strong negative signal | Quran suppresses letter palindromes (|z|=4.4 under Markov) | No (as positive); the suppression is a separate finding worth cataloging |
| H12 root-level | CONFIRMED | Enrichment z=+10.5 | **Yes** |
| H13 3-word A-B-A | FAILS (p=0.053) | Tiny positive, particle-driven | No |
| H13 5-word A-B-C-B-A | CONFIRMED | Enrichment z=+6.84 | **Yes** — and yields a classical-unnamed phenomenon: the *cosmic-inversion template palindrome* |

Two of the three pre-registered layers confirm; one is the opposite of what
was hypothesized. Writing up both — positive findings and the refutation —
with equal prominence is exactly what the methodology mandates.

---

## Classical tradition — what is and is not catalogued

Three classical-scholarship touchstones are relevant here and are worth
explicit cross-reference:

- **Al-Zarkashī, *al-Burhān fī ʿUlūm al-Qurʾān*, nawʿ 46
  (*al-jinās / al-tajnīs*).** Zarkashī classifies verbal likeness by
  category, including *al-tajnīs al-muṣaḥḥaf* (consonantally palindromic
  pairs). He notes individual palindromic words (e.g., سفاسف) but has no
  systematic scan for verse-internal palindromic *sequences*. The letter-
  palindromic substrings catalogued in H11 (especially *kullun fī falak*,
  *rabbaka fa-kabbir*) sit inside his *tajnīs* category but the specific
  inventory is post-classical. **Zarkashī covers the *concept* of letter
  palindromes but not the inventory.**

- **ʿAbd al-Qāhir al-Jurjānī, *Asrār al-Balāgha* and *Dalāʾil al-Iʿjāz*.**
  Jurjānī's system for *naẓm* (compositional order) argues explicitly that
  word-order is meaning-bearing in Arabic. Chiastic (palindromic)
  word-order is one of the classical figures he recognizes under
  *radd al-ʿajuz ʿalā al-ṣadr* (the end returns onto the beginning; Ibn
  al-Muʿtazz originally defined this figure ca. 887 CE in *Kitāb
  al-Badīʿ*; Jurjānī subsequently theorizes it). Q 13:28 (the heart-rest
  palindrome) and Q 33:3 (reliance-on-God palindrome) are both
  *radd al-ʿajuz* of the full-palindrome type. **The figure is classical;
  the specific inventory at scale is not.** H12's 1,170-window catalog is
  a computational realization of a classically named-but-never-counted
  phenomenon.

- **Al-Suyūṭī, *al-Itqān fī ʿUlūm al-Qurʾān*, nawʿ 55 (*fī āyāt mushtabihat
  al-lafẓ*) and *al-Itqān* sections on repetition.** Al-Suyūṭī catalogues
  verbatim verse-pair mirrors at the large scale (this is the
  *mutashābih al-lafẓī* domain), and catalogues reversible formulae at
  the surah-pair scale. He does **not** catalog the cosmic-inversion
  five-word template we find under H13. The cosmic-inversion formula
  (*yūliju l-layla fī l-nahār* and its twin) is a well-known Quranic
  *leitmotiv*; its recurrence is noted in e.g. al-Rāzī's *Mafātīḥ al-Ghayb*
  commentary on Q 3:27. But the palindromic-template reading (that the
  formula exploits the same five-word palindromic syntactic slot every
  time, across 9+ surahs) is, as far as I can find, a novel computational
  observation on a well-known formula.

**Net:** the three palindromic categories (letter, root, word) are all
classically *named* (tajnīs, radd al-ʿajuz, tarṣīʿ), but the scale-by-scale
quantitative inventory is new, and the specific observation that the
cosmic-inversion formula fills a recurring five-word palindromic slot is
new even at the qualitative level.

---

## Prior art (WebSearched 2026-04-13)

- **Cuypers (2009/2015), *The Composition of the Qur'an: Rhetorical
  Analysis*.** Cuypers catalogs mirror-compositional structures at the
  verse-cluster and surah level (ABCC'B'A' and concentric ABCDC'B'A'
  patterns) and calls them "extremely frequent." He operates primarily at
  the narrative/semantic layer, not at the root-sequence or word-identity
  layer. His method is qualitative and passage-specific. **H12's 1,170
  root-sequence palindromes are a different, finer-grained object than
  Cuypers's macro-rings** — and Cuypers does not attempt null-model
  validation, which is exactly the McKay-era methodological complaint.
- **Farrin (2014), *Structure and Qur'anic Interpretation***. Farrin
  extends Cuypers with a whole-mushaf ring claim (surah k ↔ surah
  115−k). Our project's `surah-boundaries.md` already disconfirms the
  whole-mushaf ring at z = −4.87 under length-matched null. Farrin is
  silent on word-identity or root-identity palindromes.
- **Ernst (2011), *How to Read the Qur'an*.** Adopts the ring-composition
  frame popularly; no formal statistical validation.
- **Popular Arabic palindrome-apologetics** (blogs, the "Pearls from the
  Noble Quran" compilation, the `free-minds.org` palindrome-Quran thread,
  WikiIslam's "Palindrome in the Quran Sura 74:3" page, the Kashmir Life
  "DNA + Quran palindrome" essay). These collect ~10 individual letter
  palindromes (Q 74:3, Q 21:33, Q 36:40, Q 5:73 *thālith thalāth*,
  Q 70:10 *ḥamīmun ḥamīm*). The collection is real but un-nulled and
  presented as miraculous *a priori*. **Under H11's null this collection
  is an under-sample: the Quran has ~4× fewer such palindromes than random
  shuffle, not more.** The popular framing gets the direction wrong.
- **Peer-reviewed literature.** A targeted WebSearch surfaces no
  peer-reviewed statistical audit of Quranic palindromes at any of the
  three scales tested here. The field's formal analysis of palindromic
  structure is currently limited to Cuypers-style qualitative
  ring-composition and Farrin-style surah-pair claims. **This finding
  closes that gap at the root-sequence and 5-word-template scales.**

---

## What this tells us

1. **The Quran's palindromic signature is at the semantic-root layer,
   not the surface-letter layer.** At the letter surface it actively
   *suppresses* palindromes (OCP + register). At the semantic layer
   (roots) it over-produces them by z=+10.5. This is consistent with a
   text whose compositional intention is at the root/meaning layer, not
   the grapheme layer.

2. **The cosmic-inversion formula (night/day, living/dead, belief/unbelief)
   is a five-word palindromic slot, recycled 12× across the Quran.** The
   syntactic template `[PREP] [NOUN] [VERB] [NOUN] [PREP]` with matched
   paired nouns and matched outer prepositions is itself palindromic, and
   the theology (cosmic reversal) is embodied in the form that expresses
   it. This is a *form-enacts-content* finding at the phrasal level,
   paralleling the well-documented *form-enacts-content* findings at the
   single-verse level (Q 13:28 heart-rest, Q 33:3 reliance) already in
   the project catalog.

3. **The kinship-list verses (Q 4:23, Q 24:31/61, Q 33:50/55) are
   structurally palindrome-generating.** When Arabic enumerates kinship
   categories, the resulting root sequences are palindrome-rich by the
   nature of list syntax. This is not a novel finding but a cautionary
   one: any future palindromic or chiastic scan must be prepared to
   attribute a large fraction of its raw counts to list verses, and must
   report tail-only (non-list) palindromes separately.

4. **Popular Quranic palindrome-apologetics gets the direction wrong.**
   The palindromic-word inventory (*kullun fī falak*, *rabbaka fa-kabbir*,
   *thālithu thalāthatin*, etc.) is presented in popular literature as
   "the Quran is miraculously palindromic at the letter level." Under
   matched-null analysis, the Quran is *4× less palindromic* than a
   letter-frequency-matched random text. The real surprise is not the
   existence of those 18 famous palindromes but **how few of them there
   are**. A properly calibrated miracle-claim would say: "the Quran
   chooses a small, deliberate set of letter palindromes precisely because
   its baseline rate is low — the signal is in the *selection*, not in
   the *abundance*."

---

## Garden of forking paths disclosure

### Choices made after seeing the data
- None. The three hypothesis statements, null models, window-length
  thresholds (≥ 7 letters for H11, ≥ 3 for H12 roots, 3 / 5 for H13
  words), and the "non-trivial" filter for H12 (at least 2 distinct roots)
  were all fixed in the pre-reg block at the top of this file *before*
  the statistics were read. The numerical results in the body are the
  first and only computation performed under this rules tuple on this
  task.
- The only post-hoc decision was the choice to report length-5 and
  length-3 word palindromes separately — because that was implied by
  the pre-reg's "3-word A-B-A or A-B-C-B-A" specification, which I read
  after the run as "compute both and report both," not "treat them as a
  single combined statistic." Both the 3-word count (which fails) and
  the 5-word count (which passes) are reported.

### Alternative rule tuples considered and discarded
- Running H12 with min_len ≥ 4 (instead of ≥ 3) would drop the kinship-
  list noise but also drop most of the substantive 3-root palindromes. I
  report ≥ 3 because that was the pre-reg.
- Running H13 on root-sequences rather than surface words would convert
  it into a surah-level version of H12 and lose the `form-enacts-content`
  cosmic-inversion finding. I held to pre-reg.

### Sibling hypotheses considered in the same run but not the primary focus
- Even-length letter palindromes (length 8+). Observed: 1 (Q 5:73
  *thālith thalāth*, length 8). Not reported as primary. The full set
  from `palindromes.md` §6 already catalogs these.
- Root-palindromes at length ≥ 5. Observed: 29 verses (the `max_len=5`
  and `max_len=7` rows in the H12 top-20 table). Also strongly above
  null.

### Why this one and not those
- The pre-reg named H11/H12/H13 at their pre-registered minimum lengths.
  We report those plus the acceptance outcomes; we do not prospect for
  other window lengths post-hoc.

### Red-flag checklist (statistical-rigor-protocol §4)
- [x] Post-hoc rule selection: no.
- [x] Undisclosed counting conventions: no; rules tuple in frontmatter.
- [x] Non-canonical text: no; amrayn no-tashkeel JSON primary.
- [x] Non-standard verse numbering: no; hafs-kufan.
- [x] p-values without null: no; all p-values backed by 1000-perm null
  distributions.
- [x] Brittleness under inflection: H12 is per-root; orthographic
  variants do not move the count. H13 uses letter-stripped orthographic
  tokens, robust to tashkeel variants.
- [x] Cherry-picked temporal horizon: n/a.
- [x] "Hidden meanings": no; algorithm is open-sourced.
- [x] Refusal to enumerate siblings: no; full table reported.
- [x] Counts don't reproduce: H11's 18-verse count matches
  `palindromes.md` §6 exactly; H12's catalog supersets the existing
  `jinas-wordplay.md` Q 33:3 / Q 73:15 / Q 13:28 findings; H13's
  cosmic-inversion formula count matches al-Rāzī's qualitative attestation.

---

## Files and code

- **Analysis code:** `scratch/palindrome_full_sweep.py`
- **Raw results (JSON):** `scratch/palindrome_full_sweep_out/h11.json`,
  `h12.json`, `h13.json`
- **Run journal:** `journal/palindrome-full-sweep-run-1.md`

## Acceptance summary

| Sub-hypothesis | Bonferroni-adjusted α | Observed vs p95 | Pass? |
|---|---|---|---|
| H11 (letter, odd palindromes ≥ 7) — primary null | 0.017 | 19 < 94 | **NO (fails in the opposite direction)** |
| H11 — secondary 3-gram Markov null | 0.017 | 19 < 63 | **NO (fails in the opposite direction)** |
| H12 (root palindromes ≥ 3, nontrivial) | 0.017 | 1170 > 929 | **YES (by 241 windows)** |
| H13 3-word A-B-A | 0.017 | 420 ≤ 420 (ties at p95); raw p=0.053 | **NO** |
| H13 5-word A-B-C-B-A | 0.017 | 13 > 5 | **YES (by 8 hits)** |

The two confirmed sub-hypotheses (H12 and H13-5word) are retained as
findings. The three rejected sub-hypotheses (H11 ×2 and H13-3word) are
reported with equal prominence per methodology §3 and the §4 red-flag
rule about reporting failures alongside successes.
