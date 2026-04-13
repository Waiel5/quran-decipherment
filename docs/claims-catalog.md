# Quranic Numerology & Structure — Claims Catalog

**Run 1 — 2026-04-12**

This file catalogs every published claim about Quranic numerology, word-counting symmetry, letter statistics, and structural (chiastic / ring) composition that the research team is aware of. Claims are reproduced *faithfully* with their original numbers — inclusion here is **not** endorsement. Many of these claims are methodologically broken, unfalsifiable, or have been empirically refuted; we still record them so that downstream tooling can test them against the `docs/methodology.md` rule tuples.

Format: YAML blocks, one per claim. Downstream parsers can load this file with any YAML multi-document reader (split on `---`). Fields are:

- `claim_id` — short slug
- `claim_statement` — precise, with the actual numbers
- `claimant` — proposer, date, source if known
- `counting_rules` — orthography / word / letter / basmala policy; use `not-disclosed-by-source` where the original does not say
- `supporting_evidence` — what numbers or examples the source provides
- `known_criticisms` — who refuted it and how
- `confidence_in_replicability` — high / medium / low
- `notes` — free-form

Add new claims by appending new `---`/YAML blocks. Do **not** reorder existing IDs; downstream files reference them.

---

## Family A — Rashad Khalifa / Code-19 / Submission.org

```yaml
claim_id: khalifa-bismillah-19-letters
claim_statement: "The opening basmala (bismi-llahi r-rahmani r-rahim) consists of exactly 19 Arabic letters, establishing 19 as the Quran's mathematical key."
claimant: "Rashad Khalifa, 1974 (initial announcement); formalised in 'Quran: Visual Presentation of the Miracle' (1982) and Appendix 1 of 'Quran: The Final Testament' (1989+). Hosted on submission.org and masjidtucson.org."
counting_rules:
  orthography: "Uthmani rasm (Khalifa counts the consonantal skeleton; does not use modern spelling for long vowels)"
  word_definition: "not-applicable"
  letter_definition: "graphemes, with several hamza/alif decisions that affect totals; Khalifa's choice is not fully disclosed but implicitly: ب س م ا ل ل ه ا ل ر ح م ن ا ل ر ح ي م = 19"
  basmala_policy: "counted-only-in-surah-1 (basmala is a separator for the other 112 instances, only numbered as verse 1 in Al-Fatiha)"
supporting_evidence: "Claim is used as the seed: 19 letters in basmala; 4 words in basmala each occur a 19-multiple number of times (see khalifa-basmala-word-counts)."
known_criticisms: "Bilal Philips (1987, 'The Qur'an's Numerical Miracle: Hoax and Heresy') counts the letters differently depending on whether long vowels written as alif/ya/waw are counted; multiple alternative counts from 18 to 22 are obtainable. Brendan McKay-style critique (not Quran-specific but applied by analogy): any short phrase in Arabic has a small number of letters and divisibility by 19 is one-in-nineteen by chance."
confidence_in_replicability: "high (the letter count of the basmala under a fixed orthography is easy to reproduce; the *interpretation* that 19 is the key is unfalsifiable)"
notes: "Anchor for entire Code-19 family. Test under every letter_definition variant in methodology.md §3."
```

---

```yaml
claim_id: khalifa-basmala-word-counts
claim_statement: "Each of the four words of the basmala occurs a multiple of 19 times in the Quran: Ism (name) 19x, Allah 2698 (19x142), al-Rahman 57 (19x3), al-Rahim 114 (19x6)."
claimant: "Rashad Khalifa, Appendix 1, Quran: The Final Testament; Edip Yüksel, 'Nineteen: God's Signature in Nature and Scripture' (2011)."
counting_rules:
  orthography: "not-disclosed-by-source (implicitly Uthmani)"
  word_definition: "orthographic-token of the specific lemma, but: counts include inflected forms (Khalifa does not clarify which); basmala instances included"
  letter_definition: "not-applicable"
  basmala_policy: "each of the 113 opening basmalas is counted as four word-tokens; this is essential for the Allah=2698 and Rahim=114 results"
supporting_evidence: "Appendix 1 tabulates the four counts; 19 * (1, 142, 3, 6) = (19, 2698, 57, 114); the sum of the multipliers 1+142+3+6 = 152 = 19x8."
known_criticisms: "If the two last verses of Surah 9 (9:128-129) are counted as genuine (which they are in every manuscript), Allah becomes 2699 and al-Rahim 115, neither divisible by 19. Khalifa's response was to declare 9:128-129 interpolations, which Sunni critics (Philips, Ahmad Deedat after his reversal) regard as textual fabrication. Count of 'ism' (19) arbitrarily excludes other occurrences of the root s-m-w."
confidence_in_replicability: "medium (reproducible if one accepts Khalifa's 9:128-129 deletion and counting policy; fails otherwise)"
notes: "This is THE load-bearing claim of the entire Code-19 edifice. Replicate under every basmala policy in methodology.md §4."
```

---

```yaml
claim_id: khalifa-quran-74-30-reference
claim_statement: "Quran 74:30 ('Over it is nineteen') is a self-referential indicator of the 19-based mathematical miracle, confirmed by 74:31 ('a lesson for humans'). Chapter 74 is 'Al-Muddaththir', called 'The Hidden' — God hiding the code until modernity."
claimant: "Rashad Khalifa, Masjid Tucson, 1974+"
counting_rules:
  orthography: "not-applicable (exegetical claim, not a counting claim)"
  word_definition: "not-applicable"
  letter_definition: "not-applicable"
  basmala_policy: "not-applicable"
supporting_evidence: "74:30-31 Arabic text; classical tafsirs (Tabari, Ibn Kathir) read the verse as about 19 angels guarding hell — Khalifa reinterprets as 19-the-number."
known_criticisms: "Traditional tafsir (Yusuf Ali, Tabari, Ibn Kathir): 19 refers to angels. Khalifa's shift from 'nineteen angels' to 'nineteen as divine signature' is exegetically novel and textually unsupported."
confidence_in_replicability: "not-applicable (interpretive claim, not empirical)"
notes: "Included because Khalifa's entire methodology treats this verse as proof-of-intent."
```

---

```yaml
claim_id: khalifa-initial-letters-multiples-of-19
claim_statement: "In each of the 29 surahs that begin with muqatta'at (disjointed letters), the initial letters occur within that surah in multiples of 19. E.g. Surah 50 (Qaf): letter ق appears 57 times (19x3); Surah 68 (Nun): letter ن appears 133 times (19x7); Surah 42 (Ha-Mim-'Ayn-Sin-Qaf): combined initial letters multiple of 19; etc."
claimant: "Rashad Khalifa, Appendix 1; elaborated in 'Quran: Visual Presentation of the Miracle' (1982)."
counting_rules:
  orthography: "Uthmani, BUT Khalifa required a non-standard spelling of the initial nun in Surah 68 ('nun-waw-nun' or similar) to reach 133"
  word_definition: "not-applicable"
  letter_definition: "graphemes, with-tanwin-as-nun for Surah 68; alif counted as-is"
  basmala_policy: "counted-only-in-surah-1 (basmalas of initial-letter surahs are not counted toward the surah's letter totals)"
supporting_evidence: "Tables in Appendix 1 listing each initial-letter surah and the count of each initial letter within it, each divisible by 19."
known_criticisms: "Bilal Philips (1987) and later Sunni critics demonstrated that Khalifa's counts use non-attested spellings (the 'nun-waw-nun' spelling of 68:1 is in no manuscript). For Surah 42 Khalifa gives multiple overlapping counts; Edip Yüksel (after departing Submitters) acknowledged several arithmetic errors. The 'every initial-letter surah works' claim fails for at least 4 of the 29 surahs under any fixed orthographic convention."
confidence_in_replicability: "low (requires orthographic edits and counting conventions that are not disclosed uniformly; fails replication under Tanzil Uthmani)"
notes: "Highest-priority replication target: will explode or confirm the whole Code-19 thesis."
```

