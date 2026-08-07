#!/usr/bin/env python3
"""H-NEW-2610: do the Sajāwandī waqf grades encode an ordered boundary hierarchy,
and do they carry prosody beyond syntax?

Runner only. Emits no interpretation. See
findings/phase-b-hypotheses/prereg-h-new-2610-waqf-prosody.md
"""

import argparse
import csv
import hashlib
import json
import math
import platform
import random
import re
import shlex
import subprocess
import sys
from bisect import bisect_left, bisect_right
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path

# --- prereg §4: frozen inputs, verified at runtime -------------------------
EXPECTED_PREREG_SHA = "d776473ea75dd6500ac4c204ac47fce534e59ab7de78caefac2b963746891b80"
EXPECTED_FULL_SHA = "382a7341300602ec8b366316d4bbe2a44955c2bf984d395bdd82dae6110b6715"
EXPECTED_MIN_SHA = "87aaab41f78d1b148c8051b8afc1ee5fa66fd6d45f2f7a2984e3f9192c458b36"
EXPECTED_QAC_SHA = "a1d12923815341face765083805d2148ed2d9f5cc3f7d6665219d887675d8c46"
EXPECTED_EQTB_SHA = "a303c24cf51b90f6cd5eb0fb25d6c591977a7797743d16e0dedc76a5af5ae0b7"
EXPECTED_2240_SHA = "cce458614dec9aa75c30faa3b46eab8d748d60aeea1caf83a47253bdbade7a88"
EXPECTED_2500_SHA = "a63aef25086205891b44215897f9e09862e5cdd1e3ab2ee59ac4d15768309d25"
EXPECTED_2530_SHA = "5ca17050c20b15734ad9a734e7bad7b938b616c924ec53dfcd24814a1473b68c"

# --- prereg §6/§7: seeds, permutations, gates ------------------------------
N_PERM = 10_000
TESTS_IN_FAMILY = 8
ALPHA_BON = 0.05 / TESTS_IN_FAMILY          # 0.00625
CORRECTED_GATE = 0.005                       # statistical-rigor-protocol §170
RAW_GATE = CORRECTED_GATE / TESTS_IN_FAMILY  # 0.000625
SEEDS = {
    "h1a_null_a": 20260509, "h1a_null_b": 20260510,
    "h1b_null_a": 20260509, "h1b_null_b": 20260510,
    "h2_null_a": 20260511, "h2_null_b": 20260512,
    "h3_null_a": 20260513, "h3_null_b": 20260514,
    "control_sample": 20260515,
}
REPLICATION_OFFSET = 10  # prereg §7: seeds +10

# --- prereg §3: the locked ladder -----------------------------------------
GRADE_RANK = {0x06D6: 1, 0x06DA: 2, 0x06D7: 3, 0x06D8: 4}
GRADE_NAME = {1: "sla_wasl_awla", 2: "jim_jaiz", 3: "qla_waqf_awla", 4: "meem_lazim"}
EXCLUDED_MARKS = {0x06DB: "muanaqa", 0x06DC: "saktah"}
LA_MARK = 0x06D9  # prereg §8.1: min-tashkeel only
# prereg §6 H3: the locked trend order. h-new-2530's "classes" field is a listing,
# not an ordering; labels are reused verbatim but the order is the registered one.
LOCKED_H3_ORDER = ["eschatological_mufassal", "narrative", "legal_medinan"]
WAQF_RANGE = range(0x06D6, 0x06EE)

# prereg §2.3: the 10 verses where full-tashkeel word segmentation differs from QAC/EQTB
DISCREPANT_VERSES = {(2, 72), (2, 181), (8, 6), (13, 37), (15, 7),
                     (27, 20), (36, 22), (37, 130), (37, 164), (41, 47)}

# --- prereg §5.3: classify() ported VERBATIM from h-new-2240.py:49-120 -----
DAGGER_ALIF = "ٰ"
TA_MARBUTA = "ة"
HAMZA = "ء"
STRIP_MARKS = set([
    "ً", "ٌ", "ٍ",
    "َ", "ُ", "ِ",
    "ّ", "ْ",
    "ٓ", "ٔ", "ٕ",
    "ـ",
    "ۛ", "ۜ", "۝", "۞", "۟", "۠", "ۡ", "ۢ",
    "ۣ", "ۤ", "ۥ", "ۦ", "ۧ", "ۨ", "۩", "۪",
    "۫", "۬", "ۭ",
    "‌", "‍", "‎", "‏",
])
HAMZA_CARRIERS = {"ؤ", "ئ", "أ", "إ", "آ"}


def clean_word(w):
    """h-new-2240.py clean_final_word, applied to a single supplied word."""
    out = []
    for ch in w:
        if ch == DAGGER_ALIF:
            out.append("ا")
        elif ch in STRIP_MARKS or ord(ch) in WAQF_RANGE:
            continue
        else:
            out.append(ch)
    return "".join(out)


