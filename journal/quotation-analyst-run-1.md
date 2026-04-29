---
phase: B
agent: quotation-analyst
run: 1
date: 2026-04-12
finding: findings/phase-b-hypotheses/quotation-analysis.md
csv: findings/phase-b-hypotheses/quotations-catalog.csv
---

# Journal — Quotation Analyst, Run 1

## Goal

Systematic analysis of DIRECT SPEECH in the Quran. Who speaks, how often, in what
style. Build a quantitative speaker-ranking and a per-speaker rhetorical profile.

## Method

1. Extracted all tokens of root q-w-l from the Leeds/Dukes morphology (v0.4) —
   **1,722 tokens**. Of these, 1,620 are verbal forms and 102 are the noun *qawl*.
2. Classified each verbal form by aspect × person × voice. Derived the sub-corpora:
   *qāla* (532), *qālū* (332), *qul* (332), *yaqūlūna* (119), *yaqūlu* (74),
   *qīla* (52), *qālat* (43), *qulnā* (27), *quwlū* (12), *naqūlu* (12).
3. Attributed each speech event to a speaker via an NER-over-Sahih pipeline (25
   named characters + 9 collective classes), with 3-verse backward propagation
   for dialogue continuation. 1,247 of 1,620 events attributed (77%).
4. Spot-checked the top-10 named speakers against the Arabic text and English
   translation — accuracy ≥90% for named prophets; slightly lower for collectives
   (Disbelievers vs Jews vs People of the Book) where Sahih renders ambiguously.
5. Cross-analyzed with:
   - Moses deep-dive (findings/phase-c-structures/moses-deep-dive.md)
   - Prophet pericope comparison (findings/phase-c-structures/)
   - Iltifāt catalog (findings/phase-b-hypotheses/iltifat-catalog.md)
   - Intra-Quranic cross-references (the 9-fold prophetic refrain)
   - Mutashābih lafẓī (findings/phase-b-hypotheses/mutashabih-lafzi.md)

## Key numerical findings

- 1,620 verbal q-w-l speech events total
- 332 *qul* imperatives (divine→Muhammad "Say!") across 306 verses
- Moses speaks 184 times (most of any human, by a factor of 2.4 over #3)
- Pharaoh 49 events across 10 surahs (densest in S26)
- Iblīs 48 events across 4 canonical retellings of one scene
- 23% of events are UNCLASSIFIED (generic "they said")
- 10 top speakers account for 90% of classified events

## Surprising findings

1. **Qul is bigger than Moses.** The divine imperative "Say!" — 332 events — is a
   larger speaker-class than any human speaker. This is a formal-literary fact
   about the Quran that is rarely stated in quantitative terms.

2. **Moses's speech-to-name ratio is 1.35**, but **Joseph's is 2.41** — Joseph
   dialogues more intensely relative to how often he's named, because S12 uses
   pronouns heavily after first naming.

3. **Q 40:28-44 is the Quran's longest non-prophetic monologue** (18 verses) —
   and it's by an unnamed "believing man of Pharaoh's family." A neglected
   narratological landmark.

4. **Paradise = companionable, Hell = adversarial.** The saved always speak *with*
   each other (mutual reminiscence); the damned always speak *against* each other
   (blame-shifting). This binary is stable across all eschatological dialogue
   passages (Q 7, 37, 38, 43, 52, 56).

5. **Four-level nesting in Q 2:67-71.** Moses reports God's reply to the
   Israelites' question within God's revelation to Muhammad within the recited
   Quran. Four levels of embedded quotation in a single passage.

6. **Iblīs's "pride-argument" is four-fold mutashābih-lafẓī.** The prostration
   refusal is retold in S7, S15, S17, S38 with the same structural elements
   (pride → reprieve → expulsion → threat → exception) but different lexicalization
   in each. One event, four angles.

7. **Non-human voices**: ant, hoopoe, earth, sky, Hell-fire, human skin, human
   hands and feet all speak directly. The Quran has a universally-vocal
   dialogical ontology.

## What I did NOT fully resolve

- Full Arabic-side content taxonomy of the *Qul* corpus. I used English
  proxies. A follow-up would tokenize the Arabic opening n-grams of each Qul
  clause.
- Word-count-weighted speaker volume (vs event-count). Moses would dominate even
  more by words-spoken than by events.
- Nested speech depth was measured by counting English "said"/"Say" — a
  rough proxy. Arabic-side *iḍāfa*-of-speech parsing would give exact depths.

## Deliverables

- findings/phase-b-hypotheses/quotation-analysis.md
- findings/phase-b-hypotheses/quotations-catalog.csv (1620 rows)
- This journal
