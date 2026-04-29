# Ayat al-Kursī Deep Dive — Run Journal

Date: 2026-04-12
Agent: deep-reader (Q 2:255 focus)
Outputs: findings/phase-c-structures/ayat-al-kursi.md

## Sources consulted

- `quran-text/quran-no-tashkeel.json` — primary Arabic corpus (Hafs-Kufan numbering)
- `data/translations/en.sahih.txt` — Saheeh International, line-aligned 1..6236
- `findings/khawatim-al-hashr-analysis.md` — comparator "Greatest" passage
- `findings/phase-b-hypotheses/divine-names-distribution.md` — name-frequency tables and Ayat-al-Kursi hits (rows for al-Hayy, al-Qayyum, al-Ali, tawhid declaration preferential pairing)
- `findings/phase-b-hypotheses/paired-opposites-network.md` — hidden/manifest pair, ghayb/shahāda; saw that the hidden/manifest pair (bāṭin/ẓāhir) is the Bonferroni-strongest novel find (p=6.9e-08). Q 2:255 J6 "yaʿlamu mā bayna aydīhim wa mā khalfahum" is a temporal cognate (before/after) of the spatial hidden/manifest pair.
- `findings/phase-c-structures/chiastic-audit.md` — Al-Baqarah 131-144 Bonferroni-surviving Abraham ring (z=+9.69), Al-Hashr ring z=+2.42
- `findings/intra-quranic-cross-references.md` — 2:255 noted as the prototype muhkam tawhid declaration

## Method

1. Extracted Q 2:255 clean text (strip rec-marks ۛۚۖۗ, preserve graphemes).
2. Split into 10 classical jumal following the user's enumeration.
3. Computed per-jumla word-count, letter-count, and mashriqi abjad.
4. Scanned all 6,236 verses for the key formulae:
   - "الله لا إله إلا هو" — 8 exact hits
   - "لا إله إلا هو" (any form) — 29 verses
   - "الذي لا إله إلا هو" — 3 verses (20:98, 59:22, 59:23)
   - "الحي القيوم" — 2 verses (2:255, 3:2); 20:111 uses prefixed "للحي القيوم"
   - "كرسي" root — 2 verses (2:255, 38:34)
   - "العلي العظيم" — 2 verses (2:255, 42:4)
   - "عرش"/throne — 28 verse hits (approx 21 for divine ʿArsh)
5. Computed letter-midpoint (189/2 = 94.5) and word-midpoint (50/2 = 25/26) to locate the verse's internal center.
6. Tabulated ring-pair metrics for the 10-jumla concentric hypothesis.
7. Compared to Khawātim al-Ḥashr (49 words, 216 letters = 6³, 15 divine names).

## Key discoveries made during this run

- **J1 (Allāh lā ilāha illā huwa) = 14 letters; J10 (wa huwa al-ʿAlī al-ʿAẓīm) = 14 letters.** Exact outer-frame letter symmetry.
- **J3 (no drowsiness/sleep) abjad = 1985; J8 (Throne extends...) abjad = 2008.** Near-equal abjad in negative↔positive cosmic mirror.
- **Letter count 189 = 27 × 7 = 3³ × 7.** Compare Khawātim al-Ḥashr (22-24) = 216 = 6³ letters + 49 = 7² words. Both passages land on clean low-prime factorizations.
- **Word-midpoint (25/26) lies inside J5**, the rhetorical intercession question. J5 is also the letter-midpoint region (positions 65-88, center at ~77; verse letter-midpoint is 95, sitting on the J5/J6 boundary). The rhetorical question is the structural center of the verse.
- **Q 42:4 = "lahu mā fī al-samāwāti wa mā fī al-arḍ wa huwa al-ʿAlī al-ʿAẓīm"** — this is literally J4 + J10 concatenated. The Quran elsewhere composes a whole verse out of two Ayat al-Kursī jumal.
- **Q 20:110-111** contains the J6 clause ("yaʿlamu mā bayna aydīhim wa mā khalfahum wa lā yuḥīṭūna bihi ʿilmā") immediately followed by "للحي القيوم" (the J2 name-pair). Q 20:110-111 is a compressed recomposition of J6 + J7 + J2 of Ayat al-Kursī.
- **"Allāh lā ilāha illā huwa" occurs in 8 verses**: 2:255, 3:2, 4:87, 9:129 (+ prefixed form), 20:8, 27:26, 28:70 (prefixed), 64:13. Three of these (20:8, 27:26, 28:70) are Meccan; five are Medinan. The formula is not a single "Medinan-era" construction — it spans Meccan surah 20 (Taha) and climaxes in the Medinan 2:255.
- **Al-Ḥayy al-Qayyūm 3× in Quran**: 2:255, 3:2, 20:111. Q 3:2 is a pure distilled version of J1 + J2. Q 20:111 sits at the end of Taha and is preceded by a J6 echo.
- **Kursī appears in only 2 verses**: 2:255 (divine) and 38:34 (Solomon's throne, in a story of Solomon's trial). ʿArsh (divine Throne) appears ~21 times. The Kursī/ʿArsh distinction is textually sharp.

## Open question / caveat

The 10-jumla ring is not a root-set chiasmus of the kind the `chiastic-audit.md` agent tests for (that agent works at verse level, not sub-verse). No null-model test was run on the J-pair metrics — the outer-frame letter match (14↔14) and J3/J8 abjad near-match (1985↔2008) are observed, not statistically controlled. They are structurally suggestive, not p-valued. Reported as such in the finding.

## Cross-references added to finding

- Khawātim al-Ḥashr comparison (direct)
- Al-Baqarah ring-center (131-144 Abraham) as a companion "anchor" in the same surah
- Q 42:4 and Q 20:110-111 as "compressed Ayat al-Kursī" verses
- Hidden/manifest pair from paired-opposites network as thematic cognate of J6