def classify(word):
    """Deterministic pausal-rime assonance class. h-new-2240.py:83-120 verbatim."""
    w = clean_word(word)
    if not w:
        return ("∅", "other")
    if w[-1] == TA_MARBUTA:
        return ("-ah", "ah")
    last = w[-1]
    prev = w[-2] if len(w) >= 2 else ""
    if last in ("ا", "ى"):
        return ("-ā", "open-ā")
    if last == "و":
        return ("-ū", "open-other")
    if last == "ي":
        return ("-ī", "open-other")
    if last == HAMZA or last in HAMZA_CARRIERS:
        if prev in ("ا",):
            return ("-āʾ", "ā-rime")
        if prev == "و":
            return ("-ūʾ", "open-other")
        if prev == "ي":
            return ("-īʾ", "open-other")
        return ("-ʾ", "other")
    rawi = last
    if prev in ("ا",):
        return ("-ā" + rawi, "ā-rime")
    if prev == "و":
        return ("-ū" + rawi, "ū-rime")
    if prev == "ي":
        return ("-ī" + rawi, "ī-rime")
    return ("-" + rawi, "short")


# --- prereg §5.1: VBR type normalisation ----------------------------------
def norm_type(w):
    out = []
    for ch in w:
        o = ord(ch)
        if o in (0x0670, 0x0671):
            out.append("ا")
        elif 0x0621 <= o <= 0x064A or o in (0x0649, 0x0629):
            out.append(ch)
    return "".join(out)


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


# --- statistics ------------------------------------------------------------
def rankdata(xs):
    """Average ranks, ties handled."""
    order = sorted(range(len(xs)), key=lambda i: xs[i])
    ranks = [0.0] * len(xs)
    i = 0
    while i < len(order):
        j = i
        while j + 1 < len(order) and xs[order[j + 1]] == xs[order[i]]:
            j += 1
        avg = (i + j) / 2.0 + 1.0
        for k in range(i, j + 1):
            ranks[order[k]] = avg
        i = j + 1
    return ranks


def pearson(xs, ys):
    n = len(xs)
    if n < 2:
        return float("nan")
    mx = sum(xs) / n
    my = sum(ys) / n
    sxy = sum((a - mx) * (b - my) for a, b in zip(xs, ys))
    sxx = sum((a - mx) ** 2 for a in xs)
    syy = sum((b - my) ** 2 for b in ys)
    if sxx <= 0 or syy <= 0:
        return float("nan")
    return sxy / math.sqrt(sxx * syy)


def spearman(xs, ys):
    return pearson(rankdata(xs), rankdata(ys))


def stratified_cov(groups, ranks, values):
    """prereg §6 H2: sum_s n_s*cov_s(g,y) / sum_s n_s."""
    by = defaultdict(list)
    for g, r, v in zip(groups, ranks, values):
        by[g].append((r, v))
    num = den = 0.0
    for cells in by.values():
        n = len(cells)
        if n < 2:
            continue
        mr = sum(c[0] for c in cells) / n
        mv = sum(c[1] for c in cells) / n
        cov = sum((c[0] - mr) * (c[1] - mv) for c in cells) / n
        num += n * cov
        den += n
    return num / den if den else float("nan")


def jonckheere(values_by_group, order):
    """JT statistic: concordant cross-group pairs, ties 0.5. O(n log n)."""
    total = 0.0
    pre = [sorted(values_by_group.get(g, [])) for g in order]
    for a in range(len(order)):
        for b in range(a + 1, len(order)):
            ys = pre[b]
            nb = len(ys)
            for x in pre[a]:
                lo = bisect_left(ys, x)
                hi = bisect_right(ys, x)
                total += (nb - hi) + 0.5 * (hi - lo)
    return total


def perm_p(obs, draws):
    """One-sided, locked direction, larger-is-more-extreme."""
    return (1 + sum(1 for d in draws if d >= obs)) / (len(draws) + 1)


def block_index(blocks):
    """Precompute permutable position groups once (blocks of size 1 are inert)."""
    idx = defaultdict(list)
    for i, b in enumerate(blocks):
        idx[b].append(i)
    return [p for p in idx.values() if len(p) > 1]


def block_shuffle(labels, groups, rng):
    """Permute labels within each precomputed position group."""
    out = list(labels)
    for positions in groups:
        vals = [out[i] for i in positions]
        rng.shuffle(vals)
        for i, v in zip(positions, vals):
            out[i] = v
    return out


# --- loaders ---------------------------------------------------------------
LOC_RE = re.compile(r"\((\d+):(\d+):(\d+):(\d+)\)")


def load_quran(path):
    return json.load(open(path, encoding="utf-8"))