---

```yaml
claim_id: khalifa-114-chapters-19x6
claim_statement: "The Quran has exactly 114 chapters = 19 x 6."
claimant: "Rashad Khalifa, 1974+"
counting_rules:
  orthography: "not-applicable"
  word_definition: "not-applicable"
  letter_definition: "not-applicable"
  basmala_policy: "not-applicable"
supporting_evidence: "114/19 = 6 exactly."
known_criticisms: "Coincidence by construction: 114 is a small integer, divisibility by 19 has 1/19 probability. Also: early variant codices (Ibn Mas'ud lacked Al-Fatiha and the two mu'awwidhatayn; Ubayy added surahs al-Hafd and al-Khal') had 111-116 surahs, so the 114 is not textually certain even within early tradition."
confidence_in_replicability: "high (trivially true for the canonical Uthmani mushaf)"
notes: "Trivial observation treated as evidence."
```

---

```yaml
claim_id: khalifa-basmala-count-114
claim_statement: "The basmala appears 114 times in the Quran despite being absent from Surah 9; the 'missing' basmala at Surah 9 is compensated by a second basmala in Surah 27 at 27:30 ('It is from Solomon, and it is in the name of God...'). From the missing basmala (Surah 9) to the extra basmala (Surah 27) is exactly 19 chapters. Sum of chapter+verse (27+30=57) is 19x3."
claimant: "Rashad Khalifa, Appendix 1"
counting_rules:
  orthography: "not-applicable"
  word_definition: "the 27:30 instance must be counted as a 'basmala' even though it is embedded in a narrative verse and not an opening formula"
  letter_definition: "not-applicable"
  basmala_policy: "opening-basmalas counted as tokens, plus 27:30"
supporting_evidence: "113 opening basmalas + 1 at 27:30 = 114 = 19x6. 27 - 9 = 18 chapters; Khalifa counts inclusively as 19. 27+30 = 57 = 19x3."
known_criticisms: "The 'inclusive' count 9 to 27 = 19 chapters is an off-by-one choice that fits the desired number. The 27:30 instance uses 'bismi-llahi r-rahmani r-rahim' phrasing verbatim but is part of Solomon's letter, not a separator."
confidence_in_replicability: "high (the text facts are real; the interpretation is the claim)"
```

---

```yaml
claim_id: khalifa-grand-total-346199
claim_statement: "Sum across all 114 suras of [sura number + number of verses in sura + sum of verse numbers 1..N] equals 346199 = 19 x 19 x 959."
claimant: "Rashad Khalifa, Appendix 1; re-cited by every Code-19 source since."
counting_rules:
  orthography: "not-applicable"
  word_definition: "not-applicable"
  letter_definition: "not-applicable"
  basmala_policy: "uses Hafs verse-numbering; verses of Al-Fatiha counted with basmala as verse 1"
  verse_numbering: "hafs-kufan (6236)"
supporting_evidence: "Arithmetic: formula is completely mechanical and reproducible."
known_criticisms: "The formula is post-hoc chosen among many possible linear combinations of chapter/verse numbers. A multiple-comparison argument (McKay, Bar-Natan style): the number of length-3 symmetric functions of (sura#, verse count, triangular-number-of-verses) is large; 1/19 of them divide by 19. 346199 / 19^2 = 959 is not itself a prime or special number."
confidence_in_replicability: "high (pure arithmetic; we will verify to the integer)"
notes: "Priority anchor test: computable from verse-numbering alone."
```

---

```yaml
claim_id: khalifa-6346-total-verses
claim_statement: "When basmalas are all counted as verses (including the 112 'unnumbered' ones), total verse count = 6346 = 19 x 334; and 6+3+4+6 = 19."
claimant: "Rashad Khalifa; Edip Yüksel"
counting_rules:
  verse_numbering: "hafs-kufan with all 113 opening basmalas numbered as verse 1 (Al-Fatiha already has basmala as v1; this effectively adds 112 verses to 6234); note 6236 - 2 (9:128-129, which Khalifa rejects) + 112 = 6346"
supporting_evidence: "6346/19 = 334 exactly; digit sum 19."
known_criticisms: "Requires both (a) rejecting 9:128-129, and (b) adding the non-numbered basmalas as verses — two non-standard moves. Under canonical Hafs (6236), the count is not divisible by 19."
confidence_in_replicability: "medium (arithmetic holds only under Khalifa's dual revision)"
```

---

```yaml
claim_id: khalifa-salat-67
claim_statement: "The word 'Salat' (contact prayer) occurs 67 times; sum of (sura + verse) for all occurrences = 4674 = 19 x 246."
claimant: "Rashad Khalifa, Appendix 1"
counting_rules:
  word_definition: "includes all inflected forms of the lemma صلاة (salat), per Khalifa's concordance"
  basmala_policy: "not-applicable"
supporting_evidence: "Khalifa's concordance table in Appendix 1."
known_criticisms: "Other concordances (e.g., al-Mu'jam al-Mufahras by Abd al-Baqi) give different totals depending on which morphological forms of the root are included."
confidence_in_replicability: "medium (lemma-level counts are reproducible if we adopt the Quranic Arabic Corpus lemmatization)"
```

---

```yaml
claim_id: khalifa-sawm-1387
claim_statement: "The Quran's fasting (sawm/siyam) references total 1387 = 19 x 73 when summed over verses-of-commandment."
claimant: "Rashad Khalifa, Appendix 1"
counting_rules: "not-disclosed-by-source (which verses count as 'commandment' is not algorithmic)"
supporting_evidence: "Tabulation in Appendix 1."
known_criticisms: "The set of 'commandment verses' is chosen ad hoc; there is no way to reproduce without Khalifa's verse list."
confidence_in_replicability: "low"
```

---

```yaml
claim_id: khalifa-zakat-hajj-3040
claim_statement: "Sum of zakat and hajj reference totals = 3040 = 19 x 160 (individually neither divides by 19, but the sum does)."
claimant: "Rashad Khalifa, Appendix 1"
counting_rules: "not-disclosed-by-source"
supporting_evidence: "Appendix 1 tables."
known_criticisms: "Openly acknowledged that individual counts are off by 1 each; combining is a post-hoc patch."
confidence_in_replicability: "low"
```

---

```yaml
claim_id: khalifa-first-revelation-19-words-76-letters
claim_statement: "The first revelation (96:1-5) consists of 19 words and 76 letters (4 x 19)."
claimant: "Rashad Khalifa"
counting_rules:
  orthography: "Uthmani rasm"
  word_definition: "orthographic-token"
  letter_definition: "graphemes under a specific hamza/alif choice (not disclosed)"
supporting_evidence: "Direct count of 96:1-5."
known_criticisms: "Word count depends on whether 'iqra' is counted as one word; letter count depends on how hamzas and long-alifs are counted. Under Tanzil Uthmani with standard grapheme counting the numbers are different."
confidence_in_replicability: "medium (reproducible once a canonical orthography is chosen)"
```

---

```yaml
claim_id: khalifa-quran-word-58
claim_statement: "The word 'Quran' (as a proper noun referring to this book) appears 58 times; excluding one occurrence that refers to 'any recitation' gives 57 = 19 x 3."
claimant: "Rashad Khalifa"
counting_rules:
  word_definition: "lemma q-r-' with semantic filter (referring to the book vs. generic recitation); filter is not algorithmic"
supporting_evidence: "Appendix 1 concordance."
known_criticisms: "The semantic exclusion is hand-picked. Al-Mu'jam al-Mufahras gives different totals for the root."
confidence_in_replicability: "low (the 'referential vs generic' distinction is interpretive)"
```

---

