#!/usr/bin/env python3
"""
H-NEW-2850 — Does derivational verb form track the grammatical subject's agency class?

Pre-registered: findings/phase-b-hypotheses/prereg-h-new-2850-agency-grammar.md
Pre-reg SHA-256 verified at runtime; SystemExit on mismatch. Frozen inputs SHA-verified.

The subject classifiers NEVER receive the verb's derivational form as an argument, so they
cannot introduce a form-correlated bias by construction. The object channel is RULE-NEW of
H-NEW-2650 verbatim; the naive PGN-discard rule is not implemented anywhere in this file.

Two of the five arms are locked NEGATIVE. If they come out positive the pre-registration
commits this test to INSTRUMENT-CONFOUNDED and a NULL finding, whatever the other arms do.

Author: Waiel Al-Shujaa.
"""

import argparse
import collections
import csv
import datetime
import hashlib
import json
import math
import os
import random
import re
import sys

ROOT = "/Users/grey/Downloads/quran"
PREREG = os.path.join(ROOT, "findings/phase-b-hypotheses/prereg-h-new-2850-agency-grammar.md")
PREREG_SHA = "7e7e98f7a60617df76c42abf66547e639baebd6cd5801990f17e3ae5239b4f2c"
FROZEN = {
    "qac": (os.path.join(ROOT, "data/morphology/quranic-corpus-morphology-0.4.txt"),
            "a1d12923815341face765083805d2148ed2d9f5cc3f7d6665219d887675d8c46"),
    "revelation_order": (os.path.join(ROOT, "data/revelation-order.csv"),
                         "74f52ec1518abf8ecbf67671ee1cdd8e4cfc553fc8c5ead8274cc7dae8916fb7"),
    "quran_no_tashkeel": (os.path.join(ROOT, "quran-text/quran-no-tashkeel.json"),
                          "253f72f32f1dd4f6288c24be1b3b81b2e32c67aedd59aecb6e4a057dae35918a"),
}
EQTB_SHA = "a303c24cf51b90f6cd5eb0fb25d6c591977a7797743d16e0dedc76a5af5ae0b7"

SEED_PRIMARY, SEED_REPLICATION, N_PERM = 20260509, 20260519, 10000
BONF_K = 20                       # prereg §7.3: 5 arms x 2 classifiers x {uncond, cond}
ALPHA_BONF = 0.05 / BONF_K        # 0.0025
GATE = 0.0005                     # prereg §7.3: the binding project novelty gate
MIN_TOKENS = 2                    # prereg §7.1

# prereg §6 — arm, form A, form B, locked sign
ARMS = [("M1", "II", "V", "+"), ("M2", "I", "VIII", "+"), ("M3", "III", "VI", "+"),
        ("C1", "I", "II", "-"), ("C2", "I", "IV", "-")]
DESCRIPTIVE_ARMS = [("D1", "I", "VII", "+"), ("D2", "IV", "VII", "+")]
FORMS = ["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X", "XI", "XII"]
L_DIV = {"{ll~ah", "rab~", "raHoma`n"}          # prereg §4.1, closed
CAUSATIVE_MEMBERS = ("II", "IV")                 # prereg §10.2
MUTAWAA_MEMBERS = ("V", "VI", "VII", "VIII")


def sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def gate_inputs(eqtb_path):
    got = sha256(PREREG)
    if got != PREREG_SHA:
        raise SystemExit(f"PRE-REG TAMPERED: {got} != {PREREG_SHA}")
    print(f"[ok] pre-reg SHA-256 verified: {got}")
    for name, (path, expect) in sorted(FROZEN.items()):
        got = sha256(path)
        if got != expect:
            raise SystemExit(f"FROZEN INPUT {name} CHANGED: {got} != {expect}")
        print(f"[ok] frozen input {name}: {got[:16]}...")
    if eqtb_path:
        got = sha256(eqtb_path)
        if got != EQTB_SHA:
            raise SystemExit(f"EQTB CHANGED: {got} != {EQTB_SHA}")
        print(f"[ok] frozen input eqtb (SECONDARY, contamination-limited): {got[:16]}...")


# ----------------------------------------------------------------- QAC parsing
LOC_RE = re.compile(r"^\((\d+):(\d+):(\d+):(\d+)\)$")
AGR_RE = re.compile(r"(?<![A-Za-z0-9:])([123](?:[MF])?(?:[SDP]))(?![A-Za-z0-9])")
PRON_RE = re.compile(r"PRON:([^|]+)")
ROOT_RE = re.compile(r"ROOT:([^|\t]+)")
LEM_RE = re.compile(r"LEM:([^|\t]+)")
CASE_RE = re.compile(r"\|(NOM|ACC|GEN)\b")
FORM_RE = re.compile(r"\|\((I{1,3}|IV|V|VI|VII|VIII|IX|X|XI|XII)\)\|")


def strip_marks(f):
    return re.sub(r"[^A-Za-z]", "", f).lstrip("~")


def load_qac():
    words = collections.defaultdict(list)
    with open(FROZEN["qac"][0], encoding="utf-8") as fh:
        for line in fh:
            if not line.startswith("("):
                continue
            parts = line.rstrip("\n").split("\t")
            if len(parts) < 4:
                continue
            m = LOC_RE.match(parts[0])
            if not m:
                continue
            loc = tuple(int(x) for x in m.groups())
            words[loc[:3]].append((loc[3], parts[1], parts[2], parts[3]))
    for k in words:
        words[k].sort()
    verses = collections.defaultdict(list)
    for (s, v, w) in words:
        verses[(s, v)].append(w)
    for k in verses:
        verses[k].sort()
    return dict(words), dict(verses)


