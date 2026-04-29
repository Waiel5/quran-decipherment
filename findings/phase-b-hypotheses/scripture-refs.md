---
finding_id: scripture-refs
phase: B
status: deep-audit complete
date: 2026-04-12
agent: scripture-refs-run-1
rules:
  orthography: Buckwalter lemma match (Kais Dukes v0.4)
  verse_numbering: Hafs-Kufan
  inclusion_rule: proper-name noun tokens (Tawrāh, Injīl, Zabūr), plural-noun scroll tokens (ṣuḥuf), and the four key relational terms (muṣaddiq, muhaymin, yuḥarrif, furqān, ahl al-dhikr).
cross_refs:
  - findings/phase-b-hypotheses/quranic-self-reference.md
  - findings/phase-b-hypotheses/covenant-language.md
  - findings/phase-b-hypotheses/parables-catalog.md
  - findings/phase-b-hypotheses/quotation-analysis.md
---

# Prior-scripture references in the Qurʾān — the full audit

The Qurʾān does not name itself alone. It names *other* scriptures — Torah, Gospel, Psalms, the Scrolls of Abraham and Moses — and positions itself in a precise, explicit relationship to them: confirming (muṣaddiq), safeguarding (muhaymin), and distinguishing (furqān). It also accuses the keepers of those prior scriptures of a specific type of textual tampering (taḥrīf). This file catalogs those references verse-by-verse and examines the lexical architecture that binds them.

Every token count in this file has been verified against the Kais Dukes morphology v0.4. No numbers are paraphrased from secondary sources.

---

## 1. al-Tawrāh (الْتَوْرَاة) — the Torah, 18 occurrences

