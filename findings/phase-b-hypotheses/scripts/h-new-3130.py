#!/usr/bin/env python3
"""
H-NEW-3130 (frontier item F-6) — Is the per-surah distribution over derived verb forms
a register signature independent of root vocabulary?

Pre-registration:
    findings/phase-b-hypotheses/prereg-h-new-3130-derived-form-fingerprint.md
The prereg SHA-256 is embedded below and verified at runtime; a mismatch aborts the run.

Design is INHERITED from H-NEW-2540 (root-held-fixed cells). Dependency stated in the prereg §3:
2540's primary channel is EQTB parser-contaminated. This runner uses QAC only, no treebank.
"""

import collections
import hashlib
import json
import os
import re
import subprocess
import sys
import datetime

import numpy as np

# ---------------------------------------------------------------- locks

EXPECTED_PREREG_SHA = "a95d6c1513b53ca07fb7309016374b0a8760d61ec2d5b37b5f7730f15e7e5869"
EXPECTED_QAC_SHA = "a1d12923815341face765083805d2148ed2d9f5cc3f7d6665219d887675d8c46"
EXPECTED_GENRE_SHA = "16ec35b2793922bd007767ccddfb6d7aeb5ca53e48394792984f88b49164572a"

SEED_NULL_A = 20260509          # prereg §5.1 — register label shuffle
SEED_NULL_B = 20260510          # prereg §5.1 — within-root form shuffle
N_PERM = 10000                  # prereg front-matter
K_BONFERRONI = 6                # prereg §7
ALPHA_BON = 0.05 / K_BONFERRONI
BINDING_GATE = 0.001            # prereg §7 — binding raw gate, stricter than Bonferroni

REPO = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.abspath(__file__)))))
PREREG_REL = "findings/phase-b-hypotheses/prereg-h-new-3130-derived-form-fingerprint.md"
QAC_REL = "data/morphology/quranic-corpus-morphology-0.4.txt"
GENRE_REL = "findings/classical-sources/neuwirth-sinai-genre-labels.tsv"
RUN_ROOT_REL = "findings/phase-b-hypotheses/runs/h-new-3130"

# prereg §2.3 — tested form set; VII/IX/XI/XII excluded for sparsity, stated not silent
FORMS = ["I", "II", "III", "IV", "V", "VI", "VIII", "X"]
FORMS_T2 = ["II", "III", "IV", "V", "VI", "VIII", "X"]   # no Form I for nominals (prereg §2.2)
SPARSE_EXCLUDED = ["VII", "IX", "XI", "XII"]
FORM_RE = re.compile(r"\((I|II|III|IV|V|VI|VII|VIII|IX|X|XI|XII)\)")
LOC_RE = re.compile(r"\((\d+):(\d+):(\d+):(\d+)\)")

CLASS_MIN = 5                   # prereg §5.1 — class-size floor for the classification arm
MIN_TOKENS_M2 = 20              # prereg §6 — robustness arm M2

# prereg §6 — the two coarsenings; order is the deciding parameter
C1_ORDER = ["legal", "narrative", "oath", "hymn", "eschat", "polemic", "liturg"]
C2_ORDER = ["oath", "eschat", "legal", "narrative", "hymn", "polemic", "liturg"]


def sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def self_check():
    """Runtime lock verification. Any mismatch aborts before a single number is computed."""
    checks = [
        ("pre-registration", os.path.join(REPO, PREREG_REL), EXPECTED_PREREG_SHA),
        ("QAC morphology", os.path.join(REPO, QAC_REL), EXPECTED_QAC_SHA),
        ("genre labels", os.path.join(REPO, GENRE_REL), EXPECTED_GENRE_SHA),
    ]
    got = {}
    for label, path, expected in checks:
        if not os.path.exists(path):
            raise SystemExit("FATAL: %s not found at %s" % (label, path))
        actual = sha256(path)
        got[label] = actual
        if actual != expected:
            raise SystemExit(
                "FATAL: %s SHA-256 mismatch.\n  expected %s\n  actual   %s\n"
                "The pre-registration is immutable; a changed file invalidates the run."
                % (label, expected, actual))
    return got


# ---------------------------------------------------------------- data

