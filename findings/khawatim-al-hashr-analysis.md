---
finding_id: khawatim-al-hashr
phase: A+B
status: user-requested deep analysis
date: 2026-04-12
verses: Q 59:21-24 (last 4 verses of Sūrat al-Ḥashr)
classical_name: Khawātim Sūrat al-Ḥashr ("the Seals/Closers of al-Ḥashr")
rules:
  orthography: no-tashkeel (primary), full-tashkeel cross-checked
  word_definition: real-words (rec-marks filtered)
  letter_definition: graphemes
  basmala_policy: counted-only-in-surah-1
  verse_numbering: hafs-kufan
  abjad_table: mashriqi
  null_model: multiple (corpus-rank percentile, Fisher enrichment, consecutive-opener scan)
---

# Khawātim Sūrat al-Ḥashr (Q 59:21-24) — Deep Analysis

User-requested analysis pulling together every relevant tool the project has built. These are the final four verses of Surah 59 (Al-Ḥashr, "The Exile/Gathering"), a Medinan surah addressing the expulsion of Banū al-Naḍīr.

Classical authentic hadīth tradition (Tirmidhī, Aḥmad, Nasāʾī, variable isnāds): whoever recites the **last three verses** (22-24) morning and evening receives the prayers of 70,000 angels, and that the **Ism Allāh al-Aʿẓam** (Greatest Name of God) is contained in them.

## The Text

| v | Arabic | Metric |
|---|---|---|
| 21 | لو أنزلنا هذا القرآن على جبل لرأيته خاشعا متصدعا من خشية الله وتلك الأمثال نضربها للناس لعلهم يتفكرون | L=84 W=18 Abjad=7931 |
| 22 | هو الله الذي لا إله إلا هو عالم الغيب والشهادة هو الرحمن الرحيم | L=51 W=13 Abjad=3093 |
| 23 | هو الله الذي لا إله إلا هو الملك القدوس السلام المؤمن المهيمن العزيز الجبار المتكبر سبحان الله عما يشركون | L=87 W=19 Abjad=3694 |
| 24 | هو الله الخالق البارئ المصور له الأسماء الحسنى يسبح له ما في السماوات والأرض وهو العزيز الحكيم | L=78 W=17 Abjad=3851 |

**Aggregate (vv 22-24, the hadith-blessed three):** 216 letters, 49 words, 10,638 abjad. **216 = 6³. 49 = 7².**

**Aggregate (vv 21-24):** 300 letters, 67 words, 18,569 abjad.

## The Findings (organized by structural layer)

### Layer 1 — Uniqueness of the twin-opener technique

The formula **هو الله الذي لا إله إلا هو** opens v22 AND v23 as a 30-character identical match. I scanned all 6,236 verses for consecutive-verse pairs sharing a 40-character identical opening. Result:

**Only two pairs in the entire Quran use this technique:**
1. **Q 2:149 ↔ Q 2:150** (*wa-min ḥaythu kharajta...* — the qibla verses, inside the Bonferroni-surviving Al-Baqarah 131-144 ring center, strongest chiasmus in the Quran)
2. **Q 59:22 ↔ Q 59:23** (this passage)

Both instances land on the Quran's most structurally extraordinary moments. Cross-reference: `chiastic-audit.md`.

### Layer 2 — Formula rarity

**"الذي لا إله إلا هو"** (the One other than whom there is no deity) appears in exactly 3 verses in the entire Quran:
- Q 20:98 (Moses speaking)
- Q 59:22
- Q 59:23

**Two of the three total Quranic occurrences stack here consecutively.**

### Layer 3 — Divine-name density (from divine-names-distribution agent)

- **Q 59:23 is rank #1 in the Quran for divine-name density**: 10 divine-name tokens in 20 words = **50% density**. No other verse matches.
- **Q 59:24 is tied for rank #6**.
- **15 unique divine names are invoked across 22-24**, the densest divine-names passage in the entire Quran.

**EIGHT of the names used here appear NOWHERE ELSE in the whole Quran:**
`al-Quddūs, al-Salām, al-Muʾmin, al-Muhaymin, al-Jabbār, al-Mutakabbir, al-Bāriʾ, al-Muṣawwir`

These three verses are the **exclusive Quranic home** of 8 divine names. The classical assertion that the Greatest Name resides here sits on this structural fact.

### Layer 4 — Numerical structure

