---
agent: vocative-addresses-run-1
date: 2026-04-12
phase: phase-b-hypotheses
status: complete
---

# Journal — Vocative Addresses Run 1

## Aim

Map every vocative (يا + noun, يا أيها + epithet) in the Quran, classify
by addressee, and test the hypothesis that "O you who believe" is a
Medinan legal-register formula with near-zero Meccan presence.

## Method

1. **Loaded data**: `quran-text/quran-no-tashkeel.json` (6236 verses),
   `data/revelation-order.csv` (Egyptian Standard + Nöldeke periods),
   `data/translations/en.sahih.txt` (Sahih International, 6249 lines).
2. **Regex scan** over the no-tashkeel Arabic for `يا\s+X` and
   `يا\s*أيها\s+X`. First pass yielded 357 verses and 62 distinct
   addressee classes.
3. **Manual curation** of edge cases:
   - Y/N on whether `يا أيه الساحر` (Q 43:49) counts as vocative — YES
     (Pharaoh's mocking address to Moses).
   - Y/N on `يا بني` occurring inside "O Children of Adam/Israel" — kept
     separate from the narrower "O my son" bucket by negative lookahead.
   - The lament particles (*yā layta*, *yā wayl*, *yā ḥasratan*) kept as
     vocatives per Al-Zarkashī's *nidāʾ al-tafajjuʿ* classification, even
     though they have no animate addressee.
4. **Content classification** for the 89 "O believers" verses: first
   word after آمنوا tabulated, then collapsed into 12 super-categories.
5. **Period breakdown** via the Egyptian Standard mushaf-to-period
   mapping.
6. **Statistical check**: binomial log-probability of 89/89 Medinan
   under a uniform-per-verse null (p_Medinan = 1623/6236 = 0.260).
7. **Ring-center cross-reference** against the 5 Bonferroni-surviving
   ring centers from `ring-center-semantics.md`.

## Key findings

- **357 vocative verses** (~5.7% of the Quran), 62 addressee classes.
- **89 "O you who believe" verses, 100% Medinan** (zero in 86 Meccan
  surahs). Log-p ≈ −119.8 ⇒ p ≈ 10⁻⁵² under uniform null.
- **49 "O my people" verses, 92% Meccan**: the polar-opposite formula.
- **13 "O Prophet" verses, 100% Medinan**: all military / marital /
  community-authority; none private-theological.
- **20 "O mankind"** split 10/10 Meccan/Medinan: the universal address.
- **12 "O People of the Scripture" (all Medinan)**: all polemical.
- **1 "O you who disbelieve"** (Q 109:1) — the Quran's only direct
  adversary-vocative.
- **12 hapax vocatives** — including the only non-human speaker of a
  vocative (an ant-queen, Q 27:18), the only address to earth/sky (Q
  11:44), fire (Q 21:69), mountains (Q 34:10).
- **"O Prophet" content**: 3/13 military, 6/13 marital/domestic, 3/13
  community-authority, 1/13 role-declaration. No private-theological.
- Meccan-Prophet vocative ≠ Medinan-Prophet vocative: the Meccan
  register uses the state-of-being epithet (*muzzammil / muddaththir*),
  the Medinan register uses the institutional title (*nabiyy / rasūl*).

## Content-class distribution for "O believers" (89 verses)

| class | n |
|---|---:|
| Prohibition (لا + V) | 27 |
| Positive imperative | 25 |
| Conditional / legal frame (إذا / إن) | 18 |
| Fear God (اتقوا) | 7 |
| Reproach / question | 3 |
| Prescribed (كتب) | 2 |
| Indicative info (إنما) | 2 |
| Legal stipulation (شهادة / ليستأذنكم) | 2 |
| Other conditional / divine assertion | 3 |

**92% are imperative / prohibitive / conditional.** The vocative is a
legal-opener.

## Top-5 surahs by O-believers density

S49 Al-Ḥujurāt (27.8%), S60 Al-Mumtaḥanah (23.1%), S61 Aṣ-Ṣaff (21.4%),
S58 Al-Mujādilah (13.6%), S5 Al-Māʾidah (13.3%).

## Negative / null results

- Ring-center overlap: only 1 of 5 centers contains a vocative (Hud 11:62).
  Not statistically surprising (p(≥1/5 | p=0.057) ≈ 0.26). But the
  qualitative observation (the one overlap is "Thamūd calling Sāliḥ by
  name to reject him" — a vocative-that-is-also-a-rhetorical-question)
  is consistent with the ring-center-questions finding.
- No meaningful vocative presence in Ar-Raḥmān (1 single *yā maʿshara*).
  Ar-Raḥmān's rhetorical engine is the question-refrain, not vocatives.

## Outputs

- `/findings/phase-b-hypotheses/vocative-addresses.md` (main finding)
- `/findings/phase-b-hypotheses/vocatives-per-verse.csv` (357 rows)
- `/findings/phase-b-hypotheses/vocatives-per-class.csv` (62 rows)
- this journal.

## Limitations

- Regex misses any orthographic ياأيها run together; Tanzil no-tashkeel
  corpus appears consistently spaced, but not exhaustively verified.
- Sahih translation has ~0.2% line-count drift (6249 vs 6236); English
  citations are illustrative only; all quantitative claims use Arabic.
- Command typology is heuristic by first-word-after-آمنوا; a tafsir-
  informed human label would move a few borderline cases.
- Not pre-registered. Meccan/Medinan expectation for "O believers" was
  priorknowledge (classical consensus); p ≈ 10⁻⁵² confirms rather than
  discovers.

## Time-to-completion

Single pass, ~1 hour equivalent. No iterations needed after the initial
regex; the pattern is linguistically crisp.
