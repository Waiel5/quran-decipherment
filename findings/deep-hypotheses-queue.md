# Deep Hypotheses Queue — For Future Rounds

This file holds hypotheses proposed by the meta-reasoning layer after each wave of findings lands. Entries are testable, specific, and include: the hypothesis, the exact computational procedure, the null model, and the acceptance criterion.

This is an append-only file. Hypotheses get promoted to findings/ once tested.

## Rules of the queue

1. Every hypothesis must be stated BEFORE the test (pre-registration against garden-of-forking-paths).
2. Every hypothesis references a rules tuple per docs/methodology.md.
3. Every hypothesis lists its null model per docs/statistical-rigor-protocol.md.
4. Priority ordering: highest-novelty first, then highest-rigor, then lowest-cost.

## Seed hypotheses (initial queue)

*The `deep-pattern` agent will populate this file on its first run with 10-15 hypotheses derived from what the current wave has found.*

---

# Wave 1 — Deep-pattern agent, 2026-04-12 (run 1)

**Author:** deep-pattern meta-reasoner
**Context consumed:** master-index.md, all phase-A/B/C finding files, methodology.md, statistical-rigor-protocol.md. See `journal/deep-pattern-run-1.md` for the reasoning process that produced this wave.

The 22 hypotheses below are organized into **seven themes**. Priorities:
- **H1–H3** are the highest-EV (high novelty, clean nulls, existing data).
- **H14, H20, H22** are the highest-scholarly-interest (classical-voice predictions).
- Medium/low priority hypotheses are still testable and pre-registerable; they are ranked by cost, not by importance.

For each hypothesis I list: (1) statement, (2) rationale, (3) computational procedure, (4) null model, (5) acceptance criterion, (6) priority. All rules tuples default to the master tuple `(no-tashkeel, orthographic-token / lemma-where-noted, graphemes, counted-only-in-surah-1, hafs-kufan, mashriqi)` unless explicitly overridden.

---

## THEME 1 — Numerical coincidences on theological lemmas

### H1 — The systematic "meaningful-N lemma audit"

**Hypothesis.** For each structurally meaningful integer N in the set `{6, 7, 12, 19, 25, 30, 40, 50, 57, 70, 77, 99, 114, 313, 786, 6236}`, the lemma-count matrix of the Quran (4,832 lemmas × count) contains AT MOST chance-expected numbers of hits when the concept tag of each N-hit lemma is independently scored for theological-centrality by a sealed rubric, EXCEPT at N=114 (rahma already confirmed) and possibly N=147 (ghayr/ilāh/jannah already confirmed). Null: the bulk of apparent "miraculous" count-matches disappear when you ask "is the lemma at this count actually theologically central, or cherry-picked from a count-bucket of many siblings?"

**Rationale.** Our team found rahma=114 and the ghayr/ilāh/jannah=147 triple by *looking*. The honest version is: enumerate every N in the meaningful-integer set, list every lemma at that N, AND list how many siblings (other lemmas at the same count) there are in each bucket. This converts "miracle" claims into a base-rate problem. The numerical-coincidences dossier already computes this for some N but does not compute the **base rate of theological-centrality per lemma** (which is the denominator the rahma claim quietly relies on).

**Computational procedure.**
1. For each N in the set above, extract `B(N) = {lemmas with count exactly N}` from the QAC v0.4 lemma table. (Data ready: `data/morphology/quranic-corpus-morphology-0.4.txt`.)
2. For each lemma ℓ in B(N), compute a **theological-centrality score** from a pre-registered rubric: (a) presence in the 99 Names of Allah list; (b) presence in Sūrat al-Fātiḥa; (c) presence in Āyat al-Kursī; (d) presence in surah titles; (e) presence in Shahāda. Score ∈ {0..5}.
3. For each N report: `|B(N)|`, the mean centrality of B(N), and the top centrality score in B(N). Also compute the count of lemmas at N±1 and the mean centrality across that neighborhood (within-window control for counting-boundary sensitivity).
4. Compare observed mean centrality-at-N to a null distribution drawn by picking uniform-random lemmas of matching count range. Report empirical p per N.

**Null model.** §1.3 word-level 2-gram surrogate (primary, sample 10⁴ surrogates of Quranic length) AND §1.4 length-matched Bukhārī-block draw (stringent, 10³ surrogates). The test is "is the enrichment of theological-central lemmas at count=N higher than in comparable Arabic prose of the same length?"

