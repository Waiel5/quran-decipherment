---
id: H-NEW-74
title: "qul" (قل = Say!) imperative — comprehensive corpus distribution
status: PRE-REGISTERED 2026-04-15
spec_locked_at: 2026-04-15 (extractor + tests locked BEFORE any per-surah inferential analysis; allowed to consult QAC structure and the verified total count of 332 from prior `imperative-run-1` work)
bonferroni_family: 2026-04-15-Wave-H-NEW-74-Qul-Distribution
bonferroni_k: 6
alpha_bon: 0.05 / 6 ≈ 0.00833
rules_tuple: (no-tashkeel, hafs-kufan, canonical-114, Tanzil-JSON for verse text, Leeds-QAC-v0.4 for morphology, qul := token with QAC features POS:V|IMPV|LEM:qaAla|2MS)
primary_data: /Users/grey/Downloads/quran/data/morphology/quranic-corpus-morphology-0.4.txt (canonical morphological identification of qul)
verse_text_data: /Users/grey/Downloads/quran/quran-text/quran-no-tashkeel.json
chronology: /Users/grey/Downloads/quran/data/revelation-order.csv
verse_counts: /Users/grey/Downloads/quran/data/hafs-verse-counts.tsv
seed: 20260417
author: h-new-74-specialist
prior_work_consulted:
  - findings/phase-b-hypotheses/csv/imperatives-qul-catalog.csv (332-token catalog from imperative-run-1)
  - findings/phase-b-hypotheses/h-new-61-opening-words.md (qul-opener finding: 5 surahs open with qul-IMPERATIVE class)
  - quotation-analysis.md (332 qul datum)
---

# [[h-new-74-qul-distribution|H-NEW-74]] — qul (قل = "Say!") Comprehensive Distribution

## Questions (operationalised)

1. **Verify total count is 332** under canonical QAC filter
   `POS:V|IMPV|LEM:qaAla|2MS`.
2. **Per-surah distribution** — which surahs use qul most/least?
   Density per 100 verses; identify top-10 and bottom-N (zero-qul surahs).
3. **Surahs that OPEN with qul** — surah-initial qul (v1, w1) and "fast-opening" qul
   (within first 3 verses). Catalogue and check for sub-corpora.
4. **Pattern in addressee context** — what kind of speech-act follows qul?
   The bare 2MS imperative is to the Prophet; what is the Prophet asked to say?
   Tabulate the immediate next 1–3 tokens (frame: *qul + X*) and identify
   high-frequency formulae (e.g. *qul yā ayyuhā…*, *qul aʿūdhu…*, *qul huwa…*,
   *qul innamā…*, *qul li-…*, *qul law…*, *qul hal…*).
5. **Correlation with surah type** — is qul-density higher in
   (a) Meccan vs Medinan, (b) Mufaṣṣal short surahs vs long, (c) surahs that
   contain explicit dialogue with kuffār?

## Classical anchor

al-Suyūṭī's *al-Itqān* and al-Zarkashī's *al-Burhān* both treat the
*qul-corpus* as the Prophet's didactic-dialogic register: the moments where
the divine voice instructs the Prophet to articulate a position in his own
voice. Classical scholars (Ibn ʿAbbās via Ṭabarī, Rāzī) explicitly note
that *qul aʿūdhu* (Q 113, 114), *qul huwa Allāhu aḥad* (Q 112), and *qul
yā ayyuhā l-kāfirūn* (Q 109) form the **muʿawwidhāt + ikhlāṣ + kāfirūn
tetralogy** — the four short surahs whose RECITATIONAL identity is bound
to qul itself. The Itqān ratifies a popular figure of "332 qul"
(matched, Sufi tradition adds, by 332 *qālū*).

## Garden-of-forking-paths disclosure (BEFORE running)

Pre-known surahs that open with qul (memorisation): Q 109 al-Kāfirūn,
Q 112 al-Ikhlāṣ, Q 113 al-Falaq, Q 114 al-Nās. The [[h-new-61-opening-words|H-NEW-61]] paper also
found Q 72 al-Jinn opens with qul (after no muqaṭṭaʿāt). I therefore
expect **5 surahs** to open with qul at (v1, w1), not the task-prompt's
"4". This expectation is locked HERE before re-running the extractor.

