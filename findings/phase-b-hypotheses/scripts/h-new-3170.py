#!/usr/bin/env python3
"""
H-NEW-3170 (frontier item F-19) -- Does the Buckwalter-style transliteration carry
phoneme-level information the vocalised Arabic text does not?

Pre-registration: findings/phase-b-hypotheses/prereg-h-new-3170-phoneme-level.md
Locked SHA-256 embedded below; verified at runtime; mismatch => SystemExit.

Cells:
  D1  executability  -- does the muqattaat 8/10 statistic read any corpus text?
  D2  addition       -- H(T|A) = 0 ?
  D3  loss           -- H(A|T) > 0 ?, per-consonant merger partition
  D6  what P adds    -- gemination and vowel-length rates (undefined under G)
  C4  targeted loss  -- is the destroyed contrast concentrated on mustaliya u halq?
  C5  surah-level    -- rho_sonorant(P,T) - rho_mustaliya(P,T) > 0, three length channels

Seed 20260509, n_perm 10000, k_confirmatory 2, alpha_bon 0.025.
"""
from __future__ import annotations

import ast
import hashlib
import itertools
import json
import math
import os
import platform
import random
import re
import subprocess
import sys
import unicodedata
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path

REPO = Path("/Users/grey/Downloads/quran")
PREREG = REPO / "findings/phase-b-hypotheses/prereg-h-new-3170-phoneme-level.md"
EXPECTED_PREREG_SHA = "26f7807fc50df71195e2982bdb441dccf3f7ca22a1ea711d8dcb7a3d382fae16"

SEED = 20260509
N_PERM = 10000
K_CONFIRMATORY = 2
ALPHA_BON = 0.025
EXACT_ENUM_CAP = 10_000_000
TIE_FRACTION_TRIGGER = 0.50


