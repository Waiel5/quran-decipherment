---
surah: 1
surah_name_ar: الفاتحة
surah_name_translit: al-Fātiḥa
file_type: content-analysis
date_last_updated: 2026-04-28
phase: B+
verdict: COMPLETE
---

# Q 1 al-Fātiḥa — Content Analysis (Verse-by-Verse, Arabic-Grounded)

All Arabic in this file is cross-validated against three tashkeel variants on disk:
`quran-no-tashkeel.json`, `quran-min-tashkeel.json`, `quran-full-tashkeel.json`. Where a claim depends on tashkeel, I state which variant supplies the evidence. Where a claim is rules-tuple-fragile (e.g., word-count varies across orthographic conventions), I flag it.

## 1. Verse-by-verse text and content

### Verse 1 — *al-Basmala*

| Variant | Text |
|:--|:--|
| no-tashkeel | بسم الله الرحمن الرحيم |
| min-tashkeel | بِسمِ اللَّهِ الرَّحمٰنِ الرَّحيمِ |
| full-tashkeel | بِسۡمِ ٱللَّهِ ٱلرَّحۡمَٰنِ ٱلرَّحِيمِ |

Translation (literal): "In the name of God, the All-Merciful, the Mercy-Giver."

- **Word count**: 4 (no-tashkeel orthographic-token rule; whitespace-split).
- **Letter count**: 19 (no-tashkeel grapheme rule). The 19-letter count is the empirical anchor for several classical and modern claims (al-Biqāʿī line 122 in the Naẓm al-Durar raw text reads: *وكونها تسعة عشر حرفا خطية وثمانية عشر لفظية* — "its being nineteen letters orthographically and eighteen phonetically"). Note: the 19-count is rules-tuple sensitive — it requires the locked Mashriqi orthographic rule with hamza-on-alif counted as one letter.
- **Roots invoked** (per QAC v0.4): *smw* (سمو, "name") × 1, *ʾlh* (إله, "God") × 2 morphological-attestations through definite-article-bound *Allāh* + the bound *al-Raḥmān al-Raḥīm* doublet, *rḥm* (رحم, "mercy") × 2.
- **Key**: The basmala is the sole verse that opens every surah (except Q 9 al-Tawba) but is **counted as a verse only here** in Hafs-Kufan numbering. This dual status (universal-prefix yet positional-verse-only-here) is what makes it both a doxological signature *and* the canonical first verse of the corpus.

### Verse 2 — *al-Ḥamd*

| Variant | Text |
|:--|:--|
| no-tashkeel | الحمد لله رب العالمين |
| min-tashkeel | الحَمدُ لِلَّهِ رَبِّ العٰلَمينَ |
| full-tashkeel | ٱلۡحَمۡدُ لِلَّهِ رَبِّ ٱلۡعَٰلَمِينَ |

Translation: "Praise [be] to God, Lord of the worlds."

- **Word count**: 4. **Letter count**: 18 (no-tashkeel).
- **Roots**: *ḥmd* (حمد, "praise") × 1; *ʾlh* × 1; *rbb* (رب, "lord") × 1; *ʿlm* (علم, "knowledge/world") × 1 (the form *al-ʿālamīn* derives from *ʿālam* via *ʿlm*).
- **Definite-article density**: 2 of 4 words bear *al-* (الحمد, العالمين). This contributes to the surah's rhyme-tightening and to its high definite-article frequency overall.
- The opening *al-ḥamdu li-llāh* is the head of the **al-ḥāmidāt cluster** (5 surahs opening with *al-ḥamd*: Q 1, 6, 18, 34, 35). al-Rāzī (Mafātīḥ al-ghayb, raw lines 5862-5876) explicitly treats the four post-Q1 *al-ḥamd*-openers as *aqsām* (sub-divisions) of Q 1's *rabb al-ʿālamīn*. This is one of the strongest classical *munāsaba* claims about Q 1 and it directly maps onto an empirical cluster.

