# Journal — razi-muqattaʿat-divine-names run 1

**Date:** 2026-04-13
**Agent:** razi-muqattaat-divine-names
**Task:** Operationalize al-Rāzī's per-letter divine-name abbreviation theory
(H20-extended): for each muqaṭṭaʿāt letter in each host surah, test whether
the classically-assigned divine name's letters are density-enriched inside
the host surah AND whether the name itself appears more often as a word
token in that surah than elsewhere in the Quran.

## Commits / artifacts

- Write-up: `findings/phase-b-hypotheses/razi-muqattaʿat-divine-names-test.md`
- Script: `scratch/razi-muqattaat-divine-names/run_test.py`
- Per-claim CSV: `scratch/razi-muqattaat-divine-names/claim_results.csv`
- Run log: `scratch/razi-muqattaat-divine-names/run.log`

## Rules tuple (locked, pre-registered)

```yaml
rules:
  orthography: no-tashkeel (quran-text/quran-no-tashkeel.json)
  word_definition: not-applicable (letter-level / whole-word regex)
  letter_definition: graphemes; hamza variants→ا; ى→ي; ة→ت; ؤ→و; ئ→ي;
                      recitation marks U+06D6..U+06ED excluded
  basmala_policy: counted-only-in-surah-1
  verse_numbering: hafs-kufan (6236 verses)
  abjad_table: not-applicable
  null_model: two-proportion z (primary) AND 1000-permutation shuffle-null
              over 14 muqaṭṭaʿāt letters (secondary, pre-registered)
```

## Procedure recap

1. Extracted 78 classical letter→name claims from the existing project
   extract `data/literature/classical-tafsir/razi-99names-extract.md` + 
   al-Suyūṭī *al-Durr* 4/679 on Q. 19:1 + al-Qurṭubī on Q. 2:1 / 20:1 / 26:1.
2. For each claim computed:
   (a) density z = two-prop z for the grapheme set of the name's
       radical (post-ال) in host surah vs rest-of-Quran;
   (b) token z = two-prop z for the word token of the full ال-prefixed name
       in host surah vs rest-of-Quran, using curated divine-names-by-verse.csv
       primary (fallback to regex on cleaned text for non-canonical names);
   (c) shuffle null z distribution: 1000 permutations assigning the name to
       a random luminous letter and its host surah.
3. Bonferroni at α = 0.05 / 78 = 6.41e-4.
4. Inverse test: rank canonical-99 names per muqaṭṭaʿāt surah by
   coverage of opening letters; check whether al-Rāzī's claims appear in
   top-5.

## Headline result

- **Density-Bonferroni (over): 7 / 78**
- **Token-Bonferroni (over):   1 / 78** (trivial: S3/Allāh)
- **BOTH:                        1 / 78**  ← acceptance required ≥ 5 → FAIL
- **Shuffle-null Bonferroni:   0 / 78**  ← under proper null, zero support
- **Inverse test hit-rate: 12/29 surahs (41.4%)**, but driven entirely by
  Allāh (ا) and single-letter muqaṭṭaʿāt; al-Rāzī's actually-interesting
  name choices (al-Laṭīf, al-Majīd, al-Ḥamīd, al-Ḥalīm, al-Qādir, al-Kabīr,
  al-Hādī) have zero top-5 hits.

## Verdict

**H20-extended: REJECTED at the strict, pre-registered acceptance criterion.**
The per-claim form of al-Rāzī's divine-names theory fares no better than the
aggregate form tested in the earlier H20 run. The ʿilm al-ḥurūf tradition's
abbreviation reading is devotionally coherent but not statistically detectable
in the text.

## Notable sub-findings

1. Every nominally-significant density claim has a shuffle-null upper-p
   between 0.02 and 0.28 — none survive Bonferroni correction under a null
   that properly controls for the letter-frequency overlap between divine
   names and muqaṭṭaʿāt openings.
2. Ibn ʿAbbās's KHYAS decomposition (ي→al-Amīn) was already
   orthographically inconsistent in the classical source — al-Amīn begins
   with alif, not yāʾ. The classical tradition itself did not defend strict
   matching.
3. The S42 (HMASQ) HMAFSQ decomposition is the strongest looking on density
   (3 of 5 letter-claims nominally over-represent), but zero survive the
   shuffle null, and no token enrichment exists.
4. S50 (Qaf) / al-Qādir: the famous surah, al-Rāzī's paradigm case for the
   "ق is a divine-name abbreviation" reading, produces density z=+3.77 but
   shuffle-null upper-p=0.275 — entirely consistent with the null.

## Multiple-comparison / test register increment

Adds **+78 tests** (1 per (surah, letter, classical-name) pre-registered
claim) to the Phase B test register. Note that all 78 were pre-registered
together as one classical-theory audit; the family-size for Bonferroni in
the write-up is 78.

## Links

- Master-index row updated (REJECTED entry added under tier "Replication
  audits (Phase A)" table, adjacent to the existing H20 aggregate entry).
- Parent muqaṭṭaʿāt density finding (muqattaat-analysis.md) is unaffected;
  this was an independent test of a specific classical interpretation
  layered on top.

## Prior art consulted (WebSearch)

- Welch (1981 EI2 art. "al-Kurʾān" §4.d)
- Massey (1996 Arabica 43/3)
- Rippin (2001 Qurʾān and its Interpretative Tradition ch. XI)
- Wikipedia Muqaṭṭaʿāt (2024 version)

No modern scholar has operationalized al-Rāzī's specific letter→name
assignments at the (surah, letter, name) granularity with a pre-registered
shuffle null; this appears to be the first such audit.
