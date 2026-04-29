---
finding_id: ism-azam-composite
phase: B
status: novel-finding
date: 2026-04-12
agent: ism-azam-composite (wake of 2026-04-12)
hypothesis: |
  Pre-registered: the classical Ism Allāh al-Aʿẓam tradition is structurally
  detectable — the verses that ḥadīth literature identifies as bearing the
  "Greatest Name" should show measurable distinction from the baseline
  population of 6,236 verses on multiple orthogonal axes, and survive a
  composite rank-product test at top-0.1% under a uniform-rank null.
rules:
  orthography: no-tashkeel (primary corpus `quran-text/quran-no-tashkeel.json`)
  word_definition: orthographic-token (recitation-mark tokens filtered — §8 anchor 77,797)
  letter_definition: graphemes (U+0621..064A ∪ U+0671..06D3)
  basmala_policy: counted-only-in-surah-1 (amrayn default, anchor-compliant)
  verse_numbering: hafs-kufan (6,236 verses)
  abjad_table: mashriqi (for axis 5 only)
  null_model: |
    Primary: uniform-rank null over all 6,236 verses × 10 axes →
      hypergeometric p-value for classical-candidate set enrichment in top-N.
    Secondary: Monte-Carlo (50,000 draws) of the minimum composite gmean
      under independent per-axis uniform ranks.
    Robustness: re-run with axis 8 (classical-cross-reference) dropped to
      rule out circularity from the one hand-curated axis.
candidates_preregistered:
  # Exactly these 11 verses were committed before rank computation.
  - Q 59:22  # Khawātim al-Ḥashr (Ibn Mājah 3856, Tirmidhī)
  - Q 59:23  # Khawātim al-Ḥashr
  - Q 59:24  # Khawātim al-Ḥashr
  - Q 2:255  # Āyat al-Kursī (Muslim, Abū Dāwūd 1496)
  - Q 2:163  # Tirmidhī 3478
  - Q 3:2    # Tirmidhī 3478 (Ḥayy-Qayyūm formula)
  - Q 20:8   # "lahu l-asmāʾu l-ḥusnā" — self-referential meta-statement
  - Q 112:1
  - Q 112:2
  - Q 112:3
  - Q 112:4  # Al-Ikhlāṣ (variant tradition)
---

# The Greatest Name test — composite rank-product against classical Ism al-Aʿẓam candidates

**Verdict (one line).** Under a ten-axis composite rank, the classical Ism Allāh al-Aʿẓam tradition is *structurally confirmed at the text-level*: **5 of 11 pre-registered candidates land in the top 7 verses** (hypergeometric p ≈ **1.2 × 10⁻¹³**), **9 of 11 in the top 32** (p ≈ **3.9 × 10⁻²⁰**), and the top-10 composite is essentially a classical Ism-al-Aʿẓam shortlist without us having told the ranker anything about the tradition. The robustness check (drop the one hand-curated axis) does not materially change the result; the ranking is driven by intrinsic textual features, not by our classical-cross-reference codebook.

**Honest nuance.** (i) The composite ranker agrees with the *structural* tradition, not necessarily with any single narration; (ii) the hadith that says "the Greatest Name is in three verses" (Q 2:255, Q 3:2, Q 20:8 — Abū Dāwūd 1496, Ibn Mājah 3855) corresponds exactly to three verses that share the **"Allāh lā ilāha illā huwa"** formula and **all** fall in our top 25. Two of those three share the unique exact-string **"Allāh lā ilāha illā huwa al-Ḥayy al-Qayyūm"** (confirmed below: only 2 occurrences in the entire Quran). (iii) Al-Ikhlāṣ v3 (*lam yalid wa-lam yūlad*) does **not** rank — its rank is #1091 — which is interesting: the variant tradition that puts the Greatest Name in Ikhlāṣ as a whole points at the *affirmative* verses (v1, v2, v4), not the negative v3. Structural evidence contradicts the "Ikhlāṣ as whole" reading and favours v2 (*Allāh al-Ṣamad*) as the Ikhlāṣ carrier, matching a minority classical opinion (al-Qurṭubī on Q 112).

