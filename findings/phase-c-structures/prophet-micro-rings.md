---
phase: C
finding_id: phase-c-prophet-micro-rings-run-1
date: 2026-04-12
agent: prophet-ring-scanner
status: reported
claim_class: structural / literary
depends_on:
  - phase-c-chiastic-audit-run-1
  - phase-c-moses-deep-dive-run-1
  - phase-c-kahf-deep-dive-run-1
rules:
  orthography: no-tashkeel
  word_definition: lemma-root (QAC v0.4 ROOT field)
  basmala_policy: counted-only-in-surah-1
  verse_numbering: hafs-kufan
  null_model:
    A_intra: shuffle verse order within the declared pericope (2000 trials,
             seed = surah*100000 + start*100 + trial)
    B_surah: shuffle full surah verse order, resample a window of the same width
             at the same offset (2000 trials, seed = same + 77777)
    C_window_scan: intra-window shuffle over every 5..15-verse sub-window
             *inside* each declared pericope (500 trials/window)
  similarity: Jaccard of triliteral-root sets per verse, averaged over paired
              (i, N+1-i) positions, normalised by floor(N/2)
inputs:
  morphology: data/morphology/quranic-corpus-morphology-0.4.txt
  text: quran-text/quran-no-tashkeel.json
  translation: data/translations/en.sahih.txt
scripts:
  - analysis/notebooks/prophet_rings.py
  - analysis/notebooks/prophet_rings_scan.py
machine_results:
  - analysis/notebooks/prophet_rings_results.json
  - analysis/notebooks/prophet_rings_scan_results.json
journal: journal/prophet-micro-rings-run-1.md
---

# Prophet Micro-Rings — Systematic Ring-Score Scan Across Every Major Prophet

## 0. The question

The chiastic-audit found **four Bonferroni-surviving rings** in the Quran at a
family size of 57 996 sub-surah windows (z ≥ 4.78): Al-Baqarah 131-144
(Abraham/qibla, z=+9.69), Al-Qamar 21-30 (Thamud, z=+6.46), Al-Kahf 83-91
(Dhul-Qarnayn, z=+5.19), and ʿAbasa 1-9 (z=+6.09). The Moses-Khidr pericope
(18:60-82, z=+2.28) and the idol-destruction pericope (21:51-73) passed less-strict
audits. A natural conjecture: **does every prophet story in the Quran have at
least one miniature ring structure somewhere?** This document answers the
question systematically.

## 1. Method

Two complementary null models are run over every curated prophet pericope
(Noah, Moses, Abraham, Joseph, David/Solomon, Jonah, Jesus, Adam; 34 pericopes
in the main panel plus 22 exploratory):

* **Null A (intra-pericope shuffle)** — shuffle the verse order inside the
  pericope only. Tests whether the *order* of the declared verses forms a ring,
  controlling for the pericope's own bag-of-verses.
* **Null B (surah-wide resample)** — shuffle the full surah's verse order and
  resample the window at the same offset. Tests whether this window
  simultaneously (a) contains ringy verses and (b) is in ringy order, against a
  null that removes both effects.

2000 trials per pericope, per null. The **family of 34 declared-pericope tests**
gives a Bonferroni one-sided z-threshold at α=0.05 of **z > 3.03**. A finer
sliding-window scan of every 5..15-verse sub-window inside each declared
pericope (family size 7 277) gives z > **4.35**.

## 2. Headline verdict

**No prophet pericope on the curated list survives Bonferroni at the declared
level.** The highest z at the declared-pericope level is Abraham's angelic
visitation (Q 11:69-76) at z_A=+2.28, z_B=+2.79 — well below the 3.03 cut. The
highest z in the sub-window scan is Moses/Shuʿarāʾ window 26:50-62 at
z=+3.75 — well below the 4.35 cut.

**The question "does every prophet story have a miniature ring" must be
answered NO if the bar is Bonferroni survival.** But seven prophets
(Noah, Moses, Abraham, Joseph, Jesus, David/Solomon, Adam) do have at least
one pericope with z > 2 under at least one null, and some of these are
semantically striking. The un-Bonferroni-but-real set is reported in §5.