def parse_qac(path):
    """Return token records. Form I is DERIVED as 'verb with no form tag' (prereg §2.2)."""
    toks = []
    for line in open(path, encoding="utf-8"):
        parts = line.rstrip("\n").split("\t")
        if len(parts) != 4 or parts[0].startswith("LOCATION") or parts[0].startswith("#"):
            continue
        m = LOC_RE.match(parts[0])
        if not m:
            continue
        feats = parts[3]
        pos_m = re.search(r"POS:([A-Z]+)", feats)
        if not pos_m:
            continue
        pos = pos_m.group(1)
        form_m = FORM_RE.search(feats)
        is_verb = (pos == "V")
        if is_verb:
            form = form_m.group(1) if form_m else "I"     # untagged verb == Form I
        else:
            if not form_m:
                continue                                   # non-verb with no form tag: not a wazn
            form = form_m.group(1)
        root_m = re.search(r"ROOT:([^|]+)", feats)
        lem_m = re.search(r"LEM:([^|]+)", feats)
        toks.append({
            "surah": int(m.group(1)), "verse": int(m.group(2)),
            "word": int(m.group(3)), "seg": int(m.group(4)),
            "pos": pos, "form": form,
            "root": root_m.group(1) if root_m else None,
            "lemma": lem_m.group(1) if lem_m else None,
        })
    return toks


def find_legal_marker_tokens(path):
    """prereg §2.4 — locate the Form IV verbs inside yaa ayyuhaa alladhiina aamanuu."""
    rows = []
    for line in open(path, encoding="utf-8"):
        parts = line.rstrip("\n").split("\t")
        if len(parts) != 4 or parts[0].startswith("LOCATION") or parts[0].startswith("#"):
            continue
        m = LOC_RE.match(parts[0])
        if not m:
            continue
        rows.append((int(m.group(1)), int(m.group(2)), int(m.group(3)),
                     int(m.group(4)), parts[3]))
    by_verse = collections.defaultdict(lambda: collections.defaultdict(list))
    for s, v, w, t, f in rows:
        by_verse[(s, v)][w].append(f)
    hits = set()
    for (s, v), words in by_verse.items():
        idx = sorted(words)
        for i in range(len(idx) - 2):
            fa = "|".join(words[idx[i]])
            fb = "|".join(words[idx[i + 1]])
            fc = "|".join(words[idx[i + 2]])
            if "ya+" in fa and "POS:N" in fa and "POS:REL" in fb \
                    and "(IV)" in fc and "ROOT:Amn" in fc:
                hits.add((s, v, idx[i + 2]))
    return hits


def load_genre(path):
    rows = [l for l in open(path, encoding="utf-8") if not l.startswith("#")]
    header = rows[0].rstrip("\n").split("\t")
    i_s = header.index("surah_number")
    i_sin = header.index("sinai_genre")
    i_neu = header.index("neuwirth_genre")
    i_ph = header.index("neuwirth_phase")
    out = {}
    for line in rows[1:]:
        p = line.rstrip("\n").split("\t")
        if len(p) <= max(i_s, i_sin, i_neu, i_ph):
            continue
        out[int(p[i_s])] = {"sinai": p[i_sin], "neuwirth": p[i_neu], "phase": p[i_ph]}
    if set(out) != set(range(1, 115)):
        raise SystemExit("FATAL: genre TSV does not cover surahs 1..114 exactly")
    return out


def coarsen(value, order):
    v = value.lower()
    for k in order:
        if k in v:
            return k
    return "other"


def phase_of(value):
    v = value.lower()
    has_mec, has_med = "meccan" in v, "medinan" in v
    if has_med and not has_mec:
        return "Medinan"
    if has_mec and not has_med:
        return "Meccan"
    return "other"


def surah_lengths(toks_all_path):
    """Verse count, word count, mean verse length per surah, from QAC locations."""
    verses = collections.defaultdict(set)
    words = collections.defaultdict(set)
    for line in open(toks_all_path, encoding="utf-8"):
        parts = line.rstrip("\n").split("\t")
        if len(parts) != 4 or parts[0].startswith("LOCATION") or parts[0].startswith("#"):
            continue
        m = LOC_RE.match(parts[0])
        if not m:
            continue
        s, v, w = int(m.group(1)), int(m.group(2)), int(m.group(3))
        verses[s].add(v)
        words[s].add((v, w))
    out = {}
    for s in range(1, 115):
        nv, nw = len(verses[s]), len(words[s])
        out[s] = {"verses": nv, "words": nw, "mean_verse_len": nw / nv if nv else 0.0}
    return out


# ---------------------------------------------------------------- statistics

def profiles_from_counts(counts):
    """counts (114, F) -> row-normalised profiles; all-zero rows become NaN."""
    tot = counts.sum(axis=1, keepdims=True)
    with np.errstate(invalid="ignore", divide="ignore"):
        p = np.where(tot > 0, counts / np.maximum(tot, 1), np.nan)
    return p