def word_single_case(words, key):
    """(case, lemma) if the word carries exactly one case-marked segment, else None."""
    segs = words[key]
    cased = [x for x in segs if CASE_RE.search(x[3])]
    if len(cased) != 1:
        return None
    c = cased[0]
    m = LEM_RE.search(c[3])
    return (CASE_RE.search(c[3]).group(1), m.group(1) if m else None)


def has_verb_seg(words, key):
    return any(x[2] == "V" for x in words[key])


def build_verbs(words, verses):
    """One record per verb segment. Explicit-subject fields computed with NO access to form."""
    out = []
    for (s, v) in sorted(verses):
        ws = verses[(s, v)]
        for wi, w in enumerate(ws):
            segs = words[(s, v, w)]
            for i, (idx, surface, tag, feat) in enumerate(segs):
                if tag != "V":
                    continue
                agrs = AGR_RE.findall(feat)
                if len(agrs) != 1:
                    raise SystemExit(f"agreement multiplicity != 1 at ({s}:{v}:{w}:{idx}): {feat}")
                fm, rm = FORM_RE.search(feat), ROOT_RE.search(feat)
                clitics = []
                for (idx2, f2, t2, ft2) in segs[i + 1:]:
                    if t2 != "PRON":
                        continue                    # EMPH / REL skipped, not terminators
                    pm = PRON_RE.search(ft2)
                    if pm:
                        clitics.append({"seg": idx2, "surface": f2,
                                        "kind": ft2.split("|")[0], "pgn": pm.group(1)})
                agr = agrs[0]
                fwd = bwd = None
                fwd_stop = None
                if agr[0] == "3":
                    for w2 in ws[wi + 1:]:                        # prereg §4.2
                        if has_verb_seg(words, (s, v, w2)):
                            fwd_stop = "VERB"
                            break
                        wc = word_single_case(words, (s, v, w2))
                        if wc is None:
                            continue
                        fwd_stop = wc[0]
                        if wc[0] == "NOM":
                            fwd = wc[1]
                        break
                    else:
                        fwd_stop = fwd_stop or "VERSE-END"
                    for w2 in reversed(ws[:wi]):                  # prereg §4.3 BWD
                        if has_verb_seg(words, (s, v, w2)):
                            break
                        wc = word_single_case(words, (s, v, w2))
                        if wc is None:
                            continue
                        if wc[0] == "NOM":
                            bwd = wc[1]
                        break
                out.append({
                    "loc": f"({s}:{v}:{w}:{idx})", "surah": s, "verse": v, "word": w, "seg": idx,
                    "wi": wi, "surface": surface,
                    "form": fm.group(1) if fm else "I",
                    "root": rm.group(1).strip() if rm else None,
                    "agr": agr,
                    "aspect": "PERF" if "|PERF" in feat else ("IMPV" if "|IMPV" in feat else "IMPF"),
                    "passive": "|PASS" in feat,
                    "clitics": clitics, "fwd": fwd, "bwd": bwd, "fwd_stop": fwd_stop,
                })
    # PROP: coordination propagation, within verse, identical agreement (prereg §4.3)
    byverse = collections.defaultdict(list)
    for r in out:
        byverse[(r["surah"], r["verse"])].append(r)
    for k in byverse:
        carry = None
        for r in sorted(byverse[k], key=lambda x: (x["wi"], x["seg"])):
            own = r["fwd"] or r["bwd"]
            if own:
                carry = (own, r["agr"])
                r["prop"] = None
            else:
                r["prop"] = carry[0] if (carry and carry[1] == r["agr"]) else None
    return out


# --------------------------------------------- subject classifiers (form-blind)
def s_expl(agr, fwd):
    """prereg §4.2. Signature carries no form argument, by design."""
    if agr[0] != "3" or fwd is None:
        return None, None, None
    return ("DIVINE" if fwd in L_DIV else "NONDIVINE"), "S-EXPL", fwd


def s_expl_ext(agr, fwd, bwd, prop):
    """prereg §4.3."""
    lab, rule, lem = s_expl(agr, fwd)
    if lab:
        return lab, rule, lem
    if agr[0] != "3":
        return None, None, None
    for cand, name in ((bwd, "S-EXPL-BWD"), (prop, "S-EXPL-PROP")):
        if cand is not None:
            return ("DIVINE" if cand in L_DIV else "NONDIVINE"), name, cand
    return None, None, None


def c_strict(v):
    return s_expl(v["agr"], v["fwd"])


def c_strict_ext(v):
    return s_expl_ext(v["agr"], v["fwd"], v["bwd"], v["prop"])


def c_wide(v):
    """prereg §4.4: S-EXPL -> S-1P -> S-2P."""
    lab, rule, lem = s_expl(v["agr"], v["fwd"])
    if lab:
        return lab, rule, lem
    if v["agr"] == "1P":
        return "DIVINE", "S-1P", None
    if v["agr"][0] == "2":
        return "NONDIVINE", "S-2P", None
    return None, None, None


def c_wide_ext(v):
    lab, rule, lem = c_strict_ext(v)
    if lab:
        return lab, rule, lem
    if v["agr"] == "1P":
        return "DIVINE", "S-1P", None
    if v["agr"][0] == "2":
        return "NONDIVINE", "S-2P", None
    return None, None, None


# ------------------------------------- RULE-NEW object channel (H-NEW-2650 §3)
def classify_clitic(f, p, s, g, a):
    b = strip_marks(f)
    if b[:1] in ("h", "k"):
        return "OBJECT", 1
    if b[:1] in ("t", "w", "y", "u"):
        return "SUBJECT", 2
    if p == "1S":
        return "OBJECT", 3
    if p == "1P":
        return ("SUBJECT", 4) if (s == 0 and g == "1P" and a == "PERF") else ("OBJECT", 4)
    return "SUBJECT", 5


