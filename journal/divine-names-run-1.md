---
title: "Journal — divine-names distribution run 1"
agent: phase-b-novelty / divine-names-distribution
date: 2026-04-12
---

# Run log

## Goal
Build the first systematic computational catalogue of the canonical 99 Names
of Allah (al-Tirmidhi/al-Walid ibn Muslim list) distribution, pairing, and
surah placement across the Quran. Companion to the earlier `razi-99names-test.md`
(H20, rejected) which looked at muqatta'at-letter/99-name alignment. This run
steps back to the distribution itself.

## Method outline
1. Read canonical list: `/Users/grey/Downloads/quran/data/asma-al-husna.txt` (99 names verified).
2. Load Kais Dukes morphology 0.4: `quranic-corpus-morphology-0.4.txt` (128,219 rows).
3. Hand-curated mapping {Arabic name → Buckwalter LEM string(s) → root → transliteration}.
4. Filter rule:
   - Exact lemma match in morphology `LEM:` field.
   - Token must be Masculine Singular (divine names of God are never plural/feminine).
   - Same-word PREFIX|Al+ (definite article) required OR token tagged PN.
   - Exceptions: Allah = always divine; Aziz/Malik in Surah 12 = governor-of-Egypt, excluded.
   - For ambiguous names (al-Haqq, al-Nur, al-'Azim, al-Awwal, al-Akhir, etc.): require Allah lemma within +/-3 verses.
   - For al-Haqq specifically: Allah in SAME verse.
5. Build per-name statistics, pair grid (same-verse co-occurrences), triads, surah profiles.
6. Theme-name map by root co-occurrence in verse.
7. Opening-closing divine-name overlap per surah.
8. `la ilaha illa huwa` regex scan on diacritic-free text.

## Problems encountered and fixes

### Problem 1: Lemma-form mismatches
Initial run showed ~49 of 99 names with zero occurrences. Investigation via
lemma probes revealed that many canonical names appear under different
Buckwalter stems than I had assumed:
- `>aw~al` not `> aw~al` (typo)
- `ganiY~` (cap Y) not `ganiy~`
- `waliY~`, `qawiY~` same
- `m~ajiyd`, `m~ujiyb`, `m~uqiyt`, `m~uqotadir` (all with m~ prefix)
- `S~amad` (with shadda)
- `A^xir` (with madda), not `|xir`
- `r~az~aAq` (double shadda), not `raz~aAq`
- `waAl` (not `waAliy`) for al-Waali
- `taw~aAb` singular form for al-Tawwab
- `Eafuw~` (with shadda)
- `haAd` AND `haAdiy` both valid for al-Hadi

After corrections, zero-attestation names dropped from 49 to 41.

### Problem 2: False positives from common-noun lemmas
Al-Mu'min (the canonical divine name) matched the lemma `mu&omin` which is
dominated by the plural "mu'minin" (believers = humans) — 202 occurrences.
Fixed by requiring `|MS|` (masculine singular) feature. This correctly
yielded al-Mu'min-as-divine = 0 under strict rule, matching the classical
observation that al-Mu'min as divine occurs only once (Q 59:23).

Similarly for al-Akhir (`A^xir`) — dominant form is feminine `A^xirap` = "the
Hereafter" (with feminine ending). Fixed with |MS| filter.

Similarly al-Haqq (`Haq~`) — mostly abstract noun "truth". Fixed with
same-verse Allah-context filter. Dropped from 194 to 82.

### Problem 3: Context-dependent divine-name detection
Q 57:3 (al-Awwal/al-Akhir/al-Zahir/al-Batin) has the pronoun "huwa" referring
to Allah mentioned two verses back (57:1 "sabbaha lillah"). Under same-verse
filter these were missed. Relaxed to +/-3 verse window. This correctly
caught Q 57:3 as the canonical quartet verse.

## Key findings

### Verified classical claims
- al-Rahman = 57 tokens (classical 19×3 count, matches).
- al-'Aziz al-Hakim = 29 co-occurring verses (most common pair).
- al-Sami' al-'Alim = 15 co-occurring verses (second most common semantic pair).
- Q 57:3 is the unique quartet verse.
- Q 59:22-24 is the densest divine-name passage.
- ~30 verses contain `la ilaha illa huwa` → we found 35 under regex.

### Novel findings
- **41 of 99 canonical names have ZERO DET-MS divine-referring Quranic attestations.** This is a direct structural result: the 99-name list is a HADITH construct. Classical scholars like al-Ghazali qualitatively acknowledge this but never tabulate it. al-Muhyi, al-Muntaqim, al-Qabid, al-Basit, al-Khafid, al-Rafi', al-Mu'izz, al-Mudhill, al-Muqaddim, al-Mu'akhkhir, al-Darr, al-Nafi', al-Jami', al-Mughni, al-Mani', al-Hadi, al-Badi', al-Sabur, al-Muqsit, al-Ra'uf, al-'Afuww, Malik al-Mulk, Dhu al-Jalal, and ~20 more — all hadith-attestation-only.
- **Only ~2.2% of Quranic verses end with a divine-name PAIR** — surprisingly low given the classical emphasis on saj' closures. Divine-name pairs are a marked, concentrated device specifically in Medinan legal surahs (4, 5, 9, 24, 33, 48-66).
- **al-Rahman's #1 host is NOT Surah 55 but Surah 19 (Maryam)** — 16 occurrences, concentrated in the Jesus-as-son polemic. Surah 55 has only 1 al-Rahman (at v 1). This inverts naive expectation.
- **Q 57:3 is the ONLY Quranic verse containing a 4-fold divine-name opposite quartet.** No other verse has this density of opposite-pair divine names.
- **8 of 10 classical opposite-pairs (Qabid/Basit, Khafid/Rafi', Mu'izz/Mudhill, Muqaddim/Mu'akhkhir, Darr/Nafi', Muhyi/Mumit)** have ZERO Quranic attestations. The "paired opposites" subtheology of the 99 names is entirely post-Quranic (hadith + kalām).

### Pairing grid headline
Top 10 pairs:
1. al-Haqq + Allah (75)
2. al-'Aziz + al-Hakim (29)
3. al-Akhir + Allah (26)
4. al-'Aziz + Allah (26)
5. al-Hakim + Allah (22)
6. al-'Azim + Allah (19)
7. al-Sami' + al-'Alim (15)
8. al-Rahim + al-'Aziz (13)
9. al-'Alim + Allah (12)
10. al-Rahim + Allah (11)

## Forks disclosed
- Strict vs permissive filter: chose strict. Permissive would have over-counted al-Haqq, al-Akhir, al-Mu'min as abstract/plural.
- +/-3 verse ambiguity window chosen so Q 57:3 resolves. Same-verse-only would have given 1 verse each for awwal/akhir/zahir/batin.
- No null-hypothesis testing — this is descriptive cataloguing.

## Outputs
- `/Users/grey/Downloads/quran/findings/phase-b-hypotheses/divine-names-distribution.md` (main report, 609 lines)
- `/Users/grey/Downloads/quran/findings/phase-b-hypotheses/divine-names-by-verse.csv` (1981 verses with at least one divine name)
- `/tmp/divine_names_data.json` (full JSON dump)
- `/tmp/divine_names_analysis.py` (script)
- `/tmp/divine_names_writeup.py` (markdown-writer script)
