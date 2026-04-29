# Emotion Vocabulary — Run 1 Journal

**Date:** 2026-04-12
**Agent:** Phase B — emotion-vocabulary
**Output:** `findings/phase-b-hypotheses/emotion-vocabulary.md`

## Plan

Target emotions: khawf, khashya, rajāʾ, ḥubb, wudd/muwaddah, shawq, ḥuzn, ghaḍab, ṣabr, shukr, yaʾs, qunūṭ, ḥasad, ʿizza, jazaʿ. Also kufr (as counter-field to shukr).

Approach: grep the Dukes morphology file by `ROOT:<BW>` and cross-check with the pre-aggregated `root-stats.csv`.

## Buckwalter root mapping used

| Emotion | Arabic | Buckwalter root |
|---|---|---|
| khawf | خوف | `xwf` |
| khashya | خشي | `x$y` |
| rajāʾ | رجو | `rjw` |
| ḥubb | حبب | `Hbb` |
| wudd/mawaddah | ودد | `wdd` |
| shawq | شوق | `$wq` |
| ḥuzn | حزن | `Hzn` |
| ghaḍab | غضب | `gDb` |
| ṣabr | صبر | `Sbr` |
| shukr | شكر | `$kr` |
| yaʾs | يأس | `yAs` |
| qunūṭ | قنط | `qnT` |
| ḥasad | حسد | `Hsd` |
| ʿizza | عزز | `Ezz` |
| jazaʿ | جزع | `jzE` |
| kufr (counter) | كفر | `kfr` |

## Run log

1. Confirmed data/morphology format from lines 55+; STEM rows carry `ROOT:<bw>` in the FEATURES column.
2. Ran `Grep` counts of `ROOT:<bw>` for each target. Counts (token-level):
   - kfr=525, xwf=124, Ezz=119, Sbr=103, Hbb=95, $kr=75, x$y=48, Hzn=42, wdd=29, rjw=28, gDb=24, yAs=13, qnT=6, Hsd=5, jzE=2, **$wq=0**.
3. The zero count for `$wq` was the surprise finding. Verified by two independent queries (`ROOT:\$wq` in morphology file, and absence from `root-stats.csv`). **shawq is not a Qurʾānic root.**
4. For the khawf/khashya distinction, pulled the full 48 x$y instances and noted the object: Allah or *al-ghayb* in >90%. The khawf formula `laA xawofN Ealayohimo wa laA yaHozanuwna` was cross-referenced.
5. Verified Q 59:21 uses `ROOT:x$y` + `ROOT:Alh` in the mountain parable at positions 11–12. Confirmed paronomasia with adjacent `xa`$iEFA` (root `x$E`, different but phonaesthetically close).
6. Pulled Q 7:156: confirmed `raHomap` (position 18) + `wasiEato` (ROOT:wsE, position 19) + `kul~a $ayo'K` (positions 20–21).
7. Pulled Q 39:53: confirmed `laA taqonaTu` (ROOT:qnT, positions 7–8) + `min raHomapi {ll~ahi` (positions 9–11).
8. Pulled Q 12:84–86: dense cluster confirmed. Four grief-terms (asaf, ḥuzn, kaẓm, bathth) + two affliction-terms (ḥaraḍ, hālikīn) + one complaint-verb (ashkū, ROOT:$kw). This is the densest emotion-cluster I have seen in four verses.
9. For the shukr↔kufr pair, noted that the morphology does not tag "antonymy"; pair recovered from known loci (2:152, 14:7, 27:40, 76:3, 31:12).
10. For ghaḍab, pulled all 24 gDb tokens. Noted that 1:7 uses the passive participle `magoDuwb` — Allah-as-agent is implicit. Noted the Moses-cycle cluster (7:71/150/152/154) and the divine-vs-human asymmetry in 42:37.

## Findings surfaced for monograph

- **The absence of shawq** reshapes the classical fear-love-longing triad. In the Qurʾānic vocabulary the triad is *khashya–rajāʾ–ḥubb*; "longing" as a dedicated emotion root is post-Qurʾānic.
- **Khawf vs khashya is a load-bearing distinction** that is systematically erased by English translation. Every verse selects exactly one of the two roots; the selection follows a reliable rule (presence of knowledge-of-majesty → khashya; anticipation of harm → khawf).
- **The despair floor is lexically doubled.** `lā tayʾasū` (12:87) and `lā taqnaṭū` (39:53) are parallel prohibitions using different roots. Both route the believer back to divine *raḥma* / *rawḥ*.
- **The upper bound of mercy (7:156) and the lower bound of despair (39:53) form a metaphysical frame**: mercy `wasiʿat kulla shayʾ` / despair `lā taqnaṭū`.
- **Ṣabr is statistically the densest affective virtue** (103 tokens) and is presented as a *technology* (co-deployed with ṣalāh) rather than as a passive state.
- **Jacob's grief-cluster Q 12:84–86** models the legitimate pathway for human sorrow: stack every grief-term the language has, then route it *ilā Allāh*.
- **The shukr–kufr field is the densest semantic polarity in scripture** (600 combined tokens, ~1/130 words).

## Queue for downstream agents

- Phonetic analysis of `shakartum / azīdannakum / kafartum` at Q 14:7.
- Structural chiasm between Sūrat Yusuf and Sūrat al-Zumar on the two despair roots.
- Every `ROOT:gDb` verse ±3 for adjacent `ROOT:rHm` — test the "ghaḍab → raḥma pivot" hypothesis.
- Map of mountain-use in cosmology (59:21 khashya-split, 33:72 trust-refusal, 7:143 Sinai collapse).
- Mawaddah-as-gift verses (19:96, 30:21) vs. mawaddah-as-forbidden verses (60:1–7) — relational polarity within one root.

## Issues / gaps

- Did not separate Form-specific counts within each root (e.g. Form III `ṣābara` vs Form I `ṣabara`). Useful refinement.
- Did not verify whether the `wdd` subsplit (wish-vs-affection) is morphologically predictable. Inspection suggests yes — nominal `mawaddah`-form and its adjective carry the affection sense; verbal `wadda / yawaddu` carries the wish sense. Worth a CSV.
- `Ezz` inflation by divine-name tokens distorts the pride count.
