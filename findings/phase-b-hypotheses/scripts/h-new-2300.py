#!/usr/bin/env python3
"""H-NEW-2300 — Dual-name fāṣila seal-grammar: does verse CONTENT predict the sealing name-PAIR?

Extends H-NEW-2070 (positional al-fawāṣil grammar) on the orthogonal SEMANTIC axis:
the classical murāʿāt al-naẓīr / tamkīn al-fāṣila claim (al-Zarkashī al-Burhān;
al-Rāzī Mafātīḥ al-ghayb; al-Suyūṭī al-Itqān nawʿ 59).

Pre-reg: findings/phase-b-hypotheses/prereg-h-new-2300-dual-name-fasila-seal.md
SHA256:  cc1962fba93c68c14026b468d0bef6bc4b66f6b701f85f5eb64168fd7c204cb5

Rules-tuple: (no-tashkeel for seal-detection + QAC-ROOT for content,
              verse-final ordered name-pair, base-normalized to 97 al-Tirmidhī
              single-token names, content = QAC stem-roots of verse body EXCLUDING
              final 2 words [the seal] + seal-roots stripped, basmala-counted-only-in-Q1,
              Hafs-Kufan, Mashriqi)

Hypotheses (Bonferroni k=2, α_cell=0.025) + 1 pre-registered directional secondary:
  H1 (primary)   — MI(dominant-content-class ; seal-class) > null   [direction LOCKED above]
  H2             — match-rate(dominant-content == seal-class) > null [direction LOCKED above]
  H3 (secondary) — MERCY-content enriches MERCY-seal (one-sided Fisher, α=0.05)
Null: permute seal-class labels across called verses (preserve marginals). seed=20260509, 10000 perms.
"""

import hashlib
import json
import math
import os
import random
import re
import statistics
import sys
from collections import Counter, defaultdict
from math import comb
from pathlib import Path

ROOT = Path("/Users/grey/Downloads/quran")
PREREG = ROOT / "findings/phase-b-hypotheses/prereg-h-new-2300-dual-name-fasila-seal.md"
EXPECTED_SHA = "cc1962fba93c68c14026b468d0bef6bc4b66f6b701f85f5eb64168fd7c204cb5"
QURAN_PATH = ROOT / "quran-text/quran-no-tashkeel.json"
NAMES_PATH = ROOT / "data/asma-al-husna.txt"
MORPH_PATH = ROOT / "data/morphology/quranic-corpus-morphology-0.4.txt"
CHRON_PATH = ROOT / "data/revelation-order.csv"
OUT_PATH = ROOT / "findings/phase-b-hypotheses/csv/h-new-2300.json"

SEED = 20260509
N_PERM = 10_000
ALPHA_BON = 0.025
ALPHA_H3 = 0.05

PAUSE = set("۞ۖۗۚ۟ۘ۠ۤۛ")

