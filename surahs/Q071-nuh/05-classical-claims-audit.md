---
surah: 71
surah_name_ar: نوح
surah_name_translit: Nūḥ
file_type: classical-claims-audit
date_last_updated: 2026-05-30
phase: B+
verdict: "5 classical claims audited: 3 VINDICATED, 1 RULES-TUPLE-FRAGILE (Wadd), 1 SHARPENED-VIA-NULL (takrār al-qaṣaṣ → dedicated surah is narrative not lexical anchor)."
---

# Q 71 Nūḥ — Classical Claims Audit

Each claim: stated with citation → rules-tuple to test it → empirical test → verdict.
Pre-registration for the two novel tests is in the surah folder; this file audits the
classical claims those tests bear on, plus three further claims.

## Claim 1 — "Sūrat Nūḥ is Meccan, 28 verses"

- **Source:** al-Qurṭubī, *al-Jāmiʿ li-aḥkām al-Qurʾān*, on Q 71:1 — *"makkiyya, wa-hiya
  thamānin wa-ʿishrūna āya"* (`ar-tafseer-al-qurtubi/71/1.json`); Ibn Kathīr "revealed
  in Makkah" (`en-tafisr-ibn-kathir/71/1.json`).
- **Rules-tuple:** Hafs-Kūfan verse-division; chronology = Nöldeke/Tanzil.
- **Test:** `data/hafs-verse-counts.tsv` line 71 = 28; `data/revelation-order.csv`
  mushaf=71 → Nöldeke #51 Middle Meccan, period "Meccan".
- **Verdict: VINDICATED.** Verse count 28 and Meccan classification both confirmed on
  disk.

## Claim 2 — "Noah was the first messenger sent"

- **Source:** al-Qurṭubī on Q 71:1 (Qatāda ← Ibn ʿAbbās ← the Prophet): *"awwalu rasūlin
  ursila Nūḥ, wa-ursila ilā jamīʿi ahli al-arḍ"* (`ar-tafseer-al-qurtubi/71/1.json`).
- **Rules-tuple:** ḥadīth-verification on disk.
- **Test:** the intercession (shafāʿa) ḥadīth — Ṣaḥīḥ al-Bukhārī idInBook 6326 & 7128
  ("Noah, the first Apostle sent by Allah to the people of the Earth") and Ṣaḥīḥ Muslim
  idInBook 386 ("thou art the first of the Messengers sent on the earth"). All verified
  on disk (`04-hadith-corpus.md` §2).
- **Verdict: VINDICATED** (the rank-claim is grounded in *muttafaq-ʿalayh* ḥadīth).
  Empirically un-falsifiable as a historical proposition, but the *textual-tradition*
  basis is verified.

## Claim 3 — "The five names at v 23 are the idols of Noah's people (Wadd, Suwāʿ, Yaghūth, Yaʿūq, Nasr)"

- **Source:** al-Ṭabarī (`ar-tafsir-al-tabari/71/23.json`), al-Baghawī
  (`ar-tafsir-al-baghawi/71/23.json`), Ibn Kathīr ← al-Bukhārī ← Ibn ʿAbbās
  (`en-tafisr-ibn-kathir/71/23.json`; Bukhārī idInBook 4712).
- **Rules-tuple:** `(no-tashkeel, orthographic-token, exact-token match, Hafs-Kūfan)`.
- **Test (Q071-F-02, PASS-DIRECTED-STRONG):** four of the five names — Suwāʿ (سواعا),
  Yaghūth (يغوث), Yaʿūq (ويعوق), Nasr (ونسرا) — are corpus-strict orthographic singletons
  occurring EXACTLY ONCE in the 6,236-verse corpus, all at Q 71:23.
- **Verdict: VINDICATED.** The classical identification corresponds to a measurable
  corpus-singleton cluster (joint placement p ≈ 4.12e-12 under a uniform-singleton H0).

