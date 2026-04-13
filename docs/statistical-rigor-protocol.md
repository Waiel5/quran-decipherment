# Statistical Rigor Protocol

**Owner:** `stats-rigor` agent
**Date:** 2026-04-12
**Status:** v1 — mandatory for every Phase A replication and every Phase B novel finding
**Scope:** any numerical claim about the Quranic text, replicated or novel

> The goal of this protocol is to make it *hard* to get a false-positive result, and
> *impossible* to get one without disclosing the forks that led to it. If a claim
> cannot survive this protocol, we do not publish it as a finding. We report the
> failure with the same prominence as a success.

---

## 0. Prior art we are grounding this in

1. **Witztum, Rips & Rosenberg, 1994, Statistical Science 9(3), 429–438** — "Equidistant Letter Sequences in the Book of Genesis." The original Bible Codes paper. Claimed that the names of famous rabbis were clustered, via ELS search, near their dates of birth/death in Genesis at p ≈ 1.6 × 10⁻⁹. Passed peer review at a top statistics journal.
2. **McKay, Bar-Natan, Bar-Hillel & Kalai, 1999, Statistical Science 14(2), 150–173** — "Solving the Bible Code Puzzle." The definitive refutation. Showed the Witztum result depended on:
   - undisclosed **degrees of freedom in selecting word forms and appellations** (the "wiggle room" was enormous; tuning it recovered almost any desired signal);
   - **surrogate-text controls** (War and Peace) producing equally "miraculous" results once the same tuning freedom was granted;
   - a **post-hoc proximity metric** that was not pre-registered;
   - a **list of names** constructed after inspecting the text.
   This paper is the methodological gold standard for debunking religious-text numerology. Read it before designing any test on the Quran.
3. **Gelman & Loken, 2013** — "The garden of forking paths: Why multiple comparisons can be a problem, even when there is no 'fishing expedition' or 'p-hacking' and the research hypothesis was posited ahead of time." Even an *honest* researcher who makes counting-rule choices conditional on the data inflates false positives. This is the dominant failure mode in pattern-hunting research.
4. **Benjamini & Hochberg, 1995, JRSS-B 57, 289–300** — FDR. The reasonable default for large families of tests.
5. **Holm, 1979, Scand. J. Statist. 6, 65–70** — Holm step-down; strictly more powerful than Bonferroni while preserving FWER.
6. **General computational stylometry on natural-language null models** — Kilgarriff 2005 ("Language is never, ever, ever, random") on why word-frequency data fail naive IID tests, and the shuffle / n-gram Markov-surrogate tradition (see e.g. Baayen 2001, *Word Frequency Distributions*) for length-matched comparable-corpus controls.
7. **Bender-Saebø et al. and subsequent Code-19 debates** — Rashad Khalifa's original 1974 claims and the extensive Arabic-language rebuttals. These have *never* been subjected to a McKay-style formal refutation in the peer-reviewed literature. This is a research opportunity: **Quranic numerology has not received the treatment Bible Codes got**, and the Phase A replication catalog can fill that gap.

---

## 1. Null models, in increasing order of stringency

A null model answers: "If the text were 'like this' but otherwise random, how often would we see a statistic at least as extreme as the observed one?" Every null model has a specific null hypothesis attached. Choosing the wrong null is the same mistake as forgetting to choose one.

### 1.1 Character-shuffle within the same verse

- **What it is.** Randomly permute the letter graphemes inside each verse, keeping verse boundaries fixed.
- **Null hypothesis tested.** "The observed pattern is no better than chance given the letter composition and verse-length distribution of the text."
- **Controls for.** Total letter frequencies in each verse, overall letter frequencies, verse lengths, surah lengths, basmala placement, the number and identity of verses.
- **Does NOT control for.** Word structure, bigram/trigram frequencies, root cohesion, morphology, diacritic patterning.
- **When it's appropriate.** First-pass sanity check on a letter-level claim (e.g. Code-19-style alleged letter counts in the huroof muqatta'at surahs). It is the **weakest** letter-level null and rejection here is uninformative; *failure to reject* here is a serious red flag because the claim must at minimum beat letter-composition noise.
- **Implementation.** For each verse independently, `np.random.shuffle` the grapheme array after orthography has been fixed. Repeat 10⁴–10⁶ times.

