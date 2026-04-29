# Elative / afʿal Run 1 — Journal

**Date.** 2026-04-12. **Phase.** B (hypothesis generation). **Task.** Catalog afʿal-pattern elatives in the Quran.

## Approach

Source: `data/morphology/quranic-corpus-morphology-0.4.txt` (Leeds Quranic Arabic Corpus v0.4), Buckwalter transliteration, 128 219 morphological segments.

The corpus does not tag ʾafʿal as a distinct category, so I used a lemma-based heuristic:

1. Select all stems whose LEM starts with Buckwalter `>a` (i.e., initial hamza-alif + fatḥa).
2. Require POS ∈ {N, ADJ, PN}.
3. Extract the ROOT and **reject** any whose root begins with `A` (initial-hamza radical), since in those cases the `>a` is part of the root, not an elative augment. This eliminates false positives `>aroD` (earth), `>amor` (command), `>ahol` (family), `>ajor` (reward), `>aliym` (painful), `>ajal` (term), `>aw~al` (first — morphologically different), `>aHad` (one), `>avar` (trace), `>amiyn` (trustworthy), `>axo*` (form-IV verbal noun), `>aw~aAb` (oft-returning).
4. Require lemma body length in 3–5 chars after the `>a` prefix (catches `>a$ad~`, `>aHab~`, `>aDal~` with shadda, as well as standard `>aCoCaC`).

Result: **414 tokens across ~60 lemmas** — a tractable list.

## Decisions / deviations

- **Included** the geminate and defective-root afʿals: `>a$ad~` (šdd, 31 tokens), `>aHab~` (ḥbb, 3), `>aDal~` (ḍll, 9), `>aEolaY`/`>awolaY` (with final weak radical y/w), `>aqoSaA`, `>a$oqaY`, `>atoqaY`. These are morphologically "afʿall" or "afʿā" variants of afʿal.
- **Excluded** `>andaAd` (andād), `>anfaAl` (anfāl), `>ankaAl` (ankāl) from elative counts: these are afʿāl *broken plurals*, not elatives. Mentioned in findings but not counted.
- **Excluded** color/defect adjectives (`>aboyaD`, `>asowad`, `>axoDar`, `>aboraS`, `>abokam`, `>aEoraj`, `>aSam~`, `>aSodaq` in partial overlap) from elative semantics, though morphologically afʿal. Called out as a separate cluster (§2 tail).
- **Special case**: `>aSam~` (aṣamm, deaf) was initially caught by the filter but its corpus forms are mostly `Sum~a`, `SumN`, i.e., the plural `ṣumm` — the parser-lemma collapses both. I kept it out of the comparative-with-min count.

## Verifications

- `akbar` total = 24 tokens (root kbr); confirmed against the 21 distinct verse locations printed.
- `aḥsan` total = 36 tokens; manually inspected all 36 for "man aḥsanu min …" (4 cases found, §6.1 in findings).
- `al-Aʿlā` = 9 tokens, distribution matched manually to Q 16:60, 20:68, 30:27, 37:8, 38:69, 53:7, 79:24, 87:1, 92:20.
- `al-Akram` = 2 elative tokens (Q 49:13 `akramakum`, Q 96:3 `al-akram`). Two further tokens in the corpus under the same lemma are form-IV verbs `akrama` (Q 89:15 twice) — kept separate.
- `awlā` = 11 tokens, verified against 8 distinct verses.
- `awliyāʾ` = 42 tokens — looked up Buckwalter `>awoliyaA^'a/&u/}i`.

## Findings summary

- Elative + `min` (comparative frame): 49 constructions, ≈ 11.8 % of all afʿal tokens. Ranked by ashadd (8), akbar (5), aḥsan (3), aqrab (3), aṣdaq (2), abyaḍ (4, but color-sense).
- "Who is more X than Y" rhetorical-question frame: 4 instances with aḥsan (Q 2:138, 4:125, 5:50, 41:33); this is a highly crystallised template with fixed word-order `wa-man aḥsanu [tamyīz] {mina llāhi / mimman Y}`.
- Takbīr formula not present as such; 3 Allāh-adjacent akbar tokens (9:72, 29:45, 40:10), each with different grammatical subject.
- Surah 87 opener and Surah 96:3 share a unique divine-attribute+rabb+imperative template (`al-Aʿlā` and `al-Akram`).
- Pharaonic usurpation of `al-aʿlā` at Q 79:24 is the most interesting theological inversion of the afʿal-attribute slot.

## Open items / deferred

- Did **not** enumerate `man aẓlamu mimman …` (aẓlam as rhetorical elative) — this would be a natural companion run. Quick count from data: `>aZolamu` occurs 15 times, worth a separate dig.
- `min + ahl` false-positive class is already excluded but some border cases (`aḥmaʿ`, `amlakh`) would need manual verification if encountered.
- Cross-chronological distribution (Meccan vs. Medinan) of afʿal tokens not computed; surah-61 top-15 (§2 surah counts) suggests Medinan-heavy but this needs the chronological-order dataset.

## Artifacts

- `findings/phase-b-hypotheses/elative-forms.md` — ~2500-word report.
- No CSV generated; all data inline in the MD.

## Runtime

Three Python extraction passes over the corpus (each ≈ 0.3 s). No external dependencies.
