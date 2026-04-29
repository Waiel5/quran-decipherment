# Numeric-word audit — run 1

**Agent:** numeric-word-audit-1
**Date:** 2026-04-12
**Output:** `findings/phase-b-hypotheses/numeric-word-distribution-audit.md`
**Script:** `scratch/numeric-word-audit/numeric_audit.py`
**Raw text:** `scratch/numeric-word-audit/numeric_audit_output.txt`
**Raw JSON:** `scratch/numeric-word-audit/numeric_audit_output.json`

## Rules tuple locked

```
no-tashkeel, orthographic-token & lemma (QAC v0.4), graphemes,
basmala counted-only-in-surah-1, hafs-kufan numbering, mashriqi abjad (not used here),
null model: within-surah verse-shuffle of numeric-lemma occurrences, 1000 perms,
numpy seed = 20260412.
```

## Pipeline

1. **QAC-based lemma extraction.** Instead of surface-token matching (which
   requires a prefix-tolerant regex and produces noise for tanwīn endings),
   I used the Leeds Quranic Arabic Corpus v0.4 directly. Numeric-in-meaning
   lemmas were whitelisted by (LEM, ROOT) pairs; semantic siblings
   (`s~abuE` "predatory beast", `Ea$iyr` "close associate", `vaman` "price",
   `nasof` "scatter", `maEo$ar` "society") were explicitly veto-listed.
2. **Morphological-feature decade rewrite.** QAC collapses 40/70/90 under
   the unit lemma with feature `MP` (masculine plural — `>arobaEiyna` "forty"
   vs `>arobaEa` "four"). I added a `DECADE_REWRITE` pass that relabels
   these to their decade integer value. Same for `miA}ap|FD` → 200.
3. **Polysemy split for *aḥad*.** Using the QAC `INDEF` tag on the tanwīn
   form, the 74 `>aHad` tokens split into 52 pronominal ("anyone") + 22
   numeric ("the One"). This is the first corpus-wide operationalisation
   of al-Rāghib's *Mufradāt* distinction for this lemma.
4. **Per-verse integer-set construction.** For each of 6,236 verses, the set
   of distinct base-integer values is computed (excluding pronominal *aḥad*
   from integer-1).
5. **Co-occurrence pair tally.** For each pair (a, b) with a<b and
   {a, b} ⊂ verse-integer-set, increment `pair_count[(a,b)]`.
6. **Null model.** For each of 1,000 permutations, reassign each numeric
   occurrence to a random verse within its own surah. Re-compute per-verse
   integer-sets and pair counts. Record per-pair mean / std and permutation
   p-value (`(n_null_ge_obs + 1) / (N_PERM + 1)`).
7. **Specific claim tests:**
   - P1: rank of 7 in the by-integer token table.
   - P2: verses containing the strict surface chain "سبع سماوات" / "السماوات السبع"
     in any prefix variant.
   - P3: forty-verses' overlap with prophet-mission keywords.
   - P4: thousand-verses' overlap with eschat keywords.

## Key numbers

- 128,219 QAC morphological segments parsed.
- 338 numeric-word tokens in ≈ 270 verses.
- 37 verses contain ≥ 2 distinct numeric integers.
- Null: verses-with-co-occurrence mean 8.16, std 2.61 → **z = +11.06, p < 10⁻³**.
- Per-pair Bonferroni α = 0.05/46 ≈ 1.09×10⁻³. Surviving pairs:
  (1, 2), (3, 10), (2, 4), (100, 1000), (4, 6), (4, 8), (7, 8).

## Verdicts

| # | Claim | Source | Verdict |
|--:|---|---|---|
| P1 | "7 is the most frequent Quranic number" | al-Suyūṭī *Itqān* nawʿ 57 / folk | **FAIL** — 7 ranks #3 (24 tokens), behind 1 (177) and 2 (25). |
| P2 | "*Sabʿ samāwāt* appears exactly 7 times" | apologetic | **CONFIRMED EXACT** — 7/7 (Q 2:29, 17:44, 23:86, 41:12, 65:12, 67:3, 71:15). |
| P3 | "40 → prophet-mission" | Ibn ʿAshūr *Taḥrīr* | **CONFIRMED** — 4/4 (100 %) vs 13.9 % base rate. |
| P4 | "1000 → eschat" | al-Qurṭubī | **PARTIAL** — 5/13 (38.5 %) vs 9.0 %; cosmic-day subset only. |
| P5 | "Same-verse co-occurrence is non-random" | novel | **PASS** — z=+11.06, p<0.001. |