## Claim 4 — "Wadd is one of the five idols" (the Wadd special case)

- **Source:** same as Claim 3; al-Baghawī additionally records the **qirāʾāt variant**
  *Wadd* (majority) vs *Wudd* (Madinan readers) (`ar-tafsir-al-baghawi/71/23.json`).
- **Rules-tuple sensitivity:** Wadd's status DEPENDS on the lens.
- **Test:** the orthographic token ودا occurs at BOTH Q 71:23 (deity) AND Q 19:96
  (*sa-yajʿalu lahumu al-raḥmānu wuddan* — "the Most Merciful will appoint for them
  affection"). So Wadd is NOT a corpus-strict orthographic singleton; it is a
  **contextual-singleton-deity** only.
- **Verdict: RULES-TUPLE-FRAGILE.** Under the orthographic-token lens Wadd is a
  non-singleton (1 of 5 fails strict-singleton). Under a semantic/sense lens (deity vs
  affection) it is a contextual singleton. The classical sources themselves flag Wadd
  as special (the Wadd/Wudd reading variant + the love/affection homography), so the
  empirical fragility MATCHES the classical hesitation rather than contradicting it.
  This is a clean example of bidirectional rules-tuple sensitivity (the variant does
  not demote the claim; it locates exactly where the claim is lens-dependent).

## Claim 5 — *Takrār al-qaṣaṣ*: the Noah story recurs across surahs (and the dedicated surah anchors it?)

- **Source:** al-Suyūṭī, *al-Itqān fī ʿulūm al-Qurʾān*, nawʿ 63 (*fī qaṣaṣ al-Qurʾān*);
  al-Zarkashī, *al-Burhān*, on *takrār al-qiṣaṣ* — the repeated-narrative principle.
  The *intuitive* extension (tested here) is that Sūrat Nūḥ, the one surah dedicated to
  the prophet, is the lexical hub of the cycle.
- **Rules-tuple:** `(no-tashkeel, QAC v0.4 ROOT, verse-union pericope)`, inherited LOCKED
  from H-NEW-2260.
- **Test (Q071-F-01, NULL):** Q 71 ranks **5th of 6** in mean intra-cycle root-Jaccard
  (mean_J 0.149); the lexical centroid is the SHORT Q 7:59-64 al-Aʿrāf retelling
  (mean_J 0.217). A length-matched random anchor reproduces Q 71's centrality (z=+0.42,
  p_perm=0.278). At the whole-surah FR scale (H-NEW-111) the five Nūḥ-host surahs are
  among Q 71's MOST DISTANT (ranks 79-102/113).
- **Verdict: SHARPENED-VIA-NULL.** The *recurrence* part of the classical claim holds
  (the cycle exists and coheres at pericope scale, H-NEW-2260, z=+2.51). But the
  intuitive *anchor* extension is FALSIFIED: the dedicated surah is the NARRATIVE
  anchor, not the LEXICAL anchor. The conserved flood-core (ark `flk`, deliverance
  `njw`) that binds the cycle is carried by the short retellings; Q 71 — which never
  names the ark and devotes vv 15-20 to cosmological signs — sits at the cycle's
  lexical periphery. This refines the project's takrār-al-qaṣaṣ understanding: a
  prophet's dedicated surah is a lexically-divergent EXPANSION, not the source from
  which the brief retellings are abridged.

## Summary

| # | Claim | Verdict |
|---|---|---|
| 1 | Meccan, 28 verses | VINDICATED |
| 2 | Noah first messenger | VINDICATED (ḥadīth-grounded) |
| 3 | Five names = the five idols | VINDICATED (corpus-singleton cluster) |
| 4 | Wadd as a fifth idol | RULES-TUPLE-FRAGILE (contextual-singleton; matches classical hesitation) |
| 5 | Dedicated surah anchors the Noah cycle | SHARPENED-VIA-NULL (narrative anchor, NOT lexical centroid) |
