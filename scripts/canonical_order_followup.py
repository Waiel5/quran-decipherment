#!/usr/bin/env python3
"""
Follow-up sensitivity: test whether the recovered-path's 17 adjacent-pair
hits REQUIRE the length metric, or whether they survive WITHOUT length.

Also: test MVL-only recovered order vs canonical with full null (the
principal-dimension claim).

Also: compute "residual tau" — after regressing out length from the
adjacency, does any structural residual recover canonical order above
chance? This separates "length-descending is canonical" from
"structural-beyond-length encodes canonical".
"""
import json
import gzip
import math
import random
import re
import time
from collections import Counter
from pathlib import Path
import sys

import numpy as np
from scipy import stats

ROOT = Path("/Users/grey/Downloads/quran")
CORPUS = ROOT / "quran-text" / "quran-no-tashkeel.json"
ROOTGRAPH = ROOT / "data" / "morphology" / "surah-root-graph.json"
OUT_CSV = ROOT / "findings" / "phase-b-hypotheses" / "csv"

SEED = 20260412
random.seed(SEED)
np.random.seed(SEED)

with open(CORPUS) as f:
    quran = json.load(f)

def norm(s):
    return re.sub(r"\s+", " ", s).strip()

N = 114
IDS = list(range(1, N + 1))
surahs = {}
for s in quran:
    sid = s["id"]
    verses = [v["text"] for v in s["verses"]]
    surahs[sid] = {
        "name": s["transliteration"],
        "text": norm(" ".join(verses)),
        "mean_vl": np.mean([len(v) for v in verses]),
    }

with open(ROOTGRAPH) as f:
    rg = json.load(f)
surah_roots = {int(k): v for k, v in rg["surahs"].items()}
all_roots = sorted({r for c in surah_roots.values() for r in c})
root_index = {r: i for i, r in enumerate(all_roots)}
R = len(all_roots)
root_mat = np.zeros((N, R))
for i, sid in enumerate(IDS):
    for r, c in surah_roots.get(sid, {}).items():
        root_mat[i, root_index[r]] = c

# ---------- Compute 5 sub-distances again ----------
texts = [surahs[IDS[i]]["text"] for i in range(N)]

def gz(s):
    return len(gzip.compress(s.encode("utf-8"), compresslevel=9))

C = np.array([gz(t) for t in texts])
NCD = np.zeros((N, N))
for i in range(N):
    for j in range(i + 1, N):
        c_xy = gz(texts[i] + " " + texts[j])
        d = (c_xy - min(C[i], C[j])) / max(C[i], C[j])
        NCD[i, j] = d; NCD[j, i] = d

root_sets = [set(surah_roots.get(IDS[i], {}).keys()) for i in range(N)]
JAC = np.zeros((N, N))
for i in range(N):
    for j in range(i + 1, N):
        a, b = root_sets[i], root_sets[j]
        un = len(a | b)
        d = 1 - (len(a & b) / un if un else 0)
        JAC[i, j] = d; JAC[j, i] = d

def bg(s):
    s = re.sub(r"\s+", "", s)
    return Counter(s[k:k+2] for k in range(len(s) - 1))
bgc = [bg(t) for t in texts]
bg_keys = sorted({k for c in bgc for k in c})
bi = {k: i for i, k in enumerate(bg_keys)}
bm = np.zeros((N, len(bg_keys)))
for i in range(N):
    tot = sum(bgc[i].values()) or 1
    for k, c in bgc[i].items():
        bm[i, bi[k]] = c / tot
eps = 1e-10
KL = np.zeros((N, N))
for i in range(N):
    for j in range(i + 1, N):
        p = bm[i] + eps; q = bm[j] + eps
        p /= p.sum(); q /= q.sum()
        m = 0.5 * (p + q)
        js = 0.5 * (np.sum(p * np.log(p / m)) + np.sum(q * np.log(q / m)))
        KL[i, j] = js; KL[j, i] = js

MVL = np.array([surahs[IDS[i]]["mean_vl"] for i in range(N)])
MV = np.zeros((N, N))
for i in range(N):
    for j in range(i + 1, N):
        d = abs(math.log(MVL[i]) - math.log(MVL[j]))
        MV[i, j] = d; MV[j, i] = d

rn = np.linalg.norm(root_mat, axis=1); rn[rn == 0] = 1
rnor = root_mat / rn[:, None]
BOR = 1 - (rnor @ rnor.T); np.fill_diagonal(BOR, 0)

def rrank(D):
    iu, ju = np.triu_indices(N, k=1)
    v = D[iu, ju]
    o = np.argsort(v, kind="stable")
    r = np.empty_like(o, dtype=np.float64)
    r[o] = np.arange(len(v))
    r /= (len(v) - 1)
    O = np.zeros_like(D)
    O[iu, ju] = r; O[ju, iu] = r
    return O

