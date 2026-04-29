# synthesis-scholar — run 1

**Date:** 2026-04-12
**Agent:** synthesis-scholar
**Role:** chief narrative synthesis; weaves computational findings + classical scholarship
**Output:** `/Users/grey/Downloads/quran/findings/scholar-commentary.md`

## Reading trajectory

1. Required foundation docs — design, methodology, master-index, statistical-rigor-protocol, claims-catalog (head).
2. Full `phase-a-replications/code19-khalifa-full-audit.md` (~414 lines).
3. Full `phase-a-replications/middle-ayah-al-baqarah.md` (~203 lines).
4. `phase-b-hypotheses/numerical-coincidences.md` — headers only + rahma=114 section + striking-list synthesis block.
5. `phase-b-hypotheses/jinas-wordplay.md` — headline numbers + top-density + Q 13:28 entry + Q 28:71-72 srmd pair.
6. `phase-c-structures/chiastic-audit.md` — method + whole-surah ranking + Bonferroni-surviving sub-surah rings (Al-Baqarah 131-144, Al-Qamar 21-30, 'Abasa 1-9, Al-Kahf 83-91) + Farrin macro-ring negative result + Cuypers Al-Ma'ida negative result.
7. `phase-b-hypotheses/palindromes.md` — Ash-Shams 7-verse palindrome, Q 33:3, Q 13:28 crossover.
8. `phase-b-hypotheses/information-theory.md` — Zipf α=1.318, Heaps β=0.618, entropy, Ar-Rahman compression signature.
9. `phase-b-hypotheses/chronological-revelation.md` — Nöldeke 4-phase verse-length ramp, Muhammad proper name, rabb decline.
10. `phase-b-hypotheses/muqattaat-analysis.md` — Stouffer Z=+4.48, two-null confirmation, ALM + qaf drive the signal.
11. `phase-b-hypotheses/root-cartography.md` — Yusuf fingerprint (sjn=12, qms=6, khf=6), McKay denominator (2,817 matching pairs).
12. `phase-b-hypotheses/word-pair-symmetry.md` — yawm/layl, bahr/barr, hayat/mawt all failed; malak/shaytan=88/88 the only clean replication.
13. `data/translations/en.sahih.txt` — Sahih English for 2:143 (line 150), 13:28 (line 1735), 21:107 (line 2590).

## Key structural decisions for the commentary

- **Tone:** Reynolds/Neuwirth/Sinai register: rigorous, respectful, non-polemical, non-apologetic. Use Arabic with transliteration for key terms (*raḥma*, *wasaṭan*, *jinās*, *tarṣīʿ*, *muqaṭṭaʿāt*).
- **Structural rhythm:** Preface → Part I (foundations) → Part II (audit of published claims) → Part III (novel findings) → Part IV (negative ledger) → Parts V-VII as placeholders for agents still running (tafsir-xref, classical-balagha, intra-quranic-xref) → Part VIII (what would change everything) → Part IX (open questions) → Part X (acknowledgments).
- **Three narrative threads identified** that unify everything:
  1. **Rule transparency is destiny.** Every disputed claim stands or falls on whether its counting rules are disclosed. The project's contribution is not new claims but the reproducible substrate beneath them.
  2. **Form enacts content at the small scale; ring composition is rare at the large scale.** Honest replication finds jinas and micro-rings everywhere (Q 13:28, Al-Baqarah 131-144, Q 28:71-72) but falsifies most whole-surah and whole-Quran ring claims (Cuypers Al-Ma'ida, Farrin macro).
  3. **The Khalifa / Al-Kaheel / Bible-Codes parallel.** McKay 1999 is the methodological template; the Phase A audit is effectively the first McKay-style treatment of Code-19.
- **Always cite findings by their markdown filename** so the reader can follow up.
- **Every numerical claim must fingerprint its rule tuple** (e.g. `[nt/rw/b1]`).
- **Open questions for the next wave:**
  - Comparable-corpus baseline for rahma=114 (is it really the only lemma with count 114 vs. a classical Arabic prose corpus of 77k tokens?). The `cross-baseline` agent is running but has not returned.
  - Whether the Yusuf fingerprint effect (rare-root = surah number) generalises to other surahs (khf=6 in Q 18 is the only known sister).
  - Pre-registered test of the qaf-50/42 trio as a single claim rather than cherry-pick.
  - Muqatta'at density effect against a classical Arabic baseline (3-gram Markov is a weak null; Bukhari block draws are the next step).
  - Phonetic-jinas measure independent of root identity (to catch tarsīʿ patterns the QAC root field misses).
  - Does the monotone Muhammad=post-Hijra asymmetry hold under alternative chronologies (Nöldeke vs Egyptian vs Bazargan)?
  - Whether the information-theory Zipf α=1.318 signature survives comparable-corpus control.

## Execution notes

- Target length 4000-5000 words. Written long-form scholarly prose, not bulleted.
- Cross-reference to files by relative path from the findings/ directory.
- Mark sections V-VII explicitly as "reserved for in-flight agent output" so the file is honest about its placeholder status.
- Orchestrator gets a 700-word summary returned as the assistant message.

## Status at finish

- Commentary drafted and written.
- No new data computed; pure synthesis.
- Honest ledger maintained throughout.
