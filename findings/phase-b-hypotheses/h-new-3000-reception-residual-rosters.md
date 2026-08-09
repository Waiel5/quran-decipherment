---
id: H-NEW-3000
title: "The reception-residual rosters — per-verse structure against formal ḥadīth reception, and a locked SUPPORTED verdict that does not survive an exact test"
phase: B
date: 2026-08-09
author: Waiel Al-Shujaa
status: "COMPLETE — the two rosters are delivered. The locked verdict is SUPPORTED under the pre-registered rule; POST-HOC exact tests do not support it, and the correction is §6."
prereg: findings/phase-b-hypotheses/prereg-h-new-3000-reception-residual-rosters.md
prereg_sha256: 6515fe1a12ebf742e3ab72d5c6e18e8c5a82d1c0a4f4fd894aa9397eed344789
script: findings/phase-b-hypotheses/scripts/h-new-3000.py
posthoc_scripts: [findings/phase-b-hypotheses/scripts/h-new-3000-posthoc.py, findings/phase-b-hypotheses/scripts/h-new-3000-posthoc-2.py, findings/phase-b-hypotheses/scripts/h-new-3000-posthoc-3.py]
run: findings/phase-b-hypotheses/runs/h-new-3000/20260808T235345Z
posthoc_runs: [findings/phase-b-hypotheses/runs/h-new-3000/20260808T235632Z-posthoc, findings/phase-b-hypotheses/runs/h-new-3000/20260808T235824Z-posthoc-2, findings/phase-b-hypotheses/runs/h-new-3000/20260808T235958Z-posthoc-3]
deliverables: [findings/phase-b-hypotheses/csv/h-new-3000-roster-1-structurally-unusual-rarely-cited.csv, findings/phase-b-hypotheses/csv/h-new-3000-roster-2-heavily-cited-structurally-ordinary.csv]
instruments: [findings/phase-b-hypotheses/h-new-2990-verse-profile.md, findings/phase-b-hypotheses/h-new-860-1-fadail-formal-count.md]
closes: findings/phase-b-hypotheses/OPEN-H-NEW-2980-reception-residual.md
method_parents: [findings/UNIT-DRIFT-DEFECT.md, findings/ABSENCE-CLAIMS.md]
analogue: findings/phase-b-hypotheses/h-new-2620-tafsir-contested.md
seed: 20260509
seed_replication: 20260519
bonferroni_k: 6
alpha_bonferroni: 0.00833333
verdict_locked: SUPPORTED
verdict_after_exact_tests: NULL
---

# H-NEW-3000 — the reception-residual rosters

## 0. The answer, in one place

**Two rosters exist, and they are the deliverable.** They were written to disk before any
inference was computed, and they stand whatever the inference says.

**The inferential arm returned SUPPORTED under the pre-registered rule — and that verdict does
not survive an exact test.** Three of six inferences cleared Bonferroni α = 0.00833 on
parametric p-values. `n_hadith` is **86 % tied at zero**, the t-approximation behind those
p-values is not trustworthy on such data, and when the same arms are judged by an exact
permutation null using the same statistic:

| arm | partial ρ | parametric p(+) | **exact p(+)** | factor |
|:--|--:|--:|--:|--:|
| **I1** `struct_z_composite` | +0.0493 | **0.00015** ✔ | **0.0081 / 0.0091** | **57×** |
| I3 `frac_hapax_root_tokens` | +0.0168 | 0.1098 | 0.2935 | 2.7× |
| **I4** `mean_root_surprisal_bits` | +0.0328 | **0.00809** ✔ | **0.1023 / 0.1116** | **13×** |
| I5 `frac_root_tokens_freq_le5` | +0.0273 | 0.0229 | 0.1304 | 5.7× |
| **I6** `−log10(rime_class_size)` | +0.0883 | 9.0 × 10⁻¹¹ ✔ | **0.0001** | — |

*(✔ = cleared the locked α. Two seeds reported where they straddle it.)*

**Only I6 survives an exact test — and I6 is a between-surah effect wearing a verse-level
column.** `rime_class_size` is the most surah-loaded column in the instrument (η² = 0.411 by
surah). Re-cut so that each verse carries its **deviation from its own surah's mean**, with
53 % of the column's variance retained, the association collapses:

> **I6, surah-mean-centred: ρ +0.0883 → +0.0284, exact p 0.0001 → 0.0193. It fails.**

**Nothing verse-level survives.** The honest terminal statement is the one the
pre-registration expected: **there is no measurable verse-level relationship between formal
ḥadīth reception and per-verse structure once length is held fixed** — which is what
H-NEW-2620 found for tafsīr and H-NEW-860.1 found at surah level.

**The largest effect anywhere in this test explains 0.78 % of the variance, and it is the one
that turns out to be a surah property. The rest explain 0.03 % to 0.24 %.**

---

## 1. The two rosters

`csv/h-new-3000-roster-1-structurally-unusual-rarely-cited.csv` and
`csv/h-new-3000-roster-2-heavily-cited-structurally-ordinary.csv` — 30 rows each, 25 columns:
reference, surah name, **full verse text**, word count, length decile, `struct_z_composite`,
**struct rank**, within-decile structural percentile *S*, `n_hadith`, **reception rank**,
within-decile reception percentile *R*, the mismatch score *M*, `n_books`, `n_hadith_all17`,
the driving span, the four composite members, and two repetition flags.