# --- Buckwalter root -> super-class for SEAL names (§3 of pre-reg) ---
SEAL_ROOT = {
    "غفور": "gfr", "رحيم": "rHm", "رحمن": "rHm", "تواب": "twb", "ودود": "wdd",
    "عفو": "Efw", "رؤوف": "rAf", "غفار": "gfr", "بر": "brr", "حليم": "Hlm",
    "شكور": "$kr",
    "عزيز": "Ezz", "حكيم": "Hkm", "حكم": "Hkm", "قهار": "qhr", "جبار": "jbr",
    "متكبر": "kbr", "كبير": "kbr", "قدير": "qdr", "قادر": "qdr", "مقتدر": "qdr",
    "علي": "Elw", "متعالي": "Elw", "عظيم": "EZm", "قوي": "qwy", "متين": "mtn",
    "عليم": "Elm", "سميع": "smE", "بصير": "bSr", "خبير": "xbr", "شهيد": "$hd",
    "حفيظ": "HfZ", "لطيف": "lTf", "رقيب": "rqb",
}
THEME = {
    "gfr": "MERCY", "rHm": "MERCY", "twb": "MERCY", "wdd": "MERCY", "Efw": "MERCY",
    "rAf": "MERCY", "brr": "MERCY", "Hlm": "MERCY", "$kr": "MERCY",
    "Ezz": "POWER", "Hkm": "POWER", "qhr": "POWER", "jbr": "POWER", "kbr": "POWER",
    "qdr": "POWER", "Elw": "POWER", "EZm": "POWER", "qwy": "POWER", "mtn": "POWER",
    "Elm": "KNOW", "smE": "KNOW", "bSr": "KNOW", "xbr": "KNOW", "$hd": "KNOW",
    "HfZ": "KNOW", "lTf": "KNOW", "rqb": "KNOW",
}
# --- independent CONTENT lexicon (verse-body roots, §4 of pre-reg) ---
CONTENT = {
    "gfr": "MERCY", "twb": "MERCY", "*nb": "MERCY", "Avm": "MERCY", "jrm": "MERCY",
    "xTA": "MERCY", "Efw": "MERCY", "Hwb": "MERCY", "swA": "MERCY", "bgy": "MERCY",
    "fsq": "MERCY", "Zlm": "MERCY", "Edw": "MERCY", "rHm": "MERCY",
    "Hkm": "POWER", "mlk": "POWER", "qdr": "POWER", "qhr": "POWER", "Ezz": "POWER",
    "jbr": "POWER", "Amr": "POWER", "qDy": "POWER", "ktb": "POWER", "glb": "POWER",
    "qtl": "POWER", "Hrb": "POWER",
    "Elm": "KNOW", "smE": "KNOW", "bSr": "KNOW", "$hd": "KNOW", "rAy": "KNOW",
    "HfZ": "KNOW", "xbr": "KNOW", "ktm": "KNOW", "bTn": "KNOW", "srr": "KNOW",
}
CLASSES = ["MERCY", "POWER", "KNOW"]

TRANSLIT = {
    "غفور": "ghafūr", "رحيم": "raḥīm", "رحمن": "raḥmān", "تواب": "tawwāb",
    "ودود": "wadūd", "عفو": "ʿafū", "رؤوف": "raʾūf", "غفار": "ghaffār",
    "بر": "barr", "حليم": "ḥalīm", "شكور": "shakūr", "عزيز": "ʿazīz",
    "حكيم": "ḥakīm", "حكم": "ḥakam", "قهار": "qahhār", "جبار": "jabbār",
    "متكبر": "mutakabbir", "كبير": "kabīr", "قدير": "qadīr", "قادر": "qādir",
    "مقتدر": "muqtadir", "علي": "ʿalī", "متعالي": "mutaʿālī", "عظيم": "ʿaẓīm",
    "قوي": "qawī", "متين": "matīn", "عليم": "ʿalīm", "سميع": "samīʿ",
    "بصير": "baṣīr", "خبير": "khabīr", "شهيد": "shahīd", "حفيظ": "ḥafīẓ",
    "لطيف": "laṭīf", "رقيب": "raqīb",
}

LOC_RE = re.compile(r"^\((\d+):(\d+):(\d+):(\d+)\)\t")


def verify_sha() -> None:
    actual = hashlib.sha256(PREREG.read_bytes()).hexdigest()
    if actual != EXPECTED_SHA:
        sys.exit(f"PRE-REG SHA MISMATCH:\n  expected={EXPECTED_SHA}\n  actual  ={actual}")
    print(f"pre-reg SHA verified: {EXPECTED_SHA[:16]}…")


def strip_al(w: str) -> str:
    return w[2:] if w.startswith("ال") else w


def base(w: str) -> str:
    if w.startswith("ال"):
        w = w[2:]
    if len(w) > 3 and w.endswith("ا"):
        w = w[:-1]
    return w