### 1.2 Word-shuffle within the same surah

- **What it is.** Randomly permute the order of words within each surah, keeping surah boundaries and word identities fixed.
- **Null hypothesis tested.** "The observed pattern is no better than chance given the bag of words in each surah."
- **Controls for.** Per-surah word frequencies, total word count, number of surahs, surah-level word inventory, verse count (if we also preserve verse lengths) — optionally also verse boundaries.
- **Does NOT control for.** Syntax, collocation, root distributions *between* surahs, semantic clustering.
- **When it's appropriate.** Claims about positional adjacency of specific words within a surah (e.g. "word X appears N verses before word Y"), counts of specific lemmas within thematic units, symmetry claims.
- **Caveat.** A claim based on *total word counts per surah* is **invariant under this null** — the statistic doesn't change because the bag is preserved — so word-shuffle is not a valid test of counts. Use it only for *positional* statistics.

### 1.3 n-gram-preserving Markov surrogates (n = 2, 3)

- **What it is.** Estimate a letter-level or word-level Markov chain of order n−1 from the real text, then generate surrogate "texts" of matching length.
- **Null hypothesis tested.** "The observed pattern is no better than chance given the local co-occurrence statistics (up to n-grams) of the text."
- **Controls for.** Everything 1.1 and 1.2 control for, PLUS local bigram/trigram frequencies, pronounceability, typical morphological cluster shapes.
- **Does NOT control for.** Long-range structure, semantics, syntax beyond n, specific lexeme identities across long distances.
- **When it's appropriate.** Claims about letter-level distributions (huroof muqatta'at counts, Code-19 letter totals), claims about gematric sums (whose distribution under a unigram null is trivially wrong because letters aren't IID).
- **Implementation.** Use Katz/Good-Turing or simple additive smoothing; report the order and the smoothing. For letters, 3-gram is the right default because Arabic triliteral roots give strong 3-letter structure. For words, 2-gram is usually enough because word-level 3-grams in a corpus this size are severely sparse.

### 1.4 Length-matched random selection from a comparable Arabic corpus

- **What it is.** Draw a block of running text of matching letter/word length from a classical Arabic corpus of the same register, compute the same statistic, repeat.
- **Null hypothesis tested.** "The observed pattern is no better than chance given **real classical Arabic prose of comparable length and register**."
- **Controls for.** Realistic morphology, realistic root distributions, realistic word lengths, realistic sentence-level structure — things no synthetic null can produce.
- **Does NOT control for.** Genre differences (Quranic register is distinctive), meter/rhythm of the text, deliberate authorial craft of any kind (the comparison texts themselves have their own crafts).
- **Comparable-corpus candidates (in rough order of decreasing rigor):**
  1. **Early hadith collections** — Sahih al-Bukhari, Sahih Muslim, Muwatta Malik. Closest register, closest vocabulary, closest date. Strongest control but with residual quoted-Quran contamination that must be stripped before use.
  2. **Classical poetry diwans** — Mu'allaqat, pre-Islamic poetry collections. Closer in date, different register (poetry vs prose), rich in archaic vocabulary.
  3. **Early prose** — Ibn Ishaq's *Sīra*, Tabari's *Tarikh*. Chronologically later but prose register. Again, strip quoted Quran.
  4. **Classical Arabic Wikipedia / modern standard Arabic** — WORST match, avoid unless we have nothing else; only useful as a rough sanity floor.
- **Implementation.** For each surrogate draw, sample a random start index in the comparable corpus and take a contiguous block equal in length to the statistic's scope (surah, whole Quran, specific verse set). Repeat 10³–10⁴ times. Record draws as a function of which corpus was used; never pool.
- **Why it's the stringent one.** This null eats the common complaint "but Arabic just works that way." If a pattern survives against real comparable Arabic, the claim that "it's an Arabic thing" is falsified.

### 1.5 Permutation tests across surah indices

- **What it is.** Randomly permute which surah gets which index (1–114), or which surah gets which length, or which surah gets which position in the mushaf. Recompute the statistic.
- **Null hypothesis tested.** "The observed ordering/indexing pattern is no better than chance given the set of surahs."
- **Controls for.** All surah-internal structure (you haven't touched a single letter), the set of surah lengths, the set of surah contents. Tests *only* the ordering/indexing claim.
- **When it's appropriate.** Any claim of the form "surah N has property P where N has some numerical relationship" — e.g. "surah length is a decreasing function of index," "prime-indexed surahs sum to X," "surah 19 specifically has property Y." These are pure ordering claims and this is the right null.
- **Implementation.** Sample uniformly from the 114! permutations of surah indices (in practice 10⁴–10⁶ random permutations is enough). Report exact p-value as rank of observed statistic.
- **Sharpen.** If the claim is specifically about *mushaf order*, the null is uniform over permutations. If the claim is specifically about *revelation order* (tartib nuzuli), use permutations of the revelation-order labels, noting that tartib nuzuli is itself contested and must be cited.

### 1.6 Choosing a null — decision tree

```
Is the claim about letter-level composition?
  ├── Yes → 1.1 (sanity), 1.3 (primary), 1.4 (stringent)
  └── No
       ├── Is it about word positions within surahs?
       │    └── 1.2 (primary), 1.3 word-level (secondary), 1.4 (stringent)
       ├── Is it about word/lemma totals?
       │    └── 1.3 word-level (primary), 1.4 (stringent)
       │         NOTE: 1.2 is invalid here; counts are invariant.
       ├── Is it about surah ordering or indexing?
       │    └── 1.5 (primary), 1.4 (only if claim also involves content)
       └── Is it about gematric sums?
            └── 1.3 letter-level (primary), 1.4 (stringent)
                 NOTE: 1.1 is almost useless here because the sum is
                 approximately invariant under letter permutation within a verse.
```

Every finding must pass **at least two** nulls from different rows of this tree.

---

## 2. Multiple-comparison protocol — the Bible-Codes trap

The single sentence that summarizes McKay et al. 1999: *"Give me 100 degrees of freedom and I will find you a miracle in War and Peace."* We defend against this at three levels.

### 2.1 Pre-registration

**Before any data is touched for a given hypothesis, the following must be committed to git:**

- the **rules tuple** (orthography, word definition, letter definition, basmala policy, verse numbering, abjad table, gematria variant);
- the **exact statistic** to be computed (a named function, not a verbal description);
- the **null model(s)** to be used and the number of surrogate draws;
- the **p-value threshold** after correction;
- the **exclusion criteria** (e.g. "we drop verses where X because Y");
- the **stopping rule** (how many draws, or what effective-sample-size threshold);
- a **text description** of the hypothesis in one sentence.

Pre-registration lives as a markdown file under `findings/phase-b-hypotheses/pre-reg/<slug>.md`, committed to git *before* the data-touching script is run. The commit hash is cited in the finding write-up. We check the commit timestamp against the results timestamp. If pre-reg postdates the result, the finding is demoted to "exploratory" and loses its p-value.

### 2.2 Corrections

Every finding report must specify which correction applies and why:

- **Bonferroni** (α/k) — used when k is small (≤ 20) and we want FWER control. Conservative but interpretable.
- **Holm-Bonferroni step-down** — default FWER correction for families of > 5 tests. Strictly more powerful than Bonferroni.
- **Benjamini-Hochberg FDR** — default when k is large (≥ 50) and we can tolerate a controlled false-discovery rate instead of strict FWER. Report q-value alongside raw p.
- **No correction** is permissible *only* when the pre-registration specified exactly one test. That "one test" must be named and its rules tuple committed.

The family, k, must include **every test we ran on this data**, not just the ones that worked. We keep a running per-phase test register (`findings/phase-b-hypotheses/test-register.md`) that every finding increments. The multiple-comparison family for any finding is "all tests in this register at the time of the finding."

### 2.3 Garden-of-forking-paths disclosure section

Every finding write-up carries a mandatory section with this heading:

```markdown
## Garden of forking paths disclosure

### Choices made after seeing the data
- <list every counting-rule choice that was decided after looking at any numbers>

### Alternative rule tuples considered and discarded
- <every rule tuple we *could* have chosen, with the count it would have produced>

### Sibling hypotheses considered
- <every hypothesis we looked at in the same sitting, with their p-values>

### Why this one and not those
- <honest answer; "because it was significant" is a red flag, not an answer>
```

If any of these sections is empty, we ask a human reviewer to certify that it really is empty. An empty disclosure on a finding that took a week of work is a lie by omission.

---

## 3. What counts as a finding

A claim is a **finding** only if *all* of the following hold:

1. **Rule tuple pre-registered.** The counting rules were committed to git before the data was touched. Commit hash cited.
2. **Two independent nulls.** The observed statistic has a corrected p-value below threshold under at least two null models drawn from different rows of the §1.6 decision tree.
3. **Corrected p-value thresholds:**
   - **Replication (Phase A):** raw p < 0.01 AND corrected p < 0.05. Replications have a smaller family and thus milder correction, but we still require a raw threshold at least as good as what the original claim asserted.
   - **Novel finding (Phase B):** corrected p < 0.005 under the registered correction family, AND the effect size must be large enough to be visible without fine-tuning (we report effect size always, not just p).
   - **"Revolutionary" finding:** corrected p < 0.001 under both nulls AND robustness under §3.5 below. We will be conservative about calling anything revolutionary.
4. **No retrofitting.** The rule tuple that produced the count must match the pre-registered tuple exactly. Any mid-stream rule change voids the pre-registration and the finding becomes exploratory.
5. **Robustness under at least one alternative.** The same claim must still hold (possibly with a weaker p) under at least one of:
   - an alternative orthography variant (e.g. the claim is made on min-tashkeel; it should also hold on no-tashkeel or Uthmani rasm);
   - an alternative verse-numbering scheme (Warsh, Basran, Damascene);
   - an alternative word-definition (with vs without clitic splitting) or letter-definition (hamza collapsed vs distinct).
   A claim that only works under one arbitrarily-chosen rule tuple, and breaks under every nearby alternative, is almost certainly an artifact of that specific rule. Bible-Codes claims had exactly this brittleness.

---

## 4. Red flags — claims we reject without running the test

These are disqualifiers. Encountering any one of them in a literature claim puts it straight in the "likely artifact" pile, and we replicate it only to document the artifact.

- **Post-hoc rule selection.** The claimant tried multiple counting conventions and kept the one that worked, without disclosing the others.
- **Undisclosed counting conventions.** The claim reports a number but not how the number was computed. No rules tuple → no finding.
- **Non-canonical text without disclosure.** Using a text variant that differs from the Hafs-Kufan standard (or a hand-edited version) without declaring it.
- **Non-standard verse numbering without disclosure.** Using Warsh, Basran, or an idiosyncratic split/merge without declaring it.
- **p-values without a null model.** A bare "p < 0.001" with no specification of what random process it's computed against. This is meaningless.
- **Brittleness under inflection.** A claim that the count of the exact form يَوْم is meaningful, but breaks completely if you include يَوْمَ, يَوْمِ, أَيَّام, الْيَوْم. Morphology is not noise; choosing one surface form out of many *is* a fork and needs disclosure.
- **Cherry-picked temporal horizon.** "The word 'day' appears 365 times, matching the solar year." But: which definition of day? Which definition of year (solar tropical 365.2422, sidereal 365.2564, Gregorian civil 365/366, Islamic lunar 354/355)? If the "matched" number only lines up with *one specific* astronomical definition that the Quran itself doesn't privilege, that's a fork.
- **"Hidden meanings" without a reproducible algorithm.** If we can't reimplement the computation in code and get the same number, it isn't a claim, it's a gesture.
- **Appeal to numerological coincidence without a null.** "19 is special because…" followed by N examples chosen from unlimited candidates.
- **Refusal to enumerate siblings.** If we ask "what about all the other words/numbers/surahs you could have chosen" and the answer is "but this one is special," the claimant has ducked the forking-paths question.
- **Counts that don't reproduce.** A claim whose numbers we can't reproduce from the raw text under any rule tuple we can think of, and whose original computation isn't open-sourced.

---

## 5. Worked example — the Day/Night word count claim

**Claim (paraphrased from the popular-apologetics literature):** the word *al-yawm* (الْيَوْم, "the day") occurs 365 times in the Quran, and the word *al-layl* (اللَّيْل, "the night") also occurs a specific number matching a solar-year-related quantity, and this encodes the length of the year. Sometimes attributed to Abdul-Razzaq Nawfal (1959, *al-I'jaz al-'adadi lil-Qur'an al-Karim*); revived by many secondary sources.

We will not run this test yet (data shape investigation still pending from `text-shape` agent). We **sketch the experimental design** here so the team can execute it later under pre-registration.

### 5.1 Explicit rules tuple (to be pre-registered before any count is run)

```yaml
rules:
  orthography: min-tashkeel            # primary; full-tashkeel as robustness alt
  word_definition: orthographic-token  # primary
  alternatives_to_test:
    word_definition:
      - orthographic-token
      - with-clitics-split             # splits off the al-
      - lemma                          # requires QAC morphology
      - dictionary-headword
    inflectional_scope:
      - exact-surface-form             # only الْيَوْم exactly
      - with-case-variants             # يَوْمَ, يَوْمِ, يَوْمٌ
      - with-definite-indefinite       # يَوْم and الْيَوْم both
      - with-plural                    # أَيَّام and variants
      - all-root-y-w-m                 # any surface form derived from root ي و م
  verse_numbering: hafs-kufan
  basmala_policy: counted-in-surah     # does not affect this particular count
  abjad_table: not-applicable
  null_model: 1.3-word-level AND 1.4-comparable-corpus
```

The forking-paths question this exposes: *depending on which row of `inflectional_scope` we pick, we get five different counts.* The literature picks whichever one equals 365. That is a fork, and the pre-registration forces us to compute **all five** and report them all, not just the one that works.

### 5.2 Statistic

Define a function `count(surface_form_filter, inflection_scope, orthography)` that returns the number of tokens in the whole Quran matching the filter under the chosen scope. The observed statistic is the **5×2 matrix** of (inflection scope × word sense {day, night}). We report all 10 cells. We do **not** privilege the cell that equals 365.

### 5.3 Null hypothesis and null models

- **Primary null (1.3 word-level, order-2 Markov surrogate).** We generate surrogate Quranic-length texts from a word-level bigram model estimated from the Quran itself. For each of 10⁵ surrogates we compute the same 10-cell matrix. We compare the observed matrix cell-by-cell to the surrogate distribution; we report an empirical p-value for each cell.
- **Stringent null (1.4 length-matched classical Arabic).** We draw blocks of 77,430-ish whitespace tokens (Hafs min-tashkeel Quran length, to be locked after `text-shape` returns) from a combined early-hadith corpus (Bukhari + Muslim, with quoted Quran stripped). Repeat 10⁴ times. For each, compute the 10-cell matrix. Report the empirical cell-wise p-value.

The null hypotheses they test:
- *Primary:* "The observed count is no higher/lower than expected given the Quran's own word bigram statistics." Rejection means "the whole-Quran count deviates from what local word-level co-occurrence predicts." This is a mild null but any Code-19-style claim should at minimum beat it.
- *Stringent:* "The observed count is no higher/lower than expected for a classical Arabic prose block of the same length and register." Rejection is the serious result. Even here, a "yes" doesn't prove intent — it proves statistical distinctiveness.

### 5.4 Multiple-comparison correction

10 cells × 2 nulls = 20 tests. With Holm-Bonferroni at α=0.05 the threshold for the smallest raw p is 0.05/20 = 0.0025. We'd want the actual strongest cell (the one the claim is about) to survive this even after we've also tested its 9 siblings. If the claimant's cell is the only one that hits 365, and every sibling cell is far away and non-distinctive, we record that as a negative result for the claim even if the single cell is nominally significant — **because the choice of that cell is itself the fork**, and we've now tested the fork family.

### 5.5 Robustness requirement

Even if one cell produces a significant corrected p, the finding is not accepted unless:
- the same cell is significant under both the 1.3 and 1.4 null;
- the same cell is significant under at least one alternative orthography (min → full or min → no tashkeel);
- the ratio of day-count to night-count is reported as an effect size, not the raw equality.

### 5.6 Garden-of-forking-paths disclosure to be filled in advance

```markdown
## Garden of forking paths disclosure

### Choices made after seeing the data
- (none — pre-registered)

### Alternative rule tuples considered and discarded
- all 10 cells of the day×night × inflection-scope matrix are reported; none are discarded
- all 4 word-definition alternatives are reported

### Sibling hypotheses considered
- "shams" (sun) vs "qamar" (moon) count parity — 2 cells
- "sana" (year) and related 4 cells
- generic temporal nouns and their cross-ratios — N cells

### Why this one and not those
- this test is the replication target; siblings are documented in the test register
  as Phase B hypotheses with their own pre-registrations
```

### 5.7 Likely outcome (guess, to be falsified by running the experiment)

Based on the McKay-style intuition that these claims typically break under inflection-scope variation, we expect:
- the exact-surface-form count for *al-yawm* ≠ 365;
- some *inflection-scope* choice produces 365 for *al-yawm*, and the literature silently picked that one;
- the parallel *al-layl* count under the "correct" scope does not match any year-like quantity;
- none of the 10 cells survives both nulls after Holm correction.

We commit to reporting this outcome regardless of which direction it goes.

---

## 6. Research opportunity flag

Quranic numerology — and Code-19 in particular — has never been subjected to a McKay-style peer-reviewed refutation. The existing rebuttals are mostly in Arabic-language religious-studies journals and don't use modern null-model methodology. **A formal, McKay-style, statistically literate audit of the dominant Quranic numerology claims is an unfilled niche in the peer-reviewed literature.** This project's Phase A can produce exactly that artifact, and we should write it up as a methodological paper once the catalog is complete. We should cite McKay et al. 1999 as our methodological template and be explicit that we are applying the same standards to a different religious text.

---

## 7. Checklist (paste into every finding write-up)

- [ ] Rules tuple pre-registered in git; commit hash cited
- [ ] Exact statistic implemented as a named function with tests
- [ ] Primary null model (§1.x) run with ≥ 10⁴ surrogates
- [ ] Second null model (different §1.x row) run
- [ ] Multiple-comparison correction applied, family size k disclosed
- [ ] Raw p, corrected p, effect size all reported
- [ ] Robustness under at least one alternative rule tuple reported
- [ ] Garden-of-forking-paths disclosure section filled (not empty)
- [ ] Red-flag checklist (§4) run; any hits explained or finding demoted
- [ ] Test register (`findings/phase-b-hypotheses/test-register.md`) incremented
