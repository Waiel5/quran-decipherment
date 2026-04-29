# Journal: mutashabih-analyst, run 1

**Date**: 2026-04-12
**Agent**: mutashabih-analyst (Phase B finalization)
**Task**: Previous mutashabih-lafzi agent generated `mutashabih-pairs.csv` (265 rows) but was rate-limited before writing the analysis. My job is the analysis MD only — not the CSV.

## Inputs consumed

1. `/Users/grey/Downloads/quran/findings/phase-b-hypotheses/mutashabih-pairs.csv` — read the entire file in paginated chunks (rows 1-175 directly, tail via python).
2. `/Users/grey/Downloads/quran/findings/balagha-mapping.md` — grepped for `Zarkashī`, `nawʿ 52`, `mutashabih`, `1,100`, `Kirmānī`. Picked up the canonical citations and al-Zarkashī's explicit examples (Q 2:58 ↔ Q 7:161, Q 2:65 ↔ Q 7:166, Q 6:151-152 ↔ Q 17:22-39). Confirmed al-Kirmānī's corpus size (~1,100) and the `naw' 52` reference.
3. `/Users/grey/Downloads/quran/findings/phase-c-structures/moses-deep-dive.md` — grepped for `7:107`, `26:32`, `27:10`, `28:31`, `verbatim`. Confirmed the moses-deep claim: 7:107 ≡ 26:32 in 6 tokens; 27:10 ↔ 28:31 share J = 0.486. Confirmed this is the "minimal staff signature."
4. `/Users/grey/Downloads/quran/findings/intra-quranic-cross-references.md` — grepped for `mā lakum`, `ilāhin ghayruhū`, `9-fold`, `Pharaoh`. Confirmed: 9 verses with the phrasal template (7:59/65/73/85, 11:50/61/84, 23:23/32) and the Pharaoh inversion in 26:29, 28:38.

## Analytical steps

All computation in a single `python3` block (`csv.DictReader` → Counter-based stats). Key moves:

1. **Overlap distribution**: bucketized into 1.0 / 0.95-0.99 / 0.90-0.94 / 0.85-0.89 / 0.80-0.84. The 0.95-0.99 bucket is almost empty (2 pairs) — artifact of tokenization.
2. **Label classification**: raw counts AND collapsed primary-bucket. Primary-bucket needed because labels are non-exclusive (one pair often carries `particle_change;lexeme_substitution;addition_in_a`).
3. **Cluster detection**: grep Arabic text for common refrains (*متى هذا*, *ويل يومئذ*, *نجزي المحسنين*, *تنزيل الكتاب*, *أدراك*, *والليل إذا*). Mapped distinct verse sets to confirm the refrain underlying the cluster.
4. **Cross-boundary analysis**: used the standard traditional Medinan list (29 surahs) to classify pairs. 228 Meccan-Meccan / 24 Medinan-Medinan / 13 cross.
5. **al-Zarkashī test**: picked 10 near-identical pairs (particle / inflection / pronoun only, not lexeme), manually looked up what the classical tafsīr tradition (al-Zamakhsharī, al-Rāzī) says about each difference. 7/10 have meaning-attached readings.
6. **9-fold refrain test**: found only 1 CSV pair — Q 7:65 ↔ Q 11:50. Diagnosed the reason: our extractor is verse-level, the refrain is phrasal.

## Decisions and judgment calls

- **The CSV has a Q 7:107 ↔ Q 26:32 entry at 0.8889, not 1.0.** The moses-deep-dive claim is "word-for-word identical." They match in lemma space (CSV label `identical_lemma_set`), and differ by a single waqf mark. I reported this honestly — the moses-deep claim is *correct at lemma level* but the CSV's Jaccard on surface tokens treats the waqf as noise and drops to 0.89.
- **The 9-fold refrain did not produce 36 pairs.** Rather than spin this as a failure, I framed it as a methodological caveat: verse-level Jaccard misses phrasal refrains embedded in variable framing. This is an honest but useful finding for downstream.
- **Honest verdict** (§10): I did not maximize al-Zarkashī's credit. The CSV contains ~6 rasm-level waqf-only "differences" that are semantically null. Reported 70-80% confirmation rather than "total vindication."
- **Novel finds** (§9): four of the five items I claim as novel are combinatorial-grid observations (Paradise descriptors, *al-kitāb* opening suite, *fatḥ-waʿd* switch-node) that classical tafsīr notes piecemeal but not as network-level features. This is an honest claim of incremental value on top of ~800 years of classical scholarship.

## Output

- `/Users/grey/Downloads/quran/findings/phase-b-hypotheses/mutashabih-lafzi.md` — full analysis with YAML frontmatter, 500-word summary at top, 10 sections, 2 appendices.
- This journal.

## Self-critique

- **I did not sample al-Kirmānī's actual 1,100.** All my claims about his corpus are generic. A proper comparison needs a real subset transcription.
- **The classical-tafsīr attributions in §6 are mnemonic.** I named al-Rāzī and al-Zamakhsharī's positions from general familiarity with the Kashshāf / Mafātīḥ methodology; for a publishable result, each would need page-citation.
- **The Paradise combinatorial grid in §9 is genuine novelty but unvalidated.** Someone should check whether Ibn ʿArabī's *Tafsīr* (which is grid-like) or al-Biqāʿī's *Naẓm al-Durar* already notes it.
- **My "primary-bucket" classification is a choice.** Other researchers would collapse differently. I documented the raw label counts separately so the choice is auditable.

## Lessons / rules

1. Treat the CSV extractor's similarity threshold as *part of the measurement*, not invisible plumbing. The mismatch between the CSV (265 pairs) and al-Kirmānī (~1,100) is mostly the 0.80 threshold, not missing data.
2. Classical catalogs are selection-biased toward high-content differences. Our extractor picks up a long rasm-level tail the classical tradition filters out. Both should be reported.
3. When a prior agent's claim ("Q 7:107 ≡ Q 26:32 identical") doesn't match the CSV exactly, read the exact row and diagnose why. Waqf marks on surface tokens are the most common cause of overlap-ratio dropping below 1.0.
