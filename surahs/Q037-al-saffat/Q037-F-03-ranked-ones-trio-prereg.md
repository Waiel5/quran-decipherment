---
surah: 37
test_id: Q037-F-03
title: Ranked-Ones oath-trio Q 37:1-3 (al-ṣāffāt / al-zājirāt / al-tāliyāt) lexical-cohesion vs Q 37 baseline
file_type: pre-registration
date_locked: 2026-05-08
seed: 20260508
n_perm: 10000
bonferroni_k: 2
bonferroni_family: Q037-F-03-ranked-ones-trio
alpha_bon: 0.025
---

# Q037-F-03 — Pre-registration: Q 37:1-3 oath-trio cohesion vs Q 37 baseline

## 1. Hypothesis (locked before observation)

**H1 (locked direction):** The opening oath-trio Q 37:1-3 (*wa-l-ṣāffāti ṣaffā* / *fa-l-zājirāti zajrā* / *fa-l-tāliyāti dhikrā*) is **more lexically cohesive** (higher mean pairwise token-cosine, higher mean root-cosine) than random 3-verse spans drawn from Q 37. This is a *positive*-cohesion direction.

**H2 (locked direction, secondary):** The oath-trio is also more cohesive than the **next-3 verses** (Q 37:4-6 — the *inna ilāhakum la-wāḥid* monotheism declaration) AND the trio is more cohesive than the **last-3 verses** (Q 37:180-182 — the *subḥāna rabbika rabbi al-ʿizza* closing).

## 2. Operational definitions

- Source: `quran-text/quran-no-tashkeel.json`; tokens are whitespace-separated orthographic words.
- Roots: QAC v0.4 root index, retrieved per verse.
- **Token-cosine** for verses i,j: cos(Counter(tokens_i), Counter(tokens_j)).
- **Root-cosine** for verses i,j: cos(Counter(roots_i), Counter(roots_j)).
- For a 3-verse span S, **cohesion** = mean of the 3 pairwise cosines.

### Permutation null (H1)
- Draw 10,000 random ordered 3-verse spans from Q 37 verses {1, ..., 182}.
- For each, compute cohesion (token-cosine) and cohesion (root-cosine).
- Two-tailed permutation p-value for cohesion(Q 37:1-3) vs the null distribution. Direction LOCKED positive (Q 37:1-3 expected to be ABOVE the median).
- Report token-cosine null p AND root-cosine null p.

### Direct comparisons (H2)
- Compare cohesion(Q 37:1-3) vs cohesion(Q 37:4-6) AND vs cohesion(Q 37:180-182).
- Pre-locked direction: Q 37:1-3 > both.

## 3. Test statistic

- C_trio_token = mean pairwise token-cosine on {v1, v2, v3}.
- C_trio_root = mean pairwise root-cosine on {v1, v2, v3}.
- p_token, p_root (permutation against random 3-spans of Q 37).
- C_456, C_180_182.

## 4. Success / Failure

- **CONFIRMED**: H1 passes (p_token ≤ α_bon = 0.025 OR p_root ≤ α_bon = 0.025) AND H2 passes (C_trio > both comparison spans).
- **DIRECTIONAL**: H1 OR H2 passes, not both.
- **NULL**: H1 fails AND H2 fails.
- **Pre-commit violation**: cohesion(Q 37:1-3) below median of random 3-spans on BOTH metrics (would falsify the "tight oath-trio" intuition).

## 5. Honest limits known a priori

- 3-token verses produce highly variable cosine values; the {v1: *wa-l-ṣāffāti ṣaffā*, v2: *fa-l-zājirāti zajrā*, v3: *fa-l-tāliyāti dhikrā*} tokens share the prefix و/ف+ال and the verbal-noun terminal-pattern, so token-cosine should be elevated by template alone.
- Roots {ṣ-f-f, z-j-r, t-l-w, dh-k-r} are 4 distinct roots; root-cosine across the 3 verses will be low (each verse has 2 roots; pairwise overlap is approximately {dh-k-r, ṣ-f-f, ...} = 0). Root-cohesion is likely lower than token-cohesion.
- The classical oath-form template *wa-X / fa-Y / fa-Z* repeats elsewhere (Q 51, Q 77, Q 79, Q 100). The cohesion is partly TEMPLATE not partly SEMANTIC.
- Pre-reg discloses: the CLASSICAL DISPUTE on the referent (al-Ṭabarī: angels; al-Rāzī: angels OR people in prayer-rows; al-Bāqillānī: the Quran's own verses). The empirical TEST does not adjudicate the classical referent; it only asks whether the 3 opening verses form an empirically-tighter cluster than random 3-verse spans of Q 37.

## 6. Rules-tuple

`(no-tashkeel, orthographic-token + QAC-root, cosine, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)`.

## 7. Bonferroni

k = 2 (token-cosine + root-cosine). α_bon = 0.025.

## 8. SHA256 lock

Embedded in `scripts/Q037_F_03_ranked_ones_trio.py`; verified at runtime.