SUB = {"NCD": rrank(NCD), "JAC": rrank(JAC), "JS": rrank(KL),
       "MVL": rrank(MV), "BOR": rrank(BOR)}

# ---------- Solver ----------
def path_cost(perm, D):
    return float(D[perm[:-1], perm[1:]].sum())

def nn_greedy(D, start):
    n = D.shape[0]
    vis = np.zeros(n, dtype=bool); perm = [start]; vis[start] = True; cur = start
    for _ in range(n - 1):
        d = D[cur].copy(); d[vis] = np.inf
        nx = int(np.argmin(d)); perm.append(nx); vis[nx] = True; cur = nx
    return np.array(perm)

def two_opt(perm, D, max_iter=10000):
    n = len(perm); best = perm.copy(); bc = path_cost(best, D)
    it = 0; imp = True
    while imp and it < max_iter:
        imp = False
        for i in range(1, n - 2):
            for j in range(i + 1, n - 1):
                a, b = best[i - 1], best[i]; c, d = best[j], best[j + 1]
                old = D[a, b] + D[c, d]; new = D[a, c] + D[b, d]
                if new + 1e-12 < old:
                    best[i:j + 1] = best[i:j + 1][::-1]
                    bc += new - old; imp = True; it += 1
                    if it >= max_iter: break
            if it >= max_iter: break
    return best, bc

def search(D, nn=114, rr=50, mi=10000):
    Dd = D.copy(); np.fill_diagonal(Dd, np.inf)
    best_p = None; best_c = math.inf
    for s in range(nn):
        seed = nn_greedy(Dd, s)
        p, c = two_opt(seed, Dd, max_iter=mi)
        if c < best_c: best_c = c; best_p = p.copy()
    for r in range(rr):
        seed = np.random.permutation(N)
        p, c = two_opt(seed, Dd, max_iter=mi)
        if c < best_c: best_c = c; best_p = p.copy()
    return best_p, best_c

# ---------- Variant 1: MVL-only ----------
print("MVL-only search...", file=sys.stderr)
p_mvl, _ = search(SUB["MVL"])
ids_mvl = [IDS[i] for i in p_mvl]
pos = {sid: i for i, sid in enumerate(ids_mvl)}
seq = [pos[sid] for sid in IDS]
canon = list(range(N))
tau_mvl, _ = stats.kendalltau(canon, seq)
seq_rev = [(N - 1) - pos[sid] for sid in IDS]
tau_mvl_rev, _ = stats.kendalltau(canon, seq_rev)
tau_mvl_use = tau_mvl_rev if abs(tau_mvl_rev) > abs(tau_mvl) else tau_mvl
dir_mvl = "reverse" if abs(tau_mvl_rev) > abs(tau_mvl) else "forward"
# adj
fp_mvl = list(reversed(ids_mvl)) if dir_mvl == "reverse" else ids_mvl
adj_mvl = len({frozenset((fp_mvl[i], fp_mvl[i + 1])) for i in range(N - 1)} &
              {frozenset((IDS[i], IDS[i + 1])) for i in range(N - 1)})

# ---------- Variant 2: 4 non-length metrics only ----------
print("NCD+JAC+JS+BOR search (no length)...", file=sys.stderr)
A4 = np.mean([SUB["NCD"], SUB["JAC"], SUB["JS"], SUB["BOR"]], axis=0)
p_4, _ = search(A4)
ids_4 = [IDS[i] for i in p_4]
pos = {sid: i for i, sid in enumerate(ids_4)}
seq = [pos[sid] for sid in IDS]
tau_4, _ = stats.kendalltau(canon, seq)
seq_rev = [(N - 1) - pos[sid] for sid in IDS]
tau_4_rev, _ = stats.kendalltau(canon, seq_rev)
tau_4_use = tau_4_rev if abs(tau_4_rev) > abs(tau_4) else tau_4
dir_4 = "reverse" if abs(tau_4_rev) > abs(tau_4) else "forward"
fp_4 = list(reversed(ids_4)) if dir_4 == "reverse" else ids_4
adj_4 = len({frozenset((fp_4[i], fp_4[i + 1])) for i in range(N - 1)} &
            {frozenset((IDS[i], IDS[i + 1])) for i in range(N - 1)})

# ---------- Variant 3: JAC-only (roots-only) ----------
print("JAC-only search...", file=sys.stderr)
p_jac, _ = search(SUB["JAC"])
ids_jac = [IDS[i] for i in p_jac]
pos = {sid: i for i, sid in enumerate(ids_jac)}
seq = [pos[sid] for sid in IDS]
tau_jac, _ = stats.kendalltau(canon, seq)
seq_rev = [(N - 1) - pos[sid] for sid in IDS]
tau_jac_rev, _ = stats.kendalltau(canon, seq_rev)
tau_jac_use = tau_jac_rev if abs(tau_jac_rev) > abs(tau_jac) else tau_jac
dir_jac = "reverse" if abs(tau_jac_rev) > abs(tau_jac) else "forward"
fp_jac = list(reversed(ids_jac)) if dir_jac == "reverse" else ids_jac
adj_jac = len({frozenset((fp_jac[i], fp_jac[i + 1])) for i in range(N - 1)} &
              {frozenset((IDS[i], IDS[i + 1])) for i in range(N - 1)})

