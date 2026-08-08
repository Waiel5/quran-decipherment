#!/usr/bin/env python3
"""
H-NEW-860.1 POST-HOC diagnostics. Everything here is labelled POST-HOC in the finding and
changes no locked verdict. It exists because the locked run produced three results that a
reader cannot interpret without it:

  1. Q 67 al-Mulk -- the rubric's rank-3, score 10 -- returned a formal count of ZERO.
     Diagnosed here: it is known by a FOUR-word incipit and the locked span is five.
  2. The residual roster's low end is dominated by very short surahs, i.e. by the
     instrument's floor rather than by neglect. A length-controlled roster is built.
  3. Only the primary arm carried a length null. Cell B and the naming arm get one here.

Plus an EXTERNAL cross-check the locked run did not use: this repository already contains
independent per-surah hadith extractions built 2026-04-28 by a different method (alias-rich
name search, Arabic + English). They are a second construction of the same measurement.

Writes to its OWN run directory. Never touches the locked run's directory.
Waiel Al-Shujaa, 2026-08-08.
"""
import glob
import hashlib
import json
import math
import os
import re
import sys
from collections import Counter, defaultdict
from datetime import datetime, timezone

import numpy as np
from scipy import stats

REPO = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", ".."))
os.chdir(REPO)
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

LOCKED_RUN = sys.argv[1] if len(sys.argv) > 1 else sorted(
    glob.glob("runs/h-new-860-1/*"))[0]
RES = json.load(open(os.path.join(LOCKED_RUN, "result.json"), encoding="utf-8"))

STAMP = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
RUNDIR = os.path.join("runs", "h-new-860-1", STAMP + "-posthoc")
os.makedirs(RUNDIR, exist_ok=False)
OUT, LOGL = {}, []


def log(m):
    print(m, flush=True)
    LOGL.append(m)


log(f"POST-HOC for locked run {LOCKED_RUN}")

# ---- re-import the locked instrument by executing the runner's definitions only ----
import importlib.util
spec = importlib.util.spec_from_file_location(
    "h8601", os.path.join("findings", "phase-b-hypotheses", "scripts", "h-new-860-1.py"))
src = open(spec.origin, encoding="utf-8").read()
HEAD = src[:src.index("# ---------------------------------------------------------------- run directory")]
ns = {"__name__": "h8601_head", "__file__": spec.origin}
exec(compile(HEAD, spec.origin, "exec"), ns)
norm, MINW, IDX_N = ns["norm"], ns["MINW"], ns["IDX_N"]
BOOKS9, HDIR, QURAN = ns["BOOKS9"], ns["HDIR"], ns["QURAN"]
log("locked normaliser and constants re-imported from the runner (head section only)")

quran = json.load(open(QURAN, encoding="utf-8"))
verses = [(su["id"], v["id"], norm(v["text"]).split()) for su in quran for v in su["verses"]]
VW = {(s, a): w for s, a, w in verses}
recs, rec_book = [], []
for b in BOOKS9:
    for h in json.load(open(os.path.join(HDIR, "the_9_books", b + ".json"),
                            encoding="utf-8"))["hadiths"]:
        recs.append(norm(h.get("arabic") or ""))
        rec_book.append(b)
PAD = [" " + t + " " for t in recs]
HWD = [t.split() for t in recs]
IDX = defaultdict(list)
for i, w in enumerate(HWD):
    seen = set()
    for j in range(len(w) - IDX_N + 1):
        g = " ".join(w[j:j + IDX_N])
        if g not in seen:
            seen.add(g)
            IDX[g].append(i)


def link_surah(N):
    spans_of, lens = {}, set()
    for s, a, w in verses:
        if len(w) < MINW:
            spans_of[(s, a)] = []
            continue
        n = min(N, len(w))
        lens.add(n)
        spans_of[(s, a)] = [" ".join(w[j:j + n]) for j in range(len(w) - n + 1)]
    own = defaultdict(set)
    for s, a, w in verses:
        for L in lens:
            for j in range(len(w) - L + 1):
                own[" ".join(w[j:j + L])].add((s, a))
    per = defaultdict(set)
    for s, a, w in verses:
        for sp in spans_of[(s, a)]:
            if len({x[0] for x in own[sp]}) != 1:
                continue
            c = IDX.get(" ".join(sp.split()[:IDX_N]))
            if not c:
                continue
            t = " " + sp + " "
            for i in c:
                if t in PAD[i]:
                    per[s].add(i)
    return {s: len(per.get(s, set())) for s in range(1, 115)}


ARMC = {N: link_surah(N) for N in (4, 5, 6)}

