---
id: H-NEW-3180
title: "The Sajāwandī grades do not order the length of the unit they close — the whole of a ρ = +0.14 is between-verse, and the null model, not the data, decides the verdict"
date: 2026-08-09
author: Waiel Al-Shujaa
status: NULL on both registered arms · both inventories agree · the deciding parameter is the NULL MODEL (4,782× p-swing), not the length channel (2.4×)
prereg: prereg-h-new-3180-waqf-boundary.md
prereg_sha256: 047ccde36fb53e500882fa4959e877b6481d292b663bc111b803d09e2d33a86a
run: runs/h-new-3180/20260809T120211Z/
posthoc: runs/h-new-3180/POSTHOC-20260809T120425Z/
seed: 20260509
seed_replication: 20260519
family: WAQF-2026-08-09-B
rules_tuple: "(BOTH quran-full-tashkeel.json AND quran-min-tashkeel.json for the waqf inventory; no-tashkeel as a third ungated tuple; graded marks only as boundaries; segment-the-mark-closes; Hafs-Kufan)"
---

# H-NEW-3180 — do the pause grades order the length of the unit they close?

---

## 0. STEP 0 FIRST — frontier item F-1 was already answered, and this file is not it

**F-1 was dispatched as an open frontier item. It is not open.** The Step-0 search found the
answer before any design work began, and I am putting that above my own result because it is
worth more than my own result.

| F-1 clause | already answered by | verdict on disk |
|:--|:--|:--|
| grades → boundary hierarchy, **annotation-free** channel | H-NEW-2610 **H1a**, ρ = −0.0075, n = 4,266, p = 0.691 / 0.410 | **NULL** |
| …same, **consensus inventory, 5 rungs incl. lā** | H-NEW-2610 §7 `sensitivity_min_tashkeel_5rung`, ρ = −0.0150, n = 4,347 | **NULL** (ungated) |
| grades → boundary hierarchy, **syntactic** channel | H-NEW-2610 **H1b** ρ = −0.1564, p = 9.999×10⁻⁵ under both nulls | PASS — but a second-tuple replication of H-NEW-2560 H5/R9, which is itself demoted **CIRCULARITY-DOMINATED** (ledger §10.142) |
| grades → **verse-final rhyme-class stability** | H-NEW-2610 **H2**, T = +3.41×10⁻⁴, p = 0.458 / 0.405; the registered instrument control **failed its own pre-set gate**, 87.72 % < 90 %; post-hoc repair T = +1.83×10⁻⁴, p = 0.491 / 0.430 | **DOUBLY NULL + INSTRUMENT-FAILED** |
| grades → **clause-length distribution** | H-NEW-2610 **H3**, JT = 2,361, p = 9.999×10⁻⁵ | PASS, then **reducible to verse length**, r(density, mean verse length) = 0.913 |

Every figure above was read out of `runs/h-new-2610/20260807T010205Z/result.json` and
`runs/h-new-2560/20260807T004157Z/result.json` — not out of either finding's prose.

`scripts/check-frontier-staleness.sh` does **not** list F-1 among the items with a finding on
disk. It is a filename/tag matcher and H-NEW-2610 does not carry the F-1 tag. **A grep of
`findings/` for "waqf" surfaced the answer in one command.** The script's own footer already
warns that absence is not proof an item is open; this is a live instance of that warning firing.

### 0.1 A correction owed to `AUDIT-WAQF-MARK-INVENTORY-DIVERGENCE.md`

That audit's counts are all correct and its binding consequence (§5) is right and I have followed
it. But its §4 states: *"no finding using pause marks has ever declared which file it used as a
rules-tuple element."* **That is false on disk, in two places, both dated 2026-08-07:**

- `h-new-2560-fasila-clause-seal.md` line 18 carries `rules_tuple: "(no-tashkeel for the waqf
  join, …)"` in its YAML, and its §"H5 rules-tuple disclosure — the waqf annotation is NOT
  identical across text variants" tabulates all three files, states that full-tashkeel contains
  zero lā, 92 fewer qlà and 111 more jīm, and **self-demotes H5 to SINGLE-TUPLE on that basis.**
