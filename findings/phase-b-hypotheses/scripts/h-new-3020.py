#!/usr/bin/env python3
"""H-NEW-3020: is the loanword donor-language field a measurement?

Jeffery (1938) as encoded in data/loanwords/jeffery-1938-loanwords.tsv, against
al-Suyuti's Itqan nawʿ 38 donor assignments extracted from the on-disk OpenITI text.

Runner only. Emits no interpretation. See
findings/phase-b-hypotheses/prereg-h-new-3020-loanword-donor-strata.md
"""

import argparse
import csv
import hashlib
import io
import json
import os
import platform
import random
import re
import subprocess
import sys
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path

# --- prereg 3.1: frozen inputs --------------------------------------------
EXPECTED_PREREG_SHA = "a552d357cabe8fdee20d0a29fc405668289ca149b18b2888063c3de859bbfb60"
EXPECTED_TSV_SHA = "d12ebac9d4bb62bbc1a8c810d7e2c069195e20113a77fb04505a84dfd4674b94"
EXPECTED_ITQAN_SHA = "a067ebb34ccabe92376f3008b9cdfb32eea9d6167062172318635e53f500fb05"
EXPECTED_QAC_SHA = "a1d12923815341face765083805d2148ed2d9f5cc3f7d6665219d887675d8c46"
EXPECTED_CHRON_SHA = "74f52ec1518abf8ecbf67671ee1cdd8e4cfc553fc8c5ead8274cc7dae8916fb7"

# --- prereg 7 / 7.1 --------------------------------------------------------
N_PERM = 10_000
TESTS_IN_FAMILY = 8
ALPHA_BON = 0.05 / TESTS_IN_FAMILY            # 0.00625
CORRECTED_GATE = 0.005
RAW_GATE = CORRECTED_GATE / TESTS_IN_FAMILY   # 0.000625
SEED_NULL_A = 20260509
SEED_NULL_B = 20260510
SEED_NULL_C = 20260511
REPLICATION_OFFSET = 10

PHASES = ["Early Meccan", "Middle Meccan", "Late Meccan", "Medinan"]
PHASE_IDX = {p: i + 1 for i, p in enumerate(PHASES)}

# --- prereg 3.2: content anchors for the nawʿ-38 roster span ---------------
START_ANCHOR = "وهذا سرد الألفاظ الواردة في القرآن من ذلك مرتبة على حروف المعجم"
END_ANCHOR = "فهذا ما وقفت عليه من الألفاظ المعربة في القرآن"

# --- prereg 3.1: provenance gate ------------------------------------------
REQUIRED_AUTHOR_SUBSTR = "السيوطي"
REQUIRED_DIED = "911"

# --- prereg 3.4: donor-family vocabulary, locked ---------------------------
NISBA = {
    "حبشي": "ethiopic", "نبطي": "aramaic", "سرياني": "syriac",
    "عبراني": "hebrew", "عبري": "hebrew", "فارسي": "persian",
    "قبطي": "coptic", "رومي": "greek", "يوناني": "greek",
    "زنجي": "zanji", "بربري": "berber", "هندي": "indic",
    "تركي": "turkish", "حوراني": "hawrani",
}
PEOPLE = {
    "الحبشة": "ethiopic", "النبط": "aramaic", "السريان": "syriac",
    "اليهود": "hebrew", "الفرس": "persian", "القبط": "coptic",
    "الروم": "greek", "اليونان": "greek", "الزنج": "zanji",
    "البربر": "berber", "الهند": "indic", "الترك": "turkish",
}
UNSPEC_RE = re.compile(r"أعجمي|أعجمية|العجم|عجمي|غير\s+عربي")
REGION_RE = re.compile(r"أهل\s+ال(?:مغرب|غرب)")

_NIS_ALT = "|".join(sorted(NISBA, key=len, reverse=True))
_PEO_ALT = "|".join(sorted(PEOPLE, key=len, reverse=True))
NISBA_RE = re.compile(r"(?:^|\s|بال|ال|ب)(" + _NIS_ALT + r")(?:ة|ين)?\b")
PEOPLE_RE = re.compile(r"ب?(?:لغة|لسان|كلام)\s+(" + _PEO_ALT + r")")