```yaml
claim_id: khalifa-numbers-in-quran
claim_statement: "There are 30 distinct numbers mentioned in the Quran; their sum = 162146 = 19 x 8534. Counting all occurrences gives 285 = 19 x 15."
claimant: "Rashad Khalifa, Appendix 1"
counting_rules:
  word_definition: "any cardinal, ordinal, or fractional numeral token; basis for 'distinct' not disclosed"
supporting_evidence: "Appendix 1 table listing the 30 unique numbers and their sums."
known_criticisms: "Whether 'half', 'third', 'double' count; whether 'thousand' and 'thousands' are one number or two; whether numbers in narrative (e.g., 7 heavens, 40 days) count — all ad hoc."
confidence_in_replicability: "medium"
```

---

```yaml
claim_id: khalifa-9-128-129-rejection
claim_statement: "Verses 9:128 and 9:129 are later human interpolations, not part of the original Quran; removing them is required for multiple 19-counts to work."
claimant: "Rashad Khalifa, Appendix 24"
counting_rules: "not-applicable (textual-critical claim)"
supporting_evidence: "Khalifa argued these verses are of Medinan style but contain Meccan themes; cites a weak hadith about a scribe's late addition."
known_criticisms: "All existing manuscripts (San'a, Birmingham, etc.) contain 9:128-129. Sunni, Shi'i, and academic scholarship uniformly reject the interpolation claim. Edip Yüksel and many ex-Submitters recognised the circularity (removing verses to save a numerical claim)."
confidence_in_replicability: "not-applicable"
notes: "Critical because MANY Khalifa counts become not-divisible-by-19 if 9:128-129 are retained."
```

---

## Family B — Classic word-pair symmetries (Al-Kaheel, Taslaman, and others)

```yaml
claim_id: pair-day-year-365
claim_statement: "The word 'yawm' (day, singular) occurs exactly 365 times in the Quran, matching the solar year."
claimant: "Attributed to various early compilers; popularised by Abdul-Daem Al-Kaheel (kaheel7.com) and cited in Caner Taslaman, 'The Quran: Unchallengeable Miracle' (2006)."
counting_rules:
  word_definition: "singular 'yawm' only, including prefix-bearing forms (bi-, wa-, fa-, li-) but EXCLUDING dual 'yawmayn', plural 'ayyam', plural 'ayyaman', possessive-suffixed forms (yawmukum, yawmihim), and the fused form 'yawma'idhin' (on that day); policy is not disclosed explicitly by al-Kaheel but must be inferred from reaching the number"
supporting_evidence: "Counting software (WikiIslam): all forms of yawm = 475; to reach 365 one excludes 3 dual + 27 plural + 10 suffixed + 70 yawma'idhin, while retaining 91 prefixed."
known_criticisms: "Islam QA (islamqa.info/en/answers/69741) rejects the claim on calendrical grounds: the Islamic calendar is 354-day lunar; the 365-day year is Gregorian. Answering-Islam's '365 Days Hoax' article documents selective counting. The same method applied to 'night' (layl) yields ~92, not 365."
confidence_in_replicability: "medium (the claim is reproducible ONLY under Al-Kaheel's specific exclusion filter; changing the filter breaks it)"
notes: "Canonical example of selective-counting. Test under every word-definition in methodology.md §2."
```

---

```yaml
claim_id: pair-month-12
claim_statement: "The word 'shahr' (month, singular) occurs exactly 12 times in the Quran."
claimant: "Al-Kaheel, Taslaman, and the general 'word count miracles' literature."
counting_rules:
  word_definition: "singular shahr only; excludes plural 'ashhur' and 'shuhur'"
supporting_evidence: "Direct concordance counts."
known_criticisms: "Plural forms (ashhur, shuhur) also appear, bringing the total to 21+. The 'miracle' depends on counting singular forms only."
confidence_in_replicability: "high (under the singular-only rule)"
```

---

```yaml
claim_id: pair-year-sana-19
claim_statement: "The word 'sana' (year, singular) occurs exactly 19 times in the Quran."
claimant: "Code-19 + Al-Kaheel school"
counting_rules:
  word_definition: "singular 'sana' only; plural 'sinin' excluded"
supporting_evidence: "Ali Adams (QuranCode) and al-Kaheel concordances."
known_criticisms: "Plural sinin excluded arbitrarily."
confidence_in_replicability: "medium"
```

---

```yaml
claim_id: pair-day-night
claim_statement: "Day (yawm) and night (layl) each occur 'balanced' numbers of times matching day-night equivalence in a 365-day year (day: 365 sing.; night: not same count but claimed balanced otherwise)."
claimant: "Al-Kaheel et al."
counting_rules: "not-disclosed-by-source; counts do NOT balance numerically and most sources do not claim they do"
supporting_evidence: "Al-Kaheel does not actually claim 365/365 for day/night; he claims 365 for day and a different layer (e.g., 12 months, 30 days, 24 hours) for the other time-units."
known_criticisms: "The day/night pair is sometimes misattributed; the real 365 claim is day-only-vs-solar-year."
confidence_in_replicability: "low (the claim is often misstated; needs disambiguation from original source)"
notes: "Clarify before testing. The actual Kaheel claim is the 365 day-count, NOT a day/night symmetry."
```

---

```yaml
claim_id: pair-man-woman-24
claim_statement: "The words 'rajul' (man) and 'imra'a' (woman) each occur exactly 24 times in the Quran, symbolising human equality."
claimant: "Widely attributed to Abdul-Razzaq Nawfal, 'al-I'jaz al-'Adadi li-l-Qur'an al-Karim' (1983); re-cited by Al-Kaheel and Taslaman."
counting_rules:
  word_definition: "singular indefinite forms only: 'rajul' and 'imra'a'; plurals rijal/nisa excluded; other singular female-referring nouns (imra'atun, 'ajuz, dhati hamlin, mushrika, mu'mina) excluded"
supporting_evidence: "WikiIslam documents the count: 24 each under strict singular-indefinite counting."
known_criticisms: "The exclusion of other singular female nouns is arbitrary; including them breaks the symmetry. The 'rajulan' in 7:155 actually refers to 70 men. Critics (Shabir Ally, Abdullah Sameer, ex-Muslim critics) argue the selection is post-hoc."
confidence_in_replicability: "high (under strict filter) / low (under natural counting)"
```

---

```yaml
claim_id: pair-dunya-akhira-115
claim_statement: "'al-dunya' (this world) and 'al-akhira' (the hereafter) each occur 115 times in the Quran."
claimant: "Nawfal (1983); Al-Kaheel; Taslaman; widely repeated."
counting_rules:
  word_definition: "definite forms 'al-dunya' and 'al-akhira' only; indefinite and prefixed forms filtered"
supporting_evidence: "Nawfal's tables; al-Kaheel's Numeric Miracle pages."
known_criticisms: "WikiIslam: 'dunya' doesn't always mean 'this world' (contexts like 'nearer', 'lower heaven'), and 'akhira' doesn't always mean 'hereafter'. Semantic selection, not linguistic."
confidence_in_replicability: "medium (reproducible under strict definite-form counting)"
```

---

```yaml
claim_id: pair-life-death-145
claim_statement: "'Life' (al-hayat and derivatives) and 'death' (al-mawt and derivatives) each occur 145 times."
claimant: "Nawfal (1983); popularised by Harun Yahya, Al-Kaheel."
counting_rules: "not-disclosed-by-source (mixes nouns and verbs; includes derivatives)"
supporting_evidence: "Tables in Nawfal and various popular sites."
known_criticisms: "WikiIslam: pure noun counts give ~78 for life, ~114 for death-related nouns. To reach 145/145 one must mix nouns and verbs asymmetrically. 'Living' (hayy) counts for 'life' but 'dying' (yamutu) selectively for 'death'. No consistent rule yields 145."
confidence_in_replicability: "low"
```

---

