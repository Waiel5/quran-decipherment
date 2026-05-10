---
finding_id: Q045-F-07
surah: 45
surah_name: al-Jāthiyah
file_type: novel-finding
date: 2026-05-10
verdict: PARTIAL
prereg_sha: bdd6f1c9de4ea1d673f9fb1534722b1ce095953f20e54ed23c2d3d89faf7b031
---

# Q045-F-07 — *waylun li-kulli affāk* corpus-uniqueness

## Verdict

**PARTIAL.** The primary phrase **ويل لكل أفاك** is corpus-singleton at Q 45:7. The secondary collocation **أفاك أثيم** is NOT corpus-singleton — it appears at both Q 26:222 AND Q 45:7. The pre-committed dual direction-lock therefore lands on PARTIAL.

## Findings

| Phrase | Loci | Verdict |
|:--|:--|:--|
| ويل لكل أفاك | Q 45:7 only | **corpus-singleton (VINDICATED)** |
| أفاك أثيم | Q 26:222, Q 45:7 | NOT singleton (FALSIFIED) |
| ويل لكل (general) | Q 45:7, Q 104:1 | 2-locus formula |
| أفاك (alone) | Q 26:222, Q 45:7 | 2-locus root |

## Loci in full

- Q 26:222: *tanazzalu ʿalā kulli affākin athīm* — "[the satans] descend upon every habitual-liar, sinner."
- Q 45:7: *waylun li-kulli affākin athīm* — "Woe to every habitual-liar, sinner."

The *affāk athīm* collocation is therefore a **twin** (Q 26:222 ↔ Q 45:7), not a singleton. The Q 45:7 distinctness comes from the *waylun li-kulli* opener-frame (which has a sibling at Q 104:1 *waylun li-kulli humazatin lumazah*).

## Cross-references

The result reveals a deeper structural fact:
- Q 26:222 / Q 45:7 share *affāk athīm* — a corpus-twin pair.
- Q 45:7 / Q 104:1 share *waylun li-kulli* — a different corpus-twin pair.
- Q 45:7 sits at the intersection of two corpus-twin lines — a *crossing-node*.

This is structurally analogous to the Q 25 *tabāraka* node (which sits at the intersection of *tabāraka alladhī* and the Furqān-corpus). The *crossing-node* observation is novel and could be pre-registered as a corpus-wide architectural pattern in a follow-up (H-NEW-XXXX).

## Cross-references

- [[Q025-al-furqan/Q025-F-02|Q025-F-02]] — *tabāraka* crossing-node analog.
- [[Q104-al-humazah/00-overview|Q 104 al-Humazah]] — *waylun li-kulli humaza* sibling locus.
- [[Q026-al-shuara/00-overview|Q 26 al-Shuʿarāʾ]] — *affāk athīm* sibling locus.
- al-Bāqillānī, *Iʿjāz al-Qurʾān*, on *al-fāṣila* (the rhyme-end of Q 45:7 *athīm* matches the rhyme-end of Q 26:222 *athīm* in the same paired-collocation).

## Honest limits

- The collocation surface-form search assumes consonantal stability; under min-tashkeel and full-tashkeel the results are identical (the diacritics distinguish but the consonantal skeleton matches).
- The "crossing-node" interpretation is post-hoc relative to this single test; promoting it to a CONFIRMED finding requires a corpus-wide systematic enumeration of phrase-pair crossings (pre-registered separately).

## Files

- pre-reg: `preregs/Q045-F-07-waylun-affak-phrase-prereg.md`
- script: `scripts/Q045_F_07_waylun_affak.py`
- output: `csv/Q045-F-07.json`