## Highlights worth surfacing to the master index

- **Q 18:22 is the densest numeric verse (6 distinct integers: 3, 4, 5, 6, 7, 8).**
  The verse self-enumerates — classical tafsīr reads the three counts
  (3+dog / 5+dog / 7+dog-as-eighth) as a deliberate rhetorical *ibhām al-ʿadad*.
- **Q 8:65 and Q 8:66 contain 20/100/200/1000 and 100/200/1000/2000** — the
  Quran's densest multi-decade integer sets, both Badr combat-ratios.
- **The (1, 3) pair is the Quran's anti-trinitarian pair** — 3/3 co-occurrences
  (Q 4:171, 5:73, 5:116) are all Jesus-Mary-Allah triad denunciations.
- **The (1, 2) pair at 5 verses** (Q 4:3, 4:11, 5:106, 16:51, 34:46) is the
  Quran's legal-dualism-vs-monadism device; p=0.001 under within-surah null.
- **Fractions never co-occur with their implicit complements** (no *niṣf* + 2,
  no *thulth* + 3). Fraction vocabulary is legally sealed off.

## Honest negatives

- Classical "7 is most frequent" — FALSE under any counting rule. Requires
  restatement ("most frequent non-trivial cardinal"). Should be flagged in
  the master-ledger correction column.
- "1000 = eschat" — only directionally true; only cosmic-day subset fits.
- "*arbaʿ* wives / 4 witnesses / 4 sacred months" cluster — 4 appears in
  16 verses, of which 4 are legal (wives Q 4:3, witnesses Q 24:4 / 24:13,
  sacred months Q 9:36) — so "4 = legal" holds at 4/16 = 25 % enrichment,
  *not* reported as a formal P-claim because it was not pre-registered.
- **(1, 1000)** is NOT a real pair (obs=1, p=0.28); despite apologetic
  framings of "one God among a thousand years," this does not occur.

## Prior art (WebSearch)

- No academic study operationalises same-verse numeric co-occurrence with
  a within-surah null model. Closest precedents:
  1. Kaltner & McKenzie (2018) *The Bible and the Qurʾān: Biblical Figures
     in the Islamic Tradition* — numeric symbolism of 40 / 7 / 12 in both
     scriptures, qualitative only.
  2. Ayoub (1984) *The Qurʾan and Its Interpreters* — symbolic readings of
     numbers in tafsīr tradition.
  3. Iranian-Quranic-Studies journal (2021, IQS) — *A Comparative Study
     of the Literal and Symbolic Meaning of the Numbers in Qur'anic Verses
     about Creation* — confirms 7-samāwāt cosmological reading, no
     quantitative null.
  4. Sayoud's Scholarpage 2020 paper — generic numerical coincidences
     catalog, no inferential framework.
- The apologetic "sabʿ samāwāt = 7 times" claim is correctly counted across
  decades of apologetic literature (Fathi Yakan, al-Kaheel, Bucaille
  disciples). Our finding confirms the count is exact and contextualises
  it: 7 of 20 *sabʿ*-cardinal verses enumerate heavens (35 %), not a
  cryptographic signature.
- "Abend-David on Quranic numbers" / "Whitley on numerology" in the task
  prompt: no published papers located under these author-query forms.
  Proceeded without those specific citations.

## What I did not do

- Did NOT touch: monograph, man-at-the-center, verse-commentaries,
  MASTER-FINDINGS-LEDGER.md, TOMORROW-TESTS-PRE-REGISTRATION.md.
- Did NOT duplicate: H-NEW-34 (abjad-residue), H-NEW-15 (clean-factorization
  windows), prime-mod-scan.
- Did NOT re-run: the 90-claim classical audit. This is orthogonal.
- Did NOT: build an abjad-gematria co-occurrence layer. Out of scope.

## Follow-up candidates (not executed here)

1. **Cross-corpus baseline.** Draw 1000 length-matched blocks from Bukhārī /
   Sīra / Jāḥiẓ, count numeric-lemma density and same-block co-occurrence.
   Question: does the z=+11 effect survive against real classical Arabic?
2. **Chronological split.** Are numeric co-occurrences Meccan-leaning or
   Medinan-leaning? Forty + Moses suggests Meccan cluster; 4-wife/4-witness
   is Medinan. Test density per revelation period.
3. **Lemma-level conditional probability.** P(samāwāt | sabʿ) and
   P(sabʿ | samāwāt) under a lemma-by-lemma matrix.
4. **Fraction-vs-cardinal sealing test.** Confirm §10.4 at lemma level
   with a chi² contingency table.