**Acceptance criterion.** A result counts as a finding if the observed centrality at N=114 is in the top 1% of the null (expected from rahma) AND at least one NEW N shows top-5% centrality enrichment that was not a seed of the hypothesis. If only N=114 survives, the interpretation is that rahma-114 is a one-of-a-kind coincidence, not an instance of a general rule.

**Priority.** 🔴 **HIGH** — this is the correct generalization of the rahma finding and the ghayr/ilāh/jannah finding. The garden of forking paths is closed off by the pre-registered integer set and the pre-registered centrality rubric. Existing data.

---

### H2 — Scan for (surah S, root R) pairs where `count(R in Quran) = S` AND R has narrative meaning in S

**Hypothesis.** Besides Yusuf/sjn=12, there exist at least 3 more (S, R) pairs where the global count of R equals the surah index S AND the narrative of surah S is substantively about R's meaning. However, the number of such hits is NOT significantly higher than chance when you control for (a) the number of roots at each count, (b) the narrative-relevance base rate, and (c) the 114-way multiple-comparison family.

**Rationale.** `sjn` = 12 with all 12 tokens in Surah 12 is the most Quran-marketing-friendly finding in the root-cartography file. But the protocol says: enumerate the whole matrix, don't report one cell. This hypothesis turns the single celebrated hit into a systematic scan and an honest null.

**Computational procedure.**
1. For S = 1..114, enumerate roots with global count = S from `data/morphology/root-index.json`. (Fast; pre-indexed.)
2. For each candidate (S, R), compute: (a) `count_in_S / count_total`; (b) whether all tokens are in S (the "hapax-surah" condition); (c) a 1-sentence semantic description of R from a fixed gloss file (Hans Wehr or comparable).
3. Independently tag each candidate for "narrative relevance to surah S" using Sahih International English translation + a sealed rubric (does R's meaning appear in surah S's title, opening verses, or standard Tafsir tagline?). Score ∈ {0..2}.
4. Report: all hits, the narrative-relevance distribution, and the count of "perfect triples" (count=S + all-in-S + narrative-tagged).

**Null model.** §1.5 permutation of surah indices (10⁴ perms). Compute the expected number of perfect-triple hits when surah index labels are shuffled. Report empirical p.

**Acceptance criterion.** At least 2 additional perfect triples beyond Yusuf/sjn. If zero or one, the Yusuf finding is downgraded to "singular coincidence, not a pattern." Either outcome is publishable.

**Priority.** 🔴 **HIGH** — mechanical, cheap, and the Yusuf triple demands this test. Existing data.

---

### H3 — Theological-opposite count parity scan

**Hypothesis.** Beyond the already-tested word-pairs (day/night, life/death, etc. most of which failed), there exist lemma-level count matches between theological opposites that have not been cataloged. Specifically: `nūr/ẓulma` (light/darkness), `ṣidq/kadhib` (truth/falsehood), `tawbah/ʿiṣyān` (repentance/disobedience), `najāt/halāk` (salvation/destruction), `shukr/kufr` (gratitude/disbelief), `ṣabr/jazaʿ` (patience/impatience), `qalb/ṣadr` (heart/chest).

**Rationale.** The surviving replication is `malak/shayṭān = 88/88` (angels vs devils). The published literature keeps testing the same ~15 pairs. Our team has not attempted the theologically obvious pairs *not* in the popular list. This is a cheap sweep to either extend the surviving-pair list or confirm that the published list is exhaustive.

**Computational procedure.**
1. For each pair (A, B) in a pre-registered list of 12-20 theological opposites, compute lemma counts under QAC v0.4.
2. Also compute under root collapse (summing all lemmas sharing a root).
3. Compute the ratio |count(A) - count(B)| / max(count(A), count(B)). Report all 12-20 raw numbers.
4. For each pair also report the nearest-integer-ratio on a Nawfal-style reading (1/1, 2/1, 3/1, etc.).

**Null model.** §1.3 word-level 2-gram surrogate. For each pair, compute the distribution of |A-B| under 10⁴ surrogates drawn from the Quran's bigram model. Report empirical p per pair. Multiple-comparison correct with Holm over 20 tests.

**Acceptance criterion.** At least 1 new pair exact-matches (like malak/shayṭān) under Holm-corrected p<0.01. If zero, report as a clean null on the Nawfal-style extended hypothesis.

**Priority.** 🟡 **MEDIUM** — derivative of existing word-pair work. Easy to run. Existing data.

---

### H4 — `raḥma` derivative-cluster audit

