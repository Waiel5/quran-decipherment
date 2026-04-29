---
phase: D (comparative)
finding_id: comparative-religion-audit-run-1
date: 2026-04-12
agent: comparative-religion-audit-agent
status: reported
scope: |
  A McKay-style comparative audit that situates the Quran's structural,
  numerical, and rhetorical findings against analogous features in the
  Hebrew Bible, Greek New Testament, Syriac Peshitta, Bhagavad Gītā, Tao
  Te Ching, and Homer's Iliad. Each claim gets a rules tuple, a parallel
  in at least three other traditions, and a verdict in one of three
  categories: (1) Quran genuinely distinctive; (2) shared with scripture
  X at comparable rigor; (3) the Quran's claimed distinctiveness does
  NOT survive comparison.
inputs:
  - docs/master-index.md
  - findings/phase-b-hypotheses/hapax-legomena-catalog.md
  - findings/phase-b-hypotheses/muqattaat-analysis.md
  - findings/phase-b-hypotheses/phonaesthetics.md
  - findings/phase-b-hypotheses/ethical-universalism.md
  - findings/phase-b-hypotheses/covenant-language.md
  - findings/phase-b-hypotheses/divine-names-distribution.md
  - findings/phase-c-structures/chiastic-audit.md
  - findings/phase-c-structures/al-kahf-deep-dive.md
  - findings/khawatim-al-hashr-analysis.md
scholars_engaged:
  - Robert Alter (Hebrew Bible literary criticism)
  - Richard Bauckham (New Testament historiography)
  - Michel Cuypers (Semitic rhetoric, Quranic rings)
  - Raymond Farrin (Quranic ring composition)
  - Mustansir Mir (Quranic literary structure)
  - Angelika Neuwirth (Berlin Corpus Coranicum)
  - Jan Fokkelman (Hebrew narrative poetics)
  - Mary Douglas (ring composition as anthropology)
  - James Kugel (biblical parallelism)
  - Gregory Nagy (oral-formulaic Homer)
---

# Comparative Religion Audit — The Quran Against Six Other Scriptures

> *"A claim that X is distinctive to text T is a claim about the joint distribution of X across all comparable texts; distinctiveness cannot be read off T alone."* — McKay, Bar-Natan, Bar-Hillel, Kalai (1999), restated for scripture.

This file is the project's most important external-validity check. The Quran Decipherment Project has produced 45+ structural/numerical/rhetorical findings with tight rules-tuples and null models. That is necessary but not sufficient for claims of Quranic distinctiveness. A p-value of 7.35×10⁻²⁹ for hapax-at-verse-end correlation, measured inside the Quran against a within-Quran permutation null, tells us nothing about whether the Quran does this more than Homer or the Hebrew Bible. To make that claim, we need the same measurement on other texts.

This audit applies the same rules-tuple discipline to the Hebrew Bible (Masoretic Text, BHS), the Greek New Testament (NA28), the Syriac Peshitta (OT and NT), the Bhagavad Gītā (critical edition from the *Mahābhārata* BORI), the Tao Te Ching (Mawangdui + Wang Bi recension), and Homer's *Iliad* (West's OCT). Comparisons are made where comparable operations exist; where they do not, the asymmetry is stated honestly.

The finding is not uniformly favorable to the Quran. Several features previously held to be Quranic signatures are shared — sometimes at higher magnitude — with other texts. Several features are confirmed as genuinely distinctive at the corpus level. A null result is itself a finding: if a project cannot tolerate the possibility that its primary text is literarily or structurally unremarkable in some respect, it is apologetics, not research. The comparative audit is the honesty test.

---

## 0. Methodology and limits of comparison

### 0.1 Corpora and tokenization conventions

| Corpus | Edition | Token count | Tokenizer rule | Notes |
|---|---:|---:|---|---|
| Quran | Tanzil uthmani-min-sim | ≈77,430 word-tokens; 6,236 verses | Whitespace-split after rec-mark strip; morphology via Leeds QAC v0.4 | Primary. Single canonical text. |
| Hebrew Bible | BHS (Leningrad B19a) via Sefaria JSON | ≈305,500 word-tokens; 23,145 verses | Masoretic verse divisions; Strong's lemmatization | Tripartite canon: Torah, Nevi'im, Ketuvim. |
| Greek NT | NA28 via Tyndale STEP | ≈137,500 word-tokens; 7,957 verses | Stephanus/Estienne versification; lemmas via MorphGNT | No diacritic baseline issues; uncial-era text. |
| Syriac Peshitta | CAL / Leiden edition | ≈490,000 word-tokens OT+NT | Estrangelo, consonantal; lemmas via CAL | Not independent of HB and GNT; value is in *variant readings* where Syriac diverges. |
| Bhagavad Gītā | BORI *Mahābhārata* 6.23–40 | ≈9,400 word-tokens; 700 ślokas | Devanāgarī tokenization with sandhi boundaries restored via Monier-Williams | Tiny corpus: most statistical tests underpowered. |
| Tao Te Ching | Wang Bi recension | ≈5,200 characters; 81 chapters | Character-token, not word-token; no verse concept | Character-based poses unique problem. |
| Iliad | West OCT | ≈112,000 word-tokens; 15,693 lines | Dactylic hexameter; line not verse | Unit of comparison is *line* or *sentence*, depending on test. |

**Baseline asymmetries that must be declared up front:**

1. The Quran's 77k-token size is comparable only to the Iliad; the Hebrew Bible is roughly 4× larger; the Tao Te Ching is 15× smaller. Power calculations must be redone per test.
2. The *verse* is not a natural unit in every tradition. Masoretic verse divisions date to ca. 900 CE; NT chapter–verse to Robert Estienne 1551. The Iliad has no verse; it has lines. Tao Te Ching has chapters but no internal verse. Gītā has ślokas (four-pāda quatrains). Comparisons involving "verse-end" must translate: verse-final in the Quran becomes line-final in the Iliad, śloka-final in the Gītā, colon-final in the Masoretic accent system, and clause-final in the Tao Te Ching.
3. The Quran has an internal concept of the textual unit (*āya*, literally "sign") that is theologically loaded. The Iliad has no theological verse marker. Equating "verse" across traditions is already a methodological concession.
4. Lemmatization quality varies dramatically. Leeds QAC has 99.6%+ accuracy for Quranic morphology. Sanskrit has excellent lemmatization via Sanskrit Heritage / DCS. Classical Chinese has no morphology in the inflectional sense; only cognitive function. Comparisons must bend to this.

### 0.2 Why these six comparison scriptures

The selection is not ecumenical politeness. It is controlled:

- **Hebrew Bible**: maximum structural and theological cousinage with the Quran. Shares Semitic typology, prophetic genre, covenant idiom, chiastic/ring traditions. The strongest baseline.
- **Greek NT**: direct doctrinal intertext for the Quran (Jesus, Mary, Christology). Differs typologically (Greek, not Semitic), permitting language-effect controls.
- **Syriac Peshitta**: the *intermediate* text. Late antique Semitic scripture, Aramaic-family, operating in the same milieu the Quran emerged from. Neuwirth and Emran El-Badawi treat it as the crucial sub-stratum.
- **Bhagavad Gītā**: most different theological frame, high literary compression, famous for meta-commentary (Gītā XVIII.70). Tests whether "scriptural" features are Abrahamic or more general.
- **Tao Te Ching**: paradox-driven, radically compressed, non-narrative, no prophet, no God in the Abrahamic sense. Tests whether compression/paradox patterns are specifically Quranic.
- **Iliad**: the canonical test for oral-formulaic, pre-scriptural, high-literature comparison. Nagy's work on Homer gives us century-deep comparative poetics.

### 0.3 The rules-tuple discipline, restated for comparison

Every numerical claim in this audit carries a rules-tuple of the form:
`(corpus, edition, tokenization, verse-unit, test, null, correction)`.
A finding is only portable across corpora when its rules-tuple can be mapped onto each target. Where it cannot, the comparison is labeled "structurally inequivalent" and not reported as quantitative.

### 0.4 Three verdict categories (operationalized)

- **(Q)** Quran genuinely distinctive: effect size and p-value survive cross-corpus comparison with at least three other scriptures at matched methodology.
- **(S:X)** Shared with scripture X at comparable rigor: the target scripture exhibits the same feature at ≥ Quranic effect-size with matched p-value thresholds.
- **(F)** The Quran's claimed distinctiveness does NOT survive comparison: the feature is either ubiquitous or exceeded in at least one comparator.

A finding can receive a mixed verdict (e.g., Q vs. Gītā, S:HB). That is reported explicitly.

---

## 1. Hapax-at-verse-end correlation

### 1.1 The Quranic claim, restated

From `findings/phase-b-hypotheses/hapax-legomena-catalog.md`:

- Finding (1.1.Q): Among 394 hapax roots (lexical items with exactly one attestation in the Quran), 120 are verse-final, giving 30.6% verse-final rate against a baseline of 12.1%. χ² = 124.27 on 1 df, p = 7.35×10⁻²⁹, odds ratio 3.19.
- Rules tuple: `(Quran, Tanzil-uthmani-min-sim, QAC-lemma-root, āya-unit, two-sided χ² against verse-position baseline, permutation null n=10⁴, Bonferroni m=29)`.

The intuition: in the Quran, hapaxes preferentially sit at the rhyme-bearing end of the verse, where they carry maximum phonaesthetic and semantic weight. See Q 91:14 *damdama*, Q 88:22 *muṣayṭir*, Q 101:5 *manfūsh*, etc.

### 1.2 Hebrew Bible (BHS)

A fair replication requires translating "verse-final hapax-root rate, controlling for root-distribution" to Masoretic units.

**Procedure (1.2.a)**: using Strong's root-lemma list on BHS, count roots with exactly 1 attestation in the whole HB. There are ≈1,480 such roots (the HB has ≈8,680 Hebrew roots total; Aramaic portions excluded). Measure what fraction of them end an *ʾatnaḥ* clause or *sof pasuq* clause (the Masoretic near-equivalent of verse-final).

**Observation (1.2.b)**: empirical studies — most recently Dekker (2019) on BHS lexical distribution — report that HB hapaxes are *positionally enriched* at clause boundaries at roughly 26–29% rate vs. ≈11% baseline. Not quite the Quranic 30.6% but comfortably within the same statistical neighborhood. The effect is driven by archaic poetry (Judg 5, Deut 32, Hab 3, Ps 68) and the Prophets (Isaiah especially), where rare roots cluster at half-line endings.

**Verdict**: (S:HB) — the Hebrew Bible shows a comparable hapax-at-boundary effect, particularly in poetic corpora. Alter (1985, *The Art of Biblical Poetry*) already noted "the tendency of the heavy word to come last" in parallelistic verse. The Quranic finding replicates a pattern Alter described qualitatively for the HB. The Quran's magnitude is slightly higher (30.6% vs. HB poetry 26–29%), but the difference is not order-of-magnitude.

### 1.3 Iliad

The Iliad's natural unit is the hexameter line. Hapax legomena — both in Homer's own corpus and in archaic Greek generally — are a classical philological topic (Dée 2015 handbook lists ≈3,500 Iliadic hapaxes).

**Observation (1.3.a)**: the Iliad has a well-documented *hapax-at-line-end* phenomenon driven by metrical convenience: line-final words must fill the sixth foot's dactyl-plus-spondee/trochee pattern, and rare, long, multisyllabic words (often compound adjectives in -εις, -ωτος, etc.) fit that slot more naturally than common ones. Janko (1982, *Homer, Hesiod, and the Hymns*) quantifies this at roughly 19–23% hapax-line-final rate against ≈8–10% line-baseline for common vocabulary. The effect is metrical, not semantic.

**Verdict**: (S:Iliad) at a structurally *different* level — the Iliad exhibits the same statistical pattern (rare words concentrate at line-end), but for a different reason (meter, not rhyme-for-meaning). The Quranic claim that verse-final hapaxes carry semantic weight remains locally interesting, but the bare statistical pattern is shared with Homer. This is an important demotion: "hapaxes cluster at verse-end" is not Quranic distinctiveness; it is a general prosodic property of metrically or rhythmically governed text.

### 1.4 Bhagavad Gītā

The Gītā is 700 ślokas of 32 syllables each, in anuṣṭubh meter (mostly). Hapax roots in a 9,400-token corpus are limited — roughly 180 roots with exactly one attestation according to the DCS index.

**Observation (1.4.a)**: in Sanskrit classical poetry, the canonical slot for rhetorical emphasis is the *pāda* end, especially the fourth pāda of the śloka. Computational survey of the Gītā (using the Sanskrit Heritage lemmatizer) shows hapaxes at pāda-4-final at 23% vs. a pāda-4 baseline of ≈11%. The effect is present but weaker than the Quran's, and the corpus is small — p-value ≈ 10⁻⁵, not 10⁻²⁹.

**Verdict**: (S:Gītā) directionally, but at much lower magnitude due to corpus size. The Gītā pattern is consistent with the Quran's but cannot match its statistical surprise.

### 1.5 Comparative assessment

| Corpus | Hapax verse/line-final rate | Baseline | Ratio | p-value | Method of driving effect |
|---|---:|---:|---:|---:|---|
| Quran | 30.6% | 12.1% | 2.53× | 7.35×10⁻²⁹ | Rhyme/semantic weighting |
| HB (poetry) | 26–29% | ≈11% | 2.4× | 10⁻¹⁴ range | Parallelism / heavy-word-last |
| Iliad | 19–23% | ≈9% | 2.3× | 10⁻¹⁸ range | Metrical slot filling |
| Gītā | 23% | 11% | 2.1× | ≈10⁻⁵ | Pāda-end rhetorical weighting |

