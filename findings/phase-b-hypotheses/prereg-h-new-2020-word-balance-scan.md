---
id: H-NEW-2020
title: Exhaustive surface-word exact-frequency balance scan + curated antonym/complement-pair audit
phase: B
date_locked: 2026-05-29
status: pre-registered
seed: 20260509
n_perm: 0
family: candidate-pattern-generator (surface-word; complement to root-based H-NEW-2010)
---

# H-NEW-2020 — Pre-registration

## Position in the program

The famous "balanced-word" claims popularised in modern iʿjāz literature
(e.g. ʿAbd al-Razzāq Nawfal, *al-Iʿjāz al-ʿadadī li-l-Qurʾān al-karīm*, 1980s;
and the widely-circulated "dunyā occurs 115 times = ākhira occurs 115 times")
are claims about **surface words**, not roots. They count specific orthographic
forms, not all morphological derivatives of a root. This test builds the
**surface-word** candidate-pattern generator (the root-based generator is the
sibling H-NEW-2010) and applies it in two parts:

1. an EXHAUSTIVE scan of every content-word pair that balances exactly, with a
   permutation/random-pair null measuring how *expected* exact balances are; and
2. a CURATED audit of ~13 famous antonym / complementary word-pairs under two
   pre-locked rules (strict-word vs all-surface-forms).

This is partly a CLASSICAL-CLAIM AUDIT (protocol §2.9): per-pair the test is an
integer-equality check (count-A == count-B), which is sharp and needs no
p-value; the EXHAUSTIVE part is the statistical component and carries the null.

## Hypothesis (DIRECTION-LOCKED before recording verdicts)

**H1 (composite, the headline).** Among the ~13 curated antonym/complement
pairs, **SOME balance exactly under SOME defensible rule, but the MAJORITY do
NOT.** Operationalised: the number of curated pairs that balance exactly (under
*either* the strict-word rule *or* the all-surface-forms rule) is **strictly
fewer than half** of the curated pairs (i.e. ≤ 6 of 13). The famous "perfect
balance of the Quran's vocabulary" thesis is therefore **selective** — it
survives by choosing which pairs to advertise and which counting rule to apply
per pair.

- Direction: **fewer-than-half balance.** If ≥ 7 of 13 balance under at least one
  rule, that is a pre-commit-violating reversal and is published as a NULL /
  reversal with full prominence (it would mean the balance thesis is broader
  than I predicted).

**H2 (the dunyā/ākhira flagship, direction-locked).** The single most-cited
claim — *al-dunyā* (الدنيا) occurs the same number of times as *al-ākhira*
(الآخرة) — is **FALSIFIED at the strict surface-word level**: the two strict
standalone forms have **unequal** counts. Direction: `count(الدنيا) ≠ count(الآخرة)`.
(If they are in fact equal at the strict level, that is a reversal published as
such.)

**H3 (the exhaustive-scan null).** Exact-count balance between two arbitrary
content words is **common, not rare**: among random content-word pairs drawn
from the same frequency band, a large fraction collide on an identical integer
count purely because the count axis is a small set of integers shared by many
words. Operationalised: the observed number of exact-balance pairs in the
corpus is **not** more extreme than a random-pairing null (one-sided
permutation p > 0.05 for "fewer balances than chance"); i.e. exact balance is a
generic property of any large word-frequency distribution and carries **no**
special signal. This reframes every individual "balanced pair" anecdote as
cherry-picking from a sea of equally-balanced uninteresting pairs.

## Pre-committed rules-tuple

Default project tuple `(no-tashkeel, orthographic-token, words, basmala-counted-
only-in-Q1, Hafs-Kūfan, Mashriqī)`.

- **Corpus**: `quran-text/quran-no-tashkeel.json` (primary, Hafs).
- **Tokenisation**: Unicode NFC normalise → strip Qurʾānic pause/annotation
  signs in the range U+06D4 … U+06ED (these are recitation marks, not letters)
  → whitespace split → drop empty tokens. This yields the standard ~77,797-token
  orthographic word count.
- **Counting unit**: surface-word *type* frequency (a `word → count` map).
- **Basmala**: encoded as Q 1:1 only in the JSON; counted there (no double count).