**Hypothesis.** Of the derivatives of root `r-ḥ-m` (raḥma, raḥmān, raḥīm, marḥama, rāḥim, ruḥm), exactly ONE has count 114. The others do NOT cluster at structurally meaningful numbers. If this hypothesis holds, it strengthens the rahma-114 claim by showing the coincidence does not smear across the family. If it fails (multiple rhm derivatives at meaningful N), the claim is evidence of selection from a lexical family.

**Rationale.** A major weakness of the rahma=114 headline is: what if ANY r-ḥ-m lemma with a plausibly high count could be cherry-picked? We need to enumerate all r-ḥ-m derivatives and see whether 114 is a one-off or whether the cluster is interesting for other reasons. Same test must be run on the whole ism-allāh divine-name cluster.

**Computational procedure.**
1. From QAC, enumerate all lemmas under root `rHm`. Report counts for each.
2. For each, check if the count is in `{6, 7, 12, 19, 25, 40, 50, 57, 77, 99, 114, 147, 313}` (pre-registered meaningful-integer set).
3. Repeat for roots `Alh` (divine name), `rbb` (Lord), `Emr` (ʿumrah/creation-age), `nfs` (self/soul).

**Null model.** Binomial test: what's the probability of k or more of a random 7-lemma cluster hitting a meaningful-integer set of size ~15 out of 4832 lemma-count positions? Comparable-corpus control optional.

**Acceptance criterion.** Exactly one 114 in the rHm cluster AND at most chance-expected hits in comparable roots ⇒ rahma-114 promoted to "non-cherry-picked singular coincidence." Multiple hits in rhm ⇒ downgrade to "lexical family, not miracle."

**Priority.** 🔴 **HIGH** — this is the robustness test that the rahma-114 claim REQUIRES before it can be called a finding. Existing data.

---

### H5 — Spelled-out numeral ↔ count self-reference scan

**Hypothesis.** Whenever the Quran spells out a numeral N in its text (e.g. *tisʿa ʿashar*, *arbaʿīna*, *thalāthatu*), there is a non-trivial excess of lemma-count matches at that N compared to spelled-out-numerals not appearing in the text.