Pre-known qul-density expectation: Q 6 al-Anʿām is the canonical "qul
surah" (commonly cited as containing the most qul commands in the
corpus). I expect Q 6 to top the per-surah count and Q 10 Yūnus, Q 3
Āl-ʿImrān, and Q 17 al-Isrāʾ to be in the top 5.

Pre-known absences: Mufaṣṣal short surahs that DO open with qul are
exactly four of the very last surahs (Q 109, 112, 113, 114 — the "say-tetra")
plus Q 72 al-Jinn; *most* short Mufaṣṣal surahs (Q 78–108, Q 110, 111) do
NOT contain qul at all. The Meccan early surahs (Q 73, 74, 96 etc.) likely
have low qul-density (different register: *yā ayyuhā / iqraʾ /
sabbiḥ-ism-rabbika*, not *qul*).

These are KNOWN before running tests; they bias only the directional
priors, not the test-statistic computations, which are mechanical from
the locked QAC filter.

## Locked extractor (frozen HERE)

For each line in QAC v0.4 morphology file:
1. Parse location (sid:vid:wid:pid).
2. Test predicate `'POS:V' in features AND 'IMPV' in features AND
   'LEM:qaAla' in features AND '|2MS' in features` (each as substring of the
   tab-delimited features field). All four must be present.
3. Record (sid, vid, wid, pid, surface_token) into the qul-catalog.

**This is the canonical definition.** Bare surface-string قل matching is
NOT the canonical definition (it under-counts because of fa-/wa- prefixes
that morphologically still carry the IMPV+2MS+qaAla features but
surface-merge with the prefix). Surface-string matching gives 294 (bare
قل) + 21 (وقل) + 18 (فقل) = 333 in our independent test, which is +1 over
the canonical 332 — the discrepancy is one position where a surface قل
is morphologically NOT qaAla-IMPV-2MS (e.g. inside a quotation frame).

## Locked test cells (Bonferroni k = 6, α_bon ≈ 0.00833)

### Cell 1 — Total count verification (descriptive + control)
Compute `total_qul = |{(s,v,w,p) : QAC line has POS:V & IMPV & LEM:qaAla
& 2MS}|`. PASS if `total_qul == 332`. Hard equality test against the
prior literature (imperative-run-1 + Quranic Arabic Corpus public count).
This is the **MW-control**: if it disagrees with 332, the morphology
file or extractor is broken.

### Cell 2 — Per-surah distribution (descriptive)
Tabulate qul count per surah. Compute density per 100 verses. Report
top-10 and bottom-N (including surahs with zero qul). PUBLISHED.

### Cell 3 — Surah-initial and fast-opening qul (descriptive + structural)
- `OPENERS_V1_W1` = surahs with qul at (v1, w1) — predicted set is
  {72, 109, 112, 113, 114}.
- `FAST_OPENERS` = surahs whose FIRST qul appears within the first 3
  verses (v ≤ 3) — extends the OPENERS_V1_W1 set.
- Verify the {Q 109, 112, 113, 114} "say-tetralogy" as a recitational unit:
  all four are canonically the daily-recitation suite (Falaq+Nās = the
  *muʿawwidhatān*; Ikhlāṣ + Kāfirūn = the *qul-pair* of obligatory
  morning-evening invocations).
- PASS = the canonical 4 (Q 109, 112, 113, 114) PLUS Q 72 are exactly
  recovered as v1-w1 qul-openers.

### Cell 4 — Addressee/speech-act follow-pattern (descriptive + clustering)
For each qul-occurrence, extract the next 1–3 normalised word-tokens after
qul (the *frame*). Tabulate the top-K most frequent (qul + X1) bigrams
and (qul + X1 + X2) trigrams.

Pre-registered formulaic frames to LOOK FOR:
- *qul aʿūdhu* (the muʿawwidhatān frame)
- *qul huwa* (the ikhlāṣ frame: *qul huwa Allāhu aḥad*; also *qul huwa
  alladhī…*)