# --- prereg 5: common label scheme ----------------------------------------
ARAM = {"aramaic", "syriac"}
PERS = {"persian"}
JEFFERY_MAP = {
    "syriac": "ARAM", "aramaic": "ARAM", "persian": "PERS",
    "hebrew": "HEB", "ethiopic": "ETH", "greek": "GRK",
    "latin": "OTHER", "south-arabian": "OTHER",
}
JEFFERY_TWO_DONOR = {"hebrew-aramaic-shared": "HEB", "syriac-aramaic-shared": "ARAM"}
SUY_MAP = {
    "aramaic": "ARAM", "syriac": "ARAM", "persian": "PERS", "hebrew": "HEB",
    "ethiopic": "ETH", "greek": "GRK", "coptic": "COPT",
    "zanji": "OTHER", "berber": "OTHER", "indic": "OTHER",
    "turkish": "OTHER", "hawrani": "OTHER",
}

# --- prereg 3.5: join keys, adopted unchanged from H-NEW-2700 3.2 ----------
BW = {"'": "ء", "|": "آ", ">": "أ", "&": "ؤ", "<": "إ", "}": "ئ", "A": "ا", "b": "ب",
      "p": "ة", "t": "ت", "v": "ث", "j": "ج", "H": "ح", "x": "خ", "d": "د", "*": "ذ",
      "r": "ر", "z": "ز", "s": "س", "$": "ش", "S": "ص", "D": "ض", "T": "ط", "Z": "ظ",
      "E": "ع", "g": "غ", "_": "ـ", "f": "ف", "q": "ق", "k": "ك", "l": "ل", "m": "م",
      "n": "ن", "h": "ه", "w": "و", "Y": "ى", "y": "ي", "F": "ً", "N": "ٌ", "K": "ٍ",
      "a": "َ", "u": "ُ", "i": "ِ", "~": "ّ", "o": "ْ", "^": "ٓ", "#": "ٔ", "`": "ٰ",
      "{": "ٱ"}
SHORT = set("ًٌٍَُِّْٓٔ")
LOC_RE = re.compile(r"\((\d+):(\d+):(\d+):(\d+)\)")
PAGE_RE = re.compile(r"^#\s*PageV\d+P\d+\s*$")
HEAD_RE = re.compile(r"^\{\s*([^}]+?)\s*\}")


def bw2ar(s):
    return "".join(BW.get(c, c) for c in s)


def key(s, drop_dagger):
    s = "".join(c for c in s if c not in SHORT and c != "ـ")
    s = s.replace("وٰ", "ا").replace("يٰ", "ا")
    s = s.replace("ٰ", "" if drop_dagger else "ا")
    for a, b in (("ٱ", "ا"), ("أ", "ا"), ("إ", "ا"), ("آ", "ا"),
                 ("ؤ", "ء"), ("ئ", "ء"), ("ة", "ه"), ("ى", "ي")):
        s = s.replace(a, b)
    return s.replace("ء", "")


def strip_al(k):
    return k[2:] if k.startswith("ال") and len(k) > 3 else k


def jkey(s, drop_dagger):
    return strip_al(key(s, drop_dagger))


def sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def require(path, expected, label):
    actual = sha256(path)
    if actual != expected:
        raise SystemExit(f"ABORT: {label} SHA-256 mismatch\n  path={path}\n"
                         f"  expected={expected}\n  actual  ={actual}")
    return actual


# ---------------------------------------------------------------- statistics
def perm_p(obs, draws):
    """prereg 7: one-sided in the locked direction."""
    return (1 + sum(1 for d in draws if d >= obs)) / (len(draws) + 1)


def rank(vals):
    n = len(vals)
    order = sorted(range(n), key=lambda i: vals[i])
    r = [0.0] * n
    i = 0
    while i < n:
        j = i
        while j + 1 < n and vals[order[j + 1]] == vals[order[i]]:
            j += 1
        avg = (i + j) / 2.0 + 1.0
        for k in range(i, j + 1):
            r[order[k]] = avg
        i = j + 1
    return r


def spearman(xs, ys):
    n = len(xs)
    if n < 3:
        return None
    rx, ry = rank(xs), rank(ys)
    mx, my = sum(rx) / n, sum(ry) / n
    num = sum((a - mx) * (b - my) for a, b in zip(rx, ry))
    dx = sum((a - mx) ** 2 for a in rx) ** 0.5
    dy = sum((b - my) ** 2 for b in ry) ** 0.5
    return num / (dx * dy) if dx and dy else 0.0


def cohen_kappa(pairs):
    """pairs: list of (label_rater1, label_rater2)."""
    n = len(pairs)
    if n == 0:
        return None
    po = sum(1 for a, b in pairs if a == b) / n
    c1 = Counter(a for a, _ in pairs)
    c2 = Counter(b for _, b in pairs)
    pe = sum((c1[c] / n) * (c2[c] / n) for c in set(c1) | set(c2))
    return (po - pe) / (1 - pe) if pe != 1.0 else 0.0


