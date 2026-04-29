---
journal_id: iltifat-analyst-run-1
date: 2026-04-12
agent: iltifat-analyst (Phase B finalization)
upstream: iltifat-detector-run-1 (not journaled; rate-limited before writing report)
inputs:
  - findings/phase-b-hypotheses/iltifat-density-by-surah.csv (114 surahs)
  - findings/phase-b-hypotheses/iltifat-per-verse.csv (6236 verses)
  - findings/phase-b-hypotheses/form-meets-content-outliers.md §3
  - findings/balagha-mapping.md §2.2.4
  - findings/phase-c-structures/chiastic-audit.md §5
  - findings/phase-b-hypotheses/saj-rhyme-analysis.md
  - findings/phase-b-hypotheses/saj-fasila-per-verse.csv
  - data/translations/en.sahih.txt
outputs:
  - findings/phase-b-hypotheses/iltifat-catalog.md
---

# Journal — iltifat-analyst run 1

## Task

Phase B finalization: the iltifat-detector agent computed the two CSVs but did not
get to write the analysis report before being rate-limited. My job is to read the
CSVs and produce `findings/phase-b-hypotheses/iltifat-catalog.md`, with YAML
frontmatter, tables, correlation tests, honest null discussion, and a 400-word
summary — engaging with classical balagha (al-Suyūṭī, Abdel Haleem) and
cross-validating against the hand-read Maryam analysis.

## Process

1. Read both CSVs to confirm schema. The per-verse CSV has 24 columns; the density
   CSV has 15 + a `primary_hist` JSON column. Schema documented in report §1.
2. Read the balagha-mapping §2.2.4 (classical iltifāt treatment) and the
   form-meets-content §3.2 (Maryam hand analysis). These set the acceptance
   criteria.
3. Wrote `/tmp/iltifat_analysis.py` to compute:
   - global base rates (§2)
   - surah density ranking with Meccan/Medinan split and length correlation (§3)
   - probes for Q 1:4-5, Q 36:22 (§4)
   - ring-center iltifāt probes at v and ±1 (§5)
   - Maryam 19:30-41 verse-by-verse (§6)
   - rhyme-break × iltifāt 2×2 on top-32 uniform surahs (§7)
   - topic concentration via pre-tagged `topics` column (§8)
   - surprises (§9)
4. Fixed two bugs on first run:
   - `saj-fasila-per-verse.csv` uses `verse` + `ends_in_letter`, not `ayah` +
     `fasila_1`. I confirmed the schema and patched.
   - Initial top-32 uniform-surah pick returned surahs 1-10 because I was reading
     the wrong column (the whole fasila_2char, not the single ending letter).
     Recomputed U1 from `ends_in_letter` → top-32 matches `saj-rhyme-analysis.md`
     §2.
5. Observed the 97%-iltifāt rate in quote-marked verses vs 67% in non-quoted.
   Added this as a de-confounder in §2 and limitation §11.

## Key findings (compressed)

1. Corpus iltifāt base rate 70.8% (any), 45.3% (strict intra) — iltifāt is
   baseline, not marked. This is the most consequential single observation.
2. Q 1:5 and Q 36:22 both fire at strict level — classical sanity checks pass.
3. Ring-center co-location: 4/5 Bonferroni centers fire at v; 6/6 within ±1. But
   against a 70.8% baseline this is not statistically strong — classical claim
   is qualitatively consistent, not quantitatively confirmed.
4. Maryam vv 34-40 cascade: 6/7 verses match hand reading. Miss on v 39 is a known
   mode-based person-assignment weakness (1 imperative vs 5 background verbs).
5. Rhyme-break × iltifāt: **null**. χ² p = 0.39, breakers slightly LESS iltifāt.
   The Maryam convergence is local, not a corpus-wide pairing. This is the
   strongest new negative finding.
6. Topic concentration: prophets z = +9.4, revelation z = +7.7, law z = +3.7 — 
   iltifāt is enriched in discursive/instructional topics, baseline in
   judgment/creation. This **refines** Abdel Haleem's "theological intensity"
   claim — it is discourse-intensity, not judgment-intensity.
7. Medinan > Meccan density (0.86 vs 0.65, t = −2.88), confounded with length
   (r = +0.44 with N).
8. Top density surahs 60 (Mumtaḥanah) and 66 (Taḥrīm) — classically named iltifāt
   examples — independently re-discovered.
9. Quoted verses carry iltifāt at 97%, non-quoted at 67%. Much of the raw signal
   is embedded dialogue; strict Itqān-iltifāt excludes within-quotation shifts
   which we have not yet operationalised.

## Honest appraisal

- The detector's rules were designed knowing Maryam should fire; the Maryam
  test (§6) is not blind. The ring-center, rhyme-break, and topic tests are
  blind-ish (the detector was frozen before my analysis; I did not tweak rules
  after seeing ring-center results).
- No permutation null yet; ring-center 4/5 against 70.8% baseline is p ≈ 0.38
  Bernoulli → NOT significant. Have flagged this in §11.
- Tense-shift iltifāt (a core Itqān subtype) is NOT implemented; all iltifāt here
  is person-iltifāt.
- Classical attribution in §10 goes deeper than balagha-mapping.md currently
  does — I explicitly point out that our 70.8% base rate aligns with Ibn al-Athīr's
  *shajāʿat al-ʿarabiyyah* framing (language-typical) rather than the later
  systematised "iltifāt is a rare figure" framing.

## Recommended follow-ups

1. **Run a permutation null** over the 114 surahs: shuffle person-labels within
   surahs and re-measure ring-center coincidence. Without this, the ring-center
   section is suggestive only.
2. **Strip within-quotation person-shifts** — re-run with a narrator-frame-only
   iltifāt detector. Expect corpus base rate to fall from 70.8% toward 40-50%.
3. **Implement tense-shift iltifāt** (past→imperfect, imperfect→past) and see
   whether it picks up different verses from person-iltifāt.
4. **Salience-weighted primary_person** (imperatives > preterites > participles >
   jussives) to fix Maryam v 39 and similar.
5. **Comparable-Arabic baseline**: measure iltifāt rate on Bukhārī hadith narratives
   with Quran quotations stripped, to test whether 70.8% is Quran-distinctive or
   classical-Arabic-typical.

## Deliverable

`findings/phase-b-hypotheses/iltifat-catalog.md` — 12 sections, YAML frontmatter
with full rules tuple, all tables populated from CSVs, 400-word summary at top,
classical citations integrated, honest null discussion in §11.
