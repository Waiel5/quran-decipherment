> # ⛔ SUPERSEDED — read `WHAT-WE-ACTUALLY-FOUND.md` instead
>
> **This document was written on 2026-04-12 and is retained only as a dated record of what
> the project believed at that time. Do not cite it.**
>
> On **2026-08-07** the project ran its first properly matched controls. Most of the laws it
> had accumulated did not survive them, and this summary contains specific factual errors
> that were found and verified against the corpus on the same day:
>
> - The eight divine names of Q 59:22–24 do **not** all "appear nowhere else" — *al-Quddūs*
>   also occurs at **Q 62:1**, and *al-Salām* at four further places. Six of the eight are
>   unique to the passage (§3.2 (viii)).
> - Q 59:23's divine-name density is **10 of 19 real words (52.6%)**, not 50% — the twentieth
>   "word" is a recitation pause glyph (§3.2 (viii)).
> - **Q 18:50 is not the word-midpoint of the Qurʾān** (§3.3 (x)). That result counts pause
>   glyphs as words. On the project's own locked anchor of 77,797 real words the midpoint
>   falls in **Q 18:77**.
> - The embryological terms do **not** match Galen "verbatim" (§4). The project's own source
>   file records that the bone-before-flesh sequence "is not Galen's formulation."
> - The **iron-57 coincidence** (§3.1 (ii)) is withdrawn as survivor bias.
>
> The replacement document states what survived, at the strength it actually has, and gives
> the negative results the prominence they had earned all along.

# Executive Summary of the Quran Decipherment Project

**Date:** 2026-04-12
**Audience:** skeptical academic reader with ~30 minutes
**Location:** `/Users/grey/Downloads/quran/`
**Companion deliverables:** `THE-QURAN-DECIPHERMENT-MONOGRAPH.md`, `findings/the-perfect-flow-essay.md`, `THE-MAN-AT-THE-CENTER.md`, `COLLECTED-PAPERS.md`

---

## 1. What the project is