- `h-new-2610-waqf-prosody.md` §7 does the same and **retracts its own priority claim** in
  2560's favour, having originally called the divergence something "nobody in this project had
  noticed."

The divergence was found on 2026-08-07, disclosed by its finder against its finder's own result,
and independently re-derived on 2026-08-09 by the audit — which then asserted the absence. This
is the project's own `ABSENCE-CLAIMS` defect occurring inside the file written to prevent a
data-provenance defect, and it is the same shape as the audit's own §6 lesson: *verifying a fact
against the source it came from cannot detect that the source is incomplete.*

Two further items settled before this run and worth carrying: the frontier map and the F-1 brief
both cite *al-Itqān* **nawʿ 27**; the recension on disk merges nawʿ 22–27 under one heading at
line 4631, so the waqf chapter is **nawʿ 28** (H-NEW-2610 §0.1 established this). And **the
muṣḥaf places no graded waqf mark at any verse end** — I reconfirmed this independently: the only
two verse-final marks in either file are saktah, at Q 18:1 and Q 69:28, both outside the graded
set. So "grade predicts *verse-final* rhyme stability" has no verse-final marks to work with.

### 0.2 What was actually left, and what this file does

H-NEW-2610's H3 measured **marks per 100 words, at sūra level, by register**. Nobody had
measured **the length of the segment each grade actually terminates, at the locus level.** That
is the literal reading of F-1's second clause and the only remaining channel that is at once
parser-free, EQTB-free, register-free, and able to carry lā. This file measures it.

---

## 1. Verdict

**NULL on both registered arms. Both inventories agree. Replications agree.** Pre-reg SHA-256
`047ccde3…a86a`, runtime-verified with `SystemExit` on mismatch. Seeds 20260509–20260514,
replication +10, 10,000 permutations per null, k = 12, α_Bonferroni = 0.0041667, **raw decision
gate 0.00041667**.

| arm | inventory | n | ρ (worst channel) | Null A p | Null B p | verdict |
|:--|:--|--:|--:|--:|--:|:--|
| **H1** | full-tashkeel, 4 rungs (the singleton) | 4,266 | **+0.13925** | **0.47825** | 9.999×10⁻⁵ | **NULL** |
| **H2** | min-tashkeel, 5 rungs incl. lā (the consensus) | 4,347 | **+0.13560** | **0.39856** | 9.999×10⁻⁵ | **NULL** |

`sign_ok = True` for both — all six ρ are positive, in the locked direction. `untestable = False`
for both. `replication_agrees = True` for both. Family verdict as pre-committed at §7.3:
**`SECOND CLEAN-CHANNEL NULL`.**

---

## 2. THE FINDING — and it is a decomposition, not a p-value

The observed ρ is **+0.14 and it is real.** What it is not is the hypothesis. Both nulls were
registered in advance and they disagree by a factor of nearly five thousand, which localises the
entire correlation:

| component | H1 (L1 words) | H2 (L1 words) | tested by |
|:--|--:|--:|:--|
| observed ρ | **+0.14333** | **+0.13248** | — |
| ‑ between-**sūra** (survives Null B) | +0.03494 | +0.03690 | nothing here |
| ‑ between-**verse**, within sūra | **+0.10071** | **+0.08891** | Null B only |
| ‑ **within-verse — the hypothesis itself** | **+0.00767** | **+0.00667** | **Null A** |
| that last component, in Null-A SD | **0.84 σ** | **0.76 σ** | p = 0.198 / 0.228 |

**Hold a verse's mark positions fixed and hold its own multiset of grade labels fixed — which is
exactly the question "is this verse's ṣlà on the short segment and its qlà on the long one?" —
and the grades are assigned with respect to length essentially at random: 0.84 standard
deviations, p = 0.198.** Everything else is the grades sitting in different verses.

The pre-registration predicted the size of the untestable component **before the run**: §4.4
computed the ρ_MIN/ρ_MAX midpoint at **+0.135** and warned that no within-verse permutation
could move it. The realised Null-A mean is **+0.1357**. The structural prediction verified to
three decimals.