```yaml
claim_id: pair-angels-devils-88
claim_statement: "'Angels' (malaika / malak) and 'devils' (shayatin / shaytan) each occur 88 times."
claimant: "Nawfal; Al-Kaheel; Taslaman; Erdem Çetinkaya; repeated on iqra.study et al."
counting_rules:
  word_definition: "all forms of the root m-l-k meaning angel (plural+singular); all forms of sh-y-t-n (plural+singular+derivatives); definite and indefinite"
supporting_evidence: "Word-by-word concordance counts under that rule."
known_criticisms: "WikiIslam: shaytan in basic form appears 69 times, angel ~11; combining forms to reach 88/88 is inconsistent with other 'miracles' in the same list that exclude plurals."
confidence_in_replicability: "medium (reproducible under the specific lump-all-forms rule)"
```

---

```yaml
claim_id: pair-sea-land-32-13
claim_statement: "The word 'bahr' (sea) occurs 32 (or 33) times and 'barr' (land) 13 times; the ratio 32:(32+13) ≈ 71% vs 13:45 ≈ 29% matches the modern measurement of Earth's surface as 71% water / 29% land."
claimant: "Abdul-Daem Al-Kaheel, kaheel7.com, 'Land and Sea' article (c. 2008); also on truth-seeker.info and answering-christianity.com."
counting_rules:
  orthography: "not-disclosed-by-source"
  word_definition: "singular forms 'bahr' and 'barr', including prefixed forms; excluding plural 'bihar' and derived forms"
supporting_evidence: "33/46 ≈ 0.717; 13/46 ≈ 0.283."
known_criticisms: "(1) WikiIslam: including all forms of 'bahr' gives 41 and all forms of 'barr' gives 12, yielding 77/23 — not the modern ratio. (2) The ratio 71/29 refers to SURFACE area, but the Quran mentions hydrosphere vs crust not in area terms. (3) 'Barr' in Arabic means 'dry land' but also 'righteousness' / 'pious' — semantic ambiguity. (4) Modern ocean-surface ratio is ~70.8% not 71.7%. (5) The word 'bahr' occurs 32 times in one source and 33 in another; the claim is not stable."
confidence_in_replicability: "medium (under Al-Kaheel's filter) / low (otherwise)"
notes: "Priority replication target: simple lemma count, easy to verify."
```

---

```yaml
claim_id: pair-sun-light-33
claim_statement: "'Sun' (shams) and 'light' (nur) each occur 33 times."
claimant: "Nawfal, Al-Kaheel"
counting_rules:
  word_definition: "singular 'shams' (with some prefixed forms including shamsan) and 'nur' (with some prefixed forms but excluding possessive-suffixed)"
supporting_evidence: "WikiIslam confirms the count is reachable under a specific filter."
known_criticisms: "Filter is not applied consistently with other 'miracle' pairs; excluding possessives for one and including prefixes for the other is arbitrary."
confidence_in_replicability: "medium"
```

---

```yaml
claim_id: pair-jesus-adam-25
claim_statement: "'Isa (Jesus) and Adam each occur 25 times in the Quran, reflecting the Quranic parallel ('The example of Jesus is like the example of Adam...', 3:59)."
claimant: "Nawfal (1983); widely cited."
counting_rules:
  word_definition: "proper-noun occurrences only; excluding possessive/pronominal references"
supporting_evidence: "Quranic concordance counts."
known_criticisms: "Confirmed by Quranic Arabic Corpus (corpus.quran.com): Jesus as 'Isa = 25; Adam = 25. THIS PAIR IS LIKELY TRUE as stated, though its miraculousness is dubious (small numbers + post-hoc pairing)."
confidence_in_replicability: "high"
notes: "One of the few that may actually replicate cleanly."
```

---

```yaml
claim_id: pair-say-said-332
claim_statement: "'Qala' (he said) and 'qul' (say!, imperative) each occur 332 times."
claimant: "Nawfal; Al-Kaheel; Taslaman"
counting_rules:
  word_definition: "exact form 'qala' vs exact form 'qul'; all other forms of q-w-l excluded"
supporting_evidence: "Quranic Arabic Corpus: 'qul' appears 332 times as an exact imperative form."
known_criticisms: "The pairing excludes the 1700+ other forms of q-w-l. Comparing two exact forms of the same verb and noting they happen to match is curious but the selection is post-hoc."
confidence_in_replicability: "high"
```

---

```yaml
claim_id: pair-muslim-women-men-41
claim_statement: "'Muslimun' (Muslim men) and 'muslimat' (Muslim women) each occur 41 times."
claimant: "Nawfal et al."
counting_rules: "not-disclosed-by-source"
supporting_evidence: "Quoted in handwiki.org/wiki/Symmetry_in_the_Quran."
known_criticisms: "Exact form dependence as with other pairs."
confidence_in_replicability: "medium"
```

---

```yaml
claim_id: pair-near-far-115
claim_statement: "'Near' (qareeb/dunya-sense) and 'far' (ba'id/akhira-sense) each occur 115 times — equivalent to the dunya/akhira pair but linguistically reframed."
claimant: "Nawfal"
counting_rules: "not-disclosed-by-source"
supporting_evidence: "handwiki listing."
known_criticisms: "Semantic slippage — same root-pair as dunya/akhira; not a new claim."
confidence_in_replicability: "low"
```

---

```yaml
claim_id: pair-winter-summer-1
claim_statement: "Winter (shita') and summer (sayf) each occur exactly 1 time (both in Surah 106, Quraysh)."
claimant: "Nawfal"
counting_rules: "direct"
supporting_evidence: "Verse 106:2 mentions the winter and summer journeys of Quraysh."
known_criticisms: "True but trivial: both words appear in the same verse, so the 'symmetry' is just that they were mentioned together. Not a distributed pattern."
confidence_in_replicability: "high"
```

---

```yaml
claim_id: pair-good-deeds-wrongdoings-167
claim_statement: "'Good deeds' (hasanat) and 'wrongdoings' (sayyi'at) each occur 167 times."
claimant: "Nawfal"
counting_rules: "not-disclosed-by-source"
supporting_evidence: "handwiki listing."
known_criticisms: "Form selection not stated."
confidence_in_replicability: "medium"
```

---

```yaml
claim_id: pair-people-prophets-50
claim_statement: "'People' (al-nas) and 'prophets/messengers' (anbiya/rusul) each occur 50 times."
claimant: "Nawfal"
counting_rules: "not-disclosed-by-source"
supporting_evidence: "handwiki listing."
known_criticisms: "Under Quranic Arabic Corpus, 'al-nas' appears far more than 50 times (>240 forms of n-w-s). The 50 count requires a very specific filter."
confidence_in_replicability: "low"
```

---

```yaml
claim_id: pair-seven-heavens-7
claim_statement: "The phrase 'seven heavens' (sab' samawat) occurs exactly 7 times."
claimant: "Al-Kaheel"
counting_rules:
  word_definition: "exact bigram 'seven heavens'"
supporting_evidence: "Direct concordance: 2:29; 17:44; 23:86; 41:12; 65:12; 67:3; 71:15 (7 occurrences)."
known_criticisms: "True as stated; small-number coincidence (7 is a common biblical/Quranic number)."
confidence_in_replicability: "high"
```

---

## Family C — Al-Kaheel "Marvels of the Number 7" system