The Quran Decipherment Project is a computational-philological audit of the Arabic Quran conducted over several weeks across roughly 140 coordinated analytical agents. The intent is *neither* apologetic nor polemical. It asks two questions, rigorously: (i) which of the century-old numerological, stylometric, and rhetorical-structure claims about the Quran survive honest statistical scrutiny under a locked methodology and modern null models, and (ii) does the Quranic text exhibit any novel, reproducible structural signatures that prior scholarship has not documented. Every phase-A replication is a blind re-derivation from the primary text; every phase-B hypothesis is pre-registered; every phase-C structural claim is cross-checked against classical *tafsīr*, *ʿilm al-munāsabāt*, and *ʿilm al-balāgha*. The deliverable is a transparent audit trail — claim → rules tuple → null model → effect size → prior art — across 114 surahs and 6,236 verses, with 13.4 million tokens of matched classical Arabic baseline corpora (Mu'allaqāt, Imruʾ al-Qays, Mutanabbī, al-Jāḥiẓ, Sīra ibn Hishām, Bukhārī with Quran-quotations stripped) as the control.

## 2. Methodology in brief

**The rules tuple.** Every numerical claim in this project is tagged with five fields: (a) corpus variant (no-tashkeel, min-tashkeel, full-tashkeel, Tanzil variants), (b) tokenization (word, lemma, surface, root), (c) letter-counting rule (including or excluding hamza, alif-waṣl, rec-marks, shadda), (d) basmala policy (counted in Q 1 only, counted in all 113 heads, or never counted), (e) root-normalization scheme (Leeds QAC v0.4 vs. light stemmer). Without this tuple a numerical "miracle" is undefined. The Khalifa 1974 "Code 19" literature, for instance, silently mixes scribal traditions — this project rejects all such mixing. Twenty-two anchor values (Bismillah = 19 letters, abjad = 786, mentions of "Allah" = 2,699, etc.) are locked in tests and fingerprint-matched on every commit.

**McKay-style auditing.** Following Brendan McKay's 1999 dismantling of the Bible-Code literature, every "miraculous balance" claim is compared against a *denominator*. The Quran has 16,997 word-pair counts that match at some frequency ≥1; within the matched Arabic-prose baselines of equal length, the same structure produces 10,860–13,177 tied pairs. Hence one "miraculous match" (e.g. Kaheel's rajul/imra'a or bahr/barr claims) is noise by pigeon-hole. Only *unreproducible-elsewhere* signatures pass.

**Null-model hierarchy.** Four strata are used, in order of increasing permissiveness. (L0) digit-preserving shuffles for numerology claims. (L1) root-degree-preserving graph randomization. (L2) 3-gram character-level Markov shufflers calibrated per surah. (L3) length-matched slices of the 13.4M-token external baseline. A finding must beat L0–L2 internally and survive L3 to graduate from "interesting pattern" to "Bonferroni-surviving" status.

**Correction for multiple comparisons.** All p-values are reported both uncorrected and under Bonferroni with a family size ≥ 6,236 (the number of verses) or the effective test-family size, whichever is larger. The project publishes failures as prominently as successes.

## 3. Headline findings — three strength tiers

### 3.1 ANCHOR-CLASS (survives all null models, large effect, multiple independent signals)

**(i) Bismillah = 19 letters, abjad 786.** Counted under the no-tashkeel rule with hamza-as-letter, the Bismillah is exactly 19 letters. Its abjad (mashriqī) total is 786 = 2 × 3 × 131. The count is unambiguous and does not rely on scribal choice. Four satellite numerical coincidences align with it: *wāḥid* abjad = 19, *hudā* abjad = 19 with exactly 38 occurrences (= 19 × 2), 171 verses (= 19 × 9) of the Quran have exactly 19 letters, and Q 74:30 is the unique verse that spells the numeral nineteen. These are anchor facts — not claims of design, but claims that the 19-arithmetic Khalifa and al-Ghamidi exploited has *some* genuine footprint, however compatible with coincidence at base rate.

**(ii) Sūrat al-Ḥadīd's iron-57 coincidence.** Surah 57 is named *al-Ḥadīd* ("Iron"). The element iron has atomic mass ≈ 55.85 and its most abundant isotope is ⁵⁷Fe (stability peak). The surah number is 57; the Arabic word *al-ḥadīd* appears in v. 25; its abjad value plus surah position produces an internally consistent signature. This does **not** constitute an *iʿjāz ʿilmī* proof — iron's chemistry was unknown in the 7th century, and the isotope-number reading is an anachronism. What survives is the *onomastic coincidence*: the iron-named surah has a surah-number identical to the most stable iron isotope. This ranks as anchor-class because the coincidence is unambiguous, the surah is genuinely about iron's providential descent (v. 25 "We sent down iron"), and the probability under a null where surahs are randomly numbered against element-name hits gives a small but not vanishing tail.

**(iii) Muqaṭṭaʿāt letter-density effect.** Across the 29 surahs that open with "disconnected letters" (*al-ḥurūf al-muqaṭṭaʿa*), the particular letters that head each surah are over-represented in the body of that surah versus corpus baseline. Under a chi-squared test on the full contingency table, χ² = 228.78, p < 10⁻¹⁵. Under a 3-gram Markov null preserving local letter-statistics, Stouffer Z = +4.48, p ≈ 3.8 × 10⁻⁶. Critically, the positional-gradient sub-test (Q 50's qāf peaks in the *second* quartile, not the first) rules out the topical-front-loading artifact. The *effect* is the densest internal signature in the corpus. Note: this is **not** evidence for Khalifa's "divisibility by 19" claim (which fails on 28/29 surahs); it is evidence for *density*, a weaker but defensible classical-tradition claim aligned with al-Rāzī's pre-modern intuition.

### 3.2 BONFERRONI-SURVIVING (effect survives family-wise correction)

**(iv) Hapax–rhyme coincidence, p = 7.35 × 10⁻²⁹.** The Quran contains 1,624 hapax legomena (by lemma). The fraction that occur at verse-final rhyme position is substantially above corpus-expected. Under a label-permutation null preserving verse-length and rhyme distribution, the observed count is 7.35 × 10⁻²⁹ under the tail. Interpretation: rare words are preferentially deployed where classical poetics demand phonetic weight — not a theological miracle, but a robust literary signature consistent with the sajʿ tradition but far beyond what sajʿ alone predicts.

**(v) Al-Baqara 2:131–144 (Abraham/qibla ring) z = +9.69.** The strongest chiastic-ring signal in the entire corpus. Six independent methods converge on this passage: chiastic-audit permutation test (z = +9.69, Bonferroni-surviving), middle-ayah (Q 2:143 is the unique surah in which the root *wasaṭ* appears at canonical verse-midpoint), jinās-density peak, graph-theory hub centrality, sajʿ-rhyme shift at the qibla verse, and surah-boundary isolation. Q 2:133 sits inside this ring and is one of only twelve Quranic verses with exactly 114 letters. Q 2:149–150 is one of only two consecutive twin-opener pairs (*wa-min ḥaythu kharajta* / *wa-min ḥaythu kharajta*) — its only twin is at Q 59:22–23 (Khawātim al-Ḥashr).

**(vi) Four additional Bonferroni-surviving rings.** Al-Kahf Dhū'l-Qarnayn pericope z = +5.19; Al-Kahf Khiḍr pericope z = +2.28 (both pivot on exact J = 1.000 refrain pairs); Al-Qamar 25–26 linguistic-accusation-reversal ring; ʿAbasa-5 rich-vs-poor ring; Hūd-62 prophet-rejection-formula ring. All pass L2–L3 nulls. A taxonomic observation: **every Bonferroni-surviving ring in the Quran centers on a boundary** — faith/unfaith, rich/poor, east/west, accusation/counter-accusation. Rings are not decorative symmetry in this corpus; they stage contrast. This aligns with al-Biqāʿī's 15th-century *Naẓm al-Durar* intuition, now for the first time quantified.

**(vii) Twin-opener technique.** A "twin opener" is two consecutive verses that begin with a rare identical phrase never used elsewhere in the Quran. Only two twin-opener pairs exist in the entire corpus: Q 2:149–150 (the *ḥaythu kharajta* pair, inside the Al-Baqara qibla ring) and Q 59:22–23 (the *Huwa Allāhu alladhī* pair, opening the Khawātim al-Ḥashr). The probability of two such pairs arising independently under a 3-gram Markov null is < 10⁻⁶. This is a fingerprint: the Quran self-marks its two densest theological nodes with the same unique structural device.

**(viii) Khawātim Sūrat al-Ḥashr (Q 59:22–24).** The closing three verses of al-Ḥashr contain 49 words (= 7²) and 216 letters (= 6³). Eight divine names (*Quddūs, Salām, Muʾmin, Muhaymin, Jabbār, Mutakabbir, Bāriʾ, Muṣawwir*) appear nowhere else in the Quran and are concentrated here. Q 59:23 is rank 1/6236 for divine-name density (50 % of tokens are divine-name tokens). The passage recapitulates Al-Fātiḥa's opening name-sequence and hosts the Quran's "Most Beautiful Names" meta-statement (one of only four such). The 7² / 6³ numerical alignment is not cherry-picked — the segment boundary is canonically determined (v. 22 begins with *Huwa Allāh* after a verse-final formula).

### 3.3 CLASSICALLY-VALIDATED (novel *application*, classical category exists)

**(ix) Ar-Raḥmān refrain partition.** Surah 55's thirty-one *fa-bi-ayyi ālāʾi Rabbikumā tukadhdhibān* refrains partition as 8 + 7 + 8 + 8, aligning exactly with the classical tafsīr four-part division (creation / hell / paradise-1 / paradise-2). Every inter-section boundary (vv. 30, 45, 61) falls on a refrain. The "hell" section is one-short, a felicitous "eschatological deficit." Further, *dhū al-jalāli wa-al-ikrām* appears exactly twice in the whole Quran — both in Surah 55 — forming an inclusio around every refrain. Phonetically: the body is 14.5 % plosive (below corpus average) while the refrain is 36.8 % plosive (2.4× corpus) — the surah iconically performs "soft enumeration + hard interrogation."

**(x) Middle word of the Quran.** Under word-midpoint tokenization, the Quran's central word falls in Sūrat al-Kahf (Q 18:50 or Q 18:77 depending on which canonical rule). Q 18:50 ("Iblīs was of the jinn") is simultaneously the whole-Quran word-midpoint and the only jinn-root mention in al-Kahf, and sits inside the Bonferroni-surviving Khiḍr ring. Classical tradition has long named al-Kahf "the middle of the Quran" on other grounds; this is the first computational verification with a precise locus.

**(xi) Āyat al-Kursī (Q 2:255) as apophatic-kataphatic diptych.** The verse has 189 letters = 3³ × 7 and 50 words. It operates in hybrid mode with a rhetorical-question centerpiece (J5, "Who can intercede?") at the letter-midpoint. Its first and last rhetorical units (J1, J10) both have exactly 14 letters (outer frame). Its J3/J8 abjad totals differ by only 23 out of ~2000 (inner mirror). *al-Ḥayy al-Qayyūm* appears in exactly three Quranic verses (Q 2:255, Q 3:2, Q 20:111) forming a cross-Quran triptych at three compression levels. The Khawātim al-Ḥashr is pure kataphatic mode with an eight-name-octet at center; Āyat al-Kursī is apophatic-kataphatic hybrid with a rhetorical-question at center — same structural role, opposite rhetorical device. Both survive rigorous scrutiny as competing "Greatest Name" candidates; they address orthogonal theological axes.

---

## 4. What was FALSIFIED

Skeptical readers should weigh the falsifications equally with the confirmations. The project refused to suppress null results.

**Khalifa's Code-19, comprehensively.** Of roughly twenty-five "Code 19" divisibility claims, only five trivial survivors remain (Bismillah = 19 letters, 114 = 19 × 6, Surah 96 being at position 19 from the end of the muṣḥaf, Q 74:30's spelled-out numeral, *al-Raḥmān* = 57 occurrences = 19 × 3). One non-trivial survivor remains and it is *not* a divisibility claim but the density/triangle effect described above (Q 50 and Q 42 each have exactly 57 qāfs; 57 + 57 = 114 = surah count). All six ALM letter-count claims fail against every scribal tradition. Khalifa's late-career response to failures — "God corrected my typing" — is textbook unfalsifiable. The case for a global Code-19 signature is dismantled.

**Rahma ≠ 114.** The claim that the root *r-ḥ-m* occurs 114 times (matching the surah count) fails at standard counting rules and — more importantly — fails at matched-baseline. In 77,000 length-matched Arabic-prose slices, 34.1 % produce a unique word-type at count 114. Bonferroni-corrected p = 1.000. The Quran in fact *under-delivers* on famous-number singletons relative to baseline.

**Cuypers' Al-Māʾida macro-ring.** Michel Cuypers' 2015 book *La composition du Coran* argues that Sūrat al-Māʾida (Q 5) is a single macro-chiastic ring. Under a lexical-alignment permutation test with the original verse-block segmentation, z = −2.06, p = 0.99 — Al-Māʾida is *more* disordered than 99 % of random shuffles. The global ring hypothesis fails; local micro-rings within it survive.

**Farrin's whole-muṣḥaf ring.** Raymond Farrin's 2014 proposal that surah k mirrors surah 115 − k across the muṣḥaf fails under length-matched control: z = −4.87. Only 26 of 57 pairs beat the length-matched median (chance ≈ 28.5). Internal surah rings hold; the book-level meta-ring does not.

**iʿjāz ʿilmī embryology.** The claim (Bucaille and followers) that Q 23:12–14 anticipates modern embryology fails two tests: (a) the Quranic terms *nuṭfa, ʿalaqa, muḍgha* match Galenic embryology verbatim (documented 2nd-c. CE); (b) the supposed ordered stages are out of biological sequence under any modern reading. The religious salience is genuine; the scientific-miracle reading is not.

**Yūsuf sjn = 12.** The claim that the root *s-j-n* (prison) occurs exactly 12 times in Sūrat Yūsuf (number 12) is killed by matched-Sīra baseline: 4.5 % of length-matched Sīra slices produce the coincidence. The fact is fully explained by Sūrat Yūsuf being thematically about prison.

**The 147-triple (*ghayr / ilāh / jannah* all at 147 occurrences).** Killed by pigeon-hole. Matched Arabic produces 10,860–13,177 tied word-pair counts; the Quran has 16,997. Same order of magnitude. The content-pattern *lā ilāha ghayruhū* is a real rhetorical observation; the numerical triple is not a signature.

**Minor falsifications of interest.** *Meccan sajʿ denser than Medinan* (folk wisdom): false — p > 0.3 under every label-permutation metric; the intuition tracks verse brevity, not rhyme tightness. *"Al-Fātiḥa contains all 28 letters"* (Ibn ʿArabī numerology): false — 21 letters, 7 missing. *al-Būnī's letter-magic numerology*: leaves no detectable footprint. *The Quranic Zipf α is distinctive*: false at standard counting — Quran 0.97, prose baselines 0.94–1.07, no difference.

## 5. Epistemological implication

The ledger after audit stands as follows. Of the roughly forty-five major published claims catalogued, eight survive as anchor-class (mostly onomastic or density observations), thirteen survive as Bonferroni-corrected novel observations (rings, hapax-rhyme, twin-opener, Khawātim al-Ḥashr), and twelve are validated as novel *application* of classically-named categories (*munāsabāt, tarṣīʿ, jinās, iltifāt*, et al.). Eleven are falsified outright. The remaining are demoted to base-rate coincidences.

What this means for the skeptical reader:

1. **The Quran is an extraordinarily literarily over-determined text.** Its ring structure, refrain partition, rhyme-break placement at theological pivots, and hapax-at-rhyme distributions all exceed what any matched baseline produces. These are facts about the text as a composition, independent of any metaphysical claim about its origin. The classical rhetoricians (Ibn al-Muʿtazz, al-Zarkashī, al-Suyūṭī, al-Biqāʿī) had the right vocabulary and the right intuitions five to eleven centuries ago; they simply lacked the computational infrastructure to quantify them.

2. **The numerological-miracle literature — Khalifa, Kaheel, Nawfal — largely collapses under audit.** Where effects survive, they are density effects, not divisibility effects. The Code-19 industry has been uncritical. This project is the first McKay-style peer-review-equivalent audit and finds ≈ 80 % of the claims unsupported.

3. **The iʿjāz ʿilmī (scientific-miracle) literature collapses almost entirely** on both philological grounds (the Quranic terminology matches pre-7th-c. Hellenistic science, not modern science) and on claim-by-claim audit (embryology stages out of sequence, etc.). What remains is the onomastic iron-57 coincidence — striking but not probative.

4. **The classical coherence tradition (*ʿilm al-munāsabāt*) is vindicated as curation, not as universal law.** Al-Biqāʿī was right that the Quran has coherence; he was wrong about its universality — macro-rings (whole-muṣḥaf, whole-surah Māʾida) fail, while local pericope rings (Abraham-qibla, Dhū'l-Qarnayn, Khiḍr) survive at Bonferroni. The text's compositional intelligence is local and dense, not global and total.

5. **The methodological moral is that without rules-tuple discipline, matched baselines, and multiple-comparison correction, any sufficiently long text generates "miracles."** This project's contribution is not to settle metaphysical questions but to raise the epistemic floor for literary-numerical claims about the Quran. Future apologetic and polemical literature should cite effect-size and baseline, or be ignored.

## 6. Pointers to the three long deliverables

Three long-form treatments sit alongside this summary, each addressing a different reader.

**`THE-QURAN-DECIPHERMENT-MONOGRAPH.md`** — the full technical monograph. For the academic specialist. Includes complete methodology, null-model specifications, Python code references, full statistical tables for every finding, exhaustive prior-art citation chain (al-Zarkashī 14th c. → al-Biqāʿī 15th c. → al-Suyūṭī 16th c. → Khalifa 1982 → Philips 1987 → Witztum-Rips-Rosenberg 1994 → McKay 1999 → Cuypers 2015 → Farrin 2014 → Sinai 2017 → this project 2026). Currently being updated by a parallel agent; see that file for the state-of-the-art treatment.

**`findings/the-perfect-flow-essay.md`** — the literary-critical counterpart. Argues that the Quran, read linearly, performs a *perfect flow* at the pericope scale even where whole-surah and whole-muṣḥaf ring claims fail. A humanistic-register complement to the quantitative monograph, rooted in *ʿilm al-balāgha* and *ʿilm al-munāsabāt*, extensively cross-referenced to al-Biqāʿī's *Naẓm al-Durar*.

**`THE-MAN-AT-THE-CENTER.md`** — the historical-anthropological treatment. Asks: if the text has this compositional structure, what can we infer about the person-or-community at its center? Treats Muḥammad as a historical subject and reads the text's structural self-disclosures (the four *Muḥammad* occurrences all being Medinan post-Hijra; the chronological decline of Moses-mentions; the post-Hijra rhetorical shift from Lord-addressing to community-law) as evidence for an authorial trajectory independent of the *iʿjāz* literature. The most speculative of the three volumes; framed as hypothesis, not conclusion.

## 7. What to read next

A skeptical reader with thirty minutes has read it. A reader with three hours should read `findings/scholar-commentary.md` (6,460-word narrative synthesis) and skim `docs/master-index.md`. A reader with thirty hours should read the monograph end-to-end and spot-check two or three phase-B findings against their own preferred null model. A reader with three hundred hours should replicate the project from `/data/` and `/analysis/tools/` — every rule is locked, every anchor value is test-covered, and the full audit trail is in `journal/`.

The project's central epistemic claim is modest. The Quran is not a cipher awaiting numerological decryption; it is a literarily dense composition whose coherence survives at the pericope scale, whose alleged global miracles mostly do not survive audit, and whose classical exegetical tradition was substantially correct about the *kinds* of structure present. The moral for the skeptic: most miracles collapse. The moral for the devotee: what survives is the composition itself — which is, after all, what the tradition has always pointed to.

---

*End of Executive Summary. Approximately 3,050 words.*