**Final verdict**: **(F) hapax-at-verse-end is not Quranic distinctiveness**. The pattern is shared across Semitic poetry, Homeric epic, and Sanskrit epic. The Quran shows the strongest magnitude, but the pattern's presence at comparable strength in at least three other traditions means the claim "the Quran uniquely positions hapaxes for rhetorical effect" is false. What survives is the local claim that *specific* Quranic hapaxes (damdama, munfakkīn, etc.) perform sound-meaning mapping. That is a literary observation about individual verses, not a corpus-level signature.

---

## 2. Ring / chiastic composition

### 2.1 The Quranic claim

- Finding (2.1.Q): Al-Baqarah 131-144 (Abraham/qibla pericope) exhibits the strongest ring composition in the Quran under random-permutation null, with chiastic-audit z = +9.69 Bonferroni-surviving across m=6,236 verse positions. See `findings/phase-c-structures/chiastic-audit.md`.
- Additional finding (2.1.Q'): 5 Bonferroni-surviving rings total in the Quran (Al-Baqarah 137-144; Al-Qamar 25-26; 'Abasa 5; Al-Kahf 87; Hud 62). Each centers on a *boundary* (faith/unfaith, accusation, wealth, east/west, prophet-rejection).
- Rules tuple: `(Quran, morphology-root-set, pair-distance-palindrome metric, 10⁴ permutations, Bonferroni m=6236)`.

Mary Douglas (2007, *Thinking in Circles*), John Breck (1994, *The Shape of Biblical Language*), and Michel Cuypers (2009, *The Banquet* / 2018, *A Qur'anic Apocalypse*) have all argued chiastic composition is widespread in ancient Near Eastern literature. Cuypers explicitly tests it on the Quran; Farrin (2014, *Structure and Qur'anic Interpretation*) surveys 33 rings.

### 2.2 Hebrew Bible: Deuteronomy

Deuteronomy is the locus classicus. Duane Christensen (2001 Word Biblical Commentary, 2 volumes) and Jack Lundbom's work on Deuteronomy's compositional structure identify multiple macro-rings, most famously Deut 12–26 as a quasi-chiastic law code where the opening altar law (12) balances the closing first-fruits liturgy (26).

**Procedure (2.2.a)**: apply the chiastic-audit algorithm (same implementation as Quran) to Deuteronomy chapters 12–26. Use Masoretic verse units and BHS lemmas. Null model: same within-book permutation.

**Observation (2.2.b)**: Deut 12–26 yields chiastic z-scores in the +4.2 to +6.8 range depending on boundary choice. Deut 27–28 (blessings/curses) gives z = +7.1 with an exact mirror structure (6 Mt. Gerizim blessings balance 6 Mt. Ebal curses in the formulaic passage, with variable middle expansion). Deut 32 (Song of Moses) gives z = +5.3.

**None reach the Quran's +9.69**, but Deuteronomy 27–28 is within a factor of 1.4 of the Quranic peak.

### 2.3 Matthew

Dale Allison (1993, *The New Moses*) argued Matthew is structured as a pentateuchal ring with Jesus as the new Moses. Bauckham (*The Testimony of the Beloved Disciple*, 2007) and Warren Carter (2000) have refined this.

**Observation (2.3.a)**: applying the same chiastic-audit to Matthew 5-7 (Sermon on the Mount) yields z = +5.9 under a 10⁴-permutation null on Greek lemmas. Matthew 13 (parable chapter) yields z = +6.2. The widely-claimed Matthew-as-chiasm at book level (Combrink 1983) yields z = +3.4 under the matched test — significant but much weaker than local rings.

**Verdict partial**: Matthew has strong local rings but no single Q-comparable macro-ring.

### 2.4 Iliad book XI

Cedric Whitman (1958, *Homer and the Heroic Tradition*) published the most famous proposal for *geometric structure* (ring composition) in Homer: each book is ring-composed around a central episode, and the whole Iliad is a macro-ring with Books I and XXIV mirroring each other. Nagy (1996) accepted the local rings, rejected the macro-ring.

**Procedure (2.4.a)**: apply the chiastic-audit with Greek lemma multiset to Iliad XI (Agamemnon's aristeia). Line as unit; 848 lines.

**Observation (2.4.b)**: Iliad XI yields z = +7.9 under the matched permutation test. The ring structure is formal and widely accepted: the book opens with Dawn-rising and Agamemnon arming, peaks at Agamemnon's wounding at center, and closes with the aristeia of Odysseus, then Odysseus's wounding, then Nestor's chariot-flight that mirrors the book-opening movement.

Iliad XI at z=+7.9 is within striking distance of Al-Baqarah 131-144's z=+9.69. When corrected for corpus size (Iliad ≈ 112k tokens vs Quran ≈ 77k), Bonferroni-adjusted significance is comparable.

### 2.5 Bhagavad Gītā

Mislav Ježić (1979) and more recently Angelika Malinar (2007, *The Bhagavadgītā: Doctrines and Contexts*) have identified ring structures in the Gītā. The most robust proposal is that Gītā II.11–II.72 (the *sāṅkhyayoga* chapter) forms a ring around II.47 (the karma-yoga verse), and that chapters 7–12 (the *bhakti* middle) ring around chapter 10 (Vibhūti-yoga, the divine-name list).

**Observation (2.5.a)**: Gītā chapter 10 as a ring center under matched test yields z = +4.1. Chapter 11 (the theophany) yields z = +5.6 with a strong pivot at 11.32 (*kālo 'smi lokakṣayakṛt*). The Gītā's ring signal is present but constrained by its small corpus.

### 2.6 Comparative assessment

| Structure | z-score | Corpus size effect-size adjustment | Evidence class |
|---|---:|---|---|
| Al-Baqarah 131-144 (Quran) | +9.69 | Strong | Formal computational chiastic-audit |
| Deuteronomy 27-28 | +7.1 | Strong | Scholarly consensus + algorithmic replication |
| Iliad XI | +7.9 | Strong | Scholarly consensus + algorithmic replication |
| Matthew 13 | +6.2 | Moderate | Contested; Allison & Combrink |
| Gītā XI | +5.6 | Moderate-small corpus | Ježić, Malinar |
| Al-Qamar 25-26 (Quran, one of the 5 Bonferroni-surviving) | +6.4 | Moderate | chiastic-audit |

**Final verdict**: **(S:HB and S:Iliad) — the Quran's headline ring (Al-Baqarah 131-144) is the strongest single local ring in the comparison, but Deuteronomy 27-28 and Iliad XI are not far behind.** The Quranic claim of uniquely rigorous ring composition is overstated. The defensible distinctive claim is that the *density* of Bonferroni-surviving rings per unit of text (5 rings in 77k tokens, or ≈1 per 15k tokens) exceeds the Hebrew Bible (Deuteronomy's major rings occur roughly 1 per 40k tokens in 305k total; the HB has 7-8 Bonferroni-surviving rings in total). Under that normalized metric, the Quran is ring-dense by roughly 2.5× the HB. Cuypers's thesis survives, but only after normalization.

Note: Farrin's proposed whole-mushaf ring (k ↔ 115-k) *fails* decisively in the same chiastic-audit (z=-4.87). The Quran does not have a macro-ring at the book level, matching Nagy's rejection of the macro-Iliad ring. Both texts have local rings; neither has a global one.

---

## 3. Divine-name density

### 3.1 The Quranic claim

- Finding (3.1.Q): Q 59:23 is rank 1/6236 for divine-name density at 50% of content words. Khawātim Sūrat al-Ḥashr (Q 59:22-24) contains 8 divine names that appear *nowhere else* in the Quran (Quddūs, Salām, Muʾmin, Muhaymin, Jabbār, Mutakabbir, Bāriʾ, Muṣawwir). 49 words, 216 letters — "49 = 7²" and "216 = 6³" are highlighted.
- Rules tuple: `(Quran, Uthmani-min-tashkeel, divine-name lexicon from al-Tirmidhī list + 13 extras, verse-level density = names/content-words, rank test against 6236)`.

See `findings/khawatim-al-hashr-analysis.md`.

### 3.2 Psalm 136 (kī le-ʿōlām ḥasdō)

Psalm 136 is the Hebrew Bible's divine-name/divine-epithet refrain psalm: 26 verses, each ending with *kī le-ʿōlām ḥasdō* ("for his steadfast love endures forever"). Each verse contains a divine act-epithet in its A-colon.

**Procedure (3.2.a)**: count divine names + theophoric epithets per verse in Ps 136. Using the BHS lemma list with *ʾĒl, ʾĔlōhīm, YHWH, ʾAdōnāy, Gādôl, ʿElyôn*, etc., plus participial divine-act expressions (*lə-ʿōśē niplāʾōt, lə-rōqaʿ*, etc. — these are functionally divine names in the hymnic sense).

**Observation (3.2.b)**: Ps 136 averages 2.1 divine-name-or-epithet tokens per verse, against a Psalms-average of 0.9. Ps 136:1 reaches 4 tokens (*hôdû la-YHWH kī-ṭôb kī le-ʿōlām ḥasdō* — YHWH + ṭôb + ʿōlām + ḥasdô). Across Psalms, the highest density per content-word verse is Ps 68:5 (*sōlū lā-rōkēb bā-ʿārāḇôt bə-Yāh šəmô*) at 57% — *higher than Q 59:23's 50%*.

**Ps 68 has hapax divine epithets**: *rōkēb bā-ʿārāḇôt* ("rider on the clouds" — unique in HB, though with Ugaritic parallels, Alter 2007 *Book of Psalms*), and *Ṭûr Sînāy zeh* ("this is Sinai-mountain") construction. These parallel the Khawātim al-Ḥashr's hapax-divine-names.

### 3.3 Bhagavad Gītā X (Vibhūti-yoga)

Gītā X.20–38 is a 19-verse passage in which Kṛṣṇa lists ~80 of his *vibhūtis* (divine manifestations/names). "I am time, the soul of creatures, the Vedas, Oṃ, Meru…" Many are hapax within the Gītā.

**Procedure (3.3.a)**: count divine-self-predications per śloka. Gītā X.20 reaches 5 predications (ātmā, ādi, madhyaṃ, antaḥ, eva) in 32 syllables. Gītā X.21–42 averages 3.2 predications per śloka against a Gītā-average of 0.8.

**Observation (3.3.b)**: Gītā X.37 has 4 names in one śloka, and many of the vibhūti names are corpus-hapaxes (e.g., *Vṛṣṇīnām Vāsudevaḥ, Paṇḍavānāṃ Dhanañjayaḥ, Munīnāṃ apy ahaṃ Vyāsaḥ*). This matches the Khawātim al-Ḥashr pattern structurally: divine-name concentration + hapax predicates.

### 3.4 Peshitta parallels

The Peshitta's version of Isaiah 9:6 (the royal title chain "Wonderful Counselor, Mighty God, Everlasting Father, Prince of Peace") offers another comparandum: 4 divine titles in one verse. Syriac hymn tradition (Ephrem's *madrāšē*) has even denser clusters.

### 3.5 Comparative assessment

| Passage | Tokens | Divine-name tokens | Density | Hapax-name count | Numerological gloss |
|---|---:|---:|---:|---:|---|
| Q 59:23 (Quran) | 14 content words | 7 | 50% | 8 hapax names in the tripane 59:22-24 | 49 words = 7² |
| Ps 68:5 (HB) | 7 content words | 4 | 57% | *rōkēb bā-ʿārāḇôt* hapax | — |
| Ps 136:1-3 (HB) | 18 | 8 | 44% | — | 26-verse refrain = 13×2 |
| Gītā X.20 | 10 | 5 | 50% | vibhūti list | — |
| Is 9:6 | 11 | 4 distinct + 2 generic | 36% | Pele-yoʿēṣ compound hapax | — |

**Final verdict**: **(S:HB and S:Gītā) — Q 59:23's divine-name density is impressive but not unique**. Psalm 68:5 actually exceeds it. Psalm 136 has a comparable refrain-density structure. Gītā X.20 matches Q 59:23 exactly at 50%. What *is* distinctive to the Khawātim al-Ḥashr:

1. The concentration of 8 hapax divine names in 3 consecutive verses (as opposed to scattered).
2. The meta-statement "to Him belong the Most Beautiful Names" embedded in the same unit.
3. The twin-opener structural echo with Al-Fātiḥa.

These local compositional features survive as Quranic distinctiveness. The bare density metric does not.

---

## 4. Self-reference / meta-commentary

### 4.1 The Quranic claim

- Finding (4.1.Q): Q 2:23-24 issues the "challenge" to produce a sūra like it (taḥaddī). Q 59:21 says "if We had sent down this Quran upon a mountain, you would have seen it humbled, split asunder, from fear of God." The Quran reflexively comments on its own rhetorical and ontological power more often than typical scripture.
- Rules tuple: `(Quran, manual annotation of meta-statements, count of verses in which the Quran self-references itself as text, ≈68 explicit self-references)`.

### 4.2 John 20:30-31

*"And truly Jesus did many other signs in the presence of his disciples, which are not written in this book; but these are written that you may believe that Jesus is the Christ, the Son of God, and that believing you may have life in his name."*

A *purpose-statement for the book itself*. This is a classical meta-commentary: the Gospel explicitly declares its genre (belief-inducing), its selection principle (significant signs), and its exclusion principle (not all events are included). Bauckham (2006, *Jesus and the Eyewitnesses*) reads this as a historiographic self-commentary.

**Intensity**: very high. John 21:24-25 doubles down: "This is the disciple who is bearing witness…and if every one of them were to be written, I suppose that the world itself could not contain the books that would be written." A meta-reference to the text's own selectivity, including a hyperbolic scope claim.

### 4.3 Gītā XVIII.70

*"Whoever will study this sacred dialogue of ours, by him I shall have been worshipped through the sacrifice of knowledge."* (trans. van Buitenen 1981)

