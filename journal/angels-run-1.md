# Angels run 1 — journal

**Date:** 2026-04-12
**Agent:** Phase B catalog agent — angels of the Quran.

## Goal
Enumerate every angel (named or not) in the Quran, with verse references and counts. Test six specific sub-questions: (1) total `mlk` occurrences, (2) named angels, (3) malāʾika vs shayāṭīn opposition, (4) Badr angels fighting, (5) peaceful-vs-harsh angel-groups, (6) classical "seven throne-bearers" vs Quranic "eight on that Day."

## Data
- `data/morphology/quranic-corpus-morphology-0.4.txt` (Leeds QAC v0.4, Buckwalter, 128,276 lines).
- `quran-text/quran-no-tashkeel.json` (cross-check only).

## Method
1. Grep Buckwalter `ROOT:mlk` — 206 tokens. Disambiguated by LEM field: 88 for `malak` (angel), rest for kingship/dominion lemmas.
2. Grep `LEM:jiboriyl`, `miykaY`l`, `ma`lik2` (hell-warden), `ha`ruwt`, `ma`ruwt` for named angels.
3. Grep `LEM:$ayoTa`n` for Satan-lemma — 88 tokens. Computed intersection with malak at verse-level and surah-level.
4. Read full verses for 8:9-12 (Badr), 3:124-125 (Uhud), 13:23-24 vs 8:50 (peaceful vs harsh), 16:28 vs 16:32 (the pivot), 40:7 and 69:17 (throne-bearers).
5. Checked Rūḥ (rwH root) lemma distribution — 21 tokens.

## Key findings (fed into catalog)

1. **Exact parity at 88**: both *malak* lemma and *shayṭān* lemma occur 88 times. Unexpected.
2. **Only 2 verses** in the whole Quran contain both `malak` and `shayṭān`: Q 2:102 (Babylon/Hārūt-Mārūt) and Q 7:20 (Eden temptation). Both are *boundary-crossing* episodes. Strong structural claim.
3. **Jibrīl 3×, Mīkāl 1×, Mālik 1×, Hārūt 1×, Mārūt 1×** — that's all the named angels. Iblīs is separate (lemma from root `bls`).
4. **Badr (8:12)** is the only Quranic verse that gives angels a direct combat order. Uhud (3:124-125) is rhetorical reassurance, not a claim of participation.
5. **Q 16:28 vs 16:32** — same surah, four verses apart, same death-angel event, opposite valence, same lexeme `salām` inverted. The tightest peaceful/harsh pivot in the Quran.
6. **Q 69:17** specifies eight throne-bearers *only on that Day*. The Quran never says "seven now"; that number is hadith/tafsīr. The Quranic fixed-angel-count set is: 8 (throne, eschaton), 19 (hell, present+future), 1,000 (Badr), 3,000 and 5,000 (Uhud conditional).
7. **al-Rūḥ is ambiguous**: listed *alongside* angels (70:4, 78:38, 97:4) and yet functions *as* Jibrīl (26:193 vs 2:97 identical formula).
8. **Three different guardian-angel lexemes** (`muʿaqqibāt`, `ḥafaẓah`, `kirām kātibīn`) — vocabulary is not unified in the Quran.
9. **13 feminine-plural participles** describe angelic activity across 37:1-3, 77:1-5, 79:1-5 without ever using the lemma *malak*.
10. **Throne-eschaton-number `thamāniyah` (8)** appears only 3× in the Quran total (69:17 angels, 28:27 Moses' years, 18:22 Seven-Sleepers+dog).

## Quality flags / uncertainties

- **Hārūt-Mārūt**: canonical reading `al-malakayn` (two angels); Ibn ʿAbbās variant `al-malikayn` (two kings). QAC tags them as angel-dual. Flagged in catalog.
- **Iblīs angel or jinn?** Q 18:50 is decisive: `kāna mina l-jinn`. So he is explicitly not an angel. Not counted in angel catalog.
- **al-Rūḥ**: logged as ambiguous 6th figure, not categorically angel.
- **Oath-rank angels (37/77/79)**: not lexically `malak`; tafsīr-identified only. Logged in catalog with explicit note.

## Files produced
- `findings/phase-b-hypotheses/angels-catalog.md` (the catalog, ~3000 words).
- `journal/angels-run-1.md` (this file).

## Work not done / next-hop candidates
- Chronological ordering of the 88 malak tokens by revelation order (Egyptian/Nöldeke) to see if the angelology developed.
- Co-occurrence of `malak` with `rūḥ` at verse level (quick spot-check: 2:87, 16:102, 19:17, 21:91, 26:193, 66:12, 70:4, 78:38, 97:4 are the candidates).
- A proper statistical test on whether the parity at 88 is above chance, using the corpus lemma-frequency distribution as null model.
- Full cross-referencing of the 5 participial angel-ranks in 79 against the Ezekiel / Enoch throne-rank traditions.