def residualise(P, x):
    """
    OLS residual of each column of P on x (prereg §5.3). x is log length.

    Rows that are not finite (a surah with zero tokens in the tuple's unit) are EXCLUDED
    from the fit and left NaN, rather than being allowed to poison the column mean and so
    every other row. Under tuple T2 five surahs (Q109, 111, 112, 113, 114) have no
    form-tagged token at all; without this guard every channel returns NaN. T1 and T3 have
    no such rows, so the confirmatory family is unaffected either way.
    """
    ok = np.isfinite(P).all(axis=1) & np.isfinite(x)
    if ok.sum() < 3:
        return P.copy()
    xo = x[ok]
    xc = xo - xo.mean()
    denom = float((xc * xc).sum())
    if denom == 0:
        return P.copy()
    b = (xc[:, None] * (P[ok] - P[ok].mean(axis=0))).sum(axis=0) / denom
    out = np.full_like(P, np.nan)
    out[ok] = P[ok] - np.outer(xo - xo.mean(), b)
    return out


def loo_nearest_centroid_accuracy(P, y, keep):
    """
    Leave-one-out nearest-centroid accuracy (prereg §5.1).
    P (n, F) profiles; y (n,) integer class ids; keep (n,) bool mask of usable rows.
    Uses squared Euclidean distance. LOO removes the held-out row from its own centroid.
    """
    X = P[keep]
    yy = y[keep]
    n = X.shape[0]
    K = int(yy.max()) + 1
    sums = np.zeros((K, X.shape[1]))
    cnts = np.zeros(K)
    np.add.at(sums, yy, X)
    np.add.at(cnts, yy, 1.0)
    # centroids with the held-out point removed from its own class
    own_sum = sums[yy] - X
    own_cnt = cnts[yy] - 1.0
    valid_own = own_cnt > 0
    cent = np.where(cnts[:, None] > 0, sums / np.maximum(cnts[:, None], 1), np.inf)
    d = ((X[:, None, :] - cent[None, :, :]) ** 2).sum(axis=2)      # (n, K)
    own_cent = np.where(valid_own[:, None],
                        own_sum / np.maximum(own_cnt[:, None], 1), np.inf)
    d[np.arange(n), yy] = ((X - own_cent) ** 2).sum(axis=1)
    d[:, cnts == 0] = np.inf
    pred = np.argmin(d, axis=1)
    return float((pred == yy).mean())


def group_diff(P, col_idx, mask, keep):
    """mean(target class) - mean(rest) on the pooled columns col_idx (prereg §5.2)."""
    v = P[:, col_idx].sum(axis=1)
    a = v[keep & mask]
    b = v[keep & ~mask]
    if len(a) == 0 or len(b) == 0:
        return float("nan")
    return float(a.mean() - b.mean())


def empirical_p_one_sided(observed, null_vals):
    """P(null >= observed), +1 correction. Directions are locked one-sided (prereg §3)."""
    null_vals = np.asarray(null_vals, dtype=float)
    return float((np.sum(null_vals >= observed) + 1) / (len(null_vals) + 1))


# ---------------------------------------------------------------- nulls

def build_token_arrays(toks, unit, marker_hits=None, ablate_marker=False):
    """
    unit: 'T1' verb tokens; 'T2' all form-tagged POS; 'T3' distinct lemma types.
    Returns surah_idx, form_idx, root_id (root-sorted), and the form list used.
    """
    forms = FORMS_T2 if unit == "T2" else FORMS
    fpos = {f: i for i, f in enumerate(forms)}
    sel = []
    seen_types = set()
    for t in toks:
        if unit == "T1" or unit == "T3":
            if t["pos"] != "V":
                continue
        if t["form"] not in fpos:
            continue
        if t["root"] is None:
            continue
        if ablate_marker and marker_hits is not None:
            if (t["surah"], t["verse"], t["word"]) in marker_hits:
                continue
        if unit == "T3":
            if t["lemma"] is None:
                continue
            key = (t["surah"], t["lemma"])
            if key in seen_types:
                continue
            seen_types.add(key)
        sel.append(t)
    surah_idx = np.array([t["surah"] - 1 for t in sel], dtype=np.int64)
    form_idx = np.array([fpos[t["form"]] for t in sel], dtype=np.int64)
    roots = sorted({t["root"] for t in sel})
    rmap = {r: i for i, r in enumerate(roots)}
    root_id = np.array([rmap[t["root"]] for t in sel], dtype=np.int64)
    order = np.argsort(root_id, kind="stable")
    return surah_idx[order], form_idx[order], root_id[order], forms