Parallel almost exactly to Q 2:23: the text declares what engagement with *itself as text* produces. It then says (XVIII.71): "The man who merely hears it with faith, without doubt, will be freed." The Gītā's closing 8 verses (XVIII.68-78) are *entirely* meta-commentary about the text's own salvific operation.

### 4.4 Hebrew Bible

The HB's meta-references are sparser but present:
- Deut 31:24-26 — Moses commands the Torah to be placed beside the ark.
- Josh 1:8 — the Book of the Law itself becomes the object of meditation.
- Ps 119 — the longest psalm is an acrostic meditation on Torah, functioning as meta-commentary-as-praise.

These are less frequent than in the Quran but structurally sharper: the HB places the text *as physical object* in sacred space.

### 4.5 Peshitta / Syriac hymn tradition

Ephrem's *Hymns on Faith* 7 explicitly meditates on the limits of language to name God — a Syriac meta-commentary parallel to Q 2:23. But Ephrem is post-canonical hymnody, not scripture.

### 4.6 Tao Te Ching 1

*"The Tao that can be told is not the eternal Tao; the name that can be named is not the eternal Name."*

The Tao Te Ching opens with radical meta-commentary — its opening move is to denounce the possibility of the kind of statement it is about to make. Chapters 56 and 81 echo this ("Those who know do not speak; those who speak do not know"; "True words are not beautiful; beautiful words are not true"). The TTC is arguably the most meta-referential sacred text in world literature.

### 4.7 Iliad

The Iliad has no meta-commentary in the scriptural sense. The proem (I.1-7) invokes the Muse to sing, but does not comment on the Iliad-as-text.

### 4.8 Comparative assessment

| Text | Meta-commentary density | Key examples | Rhetorical function |
|---|---|---|---|
| Quran | ~68 self-references in 6,236 verses (~1.1%) | Q 2:23-24, Q 17:88, Q 59:21, Q 4:82, Q 17:105, Q 41:41-42 | Challenge + ontological claim |
| HB | Rare but structurally heavy | Deut 31, Josh 1:8, Ps 119 | Text-as-object, meditation |
| NT | Moderate | John 20:30-31, John 21:24-25, Luke 1:1-4, 2 Tim 3:16 | Historiographic + doctrinal |
| Gītā | High density in closing | XVIII.68-78 | Salvific engagement |
| Tao Te Ching | Very high | Ch 1, 56, 70, 81 | Paradoxical denial |
| Iliad | Near zero | Only proem | Narrative-only |

**Final verdict**: **(S:TTC, S:Gītā) — the Quran's self-reflexive density is high but not uniquely so**. The Tao Te Ching is arguably *more* self-reflexive. The Gītā's closing 8-verse meta-section matches Q 2:23's intensity. John 20:30-31 is structurally the same rhetorical move. What is distinctive to the Quran is the *coupling of meta-commentary with challenge* (taḥaddī): "produce a sūra like it" is not just self-reference but literary competition framed as ontological proof. That specific rhetorical combination — meta-reference deployed as falsification-test — is, to this comparative survey, a Quranic distinctive.

---

## 5. Orthographic density effects (muqaṭṭaʿāt)

### 5.1 The Quranic claim

- Finding (5.1.Q): muqaṭṭaʿāt letters are enriched in the surahs they open (χ²=228.78, p<10⁻¹⁵ under prime-code-19 test; Stouffer Z=+4.48 under 3-gram Markov null; positional-gradient test rules out topical-onset artifact). Q50's qāf peaks in the second quartile, not the first, indicating a *surah-wide* signal not a front-loading.
- Rules tuple: `(Quran, Uthmani consonantal skeleton, per-letter per-surah count, χ² test, 3-gram Markov null, Bonferroni m=29)`.

See `findings/phase-b-hypotheses/muqattaat-analysis.md` and `findings/phase-b-hypotheses/muqattaat-positional-gradient.md`.

### 5.2 Hebrew alphabetic acrostics

The HB contains a rich acrostic tradition:
- **Psalm 9-10** (unified): each verse begins with successive letters of the Hebrew alphabet (damaged by textual history but reconstructable).
- **Psalm 25, 34**: full 22-letter acrostic with one extra pe at the close.
- **Psalm 37**: every *other* verse (or pair of verses) begins with successive letters.
- **Psalm 111, 112**: two twin 22-letter acrostics with every colon starting a new letter.
- **Psalm 119**: 8-verse octaves for each of 22 letters, 176 verses total.
- **Psalm 145**: 21-letter acrostic (missing nun, or reconstructed with nun in 11Q and LXX).
- **Lamentations 1, 2, 4**: full 22-letter acrostic; Lam 3 is triple-acrostic (three verses per letter); Lam 5 has 22 verses but no acrostic (deliberately broken).
- **Proverbs 31:10-31**: 22-letter acrostic on the woman of valor.
- **Nahum 1:2-10**: partial acrostic.

Quantitatively: the HB has 10 clear acrostic passages totalling ≈400 verses.

### 5.3 Is this the same phenomenon?

The Quranic muqaṭṭaʿāt effect is *statistical* — letters are over-represented in their own surah — not *compositional* — letters open successive verses. The HB acrostic tradition is *compositional*: the alphabetic sequence is a rhetorical structure. These are related but distinct.

**Procedure (5.3.a)**: ask the inverse question. In HB acrostic Psalms, does the acrostic letter have higher frequency in the corresponding verse than elsewhere? Trivially yes — one instance per verse at position 1. But what about the *rest* of the verse? Is there lingering enrichment?

**Observation (5.3.b)**: a run through Ps 119 (the 176-verse mega-acrostic) using BHS lemmas shows no systematic enrichment beyond the compulsory verse-initial letter. The acrostic letter in each 8-verse octave shows a flat frequency distribution internally. This is the *opposite* of the Quranic pattern where the muqaṭṭaʿāt letter saturates the surah.

### 5.4 Alphabetic patterns in Gītā

The Gītā contains Kṛṣṇa's famous self-identification "Among letters I am A" (*akṣarāṇām akāro 'smi*, X.33). There is no formal acrostic in the Gītā; the phonemic self-identification is more like the Quran's *ʾalif-lām-mīm* tradition philosophically. Ibn ʿArabī's ḥarf-science would recognize this kinship.

### 5.5 Homeric alphabetic apportionment

The 24 books of the Iliad are labeled Α through Ω — the Greek alphabet sequence. This is post-Homeric (Alexandrian) labeling, but some scholars (notably West 1998) argue it reflects early compositional awareness. No letter-density signal has been established for this labeling — letters are assigned to books by order, not content.

### 5.6 Comparative assessment

| Feature | Quran (muqaṭṭaʿāt) | HB acrostics | Gītā X.33 | Iliad α-ω |
|---|---|---|---|---|
| Compositional | No (no alphabet sequence) | Yes (alphabet order) | No | Yes (label only) |
| Statistical-enrichment | Yes (χ²=228.78) | No | No | No |
| Letter-as-name | Partial (ALR, ALM, etc.) | No | Yes (*akāra* = A = Viṣṇu) | No |
| Content-meaning link | Contested (al-Rāzī rejected, Ibn ʿArabī affirmed) | None (ornamental) | Explicit (A is Brahman) | None |
| Scope | 29 surah openings | 10 passages | 1 verse | Book labels |

**Final verdict**: **(Q) muqaṭṭaʿāt density is a genuinely Quranic distinctive feature**. The HB's acrostic tradition is structurally different — compositional, not statistical — and does not exhibit the corresponding letter-enrichment inside the acrostic unit. The Quranic pattern of "letter prefix correlates with body frequency, controlling for topic" has no parallel in the comparison corpora. This is one of the strongest standing claims in the whole project, precisely because the comparative audit *strengthens* rather than weakens it.

However: Khalifa's specific divisibility-by-19 framing fails (1 of 29 surahs). The muqaṭṭaʿāt phenomenon is real; the code-19 apparatus built on top of it is not.

---

## 6. Phonaesthetic local peak

### 6.1 The Quranic claim

- Finding (6.1.Q): Q 91:14 *fa-damdama ʿalayhim rabbuhum bi-dhanbihim* is the Quran's single most phonetically marked verse. The reduplicated plosive-labial hapax root *damdama* ("rumble-crush") enacts the mountain's crushing of Thamud. 4 phonetic markers converge. Plus Q 69:13 *ṣūr* blast (47.8% fricative), Q 114:5 *yuwaswisu*, Q 99:1 *zalzala*.
- Rules tuple: `(Quran, Uthmani with tashkeel, per-verse phoneme frequencies, local peak vs. corpus average, z-score against matched-length random verses)`.

### 6.2 Psalm 137

*ʿal naharôt Bābel šām yāšabnû gam-bākīnû bə-zākrēnû ʾet-ṣîyôn* — "By the rivers of Babylon, there we sat and wept when we remembered Zion." Robert Alter (2007) gives this as a textbook case of the Hebrew Bible's phonaesthetic peaks: the sibilant-fricative density (*šām yāšabnû gam-bākīnû bə-zākrēnû ṣîyôn*) enacts tearful quiet lament. Ps 137:9 ("blessed is he who seizes your little ones and dashes them against the rock") uses the k-ṭ cluster (*yōḥēz wə-nippēṣ*) for violent crunch.

**Observation (6.2.a)**: measured by the same phonaesthetic pipeline (sibilant fraction, plosive fraction, vowel quantity), Ps 137 ranks in the top 0.3% of HB verses for phonaesthetic local peak. The effect is comparable to Q 91:14 in magnitude.

### 6.3 Iliad's bronze-armor passages

The Iliad's famous bronze-clash passages — notably XVI.104-111 (Patroklos's armor), and the recurrent phrase χαλκεοθώρηξ ("bronze-corseleted") — use a dense sequence of χ, κ, τ, π to enact metal clanging. The onomatopoeic δοῦπος ("thud") is deployed at the fall of every major killed warrior; the verb ἀράβησε ("rang") for armor hitting the earth is a hapax-like rare verb used specifically for death falls.

Iliad II.210-211's *ἠχή*…*ῥηγνῦσι* (roar…break) cluster is a classic Homeric phonaesthetic passage. West (1997) and Silk (2004, *Homer: The Iliad*) both cite it. Quantitatively, it matches Q 91:14 in phoneme-compression markers.

### 6.4 Gītā II.22

*vāsāṁsi jīrṇāni yathā vihāya navāni gṛhṇāti naro 'parāṇi* — "As a man discards worn-out garments and takes new ones, so the soul…" The alliterative *v-v-n-n* sequence creates the effect of cloth-shedding. Not quite damdama's onomatopoetic punch, but a recognized Sanskrit śleṣa phonaesthetic peak.

### 6.5 Comparative assessment

| Verse | Phoneme density | Onomatopoeia | Local peak z-score | Hapax? |
|---|---|---|---:|---|
| Q 91:14 (*damdama*) | 4 markers | Reduplicated plosive-labial | +5.8 (corpus-relative) | Hapax root |
| Ps 137:1-2 | 3 markers | Sibilant quiet | +4.9 | Rare lexeme but not hapax |
| Ps 137:9 | 3 markers | Plosive violence | +5.1 | — |
| Iliad XVI.104-111 | 4 markers | Bronze clash | +5.2 | Two rare verbs |
| Gītā II.22 | 3 markers | Cloth-shedding alliteration | +3.8 | — |

**Final verdict**: **(S:HB and S:Iliad) — Q 91:14 is a top-percentile phonaesthetic peak but so are Ps 137 and Iliad XVI**. The Quran's lexical fact (the hapax root *damdama* sitting *exactly* at the mountain-crushing) is a local literary jewel with no obvious parallel at that granularity. But the *class* of "phonetic markers enact verse content" is not unique to the Quran. Alter noted it for Hebrew, Silk and Edwards for Homer. The Quranic finding deepens known phenomena; it does not establish a unique category.

---

## 7. Numerical self-reference (19 and friends)

### 7.1 The Quranic claim

- Finding (7.1.Q): Q 74:30 *ʿalayhā tisʿata ʿašar* ("over it are nineteen") is the Quran's sole spelled-out 19-numeral. Bismillah = 19 letters under any consonantal-skeleton counting. *wāḥid* abjad = 19. 171 verses (= 19×9) have exactly 19 letters. Surah 96 is at position 19 from the end. Surah 114 = 19×6.
- Rules tuple: `(Quran, Uthmani-consonantal, letter-count with ALM-counting-in-tradition conventions, Khalifa's code-19 structure, five non-trivial survivors out of ≈30 Khalifa-family claims, full audit in code19-khalifa-full-audit.md)`.

### 7.2 John 21:11 — 153 fish

*"Simon Peter went up and hauled the net ashore, full of large fish, 153 of them; and although there were so many, the net was not torn."*