---

## 3. THE DECIDING PARAMETER IS MY OWN NULL MODEL, AND A DEFENSIBLE DESIGN WOULD HAVE PUBLISHED A PASS

Stated at full prominence because it is the most important sentence in this file.

| parameter varied | p-swing (or ρ-swing) | changes the verdict? |
|:--|--:|:--|
| **null model — Null A vs Null B** | **0.47825 → 0.00010 = 4,782×** | **YES — NULL becomes PASS** |
| P6 segment orientation (closes vs opens) | ρ +0.1433 → +0.0403 = 3.6× | not at this gate |
| P5 length channel (L1 vs L3) | p 0.19798 → 0.47825 = 2.4× | no |
| P1 inventory (full vs min vs no-tashkeel) | ρ +0.1433 / +0.1325 / +0.1287 = 1.11× | no |

**Under Null B alone, both arms pass the gate at the Monte-Carlo floor in all three length
channels.** Within-sūra label permutation is not a foolish null — it is the obvious first choice,
and a lane that had registered only that null would have published *"the Sajāwandī grades order
segment length, p < 10⁻⁴, replicated, both inventories"* and it would have been wrong in exactly
the way `cross-finding-029` describes.

I locked "worst over both nulls" at §7.1 before seeing any number, and I hold to it, because
Null B leaves the grade↔verse assignment free and that assignment is verse length wearing a grade
label (§6). But the choice was **mine**, it was **free**, and it **decided the verdict**. This is
the deciding-parameter law applying to this run and not merely being cited by it.

---

## 4. All three length channels, as required — and the dominant one named

| arm | channel | ρ | Null A p | Null B p | ρ resid. on host-verse words | tie fraction |
|:--|:--|--:|--:|--:|--:|--:|
| H1 | L1 words | +0.14333 | 0.19798 | 9.999×10⁻⁵ | +0.11371 | 0.9981 |
| H1 | L2 skeleton chars | +0.14004 | 0.45555 | 9.999×10⁻⁵ | +0.11123 | 0.9944 |
| H1 | **L3 raw chars — the worst, and the headline** | **+0.13925** | **0.47825** | 9.999×10⁻⁵ | +0.11042 | 0.9899 |
| H2 | L1 words | +0.13248 | 0.22758 | 9.999×10⁻⁵ | +0.10472 | 0.9984 |
| H2 | L2 skeleton chars | +0.13058 | 0.39216 | 9.999×10⁻⁵ | +0.10414 | 0.9940 |
| H2 | **L3 raw chars — the worst, and the headline** | **+0.13560** | **0.39856** | 9.999×10⁻⁵ | +0.10869 | 0.9926 |

**Dominant channel: L3 (raw vocalised characters) is the worst in both arms**, at 2.4× and 1.8×
the p of the word channel. **No channel changes the verdict** — all three are null under Null A
and all three are at the floor under Null B. The length channel is therefore *not* the deciding
parameter here, and saying so is as much a part of the mandate as finding one when it is.

**The tie fraction is 0.99 — 39 distinct word-lengths across 4,266 segments.** The project rule
that >50 % ties requires an exact test is satisfied **by construction, not by exception**: every
p-value in this design is a permutation p-value computed under exactly the tie structure the data
has, on tie-corrected midranks. No asymptotic Spearman distribution, no *t*-approximation and no
χ² appears anywhere in `scripts/h-new-3180.py`.

**Reducibility (prereg §7.4, pre-committed).** Residualising segment length linearly on host-verse
word count moves ρ from +0.1433 to +0.1137 — it removes about a fifth, not the effect. The
mechanism is verse-level but it is **not** captured by a linear term in verse length, because
segment length is roughly *verse length ÷ (marks + 1)*. See §6.

---

## 5. Power, MDE, and the S\* vs S_max branch — including the half this design cannot see

**The UNTESTABLE branch was checked and did not fire**, but it was close enough to matter:

| arm | ρ_MAX achievable | ρ_crit (Null A at gate) | headroom |
|:--|--:|--:|--:|
| H1 | +0.3692 | +0.1660 | 2.22× |
| H2 | +0.3595 | +0.1524 | 2.36× |

**MDE, in interpretable units.** Starting from a Null-A draw and then perfectly length-ordering
the labels within a fraction *f* of permutable verses: *f* = 0.05 → power 0.00; **0.10 → 0.20;
0.15 → 0.55; 0.20 → 1.00** (20 seeds each, 632 permutable verses). **MDE ≈ 20 % of permutable
verses perfectly ordered.** The design is not blind; it would have seen a fifth of the corpus's
multi-grade verses behaving as al-Sajāwandī's definitions imply. It saw 0.84 σ.

**And now the branch that is genuinely untestable, declared in the pre-registration before the
run and not softened after it.** Only **1,834 of 4,266 loci (43.0 %)** for H1 and **1,923 of
4,347 (44.2 %)** for H2 sit in verses carrying **two or more distinct grades**. A verse with one
mark, or with three marks all jīm, is invariant under within-verse permutation. **Null A is inert
on ~57 % of the data, and the fixed component it cannot move is ~+0.13 — pushing in the locked
direction.** A Null-A NULL is therefore a null about label *assignment within verses*. It is not,
and I will not write it as, a null about the whole ρ. This is the honest analogue of the lane
whose critical value 119.45 sat above its S_max of 119: here the test is not untestable, but it
is testable over less than half of its own data, and the half it cannot see leans the way the
hypothesis wanted.

---

## 6. Post-hoc — the mechanism, and both poles of the ladder run backwards

**Everything in this section is POST-HOC, ungated, MW-7-capped (α ceiling 0.05, no replication),
and outside the Bonferroni family.** It is written to `runs/h-new-3180/POSTHOC-20260809T120425Z/`
with `POST_HOC: true` in the file. It cannot rescue anything and is not offered as doing so.

**The table below is the H2 / min-tashkeel arm** (the 12-file consensus inventory), because it is
the only one that carries lā. The full-tashkeel figures are in the same JSON and differ
negligibly on the shared rungs (ṣlà 7.33 / 22.31, jīm 8.52 / 24.38, qlà 9.37 / 26.84,
mīm 6.86 / 24.76).

| grade | rank | n | mean segment (words) | **mean host-verse words** | mean marks in host verse |
|:--|:-:|--:|--:|--:|--:|
| **ۙ lā** *(H2 only, waqf mamnūʿ)* | **1** | 68 | **9.51** | 25.82 | 2.37 |
| ۖ ṣlà *waṣl awlā* | 2 | 1,682 | 7.25 | 22.23 | 2.37 |
| ۚ jīm *jāʾiz* | 3 | 1,972 | 8.50 | 24.64 | 2.43 |
| ۗ qlà *waqf awlā* | 4 | 603 | 9.19 | 26.31 | 2.46 |
| **ۘ mīm** *lāzim* | **5** | 22 | **6.86** | 24.36 | 2.77 |

**The mechanism.** Mean host-verse length rises monotonically across the three well-powered rungs
— 22.2 → 24.6 → 26.3 words — while marks per host verse stays nearly flat at ~2.4. **Stronger
stop grades sit in longer verses, and longer verses cut into longer segments.** That is the
between-verse component of §2, and it is H-NEW-2610's H3 length law reappearing one level down:
not "which register", but "which verse".

**Both ends of the ladder invert.** The three middle rungs are monotone in the locked direction
(7.25 < 8.50 < 9.19). **lā, the bottom rung and the inventory's only prohibition, closes the
longest segments of any grade (9.51). mīm, the top rung and the only obligatory stop, closes the
shortest (6.86).** The two grades whose semantics are least ambiguous are the two that run
backwards. **n = 68 and n = 22. Nothing rests on this** — but it is the same shape as
H-NEW-2610 §3, where the omnibus washed out because ṣlà and jīm are 87.5 % of the loci and are
effectively tied, and it is consistent with that finding's untested "marks concentrate where
surface cues mislead" reading. It remains untested here too, and testing it on this run is
exactly what must not happen.

