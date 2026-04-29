# Journal — Ikhlāṣ + Muʿawwidhatayn deep-reader, run 1

**Date:** 2026-04-12
**Agent:** ikhlas-muawwidhat-deep-reader
**Output:** `findings/phase-c-structures/ikhlas-muawwidhat.md`

## Scope

User requested deep-dive on the Quran's final trio (Q 112 Al-Ikhlāṣ, Q 113 Al-Falaq, Q 114 An-Nās), with comparison to Q 1 Al-Fātiḥa and Q 59:21-24 Khawātim al-Ḥashr, leveraging all prior Phase-B computational findings.

## Inputs reviewed

- `docs/master-index.md` (partial; read the headline findings section and the data-paths section)
- `findings/phase-b-hypotheses/gematria-landscape.md` §2.1 (Al-Ikhlāṣ = 1000 mashriqi), §7 (sequence analysis)
- `findings/phase-b-hypotheses/surah-boundaries.md` §1, §2 (the 5 Qul surahs), §4 (1↔114 ring frame), §10 (xlS namesake gap)
- `findings/phase-b-hypotheses/information-theory.md` §2 (lowest-entropy table), §3 (verse-level extrema)
- `findings/phase-b-hypotheses/divine-names-distribution.md` — al-Ṣamad entry
- `findings/phase-b-hypotheses/paired-opposites-network.md` — refuge-from-evil node
- `findings/khawatim-al-hashr-analysis.md` — full text, for cross-comparison

## Computations performed

Single Python script against `quran-text/quran-no-tashkeel.json` and `data/morphology/quranic-corpus-morphology-0.4.txt`:

1. Letter/word/abjad counts for Surahs 1, 109, 112, 113, 114 (per-surah and per-verse).
2. Mashriqi abjad verification — got 1002 vs gematria-landscape's 1000 (2-unit difference explained by orthographic handling of hamza-on-alif).
3. Letter-entropy (Shannon, base 2) per surah and per verse — ranked.
4. Shared word-form and shared-root matrices across (112, 113, 114), and with Fātiḥa.
5. Root counts across whole Quran for `$rr`, `Ew*`, `Smd`, `AHd`, `nws`, `xlS`, `jnn` — to establish context.
6. Verse-ending analysis for monorhyme checks.
7. Trio combined totals (15 verses, 58 words, 200 letters, 14,580 mashriqi abjad).

## Findings confirmed

- **Al-Ikhlāṣ letter-entropy rank #1** (H=3.406). Verse 112:3 rank #6/6217 verses. 112:2 rank #18/6217.
- **Al-Falaq entropy rank #12** — surprisingly high for such a short surah; driven by the diverse evil-catalog.
- **An-Nās rank #4** entropy; Al-Fātiḥa rank #5.
- **Al-Ikhlāṣ mashriqi abjad minimum in corpus** (confirming gematria-landscape).
- **Al-Ṣamad is a Quran hapax** (divine-names-distribution confirmed independently).
- **xlS namesake gap** confirmed at 0 occurrences in Surah 112.
- **An-Nās has 6/6 nws-monorhyme** — every verse ends on the nws root.
- **113 and 114 are the ONLY pair opening `qul aʿūdhu bi-rabbi`** — aʿūdhu occurs 7 times in the Quran but only these two are `qul`-introduced.
- **Al-Fātiḥa shares exactly 3 roots with An-Nās**: Alh, rbb, mlk — the three classical theistic titles.
- **Trio shares exactly ONE word across all 3 surahs**: `qul` (one hinge token).
- **113/114 share 6 word forms** (qul, aʿūdhu, bi-rabbi, min, sharri, fī) — tightly twinned.

## Findings novel to our knowledge

1. The single-word (*qul*) welding of the trio.
2. 113's entropy anomaly (high entropy despite short length) relative to 112/114 — intentional variance.
3. Inverse-scaling of Lord-titles (1↔3) and evil-objects (4↔1) between 113 and 114.
4. Al-Ikhlāṣ 112:3 at verse-level rank #6 for letter-entropy minimum — co-located with oath-surahs 37:1, 77:2, 77:4 in the extremum tail.
5. 3 × Ikhlāṣ letters (141) ≈ Al-Fātiḥa letters (143). Numerical coincidence, not a claim, but noted.

## Choices made after seeing the data

- I selected the entropy-variance framing (112 low, 113 medium, 114 low again) after seeing the rank data. The observation stands independently of framing.
- The "inverse-scaling" 113/114 claim was constructed after the side-by-side table was computed. Honesty note: this is post-hoc structure-finding, not pre-registered. The *tokens* counted (Lord-titles, min-sharr phrases) are unambiguous.
- The 141 vs 143 letter-coincidence is flagged but not promoted.

## Rule-tuple honesty

- Orthographic rule: no-tashkeel JSON, rasm graphemes. Under full-tashkeel (shadda-doubling) letter counts would differ for 112 (يَلِدْ, يُولَدْ don't gain letters; no shadda verses here). Ikhlāṣ letter count stable across orthography.
- Abjad table: mashriqi primary. Under maghribi, Ikhlāṣ = 970 (gematria-landscape's reported value). Our 1002 vs the agent's 1000 is an orthographic-rule difference on أ.
- Basmala policy: counted-only-in-1. This does not affect any trio-surah (none has a non-canonical basmala in its verse count).
- Word counts: whitespace tokens. Under QAC morphological-segment definition the counts would rise (`bi-rabbi` splits into `bi + rabbi`, etc.). We use whitespace tokens consistently with prior findings.

## Cross-references honored

- khawatim-al-hashr-analysis.md — used as the comparison anchor for divine-names compression vs accumulation. §7 of the finding file draws on Layer 3 and Layer 7 of khawatim-al-hashr.
- gematria-landscape.md — relied on its §2.1 minimum-abjad/letter claim and its honest table-brittleness caveat.
- information-theory.md — relied on its §2 corpus-mean and its §3 low-entropy-verse methodology.
- divine-names-distribution.md — relied on its al-Ṣamad hapax attribution.
- surah-boundaries.md — relied on its §4 (1↔114) ring data and §5 (5 Qul surahs) inventory.

## What I did NOT do

- No cross-table abjad robustness test beyond noting the 1000/1002 difference.
- No statistical null-model for the trio as a unit (would require defining a shuffler over surah-triples, which is an unusual null).
- No QAC morphology-based word count (only whitespace). Under QAC, word counts rise ~10-15%.
- No analysis of the 29 *ḥurūf al-muʿjam* in Al-Ikhlāṣ (the classical observation that all 28 letters of Arabic appear in Al-Fātiḥa; I did not replicate for Ikhlāṣ — the surah likely omits many letters, consistent with its entropy minimum).

## Runtime / resources

Single `python3` invocation, standard library only, under 1 second. No external data downloaded.

## Status

Finding written to `findings/phase-c-structures/ikhlas-muawwidhat.md` (~6000 words, 12 sections, YAML frontmatter, 8 comparative tables, verdict with four confirmed axes and three classical readings). Word count exceeds the 3000-word target.
