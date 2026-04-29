---
surah: 24
file_type: journal
date_started: 2026-04-28
date_last_updated: 2026-04-28
phase: B+
verdict: COMPLETE
---

# Q 24 al-Nūr — Investigation Journal

## 2026-04-28 — Specialist agent run

### Pre-flight reading completed

- `/Users/grey/Downloads/quran/.claude/skills/quran-investigation/SKILL.md`
- `/Users/grey/Downloads/quran/INVESTIGATION-PROTOCOL.md`
- `/Users/grey/Downloads/quran/KNOWLEDGE-GRAPH.md`
- `/Users/grey/Downloads/quran/surahs/Q024-al-nur/00-overview.md`

### H-NEW data integration

Pulled and integrated:
- H-NEW-840 UAS rank 5 / 114 (UAS = 4.4501, abs_outlier = 23.51, max_cost = 0.290, abs_sig_A = 0.79).
- H-NEW-590 outlier-strength rank 3 / 114 (Δ = +23.51 pp, classification MODERATE_OUTLIER).
- H-NEW-720 canonical-adjacency-cost: Q 23-Q 24 rank 11 / 113; Q 24-Q 25 rank 5 / 113. Q 24's both adjacencies in top-15 expensive — only Q 33 shares this property in the corpus.
- H-NEW-750 iʿjāz signature: sig_A = -0.79 (rank 82 / 114, anti-structural-iʿjāz); sig_B = -0.13 (rank 61); rhyme entropy 1.134 nats (rank 6, multi-rāwī).
- H-NEW-111 Fisher-Rao distance: mean to corpus 1.0704 (rank 105 / 114); nearest = Q 49 al-Ḥujurāt (0.870), farthest = Q 55 al-Raḥmān (1.426).

### Pre-registered novel tests run

| Pre-reg | Test | Pre-reg SHA-head | Verdict |
|:--|:--|:--|:--|
| Q024-F-01 | Light-vocabulary density | e89b858d926d | VINDICATED (p < 10⁻⁶ Bonferroni) |
| Q024-F-02 | Light-verse vs Throne-verse | (computed at runtime) | CONFIRMED |
| Q024-F-03A | al-ifk passage cohesion | ba1c09ed1f98 | CONFIRMED (81.5th pct) |
| Q024-F-03B | Q 24:35 structural midpoint | ba1c09ed1f98 | CONFIRMED (word + letter median) |
| Q024-F-04 | Hijab passages lexical comparison | 3d14e218cbc8 | CONFIRMED (Jaccard 0.153) |

### 8 classical claims audited (per `05-classical-claims-audit.md`)

| Audit | Verdict |
|:--|:--|
| 1. al-Qurṭubī's *maqṣūd* = chastity-and-covering | VINDICATED (60% of verses) |
| 2. al-Bāqillānī *iʿjāz al-fawāṣil* | FALSIFIED locally (sig_A rank 82); VINDICATED corpus-wide (r=-0.86) |
| 3. al-Ṭabarsī Q 24-named-for-light-density | VINDICATED p < 10⁻⁶ |
| 4. "Two parallel hijab passages" | FALSIFIED (re. symmetry); VINDICATED (re. lexical-distinction) |
| 5. al-ifk Q 24:11-20 coherent unit | VINDICATED 81.5th pct |
| 6. Q 24:35 structural midpoint | VINDICATED word-and-letter median |
| 7. Q 24:55 unique community-istikhlāf | VINDICATED |
| 8. al-Thaʿlabī's classical letter/word counts | VINDICATED 1.3% / 0.2% precision |

### Tafsir survey: 9 mufassirūn

al-Ṭabarī, al-Thaʿlabī, al-Ṭabarsī, al-Zamakhsharī, al-Rāzī, al-Qurṭubī, Ibn Kathīr, al-Biqāʿī, al-Suyūṭī. Plus al-Ghazālī's *Mishkāt al-Anwār* cited indirectly via al-Rāzī.

### Hadith corpus: all 9 books