```yaml
claim_id: kaheel-sevens-system
claim_statement: "A comprehensive 'numeric system' in the Quran based on the number 7: Quranic chapters, verses, words, and letters all exhibit multiples of 7. Example: the word 'Hell' (jahannam) occurs 77 times; from Surah 2 (where '7' is first stated) to Surah 78 (where '7' is last stated) there are exactly 77 surahs; from first 'Allah' (1:1) to last 'Allah' (112:2) there are 6223 verses (multiple of 7)."
claimant: "Abdul-Daem Al-Kaheel, 'The Marvels of the Number Seven in the Noble Qur'an' (free e-book, 2008+)."
counting_rules:
  orthography: "Uthmani"
  word_definition: "specific lemmas (jahannam, Allah); inflected forms included selectively"
  letter_definition: "graphemes"
  basmala_policy: "included in verse counts"
supporting_evidence: "Al-Kaheel's e-book tabulates dozens of 7-divisible counts."
known_criticisms: "Same multiple-comparison issue as Code-19 but worse (7 is smaller, so ~1/7 of arbitrary integer combinations divide by 7 by chance). Critics: islamicstudies.info, WikiIslam, Abdullah Sameer. No formal peer-reviewed statistical refutation exists."
confidence_in_replicability: "medium (individual claims reproducible; the 'system' as a whole is unfalsifiable because the choice of which combinations to count is open-ended)"
```

---

```yaml
claim_id: kaheel-fatiha-7-29-139
claim_statement: "Surah Al-Fatiha has 7 verses, 29 words, and 139 letters — all prime numbers. The 14 unique 'muqatta'at letters' appear 119 times within Al-Fatiha (119 = 7 x 17)."
claimant: "Al-Kaheel, 'Beautiful Findings: The Numerical Miracle of Surat Al-Fatiha' (kaheel7.com)."
counting_rules:
  orthography: "Uthmani"
  word_definition: "orthographic-token; basmala counted as verse 1"
  letter_definition: "graphemes, with-shadda-not-doubled, hamzas collapsed"
  basmala_policy: "counted-in-surah (basmala IS verse 1 of Al-Fatiha)"
supporting_evidence: "Al-Kaheel's article tabulates: 7 verses, 29 words, 139 letters. 7, 29, 139 are all prime."
known_criticisms: "(1) The 29-words count excludes diacritics and treats clitics as fused; a with-clitics-split count gives >29. (2) The 139-letter count varies from 113 to 152 depending on alif/hamza/shadda conventions. (3) Primality is cherry-picked: 7 and 29 and 139 happen to be prime, but if any were not, no one would mention them. (4) The 'basmala as verse 1' policy is controversial — Hanafi tradition does not count it."
confidence_in_replicability: "high (under a fixed orthography and the basmala-as-v1 choice) / medium otherwise"
notes: "Priority replication anchor. Test under all six combinations of {basmala policy} x {letter definition}."
```

---

```yaml
claim_id: primalogy-al-fatiha-prime-letter-values
claim_statement: "A letter-value system (primalogy) derived from Al-Fatiha assigns prime numbers as letter values. With basmala, the total primalogy value of Al-Fatiha is 4201 (digit sum 7, both primes); without basmala, 3167 (digit sum 17, both primes)."
claimant: "Ali Adams, QuranCode software (github.com/exss/QuranCode-1); 'Quran and Primalogy: Prime Numbers and The Key' (2010+)."
counting_rules:
  abjad_table: "custom primalogy table (not standard mashriqi/maghribi); letters assigned prime values"
  basmala_policy: "reported both with and without"
supporting_evidence: "QuranCode software outputs."
known_criticisms: "Custom letter-value system has no textual or historical basis. Primality of the output is cherry-picked among many sums. No independent researcher has reproduced."
confidence_in_replicability: "medium (reproducible if QuranCode source is inspected for the letter-value table)"
```

---

## Family D — Surah-level numerical claims

```yaml
claim_id: baqarah-middle-ayah-143
claim_statement: "Ayah 2:143 is the middle ayah of Surah Al-Baqarah (286/2 = 143) and its content ('We have made you a middle nation, ummatan wasata') thematically mirrors its numerical centrality."
claimant: "Popular social media / linguisticmiracle.wordpress.com; attributed in various forms to Al-Kaheel and others. Likely earlier in traditional tafsir as a literary observation, not a numerical claim."
counting_rules:
  verse_numbering: "hafs-kufan; 286 verses in Al-Baqarah"
supporting_evidence: "286 / 2 = 143."
known_criticisms: "(1) 286 is even; a sequence of 286 has no single middle element — the 143rd and 144th are both 'middle'. Proponents choose 143 because 2:143 thematically fits; under 144 the claim fails. (2) Other recitation traditions count Al-Baqarah at 284, 285, or 287 verses, so the midpoint varies. (3) Post-hoc thematic matching: any thematic verse near the middle will seem to 'fit'."
confidence_in_replicability: "high (the arithmetic is trivial) / low (the thematic significance is subjective)"
notes: "Explicitly requested by user for replication. Test under all five verse-numbering traditions (hafs, warsh, basran, damascene, madanian)."
```

---

```yaml
claim_id: al-asr-letter-balance
claim_statement: "Surah Al-Asr (103) has 3 verses, ~14 words, and ~73 letters. Internal balance: words plus letters in ayat 1-3 sum to match total letters; other internal sum properties."
claimant: "Various; compiled in 114chambers.wordpress.com, answering-christianity.com."
counting_rules: "not-disclosed-by-source"
supporting_evidence: "Verse-by-verse sums quoted in 114chambers article."
known_criticisms: "Counts vary by 1-2 depending on orthography. The 'balance' relationships are ad hoc arithmetic; no independent confirmation across orthographies."
confidence_in_replicability: "low"
```

---

```yaml
claim_id: al-kawthar-10-structure
claim_statement: "Surah Al-Kawthar (108) has exactly 10 words and 42 letters in 3 verses. The Arabic letter alif (ا) appears 10 times; 10 distinct letters appear only once in the surah. 10 is the structural key of the shortest surah."
claimant: "Zajel Arabic Institute; M. Khyzer Bin Dost and M. Ahmad, 'Towards Exploring Mathematical Facts of Surah Al-Kawthar' (Al-Burhan journal, IIUM, 2022)."
counting_rules:
  orthography: "Uthmani"
  word_definition: "orthographic-token"
  letter_definition: "graphemes including alif/hamza — but the 'alif=10' claim depends on counting every alif including mamduda"
  basmala_policy: "basmala excluded (not counted)"
supporting_evidence: "Published in Al-Burhan: Journal of Qur'an and Sunnah Studies. Tables of letter frequencies."
known_criticisms: "Dependent on letter-counting convention; if shadda-doubled or hamza-distinct, totals change. Base-10 is an Indo-Arabic numeral convention; the 'divine 10' is anachronistic."
confidence_in_replicability: "high (peer-reviewed arithmetic) under the specific letter convention; medium otherwise"
notes: "Peer-reviewed journal source — higher prior than most Code-19 claims."
```

---

```yaml
claim_id: al-hadid-iron-gematria
claim_statement: "Surah Al-Hadid is chapter 57. The abjad (gematric) value of 'al-hadid' (الحديد) = 57. The abjad of 'hadid' alone (حديد) = 26 = atomic number of iron. Iron's most common isotope has mass number 56 (close to 57). The word 'al-hadid' appears in verse 57:25."
claimant: "Harun Yahya; Al-Kaheel; and 'The Atomic Number of Iron' articles on quranmiracles.com, truth-seeker.info, submission.org"
counting_rules:
  abjad_table: "mashriqi eastern table"
supporting_evidence: "abjad(al-hadid) = 1+30+8+4+10+4 = 57 (ا=1, ل=30, ح=8, د=4, ي=10, د=4). abjad(hadid) = 8+4+10+4 = 26. Chapter number = 57. Iron atomic number = 26. Iron mass number = 56."
known_criticisms: "(1) Iron's most abundant isotope is Fe-56, not Fe-57; the match is off by one and apologists sometimes cite Fe-57. (2) Abjad table choice is post-hoc: maghribi table yields different values. (3) Surah numbering is a later convention; in early manuscripts the order differs. (4) The claim retro-fits science to text. (5) Iron's atomic number was not known until Moseley (1913)."
confidence_in_replicability: "high (gematric arithmetic is trivial; the physics interpretation is the contested part)"
```

---