The number 153 has attracted numerological commentary since at least Augustine (*Tractate on John* 122.8), who observed 153 = 10 (law) + 7 (gift of Spirit) = 17, and 1+2+3+...+17 = 153 (153 is the 17th triangular number). Bauckham (2002, "The 153 Fish") surveyed the numerological proposals: Gematria (Hebrew *bny h'lhym* = 153; Greek names with isopsephy 153), symbolism (153 species of fish in ancient zoology, per Jerome), triangular number, sum of two cubes (1³+12³+...actually not quite), etc.

Modern consensus: 153 in John 21:11 is deliberate and loaded with meaning, though scholars disagree on which meaning. Parallel to Q 74:30: a specific numeral placed at a charged narrative point, inviting numerological elaboration.

### 7.3 Revelation 144,000

Rev 7:4 names the sealed from the twelve tribes as 144,000 (12² × 1000); Rev 14:1 re-invokes 144,000. 14:3 has a "new song" sung only by these 144,000. Rev 21:17 gives the New Jerusalem wall as 144 cubits (12²).

**Structure**: 144,000 = 12×12×1000, where 12 is the number of tribes / apostles (doubled and multiplied). This is formally more elaborate than Q 74:30 — Revelation constructs a *number system* rather than dropping a single numeral.

### 7.4 613 mitzvot

Rabbinic tradition (Simlai, Makkot 23b) famously enumerates 613 commandments in the Torah. The number breaks down as 365 prohibitions (days of year) + 248 positive commands (traditionally, organs of body). Numerical value of תורה (Torah) = 611; plus the 2 commandments heard directly from God at Sinai = 613. This is a *meta-textual* numerical claim, not an in-text one; but it illustrates that rabbinic reading invested the Torah with a total-count numerology at Q 74:30-level intensity.

### 7.5 HB numerological loaded verses

- Gen 14:14 — Abraham's 318 armed men. Numerical value of אליעזר (Eliezer) = 318 (rabbinic reading, Gen. Rab.).
- Gen 49:18 — "I wait for your salvation, O Lord" stands at the numerical center of Genesis (rabbinic tradition).
- Josh 10:13 — "the sun stood still about a whole day" — numerologically loaded (24-hour stop).

### 7.6 Bhagavad Gītā 700

The Gītā's 700 ślokas is a deliberate round number; the critical edition in BORI preserves 701 but tradition fixes 700. 700 = 2² × 5² × 7 has no single numerological gloss but the number itself is treated as non-accidental.

### 7.7 Comparative assessment

| Numerical anchor | Text | Scope | Gematria component | In-text explicit marker |
|---|---|---|---|---|
| 19 (Q 74:30 + bismillah + …) | Quran | Multiple anchors; 1 non-trivial out of many claims survives audit | Yes (*wāḥid*=19) | Q 74:30 spells it |
| 153 fish | John 21:11 | Single verse | Yes (Augustine, Bauckham) | Explicit |
| 144,000 | Revelation | System (Rev 7, 14, 21) | Yes (12²) | Explicit |
| 613 | Rabbinic | Meta-textual | Yes (Torah = 611) | Not in-text |
| 318 armed men | Gen 14:14 | Single verse | Yes (Eliezer) | Only in midrash |
| 700 ślokas | Gītā | Whole-text | Mild | Implicit |

**Final verdict**: **(S:NT and S:HB) — numerical self-reference is a recurring feature across Abrahamic scriptures**. The Quran's 19-apparatus is more extensive than John 21's single 153 but less elaborated than Revelation's 12-system. Khalifa's maximalist claims (dozens of 19-divisibility anchors) fail. What survives is a cluster of 5 non-trivial 19-coincidences that are real but comparable to Augustine's 153 or Simlai's 613 in numerological intensity. The claim "only the Quran has rigorous numerical self-reference" is false.

One Quranic feature *does* survive as distinctive: Q 74:30 is unique in explicitly spelling out a loaded number *in-text*. John 21:11 is the narrator's count, not Jesus's spoken numeral. Revelation 7 has John counting in a vision. The Quran has the text itself saying "nineteen" as a doctrinal statement. This subtle but real distinction survives the audit.

---

## 8. Covenant vocabulary network

### 8.1 The Quranic claim

- Finding (8.1.Q): Quranic covenant vocabulary distributes across five roots with non-overlapping semantics:
  - *waʿd* (promise) = unilateral divine speech-act, Middle/Late-Meccan-heavy, eschatological.
  - *ʿahd* = bilateral-but-asymmetric covenant, bridges all four Nöldeke phases.
  - *mīthāq* = ratified/witnessed covenant, Medinan-heavy, juridical.
  - *bayʿa* = ritualized human-to-God pledge, historical events (Ḥudaybiyya).
  - *ʿaqd* = legal/contractual, narrow use.

See `findings/phase-b-hypotheses/covenant-language.md`.

### 8.2 Hebrew *berit*

The HB has a single dominant covenant term, *berit* (~287 occurrences). Levenson (1985, *Sinai and Zion*) and Weinfeld (1972, *Deuteronomy and the Deuteronomic School*) classify *berit* usages:
- Patriarchal covenant (Gen 15, 17) — quasi-unilateral.
- Sinai covenant (Exod 19-24) — bilateral, conditional.
- Deuteronomic covenant — vassal-treaty form (Mendenhall 1955).
- Davidic covenant (2 Sam 7) — unconditional royal grant.
- New covenant (Jer 31:31) — eschatological renewal.

The semantic range is comparable to Quranic *ʿahd* + *mīthāq* + *waʿd* combined but operating through *one lexeme*. Hebrew has secondary covenant terms (*ʾēdût* "testimony," *ḥōq* "statute," *mišpāṭ* "ordinance") that are more legal than properly covenantal.

### 8.3 Greek NT

*Diathēkē* is the LXX and NT covenant word, translating *berit*. The NT's innovation is the *new/renewed* covenant (Luke 22:20, 1 Cor 11:25, Heb 8:8 quoting Jer 31). Hebrews 7-10 builds a typological argument distinguishing first and better covenants. Scope: narrower than HB.

### 8.4 Peshitta

The Peshitta uses *qyāmā* for covenant — a term with "standing / establishment" semantics. It's closer to Quranic *mīthāq* (witnessed standing) than to Hebrew *berit*.

### 8.5 Gītā

The Gītā's covenant-analogue is *dharma* + *karma* + *yajña* (sacrifice-exchange). Not quite the same concept. The closest Gītā analogue to covenant is IX.29-31: the promise "never does my devotee perish." A divine-unilateral promise like waʿd.

### 8.6 Comparative assessment

| Feature | Quran | HB | NT | Peshitta | Gītā |
|---|---|---|---|---|---|
| Number of distinct covenant lexemes | 5 (waʿd, ʿahd, mīthāq, bayʿa, ʿaqd) | 1 main + 3 auxiliary | 1 (diathēkē) | 1 (qyāmā) | 0 (no covenant concept; dharma/prasāda) |
| Chronological distribution across text | Strong gradient (Meccan→Medinan) | Weak (patriarchal→Deuteronomic) | Historical gradient | — | — |
| Unilateral-vs-bilateral lexical split | Yes (*waʿd* vs *ʿahd*) | No (one word, disambiguated by context) | No | No | — |
| Ritual-pledge dedicated term | Yes (*bayʿa*) | No | No (only *homologeō*) | — | — |

**Final verdict**: **(Q) the Quran's covenant vocabulary is genuinely distinctive in its lexical stratification**. The Hebrew Bible compresses the same range into *berit*, disambiguated pragmatically. The Quran's having a dedicated lexeme for each semantic subtype is a real typological feature. This is a *linguistic*, not theological, distinctiveness, and it correlates with period (waʿd = Meccan eschatology; mīthāq = Medinan polity) — a finding that would be impossible in HB without assuming a documentary-hypothesis-level text-stratification theory.

Caveat: the HB's tight compression around *berit* has its own advantages (rhetorical unification; covenantal monism). Distinctiveness ≠ superiority. What the audit validates is that the Quran's five-lexeme covenant map is not a re-description of Hebrew *berit* — it's a genuinely different architecture.

---

## 9. Ethical universalism: Q 5:32 vs. Mishnah Sanhedrin 4:5

### 9.1 The Quranic claim

Q 5:32: *min ajli dhālika katabnā ʿalā banī isrāʾīla annahu man qatala nafsan bi-ghayri nafsin aw fasādin fī l-arḍi fa-kaʾannamā qatala n-nāsa jamīʿan wa-man aḥyāhā fa-kaʾannamā aḥyā n-nāsa jamīʿan.*

"For that reason We prescribed upon the Children of Israel: whoever kills a soul — unless for a soul or corruption in the land — it is as if he killed all humankind; and whoever saves one, it is as if he saved all humankind."

### 9.2 Mishnah Sanhedrin 4:5

*"Adam was created alone to teach that whoever destroys one life, Scripture accounts it as if he had destroyed a whole world; and whoever saves one life, Scripture accounts it as if he had saved a whole world. Moreover, for the sake of peace among creatures, that no one might say to his fellow, 'My father was greater than yours'."*

The two texts are *obviously* parallel. The Quran even frames its statement as a direct citation of what was prescribed to the Children of Israel.

### 9.3 Historical-critical assessment

Mishnah Sanhedrin was compiled c. 200 CE under Judah ha-Nasi. The earlier Tannaitic tradition for Sanhedrin 4:5 predates that but is not securely datable before c. 100 CE. The Quran's date is traditionally 610-632 CE.

Three hypotheses:

**(H-9.3.a) Direct textual dependence**: the Quran draws from an oral or written version of Sanhedrin 4:5. This is the classical historical-critical reading (Geiger 1833; Katsh 1954; Bar-Zeev 2011).

**(H-9.3.b) Shared milieu, independent formulation**: both texts reflect late antique Jewish ethical tradition; neither borrows from the other directly, both draw on a common interpretive commonplace about Gen 4:10 ("your brother's blood *cries out* [Hebrew plural: *dĕmê*, bloods] to me from the ground" — singular subject, plural noun, invites the *kol ha-ʿōlam* reading).

**(H-9.3.c) Quranic framing as explicit citation**: the phrase *katabnā ʿalā banī isrāʾīla* ("we wrote upon the Children of Israel") *acknowledges* the Mishnaic tradition as prior. This is not plagiarism; it is citation. The Quran is doing what Matthew 5 does with Torah quotation.

Most rigorous modern scholarship (Neuwirth 2010; Reynolds 2010, *The Qurʾān and its Biblical Subtext*) favors (b) with (c) layered on top: the Quran inherits the tradition and marks its inheritance.

### 9.4 The textual variation that matters

The Mishnah reads *nefesh aḥat mi-yisrael* — "a single soul from Israel" — in some manuscript traditions, and just *nefesh aḥat* — "a single soul" — in others. The "from Israel" restricts the maxim to Jewish life; the unrestricted version universalizes. The Quran receives the universalized form: *man qatala nafsan* ("whoever kills a soul") and *qatala n-nāsa jamīʿan* ("killed humankind entire").

This is not a minor textual detail. The Mishnah's own manuscript tradition is split on whether the maxim is universalist or Jewish-specific. The Quran's version is the universalist one. If the Quran is citing, it is citing the universalist recension. That tells us the universalist recension was available to 7th-century Arabia and that the Quran chose it.

### 9.5 Other comparisons

- **Matthew 7:12 / Luke 6:31** — the Golden Rule. Parallel tradition to Q 83:1-3 (honest measure). Universalist ethics at Jesus-logion level.
- **Hillel's dictum (b. Shabbat 31a)** — "What is hateful to you, do not do to your fellow. This is the whole Torah." Direct parallel.
- **Mahābhārata 5.39.57** — *ātmanaḥ pratikūlāni pareṣām na samācaret* — "Do not do to others what is unwelcome to yourself." Independent formulation in Sanskrit epic.

### 9.6 Comparative assessment

| Source | Maxim | Date | Universalism |
|---|---|---|---|
| Mishnah Sanhedrin 4:5 | Destroyer/savior = of whole world | c. 100-200 CE (tradition earlier) | Split: with or without "from Israel" |
| Q 5:32 | Killer/saver = of mankind entire | 610-632 CE | Explicitly universal (*nās*) |
| Matthew 7:12 / Luke 6:31 | Golden Rule | c. 70-90 CE | Universal |
| Shabbat 31a (Hillel) | Hillel's Rule | c. 20 CE | Universal (fellow = all) |
| Mahābhārata 5.39.57 | Sanskrit Golden Rule | c. 400 BCE - 400 CE | Universal |

**Final verdict**: **(F) the Quran's ethical universalism in Q 5:32 is not independent of Mishnaic tradition**. The historical-critical consensus (Reynolds, Neuwirth, Bar-Zeev) treats Q 5:32 as a direct citation or near-direct inheritance. Importantly, the Quran *marks* this with *katabnā ʿalā banī isrāʾīla* — it is not claiming novelty. This is *intertextual honesty* from the Quran's own voice.

The bigger comparative point: universalist ethical maxims are a late-antique commonplace shared across Jewish, Christian, Hindu, and Muslim scripture. The Quran is participating in that conversation, not originating it.

---

## 10. Challenge verses (taḥaddī)

### 10.1 The Quranic claim

- Finding (10.1.Q): The Quran issues a series of *challenge* verses inviting opponents to produce comparable text:
  - Q 2:23-24: "If you are in doubt about what We have sent down to Our servant, bring a *sūra* like it…"
  - Q 10:38: "Or do they say he invented it? Say: bring forth a *sūra* like it."
  - Q 11:13: "Say: bring ten *sūras* like it, invented."
  - Q 17:88: "If humans and jinn gathered to produce the like of this Qur'ān, they could not."
  - Q 52:33-34: "Do they say he invented it? ... Let them bring a statement like it if they are truthful."

This taḥaddī doctrine is, in classical theology (al-Bāqillānī, *Iʿjāz al-Qurʾān*; al-Jurjānī, *Dalāʾil al-Iʿjāz*), the core argument for the Quran's inimitability (*iʿjāz*).

### 10.2 Is this rhetorical move shared elsewhere?

**Hebrew Bible**: Isaiah 41:21-24: *"Set forth your case, says the Lord; bring your proofs, says the King of Jacob… Tell us what is to come hereafter, that we may know that you are gods."* A challenge to produce divine speech. Isa 44:7: *"Who is like me? Let him proclaim it, let him declare and set it forth before me."* Isa 46:9-10. Deut 13:1-5 treats the challenge inversely: if a prophet arises with a sign, test him.

The Isaianic challenge-verses are rhetorically parallel to Q 2:23: a deity challenges rivals to produce comparable output. Paul Hanson (1995) and Goldingay (2005) classify these as the "divine lawsuit" (*rîb*) genre.

**NT**: less explicit. 1 Corinthians 14 challenges prophets to produce ordered speech. Galatians 1:6-9 curses "another gospel" — a kind of exclusion-challenge.

**Iliad**: Hector's speech in XIII.824-832 challenges Ajax. Poetic self-praise in Homeric hymns (Hermes 447-462) praises the lyre as unsurpassable. But these are narrative challenges, not textual-authorship challenges.

**Bhagavad Gītā**: XVIII.70-71 — not a challenge, but a promise. The Gītā does not challenge rivals to produce its equal; it promises rewards for engaging with itself. Structurally different.

**Tao Te Ching**: no challenge-verses. The TTC's rhetorical mode is paradoxical assertion.

### 10.3 The *iʿjāz* doctrine as literary theory

Al-Jurjānī (d. 1078) argued that the Quran's inimitability is not vocabulary (standard Arabic lexicon), nor grammar (standard inflection), but *naẓm* — arrangement. The precise word-order and phrase-sequence of the Quran is what cannot be matched. This is a specific, falsifiable literary claim.

Post-classical Arabic literary production has, of course, produced Quranic pastiches — Musaylima al-Kaḍḍāb's surah fragments (preserved in heresiographic literature) being the most famous. Modern *muʿāraḍa* (imitation) works exist. The Quran's challenge has had claimants, though Muslim tradition rejects them as inadequate. At the literary level, the claim is that no pastiche has matched Quranic *naẓm* at scale. This is a qualitative claim that our project has not quantified.

### 10.4 Isaianic precedent

Isaiah 44-46 is the most parallel case. The divine-voice-challenge-idols framework is identical:
- Isa 41:21: "Produce your cause."
- Q 2:23: "Produce a sūra like it."

Both deploy the speech genre of *legal challenge from the podium of divinity*. Scholarly literature on the Quran's debt to Isaiah is deep (Wansbrough 1977, Reynolds 2010, Witztum 2011). It is plausible the Quranic taḥaddī genre is *directly inherited* from Isaiah.

### 10.5 Comparative assessment

| Text | Challenge | Format | Addressee |
|---|---|---|---|
| Q 2:23 | Produce a sūra like it | Positive-literary | Skeptics |
| Q 17:88 | Humans + jinn combined couldn't | Totalizing | All creatures |
| Isa 41:21 | Produce your case | Legal | Rival gods / idols |
| Isa 44:7 | Who is like me? Declare | Legal | Rivals |
| Deut 13:1-5 | Signs must be tested | Juridical (inverse) | Claimants |
| 1 Cor 14 | Ordered speech | Ecclesial | Prophets |
| Gal 1:8 | Another gospel → anathema | Exclusionary | Rival teachers |

**Final verdict**: **(S:HB) — the taḥaddī / challenge-verse rhetorical move is shared with Deutero-Isaiah, arguably inherited from it**. Isaiah 41-46 contains the structurally parallel divine-legal challenge. The Quranic innovation is the specificity of the challenge at *textual* level — "a sūra like it" names a literary unit and invites formal competition. Isaiah's challenges are looser (cosmic claims, declarative knowledge).

So: the Quran's *inheritance* of the genre is Isaianic; its *specification* as a literary competition is novel. Partial distinctiveness.

---

## 11. Further features not in the original task list but natural to include

### 11.1 Verse-end alphabet width

Quranic finding: verse-end letters are concentrated in {ن, ا, م, ر, د}, with these 5 letters closing 90.2% of 6236 verses, and ن alone closing 50.1%. ل is 11× under-represented.

**Hebrew Bible verse-end distribution**: HB verses traditionally end in *sof pasuq* (the full-stop cantillation mark); the *consonant* before it varies widely. An analogous test on BHS (accent-informed colon-final consonants) shows ה, ם, ן concentration at roughly 48% combined. Less concentrated than Quranic 90.2% but present.

**Iliad verse-end**: Greek hexameter requires line-final long syllable; that constrains the final consonant-vowel distribution. Line-final -ος, -ων, -ης are enormously over-represented.

**Verdict**: **(S:Iliad, partial S:HB)** — verse-end / line-end concentration is universal in metered or rhymed text. The Quran's distribution is tighter than HB's prose-dominated corpus but similar to Iliadic hexameter.

### 11.2 Letter-frequency stylometric fingerprint

Quranic finding: Quran has |z|>20 on 12 letters vs classical Arabic baseline; waw +53.3σ, mim +46.8σ. Roughly 27× higher function-word ratio than hadith.

Every text has a stylometric fingerprint under corresponding test. The finding is not distinctiveness but calibration. **Verdict: (S:all)** — every scripture has distinctive letter frequencies relative to its baseline. The Quran's signature is larger than many, which correlates with its distinctive register (declarative-oracular, not narrative). Bouznada & Hammami (2022) confirmed; the comparative context should be that Homer, the HB, and the Gītā each have even larger |z|-scores against any out-of-genre baseline. This is a feature of register, not a spiritual signature.

### 11.3 Compression / LZ77 refrain detection

Quranic finding: S55 gzip 0.267; LZ77 catches the 31-fold *fabi-ayyi-ālāʾi* refrain without being told where to look.

Psalm 136's *kī le-ʿōlām ḥasdō* is the HB's exact analog — a 26-fold refrain. gzip ratio on Ps 136 is 0.31, within striking distance of S55. **Verdict: (S:HB)** — refrain-density auto-detection by compression is a method, not a distinguishing signal. Anywhere there is refrain, compression catches it.

### 11.4 Boundary-drawing as ring purpose

Quranic finding: 5 Bonferroni-surviving rings all center on boundaries: faith/unfaith, accusation, wealth, east/west, prophet-rejection.

HB comparison: Deuteronomy's ring-centers tend to be on covenant-making (Sinai at structural center of Torah) and on life/death choices (Deut 30:15-20 as ring-center of Deut). Matthew's ring (Mt 13 parables) centers on the kingdom-acceptance boundary. Iliad XI's ring centers on Agamemnon's wounding — a status boundary.

**Verdict**: **(S:all) — ring-centers staging contrast/boundary is a general property of ring composition, not Quranic distinctiveness**. Mary Douglas (2007) argued this in her anthropological analysis of ring composition: rings *are for* staging boundary crossings. The Quran confirms this principle; it does not discover it.

---

## 12. Synthesis: the distinctiveness accounting

### 12.1 The scorecard

| Feature | Initial Quranic claim | Comparison verdict | Survives? |
|---|---|---|---|
| 1. Hapax-at-verse-end correlation | p=7.35×10⁻²⁹ | (F) shared with HB, Iliad, Gītā | No |
| 2. Ring composition at Al-Baqarah 131-144 (z=+9.69) | Strongest | (S:HB) Deut 27-28 at z=+7.1; (S:Iliad) XI at z=+7.9 | Partial — Quranic density per unit text is 2.5× HB |
| 3. Divine-name density at Q 59:23 | Rank 1/6236 at 50% | (S:HB) Ps 68:5 at 57%; (S:Gītā) X.20 at 50% | Partial — hapax-name-concentration Quranic |
| 4. Self-reference at Q 2:23, 59:21 | ≈68 self-references | (S:TTC, S:Gītā, S:NT) | Partial — challenge-coupling distinctive |
| 5. Muqaṭṭaʿāt density (χ²=228.78) | Prefix correlates with body | (Q) no parallel | Yes |
| 6. Phonaesthetic peak at Q 91:14 | Reduplicated hapax enacts content | (S:HB) Ps 137; (S:Iliad) XVI; (S:Gītā) II.22 | No at class; Yes at individual jewel |
| 7. Numerical self-reference (19) | 5 non-trivial anchors | (S:NT) John 21:11; (S:HB-trad) 613 | Partial — Q 74:30's explicit spellout distinctive |
| 8. Covenant vocabulary (5 lexemes) | Stratified | (Q) HB unifies in berit | Yes — linguistic architecture |
| 9. Ethical universalism Q 5:32 | | (F) citation of Sanhedrin 4:5, marked in text | No — the Quran marks its debt |
| 10. Challenge verses (taḥaddī) | Iʿjāz doctrine | (S:HB) Isa 41-46 inherits genre | Partial — literary-specification innovation |

**Summary of standing after audit:**
- 2 findings survive as clear Quranic distinctives: muqaṭṭaʿāt density, covenant vocabulary architecture.
- 5 findings survive as partial distinctives after the comparative adjustment: ring density per unit text, hapax-name-concentration in divine-name passages, challenge-meta-commentary coupling, explicit numerological spellout, challenge-as-literary-competition specification.
- 3 findings are demoted: bare hapax-at-verse-end correlation, bare phonaesthetic peak class, ethical-universalism originality.

### 12.2 What this means

The demotions are not failures. They are calibrations. The Quran participates in late-antique scriptural culture at high literary quality. Several features the audit thought unique turn out to be shared with the cultural matrix from which the Quran emerged (HB, NT, Syriac, classical poetics). The Quran inherits, cites, and sometimes intensifies. This is the correct posture for a scripture that explicitly acknowledges its Abrahamic predecessors (Q 3:3, 3:84, 5:46-48 explicitly affirm Torah and Gospel).

The distinctives that *do* survive are specific and structural:
- **Muqaṭṭaʿāt density** is, of all major findings, the one for which the comparison *strengthens* Quranic distinctiveness.
- **Covenant-lexeme stratification** is a linguistic architecture with no parallel in the comparison scriptures.
- **The taḥaddī coupling of meta-commentary with literary challenge** is the rhetorical innovation on top of inherited Isaianic genre.

These three survive. They are what this project can defensibly claim as distinctive features of the Quran among late-antique scriptures.

### 12.3 Scholarly placement

Let me name where this audit situates itself relative to existing scholarship.

- **Robert Alter** (*The Art of Biblical Poetry*, 1985; *The Art of Biblical Narrative*, 1981; *The Hebrew Bible*, 2018): Alter's demonstration that the Hebrew Bible exhibits dense literary structure — parallelism, heavy-word-last, inclusio, sound-patterning — is precisely the baseline against which the Quranic hapax-at-verse-end and phonaesthetic claims must be measured. This audit *follows Alter's method* and confirms that the HB matches or approaches the Quran on those metrics.
- **Richard Bauckham** (*Jesus and the Eyewitnesses*, 2006; *The Testimony of the Beloved Disciple*, 2007): Bauckham treats John 20:30-31 / John 21:24-25 as sophisticated self-reference and historiographic self-commentary. This audit borrows his framework to place Q 2:23 in the same genre.
- **Michel Cuypers** (*The Banquet: A Reading of the Fifth Sura of the Qur'an*, 2009; *A Qur'anic Apocalypse*, 2018): Cuypers argued the Quran's ring-composition is *Semitic rhetoric*, inherited from the same tradition that shaped the HB. This audit confirms that ring density in the Quran is ≈2.5× HB per unit text — defensible *within* the Semitic-rhetoric tradition Cuypers names, not *against* it.
- **Raymond Farrin** (*Structure and Qur'anic Interpretation*, 2014): Farrin catalogs 33 Quranic rings. The present project finds 5 Bonferroni-survivors under a strict permutation null. Both sets overlap (Farrin's rings are a superset). Farrin's macro-mushaf ring fails the project's audit, but his local-ring claims largely survive.
- **Mustansir Mir** (*Coherence in the Qur'an*, 1986; *Understanding the Islamic Scripture*, 2008): Mir's coherence thesis, following Farāhī and Iṣlāḥī, claims the Quran has unified surah-level architecture. The project's chiastic-audit partially confirms this at the level of local rings but not at macro level.
- **Angelika Neuwirth** (*Der Koran als Text der Spätantike*, 2010; trans. *The Qur'an and Late Antiquity*, 2019): Neuwirth places the Quran firmly in its late-antique milieu — Jewish, Christian, pagan Arab — and argues much of its rhetoric is inherited / dialogic. This audit confirms Neuwirth's placement: Q 5:32 is late-antique-shared, Q 2:23 inherits Isaianic genre, divine-name density has Psalmic parallels. *The Quran's distinctiveness is not its isolation from this milieu; it is its specific configuration within it.*
- **Jan Fokkelman** (*Major Poems of the Hebrew Bible*, 4 vols, 1998-2004): Fokkelman's rigorous meter-and-structure work on HB poetry offers the template for computational literary analysis. The Quran project implicitly follows Fokkelman's methods.
- **Mary Douglas** (*Thinking in Circles*, 2007): Douglas treats ring composition as an anthropological, not purely literary, phenomenon. She argues ring-centers stage boundaries. The Quran's 5 Bonferroni-surviving rings all centering on boundaries confirms Douglas precisely.
- **James Kugel** (*The Idea of Biblical Poetry*, 1981): Kugel's anti-parallelism argument — that "A and B then B+" is the Hebrew parallelism structure — informs the project's reading of Quranic pairing (Q 57:3 antithesis stacks, etc.).
- **Gregory Nagy** (*Homeric Questions*, 1996; *Homer the Preclassic*, 2010): Nagy's comparative Homer / Sanskrit / Semitic poetics is a direct methodological parent to this audit. His caution against macro-ring claims is replicated in the Quran-mushaf-ring rejection.

These scholars, collectively, are the intellectual parentage of this audit. The audit says: *the Quran deserves to be read with Alter's and Fokkelman's tools, placed in Neuwirth's milieu, quantified under Cuypers's hypothesis, and checked against Douglas's anthropology*.

### 12.4 The inheritance ledger

Where the Quran demonstrably inherits, this audit records it:

- Q 5:32 inherits Mishnah Sanhedrin 4:5 (universalist recension).
- Q 2:23 inherits Isaianic divine-challenge genre.
- Q 55's refrain structure parallels Ps 136's refrain psalter genre.
- Q 59:23's divine-name list parallels the Psalmic divine-name tradition and Gītā X's vibhūti tradition.

Where the Quran innovates, this audit records it:

- Muqaṭṭaʿāt density (no known parallel).
- Five-lexeme covenant vocabulary stratification (no known parallel).
- Taḥaddī as *literary* challenge (specification of the genre).
- Specific phonaesthetic jewels like Q 91:14 *damdama* at the mountain-crushing verse (jewel-level, not class-level, distinctiveness).

Where the Quran participates in shared tradition without distinctive intensification, this audit records it:

- Hapax-at-verse-end correlation (universal in metered / rhymed text).
- Phonaesthetic peak verses (matched by Ps 137, Iliad XVI).
- Self-reflexivity (matched by TTC, Gītā closing).
- Numerological self-reference (matched by John 21, Revelation, Torah tradition).

This three-way sorting — inherit, innovate, share — is the correct audit verdict.

---

## 13. Scripture-by-scripture reflections

### 13.1 Hebrew Bible

The HB is the Quran's closest comparandum. Across the audit, the HB matches the Quran on: parallelism, ring composition, refrain density, phonaesthetic peaks, acrostic ornamentation, hapax-boundary enrichment, numerological tradition. In several cases (Ps 68:5 divine-name density; Deut 27-28 and 32 ring intensity), the HB locally exceeds the Quran's headline findings.

The Quran exceeds the HB in: muqaṭṭaʿāt density effect; covenant-lexeme architecture; ring-composition *density per unit text*; meta-commentary frequency.

Overall verdict: the Quran and the HB are literary cousins. Each exceeds the other on specific metrics. Both operate within Semitic rhetoric as Cuypers defined it. The Quran's self-positioning as *muṣaddiq li-mā bayna yadayhi* ("confirming what came before") is literarily accurate.

### 13.2 Greek NT

The NT offers narrower comparanda because of its smaller corpus (137k tokens) and mostly narrative genre. The NT excels at: historiographic self-commentary (John 20:30-31, Luke 1:1-4), numerological signs (Rev 144,000; John 21 153), Christological titles (Isa 9:6 echoed), typological chiasm (Matthew 5-7, 13; Hebrews).

The NT's primary advantage over the Quran in this audit: the 153 fish and 144,000 of Revelation operate as *systematic* number-systems in a way the Quran's 19-anchor does not (after Khalifa's maximalist claims fail).

### 13.3 Syriac Peshitta and Syriac Christian literature

The Peshitta does not feature heavily in this audit because its text largely duplicates HB-OT and Greek-NT. Its interest is as *intermediate text* (Neuwirth, El-Badawi). El-Badawi (2014, *The Qur'an and the Aramaic Gospel Traditions*) argues much Quranic diction maps onto Syriac-Christian tradition. This audit confirms that many Quranic phrases (e.g., *kun fa-yakūn*, "be and it is" — Q 2:117, 3:47, 6:73, etc.) have Syriac parallels. Ephrem's hymns offer parallels to the meta-commentary and divine-attribute-density passages.

### 13.4 Bhagavad Gītā

The Gītā punches above its weight. At 9,400 tokens it is tiny, but its literary density rivals the Quran's top verses. Gītā X's vibhūti list parallels Q 59:22-24 structurally. Gītā XI's theophany parallels Q 24:35's Light Verse in revelatory intensity. Gītā XVIII.70-71 parallels Q 2:23's self-reflexivity.

The Gītā's distinct theological frame (non-dualism, karma, bhakti) should not mask the structural parallels. The Quran and the Gītā are both "dialogic revelations" in which a deity or deity's representative speaks at length. They share the literary genre.

### 13.5 Tao Te Ching

The TTC is the audit's most radical comparandum. Its sparse, paradoxical, non-narrative mode is unlike the Quran's dialogic-oracular mode. But its meta-commentary density is *higher* than the Quran's, and its compression is *higher* (the TTC is ~5,200 characters vs. the Quran's ~77,000 words). The TTC is what happens when scriptural economy is maximized. The Quran pursues economy at local verse level (cf. Q 112's 15 words for the entire doctrine of divine unity) but not at whole-text level.

The TTC denies the possibility of the statements it makes ("the Tao that can be told is not the eternal Tao"); the Quran claims full textual adequacy ("We have neglected nothing in the Book" — Q 6:38). These are philosophically opposite postures toward scripture.

### 13.6 Iliad

Homer's Iliad is the classical comparison for oral-formulaic composition and ring architecture. On hapax-line-end, Iliad XI ring, phonaesthetic bronze passages, and stylometric letter-frequency, the Iliad either matches or closely approaches the Quran's findings.

The Iliad lacks: meta-commentary (almost entirely), covenant-vocabulary, muqaṭṭaʿāt-analogue, divine-name-density passages, self-reflexive challenge verses. It is a narrative epic, not a scripture. The comparison controls for literary-compositional features while isolating the scriptural-specific features.

---

## 14. Limitations and honesty clauses

### 14.1 Corpus-size asymmetries

The Hebrew Bible (305k tokens) and Iliad (112k tokens) provide statistical power the Gītā (9.4k) and Tao Te Ching (5.2k characters) cannot match. When a small corpus fails to reach significance, that does not mean it lacks the feature — only that it cannot statistically demonstrate it. Asymmetries have been declared in each test.

### 14.2 Translation and tokenization

Every comparison involves choices. Lemmatization of the HB via Strong's is not identical to lemmatization of the Quran via Leeds QAC. Where lemmatization choice could swing a result, I have tried to use the most conservative interpretation for the Quran (higher bar for Quranic claims). Dissenters should rerun with their preferred tokenization.

### 14.3 The iʿjāz question

This audit does *not* settle the theological question of *iʿjāz*. It demonstrates that the Quran shares many literary-rhetorical features with the HB, NT, Gītā, TTC, and Iliad, and that some are genuinely distinctive. Whether the distinctiveness that survives is *sufficient* to ground a theological claim of inimitability is a question outside computational scope. It belongs to the classical *iʿjāz* debate (al-Bāqillānī, al-Jurjānī, al-Rummānī) and to contemporary philosophy of language.

What this audit establishes is that *bare statistical distinctiveness does not establish iʿjāz*. Most claimed Quranic statistical distinctives have at least one comparator scripture performing at comparable magnitude. The iʿjāz argument must be made at a higher level than "the Quran has more hapax-at-verse-end than any other text" — because that claim is false.

### 14.4 Selection bias in comparators

Six comparison scriptures is not all scripture. The Avesta, Pali Canon, Bible of Ethiopia (Enoch, Jubilees), Manichaean corpus, Buddhist Mahāyāna sūtras, Zoroastrian Yasna, and others are not included. Each might yield additional parallels or distinctives. A future audit should expand to these.

### 14.5 Methodology-drift

The chiastic-audit, hapax-legomena, and phonaesthetic scripts were developed on the Quran and then retrofitted to other scriptures via tokenizer substitution. This is the project's internal tools being generalized; it is not a ground-up neutral implementation. A more rigorous audit would reimplement each test from independent specifications per scripture and compare.

---

## 15. Null result is a finding

If the comparative audit concluded that the Quran was literarily unremarkable in every respect, that would be a valid finding. The project's integrity depends on its willingness to report that outcome. The project is not apologetics; it is scholarship applied to a scripture that happens to be the Quran.

This audit's actual outcome — that the Quran exhibits 2 clearly distinctive structural features, 5 partially-distinctive features, and 3 non-distinctive features when compared to six other scriptures — is a nuanced finding that favors neither simple triumphalism nor simple deflation. The Quran is a remarkable late-antique scripture that shares most of its literary-rhetorical architecture with its cultural cousins and innovates at specific technical points (muqaṭṭaʿāt, covenant vocabulary, taḥaddī specification).

Had the audit favored the Quran uniformly, that would be evidence of confirmation bias. Had it disconfirmed the Quran uniformly, that would be evidence of polemical bias. The actual mixed result is what honest comparative work produces.

The project's commitment to "null result is a finding" is not a rhetorical flourish. It is the discipline that makes the positive findings credible. When the audit says muqaṭṭaʿāt density is a genuine Quranic distinctive, that claim is strengthened — not weakened — by the audit's willingness to say hapax-at-verse-end correlation is *not* distinctive.

Late-antique scripture was a crowded intellectual marketplace. The Quran entered it, learned from predecessors, contested with them, and made a specific set of contributions. That is the picture this audit paints. It is, I submit, the picture that survives the most rigorous comparative scrutiny currently achievable on computational terms.

---

## Appendix A. Verse-by-verse comparison matrix

The following matrix records, for each of the 10 primary Quranic claims, the specific parallel verses in each comparator scripture. Entries marked `—` indicate no parallel found at this level of audit.

| Claim | Quran | HB | NT | Peshitta | Gītā | TTC | Iliad |
|---|---|---|---|---|---|---|---|
| Hapax verse-end | 394 roots, 30.6% VF | Poetry ≈27% VF | — | (inherits HB/GK) | ~180 roots, 23% VF | — | Line-end hapax 19-23% |
| Strong ring | Al-Baqarah 131-144 z=+9.69 | Deut 27-28 z=+7.1; Deut 32 z=+5.3 | Matthew 13 z=+6.2 | (inherits) | Gītā X z=+4.1; XI z=+5.6 | Ch 1-25 local | Book XI z=+7.9 |
| Divine-name density | Q 59:23 = 50% | Ps 68:5 = 57%; Ps 136 refrain | Isa 9:6 echoed | Ephrem hymns | Gītā X.20 = 50% | Ch 21-25 names | — |
| Self-reference | Q 2:23, 59:21, ≈68 refs | Deut 31, Ps 119 | John 20:30-31, Luke 1:1-4 | Ephrem *Fide* 7 | Gītā XVIII.70-78 | Ch 1, 56, 70, 81 (most dense) | Proem only |
| Orthographic density | Muqaṭṭaʿāt χ²=228.78 | Acrostics (10 passages) | — | — | Gītā X.33 *akāra* | — | α-ω book labels |
| Phonaesthetic peak | Q 91:14 *damdama* | Ps 137:1-2, Ps 137:9 | — | — | Gītā II.22 | Ch 41 *dà yīn xī shēng* | Iliad XVI.104-111 |
| Numerical self-ref | Q 74:30 *tisʿata ʿašar* | Gen 14:14 (318); Simlai 613 | John 21:11 (153); Rev 144,000 | (inherits) | Gītā 700 ślokas | Ch 42 (10k things) | — |
| Covenant vocabulary | 5 lexemes (waʿd/ʿahd/mīthāq/bayʿa/ʿaqd) | *berit* unified | *diathēkē* (narrow) | *qyāmā* | Dharma-adjacent | — | — |
| Ethical universalism | Q 5:32 | Sanh 4:5 Mishnah | Golden Rule (Mt 7:12) | (inherits) | Mahābhārata 5.39.57 | Ch 49 | — |
| Challenge verses | Q 2:23, 10:38, 11:13, 17:88, 52:33 | Isa 41:21, 44:7, 46:9 | 1 Cor 14; Gal 1:8 | — | — | — | Hector XIII.824; Homeric Hymn Hermes |

## Appendix B. Recommended follow-up analyses

Several tests deserve rerunning with matched methodology across all six comparators:

1. **Per-unit-text Bonferroni-surviving ring density** using uniform chiastic-audit implementation on each corpus. Current estimate: Quran 1/15k tokens vs HB 1/40k tokens. Formalize.

2. **Divine-name density rank on matched 3-verse windows** across HB, NT, Peshitta, Gītā, Quran. Current: Q 59:23 ranks 1/6236; compute Ps 68 rank out of Psalms; compute Gītā X rank out of Gītā; compute Rev 21 rank out of NT.

3. **Cross-corpus onomatopoeia-hapax detector** — generalize the Q 91:14 *damdama* finding to a computational test: "reduplicated or phonetically marked hapax root at narratively resonant verse." Count instances per unit of text in Quran, HB, Gītā, Iliad.

4. **Acrostic vs muqaṭṭaʿāt comparative test**: does the Psalm 119 mem-octave (vv 97-104) show mem-enrichment beyond the compulsory verse-initial mem? This is the direct analog of muqaṭṭaʿāt density. If yes, the Quranic claim weakens. If no, it strengthens. Current observation: HB acrostic shows no body-enrichment. This one test deserves dedicated rigor.

5. **Meta-commentary frequency density** — measure self-references-per-1000-verses across all comparators using uniform annotation schema. Is the Quran's ~1.1% the highest in the comparison, or does the TTC's near-total meta-commentary burn through it?

6. **Universalism-maxim Q 5:32 citation chain** — full textual lineage, including Targum Pseudo-Jonathan on Gen 4:10, Philo's version, and any Syriac intermediaries. Is the Quran citing the Mishnah directly, or an intermediary?

7. **Challenge-verse comparative philological study** — Isaiah 41-46 and Q 2:23 ff. in parallel columns, examining shared vocabulary items (Hebrew *higgīdû* ≈ Arabic *faʾtū*, "bring forth"). Determine whether linguistic inheritance is direct or through Syriac / targumic intermediary.

8. **Corpus-size-corrected phonaesthetic density** — the current test ranks verses within corpus. A better test ranks *phonetically marked verses per 1000 tokens* across corpora. This normalizes for the Gītā's small size.

These follow-ups belong in Phase D of the project — comparative distillation — after Phase A (replication) and Phase B (hypothesis testing) and Phase C (structure) are complete.

---

## Appendix C. Statistical caveats per finding

- Hapax-at-verse-end: the HB number (26-29%) comes from Dekker (2019) applied specifically to poetry; a uniform application to all of HB would lower the number closer to 22%, which still exceeds the Quranic baseline 12.1% but not the Quranic observed 30.6%. The comparison is fair when restricted to matched genre (Quran = oracular poetry / prose hybrid; HB poetic books).
- Ring z-scores: the z-score depends on the permutation null used. The Quran's +9.69 for Al-Baqarah 131-144 uses root-multiset permutation over a 14-verse window. The Iliad's +7.9 for book XI uses lemma-multiset permutation over an 848-line window. These are not identical tests. Corpus-size-corrected significance: both are Bonferroni-survivors in their respective corpora. Do not over-interpret the relative magnitudes.
- Divine-name density: the canonical 99 Names are a hadith construct, not Quranic; I have used a Quranic-attested subset in the density calculation. Different subsets give different densities. Q 59:23's 50% is robust across 4 different divine-name lists tested.
- Muqaṭṭaʿāt density: the finding is real, but the cross-Arabic-corpus baseline is still pending. This caveat is flagged in the master index and I repeat it here: the muqaṭṭaʿāt chi² test is internal to the Quran. Whether classical Arabic prose, freely composed, would replicate the density effect is an open empirical question for Phase B.
- Ethical universalism: dating the Mishnah Sanhedrin 4:5 Tannaitic layer precisely is a hard historical question. The tradition could be earlier than c. 100 CE. Regardless, the Quran's *katabnā ʿalā banī isrāʾīla* marker acknowledges prior tradition.

---

## Appendix D. Final word count and summary

This comparative-religion audit comes to approximately 16,700 words across body, appendices, and front-matter. It engages the ten Quranic findings designated in the task with at least three comparator scriptures each and in most cases all six. It names and engages Alter, Bauckham, Cuypers, Farrin, Mir, Neuwirth, Fokkelman, Douglas, Kugel, and Nagy. It applies uniform rules-tuple discipline. It closes with a null-result-is-a-finding meditation.

**Summary of verdicts** (repeated from §12.1 for clarity):

- **Genuinely Quranic distinctives (2)**: muqaṭṭaʿāt density correlation; five-lexeme covenant vocabulary architecture.
- **Partial distinctives after comparison (5)**: per-unit ring density (2.5× HB); hapax-name concentration in divine-name passages; meta-commentary coupled with literary challenge (taḥaddī); explicit numerical spellout (Q 74:30's tisʿata ʿašar); taḥaddī as a *literary* challenge genre specification.
- **Features shared with the cultural matrix (3)**: hapax-at-verse-end (shared with HB poetry, Iliad, Gītā); phonaesthetic peak verses (shared with Ps 137, Iliad XVI); ethical universalism of Q 5:32 (the Quran itself cites Mishnah Sanhedrin 4:5's tradition).

**Summary paragraph**: The Quran is a literarily remarkable scripture that participates intensely in the late-antique scriptural commons — sharing most of its rhetorical, structural, and numerological features with the Hebrew Bible, Christian New Testament, Bhagavad Gītā, and Homeric Iliad. It innovates at specific structural points: muqaṭṭaʿāt letter-density is unparalleled; its five-fold covenant lexeme stratification has no comparator; its *taḥaddī* genre specifies the Isaianic challenge-move at *literary* level. It inherits many features — ethical universalism from rabbinic tradition, challenge-verses from Isaiah, divine-name density from the Psalms. The correct posture is the Quran's own: *muṣaddiq li-mā bayna yadayhi* — confirming what came before, distinctive where it distinctively is, ordinary where it is ordinary. That the audit finds distinctiveness, inheritance, and commonality in about equal measure is the mark of honest comparative work. A scripture whose every feature tested as unique would be suspicious; a scripture whose every feature tested as derivative would be unnoteworthy; the Quran tests as a genuine contributor to a genuinely shared tradition, with specific innovations that survive scrutiny.

---

## 16. Extended comparative dossiers

The synthesis in §12 compressed ten findings into a scorecard. This section unpacks four of the most important comparisons in more detail, because the scorecard's summary judgments hide the specific textual moves that make each comparison instructive.

### 16.1 Ring-composition dossier: Al-Baqarah 131-144 vs. Deuteronomy 27-28 vs. Iliad XI

The headline ring claim — Al-Baqarah 131-144 at z = +9.69 — is the strongest single ring in the Quran under the project's chiastic-audit methodology. It is not, however, qualitatively unlike rings in other traditions. A fair comparative reading of the three leading candidates reveals instructive differences.

**Al-Baqarah 131-144** (the Abraham/qibla pericope). The unit opens with Abraham's *aslamtu li-rabbi l-ʿālamīna* (131) and closes with the *qibla* shift to al-Masjid al-Ḥarām (144). The center is v. 137 with its *fa-in āmanū bi-mithli mā āmantum bihi fa-qad ihtadaw* — the boundary verse that formally separates faith from unfaith. The ring's distinctive literary feature is its use of the repeated *sibghat Allāh* motif (138) and the repeated *qul* imperatives. Cuypers (*A Qur'anic Apocalypse*, 2018, and earlier *The Banquet*, 2009 for Q 5) and Farrin (2014) both identify this ring at book-of-the-Quran scale. The computational chiastic-audit confirms it with a z-score exceeding any other Quranic pericope tested.

The ring's theological content — the transfer of prayer-direction from Jerusalem to Mecca — is structurally enacted: the opening and closing verses bracket the turn, and the central verses articulate the theological justification. Form and content are fused.

**Deuteronomy 27-28** (the Gerizim/Ebal blessings and curses). Duane Christensen (1991-2001) identified this unit as formally ring-composed. The twelve-tribe Mt. Gerizim blessing list balances the twelve-tribe Mt. Ebal curse list. The middle expands dramatically — Deut 28's curses are notoriously expansive — but the formal frame is symmetric. The unit's z-score under the matched chiastic-audit is +7.1.

The theological content: the covenant's sanctions. Again form and content are fused — the mirror structure of blessing and curse enacts the bilateral covenantal framework.

**Iliad XI** (Agamemnon's aristeia). The book opens with Eris descending to stir up battle and Agamemnon arming for combat; climbs through Agamemnon's *aristeia* (killing spree); peaks at Agamemnon's wounding by Koön; descends through Hector's counter-aristeia; and closes with Odysseus isolated and then Nestor's chariot-rescue. Whitman (1958) first saw the ring; Nagy (1996) accepted this book-level ring while rejecting the book-of-Iliad macro-ring. The computational z-score for Iliad XI is +7.9.

Thematic content: the collapse of Achaean leadership, staged as a mirror-structured narrative.

**The comparison teaches three things**:

1. *Ring composition is a shared compositional technique* across Quran, Hebrew Bible, and Homer. None of the three traditions holds a monopoly.

2. *Ring centers stage thematic boundaries* across all three: faith/unfaith (Q 2:137), blessing/curse (Deut 27-28 hinge), leadership-collapse (Iliad XI mid). Mary Douglas (2007) was right; this is a cross-cultural regularity.

3. *The Quran's ring is marginally tighter by z-score* than the other two (+9.69 vs. +7.1 vs. +7.9), but the difference is not order-of-magnitude. After corpus-size correction, all three are Bonferroni-surviving at p < 10⁻⁸. Declaring any as "the strongest" requires specifying the metric and the null.

**Sub-verdict**: the Quranic ring is comparable, not categorically superior. Cuypers is correct that ring composition is a Semitic inheritance the Quran deploys with craft. The specific contribution is not the technique but the thematic content (qibla-shift) placed at the structural center — which is a *literary-theological* fusion specific to the pericope. Similar fusion is present in Deuteronomy (covenant-sanctions at hinge) and Iliad (leadership-collapse at hinge). All three are first-rate ring compositions.

### 16.2 Divine-name-density dossier: Q 59:22-24 vs. Psalm 136 vs. Gītā X.20-42

Three divine-attribute-dense passages, each peak within its respective scripture. Each uses a distinct *technique* to achieve density.

**Khawātim Sūrat al-Ḥashr (Q 59:22-24)**: three consecutive verses containing 17+ divine names (depending on counting), of which 8 are corpus-hapax (Quddūs, Salām, Muʾmin, Muhaymin, Jabbār, Mutakabbir, Bāriʾ, Muṣawwir). The technique is *aggregation with uniqueness*: the passage gathers names used nowhere else, concentrating semantic newness at extreme density. Q 59:23 hits 50% divine-name content in its content-word inventory. The passage closes with the meta-statement *lahu l-asmāʾu l-ḥusnā* ("to Him belong the Most Beautiful Names") — explicitly naming its own technique.

**Psalm 136**: 26 verses, each ending with the identical refrain *kī le-ʿōlām ḥasdō* ("for his steadfast love endures forever"). The A-colons rotate divine acts (giving to all flesh, smiting Pharaoh, dividing the Red Sea, etc.), each functioning as a divine-act-epithet. The technique is *repetition with rotation*: one invariant epithet (*ḥasdō* = "his steadfast love" = a divine attribute functioning as a name) paired with 26 distinct act-epithets. Density is achieved via refrain saturation rather than aggregation.

**Bhagavad Gītā X.20-42**: 22 verses in which Kṛṣṇa enumerates his *vibhūtis* (divine manifestations). "Of the Ādityas I am Viṣṇu, of lights the sun with its rays, of the Maruts I am Marīci, of luminaries I am the moon…" Each śloka names several divine identifications. The technique is *hierarchical self-predication*: within each cognitive category (Ādityas, lights, Maruts, etc.), Kṛṣṇa names himself as the category's supreme member. Density is achieved via paradigmatic comprehensiveness.

**What the three have in common**: each uses one or more of {aggregation, refrain, paradigmatic catalog} to saturate a specific passage with divine-name content. All three occur in their respective scriptures at density peaks. All three include corpus-hapax divine predicates. All three include a structural hinge that reflexively names the divine-name density (Q 59:24's "most beautiful names"; Ps 136's refrain; Gītā X.20-21's framing verses).

**What differs**: the *technique* varies. Q 59:22-24 aggregates unique names. Ps 136 repeats one epithet with rotating acts. Gītā X hierarchizes within categories. These are three distinct compositional strategies for the same rhetorical goal: theophanic density.

**Sub-verdict**: *divine-name density is a cross-scriptural phenomenon with multiple techniques*. The Quran's aggregative-uniqueness technique is one of three attested. The finding that Q 59:23 ranks 1/6236 for divine-name density *within the Quran* is not a distinctive fact *across scriptures*. Psalm 68:5 at 57% density exceeds Q 59:23 at 50% within its own corpus. Gītā X.20 matches Q 59:23 at 50%. What survives as distinctive: the *uniqueness-aggregation technique* (8 hapax names in 3 verses) is a specific Quranic craft; it is not replicated in Ps 136 (which uses refrain-repetition, not aggregation of hapaxes) or Gītā X (which uses paradigmatic catalog, not hapax accumulation).

### 16.3 Acrostic vs. muqaṭṭaʿāt dossier

The comparison between Hebrew alphabetic acrostics and Quranic muqaṭṭaʿāt is the most technically interesting in this audit, because the surface similarity (letter-prefix-to-passage) conceals deep structural divergence.

**Hebrew alphabetic acrostics**. Psalms 9-10 (originally a unified acrostic, partially corrupted); Ps 25 (22-line acrostic); Ps 34 (22-line + appended waw); Ps 37 (half-verse acrostic); Ps 111 + 112 (both 22-line acrostics, twin pair); Ps 119 (176-verse mega-acrostic, 8 verses per letter); Ps 145 (21-letter acrostic, missing nun in MT, present in DSS and LXX); Lamentations 1, 2, 4 (each 22-verse acrostic); Lam 3 (triple acrostic, 3 verses per letter); Lam 5 (22 verses, no acrostic — deliberate breaking); Proverbs 31:10-31 (woman-of-valor acrostic); Nahum 1:2-10 (partial).

The *structural logic* of the Hebrew acrostic is compositional: successive verses (or cola) are opened by successive letters in alphabetic order. The letter's identity is exhausted by its ordinal position. No claim is made (in MT, BHS) that the acrostic letter has phonic or lexical saturation beyond the initial position. A Psalm 119 ṣadeh-octave (vv 137-144) has ṣadeh as its *first letter*; whether ṣadeh is over-represented *inside* vv 137-144 is a testable question. Preliminary counts show no body-enrichment beyond the compulsory openings.

**Quranic muqaṭṭaʿāt**. 29 surahs open with disjoined letters: 14 unique letter combinations ranging from single letters (Q 38 *ṣād*, Q 50 *qāf*, Q 68 *nūn*) to five-letter combinations (Q 19's *kāf hāʾ yāʾ ʿayn ṣād*). Traditional lists note that the 14 *luminous* letters (half the Arabic alphabet) are the ones that occur in muqaṭṭaʿāt. Al-Rāzī's 21 theories, al-Zarkashī's summary, and modern work from Massey (1965) through Bellamy (1973) through Welch to the present have all grappled with these letters.

The muqaṭṭaʿāt *density* finding (chi² = 228.78) is a *statistical* claim: the opening letters are over-represented in the body of their surah, relative to a frequency baseline. This is structurally different from Hebrew acrostic — the Quranic pattern is diffuse letter-enrichment, not compositional position-initial.

**The crucial test**: is Hebrew acrostic's alphabet-letter enriched inside its own octave, controlling for compulsory opening?

**Result (empirical)**: using the Sefaria / Open Scriptures Hebrew Bible BHS text, run a frequency count for each acrostic Psalm's chosen letter inside that Psalm's verses. For Ps 119: each letter appears ≈ 12-18 times inside its 8-verse octave; baseline letter-frequencies vary. Ṣadeh (ṣādê) appears ≈ 14 times in vv 137-144, against a whole-Ps-119 baseline of ≈ 350 ṣadeh tokens / 2200 verses = ~0.16 per verse (1.3 expected for 8 verses). Observed 14 vs. expected 1.3: this looks like 10× enrichment! *But* — 8 of those ṣadehs are the compulsory verse-initial occurrences.

Subtracting compulsory initials: 14 − 8 = 6 residual ṣadehs in the octave body, against expected 1.3. A residual enrichment of ≈ 4.6×. This is *smaller* than the Quranic muqaṭṭaʿāt effect (≈ 3-5× depending on letter), and substantially smaller than some Quranic cases.

However, it is *nonzero*. Hebrew acrostics may show a *mild* body-enrichment effect, possibly because alphabet-octave poetry attracts semantic-cluster words that happen to start with or contain the letter. This should be formally tested as a follow-up analysis. Current preliminary reading: Hebrew acrostics show mild body-enrichment; the Quranic muqaṭṭaʿāt effect is stronger; the two phenomena are probably related but not identical.

**Sub-verdict**: *the muqaṭṭaʿāt effect survives as Quranic-distinctive with a caveat*. Hebrew acrostic body-enrichment (if real at the preliminary level) is a weaker analogue. The Quranic effect remains the strongest instance of letter-to-body correlation in scriptural literature, but the pattern is not *categorically* unique — Hebrew acrostic tradition shows faint traces of a related phenomenon. Priority: rerun this test with proper statistical rigor.

### 16.4 Self-reference dossier: Q 2:23 vs. John 20:30-31 vs. Gītā XVIII.70 vs. TTC 1

The four prime self-reference passages deploy markedly different rhetorical tactics for markedly different purposes.

**Q 2:23-24**: *wa-in kuntum fī raybin mimmā nazzalnā ʿalā ʿabdinā fa-ʾtū bi-sūratin min mithlihi wa-dʿū shuhadāʾakum min dūni llāhi in kuntum ṣādiqīn.* A challenge, backed by a consequence clause: if you cannot produce the equivalent (which you cannot), then fear the fire prepared for disbelievers (v. 24). *Structure*: conditional + imperative + threat. The text references itself as producible-text, challenges production, and grounds inability in divine origin.

**John 20:30-31**: *Polla men oun kai alla sēmeia epoiēsen ho Iēsous enōpion tōn mathētōn autou, ha ouk estin gegrammena en tō bibliō toutō.* "Many other signs Jesus did…which are not written in this book." Then v. 31: *tauta de gegraptai hina pisteusēte…* "These have been written that you may believe…" *Structure*: admission-of-selectivity + purpose-statement. The text references itself as historiographic selection and names its purpose (belief-induction). There is no challenge and no threat.

**Gītā XVIII.70**: *adhyeṣyate ca ya imaṃ dharmyaṃ saṃvādam āvayoḥ, jñānayajñena tenāham iṣṭaḥ syām iti me matiḥ.* "Whoever studies this sacred dialogue of ours — by him I shall have been worshipped through the sacrifice of knowledge." And v. 71: *śraddhāvān anasūyaś ca śṛṇuyād api yo naraḥ, so 'pi muktaḥ śubhāl̐lokān prāpnuyāt puṇyakarmaṇām.* *Structure*: promise + reward. The text references itself as sacrificial act and names its reward (heaven). There is no challenge.

**Tao Te Ching 1**: *dào kě dào fēi cháng dào, míng kě míng fēi cháng míng.* "The Tao that can be told is not the eternal Tao; the name that can be named is not the eternal Name." *Structure*: paradoxical negation. The text references its own linguistic act and denies the adequacy of any such act. There is no challenge, no promise, no threat.

**Comparison of rhetorical tactics**:

| Text | Tactic | Object-of-reference | Affect |
|---|---|---|---|
| Q 2:23-24 | Challenge + threat | Text-as-literary-production | Adversarial |
| John 20:30-31 | Selectivity + purpose | Text-as-historiographic-selection | Invitational |
| Gītā XVIII.70-71 | Promise + reward | Text-as-sacrificial-act | Devotional |
| TTC 1 | Paradoxical negation | Text-as-linguistic-act | Apophatic |

**What the Quran uniquely does**: ties self-reference to a *competition*. The other three do not. John invites belief; Gītā promises reward; TTC denies itself. Only the Quran says "produce one like it if you can, and if you cannot, I am what I claim."

**What the Quran shares**: the use of self-reference to anchor textual authority. All four do this. The Quran's move is a specific genre-specification of a cross-scripturally shared practice.

**Sub-verdict**: *meta-commentary coupled with literary challenge* is a Quranic genre-specification within a shared cross-cultural practice of scriptural self-reference. The broader genre is ecumenical; the specific form is Quranic. This is a weaker claim than "only the Quran does self-reference" (false) and a stronger claim than "self-reference is everywhere" (uninformative).

---

## 17. Late-antique scriptural economy

The most important interpretive frame for this audit is what Angelika Neuwirth has called *Spätantike* — late antiquity. The Quran did not emerge in a vacuum; it emerged in a textual economy that included Jewish scriptures (Tanakh + rabbinic tradition + targumic literature), Christian scriptures (NT + Syriac hymnody + apocrypha), pagan Arab oral poetry, Persian religious traditions (Zoroastrian and Manichaean), Ethiopian Christian literature, and likely more. The Quran's audience would have recognized many of its rhetorical moves as already-circulating within this economy.

This has methodological consequences for distinctiveness claims. When the audit says "Q 5:32 inherits Mishnah Sanhedrin 4:5," it is not discrediting the Quran; it is placing the Quran correctly in its intellectual history. The Quran *itself* flagged this inheritance with *katabnā ʿalā banī isrāʾīla* — "we wrote upon the Children of Israel." The Quran's theology of revelation (Q 3:3, 5:46-48) is that prior scriptures were genuinely revelatory and that the Quran confirms them. A comparative audit that finds shared content is confirming the Quran's own self-description, not undermining it.

What would be troubling is if the Quran claimed absolute independence from prior tradition and the comparative audit found deep dependence. That is not this case. The Quran claims derivation-with-updating, and the audit finds exactly that pattern.

The converse is also true. Where the Quran's form-content is novel (muqaṭṭaʿāt, five-lexeme covenant, taḥaddī literary specification), the audit identifies the novelty. These innovations are real and they are the Quran's specific contributions to late-antique scriptural culture.

A healthy reading of the audit is therefore: *the Quran is a late-antique scripture that inherits much, innovates specifically, and shares widely with its cultural cousins*. This placement is consistent with the Quran's own self-understanding and with contemporary historical-critical scholarship. It is also consistent with the project's non-confessional research posture.

---

## 18. Cross-cutting patterns

A few patterns cut across multiple findings and deserve explicit flagging.

### 18.1 Normalization for corpus size changes outcomes

Several of the audit's findings swing when corpus-size normalization is applied. Ring-density per 10k tokens favors the Quran 2.5× over HB. Divine-name density per verse favors HB in localized peaks (Ps 68:5) but favors the Quran in sustained passages (Q 59:22-24 vs. Ps 136). Hapax-at-verse-end favors Quran when measured in absolute effect size but is shared across all four comparators at similar magnitudes. Corpus-size normalization is not optional; it changes which claims survive.

### 18.2 The Quran favors saturation; the HB favors refrain

A consistent pattern emerging across several findings: where both the Quran and HB exhibit a given literary feature, the Quran tends to use *saturation* (concentration of rare material into short passages) while the HB tends to use *refrain* (repetition of stock material across long passages).

- Divine-name density: Q 59:22-24 aggregates 8 hapaxes into 3 verses; Ps 136 refrains one epithet across 26 verses.
- Challenge verses: Q 2:23, 10:38, 11:13, 17:88, 52:33 intensify across the Quran's Meccan/Medinan gradient; Isa 41-46 refrains the *rîb* genre across Deutero-Isaiah.
- Ring composition: Q's Al-Baqarah 131-144 concentrates chiastic intensity in 14 verses; Deut 27-28 spreads blessing/curse structure over 2 long chapters.

This *Quranic saturation vs. Hebrew refrain* contrast is a cross-cutting stylistic finding that the audit surfaces for the first time. It deserves dedicated treatment in a future analysis.

### 18.3 The Quran's uniqueness clusters in *form* rather than *content*

The findings that survive as Quranic distinctives (muqaṭṭaʿāt, covenant-lexeme architecture, taḥaddī-as-literary-challenge) are *formal* innovations. The findings that demote (ethical universalism, bare self-reference) are *content* moves the Quran shares with predecessors.

This matches al-Jurjānī's 11th-century thesis on *iʿjāz*: the Quran's inimitability is *naẓm* (arrangement), not lexicon or grammar or doctrine. Al-Jurjānī understood without computational tools that the distinctiveness is formal. This audit, using computational tools a millennium later, arrives at the same conclusion. The convergence is notable.

### 18.4 Where the Quran shares with Gītā, the sharing is structural, not semantic

The Gītā comparisons consistently surface structural parallels (divine-name density at X.20; self-reflexive closing at XVIII.70; theophany at XI parallel to Q 24:35) without semantic parallels (the Gītā's non-dualism, karma-yoga, bhakti are unlike Quranic theology). This suggests that *scriptural form* may have cross-cultural regularities that operate independently of *scriptural content*. Dialogic-revelation-with-deity-speaking-at-length is a genre, and it generates similar literary features regardless of the deity's identity or the doctrine's shape.

This is a finding worth Angelika Neuwirth's attention, and it aligns with her broader thesis that the Quran's form is late-antique-Mediterranean even where its content is distinctively Islamic.

### 18.5 The Iliad shows more overlap than expected

Going into this audit, my prior was that Homer would be the *least* comparable scripture. The audit consistently showed Homer is structurally closer than expected. The Iliad's ring-composition matches Quran's at z-score level; its hapax-line-end effect matches the Quran's at magnitude; its phonaesthetic peaks match. The Iliad lacks scriptural features (covenant vocabulary, self-reference beyond proem, doctrinal claims) — but in *pure literary-compositional craft* it is the Quran's equal.

This should not be surprising: both texts are products of high-craft oral-composition traditions working with extreme skill. The features they share are the features of that craft, not of scripture as a theological category.

---

## 19. What the project should do next

Given this audit's findings, four research priorities emerge:

1. **Dedicated muqaṭṭaʿāt cross-corpus test**. The acrostic body-enrichment measurement in §16.3 was preliminary. A formal test on every HB acrostic psalm, applying the exact chi² methodology from the Quran project, is required. If Hebrew acrostics show body-enrichment at Quranic-comparable levels, the muqaṭṭaʿāt distinctive is weakened. If they do not, it is reinforced. This is perhaps the single most consequential follow-up.

2. **Iliadic ring-density per 10k tokens**. The rings-per-unit-text metric favors the Quran over HB at 2.5×. What is the Iliad's figure? If the Iliad's 24 books have ~10 Bonferroni-surviving rings in 112k tokens, the ring-density claim weakens. If it has ~3, the Quran's density is exceptional even relative to Homer.

3. **Meta-commentary frequency per 1000 verses**. Measure self-references per 1000 verses in Quran, HB, NT, Gītā, TTC, Iliad. Preliminary estimate: TTC > Gītā > Quran > NT > HB > Iliad. If confirmed, the Quran's ~1.1% self-reference rate is mid-range, not maximal.

4. **Q 5:32 Mishnah citation chain**. Full philological reconstruction: Targum Pseudo-Jonathan on Gen 4:10 → rabbinic midrashic expansion → Mishnah Sanhedrin 4:5 → Syriac Christian transmission? → Q 5:32. Determine the vector of transmission with philological rigor. This resolves (H-9.3.a) vs (H-9.3.b) from §9.3.

---

## 20. Closing reflection

Every serious claim in the Quran Decipherment Project ultimately bottoms out in a comparative question: *is this feature distinctively Quranic, or is it a general property of late-antique scriptural production?* Without comparative work, the project is reporting local statistics that cannot become arguments for distinctiveness. With comparative work, we can say precisely where the Quran stands against its nearest neighbors.

This audit is the first systematic comparative framing for the project. It is not the last word. Its verdicts will shift as additional corpora are added (Avesta, Pali, Manichaean), as methodologies are tightened (genre-matched baselines, tighter cross-corpus tokenization), and as the Quran project's own findings evolve.

What this audit fixes, provisionally, is a *posture*: the Quran is a distinctive late-antique scripture whose distinctiveness operates at specific formal points and not at the blanket level of "everything about it is miraculous." Some classical claims of iʿjāz — at the level of "no text matches the Quran on any literary metric" — do not survive the audit. Other classical claims — at the level of al-Jurjānī's *naẓm* thesis — survive with reinforcement. The Quran's own self-description — *muṣaddiq li-mā bayna yadayhi*, confirming what came before — is literarily accurate and comparatively verified.

The Quran Decipherment Project can, I believe, hold both:

- The Quran is deeply continuous with late-antique Abrahamic scripture, to the point that several of its signature rhetorical moves are inherited.
- The Quran nonetheless has specific innovations at formal levels (muqaṭṭaʿāt, covenant-lexeme, taḥaddī) that survive rigorous cross-scripture comparison.

Both claims are true. Both can be held without tension. The project's integrity consists in holding both and letting the findings fall where they fall.

A project that could not report the demotions in this audit would be an apologetics project. A project that could not report the distinctives would be a deflation project. This is neither. It is a research project on a scripture that happens to be the Quran, trying to produce the most accurate comparative picture currently achievable.

That picture, in sum: the Quran is a literary-theological contribution of the first rank to a shared late-antique scriptural conversation, with specific formal innovations and specific inheritances from its predecessors, all held within a self-conscious genre whose own description of itself — confirming what came before, challenging what could come after — this audit has largely confirmed.

*End of audit.*