- *qul yā ayyuhā* (the kāfirūn-style direct address)
- *qul innī / innamā / inna* (the certainty-frame)
- *qul law* (the counterfactual-rhetorical frame)
- *qul hal* / *qul a-* (the rhetorical-question frame)
- *qul man* (the "who?" interrogative-frame)
- *qul li-* (the "tell to-X…" cliticised-addressee frame)
- *qul aʾaʿbudu / aʾatakhidhu* (the *aʾa-* counter-question frame)

PASS = ≥ 3 of these formulaic frames each appear ≥ 5 times in the catalog
(threshold pre-registered to test structural recurrence).

### Cell 5 — qul-density × Meccan/Medinan (Mann-Whitney U)
For each surah, compute `density = qul_count * 100 / verse_count`.
Two-sample Mann-Whitney U on density distributions (Meccan vs Medinan).
α_bon = 0.00833.

Pre-registered prediction: density LOWER in early-Meccan (different
register) but BIMODAL in Mufaṣṣal (the "say-tetra" pulls Mufaṣṣal density
up via short-surah denominator effect). Net Meccan-vs-Medinan direction
ambiguous a-priori; this is genuinely a test, not a confirmation.

### Cell 6 — qul-density × revelation-phase ANOVA / Kruskal-Wallis
Use Nöldeke 4-phase classification (Early Meccan / Middle Meccan / Late
Meccan / Medinan). Kruskal-Wallis H test on densities across the 4
phases. α_bon = 0.00833. Phase-with-highest-density flagged in
findings.

Pre-registered prediction: Late Meccan > Medinan > Middle Meccan > Early
Meccan (qul as a polemical-dialogic device develops as the
Meccan dawʿah escalates, then settles in Medinan legal address).

## MW-positive control

Cell 1 IS the MW-control: total = 332 (matches imperative-run-1 + public
QAC count). Cell 3 also serves as a structural positive control:
{Q 109, 112, 113, 114} MUST be among v1-w1 qul-openers, and Q 72 should
also be present (per [[h-new-61-opening-words|H-NEW-61]]).

## Pre-committed verdict table

| Outcome | Verdict |
|---|---|
| Cell 1 fails (total ≠ 332) | EXTRACTOR_BROKEN — invalidate downstream |
| Cell 1 passes, Cells 2–3 published | descriptive baseline RATIFIED |
| Cell 4 ≥ 3 frames each ≥ 5x | qul-formulaic structure CONFIRMED |
| Cell 5 sig | period correlates with qul-density |
| Cell 6 sig | revelation-phase correlates with qul-density |
| All inferential cells null | distribution is non-uniform but not phase-correlated |

## Honest a-priori risk

This is a comparatively LOW-stakes hypothesis: the 332 count is widely
cited and the per-surah distribution is mechanical from QAC. The
NOVELTY would be in:
- Cell 4's formulaic frame catalog (which "qul + X" frames are pre-locked
  templates of the corpus?)
- Cell 6's phase-correlation if it survives Bonferroni.
- Possibly Cell 3's confirmation that Q 72 belongs to the "qul-opening"
  family as a 5th member.

The TEST cells (5, 6) may yield null results, in which case the finding
is "qul-density is not phase-correlated; it is concentrated in the dialogic
mid-corpus surahs (Q 6, 10, 3, 17) and the polemical Mufaṣṣal short
suras (109/112/113/114), but no clean Nöldeke-phase trend."

## Integrity

- Extractor + four-feature QAC predicate locked.
- 6 test cells declared; α_bon = 0.00833.
- Cell 1 is MW-control = total count ≡ 332.
- Cell 3 has a pre-registered hard-equality predicate (the 5-surah
  v1-w1 set).
- Cell 4 has pre-registered formulaic frames + threshold (≥ 3 of 9
  frames each ≥ 5x).
- Seed 20260417.
- Author: [[h-new-74-qul-distribution|h-new-74]]-specialist.