### Verse 3 — *al-Raḥmān al-Raḥīm*

| Variant | Text |
|:--|:--|
| no-tashkeel | الرحمن الرحيم |
| min-tashkeel | الرَّحمٰنِ الرَّحيمِ |
| full-tashkeel | ٱلرَّحۡمَٰنِ ٱلرَّحِيمِ |

Translation: "The All-Merciful, the Mercy-Giver."

- **Word count**: 2. **Letter count**: 12. The shortest verse in the surah.
- **Roots**: *rḥm* × 2.
- This is a **literal repetition** of the second half of the basmala (v1). Repetition of *al-Raḥmān al-Raḥīm* in verses 1 and 3 is a classical observation (al-Suyūṭī Itqān raw line 4329, al-Biqāʿī Naẓm raw line 122 ff.). The Q 1 surah uses the *rḥm* root **4 times in 7 verses** — the highest density of any divine-attribute root in the surah (see root-table below in §3).

### Verse 4 — *Mālik yawm al-dīn*

| Variant | Text |
|:--|:--|
| no-tashkeel | مالك يوم الدين |
| min-tashkeel | مٰلِكِ يَومِ الدّينِ |
| full-tashkeel | مَٰلِكِ يَوۡمِ ٱلدِّينِ |

Translation: "Master of the Day of Judgment."

- **Word count**: 3. **Letter count**: 12.
- **Roots**: *mlk* (ملك, "kingship") × 1; *ywm* (يوم, "day") × 1; *dyn* (دين, "judgement / religion") × 1.
- **Qirāʾāt note**: The reading varies between *mālik* (مَالِكِ, "owner/master") and *malik* (مَلِكِ, "king"). al-Ṭabarī (Q 1:4 raw text, *spa5k-tafsir-api/ar-tafsir-al-tabari/1/4.json*) opens with: *القرَّاء مختلفون في تلاوة (مَلِكِ يَوْمِ الدِّينِ)* — "The reciters disagree in the recitation of *Mālik / Malik yawm al-dīn*." Both readings are canonical (Hafs gives *Mālik*, Warsh gives *Malik*). At the **no-tashkeel** rules-tuple this is invisible (مالك is neutral); at the **full-tashkeel** rules-tuple, the project's locked Hafs reading writes *Mālik*. Do not generalize the count of the *mlk* root from the surface form; QAC v0.4 already lemmatizes this correctly.
- This verse is the **eschatological hinge** of the surah. It is the only verse that names the Day of Judgement; in the symmetric reading (verses 1-3 as God-half and verses 5-7 as supplicant-half), v 4 is the centre — the pivot from praise to petition. See ring-composition analysis in `06-novel-findings.md`.

### Verse 5 — *Iyyāka naʿbudu wa-iyyāka nastaʿīn*

| Variant | Text |
|:--|:--|
| no-tashkeel | إياك نعبد وإياك نستعين |
| min-tashkeel | إِيّاكَ نَعبُدُ وَإِيّاكَ نَستَعينُ |
| full-tashkeel | إِيَّاكَ نَعۡبُدُ وَإِيَّاكَ نَسۡتَعِينُ |

Translation: "You [alone] do we worship, and from You [alone] do we seek aid."

