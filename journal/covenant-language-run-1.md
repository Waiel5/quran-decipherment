---
run: covenant-language-run-1
date: 2026-04-12
agent: covenant-deep-agent
phase: B
---

# Covenant-language run — working journal

## Plan

- Extract five roots (`Ehd`, `wEd`, `wvq`, `byE`, `Eqd`) from QAC morphology.
- Cross-reference to Meccan/Medinan period (from `quran-no-tashkeel.json`)
  and Nöldeke phase (from `data/revelation-order.csv`).
- Map covenant-partners per verse using Sahih translations.
- Investigate 7:172 separately (primordial covenant).

## Method

Morphology file is Buckwalter-transliterated; root codes verified:
- ʿahd = `Ehd` (ع-ه-د = E-h-d)
- waʿd = `wEd` (و-ع-د = w-E-d)
- mīthāq = `wvq` (و-ث-ق = w-v-q; `v` is Buckwalter for ث)
- bayʿ = `byE` (ب-ي-ع = b-y-E)
- ʿaqd = `Eqd` (ع-ق-د = E-q-d)

Initial wrong guess was `bye` (lowercase) which returned 0; corrected
to `byE` (ayn=capital E). Retained after verification.

Counts obtained:
- `Ehd` 46 occ / 36 verses
- `wEd` 151 / 130
- `wvq` 34 / 29
- `byE` 15 / 11
- `Eqd` 7 / 7

## Translation alignment

The Sahih file `en.sahih.txt` has 6249 lines vs 6236 JSON verses — an
offset I initially worried about. Spot-checked:
- line 1 = 1:1 (basmala)
- line 8 = 2:1 (Alif Lam Meem) ✓
- line 184 = 2:177 ("Righteousness is not...") ✓
- line 4593 = 48:10 (Indeed those who pledge allegiance...) ✓

So the sequential Python mapping (each JSON verse → next trans line)
works correctly. The 13 extra lines are apparently at the file tail
or blank lines between surahs; they don't affect alignment for
within-corpus verses.

## Key finds as I went

1. **First surprise:** `wEd` is *Meccan-heavy* (101/130 Meccan), the
   opposite of the task's hypothesis. Re-read task: it says "check for
   early-Meccan primordial covenant verses" and "Medinan legal-vocabulary
   increases" — so this is not a contradiction but a **decomposition**:
   different covenant roots have different temporal profiles.
2. **Nöldeke gradient** for `Ehd` is 1 → 8 → 7 → 20 (monotonic) — this is
   the cleanest diachronic signal of the five.
3. **7:172 doesn't use any of the five roots.** This was the most
   unexpected empirical finding. Verified by reading all 26
   morphology-lines of the verse: the governing verbs are `Ax*` (take)
   and `$hd` (witness). Noted prominently in §3.
4. **Q 48:10 is unusually dense.** Combines `byE`, `Ehd`, and `nqD`
   (naqaḍa = break) in a single 21-word verse. Flagged as the
   highest-density covenant verse.
5. **2:27 / 13:25 doublet.** Same opening formula, different sanction
   clause. Connects to the existing mutashābih-lafẓī work (findings/
   phase-b-hypotheses/mutashabih-lafzi.md — noted but not cross-checked).

## Choices / garden-of-forks

- **Classified `wEd` verses by reading translations** rather than by
  Arabic syntax. This is a heuristic with noisy edge cases (e.g. many
  "other" verses). The headline categories are stable but individual
  assignments are approximate.
- **Included `biyaʿ` (22:40 synagogues) under `byE`** — it is the same
  root but different semantic field. Noted in lemma inventory.
- **Did not run a permutation test** on period labels. With 5 roots and
  clear Cohen-d-like separation (e.g. `byE` 1 vs 10 Meccan/Medinan)
  formal testing is almost unnecessary, but under the protocol this
  would need to be added for Phase-C pre-registration.
- **Did not cross-check the `mīthāqan ghalīẓā` triptych count**
  independently — took my reading of 4:21, 4:154, 33:7. Verified by
  scanning `scratch/covenant/root-wvq.tsv`: those three verses do all
  contain `mīthāq` contextualised with an intensifier.

## Sibling hypotheses considered but not pursued

- Full network of covenant-verb / covenant-noun cooccurrence (e.g. `Ehd`
  + `Ax*` "to take covenant" vs `Ehd` + `wfy` "to fulfil covenant"). A
  bipartite-graph treatment would be cleaner than the tables.
- **Amāna** (`Amn` root, entrusted trust) — Q 33:72 — is arguably the
  sixth covenant-lexeme. Not included in the requested set; briefly noted
  in §3.
- **ʿurwa al-wuthqā** (2:256, 31:22) — "the most trustworthy handhold"
  — uses `wvq` root but in a metaphorical not covenant-event sense.
  Kept in the `wvq` count but flagged in lemma inventory.
- Arabic side reading not done — I worked from QAC morphology + Sahih
  translation. For a definitive claim on 7:172's lexical uniqueness I'd
  want to verify that no other covenant root appears in the
  *surrounding verses* 7:171 / 7:173, which I did confirm (only `Ax*`
  and `$hd` in 7:172 itself; 7:171 mentions the Tūr; 7:173 continues
  without covenant vocabulary).

## Prior art read (or searched for)

- Wadad Kadi (el-Qadi) 2003 in *PAPS* on primordial covenant —
  foundational English treatment; named in §12.
- Al-Rāzī, Ibn Taymiyya, Ibn ʿAṭāʾillāh per task prompt — traced at the
  level of known positions, not primary-text consulted in this run.
- No computational/stylometric prior on covenant-family roots
  specifically. Sadeghi-style diachronic work covers verse length and
  morpheme frequencies but not this semantic field.

## What's statistically clean

- Meccan/Medinan split for `wvq` (5/24) and `byE` (1/10): binomial test
  against a 60/40 null (corpus background Meccan/Medinan surah balance)
  gives p-values essentially at 10^-4. Flagged for Phase-C pre-reg.
- Nöldeke monotonic ramp for `Ehd` (1/8/7/20): 4-phase F-test would
  give a substantive effect-size — not computed here.

## What's not clean

- `wEd` categorisation by English translation key-word match is a
  heuristic. The 83-verse "other" bucket includes most of the richest
  prophet-narrative promises (Noah, Salih, Hud) and needs manual
  re-reading for a Phase-C claim.
- The tripartite "covenant-chain" reading of 3:81 / 3:187 / 33:7 is
  interpretive, not stylometric. It's classical exegetical reasoning
  extended to the three verses' co-occurring formulas.

## Outputs

- `findings/phase-b-hypotheses/covenant-language.md` — main report.
- `scratch/covenant/*.tsv` — machine-readable per-root location tables.
- `scratch/covenant/verse-lists.txt` — human-readable summary.
- `scratch/covenant/covenant-verses-full.txt` — full translated verses.
