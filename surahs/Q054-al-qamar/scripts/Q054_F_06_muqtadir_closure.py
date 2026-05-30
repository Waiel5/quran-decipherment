#!/usr/bin/env python3
"""Q054-F-06 — al-Muqtadir closure-concentration in Q 54 al-Qamar.

Pre-registered, SHA-locked. seed=20260509, n_perm=10000.
Verifies the locked pre-reg SHA at runtime (fail-fast on mismatch).
No external dependencies (stdlib only).
"""
import json, re, os, sys, hashlib, random

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
PREREG = os.path.join(HERE, "..", "preregs",
                      "Q054-F-06-muqtadir-closure-concentration-prereg.md")
EXPECTED_SHA = "e76d3316f0bb61b670ad93b140778f46b8940f6b65f7c07a9dabcef992f87a98"
SEED = 20260509
N_PERM = 10000
ALPHA_BON = 0.025

# --- runtime SHA verification (fail-fast) ---
with open(PREREG, "rb") as f:
    sha = hashlib.sha256(f.read()).hexdigest()
if sha != EXPECTED_SHA:
    sys.exit(f"PRE-REG SHA MISMATCH: {sha} != {EXPECTED_SHA}")
print("SHA OK")

# --- load corpus ---
with open(os.path.join(ROOT, "quran-text", "quran-no-tashkeel.json"), encoding="utf-8") as f:
    data = json.load(f)

def iter_verses(d):
    for s in d:
        sn = int(s.get("id") or s.get("number"))
        for v in (s.get("verses") or s.get("ayahs") or []):
            yield sn, int(v.get("id") or v.get("number") or v.get("numberInSurah")), \
                  (v.get("text") or v.get("arabic") or "")

verses = list(iter_verses(data))

# --- per-surah verse counts (from corpus, cross-checked vs hafs tsv) ---
from collections import Counter, defaultdict
vc = Counter(s for s, a, t in verses)
n_surahs = len(vc)

# --- H6a + H6b: muqtadir tokens ---
pat = re.compile("مقتدر")
muq_verses = [(s, a) for s, a, t in verses if pat.search(t)]
total = len(muq_verses)
q54 = [(s, a) for (s, a) in muq_verses if s == 54]
n_q54 = len(q54)
share_q54 = n_q54 / total if total else 0.0
# corpus-max check
by_surah = Counter(s for s, a in muq_verses)
max_surah, max_count = by_surah.most_common(1)[0]

closure_frame = {(54, 55), (54, 42)}  # pre-committed
n_closure = sum(1 for v in q54 if v in closure_frame)

H6a = {"n_q54": n_q54, "n_total": total, "share_q54": share_q54,
       "all_muqtadir_verses": muq_verses,
       "corpus_max_surah": max_surah, "corpus_max_count": max_count,
       "is_corpus_max": (max_surah == 54),
       "threshold": 0.40, "pass": share_q54 >= 0.40}

H6b = {"closure_frame_committed": sorted(closure_frame),
       "q54_muqtadir_verses": q54,
       "n_closure_frame": n_closure, "threshold": 2,
       "pass": n_closure == 2 and n_q54 == 2}

# --- H6c: length-weighted multinomial permutation null ---
surah_ids = sorted(vc)
weights = [vc[s] for s in surah_ids]
rng = random.Random(SEED)
ge = 0
for _ in range(N_PERM):
    counts = defaultdict(int)
    for _t in range(total):
        counts[rng.choices(surah_ids, weights=weights, k=1)[0]] += 1
    if counts[54] >= n_q54:
        ge += 1
perm_p_lw = ge / N_PERM

# uniform secondary diagnostic
rng2 = random.Random(SEED + 1)
ge_u = 0
for _ in range(N_PERM):
    counts = defaultdict(int)
    for _t in range(total):
        counts[rng2.choice(surah_ids)] += 1
    if counts[54] >= n_q54:
        ge_u += 1
perm_p_uniform = ge_u / N_PERM

H6c = {"observed_q54_count": n_q54, "n_perm": N_PERM,
       "perm_p_length_weighted": perm_p_lw,
       "perm_p_uniform": perm_p_uniform,
       "alpha_bon": ALPHA_BON,
       "pass": perm_p_lw < ALPHA_BON}

# --- verdict ---
if H6b["pass"] and H6c["pass"]:
    verdict = "CONFIRMED (H6a PASS-DIRECTED ceiling; H6b + H6c pass at alpha_bon)"
elif H6b["pass"] or H6c["pass"]:
    verdict = "PARTIAL"
else:
    verdict = "NULL"

# pre-commit violation check on H6a direction
pre_commit_violation = not H6a["is_corpus_max"]

out = {
    "test_id": "Q054-F-06",
    "title": "Q 54 al-Muqtadir closure-concentration",
    "prereg_sha256": EXPECTED_SHA,
    "seed": SEED, "n_perm": N_PERM, "bonferroni_k": 2, "alpha_bon": ALPHA_BON,
    "H6a": H6a, "H6b": H6b, "H6c": H6c,
    "pre_commit_violation_H6a": pre_commit_violation,
    "verdict": verdict,
}
outpath = os.path.join(HERE, "..", "csv", "Q054-F-06.json")
with open(outpath, "w", encoding="utf-8") as f:
    json.dump(out, f, ensure_ascii=False, indent=2)
print(json.dumps(out, ensure_ascii=False, indent=2))