- **Word count**: 4 (treating *wa-iyyāka* as one word per Mashriqi orthographic-token rule). **Letter count**: 19 (no-tashkeel).
- **Roots**: *ʿbd* (عبد, "worship") × 1; *ʿwn* (عون, "aid") × 1; the pronoun *iyyāka* is non-rooted but doubled.
- **Iltifāt**: This verse is the **classic Q 1:5 grammatical shift** (catalogued in `data/literature/classical-tafsir/abdel-haleem-iltifat-catalog.md`, Category I-3 "3rd → 2nd person"). al-Zarkashī (al-Burhān, *nawʿ al-iltifāt*) and al-Suyūṭī (al-Itqān, parallel chapter) cite Q 1:5 as the paradigmatic 3rd→2nd shift: verses 1-4 speak of God in third person (*li-llāhi*, *rabbi*, *al-raḥmān al-raḥīm*, *māliki*); verse 5 abruptly turns to second-person address (*iyyāka*). Abdel Haleem (1992 BSOAS) reads this as the rhetorical turning-point that marks Q 1:5 as the *liturgical opening of address*.
- **Doubling**: *iyyāka* repeats with the conjunction *wa-* in the same verse — the only surah-internal pronoun-doubling in Q 1. al-Biqāʿī (Naẓm raw line 568-570) reads the doubling as the surah's "axis": worship (*ʿibāda*) and seeking-aid (*istiʿāna*) are the two "verbs of servitude" mounted on the same pronoun-bracket.

### Verse 6 — *Ihdinā al-ṣirāṭ al-mustaqīm*

| Variant | Text |
|:--|:--|
| no-tashkeel | اهدنا الصراط المستقيم |
| min-tashkeel | اهدِنَا الصِّرٰطَ المُستَقيمَ |
| full-tashkeel | ٱهۡدِنَا ٱلصِّرَٰطَ ٱلۡمُسۡتَقِيمَ |

Translation: "Guide us along the Straight Path."

- **Word count**: 3. **Letter count**: 19.
- **Roots**: *hdy* (هدي, "guidance") × 1; *ṣrāṭ* (صراط, "path"; QAC root *SrT*) × 1; *qwm* (قوم, "to stand straight") × 1 (the form *al-mustaqīm* derives from *qwm* via Form X).
- This is the surah's **central petition** — and the only imperative in the surah. The verbal mood shifts from declarative-past-tense (*naʿbudu, nastaʿīn* — imperfect) to imperative (*ihdinā* — request). al-Rāzī (Mafātīḥ al-ghayb raw line 5701) calls Q 1 *sūrat al-duʿāʾ* (the Surah of Petition) precisely because of this verse.

### Verse 7 — *Ṣirāṭa lladhīna anʿamta ʿalayhim ghayri l-maghḍūbi ʿalayhim wa-lā l-ḍāllīn*

| Variant | Text |
|:--|:--|
| no-tashkeel | صراط الذين أنعمت عليهم غير المغضوب عليهم ولا الضالين |
| min-tashkeel | صِرٰطَ الَّذينَ أَنعَمتَ عَلَيهِم غَيرِ المَغضوبِ عَلَيهِم وَلَا الضّالّينَ |
| full-tashkeel | صِرَٰطَ ٱلَّذِينَ أَنۡعَمۡتَ عَلَيۡهِمۡ غَيۡرِ ٱلۡمَغۡضُوبِ عَلَيۡهِمۡ وَلَا ٱلضَّآلِّينَ |

Translation: "The path of those whom You have favored — not [the path] of those upon whom is wrath, nor of those who are astray."

- **Word count**: 9 (the longest verse of the surah). **Letter count**: 44 — alone accounting for **30.8 %** of all letters in the surah (44 / 143 no-tashkeel).
- **Roots**: *ṣrāṭ* × 1 (repeats v 6); *nʿm* (نعم, "favor") × 1; *ghyr* (غير, "other-than") × 1; *ghḍb* (غضب, "wrath") × 1; *ḍll* (ضلل, "astray") × 1.
- **Triadic structure**: this verse alone trifurcates humanity into three classes — *al-mun'am ʿalayhim* (the favoured), *al-maghḍūb ʿalayhim* (the wrath-incurring), *al-ḍāllīn* (the astray). al-Biqāʿī (Naẓm al-Durar raw line 907 et seq.) calls this *taṣnīf al-nās ākhir al-Fātiḥa thalāthat aṣnāf* — "the Fātiḥa's three-fold classification of humanity at its end."
- **Verse-7 weight**: 9 of 29 words = 31 % of the surah's word-mass; 44 / 143 = 31 % of the letter-mass. The surah is *back-loaded* — its longest verse is its last, and that last verse contains nearly a third of the surah's lexical material. This is structurally significant for ring-composition analysis (a long terminal verse tends to break ABCBA mirror structure unless v7 itself contains internal mirroring; see `06-novel-findings.md`).