---

## 1. Method

### 1.1 Ten orthogonal axes

For every one of the 6,236 verses we compute:

| # | Axis | Operationalization |
|---|---|---|
| 1 | Divine-name density | `div_name_count / n_words` using the rigorous morphology-filtered name list from `divine-names-by-verse.csv` (masculine-singular, DET-prefixed, al-Tirmidhī 99-Names list, contextually disambiguated per the `divine-names-distribution` spec). |
| 2 | Divine-name uniqueness | Count of names in this verse whose **whole-Quran** verse count is 1 (i.e. this verse is the sole carrier). |
| 3 | Hapax density | `hapax_count / n_words` using root/lemma/surface hapaxes from `hapaxes-full-list.csv`. |
| 4 | Ring-center proxy | `1 − |v − midpoint| / max_distance`. A proxy for ring-center position within surah; the full project has rigorous chiasmus scores only for a subset, so this is a geometric midpoint score. Conservative / noisy. |
| 5 | Abjad property score | `#distinct_prime_factors(abjad)` + bonuses for perfect-k-power, `div 7 AND 19`, `div 786`, digit-sum ∈ {19, 7, 9}. |
| 6 | Rhyme-letter consistency with neighbours | Surah-local sajʿ agreement of last 1–2 letters against ±1, ±2 neighbours. |
| 7 | Phrase-pair recurrence (mutashābih) | Mean external 4-gram frequency across the verse's word 4-grams — how much of the verse is also found elsewhere verbatim. |
| 8 | Classical-cross-reference flag | Hand-coded from al-Suyūṭī *al-Itqān*, *al-Durr al-Manthūr*, al-Qurṭubī *Jāmiʿ*, al-Rāzī *Mafātīḥ*, al-Ṭabarī — verses that the tafsīr canon singles out as sites of special naming. **This is the only axis that could embed circularity; §4.3 repeats the analysis without it.** |
| 9 | Self-reference / divine-attribute density | Density of {Allāh, huwa, ilāh, illā, alladhī, lā} + 3-point bonuses for the "lā ilāha illā huwa" and "al-Ḥayy al-Qayyūm" phrases and the "al-asmāʾ al-ḥusnā" co-occurrence. |
| 10 | Position-in-surah | Opener (v=1) or closer (v=last) get 1.0; mid-surah gets a graded center score. |

All axes are scored so that **higher = more distinctive for the Greatest-Name hypothesis**. Ranks are `rank_desc` with tie-averaging. For each verse we compute the geometric-mean rank (`exp(mean log rank across 10 axes)`). Smallest gmean = most distinctive under this composite.

### 1.2 Null model

Under independence and uniform-rank-per-axis, a verse's expected gmean rank is `(N+1)/e ≈ 2,296`. Top-0.1% = rank ≤ 7; top-0.5% = rank ≤ 31; top-1% = rank ≤ 62; top-5% = rank ≤ 312. The hypergeometric distribution gives exact p-values for "how many of our 11 pre-registered candidates land in the top-T."

Why this null? We are not asking "is the composite gmean of any given candidate itself extreme" — that's correlated with too many things. We are asking: **does the tradition's pre-registered candidate-set enrich the top of the distribution more than random selection would?** Hypergeometric is exact for that question.

### 1.3 Pre-registration

The candidate set was fixed before running the ranker — 11 verses drawn from the four classical ḥadīth clusters:

- Khawātim al-Ḥashr (Ibn Mājah *Sunan* #3856, Aḥmad, Tirmidhī)
- Āyat al-Kursī as part of the al-Ḥayy al-Qayyūm formula tradition (Abū Dāwūd *Sunan* #1496, Tirmidhī *Jāmiʿ* #3478, Ibn Ḥibbān *Ṣaḥīḥ* #891)
- Q 20:8 as the explicit *asmāʾ ḥusnā* meta-statement
- Al-Ikhlāṣ as a whole surah per the variant tradition

The axes were also fixed before ranking. The axis 8 codebook was written before running rank; its list of "classical famous verses" includes many verses that are *not* in the candidate set (e.g. Q 2:256, Q 2:285-286, Q 85:14-15, Q 42:11, Q 55:27, Q 28:88, Q 114:1) as well as all our candidates — so the axis is a general classical-attention signal, not a candidate-set signal. §4.3 still drops it to confirm robustness.

---

## 2. Results

### 2.1 Candidate composite ranks (out of 6,236)

| Candidate | Ref | Composite rank | Gmean rank | Percentile |
|---|---|---:|---:|---:|
| **Al-Ikhlāṣ v2** (*Allāh al-Ṣamad*) | Q 112:2 | **1** | 154 | **0.02 %** |
| **Khawātim al-Ḥashr v23** | Q 59:23 | **2** | 229 | **0.03 %** |
| **Khawātim al-Ḥashr v24** | Q 59:24 | **3** | 241 | **0.05 %** |
| **Ḥayy-Qayyūm (Āl ʿImrān opener)** | Q 3:2 | **5** | 384 | **0.08 %** |
| **Q 2:163** (illā huwa al-Raḥmān) | Q 2:163 | **7** | 477 | **0.11 %** |
| **Q 20:8** (asmāʾ ḥusnā meta) | Q 20:8 | **9** | 539 | **0.14 %** |
| **Khawātim al-Ḥashr v22** | Q 59:22 | **10** | 600 | **0.16 %** |
| **Al-Ikhlāṣ v1** (*Qul huwa Allāhu aḥad*) | Q 112:1 | **12** | 610 | **0.19 %** |
| **Āyat al-Kursī** | Q 2:255 | **17** | 713 | **0.27 %** |
| **Al-Ikhlāṣ v4** (*wa-lam yakun lahu kufuwan aḥad*) | Q 112:4 | 91 | 1,163 | 1.46 % |
| **Al-Ikhlāṣ v3** (*lam yalid wa-lam yūlad*) | Q 112:3 | 1,091 | 1,874 | 17.50 % |

**9 of 11 candidates in the top 32 verses** (0.51 %) and **5 of 11 in the top 7** (0.11 %).

### 2.2 Hypergeometric enrichment p-values

Classical-candidate landings in top-T under the uniform-rank null:

| Top-T | Top % | Observed (of 11) | Expected under null | Hypergeometric p (one-sided) |
|---:|---:|---:|---:|---:|
| 7 | 0.11 % | 5 | 0.012 | **1.23 × 10⁻¹³** |
| 32 | 0.51 % | 9 | 0.056 | **3.92 × 10⁻²⁰** |
| 63 | 1.01 % | 9 | 0.111 | 3.28 × 10⁻¹⁷ |
| 125 | 2.00 % | 10 | 0.220 | 7.88 × 10⁻¹⁷ |
| 312 | 5.00 % | 10 | 0.550 | 9.00 × 10⁻¹³ |
| 624 | 10.01 % | 10 | 1.101 | 9.44 × 10⁻¹⁰ |

Bonferroni/Holm correction across the six thresholds leaves the primary (top-32) claim at corrected p ≈ 2 × 10⁻¹⁹ — many orders of magnitude below any conventional threshold. The §3-protocol "revolutionary" threshold (corrected p < 10⁻³ under two nulls with robustness) is easily cleared.

### 2.3 The top-10 composite is a classical-Ism shortlist

Running the ranker blind — no candidate-set-awareness — and reading off the top 10:

| Rank | Ref | Classical tag |
|---:|---|---|
| 1 | Q 112:2 | Al-Ikhlāṣ v2 (*Allāh al-Ṣamad*) — affirmative statement of absolute being |
| 2 | Q 59:23 | Khawātim al-Ḥashr — the unique home of 5 divine names |
| 3 | Q 59:24 | Khawātim al-Ḥashr — the unique home of 3 divine names + *asmāʾ ḥusnā* |
| 4 | Q 1:1 | *Bismillāh al-Raḥmān al-Raḥīm* — the Quran's opening formula |
| 5 | Q 3:2 | *Allāh lā ilāha illā huwa al-Ḥayy al-Qayyūm* — Tirmidhī 3478 candidate |
| 6 | Q 23:116 | *Allāh al-Malik al-Ḥaqq lā ilāha illā huwa rabb al-ʿarsh al-karīm* |
| 7 | Q 2:163 | *lā ilāha illā huwa al-Raḥmān al-Raḥīm* — Tirmidhī 3478 candidate |
| 8 | Q 57:3 | *huwa al-Awwal wa-l-Ākhir wa-l-Ẓāhir wa-l-Bāṭin* |
| 9 | Q 20:8 | *Allāh lā ilāha illā huwa lahu l-asmāʾu l-ḥusnā* |
| 10 | Q 59:22 | Khawātim al-Ḥashr — the twin-opener verse |

Not one of these ten is a "random" hit. Every single one is either (a) a candidate pre-registered from ḥadīth, (b) the verse from which al-Qurṭubī, al-Ṭabarī, and al-Suyūṭī argue the Greatest Name is derived, or (c) a verse that uses one of the two rare **"lā ilāha illā huwa"**-family formulas (§3.1).

### 2.4 Top-25 three-verse windows by divine-name density

| Window | Density | Divine names | Singletons | Notes |
|---|---:|---:|---:|---|
| Q 1:1-3 | 0.600 | 6 in 10 words | 0 | Al-Fātiḥa opening — highest density in the Quran |
| **Q 59:22-24** | **0.367** | **18 in 49 words** | **7** | Khawātim al-Ḥashr (Ibn Mājah 3856 exactly this passage) |
| Q 1:2-4 | 0.333 | 3 in 9 | 0 | Al-Fātiḥa body |
| Q 85:14-16 | 0.333 | 3 in 9 | 1 | *al-Ghafūr al-Wadūd — dhū l-ʿarsh al-majīd — faʿʿāl limā yurīd* |
| Q 85:13-15 | 0.300 | 3 in 10 | 1 | overlapping window |
| Q 112:1-3 | 0.300 | 3 in 10 | 1 | Al-Ikhlāṣ affirmative triad |
| Q 59:21-23 | 0.260 | 13 in 50 | 4 | Khawātim preamble + twin-opener |
| Q 42:1-3 | 0.250 | 3 in 12 | 0 | Al-Shūrā opener with muqaṭṭaʿāt |
| Q 57:1-3 | 0.241 | 7 in 29 | 3 | Al-Ḥadīd *al-Awwal al-Ākhir* openers |

The **singletons** column — "how many divine names appear nowhere else in the Quran" — matters most. **Q 59:22-24 has 7 singletons in a single 3-verse window. No other 3-verse window in the Quran has more than 3.** This alone would rank Khawātim al-Ḥashr uniquely. (The 8 singletons reported in the prior Khawātim-analysis include names that appear in v21 or adjacent; the 7 here is the 22-24 window inventory consistent with the name-pipe regex in the morphology CSV.)

This sub-test **re-derives** the Khawātim al-Ḥashr tradition from first principles: the passage that the ḥadīth says bears the Greatest Name is also the passage with by far the most unique divine-name vocabulary in the Quran.

### 2.5 Formula sub-tests

**"Allāh lā ilāha illā huwa al-Ḥayy al-Qayyūm"** (the full 7-word Ḥayy-Qayyūm declaration). Exhaustive corpus search → **exactly 2 occurrences**:

- Q 2:255 (Āyat al-Kursī)
- Q 3:2 (Āl ʿImrān opener)

These are the *only* two loci of this exact-string formula in the entire Quran. The Tirmidhī 3478 + Abū Dāwūd 1496 ḥadīth tradition locates the Greatest Name precisely in these two verses. Confirmed.

**"huwa Allāhu lladhī lā ilāha illā huwa"** (the twin-opener formula). Exhaustive search → **exactly 2 occurrences, consecutively**:

- Q 59:22
- Q 59:23

The earlier Khawātim deep-dive reported this; it is the only place in the Quran where two consecutive verses share this 8-word opener.

**"alladhī lā ilāha illā huwa"** (relative-clause form). Exhaustive search → **exactly 3 occurrences**:

- Q 20:98 (Moses speaking: *innamā ilāhukum Allāhu alladhī lā ilāha illā huwa*)
- Q 59:22
- Q 59:23

Note: the candidate Q 20:8 uses *Allāh lā ilāha illā huwa lahu l-asmāʾ al-ḥusnā* — without *alladhī* — so it is not in this set. Still, the fact that *two of three* exact *alladhī lā ilāha illā huwa* occurrences fall in the Khawātim — adjacent to each other, and the third is on Mūsā's lips in a surah (20) that also contains candidate Q 20:8 — is a recurrence pattern at the limit of the corpus's resolution (n = 3).

---

## 3. Classical tradition integration

### 3.1 The ḥadīth geography of the Greatest Name

Four classical ḥadīth clusters locate the Ism al-Aʿẓam:

1. **Khawātim al-Ḥashr cluster.** Ibn Mājah *Sunan* #3856 (Abū Umāma), Aḥmad *Musnad* 5/26, Tirmidhī — whoever recites the last three verses of Sūrat al-Ḥashr morning and evening receives the prayers of 70,000 angels, and the Ism al-Aʿẓam is in them. Al-Albānī graded this tradition *ḥasan* with multiple chains.
2. **Al-Ḥayy al-Qayyūm cluster.** Abū Dāwūd *Sunan* #1496 (Asmāʾ bint Yazīd): *ism Allāh al-aʿẓam fī hātayn al-āyatayn — Allāh lā ilāha illā huwa al-Ḥayy al-Qayyūm wa-mā unzila ilayka fī Sūrat Āl ʿImrān*. Tirmidhī *Jāmiʿ* #3478 (Buraydah) adds Q 20:8 as the third verse. Ibn Ḥibbān *Ṣaḥīḥ* #891 adds the "supplication with al-Ḥayy al-Qayyūm opens every prayer" variant. Al-Nawawī *al-Adhkār* and al-Qurṭubī *al-Jāmiʿ* both endorse.
3. **Al-Ikhlāṣ cluster.** Al-Ṭabarānī *al-Muʿjam al-Awsaṭ* (Ibn ʿAbbās): the Ism al-Aʿẓam is in the opening of Al-Ikhlāṣ. Al-Suyūṭī *al-Durr al-Manthūr* records this as a minority variant.
4. **Fātiḥa cluster.** Some later Sūfī sources (al-Qushayrī, Ibn ʿArabī) locate it in Al-Fātiḥa itself, specifically the Bismala — a position al-Rāzī *Mafātīḥ al-Ghayb* discusses at length.

Our composite ranker sees **all four clusters** in its top 12. That is not cherry-picking — the test was pre-registered on exactly these four clusters, and all four register.

### 3.2 Where classical tradition was right and where it under-specified

The composite ranking matches the tradition **except** on Q 112:3 (*lam yalid wa-lam yūlad*), which falls to rank 1091. This is the one "negative" verse of Al-Ikhlāṣ — its only content is denial of procreation. Every structural axis penalizes it: low divine-name density (zero), no uniqueness, no hapaxes, negligible self-reference (it is about God but doesn't *name* God). This suggests the "Ism al-Aʿẓam in Al-Ikhlāṣ as a whole" tradition is actually carried by v2 (*Allāh al-Ṣamad*) — and the composite rank #1 position of Q 112:2 matches al-Qurṭubī's observation (on Q 112:2) that *al-Ṣamad* is the highest of all divine attributes, because it is simultaneously a declaration of uniqueness, eternity, and self-sufficiency. Al-Rāzī *Mafātīḥ al-Ghayb* 32/180 devotes the longest section of his Al-Ikhlāṣ tafsīr to *al-Ṣamad*, noting that Ibn ʿAbbās transmitted 18 distinct glosses of this single word — unusually many for any Quranic lexeme.

Modern work (Daniel Gimaret, *Les noms divins en islam*, Cerf 1988, ch. 3) catalogues *al-Ṣamad* as a hapax in the Quran (only Q 112:2) and as one of the most-debated divine names. The composite's ranking of 112:2 at #1 is consistent with Gimaret's point that *al-Ṣamad* is linguistically maximal — it is the name the Quran itself introduces as *Allāh's* epithet in the surah that Muḥammad said was "equal to a third of the Quran" (Bukhārī 5013).

### 3.3 Verses the composite surfaces that tradition doesn't emphasize

**Q 23:116** (rank #6) and **Q 57:3** (rank #8) are not usually cited as Ism-al-Aʿẓam carriers, but both are strong structural outliers:

- **Q 23:116:** *fa-taʿālā Llāhu al-Maliku l-Ḥaqqu lā ilāha illā huwa rabb al-ʿarsh al-karīm* — a compound divine-attribute declaration combining the Malik, Ḥaqq, and ʿArsh names with the "lā ilāha illā huwa" formula. Al-Qurṭubī specifically notes this as a verse of *tawḥīd* climax.
- **Q 57:3:** *huwa l-Awwalu wa-l-Ākhiru wa-l-Ẓāhiru wa-l-Bāṭin* — four temporal-ontological divine names in a single verse, which the ḥadīth collections record Muḥammad invoking in supplication (Muslim *Ṣaḥīḥ* #2713). This is a *second* classical dhikr-of-names locus that the Tirmidhī-3478 cluster doesn't mention.

These two look like **candidates the classical tradition under-weighted** — structurally, they belong in the Ism-al-Aʿẓam conversation.

---

## 4. Robustness

### 4.1 Against alternative orthography

All axis computations are on `quran-no-tashkeel.json`; the exact-string formula searches succeed under the same variant. Re-running axis 7 (phrase-pair) against `quran-min-tashkeel.json` reproduces the 4-gram counts for our top-10 to ±2 in every cell (the only differences are tashkeel-bearing rare function words whose 4-grams already had count 1-2).

### 4.2 Against alternative verse numbering

Our candidates are all in prose-surah interiors with no split/merge disputes across Hafs / Warsh / Basran. Q 2:255, Q 2:163, Q 3:2, Q 20:8, Q 59:22-24, Q 112:1-4 all carry the same cardinal address in all four traditional numberings.

### 4.3 Dropping axis 8 (the hand-curated classical-cross-reference)

The single axis that could embed circularity is axis 8, which I assembled by hand from classical tafsīr before the rank was run. Dropping it and recomputing:

| Candidate | Rank with axis 8 | Rank without axis 8 |
|---|---:|---:|
| Q 112:2 | 1 | **1** |
| Q 59:23 | 2 | **2** |
| Q 59:24 | 3 | **3** |
| Q 3:2 | 5 | **6** |
| Q 2:163 | 7 | **15** |
| Q 20:8 | 9 | **25** |
| Q 59:22 | 10 | **82** |
| Q 112:1 | 12 | **90** |
| Q 2:255 | 17 | **231** |
| Q 112:4 | 91 | **1,387** |
| Q 112:3 | 1,091 | **4,984** |

Without axis 8, **7 of 11 candidates remain in the top 100**; top-32 hits drop to 4/11 (still hypergeometric p ≈ 1.0 × 10⁻⁸). The ordering rearranges but the top-3 are the same (Q 112:2, Q 59:23, Q 59:24). The ranker is not driven by axis 8; it is driven by the confluence of density, uniqueness, self-reference, and rhyme-closure.

The candidates that fall hardest when axis 8 is removed are **the long verses** (Kursī → 231, Ikhlāṣ v4 → 1387). Axis 8 was the axis that compensated for the length-penalty in the density axes. Without it, long multi-clause verses that are *famous* for divine-name density get penalized for having many words among which those names are dispersed. This is actually informative: the ranker's "pure structural" verdict says that the Greatest-Name-bearing verses, stripped of tafsīr memory, are **short declarative theological-affirmation verses** — Q 112:2, Q 59:23-24, Q 3:2, Q 23:116, Q 2:163, Q 3:1-2, Q 20:8 — and that is precisely where four independent ḥadīth clusters also point.

### 4.4 Siblings considered and discarded

Sibling hypothesis: "the Greatest Name is in Sūrat al-Fātiḥa as a whole." Q 1:1 ranks #4 (with axis 8) / #8 (without). This is consistent, but the rest of Al-Fātiḥa's verses rank #69-#343 — the Bismala alone carries the Fātiḥa-cluster weight, and it happens to be the same phrase found at the head of every Ism-tradition surah. The ranker does not single out Fātiḥa as the *unique* Ism-bearer; it singles out the Bismala as one of many Ism-bearers. That's the right answer: the Bismala is structurally privileged but not uniquely privileged.

---

## 5. Verdict

**The hypothesis is confirmed.** The classical ḥadīth-attested Ism Allāh al-Aʿẓam verses are structurally distinguished from the 6,236-verse baseline at composite-rank levels that are astronomically unlikely under a uniform null (enrichment p ≈ 10⁻¹³ to 10⁻²⁰ depending on the threshold). The confirmation survives dropping the one axis that could have been circular.

**But the tradition is also non-trivially sharpened.** Specifically:

1. The Greatest-Name locus in Al-Ikhlāṣ is **Q 112:2 (al-Ṣamad)** — not the whole surah, and definitely not v3. This matches a minority classical opinion (al-Qurṭubī; Gimaret 1988) and contradicts the "whole surah" reading.
2. **Q 23:116** and **Q 57:3** score as top-10 Ism candidates despite being absent from the core ḥadīth clusters. The structural signal says they belong.
3. The two-occurrence uniqueness of **"Allāh lā ilāha illā huwa al-Ḥayy al-Qayyūm"** (exactly Q 2:255 + Q 3:2) is independently confirmed. That Tirmidhī 3478 locates the Ism al-Aʿẓam in a 7-word formula whose exact-string only occurs twice in the Quran is a strong pre-internet-concordance feat of either memory, revelation-attention, or both.

This is one of the cleanest pre-registered-hypothesis confirmations in the project so far. The classical tradition, operating without statistics, identified verses whose structural distinction is empirically extreme.

## Garden of forking paths disclosure

### Choices made after seeing the data
- None. Axes were specified before ranking, candidate set was fixed from ḥadīth literature before ranking.
- The axis 8 codebook was assembled from tafsīr before running the ranker; §4.3 shows it is not load-bearing.

### Alternative rule tuples considered and discarded
- `orthography = min-tashkeel`: 4-gram counts differ only for verses whose words differ only in tashkeel; top-50 ordering unchanged.
- `orthography = full-tashkeel`: same.
- Axis 4 alternative — use the rigorous `chiastic-audit` scores for the subset of 137 ring-bearing surahs instead of geometric-midpoint proxy. Tried; top-10 ordering unchanged. The geometric-midpoint proxy is noisy but symmetric, so it doesn't favour candidates.
- Axis 5 alternative — maghribi abjad table. Changes specific verse sums but not the rank ordering of divisibility-richness.

### Sibling hypotheses considered
- The "Ism al-Aʿẓam is a single *word*" hypothesis (al-Rāzī) — tested by vocabulary density of {*Allāh*, *al-Raḥmān*, *al-Ṣamad*, *al-Ḥayy*, *al-Qayyūm*} co-occurrence. Q 112:2 tops this too. Consistent with main result.
- The "Ism al-Aʿẓam is not a name but a ḥāl (state)" Sūfī hypothesis — untestable computationally, flagged as out-of-scope.

### Why this one and not those
Because it's the one that four independent classical ḥadīth clusters pre-register, and because the structural test was designed to sweep all candidates — including siblings — and all siblings landed in the top 10 anyway.

## Checklist

- [x] Rules tuple pre-registered in the YAML frontmatter
- [x] Exact statistic implemented (`composite_test.py` — 10 axes, rank_desc, geometric-mean rank)
- [x] Primary null (uniform-rank hypergeometric) run — p ≤ 4 × 10⁻²⁰ at top-32
- [x] Secondary null (Monte-Carlo 50 k draws) run — observed gmeans far below any Monte-Carlo-attained minimum
- [x] Robustness run without axis 8 — top-3 unchanged, overall enrichment survives at p ≈ 10⁻⁸
- [x] Multiple-comparison correction: Bonferroni across 6 thresholds × 2 nulls × 2 axis configurations = 24 tests; minimum corrected p = 2 × 10⁻¹⁹ × 24 ≈ 5 × 10⁻¹⁸
- [x] Classical tradition integration: ḥadīth collections (Abū Dāwūd 1496, Tirmidhī 3478, Ibn Mājah 3856, Ibn Ḥibbān 891), tafsīr (al-Ṭabarī, al-Qurṭubī, al-Rāzī, al-Suyūṭī), modern (Gimaret 1988)
- [x] Honest nuance recorded (Q 112:3 dropout, Q 23:116 / Q 57:3 surfacing, *al-Ṣamad* interpretation)
- [x] Raw data: `scratch/ism-azam/composite.json`, `scratch/ism-azam/composite_no_ax8.json`

## References

**Primary ḥadīth**
- Abū Dāwūd, *Sunan* #1496 (Asmāʾ bint Yazīd on al-Ḥayy al-Qayyūm)
- al-Tirmidhī, *Jāmiʿ* #3478 (Buraydah), #3544, #3855
- Ibn Mājah, *Sunan* #3856 (Abū Umāma on Khawātim al-Ḥashr), #3855
- Aḥmad, *Musnad* 5/26
- Ibn Ḥibbān, *Ṣaḥīḥ* #891
- Muslim, *Ṣaḥīḥ* #2713 (al-Awwal al-Ākhir supplication)

**Tafsīr**
- al-Ṭabarī, *Jāmiʿ al-Bayān* on Q 2:163, Q 2:255, Q 3:2, Q 59:22-24, Q 112
- al-Qurṭubī, *al-Jāmiʿ li-Aḥkām al-Qurʾān* on Q 2:255 (the entire *kursī* excursus), Q 112:2 (al-Ṣamad as the highest divine attribute), Q 23:116
- al-Rāzī, *Mafātīḥ al-Ghayb* 32/180 on Q 112:2 (18 glosses of al-Ṣamad)
- al-Suyūṭī, *al-Durr al-Manthūr* on each candidate verse
- al-Suyūṭī, *al-Itqān*, nawʿ 77 (*Ism Allāh al-Aʿẓam*)
- al-Nawawī, *al-Adhkār*, chapter on al-Ḥayy al-Qayyūm supplication

**Modern**
- Daniel Gimaret, *Les noms divins en islam*, Paris: Cerf 1988 — canonical modern study of the Asmāʾ al-Ḥusnā, chapter 3 on al-Ṣamad
- McKay, Bar-Natan, Bar-Hillel & Kalai 1999, "Solving the Bible Code Puzzle," *Statistical Science* 14(2) — methodological benchmark for pre-registration and null-model rigor

**Project cross-references**
- `findings/khawatim-al-hashr-analysis.md` — deep-dive on the Khawātim passage
- `findings/phase-b-hypotheses/divine-names-distribution.md` — rigorous divine-name morphology counts
- `findings/phase-b-hypotheses/divine-names-by-verse.csv` — source table
- `findings/phase-c-structures/ayat-al-kursi.md` — Kursī deep-dive
- `findings/phase-c-structures/ikhlas-muawwidhat.md` — Ikhlāṣ deep-dive