def counts_matrix(surah_idx, form_idx, n_forms):
    flat = np.bincount(surah_idx * n_forms + form_idx, minlength=114 * n_forms)
    return flat.reshape(114, n_forms).astype(float)


def within_root_shuffle(form_idx, root_id, rng):
    """
    Null B (prereg §4.3 ROOT-A): permute form labels WITHIN root, holding each token's
    surah fixed. Preserves every root's corpus-wide form distribution and every surah's
    root inventory; destroys only surah-specific allocation of forms within a root.
    Arrays arrive sorted by root_id, so a lexsort by (root, random) permutes within root.
    """
    r = rng.random(len(form_idx))
    order = np.lexsort((r, root_id))
    return form_idx[order]


def loso_root_expected(surah_idx, form_idx, root_id, n_forms):
    """
    ROOT-B (prereg §4.3): leave-one-surah-out root-expected profile e_s.
    e_s(f) = sum_r n_s(r) * q_r^{(-s)}(f) / sum_r n_s(r)
    """
    n_roots = int(root_id.max()) + 1
    root_form = np.zeros((n_roots, n_forms))
    np.add.at(root_form, (root_id, form_idx), 1.0)
    sur_root_form = np.zeros((114, n_roots, n_forms))
    np.add.at(sur_root_form, (surah_idx, root_id, form_idx), 1.0)
    E = np.zeros((114, n_forms))
    for s in range(114):
        loso = root_form - sur_root_form[s]                     # (n_roots, n_forms)
        tot = loso.sum(axis=1, keepdims=True)
        q = np.where(tot > 0, loso / np.maximum(tot, 1), 0.0)
        n_s_r = sur_root_form[s].sum(axis=1)                    # (n_roots,)
        denom = n_s_r.sum()
        if denom > 0:
            E[s] = (n_s_r[:, None] * q).sum(axis=0) / denom
    return E


# ---------------------------------------------------------------- verdict
#
# DIFFED LINE BY LINE AGAINST PREREG §7 BEFORE THE RUN. The mapping is:
#   prereg §7 "An arm PASSES iff (a) direction matches §3 AND (b) worst p across L0-L3 < 0.001"
#       -> arm_passes(): requires direction_ok AND worst_p < BINDING_GATE. Both. No 'or'.
#   prereg §7 step 1 UNTESTABLE-AT-THIS-N iff S* > S_max for H1-ROOT
#   prereg §7 step 2 NULL                 iff H1-RAW does not PASS
#   prereg §7 step 3 ROOT-EXPLAINED       iff H1-RAW PASSES and H1-ROOT does not PASS
#   prereg §7 step 4 CONFIRMED            iff H1-ROOT PASSES and (D1-ROOT or D2-ROOT) PASSES
#   prereg §7 step 5 DIRECTIONAL          iff H1-ROOT PASSES and neither D1-ROOT nor D2-ROOT
# Evaluation order is the prereg's order. No other verdict string may be emitted.


def arm_passes(arm):
    return bool(arm["direction_ok"]) and (arm["p_worst"] < BINDING_GATE)


def decide(arms, s_star_h1root, s_max_h1root):
    if s_star_h1root > s_max_h1root:
        return "UNTESTABLE-AT-THIS-N"
    if not arm_passes(arms["H1-RAW"]):
        return "NULL"
    if not arm_passes(arms["H1-ROOT"]):
        return "ROOT-EXPLAINED"
    if arm_passes(arms["D1-ROOT"]) or arm_passes(arms["D2-ROOT"]):
        return "CONFIRMED"
    return "DIRECTIONAL"


# ---------------------------------------------------------------- run