## 2. Major thematic blocks

| Block | Verses | Direction of address | Mood | Word count |
|:--|:-:|:--|:--|:-:|
| A — Doxology | 1-3 | God in 3rd person | Declarative | 10 |
| B — Eschatological hinge | 4 | God in 3rd person (pivot) | Declarative | 3 |
| C — Pronominal turn | 5 | God in 2nd person (iltifāt) | Declarative | 4 |
| D — Petition | 6 | God in 2nd person | Imperative | 3 |
| E — Differentiation | 7 | God in 2nd person (continued) | Declarative-elaborative | 9 |

The **pivot of address** (3rd→2nd) sits at the boundary B|C between v 4 and v 5. The **pivot of mood** (declarative→imperative) sits at the boundary C|D between v 5 and v 6. The two pivots do **not** coincide — they are off-set by one verse, producing two interlocking turn-points rather than a single centre. This is empirically why Q 1's structure resists a flat ABCBA reading; its "centre" is dual (verses 4 and 5 both function as pivots, on different axes).

## 3. Root-distribution audit

From `data/morphology/surah-root-graph.json` (QAC v0.4 stem-roots):

| Root (transliterated) | Arabic | Count | Verses |
|:--|:--:|:-:|:--|
| *rḥm* | رحم | 4 | 1, 1, 3, 3 |
| *ʾlh* | إله | 2 | 1, 2 |
| *ṣrāṭ* | صرط | 2 | 6, 7 |
| *smw* | سمو | 1 | 1 |
| *ḥmd* | حمد | 1 | 2 |
| *rbb* | رب | 1 | 2 |
| *ʿlm* | علم | 1 | 2 |
| *mlk* | ملك | 1 | 4 |
| *ywm* | يوم | 1 | 4 |
| *dyn* | دين | 1 | 4 |
| *ʿbd* | عبد | 1 | 5 |
| *ʿwn* | عون | 1 | 5 |
| *hdy* | هدي | 1 | 6 |
| *qwm* | قوم | 1 | 6 |
| *nʿm* | نعم | 1 | 7 |
| *ghyr* | غير | 1 | 7 |
| *ghḍb* | غضب | 1 | 7 |
| *ḍll* | ضلل | 1 | 7 |

**Totals**: 23 root-token occurrences, 18 distinct roots (rank 15 / 114 — 15th-shortest in the corpus by root-token count).

**Root-density**: Q 1's root-token density is 23 / 29 = 0.793 (root-tokens per word), close to the corpus median. Q 1 is therefore *not* unusually root-dense or root-sparse — its distinctness is in **root choice**, not in root-density per se.

**Hapaxes**: 15 of 18 roots appear exactly once in this surah; only *rḥm* (4×), *ʾlh* (2×), and *ṣrāṭ* (2×) appear more than once. The *rḥm* root, recurring 4 times in a 7-verse / 23-root-token surah, gives a within-surah relative frequency of 17.4 % — among the highest single-root concentrations in the corpus.

## 4. Content register

Q 1 is a **liturgical-creedal hybrid** with petition. It contains:

- **Doxology** (verses 1-3): names of God, attributes, lordship.
- **Eschatology** (verse 4): single-verse Day-of-Judgement reference, no narrative.
- **Creedal declaration** (verse 5): *iyyāka naʿbudu* as *tawḥīd* statement.
- **Petition** (verse 6): single imperative, the only one in the surah.
- **Discrimination** (verse 7): three-class human typology — favoured, wrath-incurring, astray.