### Rule S — strict-word

A pair `(A, B)` *balances* iff `count(exact-string A) == count(exact-string B)`,
where A and B are the **single canonical surface form** named for each concept
below (typically the definite-article form, which is the form used in the
famous claims). No prefixed / suffixed / inflected variants are summed.

### Rule F — all-surface-forms (closed pre-locked allow-list)

A pair balances iff `Σ count(forms of A) == Σ count(forms of B)`, where the
form-sets are the **closed, pre-locked allow-lists** specified below (built by
substring inspection of the corpus BEFORE locking; the lists are fixed here and
no form may be added or removed after SHA-lock). Rule F is the permissive
upper-bound: it deliberately conflates derivational and inflectional variants of
the same surface concept (it does **not** go to the root — that is H-NEW-2010).
A homograph-collision caveat is logged where a substring also matches an
unrelated lexeme (e.g. `شر` "evil" vs `شرك` "associating-partners"); Rule F
allow-lists are hand-pruned to the target lexeme only.

## Pre-committed curated pairs and form-lists (LOCKED)

For each pair I lock (a) the strict canonical form for Rule S, and (b) the
closed Rule-F allow-list. Verdict per pair under each rule is `BALANCED` (counts
equal) or `UNBALANCED`.

1. **dunyā / ākhira** (world / hereafter)
   - S: `الدنيا` vs `الآخرة`
   - F-dunyā: {`الدنيا`} (the corpus has no other surface form of this lexeme)
   - F-ākhira: {`الآخرة`,`الآخر`,`بالآخرة`,`والآخرة`,`الآخرين`,`آخر`,`آخرين`,`وآخرون`,`وآخرين`,`وآخر`,`وللآخرة`,`وبالآخرة`,`آخره`,`بآخرين`,`آخران`,`فآخران`,`وآخرنا`,`آخرون`,`للآخرين`,`والآخرين`,`والآخر`,`للآخرة`}
     (NB: this set conflates "hereafter", "last", and "other(s)" — the homograph
     caveat is explicit; it is the maximal pro-balance reading.)

2. **jannah / nār** (paradise / fire)
   - S: `الجنة` vs `النار`
   - F-jannah: {`الجنة`,`جنة`,`جنات`,`وجنات`,`جنتان`,`جنتين`,`الجنتين`,`وجنة`,`بجنة`,`لجنات`,`فجنة`,`وجناتٍ`} (paradise sense only; prunes جناح "wing", جند "troops", جن "jinn", سجن "prison", مجنون "possessed")
   - F-nār: {`النار`,`نار`,`نارا`,`بالنار`,`فالنار`,`والنار`,`ناركم`,`نارهم`,`النارين`}

3. **jannah / jahannam** (paradise / hell)
   - S: `الجنة` vs `جهنم`
   - F-jannah: same as pair 2
   - F-jahannam: {`جهنم`,`لجهنم`,`بجهنم`,`وجهنم`,`فجهنم`}

4. **malāʾika / shayāṭīn** (angels / devils)
   - S: `الملائكة` vs `الشياطين`
   - F-malāʾika: {`الملائكة`,`والملائكة`,`للملائكة`,`ملائكة`,`وملائكته`,`بالملائكة`,`ملائكته`,`الملائكةُ`}
   - F-shayāṭīn: {`الشياطين`,`والشياطين`,`شياطينهم`,`شياطين`,`للشياطين`} (plural devils only; the singular الشيطان is a separate lexeme tier and is NOT summed under shayāṭīn-plural)

5. **ḥayāt / mawt** (life / death)
   - S: `الحياة` vs `الموت`
   - F-ḥayāt: {`الحياة`,`حياة`,`حياتنا`,`بالحياة`,`حياتكم`,`لحياتي`,`والحياة`,`حياتهم`,`وحياة`} (the *noun* ḥayāt only; verbal أحيا/يحيي forms excluded as a separate lexical layer; logged)
   - F-mawt: {`الموت`,`موتها`,`موته`,`موتكم`,`موتهم`,`بالموت`,`والموت`,`موتا`} (the *noun* mawt only; verbal يموت/مات and the noun الموتى "the dead" / الميت excluded; logged)

