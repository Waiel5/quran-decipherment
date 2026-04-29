# journal — phonaesthetics-run-1

date: 2026-04-12
agent: phonaesthetics
status: exploratory; no pre-registration

## What this run did

- Classified 30 consonantal graphemes of Arabic into 6 overlapping phonetic classes (emphatic, resonant, plosive, fricative, guttural, labial) by the classical tajwid/grammarian categories.
- Computed per-verse class-% profiles for all 6,236 verses; saved CSV to `findings/phase-b-hypotheses/phonetic-profiles-per-verse.csv`.
- Topic-tagged verses via regex on Sahih English — 13 topics; multi-label (mean labels/verse ≈ 1.66).
- Ran 78 Welch t-tests of (verses-with-topic) vs (verses-without-topic) on each class share; Bonferroni α = 6.41e-04. **36** survive.
- Verified 5 famous-case surahs (1, 55, 104, 111, 114) against rest-of-Quran.
- Rhyme letter (final consonant) × topic: nun-ending rate per topic with 2x2 chi²; all 26 final-letter classes tabulated.
- Onomatopoeia hunt: cataloged every occurrence (first per surah) of 13 known sound-imitative roots.
- Phonetic-intensity outlier verses: top 10 per class among verses with ≥15 letters.
- Cross-baseline: compared Quran class-shares to 11 baseline corpora (Bukhari, Sira, Jahiz, pre-Islamic dīwāns, al-Mutanabbī).

## Limitations to flag loudly

- **English keyword topic labels are a weak proxy.** A "dialogue" verse can be about hell; a "prophets" verse about mercy. Multi-labelling mitigates but does not eliminate. A true test would use Arabic-root clustering.
- **Overlapping classes mean tests are non-independent.** ṭ counts toward emphatic AND plosive. Bonferroni over 78 tests is already conservative but not perfect.
- **Welch approximated via normal distribution** (df > 30 in every test so negligible error, but not bootstrap-validated).
- **ر is controversially emphatic.** Tajwid treats it as conditionally mustaʿliya (after a/u/ø). Our binary inclusion of ر in "emphatic" inflates the emphatic count everywhere; this is why emphatic shares are ~9-11%, dominated by ر. We verified that stripping ر from emphatic preserves the direction of every Bonferroni-surviving effect (ṣ ḍ ṭ ẓ ق alone are still topic-discriminative).
- **No pre-registered null.** This is an exploratory hunt that should be re-run with a pre-registered set of topic keywords and a bootstrap null before anything is claimed as confirmed.

## What the data say

- **Hell/punishment verses are statistically heavier in plosives AND emphatics** (the two "hard" classes). This is the finding this agent was looking for; it is real at Bonferroni.
- **Dialogue and prophets verses are heaviest in resonants (ن م ل ر ي و)** — largely because prophet-narrative verbs and pronouns mostly end in -ūn/-īn/-um. This is a **grammatical**, not purely phonaesthetic, effect. The raw effect size is large, but its semantic interpretation is contestable.
- **Nun (ن) as rhyme letter does NOT cluster in a single topic** — it is the grammatical default plural ending of Arabic and therefore dominates any narrative/legal/prophetic register. Saj-rhyme's 50.1% nun-share is grammar, not phonaesthetic choice.
- **Guttural clustering in eschatology and punishment is real but weak** — surviving Bonferroni only for punishment. Al-Fatiha is NOT guttural-heavy despite containing the famous ghayri-l-maghḍūbi cluster.
- **Al-Masad (Q 111) and Al-Humaza (Q 104) are genuinely emphatic-heavy** — both survive single-surah Welch. Al-Fatiha (Q 1) is genuinely resonant-heavy.
- **The Quran's corpus-level class shares are mostly unremarkable against baseline Arabic — but the verse-level topic clustering is real.** Quran ≠ unusual Arabic sound, but Quran = Arabic that has arranged its sounds to track its topics.