def build_junctures(quran, grade_map, la_rank=None):
    """Every verse-internal juncture; tag those carrying a grade mark."""
    verses = {}
    for s in quran:
        for v in s["verses"]:
            verses[(s["id"], v["id"])] = v["text"].split()
    juncts = []
    for (c, v), words in sorted(verses.items()):
        for i in range(len(words) - 1):
            wl, wr = words[i], words[i + 1]
            marks = [ord(ch) for ch in wl if ord(ch) in WAQF_RANGE]
            g = [grade_map[m] for m in marks if m in grade_map]
            other = [EXCLUDED_MARKS[m] for m in marks if m in EXCLUDED_MARKS]
            juncts.append({
                "surah": c, "verse": v, "word": i + 1,
                "w_left": wl, "w_right": wr,
                "grade": g[0] if len(g) == 1 else None,
                "n_grade_marks": len(g),
                "other_mark": other[0] if other else None,
                "pos_norm": (i + 1) / len(words),
            })
    return verses, juncts


def compute_vbr(verses, juncts):
    """prereg §5.1."""
    f_end, f_beg, n_type = Counter(), Counter(), Counter()
    for words in verses.values():
        for w in words:
            n_type[norm_type(w)] += 1
        f_end[norm_type(words[-1])] += 1
        f_beg[norm_type(words[0])] += 1
    for j in juncts:
        tl, tr = norm_type(j["w_left"]), norm_type(j["w_right"])
        j["vbr"] = (math.log((f_end[tl] + 0.5) / (n_type[tl] - 1 + 1.0))
                    + math.log((f_beg[tr] + 0.5) / (n_type[tr] - 1 + 1.0)))
    return {"n_types": len(n_type)}


def load_eqtb(path):
    """Real tokens ordered corpus-linearly; dependency edges within sentences."""
    rows = []
    with open(path, encoding="utf-16", newline="") as fh:
        for r in csv.DictReader(fh, delimiter="\t"):
            if r["location"] == "_":
                continue
            rows.append((int(r["chapter_id"]), int(r["verse_id"]), int(r["word_id"]),
                         int(r["tok_id"]), int(r["sentence_id"]), int(r["token_id"]),
                         r["ref_token_id"]))
    rows.sort(key=lambda t: (t[0], t[1], t[2], t[3]))
    lin = {}
    last_tok_of_word = {}
    for i, t in enumerate(rows):
        lin[(t[4], t[5])] = i
        last_tok_of_word[(t[0], t[1], t[2])] = i
    edges = []
    for t in rows:
        ref = t[6]
        if not ref or ref in {"_", "-1"}:
            continue
        head = (t[4], int(ref))
        if head in lin:
            a, b = lin[(t[4], t[5])], lin[head]
            if a != b:
                edges.append((min(a, b), max(a, b)))
    return rows, lin, last_tok_of_word, edges


def crossing_counts(cuts, edges, n_tokens):
    """XC via difference array: edge (a,b) covers cuts a..b-1."""
    diff = [0] * (n_tokens + 2)
    for a, b in edges:
        diff[a] += 1
        diff[b] -= 1
    run = 0
    cover = [0] * (n_tokens + 2)
    for i in range(n_tokens + 1):
        run += diff[i]
        cover[i] = run
    return {c: cover[c] for c in cuts}


def load_qac_wordcounts(path):
    wc = defaultdict(int)
    with open(path, encoding="utf-8") as fh:
        for line in fh:
            if line.startswith("#") or line.startswith("LOCATION") or not line.strip():
                continue
            f = line.rstrip("\n").split("\t")
            if len(f) != 4:
                continue
            m = LOC_RE.fullmatch(f[0])
            if m:
                k = (int(m[1]), int(m[2]))
                wc[k] = max(wc[k], int(m[3]))
    return wc