def rule_new(v):
    s = 0
    for c in v["clitics"]:
        if c["kind"] != "SUFFIX":
            continue
        verdict, _ = classify_clitic(c["surface"], c["pgn"], s, v["agr"], v["aspect"])
        if verdict == "OBJECT":
            return True
        s += 1
    return False


# --------------------------------------------------------------- statistics
def log_comb(n, k):
    return math.lgamma(n + 1) - math.lgamma(k + 1) - math.lgamma(n - k + 1)


def sign_test_two_sided(n_pos, n_neg):
    n = n_pos + n_neg
    if n == 0:
        return 1.0
    k = max(n_pos, n_neg)
    tail = sum(math.exp(log_comb(n, i) - n * math.log(2.0)) for i in range(k, n + 1))
    return min(1.0, 2.0 * tail)


def weighted_T(cells):
    """prereg §7.2 — T = sum w_r (p_rA - p_rB) / sum w_r, smoothed."""
    num = den = 0.0
    for (ya, na, yb, nb) in cells:
        w = 2.0 * na * nb / (na + nb)
        num += w * ((ya + 0.5) / (na + 1) - (yb + 0.5) / (nb + 1))
        den += w
    return num / den if den else float("nan")


def macro_T(cells):
    d = [ya / na - yb / nb for (ya, na, yb, nb) in cells]
    return sum(d) / len(d) if d else float("nan")


def mh_or(cells):
    num = den = 0.0
    for (ya, na, yb, nb) in cells:
        a, b, c, d = ya, na - ya, yb, nb - yb
        n = a + b + c + d
        if n == 0:
            continue
        num += a * d / n
        den += b * c / n
    if den == 0:
        return "inf" if num > 0 else None       # JSON-safe; no non-finite literals in result.json
    return num / den


def cmh(strata):
    """Cochran-Mantel-Haenszel over 2x2 strata (a,b,c,d) = (A-div, A-nondiv, B-div, B-nondiv)."""
    S_a = S_E = S_V = 0.0
    used = 0
    for (a, b, c, d) in strata:
        n = a + b + c + d
        if n < 2:
            continue
        r1, r2, c1, c2 = a + b, c + d, a + c, b + d
        if r1 == 0 or r2 == 0 or c1 == 0 or c2 == 0:
            continue
        S_a += a
        S_E += r1 * c1 / n
        S_V += r1 * r2 * c1 * c2 / (n * n * (n - 1))
        used += 1
    if S_V <= 0:
        return {"or_cmh": None, "chi2": None, "p": None, "strata_used": used}
    chi2 = (abs(S_a - S_E) - 0.5) ** 2 / S_V
    p = math.erfc(math.sqrt(chi2 / 2.0))
    return {"or_cmh": mh_or([(a, a + b, c, c + d) for (a, b, c, d) in strata]),
            "chi2": chi2, "p": p, "strata_used": used, "sum_a": S_a, "sum_E": S_E}


def null_b(cells, t_obs, seed, n_perm=N_PERM):
    """prereg §7.2 — margin-preserving token-label permutation within each root."""
    rng = random.Random(seed)
    ge = le = extreme = 0
    labels = []
    for (ya, na, yb, nb) in cells:
        labels.append([1] * (ya + yb) + [0] * (na + nb - ya - yb))
    for _ in range(n_perm):
        perm_cells = []
        for k, (ya, na, yb, nb) in enumerate(cells):
            lab = labels[k][:]
            rng.shuffle(lab)
            perm_cells.append((sum(lab[:na]), na, sum(lab[na:]), nb))
        t = weighted_T(perm_cells)
        if t >= t_obs:
            ge += 1
        if t <= t_obs:
            le += 1
        if abs(t) >= abs(t_obs):
            extreme += 1
    return {"p_ge": (ge + 1) / (n_perm + 1), "p_le": (le + 1) / (n_perm + 1),
            "p_two_sided": (extreme + 1) / (n_perm + 1), "n_perm": n_perm}


# ------------------------------------------------------------------ analysis
def arm_stats(rows, fa, fb, locked, seed, min_tokens=MIN_TOKENS, run_null=True,
              strat_key=None):
    """rows: list of dicts with root, form, divine(0/1), and optionally a stratifier."""
    by = collections.defaultdict(lambda: {fa: [], fb: []})
    for r in rows:
        if r["form"] in (fa, fb):
            by[r["root"]][r["form"]].append(r)
    cells, roots, strata = [], [], []
    n_pos = n_neg = n_tie = 0
    ya = na = yb = nb = 0
    for rt in sorted(by):
        A, B = by[rt][fa], by[rt][fb]
        if len(A) < min_tokens or len(B) < min_tokens:
            continue
        a1, b1 = sum(x["divine"] for x in A), sum(x["divine"] for x in B)
        cells.append((a1, len(A), b1, len(B)))
        pa, pb = a1 / len(A), b1 / len(B)
        roots.append({"root": rt, "n_a": len(A), "y_a": a1, "p_a": pa,
                      "n_b": len(B), "y_b": b1, "p_b": pb, "diff": pa - pb})
        ya += a1; na += len(A); yb += b1; nb += len(B)
        if pa > pb:
            n_pos += 1
        elif pa < pb:
            n_neg += 1
        else:
            n_tie += 1
        if strat_key:
            for sv in (0, 1):
                As = [x for x in A if x[strat_key] == sv]
                Bs = [x for x in B if x[strat_key] == sv]
                if not As or not Bs:
                    continue
                aa = sum(x["divine"] for x in As); bb = len(As) - aa
                cc = sum(x["divine"] for x in Bs); dd = len(Bs) - cc
                strata.append((aa, bb, cc, dd))
    out = {
        "form_a": fa, "form_b": fb, "locked_sign": locked, "n_roots": len(roots),
        "tokens_a": na, "divine_a": ya, "rate_a": ya / na if na else None,
        "tokens_b": nb, "divine_b": yb, "rate_b": yb / nb if nb else None,
        "pooled_gap": (ya / na - yb / nb) if (na and nb) else None,
        "T_weighted": weighted_T(cells) if cells else None,
        "T_macro_unsmoothed": macro_T(cells) if cells else None,
        "mh_or": mh_or(cells) if cells else None,
        "roots_a_gt_b": n_pos, "roots_a_lt_b": n_neg, "roots_tied": n_tie,
        "sign_test_p": sign_test_two_sided(n_pos, n_neg),
        "roots": roots,
    }
    obs_sign = None
    if out["pooled_gap"] is not None:
        obs_sign = "+" if out["pooled_gap"] > 0 else ("-" if out["pooled_gap"] < 0 else "0")
    out["observed_sign"] = obs_sign
    out["sign_held"] = (obs_sign == locked)
    if run_null and cells:
        t = out["T_weighted"]
        nb_res = null_b(cells, t, seed)
        nb_rep = null_b(cells, t, seed + 10)
        out["null_b"] = nb_res
        out["null_b_replication"] = nb_rep
        out["null_b_directional_p"] = nb_res["p_ge"] if locked == "+" else nb_res["p_le"]
    if strat_key:
        out["cmh"] = cmh(strata)
        out["cmh_n_strata_built"] = len(strata)
        for sv in (0, 1):
            sub = [r for r in rows if r.get(strat_key) == sv]
            s = arm_stats(sub, fa, fb, locked, seed, min_tokens, run_null=False)
            out[f"stratum_{strat_key}_{sv}"] = {k: s[k] for k in
                                                ("n_roots", "tokens_a", "divine_a", "rate_a",
                                                 "tokens_b", "divine_b", "rate_b", "pooled_gap",
                                                 "roots_a_gt_b", "roots_a_lt_b", "roots_tied",
                                                 "sign_test_p", "observed_sign")}
    return out


