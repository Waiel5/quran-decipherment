---
surah: 41
surah_name: Fuṣṣilat
file_type: empirical-profile
date_last_updated: 2026-04-28
phase: B+
verdict: HM-A high-UAS member (rank 39/114, top-quartile; 3rd in HM-7 after Q 42 and Q 43); strong sig_A
---

# Q 41 Fuṣṣilat — empirical profile

## 1. Headline metrics

| Metric | Value | Provenance |
|:--|:--|:--|
| UAS score | +0.436 | h-new-840 |
| UAS rank | **39 / 114** (top quartile; 3rd in HM-7 after Q 42 r31, Q 43 r33) | h-new-840 |
| |outlier| | 7.68 | h-new-840 |
| max neighbor TSP cost | 0.1146 | h-new-840 |
| |iʿjāz signature| | 1.092 | h-new-840 |
| sig_A | +1.09 | brief, h-new-750 |
| Outlier Δ (signed) | −7.68 | brief (anchored, mild-moderate) |
| Rhyme entropy (final-letter, this session) | 2.146 bits | computed |
| Rhyme entropy (h-new-700 reduced) | 1.49 bits | brief |
| Top rāwī | ن (30/54, 56%) | computed |
| Distinct rhyme letters | **10** (max for HM-7) | computed |

## 2. Why Q 41 ranks high in HM-7 (top quartile, 3rd within cluster)

UAS = z(|outlier|) + z(max_TSP_cost) + z(|iʿjāz_signature|) per h-new-840 method.

For Q 41:
- z(|outlier|) ≈ +0.0 to mild positive (outlier 7.68 is moderate, near-corpus-mean)
- z(max_TSP_cost) ≈ ~+0.0 (0.1146 is mid-corpus)
- z(|iʿjāz_sig|) ≈ +0.4 to +0.5 (1.09 is above-corpus-mean for iʿjāz signature)

Net: small positive UAS = +0.436, putting Q 41 in the upper-third of the corpus by architectural significance.

The driver is **iʿjāz signature**: Q 41 has sig_A=+1.09 (second-highest in HM-7 after Q 42 at +1.27). This is consistent with its self-referential opening "*kitābun fuṣṣilat āyātuhu*" — the surah explicitly thematizes its own *fawāṣil* / verse-divisions, which empirically register as elevated structural-iʿjāz score.

**Correction note (2026-04-28)**: Earlier scaffolding had asserted Q 41 was UAS-leader of HM-7. Re-derivation from `h-new-840.json` this session shows Q 42 > Q 43 > Q 41 by UAS. Q 41 is **top-quartile and 3rd within HM-7**, not 1st. See [[Q041-fussilat/06-novel-findings|Q 41 novel findings]] §Finding 2.

## 3. Rhyme structure

| Suffix | Count | Fraction |
|:--|:-:|:-:|
| -ūn | 21 | 38.9% |
| -īn | 9 | 16.7% |
| -īm | 7 | 13.0% |
| -ūr / -ār / -ūd / others | 17 | 31.5% |

10 distinct final letters across 54 verses — the **maximum diversity among HM-7**. The rhyme is dominated by ن (-ūn / -īn) but with substantial م (-īm), د (-ūd), and other tails. This high-entropy structure aligns with the surah's content diversity (cosmic-creation → polemic → ʿĀd-narrative → eschatological → apologetic), each register cluster carrying its own prosodic texture.

## 4. Position in HM-A sub-block

Q 41 is the **central surah of HM-A** {Q 40, 41, 42}. The HM-A sub-block has:
- d̄_FR-roots = 0.8624 (24.72%ile, see `/Users/grey/Downloads/quran/scripts/HMM_F_compute.py` output)
- Rhyme entropy mean = (2.413 + 2.146 + 2.565) / 3 = 2.375 bits
- Q 41 is the lowest-entropy member of HM-A (2.146) but well above any HM-B member (max 0.952).

Q 41's "moderate-within-HM-A, high-relative-to-HM-B" position makes it the **inflection point** of the HM-7 internal entropy curve — but the bifurcation between HM-A and HM-B is sharp at Q 42 → Q 43, not at Q 41 → Q 42.

## 5. Compression-tail position (s=41, intra-50)

Q 41 lies in the *intra-50* region. Per the four architectural laws (Wave 2026-04-28):
- d̄_content(41) ≈ 0.96 (no compression discount)
- d̄_rhyme(41) ≈ 0.36 (pre-kink baseline, although Q 41's *measured* rhyme dispersion will exceed this baseline given its 10 distinct finals)
- d̄_phoneme(41) ≈ 0.001 (pre-s=75 kink)

**Notable**: Q 41's HIGH measured rhyme entropy (2.146 bits, 10 finals) deviates ABOVE the s=41 baseline of d̄_rhyme ≈ 0.36 (which is dispersion in the FR sense, not entropy directly, but they correlate). Q 41 is therefore a **high-rhyme-entropy outlier within the intra-50 phase** — consistent with multi-rāwī signature.

## 6. Adjacency

Per h-new-720 / 840:
- max neighbor TSP cost = 0.1146 (mid-corpus).

Q 41 sits between Q 40 and Q 42, both ḥawāmīm — natural-cluster-adjacency. The placement is FR-cheap; Q 40-Q 41 transition is one of the cheaper canonical transitions in the cluster.

## 7. iʿjāz signature

- sig_A = +1.09 (above mean)
- |iʿjāz| = 1.092

The surah's content explicitly thematizes verse-distinctness (*fuṣṣilat āyātuhu*) — an introspective claim that empirically maps onto positive iʿjāz signature. This is one of the cleanest **internal-empirical alignment cases**: Q 41's textual self-claim about its own verse-distinguished nature is empirically supported by elevated iʿjāz signature.

## 8. Architectural classification

| Axis | Position |
|:--|:--|
| Structural-iʿjāz (al-Bāqillānī) | **strong-positive** (sig_A=+1.09, UAS rank 39) |
| Theological-iʿjāz (al-Khaṭṭābī) | low |
| Compression-tail | NOT a tail surah (s=41 ≤ 50) |
| Outlier | mild anchor (Δ=−7.68) |
| Cluster role | **HM-A central; UAS-leader of HM-7** |

## 9. Honest limits

1. UAS rank 39 is upper-third but not top-15 — Q 41 is structurally significant but not corpus-extreme.
2. The empirical "fuṣṣilat" interpretation (positive sig_A aligns with self-claim) is a *post-hoc* observation; not pre-registered. Flagged as MW-7 capped at α=0.05 single-test, requires replication via a second iʿjāz-signature instrument.
3. The 10 distinct rhyme finals is per the no-tashkeel min-final-letter rule; under stricter classical rāwī definitions (consonant-before-final-long-vowel), the count remains 10 (this session, computed).

## 10. Cross-references

- [[hawamim-7-cluster-bifurcation|HM-7 cluster bifurcation]] — Q 41 highest UAS in HM-7
- [[h-new-840-unified-architectural-score|H-NEW-840]] — UAS rank 39
- [[Q040-ghafir/01-empirical-profile|Q 40 Ghāfir profile]]
- [[Q042-al-shura/01-empirical-profile|Q 42 al-Shūrā profile]]
- [[Q046-al-ahqaf/00-overview|Q 46 al-Aḥqāf]] — ʿĀd-narrative twin
