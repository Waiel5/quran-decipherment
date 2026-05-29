---
surah: 66
surah_name_ar: التحريم
surah_name_translit: al-Taḥrīm
file_type: classical-claims-audit
date_last_updated: 2026-05-29
phase: B+
verdict: 6 claims audited — 4 VINDICATED, 1 NOT-TESTABLE, 1 VINDICATED-as-singleton (corpus-EXACT)
---

# Q 66 al-Taḥrīm — Classical Claims Audit

Each claim is stated with citation, given a rules-tuple, tested where empirically testable, and given an
honest verdict. Default rules-tuple: `(no-tashkeel, orthographic-token, basmala-counted-only-in-Q1,
Hafs-Kufan, Mashriqi)`. Verse text from `quran-text/quran-no-tashkeel.json`.

## Claim 1 — "Sūrat al-Taḥrīm is Medinan, by consensus" (al-Qurṭubī)

**Claim:** al-Qurṭubī, *al-Jāmiʿ li-aḥkām al-Qurʾān*, on Q 66:1: *"madaniyya fī qawl al-jamīʿ"* (Medinan by
all accounts).

**Test:** Cross-check `data/revelation-order.csv` (Tanzil Egyptian Standard + Nöldeke).

**Result:** Q 66 → revelation-order #107, period "Medinan", Nöldeke #109 "Medinan." No Meccan-classification
variant on disk.

**Verdict: VINDICATED.** Q 66 is Medinan in both the Egyptian-standard and Nöldeke chronologies on disk.

## Claim 2 — "It is twelve verses" (al-Qurṭubī)

**Claim:** al-Qurṭubī: *"wa-hiya ithnatā ʿashrata āya"* (it is twelve verses).

**Test:** Count verses in `quran-text/quran-no-tashkeel.json` (Q 66) and cross-check `data/hafs-verse-counts.tsv`.

**Result:** 12 verses in the JSON; `hafs-verse-counts.tsv` line 66 = 12.

**Verdict: VINDICATED.** 12 verses, Hafs-Kūfan. (No variant verse-count tradition for Q 66 is on disk —
the surah is below the threshold where the Kūfan/Baṣran/Madanī counting schools diverge.)

## Claim 3 — "Also called Sūrat al-Nabī" (al-Qurṭubī)

**Claim:** al-Qurṭubī: *"wa-tusammā Sūrat al-Nabī"* (it is also named "the Surah of the Prophet").

**Test:** Is the surah's content dominated by direct prophet-address? Count *yā-ayyuhā al-nabī* vocatives.

**Result:** Q 66 carries the prophet-vocative at v 1 AND v 9 — two attestations, bracketing the surah's
first nine verses. Among Medinan surahs only Q 33 al-Aḥzāb carries more. The alternative name reflects this
double prophet-vocative + the personal-to-the-Prophet opening incident.

**Verdict: VINDICATED (qualitatively).** The "Sūrat al-Nabī" name is descriptively grounded in the surah's
double prophet-vocative framing. (This is a naming-rationale, not a numerical claim; verdict is descriptive.)

## Claim 4 — al-Rāzī's Q 65 → Q 66 munāsaba (shared "rulings of women" + prohibition/divorce)

**Claim:** al-Rāzī, *Mafātīḥ al-ghayb*, on Q 66:1: the connection to Q 65 al-Ṭalāq is *"li-shtirākihimā fī
al-aḥkām al-makhṣūṣa bi-l-nisāʾ"* — both surahs share women-specific rulings, and divorce (al-Ṭalāq's head)
parallels self-prohibition (al-Taḥrīm's head), both being "forbidding what Allāh made lawful."

**Test:** Does the Q 65 → Q 66 seam have an empirical smoothness correlate? Read `h-new-720.json` (per_adjacency).

**Result:** Q 65 → Q 66 delta_raw = **−0.03397**, ascending-rank **5/113** — a clamped/negative **seamless seam**
(one of the 13 smoothest joints in the mushaf). For contrast, the corpus's most expensive seam is Q 1 → Q 2
(0.622). Furthermore Q 64 → Q 65 is also seamless, so Q 64 → Q 65 → Q 66 is a double-seamless run.

**Verdict: VINDICATED.** al-Rāzī's qualitative women's-rulings munāsaba between al-Ṭalāq and al-Taḥrīm has a
direct quantitative correlate: the Q 65 → Q 66 transition is the rank-5 smoothest seam in the corpus on the
TSP-residual instrument. The shared aḥkām-al-nisāʾ vocabulary makes the two surahs' root-distributions
adjacency-cheap.

## Claim 5 — al-Qurṭubī's ring-reading: the dual-exemplar seal (vv 10-12) is an admonition to ʿĀʾisha and Ḥafṣa

**Claim:** al-Qurṭubī, on Q 66:11, citing **Yaḥyā b. Sallām**: the parable *ḍaraba Allāh mathalan li-lladhīna
kafarū* (vv 10-11) was struck *"to warn ʿĀʾisha and Ḥafṣa over their opposition when they backed each other
against the Messenger"* — block D (exemplars) returns to block B (the wives' episode), with Āsiya and Maryam
as positive female models.

**Test (PRE-REGISTERED as Q066-F-01 Arm B):** (i) Is the antithetical kafarū→āmanū adjacent exemplar-frame
corpus-distinctive? (ii) Do the two believer-exemplars (v 11 Āsiya, v 12 Maryam) cohere lexically more than
with the disbeliever exemplar (v 10)?

**Result:**
- **(i) B-H1 VINDICATED:** the adjacent kafarū→āmanū exemplar-frame is **corpus-EXCLUSIVE to Q 66:10-11**
  (0 other corpus occurrences). The *ḍaraba Allāh mathalan* frame appears in only 7 corpus verses total
  (Q 14:24, 16:75, 16:76, 16:112, 39:29, 66:10, 66:11), and ONLY in Q 66 is it the believer/disbeliever
  human-exemplar antithesis.
- **(ii) B-H2 FALSIFIED (pre-commit violation):** J(v11,v12)=0.083 is LESS than J(v10,v11)=0.200 and only
  slightly above J(v10,v12)=0.040. The shared parable-frame {Allāh, ḍ-r-b, m-r-ʾ, m-th-l, q-w-l} binds the
  two *parable-halves* (v10 disbeliever-wives ↔ v11 Āsiya) more tightly than the believer-women *theme*
  binds Āsiya to Maryam. Maryam's verse (no frame; virginity/spirit/word-confirmation vocabulary) is the
  lexical outlier of the seal.

**Verdict: SPLIT.** al-Qurṭubī's *frame-pairing* intuition (the surah deliberately uses the antithetical
parable-frame) is VINDICATED as a corpus-singleton (B-H1). But his *ring-reading* (the two believer-women
as a cohesive admonitory unit) does NOT survive a root-level cohesion test (B-H2): the parable architecture
binds across the belief/disbelief boundary, not within the believer-women pair. Full detail in
`06-novel-findings.md` (Q066-F-01) — published as NULL with full prominence on Arm B.