```yaml
claim_id: al-insan-middle-word-silver
claim_statement: "Surah Al-Insan (76) has 247 words; the middle word (word #124) is 'fiddah' (silver), which itself appears 3 times in the surah and is located in the middle verse (16 of 31)."
claimant: "Compiled in handwiki.org/wiki/Symmetry_in_the_Quran; attributed to various Arabic authors."
counting_rules:
  orthography: "not-disclosed-by-source"
  word_definition: "orthographic-token, 247 words"
supporting_evidence: "Direct count and positional claim."
known_criticisms: "Word-token count varies between 243 and 254 under different tokenizations; the '247' and '#124' claims break outside a specific tokenization."
confidence_in_replicability: "medium"
```

---

```yaml
claim_id: al-qadr-numerical
claim_statement: "Surah Al-Qadr (97) has 30 words; the 27th word is 'hiya' (it/she), thematically pointing to laylat al-qadr being the 27th night of Ramadan."
claimant: "answering-christianity.com 'Surat Al-Qadr's Numerical Miracle'; various popular sources."
counting_rules: "orthographic-token; basmala excluded"
supporting_evidence: "Direct count."
known_criticisms: "Word-token count depends on clitic treatment; the 27th-of-Ramadan identification is a minority tradition, not consensus."
confidence_in_replicability: "medium"
```

---

## Family E — Structural / chiastic / ring-composition claims

```yaml
claim_id: farrin-quran-wide-ring
claim_statement: "The 114 surahs of the Quran are organised as 9 opening 'groups' and 9 closing 'groups' in concentric correspondence, with a central group dealing with the Hereafter. Each surah and group exhibits ring (chiastic) composition."
claimant: "Raymond Farrin, 'Structure and Qur'anic Interpretation: A Study of Symmetry and Coherence in Islam's Holy Text' (White Cloud Press, 2014). Builds on Michel Cuypers, Amin Islahi, Neal Robinson."
counting_rules:
  orthography: "not-applicable (structural-literary, not counting)"
  word_definition: "not-applicable"
  letter_definition: "not-applicable"
supporting_evidence: "Farrin identifies ABCBA-style parallels within surahs and between surah pairs; uses Cuypers' three figures (parallel, mirror, concentric)."
known_criticisms: "Nicolai Sinai, 'Review: Going Round in Circles' (Journal of Qur'anic Studies, 2017): Farrin and Cuypers 'substantially overplay their hand' by making ring structures ubiquitous; many of the correspondences are loose and subjective; no statistical significance test applied."
confidence_in_replicability: "low (literary, not numerical; each ring claim must be evaluated on its own)"
notes: "Included as the most respected structural claim set."
```

---

```yaml
claim_id: cuypers-ma'ida-chiasmus
claim_statement: "Surah Al-Ma'ida (5) is a concentric chiasmus centered on verses 5:40-43 (God's sovereignty); Cuypers demonstrates the entire 120-verse surah as a ring of nested ABCDC'B'A' units."
claimant: "Michel Cuypers, 'The Composition of the Qur'an: Rhetorical Analysis' (Bloomsbury, 2015); earlier 'Le Festin' (2007) on Surah Al-Ma'ida specifically."
counting_rules: "not-applicable"
supporting_evidence: "Cuypers' rhetorical analysis diagrams."
known_criticisms: "Sinai (2017): Cuypers' semantic parallels are often distant or strained; no quantitative threshold for 'parallel'."
confidence_in_replicability: "low (subjective literary analysis)"
```

---

```yaml
claim_id: ayat-al-kursi-chiasmus
claim_statement: "Ayat al-Kursi (2:255) contains nine sentences forming a chiasm (ABCDEDCBA) centered on God's knowledge."
claimant: "Traditional observation; formalised by various modern rhetorical analysts."
counting_rules: "not-applicable"
supporting_evidence: "Direct textual structure."
known_criticisms: "Literary claim, no quantitative test; the 'nine sentences' count depends on parsing."
confidence_in_replicability: "medium"
```

---

## Family F — Bassam Jarrar / numerical prophecy

```yaml
claim_id: jarrar-israel-2022
claim_statement: "Based on Sura 17 (Al-Isra) verses 4-7 and numerical calculations rooted in the Code-19 family, the state of Israel will fall / decline in 2022 CE (specifically between March and June 2022 in later refinements). Calculation involves abjad values of 'hatmiyyah' (inevitability) and 'idha ja'a wa'd al-akhirah' ('when the promise of the hereafter comes')."
claimant: "Bassam Nihad Jarrar, Palestinian scholar, founder of Noon Center for Qur'anic Studies. First published as 'Zawal Isra'il 'Aam 2022' (1415 AH / 1995, 2nd ed. 1417 AH / 1996). Also 'Mu'jizat al-Tis'ata 'Ashar' (The Miracle of Nineteen, 1991)."
counting_rules:
  abjad_table: "mashriqi"
  word_definition: "lemma-level for the prophecy-relevant phrases"
  orthography: "Uthmani"
supporting_evidence: "Jarrar's 1996 book derives the year by (a) summing abjad values of specific Quranic phrases and (b) applying 19-based arithmetic. 'Israel' by abjad = 302; Jarrar's computation arrives at 1443 AH ≈ 2022 CE."
known_criticisms: "(1) The prediction failed: Israel did not fall in 2022. (2) Sophie Chamas, 'Counting the Ways: The Multiplicity of Apocalypses in Bassam Jarrar's The Decline of Israel' (Bryn Mawr thesis) documents how Jarrar's arithmetic allows many alternative dates. (3) After 2022, Jarrar and followers reinterpreted 'decline' as gradual rather than the original 'fall'."
confidence_in_replicability: "medium (the arithmetic is reproducible from the book; the prediction has empirically failed)"
notes: "Historically falsified. Replicating his calculation is valuable as a methodological example of unfalsifiable prophecy generation."
```

---

## Family G — Huruf muqatta'at and frequency claims

```yaml
claim_id: muqattaat-29-surahs-14-letters
claim_statement: "The disjointed letters (muqatta'at) open 29 of the 114 surahs and use 14 distinct letters out of the 28-letter Arabic alphabet (exactly half)."
claimant: "Classical observation; formalised numerologically by Khalifa and successors."
counting_rules:
  letter_definition: "graphemes; includes ا ه ح ط ي ك ل م ن س ع ص ق ر (14 letters)"
supporting_evidence: "Direct enumeration."
known_criticisms: "True as stated; the 'half the alphabet' observation is noted in classical tafsir, not originally numerological."
confidence_in_replicability: "high"
```

---

```yaml
claim_id: muqattaat-letters-in-opening-surahs
claim_statement: "The 14 muqatta'at letters collectively appear a specific number of times within each surah's muqatta'at that is supposedly a multiple of 19 when summed. E.g., Surah 42 (HM 'SQ) has its 5 initials summing in a 19-divisible way."
claimant: "Rashad Khalifa; elaborated in qurantalk.gitbook.io/quran-initial-count"
counting_rules:
  letter_definition: "graphemes; with-shadda-single; alif-maqsura-as-ya"
  basmala_policy: "counted-only-in-surah-1"
supporting_evidence: "Tables in Appendix 1."
known_criticisms: "Multiple failures documented: Khalifa's counts for Surah 42 and Surah 68 required orthographic edits not present in any manuscript. See khalifa-initial-letters-multiples-of-19."
confidence_in_replicability: "low"
```

---

## Family H — Prophets and names