# ---------- Variant 4: length-residualized NCD ----------
# Regress NCD(i,j) on |log MVL_i - log MVL_j|, take residual
print("Length-residualized NCD search...", file=sys.stderr)
iu, ju = np.triu_indices(N, k=1)
x = MV[iu, ju]
y = NCD[iu, ju]
slope, intercept, r, p, se = stats.linregress(x, y)
resid = y - (slope * x + intercept)
NCD_resid = np.zeros((N, N))
NCD_resid[iu, ju] = resid
NCD_resid[ju, iu] = resid
# rank-normalize
NCD_resid_rank = rrank(NCD_resid)
p_res, _ = search(NCD_resid_rank)
ids_res = [IDS[i] for i in p_res]
pos = {sid: i for i, sid in enumerate(ids_res)}
seq = [pos[sid] for sid in IDS]
tau_res, _ = stats.kendalltau(canon, seq)
seq_rev = [(N - 1) - pos[sid] for sid in IDS]
tau_res_rev, _ = stats.kendalltau(canon, seq_rev)
tau_res_use = tau_res_rev if abs(tau_res_rev) > abs(tau_res) else tau_res
dir_res = "reverse" if abs(tau_res_rev) > abs(tau_res) else "forward"
fp_res = list(reversed(ids_res)) if dir_res == "reverse" else ids_res
adj_res = len({frozenset((fp_res[i], fp_res[i + 1])) for i in range(N - 1)} &
              {frozenset((IDS[i], IDS[i + 1])) for i in range(N - 1)})

# ---------- Null for MVL-only variant (10,000 perms) ----------
print("MVL-only null (10k perms)...", file=sys.stderr)
rng = np.random.default_rng(SEED)
null_abs = np.empty(10000)
null_adj = np.empty(10000, dtype=np.int64)
canon_adj = {frozenset((IDS[i], IDS[i + 1])) for i in range(N - 1)}
for k in range(10000):
    perm = rng.permutation(N)
    pos = np.empty(N, dtype=np.int64); pos[perm] = np.arange(N)
    seq = pos[np.arange(N)]
    t, _ = stats.kendalltau(np.arange(N), seq)
    t_r, _ = stats.kendalltau(np.arange(N), (N - 1) - seq)
    null_abs[k] = max(abs(t), abs(t_r))
    ids_null = [IDS[i] for i in perm]
    null_adj[k] = len({frozenset((ids_null[i], ids_null[i + 1])) for i in range(N - 1)} & canon_adj)

p_mvl = (np.sum(null_abs >= abs(tau_mvl_use)) + 1) / 10001
p_mvl_adj = (np.sum(null_adj >= adj_mvl) + 1) / 10001
p_jac_tau = (np.sum(null_abs >= abs(tau_jac_use)) + 1) / 10001
p_jac_adj = (np.sum(null_adj >= adj_jac) + 1) / 10001
p_4_tau = (np.sum(null_abs >= abs(tau_4_use)) + 1) / 10001
p_4_adj = (np.sum(null_adj >= adj_4) + 1) / 10001
p_res_tau = (np.sum(null_abs >= abs(tau_res_use)) + 1) / 10001
p_res_adj = (np.sum(null_adj >= adj_res) + 1) / 10001

out = {
    "variant_MVL_only":      {"tau": tau_mvl_use, "dir": dir_mvl, "adj": adj_mvl, "p_tau": p_mvl, "p_adj": p_mvl_adj},
    "variant_JAC_only":      {"tau": tau_jac_use, "dir": dir_jac, "adj": adj_jac, "p_tau": p_jac_tau, "p_adj": p_jac_adj},
    "variant_4nonlength":    {"tau": tau_4_use,   "dir": dir_4,   "adj": adj_4,   "p_tau": p_4_tau,   "p_adj": p_4_adj},
    "variant_NCD_resid":     {"tau": tau_res_use, "dir": dir_res, "adj": adj_res, "p_tau": p_res_tau, "p_adj": p_res_adj},
    "note": "NCD_resid = NCD with |log-MVL-difference| regressed out; length-independent structural signal.",
    "length_MVL_canonical_corr_r": float(r),
    "length_MVL_canonical_corr_p": float(p),
}

with open(OUT_CSV / "canonical_order_followup.json", "w") as f:
    json.dump(out, f, indent=2)

print(json.dumps(out, indent=2))