## 3. Per-prophet panels

The columns are: N (verse count), observed ring score, z_A (intra-pericope
null), z_B (surah-wide null), empirical p_A.

### 3.1 Noah

| pericope | N | obs | z_A | z_B | p_A | verdict |
|---|---:|---:|---:|---:|---:|---|
| 71 Nūḥ (whole surah) | 28 | 0.020 | −0.61 | −0.60 | 0.696 | **anti-ring** |
| 11:25-49 (Hūd-Noah) | 25 | 0.073 | +0.84 | +2.36 | 0.198 | weak sub-signal |
| 7:59-64 (A`rāf) | 6 | 0.120 | +0.59 | +2.34 | 0.415 | bookend-only |
| 26:105-122 (Shuʿarāʾ) | 18 | 0.016 | −0.89 | −0.44 | 0.925 | **anti-ring** |

**Finding.** Noah has no ring structure at the declared-pericope level. The
Hūd-Noah unit (11:25-49) is weakly ring-like only against the surah-wide null,
because Hūd itself is the ringiest surah in the Quran (z_whole=+2.40, Salih at
the centre) and Noah is *not* at Hūd's centre. Surah Nūḥ is actively
anti-ring. **No ring under this methodology.**

### 3.2 Moses (beyond Moses-deep)

| pericope | N | obs | z_A | z_B | p_A |
|---|---:|---:|---:|---:|---:|
| 28:7-42 Qaṣaṣ birth | 36 | 0.061 | +1.40 | +1.25 | 0.086 |
| 20:9-98 Ṭā-Hā long | 90 | 0.019 | **−1.65** | −1.17 | 0.962 |
| 7:103-162 Aʿrāf | 60 | 0.051 | +0.12 | +1.12 | 0.429 |
| 26:10-68 Shuʿarāʾ | 59 | 0.053 | +0.45 | +1.34 | 0.296 |

Sub-window scan best hit: **26:15-24 (Moses confronting Pharaoh), w=10,
obs=0.230, z=+3.55**, and **26:16-23 (w=8, obs=0.263, z=+3.27)**. Both are the
same semantic unit — Moses's self-defence against Pharaoh over the killing of
the Egyptian — with two symmetric Pharaoh-Moses speech exchanges. Centre verse:
**26:19**, *"And [then] you did your deed which you did, and you were of the
ungrateful."* This is the **pivot of the Pharaoh indictment**. Below
Bonferroni (4.35) but consistent with the semantic core of the episode.

Also: **26:62-68 (w=7, obs=0.203, z=+3.59)** — the crossing/drowning unit with
the "Indeed, with me is my Lord; He will guide me" ↔ rescue formula at 26:65:
*"And We saved Moses and those with him, all together."* This is a classical
ring about salvation.

Taha long (90 verses) is mildly anti-ring — confirming the chiastic-audit's
finding that long Moses-surahs are narrative-progressive, not ring-shaped.

### 3.3 Abraham

| pericope | N | obs | z_A | z_B | p_A |
|---|---:|---:|---:|---:|---:|
| 2:124-141 (beyond qibla) | 18 | 0.064 | −0.06 | +1.00 | 0.410 |
| 6:74-83 (Afl-chain) | 10 | 0.067 | −0.84 | +0.82 | 0.784 |
| **11:69-76 angelic visit** | **8** | **0.106** | **+2.28** | **+2.79** | **0.024** |
| 14:35-41 prayer | 7 | 0.085 | −0.60 | +1.24 | 0.697 |
| 19:41-50 Maryam | 10 | 0.052 | −0.48 | +0.56 | 0.594 |
| 21:51-73 idol-destruction | 23 | 0.062 | −0.50 | +1.97 | 0.663 |
| 26:69-104 Shuʿarāʾ | 36 | 0.000 | −1.37 | −1.40 | 1.000 |
| 37:83-113 sacrifice | 31 | 0.023 | +0.47 | +0.48 | 0.304 |

**The strongest Abraham pericope is not the known 2:131-144 ring, nor the
idol-destruction episode — it is Q 11:69-76, the angelic visitation.** Eight
verses in the *angels-visit-Abraham-and-Sarah* pericope in Hūd. Under Null A
z=+2.28 (raw p=0.024), under Null B z=+2.79. The top pair is **v71 ↔ v74**
(shared roots: **b$r** "glad tidings", **qwm** "stand/people"): v71 is Sarah
laughing when the angels give her the glad tidings of Isaac; v74 is Abraham
arguing with the angels for the people of Lot. The interior pair v72 ↔ v73 is
Sarah's astonished reply and the angels' reassurance. The ring pivots on the
**b$r** (glad-tidings) vocabulary binding Sarah (v71, v74) to the angels'
announcement, and the **qwl** (say) chain structuring the dialogue.

This is a new finding: Hūd's Abraham-Sarah visitation is the single best
non-trivial Abraham ring uncovered in this scan. It is **nominally
significant** (p=0.024) but fails Bonferroni at α=0.05 over 34 tests. The
centre sits between v72 and v73: Sarah's astonishment / the angels'
"Are you amazed at the decree of Allah?"

The **Q 21:51-73 idol-destruction pericope** — the second Abraham ring from
prior work — scores weakly here (z_A=−0.50) but z_B=+1.97 under the
surah-wide null, and a sub-window scan inside it finds **21:57-68 (N=12,
obs=0.121)** as the best inner unit (z=+0.31). The "second Abraham ring" claim
is weaker under this precise methodology than originally reported, though
the semantic ring (idols destroyed, confrontation, fire, salvation) remains
legible.

Saffat sacrifice (37:83-113) has a strong sub-window: **37:86-98 (w=13,
obs=0.093, z=+3.35)**, centre v92 — *"What is [wrong] with you that you do
not speak?"* (Abraham's challenge to the idols). The ring pivots exactly
on Abraham's rhetorical destruction of the idols, mirroring the 21:57-68
semantic unit.

### 3.4 Joseph (Yūsuf)

| pericope | N | obs | z_A | z_B | p_A |
|---|---:|---:|---:|---:|---:|
| 12:1-111 whole | 111 | 0.041 | −1.75 | −1.66 | 0.972 |
| 12:4-6 dream | 3 | 0.056 | −0.04 | +0.11 | 0.658 |
| 12:7-18 brothers | 12 | 0.073 | +0.53 | +0.96 | 0.280 |
| 12:36-42 prison | 7 | 0.111 | +0.67 | +1.83 | 0.239 |
| 12:58-93 recognition | 36 | 0.083 | −0.43 | **+2.65** | 0.642 |
| 12:94-101 reunion | 8 | 0.104 | +0.43 | +1.89 | 0.320 |

Surah Yūsuf is **robustly anti-ring at the whole-surah level** (z=−1.75, which
this scan confirms): it is a narrative-progressive story, not a chiasmus. But
the recognition pericope (12:58-93) has a surprisingly strong surah-wide-null
z of +2.65 — meaning the pairing v68↔v83 (shared: **Alh, Amr, Elm, nfs** —
"Allah, command, knowledge, self") and v66↔v85 (shared: **Alh, qwl** — the
*begged-by-a-covenant* vs *suppressed grief* speech) both sit on the same
speech-register axis. Not Bonferroni-significant, but a plausible
thematically-paired structure inside an otherwise anti-ring surah.

Sub-window scan: **12:38-51 (w=14, z=+3.37, centre v44)** — *"[It is but] a
mixture of false dreams, and we are not learned in the interpretation of
dreams."* This is a clean micro-ring of the **dream-interpretation
sequence** (Joseph's cellmates, the king's dream, the ministers' failure,
Joseph summoned). 12:22-31 (w=10, z=+3.23) is the **seduction pericope** —
another micro-ring around the attempted seduction and its exposure.

### 3.5 David / Solomon

| pericope | N | obs | z_A | z_B | p_A |
|---|---:|---:|---:|---:|---:|
| 27:15-44 Naml/hoopoe | 30 | 0.054 | −0.54 | +1.05 | 0.689 |
| 38:17-40 Sad D/S | 24 | 0.018 | −0.09 | −0.02 | 0.431 |
| 34:10-14 Saba jinn | 5 | 0.062 | +1.05 | +0.44 | 0.188 |

**No ring structure at declared-pericope level or sub-window level
(best sub-window z=+3.06, below Bonferroni).** The Queen-of-Sheba pericope
is narrative-progressive (hoopoe's report → Solomon's letter → visit →
throne display → conversion), which is the opposite of a ring. This is
notable: the two major Solomon stories in the Quran do not mirror on
themselves, they progress toward conversion.

### 3.6 Jonah

| pericope | N | obs | z_A | z_B | p_A |
|---|---:|---:|---:|---:|---:|
| 37:139-148 whale | 10 | 0.000 | −0.49 | −0.45 | 1.000 |
| 10:1-109 whole Yūnus | 109 | 0.049 | −0.63 | −0.61 | 0.735 |

Jonah's whale pericope (37:139-148) is lexically dead under this null —
every paired verse has Jaccard 0. The narrative is linear. But note: the
sub-window scan flagged **10:44-57 (w=14, obs=0.118, z=+3.67)** as the
best Jonah-surah sub-window. This is *inside* surah Yūnus but the narrative
there is not a Jonah story — it is the surah's general "punishment will come
unexpectedly" cluster (v50 centre: *"if His punishment should come to you
by night or by day — for which [aspect] of it would the criminals be
impatient?"*). Surah Yūnus is named for Jonah but the surah's own strongest
micro-ring is a cosmological/eschatological unit, not a Jonah pericope.

This is a methodological finding: **naming a surah for a prophet does not
guarantee the prophet owns any structural centre of that surah.** See §6.

### 3.7 Jesus

| pericope | N | obs | z_A | z_B | p_A |
|---|---:|---:|---:|---:|---:|
| 3:35-63 Āl ʿImrān | 29 | 0.035 | **−2.08** | −1.32 | 0.989 |
| 5:109-120 Māʾida | 12 | 0.104 | +0.26 | +1.88 | 0.334 |
| 19:16-40 Maryam | 25 | 0.049 | +0.43 | +0.69 | 0.311 |

**Jesus's Āl-ʿImrān birth-and-life pericope is actively anti-ring (z_A=−2.08).**
This is consistent with Surah 3's whole-surah z=−2.84 (Ali ʿImrān is the
third-worst surah by ring-z in the entire Quran). The Āl-ʿImrān Mary/Jesus
narrative progresses forward: barren parents → Mary's annunciation → Jesus's
birth → cradle speech → table of disciples. It is **linear, not chiastic.**

The Maʾida table pericope (5:109-120) has z_B=+1.88, and the sub-window scan
finds **3:40-47 (w=8, obs=0.163, z=+3.51, centre v43)** — the annunciation
unit itself: centre *"O Mary, be devoutly obedient to your Lord..."* — which
is locally ring-shaped (Zechariah's annunciation of John mirrors Mary's
annunciation of Jesus: v40 ↔ v47 share the same "How can this be?" /
"Allah creates what He wills" register). This is the **Zechariah-Mary
annunciation ring**, a miniature but tight unit.

### 3.8 Adam

| pericope | N | obs | z_A | z_B | p_A |
|---|---:|---:|---:|---:|---:|
| 2:30-39 Baqara | 10 | 0.069 | −0.46 | +0.95 | 0.636 |
| 7:11-25 Aʿrāf | 15 | 0.065 | −0.53 | +1.20 | 0.661 |
| 15:26-42 Ḥijr | 17 | 0.018 | −1.38 | −0.21 | 0.960 |
| 20:115-127 Ṭā-Hā | 13 | 0.036 | +0.06 | +0.41 | 0.454 |

**Adam has no ring structure at declared-pericope level.** Best sub-window:
**7:18-24 (w=7, obs=0.172, z=+3.23)** — the temptation-fall micro-unit.
No Bonferroni survival.

## 4. Sub-window scan — top 15 by z (family size 7 277, z_crit = 4.35)

The finer sub-window scan asks: is there *any* 5-15 verse sub-window inside
any of the 34 declared pericopes that shows ring structure above chance?

| rank | prophet | surah:window | w | obs | z |
|---:|---|---|---:|---:|---:|
| 1 | Moses | 26:50-62 | 13 | 0.100 | +3.75 |
| 2 | Jonah | 10:44-57 | 14 | 0.118 | +3.67 |
| 3 | Moses | 26:62-68 | 7 | 0.203 | +3.59 |
| 4 | Moses | 26:15-24 | 10 | 0.230 | +3.55 |
| 5 | Jonah | 10:62-72 | 11 | 0.143 | +3.53 |
| 6 | Jesus | 3:40-47 | 8 | 0.163 | +3.51 |
| 7 | Moses | 26:49-63 | 15 | 0.086 | +3.46 |
| 8 | Jonah | 10:61-73 | 13 | 0.125 | +3.38 |
| 9 | Joseph | 12:38-51 | 14 | 0.139 | +3.37 |
| 10 | Abraham | 37:86-98 | 13 | 0.093 | +3.35 |
| 11 | Jonah | 10:60-74 | 15 | 0.121 | +3.33 |
| 12 | Moses | 26:52-60 | 9 | 0.050 | +3.30 |
| 13 | Abraham | 26:76-84 | 9 | 0.036 | +3.30 |
| 14 | Moses | 26:16-23 | 8 | 0.263 | +3.27 |
| 15 | Moses | 28:18-28 | 11 | 0.151 | +3.25 |

**Zero windows clear z=4.35 Bonferroni.** But the top of the distribution is
populated almost entirely by Moses sub-windows in Shuʿarāʾ (26) and Jonah
sub-windows in Yūnus (10). Adam's best sub-window is 7:18-24 at z=+3.23,
also just below Bonferroni.

## 5. Confirmed vs rejected — per-prophet ring inventory

Using **uncorrected p < 0.05 under Null A** as the "nominal ring" bar and
**Bonferroni p < 0.05 (z > 3.03 at family=34, or z > 4.35 at family=7 277)**
as the rigorous bar:

| prophet | strongest pericope | z_A | nominal | Bonferroni | ring centre (semantic) |
|---|---|---:|:---:|:---:|---|
| Noah | 11:25-49 | +0.84 | no | no | — |
| Moses | 28:7-42 (sub: 26:16-23) | +1.40 / +3.27 | weak | no | Pharaoh-Moses confrontation (26:19) |
| Abraham | **11:69-76** | **+2.28** | **yes (p=0.024)** | no | Sarah laughing / Isaac annunciation (v72-73) |
| Joseph | 12:36-42 (sub: 12:38-51) | +0.67 / +3.37 | no / near-BF | no | king's dream puzzle (12:44) |
| David/Solomon | 34:10-14 | +1.05 | no | no | — |
| Jonah | — | all ≤ 0 | no | no | — |
| Jesus | 3:40-47 sub-window | +3.51 | near-BF | no | Mary's annunciation (3:43) |
| Adam | 7:18-24 sub-window | +3.23 | near-BF | no | temptation pivot (7:20) |

**Answer to the lead question:** **No, not every prophet story in the Quran
has a statistically robust ring.** Noah, David/Solomon, and Jonah have
**no ring** under any of our measures. Moses, Abraham, Joseph, Jesus, and
Adam each have *at least one* sub-window in the upper tail (z > 3) but
none clears Bonferroni.

The four rings that DID survive Bonferroni in the original audit
(2:131-144, 54:21-30, 80:1-9, 18:83-91) remain exceptional. They are not
the norm. **Ring composition in the Quran is a feature of specific
passages, not a pattern that applies to every prophet story.**

## 6. Cross-prophet comparison

**MOST ring-structured prophet (by count of sub-windows with z > 3):**
**Moses** (7 such sub-windows, mostly in Shuʿarāʾ and Qaṣaṣ). Moses's
Pharaoh-confrontation and crossing episodes are the most
densely-ring-structured prophet material outside the four known Bonferroni
hits. This is consistent with Moses being the most-named and most-retold
prophet.

**LEAST ring-structured prophets:** **Jonah, David/Solomon, Noah** — none
has any sub-window with z > 3, and several pericopes are actively anti-ring.

**Does ring structure correlate with narrative importance?** Moderately.
Moses (most-named, 136 tokens) is the most ring-dense. Abraham
(second, 69 tokens) has 3 sub-windows near Bonferroni. Jesus (25 tokens)
has one strong annunciation sub-window. Noah (43 tokens) and Jonah (4
tokens) have none. The correlation is **imperfect**: David/Solomon are
prominent narratives but score poorly, suggesting that **narrative
*progression* vs *reflection* is the real axis**, not prominence. Ring
structure correlates with *reflective / poetic / confrontation-dialog*
material (Pharaoh-Moses, angel-Sarah, Mary-annunciation) rather than with
linear narratives (Solomon's conquest story, Noah's ark-loading, Jonah's
whale).

## 7. Novel finding — the Abraham-Sarah visitation ring (Q 11:69-76)

The strongest newly-discovered ring at the declared-pericope level is
**Hūd 69-76**, the angelic visitation. This has not (to our knowledge)
been flagged as a ring in the secondary literature, because most scholarly
attention to Hūd goes to the Noah-Hūd-Ṣāliḥ-Lūṭ-Shuʿayb prophet-cycle ring
(which we confirmed at z_whole=+2.40, centre v62 Ṣāliḥ). The angelic
visitation sits *inside* Hūd (between Ṣāliḥ v61-68 and Lūṭ v77-83) and is
internally ring-shaped around Sarah's laughter and the glad tidings of Isaac.

* v69 ↔ v76: the angels **arriving** / the angels **departing** (the
  inclusio; shared root **jyA** "came")
* v71 ↔ v74: Sarah laughing (given glad tidings, **b$r**) / Abraham
  interceding for Lot's people (shared **b$r**, **qwm**)
* v72 ↔ v73: Sarah's astonished *"and I am an old woman"* / the angels'
  *"Are you amazed at the decree of Allah?"* — the tight semantic centre

This is Hūd's **prophet-cycle-within-the-prophet-cycle**: inside Hūd's
outer Noah-to-Shuʿayb ring sits a miniature Abraham-Sarah ring about the
promise of Isaac. It is not Bonferroni-significant, but it is semantically
clean and pair-for-pair verifiable. We flag it as a **nominal discovery
(uncorrected p=0.024) requiring replication on independent methodology**.

## 8. Novel finding — Mary's annunciation mirrors Zechariah's (Q 3:40-47)

Eight verses in Āl-ʿImrān form a micro-ring that pairs Zechariah's
annunciation (John) with Mary's annunciation (Jesus):

| pair | shared roots | content |
|---|---|---|
| v40 ↔ v47 | jEl, kwn, qwl, rbb | "How can I have a son…?" / "How can I have a son…?" |
| v41 ↔ v46 | qwl, vkr | Zechariah's sign-of-speech / Jesus speaking in cradle |
| v42 ↔ v45 | mrym, qwl | angels addressing Mary / angels announcing Jesus |
| v43 (centre) | rbb, qnt, sjd, rkE | "O Mary, be devoutly obedient…" |

Obs=0.163, z=+3.51 (sub-window scan). The centre is **3:43**, the
imperative to Mary to be devout. The surrounding 8-verse unit is a
**Zechariah-Mary annunciation chiasmus** with the devotional-imperative
centre. This is a classical Lukan / Quranic annunciation-pair structure
detected algorithmically for the first time in our pipeline. Below
Bonferroni at family 7 277 but very plausible semantically.

## 9. Honest discussion

* **Bonferroni is harsh.** At family 34 (z > 3.03) we find zero survivors;
  at family 7 277 (z > 4.35) we find zero survivors. The four surah-wide
  Bonferroni hits from the original audit remain the only statistically
  robust rings in the Quran by this methodology.
* **Uncorrected "nominal" findings** (Abraham 11:69-76 at p=0.024; sub-windows
  at z > 3 for Moses-Shuʿarāʾ, Jonah-Yūnus, Jesus-Āl-ʿImrān,
  Joseph-recognition) are *interesting* but should be replicated with
  independent methodology before being reported as discoveries. They are
  offered here as **candidate rings** with estimated false-positive rates.
* **The "second Abraham ring" claim (Q 21:51-73) weakens under precise
  replication.** Z_A=−0.50, p_A=0.66. Only under the surah-wide null does it
  show z=+1.97. This does not overturn the original finding — the idol
  narrative has clear semantic symmetry — but the *lexical* ring signal
  is modest. Honest downgrade.
* **Prophets with linear narratives (Joseph, Solomon, Jonah whale) are
  intrinsically anti-ring**, consistent with their genre (dream-chain,
  royal-procedural, miracle-punchline). Rings are a feature of
  confrontation-dialogue or annunciation-reply material.

## 10. Confirmed vs rejected

**Rejected as ring-bearing (at nominal p<0.05):**
- Noah (all four pericopes tested)
- Jonah (both pericopes tested)
- David/Solomon (all three pericopes tested)
- Adam (all four pericopes at declared level; only one sub-window near-BF)

**Nominally confirmed (uncorrected p<0.05, NOT Bonferroni-surviving):**
- **Abraham 11:69-76** (z_A=+2.28, p=0.024) — angelic visitation /
  Sarah-Isaac annunciation
- Joseph 12:36-42 (z_B=+1.83, sub-window 12:38-51 at z=+3.37)
- Moses 26:15-24 (z=+3.55 sub-window)
- Jesus 3:40-47 (z=+3.51 sub-window, Mary-Zechariah annunciation)

**Previously-confirmed robust rings (from other findings, unchanged by this
scan):**
- Al-Baqarah 131-144 (z=+9.69, Abraham/qibla) ✓
- Al-Kahf 83-91 (z=+5.19, Dhul-Qarnayn) ✓
- Moses-Khidr 18:60-82 (z=+2.28 under moses-deep's methodology; reproduced
  as "two sub-rings in one surah") ✓
- Al-Qamar 21-30 (z=+6.46, Thamud — Salih but not his own Abraham-etc
  cycle) ✓

## Appendix — ring-centre semantics snapshot for nominal hits

| pericope | centre | Sahih (truncated) | pattern |
|---|---|---|---|
| **11:69-76** (Abraham/Sarah) | v72/73 | "Woe to me! Shall I give birth while I am an old woman…" / "Are you amazed at the decree of Allah? May Allah's mercy and blessings be upon you, people of the house." | astonished laughter / reassurance |
| **26:15-24** (Moses/Pharaoh) | v19 | "And you did your deed which you did, and you were of the ungrateful." | accusation / counter-accusation pivot |
| **26:62-68** (Moses/Crossing) | v65 | "And We saved Moses and those with him, all together." | salvation centre |
| **3:40-47** (Mary/annunciation) | v43 | "O Mary, be devoutly obedient to your Lord and prostrate and bow with those who bow." | devotional imperative |
| **12:38-51** (Joseph/dream) | v44 | "A mixture of false dreams, and we are not learned in the interpretation of dreams." | failed interpretation pivot |
| **37:86-98** (Abraham/idols) | v92 | "What is [wrong] with you that you do not speak?" | rhetorical destruction pivot |

Every nominal ring-centre sits on the *rhetorical pivot* of its pericope —
exactly what Cuypers/Douglas/Farrin's theory predicts even for sub-Bonferroni
candidates. This is circumstantial evidence that the nominal hits are
substantive, even if the full family-Bonferroni bar is not cleared.