def median(xs):
    s = sorted(xs)
    n = len(s)
    if not n:
        return None
    return s[n // 2] if n % 2 else (s[n // 2 - 1] + s[n // 2]) / 2.0


# ------------------------------------------------------------------ loaders
def load_itqan_roster(path):
    """prereg 3.2 / 3.3 / 3.4."""
    text = path.read_text(encoding="utf-8")
    lines = text.split("\n")

    head = lines[:40]
    author = next((l for l in head if "010.AuthorNAME" in l), "")
    died = next((l for l in head if "011.AuthorDIED" in l), "")
    if REQUIRED_AUTHOR_SUBSTR not in author or REQUIRED_DIED not in died:
        raise SystemExit("ABORT: Itqan provenance gate failed (prereg 3.1)\n"
                         f"  AuthorNAME={author!r}\n  AuthorDIED={died!r}")

    start = end = None
    for i, l in enumerate(lines):
        if start is None and START_ANCHOR in l:
            start = i
        elif start is not None and END_ANCHOR in l:
            end = i
            break
    if start is None or end is None or end <= start:
        raise SystemExit("ABORT: nawʿ-38 span anchors not found or out of order (prereg 3.2)")

    seg = lines[start + 1:end]
    paras, cur = [], None
    for l in seg:
        if PAGE_RE.match(l):
            continue
        if l.startswith("~~"):
            if cur is not None:
                cur += " " + l[2:].strip()
            continue
        if l.startswith("#"):
            if cur is not None:
                paras.append(cur)
            cur = l[1:].strip()
    if cur is not None:
        paras.append(cur)

    entries = []
    for pr in paras:
        m = HEAD_RE.match(pr)
        if m:
            entries.append({"headword": m.group(1), "body": pr[m.end():]})
        elif entries:
            entries[-1]["body"] += " " + pr

    for e in entries:
        body = e["body"]
        fams, order = set(), {}
        for m in NISBA_RE.finditer(body):
            fam = NISBA[m.group(1)]
            fams.add(fam)
            order.setdefault(fam, m.start())
        for m in PEOPLE_RE.finditer(body):
            fam = PEOPLE[m.group(1)]
            fams.add(fam)
            order.setdefault(fam, m.start())
        e["families"] = sorted(fams)
        e["first_named"] = min(fams, key=lambda f: order[f]) if fams else None
        e["unspecified_foreign"] = bool(UNSPEC_RE.search(body))
        e["region_marker"] = bool(REGION_RE.search(body))
    return entries, (start + 1, end)


def load_registry(path):
    lines = [l for l in path.read_text(encoding="utf-8").split("\n") if not l.startswith("#")]
    return list(csv.DictReader(io.StringIO("\n".join(lines)), delimiter="\t"))


def load_qac(path):
    """Per-lemma-key surah->token-count, plus the lemma multiset for the ambiguity gate."""
    counts = {1: defaultdict(Counter), 2: defaultdict(Counter)}
    lemmas = {1: defaultdict(set), 2: defaultdict(set)}
    form_counts = {1: defaultdict(Counter), 2: defaultdict(Counter)}
    with open(path, encoding="utf-8") as fh:
        for line in fh:
            if line.startswith("#") or line.startswith("LOCATION") or not line.strip():
                continue
            f = line.rstrip("\n").split("\t")
            if len(f) != 4:
                continue
            m = LOC_RE.fullmatch(f[0])
            if not m:
                continue
            surah = int(m.group(1))
            lm = re.search(r"(?:^|\|)LEM:([^|]+)", f[3])
            for tier, dd in ((1, False), (2, True)):
                form_counts[tier][jkey(bw2ar(f[1]), dd)][surah] += 1
                if lm:
                    k = jkey(bw2ar(lm.group(1)), dd)
                    counts[tier][k][surah] += 1
                    lemmas[tier][k].add(lm.group(1))
    return counts, lemmas, form_counts


def resolve(word, counts, lemmas, form_counts):
    """prereg 3.5: tier 1 then tier 2; LEM first then FORM; ambiguity gate."""
    if " " in word.strip():
        return None, "multiword"
    for tier in (1, 2):
        k = jkey(word, tier == 2)
        if k in counts[tier]:
            if len(lemmas[tier][k]) > 1:
                return None, "ambiguous"
            return counts[tier][k], f"lem-tier{tier}"
    for tier in (1, 2):
        k = jkey(word, tier == 2)
        if k in form_counts[tier]:
            return form_counts[tier][k], f"form-tier{tier}"
    return None, "unmatched"


# --------------------------------------------------------------------- main
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo", default=".")
    ap.add_argument("--perms", type=int, default=N_PERM)
    ap.add_argument("--out", default=None, help="SMOKE runs only; keeps them out of findings/")
    args = ap.parse_args()
    repo = Path(args.repo).resolve()
    n_perm = args.perms
    smoke = args.out is not None

    rel = {
        "prereg": "findings/phase-b-hypotheses/prereg-h-new-3020-loanword-donor-strata.md",
        "tsv": "data/loanwords/jeffery-1938-loanwords.tsv",
        "itqan": "data/literature/classical-tafsir/raw/suyuti-itqan.openiti.raw.txt",
        "qac": "data/morphology/quranic-corpus-morphology-0.4.txt",
        "chron": "data/revelation-order.csv",
    }
    P = {k: repo / v for k, v in rel.items()}

    shas = {
        "prereg": require(P["prereg"], EXPECTED_PREREG_SHA, "pre-registration"),
        "jeffery_tsv": require(P["tsv"], EXPECTED_TSV_SHA, "Jeffery registry"),
        "suyuti_itqan": require(P["itqan"], EXPECTED_ITQAN_SHA, "al-Suyuti Itqan"),
        "qac_v04": require(P["qac"], EXPECTED_QAC_SHA, "QAC v0.4"),
        "revelation_order": require(P["chron"], EXPECTED_CHRON_SHA, "revelation order"),
    }
    print("[3020] all input SHA-256 gates passed", file=sys.stderr)

    # ---------------------------------------------------------------- inputs
    entries, span = load_itqan_roster(P["itqan"])
    registry = load_registry(P["tsv"])

    phase_of = {}
    with open(P["chron"], encoding="utf-8") as fh:
        for r in csv.DictReader(fh):
            phase_of[int(r["mushaf_order"])] = r["noldeke_phase"].strip()
    if set(phase_of.values()) - set(PHASES):
        raise SystemExit("ABORT: unexpected noldeke_phase value")

    counts, lemmas, form_counts = load_qac(P["qac"])
    surah_words = Counter()
    for k, cc in counts[1].items():
        for s, n in cc.items():
            surah_words[s] += n

    # ------------------------------------------------- census (prereg 2, 10)
    reg_shared = {"hebrew-aramaic-shared", "syriac-aramaic-shared"}
    census = {
        "jeffery_registry": {
            "file_lines": len(P["tsv"].read_text(encoding="utf-8").split("\n")) - 1,
            "data_rows": len(registry),
            "note": "the brief and FRONTIER-MAP report '506 rows'; that is the line count",
            "by_source_language": dict(Counter(r["source_language"] for r in registry)),
            "by_confidence": dict(Counter(r["confidence"] for r in registry)),
            "by_suyuti_flag": dict(Counter(r["suyuti_naw_38_attested"] for r in registry)),
            "two_donor_label_rows": sum(1 for r in registry if r["source_language"] in reg_shared),
            "single_donor_label_rows": sum(1 for r in registry
                                           if r["source_language"] not in reg_shared),
            "unambiguous_rows_single_donor_and_HIGH":
                sum(1 for r in registry
                    if r["source_language"] not in reg_shared and r["confidence"] == "HIGH"),
        },
        "suyuti_nawa_38": {
            "span_line_index_0based": list(span),
            "headword_entries": len(entries),
            "entries_with_a_family": sum(1 for e in entries if e["families"]),
            "entries_multi_family": sum(1 for e in entries if len(e["families"]) > 1),
            "entries_unspecified_foreign_only":
                sum(1 for e in entries if not e["families"] and e["unspecified_foreign"]),
            "entries_region_marker_only":
                sum(1 for e in entries if not e["families"] and e["region_marker"]),
            "entries_no_marker":
                sum(1 for e in entries if not e["families"] and not e["unspecified_foreign"]
                    and not e["region_marker"]),
            "by_family_entries": dict(Counter(f for e in entries for f in e["families"])),
        },
    }
    lab = census["suyuti_nawa_38"]["entries_with_a_family"]
    census["suyuti_nawa_38"]["internal_disagreement_rate_of_labelled"] = (
        census["suyuti_nawa_38"]["entries_multi_family"] / lab if lab else None)

    # --------------------------------------------------------- QAC resolution
    def attach(word):
        cc, how = resolve(word, counts, lemmas, form_counts)
        if cc is None:
            return None, how
        tok = sum(cc.values())
        num = sum(n * PHASE_IDX[phase_of[s]] for s, n in cc.items() if s in phase_of)
        den = sum(n for s, n in cc.items() if s in phase_of)
        if den == 0:
            return None, "no-phase"
        mean_host_len = sum(n * surah_words[s] for s, n in cc.items()) / tok
        return {"phi": num / den, "tokens": tok, "surah_counts": dict(cc),
                "mean_host_surah_words": mean_host_len, "how": how}, how

    suy_types, suy_join = {}, Counter()
    for e in entries:
        d, how = attach(e["headword"])
        suy_join[how] += 1
        if d:
            suy_types[e["headword"]] = dict(d, families=e["families"],
                                            first_named=e["first_named"])

    jef_types, jef_join = {}, Counter()
    for r in registry:
        d, how = attach(r["arabic_lemma"])
        jef_join[how] += 1
        if d:
            jef_types[r["arabic_lemma"]] = dict(d, donor=r["source_language"],
                                                confidence=r["confidence"],
                                                suyuti_flag=r["suyuti_naw_38_attested"])

    # ------------------------------------------------ overlap roster (join key)
    suy_by_key = {}
    for e in entries:
        suy_by_key.setdefault(jkey(e["headword"], False), e)
    jef_by_key = {}
    for r in registry:
        jef_by_key.setdefault(jkey(r["arabic_lemma"], False), r)
    overlap_keys = sorted(set(suy_by_key) & set(jef_by_key))

    # ---------------------------------------------------------- tuple mapping
    def suy_label(e, tuple_id):
        fams = e["families"]
        if tuple_id == "T3":
            fams = [f for f in fams if f != "aramaic"]
        if not fams:
            return None
        if len(fams) > 1:
            if tuple_id == "T2":
                return SUY_MAP.get(e["first_named"])
            return None
        return SUY_MAP.get(fams[0])

    def jef_label(r, tuple_id):
        sl = r["source_language"]
        if sl in JEFFERY_TWO_DONOR:
            return JEFFERY_TWO_DONOR[sl] if tuple_id == "T2" else None
        return JEFFERY_MAP.get(sl)

    # ==================================================================== 6
    # NUISANCE CHANNELS -- reported before any primary statistic
    # ==================================================================== 6
    all_phi = [(t["phi"], t["tokens"], t["mean_host_surah_words"])
               for t in list(suy_types.values()) + list(jef_types.values())]
    import math
    nuisance = {
        "_ORDER": "prereg 6 -- these are computed and reported BEFORE any primary statistic",
        "n_types_pooled": len(all_phi),
        "rho_phi_vs_log_token_count":
            spearman([math.log(a[1]) for a in all_phi], [a[0] for a in all_phi]),
        "rho_phi_vs_log_mean_host_surah_words":
            spearman([math.log(a[2]) for a in all_phi], [a[0] for a in all_phi]),
    }

    # =============================================== rosters for H2 / H3 (T1..T3)
    def build_strata(labeller, items, tuple_id, types_by_word, wordfn):
        aram, pers = [], []
        excluded_both = 0
        for it in items:
            w = wordfn(it)
            if w not in types_by_word:
                continue
            fams = it.get("families") if isinstance(it, dict) and "families" in it else None
            if fams and ("persian" in fams) and (set(fams) & ARAM):
                excluded_both += 1
                continue
            lb = labeller(it, tuple_id)
            if lb == "ARAM":
                aram.append((w, types_by_word[w]))
            elif lb == "PERS":
                pers.append((w, types_by_word[w]))
        return aram, pers, excluded_both

    def delta(aram, pers):
        if not aram or not pers:
            return None
        return (sum(t["phi"] for _, t in pers) / len(pers)
                - sum(t["phi"] for _, t in aram) / len(aram))

    # ------------------------------------------------------------- null engines
    def null_A(aram, pers, seed, nperm):
        pool = [t for _, t in aram] + [t for _, t in pers]
        na = len(aram)
        rng = random.Random(seed)
        draws = []
        for _ in range(nperm):
            idx = list(range(len(pool)))
            rng.shuffle(idx)
            a = [pool[i]["phi"] for i in idx[:na]]
            p = [pool[i]["phi"] for i in idx[na:]]
            draws.append(sum(p) / len(p) - sum(a) / len(a))
        return draws

    def phi_under(surah_counts, pmap):
        num = sum(n * pmap[s] for s, n in surah_counts.items() if s in pmap)
        den = sum(n for s, n in surah_counts.items() if s in pmap)
        return num / den if den else None

    def null_B(aram, pers, seed, nperm):
        surahs = sorted(phase_of)
        idxs = [PHASE_IDX[phase_of[s]] for s in surahs]
        rng = random.Random(seed)
        draws = []
        for _ in range(nperm):
            perm = idxs[:]
            rng.shuffle(perm)
            pmap = dict(zip(surahs, perm))
            a = [phi_under(t["surah_counts"], pmap) for _, t in aram]
            p = [phi_under(t["surah_counts"], pmap) for _, t in pers]
            a = [x for x in a if x is not None]
            p = [x for x in p if x is not None]
            if not a or not p:
                continue
            draws.append(sum(p) / len(p) - sum(a) / len(a))
        return draws

    def terciles(items):
        s = sorted(items, key=lambda x: x[1]["tokens"])
        n = len(s)
        c1, c2 = n // 3, 2 * n // 3
        return [s[:c1], s[c1:c2], s[c2:]]

    def null_C(aram, pers, seed, nperm):
        """prereg 7: permute labels WITHIN token-count terciles. Returns (draws, underpowered)."""
        tagged = [(w, t, "A") for w, t in aram] + [(w, t, "P") for w, t in pers]
        s = sorted(tagged, key=lambda x: x[1]["tokens"])
        n = len(s)
        c1, c2 = n // 3, 2 * n // 3
        blocks = [s[:c1], s[c1:c2], s[c2:]]
        underpowered = any(
            sum(1 for x in b if x[2] == "A") < 2 or sum(1 for x in b if x[2] == "P") < 2
            for b in blocks)
        rng = random.Random(seed)
        draws = []
        for _ in range(nperm):
            a_ph, p_ph = [], []
            for b in blocks:
                labs = [x[2] for x in b]
                rng.shuffle(labs)
                for x, lb in zip(b, labs):
                    (a_ph if lb == "A" else p_ph).append(x[1]["phi"])
            if not a_ph or not p_ph:
                continue
            draws.append(sum(p_ph) / len(p_ph) - sum(a_ph) / len(a_ph))
        return draws, underpowered

    # ------------------------------------------------------------------- H1
    def h1_pairs(tuple_id):
        out = []
        for k in overlap_keys:
            jl = jef_label(jef_by_key[k], tuple_id)
            sl = suy_label(suy_by_key[k], tuple_id)
            if jl and sl:
                out.append((jl, sl, k))
        return out

    def run_h1(tuple_id, seed_a, seed_b, nperm):
        pairs = h1_pairs(tuple_id)
        pr = [(a, b) for a, b, _ in pairs]
        k_obs = cohen_kappa(pr)
        if k_obs is None or len(pr) < 3:
            return {"n_pairs": len(pr), "kappa": k_obs, "insufficient": True}
        raw_agree = sum(1 for a, b in pr if a == b) / len(pr)
        rngA = random.Random(seed_a)
        drawsA = []
        for _ in range(nperm):
            bs = [b for _, b in pr]
            rngA.shuffle(bs)
            drawsA.append(cohen_kappa(list(zip([a for a, _ in pr], bs))))
        rngB = random.Random(seed_b)
        drawsB = []
        for _ in range(nperm):
            as_ = [a for a, _ in pr]
            rngB.shuffle(as_)
            drawsB.append(cohen_kappa(list(zip(as_, [b for _, b in pr]))))
        return {
            "n_pairs": len(pr), "kappa": k_obs, "raw_agreement": raw_agree,
            "p_null_A_permute_suyuti": perm_p(k_obs, drawsA),
            "p_null_B_permute_jeffery": perm_p(k_obs, drawsB),
            "confusion": {f"{a}|{b}": c for (a, b), c in Counter(pr).items()},
            "jeffery_marginal": dict(Counter(a for a, _ in pr)),
            "suyuti_marginal": dict(Counter(b for _, b in pr)),
            "words": [w for _, _, w in pairs],
            "insufficient": False,
        }

    # ---------------------------------------------------------------- H2 / H3
    def run_delta(aram, pers, seed_a, seed_b, seed_c, nperm):
        d = delta(aram, pers)
        if d is None:
            return {"n_aram": len(aram), "n_pers": len(pers), "delta": None,
                    "insufficient": True}
        dA = null_A(aram, pers, seed_a, nperm)
        dB = null_B(aram, pers, seed_b, nperm)
        dC, under = null_C(aram, pers, seed_c, nperm)
        return {
            "n_aram": len(aram), "n_pers": len(pers), "delta": d,
            "mean_phi_aram": sum(t["phi"] for _, t in aram) / len(aram),
            "mean_phi_pers": sum(t["phi"] for _, t in pers) / len(pers),
            "median_tokens_aram": median([t["tokens"] for _, t in aram]),
            "median_tokens_pers": median([t["tokens"] for _, t in pers]),
            "p_null_A_label": perm_p(d, dA),
            "p_null_B_phase": perm_p(d, dB),
            "p_null_C_freq_stratified": perm_p(d, dC),
            "null_C_underpowered": under,
            "aram_words": [w for w, _ in aram], "pers_words": [w for w, _ in pers],
            "insufficient": False,
        }

    results = {}
    for tid in ("T1", "T2", "T3"):
        h1 = run_h1(tid, SEED_NULL_A, SEED_NULL_B, n_perm)

        s_items = [dict(e, _w=e["headword"]) for e in entries]
        a2, p2, exc2 = build_strata(suy_label, s_items, tid, suy_types, lambda x: x["_w"])
        h2 = run_delta(a2, p2, SEED_NULL_A, SEED_NULL_B, SEED_NULL_C, n_perm)
        h2["excluded_names_both_ARAM_and_PERS"] = exc2

        j_items = [dict(jef_by_key[k], _w=jef_by_key[k]["arabic_lemma"]) for k in overlap_keys]
        a3, p3, _ = build_strata(jef_label, j_items, tid, jef_types, lambda x: x["_w"])
        h3 = run_delta(a3, p3, SEED_NULL_A, SEED_NULL_B, SEED_NULL_C, n_perm)

        # prereg 10.1 -- declared descriptive: same words, only the rater changes
        s_items_ov = [dict(suy_by_key[k], _w=suy_by_key[k]["headword"]) for k in overlap_keys]
        a4, p4, _ = build_strata(suy_label, s_items_ov, tid, suy_types, lambda x: x["_w"])
        results[tid] = {
            "H1_rater_agreement": h1,
            "H2_delta_suyuti_full_roster": h2,
            "H3_delta_jeffery_overlap": h3,
            "DESCRIPTIVE_delta_suyuti_overlap": {
                "n_aram": len(a4), "n_pers": len(p4), "delta": delta(a4, p4),
                "gate": "none -- prereg 10, MW-7 ceiling if used inferentially",
            },
        }

    # ------------------------------------------------------ replication (+10)
    rep = {}
    for tid in ("T1",):
        rep["H1"] = run_h1(tid, SEED_NULL_A + REPLICATION_OFFSET,
                           SEED_NULL_B + REPLICATION_OFFSET, n_perm)
        s_items = [dict(e, _w=e["headword"]) for e in entries]
        a2, p2, _ = build_strata(suy_label, s_items, tid, suy_types, lambda x: x["_w"])
        rep["H2"] = run_delta(a2, p2, SEED_NULL_A + REPLICATION_OFFSET,
                              SEED_NULL_B + REPLICATION_OFFSET,
                              SEED_NULL_C + REPLICATION_OFFSET, n_perm)
        j_items = [dict(jef_by_key[k], _w=jef_by_key[k]["arabic_lemma"]) for k in overlap_keys]
        a3, p3, _ = build_strata(jef_label, j_items, tid, jef_types, lambda x: x["_w"])
        rep["H3"] = run_delta(a3, p3, SEED_NULL_A + REPLICATION_OFFSET,
                              SEED_NULL_B + REPLICATION_OFFSET,
                              SEED_NULL_C + REPLICATION_OFFSET, n_perm)

    # ==========================================================================
    # VERDICTS -- prereg 8, transcribed clause by clause
    #   "PASSES iff (i) the observed statistic's sign matches its locked
    #    direction in 4, AND (ii) EVERY null registered for it in 7 yields
    #    raw permutation p < 0.000625."
    #   "Otherwise the hypothesis is NULL."
    #   "If the observed sign is OPPOSITE to the locked direction, the verdict
    #    is 'NULL, REVERSED'."
    #   "A Null C reported UNDERPOWERED per 7 is EXCLUDED from clause (ii)."
    # All three locked directions in 4 are 'statistic > 0'.
    # ==========================================================================
    def verdict(stat, pvals, underpowered_excluded=None):
        if stat is None:
            return "NULL, INSUFFICIENT-DATA", None
        direction_ok = stat > 0                                   # 4: all locks are > 0
        gates = {k: v for k, v in pvals.items()
                 if not (underpowered_excluded and k == underpowered_excluded)}
        all_gates = all(p < RAW_GATE for p in gates.values())
        if direction_ok and all_gates:
            return "PASS", gates                                  # 8 clause (i) and (ii)
        if stat < 0:
            return "NULL, REVERSED", gates                        # 8: sign OPPOSITE the lock
        return "NULL", gates                                      # 8: "otherwise ... NULL"

    verdicts = {}
    for tid in ("T1", "T2", "T3"):
        r = results[tid]
        h1 = r["H1_rater_agreement"]
        if h1.get("insufficient"):
            verdicts.setdefault(tid, {})["H1"] = "NULL, INSUFFICIENT-DATA"
        else:
            v, _ = verdict(h1["kappa"], {"A": h1["p_null_A_permute_suyuti"],
                                         "B": h1["p_null_B_permute_jeffery"]})
            verdicts.setdefault(tid, {})["H1"] = v
        for hk, name in (("H2_delta_suyuti_full_roster", "H2"),
                         ("H3_delta_jeffery_overlap", "H3")):
            h = r[hk]
            if h.get("insufficient"):
                verdicts[tid][name] = "NULL, INSUFFICIENT-DATA"
                continue
            pv = {"A": h["p_null_A_label"], "B": h["p_null_B_phase"],
                  "C": h["p_null_C_freq_stratified"]}
            v, _ = verdict(h["delta"], pv,
                           underpowered_excluded="C" if h["null_C_underpowered"] else None)
            if h["null_C_underpowered"]:
                v += " (Null C UNDERPOWERED, excluded from gate per prereg 7)"
            verdicts[tid][name] = v

    # ------------------------------------------------ descriptive: prereg 10.4
    suy_keys = set(suy_by_key)
    flag_check = Counter()
    for r in registry:
        k = jkey(r["arabic_lemma"], False)
        flag_check[(r["suyuti_naw_38_attested"], k in suy_keys)] += 1

    payload = {
        "id": "H-NEW-3020",
        "prereg": rel["prereg"],
        "prereg_sha256": shas["prereg"],
        "input_sha256": shas,
        "utc": datetime.now(timezone.utc).isoformat(),
        "n_permutations": n_perm,
        "tests_in_family": TESTS_IN_FAMILY,
        "alpha_bonferroni": ALPHA_BON,
        "corrected_novelty_gate": CORRECTED_GATE,
        "raw_p_gate": RAW_GATE,
        "seeds": {"A": SEED_NULL_A, "B": SEED_NULL_B, "C": SEED_NULL_C,
                  "replication_offset": REPLICATION_OFFSET},
        "SMOKE_RUN": smoke,
        "A_nuisance_channels_prereg_6": nuisance,
        "B_census_prereg_2_and_10": census,
        "C_join": {
            "suyuti_roster_join": dict(suy_join),
            "jeffery_registry_join": dict(jef_join),
            "suyuti_types_resolved": len(suy_types),
            "jeffery_types_resolved": len(jef_types),
            "overlap_join_keys": len(overlap_keys),
        },
        "D_results_by_tuple": results,
        "E_verdicts": verdicts,
        "F_replication_seed_plus_10_T1": rep,
        "G_descriptive_registry_flag_vs_extracted_roster": {
            f"flag={a}|in_extracted_roster={b}": c for (a, b), c in flag_check.items()
        },
        "python": platform.python_version(),
    }

    # ----------------------------------------------- immutable run directory
    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    base = Path(args.out) if smoke else repo / "findings/phase-b-hypotheses/runs/h-new-3020"
    run_dir = base / stamp
    os.makedirs(run_dir, exist_ok=False)          # STANDING RULE 2026-08-08 3
    with open(run_dir / "result.json", "x", encoding="utf-8") as fh:
        json.dump(payload, fh, ensure_ascii=False, indent=2)
    try:
        head = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=repo,
                                       text=True).strip()
    except Exception:
        head = None
    manifest = {
        "id": "H-NEW-3020", "utc": stamp, "git_head": head,
        "inputs": rel, "input_sha256": shas,
        "run_dir": f"findings/phase-b-hypotheses/runs/h-new-3020/{stamp}/",
        "n_permutations": n_perm, "SMOKE_RUN": smoke,
    }
    with open(run_dir / "manifest.json", "x", encoding="utf-8") as fh:
        json.dump(manifest, fh, ensure_ascii=False, indent=2)
    print(f"[3020] wrote {run_dir}", file=sys.stderr)
    print(json.dumps({"nuisance": nuisance, "verdicts": verdicts}, ensure_ascii=False,
                     indent=2))


if __name__ == "__main__":
    main()