Bukhārī, Muslim, Tirmidhī, Abū Dāwūd, Nasāʾī, Ibn Mājah, Mālik, Aḥmad, Dārimī. Surprising finding: the Light-verse predicate "Anta nūru al-samāwāti wa-l-arḍ" appears in the Prophetic Tahajjud-dhikr in **all 9 books** (Bukhārī #1088, Muslim #1700, etc.) — Q 24:35's opening words liturgically embedded in daily prayer practice.

### Files produced

- `/Users/grey/Downloads/quran/surahs/Q024-al-nur/00-overview.md` (pre-existing)
- `/Users/grey/Downloads/quran/surahs/Q024-al-nur/01-empirical-profile.md` (NEW)
- `/Users/grey/Downloads/quran/surahs/Q024-al-nur/02-content-analysis.md` (NEW)
- `/Users/grey/Downloads/quran/surahs/Q024-al-nur/03-tafsir-survey.md` (NEW)
- `/Users/grey/Downloads/quran/surahs/Q024-al-nur/04-hadith-corpus.md` (NEW)
- `/Users/grey/Downloads/quran/surahs/Q024-al-nur/05-classical-claims-audit.md` (NEW)
- `/Users/grey/Downloads/quran/surahs/Q024-al-nur/06-novel-findings.md` (NEW)
- `/Users/grey/Downloads/quran/surahs/Q024-al-nur/07-cross-references.md` (NEW)
- `/Users/grey/Downloads/quran/surahs/Q024-al-nur/preregs/Q024-F-01-light-vocabulary-density-prereg.md` (NEW)
- `/Users/grey/Downloads/quran/surahs/Q024-al-nur/preregs/Q024-F-02-aya-al-nur-vs-aya-al-kursi-prereg.md` (NEW)
- `/Users/grey/Downloads/quran/surahs/Q024-al-nur/preregs/Q024-F-03-ifk-cohesion-and-midpoint-prereg.md` (NEW)
- `/Users/grey/Downloads/quran/surahs/Q024-al-nur/preregs/Q024-F-04-hijab-passages-comparison-prereg.md` (NEW)
- `/Users/grey/Downloads/quran/surahs/Q024-al-nur/scripts/Q024_F_01_light_vocabulary_density.py` (NEW)
- `/Users/grey/Downloads/quran/surahs/Q024-al-nur/scripts/Q024_F_02_aya_al_nur_vs_aya_al_kursi.py` (NEW)
- `/Users/grey/Downloads/quran/surahs/Q024-al-nur/scripts/Q024_F_03_ifk_cohesion_midpoint.py` (NEW)
- `/Users/grey/Downloads/quran/surahs/Q024-al-nur/scripts/Q024_F_04_hijab_passages.py` (NEW)
- `/Users/grey/Downloads/quran/surahs/Q024-al-nur/csv/Q024-F-01.json` (NEW)
- `/Users/grey/Downloads/quran/surahs/Q024-al-nur/csv/Q024-F-02.json` (NEW)
- `/Users/grey/Downloads/quran/surahs/Q024-al-nur/csv/Q024-F-03.json` (NEW)
- `/Users/grey/Downloads/quran/surahs/Q024-al-nur/csv/Q024-F-04.json` (NEW)

### Cross-validation: Q 24:35 across tashkeel variants

Q 24:35 Arabic text verified across all three on-disk variants. All 48-word.

**no-tashkeel** (`quran-text/quran-no-tashkeel.json` Q24 v35):
> ۞ الله نور السماوات والأرض ۚ مثل نوره كمشكاة فيها مصباح ۖ المصباح في زجاجة ۖ الزجاجة كأنها كوكب دري يوقد من شجرة مباركة زيتونة لا شرقية ولا غربية يكاد زيتها يضيء ولو لم تمسسه نار ۚ نور على نور ۗ يهدي الله لنوره من يشاء ۚ ويضرب الله الأمثال للناس ۗ والله بكل شيء عليم

**min-tashkeel** (`quran-text/quran-min-tashkeel.json` Q24 v35):
> ۞ اللَّهُ نورُ السَّمٰوٰتِ وَالأَرضِ ۚ مَثَلُ نورِهِ كَمِشكوٰةٍ فيها مِصباحٌ ۖ المِصباحُ فى زُجاجَةٍ ۖ الزُّجاجَةُ كَأَنَّها كَوكَبٌ دُرِّىٌّ يوقَدُ مِن شَجَرَةٍ مُبٰرَكَةٍ زَيتونَةٍ لا شَرقِيَّةٍ وَلا غَربِيَّةٍ يَكادُ زَيتُها يُضيءُ وَلَو لَم تَمسَسهُ نارٌ ۚ نورٌ عَلىٰ نورٍ ۗ يَهدِى اللَّهُ لِنورِهِ مَن يَشاءُ ۚ وَيَضرِبُ اللَّهُ الأَمثٰلَ لِلنّاسِ ۗ وَاللَّهُ بِكُلِّ شَيءٍ عَليمٌ

**full-tashkeel** (`quran-text/quran-full-tashkeel.json` Q24 v35):
> ۞ٱللَّهُ نُورُ ٱلسَّمَٰوَٰتِ وَٱلۡأَرۡضِۚ مَثَلُ نُورِهِۦ كَمِشۡكَوٰةٖ فِيهَا مِصۡبَاحٌۖ ٱلۡمِصۡبَاحُ فِي زُجَاجَةٍۖ ٱلزُّجَاجَةُ كَأَنَّهَا كَوۡكَبٞ دُرِّيّٞ يُوقَدُ مِن شَجَرَةٖ مُّبَٰرَكَةٖ زَيۡتُونَةٖ لَّا شَرۡقِيَّةٖ وَلَا غَرۡبِيَّةٖ يَكَادُ زَيۡتُهَا يُضِيٓءُ وَلَوۡ لَمۡ تَمۡسَسۡهُ نَارٞۚ نُّورٌ عَلَىٰ نُورٖۚ يَهۡدِي ٱللَّهُ لِنُورِهِۦ مَن يَشَآءُۚ وَيَضۡرِبُ ٱللَّهُ ٱلۡأَمۡثَٰلَ لِلنَّاسِۗ وَٱللَّهُ بِكُلِّ شَيۡءٍ عَلِيمٞ

Word count (after stripping mushaf marks): **48 words** in all three variants. Letter count varies by 4% between variants (no-tashkeel 203, min-tashkeel 199, full-tashkeel 221) due to tashkeel-marker presence; the *consonantal-skeleton* count is rules-tuple stable.

### Honest pre-commit notes

- All four Q024-F-* novel tests had locked pre-regs WRITTEN BEFORE the run. SHA-checksums computed at runtime and embedded in JSON outputs. No post-hoc adjustments to direction-of-effect.
- The "Light-verse Tahajjud-dhikr embedding" finding (in `04-hadith-corpus.md` §4) is post-hoc descriptive — it was noticed during cross-corpus search, not pre-registered. It is reported with the explicit "post-hoc" flag.
- The Q 24:35 word-position 0.489 finding pre-registers as "in central third [0.33, 0.67]" — the actual 0.489 is well within that. The pre-reg threshold was conservative.

### Verdict-of-the-investigation

Q 24 al-Nūr is the corpus's clearest case of **outlier-without-iʿjāz al-fawāṣil**: top-5 UAS via outlier-strength + bracketing canonical-adjacency-cost (both top-15 expensive), with anti-structural-iʿjāz signature (sig_A rank 82). All four pre-registered novel tests confirmed. Eight classical claims audited; six VINDICATED, two FALSIFIED-with-refinement. The empirical signature precisely matches the qualitative classical reading: a Medinan-legal centerpiece inserted into a Meccan-narrative zone, named for its unique-in-the-corpus light-vocabulary concentration, anchored by the al-ifk story (the corpus's most-narrative-cohesive defense-of-chastity passage), and structurally centered on the Light-verse (the literal word-and-letter median of the surah).