**P6, the orientation parameter, is informative and was declared in advance.** The segment a mark
*opens* gives ρ = +0.040 against +0.143 for the segment it *closes* — a 3.6× drop. The
association is with what precedes the mark, not what follows it. Ungated.

---

## 7. Both inventories, as the audit requires

| tuple | n | grades | ρ (L1) | verdict |
|:--|--:|:--|--:|:--|
| `quran-full-tashkeel.json` (the singleton the map named) | 4,266 | 4 — **no lā** | +0.14333 | **NULL** (gated, H1) |
| `quran-min-tashkeel.json` (the 12-file consensus) | 4,347 | 5 — lā present | +0.13248 | **NULL** (gated, H2) |
| `quran-no-tashkeel.json` (third tuple) | 4,347 | 5 — lā present | +0.12867 | ungated variant |

**The inventory is not the deciding parameter for this question** — the three tuples span 1.11×
in ρ and agree on the verdict. **Which inventory is correct is not settled here and I have not
settled it by preference**; that needs a printed-muṣḥaf comparison or the upstream provenance
record, neither of which is on disk. What is now on the record is that the F-1 concern — that
running on the singleton would test a hierarchy with its negative pole deleted — **is a real
concern that this particular test survives**, because both arms were run and both are null.

`P4` (admitting saktah and muʿānaqa as segmentation boundaries) moves ρ by ≤ 0.001. Ungated.

---

## 8. Controls, checked against all three ways a control fails

Per `cross-finding-030-three-ways-a-control-fails.md`, checked before the run and reported after:

1. **Does it discriminate?** **Yes.** Within-verse relabelling moves ρ across a range of ~0.47
   (ρ_MIN −0.099 → ρ_MAX +0.369), and the realised Null-A SD is 0.0091 with the observed 0.84 σ
   inside it. A null with real spread that the observed did not clear. **Not mechanism 1.**
2. **Does it apply?** **Only partially, and this is a declared, quantified mechanism-2
   exposure.** Null A is inert on 57 % of loci (§5). It is the reason Null B exists and the
   reason §5 is written the way it is. Declared in the pre-registration, not discovered afterwards.
3. **Does it duplicate the treatment?** **No.** Null A destroys exactly the grade↔length
   association under test while holding mark positions, mark density, verse length, sūra
   identity and register **identical by construction**. **Not mechanism 3.**

**Instrument control (prereg §4.6), and it could have failed.** Before any statistic, the parser
had to reproduce H-NEW-2610's published loci counts exactly. It did:
full-tashkeel {1:1651, 2:2083, 3:511, 4:21}, n = 4,266; min-tashkeel {1:68, 2:1682, 3:1972,
4:603, 5:22}, n = 4,347 — **exact match on every cell**, against an independent prior
implementation. The run aborts with `SystemExit` otherwise; there is no "close enough" branch.

---

## 9. Verdict-function diff against the pre-registration — what I compared, line by line

Done **before** the run, as required. Prereg §7.1 is the authority;
`scripts/h-new-3180.py::verdict()` is the transcription. Thirteen items compared:

| # | prereg §7.1 | script | match |
|--:|:--|:--|:-:|
| 1 | `p = (1 + #{rho_perm >= rho_obs}) / (1 + n_perm)` | `(1 + int((d >= rho_obs[c]).sum())) / (1 + n_perm)` | ✔ |
| 2 | `p_opp` uses `<=` | `(d <= rho_obs[c]).sum()` | ✔ |
| 3 | `worst_p = max over c, N` | `max(... for c in CHANNELS for N in ("A","B"))` — **max, not min; all 3 channels; both nulls** | ✔ |
| 4 | `worst_p_opp = max over c, N` | same construction | ✔ |
| 5 | `sign_ok` = ALL three c | `all(rho_obs[c] > 0 for c in CHANNELS)` | ✔ |
| 6 | `sign_rev` = ALL three c | `all(rho_obs[c] < 0 …)` | ✔ |
| 7 | `rho_crit` = (1−RAW_GATE) quantile of **Null A** | `np.quantile(d, 1 - RAW_GATE)` guarded by `if tag == "A"` | ✔ |
| 8 | `untestable` = **ANY** c | `any(...)` — not `all` | ✔ |
| 9 | branch order: UNTESTABLE **first**, not overridable | `if untestable: … elif sign_ok … elif sign_rev … else NULL` | ✔ |
| 10 | `RAW_GATE = 0.005 / 12` | `RAW_GATE = 0.005 / TESTS_IN_FAMILY`, `TESTS_IN_FAMILY = 12`; strict `<` in both | ✔ |
| 11 | §7.2 replication mismatch → `NULL-UNSTABLE` | applied in `main()` after both replications | ✔ |
| 12 | §7.3 four family branches | `family_verdict()`, all four present | ✔ |
| 13 | §7.4 reducibility computed whatever the verdict | `rho_residualised_on_host_verse_wordcount` | ✔ |

This project has published a case (H-NEW-2600, ledger §10.144) where a runner declared a verdict
under a **looser** rule than the one registered, which defeats pre-registration entirely. The
table above is the check that failure demands.

---

## 10. What I got wrong, and everything added after the lock

**At full prominence, as required.**

1. **I ran a 50-permutation smoke run on the real data before the final run, and it made the
   observed ρ visible to me.** It was written to a scratch directory outside `findings/`, with
   `SMOKE_RUN: true` in its own output, so that no official-looking run directory was
   manufactured. **No gate, direction, seed, channel, statistic, null or family size was changed
   as a result** — the pre-registration was already SHA-locked and the script's runtime check
   would have aborted any edit to it. The deterministic statistics are identical between smoke
   and final run by construction; only the p-values differ. Recording this is part of it.
2. **The post-hoc section §6 was written after seeing the null.** It is labelled, gated off,
   MW-7-capped and stored in its own directory. It cannot and does not rescue anything.
2b. **Nine numbers in the first draft of this file were wrong in the fifth decimal**, because I
   transcribed them from a console line that printed four decimals and then padded — ρ = 0.14004
   written as 0.13997, 0.13925 as 0.13930, and seven residualised ρ likewise. **A machine check
   of every quoted number against `result.json` caught all nine and they are corrected above.**
   None changed any verdict, and that is exactly why the class of error is worth naming: a
   number that drifts silently and changes nothing is the one that survives into the next
   citation. This is the same shape as the *Itqān* nawʿ drift recorded at
   `cross-finding-029` anchor 5 — the mechanically-checkable field verified, the transcribed one
   rotted.
3. **I initially reached for a segment-length test as though F-1 were open.** It was not, and the
   only reason this file is not a duplicate of H-NEW-2610 is that Step 0 was run first and the
   scope was cut down to the one unmeasured channel. Had I designed before grepping, I would have
   re-run H1a and H2 under a new number. **The staleness script would not have stopped me** — it
   does not list F-1.
4. **k = 12 is deliberately conservative** (2 arms × 3 channels × 2 nulls). Counting arms alone
   gives k = 4 and a looser gate. Per the project rule that Bonferroni tightening self-verifies
   while loosening requires ratification, k = 12 was adopted at lock and **has not been reduced
   after the fact.** It made no difference: the worst p is 0.478 against a gate of 0.00042.
5. **No run directory was deleted.** Both the registered run and the post-hoc directory are on
   disk. Nothing was written into the registered run directory after it was created —
   `os.makedirs(exist_ok=False)`, all files opened `'x'`.
6. **The pre-registration has not been edited since it was hashed.**

---

## 11. Honest limits

1. **The marks are not the Quran.** A twelfth-century editorial layer over a seventh-century
   text, descending from al-Sajāwandī (d. 560/1165), mediated entirely through al-Suyūṭī, whose
   *ʿIlal al-wuqūf* is not on disk. Every result here is about a reciting tradition's analysis.