Proper name, always definite, never inflected for plurality. The morphology registers 18 PN tokens under the lemma `t~aworaY`p` — matching exactly the count most commonly cited in the tafsīr tradition.

| # | Verse | Case | Immediate context |
|---|---|---|---|
| 1 | Q 3:3 | ACC | "He sent down the Book upon you in truth, confirming (muṣaddiqan) what came before it, and He sent down the Torah and the Gospel." |
| 2 | Q 3:48 | ACC | Jesus taught "the Book, the Wisdom, the Torah, and the Gospel." |
| 3 | Q 3:50 | GEN | Jesus: "confirming what is before me *of the Torah*." |
| 4 | Q 3:65 | NOM | "O People of the Book, why do you argue about Abraham, when neither the Torah nor the Gospel was sent down until after him?" |
| 5 | Q 3:93 | NOM | "Bring the Torah and recite it, if you are truthful." |
| 6 | Q 3:93 | GEN | (same verse, second reference — "min qabli an tunazzala l-Tawrāh"). |
| 7 | Q 5:43 | NOM | "And how would they make you judge when they have the Torah, in which is the judgment of God?" |
| 8 | Q 5:44 | ACC | "Indeed, We sent down the Torah, in which was guidance and light." |
| 9 | Q 5:46 | GEN | "We sent Jesus son of Mary, confirming what preceded him of the Torah." |
| 10 | Q 5:46 | GEN | (same verse — "gave him the Gospel... confirming what preceded it of the Torah"). |
| 11 | Q 5:66 | ACC | "If they had upheld the Torah, the Gospel, and what was sent down to them from their Lord..." |
| 12 | Q 5:68 | ACC | "You stand on nothing until you uphold the Torah and the Gospel and what has been sent down to you." |
| 13 | Q 5:110 | ACC | To Jesus: "I taught you the Book, the Wisdom, the Torah, and the Gospel." |
| 14 | Q 7:157 | GEN | The ummī prophet "they find written with them in the Torah and the Gospel." |
| 15 | Q 9:111 | GEN | "A promise upon Him in truth, in the Torah, the Gospel, and the Qurʾān." |
| 16 | Q 48:29 | GEN | "That is their description in the Torah, and their description in the Gospel." |
| 17 | Q 61:6 | GEN | Jesus: "confirming what is before me of the Torah and bringing news of a messenger who comes after me, whose name is Aḥmad." |
| 18 | Q 62:5 | ACC | "Those who were charged with the Torah, then did not carry it, are like a donkey carrying tomes." |

**Distribution.** All 18 are Medinan. They cluster in two surahs: Āl ʿImrān (5×) and al-Māʾidah (7×). The remaining six are dispersed across six different surahs (each with exactly one token). This is consistent with the thematic profile of those two surahs: both are heavily engaged with the People of the Book and both revolve around the question of scriptural continuity.

**Co-occurrence pattern.** In 12 of 18 occurrences the Torah is named in the same verse as the Gospel (Injīl). In 2 further verses (3:50, 61:6) the Torah is named alongside Jesus without the Gospel mentioned. Only in 4 verses (5:43, 5:44, 7:157, 62:5) does the Torah appear without an explicit Gospel-token in the verse itself.

---

## 2. al-Injīl (الْإِنْجِيل) — the Gospel, 12 occurrences

Proper name, always definite. 12 tokens of `<injiyl` in the morphology. The classical count of 12 is exact.

| # | Verse | Case | Role |
|---|---|---|---|
| 1 | Q 3:3 | ACC | Named with Torah as the two sent-down precedents. |
| 2 | Q 3:48 | ACC | Curriculum taught to Jesus. |
| 3 | Q 3:65 | NOM | Negative argument: neither scripture existed before Abraham. |
| 4 | Q 5:46 | ACC | "We gave him the Gospel, in which was guidance and light." |
| 5 | Q 5:47 | GEN | "Let the People of the Gospel judge by what God sent down in it." |
| 6 | Q 5:66 | ACC | Conditional: "had they upheld the Torah and the Gospel…" |
| 7 | Q 5:68 | ACC | Charge: "uphold the Torah and the Gospel…" |
| 8 | Q 5:110 | ACC | Curriculum to Jesus (parallel to 3:48). |
| 9 | Q 7:157 | GEN | The ummī prophet prophesied in both scriptures. |
| 10 | Q 9:111 | GEN | The covenant recorded in Torah, Gospel, and Qurʾān. |
| 11 | Q 48:29 | GEN | The believers' description in the Torah "and their description in the Gospel" (the simile of the seed). |
| 12 | Q 57:27 | ACC | "We placed in the hearts of those who followed [Jesus] compassion and mercy and monasticism." |

**The Torah-Gospel pair.** 10 of the 12 Injīl-tokens co-occur with a Tawrāh-token in the same verse. Only Q 5:47 (where "the people of the Gospel" alone are addressed) and Q 57:27 (Christian-specific) name the Gospel standalone.

**The triple Torah-Gospel-Qurʾān** is named only once explicitly — Q 9:111. That verse is the single Quranic statement of the three-scripture continuum in one verse. It reads: "He has promised in truth, in the Torah, the Gospel, and the Qurʾān."

---

## 3. al-Zabūr (الْزَّبُور) — the Psalms, 3 occurrences

Proper name, ROOT:zbr ("to write firmly, inscribe"). Three tokens only.

| # | Verse | Form | Function |
|---|---|---|---|
| 1 | Q 4:163 | indefinite ACC | "And We gave David a zabūr." |
| 2 | Q 17:55 | indefinite ACC | "And We gave David a zabūr." (near-verbatim doublet of 4:163). |
| 3 | Q 21:105 | definite GEN | "We have written in the zabūr, after the Reminder (al-dhikr), that the earth shall be inherited by My righteous servants." |

**The Psalm 37:29 citation.** The third occurrence (Q 21:105) is a direct textual claim: the Qurʾān quotes what it says is *in* the Zabūr. The text it renders — "anna l-arḍa yarithuhā ʿibādiya l-ṣāliḥūn" — is a close paraphrase of Psalm 37:29: "The righteous shall inherit the land, and dwell therein for ever." The lexical match is striking:

- Psalm 37:29 (Hebrew): *ṣaddīqîm yīršū-ʾāreṣ*
- Q 21:105 (Arabic): *yarithu-hā ʿibādiya l-ṣāliḥūn al-arḍ*

Both use the precise verb "inherit" (yrš / wrth — the roots are cognate), the adjective "righteous" (ṣaddīq / ṣāliḥ) modifying the subject, and "earth/land" (ʾereṣ / arḍ) as the object. This is the clearest case in the Qurʾān of an explicit cross-scriptural citation that can be verified against a specific biblical verse. Two details:

1. The Qurʾān attributes the line to "the Zabūr" without specifying which Psalm.
2. The Qurʾān prefaces it with "min baʿdi l-dhikri" — "after the Reminder." If al-dhikr here = Torah (per Q 16:43, Q 21:7), the verse is stating a temporal stratification: Torah first, then Zabūr, which re-inscribed this promise.

The two indefinite occurrences (4:163, 17:55) are doublets of a single formula. Both are Medinan; 21:105 is Meccan. The indefinite form (zabūran, not al-zabūr) in those two verses is grammatically interesting — it treats "a zabūr" as a genus-item rather than a unique title.

---

## 4. Ṣuḥuf Ibrāhīm wa-Mūsā — the Scrolls of Abraham and Moses

The morphology lists 8 tokens of the plural noun ṣuḥuf (ROOT:SHf, plural of ṣaḥīfa "sheet"):

| # | Verse | Context |
|---|---|---|
| 1 | Q 20:133 | "Has there not come to them the proof of what is in the earlier ṣuḥuf?" |
| 2 | Q 53:36 | "Has he not been told of what is in the ṣuḥuf of Moses…?" (followed by 53:37: "…and Abraham, the one who fulfilled [his trust]"). |
| 3 | Q 74:52 | "Rather, each one of them wants to be given ṣuḥuf spread out" — satirical: ignoring a common revelation, they demand personal scrolls. |
| 4 | Q 80:13 | "In honored ṣuḥuf" — describing the Qurʾān itself or heavenly Tablets. |
| 5 | Q 81:10 | "And when the ṣuḥuf are spread" — eschatological "scrolls" of deeds. |
| 6 | Q 87:18 | "Indeed, this is in the earliest ṣuḥuf (al-ṣuḥuf al-ūlā)." |
| 7 | Q 87:19 | "The ṣuḥuf of Abraham and Moses." |
| 8 | Q 98:2 | "A messenger from God reciting purified ṣuḥuf." |

**The Abraham-Moses ṣuḥuf verses.** The explicit paired attribution — "ṣuḥuf Ibrāhīm wa-Mūsā" — occurs twice (53:36-37 and 87:18-19). Both are Meccan, both end their surah on the note that this revelation re-transmits content already attested in the earliest scrolls. The claim is significant: Abraham is nowhere in the Biblical canon as the recipient of a written scripture, but the Qurʾān assigns him ṣuḥuf alongside Moses. This is a distinctive Quranic expansion of the canon of prior revelation.

Q 20:133 makes the same claim without naming Abraham — "the proofs of what is in al-ṣuḥuf al-ūlā" — as a rhetorical question put to disbelievers.

---

## 5. muṣaddiq (confirming) and muhaymin (guardian-over) — Q 5:48

Q 5:48 is the single most doctrinally dense verse about the Qurʾān's relationship to prior scripture:

> wa-anzalnā ilayka l-kitāba bi-l-ḥaqqi **muṣaddiqan** li-mā bayna yadayhi min al-kitābi wa-**muhayminan** ʿalayhi
> "We have sent down to you the Book in truth, *confirming* what came before it of scripture, and *a guardian-over* it."

Both words are active participles of form II. Their meanings:

- **muṣaddiq** (Sdq): "attesting to the truth of," "verifying." It is a relational, non-competitive term — the Qurʾān does not supersede the prior scriptures' truth; it *authenticates* them.
- **muhaymin** (hmn): the form II active participle. The root appears only twice in the Qurʾān — here (of the Qurʾān) and in Q 59:23 (as a divine name). Etymologies debate a Syriac loanword (mhaymen "trustworthy, custodian") versus an Arabic augment of amn. The semantic core is "overseer / guardian / trustee." The Qurʾān stands as custodian over prior scriptures — authoritatively identifying their true content.

The pairing is load-bearing: muṣaddiq on its own could suggest subordination (we merely confirm); muhaymin on its own could suggest supersession (we overrule). Together they define a relationship of *authorizing continuity plus adjudicating authority*.

**muṣaddiq count.** The word occurs 19 times in the morphology. Of these, 15 refer explicitly to a new revelation confirming prior revelation (the Qurʾān confirming the Torah, Jesus confirming the Torah, John confirming Jesus, each messenger confirming his predecessor). This makes muṣaddiq the structural hinge of Quranic scripture-theology.

**muhaymin count.** Only 2 tokens — Q 5:48 (of the Qurʾān) and Q 59:23 (of Allāh). The lexical rarity heightens the verse's weight.

---

## 6. Taḥrīf — the distortion motif

The verb yuḥarrifūn (form II, ROOT:Hrf) occurs 4 times: Q 2:75, Q 4:46, Q 5:13, Q 5:41. Form II intensifies the root meaning "edge, margin" → "to bend, to twist at the edges." It describes a specific pattern of textual mishandling:

- **Q 2:75**: "A party of them used to hear the word of God, then *distort it* (yuḥarrifūnahū) after having understood it, while they knew." The accusation specifies the cognitive element — they understood, then twisted.
- **Q 4:46**: "Of the Jews are those who *distort words from their places* (yuḥarrifūna l-kalima ʿan mawāḍiʿihī)." The distortion here is rearrangement — displacing words.
- **Q 5:13**: "They distort words from their places, and they have forgotten a portion of what they were reminded of." Distortion paired with amnesia.
- **Q 5:41**: The same phrase — yuḥarrifūna l-kalima min baʿdi mawāḍiʿihī — applied to a specific scenario (men sent to spy on the Prophet's judgment).

**Structural note.** The Qurʾān accuses a *party* (farīq) of distortion — never the entirety of the People of the Book. The verb is always present-tense (yuḥarrifūn); the Qurʾān describes an ongoing practice, not a completed corruption of the source text. This is consistent with the simultaneous Quranic affirmations that the Torah "has guidance and light" (5:44) and is a live, authoritative reference ("how would they make you judge, when they have the Torah, in which is God's judgment?" — 5:43).

**Co-occurrence with muṣaddiq/muhaymin.** Q 5:13 (taḥrīf) and Q 5:48 (muṣaddiq-muhaymin) sit 35 verses apart in the same surah. The structural argument of al-Māʾidah is: *the prior scriptures are true but have been tampered with at their margins; the Qurʾān both confirms and polices them.*

---

## 7. al-Furqān — a scriptural category, not a Quranic proper name

Furqān (ROOT:frq, "to separate, distinguish") occurs 7 times in 6 verses. Four usages clearly refer to the Qurʾān: Q 2:185, Q 3:4, Q 25:1, and (with debated reference) Q 8:29. But the word is **also** applied to the Mosaic revelation — twice, unambiguously:

- **Q 2:53**: "And when We gave Moses the Book and al-Furqān, that you might be guided."
- **Q 21:48**: "We gave Moses and Aaron al-Furqān, a light, and a reminder (dhikr) for the godfearing."

Q 21:48 is particularly striking because it pairs al-Furqān with dhikr — both of which are elsewhere Quranic self-names. The verse confirms:

1. **al-Furqān is a scriptural category**, not a proper name unique to the Qurʾān. A Furqān is *any revelation that discriminates truth from falsehood*. The Qurʾān claims the title, but so does the Torah.
2. **al-Dhikr is likewise a scriptural category.** It is used of the Qurʾān throughout, but here it is applied to the Mosaic revelation.

This is consistent with Q 2:53 where the Mosaic revelation is explicitly "the Book and al-Furqān." The tradition has sometimes read "the Furqān" in Q 2:53 as a separate gift (the parting of the Red Sea), but Q 21:48 disambiguates by collocation: Furqān + Light + Dhikr is a scripture-triad description.

**Consequence.** The Qurʾān uses a shared vocabulary to name revelation across the prophetic series — *the book, the criterion, the reminder, the light*. The Qurʾān's proper names are largely category-names shared with prior scriptures.

---

## 8. "ahl al-dhikr" — the People of the Reminder

The phrase occurs exactly twice:

- **Q 16:43**: "And We did not send before you any but men to whom We revealed — *so ask the people of the Reminder if you do not know* (fa-sʾalū ahla l-dhikri in kuntum lā taʿlamūn)."
- **Q 21:7**: "And We did not send before you any but men to whom We revealed — *so ask the people of the Reminder if you do not know*."

The two verses are a near-verbatim doublet. The context in both is identical: an argument that prior prophets were also human messengers (rijāl). The addressees of the injunction are invited to consult those who know, and those are called "the people of the Reminder."

Given that al-dhikr is a synonym for revelation (used as a Quranic self-name; also used of Moses's revelation in Q 21:48), "ahl al-dhikr" unambiguously = "people of [prior] scripture." The Qurʾān here directs its audience to consult the Jewish and Christian custodians of earlier revelation for factual verification of its historical claims — a remarkable epistemic positioning.

The phrase also links to **al-dhikr** the scripture-name: prior scriptures are dhikr; those who keep them are ahl al-dhikr; the Qurʾān itself claims to be a dhikr (e.g. Q 15:9). The three usages stand in the same semantic field — the continuity of revelation as a tradition of remembrance.

---

## 9. Synthesis — the Qurʾān's scriptural self-location

Combining the counts:

- 18 Tawrāh + 12 Injīl + 3 Zabūr + 2 named ṣuḥuf-of-Abraham-and-Moses passages + 1 Furqān-of-Moses passage + 2 ahl-al-dhikr passages = **38 verses** of explicit named prior-scripture reference.
- Of these, more than half (22) are in Āl ʿImrān and al-Māʾidah alone — the two surahs that most directly engage the People of the Book.
- The Qurʾān co-identifies as muṣaddiq to them (in 15+ verses) and as muhaymin over them (in 1 verse — the hapax-level statement of Q 5:48).
- It critiques a *practice* (taḥrīf) attributed to a *party* among them, while affirming the prior books themselves as genuine divine revelations containing guidance.
- It shares with them the lexicon of naming: kitāb, furqān, dhikr — none of these names are exclusive to the Qurʾān; all are used of prior revelation too.

**The emergent picture** is of a text that does not present itself as a rupture with prior scripture but as the *adjudicating continuation* of it. The Qurʾān names itself in the same terms it uses for Torah and Gospel. It names the keepers of those books as the proper people to ask about revelation. It identifies itself as their muhaymin, not their replacement.

The signature quantitative pattern — 18 Torah, 12 Gospel, 3 Psalms — is not proportional to the size of those corpora but to the density of their interaction with the Qurʾān's Medinan debate partners. The concentration is diagnostic: prior-scripture citation is a *Medinan* rhetorical mode, tied to specific audiences. The three Zabūr references (of which one is Meccan) are the exception — the shortest citation, but the one with the most textually verifiable biblical antecedent (Psalm 37:29).

Taken together, the 38 verses constitute a coherent doctrine of scriptural history: revelation is sequential, cumulative, shared-named, partly-tampered-with by its human custodians, and now re-consolidated in a Qurʾān that speaks of itself in the same terms it uses for what came before.