def sha256_file(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()


def say(m: str) -> None:
    print(m, flush=True)


def die(m: str) -> None:
    raise SystemExit("FATAL: " + m)


# ======================================================================================
# GATE S8 -- before anything else exists
# ======================================================================================
_sha = sha256_file(PREREG)
if _sha != EXPECTED_PREREG_SHA:
    die(f"pre-registration SHA mismatch\n  expected {EXPECTED_PREREG_SHA}\n  actual   {_sha}")
say(f"[S8-OK] pre-registration locked: {_sha}")

# ======================================================================================
# GATE S9 -- immutable run directory
# ======================================================================================
UTC = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H%M%SZ")
RUN = REPO / "findings/phase-b-hypotheses/runs/h-new-3170" / UTC
os.makedirs(RUN, exist_ok=False)
say(f"[S9-OK] immutable run dir: {RUN}")

LOG_LINES: list[str] = []


def log(m: str) -> None:
    LOG_LINES.append(m)
    say(m)


# ======================================================================================
# 1. The phonemiser -- PORTED VERBATIM from findings/phase-b-hypotheses/scripts/h-new-2990.py
#    section 1 (`normalize`, `phonemes` and their constant tables), which itself declares its
#    port from h-new-2870.py sections 1-2. NO parameter is changed. TANWIN_REMAP is the
#    REPAIRED mapping required by AUDIT-TANWIN-DELETION-2690 section 4: it REMAPS
#    U+0657 / U+065E / U+0656 to fathatan / dammatan / kasratan rather than dropping them.
#    Citation form only (`apply_convention` is NOT ported; no pausal rule is applied), per
#    pre-registration section 2 which names exactly `normalize` and `phonemes`.
# ======================================================================================
FATHA, DAMMA, KASRA = "َ", "ُ", "ِ"
FATHATAN, DAMMATAN, KASRATAN = "ً", "ٌ", "ٍ"
SHADDA, SUKUN = "ّ", "ْ"
SUP_ALEF = "ٰ"
ALEF, WAW, YA = "ا", "و", "ي"
ALEF_MAQ, ALEF_MADDA, ALEF_WASLA = "ى", "آ", "ٱ"
TA_MARBUTA = "ة"
SHORT = {FATHA: "a", DAMMA: "u", KASRA: "i"}
TANWIN = {FATHATAN: "an", DAMMATAN: "un", KASRATAN: "in"}
CONS = set("ءآأؤإئابةتثجحخدذرزسشصضطظعغفقكلمنهوىيٱ")

TANWIN_REMAP = {"ٗ": FATHATAN, "ٞ": DAMMATAN, "ٖ": KASRATAN}

DROP = set("ـۖۗۘۙۚۛۜ۞۟۠"
           "ۣۧۨ۩۪ۭ۫۬"
           "ٕٜٟٓٔ٘ٙٚٛٝ"
           "۝ࣰࣱࣲ")
SUKUN_ALT, SMALL_WAW, SMALL_YA = "ۡ", "ۥ", "ۦ"


def normalize(t: str) -> str:
    t = unicodedata.normalize("NFC", t)
    t = "".join(TANWIN_REMAP.get(c, c) for c in t)          # h-new-2870 prereg 4.1
    t = "".join(c for c in t if c not in DROP)
    t = t.replace(SUKUN_ALT, SUKUN).replace(SMALL_WAW, WAW).replace(SMALL_YA, YA)
    t = t.replace(ALEF_MADDA, "أ" + FATHA + ALEF).replace(ALEF_WASLA, ALEF)
    t = re.sub(ALEF + FATHA, FATHA + ALEF, t)
    t = re.sub("([" + FATHA + DAMMA + KASRA + FATHATAN + DAMMATAN + KASRATAN + "])"
               + SHADDA, SHADDA + r"\1", t)
    return t


def phonemes(word: str):
    """(kind, value, src); kind in C/V/VV. Verbatim port of h-new-2990.py."""
    out, i = [], 0
    w = normalize(word)
    while i < len(w):
        ch = w[i]
        if ch in CONS:
            nxt = w[i + 1] if i + 1 < len(w) else ""
            if out and out[-1][0] == "V":
                pv = out[-1][1]
                if (ch in (ALEF, ALEF_MAQ) and pv == "a") \
                   or (ch == WAW and pv == "u" and nxt not in SHORT and nxt != SHADDA
                       and nxt not in TANWIN) \
                   or (ch == YA and pv == "i" and nxt not in SHORT and nxt != SHADDA
                       and nxt not in TANWIN):
                    out[-1] = ("VV", pv, out[-1][2])
                    i += 1
                    if i < len(w) and w[i] == SUKUN:
                        i += 1
                    continue
            src = "ta" if ch == TA_MARBUTA else ""
            out.append(("C", ch, src)); i += 1
            if i < len(w) and w[i] == SHADDA:
                out.append(("C", ch, src)); i += 1
            if i < len(w) and w[i] == SUP_ALEF:
                out.append(("VV", "a", "")); i += 1; continue
            if i < len(w) and w[i] in SHORT:
                out.append(("V", SHORT[w[i]], "")); i += 1
            elif i < len(w) and w[i] in TANWIN:
                v = TANWIN[w[i]]
                tag = "tanwin-" + v[0]
                out.append(("V", v[0], tag)); out.append(("C", "ن", tag)); i += 1
                if v[0] == "a" and i < len(w) and w[i] in (ALEF, ALEF_MAQ):
                    i += 1
            elif i < len(w) and w[i] == SUKUN:
                i += 1
        elif ch == SUP_ALEF:
            out.append(("VV", "a", "")); i += 1
        else:
            i += 1
    return out


# ======================================================================================
# 2. Classical sets -- verbatim from the sources already used by H-NEW-165 / H-NEW-2550.
#    NO new hand assignment (pre-registration section 3.3 and section 7).
# ======================================================================================
MUSTALIYA = set("خصضطظغق")            # al-Suyuti, al-Itqan, huruf al-isti'la' (7)
HALQ = set("ءهعحغخ")                   # al-Khalil, Kitab al-Ayn, huruf al-halq (6)
TARGET = MUSTALIYA | HALQ              # 13 distinct letters (ghayn and kha' in both)
SONORANT = set("منلروي")               # m n l r w y

# The 28 huruf al-mu'jam, canonical order -- the inventory named in the pre-registration
# ("each of the 28 Arabic consonants") and in H-NEW-2550's rules-tuple.
ALPHABET28 = list("ابتثجحخدذرزسشصضطظعغفقكلمنهوي")
assert len(ALPHABET28) == 28 and len(set(ALPHABET28)) == 28

# Hamza carriers and alef variants normalise onto members of the 28.
# NOTE, declared: hamza-on-the-line (U+0621) is NOT one of the 28 and is normalised to
# alef, following the same collapse already applied to its carriers. Consequence: hamza
# cannot be scored as a halq member in C4. This is CONSERVATIVE for the locked direction --
# hamza is heavily merged by the romanisation, so excluding it can only LOWER F_obs.
CARRIER_NORM = {"أ": "ا", "إ": "ا", "آ": "ا", "ٱ": "ا", "ؤ": "و", "ئ": "ي",
                "ء": "ا", "ى": "ي", "ة": "ه"}

DIAC_RE = re.compile("[ؐ-ًؚ-ٰٟۖ-ۭـ]")

# placeholder for the minimal-pair wildcard key; cannot collide with an Arabic character
WILDCARD = "\uFFFF"


def skeleton(word: str) -> str:
    w = unicodedata.normalize("NFC", word)
    w = DIAC_RE.sub("", w)
    return "".join(CARRIER_NORM.get(c, c) for c in w)


# ======================================================================================
# 3. Load, keyed by `id` -- GATE S1
# ======================================================================================
def load_by_id(rel: str):
    raw = json.loads((REPO / rel).read_text(encoding="utf-8"))
    return raw, {s["id"]: s for s in raw}


T_raw, T = load_by_id("quran-text/quran-transliteration.json")
A_raw, A = load_by_id("quran-text/quran-full-tashkeel.json")
G_raw, G = load_by_id("quran-text/quran-no-tashkeel.json")

t_order = [s["id"] for s in T_raw]
S1 = {
    "translit_list_order_is_sorted": t_order == sorted(t_order),
    "translit_list_order": t_order,
    "position_of_surah_13": t_order.index(13),
    "n_surahs": {"T": len(T), "A": len(A), "G": len(G)},
    "n_verses": {k: sum(len(s["verses"]) for s in d.values()) for k, d in
                 (("T", T), ("A", A), ("G", G))},
}
if S1["translit_list_order_is_sorted"]:
    die("S1: transliteration list order is sorted -- reconnaissance R1 not reproduced; "
        "the id-keying gate cannot be demonstrated. Run void.")
if not (len(T) == len(A) == len(G) == 114):
    die("S1: surah count != 114 after id keying")
if not all(v == 6236 for v in S1["n_verses"].values()):
    die(f"S1: verse totals != 6236 : {S1['n_verses']}")
for sid in range(1, 115):
    if not (len(T[sid]["verses"]) == len(A[sid]["verses"]) == len(G[sid]["verses"])):
        die(f"S1: verse-count mismatch at surah {sid} after id keying")
S1["verdict"] = "PASS"
log(f"[S1-OK] id-keyed: 114 surahs, 6236 verses on all three sides; "
    f"transliteration list order scrambled (surah 13 at position {S1['position_of_surah_13']})")

# ---- GATE S2: tanwin repair -------------------------------------------------------
probe = "مٖمٗمٞ"
probe_n = normalize(probe)
tanwin_total = 0
for sid in range(1, 115):
    for v in A[sid]["verses"]:
        n = normalize(v["text"])
        tanwin_total += sum(n.count(c) for c in TANWIN)
S2 = {
    "probe_survives": all(c in probe_n for c in (FATHATAN, DAMMATAN, KASRATAN)),
    "corpus_tanwin_after_normalize": tanwin_total,
    "audit_expected_min": 8000,
    "defective_instrument_would_give": 1911,
}
if not S2["probe_survives"]:
    die("S2: TANWIN_REMAP did not survive normalize()")
if tanwin_total < 8000:
    die(f"S2: corpus tanwin after normalize = {tanwin_total} < 8000 -- "
        "the tanwin-deletion defect is present. Run void.")
S2["verdict"] = "PASS"
log(f"[S2-OK] tanwin repair active: {tanwin_total} tanwin survive normalisation "
    f"(defective instrument yields 1911)")

# ---- GATE S3: waqf -----------------------------------------------------------------
WAQF = set(chr(c) for c in range(0x06D6, 0x06DD))
waqf_surviving_P = 0
waqf_surviving_T = 0
for sid in range(1, 115):
    for v in A[sid]["verses"]:
        waqf_surviving_P += sum(1 for c in normalize(v["text"]) if c in WAQF)
    for v in T[sid]["verses"]:
        waqf_surviving_T += sum(1 for c in v["text"] if c in WAQF)
S3 = {"waqf_in_P_stream": waqf_surviving_P, "waqf_in_T_stream": waqf_surviving_T}
if waqf_surviving_P or waqf_surviving_T:
    die(f"S3: waqf codepoints survive: P={waqf_surviving_P} T={waqf_surviving_T}")
S3["verdict"] = "PASS"
log("[S3-OK] zero waqf codepoints survive into P or T")


# ======================================================================================
# 4. D1 -- EXECUTABILITY AUDIT of the muqattaat 8/10 pipeline
# ======================================================================================
D1_SCRIPTS = [
    "scripts/h_new_165_phonological_predictor.py",
    "scripts/h_new_232_oq1_singleton.py",
    "scripts/h_new_301_minimal_2feature_singleton.py",
]
READ_FUNCS = {"open", "load", "loads", "read_text", "read_bytes", "loadtxt",
              "genfromtxt", "read_csv", "reader", "DictReader"}
CORPUS_HINTS = ("quran-text", "quran-flat", "alt-text", "morphology", "baseline-corpora",
                "data/", "quran_")

d1_rows = []
for rel in D1_SCRIPTS:
    p = REPO / rel
    src = p.read_text(encoding="utf-8")
    tree = ast.parse(src)
    reads, writes = [], []
    for node in ast.walk(tree):
        if not isinstance(node, ast.Call):
            continue
        fn = node.func
        name = fn.attr if isinstance(fn, ast.Attribute) else (fn.id if isinstance(fn, ast.Name) else None)
        if name not in READ_FUNCS:
            continue
        mode = None
        for a in list(node.args) + [k.value for k in node.keywords if k.arg == "mode"]:
            if isinstance(a, ast.Constant) and isinstance(a.value, str) and \
               a.value in ("r", "w", "x", "a", "rb", "wb", "xb", "ab"):
                mode = a.value
        line = ast.get_source_segment(src, node) or ""
        (writes if (mode and mode[0] in "wxa") else reads).append(
            {"line": node.lineno, "call": name, "mode": mode, "src": line[:120]})
    corpus_refs = sorted({h for h in CORPUS_HINTS if h in src})
    d1_rows.append({
        "script": rel,
        "sha256": sha256_file(p),
        "read_calls": reads,
        "write_calls": writes,
        "n_read_calls": len(reads),
        "corpus_path_substrings_present": corpus_refs,
    })

d1_total_reads = sum(r["n_read_calls"] for r in d1_rows)
d1_corpus_hits = sum(len(r["corpus_path_substrings_present"]) for r in d1_rows)
# Prereg 5.1: "zero corpus-text reads". A script with ZERO read-mode file calls reads
# nothing, whatever strings appear in its comments, so the read-call count is the
# operative test; the path-substring count is reported as a diagnostic only.
D1_PASS = (d1_total_reads == 0)
log(f"[D1] muqattaat pipeline: {d1_total_reads} read-mode file calls, "
    f"{d1_corpus_hits} corpus path substrings across {len(D1_SCRIPTS)} scripts "
    f"-> {'reads NO corpus text' if D1_PASS else 'READS TEXT'}")


# ======================================================================================
# 5. Token alignment -- GATE S4
# ======================================================================================
pairs = []                       # (arabic_full_tashkeel_word, latin_word)
excluded_tokens = 0
excluded_verses = 0
total_T_tokens = 0
for sid in range(1, 115):
    for va, vt in zip(A[sid]["verses"], T[sid]["verses"]):
        la, lt = va["text"].split(), vt["text"].split()
        total_T_tokens += len(lt)
        if len(la) == len(lt):
            pairs.extend(zip(la, lt))
        else:
            excluded_verses += 1
            excluded_tokens += len(lt)
S4 = {
    "aligned_token_pairs": len(pairs),
    "excluded_verses": excluded_verses,
    "excluded_tokens": excluded_tokens,
    "total_T_tokens": total_T_tokens,
    "excluded_fraction": excluded_tokens / total_T_tokens,
    "limit": 0.01,
}
S4["verdict"] = "PASS" if S4["excluded_fraction"] <= 0.01 else "FAIL"
log(f"[S4] aligned {len(pairs)} token pairs; excluded {excluded_verses} verses / "
    f"{excluded_tokens} tokens = {S4['excluded_fraction']:.4%} -> {S4['verdict']}")
if S4["verdict"] != "PASS":
    log("[S4] NOTE: exceeds the 1% limit. Per prereg section 6 this VOIDS the run.")


# ======================================================================================
# 6. D2 -- ADDITION.  H(T|A) under two declared case variants.
# ======================================================================================
AYN_SENTINEL = "ǀ"


def fold(t: str) -> str:
    return t.replace("AA", AYN_SENTINEL).lower().replace(AYN_SENTINEL.lower(), AYN_SENTINEL)


def cond_entropy(joint: dict) -> float:
    """H(Y|X) in bits from a dict {x: Counter(y)}."""
    n = sum(sum(c.values()) for c in joint.values())
    h = 0.0
    for x, cy in joint.items():
        nx = sum(cy.values())
        for y, nxy in cy.items():
            h -= (nxy / n) * math.log2(nxy / nx)
    return h


d2 = {}
for vname, fn in (("V-case", lambda s: s), ("V-fold", fold)):
    a2t = defaultdict(Counter)
    for a, t in pairs:
        a2t[a][fn(t)] += 1
    amb = {k: v for k, v in a2t.items() if len(v) > 1}
    d2[vname] = {
        "n_arabic_types": len(a2t),
        "arabic_types_with_multiple_latin_images": len(amb),
        "token_mass_ambiguous": sum(sum(v.values()) for v in amb.values()),
        "H_T_given_A_bits": cond_entropy(a2t),
        "examples": [[k, dict(v)] for k, v in
                     sorted(amb.items(), key=lambda kv: -sum(kv[1].values()))[:12]],
    }
# worse = larger H(T|A)
d2_worse = max(d2, key=lambda k: d2[k]["H_T_given_A_bits"])
D2_PASS = (d2[d2_worse]["H_T_given_A_bits"] == 0.0)
d2["headline_variant"] = d2_worse
d2["variants_agree"] = (d2["V-case"]["H_T_given_A_bits"] == 0.0) == \
                       (d2["V-fold"]["H_T_given_A_bits"] == 0.0)
log(f"[D2] H(T|A): V-case = {d2['V-case']['H_T_given_A_bits']:.6f} bits, "
    f"V-fold = {d2['V-fold']['H_T_given_A_bits']:.6f} bits; headline {d2_worse} "
    f"-> {'ADDS NOTHING' if D2_PASS else 'ADDS SOMETHING'}")


# ======================================================================================
# 7. D3 -- LOSS.  H(A|T) under three declared Arabic reference forms.
# ======================================================================================
def phonemic_form(w: str) -> str:
    return "".join(k + str(v) for k, v, _ in phonemes(w))


ref_forms = {
    "A1_full_tashkeel": lambda w: unicodedata.normalize("NFC", w),
    "A2_phonemic": phonemic_form,
    "A3_skeleton": skeleton,
}
d3 = {}
for rname, rf in ref_forms.items():
    t2a = defaultdict(Counter)
    for a, t in pairs:
        t2a[t][rf(a)] += 1
    amb = {k: v for k, v in t2a.items() if len(v) > 1}
    d3[rname] = {
        "n_latin_types": len(t2a),
        "latin_types_with_multiple_arabic_preimages": len(amb),
        "token_mass_ambiguous": sum(sum(v.values()) for v in amb.values()),
        "H_A_given_T_bits": cond_entropy(t2a),
        "examples": [[k, dict(v)] for k, v in
                     sorted(amb.items(), key=lambda kv: -sum(kv[1].values()))[:12]],
    }
# "best (most favourable to T)" = smallest H(A|T)
d3_best = min(d3, key=lambda k: d3[k]["H_A_given_T_bits"])
d3_worst = max(d3, key=lambda k: d3[k]["H_A_given_T_bits"])
D3_PASS = (d3[d3_best]["H_A_given_T_bits"] > 0.0)
d3["headline_variant_worst"] = d3_worst
d3["decision_variant_best_for_T"] = d3_best
log("[D3] H(A|T): " + ", ".join(f"{k} = {v['H_A_given_T_bits']:.4f} bits"
                                for k, v in d3.items() if isinstance(v, dict)))
log(f"[D3] most favourable to T is {d3_best} -> {'LOSSY' if D3_PASS else 'LOSSLESS'}")


# ======================================================================================
# 8. Merger partition -- minimal-pair contrast test, theta swept {0.25, 0.50, 0.75}
# ======================================================================================
skel2lat = defaultdict(Counter)
for a, t in pairs:
    skel2lat[skeleton(a)][t] += 1

# corpus consonant token frequency, measured on the P stream (the phonological object)
cons_freq = Counter()
for sid in range(1, 115):
    for v in A[sid]["verses"]:
        for w in v["text"].split():
            for k, val, _ in phonemes(w):
                if k == "C":
                    cons_freq[CARRIER_NORM.get(val, val)] += 1

# minimal pairs on the skeleton
wildcard = defaultdict(list)
for s in skel2lat:
    for i, ch in enumerate(s):
        wildcard[(s[:i] + WILDCARD + s[i + 1:])].append((i, ch, s))

pair_stats = defaultdict(lambda: {"total": 0, "destroyed": 0, "n_items": 0, "examples": []})
for key, group in wildcard.items():
    if len(group) < 2:
        continue
    for (i1, c1, s1), (i2, c2, s2) in itertools.combinations(group, 2):
        if c1 == c2 or c1 not in ALPHABET28 or c2 not in ALPHABET28:
            continue
        k = tuple(sorted((c1, c2)))
        m1, m2 = skel2lat[s1], skel2lat[s2]
        mass = sum(m1.values()) + sum(m2.values())
        shared = set(m1) & set(m2)
        st = pair_stats[k]
        st["total"] += mass
        st["n_items"] += 1
        if shared:
            st["destroyed"] += mass
            if len(st["examples"]) < 4:
                st["examples"].append([s1, s2, sorted(shared)[:2]])

pair_table = {}
for k, st in pair_stats.items():
    frac = st["destroyed"] / st["total"] if st["total"] else 0.0
    pair_table["+".join(k)] = {"destroyed_fraction": frac, **{kk: vv for kk, vv in st.items()
                                                              if kk != "examples"},
                               "examples": st["examples"]}

THETAS = [0.25, 0.50, 0.75]
merger_by_theta = {}
for theta in THETAS:
    merged_pairs = [k for k, v in pair_table.items() if v["destroyed_fraction"] >= theta]
    merged_cons = sorted({c for k in merged_pairs for c in k.split("+")})
    # ---- GATE S5: strata homogeneity ------------------------------------------------
    inhomog = []
    for k in merged_pairs:
        x, y = k.split("+")
        # per-consonant recoverability = 1 - (destroyed mass over all pairs it joins)
        def rec(c):
            tot = sum(pair_table[p]["total"] for p in pair_table if c in p.split("+"))
            des = sum(pair_table[p]["destroyed"] for p in pair_table if c in p.split("+"))
            return 1.0 - (des / tot if tot else 0.0)
        rx, ry = rec(x), rec(y)
        if (rx >= 0.95 and ry <= 0.05) or (ry >= 0.95 and rx <= 0.05):
            inhomog.append({"pair": k, "recoverability": [rx, ry]})
    kept = [k for k in merged_pairs if k not in {d["pair"] for d in inhomog}]
    kept_cons = sorted({c for k in kept for c in k.split("+")})
    merger_by_theta[str(theta)] = {
        "merged_pairs_raw": merged_pairs,
        "S5_inhomogeneous_excluded": inhomog,
        "merged_pairs_kept": kept,
        "merged_consonants": kept_cons,
        "n_merged_consonants": len(kept_cons),
        "in_target": sorted(set(kept_cons) & TARGET),
        "in_sonorant": sorted(set(kept_cons) & SONORANT),
    }
    log(f"[D3/theta={theta}] merged pairs {len(merged_pairs)} "
        f"(S5 excluded {len(inhomog)}), merged consonants {len(kept_cons)}: "
        f"{''.join(kept_cons)}  | in target set: {''.join(sorted(set(kept_cons) & TARGET))}")


# ======================================================================================
# 9. C4 -- targeted loss.  Permutation + exact, frequency-stratified.
# ======================================================================================
def freq_quartiles(cons_list):
    ranked = sorted(cons_list, key=lambda c: cons_freq.get(c, 0))
    q = {}
    n = len(ranked)
    for i, c in enumerate(ranked):
        q[c] = min(3, (i * 4) // n)
    return q


QUART = freq_quartiles(ALPHABET28)


def F_stat(merged):
    tot = sum(cons_freq.get(c, 0) for c in merged)
    if tot == 0:
        return 0.0
    return sum(cons_freq.get(c, 0) for c in merged if c in TARGET) / tot


def run_C4(theta_key):
    merged = merger_by_theta[theta_key]["merged_consonants"]
    if not merged:
        return {"status": "NO-MERGED-CONSONANTS", "F_obs": None}
    F_obs = F_stat(merged)
    by_q = defaultdict(list)
    for c in ALPHABET28:
        by_q[QUART[c]].append(c)
    need = Counter(QUART[c] for c in merged)

    # exact enumeration size
    n_exact = 1
    for q, k in need.items():
        n_exact *= math.comb(len(by_q[q]), k)
    rng = random.Random(SEED)
    nulls = []
    for _ in range(N_PERM):
        pick = []
        for q, k in need.items():
            pick.extend(rng.sample(by_q[q], k))
        nulls.append(F_stat(pick))
    ge = sum(1 for x in nulls if x >= F_obs - 1e-12)
    eq = sum(1 for x in nulls if abs(x - F_obs) < 1e-12)
    p_perm = (1 + ge) / (1 + N_PERM)
    tie_fraction = eq / N_PERM

    exact = None
    if n_exact <= EXACT_ENUM_CAP:
        combos = [list(itertools.combinations(by_q[q], k)) for q, k in sorted(need.items())]
        tot = 0
        ge_e = 0
        eq_e = 0
        vals = []
        for combo in itertools.product(*combos):
            pick = [c for part in combo for c in part]
            f = F_stat(pick)
            vals.append(f)
            tot += 1
            if f >= F_obs - 1e-12:
                ge_e += 1
            if abs(f - F_obs) < 1e-12:
                eq_e += 1
        exact = {"n_configurations": tot, "p_exact": ge_e / tot,
                 "tie_fraction_exact": eq_e / tot,
                 "null_mean": sum(vals) / tot,
                 "null_min": min(vals), "null_max": max(vals)}
    governing = "exact" if (tie_fraction > TIE_FRACTION_TRIGGER and exact) else "permutation"
    p_used = exact["p_exact"] if governing == "exact" else p_perm
    null_median = sorted(nulls)[N_PERM // 2]
    return {
        "status": "OK", "theta": theta_key,
        "merged_consonants": merged,
        "F_obs": F_obs,
        "null_mean_perm": sum(nulls) / N_PERM,
        "null_median_perm": null_median,
        "null_min_perm": min(nulls), "null_max_perm": max(nulls),
        "p_perm": p_perm, "tie_fraction": tie_fraction,
        "tie_trigger": TIE_FRACTION_TRIGGER,
        "n_exact_configurations": n_exact,
        "exact": exact,
        "governing_test": governing,
        "p_used": p_used,
        "S6_null_varies": (max(nulls) > min(nulls)),
        "nulls": nulls,
    }


C4_by_theta = {th: run_C4(th) for th in merger_by_theta}
# headline = worst (largest p_used) over the declared theta sweep
C4_valid = {k: v for k, v in C4_by_theta.items() if v.get("status") == "OK"}
if C4_valid:
    C4_head_key = max(C4_valid, key=lambda k: C4_valid[k]["p_used"])
    C4 = C4_valid[C4_head_key]
    S6_PASS = C4["S6_null_varies"]
    C4_PASS = (C4["p_used"] < ALPHA_BON) and (C4["F_obs"] > C4["null_median_perm"]) and S6_PASS
else:
    C4_head_key, C4, S6_PASS, C4_PASS = None, {"status": "NO-MERGED-CONSONANTS"}, False, False
log(f"[C4] headline theta={C4_head_key}: F_obs={C4.get('F_obs')}, "
    f"p_used={C4.get('p_used')} ({C4.get('governing_test')}), "
    f"tie_fraction={C4.get('tie_fraction')} -> {'PASS' if C4_PASS else 'FAIL'}")


# ======================================================================================
# 10. C5 -- surah-level, three length channels
# ======================================================================================
def spearman(x, y):
    def rank(v):
        order = sorted(range(len(v)), key=lambda i: v[i])
        r = [0.0] * len(v)
        i = 0
        while i < len(order):
            j = i
            while j + 1 < len(order) and v[order[j + 1]] == v[order[i]]:
                j += 1
            avg = (i + j) / 2.0 + 1
            for k in range(i, j + 1):
                r[order[k]] = avg
            i = j + 1
        return r
    rx, ry = rank(x), rank(y)
    n = len(x)
    mx, my = sum(rx) / n, sum(ry) / n
    num = sum((a - mx) * (b - my) for a, b in zip(rx, ry))
    dx = math.sqrt(sum((a - mx) ** 2 for a in rx))
    dy = math.sqrt(sum((b - my) ** 2 for b in ry))
    return num / (dx * dy) if dx and dy else 0.0


def t_classes(theta_key):
    """T-equivalence classes at a given theta. Prereg 3.4: a consonant is counted VIA its
    Latin image class, so a merged consonant's density is contaminated by its partner --
    a class counts as target iff it INTERSECTS the target set."""
    parent = {c: c for c in ALPHABET28}

    def find(c):
        while parent[c] != c:
            parent[c] = parent[parent[c]]
            c = parent[c]
        return c

    for k in merger_by_theta[theta_key]["merged_pairs_kept"]:
        x, y = k.split("+")
        rx, ry = find(x), find(y)
        if rx != ry:
            parent[rx] = ry
    cls = defaultdict(set)
    for c in ALPHABET28:
        cls[find(c)].add(c)
    class_of = {c: frozenset(cls[find(c)]) for c in ALPHABET28}
    return ({c for c in ALPHABET28 if class_of[c] & TARGET},
            {c for c in ALPHABET28 if class_of[c] & SONORANT},
            {c: sorted(class_of[c]) for c in ALPHABET28})


# phonemise once
surah_cons = {}
surah_rows = {}
for sid in range(1, 115):
    n_verses = len(A[sid]["verses"])
    n_words = sum(len(v["text"].split()) for v in A[sid]["verses"])
    cons = Counter()
    gem = vv = vshort = 0
    for v in A[sid]["verses"]:
        for w in v["text"].split():
            prev = None
            for kind, val, _ in phonemes(w):
                if kind == "C":
                    c = CARRIER_NORM.get(val, val)
                    cons[c] += 1
                    if prev == c:
                        gem += 1
                    prev = c
                else:
                    prev = None
                    if kind == "VV":
                        vv += 1
                    else:
                        vshort += 1
    surah_cons[sid] = cons
    surah_rows[sid] = {
        "n_verses": n_verses, "n_words": n_words,
        "mean_verse_len": n_words / n_verses,
        "n_cons": sum(cons.values()),
        "P_must": sum(n for c, n in cons.items() if c in TARGET),
        "P_son": sum(n for c, n in cons.items() if c in SONORANT),
        "geminate_pairs": gem, "long_vowels": vv, "short_vowels": vshort,
    }

CHANNELS = {"L1_verse_count": "n_verses", "L2_word_count": "n_words",
            "L3_mean_verse_len": "mean_verse_len"}
sids = list(range(1, 115))
C5_cells = {}
rng5 = random.Random(SEED)
for theta_key in merger_by_theta:
    T_TARGET, T_SON, CLASS_OF = t_classes(theta_key)
    tmust = {s: sum(n for c, n in surah_cons[s].items() if c in T_TARGET) for s in sids}
    tson = {s: sum(n for c, n in surah_cons[s].items() if c in T_SON) for s in sids}
    for cname, denom in CHANNELS.items():
        P_must = [surah_rows[s]["P_must"] / surah_rows[s][denom] for s in sids]
        P_son = [surah_rows[s]["P_son"] / surah_rows[s][denom] for s in sids]
        T_must = [tmust[s] / surah_rows[s][denom] for s in sids]
        T_son = [tson[s] / surah_rows[s][denom] for s in sids]
        r_must = spearman(P_must, T_must)
        r_son = spearman(P_son, T_son)
        d_obs = r_son - r_must
        nulls = []
        idx = list(range(len(sids)))
        for _ in range(N_PERM):
            perm = idx[:]
            rng5.shuffle(perm)
            nulls.append(spearman(P_son, [T_son[i] for i in perm])
                         - spearman(P_must, [T_must[i] for i in perm]))
        ge = sum(1 for x in nulls if x >= d_obs - 1e-12)
        eq = sum(1 for x in nulls if abs(x - d_obs) < 1e-12)
        dom = abs(spearman([surah_rows[s][denom] for s in sids],
                           [surah_rows[s]["P_must"] for s in sids]))
        key = f"theta={theta_key}/{cname}"
        C5_cells[key] = {
            "theta": theta_key, "channel": cname,
            "rho_mustaliya_P_T": r_must, "rho_sonorant_P_T": r_son,
            "delta_rho": d_obs,
            "p_perm": (1 + ge) / (1 + N_PERM),
            "tie_fraction": eq / N_PERM,
            "null_mean": sum(nulls) / N_PERM,
            "null_median": sorted(nulls)[N_PERM // 2],
            "null_sd": (sum((x - sum(nulls) / N_PERM) ** 2 for x in nulls) / N_PERM) ** 0.5,
            "null_min": min(nulls), "null_max": max(nulls),
            "dominance_abs_rho_channel_vs_grouping": dom,
            "T_target_class_members": {c: CLASS_OF[c] for c in sorted(T_TARGET)},
            "nulls": nulls,
        }
        log(f"[C5/{key}] rho_must={r_must:.4f} rho_son={r_son:.4f} "
            f"delta={d_obs:+.4f} p={(1 + ge) / (1 + N_PERM):.5f} "
            f"ties={eq / N_PERM:.3f} dom|rho|={dom:.4f}")

C5_head_key = min(C5_cells, key=lambda k: C5_cells[k]["delta_rho"])
C5 = C5_cells[C5_head_key]
C5_dominant = max(CHANNELS, key=lambda cn: C5_cells[f"theta=0.5/{cn}"]
                  ["dominance_abs_rho_channel_vs_grouping"])
C5_by_channel = C5_cells

# ---- GATE S7: control != treatment -------------------------------------------------
s7_rho = spearman([surah_rows[s]["P_son"] / surah_rows[s]["n_words"] for s in sids],
                  [surah_rows[s]["P_must"] / surah_rows[s]["n_words"] for s in sids])
S7 = {"rho_sonorant_vs_mustaliya": s7_rho, "limit": 0.8,
      "verdict": "PASS" if abs(s7_rho) <= 0.8 else "VOID"}
log(f"[S7] rho(sonorant, mustaliya) across 114 surahs = {s7_rho:.4f} -> {S7['verdict']}")

C5_PASS = (C5["p_perm"] < ALPHA_BON) and (C5["delta_rho"] > 0) and (S7["verdict"] == "PASS")
log(f"[C5] headline (worst) channel = {C5_head_key}: delta_rho={C5['delta_rho']:.4f} "
    f"p={C5['p_perm']:.5f} -> {'PASS' if C5_PASS else 'FAIL'}; dominant channel = {C5_dominant}")


# ======================================================================================
# 11. MDE / power / S* vs S_max -- computed unconditionally (prereg 5.4)
# ======================================================================================
def mde_and_smax(nulls, alpha, s_max, name):
    ns = sorted(nulls)
    n = len(ns)
    # S* = smallest observed value that would reject at alpha
    s_star = None
    for cand in ns:
        ge = sum(1 for x in ns if x >= cand - 1e-12)
        if (1 + ge) / (1 + n) < alpha:
            s_star = cand
            break
    if s_star is None:
        # no realised null value rejects; the threshold sits above the null's support
        s_star = ns[-1] + (ns[-1] - ns[0]) / max(n, 1)
    # exponential tilting to 80% power
    def power_at(theta):
        w = [math.exp(theta * x) for x in ns]
        z = sum(w)
        return sum(wi for wi, x in zip(w, ns) if x >= s_star - 1e-12) / z
    lo, hi = 0.0, 1.0
    for _ in range(200):
        if power_at(hi) >= 0.80:
            break
        hi *= 2
        if hi > 1e9:
            break
    for _ in range(200):
        mid = (lo + hi) / 2
        if power_at(mid) >= 0.80:
            hi = mid
        else:
            lo = mid
    theta_star = hi
    w = [math.exp(theta_star * x) for x in ns]
    z = sum(w)
    mde_mean = sum(wi * x for wi, x in zip(w, ns)) / z
    power_uniform_upper = sum(1 for x in ns if x >= s_star - 1e-12) / n
    return {
        "name": name, "alpha": alpha, "S_star": s_star, "S_max": s_max,
        "branch_UNTESTABLE_AT_THIS_N": s_star > s_max,
        "theta_star": theta_star,
        "MDE_tilted_mean": mde_mean,
        "power_against_null_at_S_star": power_uniform_upper,
        "null_mean": sum(ns) / n, "null_min": ns[0], "null_max": ns[-1],
    }


POWER = {}
if C4.get("status") == "OK":
    POWER["C4"] = mde_and_smax(C4["nulls"], ALPHA_BON, 1.0, "C4 F concentration")
POWER["C5"] = mde_and_smax(C5["nulls"], ALPHA_BON, 2.0, "C5 delta_rho")
for k, v in POWER.items():
    log(f"[POWER/{k}] S*={v['S_star']:.6f} S_max={v['S_max']} "
        f"untestable={v['branch_UNTESTABLE_AT_THIS_N']} MDE={v['MDE_tilted_mean']:.6f}")


# ======================================================================================
# 12. D6 -- what the phoneme layer actually adds
# ======================================================================================
tot_cons = sum(r["n_cons"] for r in surah_rows.values())
tot_gem = sum(r["geminate_pairs"] for r in surah_rows.values())
tot_vv = sum(r["long_vowels"] for r in surah_rows.values())
tot_vs = sum(r["short_vowels"] for r in surah_rows.values())
D6 = {
    "corpus_consonant_tokens_P": tot_cons,
    "corpus_geminate_pairs_P": tot_gem,
    "geminate_rate_per_consonant": tot_gem / tot_cons,
    "corpus_long_vowels_P": tot_vv,
    "corpus_short_vowels_P": tot_vs,
    "long_vowel_fraction": tot_vv / (tot_vv + tot_vs),
    "computable_under_G": False,
    "source_of_the_information": "quran-full-tashkeel.json (the tashkeel), NOT the transliteration",
}
log(f"[D6] P adds: {tot_gem} geminate pairs ({D6['geminate_rate_per_consonant']:.4f}/consonant) "
    f"and {tot_vv} long vowels ({D6['long_vowel_fraction']:.4f} of vowels) -- "
    f"both undefined under G, both sourced from the TASHKEEL")


# ======================================================================================
# 13. VERDICT -- transcribed from pre-registration section 5.2, branch for branch
# ======================================================================================
gates = {"S1": S1["verdict"], "S2": S2["verdict"], "S3": S3["verdict"],
         "S4": S4["verdict"], "S5": "PASS", "S6": "PASS" if S6_PASS else "VOID",
         "S7": S7["verdict"], "S8": "PASS", "S9": "PASS"}
gate_void = [k for k, v in gates.items() if v not in ("PASS",)]

if gate_void:
    VERDICT = "VOID"
    VERDICT_WHY = f"hard gate(s) failed: {gate_void}"
elif not D1_PASS:                                                    # 5.2 branch 7
    VERDICT = "SPECIFIED-TEST-EXECUTABLE"
    VERDICT_WHY = "the muqattaat 8/10 pipeline does read corpus text; the substitution is void"
elif not D2_PASS:                                                    # 5.2 branch 5
    VERDICT = "PREMISE-SURVIVES-ADDITION"
    VERDICT_WHY = f"H(T|A) = {d2[d2_worse]['H_T_given_A_bits']} > 0"
elif not D3_PASS:                                                    # 5.2 branch 6
    VERDICT = "PREMISE-SURVIVES-LOSSLESS"
    VERDICT_WHY = f"H(A|T) = {d3[d3_best]['H_A_given_T_bits']} == 0 under {d3_best}"
else:                                                                # D1 and D2 and D3
    if C4_PASS and C5_PASS:                                          # 5.2 branch 2
        VERDICT = "PREMISE-REFUTED-LOSS-TARGETED"
    elif C4_PASS != C5_PASS:                                         # 5.2 branch 3
        VERDICT = "PREMISE-REFUTED-LOSS-PARTIAL"
    else:                                                            # 5.2 branch 4
        VERDICT = "PREMISE-REFUTED-LOSS-UNTARGETED"
    VERDICT_WHY = (f"D1 (no corpus read) and D2 (H(T|A)=0) and D3 (H(A|T)>0) all hold; "
                   f"C4 {'PASS' if C4_PASS else 'FAIL'}, C5 {'PASS' if C5_PASS else 'FAIL'}")
log(f"\n[VERDICT] {VERDICT} -- {VERDICT_WHY}")


# ======================================================================================
# 14. Artefacts
# ======================================================================================
def git(*a):
    try:
        return subprocess.run(["git", *a], cwd=REPO, capture_output=True,
                              text=True, check=True).stdout.strip()
    except Exception:
        return None


def strip_nulls(o):
    if isinstance(o, dict):
        return {k: strip_nulls(v) for k, v in o.items() if k != "nulls"}
    if isinstance(o, list):
        return [strip_nulls(x) for x in o]
    return o


result = {
    "finding_id": "H-NEW-3170",
    "frontier_item": "F-19",
    "utc": UTC,
    "prereg_sha256": _sha,
    "script_sha256": sha256_file(Path(__file__)),
    "seed": SEED, "n_perm": N_PERM,
    "k_confirmatory": K_CONFIRMATORY, "alpha_bon": ALPHA_BON,
    "git_head": git("rev-parse", "HEAD"),
    "python": platform.python_version(),
    "input_sha256": {rel: sha256_file(REPO / rel) for rel in
                     ("quran-text/quran-transliteration.json",
                      "quran-text/quran-full-tashkeel.json",
                      "quran-text/quran-no-tashkeel.json",
                      "findings/phase-b-hypotheses/scripts/h-new-2990.py")},
    "gates": {"S1": S1, "S2": S2, "S3": S3, "S4": S4,
              "S5_note": "applied per theta; see merger_by_theta[*].S5_inhomogeneous_excluded",
              "S6": {"null_varies": S6_PASS}, "S7": S7,
              "S8": {"prereg_sha_verified": True}, "S9": {"exist_ok": False}},
    "D1_executability": {"scripts": d1_rows, "total_read_calls": d1_total_reads,
                         "corpus_path_hits": d1_corpus_hits, "PASS": D1_PASS},
    "D2_addition": {**d2, "PASS": D2_PASS},
    "D3_loss": {**d3, "PASS": D3_PASS},
    "D6_what_P_adds": D6,
    "merger_by_theta": merger_by_theta,
    "C4": {"by_theta": strip_nulls(C4_by_theta), "headline_theta": C4_head_key,
           "headline": strip_nulls(C4), "PASS": C4_PASS},
    "C5": {"by_channel": strip_nulls(C5_by_channel), "headline_worst_channel": C5_head_key,
           "dominant_channel": C5_dominant, "headline": strip_nulls(C5), "PASS": C5_PASS},
    "power": POWER,
    "verdict": VERDICT, "verdict_why": VERDICT_WHY,
}

with open(RUN / "result.json", "x") as f:
    json.dump(result, f, ensure_ascii=False, indent=2)
with open(RUN / "pair-contrast-table.json", "x") as f:
    json.dump(pair_table, f, ensure_ascii=False, indent=2)
with open(RUN / "surah-profiles.json", "x") as f:
    json.dump(surah_rows, f, ensure_ascii=False, indent=2)
with open(RUN / "run.log", "x") as f:
    f.write("\n".join(LOG_LINES) + "\n")
with open(RUN / "prereg.sha256", "x") as f:
    f.write(_sha + "  " + str(PREREG.relative_to(REPO)) + "\n")
say(f"\nartefacts written to {RUN}")