# ---- 1. N-sensitivity on the rubric's top-10 -------------------------------------------
RUB = {int(k[1:]): v["score"] for k, v in
       json.load(open("findings/phase-b-hypotheses/csv/h-new-860.json",
                      encoding="utf-8"))["hadith_emphasis_scores"].items()}
top10 = sorted(RUB, key=lambda s: (-RUB[s], s))[:10]
log("\n1. SPAN SENSITIVITY on the rubric's top-10 surahs (quotation instrument, surah level)")
log(f"   {'surah':>6}{'rubric':>8}{'N=4':>7}{'N=5':>7}{'N=6':>7}")
sens = {}
for s in top10:
    sens[s] = {N: ARMC[N][s] for N in (4, 5, 6)}
    log(f"   Q{s:<5}{RUB[s]:>8}{ARMC[4][s]:>7}{ARMC[5][s]:>7}{ARMC[6][s]:>7}")
OUT["span_sensitivity_rubric_top10"] = sens

# ---- 2. Q 67 diagnostic ----------------------------------------------------------------
q67 = VW[(67, 1)]
log(f"\n2. Q 67:1 has {len(q67)} words: {' '.join(q67)}")
inc4 = " ".join(q67[:4])
n_inc4 = sum(1 for p in PAD if " " + inc4 + " " in p)
inc5 = " ".join(q67[:5])
n_inc5 = sum(1 for p in PAD if " " + inc5 + " " in p)
log(f"   4-word incipit  [{inc4}] occurs in {n_inc4} records")
log(f"   5-word incipit  [{inc5}] occurs in {n_inc5} records")
log(f"   -> the locked N=5 arm cannot see a surah cited by its four-word incipit.")
OUT["q67_incipit"] = dict(words=len(q67), incipit4=inc4, n_records_incipit4=n_inc4,
                          incipit5=inc5, n_records_incipit5=n_inc5,
                          surah_count_N4=ARMC[4][67], surah_count_N5=ARMC[5][67])
# how general is this? count surahs whose 4-word incipit appears but 5-word does not
gen = []
for s in range(1, 115):
    w = VW[(s, 1)]
    if len(w) < 5:
        continue
    a4 = sum(1 for p in PAD if " " + " ".join(w[:4]) + " " in p)
    a5 = sum(1 for p in PAD if " " + " ".join(w[:5]) + " " in p)
    if a4 >= 5 and a4 > 2 * max(a5, 1):
        gen.append(dict(surah=s, incipit4=" ".join(w[:4]), n4=a4, n5=a5))
log(f"   surahs whose 4-word opening is cited >=5 times and >2x its 5-word extension: {len(gen)}")
for g in sorted(gen, key=lambda g: -g["n4"])[:8]:
    log(f"      Q{g['surah']:<4} n4={g['n4']:4} n5={g['n5']:4}  [{g['incipit4']}]")
OUT["incipit_truncation_general"] = gen

# ---- 3. length-controlled residual roster ----------------------------------------------
sc = RES["surah_counts"]
S = list(range(1, 115))
union = {s: sc[str(s)]["union"] for s in S}
words = {s: sc[str(s)]["words"] for s in S}
uasr = {s: sc[str(s)]["uas_rank"] for s in S}
outl = {s: sc[str(s)]["outlier"] for s in S}
r_rec = stats.rankdata([-union[s] for s in S])
r_len = stats.rankdata([-math.log(words[s]) for s in S])
b = np.column_stack([np.ones(114), r_len])
beta, *_ = np.linalg.lstsq(b, r_rec, rcond=None)
resid_rec = r_rec - b @ beta
r_out = stats.rankdata([-outl[s] for s in S])
r_uas = np.array([uasr[s] for s in S], dtype=float)
struct = np.minimum(r_uas, r_out)
gap = resid_rec - stats.zscore(struct) * np.std(resid_rec)
log("\n3. LENGTH-CONTROLLED roster (reception rank residualised on log surah word count)")
log("   structurally extreme, cited far less than its LENGTH predicts:")
order = np.argsort(-(resid_rec))
neglected = []
for i in order:
    s = S[i]
    if struct[i] <= 30:
        neglected.append(dict(surah=s, uas_rank=uasr[s], outlier_rank=int(r_out[i]),
                              union=union[s], words=words[s],
                              length_residual=float(resid_rec[i])))
    if len(neglected) >= 12:
        break
for r in neglected:
    log(f"      Q{r['surah']:<4} UASrank {r['uas_rank']:3} outRank {r['outlier_rank']:3} "
        f"count {r['union']:4} words {r['words']:5}  length-residual {r['length_residual']:+7.1f}")