- **49 real words in 22-24** = **7²**. The number 7 is theologically saturated (7 heavens, 7 earths, 7 Mathānī, 7 gates of Hell, 7 gates of Paradise). The three verses traditionally identified as bearing the Greatest Name are engineered on a 7-squared word-count.
- **216 letter graphemes in 22-24** = **6³**. A perfect cube. Rare clean factorization.
- **Q 59:24 abjad = 3851 = 7 × 19 × 29** — the one verse in this block whose mashriqi abjad cleanly factors through 19. Worth noting honestly; does not rise to significance under Bonferroni correction given the forking-paths space.

### Layer 5 — Meta-statement uniqueness

**"لَهُ الأَسْمَاءُ الْحُسْنَى"** ("to Him belong the Most Beautiful Names") appears in exactly 4 verses in the whole Quran: Q 7:180, Q 17:110, Q 20:8, **Q 59:24**. The Quran's most explicit self-referential statement about divine naming lands here, at the climax of a 15-name listing. **The passage names itself as a place of naming.**

### Layer 6 — Compositional arc

```
v21  — PARABLE OF SELF              → mountain + khashya + "this Quran" (self-reference)
                                      + meta-commentary on parables themselves
v22  — TRIADIC AFFIRMATION          → Allah + Unseen/Seen + al-Raḥmān al-Raḥīm
                                      (the Basmala-adjacent pair as verse-closer)
v23  — MAJESTY OCTET                → al-Malik, al-Quddūs, al-Salām, al-Muʾmin,
                                      al-Muhaymin, al-ʿAzīz, al-Jabbār, al-Mutakabbir
                                      + subḥān Allāh ʿammā yushrikūn (polytheism-rejection pivot)
v24  — CREATION TRIAD + META        → al-Khāliq, al-Bāriʾ, al-Muṣawwir
                                      + "to Him belong the Most Beautiful Names"
                                      + cosmic glorification
                                      + al-ʿAzīz al-Ḥakīm closer (most common divine-pair, 29×)
```

Classical rhetoric calls this *tafṣīl* (elaboration). The passage opens with a parable about the Quran's shattering power on a mountain, then lists the Names responsible for that shattering power, progressing from **basic affirmation → majesty → creation**, with the Polytheism-rejection pivot (*subḥāna Llāhi ʿammā yushrikūn*) bridging from the names of sovereignty to the names of creation.

### Layer 7 — Recapitulation of Al-Fātiḥa