```yaml
claim_id: prophets-mention-counts
claim_statement: "Prophet Musa (Moses) is mentioned most: 136 times. 'Isa (Jesus) appears 25 times. Muhammad appears 4 times by name + 1 time as 'Ahmad' = 5. Ibrahim (Abraham) 69 times. Adam 25. Nuh (Noah) 43."
claimant: "Standard concordance counts (al-Mu'jam al-Mufahras); reproduced on bayanulquran-academy.com and other popular sites."
counting_rules:
  word_definition: "proper-noun occurrences only; excluding pronouns, titles, 'the messenger'"
  orthography: "Uthmani"
supporting_evidence: "Quranic Arabic Corpus and al-Mu'jam al-Mufahras concordances."
known_criticisms: "The Jesus=Adam=25 symmetry (see pair-jesus-adam-25) is the load-bearing 'miracle' here; other counts are uninterpreted facts. Muhammad being mentioned only 5 times (vs Moses 136) is sometimes cited against the 'Muhammad wrote it himself' theory, which is a different argument."
confidence_in_replicability: "high"
```

---

## Family I — Meta claims / overall totals

```yaml
claim_id: quran-word-total-77449
claim_statement: "The Quran contains approximately 77,449 words and ~320,015 letters across 6,236 verses in 114 chapters."
claimant: "Traditional count (al-Suyuti, al-Itqan); reproduced on islamweb.net and jomalquran.my."
counting_rules:
  orthography: "Uthmani rasm"
  word_definition: "orthographic-token as written in Uthmani (clitics attached)"
  letter_definition: "graphemes without diacritics"
  basmala_policy: "counted-in-surah (113 opening basmalas included)"
  verse_numbering: "hafs-kufan (6236)"
supporting_evidence: "al-Suyuti's tally; modern reproductions give 77,430 to 77,934 depending on convention."
known_criticisms: "The 'total word count' varies across sources by a few thousand; there is no single canonical number. See docs/methodology.md §2."
confidence_in_replicability: "high (under fixed convention) / medium (across conventions)"
```

---

```yaml
claim_id: sum-all-numbers-162146
claim_statement: "The sum of all numbers explicitly mentioned in the Quran is 162146 (Khalifa: 162146 = 19 x 8534)."
claimant: "Rashad Khalifa, Appendix 1; repeated in handwiki.org/wiki/Symmetry_in_the_Quran as '162,146 = 19 × 8534'."
counting_rules:
  word_definition: "cardinal, ordinal, and fractional numbers treated as numbers; repetitions counted separately"
supporting_evidence: "Khalifa's tables."
known_criticisms: "What counts as a 'number' is ad hoc (half, third, twice, couple, few, many?). No reproducible algorithm."
confidence_in_replicability: "low"
```

---

```yaml
claim_id: quran-6236-or-variant-numbering
claim_statement: "The Quran has 6,236 verses under Hafs; 6,214 under Warsh; 6,205 under Basran; 6,227 under Damascene; 6,217 under Madinan II; etc. Different recitation schools split long verses differently."
claimant: "Standard tradition."
counting_rules:
  verse_numbering: "varies by school"
supporting_evidence: "Well documented."
known_criticisms: "Not a miracle claim per se; but IMPORTANT because any numerological claim depending on '286 verses in Al-Baqarah' fails under warsh (285) or basran (287). Noted by islamqa.info among critics of numerology."
confidence_in_replicability: "high"
notes: "Core sanity check: every numerological claim should be re-run under all 5 verse numberings."
```

---

## Family J — Critical / refutation literature

```yaml
claim_id: philips-code19-refutation
claim_statement: "Rashad Khalifa's Code-19 theory is a 'hoax or heresy': (1) Khalifa falsified counts by using non-attested orthography; (2) rejected 9:128-129 ad hoc to save claims; (3) individual initial-letter surah counts fail under standard Uthmani; (4) the multiple-comparison problem invalidates statistical significance."
claimant: "Abu Ameenah Bilal Philips, 'The Qur'an's Numerical Miracle: Hoax or Heresy?' (Al-Furqan Publications, 1987)."
counting_rules: "Philips re-counts under standard Hafs/Uthmani and shows mismatches."
supporting_evidence: "Book-length refutation; widely regarded by Sunni scholarship as the definitive rebuttal."
known_criticisms: "19.org and Submitters respond: Philips misunderstands Khalifa's counting rules; however ex-Submitters (Yüksel) admit Khalifa had arithmetic errors."
confidence_in_replicability: "high (Philips' refutation is itself reproducible)"
```

---

```yaml
claim_id: mckay-moby-dick-parody
claim_statement: "Equidistant-Letter-Sequence (ELS) style statistical claims — applied to the Torah by Witztum/Rips/Rosenberg and by analogy defended for the Quran — are refuted by finding similarly 'significant' patterns in arbitrary texts. McKay et al. found comparable patterns in Moby Dick and War and Peace."
claimant: "Brendan McKay, Dror Bar-Natan, Maya Bar-Hillel, Gil Kalai, 'Solving the Bible Code Puzzle' (Statistical Science, 1999)."
counting_rules: "statistical, not lexical"
supporting_evidence: "Peer-reviewed paper demonstrating the methodology's fragility."
known_criticisms: "Applies by analogy to Quran Code-19, not directly. No published McKay-style paper has targeted Khalifa specifically, but the multiple-comparison / researcher-degrees-of-freedom critique is standard."
confidence_in_replicability: "high"
notes: "Not a Quran claim itself, but the best statistical refutation framework we have."
```

---

```yaml
claim_id: wikiislam-word-count-refutations
claim_statement: "Every major word-count 'miracle' (day/night, man/woman, life/death, dunya/akhira, angels/devils, sun/light, sea/land) fails under natural counting rules; each is reproducible only under a bespoke filter of included/excluded morphological forms."
claimant: "WikiIslam editors (anonymous, ~2010-2020)."
counting_rules: "WikiIslam uses Quranic Arabic Corpus lemma counts."
supporting_evidence: "Article-by-article refutations with concordance counts."
known_criticisms: "WikiIslam is a polemical site, not peer-reviewed. Its factual concordance counts are nevertheless cross-checkable via corpus.quran.com."
confidence_in_replicability: "high (the raw counts are verifiable)"
```

---

```yaml
claim_id: sinai-ring-composition-critique
claim_statement: "Ring-composition claims (Farrin, Cuypers, Robinson) are literarily suggestive but methodologically unbounded: without a quantitative threshold for 'parallel', any text can be carved into concentric rings. The claims 'substantially overplay their hand'."
claimant: "Nicolai Sinai, 'Review: Going Round in Circles', Journal of Qur'anic Studies 19.3 (2017)."
counting_rules: "not-applicable"
supporting_evidence: "Peer-reviewed review essay."
known_criticisms: "None directly; Farrin defenders argue ring composition is culturally attested in Near Eastern literature."
confidence_in_replicability: "high"
```

---

## Family K — Edge cases and one-off claims

```yaml
claim_id: year-sana-19-sana-x-19-plural
claim_statement: "The singular 'sana' (year) occurs 19 times in the Quran. Further: 'sinin' (plural years) occurs in 7:130 as '19 years' specifically (Joseph in prison)."
claimant: "Code-19 school"
counting_rules: "exact singular form"
supporting_evidence: "Direct count."
known_criticisms: "Coincidental small integer."
confidence_in_replicability: "medium"
```

---

```yaml
claim_id: 30-numbers-in-quran
claim_statement: "The Quran mentions exactly 30 distinct numbers (cardinals and fractions)."
claimant: "Rashad Khalifa; widely re-cited."
counting_rules: "cardinal + fractional; 'dozen', 'few', 'many' excluded"
supporting_evidence: "List: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 19, 20, 30, 40, 50, 60, 70, 80, 99, 100, 200, 300, 1000, 2000, 3000, 5000, 50000, 100000, plus fractions 1/2, 1/3, 1/4, 1/5, 1/6, 1/8, 1/10, 2/3 = 30 distinct cardinal-or-fractional numbers."
known_criticisms: "Exact enumeration reproducible; the significance of 'exactly 30' is unclear."
confidence_in_replicability: "high"
```

---