**Rationale.** The Q 74:30 finding (*tisʿa ʿashar* is the only spelled-out 19) is suggestive. The Q 18:25 finding (309 as *thalāth mi'a sinīn wa-zdādū tisʿan*) is also on the list. A systematic scan asks: for every numeral the Quran bothers to spell out, is the count of some thematically related lemma ALSO that number?

**Computational procedure.**
1. Extract all verse-contained spelled-out Arabic numerals via a pre-registered regex list: `واحد, اثنين, ثلاث, اربع, خمس, ست, سبع, ثمان, تسع, عشر, عشرين, ثلاثين, اربعين, خمسين, ستين, سبعين, ثمانين, تسعين, ماية, الف, عشرة, تسع وتسعون`, etc.
2. For each numeral N found, enumerate `B(N) = {lemmas with count exactly N}` and report: (a) the lemmas; (b) their centrality scores per H1's rubric.
3. Compute the mean centrality of B(N) for N-in-text vs N-not-in-text.

**Null model.** §1.3 word-level 2-gram null for base rate of centrality-match; §1.5 permutation of the spelled-out-numerals across possible N values (keep the set of numerals fixed but shuffle which N each links to).

**Acceptance criterion.** B(N-in-text) mean centrality > B(N-not-in-text) mean centrality at empirical p<0.01.

**Priority.** 🟡 **MEDIUM** — novel framing but cheap. Existing data.

---

## THEME 2 — Surah-anchored vocabulary fingerprints

### H6 — "Every surah has a signature root" test

**Hypothesis.** For each surah S, compute its **signature root** as the triliteral root R that maximizes `(count(R in S) / count(R in Quran)) × (count(R in S))` (concentration × mass). The distribution of signature-root scores should show a long-tailed structure where ~5-15 surahs have signature roots with concentration > 0.75 AND those signature roots should have obvious thematic correspondence to the surah (like sjn/Yusuf, khf/Kahf).

**Rationale.** We found 3 specific hits (sjn/12, qmS/12, khf/18, myl/4) in the root-cartography findings. The general shape of the distribution has NOT been computed. If the top-10 signature-root surahs are all thematic, the "surah-fingerprint" hypothesis is real. If only the published cases are thematic, the discovery mechanism was cherry-picking.

**Computational procedure.**
1. For each (S, R) pair with count(R in S) ≥ 4, compute `concentration(S,R) = count(R in S) / count(R in Quran)`.
2. Rank by `concentration × count(R in S)` within each surah. Take the top-1 root per surah.
3. Report the 114-row table: surah, signature root, its concentration, and its Sahih-gloss meaning.
4. Have a sealed rubric rate each of the 114 signature roots against the surah's standard-tafsir theme: "thematic / unrelated / neutral." Report the distribution.

**Null model.** §1.5 permutation of surah index labels (10⁴ permutations). How often does a random permutation produce ≥K thematic-signature hits in the top ranks? Report empirical p.

**Acceptance criterion.** ≥15 of 114 signature-root surahs are tagged "thematic" with corrected p<0.01.

**Priority.** 🔴 **HIGH** — this is the natural extension of the Yusuf/sjn finding, and it converts a one-off observation into a distributional claim. Existing data.

---

### H7 — The "rare-root monopoly" catalog

**Hypothesis.** For each root R with global count between 4 and 15, if ALL tokens of R are contained in a single surah S, that's a "monopoly". We have 4 reported monopolies (sjn, qmS, khf, myl). The total number of monopolies under this filter is a finite, computable set. That set is enriched for narrative-signature words (monopolies are plot-drivers) compared to a word-shuffle null.

**Computational procedure.**
1. From `root-index.json`, enumerate all R with 4 ≤ count ≤ 15 where every token lives in a single surah. (Fast.)
2. For each monopoly, report the surah, the root, the count, and the Sahih gloss.
3. Tag each with narrative-relevance score (0-2).

**Null model.** §1.5 permutation of verse-to-surah assignments preserving verse lengths and bag-of-roots (this preserves root counts and verse lengths but shuffles *which* surah each verse goes into). Under this null, count the number of monopolies.

**Acceptance criterion.** Observed monopoly count > 95th percentile of null.

**Priority.** 🟡 **MEDIUM** — builds directly on root-cartography without requiring new data. Quick to run.

---

### H8 — Anti-monopoly: roots that avoid a specific surah

**Hypothesis.** For each surah S and each common root R (count ≥ 50 in Quran), compute `expected(R in S) = count(R) × len(S) / total_len`. Report `(observed - expected) / sqrt(expected)` as a z-score. The **minimum** per surah is the "avoided root" of S. Surahs with extreme minimum z-scores (e.g. |z| > 3) are "avoidance surahs"; the avoided root is a thematic clue.

**Rationale.** The Yusuf/sjn pattern is a "mono-surah root". The inverse — a root that is conspicuously absent from a specific surah — has not been scanned. If Ar-Rahman (Q 55) conspicuously lacks the root `xsr` (loss), or Al-Ikhlas (Q 112) conspicuously lacks root `kfr` (disbelief), those are form-enacts-content findings of the same flavor as the monopolies.

**Computational procedure.** Compute a 114×N_roots expected-vs-observed z matrix. Report the bottom-3 z per surah and tag their meaning.

**Null model.** §1.3 word-level unigram surrogate at 10⁴ draws (controls for length but not bigram structure).

**Acceptance criterion.** ≥5 surahs with |z| > 3 whose missing-root is thematically significant beyond Bonferroni over 114×N_roots.

**Priority.** 🟢 **LOW** — interesting but will be drowned by Bonferroni. Existing data.

---

## THEME 3 — Ring structures for prophet pericopes

### H9 — Prophet-pericope ring sweep

**Hypothesis.** The chiastic-ring signal that surfaced in Al-Baqara 131-144 (Abraham) is a *general* feature of prophet-pericopes: similarly significant rings exist for the Moses narrative in Surah 20 (Ṭā-Hā) and Surah 28 (Al-Qaṣaṣ), the Yusuf narrative in Surah 12 (entirety), the Noah narrative in Surah 71, the Dhū'l-Qarnayn narrative in Al-Kahf 83-98 (already confirmed), and the Maryam/Yaḥyā narrative in Surah 19.

**Rationale.** The Al-Kahf Dhū'l-Qarnayn ring at 83-91 is already Bonferroni-surviving. The Al-Baqara Abraham/qibla ring is the strongest. This raises the question: is ring-composition the *default* mode of prophet-pericope structure in the Quran, or is Al-Baqara 131-144 unique?

**Computational procedure.**
1. Pre-register the 7 prophet pericopes with exact verse ranges from *tafsīr al-jalālayn* or a standard surah-outline source. Pericope ranges:
   - Moses in Ṭā-Hā: Q 20:9-98
   - Moses in Al-Qaṣaṣ: Q 28:3-46
   - Yusuf (whole): Q 12:1-111
   - Noah in Hūd: Q 11:25-49
   - Noah in An-Nūḥ: Q 71:1-28
   - Maryam: Q 19:1-40
   - Abraham in As-Sāffāt: Q 37:83-113
2. Apply the existing chiastic-audit pipeline (paired root-set Jaccard) to each pericope.
3. Compute z-score vs within-pericope verse-shuffle null (same null used for the 131-144 hit).

**Null model.** §1.2 verse-shuffle-within-pericope, 10³ shuffles per pericope. Holm-Bonferroni over 7 tests.

**Acceptance criterion.** ≥3 pericopes with corrected p<0.01. If all 7 hit, ring-composition is the default; if only 1-2, Al-Baqara is unique.

**Priority.** 🔴 **HIGH** — the single most important test for the Quran's structural claims. Maps directly onto Farrin 2014, Cuypers 2009 debate. Existing data + existing pipeline.

---

### H10 — Qibla-moment structural uniqueness test

**Hypothesis.** The qibla-change verses (Q 2:142-150) are the LOCAL peak of ring-composition density in Al-Baqara, but there are other "covenant moments" in the Quran that should have similar local structure: the Bayʿat al-Riḍwān (Q 48:10,18), the treaty of Hudaybiya (Q 48), the oath in Ās (Q 5:3). Test whether these verses also form local rings.

**Computational procedure.** Sliding-window Jaccard chiasmus test at window=5-15 on each of these candidate covenant-moment regions. Compare z-scores.

**Null model.** §1.2 window-shuffle.

**Acceptance criterion.** At least one additional covenant-moment scores z > 4 with corrected p<0.005.

**Priority.** 🟡 **MEDIUM** — niche but interesting.

---

## THEME 4 — Palindromic scanning at all scales

### H11 — Full odd-length palindrome scan with proper null

**Hypothesis.** Length-7 letter-count palindromes (the Ash-Shams and Takwir cases) are the headline. But the full spectrum — lengths 3, 5, 7, 9, 11 — has not been systematically scanned under the word-shuffle null. Specifically: does the Quran exhibit excess palindromic subruns at each length, or is the length-7 case the only statistically distinguishable signal?

**Computational procedure.**
1. For each odd L in {3, 5, 7, 9, 11, 13}, find all contiguous L-verse windows across all 114 surahs whose verse-letter-count sequence is a palindrome.
2. Compare count to a §1.2 null that shuffles verses within each surah (preserving the bag of verses) 10³ times.
3. Report counts and z-scores per L.

**Null model.** §1.2 verse-shuffle-within-surah (palindrome is a positional claim; bag is preserved).

**Acceptance criterion.** At least one L-value besides 7 shows excess palindromes with Holm-corrected p<0.01 across the 6 L values.

**Priority.** 🔴 **HIGH** — cheap, mechanical, directly extends the Ash-Shams finding. Existing data.

---

### H12 — Root-sequence palindrome scan (extends Q 13:28)

**Hypothesis.** The Q 13:28 root-sequence palindrome (dkr-Alh-Tmn-qlb) is one of K perfect root-sequence palindromes in the Quran where K is to be determined. K should be low (≤30) because root-sequence palindromes are structurally rare; those few that exist will cluster on verses whose content describes equilibrium, reflection, or cyclicality.

**Computational procedure.**
1. For each verse with ≥ 4 root-bearing stems, extract the root sequence.
2. Check if it's a palindrome (identity on reverse, ignoring unique roots that appear only once at the ends).
3. Report the full list plus semantic tag per verse.

**Null model.** §1.2 bag-of-roots shuffle within verse (preserve stem count and root multiset, shuffle order) 10³ times.

**Acceptance criterion.** Count of perfect root-palindrome verses exceeds 95th percentile of null; AND the verses are enriched for reflection/equilibrium semantic tags vs base rate.

**Priority.** 🟡 **MEDIUM** — the existing jinas-wordplay CSV probably already has most of this; may just need a re-filter pass.

---

### H13 — Word-level palindromes across word boundaries

**Hypothesis.** The Q 5:73 finding — the 8-letter palindrome *thālithu thalāthatin* spanning a word boundary inside the Trinity-condemnation verse — generalizes. A systematic scan for 4+ letter palindromes spanning word boundaries (ignoring whitespace) will find additional hits, and these hits will be enriched for rhetorically marked positions (condemnations, oaths, paradoxes).

**Computational procedure.**
1. For each verse, concatenate words (strip whitespace), then scan for maximal palindromic substrings of length ≥ 4.
2. For each found palindrome, record (a) the verse; (b) whether it crosses a word boundary; (c) the rhetorical tag from Sahih.

**Null model.** §1.1 within-verse letter shuffle (10³ per verse). Count the expected number of length-≥4 palindromic substrings per verse under the shuffle.

**Acceptance criterion.** At least 5 new word-boundary-crossing palindromes on rhetorically marked verses, vs random baseline.

**Priority.** 🟢 **LOW** — noise risk is high but the existing palindromes file already has some infra.

---

## THEME 5 — Chronological / stylometric drift

### H14 — Per-surah Zipf α heterogeneity and its correlates

**Hypothesis.** The whole-Quran Zipf α=1.318 conceals significant per-surah variation. Each of the 114 surahs individually fits a Zipf distribution with its own α_s, and these α_s values CORRELATE with revelation order / Nöldeke phase. Specifically: Early Meccan surahs have α_s > 1.5 (more extreme vocabulary concentration, because oracular style repeats few theological terms) and Medinan surahs have α_s ≈ 1.1 (because legal prose uses a flatter vocabulary).

**Rationale.** The info-theory run computed the whole-Quran α but not per-surah. The diachronic-ramp run saw verse-length double across phases. If α also changes, that's a second independent diachronic signal and it illuminates the *content* of the drift (oracular → legal). This is the single best Liberman-voice hypothesis: use standard computational-linguistics fittings to test a historiographical claim.

**Computational procedure.**
1. For each surah with ≥ 30 lemma tokens, fit a Zipf distribution via OLS on log-rank vs log-frequency. Report α_s and R².
2. Plot α_s against Nöldeke phase and revelation order. Report Spearman ρ.
3. Cross-check by fitting α within length-matched bins of surahs (since Zipf α depends on sample size).

**Null model.** §1.5 permutation of revelation-order labels across surahs (10⁴). Does the observed ρ exceed 95th percentile?

**Acceptance criterion.** |Spearman ρ(α_s, revelation-order)| > 0.3 with empirical p<0.01 AND the length-controlled version still significant.

**Priority.** 🔴 **HIGH** — this is the cleanest Liberman-voice test in the queue. Existing data. Would be the first published Zipf-drift analysis of the Quran.

---

### H15 — Type-token ratio U-curve across chronology (Medinan bounce-back)

**Hypothesis.** The diachronic-ramp file showed TTR drops 0.722 → 0.456 → 0.370 → 0.453 across Nöldeke phases. The Medinan phase *rises* from Late Meccan. Is this U-shape real, significant, and attributable to specific vocabulary — namely Medinan-era legal/community vocabulary (kitāb, shahāda, dayn, waṣiyya, ʿamal)?

**Computational procedure.**
1. Compute TTR per surah at matched lemma counts (draw fixed N=200 lemmas from each, 100 resamples, mean TTR). This is the length-controlled TTR.
2. Compute Medinan-specific "new-lemma" lists (lemmas that first appear in Medinan phase).
3. Report whether those new lemmas are disproportionately legal/community-topic words.

**Null model.** §1.5 permutation of Nöldeke labels.

**Acceptance criterion.** Length-controlled TTR U-curve significant with corrected p<0.01 AND legal-community lemma enrichment > chance.

**Priority.** 🟡 **MEDIUM** — natural next step after the Nöldeke ramp finding.

---

### H16 — Proper-name entry-time curve

**Hypothesis.** "Muhammad" enters the Quran only at revelation position 89. Test whether other proper names (Maryam, Isa, Ibrāhīm, Mūsā, Nūḥ, Yūsuf, Sulaymān, Dāwūd, Hārūn, Lūṭ, Hūd, Ṣāliḥ, Yūnus, Luqmān, Dhū'l-Kifl) have chronological entry curves that cluster in distinct patterns: Old-Testament prophets enter EARLY (Meccan); Arabian prophets (Hūd, Ṣāliḥ, Shuʿayb) enter MIDDLE Meccan; Muhammad enters LATE (Medinan).

**Computational procedure.**
1. For each proper noun lemma, find the earliest revelation position (per Egyptian standard ordering).
2. Tag each by tradition (OT prophet, Arabian prophet, Muhammadan). Plot entry positions by category.
3. Test with Kruskal-Wallis.

**Null model.** §1.5 permutation of revelation-order labels over the 114 surahs, 10⁴ draws.

**Acceptance criterion.** Category-level entry-position distributions differ at corrected p<0.01.

**Priority.** 🟡 **MEDIUM** — natural extension of the Muhammad-89 finding. Existing data.

---

## THEME 6 — Muqatta'at internal structure

### H17 — Positional gradient within muqatta'at surahs

**Hypothesis.** Within a muqatta'at surah, the opening letters of that surah are MORE concentrated in the EARLY verses than in the LATE verses. I.e., the enrichment is front-loaded. This would explain why 3 surahs dominate the Stouffer Z: the front-loading effect is strong in those 3, weak elsewhere.

**Rationale.** The muqatta'at density finding has a 3-surah carrier (Q50, Q2, Q29). If the enrichment is *positional* (front-heavy), the "carrier" may actually be "surahs whose content is front-loaded on a particular topic that uses those letters" — e.g. Q50 opens with ق-heavy eschatology (*qiyāma*, *qurʾān*, *qawl*, *qarīb*).

**Computational procedure.**
1. For each of the 29 muqatta'at surahs, divide the surah into quartiles by letter position.
2. Compute opening-letter rate per quartile. Report gradient via linear fit or quartile-1 vs quartile-4 ratio.
3. Aggregate across surahs: is the mean gradient steeper than 0?

**Null model.** §1.1 within-verse letter-shuffle, with the surah's verses preserved (this preserves per-surah bag-of-letters but shuffles position). 10³ draws.

**Acceptance criterion.** Positive gradient significant across the 29 surahs under §1.1 null with empirical p<0.01.

**Priority.** 🔴 **HIGH** — this is the single test that would diagnose WHY the muqatta'at density effect exists. Existing data.

---

### H18 — Non-muqatta'at letter inverse effect

**Hypothesis.** If the 14 "luminous letters" are statistically over-used inside their muqatta'at surahs, the 14 "non-luminous" letters should be statistically UNDER-used inside those same surahs (by conservation of letter mass). Specifically: in Q50, the non-opening letters should be anti-enriched.

**Computational procedure.**
1. For each muqatta'at surah, compute chi² for (opening letters vs non-opening letters) vs (in-surah vs out-of-surah). Report the per-letter z-scores for both sides.

**Null model.** §1.3 letter-level 3-gram Markov surrogate, same one used in the original muqattaat-analysis run.

**Acceptance criterion.** Mean non-opening-letter z across the 29 surahs is significantly negative at p<0.01.

**Priority.** 🟡 **MEDIUM** — conservation sanity check. Would confirm or refute the "letter-accounting" interpretation. Existing data.

---

### H19 — Muqatta'at combination signature beyond opening letters

**Hypothesis.** Each unique muqatta'at combination (ALM, ALR, HM, etc.) has its own "signature letter" beyond the combination itself — a 15th letter that is statistically enriched inside surahs of that combo but not in other muqatta'at combos. E.g., the 6 ḤM surahs (Q40-46) might all have ج (jīm) or ف (fāʾ) over-enriched.

**Rationale.** This tests whether the muqatta'at encode additional information (combination-specific signature) or are just surface markers. Al-Rāzī's theory that muqatta'at = divine-name abbreviations would predict specific extra letters per combination.

**Computational procedure.**
1. For each combination with ≥2 member surahs (ALM, ALR, TSM, HM), compute the letter-frequency vector aggregated over member surahs.
2. Z-score each of the 28 letters against the combined frequency vector of all non-member surahs.
3. Report the top-enriched non-opening letter per combination.

**Null model.** §1.5 surah-index permutation across the 29 muqatta'at surahs.

**Acceptance criterion.** At least one combination has a non-opening signature letter with |z| > 3 and the same letter appears across ≥2 member surahs with the same sign.

**Priority.** 🟡 **MEDIUM** — al-Rāzī voice. Existing data.

---

## THEME 7 — Classical-scholar predictions operationalized

### H20 — Al-Rāzī's "muqatta'at = divine names abbreviation" theory

**Hypothesis.** Al-Fakhr al-Dīn al-Rāzī (d. 1209) proposed in *Mafātīḥ al-Ghayb* that the 14 muqatta'at letters are abbreviations of 14 divine names. If true, the 14 letters should collectively be able to compose (as initial letters) a subset of the 99 Names of Allah that is statistically enriched compared to random 14-letter subsets.

**Rationale.** The muqatta'at are theologically unique. Our team's data — the 14 luminous letters — lets us test Rāzī's specific claim computationally. The 99 Names of Allah are a fixed list (pre-Islamic to standard); check which ones have initial letters within the 14-luminous set.

**Computational procedure.**
1. For each of the 99 Names of Allah (using the standard Tirmidhī list), check if the initial letter is one of {ا ح ر س ص ط ع ق ك ل م ن ه ي}.
2. Compare to a random 14-letter subset of the 28-letter alphabet. Expected ≈ 99 × 14/28 = 49.5.
3. Also check the 14 NON-luminous letters. Expected 49.5.

**Null model.** §1.5 permutation of the 14-vs-14 letter split across the 28 alphabet.

**Acceptance criterion.** Observed luminous-initial-Names > 60 (20% excess) at p<0.01.

**Priority.** 🔴 **HIGH-SCHOLARLY** — this operationalizes a thousand-year-old classical theory. If it works, it's a headline "classical tradition was right, here's the math." If it fails, it's a clean refutation. Novel test. Existing data.

---

### H21 — Al-Suyūṭī's *Itqān* rare-word claims audit

**Hypothesis.** Al-Suyūṭī's *al-Itqān fī ʿUlūm al-Qurʾān* chapters 38-39 ("On the rare words of the Quran") list words whose occurrence the classical tradition noted as exactly-N or single. A systematic verification of his claims against QAC v0.4 will reveal (a) how accurate classical counting was, and (b) whether any of his claims are computationally MORE interesting than noted.

**Computational procedure.**
1. Acquire a digital copy of al-Itqān chapters 38-39 (literature-archivist task).
2. For each rare-word claim, extract the word + claimed count.
3. Verify against QAC.

**Null model.** Not applicable (replication task). Report per-claim accuracy.

**Acceptance criterion.** N/A — report verification percentage.

**Priority.** 🟡 **MEDIUM-SCHOLARLY** — depends on acquiring primary source. Scholarly value is high.

---

### H22 — The "kalām Allāh" self-reference density test

**Hypothesis.** The Quran refers to itself — as *kitāb*, *qurʾān*, *dhikr*, *tanzīl*, *furqān*, *kalām*, *āyāt*, *sūrah*, *hudā*, *nūr* — at a rate significantly higher than comparable classical Arabic texts refer to themselves. This self-reference density is a genuine distinguishing feature and can be quantified.

**Rationale.** The Quran's self-description as *raḥma li-l-ʿālamīn* and the rahma=114 finding suggest the text has metatextual density. Systematically quantify it: what fraction of Quranic verses contain a self-reference lemma? Compare to Bukhārī / Muwaṭṭaʾ (with quoted Quran stripped).

**Computational procedure.**
1. Pre-register a list of ~10 Quranic self-reference lemmas. Count all verses containing at least one.
2. Report: fraction of verses, length-normalized rate.
3. Acquire Bukhārī text. Strip quoted Quran via Quran-text matching. Count self-reference lemmas per 1000 verses.

**Null model.** §1.4 length-matched classical Arabic block. 10³ draws from Bukhārī of matching length.

**Acceptance criterion.** Quran rate > 99th percentile of Bukhārī-block null.

**Priority.** 🔴 **HIGH-SCHOLARLY** — this is a genuinely novel systematic quantification of a traditional theological claim. It also exercises the §1.4 stringent null we need to implement anyway for rahma-114. Needs cross-baseline corpus (literature-archivist task upstream).

---

## Summary — priority triage

| Priority | Hypothesis IDs | Data needed |
|---|---|---|
| 🔴 HIGH | H1, H2, H4, H6, H9, H11, H14, H17, H20, H22 | H1-H17 use existing data; H22 needs Bukhārī |
| 🟡 MEDIUM | H3, H5, H7, H10, H12, H15, H16, H18, H19, H21 | H21 needs al-Itqān PDF; others existing |
| 🟢 LOW | H8, H13 | existing |

**Sequence recommendation for the next mechanical wave:**
1. H4 (rahma-robustness, fastest sanity check; cheap gate on the headline)
2. H2 (count=surah scan, extends Yusuf finding)
3. H17 (muqatta'at positional gradient; diagnoses the muqatta'at carrier surahs)
4. H9 (prophet-pericope ring sweep; highest structural payoff)
5. H11 (palindrome length-sweep; extends Ash-Shams)
6. H14 (per-surah Zipf drift; the Liberman move)
7. H20 (al-Rāzī muqatta'at test; the classical-scholar move)
8. H1 (theological-lemma meaningful-N audit; the systematic version)
9. H22 (self-reference density vs Bukhārī; the stringent comparable-corpus test)

Running these 9 in this order gives tight coverage of (a) robustness of the headline finding, (b) systematic extension of 4 separate lineage-findings, (c) a classical-voice test, and (d) the first stringent comparable-corpus validation.