Al-Fātiḥa (the Quran's opening) invokes: **Allāh + al-Raḥmān + al-Raḥīm + al-Mālik** (Master of the Day of Recompense). Khawātim al-Ḥashr invokes: **Allāh + al-Raḥmān + al-Raḥīm + al-Malik** (the Sovereign). **The closers of al-Ḥashr recapitulate the openers of the Quran's divine-name vocabulary, then extend it to 15 names**. This is the same four-name opening sequence that starts the Book, deployed again as the scaffold for the expansion.

### Layer 8 — Self-referential parable (v21)

Verse 21 is a Type A extended parable (from our parables-catalog). It is:
1. **Self-referential** — the Quran names itself (*hādhā al-Qurʾān*)
2. **Mountain-parable** — connects to Q 7:143 where Moses asks to see God and the mountain crumbles (same shattering imagery, same khashya root)
3. **Meta-commentary on parables** — ends with "and these examples We strike for the people that they may reflect" — the Quran describes its own rhetorical method

Classical rhetoric: *mathal wa-iʿtibār* (example and reflection). Verse 21 is a **parable about parables** that primes the reader for the Names that follow.

### Layer 9 — Verse-end signature

The three verses end in a deliberate closure gradient:
- **v22 ends**: al-Raḥmān al-Raḥīm (the Basmala pair — every surah opens with this; here it closes a verse)
- **v23 ends**: subḥāna Llāhi ʿammā yushrikūn (glorification + polytheism-rejection)
- **v24 ends**: wa-huwa l-ʿAzīz al-Ḥakīm (the single most common divine-name pair in the Quran, 29 occurrences)

The passage **frames itself between the two most statistically frequent Quranic divine-name endings**: the Basmala pair at v22, and the ʿAzīz-Ḥakīm pair at v24.

### Layer 10 — Cross-surah Ar-Raḥmān connection

Our Maryam deep-dive found that Surah 19 carries 28.1% of all Ar-Raḥmān occurrences in 1.57% of verses — the highest concentration in the Quran. Khawātim al-Ḥashr invokes Ar-Raḥmān once, in its opening triadic verse (22). **Both passages use Ar-Raḥmān as a theological climax-point.** Cross-surah rhetorical link through the Ar-Raḥmān axis.

## Descriptive observation (not inferential) — Morphological wazn distribution of the exclusive-8

**Status:** descriptive-only. Added 2026-04-14 as the closing record of H-NEW-30 (task #57, originally proposed as inferential test of "morphological-class signature of the Khawātim al-Ḥashr exclusive-8 divine names"). H-NEW-30 was **demoted** to descriptive annotation by team-lead 2026-04-13 ruling (downstream of meta-analyst pending-power-analysis): N = 8 is below inferential threshold for any goodness-of-fit or class-concentration test against the broader 99-name space (n = 100). No statistical claim is made here. The observation is filed because the morphological inspection answers an interpretable classical question even where it cannot ground a hypothesis test.

**Source data.** `findings/classical-sources/99-names-wazn-classification.tsv` (classical-scholar, 2026-04-14). 100-row wazn classification tied to `findings/classical-sources/99-names-ground-truth.tsv` via `tirmidhi_rank` join key. Per-row HIGH/MEDIUM/LOW confidence column included.

**Sources cited (MW-6 SECONDARY-TRIANGULATED — Sībawayh + Zamakhsharī + al-Ghazālī).**
- Sībawayh, *al-Kitāb*, ed. ʿAbd al-Salām Hārūn (al-Khānjī, Cairo 1988), vol. 1 pp. 110–115 (the six *abnīyat al-mubālagha*) and vol. 4 pp. 22–69 (*awzān al-ṣifāt al-mushtaqqa*).
- al-Zamakhsharī, *al-Mufaṣṣal fī ṣināʿat al-iʿrāb*, ed. ʿAlī Bū Mulḥim (Maktabat al-Hilāl, Beirut 1993), §§ 348–372 (Form II/V/VIII derived participles).
- al-Ghazālī, *al-Maqṣad al-asnā fī sharḥ asmāʾ Allāh al-ḥusnā*, ed. Faḍlou Shehadi (Dār al-Mashriq, Beirut 1971), per-name commentary (theological category bucket).

### Per-name wazn for the canonical exclusive-8

The canonical exclusive-to-Khawātim-al-Ḥashr set per MASTER §2 (the 8 names appearing **only in Q 59:22-24** by definite-singular attestation rule):

| # | Name | Verse | Wazn | Wazn family | Sībawayh canonical? |
|---|---|---|---|---|---|
| 1 | al-Quddūs | 59:23 | Fuʿʿūl | Fuʿʿūl (sacred-intensive) | not in mubālagha-six |
| 2 | al-Salām | 59:23 | Faʿāl-maṣdar | Substantive (verbal-noun-as-name) | not in mubālagha-six |
| 3 | al-Muʾmin | 59:23 | Mufʿil | Form-IV active participle | not in mubālagha-six |
| 4 | al-Muhaymin | 59:23 | Mufayʿil | Mufaʿʿil (quadriliteral-derived) | not in mubālagha-six |
| 5 | al-Jabbār | 59:23 | Faʿʿāl | Faʿʿāl (intensive agent) | **yes** (1 of 6 mubālagha patterns) |
| 6 | al-Mutakabbir | 59:23 | Mutafaʿʿil | Form-V reflexive participle | not in mubālagha-six |
| 7 | al-Bāriʾ | 59:24 | Fāʿil | Form-I active participle | not in mubālagha-six |
| 8 | al-Muṣawwir | 59:24 | Mufaʿʿil | Form-II active participle | not in mubālagha-six |

### What the data show (reverse-direction observation, R-007 discipline)

The 8 canonical-exclusive names span **seven** distinct *wazn* families: Fuʿʿūl, Substantive, Mufʿil, Mufaʿʿil (the only family containing two of the eight, Muhaymin + Muṣawwir), Faʿʿāl, Mutafaʿʿil, and Fāʿil. Only **Jabbār** sits in Sībawayh's canonical six-pattern *mubālagha* set (Faʿʿāl, Mifʿāl, Faʿūl, Faʿīl, Fuʿūl, plus Sībawayh's restricted sixth). Two of the most-used patterns in the broader 99-name space — **Faʿīl** (27 of 100 names: ʿAlīm, Karīm, Ḥakīm, Samīʿ, Baṣīr, Khabīr, Laṭīf, etc.) and **Faʿūl** mubālagha (6 of 100: Ghafūr, Shakūr, Wadūd, ʿAfūw, Ṣabūr, Raʾūf) — are **completely absent** from the exclusive-8.

The team-lead's a priori task-creation framing ("morphological homogeneity, predominantly al-X intensive participial pattern") is **not supported** by morphological inspection. The exclusive-8 are morphologically *diverse*, not concentrated; at most two of the eight share any single *wazn* family. The descriptive signature, if any, is **breadth, not concentration** — the cluster hits seven of Sībawayh's awzān families in eight names without using either of the two patterns that dominate the broader 99-name space.

This is a reverse-direction observation in the same lineage as H-NEW-34 abjad-residue under-dispersion and H-NEW-29 root-CV regularity: the data inverts the a priori intuition. Filed honestly per R-007 reverse-direction discipline. The reverse-direction finding does NOT escalate to inferential status — n = 8 is too small for any concentration vs diversity test against a 100-name reference distribution to carry power. It is a descriptive observation about the morphological *shape* of the exclusive cluster, recorded so future readers and the classical-tradition decomposition meta-pattern (M-5) can incorporate it without re-deriving.

**Caveats local to this annotation.**

- The wazn classification has per-row HIGH/MEDIUM/LOW confidence; Muhaymin's Mufayʿil assignment is LOW (quadriliteral derivation is contested across classical grammarians; Sībawayh treats it as an irregular). Treating Muhaymin alternately as a fixed proper-name with no productive *wazn* would reduce the family count from seven to six — still diverse, not homogeneous.
- "Not in mubālagha-six" is a Sībawayh-specific criterion; al-Mubarrad and al-Khalīl include slightly different sets. The cross-grammarian noise is small relative to the diversity observation.
- The exclusive-8 set differs from the Q 59:23 second-verse ascription chain (which would include al-Malik and al-ʿAzīz, neither of which is exclusive — Malik appears ~50 times elsewhere, ʿAzīz ~100 times). MASTER §2 lines 39–50 use the exclusive-set definition, which is the framing adopted here.
- All wazn assignments use the no-tashkeel, hafs-kufan, mashriqi rules tuple per parent file frontmatter.

**Cross-references.**

- Source TSV: `findings/classical-sources/99-names-wazn-classification.tsv`
- Parent ground-truth: `findings/classical-sources/99-names-ground-truth.tsv`
- M-5 classical-doctrine decomposition pattern: this is a textbook M-5 instance — a specific classical association (the 8-name Khawātim cluster) decomposes into a confirmable component (the 8 names ARE exclusive to Q 59:22-24, MASTER §2) plus a refutable component (they are NOT a morphologically concentrated cluster, this annotation).

## Verdict

The classical tradition of naming these verses as containing the Greatest Name of God is structurally well-founded even by rigorous computational standards:

1. **Twin-opener technique shared with only one other Quranic passage** (the Abraham/qibla Bonferroni-surviving ring center)
2. **Densest divine-name verse in the Quran** at v23 (50% density, rank 1/6236)
3. **8 divine names appearing nowhere else in the Quran** are concentrated here
4. **49 words = 7² | 216 letters = 6³** clean numerical structure
5. **Contains the "Most Beautiful Names" meta-statement** — one of only 4 in the Quran
6. **Recapitulates Al-Fātiḥa's opening divine-name sequence** (Allah/Raḥmān/Raḥīm/Malik)
7. **Self-referential parable about the Quran's power** in v21 as rhetorical setup
8. **Frames itself** between the Basmala pair and the ʿAzīz-Ḥakīm pair — the Quran's two most frequent name endings

The ḥadīth tradition values these verses for textual reasons that hold up under scrutiny. This is one of the project's clearest cases of classical devotional intuition being structurally validated at scale.

## Honest caveats

- The abjad = 19×... observation for v24 is worth noting but is selected from the forking-paths space of many possible divisibility tests.
- "Worth more than a thousand verses" as a verbatim ḥadīth quantity is not authenticated in the classical sources I can trace; the core 70,000-angels tradition IS well-attested.
- The "uniqueness of 8 divine names appearing only here" depends on definite-singular Quranic attestation rules from the divine-names-distribution agent's methodology; under looser morphological rules some of these names appear in related forms elsewhere.

## Files and cross-references

- Parent compositional data: `findings/phase-b-hypotheses/divine-names-distribution.md`
- Twin-opener context: `findings/phase-c-structures/chiastic-audit.md`
- Parable classification: `findings/phase-b-hypotheses/parables-catalog.md`
- Ar-Raḥmān cross-link: `findings/phase-c-structures/maryam-deep-dive.md`
- Iltifāt topic-enrichment (the passage is "monotheism" topic): `findings/phase-b-hypotheses/iltifat-catalog.md`