```yaml
claim_id: heavens-earth-7-each
claim_statement: "'Seven heavens' as a phrase appears 7 times; 'earth' (ard) appears in balanced proportion with heaven (sama) references."
claimant: "Al-Kaheel; Harun Yahya"
counting_rules: "bigram match for 'sab' samawat'; lemma match for ard and sama"
supporting_evidence: "Direct enumeration."
known_criticisms: "The 'balance' between heaven/earth mentions varies by exact form; one popular version says sama=310, ard=461, very unbalanced."
confidence_in_replicability: "medium"
```

---

```yaml
claim_id: qibla-7
claim_statement: "The word 'qibla' (prayer direction) occurs exactly 7 times in the Quran."
claimant: "Al-Kaheel"
counting_rules: "lemma count"
supporting_evidence: "Direct."
known_criticisms: "True but trivial."
confidence_in_replicability: "high"
```

---

```yaml
claim_id: al-khateeb-chiastic-114chambers
claim_statement: "114 Chambers blog (anon. 'Siham Karami') visualises the whole Quran as nested chiastic structures, with quantitative summary tables of word/letter counts per surah showing concentric balance."
claimant: "114chambers.wordpress.com (anonymous, Siham Karami, 2014+)."
counting_rules: "not-disclosed-by-source for many claims"
supporting_evidence: "Blog posts with images and tables."
known_criticisms: "Self-published, anonymous, no peer review. Some counts diverge from corpus.quran.com."
confidence_in_replicability: "low"
```

---

```yaml
claim_id: taslaman-2006-comprehensive
claim_statement: "Comprehensive restatement of the Code-19 + word-pair symmetry tradition with additional novel claims (e.g., mathematical structure in Surah 113 (Al-Falaq) counts, and a 'Mathematical Miracle in Lexical Concordance' [MMLC] framework)."
claimant: "Caner Taslaman, 'The Quran: Unchallengeable Miracle' (Citlembik, 2006; trans. Ender Gürol)."
counting_rules:
  orthography: "Uthmani; Taslaman occasionally signals but does not systematically disclose"
  word_definition: "lemma with some inflections included"
supporting_evidence: "Book-length tabulation."
known_criticisms: "Taslaman adopts Khalifa's rules without full disclosure; critics note the same selective-counting pattern applies."
confidence_in_replicability: "medium"
notes: "Source PDF available at quranmiracles.com/wp-content/uploads/2011/06/UNCHALLENGEABLE-MIRACLE.pdf"
```

---

```yaml
claim_id: ali-adams-qurancode
claim_statement: "The QuranCode open-source software (by Ali Adams / exss) computes thousands of numerical properties of the Quranic text (abjad values, frequency tables, divisibility checks) and claims many patterns matching primes, 19, 7, and composite factors."
claimant: "Ali Adams, 'QuranCode-1', github.com/exss/QuranCode-1 (2010+)"
counting_rules:
  orthography: "configurable (Uthmani, Simple, Simple-Minimal)"
  word_definition: "orthographic-token"
  letter_definition: "configurable hamza/alif/shadda policies"
  abjad_table: "mashriqi default, maghribi optional, custom primalogy"
supporting_evidence: "Open-source; reproducible in principle."
known_criticisms: "Software outputs billions of features; without a pre-specified hypothesis, any 'match' is multiple-comparison gold mining. No statistical null model applied in published claims."
confidence_in_replicability: "high (the software is open-source) but the specific claims suffer the same researcher-degrees-of-freedom issue"
notes: "Potentially useful as a feature-extraction library for our own replications."
```

---

```yaml
claim_id: submission-org-verify-rashad-counts
claim_statement: "Submission.org publishes four different versions of Rashad Khalifa's initial-letter counts, showing his numbers changed over publications."
claimant: "19.org (ex-Submitter dissent), 'Rashad's four published counts of the Quranic initials, Four different times'"
counting_rules: "Khalifa's own varying claims"
supporting_evidence: "Internal Submission.org archive."
known_criticisms: "Shows that even Khalifa could not settle on a single count — evidence of arithmetic instability."
confidence_in_replicability: "high (the four publications are documented)"
notes: "Meta-evidence against the reliability of the original Code-19 corpus."
```

---

```yaml
claim_id: quran-constant-114chambers
claim_statement: "A 'Quran constant' — a specific large integer derived from sura-verse structure — is a mathematical 'security checksum' for the text."
claimant: "114 Chambers blog, 'The Quran Constant, a Divine Math-based Text Security System' (2022)"
counting_rules: "not-disclosed-by-source (mixes verse counts, sura numbers, and gematric sums)"
supporting_evidence: "Blog post with derivation."
known_criticisms: "Post-hoc constant construction; fits Khalifa's 346199 family."
confidence_in_replicability: "low"
```

---

```yaml
claim_id: hell-jahannam-77
claim_statement: "The word 'jahannam' (hell) appears exactly 77 times in the Quran (77 = 7 x 11)."
claimant: "Al-Kaheel, 'Marvels of the Number Seven'"
counting_rules: "lemma 'jahannam'; all forms"
supporting_evidence: "Quranic Arabic Corpus: jahannam as a proper noun appears 77 times (replicable)."
known_criticisms: "True but one of many lemmas; ~1/7 of lemma counts divide by 7."
confidence_in_replicability: "high"
```

---

```yaml
claim_id: allah-first-last-6223
claim_statement: "From the first occurrence of 'Allah' (1:1) to the last occurrence (112:2), there are exactly 6223 verses — a multiple of 7."
claimant: "Al-Kaheel"
counting_rules:
  word_definition: "lemma Allah"
  verse_numbering: "hafs-kufan"
supporting_evidence: "6223 = 7 x 889."
known_criticisms: "Depends on which verse is the 'first' and 'last' (basmala is verse 1 of Al-Fatiha under Kufan numbering; under other numberings the first Allah is 1:2). 6223 is not special beyond 7-divisibility."
confidence_in_replicability: "medium"
```

---

```yaml
claim_id: numerological-interpretation-qaf
claim_statement: "The letter ق (qaf) appears 57 times in Surah 50 (Qaf), and 57 times in Surah 42 (Shura), summing to 114 = 19 x 6; further, the Arabic word for 'Quran' is spelled with a qaf, tying these occurrences to the name of the book."
claimant: "Rashad Khalifa"
counting_rules:
  letter_definition: "graphemes, with-shadda-doubled (?); qaf in the opening ق counted"
  basmala_policy: "not counted for the qafs in the basmala"
supporting_evidence: "Khalifa's Appendix 1 claim."
known_criticisms: "Other researchers (including Muslim critics) get different counts for qaf in Surah 50 depending on shadda treatment; the 114 total is a post-hoc sum."
confidence_in_replicability: "medium"
```

---

## Metadata / next-steps

- Claims in this file: **45**
- Priority for replication (Phase 1): khalifa-bismillah-19-letters, khalifa-basmala-word-counts, khalifa-initial-letters-multiples-of-19, khalifa-grand-total-346199, pair-sea-land-32-13, pair-jesus-adam-25, baqarah-middle-ayah-143, kaheel-fatiha-7-29-139, al-kawthar-10-structure, al-hadid-iron-gematria.
- Claims that are structurally literary (no counting): khalifa-quran-74-30-reference, farrin-quran-wide-ring, cuypers-ma'ida-chiasmus, ayat-al-kursi-chiasmus, sinai-ring-composition-critique. These need qualitative, not numerical, review.
- Claims already falsified by time: jarrar-israel-2022.
- Claims that almost certainly replicate cleanly: pair-jesus-adam-25, pair-say-said-332, pair-seven-heavens-7, hell-jahannam-77, prophets-mention-counts, qibla-7, khalifa-114-chapters-19x6, muqattaat-29-surahs-14-letters.
- Claims that fundamentally depend on non-disclosed rules (treat with care): pair-life-death-145, pair-people-prophets-50, khalifa-sawm-1387, 114chambers-* family.

To add new claims, append a new YAML block at the end of the relevant Family section. Never renumber or reorder existing `claim_id`s; downstream files reference them.