def run_cell(toks, genre, lens, unit, label_col, coarse_order,
             marker_hits, ablate_marker=False, min_tokens=0, n_perm=N_PERM):
    surah_idx, form_idx, root_id, forms = build_token_arrays(
        toks, unit, marker_hits, ablate_marker)
    n_forms = len(forms)
    counts = counts_matrix(surah_idx, form_idx, n_forms)
    P_obs = profiles_from_counts(counts)

    labels_raw = [genre[s][label_col] for s in range(1, 115)]
    lab = [coarsen(v, coarse_order) for v in labels_raw]
    sizes = collections.Counter(lab)
    classes = sorted([c for c, n in sizes.items() if n >= CLASS_MIN])
    cmap = {c: i for i, c in enumerate(classes)}
    y = np.array([cmap.get(l, -1) for l in lab])
    tok_tot = counts.sum(axis=1)
    keep = (y >= 0) & (tok_tot >= max(min_tokens, 1)) & np.isfinite(P_obs).all(axis=1)

    nar = np.array([l == "narrative" for l in lab])
    leg = np.array([l == "legal" for l in lab])
    iIV = [forms.index("IV")] if "IV" in forms else []
    iVVI = [forms.index(f) for f in ("V", "VI") if f in forms]

    lenvars = {
        "L0": None,
        "L1": np.log(np.array([max(lens[s]["verses"], 1) for s in range(1, 115)], float)),
        "L2": np.log(np.array([max(lens[s]["words"], 1) for s in range(1, 115)], float)),
        "L3": np.log(np.array([max(lens[s]["mean_verse_len"], 1e-9)
                               for s in range(1, 115)], float)),
    }

    def channels(P):
        out = {}
        for ch, x in lenvars.items():
            out[ch] = P if x is None else residualise(P, x)
        return out

    P_ch = channels(P_obs)
    obs = {
        "H1": {ch: loo_nearest_centroid_accuracy(P_ch[ch], y, keep) for ch in lenvars},
        "D1": {ch: group_diff(P_ch[ch], iIV, nar, keep) for ch in lenvars},
        "D2": {ch: group_diff(P_ch[ch], iVVI, leg, keep) for ch in lenvars},
    }

    # ---- Null A: shuffle register labels across surahs (profiles fixed)
    rngA = np.random.default_rng(SEED_NULL_A)
    nullA = {k: {ch: np.empty(n_perm) for ch in lenvars} for k in ("H1", "D1", "D2")}
    keep_idx = np.where(keep)[0]
    for i in range(n_perm):
        perm = rngA.permutation(keep_idx)
        y_p = y.copy()
        y_p[keep_idx] = y[perm]
        nar_p = nar.copy(); nar_p[keep_idx] = nar[perm]
        leg_p = leg.copy(); leg_p[keep_idx] = leg[perm]
        for ch in lenvars:
            nullA["H1"][ch][i] = loo_nearest_centroid_accuracy(P_ch[ch], y_p, keep)
            nullA["D1"][ch][i] = group_diff(P_ch[ch], iIV, nar_p, keep)
            nullA["D2"][ch][i] = group_diff(P_ch[ch], iVVI, leg_p, keep)

    # ---- Null B: within-root form shuffle (labels fixed, profiles recomputed)
    rngB = np.random.default_rng(SEED_NULL_B)
    nullB = {k: {ch: np.empty(n_perm) for ch in lenvars} for k in ("H1", "D1", "D2")}
    for i in range(n_perm):
        f_p = within_root_shuffle(form_idx, root_id, rngB)
        c_p = counts_matrix(surah_idx, f_p, n_forms)
        P_p = profiles_from_counts(c_p)
        P_pch = channels(P_p)
        for ch in lenvars:
            nullB["H1"][ch][i] = loo_nearest_centroid_accuracy(P_pch[ch], y, keep)
            nullB["D1"][ch][i] = group_diff(P_pch[ch], iIV, nar, keep)
            nullB["D2"][ch][i] = group_diff(P_pch[ch], iVVI, leg, keep)

    # ---- ROOT-B: residualised profile d_s = p_s - e_s, under Null A
    E = loso_root_expected(surah_idx, form_idx, root_id, n_forms)
    D_obs = P_obs - E
    D_ch = channels(D_obs)
    rootB = {}
    for name, cols, mask in (("D1", iIV, nar), ("D2", iVVI, leg)):
        o = {ch: group_diff(D_ch[ch], cols, mask, keep) for ch in lenvars}
        nd = {ch: np.empty(n_perm) for ch in lenvars}
        rngC = np.random.default_rng(SEED_NULL_A)
        for i in range(n_perm):
            perm = rngC.permutation(keep_idx)
            m_p = mask.copy(); m_p[keep_idx] = mask[perm]
            for ch in lenvars:
                nd[ch][i] = group_diff(D_ch[ch], cols, m_p, keep)
        rootB[name] = {
            "observed": o,
            "p": {ch: empirical_p_one_sided(o[ch], nd[ch]) for ch in lenvars},
        }
    rootB["H1"] = {
        "observed": {ch: loo_nearest_centroid_accuracy(D_ch[ch], y, keep) for ch in lenvars}
    }

    def pack(stat, nulls):
        p = {ch: empirical_p_one_sided(obs[stat][ch], nulls[stat][ch]) for ch in lenvars}
        worst_ch = max(p, key=lambda c: p[c])
        best_ch = min(p, key=lambda c: p[c])
        return {
            "observed": obs[stat],
            "p_by_channel": p,
            "p_worst": p[worst_ch],
            "worst_channel": worst_ch,
            "p_best": p[best_ch],
            "best_channel": best_ch,
            # dominant = the length channel that moves p furthest from the uncontrolled L0
            "dominant_channel": max(lenvars, key=lambda c: abs(p[c] - p["L0"])),
            "p_swing": (p[worst_ch] / p[best_ch]) if p[best_ch] > 0 else float("inf"),
            "null_mean": {ch: float(np.mean(nulls[stat][ch])) for ch in lenvars},
            "null_sd": {ch: float(np.std(nulls[stat][ch])) for ch in lenvars},
            "null_q999": {ch: float(np.quantile(nulls[stat][ch], 1 - BINDING_GATE))
                          for ch in lenvars},
            "null_max": {ch: float(np.max(nulls[stat][ch])) for ch in lenvars},
        }

    arms = {}
    for stat, nulls, tag in (("H1", nullA, "RAW"), ("H1", nullB, "ROOT"),
                             ("D1", nullA, "RAW"), ("D1", nullB, "ROOT"),
                             ("D2", nullA, "RAW"), ("D2", nullB, "ROOT")):
        a = pack(stat, nulls)
        # direction: H1 accuracy above null mean; D1/D2 locked POSITIVE (prereg §3)
        if stat == "H1":
            a["direction_ok"] = all(a["observed"][ch] > a["null_mean"][ch] for ch in lenvars)
            a["locked_direction"] = "accuracy above null"
        else:
            a["direction_ok"] = all(a["observed"][ch] > 0 for ch in lenvars)
            a["locked_direction"] = "POSITIVE"
        a["passes"] = arm_passes(a)
        arms["%s-%s" % (stat, tag)] = a

    # ---- S* and S_max for the UNTESTABLE branch (prereg §5.5), H1-ROOT
    s_star = max(arms["H1-ROOT"]["null_q999"][ch] for ch in lenvars)
    s_max = 1.0                                      # perfect LOO accuracy
    # D1/D2 attainable maxima given observed marginals (extreme label assignment)
    def attainable_max(P, cols, mask):
        v = np.sort(P[keep][:, cols].sum(axis=1))[::-1]
        k = int((mask & keep).sum())
        if k == 0 or k == len(v):
            return float("nan")
        return float(v[:k].mean() - v[k:].mean())
    dmax = {
        "D1": attainable_max(P_obs, iIV, nar),
        "D2": attainable_max(P_obs, iVVI, leg),
    }

    # ---- tie fractions (prereg §2.3)
    def tie_fraction(vals):
        vals = vals[np.isfinite(vals)]
        c = collections.Counter(np.round(vals, 12))
        return float(sum(n for n in c.values() if n > 1) / len(vals)) if len(vals) else float("nan")
    ties = {
        "form_IV_share": tie_fraction(P_obs[:, iIV].sum(axis=1)) if iIV else None,
        "form_V_VI_share": tie_fraction(P_obs[:, iVVI].sum(axis=1)) if iVVI else None,
        "form_VI_share": (tie_fraction(P_obs[:, forms.index("VI")])
                          if "VI" in forms else None),
    }

    # ---- MDE / power for D1 and D2 (prereg §5.5)
    mde = {}
    for name, cols, mask, nulls in (("D1", iIV, nar, nullA), ("D2", iVVI, leg, nullA)):
        ch = arms["%s-RAW" % name]["worst_channel"]
        need = float(np.quantile(nulls[name][ch], 1 - BINDING_GATE))
        base = float(np.nanmean(P_obs[keep][:, cols].sum(axis=1)))
        mde[name] = {
            "channel": ch,
            "S_star_needed": need,
            "S_max_attainable": dmax[name],
            "untestable_branch_fires": bool(need > dmax[name]) if dmax[name] == dmax[name] else None,
            "mean_share_baseline": base,
            "MDE_as_multiple_of_baseline": (need / base) if base > 0 else float("inf"),
        }

    return {
        "unit": unit, "label_col": label_col,
        "coarsening": "C1" if coarse_order is C1_ORDER else "C2",
        "ablate_marker": ablate_marker, "min_tokens": min_tokens,
        "forms_used": forms, "n_tokens": int(len(surah_idx)),
        "n_surahs_kept": int(keep.sum()),
        "classes": classes, "class_sizes": {c: int(sizes[c]) for c in classes},
        "dropped_classes": {c: int(n) for c, n in sizes.items() if n < CLASS_MIN},
        "arms": arms,
        "root_B": rootB,
        "S_star_H1ROOT": s_star, "S_max_H1ROOT": s_max,
        "tie_fractions": ties,
        "mde": mde,
        "per_surah_profile": {str(s + 1): {forms[j]: float(P_obs[s, j])
                                           for j in range(n_forms)}
                              for s in range(114)},
    }