def toks(text: str) -> list[str]:
    return [w for w in text.split() if not all(c in PAUSE for c in w)]


def load_divine() -> set[str]:
    names = []
    for raw in NAMES_PATH.read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        if not line or line.startswith("#"):
            continue
        names.append(" ".join(line.split()))
    return {strip_al(n) for n in names if len(n.split()) == 1}


def load_morphology():
    """(sid,ayah) -> list[(wordidx, root)] ; (sid,ayah) -> max word index."""
    vr = defaultdict(list)
    maxw = defaultdict(int)
    for line in MORPH_PATH.read_text(encoding="utf-8").splitlines():
        m = LOC_RE.match(line)
        if not m:
            continue
        sid, ayah, wi, _ = map(int, m.groups())
        key = (sid, ayah)
        if wi > maxw[key]:
            maxw[key] = wi
        if "ROOT:" in line:
            feats = line.rstrip().split("\t")[-1]
            for f in feats.split("|"):
                if f.startswith("ROOT:"):
                    vr[key].append((wi, f[5:]))
    return vr, maxw


def seal_class(b1: str, b2: str):
    t1 = THEME.get(SEAL_ROOT.get(b1, ""))
    t2 = THEME.get(SEAL_ROOT.get(b2, ""))
    return t1 if (t1 and t2 and t1 == t2) else None


def body_roots(key, vr, maxw, seal_fam, strip_seal: bool):
    mx = maxw.get(key, 0)
    rs = [r for wi, r in vr.get(key, []) if wi <= mx - 2]  # exclude final 2 words (the seal)
    if strip_seal:
        rs = [r for r in rs if r not in seal_fam]
    return rs


def dominant_content(rs):
    cnt = Counter(CONTENT[r] for r in rs if r in CONTENT)
    if not cnt:
        return None
    mc = cnt.most_common()
    if len(mc) > 1 and mc[0][1] == mc[1][1]:
        return None  # tie -> no call
    return mc[0][0]


def mutual_info(pairs):
    n = len(pairs)
    if n == 0:
        return 0.0
    px = Counter(p[0] for p in pairs)
    py = Counter(p[1] for p in pairs)
    pxy = Counter(pairs)
    mi = 0.0
    for (x, y), nxy in pxy.items():
        pxy_ = nxy / n
        mi += pxy_ * math.log2(pxy_ / ((px[x] / n) * (py[y] / n)))
    return mi


def match_rate(pairs):
    if not pairs:
        return 0.0
    return sum(1 for x, y in pairs if x == y) / len(pairs)


def fisher_one_sided(a, b, c, d):
    """One-sided (upper-tail) Fisher exact: enrichment of cell a."""
    n = a + b + c + d
    r1 = a + b
    r2 = c + d
    c1 = a + c

    def p(x):
        bb = r1 - x
        cc = c1 - x
        dd = r2 - cc
        if bb < 0 or cc < 0 or dd < 0 or x < 0:
            return 0.0
        return comb(r1, x) * comb(r2, cc) / comb(n, c1)

    tot = 0.0
    for x in range(a, min(r1, c1) + 1):
        tot += p(x)
    return tot


def pct(sorted_vals, q):
    idx = min(len(sorted_vals) - 1, int(q * len(sorted_vals)))
    return sorted_vals[idx]


