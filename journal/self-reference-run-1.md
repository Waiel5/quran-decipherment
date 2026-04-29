---
run_id: self-reference-run-1
phase: B
date: 2026-04-12
agent: Phase B deep agent — Quranic self-reference
inputs:
  - /Users/grey/Downloads/quran/quran-text/quran-no-tashkeel.json
  - /Users/grey/Downloads/quran/data/morphology/quranic-corpus-morphology-0.4.txt
  - /Users/grey/Downloads/quran/findings/intra-quranic-cross-references.md
  - /Users/grey/Downloads/quran/findings/khawatim-al-hashr-analysis.md
  - /Users/grey/Downloads/quran/docs/master-index.md
output: /Users/grey/Downloads/quran/findings/phase-b-hypotheses/quranic-self-reference.md
---

# Journal — Quranic self-reference run 1

## Method
- Normalization: collapse all alef variants (آ إ أ ٱ → ا), alif-maksūra ى → ي, tā marbūṭa ة → ه. Applied to every verse of the no-tashkeel JSON before regex.
- Root verification cross-checked against the Kais Dukes morphology (ROOT:qrA, ROOT:frq, ROOT:*kr, ROOT:Hqq, ROOT:nzl).
- "Self-reference" defined strictly: the noun refers to THIS revelation (the Qurʾān-text) and not to Torah, Gospel, the genus "book," or unrelated homograph (e.g., dhikr = "male").

## Key counts (verse-level)
- hādhā l-Qurʾān (the definite deictic self-reference) — 16 verses (list below).
- al-Qurʾān (definite, any context referring to the revelation) — 50 verse-occurrences.
- al-Furqān — 6 verses, 4 of them referring to the revelation to Muḥammad.
- al-Dhikr as Quran-name — 11 verses (excluded: ahl al-dhikr, al-dhikr=male).
- al-Dhikrā — 8 verses.
- al-Furqān — 7 tokens, 6 verses.
- tanzīl (verbal noun, "the sending-down") — 15 verses, effectively all self-referential.
- al-Ḥaqq referring to the revelation — c. 12 verses under "huwa l-ḥaqq" + 15+ under "bi-l-ḥaqq nazzalnāhu/anzalnāhu."
- al-Nūr = the Quran — Q 4:174, 5:15, 7:157, 42:52, 64:8 (5 clear).
- al-mathānī — 2 verses (Q 15:87, Q 39:23).
- kitāb mubārak — Q 6:92, 6:155, 38:29 + "dhikr mubārak" Q 21:50 (4 total).
- qurʾān + explicit descriptor — karīm 56:77, majīd 85:21, mubīn 15:1 + 36:69, ʿaẓīm 15:87, ʿajab 72:1, ʿarabī 12:2, 20:113, 39:28, 41:3, 42:7, 43:3, 46:12.
- Challenge verses — 3 canonical ("produce surah/10 surahs/like it"): Q 2:23, 10:38, 11:13; + Q 17:88 (total Qurʾān); + Q 52:33-34 (produce "ḥadīth mithlihi"). Five challenge-verses total.

## Novel observations during the run
1. The genre-rejection stack in Q 69:40-47 and Q 81:19-25 reads like a formal **seven-way genre denial**: not poet, not soothsayer, not possessed (majnūn), not Satan's speech, not fabrication (tuqawwul), not asāṭīr al-awwalīn, not siḥr. These are the seven negations against which the Quran positions itself.
2. "hādhā l-Qurʾān" is distributed almost entirely in Meccan surahs (15 of 16 — Q 59:21 is the sole Medinan). The deictic self-gesture is a polemical device tied to the Meccan apologetic.
3. Q 75:17-19 is the strongest meta-programmatic statement: collection, recitation, explication are ALL divine obligation. Three distinct acts of textuality (jamʿ, qurʾān, bayān) in three consecutive verses. This is the Quran's own self-description as a text under production.
4. Q 17:82 + Q 17:88 + Q 17:89 + Q 17:106 cluster four meta-Quranic statements in one surah, plus Q 17:9 — Surat al-Isrāʾ is the densest self-reference surah.
5. mathānī in Q 39:23 is yoked to mutashābih ("tashābaha... mathānī"). The verse doesn't just name the text — it describes its compositional method: self-similar twinned parallels. The two mathānī verses (15:87, 39:23) encode two different scalings of the same structural principle.
6. Descriptor-adjectives cluster into two theological families:
   (a) the "dignity" family: karīm / majīd / ʿaẓīm / kitāb maknūn / lawḥ maḥfūẓ (the Quran as precious object)
   (b) the "function" family: mubīn / mubārak / hudan / shifāʾ / rahma / nūr (the Quran as active agent)
   These correspond to the *ontological* vs the *operational* descriptions of the text.
7. The "ummī" / "self-taught" motif (Q 29:48, 7:157, 62:2) pairs with the challenge verses: the Quran's self-description includes a claim about its human vessel's inability to have composed it.
8. "qawl rasūl karīm" appears twice in near-identical form — Q 69:40 (of Muḥammad, via denial of poetry) and Q 81:19 (of Gabriel). The same formula frames both ends of the revelation chain.

## Pitfalls
- al-Ḥaqq has enormous semantic range. Only verses where "al-ḥaqq" refers specifically to the revealed content (vs. God as al-Ḥaqq, or an abstract concept) count as self-naming. "huwa l-ḥaqq min rabbika/rabbihim" (Q 2:91, 32:3, 34:6, 35:31, 47:2, ...) is the diagnostic formula.
- al-Kitāb is over 250 tokens. Only a subset refer to the Quran (many refer to Torah, to the heavenly Kitāb, to records, etc.). In context, "tilka āyātu l-kitāb" openings (Q 10:1, 12:1, 13:1, 15:1, 26:2, 27:1, 28:2, 31:2) are self-naming.
- "dhikr" homographs (the male dhikr = Q 3:36, 53:21, 53:45, 75:39, 92:3, 6:143, 6:144) must be excluded — easy to over-count.

## Cross-links
- master-index: category "self-reference / meta-textual" — this finding creates it.
- khawatim-al-hashr-analysis: Q 59:21 is the Medinan exception to the hādhā-l-Qurʾān Meccan pattern, and stacks self-reference + divine-name density.
- intra-quranic-cross-references: Q 39:23 already established as the self-describing "mathānī" verse.
- parables-catalog: Q 59:21 (parable about the Quran's own power).