def main():
    hashes = self_check()
    qac_path = os.path.join(REPO, QAC_REL)
    toks = parse_qac(qac_path)
    genre = load_genre(os.path.join(REPO, GENRE_REL))
    lens = surah_lengths(qac_path)
    marker_hits = find_legal_marker_tokens(qac_path)

    stamp = datetime.datetime.now(datetime.timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    run_dir = os.path.join(REPO, RUN_ROOT_REL, stamp)
    os.makedirs(run_dir, exist_ok=False)          # write-once (standing rule 3)

    # corpus census, reported not asserted
    verb_forms = collections.Counter(t["form"] for t in toks if t["pos"] == "V")
    all_forms = collections.Counter(t["form"] for t in toks)
    by_pos = collections.Counter(t["pos"] for t in toks)
    root2f = collections.defaultdict(set)
    lem2f = collections.defaultdict(set)
    for t in toks:
        if t["pos"] != "V" or t["root"] is None:
            continue
        root2f[t["root"]].add(t["form"])
        if t["lemma"]:
            lem2f[t["lemma"]].add(t["form"])
    multi_roots = {r for r, v in root2f.items() if len(v) > 1}
    nverb = sum(1 for t in toks if t["pos"] == "V" and t["root"])
    n_multi = sum(1 for t in toks if t["pos"] == "V" and t["root"] in multi_roots)

    # phase crosstab / effective n (prereg §5.4)
    lab_c1 = {s: coarsen(genre[s]["sinai"], C1_ORDER) for s in range(1, 115)}
    ct = collections.defaultdict(collections.Counter)
    for s in range(1, 115):
        ct[lab_c1[s]][phase_of(genre[s]["phase"])] += 1
    degenerate = [c for c, v in ct.items()
                  if sum(1 for p in ("Meccan", "Medinan") if v[p] > 0) < 2]
    n_degenerate = sum(sum(ct[c].values()) for c in degenerate)

    census = {
        "verb_form_counts": dict(verb_forms),
        "all_pos_form_counts": dict(all_forms),
        "form_tagged_by_pos": dict(by_pos),
        "explicit_form_I_tags_on_verbs": 0,
        "verbs_untagged_treated_as_form_I": verb_forms["I"],
        "distinct_verb_lemmas": len(lem2f),
        "verb_lemmas_with_more_than_one_form": sum(1 for v in lem2f.values() if len(v) > 1),
        "distinct_verb_roots": len(root2f),
        "verb_roots_with_more_than_one_form": len(multi_roots),
        "verb_tokens_on_multi_form_roots": n_multi,
        "verb_tokens_on_single_form_roots": nverb - n_multi,
        "legal_marker_form_IV_tokens": len(marker_hits),
        "sparse_forms_excluded": SPARSE_EXCLUDED,
        "phase_crosstab_C1": {k: dict(v) for k, v in ct.items()},
        "phase_degenerate_registers": sorted(degenerate),
        "n_in_phase_degenerate_strata": n_degenerate,
        "effective_n_against_phase": 114 - n_degenerate,
    }

    cells = {}
    # confirmatory family: T1 x R1 (prereg §7)
    cells["PRIMARY_T1_R1"] = run_cell(toks, genre, lens, "T1", "sinai", C1_ORDER, marker_hits)
    # robustness tuples (prereg §6) — descriptive, cannot alter the verdict
    cells["T2_allpos_R1"] = run_cell(toks, genre, lens, "T2", "sinai", C1_ORDER, marker_hits)
    cells["T3_lemmatypes_R1"] = run_cell(toks, genre, lens, "T3", "sinai", C1_ORDER, marker_hits)
    cells["T1_R2_neuwirth"] = run_cell(toks, genre, lens, "T1", "neuwirth", C1_ORDER, marker_hits)
    cells["T1_R3_coarsenC2"] = run_cell(toks, genre, lens, "T1", "sinai", C2_ORDER, marker_hits)
    cells["T1_R1_markerablated"] = run_cell(toks, genre, lens, "T1", "sinai", C1_ORDER,
                                            marker_hits, ablate_marker=True)
    cells["T1_R1_min20"] = run_cell(toks, genre, lens, "T1", "sinai", C1_ORDER,
                                    marker_hits, min_tokens=MIN_TOKENS_M2)

    primary = cells["PRIMARY_T1_R1"]
    verdict = decide(primary["arms"], primary["S_star_H1ROOT"], primary["S_max_H1ROOT"])

    result = {
        "finding_id": "H-NEW-3130",
        "frontier_item": "F-6",
        "title": "Is the per-surah derived-verb-form distribution a register signature "
                 "independent of root vocabulary?",
        "run_utc": stamp,
        "hashes": hashes,
        "prereg_sha256": EXPECTED_PREREG_SHA,
        "seeds": {"null_A_register_shuffle": SEED_NULL_A,
                  "null_B_within_root_form_shuffle": SEED_NULL_B},
        "n_perms": N_PERM,
        "k_bonferroni": K_BONFERRONI,
        "alpha_bonferroni": ALPHA_BON,
        "binding_raw_gate": BINDING_GATE,
        "census": census,
        "cells": cells,
        "verdict": verdict,
        "verdict_rule": "prereg §7, evaluated in order: UNTESTABLE-AT-THIS-N / NULL / "
                        "ROOT-EXPLAINED / CONFIRMED / DIRECTIONAL",
        "confirmatory_family": ["H1-RAW", "H1-ROOT", "D1-RAW", "D1-ROOT", "D2-RAW", "D2-ROOT"],
        "arm_pass_flags": {k: bool(v["passes"]) for k, v in primary["arms"].items()},
    }

    with open(os.path.join(run_dir, "result.json"), "x", encoding="utf-8") as fh:
        json.dump(result, fh, ensure_ascii=False, indent=2, sort_keys=True)

    manifest = {
        "run_utc": stamp,
        "script": os.path.relpath(os.path.abspath(__file__), REPO),
        "script_sha256": sha256(os.path.abspath(__file__)),
        "prereg": PREREG_REL, "prereg_sha256": EXPECTED_PREREG_SHA,
        "inputs": {QAC_REL: EXPECTED_QAC_SHA, GENRE_REL: EXPECTED_GENRE_SHA},
        "python": sys.version, "numpy": np.__version__,
        "seeds": {"A": SEED_NULL_A, "B": SEED_NULL_B}, "n_perms": N_PERM,
        "verdict": verdict,
    }
    try:
        manifest["git_head"] = subprocess.check_output(
            ["git", "-C", REPO, "rev-parse", "HEAD"], text=True).strip()
    except Exception as exc:
        manifest["git_head"] = "unavailable: %s" % exc
    with open(os.path.join(run_dir, "manifest.json"), "x", encoding="utf-8") as fh:
        json.dump(manifest, fh, ensure_ascii=False, indent=2, sort_keys=True)

    print("H-NEW-3130 — run %s" % stamp)
    print("run dir: %s" % run_dir)
    print()
    print("VERDICT: %s" % verdict)
    print()
    print("Confirmatory family (T1 x R1), binding raw gate p < %.4f:" % BINDING_GATE)
    for name in result["confirmatory_family"]:
        a = primary["arms"][name]
        print("  %-9s obs[%s]=%+.4f  p_worst=%.5f (%s)  p_best=%.5f (%s)  swing=%.1fx  "
              "dir_ok=%s  PASS=%s"
              % (name, a["worst_channel"], a["observed"][a["worst_channel"]],
                 a["p_worst"], a["worst_channel"], a["p_best"], a["best_channel"],
                 a["p_swing"], a["direction_ok"], a["passes"]))
    print()
    print("S* = %.4f  S_max = %.4f  untestable branch fires: %s"
          % (primary["S_star_H1ROOT"], primary["S_max_H1ROOT"],
             primary["S_star_H1ROOT"] > primary["S_max_H1ROOT"]))
    print("effective n against phase: %d of 114 (degenerate registers: %s)"
          % (census["effective_n_against_phase"], ", ".join(census["phase_degenerate_registers"])))
    return 0


if __name__ == "__main__":
    sys.exit(main())