### 1.1 How a verse gets onto a roster

Locked in prereg §5 before anything was computed. Within each of ten **length deciles**:

- **S** = the verse's mid-rank percentile on `struct_z_composite` among all verses of its decile;
- **R** = **exactly 0** if the verse is never quoted; otherwise its mid-rank percentile among
  the **cited** verses of its decile;
- **M = S − R.** Roster 1 is the top 30 by *M*; roster 2 is the top 30 by *−M*.

> **Why R collapses the zero block to 0, and why that decision had to be made in advance.**
> 86 % of eligible verses carry no citation. Under a plain percentile every one of them scores
> ≈ 0.43 and a *singly*-cited verse ≈ 0.87 — so a verse quoted once would outrank Q 112:1's
> 102 on a hair of structural difference, and the "heavily cited" roster would fill with
> once-cited verses. **The concentration is a property of the object, and the instrument
> encodes it instead of being deformed by it.**

### 1.2 Roster 1 — structurally unusual, rarely cited

All thirty carry **zero** ḥadīth citations. Every length decile is represented (4/1/4/3/4/3/3/3/3/2),
so this is not a roster of short verses or of long ones.

| # | verse | w | comp | struct rank | the verse |
|--:|:--|--:|--:|--:|:--|
| 1 | **Q 111:5** | 5 | **+5.19** | **1** | *fī jīdihā ḥablun min **masad*** — the palm-fibre rope |
| 2 | **Q 37:47** | 7 | +4.57 | 4 | *lā fīhā **ghawl** wa-lā hum ʿanhā **yunzafūn*** |
| 3 | **Q 38:3** | 10 | +2.80 | 35 | *wa-lāta **ḥīna manāṣ*** |
| 4 | Q 9:57 | 11 | +1.75 | 99 | *malja'an aw **maghārātin** aw **muddakhalan*** |
| 5 | **Q 22:73** | 28 | +1.61 | 115 | the parable of the **fly** — *lan yakhluqū **dhubāban*** |
| 6 | **Q 18:18** | 22 | +1.17 | 206 | the sleepers — *aqāẓan wa-hum **ruqūd***, the dog *bi-l-**waṣīd*** |
| 7 | **Q 22:45** | 14 | +1.98 | 74 | *wa-**bi'rin muʿaṭṭalatin** wa-**qaṣrin mashīd*** |
| 8 | Q 11:108 | 18 | +1.36 | 163 | *ʿaṭāʾan ghayra **majdhūdh*** |
| 9 | **Q 34:16** | 16 | +2.23 | 60 | ***sayl al-ʿarim*** — *ukulin **khamṭin** wa-**athlin** wa-shayʾin min **sidr*** |
| 10 | **Q 38:31** | 6 | +3.82 | 9 | ***al-ṣāfinātu l-jiyād*** — Sulaymān's horses |
| 11 | Q 37:67 | 7 | +3.49 | 12 | *la-**shawban** min **ḥamīm*** |
| 12 | **Q 20:12** | 9 | +2.59 | 42 | *fa-khlaʿ naʿlayka … bi-l-wādi l-muqaddasi **Ṭuwā*** |
| 13 | Q 11:74 | 11 | +1.72 | 101 | *fa-lammā dhahaba ʿan Ibrāhīma l-**rawʿ*** |
| 14 | **Q 20:39** | 22 | +1.12 | 220 | Mūsā in the **tābūt** cast into the **yamm** |
| 15 | **Q 22:27** | 14 | +1.90 | 83 | *ʿalā kulli **ḍāmirin** … min kulli **fajjin ʿamīq*** |
| 16 | **Q 106:2** | 4 | **+5.05** | **3** | ***īlāfihim** riḥlata l-shitāʾi wa-l-ṣayf* |
| 17 | **Q 13:13** | 19 | +1.17 | 208 | the thunder — *shadīdu l-**miḥāl*** |
| 18 | **Q 69:7** | 15 | +1.56 | 129 | *sabʿa layālin wa-thamāniyata ayyāmin **ḥusūman** … **aʿjāzu nakhlin khāwiya*** |
| 19 | Q 20:118 | 7 | +2.57 | 44 | *allā tajūʿa fīhā wa-lā **taʿrā*** |
| 20 | Q 61:4 | 11 | +1.65 | 106 | *ka-annahum **bunyānun marṣūṣ*** |
| 21 | **Q 91:10** | 4 | +4.51 | 5 | *wa-qad khāba man **dassāhā*** |
| 22 | Q 38:22 | 23 | +1.04 | 246 | the two litigants — *wa-lā **tushṭiṭ*** |
| 23 | Q 21:18 | 13 | +1.50 | 142 | *naqdhifu bi-l-ḥaqqi ʿalā l-bāṭili **fa-yadmaghuh*** |
| 24 | **Q 16:66** | 17 | +1.11 | 222 | milk *min bayni **farthin** wa-damin … **sāʾighan** li-l-shāribīn* |
| 25 | **Q 37:103** | 4 | +4.24 | 6 | *wa-**tallahu li-l-jabīn*** — the binding of the son |
| 26 | **Q 69:32** | 7 | +2.56 | 47 | *fī **silsilatin dharʿuhā sabʿūna dhirāʿan** fa-slukūh* |
| 27 | Q 11:106 | 9 | +2.09 | 67 | *lahum fīhā **zafīrun wa-shahīq*** |
| 28 | Q 50:36 | 15 | +1.52 | 133 | *fa-**naqqabū** fī l-bilādi hal min **maḥīṣ*** |
| 29 | Q 37:11 | 12 | +1.58 | 124 | *khalaqnāhum min **ṭīnin lāzib*** |
| 30 | **Q 22:5** | 69 | +1.18 | 204 | the embryology verse — *nuṭfa, ʿalaqa, **muḍgha mukhallaqa***, *ardhali l-ʿumur* |

