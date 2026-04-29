# Literature Catalog — Run 1

**Date:** 2026-04-12
**Agent:** lit-search
**Output:** `docs/claims-catalog.md`

## Summary of run

### How many claims found
**45 distinct claims** captured across 11 thematic families (A–K). This comfortably exceeds the 30-claim minimum. The file is designed for append-only extension so future runs can add more without renumbering.

### Sources searched

**Primary-source claimant websites / books (treated as claims to verify):**
- submission.org — Rashad Khalifa's Appendix 1, Code-19 tables
- masjidtucson.org — Submitters' current canonical tables
- 19.org — ex-Submitter dissent (Yüksel era)
- kaheel7.com / kaheel7.net — Abdul-Daem Al-Kaheel's numeric-miracle / seven-system e-books
- 114chambers.wordpress.com — anonymous ring-composition + Quran Constant
- quranmiracles.com — Taslaman's "Unchallengeable Miracle" source PDF
- truth-seeker.info, answering-christianity.com, quranmiraclescience.com — Harun-Yahya-tradition restatements
- quran-islam.org — Quranist / Al-Kaheel adjacent
- linguisticmiracle.wordpress.com — Baqarah middle-ayah claim
- iqra.study, islamicity.org, funci.org — secondary re-statements
- i3gaz.com — primalogy / prime numbers source

**Critical / refutation literature:**
- WikiIslam (wikiislam.net + the GitHub mirror) — article-by-article word-count refutations
- answering-islam.org — Jochen Katz's 365-days-hoax and related
- islamhouse.com — Bilal Philips-derived fatwa
- islamqa.info — mainstream Sunni skepticism
- friendlyexmuslim.com (Abdullah Sameer) — ex-Muslim critique
- asharisassemble.com — Shabir Ally-derived critique
- Religions Wiki — general "argument from scriptural codes" framing

**Academic / peer-reviewed:**
- Raymond Farrin (2014), "Structure and Qur'anic Interpretation"
- Michel Cuypers (2007, 2015), rhetorical / chiasmus analysis
- Nicolai Sinai (2017), JQS review essay "Going Round in Circles"
- Sophie Chamas, Bryn Mawr thesis on Bassam Jarrar apocalypses
- M. Khyzer Bin Dost & M. Ahmad (2022), Al-Burhan journal, Al-Kawthar mathematical facts
- Corpus Quran (corpus.quran.com) for lemma-level baseline counts
- Mohammad Alhawarat (2015), text-mining study (thesai.org)
- Brendan McKay et al. (1999), Statistical Science — ELS refutation framework, applied by analogy

**Wikipedia / reference:**
- Quran code, Rashad Khalifa, Edip Yüksel, Muqatta'at, Al-Fatiha, Al-Hadid, Al-Baqara pages

### Which categories of claim are most common

By count in the catalog:
1. **Word-pair symmetries** (Family B) — 15 claims. By far the largest category. Rajul/imra'a, dunya/akhira, sun/moon, day/night, life/death, land/sea, angels/devils, seven heavens, etc. Mostly traceable to 'Abd al-Razzaq Nawfal's 1983 "al-I'jaz al-'Adadi li-l-Qur'an al-Karim," re-amplified by Al-Kaheel and Taslaman.
2. **Code-19 claims** (Family A) — 14 claims. Rashad Khalifa's Appendix 1 is the canonical source; Yüksel and 19.org are derivatives.
3. **Surah-level individual claims** (Family D) — 7 claims. Al-Fatiha, Baqarah, Al-Asr, Al-Kawthar, Al-Hadid, Al-Insan, Al-Qadr.
4. **Structural / chiastic** (Family E) — 3 claims. Farrin, Cuypers, Ayat al-Kursi.
5. **Critical/refutation literature** (Family J) — 4 entries treated as "claims" for symmetry.
6. **Numerical prophecy** (Family F) — 1 claim (Jarrar 2022), which has already failed empirically.
7. **Huruf muqatta'at frequency** (Family G) — 2 claims (overlap with Code-19).
8. **Prophet-name counts** (Family H) — 1 aggregated claim.
9. **Meta / totals** (Family I) — 3 claims.
10. **One-off / edge** (Family K) — 10 claims.

### Replicable vs unfalsifiable

**Cleanly replicable** (can be computed from the text under a fixed rule tuple; correctness is purely arithmetic):
- khalifa-114-chapters-19x6 (trivially true)
- khalifa-grand-total-346199 (pure arithmetic over hafs-kufan)
- khalifa-bismillah-19-letters (under a fixed letter convention)
- pair-jesus-adam-25 (corpus.quran.com already confirms)
- pair-say-said-332 (confirmed by Quranic Arabic Corpus)
- pair-seven-heavens-7, qibla-7, hell-jahannam-77
- prophets-mention-counts
- muqattaat-29-surahs-14-letters
- al-hadid-iron-gematria (abjad arithmetic)
- al-kawthar-10-structure (peer-reviewed source)

**Reproducible only under the source's specific filter** (the filter itself is the claim):
- pair-day-year-365 — selective inclusion/exclusion of yawm forms
- pair-man-woman-24 — strict singular-indefinite
- pair-dunya-akhira-115 — definite-only
- pair-angels-devils-88 — lump-all-forms
- pair-sea-land-32-13 — singular-only
- khalifa-basmala-word-counts — requires rejecting 9:128-129

