#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
H-NEW-2670 — Joint conjunction improbability: the muqaṭṭaʿāt-14 under ALL declared
constraints simultaneously.

H-NEW-2550 tested the 14 muqaṭṭaʿāt letters one axis at a time and applied Bonferroni
k = 28. Bonferroni controls the family-wise error of a UNION. It cannot answer the
INTERSECTION question: how many of the 40,116,600 possible 14-subsets satisfy ALL the
observed properties simultaneously? This script computes that number exactly, reports the
shrinkage curve under several orderings, measures pairwise independence between the
properties, and — most importantly — runs the uniqueness-by-construction control that
distinguishes a real joint constraint from constraint-stacking.

Pre-registration:
  findings/phase-b-hypotheses/prereg-h-new-2670-joint-conjunction.md
Its SHA-256 is embedded below and verified at runtime (SystemExit on mismatch), per
INVESTIGATION-PROTOCOL §1.2. Frozen input SHAs are verified likewise.

DEPENDENCY DISCLOSURE (deviation from Protocol §7.1 "stdlib only"): numpy is used, for the
same reason H-NEW-2550 declared it — the null is an EXACT enumeration of all 40,116,600
subsets. A stdlib-only guard independently re-derives the joint survivor count.

Author: Waiel Al-Shujaa
"""

import hashlib
import itertools
import json
import math
import os
import random
import sys
import time
from datetime import datetime, timezone

import numpy as np

# ----------------------------------------------------------------------------
# 0. PATHS, PRE-REGISTRATION GATE, FROZEN INPUT GATE
# ----------------------------------------------------------------------------

ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", ".."))
PREREG = os.path.join(ROOT, "findings", "phase-b-hypotheses",
                      "prereg-h-new-2670-joint-conjunction.md")
OUT_JSON = os.path.join(ROOT, "findings", "phase-b-hypotheses", "csv", "h-new-2670.json")

PREREG_SHA256 = "d6c5a48179585f665c5563f7357629ebb616bb00d075bf4fac2032034615fe7c"

FROZEN_INPUTS = {
    "quran-text/quran-full-tashkeel.json":
        "382a7341300602ec8b366316d4bbe2a44955c2bf984d395bdd82dae6110b6715",
    "quran-text/quran-no-tashkeel.json":
        "253f72f32f1dd4f6288c24be1b3b81b2e32c67aedd59aecb6e4a057dae35918a",
    "findings/phase-b-hypotheses/csv/h-new-69.json":
        "86d4796bc6dc2cc807565048f9ee7a1944f52bd5cc434e847481351d6bd56fb3",
    "findings/phase-b-hypotheses/scripts/h-new-2550.py":
        "87aeabfff8c25d4563e77db1f9b5f59d202f824fb33a08e1606f2febe3c7264a",
}

SEED = 20260509
SEED_REPLICATION = 20260519
N_CONTROL = 1000
N_ORDER_PERMS = 500
N_SUBSETS = 40116600            # C(28,14)


def _sha256(path):
    with open(path, "rb") as fh:
        return hashlib.sha256(fh.read()).hexdigest()


def verify_gates():
    got = _sha256(PREREG)
    if got != PREREG_SHA256:
        raise SystemExit(
            "PRE-REGISTRATION SHA MISMATCH — refusing to run.\n"
            f"  expected {PREREG_SHA256}\n  actual   {got}\n"
            "Per INVESTIGATION-PROTOCOL §1.2 this run is void."
        )
    print(f"[gate] pre-reg SHA-256 verified: {got}")
    for rel, want in FROZEN_INPUTS.items():
        have = _sha256(os.path.join(ROOT, rel))
        if have != want:
            raise SystemExit(
                f"FROZEN INPUT SHA MISMATCH — refusing to run.\n  {rel}\n"
                f"  expected {want}\n  actual   {have}"
            )
    print(f"[gate] {len(FROZEN_INPUTS)} frozen inputs verified")
    return got


# ----------------------------------------------------------------------------
# 1. THE ATTESTED 14 — DERIVED FROM THE CORPUS, NEVER ASSERTED  (MW-6a, MW-6b)
# ----------------------------------------------------------------------------

VOCALISATION = set(range(0x064B, 0x0653)) | {0x0670}

H1740_SURAHS = [2, 3, 7, 10, 11, 12, 13, 14, 15, 19, 20, 26, 27, 28, 29, 30, 31, 32,
                36, 38, 40, 41, 42, 43, 44, 45, 46, 50, 68]
ZAMAKHSHARI_14 = set("الم" "ص" "ر" "ك" "ه" "ي" "ع" "ط" "س" "ح" "ق" "ن")
ZAMAKHSHARI_COUNTS = {"mahmusa": 5, "majhura": 9, "shadida": 4, "rikhwa": 10, "mutbaqa": 2,
                      "munfatiha": 12, "mustaliya": 3, "munkhafida": 11, "qalqala": 2}


def derive_muqattaat():
    with open(os.path.join(ROOT, "quran-text", "quran-full-tashkeel.json"), encoding="utf-8") as fh:
        full = json.load(fh)
    with open(os.path.join(ROOT, "quran-text", "quran-no-tashkeel.json"), encoding="utf-8") as fh:
        nt = json.load(fh)
    loci, scanned = [], 0
    for si, srh in enumerate(full):
        for vi in (0, 1):
            if vi >= len(srh["verses"]):
                continue
            scanned += 1
            tok = srh["verses"][vi]["text"].split()[0]
            if not any(ord(c) in VOCALISATION for c in tok):
                loci.append({"surah": srh["id"], "verse": srh["verses"][vi]["id"],
                             "opening": nt[si]["verses"][vi]["text"].split()[0]})
    letters = sorted({c for lc in loci for c in lc["opening"]})
    surahs = sorted({lc["surah"] for lc in loci})
    assert len(loci) == 30, f"MW-6a: expected 30 loci, got {len(loci)}"
    assert surahs == H1740_SURAHS, "MW-6a: surah catalogue disagrees with H-NEW-1740 §1"
    assert len(letters) == 14, f"MW-6b: expected 14 letters, got {len(letters)}"
    assert set(letters) == ZAMAKHSHARI_14, "MW-6b: derived 14 != al-Zamakhshari's fourteen"
    print(f"[MW-6a/b] {len(loci)} loci / {len(surahs)} surahs / 14 letters derived from "
          f"corpus; {scanned} tokens scanned, 0 false positives")
    return loci, letters, surahs


# ----------------------------------------------------------------------------
# 2. LETTER FREQUENCY — reproduces H-NEW-1810 exactly  (MW-6d)
# ----------------------------------------------------------------------------

FOLD = {"أ": "ا", "إ": "ا", "آ": "ا", "ٱ": "ا", "ى": "ي", "ة": "ت", "ؤ": "و", "ئ": "ي"}
H1810 = {"ا": 59280, "ل": 38191, "ن": 27270, "م": 26735, "ي": 25747, "و": 25486,
         "ه": 14850, "ت": 12864, "ر": 12403, "ب": 11491, "ك": 10497, "ع": 9405,
         "ف": 8747, "ق": 7034, "س": 6012, "د": 5991, "ذ": 4932, "ح": 4140,
         "ج": 3317, "خ": 2497, "ش": 2124, "ص": 2072, "ض": 1686, "ز": 1599,
         "ث": 1414, "ط": 1273, "غ": 1221, "ظ": 853}
H1810_TOTAL, H1810_HAMZA = 329131, 1578
H1810_TOP14 = list("النميوهترب") + ["ك", "ع", "ف", "ق"]


def letter_frequencies():
    with open(os.path.join(ROOT, "quran-text", "quran-no-tashkeel.json"), encoding="utf-8") as fh:
        d = json.load(fh)
    c = {}
    for srh in d:
        for v in srh["verses"]:
            for ch in v["text"]:
                ch = FOLD.get(ch, ch)
                if "ء" <= ch <= "ي":
                    c[ch] = c.get(ch, 0) + 1
    hamza = c.pop("ء", 0)
    total = sum(c.values())
    assert c == H1810, "MW-6d: letter frequencies do not reproduce H-NEW-1810"
    assert total == H1810_TOTAL and hamza == H1810_HAMZA, "MW-6d: totals"
    top14 = [k for k, _ in sorted(c.items(), key=lambda kv: -kv[1])][:14]
    assert top14 == H1810_TOP14, f"MW-6d: TOP14 {''.join(top14)} != H-NEW-1810 rank 1-14"
    print(f"[MW-6d] letter frequencies reproduce H-NEW-1810 (total {total}, hamza {hamza}); "
          f"TOP14 = {''.join(top14)}")
    return c, hamza, top14


# ----------------------------------------------------------------------------
# 3. THE LOCKED CLASS TABLE (pre-reg §1)
# ----------------------------------------------------------------------------

ALPHABET28 = list("ابتثجحخدذرزسشصضطظعغفقكلمنهوي")

MAHMUSA    = set("تثحخسشصفكه")     # 10 — al-Zamakhshari, al-Kashshaf ad Q 2:1
SHADIDA    = set("ابتجدطقك")        # 8
MUTBAQA    = set("صضطظ")            # 4
MUSTALIYA  = set("خصضطظغق")         # 7
QALQALA    = set("بجدطق")           # 5
BAYNIYYA   = set("رعلمن")           # 5 — RT-2 only (later tripartite tajwid)

SONORANT   = set("رلمنوي")          # 6 — H-NEW-69 phonotactic side-test
DOTLESS    = set("احدرسصطعكلمهو")   # 13 — H-NEW-60 per-letter table
PHARYNGEAL = set("اهعح")            # 4 — H-NEW-44.2 al-Khalil POA class

H69_K = {"G1_shamsiyyah": 6, "G2_qamariyyah": 8, "G3_majhura_Sibawayh": 9,
         "G4_mahmusa_Sibawayh": 5, "G5_modern_voiced": 7, "G6_modern_voiceless": 7,
         "G7_safir": 2, "G8_itbaq": 2}


def load_h69_groupings():
    with open(os.path.join(ROOT, "findings", "phase-b-hypotheses", "csv", "h-new-69.json"),
              encoding="utf-8") as fh:
        d = json.load(fh)
    return {g["name"]: set(g["letters"]) for g in d["groupings_tested"]}


def assert_class_table(muq14, G):
    """MW-6c, MW-6e, MW-6f, MW-6i — every table pinned to a published source."""
    S = set(muq14)
    got = {"mahmusa": len(S & MAHMUSA), "majhura": len(S - MAHMUSA),
           "shadida": len(S & SHADIDA), "rikhwa": len(S - SHADIDA),
           "mutbaqa": len(S & MUTBAQA), "munfatiha": len(S - MUTBAQA),
           "mustaliya": len(S & MUSTALIYA), "munkhafida": len(S - MUSTALIYA),
           "qalqala": len(S & QALQALA)}
    assert got == ZAMAKHSHARI_COUNTS, (
        f"MW-6c: table fails al-Zamakhshari's nine stated counts\n  stated {ZAMAKHSHARI_COUNTS}"
        f"\n  computed {got}")
    assert (len(MAHMUSA), len(SHADIDA), len(MUTBAQA), len(MUSTALIYA), len(QALQALA),
            len(BAYNIYYA)) == (10, 8, 4, 7, 5, 5), "MW-6f: genus sizes"
    assert (len(SONORANT), len(DOTLESS), len(PHARYNGEAL)) == (6, 13, 4), "MW-6f: block sizes"
    for name, g in G.items():
        assert len(S & g) == H69_K[name], f"MW-6e: H-NEW-69 {name} overlap"
    # MW-6i — the redundancies the pre-reg discloses must be REAL, so the disclosure
    # cannot silently become false.
    assert G["G8_itbaq"] == MUTBAQA, "MW-6i: G8 itbaq != mutbaqa (pre-reg §1.3 disclosure)"
    assert G["G4_mahmusa_Sibawayh"] == MAHMUSA, "MW-6i: G4 != mahmusa"
    assert G["G1_shamsiyyah"] | G["G2_qamariyyah"] == set(ALPHABET28), "MW-6f: G1/G2"
    assert G["G3_majhura_Sibawayh"] | G["G4_mahmusa_Sibawayh"] == set(ALPHABET28), "MW-6f: G3/G4"
    assert G["G5_modern_voiced"] | G["G6_modern_voiceless"] == set(ALPHABET28), "MW-6f: G5/G6"
    # MW-6f — H-NEW-60 and H-NEW-44.2.1
    assert len(S & DOTLESS) == 11, "MW-6f: H-NEW-60 dotless 11/13"
    assert len(S & PHARYNGEAL) == 4, "MW-6f: H-NEW-44.2.1 pharyngeal 4/4"
    assert len(S & SONORANT) == 5, "MW-6f: H-NEW-69 sonorant 5/6"
    print(f"[MW-6c/e/f/i] class table verified: al-Zamakhshari's nine counts {got}; "
          f"H-NEW-69 overlaps reproduce; G8==mutbaqa and G4==mahmusa (disclosed redundancies)")
    return got


# ----------------------------------------------------------------------------
# 4. COORDINATE SYSTEM — every declared property is a function of these
# ----------------------------------------------------------------------------
# name, letter-class, bit-width.  Field widths hold min(|f|, 14) without carry, so packed
# half-keys add exactly.  G2=14-G1, G3=14-mahmusa, G4=mahmusa, G6=14-G5, G8=mutbaqa,
# rikhw=14-shadida-bayniyya are DERIVED, never stored.
COORDS = [("mahmusa", MAHMUSA, 4), ("shadida", SHADIDA, 4), ("mutbaqa", MUTBAQA, 3),
          ("mustaliya", MUSTALIYA, 3), ("qalqala", QALQALA, 3), ("top14", None, 4),
          ("G1", None, 4), ("G5", None, 4), ("G7", None, 2), ("sonorant", SONORANT, 3),
          ("dotless", DOTLESS, 4), ("pharyngeal", PHARYNGEAL, 3), ("bayniyya", BAYNIYYA, 3)]
CIX = {n: i for i, (n, _, _) in enumerate(COORDS)}
NC = len(COORDS)
MASS_BIT = sum(w for _, _, w in COORDS)          # 44
SHIFTS, MASKS = [], []
_s = 0
for _n, _c, _w in COORDS:
    SHIFTS.append(_s)
    MASKS.append((1 << _w) - 1)
    _s += _w
BALANCE_LOW_BITS = sum(w for _, _, w in COORDS[:5])     # coords 0..4 occupy the low bits
BALANCE_MASK = (1 << BALANCE_LOW_BITS) - 1


def build_classes(G, top14):
    cls = []
    for name, c, _w in COORDS:
        if c is not None:
            cls.append(c)
        elif name == "top14":
            cls.append(set(top14))
        elif name == "G1":
            cls.append(G["G1_shamsiyyah"])
        elif name == "G5":
            cls.append(G["G5_modern_voiced"])
        elif name == "G7":
            cls.append(G["G7_safir"])
        else:
            raise AssertionError(name)
    for (n, _, w), c in zip(COORDS, cls):
        assert min(len(c), 14) < (1 << w), f"field {n} too narrow"
    return cls


def coords_of(subset, classes):
    return [len(subset & c) for c in classes]


# ----------------------------------------------------------------------------
# 5. EXACT ENUMERATION — meet in the middle over all C(28,14) subsets  (MW-6g)
# ----------------------------------------------------------------------------

def half_table(letters, classes, freq):
    """Packed key + mass for every subset of one 14-letter half, grouped by cardinality."""
    n = len(letters)
    per_letter_key = np.zeros(n, dtype=np.int64)
    per_letter_mass = np.zeros(n, dtype=np.int64)
    for i, ch in enumerate(letters):
        k = 0
        for t, c in enumerate(classes):
            if ch in c:
                k |= (1 << SHIFTS[t])
        per_letter_key[i] = k
        per_letter_mass[i] = freq[ch]
    by_size = {j: ([], []) for j in range(n + 1)}
    for m in range(1 << n):
        j = m.bit_count()
        k = 0
        w = 0
        mm = m
        while mm:
            b = (mm & -mm).bit_length() - 1
            k += int(per_letter_key[b])
            w += int(per_letter_mass[b])
            mm &= mm - 1
        by_size[j][0].append(k)
        by_size[j][1].append(w)
    return {j: (np.array(a, dtype=np.int64), np.array(b, dtype=np.int64))
            for j, (a, b) in by_size.items()}


def enumerate_exact(classes, freq):
    """Returns (unique packed keys, counts). Total must equal C(28,14) exactly."""
    A, B = ALPHABET28[:14], ALPHABET28[14:]
    ta, tb = half_table(A, classes, freq), half_table(B, classes, freq)
    mass_thresh = 0.50 * H1810_TOTAL
    out = np.empty(N_SUBSETS, dtype=np.int64)
    pos = 0
    for j in range(0, 15):
        ka, wa = ta[j]
        kb, wb = tb[14 - j]
        if ka.size == 0 or kb.size == 0:
            continue
        for lo in range(0, ka.size, 512):
            kas, was = ka[lo:lo + 512], wa[lo:lo + 512]
            blk = kas[:, None] + kb[None, :]
            msk = (was[:, None] + wb[None, :]) > mass_thresh
            blk += msk.astype(np.int64) << MASS_BIT
            f = blk.ravel()
            out[pos:pos + f.size] = f
            pos += f.size
    assert pos == N_SUBSETS, f"MW-6g: enumerated {pos}, expected C(28,14)={N_SUBSETS}"
    keys, counts = np.unique(out, return_counts=True)
    del out
    assert int(counts.sum()) == N_SUBSETS, "MW-6g: counts do not sum to C(28,14)"
    print(f"[MW-6g] enumerated {N_SUBSETS:,} subsets exactly; "
          f"{keys.size:,} distinct property-coordinate profiles")
    return keys, counts


def unpack(keys):
    C = np.empty((keys.size, NC), dtype=np.int8)
    for t in range(NC):
        C[:, t] = ((keys >> SHIFTS[t]) & MASKS[t]).astype(np.int8)
    massbit = ((keys >> MASS_BIT) & 1).astype(bool)
    return C, massbit


# ----------------------------------------------------------------------------
# 6. THE ELEVEN DECLARED PROPERTIES (pre-reg §1)  +  derived statistics
# ----------------------------------------------------------------------------

PROP_IDS = ["P1", "P2", "P3", "P4", "P5", "P6", "P7", "P8", "P9", "P10", "P11"]
PROP_DESC = {
    "P1":  "mahmusa (voiceless, 10) split at floor: |S n f| = 5",
    "P2":  "shadida (stops, 8) split at floor: |S n f| = 4",
    "P3":  "mutbaqa (emphatic, 4) split at floor: |S n f| = 2",
    "P4":  "mustaliya (raised, 7) split at floor: |S n f| in {3,4}",
    "P5":  "qalqala (5) split at floor: |S n f| in {2,3}",
    "P6":  "corpus letter-mass share > 0.50",
    "P7":  "overlap with corpus TOP14 by frequency >= 10",
    "P8":  "max Jaccard against H-NEW-69's eight classical 14-cuts <= 0.400",
    "P9":  "sonorants: |S n {r l m n w y}| >= 5",
    "P10": "dotless: |S n DOTLESS(13)| >= 11",
    "P11": "pharyngeal/glottal exhaustivity: |S n {a h ' h}| = 4",
}
PROP_SRC = {
    "P1": "al-Zamakhshari, al-Kashshaf ad Q 2:1 PageV01P028-029; H-NEW-2550 T-A; H-NEW-69 G4",
    "P2": "al-Zamakhshari, al-Kashshaf ad Q 2:1; H-NEW-2550 T-A",
    "P3": "al-Zamakhshari, al-Kashshaf ad Q 2:1; H-NEW-2550 T-A; H-NEW-69 G8",
    "P4": "al-Zamakhshari, al-Kashshaf ad Q 2:1; H-NEW-2550 T-A",
    "P5": "al-Zamakhshari, al-Kashshaf ad Q 2:1; H-NEW-2550 T-A",
    "P6": "H-NEW-1810 T3 (threshold 0.50 pre-locked there before observation)",
    "P7": "H-NEW-1810 T2-weak; al-Suyuti, al-Itqan nawʿ 6",
    "P8": "H-NEW-69 (NULL on all 8 classical 14-cuts)",
    "P9": "H-NEW-69 post-hoc sonorant observation; H-NEW-2550 §4 T-F  [MW-7 CAPPED]",
    "P10": "H-NEW-60 dotless preference, p=0.000919, post-hoc-noticed  [MW-7 CAPPED]",
    "P11": "H-NEW-44.2.1 pharyngeal exhaustivity, PASS-DIRECTED p=0.049  [MW-7 CAPPED]",
}
MW7_CAPPED = {"P9", "P10", "P11"}


def jaccard_max(C, Gsizes):
    """max over G1..G8 of k/(14+|G|-k), from the stored/derived coordinates."""
    g1 = C[:, CIX["G1"]].astype(np.int32)
    g5 = C[:, CIX["G5"]].astype(np.int32)
    g7 = C[:, CIX["G7"]].astype(np.int32)
    mah = C[:, CIX["mahmusa"]].astype(np.int32)
    mut = C[:, CIX["mutbaqa"]].astype(np.int32)
    ks = {"G1_shamsiyyah": g1, "G2_qamariyyah": 14 - g1,
          "G3_majhura_Sibawayh": 14 - mah, "G4_mahmusa_Sibawayh": mah,
          "G5_modern_voiced": g5, "G6_modern_voiceless": 14 - g5,
          "G7_safir": g7, "G8_itbaq": mut}
    best = np.zeros(C.shape[0], dtype=np.float64)
    for name, k in ks.items():
        np.maximum(best, k / (14.0 + Gsizes[name] - k), out=best)
    return best


def declared_indicators(C, massbit, Gsizes):
    c = {n: C[:, CIX[n]] for n in CIX}
    mj = jaccard_max(C, Gsizes)
    I = np.empty((C.shape[0], 11), dtype=bool)
    I[:, 0] = c["mahmusa"] == 5
    I[:, 1] = c["shadida"] == 4
    I[:, 2] = c["mutbaqa"] == 2
    I[:, 3] = (c["mustaliya"] == 3) | (c["mustaliya"] == 4)
    I[:, 4] = (c["qalqala"] == 2) | (c["qalqala"] == 3)
    I[:, 5] = massbit
    I[:, 6] = c["top14"] >= 10
    I[:, 7] = mj <= 0.400 + 1e-12
    I[:, 8] = c["sonorant"] >= 5
    I[:, 9] = c["dotless"] >= 11
    I[:, 10] = c["pharyngeal"] == 4
    return I, mj


def d_taxonomy(C, tripartite):
    """H-NEW-2550's imbalance statistic D. tripartite=False -> T-A (5 genera);
    True -> T-C (7 genera, later tajwid manner split)."""
    mah = C[:, CIX["mahmusa"]].astype(np.float64)
    sha = C[:, CIX["shadida"]].astype(np.float64)
    mut = C[:, CIX["mutbaqa"]].astype(np.float64)
    mus = C[:, CIX["mustaliya"]].astype(np.float64)
    qal = C[:, CIX["qalqala"]].astype(np.float64)
    D = np.abs(mah - 5.0) + np.abs(mut - 2.0) + np.abs(mus - 3.5) + np.abs(qal - 2.5)
    if not tripartite:
        return D + np.abs(sha - 4.0)
    bay = C[:, CIX["bayniyya"]].astype(np.float64)
    rik = 14.0 - sha - bay
    return D + np.abs(sha - 4.0) + np.abs(bay - 2.5) + np.abs(rik - 7.5)


# ----------------------------------------------------------------------------
# 7. SHRINKAGE CURVES + INDEPENDENCE, all from the 2^11 pattern histogram
# ----------------------------------------------------------------------------

def pattern_histogram(I, counts):
    code = np.zeros(I.shape[0], dtype=np.int32)
    for t in range(11):
        code |= I[:, t].astype(np.int32) << t
    return np.bincount(code, weights=counts.astype(np.float64), minlength=2048).astype(np.int64)


def survivors(hist, idxs):
    """Exact count of subsets satisfying every property in idxs."""
    if not idxs:
        return int(hist.sum())
    m = 0
    for t in idxs:
        m |= 1 << t
    codes = np.arange(2048)
    return int(hist[(codes & m) == m].sum())


def curve(hist, order):
    return [survivors(hist, list(order[:d])) for d in range(1, len(order) + 1)]


# ----------------------------------------------------------------------------
# 8. THE CRITICAL CONTROL — uniqueness by construction (pre-reg §6)
# ----------------------------------------------------------------------------

BAL = ["mahmusa", "shadida", "mutbaqa", "mustaliya", "qalqala"]
DIRECTED = [("top14", "K7"), ("sonorant", "K9"), ("dotless", "K10"), ("pharyngeal", "K11")]


def profile_survivors(keys, C, massbit, mj, counts, x_coords, x_mass, x_mj,
                      medians, self_directed):
    """Exact number of 14-subsets sharing reference set X's own same-kind property profile.

    K1-K5 equality on the five genera; K6 the FIXED mass>0.50 threshold (dropped from X's
    profile if X lacks it); K7/K9/K10/K11 at-least-as-extreme on their coordinate; K8
    at-least-as-non-coincident.  self_directed=True points K7-K11 away from the null median
    on the side X actually falls (Control-2, the fairer guard).
    """
    # K1-K5 in one int64 comparison on the low bits of the packed key.
    bkey = 0
    for n in BAL:
        bkey |= (int(x_coords[CIX[n]]) & MASKS[CIX[n]]) << SHIFTS[CIX[n]]
    sel = np.flatnonzero((keys & BALANCE_MASK) == bkey)
    assert sel.size, "X must share its own balance profile — packing error"
    if x_mass:                                       # K6 (fixed threshold)
        sel = sel[massbit[sel]]
    thr = float(x_mj[0])                             # K8
    if (not self_directed) or thr <= medians["maxjaccard"]:
        sel = sel[mj[sel] <= thr + 1e-12]
    else:
        sel = sel[mj[sel] >= thr - 1e-12]
    for name, _lbl in DIRECTED:                      # K7, K9, K10, K11
        if sel.size == 0:
            break
        v = int(x_coords[CIX[name]])
        col = C[sel, CIX[name]]
        sel = sel[col >= v] if ((not self_directed) or v >= medians[name]) else sel[col <= v]
    n_props = 11 if x_mass else 10
    w = int(counts[sel].sum()) if sel.size else 0
    assert w >= 1, "X is always in its own profile class — filter error"
    return w, n_props


def weighted_median(vals, counts):
    o = np.argsort(vals)
    cs = np.cumsum(counts[o])
    return float(vals[o][np.searchsorted(cs, cs[-1] // 2)])


# ----------------------------------------------------------------------------
# 9. STDLIB-ONLY GUARD — independent re-derivation of the joint survivor count
# ----------------------------------------------------------------------------

def stdlib_guard(classes, freq, Gsizes, G):
    """Pure-stdlib bitmask enumeration of all C(28,14) subsets, no numpy, no
    meet-in-the-middle.  Re-derives the P1..P11 joint count and the P1..P5 count."""
    idx = {ch: i for i, ch in enumerate(ALPHABET28)}
    def mask_of(s):
        m = 0
        for ch in s:
            m |= 1 << idx[ch]
        return m
    m_mah, m_sha = mask_of(MAHMUSA), mask_of(SHADIDA)
    m_mut, m_mus, m_qal = mask_of(MUTBAQA), mask_of(MUSTALIYA), mask_of(QALQALA)
    m_top = mask_of(classes[CIX["top14"]])
    m_g1, m_g5, m_g7 = mask_of(G["G1_shamsiyyah"]), mask_of(G["G5_modern_voiced"]), mask_of(G["G7_safir"])
    m_son, m_dot, m_pha = mask_of(SONORANT), mask_of(DOTLESS), mask_of(PHARYNGEAL)
    w = [freq[ch] for ch in ALPHABET28]
    thr = 0.50 * H1810_TOTAL
    gs = Gsizes
    n5 = n11 = 0
    for combo in itertools.combinations(range(28), 14):
        m = 0
        for b in combo:
            m |= 1 << b
        if (m & m_mah).bit_count() != 5:
            continue
        if (m & m_sha).bit_count() != 4:
            continue
        if (m & m_mut).bit_count() != 2:
            continue
        if (m & m_mus).bit_count() not in (3, 4):
            continue
        if (m & m_qal).bit_count() not in (2, 3):
            continue
        n5 += 1
        if sum(w[b] for b in combo) <= thr:
            continue
        if (m & m_top).bit_count() < 10:
            continue
        k1 = (m & m_g1).bit_count()
        k5 = (m & m_g5).bit_count()
        k7 = (m & m_g7).bit_count()
        kmut = 2
        kmah = 5
        jm = max(k1 / (14 + gs["G1_shamsiyyah"] - k1),
                 (14 - k1) / (14 + gs["G2_qamariyyah"] - (14 - k1)),
                 (14 - kmah) / (14 + gs["G3_majhura_Sibawayh"] - (14 - kmah)),
                 kmah / (14 + gs["G4_mahmusa_Sibawayh"] - kmah),
                 k5 / (14 + gs["G5_modern_voiced"] - k5),
                 (14 - k5) / (14 + gs["G6_modern_voiceless"] - (14 - k5)),
                 k7 / (14 + gs["G7_safir"] - k7),
                 kmut / (14 + gs["G8_itbaq"] - kmut))
        if jm > 0.400 + 1e-12:
            continue
        if (m & m_son).bit_count() < 5:
            continue
        if (m & m_dot).bit_count() < 11:
            continue
        if (m & m_pha).bit_count() != 4:
            continue
        n11 += 1
    return n5, n11


# ----------------------------------------------------------------------------
# 10. MAIN
# ----------------------------------------------------------------------------

def main():
    t0 = time.time()
    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    run_dir = os.path.join(ROOT, "runs", "h-new-2670", stamp)
    os.makedirs(run_dir, exist_ok=True)

    prereg_sha = verify_gates()
    loci, muq14, surahs = derive_muqattaat()
    freq, hamza, top14 = letter_frequencies()
    G = load_h69_groupings()
    zam = assert_class_table(muq14, G)
    Gsizes = {k: len(v) for k, v in G.items()}
    classes = build_classes(G, top14)

    S = set(muq14)
    x_coords = np.array(coords_of(S, classes), dtype=np.int32)
    x_mass = sum(freq[c] for c in S) / H1810_TOTAL

    # ---- MW-6j: every declared property must be TRUE of the attested set --------
    Cx = x_coords.reshape(1, -1).astype(np.int8)
    Ix, mjx = declared_indicators(Cx, np.array([x_mass > 0.50]), Gsizes)
    assert Ix.all(), (
        "MW-6j: a declared property is FALSE of the attested set — property list is "
        f"misdefined: {[PROP_IDS[i] for i in range(11) if not Ix[0, i]]}")
    assert abs(float(mjx[0]) - 0.400) < 1e-9, f"MW-6e: max Jaccard {mjx[0]} != 0.400"
    assert abs(x_mass - 0.7441) < 5e-5, f"MW-6d: mass share {x_mass} != H-NEW-1810 0.7441"
    print(f"[MW-6j] all 11 declared properties verified TRUE of the attested set; "
          f"mass share {x_mass:.4f}, max Jaccard {float(mjx[0]):.4f}")

    # ---- exact enumeration ------------------------------------------------------
    t = time.time()
    keys, counts = enumerate_exact(classes, freq)
    C, massbit = unpack(keys)
    print(f"[time] enumeration {time.time()-t:.1f}s")

    I, mj = declared_indicators(C, massbit, Gsizes)
    hist = pattern_histogram(I, counts)
    assert int(hist.sum()) == N_SUBSETS, "pattern histogram total"

    # ---- marginals --------------------------------------------------------------
    marginals = {}
    for t_ in range(11):
        n = survivors(hist, [t_])
        marginals[PROP_IDS[t_]] = {"n": n, "p": n / N_SUBSETS,
                                   "desc": PROP_DESC[PROP_IDS[t_]],
                                   "source": PROP_SRC[PROP_IDS[t_]],
                                   "mw7_capped": PROP_IDS[t_] in MW7_CAPPED}
        print(f"    marginal {PROP_IDS[t_]:>3}  n={n:>12,}  p={n/N_SUBSETS:.8f}")

    # ---- MW-6h: reproduce H-NEW-2550's 1,024,500 --------------------------------
    n_bal = survivors(hist, [0, 1, 2, 3, 4])
    assert n_bal == 1_024_500, f"MW-6h: P1..P5 count {n_bal:,} != H-NEW-2550's 1,024,500"
    print(f"[MW-6h] P1^..^P5 = {n_bal:,} = {n_bal/N_SUBSETS:.6f} — reproduces H-NEW-2550 §3 "
          f"through an independent engine")
    DA = d_taxonomy(C, False)
    DC = d_taxonomy(C, True)
    n_DA = int(counts[DA <= 1.0 + 1e-9].sum())
    n_DC = int(counts[DC <= 6.0 + 1e-9].sum())
    assert n_DA == 1_024_500, f"MW-6h: D_TA<=1.0 gives {n_DA:,}"
    assert abs(n_DC / N_SUBSETS - 0.5567158) < 1e-6, f"MW-6h: D_TC<=6.0 p={n_DC/N_SUBSETS}"
    print(f"[MW-6h] aggregate arms reproduce H-NEW-2550 §4: T-A p={n_DA/N_SUBSETS:.7f}, "
          f"T-C p={n_DC/N_SUBSETS:.7f}")

    # ---- THE JOINT COUNT ---------------------------------------------------------
    W = survivors(hist, list(range(11)))
    W8 = survivors(hist, list(range(8)))
    print(f"\n[JOINT] all 11 declared properties: W = {W:,}  "
          f"p_exact = {W}/{N_SUBSETS} = {W/N_SUBSETS:.12g}")
    print(f"[JOINT] MW-7-capped (P1..P8 only):   W8 = {W8:,}  p = {W8/N_SUBSETS:.12g}")
    assert W >= 1, "PRE-COMMIT VIOLATION: W=0 means a property is misdefined (pre-reg §7)"

    # naive independence product
    naive = 1.0
    for t_ in range(11):
        naive *= marginals[PROP_IDS[t_]]["p"]

    # ---- shrinkage curves --------------------------------------------------------
    declared = list(range(11))
    by_restrict = sorted(declared, key=lambda t_: marginals[PROP_IDS[t_]]["n"])
    orders = {
        "O1_declared": declared,
        "O2_reverse": declared[::-1],
        "O3_most_restrictive_first": by_restrict,
        "O4_least_restrictive_first": by_restrict[::-1],
    }
    curves = {k: {"order": [PROP_IDS[i] for i in v], "survivors": curve(hist, v)}
              for k, v in orders.items()}
    rnd = random.Random(SEED)
    env = [[] for _ in range(11)]
    for _ in range(N_ORDER_PERMS):
        o = declared[:]
        rnd.shuffle(o)
        for d, v in enumerate(curve(hist, o)):
            env[d].append(v)
    envelope = [{"depth": d + 1, "min": min(e), "median": int(np.median(e)), "max": max(e)}
                for d, e in enumerate(env)]
    curves["O5_random_500"] = {"order": "500 uniformly random orderings, seed 20260509",
                               "envelope": envelope}
    capped_order = list(range(8))
    curves["MW7_capped_P1_P8_declared"] = {"order": [PROP_IDS[i] for i in capped_order],
                                           "survivors": curve(hist, capped_order)}

    # ---- independence matrix ------------------------------------------------------
    pairs = []
    for a in range(11):
        for b in range(a + 1, 11):
            na, nb = marginals[PROP_IDS[a]]["n"], marginals[PROP_IDS[b]]["n"]
            nab = survivors(hist, [a, b])
            pa, pb, pab = na / N_SUBSETS, nb / N_SUBSETS, nab / N_SUBSETS
            lift = pab / (pa * pb) if pa * pb > 0 else float("nan")
            den = math.sqrt(pa * (1 - pa) * pb * (1 - pb))
            phi = (pab - pa * pb) / den if den > 0 else float("nan")
            nested = (nab == min(na, nb))
            rel = "NESTED" if nested else (
                "NOT INDEPENDENT" if (abs(phi) >= 0.5 or lift >= 2.0) else "approx independent")
            pairs.append({"a": PROP_IDS[a], "b": PROP_IDS[b], "n_a": na, "n_b": nb,
                          "n_ab": nab, "lift": lift, "phi": phi, "relation": rel})
    nested_pairs = [p for p in pairs if p["relation"] == "NESTED"]
    notindep = [p for p in pairs if p["relation"] == "NOT INDEPENDENT"]
    print(f"\n[independence] {len(nested_pairs)} NESTED pairs, {len(notindep)} NOT-INDEPENDENT "
          f"pairs of {len(pairs)}")
    for p in nested_pairs + notindep:
        print(f"    {p['a']:>3} x {p['b']:<3} lift={p['lift']:8.3f} phi={p['phi']:+.3f}  "
              f"{p['relation']}")
    # effective property count: collapse NESTED chains
    parent = {i: i for i in range(11)}
    def find(i):
        while parent[i] != i:
            parent[i] = parent[parent[i]]
            i = parent[i]
        return i
    for p in nested_pairs:
        a, b = PROP_IDS.index(p["a"]), PROP_IDS.index(p["b"])
        ra, rb = find(a), find(b)
        if ra != rb:
            parent[rb] = ra
    n_effective = len({find(i) for i in range(11)})

    # ---- RT-2 (tripartite taxonomy) ------------------------------------------------
    bay_obs = int(x_coords[CIX["bayniyya"]])
    rik_obs = 14 - int(x_coords[CIX["shadida"]]) - bay_obs
    rt2_fail = {"bayniyya": {"size": 5, "in_set": bay_obs, "floor_window": [2, 3],
                             "satisfied": bay_obs in (2, 3)},
                "rikhw": {"size": 15, "in_set": rik_obs, "floor_window": [7, 8],
                          "satisfied": rik_obs in (7, 8)}}
    assert not rt2_fail["bayniyya"]["satisfied"] and not rt2_fail["rikhw"]["satisfied"], (
        "pre-reg §2 pre-declared that both RT-2 extra balance properties FAIL on the "
        "attested set; they do not — the pre-declaration was wrong and must be published")
    print(f"\n[RT-2] tripartite taxonomy: attested takes {bay_obs}/5 bayniyya and "
          f"{rik_obs}/15 rikhw — BOTH extra balance properties FAIL on the attested set, "
          f"exactly as pre-declared (pre-reg §2)")

    aggregate = {
        "RT-1b_T-A": {"D_obs": 1.0, "n": n_DA, "p": n_DA / N_SUBSETS},
        "RT-2b_T-C": {"D_obs": 6.0, "n": n_DC, "p": n_DC / N_SUBSETS},
    }
    code_all = np.zeros(C.shape[0], dtype=np.int32)
    for t_ in range(11):
        code_all |= I[:, t_].astype(np.int32) << t_
    for lbl, D, dobs in (("RT-1b_T-A", DA, 1.0), ("RT-2b_T-C", DC, 6.0)):
        keep = D <= dobs + 1e-9
        for others, name in ((list(range(5, 11)), "with_P6_P11"),
                             ([5, 6, 7], "with_P6_P8_only")):
            m = 0
            for t_ in others:
                m |= 1 << t_
            sel = keep & ((code_all & m) == m)
            aggregate[lbl][name] = {"n": int(counts[sel].sum()),
                                    "p": float(counts[sel].sum()) / N_SUBSETS}
        print(f"[{lbl}] D<={dobs}: n={aggregate[lbl]['n']:,} "
              f"| + P6..P11: n={aggregate[lbl]['with_P6_P11']['n']:,} "
              f"| + P6,P7,P8: n={aggregate[lbl]['with_P6_P8_only']['n']:,}")

    # ---- THE CRITICAL CONTROL ------------------------------------------------------
    medians = {n: weighted_median(C[:, CIX[n]].astype(np.float64), counts)
               for n in ("top14", "sonorant", "dotless", "pharyngeal")}
    medians["maxjaccard"] = weighted_median(mj, counts)
    print(f"\n[control] null medians: {medians}")

    control = {}
    for variant, self_dir in (("Control-1_direction_locked", False),
                              ("Control-2_self_directed_PRIMARY", True)):
        W_obs_ctrl, _ = profile_survivors(keys, C, massbit, mj, counts, x_coords,
                                          x_mass > 0.50, mjx, medians, self_dir)
        per_seed = {}
        for sd in (SEED, SEED_REPLICATION):
            rr = random.Random(sd)
            Ws, nprops_declared = [], []
            for _ in range(N_CONTROL):
                R = set(rr.sample(ALPHABET28, 14))
                rc = np.array(coords_of(R, classes), dtype=np.int32)
                rmass = sum(freq[c] for c in R) / H1810_TOTAL
                Cr = rc.reshape(1, -1).astype(np.int8)
                Ir, mjr = declared_indicators(Cr, np.array([rmass > 0.50]), Gsizes)
                w_r, _ = profile_survivors(keys, C, massbit, mj, counts, rc, rmass > 0.50,
                                           mjr, medians, self_dir)
                Ws.append(w_r)
                nprops_declared.append(int(Ir.sum()))
            Wa = np.array(Ws, dtype=np.int64)
            q = float((Wa <= W_obs_ctrl).sum()) / N_CONTROL
            per_seed[str(sd)] = {
                "q_frac_random_at_least_as_unique": q,
                "n_random_le_W_obs": int((Wa <= W_obs_ctrl).sum()),
                "W_random_min": int(Wa.min()), "W_random_q1": float(np.percentile(Wa, 25)),
                "W_random_median": float(np.median(Wa)),
                "W_random_q3": float(np.percentile(Wa, 75)), "W_random_max": int(Wa.max()),
                "W_random_mean": float(Wa.mean()),
                "n_random_with_W_eq_1": int((Wa == 1).sum()),
                "n_random_with_W_le_10": int((Wa <= 10).sum()),
                "n_random_with_W_le_100": int((Wa <= 100).sum()),
                "declared_props_satisfied_mean": float(np.mean(nprops_declared)),
                "declared_props_satisfied_max": int(np.max(nprops_declared)),
                "declared_props_satisfied_hist": np.bincount(
                    np.array(nprops_declared), minlength=12).tolist(),
            }
            print(f"  [{variant} seed {sd}] W_obs={W_obs_ctrl:,}  "
                  f"q={q:.3f}  random W: min={Wa.min():,} med={np.median(Wa):,.0f} "
                  f"max={Wa.max():,}  #(W_r=1)={int((Wa==1).sum())}")
        control[variant] = {"W_obs_under_control_rule": W_obs_ctrl, "by_seed": per_seed}

    q_primary = control["Control-2_self_directed_PRIMARY"]["by_seed"][str(SEED)][
        "q_frac_random_at_least_as_unique"]
    control_verdict = "CONTROL-PASSED" if q_primary < 0.05 else "CONTROL-FAILED"

    # ---- LOCKED VERDICT (pre-reg §7) ------------------------------------------------
    if W == 0:
        final = "PRE-COMMIT VIOLATION (W=0)"
    elif W > 100:
        final = "CONJUNCTION-ADDS-NOTHING"
    elif control_verdict == "CONTROL-FAILED":
        final = "ARTEFACT-OF-CONSTRAINT-STACKING"
    elif W == 1:
        final = "JOINT-CONJUNCTION-REMARKABLE"
    else:
        final = "JOINT-CONJUNCTION-NEAR-UNIQUE"
    print(f"\n[VERDICT] W={W:,}  control={control_verdict} (q={q_primary:.3f})  -> {final}")

    # ---- stdlib guard ----------------------------------------------------------------
    t = time.time()
    g5, g11 = stdlib_guard(classes, freq, Gsizes, G)
    assert g5 == n_bal, f"stdlib guard P1..P5 {g5} != {n_bal}"
    assert g11 == W, f"stdlib guard joint {g11} != {W}"
    print(f"[guard] stdlib-only independent enumeration agrees: P1..P5={g5:,}, joint={g11:,} "
          f"({time.time()-t:.1f}s)")

    payload = {
        "finding_id": "H-NEW-2670",
        "title": "Joint conjunction improbability: the muqattaat-14 under ALL declared "
                 "constraints simultaneously",
        "date": "2026-08-07", "author": "Waiel Al-Shujaa",
        "run_utc": stamp, "run_dir": os.path.relpath(run_dir, ROOT),
        "prereg_sha256": prereg_sha, "frozen_inputs": FROZEN_INPUTS,
        "seed": SEED, "seed_replication": SEED_REPLICATION,
        "n_subsets_exact": N_SUBSETS, "n_distinct_profiles": int(keys.size),
        "muqattaat": {"n_loci": len(loci), "n_surahs": len(surahs), "surahs": surahs,
                      "letters": muq14, "mass_share": x_mass,
                      "coords": {n: int(x_coords[CIX[n]]) for n in CIX},
                      "max_jaccard": float(mjx[0])},
        "zamakhshari_stated_counts": zam,
        "declared_properties": marginals,
        "naive_independence_product_p": naive,
        "naive_independence_product_n": naive * N_SUBSETS,
        "joint": {"W_all_11": W, "p_exact_fraction": f"{W}/{N_SUBSETS}",
                  "p_exact": W / N_SUBSETS,
                  "W_mw7_capped_P1_P8": W8, "p_mw7_capped": W8 / N_SUBSETS,
                  "P1_P5_balance_block": n_bal},
        "shrinkage_curves": curves,
        "independence_matrix": pairs,
        "independence_summary": {"n_nested": len(nested_pairs),
                                 "n_not_independent": len(notindep),
                                 "effective_property_count": n_effective,
                                 "naive_vs_true_ratio": (naive * N_SUBSETS / W) if W else None},
        "rt2_tripartite": {"extra_balance_properties": rt2_fail,
                           "note": "both FAIL on the attested set, as pre-declared"},
        "aggregate_balance_arms": aggregate,
        "control": {"null_medians": medians, "variants": control,
                    "q_primary": q_primary, "control_verdict": control_verdict},
        "verdict": final,
        "runtime_seconds": round(time.time() - t0, 1),
    }
    os.makedirs(os.path.dirname(OUT_JSON), exist_ok=True)
    for p in (OUT_JSON, os.path.join(run_dir, "h-new-2670.json")):
        with open(p, "w", encoding="utf-8") as fh:
            json.dump(payload, fh, ensure_ascii=False, indent=2)
    with open(os.path.join(run_dir, "script.sha256"), "w") as fh:
        fh.write(_sha256(os.path.abspath(__file__)) + "  h-new-2670.py\n")
    print(f"\n[done] {OUT_JSON}\n[done] {run_dir}  ({time.time()-t0:.1f}s total)")


if __name__ == "__main__":
    main()