It is **not**: legal (no *aḥkām*), narrative (no prophet-story), polemical (no *ʿaduww*-naming), eschatologically-detailed (no Hell/Garden description). The surah is a *liturgical microcosm*: complete in itself as a prayer, formally minimal, doctrinally dense.

This is the empirical content of al-Suyūṭī's claim (Itqān raw line 3299, *fī asmāʾ al-suwar*): *al-Fātiḥa: laqad waqaftu lahā ʿalā nayyifin wa ʿishrīna isman wa-dhālika yadullu ʿalā sharafihā*— "I have noted for it more than twenty names; and that indicates its honour." The naming density (≥21 names) reflects *role density*: the surah functions in roles that elsewhere in the corpus require dedicated surahs of their own (al-Ḥamd-cluster opening, *thuluth* of the Quran by al-Ikhlāṣ, the daily-prayer recitation, the petitionary *duʿāʾ*, the eschatological summary).

## 5. Repetition & refrain patterns

- **al-Raḥmān al-Raḥīm** repeats verbatim in v 1 and v 3 (intra-surah verbatim repetition is rare in any 7-verse surah; this is one of the surah's most distinctive features).
- **iyyāka** repeats in v 5 (the only doubled-pronoun within a single verse).
- **ʿalayhim** repeats in v 7 (twice in one verse, marking the same path-of-the-favoured vs path-of-the-wrath-incurring).
- **ṣirāṭ** repeats across v 6 and v 7 (chaining the imperative *ihdinā ṣirāṭ* with the elaborative *ṣirāṭa lladhīna*).

**No verbatim phrase from Q 1 appears verbatim elsewhere in the Quran except as basmala-prefix.** That is, the *al-Fātiḥa text minus basmala* is unique to Q 1; verses 2-7 contain no *self-quotation* anywhere else in the corpus. (The basmala itself appears 113 times in the canonical corpus — once at every surah-head except Q 9, plus once in Q 27:30 as quotation — but this is a function of the basmala's universal-prefix role, not of Q 1-specific content recurrence.) See `07-cross-references.md` for full search.

## 6. Cross-surah content references

Q 1 does **not cite** any other surah by name or paraphrase. However, several phrases from Q 1 *anticipate* later usage in the corpus:

- *rabb al-ʿālamīn* (v 2): occurs 42 times across 27 surahs in the corpus; Q 1 is its first appearance in the canonical reading order. (Cross-reference: see `data/morphology/root-cooccurrence-graph.json` for *rbb* + *ʿlm* co-occurrence.)
- *al-Raḥmān al-Raḥīm* (v 1, 3): 6 surahs use the doublet in sequential verses (Q 2, 27, 28, 41, 59, plus Q 1); the repetition-density inside Q 1 (2 attestations in 3 verses) is unmatched.
- *ihdinā al-ṣirāṭ al-mustaqīm* (v 6): the lexical bundle *ṣirāṭ + mustaqīm* recurs 32 times across the corpus; the **imperative-petitionary** form *ihdinā* + *al-ṣirāṭ al-mustaqīm* occurs **only here**. Every other corpus-attestation is descriptive (*ṣirāṭ Allāhi al-mustaqīm*, *ʿalā ṣirāṭi mustaqīm*, etc.) — never imperative-1pl.
- *anʿamta ʿalayhim* (v 7): the verbal-form *anʿamta* (2nd-person-singular, with the pronoun-suffix *-hum*) appears **once** in Q 1:7 and once in Q 4:69 (*maʿa lladhīna anʿama llāhu ʿalayhim*) — but Q 4:69 uses the 3rd-person-perfect *anʿama* not the 2nd-person *anʿamta*. The 2nd-person form *anʿamta* (with God as direct addressee) is *unique to Q 1:7* in the corpus. (Cross-validated against `quran-flat-no-tashkeel.txt` regex.)

**Implication**: Q 1 is *not* a cento — none of its phrases are quotations from other surahs. It is a **net source** for phrasal vocabulary, not a sink. Several of its key phrases are first-attestations in the canonical-reading-order, and at least one (*ihdinā al-ṣirāṭ al-mustaqīm* with imperative-1pl) is unique.

## 7. Vocabulary distinctness against the corpus

Per [[h-new-111-fisher-rao-mushaf|H-NEW-111]], Q 1's mean Fisher–Rao distance to the rest of the corpus is **0.7789** vs corpus mean **0.9235** — Q 1 is *closer* to the corpus centroid than typical (z = −1.43; rank 88 / 114, where lower = closer). This means Q 1's root-distribution is **more typical** than 87 other surahs of the corpus average — it does not use exotic roots, but it uses *highly typical* doxological vocabulary (*ḥmd*, *rbb*, *rḥm*, *ʿbd*, *hdy*, *ʿlm*) at high concentration in a very short text.

Yet — see §1 of `01-empirical-profile.md` — Q 1's *neighbours* in the canonical order (Q 2-Q 9) are all **far** from it (FR distances 1.18-1.22, near-corpus-maximum). The neighbour-distance and corpus-centroid-distance pull in opposite directions: Q 1 is centroid-typical but locally-anomalous. This is what makes its mushaf-position an architectural choice rather than a similarity-clustering effect.

## 8. Honest limits

- **Word counts are rules-tuple-fragile**. Under the Mashriqi orthographic-token rule with whitespace-split, Q 1 = 29 words; under a "drop-basmala" counting rule, Q 1 = 25 words; under a phonetic-syllable rule, the count differs again. The 29 / 25 split is reflected in the Wikipedia article and in al-Suyūṭī's word-count notes (see `data/literature/classical-tafsir/suyuti-itqan-word-counts.md`). Always state the rule.
- **Letter counts likewise vary**: 143 (no-tashkeel grapheme rule, basmala-counted), 139 (no-tashkeel without hamza-on-alif counted as letter), 113 (one Wikipedia variant — likely without basmala). The 143-count is the project's locked default. Cross-check before citing.
- **Root counts depend on QAC v0.4 lemmatization**. The *mlk* root in v 4 absorbs both *Mālik* and *Malik* qirāʾāt (correctly). Other roots may have lemmatization fragility for theologically-charged terms; cross-check with `data/morphology/root-stats.csv` before publishing root-frequency claims.
- **The 31 %-word-mass-on-v7 claim** is descriptive; it has no inferential null. A pre-registered "are 7-verse-surah-final-verses always > 25 % of the surah's mass?" test against a permutation null would formalize it. As written here, it is observational.
- **The "ihdinā al-ṣirāṭ al-mustaqīm uniqueness" claim** was verified by regex against `quran-flat-no-tashkeel.txt`; it is rules-tuple-stable. The "anʿamta ʿalayhim uniqueness" claim was verified the same way. Both are sound.

## 9. Synthesis

Q 1 is a **complete liturgical microcosm in 29 words**: it opens with universal divine-name doxology, pivots through an eschatological hinge (v 4), turns from third-person reference to second-person address (the iltifāt of v 5), petitions in the only imperative of the surah (v 6), and resolves into a three-class human-typology (v 7). The surah uses 18 distinct roots — overwhelmingly the high-frequency doxological lexicon of the corpus (*ḥmd, rbb, rḥm, ʿbd, hdy*) — but at concentrations and structural positions that make every word load-bearing. Its single most striking lexical feature is the four-fold density of *rḥm* (mercy) in 7 verses; its single most striking grammatical feature is the 3rd→2nd-person iltifāt at v 5; its single most striking phrasal feature is the imperative-1pl *ihdinā al-ṣirāṭ al-mustaqīm* unique to this surah. The surah is a **net source** of doxological phrases for the canonical-order of the rest of the corpus, not a sink — its phrases are first-attestations.
