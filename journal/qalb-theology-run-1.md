---
run: qalb-theology-run-1
phase: C
date: 2026-04-12
agent: Phase-C deep agent
target: /Users/grey/Downloads/quran/findings/phase-c-structures/qalb-theology.md
---

# Qalb-Theology — Run Journal

## Approach

1. Extracted all ROOT:qlb entries from the Quranic Arabic Corpus morphology table (128k lines). Raw count: 168 tokens across 9 distinct lemmas.
2. Separated noun lemma (qalob) from verb lemmas (inqalaba, qallaba, taqallub, etc.) and mapped each token to its (sura, verse) reference, yielding 155 unique verses.
3. Built a Python lookup joining:
   - quran-text/quran-no-tashkeel.json (Arabic + sura metadata including meccan/medinan type)
   - data/translations/en.sahih.txt (linear verse-by-verse English)
   - /tmp/qlb_verses_full.tsv (my derived tsv of ref + type + English)
4. Ran co-occurrence scans for: disease, seal/stamp, turn, tranquillity, reassure, fear, remembrance, faith, belief, hypocrites, soften, harden, blind. Every scan found exactly the predicted set (plus a few surprises: Q 83:14 *rāna* "covering" as another sealing-verb).
5. Extracted comparable root data for ṣadr (ROOT:Sdr, 46 tokens), fuʾād (ROOT:fAd, 16), lubb (ROOT:lbb, 16).

## Key statistics (verified)

- **Total q-l-b tokens**: 168
- **Unique verses**: 155 (Meccan 56, Medinan 99)
- **Nominal tokens**: 132 (112 plural *qulūb*, 20 singular *qalb*)
- **Verb tokens**: 25 (17 inqalaba, 6 qallaba, 2 nuqallibu/yuqallibu forms)
- **Verbal-noun tokens**: 11 (taqallub, mutaqallab, munqalab, munqalibūn)
- **Verses with 2+ qlb-tokens**: 13 (notably Q 13:28, the chiasmus ayah — two *qulūb* in chiasm)
- **Disease-in-hearts formula**: exactly 10 verses, **all Medinan** (verified by sura-type lookup): Q 2:10, 5:52, 8:49, 9:125, 22:53, 24:50, 33:12, 33:32, 33:60, 47:29.
- **Sealing verbs (khatama/ṭabaʿa/rāna)** on hearts: 12+ verses across both Meccan and Medinan.
- **Dhikr-qalb family**: 6 core verses (13:28, 18:28, 24:37, 39:22, 39:23, 57:16).

## Novel findings discovered in-run

1. **The q-l-b root's self-demonstration.** I had not expected the dominance of *turning* as the defining heart-action, but it becomes obvious once you lay out *qallaba* (qibla-turning, day-night, sleeper-turning, hearts-turning) side by side. The heart is etymologically *the turner*; the Quran makes this ontological.
2. **Grammatical voice tracks theological agency.** When Allah is subject of action-on-heart, the preposition is *fī* (into) or *ʿalā* (upon) — receptive heart. When hearts are subjects of their own state, the verbs are intransitive (rest, tremble, harden). The Quran encodes receptive vs expressive states grammatically.
3. **Q 22:46 nests the heart-terms explicitly**: *al-qulūb allatī fī ṣ-ṣudūr* — "hearts within breasts" — giving the Quran's own anatomy of ṣadr-containing-qalb. Tirmidhī's onion schema is authorised by the text itself.
4. **Fuʾād is NEVER object of divine seal/harden/soften, only of divine *strengthening***. The Prophet's heart is *fuʾād* when being firmed (Q 11:120, 25:32), but *qalb* is never so strengthened — it is the one that needs to *rest*. Different functional roles for different heart-terms.
5. **Lubb is never singular, never acted-upon.** It exists only as a *class-of-persons* (*ulū l-albāb*). The Quran reserves *lubb* for *achievement*, not *organ*.

## Things I checked and confirmed

- All 10 disease-in-hearts verses are Medinan. Verified by looking up sura_type for each.
- The Q 13:28 chiasmus has 2 qalb-tokens (one as subject *qulūbuhum*, one as noun *al-qulūb*). Confirmed via corpus.
- The Q 50:37 "whoever has a qalb" is the unique indefinite singular-qalb-as-subject use.
- Q 33:4 is the *qalbayn* ("two hearts in his interior") verse — the only dual form of qalb in the Quran, used to refute a pre-Islamic sociological error about adoption/divorce claims.
- The *sharaḥa aṣ-ṣadr* pattern (Q 6:125, 20:25, 39:22, 94:1) is exclusive to ṣadr. No *sharaḥa al-qalb* exists.
- The triad *samʿ + baṣar + fuʾād/qalb* appears with *fuʾād* in Q 16:78, 17:36, 23:78, 32:9, 46:26, 67:23 — and with *qalb* in Q 2:7, 16:108, 45:23. The two terms are interchangeable in sensory-triad contexts but not elsewhere.

## Decisions

- I included Q 83:14 *rāna* (rust/covering) in the sealing cluster because it functionally seals, but I marked it as a distinct root r-y-n — this is still within the broader seal-phenomenology.
- I resisted the temptation to read the four heart-terms as equivalent. The corpus evidence is strongly against that; each has a domain with minimal overlap.
- I kept the nafs-states ↔ heart-states correspondence to *structural* not lexical identification — but flagged the key fact that *ṭ-m-ʾ-n* is literally the same root used for both *nafs muṭmaʾinna* (Q 89:27) and *taṭmaʾinnu l-qulūb* (Q 13:28). This is the strongest lexical bridge between the Quran's two anthropologies.
- I used Sahih International for English throughout; where the translation obscures Arabic precision (e.g., *afʾida* rendered as "hearts" indistinctly from *qulūb*) I flagged the Arabic explicitly.

## Follow-ups for future phases

- The *ṭumaʾnīna/sakīna* terminology deserves its own deep-dive. Both "peace/descent" but used differently: *sakīna* is *sent-down* (external); *iṭmiʾnān* is *attained/arrived* (internal). Q 48:4 puts both in tension.
- The hypocrite sub-corpus (~60 Medinan verses) could be extracted as its own lexical study, with the marad fī qulūbihim formula as anchor.
- The *qallaba/inqalaba* verb-family is a candidate bridge between eschatology (Day of turning, Q 33:66) and psychology (hearts-turning) — worth its own analysis.
- Cross-check: does the same dhikr-qalb pattern extend to *tadhakkur*, *tadabbur*, *tafakkur*? These are the other "reflection" roots; if they also cluster with qalb, the Q 13:28 pattern is part of a larger receptive-interior network.

## Files produced

- `/Users/grey/Downloads/quran/findings/phase-c-structures/qalb-theology.md` — main findings (4530 words)
- This journal

## Ad hoc data files (temp)

- `/tmp/qlb_all.txt` — 168 qlb morphology rows
- `/tmp/qlb_verses_full.tsv` — (ref, type, English) for 155 verses
- `/tmp/sadr.txt`, `/tmp/fuad.txt`, `/tmp/lubb.txt` — sibling-root extractions
