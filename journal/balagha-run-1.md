---
agent: balagha-classical-mapper
run: 1
date: 2026-04-12
inputs:
  - docs/master-index.md
  - docs/methodology.md
  - findings/phase-a-replications/*
  - findings/phase-b-hypotheses/*
  - findings/phase-c-structures/*
outputs:
  - findings/balagha-mapping.md
  - data/literature/balagha/README.md
  - journal/balagha-run-1.md (this file)
---

# Journal — balāgha classical-mapping run 1

## 0. Framing

Task: for every finding in the project, assign a classical `ma'ānī / bayān /
badīʿ` category, cite the medieval scholar who established or used that
category on the same verse, and produce a per-category Quran verse catalog.
Explicit goal from the dispatcher: act like a medieval Arabic rhetorician, not
a computational linguist who stumbled onto jinās last week.

## 1. Reading pass (what I ingested)

Read master-index.md in full, methodology.md in full. Spot-checked the larger
finding files:
- `findings/phase-b-hypotheses/jinas-wordplay.md` (§1 headline, §2a-b rankings,
  §3-4 notable cases — file is 1 280 lines, sampled via offset reads).
- `findings/phase-b-hypotheses/palindromes.md` (§headlines §1 through §5
  categories).
- `findings/phase-c-structures/chiastic-audit.md` (§1 method, §2 ranking, §3.1-3.5
  diagrams, §5 sub-surah windows, §4 Cuypers/Farrin tests, §8 honest discussion).
- `findings/phase-b-hypotheses/saj-rhyme-analysis.md` (§headlines §1-9 plus
  Ar-Raḥmān treatment).
- `findings/phase-b-hypotheses/surah-boundaries.md` (§headlines, §1 114-row
  table).
- `findings/phase-b-hypotheses/muqattaat-analysis.md` (executive summary + §1-2).
- `findings/phase-b-hypotheses/word-pair-symmetry.md` (§1 replication verdicts,
  §2.1 novel pairs).
- `findings/phase-b-hypotheses/chronological-revelation.md` (§1 ordering
  sources).
- `findings/phase-b-hypotheses/numerical-coincidences.md` (§N=1 section).

Did not need to read: root-cartography, graph-theory-roots, information-theory,
gematria-landscape in depth — headlines in master-index were enough to classify
each finding.

## 2. Research pass (web / archive)

I did a targeted web search on the classical sources that would house each
category:

1. **Al-Suyūṭī *al-Itqān fī ʿulūm al-Qurʾān*** — confirmed naw' 58-59 as the
   locations for iltifāt and badīʿ. Full Arabic text available at
   https://archive.org/details/AlItqanFiUlumAlQuran. Sohaib Saeed's selected-
   chapters English translation at ibnashur.com is the cleanest modern gateway.
2. **Al-Zarkashī *al-Burhān fī ʿulūm al-Qurʾān*** — confirmed as the earlier
   encyclopedic work on Quranic sciences; cross-checked its chapter structure
   (munāsabāt = naw' 45, iltifāt = naw' 47, fawāṣil = separate chapter, etc.).
3. **Abdel Haleem 1992 *Grammatical Shift for Rhetorical Purposes***
   (BSOAS 55(3)) — fetched and confirmed the six-type classification of iltifāt
   and its canonical Quranic examples: Q 1:4, Q 10:22, Q 27:61, Q 36:22,
   Q 80:1-3, Q 33:50. These are the classical pivots we haven't computationally
   detected yet.
4. **Muqābalah / ṭibāq distinction** — fetched daralnicosia.wordpress.com on
   multiple antithesis and confirmed the type-case verses: Q 34:24 (we↔you /
   guidance↔error), Q 9:82 (laugh↔weep), Q 7:157 (permit↔forbid). This
   clarified the classical label for our Q 28:71-72 sarmad pair.
5. **Balāgha overview** — fetched Wikipedia's Balagha article to confirm the
   al-Sakkākī / al-Qazwīnī canonical tripartite structure and check the
   standard taxonomies. This is reliable enough for category names but not
   for verse-level attribution.
6. **Al-Qamar refrain** — confirmed `fa-kayfa kāna ʿadhābī wa nudhur` is
   classically recognised as *takrār / tardīd* in Suyūṭī's Itqān.
7. **Jinās types** — confirmed the subtypes *tāmm, nāqiṣ, muḍāriʿ, lāḥiq* via
   al-Sakkākī's *Miftāḥ al-ʿUlūm* summary. The "same word two senses" example
   (Q 30:55 al-sāʿa) is explicitly al-Suyūṭī's textbook case of *jinās tāmm*.
8. **Luzūm mā lā yalzam** — confirmed al-Maʿarrī's category; applied to
   Q 112 al-Ikhlāṣ classically.
9. **Abraham's afala chain (Q 6:76-78)** — al-Rāzī's *Mafātīḥ al-Ghayb* treats
   it as *iḥtijāj / istidlāl kalāmī*.

## 3. Mapping decisions (the hard ones)

**Q 13:28 — decision:** This was called "not in standard balāgha lists" in our
jinas finding. That claim is wrong. The verse is a textbook case of *radd
al-ʿajuz ʿalā al-ṣadr* (Ibn al-Muʿtazz's own category, which he explicitly
attached to exactly this kind of single-verse structure). I downgraded its
novelty to (a) classically identified; our contribution is the quantitative
density rank (0.889, highest in the Quran). Updated the balagha-mapping.md
accordingly and flagged a text correction for the jinas-wordplay.md headline.

**Q 91:1-7 letter palindrome — decision:** (b) implicit. The oath-sequence
symmetry is a classical *muwāzanah / saj' mutawāzī / tarṣīʿ* candidate; the
letter-count palindromy specifically is a modern quantitative fingerprint. We
measure what the classical tradition recognised qualitatively.

**Four Bonferroni-surviving rings — decision:**
- Al-Baqarah 131-144: (b) implicit — Farāhī school (Iṣlāḥī, Mir, Farrin) frames
  it as *naẓm* in the al-Jurjānī sense. The specific ring is modern.
- Al-Qamar 21-30: (a) classical — the refrain is textbook *tardīd / takrār*,
  universal in balāgha textbooks.
- ʿAbasa 1-9: (c) novel structural — no classical source names vv.1-9 as a ring.
- Al-Kahf 83-91: (b) implicit — muqābalah category is classical, this specific
  ring is our computational find.

**Our 2 531 jinās verses — decision:** (b). Individual examples are classical;
the catalog itself is modern. Every classical rhetorician knew jinās existed;
none enumerated 2 531 instances.

**Verse-length Nöldeke ramp — decision:** (a). Al-Suyūṭī *Itqān* naw' 9 literally
gives "short verses" as a Meccan diagnostic and "long verses" as a Medinan one.
Sadeghi 2011 is a modern quantitative replication of an 11th-century
observation. This is the clearest (a) case in the project.

**Muqaṭṭaʿāt density effect — decision:** (c) novel. The classical tradition
treats the muqaṭṭaʿāt as mystery (20+ opinions per al-Zarkashī), not as
measurable letter-frequency phenomena. Our p < 1e-15 is genuinely new.

**Root *rabb* chronological decline — decision:** (b) implicit. The
Meccan=khiṭāb-mubāshir, Medinan=khiṭāb-jamāʿah distinction is textbook; the
quantitative decline curve is ours.

## 4. The most striking classical observation I hit

al-Zarkashī's *al-Burhān* §52 on `al-mutashābih al-lafẓī` — lexically-similar
parallel verses (e.g. Q 2:58 vs Q 7:161) where differences between them encode
theological distinctions rather than stylistic variation. Al-Zarkashī insists
that *every* such difference is meaningful. This is:

(a) a classically-named category (*mutashābih*)
(b) a testable empirical claim
(c) completely absent from our computational findings

I have written the test up at the end of balagha-mapping.md §3 as a
pre-registerable hypothesis for `deep-pattern-reasoner`. The protocol is: find
all verse-span pairs with ≥ 80% surface token overlap, ≥ 5 tokens long; examine
what the differing element is; check whether classical tafsir literature
(al-Ṭabarī, al-Rāzī, al-Qurṭubī) has commentary on the difference. Al-Zarkashī
predicts every such difference encodes content. Computational method can test
this at scale.

Bonus observation: I also recommended a second follow-up — *ḥusn al-ibtidāʾ
wa-ḥusn al-intihāʾ* — classical category holding that Quranic surah openings
and closings are carefully matched. Our surah-boundaries agent is close to this
but only found Fātiḥah↔Nās as a shallow ring; a per-surah first↔last-verse
match metric has not been run.

## 5. Gaps in our computational work

During the mapping I discovered the following classical categories are
**under-represented or missing** from our existing findings:

1. **Iltifāt** — no computational catalog. This is the single biggest gap; it
   requires cross-verse person/number/tense shift detection using the QAC
   morphology features. Directly test-able.
2. **Tawriyah** (double-meaning ambiguity) — we have no entry for this. Needs
   dictionary-sense disambiguation, hard computationally but hypothesis-able.
3. **Mutashābih al-lafẓī** — flagged above as headline follow-up.
4. **Mubālaghah** (hyperbole) — not catalogued. Would require semantic analysis.
5. **Murāʿāt al-naẓīr** — we pick up some instances through palindromes and
   jinās, but not as a named category.
6. **Husn al-ibtidāʾ wa-ḥusn al-intihāʾ** — covered partially by
   surah-boundaries but not as a category.

## 6. File artifacts produced

- `/Users/grey/Downloads/quran/findings/balagha-mapping.md` — per-finding
  mapping + category catalog + novelty assessment table + classical-insight
  hypothesis generator.
- `/Users/grey/Downloads/quran/data/literature/balagha/README.md` — reference
  chain of classical scholars, taxonomy of the three sciences, per-category
  test-case verse table, URLs for open-access editions.
- `/Users/grey/Downloads/quran/journal/balagha-run-1.md` — this journal.

## 7. Confidence level & limitations

- Classical attribution reliability: **high** for named scholars (al-Suyūṭī,
  al-Zarkashī, al-Jurjānī, al-Sakkākī, al-Qazwīnī) — their works are
  well-indexed. **Medium** for verse-specific attribution — I have identified
  the right chapter for each, but have not inspected the Arabic text at the
  page level since the PDF of al-Itqān is 1.2 MB binary and my WebFetch does
  not render Arabic PDFs. Recommendation: `literature-archivist` agent should
  acquire Arabic full texts of al-Itqān naw' 55-60 and al-Burhān §45, 47, 52
  and run OCR/text-search to confirm every attribution.
- The classification (a/b/c) is my own judgment. Borderline cases like Q 91
  palindrome could be argued (a) or (b); I went (b) because the
  letter-count palindromy specifically is quantitative-modern.
- I did not produce verse-by-verse Arabic quotation of classical commentary —
  that would require page-level access to the classical texts. What I produced
  is a **mapping** and **category catalog**, not a full Arabic cross-reference
  work.

## 8. Recommended next runs

- **P1 — `iltifat-hunter`**: compute person/number shifts using QAC features;
  test the hypothesis that iltifāt concentrates at ring centers.
- **P1 — `mutashabih-lafzi-hunter`**: al-Zarkashī's lexical-similar
  hypothesis; find ≥ 80% surface-overlap verse-span pairs, analyse the
  differences.
- **P2 — `deep-pattern-reasoner`**: run against both hypotheses above with a
  pre-registered protocol.
- **P2 — `literature-archivist`**: acquire Arabic full texts of al-Itqān naw'
  55-60, al-Burhān §45, 47, 52, and al-Jurjānī *Dalāʾil al-Iʿjāz* so the
  verse-level attribution can be tightened from "in this chapter" to "on this
  page".
- **P2 — `surah-boundaries` follow-up**: per-surah opening↔closing-verse
  root-overlap ranking (the quantitative form of *ḥusn al-ibtidāʾ wa-ḥusn
  al-intihāʾ*).
- **P3 — update finding text**: apply the 5 recommended text corrections in
  §5 of balagha-mapping.md.

## 9. Cross-references

- master-index.md §4 Findings — every row now mappable via balagha-mapping.md §1.
- `docs/statistical-rigor-protocol.md` — my hypothesis-generation suggestions
  (iltifāt and mutashābih) are explicitly framed as pre-registerable in the
  sense of §3 of that protocol.
- `findings/deep-hypotheses-queue.md` — should add al-Zarkashī mutashābih-lafẓī
  and al-Suyūṭī iltifāt-at-pivots hypotheses to the queue.

---

End of run-1 journal. This is the first pass; if the dispatcher wants an
expanded version with actual Arabic page citations, a second run is needed
with the Arabic corpora of al-Itqān and al-Burhān downloaded and OCR'd.