def main() -> None:
    verify_sha()
    DIVINE = load_divine()
    print(f"Divine base-name set: {len(DIVINE)} single-token al-Tirmidhī names")
    corpus = json.loads(QURAN_PATH.read_text(encoding="utf-8"))
    vr, maxw = load_morphology()

    # period map (descriptive)
    period_by_sid = {}
    for ln in CHRON_PATH.read_text(encoding="utf-8").splitlines()[1:]:
        parts = ln.split(",")
        if len(parts) >= 5:
            try:
                period_by_sid[int(parts[1])] = parts[4].strip()
            except ValueError:
                pass

    # --- detect every verse-final divine-name PAIR (IDENTICAL detector to H-NEW-2070) ---
    seal_rows = []  # (sid, ayah, b1, b2, surface)
    for s in corpus:
        sid = int(s["id"])
        for v in s["verses"]:
            ayah = int(v["id"])
            tk = toks(v["text"])
            if len(tk) < 2:
                continue
            b1, b2 = base(tk[-2]), base(tk[-1])
            if b1 in DIVINE and b2 in DIVINE:
                seal_rows.append((sid, ayah, b1, b2, f"{tk[-2]} {tk[-1]}"))
    print(f"\nVerses closing on a divine-name PAIR: {len(seal_rows)}")

    # --- pure-class subset ---
    pure = []  # (sid, ayah, b1, b2, surface, seal_class, seal_fam)
    for sid, ayah, b1, b2, surf in seal_rows:
        cl = seal_class(b1, b2)
        if cl is not None:
            pure.append((sid, ayah, b1, b2, surf, cl, (SEAL_ROOT[b1], SEAL_ROOT[b2])))
    print(f"Pure-class seal verses (both names same super-class): {len(pure)}")
    print(f"  class sizes: {dict(Counter(r[5] for r in pure))}")

    # --- build called-verse contingency (PRIMARY: leakage-stripped) ---
    def build_called(strip_seal):
        data, called_locs = [], []
        for sid, ayah, b1, b2, surf, cl, fam in pure:
            rs = body_roots((sid, ayah), vr, maxw, set(fam), strip_seal)
            dc = dominant_content(rs)
            if dc is not None:
                data.append((cl, dc))
                called_locs.append((sid, ayah, cl, dc, surf))
        return data, called_locs

    data, called_locs = build_called(strip_seal=True)
    n_called = len(data)
    print(f"\nCalled verses (≥1 content-root, unambiguous dominant class, STRIPPED): {n_called}/{len(pure)}")

    obs_mi = mutual_info(data)
    obs_match = match_rate(data)
    print(f"Observed MI = {obs_mi:.4f} bits ; match-rate = {obs_match:.4f}")

    # confusion matrix
    cm = Counter(data)
    confusion = {sc: {cc: cm.get((sc, cc), 0) for cc in CLASSES} for sc in CLASSES}

    # --- permutation null (H1 + H2): permute seal-class labels across called verses ---
    rng = random.Random(SEED)
    seal_lab = [d[0] for d in data]
    cont_lab = [d[1] for d in data]
    mi_null, match_null = [], []
    for _ in range(N_PERM):
        rng.shuffle(seal_lab)
        perm = list(zip(seal_lab, cont_lab))
        mi_null.append(mutual_info(perm))
        match_null.append(match_rate(perm))
    p_mi = sum(1 for x in mi_null if x >= obs_mi) / N_PERM
    p_match = sum(1 for x in match_null if x >= obs_match) / N_PERM
    mi_null_s = sorted(mi_null)
    match_null_s = sorted(match_null)
    h1_pass = p_mi <= ALPHA_BON
    h2_pass = p_match <= ALPHA_BON

    # --- H3: MERCY-content x MERCY-seal 2x2 (leakage-stripped) over ALL pure-class verses ---
    tab = Counter()
    for sid, ayah, b1, b2, surf, cl, fam in pure:
        rs = body_roots((sid, ayah), vr, maxw, set(fam), strip_seal=True)
        has_mercy = any((r in CONTENT and CONTENT[r] == "MERCY") for r in rs)
        tab[(has_mercy, cl == "MERCY")] += 1
    a = tab[(True, True)]
    b = tab[(True, False)]
    cc = tab[(False, True)]
    d = tab[(False, False)]
    p_h3 = fisher_one_sided(a, b, cc, d)
    odds = (a * d) / (b * cc) if (b * cc) else float("inf")
    h3_pass = p_h3 <= ALPHA_H3

    # --- leakage SENSITIVITY (MW-6): seal-roots kept in body ---
    data_keep, _ = build_called(strip_seal=False)
    obs_mi_keep = mutual_info(data_keep)
    obs_match_keep = match_rate(data_keep)
    rng2 = random.Random(SEED)
    sl2 = [x[0] for x in data_keep]
    co2 = [x[1] for x in data_keep]
    mi_k, mr_k = [], []
    for _ in range(N_PERM):
        rng2.shuffle(sl2)
        pm = list(zip(sl2, co2))
        mi_k.append(mutual_info(pm))
        mr_k.append(match_rate(pm))
    p_mi_keep = sum(1 for x in mi_k if x >= obs_mi_keep) / N_PERM
    p_match_keep = sum(1 for x in mr_k if x >= obs_match_keep) / N_PERM

    # --- verdict (LOCKED rule, §6) ---
    if obs_mi < statistics.median(mi_null) and obs_match < statistics.median(match_null):
        verdict = "NULL (reverse/formulaic — seals NOT content-matched)"
    elif h1_pass and h2_pass and h3_pass:
        verdict = "EXTENDS H-NEW-2070 (PASS-DIRECTED-CONTENT)"
    elif h1_pass and h2_pass and not h3_pass:
        verdict = "PARTIAL (H1+H2 pass; H3 directional not significant)"
    elif h1_pass or h2_pass:
        verdict = "PARTIAL (one of H1/H2)"
    else:
        verdict = "NULL"

    # --- descriptive: top pairs per class + exemplar called verses ---
    pure_pair_counts = Counter((r[2], r[3]) for r in pure)
    top_pairs_by_class = {c: [] for c in CLASSES}
    for (b1, b2), n in pure_pair_counts.most_common():
        cl = seal_class(b1, b2)
        top_pairs_by_class[cl].append({
            "pair_ar": f"{b1} + {b2}",
            "pair_translit": f"{TRANSLIT.get(b1, b1)} + {TRANSLIT.get(b2, b2)}",
            "count": n,
        })
    # exemplar matched mercy verses (forgiveness content -> mercy seal)
    mercy_examples = []
    for sid, ayah, b1, b2, surf, cl, fam in pure:
        if cl != "MERCY":
            continue
        rs = body_roots((sid, ayah), vr, maxw, set(fam), strip_seal=True)
        mercy_hits = sorted({r for r in rs if r in CONTENT and CONTENT[r] == "MERCY"})
        if mercy_hits:
            mercy_examples.append({
                "loc": f"Q{sid}:{ayah}", "seal": f"{TRANSLIT.get(b1, b1)} {TRANSLIT.get(b2, b2)}",
                "mercy_content_roots": mercy_hits,
            })
    power_examples = []
    for sid, ayah, b1, b2, surf, cl, fam in pure:
        if cl != "POWER":
            continue
        rs = body_roots((sid, ayah), vr, maxw, set(fam), strip_seal=True)
        hits = sorted({r for r in rs if r in CONTENT and CONTENT[r] == "POWER"})
        if hits:
            power_examples.append({
                "loc": f"Q{sid}:{ayah}", "seal": f"{TRANSLIT.get(b1, b1)} {TRANSLIT.get(b2, b2)}",
                "power_content_roots": hits,
            })

    out = {
        "finding_id": "H-NEW-2300",
        "title": "Dual-name fāṣila seal-grammar — verse-content predicts the sealing name-pair (content↔seal matching)",
        "extends": "H-NEW-2070",
        "pre_reg_sha256": EXPECTED_SHA,
        "seed": SEED, "n_perm": N_PERM,
        "alpha_bon_per_cell": ALPHA_BON, "bonferroni_k": 2, "alpha_H3": ALPHA_H3,
        "rules_tuple": "(no-tashkeel seal-detect + QAC-ROOT content, verse-final ordered "
                       "name-pair, base-normalized to 97 al-Tirmidhī single-token names, "
                       "content = body roots excl. final-2-words + seal-roots stripped, "
                       "basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)",
        "classes": CLASSES,
        "n_verses_closing_divine_pair": len(seal_rows),
        "n_pure_class_verses": len(pure),
        "pure_class_sizes": dict(Counter(r[5] for r in pure)),
        "n_called_primary": n_called,
        "primary_leakage_stripped": {
            "H1_MI": {
                "observed": obs_mi, "null_mean": statistics.mean(mi_null),
                "null_median": statistics.median(mi_null),
                "null_p97_5": pct(mi_null_s, 0.975), "p_perm": p_mi, "pass": h1_pass,
            },
            "H2_match_rate": {
                "observed": obs_match, "null_mean": statistics.mean(match_null),
                "null_median": statistics.median(match_null),
                "null_p97_5": pct(match_null_s, 0.975), "p_perm": p_match, "pass": h2_pass,
            },
            "confusion_seal_rows_x_content_cols": confusion,
        },
        "H3_mercy_content_enriches_mercy_seal": {
            "table_2x2": {
                "mercy_content_AND_mercy_seal": a,
                "mercy_content_AND_other_seal": b,
                "no_mercy_content_AND_mercy_seal": cc,
                "no_mercy_content_AND_other_seal": d,
            },
            "odds_ratio": odds, "fisher_one_sided_p": p_h3, "pass": h3_pass,
        },
        "leakage_sensitivity_seal_roots_kept": {
            "n_called": len(data_keep),
            "MI_observed": obs_mi_keep, "MI_p_perm": p_mi_keep,
            "match_observed": obs_match_keep, "match_p_perm": p_match_keep,
            "note": "inflated by self-seal echo; NOT the claim under test; for contrast only",
        },
        "verdict": verdict,
        "top_pairs_by_seal_class": top_pairs_by_class,
        "n_mercy_matched_examples": len(mercy_examples),
        "mercy_matched_examples": mercy_examples[:40],
        "n_power_matched_examples": len(power_examples),
        "power_matched_examples": power_examples[:30],
    }
    os.makedirs(OUT_PATH.parent, exist_ok=True)
    OUT_PATH.write_text(json.dumps(out, indent=2, ensure_ascii=False), encoding="utf-8")

    print("\n=== PRIMARY (leakage-stripped) ===")
    print(f"H1 MI:    obs={obs_mi:.4f}  null_mean={statistics.mean(mi_null):.4f}  "
          f"p97.5={pct(mi_null_s,0.975):.4f}  p={p_mi:.5f}  pass={h1_pass}")
    print(f"H2 match: obs={obs_match:.4f}  null_mean={statistics.mean(match_null):.4f}  "
          f"p97.5={pct(match_null_s,0.975):.4f}  p={p_match:.5f}  pass={h2_pass}")
    print("confusion (seal rows x content cols):")
    print("          " + "  ".join(f"{c:>6}" for c in CLASSES))
    for sc in CLASSES:
        print(f"  {sc:>6}: " + "  ".join(f"{confusion[sc][ccc]:6d}" for ccc in CLASSES))
    print(f"\n=== H3 (MERCY-content -> MERCY-seal, leakage-stripped) ===")
    print(f"  2x2: a={a} b={b} c={cc} d={d}  OR={odds:.3f}  Fisher one-sided p={p_h3:.3e}  pass={h3_pass}")
    print(f"\n=== leakage SENSITIVITY (seal-roots kept) ===")
    print(f"  MI obs={obs_mi_keep:.4f} p={p_mi_keep:.5f}  |  match obs={obs_match_keep:.4f} p={p_match_keep:.5f}")
    print(f"\nVERDICT: {verdict}")
    print(f"Wrote: {OUT_PATH}")


if __name__ == "__main__":
    main()