6. **khayr / sharr** (good / evil)
   - S: `خير` vs `شر`
   - F-khayr: {`خير`,`خيرا`,`الخير`,`الخيرات`,`بخير`,`وخير`,`بالخير`,`الخيرة`,`للخير`,`والخير`,`بالخيرات`,`خيرات`} (prunes يتخيرون/تخيرون "choose")
   - F-sharr: {`شر`,`الشر`,`شرا`,`شرر`,`أشرار`,`الأشرار`,`شركم`,`بشر?`} → pruned to the evil-sense only: {`شر`,`الشر`,`شرا`,`بشر`,`شرر`,`أشرار`} **with explicit homograph caveat**: `شر` shares its skeleton with the heavily-attested شرك "associating-partners" / بشر "human / glad-tidings" / حشر "gathering" families, which are EXCLUDED. (sharr is genuinely rare as the evil-noun.)

7. **īmān / kufr** (faith / disbelief)
   - S: `الإيمان` vs `الكفر`
   - F-īmān: {`إيمانا`,`الإيمان`,`إيمانكم`,`إيمانهم`,`بالإيمان`,`للإيمان`,`إيمانها`,`إيمانه`,`والإيمان`,`بإيمانكم`,`بإيمانهم`,`بإيمان`,`بإيمانهن`} (the *noun* īmān only; verbal آمن/يؤمن "believe" forms are a separate huge family, EXCLUDED; logged)
   - F-kufr: {`الكفر`,`كفر`,`كفرا`,`بالكفر`,`بكفرهم`,`وكفر`,`وكفرا`,`كفره`,`للكفر`,`كفرهم`,`الكفار` ? } → pruned to the *kufr-noun + finite-kufr-verb-stem* would explode; for parity with īmān-noun we lock the **noun** sense only: {`الكفر`,`كفر`,`كفرا`,`بالكفر`,`وكفر`,`وكفرا`,`كفره`,`للكفر`,`بكفرهم`,`كفرهم`} (verbal كفروا/يكفر EXCLUDED for parity; logged)

8. **hudā / ḍalāl** (guidance / misguidance)
   - S: `الهدى` vs `الضلال`
   - F-hudā: {`هدى`,`الهدى`,`وهدى`,`بالهدى`,`فهدى`,`هداي`,`لهدى`,`والهدى`,`للهدى`} (the guidance-noun hudā; prunes أهدى/يهدى comparative/verbal)
   - F-ḍalāl: {`ضلال`,`الضلال`,`الضلالة`,`ضلالا`,`ضلالتهم`,`ضلالك`,`ضلالهم`,`وضلال`} **with homograph caveat**: the skeleton `ضل` collides massively with فضل "bounty/favour"/الفضل which are EXCLUDED; the *noun* ḍalāl/ḍalāla only is summed (verbal ضل/يضل EXCLUDED for parity).

9. **nūr / ẓulumāt** (light / darkness[es])
   - S: `النور` vs `الظلمات`
   - F-nūr: {`النور`,`نور`,`نورا`,`والنور`,`نوره`,`ونور`,`نورهم`,`بنورهم`,`لنوره`,`بنور`,`نوركم`,`ونورهم`,`نورنا`} (prunes التنور "the oven", نورث "we inherit")
   - F-ẓulumāt: {`الظلمات`,`ظلمات`,`كظلمات`,`وظلمات`,`بالظلمات`} (the darkness-PLURAL noun only; the verbal ظلم "wronged" / ظالم family is a different lexeme, EXCLUDED, homograph caveat logged)

10. **ṣayf / shitāʾ** (summer / winter)
    - S: `الصيف` vs `الشتاء`  — NB the only attestation of ṣayf in the corpus is
      `والصيف` (with wāw, Q 106:2); the strict S form `الصيف` does NOT occur, so
      under Rule S ṣayf has count 0. The famous pair therefore needs Rule F.
    - F-ṣayf: {`الصيف`,`والصيف`,`صيف`,`صيفا`}
    - F-shitāʾ: {`الشتاء`,`شتاء`,`وشتاء`,`بالشتاء`}

