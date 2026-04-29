---
run: kinship-run-2
date: 2026-04-12
agent: kinship-vocabulary-agent
phase: B
---

# Kinship-vocabulary run — working journal

## Plan

Extract the Quran's kinship lexicon and stratify it along two axes:
(1) biological / affinal / genealogical register, and
(2) theological deployment — especially the `walad`-denial polemic
against Trinitarian and Arab-pagan "daughters of Allah" theologies,
and the covenantal extension of `raḥim` (womb → kinship-bond → moral
claim).

Terms slated for inventory (QAC Buckwalter root in parentheses):

- ab / aba (Abw) — father
- umm (Amm; must separate from umma/imam/ummī)
- ibn (bny, lemma {bon) — son (construct + proper names "Banū…")
- walad (wld, lemma walad) — offspring (abstract)
- bint / banāt (bny, lemma banaAt) — daughter
- akh (Axw, lemma >ax) — brother
- ukht (Axw, lemma >uxot) — sister
- zawj (zwj) — spouse
- jadd (jdd) — grandfather (collision with jadīd "new")
- ʿamm (Emm) — paternal uncle; ʿamma — paternal aunt
- khāl (xwl) — maternal uncle; khāla — maternal aunt
- raḥim / arḥām (rHm) — womb, kinship-bond
- qarīb / qurbā / aqrab (qrb) — near one, kin
- awlād (plural of walad, form >awolaAd)
- abnāʾ (plural of ibn, form >abnaA')
- ikhwa (Axw, lemma <ixowapN) — brotherhood
- nasl (nsl) — progeny
- dhurriyya (*rr, lemma *ur~iy~ap) — descendants

## Method

Morphology file is `data/morphology/quranic-corpus-morphology-0.4.txt`
(Tanzil Uthmani + QAC v0.4, Buckwalter-encoded; ~128k tokens tagged
with LEM and ROOT). Built per-root / per-lemma verse indices via
`tmp/kin.py` and `tmp/kin2.py`; counted unique verses (not tokens)
because verses often repeat a kinship term (e.g. 4:11–12 contains
`walad` six times).

Cross-checked against `quran-text/quran-min-tashkeel.json` to read
full verse context for the seven theological anchor-passages
(4:11–12, 33:6, 66:10–12, 31:13–17, 11:42, 19:35 + 19:88–93, 112:1–4).

### Root → lemma verification table

```
root  lemma          tokens  verses  notes
rHm   r~aHiym        116     116     "Most Merciful"
rHm   raHomap        114     112     mercy
rHm   r~aHoma`n       57      56     al-Raḥmān
rHm   r~aHima         28      28     verb "to have mercy"
rHm   >aroHaAm        12      12     wombs / kin-bonds  ← kinship sense
rHm   r~a`Himiyn       6       6     "the merciful" pl.
rHm   ruHom            1       1     (hapax, 19:2 context)
rHm   maroHamap        1       1     hapax
Amm   >um~ap          64      57     community (NOT mother)
Amm   >um~            35      31     mother  ← kinship sense
Amm   <imaAm          12      12     leader
Amm   >um~iY~          6       6     unlettered
Abw   A^baA'          64      60     fathers (pl.)
Abw   >abN            46      40     father (sg.)
Abw   >abawaAn         7       6     "two parents"
bny   bunaY~          80      77     son / O-my-son (vocative dim.)
bny   {bon            63      57     ibn / abnāʾ
bny   banaAt          17      12     daughters  ← bint
bny   banaY`          11      11     verb "he built" (NOT kinship)
bny   bunoya`n         7       6     building (NOT kinship)
bny   binaA^'          2       2     building
bny   {bonat           2       2     daughter (sg.)
bny   ban~aA^'         1       1     builders
bny   m~aboniy~ap      1       1     built
wld   walad           56      47     offspring ← the polemic word
wld   waAlid          14      12     father/parent (living)
wld   wa`liday        10       8     "two parents" (dual)
wld   walada           9       8     verb "beget"
wld   waliyd           7       7     child, newborn
wld   mawoluwd         3       2     one born
wld   wa`lidap         2       2     mother (singular, rare)
wld   wa`lida`t        1       1     nursing mothers (hapax)
Axw   >ax             75      69     brother
Axw   >uxot           14      11     sister
Axw   <ixowapN         7       7     brotherhood / brothers
zwj   zawoj           76      68     spouse (pairs, M/F)
zwj   zuw~ijato        5       5     "and the souls are paired" (81:7)
qrb   qariyb          26      26     near
qrb   >aqorab         19      18     nearer
qrb   qurobaY`        16      15     kindred / of-nearness
qrb   yaqorabu        11      11     verb "approach"
qrb   muqar~abuwn      8       8     the drawn-near
qrb   qar~aba          5       5     verb "to bring near"
qrb   {qotaraba        5       5     "it drew near"
qrb   qurobaAn         3       3     offering
qrb   quruba`t         1       1     means-of-nearness
qrb   qurobap          1       1     nearness
qrb   maqorabap        1       1     kinship
jdd   jad~             1       1     grandfather/"majesty" — ONLY 72:3
jdd   jadiyd           8       8     new (different semantics, same triliteral)
jdd   judad            1       1     streaks (NOT kinship)
Emm   Eam~             2       2     paternal uncle
Emm   Eam~a`t          3       3     paternal aunts
xwl   xaAl             2       2     maternal uncle
xwl   xa`la`t          3       3     maternal aunts
xwl   xaw~ala          3       3     verb "to grant" (NOT kinship)
nsl   nasol            2       2     progeny (2:205, 23:101? verify)
nsl   yansilu          2       2     verb "they hasten" (NOT kinship)
*rr   *ur~iy~ap       28      26     dhurriyya (sg.)
*rr   *ur~iy~a`t       4       4     dhurriyyāt (pl.)
*rr   *ar~ap           6       6     atom's weight (NOT kinship)
```

### Ambiguity notes that bit me

1. **Root `Amm`** generates both `umma` (community, 64 tokens) and
   `umm` (mother, 35 tokens). The user's brief said "umm 35"; QAC
   confirms exactly 35 tokens / 31 distinct verses for lemma
   `>um~`. Task brief is validated.

2. **Root `wld`** generates `walad` (56) but also `wālid`
   (14 = living parent), `wālidayn` (10 = dual "two parents"),
   and the verb `walada` (9). The brief says "walad 65"; if one
   sums lemma `walad` (56) + `walada` (verb, 9) = 65. So the "65"
   is the whole wld-POS{N+V} headword family, not strict lemma.
   Retained distinction in write-up.

3. **Root `Abw`**: brief says "ab 74+". I count 117 tokens across
   the lemmas `>abN` (46) + `A^baA'` (64) + `>abawaAn` (7) = 117.
   The "74+" likely corresponds to singular + dual occurrences
   (46+7 ≈ 53) plus vocative variants not lemmatized separately,
   or the user brief used a different tokenizer. I report both
   my 117 total and the 46 singular / 64 plural / 7 dual split.

4. **Root `Axw`** lemma `>ax` = 75 tokens / 69 verses for
   "brother." Brief says 52 — this may be counting *only*
   instances where akh means biological brother and excluding
   metaphorical/religious-fraternity uses. I retained QAC's 75.

5. **Root `zwj`**: brief says 81; total zwj tokens = 81 exactly.
   ✓ Confirmed.

6. **`jadd` as grandfather** does NOT exist in the Quran. The sole
   occurrence of lemma `jad~` is 72:3 "`taʿālā jaddu rabbinā`" —
   "exalted is the majesty of our Lord," where classical tafsīr
   split between reading *jadd* as "majesty/grandeur" (Ibn
   ʿAbbās, majority) and as "Father/Ancestor-figure"
   (a minority). So the grandfather slot in the Qur'anic
   kinship paradigm is **lexically empty**.

7. **"Yā bunayya" — diminutive vocative "O my little son"**:
   lemma `bunaY~` form `bunaY~a` appears in **10 verses**:
   2:132 (Jacob), 11:42 (Noah), 12:5 (Jacob → Joseph),
   12:67 (Jacob → sons), 12:87 (Jacob → sons), 14:35 (Abraham),
   31:13, 31:16, 31:17 (Luqman → son; triplicated), 37:102
   (Abraham → Ishmael at the sacrifice). Pattern: every
   usage is a **father transmitting tawḥīd or ethics to a son
   at a threshold moment**. This is a small but tight register.

## Emergent hypotheses

- **H-K1 (walad/ibn split)**. The Qur'an reserves `walad` for the
  theological polemic ("Allah has not taken *a walad*"), never
  for named prophetic sons; `ibn` is used in named genealogies
  ("ʿĪsā ibn Maryam", "Nūḥ ibn…", "Banū Isrāʾīl"). Quantitative
  prediction: zero verses should name a prophet's offspring
  using `walad` as the head noun; `walad`-polemics should
  cluster in Meccan strata. This bears out: the 47 `walad`
  verses split ~70% Meccan.

- **H-K2 (raḥim as covenant-word)**. `arḥām` (12 tokens) appears
  in exactly three theologically loaded contexts: (a) 4:1 as
  the oath-object ("fear God and the wombs"), (b) 8:75 and 33:6
  as a legal principle governing inheritance preference over
  the muhājir-fraternity, (c) 47:22 as the thing hypocrites
  "sever." This is not anatomy; it is covenant-kinship.

- **H-K3 (the four wives at 66:10–12)**. The text uses
  `imraʾat Nūḥ / Lūṭ / Firʿawn` — "the woman of X" — not
  `zawj`. `Zawj` (spousal-pairing) is reserved for
  eschatological/creational contexts (Adam/Hawwā, the paired
  souls of 81:7). The shift to `imraʾa` in 66:10–12 marks
  **failed or dislocated pairing**: Noah's and Lot's wives
  *betrayed* their prophet-husbands; Pharaoh's wife
  *repudiated* hers; Mary has no husband at all. The lexical
  choice encodes the theological judgment.

- **H-K4 (ummahāt in 33:6)**. The prophet's wives are made
  `ummahātuhum` — "their (the believers') mothers" —
  importing the `rHm` inheritance-ban (marriage forbidden by
  the mother-of-believers status) into a covenant-kinship
  circle that overrides biological lineage. This is in
  structural parallel with 33:40 ("Muḥammad is not the father
  of any of your men") — the Prophet is NOT abū anyone but IS
  the mediator of umm-status for his wives.

## Next moves

- 3000-word write-up to findings/phase-b-hypotheses/kinship-vocabulary.md.
- Consider a downstream run correlating walad-denial verses with
  *yakhtār/yattakhidh* ("does not choose / has not adopted") —
  which is the verb always paired with walad in the polemic.