def main():
    global N_PERM
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo", default=".")
    ap.add_argument("--eqtb", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--perms", type=int, default=N_PERM,
                    help="permutation count; anything other than 10000 marks the "
                         "run SMOKE and its p-values are not interpretable")
    args = ap.parse_args()
    N_PERM = args.perms
    smoke = (N_PERM != 10_000)
    repo = Path(args.repo).resolve()
    fp = lambda p: str(repo / p)

    # ---- prereg §4: gate on every hash ------------------------------------
    prereg = fp("findings/phase-b-hypotheses/prereg-h-new-2610-waqf-prosody.md")
    hashes = {
        "prereg": require(prereg, EXPECTED_PREREG_SHA, "prereg"),
        "quran_full_tashkeel": require(fp("quran-text/quran-full-tashkeel.json"),
                                       EXPECTED_FULL_SHA, "full-tashkeel"),
        "quran_min_tashkeel": require(fp("quran-text/quran-min-tashkeel.json"),
                                      EXPECTED_MIN_SHA, "min-tashkeel"),
        "qac_v04": require(fp("data/morphology/quranic-corpus-morphology-0.4.txt"),
                           EXPECTED_QAC_SHA, "QAC"),
        "eqtb_quranic_csv": require(args.eqtb, EXPECTED_EQTB_SHA, "EQTB"),
        "h_new_2240": require(fp("findings/phase-b-hypotheses/csv/h-new-2240.json"),
                              EXPECTED_2240_SHA, "h-new-2240"),
        "h_new_2500": require(fp("findings/phase-b-hypotheses/csv/h-new-2500.json"),
                              EXPECTED_2500_SHA, "h-new-2500"),
        "h_new_2530": require(fp("findings/phase-b-hypotheses/csv/h-new-2530.json"),
                              EXPECTED_2530_SHA, "h-new-2530"),
    }
    hashes["script"] = sha256(__file__)

    res = {"id": "H-NEW-2610", "prereg_sha256": hashes["prereg"],
           "SMOKE_RUN": smoke, "n_perm": N_PERM, "tests_in_family": TESTS_IN_FAMILY,
           "alpha_bonferroni": ALPHA_BON, "raw_gate": RAW_GATE,
           "corrected_gate": CORRECTED_GATE, "seeds": SEEDS}

    # ---- corpus + junctures ----------------------------------------------
    quran = load_quran(fp("quran-text/quran-full-tashkeel.json"))
    verses, juncts = build_junctures(quran, GRADE_RANK)
    census = Counter()
    for s in quran:
        for v in s["verses"]:
            for ch in v["text"]:
                if ord(ch) in WAQF_RANGE:
                    census[hex(ord(ch))] += 1
    res["glyph_census_full_tashkeel"] = dict(sorted(census.items()))
    res["corpus"] = {"surahs": len(quran), "verses": len(verses),
                     "words": sum(len(w) for w in verses.values()),
                     "verse_internal_junctures": len(juncts)}

    marked = [j for j in juncts if j["grade"] is not None]
    multi = [j for j in juncts if j["n_grade_marks"] > 1]
    res["eligible_loci"] = {"n": len(marked),
                            "by_grade": dict(sorted(Counter(j["grade"] for j in marked).items())),
                            "grade_names": GRADE_NAME,
                            "junctures_with_multiple_grade_marks": len(multi),
                            "excluded_saktah": sum(1 for j in juncts if j["other_mark"] == "saktah"),
                            "excluded_muanaqa": sum(1 for j in juncts if j["other_mark"] == "muanaqa")}

    vbr_meta = compute_vbr(verses, juncts)
    res["vbr_meta"] = vbr_meta

    # ---- EQTB channel -----------------------------------------------------
    qac_wc = load_qac_wordcounts(fp("data/morphology/quranic-corpus-morphology-0.4.txt"))
    rows, lin, last_tok, edges = load_eqtb(args.eqtb)
    eqtb_wc = defaultdict(int)
    for t in rows:
        eqtb_wc[(t[0], t[1])] = max(eqtb_wc[(t[0], t[1])], t[2])
    disagree = [k for k in qac_wc if qac_wc[k] != eqtb_wc.get(k)]
    if disagree:
        raise SystemExit(f"ABORT: EQTB/QAC word-count disagreement on {len(disagree)} verses "
                         f"(prereg §5.2 requires 100%): {disagree[:10]}")
    res["eqtb"] = {"real_tokens": len(rows), "dependency_edges": len(edges),
                   "sentences": len({t[4] for t in rows}),
                   "qac_eqtb_wordcount_agreement": 1.0,
                   "verses_excluded_word_segmentation": sorted(DISCREPANT_VERSES)}

    dep_ok = [j for j in marked if (j["surah"], j["verse"]) not in DISCREPANT_VERSES]
    cuts = {last_tok[(j["surah"], j["verse"], j["word"])] for j in dep_ok}
    all_cuts = set()
    for j in juncts:
        k = (j["surah"], j["verse"], j["word"])
        if (j["surah"], j["verse"]) not in DISCREPANT_VERSES and k in last_tok:
            all_cuts.add(last_tok[k])
    xc_map = crossing_counts(all_cuts | cuts, edges, len(rows))
    for j in juncts:
        k = (j["surah"], j["verse"], j["word"])
        j["xc"] = xc_map.get(last_tok.get(k)) if (j["surah"], j["verse"]) not in DISCREPANT_VERSES else None
    res["eqtb"]["marked_loci_in_dep_channel"] = len(dep_ok)
    res["eqtb"]["marked_loci_dropped"] = len(marked) - len(dep_ok)

    # ---- H2 outcome: fāṣila rhyme match -----------------------------------
    j2240 = json.load(open(fp("findings/phase-b-hypotheses/csv/h-new-2240.json"), encoding="utf-8"))
    dom_2240 = {r["surah"]: r["dominant_class"] for r in j2240["per_surah"]}
    dom_mine = {}
    for s in quran:
        cnt = Counter(classify(v["text"].split()[-1])[0] for v in s["verses"])
        dom_mine[s["id"]] = cnt.most_common(1)[0][0]
    agree = sum(1 for k in dom_2240 if dom_2240[k] == dom_mine.get(k))
    agree_rate = agree / len(dom_2240)
    res["rhyme_instrument_control"] = {
        "n_surahs": len(dom_2240), "agreement": agree, "agreement_rate": agree_rate,
        "abort_threshold": 0.90,
        "disagreements": sorted(k for k in dom_2240 if dom_2240[k] != dom_mine.get(k)),
        "instrument_failure": agree_rate < 0.90}
    for j in juncts:
        j["rm"] = int(classify(j["w_left"])[0] == dom_2240.get(j["surah"]))

    # ---- descriptive calibration ladder (prereg §8.1) ---------------------
    def summ(sel, key):
        vals = [j[key] for j in sel if j.get(key) is not None]
        if not vals:
            return None
        n = len(vals)
        m = sum(vals) / n
        sd = math.sqrt(sum((v - m) ** 2 for v in vals) / n) if n > 1 else 0.0
        return {"n": n, "mean": m, "sd": sd, "median": sorted(vals)[n // 2]}

    verse_bound = []
    ordered = sorted(verses.items())
    for idx, ((c, v), words) in enumerate(ordered):
        if idx + 1 >= len(ordered):
            continue
        nxt = ordered[idx + 1][1]
        vb = {"w_left": words[-1], "w_right": nxt[0], "surah": c}
        verse_bound.append(vb)
    f_end, f_beg, n_type = Counter(), Counter(), Counter()
    for words in verses.values():
        for w in words:
            n_type[norm_type(w)] += 1
        f_end[norm_type(words[-1])] += 1
        f_beg[norm_type(words[0])] += 1
    for vb in verse_bound:
        tl, tr = norm_type(vb["w_left"]), norm_type(vb["w_right"])
        vb["vbr"] = (math.log((f_end[tl] - 1 + 0.5) / (n_type[tl] - 1 + 1.0))
                     + math.log((f_beg[tr] - 1 + 0.5) / (n_type[tr] - 1 + 1.0)))
    unmarked = [j for j in juncts if j["grade"] is None and j["other_mark"] is None]
    rng_ctl = random.Random(SEEDS["control_sample"])
    ctl = rng_ctl.sample(unmarked, min(len(marked), len(unmarked)))
    ladder = {"verse_boundary": {"vbr": summ(verse_bound, "vbr")},
              "unmarked_junctures": {"vbr": summ(unmarked, "vbr"),
                                     "xc": summ(unmarked, "xc"),
                                     "rm_rate": sum(j["rm"] for j in unmarked) / len(unmarked)},
              "matched_control_sample": {"vbr": summ(ctl, "vbr"), "xc": summ(ctl, "xc"),
                                         "rm_rate": sum(j["rm"] for j in ctl) / len(ctl)}}
    for r in (1, 2, 3, 4):
        sel = [j for j in marked if j["grade"] == r]
        ladder[GRADE_NAME[r]] = {"rank": r, "n": len(sel),
                                 "vbr": summ(sel, "vbr"), "xc": summ(sel, "xc"),
                                 "rm_rate": sum(j["rm"] for j in sel) / len(sel),
                                 "pos_norm": summ(sel, "pos_norm")}
    for code, nm in EXCLUDED_MARKS.items():
        sel = [j for j in juncts if j["other_mark"] == nm]
        if sel:
            ladder[nm + "_excluded"] = {"n": len(sel), "vbr": summ(sel, "vbr"),
                                        "xc": summ(sel, "xc")}
    res["calibration_ladder"] = ladder

    # ---- H1a / H1b --------------------------------------------------------
    def run_spearman(sel, key, sign, seed_a, seed_b):
        """Spearman rho(grade_rank, instrument), two permutation schemes.

        Fast path: rho = pearson(rank(g), rank(y)). rank(y) is fixed; permuting g
        permutes rank(g) as the same multiset, so all Pearson normalisers are
        constant and rho is affine-increasing in S = sum(rg[i]*ry[i]). Permuting
        therefore only needs S. Verified against the general path below.
        """
        g = [j["grade"] for j in sel]
        y = [j[key] for j in sel]
        blocks = block_index([j["surah"] for j in sel])
        rho = spearman(g, y)
        rg = rankdata(g)
        ry = rankdata(y)
        obs_S = sign * sum(a * b for a, b in zip(rg, ry))
        # equivalence check between fast path and the general statistic
        assert abs(pearson(rg, ry) - rho) < 1e-9, "rank/pearson identity broken"
        out = {"n": len(sel), "spearman_rho": rho, "locked_sign": sign,
               "statistic_S_signed": obs_S}
        for nm, seed, blk in (("null_a", seed_a, None), ("null_b", seed_b, blocks)):
            for tag, sd in [("", seed), ("_replication", seed + REPLICATION_OFFSET)]:
                rng = random.Random(sd)
                draws = []
                for _ in range(N_PERM):
                    if blk is None:
                        rp = rg[:]
                        rng.shuffle(rp)
                    else:
                        rp = block_shuffle(rg, blk, rng)
                    draws.append(sign * sum(a * b for a, b in zip(rp, ry)))
                p = perm_p(obs_S, draws)
                p_opp = (1 + sum(1 for d in draws if d <= obs_S)) / (len(draws) + 1)
                out[nm + tag] = {"seed": sd, "p_raw": p,
                                 "p_bonferroni": min(1.0, TESTS_IN_FAMILY * p),
                                 "passes_gate": p < RAW_GATE,
                                 "p_raw_opposite_tail_POSTHOC_MW7": p_opp}
        out["direction_matches_lock"] = (sign * rho) > 0
        out["PASS"] = (out["direction_matches_lock"]
                       and out["null_a"]["passes_gate"] and out["null_b"]["passes_gate"])
        return out

    res["H1a_vbr"] = run_spearman(marked, "vbr", +1,
                                  SEEDS["h1a_null_a"], SEEDS["h1a_null_b"])
    res["H1b_xc"] = run_spearman(dep_ok, "xc", -1,
                                 SEEDS["h1b_null_a"], SEEDS["h1b_null_b"])

    # prereg §8.5: H1a with lāzim dropped
    res["H1a_without_lazim"] = {
        "spearman_rho": spearman([j["grade"] for j in marked if j["grade"] != 4],
                                 [j["vbr"] for j in marked if j["grade"] != 4]),
        "n": sum(1 for j in marked if j["grade"] != 4), "gated": False}

    # ---- H2 ---------------------------------------------------------------
    h2 = [j for j in dep_ok if j["xc"] is not None]
    strata = [min(j["xc"], 6) for j in h2]
    g2 = [j["grade"] for j in h2]
    y2 = [j["rm"] for j in h2]
    obs2 = stratified_cov(strata, g2, y2)
    h2res = {"n": len(h2), "strata_buckets": sorted(set(strata)),
             "statistic_T": obs2, "locked_direction": "T > 0",
             "instrument_failure": res["rhyme_instrument_control"]["instrument_failure"],
             "rm_rate_overall": sum(y2) / len(y2),
             "by_stratum": {}}
    for s in sorted(set(strata)):
        sel = [(g, y) for st, g, y in zip(strata, g2, y2) if st == s]
        h2res["by_stratum"][str(s)] = {"n": len(sel),
                                       "rm_rate": sum(y for _, y in sel) / len(sel),
                                       "mean_grade": sum(g for g, _ in sel) / len(sel)}
    # Fast path: strata membership and within-stratum g composition are fixed under
    # both schemes (Null B blocks refine Null A blocks), so n_s, gbar_s and ybar_s are
    # constant and T is affine-increasing in sum_i g_i*y_i over non-degenerate strata.
    strat_n = Counter(strata)
    keep = {s for s, n in strat_n.items() if n >= 2}
    idx_keep = [i for i, s in enumerate(strata) if s in keep]
    obs_S2 = sum(g2[i] * y2[i] for i in idx_keep)
    blocks_a = block_index(strata)
    blocks_b = block_index([(j["surah"], min(j["xc"], 6)) for j in h2])
    # verify the fast path is affine-increasing in the registered statistic
    _rng = random.Random(999983)
    _pts = []
    for _ in range(3):
        _gp = block_shuffle(g2, blocks_a, _rng)
        _pts.append((sum(_gp[i] * y2[i] for i in idx_keep),
                     stratified_cov(strata, _gp, y2)))
    _pts.append((obs_S2, obs2))
    _s0, _t0 = _pts[0]
    _s1, _t1 = _pts[1]
    _slope = (_t1 - _t0) / (_s1 - _s0)
    assert _slope > 0, "H2 fast path is not increasing in the registered statistic"
    for _s, _t in _pts[2:]:
        assert abs((_t0 + _slope * (_s - _s0)) - _t) < 1e-9, "H2 fast path is not affine"
    for nm, seed, blk in (("null_a", SEEDS["h2_null_a"], blocks_a),
                          ("null_b", SEEDS["h2_null_b"], blocks_b)):
        for tag, sd in [("", seed), ("_replication", seed + REPLICATION_OFFSET)]:
            rng = random.Random(sd)
            draws = []
            for _ in range(N_PERM):
                gp = block_shuffle(g2, blk, rng)
                draws.append(sum(gp[i] * y2[i] for i in idx_keep))
            p = perm_p(obs_S2, draws)
            h2res[nm + tag] = {"seed": sd, "p_raw": p,
                               "p_bonferroni": min(1.0, TESTS_IN_FAMILY * p),
                               "passes_gate": p < RAW_GATE}
    h2res["statistic_S_fastpath"] = obs_S2
    h2res["direction_matches_lock"] = obs2 > 0
    h2res["PASS"] = (h2res["direction_matches_lock"] and not h2res["instrument_failure"]
                     and h2res["null_a"]["passes_gate"] and h2res["null_b"]["passes_gate"])
    res["H2_beyond_syntax"] = h2res

    # POST-HOC (MW-7, alpha ceiling 0.05, no replication, NOT gated, NOT a rescue):
    # added after the registered instrument control failed. Both the sura dominant
    # class and the pre-pause word class are computed from full-tashkeel by the same
    # ported classify(), removing the min/full orthographic mismatch that caused the
    # failure. This cannot substitute for the registered H2.
    y2sc = [int(classify(j["w_left"])[0] == dom_mine.get(j["surah"])) for j in h2]
    obs2sc = stratified_cov(strata, g2, y2sc)
    sc = {"POST_HOC": True, "gated": False, "MW7_alpha_ceiling": 0.05,
          "reason_added": "registered rhyme instrument control failed at "
                          "87.7 percent versus a 90 percent pre-registered threshold",
          "statistic_T": obs2sc, "rm_rate_overall": sum(y2sc) / len(y2sc),
          "direction_matches_H2_lock": obs2sc > 0}
    obs_S2sc = sum(g2[i] * y2sc[i] for i in idx_keep)
    for nm, seed, blk in (("null_a", SEEDS["h2_null_a"], blocks_a),
                          ("null_b", SEEDS["h2_null_b"], blocks_b)):
        rng = random.Random(seed)
        draws = []
        for _ in range(N_PERM):
            gp = block_shuffle(g2, blk, rng)
            draws.append(sum(gp[i] * y2sc[i] for i in idx_keep))
        sc[nm] = {"seed": seed, "p_raw": perm_p(obs_S2sc, draws)}
    res["H2_POSTHOC_self_consistent_rhyme"] = sc

    # prereg §8.7: alternative syntactic control = EQTB sentence-boundary status
    sent_of = {}
    for t in rows:
        sent_of.setdefault((t[0], t[1], t[2]), t[4])
    alt = []
    for j in h2:
        a = sent_of.get((j["surah"], j["verse"], j["word"]))
        b = sent_of.get((j["surah"], j["verse"], j["word"] + 1))
        alt.append(int(a != b) if a is not None and b is not None else 0)
    res["H2_alt_control_sentence_boundary"] = {
        "statistic_T": stratified_cov(alt, g2, y2), "gated": False,
        "n_at_sentence_boundary": sum(alt)}

    # ---- H3 ---------------------------------------------------------------
    j2500 = json.load(open(fp("findings/phase-b-hypotheses/csv/h-new-2500.json"), encoding="utf-8"))
    j2530 = json.load(open(fp("findings/phase-b-hypotheses/csv/h-new-2530.json"), encoding="utf-8"))
    members = j2500["genre_proxy"]["members"]
    classes_2530 = set(j2530["primary_3register"]["classes"])
    if classes_2530 != set(LOCKED_H3_ORDER):
        raise SystemExit(f"ABORT: register labels differ from prereg: "
                         f"{sorted(classes_2530)} vs {sorted(LOCKED_H3_ORDER)}")
    order3 = list(LOCKED_H3_ORDER)
    reg_of = {}
    for reg, ss in members.items():
        for s in ss:
            reg_of[s] = reg
    words_per_surah = Counter()
    marks_per_surah = Counter()
    verses_per_surah = Counter()
    for s in quran:
        for v in s["verses"]:
            words_per_surah[s["id"]] += len(v["text"].split())
            verses_per_surah[s["id"]] += 1
    for j in marked:
        marks_per_surah[j["surah"]] += 1
    dens = {s: 100.0 * marks_per_surah[s] / words_per_surah[s] for s in words_per_surah}
    surahs3 = sorted(s for s in reg_of if reg_of[s] in order3)
    labels3 = [reg_of[s] for s in surahs3]
    vals3 = [dens[s] for s in surahs3]
    by_group = defaultdict(list)
    for lab, v in zip(labels3, vals3):
        by_group[lab].append(v)
    obs3 = jonckheere(by_group, order3)
    h3 = {"registers_source": j2530["genre_proxy_source"], "order_locked": order3,
          "labels_verbatim_from": "h-new-2530.json primary_3register.classes",
          "n_surahs": len(surahs3), "statistic_JT": obs3,
          "per_register": {r: {"n": len(by_group[r]),
                               "mean_density_per_100w": sum(by_group[r]) / len(by_group[r]),
                               "median": sorted(by_group[r])[len(by_group[r]) // 2]}
                           for r in order3}}
    vc = sorted(surahs3, key=lambda s: verses_per_surah[s])
    tert = {}
    for i, s in enumerate(vc):
        tert[s] = 0 if i < len(vc) // 3 else (1 if i < 2 * len(vc) // 3 else 2)
    blocks3 = block_index([tert[s] for s in surahs3])
    for nm, seed, blk in (("null_a", SEEDS["h3_null_a"], None),
                          ("null_b", SEEDS["h3_null_b"], blocks3)):
        for tag, sd in [("", seed), ("_replication", seed + REPLICATION_OFFSET)]:
            rng = random.Random(sd)
            draws = []
            for _ in range(N_PERM):
                if blk:
                    lp = block_shuffle(labels3, blk, rng)
                else:
                    lp = labels3[:]
                    rng.shuffle(lp)
                bg = defaultdict(list)
                for lab, v in zip(lp, vals3):
                    bg[lab].append(v)
                draws.append(jonckheere(bg, order3))
            p = perm_p(obs3, draws)
            h3[nm + tag] = {"seed": sd, "p_raw": p,
                            "p_bonferroni": min(1.0, TESTS_IN_FAMILY * p),
                            "passes_gate": p < RAW_GATE}
    means = [h3["per_register"][r]["mean_density_per_100w"] for r in order3]
    h3["direction_matches_lock"] = means[0] < means[1] < means[2]
    h3["PASS"] = (h3["direction_matches_lock"]
                  and h3["null_a"]["passes_gate"] and h3["null_b"]["passes_gate"])
    h3["robustness_4class_means"] = {
        r: sum(dens[s] for s in ss) / len(ss) for r, ss in members.items()}
    # prereg §8.6: density residualised on mean verse length (descriptive)
    mvl = {s: words_per_surah[s] / verses_per_surah[s] for s in words_per_surah}
    xs = [mvl[s] for s in surahs3]
    mx, my = sum(xs) / len(xs), sum(vals3) / len(vals3)
    sxx = sum((x - mx) ** 2 for x in xs)
    beta = sum((x - mx) * (y - my) for x, y in zip(xs, vals3)) / sxx if sxx else 0.0
    resid = [y - (my + beta * (x - mx)) for x, y in zip(xs, vals3)]
    rg = defaultdict(list)
    for lab, r in zip(labels3, resid):
        rg[lab].append(r)
    h3["residualised_on_mean_verse_length"] = {
        "beta": beta, "r_density_vs_mean_verse_length": pearson(xs, vals3),
        "mean_residual_by_register": {r: sum(rg[r]) / len(rg[r]) for r in order3},
        "gated": False}
    res["H3_register"] = h3

    # ---- prereg §8.1: min-tashkeel rules-tuple sensitivity ----------------
    qmin = load_quran(fp("quran-text/quran-min-tashkeel.json"))
    grade5 = {LA_MARK: 1, 0x06D6: 2, 0x06DA: 3, 0x06D7: 4, 0x06D8: 5}
    vmin, jmin = build_junctures(qmin, grade5)
    compute_vbr(vmin, jmin)
    mmin = [j for j in jmin if j["grade"] is not None]
    cmin = Counter()
    for s in qmin:
        for v in s["verses"]:
            for ch in v["text"]:
                if ord(ch) in WAQF_RANGE:
                    cmin[hex(ord(ch))] += 1
    res["sensitivity_min_tashkeel_5rung"] = {
        "gated": False,
        "glyph_census": dict(sorted(cmin.items())),
        "ladder": {"1": "la_mamnu (U+06D9)", "2": "sla", "3": "jim", "4": "qla", "5": "meem_lazim"},
        "n": len(mmin),
        "by_grade": dict(sorted(Counter(j["grade"] for j in mmin).items())),
        "spearman_rho_vbr": spearman([j["grade"] for j in mmin], [j["vbr"] for j in mmin]),
        "note": "min-tashkeel carries a different Sajawandi apparatus and a different "
                "word segmentation; see prereg section 2.6 and 8.1"}

    # ---- pairwise contrasts (prereg §8.4, NOT gated) ----------------------
    pc = {}
    for a, b in ((1, 2), (2, 3), (3, 4)):
        xa = [j["vbr"] for j in marked if j["grade"] == a]
        xb = [j["vbr"] for j in marked if j["grade"] == b]
        pc[f"{GRADE_NAME[a]}_vs_{GRADE_NAME[b]}"] = {
            "n_a": len(xa), "n_b": len(xb),
            "mean_vbr_a": sum(xa) / len(xa), "mean_vbr_b": sum(xb) / len(xb),
            "delta": sum(xb) / len(xb) - sum(xa) / len(xa)}
    res["pairwise_vbr_contrasts_ungated"] = pc

    res["verdict_inputs"] = {
        "H1a_PASS": res["H1a_vbr"]["PASS"], "H1b_PASS": res["H1b_xc"]["PASS"],
        "H2_PASS": res["H2_beyond_syntax"]["PASS"], "H3_PASS": res["H3_register"]["PASS"]}

    # ---- immutable run record (prereg §10) --------------------------------
    ts = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    outdir = Path(args.out) / ts
    if outdir.exists():
        raise SystemExit(f"ABORT: run directory already exists: {outdir}")
    outdir.mkdir(parents=True)
    (outdir / "result.json").write_text(json.dumps(res, ensure_ascii=False, indent=2),
                                        encoding="utf-8")
    try:
        commit = subprocess.run(["git", "-C", str(repo), "rev-parse", "HEAD"],
                                capture_output=True, text=True, check=True).stdout.strip()
    except Exception:
        commit = "UNAVAILABLE"
    manifest = {"id": "H-NEW-2610", "SMOKE_RUN": smoke, "utc": ts,
                "command": " ".join(shlex.quote(a) for a in sys.argv),
                "git_commit": commit, "python": sys.version,
                "platform": platform.platform(), "seeds": SEEDS,
                "n_perm": N_PERM, "sha256": hashes}
    (outdir / "manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2),
                                          encoding="utf-8")
    print(f"run dir: {outdir}")
    print(json.dumps(res["verdict_inputs"], indent=2))


if __name__ == "__main__":
    main()