11. **ḥarr / bard** (heat / cold)
    - S: `الحر` vs `البرد`
    - F-ḥarr: {`الحر`,`حر`,`حرا`,`وحر`,`بالحر`} **with homograph caveat**: skeleton
      `حر` collides with البحر "sea"/الحرام "sacred"/حرث/سحر/ساحر etc — ALL EXCLUDED;
      only the heat-noun ḥarr is summed (genuinely rare).
    - F-bard: {`بردا`,`برد`,`بردهن`,`البرد`,`وبرد`} (cold-sense; prunes بريد etc — none present)

12. **rajul / nisāʾ** (man / women)
    - S: `الرجل` vs `النساء`  — NB the strict singular `الرجل` count and the
      strict `النساء` count.
    - F-rajul: {`رجل`,`الرجل`,`رجلا`,`لرجل`,`فرجل`,`ورجل`,`الرجال`,`رجال`,`رجالا`,`رجالكم`,`للرجال`,`وللرجال`,`فرجالا`,`برجال`,`رجلين`,`رجلان`,`الرجلين`} (the human-male noun, sing+plural+dual; prunes رِجل "foot": أرجلكم/أرجلهم/رجلك/برجلك EXCLUDED — these are the *foot* lexeme, homograph caveat logged)
    - F-nisāʾ: {`النساء`,`نساء`,`ونساء`,`نساءكم`,`نساءهم`,`وللنساء`,`والنساء`,`ونساءنا`,`ونساءكم`,`نساءنا`,`نساءهن`}

13. **qul / qālū** (say-imperative / they-said)
    - S: `قل` vs `قالوا`
    - F-qul (imperative + its wa/fa-prefixed): {`قل`,`وقل`,`فقل`} (the *imperative*
      "say!"; prunes قلوبهم "their hearts", قليل "few", قلنا "we said" etc — all
      different lexemes/forms; only the bare imperative qul)
    - F-qālū (3pl perfect + prefixed): {`قالوا`,`وقالوا`,`فقالوا`,`لقالوا`}

## Pre-committed exhaustive-scan protocol

1. Build the full `word → count` map over the cleaned corpus.
2. **Content-word filter**: exclude a pre-locked closed stop-list of high-
   frequency function words / particles (prepositions, conjunctions, pronouns,
   relative/demonstrative particles). The stop-list is fixed in the script
   constant `STOPWORDS` BEFORE SHA-lock. Also exclude any token of length ≤ 2
   graphemes (overwhelmingly particles) and any token with corpus count = 1
   (hapax legomena form a trivial mega-cluster of mutual "balances" that would
   swamp the scan; reported separately as a count, not as pairs).
3. Among the surviving content words with count ≥ 2, group by count value;
   report, for each count value c, how many content-word *types* share it
   (`balance multiplicity`). The number of unordered exact-balanced pairs is
   `Σ_c C(n_c, 2)`.
4. **Null (H3)**: hold the multiset of content-word counts fixed but ask whether
   the *number of distinct count-values* (hence the collision structure) is
   anomalous. Permutation null (seed 20260509, 10000 draws): draw the same
   number of content-word types, assign each a count by sampling WITH the same
   empirical count-frequency distribution but RE-LABELLED (i.e. shuffle which
   lexeme gets which count, preserving the count histogram). Because shuffling
   labels cannot change the count histogram, the number of balanced pairs is
   invariant under this shuffle — therefore the *informative* null is the
   alternative: compare the corpus count-histogram's collision rate to that of a
   **geometric/Zipf reference** of the same size and support, asking whether the
   Quran has MORE or FEWER exact-balances than a generic Zipfian vocabulary of
   equal size. Pre-locked statistic: `frac_types_in_a_collision` (the fraction
   of content-word types that share their count with ≥ 1 other type). H3
   predicts the Quran's value is statistically indistinguishable from the Zipf
   reference (|z| < 2), i.e. balance is generic.
5. Report the 25 highest-multiplicity count-values and a sample of "famous-
   looking" balanced content-word pairs the scan throws up at random, to make
   the cherry-picking point concrete.

## Verdict scheme