def loro(rows, fa, fb, locked):
    """Leave-one-root-out range of the pooled gap."""
    by = collections.defaultdict(lambda: {fa: [], fb: []})
    for r in rows:
        if r["form"] in (fa, fb):
            by[r["root"]][r["form"]].append(r)
    el = [rt for rt in by if len(by[rt][fa]) >= MIN_TOKENS and len(by[rt][fb]) >= MIN_TOKENS]
    if len(el) < 2:
        return None
    gaps = []
    for drop in el:
        keep = [rt for rt in el if rt != drop]
        ya = sum(sum(x["divine"] for x in by[rt][fa]) for rt in keep)
        na = sum(len(by[rt][fa]) for rt in keep)
        yb = sum(sum(x["divine"] for x in by[rt][fb]) for rt in keep)
        nb = sum(len(by[rt][fb]) for rt in keep)
        if na and nb:
            gaps.append(ya / na - yb / nb)
    return {"min": min(gaps), "max": max(gaps), "n": len(gaps),
            "all_match_locked_sign": all((g > 0) == (locked == "+") for g in gaps)}


def load_eqtb(path):
    """Secondary transitivity: verb locations with >=1 Obj dependent. Join (sentence_id, token_id)."""
    rows = []
    with open(path, encoding="utf-16") as fh:
        for r in csv.DictReader(fh, delimiter="\t"):
            rows.append(r)
    idx = {}
    for r in rows:
        idx[(r["sentence_id"], r["token_id"])] = r
    obj_locs = set()
    for r in rows:
        if r["rel_label"] != "Obj":
            continue
        h = idx.get((r["sentence_id"], r["ref_token_id"]))
        if h and h["pos"] == "V" and h["location"].startswith("("):
            obj_locs.add(h["location"])
    subj_nominal = {}
    for r in rows:
        if r["rel_label"] != "Subj" or r["pos"] not in ("N", "PN"):
            continue
        h = idx.get((r["sentence_id"], r["ref_token_id"]))
        if h and h["pos"] == "V" and h["location"].startswith("("):
            subj_nominal.setdefault(h["location"], r["lemma"])
    return obj_locs, subj_nominal


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--eqtb", help="Path to EQTB Quranic.csv (SECONDARY, optional)")
    args = ap.parse_args()

    gate_inputs(args.eqtb)
    words, verses = load_qac()
    verbs = build_verbs(words, verses)
    print(f"[load] {len(verbs)} verb segments")
    active = [v for v in verbs if not v["passive"] and v["root"]]
    print(f"[load] {len(active)} active verbs with a root")

    # ---- object-channel coverage assertion (prereg §5.1)
    covered = total = 0
    for v in verbs:
        s = 0
        for c in v["clitics"]:
            if c["kind"] != "SUFFIX":
                continue
            total += 1
            classify_clitic(c["surface"], c["pgn"], s, v["agr"], v["aspect"])
            covered += 1
            s += 1
    if covered != total:
        raise SystemExit(f"RULE-NEW COVERAGE FAILURE: {covered} != {total}")
    print(f"[ok] RULE-NEW covers {covered}/{total} post-verb SUFFIX PRON tokens (100%)")

    eqtb_obj, eqtb_subj = (set(), {})
    if args.eqtb:
        eqtb_obj, eqtb_subj = load_eqtb(args.eqtb)
        print(f"[eqtb] {len(eqtb_obj)} verb locations with an Obj edge; "
              f"{len(eqtb_subj)} with a nominal Subj edge")

    for v in active:
        v["T1"] = 1 if rule_new(v) else 0
        v["T2"] = 1 if v["loc"] in eqtb_obj else 0

    # ---- build classified row sets
    CLASSIFIERS = {"C-STRICT": c_strict, "C-WIDE": c_wide,
                   "C-STRICT-EXT": c_strict_ext, "C-WIDE-EXT": c_wide_ext}
    rowsets, labelling = {}, {}
    for name, fn in CLASSIFIERS.items():
        rs = []
        lab_by_loc = {}
        for v in active:
            lab, rule, lem = fn(v)
            if lab is None:
                continue
            lab_by_loc[v["loc"]] = (lab, rule, lem)
            rs.append({"loc": v["loc"], "root": v["root"], "form": v["form"], "agr": v["agr"],
                       "divine": 1 if lab == "DIVINE" else 0, "rule": rule, "subject_lemma": lem,
                       "T1": v["T1"], "T2": v["T2"], "surah": v["surah"], "verse": v["verse"]})
        rowsets[name] = rs
        labelling[name] = lab_by_loc
        print(f"[classify] {name}: {len(rs)}/{len(active)} = {len(rs)/len(active):.4f}")

    # ---- coverage by form (prereg §10.4, §10.5)
    coverage = {}
    for name, rs in rowsets.items():
        per = {}
        for F in FORMS:
            tot = sum(1 for v in active if v["form"] == F)
            cls = sum(1 for r in rs if r["form"] == F)
            per[F] = {"active": tot, "classified": cls,
                      "coverage": cls / tot if tot else None}
        coverage[name] = per

    # ---- ambiguous classes (prereg §10.4)
    n1s = sum(1 for v in active if v["agr"] == "1S")
    n3_noexpl = sum(1 for v in active if v["agr"][0] == "3" and v["fwd"] is None)
    n3_stop = collections.Counter(v["fwd_stop"] for v in active if v["agr"][0] == "3")
    qwl_locs = set()
    for (s, v) in verses:
        seen = False
        for w in verses[(s, v)]:
            for (i, su, tg, ft) in words[(s, v, w)]:
                if tg == "V":
                    if seen:
                        a = AGR_RE.findall(ft)
                        if a and a[0] == "1P":
                            qwl_locs.add(f"({s}:{v}:{w}:{i})")
                    rm = ROOT_RE.search(ft)
                    if rm and rm.group(1).strip() == "qwl":
                        seen = True
    voc_verses = set()
    for (s, v) in verses:
        segs = [x for w in verses[(s, v)] for x in words[(s, v, w)]]
        if any(x[2] == "VOC" for x in segs) and any(
                (LEM_RE.search(x[3]).group(1) if LEM_RE.search(x[3]) else "") in ("rab~", "{ll~ah")
                for x in segs if x[2] in ("N", "PN")):
            voc_verses.add((s, v))
    n2_voc = sum(1 for v in active if v["agr"][0] == "2" and (v["surah"], v["verse"]) in voc_verses)
    rab_yusuf = [v["loc"] for v in active
                 if v["fwd"] == "rab~" and v["surah"] == 12 and 20 <= v["verse"] <= 50]
    ambiguous = {
        "first_person_singular_unclassified": n1s,
        "third_person_no_explicit_subject": n3_noexpl,
        "third_person_forward_window_terminator": dict(n3_stop),
        "one_p_verbs_with_prior_qwl_in_verse": len(qwl_locs),
        "two_p_verbs_in_verse_with_vocative_and_divine_name": n2_voc,
        "rab_subject_tokens_in_Q12_20_50_error_bound": len(rab_yusuf),
        "rab_subject_tokens_in_Q12_20_50_locations": rab_yusuf,
    }

    # ---- inter-rule agreement (prereg §4.6)
    both = [v for v in active if v["agr"][0] == "3" and v["fwd"] and v["bwd"]]
    agree_fb = sum(1 for v in both if (v["fwd"] in L_DIV) == (v["bwd"] in L_DIV))
    ext_diff = [v for v in active if v["fwd"] is None and (v["bwd"] or v["prop"])]
    eqtb_cmp = []
    for v in active:
        if v["loc"] in eqtb_subj and v["fwd"] is not None:
            eqtb_cmp.append(((eqtb_subj[v["loc"]] in L_DIV), (v["fwd"] in L_DIV)))
    agreement = {
        "fwd_vs_bwd_both_present": len(both),
        "fwd_vs_bwd_agree": agree_fb,
        "fwd_vs_bwd_rate": agree_fb / len(both) if both else None,
        "ext_only_labelled": len(ext_diff),
        "eqtb_subj_overlap_n": len(eqtb_cmp),
        "eqtb_subj_agree": sum(1 for a, b in eqtb_cmp if a == b),
        "eqtb_subj_agree_rate": (sum(1 for a, b in eqtb_cmp if a == b) / len(eqtb_cmp)
                                 if eqtb_cmp else None),
        "eqtb_contamination_note": "EQTB syntax was parser-initialised with verb_form among its "
                                   "inputs (H-NEW-2540 7.2); this comparison is contamination-limited.",
    }

    # ---- THE ARMS
    results = {}
    for classifier in ("C-STRICT", "C-WIDE"):
        rs = rowsets[classifier]
        arms = {}
        for aid, fa, fb, locked in ARMS:
            st = arm_stats(rs, fa, fb, locked, SEED_PRIMARY, strat_key="T1")
            st["loro"] = loro(rs, fa, fb, locked)
            st["cmh_T2"] = None
            if args.eqtb:
                st2 = arm_stats(rs, fa, fb, locked, SEED_PRIMARY, run_null=False, strat_key="T2")
                st["cmh_T2"] = st2["cmh"]
                st["stratum_T2_0"] = st2.get("stratum_T2_0")
                st["stratum_T2_1"] = st2.get("stratum_T2_1")
            st["sensitivity_min1"] = {k: v for k, v in
                                      arm_stats(rs, fa, fb, locked, SEED_PRIMARY, min_tokens=1,
                                                run_null=False).items() if k != "roots"}
            arms[aid] = st
        results[classifier] = arms

    # ---- sensitivities on the extended classifiers (NOT in the confirmatory family)
    sens_ext = {}
    for classifier in ("C-STRICT-EXT", "C-WIDE-EXT"):
        rs = rowsets[classifier]
        sens_ext[classifier] = {
            aid: {k: v for k, v in arm_stats(rs, fa, fb, locked, SEED_PRIMARY,
                                             run_null=False).items() if k != "roots"}
            for aid, fa, fb, locked in ARMS}

    # ---- S-1P-QCUT and S-2P-VCUT sensitivities (prereg §4.5)
    rs_q = [r for r in rowsets["C-WIDE"] if not (r["rule"] == "S-1P" and r["loc"] in qwl_locs)]
    rs_v = [r for r in rowsets["C-WIDE"]
            if not (r["rule"] == "S-2P" and (r["surah"], r["verse"]) in voc_verses)]
    sens_cut = {
        "S-1P-QCUT": {aid: {k: v for k, v in arm_stats(rs_q, fa, fb, locked, SEED_PRIMARY,
                                                       run_null=False).items() if k != "roots"}
                      for aid, fa, fb, locked in ARMS},
        "S-2P-VCUT": {aid: {k: v for k, v in arm_stats(rs_v, fa, fb, locked, SEED_PRIMARY,
                                                       run_null=False).items() if k != "roots"}
                      for aid, fa, fb, locked in ARMS},
    }

    # ---- conservative-denominator sensitivity (prereg §10.5)
    sens_cons = {}
    for classifier in ("C-STRICT", "C-WIDE"):
        lab = labelling[classifier]
        rs = [{"loc": v["loc"], "root": v["root"], "form": v["form"],
               "divine": 1 if lab.get(v["loc"], (None,))[0] == "DIVINE" else 0,
               "T1": v["T1"], "T2": v["T2"]} for v in active]
        sens_cons[classifier] = {
            aid: {k: v for k, v in arm_stats(rs, fa, fb, locked, SEED_PRIMARY,
                                             run_null=False).items() if k != "roots"}
            for aid, fa, fb, locked in ARMS}

    # ---- chronology sensitivity
    period = {}
    with open(FROZEN["revelation_order"][0], encoding="utf-8") as fh:
        for row in csv.DictReader(fh):
            period[int(row["mushaf_order"])] = row["period"]
    sens_chron = {}
    for classifier in ("C-STRICT", "C-WIDE"):
        rs = rowsets[classifier]
        sens_chron[classifier] = {}
        for per in ("Meccan", "Medinan"):
            sub = [r for r in rs if period.get(r["surah"]) == per]
            sens_chron[classifier][per] = {
                aid: {k: v for k, v in arm_stats(sub, fa, fb, locked, SEED_PRIMARY,
                                                 run_null=False).items() if k != "roots"}
                for aid, fa, fb, locked in ARMS}

    # ---- descriptive arms
    descriptive = {}
    for classifier in ("C-STRICT", "C-WIDE"):
        descriptive[classifier] = {
            aid: {k: v for k, v in arm_stats(rowsets[classifier], fa, fb, locked, SEED_PRIMARY,
                                             min_tokens=1, run_null=False).items() if k != "roots"}
            for aid, fa, fb, locked in DESCRIPTIVE_ARMS}

    # ---- person-composition arm (prereg §7.4) — reported AS a person result
    person_rows = [{"loc": v["loc"], "root": v["root"], "form": v["form"],
                    "divine": 1 if v["agr"] == "1P" else 0, "T1": v["T1"]} for v in active]
    person_arm = {aid: {k: val for k, val in arm_stats(person_rows, fa, fb, locked, SEED_PRIMARY,
                                                       run_null=False).items() if k != "roots"}
                  for aid, fa, fb, locked in ARMS}
    person_by_form = {}
    for F in FORMS:
        pool = [v for v in active if v["form"] == F]
        if not pool:
            continue
        person_by_form[F] = {
            "n": len(pool),
            "p_1P": sum(1 for v in pool if v["agr"] == "1P") / len(pool),
            "p_1S": sum(1 for v in pool if v["agr"] == "1S") / len(pool),
            "p_2": sum(1 for v in pool if v["agr"][0] == "2") / len(pool),
            "p_3": sum(1 for v in pool if v["agr"][0] == "3") / len(pool),
        }

    # ---- VERDICT (prereg §9), diffed clause by clause
    verdicts = {}
    for classifier in ("C-STRICT", "C-WIDE"):
        arms = results[classifier]
        c_signs = [arms[a]["observed_sign"] for a in ("C1", "C2")]
        instrument_confounded = all(s == "+" for s in c_signs)

        def passes(a):
            st = arms[a]
            nb = st.get("null_b")
            return (st["sign_held"] and st["sign_test_p"] < GATE
                    and nb is not None and nb["p_two_sided"] < GATE)

        all_signs_match = all(arms[a]["sign_held"] for a in ("M1", "M2", "M3", "C1", "C2"))
        m_pass = [a for a in ("M1", "M2", "M3") if passes(a)]
        c_pass = [a for a in ("C1", "C2") if passes(a)]
        cond_ok, cond_detail = [], {}
        for a in m_pass + c_pass:
            cm = arms[a]["cmh"]
            locked = arms[a]["locked_sign"]
            orv = cm["or_cmh"]
            orv = float("inf") if orv == "inf" else orv     # "inf" is the JSON-safe encoding
            ok = (orv is not None and cm["p"] is not None
                  and ((orv > 1) if locked == "+" else (orv < 1))
                  and cm["p"] < GATE)
            cond_detail[a] = {"or_cmh": cm["or_cmh"], "p": cm["p"], "retains_direction_and_gate": ok}
            cond_ok.append(ok)
        if instrument_confounded:
            verdict = "INSTRUMENT-CONFOUNDED"
        elif all_signs_match and m_pass and c_pass and cond_ok and all(cond_ok):
            verdict = "AGENCY-TRACKED"
        elif all_signs_match and m_pass and c_pass:
            verdict = "AGENCY-TRANSITIVITY-EXPLAINED"
        else:
            verdict = "NULL"
        verdicts[classifier] = {
            "verdict": verdict,
            "clause_a_all_five_signs_match": all_signs_match,
            "clause_b_M_arms_passing_gate": m_pass,
            "clause_b_C_arms_passing_gate": c_pass,
            "clause_c_transitivity_conditioned": cond_detail,
            "escape_hatch_both_causative_arms_positive": instrument_confounded,
            "gate": GATE, "bonferroni_alpha": ALPHA_BONF, "family_k": BONF_K,
        }

    # ---- census + dissociation rosters (prereg §10.1, §10.2)
    quran = json.load(open(FROZEN["quran_no_tashkeel"][0], encoding="utf-8"))
    vtext = {(s["id"], v["id"]): v["text"] for s in quran for v in s["verses"]}
    census = []
    lab_w = labelling["C-WIDE"]
    for v in active:
        if v["loc"] not in lab_w:
            continue
        lab, rule, lem = lab_w[v["loc"]]
        census.append({"location": v["loc"], "surah": v["surah"], "verse": v["verse"],
                       "root": v["root"], "form": v["form"], "aspect": v["aspect"],
                       "agreement": v["agr"], "subject_label": lab, "subject_lemma": lem or "",
                       "rule_fired": rule, "T1_object_clitic": v["T1"], "T2_eqtb_obj": v["T2"],
                       "verse_text": vtext.get((v["surah"], v["verse"]), "")})
    census.sort(key=lambda r: (r["surah"], r["verse"], r["location"]))

    by_root_form = collections.defaultdict(lambda: collections.defaultdict(list))
    for r in census:
        by_root_form[r["root"]][r["form"]].append(r)
    dissoc = []
    for rt in sorted(by_root_form):
        for cf in CAUSATIVE_MEMBERS:
            for mf in MUTAWAA_MEMBERS:
                A, B = by_root_form[rt][cf], by_root_form[rt][mf]
                if not A or not B:
                    continue
                ya = sum(1 for x in A if x["subject_label"] == "DIVINE")
                yb = sum(1 for x in B if x["subject_label"] == "DIVINE")
                ra, rb = ya / len(A), yb / len(B)
                if ra == rb:
                    continue
                dissoc.append({
                    "root": rt, "causative_form": cf, "mutawaa_form": mf,
                    "n_causative": len(A), "divine_causative": ya, "rate_causative": round(ra, 4),
                    "n_mutawaa": len(B), "divine_mutawaa": yb, "rate_mutawaa": round(rb, 4),
                    "direction": "causative_more_divine" if ra > rb else "mutawaa_more_divine",
                    "perfect_dissociation": (ra == 1.0 and rb == 0.0) or (ra == 0.0 and rb == 1.0),
                    "causative_locations": ";".join(f"{x['location']}={x['subject_label'][0]}" for x in A),
                    "mutawaa_locations": ";".join(f"{x['location']}={x['subject_label'][0]}" for x in B),
                })

    # ---- blinded validation sample (prereg §10.3)
    rng = random.Random(SEED_PRIMARY)
    samples, key_rows = [], []
    sid = 0
    loc2verb = {v["loc"]: v for v in active}
    for F in FORMS:
        for lab in ("DIVINE", "NONDIVINE"):
            cell = sorted([r for r in census if r["form"] == F and r["subject_label"] == lab],
                          key=lambda r: r["location"])
            rng.shuffle(cell)
            for r in cell[:10]:
                sid += 1
                s_id = f"S{sid:03d}"
                samples.append({"sample_id": s_id, "verb_location": r["location"],
                                "verb_surface": loc2verb[r["location"]]["surface"],
                                "verse_text": r["verse_text"],
                                "review_subject_is_divine": "", "review_subject_span": "",
                                "review_notes": ""})
                key_rows.append({"sample_id": s_id, "verb_location": r["location"],
                                 "form": F, "rule_label": lab, "rule_fired": r["rule_fired"],
                                 "subject_lemma": r["subject_lemma"], "root": r["root"],
                                 "agreement": r["agreement"]})
    rng2 = random.Random(SEED_REPLICATION)
    order = list(range(len(samples)))
    rng2.shuffle(order)

    # ---- write immutable run dir (prereg §11)
    ts = datetime.datetime.now(datetime.timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    rundir = os.path.join(ROOT, "findings/phase-b-hypotheses/runs/h-new-2850", ts)
    os.makedirs(rundir, exist_ok=False)
    result = {
        "finding_id": "H-NEW-2850",
        "prereg_sha256": PREREG_SHA,
        "frozen_inputs": {k: v[1] for k, v in FROZEN.items()},
        "eqtb_used_secondary": bool(args.eqtb), "eqtb_sha256": EQTB_SHA if args.eqtb else None,
        "seeds": {"primary": SEED_PRIMARY, "replication": SEED_REPLICATION, "n_perm": N_PERM},
        "family_k": BONF_K, "bonferroni_alpha": ALPHA_BONF, "decision_gate": GATE,
        "n_verbs": len(verbs), "n_active_with_root": len(active),
        "classifier_counts": {k: len(v) for k, v in rowsets.items()},
        "coverage_by_form": coverage,
        "ambiguous_classes": ambiguous,
        "inter_rule_agreement": agreement,
        "arms": results,
        "verdicts": verdicts,
        "person_composition_arm": {"note": "This is a PERSON result, not an agency result "
                                           "(prereg 7.4).",
                                   "by_form": person_by_form, "arms": person_arm},
        "sensitivity_extended_classifiers": sens_ext,
        "sensitivity_person_channel_cuts": sens_cut,
        "sensitivity_conservative_denominator": sens_cons,
        "sensitivity_chronology": sens_chron,
        "descriptive_arms": descriptive,
        "census_rows": len(census), "dissociation_rows": len(dissoc),
        "validation_sample_rows": len(samples),
    }
    with open(os.path.join(rundir, "result.json"), "x", encoding="utf-8") as fh:
        json.dump(result, fh, ensure_ascii=False, indent=1)
    with open(os.path.join(rundir, "census-roster.tsv"), "x", encoding="utf-8", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(census[0].keys()), delimiter="\t")
        w.writeheader()
        for r in census:
            w.writerow(r)
    DISSOC_COLS = ["root", "causative_form", "mutawaa_form", "n_causative", "divine_causative",
                   "rate_causative", "n_mutawaa", "divine_mutawaa", "rate_mutawaa", "direction",
                   "perfect_dissociation", "causative_locations", "mutawaa_locations"]
    with open(os.path.join(rundir, "dissociation-roster.tsv"), "x", encoding="utf-8", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=DISSOC_COLS, delimiter="\t")
        w.writeheader()
        for r in dissoc:
            w.writerow(r)
    with open(os.path.join(rundir, "validation-sample.tsv"), "x", encoding="utf-8", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(samples[0].keys()), delimiter="\t")
        w.writeheader()
        for r in samples:
            w.writerow(r)
    with open(os.path.join(rundir, "validation-key.json"), "x", encoding="utf-8") as fh:
        json.dump({"seed": SEED_PRIMARY, "replication_seed": SEED_REPLICATION,
                   "replication_order": order, "rows": key_rows}, fh, ensure_ascii=False, indent=1)
    with open(os.path.join(rundir, "manifest.json"), "x", encoding="utf-8") as fh:
        json.dump({"finding_id": "H-NEW-2850", "utc": ts,
                   "prereg": "findings/phase-b-hypotheses/prereg-h-new-2850-agency-grammar.md",
                   "prereg_sha256": PREREG_SHA,
                   "script": "findings/phase-b-hypotheses/scripts/h-new-2850.py",
                   "frozen_inputs": {k: {"path": os.path.relpath(v[0], ROOT), "sha256": v[1]}
                                     for k, v in FROZEN.items()},
                   "eqtb": {"used": bool(args.eqtb), "role": "SECONDARY transitivity only",
                            "sha256": EQTB_SHA if args.eqtb else None},
                   "seeds": {"primary": SEED_PRIMARY, "replication": SEED_REPLICATION,
                             "n_perm": N_PERM},
                   "outputs": ["result.json", "census-roster.tsv", "dissociation-roster.tsv",
                               "validation-sample.tsv", "validation-key.json"]},
                  fh, ensure_ascii=False, indent=1)

    # ---- console report
    print("\n=== CLASSIFIER COVERAGE BY FORM (denominator declaration, prereg 10.5) ===")
    hdr = f"{'form':<6}{'active':>8}" + "".join(f"{c:>14}" for c in ("C-STRICT", "C-WIDE"))
    print(hdr)
    for F in ["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "X"]:
        a = coverage["C-STRICT"][F]["active"]
        print(f"{F:<6}{a:>8}" + "".join(
            f"{coverage[c][F]['coverage']:>14.4f}" for c in ("C-STRICT", "C-WIDE")))

    for classifier in ("C-STRICT", "C-WIDE"):
        print(f"\n=== ARMS — {classifier} ===")
        for aid, fa, fb, locked in ARMS:
            st = results[classifier][aid]
            if st["n_roots"] == 0:
                print(f"  {aid} {fa}->{fb} locked {locked}: NO ELIGIBLE ROOTS")
                continue
            nb = st.get("null_b") or {}
            cm = st["cmh"]
            print(f"  {aid} {fa}->{fb} locked {locked}  roots={st['n_roots']}")
            print(f"     {st['divine_a']}/{st['tokens_a']}={st['rate_a']:.4f} vs "
                  f"{st['divine_b']}/{st['tokens_b']}={st['rate_b']:.4f}  "
                  f"gap={st['pooled_gap']:+.4f}  T={st['T_weighted']:+.4f} "
                  f"(macro {st['T_macro_unsmoothed']:+.4f})  MH-OR={st['mh_or']}")
            print(f"     roots {st['roots_a_gt_b']}/{st['roots_a_lt_b']}/{st['roots_tied']}  "
                  f"sign p={st['sign_test_p']:.3e}  NullB 2s={nb.get('p_two_sided')}  "
                  f"dir={st.get('null_b_directional_p')}  "
                  f"sign {'HELD' if st['sign_held'] else 'FLIPPED'}")
            print(f"     CMH(root x T1) OR={cm['or_cmh']} p={cm['p']} strata={cm['strata_used']}")
            for sv in (0, 1):
                s = st.get(f"stratum_T1_{sv}")
                if s and s["n_roots"]:
                    print(f"       T1={sv}: roots={s['n_roots']} gap={s['pooled_gap']:+.4f} "
                          f"sign p={s['sign_test_p']:.3e}")
                else:
                    print(f"       T1={sv}: no power in stratum")
        v = verdicts[classifier]
        print(f"  --> VERDICT {classifier}: {v['verdict']}")

    print("\n=== PERSON-COMPOSITION ARM (a person result, not an agency result) ===")
    for F in ["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "X"]:
        d = person_by_form[F]
        print(f"  {F:<5} n={d['n']:>6}  1P={d['p_1P']:.4f} 1S={d['p_1S']:.4f} "
              f"2={d['p_2']:.4f} 3={d['p_3']:.4f}")

    print(f"\n[run] {rundir}")
    print(f"[census] {len(census)} rows   [dissociation] {len(dissoc)} rows   "
          f"[validation] {len(samples)} rows, review columns BLANK by design")


if __name__ == "__main__":
    main()