log("   structurally ordinary, cited far more than its length predicts:")
overcited = []
for i in np.argsort(resid_rec):
    s = S[i]
    if struct[i] >= 60:
        overcited.append(dict(surah=s, uas_rank=uasr[s], outlier_rank=int(r_out[i]),
                              union=union[s], words=words[s],
                              length_residual=float(resid_rec[i])))
    if len(overcited) >= 12:
        break
for r in overcited:
    log(f"      Q{r['surah']:<4} UASrank {r['uas_rank']:3} outRank {r['outlier_rank']:3} "
        f"count {r['union']:4} words {r['words']:5}  length-residual {r['length_residual']:+7.1f}")
OUT["length_controlled_roster"] = dict(neglected=neglected, overcited=overcited)

# ---- 4. length nulls on the non-primary arms -------------------------------------------
def partial_sp(x, y, z):
    rx, ry, rz = stats.rankdata(x), stats.rankdata(y), stats.rankdata(z)
    def rs(a):
        bb = np.column_stack([np.ones(len(rz)), rz])
        be, *_ = np.linalg.lstsq(bb, a, rcond=None)
        return a - bb @ be
    r, p = stats.pearsonr(rs(rx), rs(ry))
    return float(r), float(p)


RUB_SET = sorted(RUB)
log("\n4. LENGTH NULLS on arms the locked run did not test (POST-HOC)")
for label, subset in (("cell A (36)", RUB_SET), ("cell B (114)", S)):
    for ins in ("quotation", "naming", "union"):
        x = [sc[str(s)][ins] for s in subset]
        y = [uasr[s] for s in subset]
        z = [math.log(words[s]) for s in subset]
        raw = stats.spearmanr(x, y)
        pr, pp = partial_sp(x, y, z)
        log(f"   {label:12} {ins:9}: raw rho {raw.statistic:+.4f} (p={raw.pvalue:.4g})  ->  "
            f"partial {pr:+.4f} (p={pp:.4g})")
        OUT.setdefault("partials", {})[f"{label}|{ins}"] = dict(
            raw_rho=float(raw.statistic), raw_p=float(raw.pvalue),
            partial_rho=pr, partial_p=pp)

# ---- 5. external cross-check ------------------------------------------------------------
log("\n5. EXTERNAL CROSS-CHECK against this repository's own 2026-04-28 extractions")
ext = {}
for f in sorted(glob.glob("data/literature/hadith/Q*-citations*.md")):
    m = re.search(r"Q(\d{3})", os.path.basename(f))
    txt = open(f, encoding="utf-8").read()
    t = re.search(r"Total hits across 9 books:\s*\*?\*?\s*(\d+)", txt)
    if m and t:
        ext[int(m.group(1))] = dict(source=os.path.basename(f), n=int(t.group(1)))
for f in sorted(glob.glob("data/literature/hadith/Q*-citations*.json")):
    m = re.search(r"Q(\d{3})", os.path.basename(f))
    d = json.load(open(f, encoding="utf-8"))
    n = 0
    for v in d.values():
        n += len(v) if isinstance(v, list) else sum(len(x) for x in v.values())
    if m:
        ext[int(m.group(1))] = dict(source=os.path.basename(f), n=n)
log(f"   {'surah':>6}{'independent':>13}{'this run (U)':>14}{'quotation':>11}{'naming':>8}  method note")
NOTE = {1: "alias-rich name search (umm al-kitab, al-sab' al-mathani) + English",
        2: "alias + English", 6: "hand-tagged verse motifs", 9: "alias + English",
        19: "hand-tagged narrative motifs", 33: "hand-tagged verse + English motifs"}
for s in sorted(ext):
    log(f"   Q{s:<5}{ext[s]['n']:>13}{union[s]:>14}{sc[str(s)]['quotation']:>11}"
        f"{sc[str(s)]['naming']:>8}  {NOTE.get(s,'')}")
OUT["external_crosscheck"] = {str(s): dict(independent=ext[s]["n"], source=ext[s]["source"],
                                           this_union=union[s],
                                           this_quotation=sc[str(s)]["quotation"],
                                           this_naming=sc[str(s)]["naming"])
                              for s in ext}

# ---- write ------------------------------------------------------------------------------
with open(os.path.join(RUNDIR, "result.json"), "x", encoding="utf-8") as f:
    json.dump(dict(id="H-NEW-860.1-posthoc", locked_run=LOCKED_RUN, run=STAMP, **OUT),
              f, ensure_ascii=False, indent=2, default=str)
with open(os.path.join(RUNDIR, "console.log"), "x", encoding="utf-8") as f:
    f.write("\n".join(LOGL) + "\n")
print(f"\nPOST-HOC DONE -> {RUNDIR}")