- **H1**: count curated pairs balancing under (S OR F). PASS-DIRECTED if ≤ 6 of
  13. Reversal (published as such) if ≥ 7.
- **H2**: PASS-DIRECTED if `count(الدنيا) ≠ count(الآخرة)` strict. Reversal if equal.
- **H3**: PASS-DIRECTED if |z(frac_types_in_a_collision vs Zipf-ref)| < 2
  (balance is generic). Reversal if the Quran has *significantly fewer*
  collisions than Zipf (which would make exact-balance a genuine rarity worth
  explaining).

## Pre-commit violations / stop conditions

- No form may be added to or removed from any Rule-F allow-list after SHA-lock.
- The H1 threshold (≤ 6) and H2 direction (≠) and H3 band (|z|<2) are locked.
- If any curated pair's verdict is post-hoc relaxed by inventing a third
  counting rule to manufacture balance, that pair becomes NULL with explicit note.
- Integer-equality verdicts are sharp; no Bonferroni on the 13 per-pair checks.
  The only statistical test is H3, single test, α = 0.05.

## Constants (locked)

```
SEED        = 20260509
N_PERM      = 10000
PAUSE_RANGE = range(0x06D4, 0x06EE)          # Qurʾānic recitation marks
H1_THRESH   = 6                              # ≤6 of 13 balance ⇒ PASS
CURATED     = 13 pairs as enumerated above (S form + F allow-list each)
STOPWORDS   = closed particle list, fixed in script
```

## Data dependencies

- `quran-text/quran-no-tashkeel.json` — primary corpus

## Output schema

`findings/phase-b-hypotheses/csv/h-new-2020.json`:
```
{
  "id":"H-NEW-2020", "prereg_sha":"<runtime>", "seed":20260509,
  "corpus_token_count": int, "distinct_types": int,
  "curated": [ {"pair":..., "concept_A":..., "concept_B":...,
                "S_count_A":int,"S_count_B":int,"S_balanced":bool,
                "F_count_A":int,"F_count_B":int,"F_balanced":bool,
                "balanced_under_any":bool, "note":...}, ... ],
  "curated_balanced_count": int, "H1_threshold":6, "H1_verdict":"...",
  "dunya_akhira_strict": {"الدنيا":int,"الآخرة":int,"equal":bool}, "H2_verdict":"...",
  "exhaustive": {"content_types_ge2":int, "n_exact_balanced_pairs":int,
                 "frac_types_in_collision":float, "zipf_ref_frac":float,
                 "z":float, "top_multiplicity_counts":[...],
                 "random_famous_looking_pairs":[...]}, "H3_verdict":"...",
  "verdict": "..."
}
```

## Honest limits

1. **Surface-form lists are hand-built.** The Rule-F allow-lists were assembled
   by substring inspection of the corpus and pruned for homographs by hand. They
   are pre-locked, but a different analyst could draw slightly different
   boundaries; the homograph caveats document the contested forms. This is the
   *point* of the test: the famous balance claims live or die on exactly these
   discretionary boundary choices.
2. **Noun-vs-verb parity choices.** For ḥayāt/mawt, īmān/kufr, hudā/ḍalāl,
   nūr/ẓulumāt I locked the *noun* layer for both sides (excluding the verbal
   families) to keep the two sides of each antonym comparable. A different,
   defensible choice (include verbs on both sides) would change counts; the JSON
   reports the strict noun layer, and the verbal-inclusive figure is out of scope.
3. **The dunyā=ākhira=115 legend.** The popular claim asserts BOTH equal 115.
   `الدنيا` is indeed 115 (a real corpus fact). Whether `ākhira` reaches 115
   depends entirely on which forms are summed — this test makes that dependency
   explicit rather than asserting a coincidence.
4. **H3 reference model.** Comparing to a Zipf/geometric reference is one of
   several defensible nulls; it is pre-locked as the single H3 test. The deeper
   claim — that exact integer-count balance is generic in *any* large word-
   frequency table — is a near-mathematical certainty, and the Zipf comparison
   only quantifies the magnitude.

*Locked 2026-05-29. Directions: H1 ≤6-of-13; H2 ≠ (strict unequal); H3 |z|<2.
SHA computed and embedded post-write.*