2. **The named confound is not resolved and this design cannot resolve it.** If the grades
   re-encode the grammarian's clause analysis, a null in a length channel does not distinguish
   "the grades are not a length hierarchy" from "clause length is not what the grammarian was
   tracking." What this file establishes is narrower: **whatever the grades track, it is not
   visible in the length of the span they close, once the verse is held fixed.**
3. **Null A sees 43 % of the loci** (§5). The largest single limitation.
4. **The grade→rank map is a lossy coarsening**, declared as parameter P2: the printed inventory
   is not a 1:1 rendering of al-Sajāwandī's five *marātib*, and ṣlà/qlà are terms of the later
   muṣḥaf-printing tradition (H-NEW-2610 §0.1).
5. **lā n = 68, mīm n = 21/22.** Both poles are thin and both invert (§6). Nothing rests on them.
6. **Not Quran-specific.** No matched Classical-Arabic corpus carries waqf marks, so there is
   nothing to compare against. Quran-internal throughout; not a full Phase-B cross-corpus finding
   under `docs/statistical-rigor-protocol.md` §3.
7. **The permutation tests condition on mark placement as given** and cannot detect error,
   inconsistency, or regional variation in the muṣḥaf's own placement — of which there is real
   historical variation across printing traditions, as this file's own §7 shows.
8. **No human review of any annotation** was performed.
9. **A PASS here would not have been independent of H-NEW-2610 H1b**, since both measure
   "does the mark close a constituent" — this was stated at prereg §1.3 before the run. The NULL
   is correspondingly the more informative outcome, which is why it was worth running.

---

## 12. What this changes

**The standing verdict on al-Sajāwandī hardens.** Before this run, the grade ordering was known
to fail in one annotation-free channel (H-NEW-2610's verse-boundary resemblance, ρ = −0.008) and
to succeed in one contaminated channel (EQTB arc-crossing, ρ = −0.156, itself
circularity-dominated). **It now fails in a second, independent, annotation-free channel** —
built on nothing but word counts and character counts — while the raw correlation that exists in
that channel resolves entirely into "stronger grades sit in longer verses."

The retirement/vindication ledger entry stands where H-NEW-2610 left it — **partially
vindicated** — with the *placement* claim intact (marked junctures are enormously more
boundary-like than unmarked ones) and the *graded architecture* claim now failing in every
parser-free channel yet built. This is the same shape as H-NEW-2220 / cross-finding-026's
anti-chiasmus bound: a classically asserted structure survives as placement but not as the graded
hierarchy the tradition describes.

**I have not written a MASTER-FINDINGS-LEDGER entry.** Several lanes are appending to that file
concurrently and a blind append risks a conflict; integration is the team lead's call.

---

## 13. Cross-references

- **[[h-new-2610-waqf-prosody]]** — the finding that already answered F-1. Read §0 above before
  citing this file as if it were the F-1 test. Its H1a is the first annotation-free null; this is
  the second, on a different instrument.
- **[[h-new-2560-fasila-clause-seal]]** — H5/R9, the monotone grade ladder and the first
  disclosure of the text-file divergence. Demoted CIRCULARITY-DOMINATED at ledger §10.142.
- **[[AUDIT-WAQF-MARK-INVENTORY-DIVERGENCE]]** — its §5 binding consequence is followed here in
  full (both inventories run, source declared as a rules-tuple element). Its §4 absence-claim is
  corrected at §0.1 above.
- **[[cross-finding-029-the-deciding-parameter]]** — §3 is a new anchor for it, and an unusual
  one: the deciding parameter is the **null model**, at a 4,782× p-swing, and it was declared in
  advance rather than discovered in an audit.
- **[[cross-finding-030-three-ways-a-control-fails]]** — §8 checks all three mechanisms; the
  second (does not apply) is a partial, declared exposure.
- **[[h-new-2600-mutawaa-lattice]]** — ledger §10.144, the verdict-rule violation that §9's
  line-by-line diff exists to prevent.

*Bismillāhi al-Raḥmāni al-Raḥīm.*