**This roster is a roll-call of the Qurʾān's lexical singularities, recovered by a rate over
root frequencies with no list of any kind.** *masad*, *ghawl*, *manāṣ*, *muddakhal*,
*waṣīd*, *maʿaṭṭala*/*mashīd*, *khamṭ*/*athl*/*sidr*, *ṣāfināt*/*jiyād*, *Ṭuwā*,
*ḥusūman*/*aʿjāz nakhl*, *lāzib*, *marṣūṣ*, *dassāhā*, *īlāf* — several are among the most
discussed *gharīb al-Qurʾān* items in the tradition. **None of them is verbatim quoted in the
nine canonical books.**

Three entries are worth naming separately because they are not obscure at all:
**Q 37:103**, the binding of Ibrāhīm's son; **Q 22:5**, the embryology verse; **Q 22:73**, the
parable of the fly. Each is theologically central, lexically extraordinary, and carries no
distinctive verbatim quotation in the nine books.

### 1.3 Roster 2 — heavily cited, structurally ordinary

| # | verse | w | comp | struct rank | n_ḥ | reception rank | the verse |
|--:|:--|--:|--:|--:|--:|--:|:--|
| 1 | **Q 109:1** | 3 | −0.83 | 5362 | **55** | **3** | *qul yā ayyuhā l-kāfirūn* |
| 2 | Q 6:158 | 37 | −0.59 | 5075 | 12 | 43.5 | *lā yanfaʿu nafsan īmānuhā* |
| 3 | **Q 33:21** | 17 | −0.54 | 4872 | **33** | **7** | ***uswatun ḥasana*** |
| 4 | **Q 6:82** | 11 | −0.57 | 4995 | 9 | 85.5 | *lam yalbisū īmānahum bi-ẓulm* |
| 5 | Q 9:80 | 25 | −0.51 | 4754 | 11 | 51.5 | *in tastaghfir lahum sabʿīna marra* |
| 6 | Q 18:72 | 8 | −0.58 | 5036 | 8 | 106.5 | *a-lam aqul innaka lan tastaṭīʿa maʿiya ṣabrā* |
| 7 | Q 33:70 | 8 | −0.59 | 5103 | 5 | 188 | *wa-qūlū qawlan sadīdā* |
| 8 | Q 5:105 | 19 | −0.55 | 4923 | 11 | 51.5 | *ʿalaykum anfusakum* |
| 9 | **Q 6:162** | 9 | −0.50 | 4640 | 14 | 30.5 | *inna ṣalātī wa-nusukī wa-maḥyāya wa-mamātī* |
| 10 | **Q 65:2** | 30 | −0.40 | 3907 | **36** | **5** | the *ṭalāq* witness verse |
| 11 | Q 4:136 | 28 | −0.57 | 5016 | 8 | 106.5 | *āminū bi-Llāhi wa-rasūlih* |
| 12 | Q 3:102 | 12 | −0.59 | 5106 | 7 | 128 | *ittaqū Llāha ḥaqqa tuqātih* |
| 13 | **Q 28:56** | 13 | −0.59 | 5097 | 7 | 128 | *innaka lā tahdī man aḥbabt* |
| 14 | Q 18:75 | 9 | −0.58 | 5036 | 6 | 155.5 | *a-lam aqul laka…* |
| 15 | Q 19:77 | 8 | −0.51 | 4728 | 9 | 85.5 | *la-ūtayanna mālan wa-waladā* |
| 16 | **Q 3:97** | 25 | −0.53 | 4839 | 9 | 85.5 | *wa-li-Llāhi ʿalā l-nāsi ḥijju l-bayt* |
| 17 | **Q 2:156** | 10 | −0.55 | 4896 | 7 | 128 | ***innā li-Llāhi wa-innā ilayhi rājiʿūn*** |
| 18 | Q 3:128 | 12 | −0.46 | 4370 | 14 | 30.5 | *laysa laka mina l-amri shayʾ* |
| 19 | **Q 87:1** | 4 | −0.40 | 3887 | **63** | **2** | *sabbiḥ isma rabbika l-aʿlā* |
| 20 | Q 83:6 | 5 | −0.65 | 5257 | 8 | 106.5 | *yawma yaqūmu l-nāsu li-rabbi l-ʿālamīn* |
| 21 | Q 43:14 | 4 | −0.61 | 5171 | 9 | 85.5 | *wa-innā ilā rabbinā la-munqalibūn* |
| 22 | Q 39:46 | 17 | −0.56 | 4983 | 7 | 128 | *quli llāhumma fāṭira l-samāwāti wa-l-arḍ* |
| 23 | Q 8:24 | 20 | −0.49 | 4604 | 9 | 85.5 | *yaḥūlu bayna l-marʾi wa-qalbih* |
| 24 | **Q 25:68** | 22 | −0.42 | 4108 | **32** | **8** | the *ʿibād al-Raḥmān* prohibitions |
| 25 | Q 63:8 | 17 | −0.47 | 4442 | 12 | 43.5 | *wa-li-Llāhi l-ʿizzatu wa-li-rasūlih* |
| 26 | **Q 3:64** | 31 | −0.55 | 4927 | 6 | 155.5 | *taʿālaw ilā kalimatin sawāʾin baynanā wa-baynakum* |
| 27 | Q 8:33 | 12 | **−0.82** | **5358** | 4 | 236.5 | *wa-mā kāna Llāhu li-yuʿadhdhibahum wa-anta fīhim* |
| 28 | Q 2:163 | 9 | −0.59 | 5095 | 4 | 236.5 | *wa-ilāhukum ilāhun wāḥid* |
| 29 | **Q 3:169** | 13 | −0.50 | 4697 | 7 | 128 | the martyrs — *bal aḥyāʾun ʿinda rabbihim yurzaqūn* |
| 30 | **Q 17:85** | 14 | −0.44 | 4277 | 10 | 64.5 | *yasʾalūnaka ʿani l-rūḥ* |

**Every entry is built from the corpus's commonest roots** — *Allāh*, *rabb*, *qawl*, *īmān*,
*ʿamal*, *rasūl* — which is precisely what `struct_z_composite` measures as *ordinary*. Nine
of the top twenty most-cited verses in the whole corpus appear here.

> **This is not a list of verses the tradition was wrong to dwell on, and §7.1 forbids reading
> it that way.** H-NEW-2990's own worked example settles it: **Q 1:1, the basmala, scores
> −0.531 on this composite** for the same reason — three of the most frequent roots in the
> Qurʾān. **A verse's importance is not what is being measured.** What roster 2 says is
> narrower and still worth saying: *the most-quoted verses of the ḥadīth corpus are lexically
> ordinary*, and their reception cannot be explained by the structural properties this
> instrument measures.

### 1.4 The repetition artefact that destroyed H-NEW-2620's roster cannot occur here

H-NEW-2620 §7.1 found, post-hoc, that **~73 % of its "structurally extreme but exegetically
ignored" roster was repetition** — 20 of 30 entries were later occurrences of an earlier verse
text, 11 of them the Q 55 refrain. Its roster is largely a repetition detector.

**Measured here: 0 of 30 on roster 1, 0 of 30 on roster 2, and 0 of 5,371 in the whole
analysis set.** Not one verse whose exact text occurs more than once survives into this test.

The reason is structural, not luck: H-NEW-860.1's eligibility rule already excludes any verse
with **no distinctive span** — 265 verses — and an exactly-repeated verse has none by
definition. **The reception instrument's own eligibility gate is a repetition filter, and it
was not built to be one.** The flags were pre-registered anyway (prereg §5.3), because the
2620 lesson is that finding this out post-hoc is too late.

---

## 2. The structural columns, and why these

### 2.1 What the declarations file said, and what was excluded because of it

`csv/h-new-2990-column-declarations.csv` was read before any column was chosen (prereg §0.7).
It flags **exactly two** columns `length_dominated = True`:

> **`sum_root_surprisal_bits` (ρ = +0.9411) and `n_root_types` (ρ = +0.9508) — excluded. Both
> are raw sums that scale with length by construction. Neither is used in any arm.**

Also excluded, each for a stated reason:

- **The six `IS_LENGTH` columns.** They *are* length. One is the control; none is a measure.
- **`struct_z_composite_resid`.** H-NEW-2990 §3.3 measured that the OLS-on-rank residualisation
  makes the column **worse** — ρ against `n_words` moves from −0.1824 to **+0.2382**, because a
  linear-in-rank subtraction fitted to means over-corrects a distribution with skewness +3.63.
  Its own finding says *"use `struct_z_composite`, not `struct_z_composite_resid`"*, and this
  test does. **Length is controlled here by stratification and by partial correlation, not by
  that column.**

### 2.2 What was chosen

> **`struct_z_composite`** — and, as H-NEW-2990 §8 condition 2 requires, **its four members are
> named, and every one is also tested separately** (I3–I6), so nothing is laundered by
> averaging.

| member | sign | denominator | ρ vs `n_words` |
|:--|:--:|:--|--:|
| `frac_hapax_root_tokens` | + | `n_root_tokens` | +0.0105 |
| `mean_root_surprisal_bits` | + | per-root-token mean; invariant | −0.2333 |
| `frac_root_tokens_freq_le5` | + | `n_root_tokens` | +0.0692 |
| `log10(rime_class_size)` | − | corpus constant, keyed by the verse's own fāṣila | +0.1427 |

A fifth candidate, `root_simpson_repeat`, was dropped by H-NEW-2990's own locked gate at
ρ = +0.4436 and is **not reinstated**.

**Substantively, higher = the verse is built from rarer roots, carries more corpus-singleton
roots, and ends on a rarer rhyme.** That is the whole of what "structurally unusual" means
here, and §7.1 states what it does not mean.

### 2.3 The length control, and a disagreement between the two instruments

**Locked: `n_words` as published in `h-new-2990-verse-profile.csv`** — the structural
instrument's own `PRIMARY LENGTH VARIABLE`, against which every ρ in its declarations table is
measured. Using anything else would make this test's length control incommensurable with the
instrument's published numbers.

**The two files disagree on word count for 354 of 5,371 analysis-set verses (364 of 6,236
overall), by at most 2 words, at ρ = 0.99959.** The profile counts the ʿuthmānī text; the
reception file counts the imlāʾī text, which splits units like *yā ayyuhā* differently. The
alternative was pre-registered as sensitivity **S1** rather than left undisclosed, and it moves
I1 from +0.0493 to **+0.0496**.

### 2.4 Denominators, declared

`frac_hapax_root_tokens` and `frac_root_tokens_freq_le5` divide by **`n_root_tokens`**.
`mean_root_surprisal_bits` is a per-root-token mean of −log₂ corpus root frequency.
`rime_class_size` is a count, not a rate. **`n_hadith` is never divided by anything** — it is
used raw and ranked.

---

## 3. The length control, discharged

`UNIT-DRIFT-DEFECT.md` §5's standing requirement. Measured on the analysis set:

| variable | ρ with `n_words` |
|:--|--:|
| **`n_hadith`** | **+0.1796** |
| **`struct_z_composite`** | **−0.0986** |

**The two nuisance loadings have opposite signs, so here the length control *strengthens* the
association rather than destroying it** — bare ρ = +0.0306, partial ρ = +0.0493. This is
H-NEW-860.1 §7.2's mechanism running the other way: there, two opposite loadings *manufactured*
an anti-alignment; here they *suppress* an alignment.

**Recorded because it is the opposite of what this repository's recent findings have trained a
reader to expect**, and because it means "the effect is just length" is not the explanation
available for whatever remains. The explanation that *is* available is §6.

Three independent controls were applied, and all three are reported:

1. **Partial Spearman** on mid-ranks, controlling `n_words` (I1, I3–I6).
2. **Stratified permutation** within `n_words` deciles, 10,000 draws, two seeds (I2), plus
   quintiles (S6).
3. **Surah-mean-centring** of the column itself (POST-HOC, §6.3) — the *self re-cut* of
   `UNIT-DRIFT-DEFECT.md` §6, applied to the unit that turned out to matter.

---

## 4. The locked verdict, diffed against the pre-registration

The runner printed prereg §6.1's decision logic with the observed numbers substituted, before
any declaration:

```
alpha = 0.05/6 = 0.00833333
I1: rho = +0.0493  p(+) = 0.0001  PASS <- rho>0 and p(+)<alpha : True    [struct_z_composite]
I2: rho = +0.0306  p(+) = 0.0085  PASS : False                            [stratified permutation, k=10]
I3: rho = +0.0168  p(+) = 0.1098  PASS : False                            [+frac_hapax_root_tokens]
I4: rho = +0.0328  p(+) = 0.0081  PASS : True                             [+mean_root_surprisal_bits]
I5: rho = +0.0273  p(+) = 0.0229  PASS : False                            [+frac_root_tokens_freq_le5]
I6: rho = +0.0883  p(+) = 0.0000  PASS : True                             [-log10(rime_class_size)]
passes = ['I1', 'I4', 'I6']   reverses = []
VERDICT = SUPPORTED
```

**VERDICT = SUPPORTED is what the locked rule returns, and it is declared as such.** §6 is why
no reader should believe it, and the correction is placed here rather than by touching the
pre-registration.

### 4.1 I2 — the one arm that carried an exact null, and the two bin widths

| null | ρ_obs | p(+) seed 20260509 | seed 20260519 | null mean | null sd |
|:--|--:|--:|--:|--:|--:|
| **k = 10 deciles (PRIMARY)** | +0.0306 | **0.0085** | **0.0093** | +0.0006 | 0.0127 |
| k = 5 quintiles (S6) | +0.0306 | 0.0064 | 0.0069 | −0.0017 | 0.0128 |

**The two bin widths disagree across α = 0.00833, and the finer bin is the one that fails.**
Both were pre-registered and both are reported, per `UNIT-DRIFT-DEFECT.md` §6.1 requirement 2;
k = 10 was locked primary in prereg §4 **before** any p existed, on the stated ground that the
statistic is a correlation, for which §6.1 says stratified permutation *"is decisive and
remains so"*, and that the finer bin holds length more nearly fixed. Both null means sit within
0.002 of zero, so the nulls are properly centred.

### 4.2 The sensitivities — and the one that matters most

| arm | n | bare ρ | partial ρ | p (2-sided) |
|:--|--:|--:|--:|--:|
| **primary (I1)** | 5,371 | +0.0306 | **+0.0493** | 0.0003 |
| S1 — length control = imlāʾī `n_words` | 5,371 | +0.0306 | +0.0496 | 0.0003 |
| S2 — reception = `n_hadith_all17` | 5,371 | +0.0296 | +0.0485 | 0.0004 |
| S3 — reception = `n_books` (breadth) | 5,371 | +0.0301 | +0.0488 | 0.0003 |
| S4 — first occurrences only | 5,371 | +0.0306 | +0.0493 | 0.0003 |
| **S5 — cited verses only** | **749** | **+0.0024** | **+0.0061** | **0.8667** |

> **S5 is the diagnostic that should be read first. Among the 749 verses the tradition actually
> quotes, structure has no relation whatever to how much it quotes them — ρ = +0.006,
> p = 0.87.** Whatever association exists lives entirely in the **binary** contrast between
> cited and uncited, and not at all in the graded reception.

And that binary contrast, laid out (POST-HOC D4), is a **non-monotone** gradient of four
percentage points:

| within-decile structural quintile | Q1 (most ordinary) | Q2 | Q3 | Q4 | Q5 (most unusual) |
|:--|--:|--:|--:|--:|--:|
| **cited rate** | 12.29 % | 12.00 % | **16.03 %** | 14.88 % | 14.53 % |

**The maximum is Q3, not Q5.** A monotone structural gradient is not what the data contain.

---

## 5. The concentration, reproduced

Recomputed here from the locked instrument, independently of `OPEN-H-NEW-2980`, and it agrees
exactly: **749 of 5,371 eligible verses (13.9 %) carry any citation; the top 20 carry 21.3 % of
all 3,147 citations; Q 112:1 alone carries 102 across all nine books.**

**865 verses are excluded, never zeroed** — 600 under four words, 265 with no distinctive span.

The top 20 with their structural standing added, which is a result in itself:

| verse | n_ḥ | struct rank (of 5,371) | S |
|:--|--:|--:|--:|
| Q 112:1 | 102 | 1768 | 0.496 |
| Q 87:1 | 63 | 3887 | 0.200 |
| Q 109:1 | 55 | **5362** | 0.006 |
| Q 64:1 | 54 | 2387 | 0.599 |
| Q 65:2 | 36 | 3907 | 0.177 |
| Q 3:77 | 34 | 2544 | 0.475 |
| Q 33:21 | 33 | 4872 | 0.076 |
| Q 25:68 | 32 | 4108 | 0.242 |
| Q 1:7 | 30 | 2326 | 0.597 |
| Q 2:158 | 27 | 2274 | 0.613 |
| Q 2:125 | 24 | **688** | 0.948 |
| Q 113:1 | 22 | **240** | 0.873 |
| Q 2:187 | 21 | 1879 | 0.651 |
| Q 2:196 | 21 | 782 | 0.915 |
| Q 24:37 | 21 | 1153 | 0.864 |
| Q 4:95 | 20 | 3292 | 0.301 |
| Q 48:2 | 20 | 3238 | 0.432 |
| Q 88:1 | 19 | 1073 | 0.622 |
| Q 92:5 | 18 | 1868 | 0.483 |
| Q 114:1 | 18 | 776 | 0.689 |

**The twenty most-received verses in the ḥadīth corpus span struct ranks 240 to 5,362 and
within-decile percentiles 0.006 to 0.948 — essentially the entire range.** Q 113:1 sits at rank
240 and Q 109:1 at rank 5,362, and both are muʿawwidhāt-adjacent liturgical incipits. **Whatever
selects a verse for heavy citation, it is not this structural axis, and the descriptive table
says so before any p-value does.**

---

## 6. POST-HOC — why the locked SUPPORTED verdict should not be believed

**Everything in this section is POST-HOC. It changes no locked verdict and issues none.**
Runs `…-posthoc`, `…-posthoc-2`, `…-posthoc-3`, all three retained. It is here because the
alternative — publishing SUPPORTED and letting a reader discover this — is not acceptable.

### 6.1 A parametric p on an 86 %-tied outcome is 13–57× too liberal, and it was measurable

The locked design gave **one** relationship both a parametric p and an exact permutation null:
`struct_z_composite` × `n_hadith`, as I1 and I2. **They disagreed by 57×** — 0.00015 against
0.0085. That disagreement was visible in the locked run itself and is the reason for this
section.

D6 re-runs the stratified permutation with the **partial Spearman as the test statistic**, so
the null and the statistic it judges are the same quantity. *(D1 in the first post-hoc run used
the bare Spearman, which is unfair to I4 specifically: I4's bare ρ is +0.0020 while its partial
is +0.0328, so a null built on the bare statistic cannot see where I4's association lives. That
defect was found by reading D1's own output, and D6 is the repair.)*

| arm | partial ρ | parametric p(+) | **exact p(+) — seed 1 / seed 2** | clears α? |
|:--|--:|--:|--:|:--|
| I1 `struct_z_composite` | +0.0493 | 0.00015 | **0.0081 / 0.0091** | **straddles — no** |
| I3 `frac_hapax_root_tokens` | +0.0168 | 0.1098 | 0.2935 / 0.2909 | no |
| I4 `mean_root_surprisal_bits` | +0.0328 | 0.00809 | **0.1023 / 0.1116** | **no** |
| I5 `frac_root_tokens_freq_le5` | +0.0273 | 0.0229 | 0.1304 / 0.1317 | no |
| I6 `−log10(rime_class_size)` | +0.0883 | 9.0 × 10⁻¹¹ | 0.0001 / 0.0001 | yes |

**Two of the three locked passes fail an exact test of the identical statistic.** I4 fails by a
factor of 13. I1 straddles α across two seeds and clears on neither reading a second seed
supports.

> **The generalisable rule this produces, and it is cheap: when the outcome is heavily tied —
> here 86 % at a single value — the t-approximation for a (partial) Spearman is not usable, and
> the error is one-directional and large. Compute the exact permutation p. It is the same one
> line of code the null already needs.**

This is a sibling of `UNIT-DRIFT-DEFECT.md` §6.1, which established that a *null's* free
parameter can move an answer from p = 0.002 to p = 0.713. Here it is the *p-value's
approximation*, not the null's bin width, and the direction is the same: **the cheap
approximation is the optimistic one.**

### 6.2 A within-surah permutation is not a control for surah-level confounding

D2 and D7 permuted `n_hadith` **within surah**, and under that null I1, I4, I5 and I6 all clear
α. **That result should not be used, and the reason is a defect in the diagnostic rather than a
fact about the data.**

A within-surah permutation leaves the **between-surah component of a globally-computed
statistic fixed across every draw.** For a surah-loaded column the null therefore cannot
reproduce the part of the observed value that the between-surah structure contributes, and the
observation looks extreme close to by construction. **It tests within-surah exchangeability; it
does not test whether the association is a surah-level artefact.** Reported and set aside.

### 6.3 The one surviving arm is a between-surah effect wearing a verse-level column

D3 measured how much of each column is **between-surah** variance:

| column | η² by surah |
|:--|--:|
| **`rime_class_size`** | **0.4110** |
| `n_words` | 0.3396 |
| `struct_z_composite` | 0.2597 |
| `n_hadith` | 0.1941 |
| `mean_root_surprisal_bits` | 0.1513 |
| `frac_root_tokens_freq_le5` | 0.1066 |
| `frac_hapax_root_tokens` | 0.0927 |

**I6's column is the most surah-loaded in the instrument, and I6 is the only arm that survived
an exact test.** D8 settles the tension by re-cutting the column rather than the null — each
verse carries its **deviation from its own surah's mean**:

| arm | partial ρ | exact p(+) seed 1 / seed 2 | clears α? |
|:--|--:|--:|:--|
| I6 `−log10(rime_class_size)`, as locked | +0.0883 | 0.0001 / 0.0001 | yes |
| **I6, surah-mean-centred** | **+0.0284** | **0.0193 / 0.0170** | **no** |
| I1 `struct_z_composite`, as locked | +0.0493 | 0.0081 / 0.0091 | no |
| I1, surah-mean-centred | +0.0221 | 0.1101 / 0.1122 | no |

> **Centring retains 53.1 % of `rime_class_size`'s variance and 74.0 % of the composite's, so
> this is not a power collapse from destroying the column. The association simply is not there
> once the surah is taken out of it.**

**This is `OPEN-H-NEW-2980`'s ill-posedness returning in a subtler form.** That file ruled the
rosters unbuildable because the only structural instruments were **per-surah** and assigning a
verse its surah's score would measure surah membership under a verse-level label. H-NEW-2990
removed that defect: every column is computed from the verse's own text. **And the defect came
back anyway** — not through an inherited score, but through a genuinely verse-level column whose
*variance* is 41 % between surahs. `rime_class_size` is keyed to the verse's own fāṣila, and
verses in one surah mostly rhyme alike.

> **The generalisation, which is the most transferable thing in this finding:**
> **verse-locality of a column's *definition* does not make its *variance* verse-level.** A
> column can satisfy every locality rule at construction and still carry most of its
> information at a coarser unit. **The check is one number — η² by the coarser unit — and it
> belongs beside ρ-against-length in any future instrument's declarations.**

### 6.4 What is left

Nothing. **No arm survives an exact test at the pre-registered α once the unit its variance
lives at is accounted for.** The largest effect in the whole test explains **0.78 %** of the
variance and is the one that turns out to be a surah property; the rest explain 0.03 %–0.24 %;
and among the 749 verses actually cited there is no relationship at all (ρ = +0.006, p = 0.87).

**Read as the pre-registration expected it to be read, the inferential result is NULL**, and it
joins H-NEW-2620 (tafsīr, NULL on all six) and H-NEW-860.1 (surah level, no relationship in
either direction under a size control). **Three instruments, three units, one answer.**

---

## 7. Honest limits

1. **`struct_z_composite` cannot certify that a verse is interesting**, and roster 2 must not
   be read as a list of verses the tradition over-values. H-NEW-2990 §7.1 and its worked
   example — **Q 1:1 scores −0.531** — settle this. Declared in prereg §8.1 before any result.
2. **Power is low by construction and a NULL here is weak evidence of absence.** 86 % of the
   analysis set is tied at zero. Per `findings/ABSENCE-CLAIMS.md`, the correct reading is *no
   relationship was detected*, not *no relationship exists*.
3. **The locked verdict is SUPPORTED and this document does not retract it** — it cannot, the
   rule was fixed in advance and the numbers are what they are. §6 is the correction, placed in
   the finding because `UNIT-DRIFT-DEFECT.md` §9 forbids editing a pre-registration after its
   run. **A reader citing this work should cite §0 and §6, not the frontmatter's
   `verdict_locked`.**
4. **The exact-null repair is post-hoc.** The pre-registration gave a permutation null to I2
   only; I1 and I3–I6 were registered as parametric. **A future pre-registration in this family
   should register an exact null for every arm whose outcome is heavily tied**, and this one
   should have.
5. **Reception is verbatim quotation and explicit naming, and nothing else** — no allusion, no
   paraphrase, no thematic commentary, no *asbāb al-nuzūl*. H-NEW-860.1 §9.3 measures the gap
   at an order of magnitude for Q 19. **Roster 1 says these verses are not verbatim quoted in
   the nine books. It does not say the tradition ignored them**, and the *gharīb al-Qurʾān* and
   tafsīr literatures are exactly where it did not.
6. **`n_hadith` inherits H-NEW-860.1's N = 5 span choice**, disclosed there as a real degree of
   freedom that separates its UNDETERMINED from a REVERSES. Not re-derived here.
7. **Chain grade is not modelled**; **Musnad Aḥmad is incomplete upstream** (chapters 8–30
   absent from the source scrape).
8. **The mismatch score *M* is one defensible construction among several.** The zero-collapse
   in *R* (§1.1) is a real choice, locked in advance with its reason; a different treatment of
   the tied-zero block would produce a different roster 2. Roster 1 is insensitive to it — with
   *R* = 0 for every uncited verse, roster 1 is simply the top 30 by within-decile structural
   percentile among uncited verses.
9. **The two rosters share one ordering.** They are its two tails, not two independent
   measurements.

---

## 8. Run record

- Pre-registration SHA-256 `6515fe1a12ebf742e3ab72d5c6e18e8c5a82d1c0a4f4fd894aa9397eed344789`,
  embedded as a literal in the script and verified at runtime, together with five frozen
  inputs. **A mismatch aborts before any run directory is created.** `scripts/verify-prereg-locks.sh`
  covers this lock; it reported **12/12 clean** with this one added.
- **The pre-registration has not been edited since the run and will not be.** Every correction
  in §6 is recorded here.
- **The rosters were written to disk and published before any inference was computed**
  (prereg §7 step 5). The runner prints `[PERSIST] both rosters on disk. Nothing inferential
  has been computed.` Six lanes were lost to connection failures on 2026-08-08, one after being
  told to persist first; **the order of work inside a fragile lane is part of the registration.**
- Immutable run directory `runs/h-new-3000/20260808T235345Z/`, `exist_ok=False`, every file
  opened mode `'x'`. `result.json` and `manifest.json` written **once**, at completion. **No
  file inside any run directory was overwritten and no run directory was deleted.**
- Three post-hoc runs, all retained: `…235632Z-posthoc`, `…235824Z-posthoc-2`,
  `…235958Z-posthoc-3`. Manifest paths are repo-relative.
- **Numerical self-tests before the run:** the partial-Spearman identity checked against a
  direct OLS-residual computation on the ranks over 20 random datasets (max |diff| =
  1.9 × 10⁻¹⁶, aborting above 1 × 10⁻⁹); mid-rank percentile behaviour against hand-computed
  values; Spearman endpoints. **The permutation optimisation — permuting ranks rather than
  re-ranking, an identity under within-block permutation — is verified against the literal slow
  route on the first 25 draws of every call**, aborting on any disagreement beyond 1 × 10⁻⁹.
- Seeds 20260509 primary, 20260519 replication. 10,000 permutations per null. **Every
  permutation result is reported at both seeds.**
- The verdict logic was printed with the observed numbers substituted and diffed against
  prereg §6.1 before declaration (§4).

---

## 9. Cross-references

- **[[OPEN-H-NEW-2980-reception-residual]]** — the open question this closes. Its concentration
  census is reproduced exactly here (13.9 %, 21.3 %, Q 112:1 = 102); its ill-posedness ruling is
  vindicated in an unexpected way by §6.3.
- **[[h-new-2990-verse-profile]]** — the instrument. Its §8 conditions are met: rank statistics
  only, the column and its four members named, stratified on `n_words`. **Its §7.1 limit is the
  binding one for roster 2.** §6.3 proposes one addition to its declarations: **η² by surah**
  beside ρ against length.
- **[[h-new-860-1-fadail-formal-count]]** — the reception instrument. Its eligibility rule turns
  out to be a repetition filter (§1.4). Its §7.2 mechanism runs in reverse here (§3).
- **[[h-new-2620-tafsir-contested]]** — the tafsīr analogue, NULL on all six. Its §7.1
  repetition artefact **cannot occur here** (§1.4), and its lesson was pre-registered rather
  than discovered post-hoc.
- **`findings/UNIT-DRIFT-DEFECT.md`** — §5 discharged in §3; §6.1's shape recurs in §6.1 with
  the p-value approximation in place of the bin width; §7 write-once and §9 never-edit both
  observed.
- **`findings/ABSENCE-CLAIMS.md`** — §7.2: this is a low-power NULL and is labelled one.

---

*Run 2026-08-09 by Waiel Al-Shujaa against a pre-registration locked before any association
between structure and reception existed. The rosters were on disk before the first p-value.
The verdict rule returned SUPPORTED and an exact test does not support it — and a column can be
verse-local by definition while its variance lives in the surah.*

*Bismillāhi al-Raḥmāni al-Raḥīm.*