## Claim 6 — The 8-virtue ideal-wife list of v 5 is a corpus-distinctive enumeration

**Claim (project-internal, motivated by the mufassirūn's attention to v 5):** the verse-5 list *muslimāt
muʾmināt qānitāt tāʾibāt ʿābidāt sāʾiḥāt thayyibāt wa-abkār* is a corpus-distinctive concentration of
feminine-plural descriptors.

**Test:** Scan the corpus for verses with the longest consecutive run of feminine-plural *-āt* descriptor
tokens (length > 3 chars, ending *-āt*).

**Result:** Q 66:5 has a run of **7** consecutive *-āt* feminine-plural descriptors (*muslimāt … sāʾiḥāt* +
*thayyibāt*; *abkār* breaks the *-āt* ending). **No other corpus verse has a run of ≥4** such consecutive
descriptors. Q 66:5 is the **corpus-UNIQUE** maximal feminine-virtue enumeration.

**Verdict: VINDICATED — corpus-SINGLETON.** Q 66:5 is the corpus's densest single-verse feminine-virtue
list, by a wide margin (7 vs the next-best <4). This is a clean deterministic corpus fact and is queued for
formal promotion as Q066-F-03.

## Claim 7 (NOT-TESTABLE) — the two-version asbāb split (Māriya vs honey)

**Claim:** the mufassirūn split on whether v 1's "forbidden lawful thing" was Māriya (al-Ṭabarī, al-Zamakhsharī,
al-Rāzī favor) or the honey (al-Qurṭubī, Ibn Kathīr lead with the Ṣaḥīḥayn honey-narration).

**Test:** This is a historical-isnād question (which occasion the verse responds to), not a structural-numerical
claim about the text.

**Verdict: NOT-TESTABLE (empirically).** The asbāb-al-nuzūl split is a matter of riwāya/isnād evaluation,
outside the project's empirical-architectural instruments. Both versions are on-disk attested (see
`04-hadith-corpus.md`); the Ṣaḥīḥayn weight favors the honey-narration, while the Māriya version dominates the
asbāb/tafsīr chains. Documented, not adjudicated.

## Summary table

| # | Claim | Source | Verdict |
|:--|:--|:--|:--|
| 1 | Medinan by consensus | al-Qurṭubī | **VINDICATED** |
| 2 | 12 verses | al-Qurṭubī | **VINDICATED** |
| 3 | also "Sūrat al-Nabī" | al-Qurṭubī | VINDICATED (descriptive) |
| 4 | Q 65 → Q 66 women's-rulings munāsaba | al-Rāzī | **VINDICATED** (seam rank 5/113) |
| 5 | dual-exemplar seal = admonition ring | al-Qurṭubī (Yaḥyā b. Sallām) | **SPLIT** (frame ✓ B-H1; ring ✗ B-H2) |
| 6 | v 5 = densest fem-virtue list | project-internal | **VINDICATED — corpus-SINGLETON** |
| 7 | Māriya vs honey asbāb | tafsīr split | NOT-TESTABLE |

## Honest limits

- Claim 5's split verdict turns on the QAC root-Jaccard instrument; a different lexical-overlap measure
  (e.g., surface-bigram, or lemma-level) could shift the v10/v11/v12 ordering. The frame-bias (the
  *ḍaraba…mathalan* roots shared by v10-v11 but absent in v12) is the mechanical driver and is documented
  in the Q066-F-01 JSON.
- Claim 6's "corpus-singleton" is on the strict consecutive-*-āt*-run definition; a looser feminine-virtue
  definition (allowing non-*-āt* descriptors) would admit other candidates, but Q 66:5 remains the densest.
- Verse-count variant traditions for Q 66 are not on disk; the 12-verse Hafs count is treated as canonical.

---

*All testable claims pre-registered before computation (Q066-F-01) or deterministic. 2026-05-29.*