**Fundamentally unfalsifiable or not disclosed enough to test:**
- khalifa-sawm-1387 / zakat-hajj-3040 (Khalifa's "commandment verses" set is not algorithmic)
- kaheel-sevens-system (system as a whole is infinitely flexible)
- 114chambers family (mix of rules, no disclosure)
- farrin-quran-wide-ring / cuypers-ma'ida-chiasmus — literary, no quantitative threshold for "parallel"
- sum-all-numbers-162146 — "what counts as a number?"
- ali-adams-qurancode bulk outputs — researcher-degrees-of-freedom

**Already empirically falsified:**
- jarrar-israel-2022 — Israel did not fall in 2022

### Disclosure: who spells out their counting rules?

**Explicitly disclose (high):**
- Raymond Farrin — rhetorical-analysis methodology is openly rule-based (though subjective)
- Michel Cuypers — same
- M. Khyzer Bin Dost & M. Ahmad (Al-Kawthar paper) — peer-reviewed, rules stated
- Ali Adams / QuranCode — open-source, rules configurable and inspectable
- Nicolai Sinai, Bilal Philips — critical literature states its recounting rules

**Partially disclose:**
- Rashad Khalifa — names basmala-as-separator policy, but word-definition and hamza conventions left implicit; changed counts across four published versions
- Edip Yüksel — adopts Khalifa's rules without fully re-stating them
- Abdul-Daem Al-Kaheel — usually states which forms are counted for one side of a pair but not the other
- Caner Taslaman — inherits Khalifa's rules implicitly

**Do NOT disclose (low):**
- 'Abd al-Razzaq Nawfal (1983) — original word-pair tables with no method
- Harun Yahya popularisations
- 114chambers blog
- Bassam Jarrar's prophecy arithmetic (the book exists but the filter for which phrases to abjad-sum is chosen post-hoc)
- Most social-media / medium.com restatements

### Honest assessment

This literature is largely bad. The dominant pattern is:

1. Start with a desired round number (365, 19, 7, 114, 2022)
2. Find any lexical or arithmetical combination that yields it
3. Declare the combination the "rule"
4. Treat successes as miracles and silently drop failures

The **researcher-degrees-of-freedom** problem is enormous. The Quran has ~77,000 words across 6,236 verses; any sufficiently expressive filter can find a 19-multiple, a 7-multiple, or a prime. The McKay/Bar-Hillel refutation of Bible-code ELS applies by direct analogy, but (as far as I can find) no one has published a McKay-style formal refutation of Khalifa's specific Code-19 — Bilal Philips' 1987 book is the closest, and it attacks arithmetic errors case-by-case rather than via a statistical null model.

A small number of claims (Jesus=Adam=25, qul=qala=332, 114 chapters=19x6) are arithmetically true under natural counting and can be replicated cleanly — but "true" does not mean "miraculous"; these are small integers where coincidence is expected. The academic structural work (Farrin, Cuypers) is substantively interesting but non-quantitative, and Nicolai Sinai's 2017 JQS critique is the mature academic response.

**For our replication work:** most productive targets are the claims with disclosed rules and small arithmetic. Our job is to (a) reproduce each claim's number under the claimed rule tuple, (b) recompute under the canonical methodology.md rule tuples, (c) compute the rate at which similar filters yield similar-looking "miracles" in random permutations of the same text — this gives us an empirical multiple-comparison correction. That last step is the novel contribution and what actually tests the claims.

### Gaps / followups

- Could not locate primary-source detail for **Halil Karaarslan** (Turkish); search returned no Quran-specific results under that name. May be mis-spelled or obscure. Needs a Turkish-language search pass.
- **Sami Angawi** does not appear to have Quran-numerology claims; his work is on Islamic architecture / sacred proportion in building. Removed from catalog.
- **Iqbal Al-Khateeb** — no specific "Khateeb" author confirmed; 114 Chambers (anon. "Siham Karami") is the closest match for anon-chiastic work and is included.
- **Adnan Al-Refaei** — has a TV series "The Great Miracle" with Code-19 adjacent material; confirmed existence but could not retrieve specific numerical claims beyond the general 19-framework. Placeholder-eligible for a future run.
- **Bassam Jarrar's actual arithmetic** — the 1996 book is in Arabic and I could not retrieve the exact sum-derivation. Needs an Arabic-source search pass for a proper replication.
- **No McKay-style statistical refutation of Khalifa specifically** — this is a literature gap. We may want to write this paper ourselves as part of the project's deliverables.

### Confidence in catalog exhaustiveness

**Medium.** I am confident the catalog covers the major canonical Code-19 and word-pair claims, the famous surah-level claims (Fatiha/Baqarah/Kawthar/Hadid), and the main academic structural work. I am less confident about:
- Arabic-language-only claims from Jarrar, al-Refaei, Nabulsi, and others
- Turkish-language claims (Taslaman is the only Turkish source captured; Karaarslan remains missing)
- Lesser-known popular-science books (Harun Yahya / Global Publishing has dozens of titles we have not individually indexed)
- Minor Shi'i numerological traditions — the catalog is Sunni-heavy
- Sufi gematria (Ibn Arabi, al-Buni) traditions — these are historically older than Nawfal/Khalifa but not "published claims" in the modern sense

Plan: run 2 should specifically target Arabic-language primary sources for Jarrar and al-Refaei, Turkish for Karaarslan, and a sweep of Harun Yahya's Quran-numerology titles.
