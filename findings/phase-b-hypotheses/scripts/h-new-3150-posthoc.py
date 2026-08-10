#!/usr/bin/env python3
"""H-NEW-3150 POST-HOC — the pre-registered rime control was ORTHOGRAPHIC and did not
control rhyme. This re-runs the six confirmatory arms under a PHONOLOGICAL rime and
over the full nominal frame (not just the 35% the template matcher labels).

POST-HOC. Not pre-registered. Reported as post-hoc in the finding.
"""
import bisect, collections, hashlib, json, math, os, random, re, sys
from datetime import datetime, timezone
from pathlib import Path
ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "findings/phase-b-hypotheses/scripts"))
import importlib.util
spec = importlib.util.spec_from_file_location(
    "main3150", ROOT / "findings/phase-b-hypotheses/scripts/h-new-3150.py")
M = importlib.util.module_from_spec(spec); spec.loader.exec_module(M)

VOW = set("aui"); LONG = {"iy": "ii", "uw": "uu", "aA": "aa"}; DIPH = {"ay": "ay", "aw": "aw"}
def rime_v(lem):
    """Phonological rime from the VOCALISED lemma: (nucleus, final consonant)."""
    L = M.norm_lemma(lem)
    if not L: return ("?", "?")
    if L.endswith("~"): c, rest = L[-2], L[:-2]
    else: c, rest = L[-1], L[:-1]
    for k, v in list(LONG.items()) + list(DIPH.items()):
        if rest.endswith(k): return (v, c)
    if rest.endswith("A") or rest.endswith("`"): return ("aa", c)
    if rest and rest[-1] in VOW: return ("V" + rest[-1], c)
    if rest.endswith("o"): return ("C0", c)
    return ("-", c)

def main():
    M.verify_prereg()
    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    out = ROOT / "findings/phase-b-hypotheses/runs/h-new-3150-posthoc" / stamp
    os.makedirs(out, exist_ok=False)
    print("post-hoc run dir:", out)

    segs = []
    with open(M.QAC, encoding="utf-8") as fh:
        for line in fh:
            if not line.startswith("("): continue
            p = line.rstrip("\n").split("\t")
            if len(p) < 4: continue
            loc = p[0].strip("()").split(":"); feats = p[3]
            g = lambda pat: (re.search(pat, feats).group(1) if re.search(pat, feats) else None)
            segs.append(dict(s=int(loc[0]), v=int(loc[1]), w=int(loc[2]),
                             pos=g(r"POS:(\w+)"), lem=g(r"LEM:([^|]+)"), root=g(r"ROOT:([^|]+)")))
    wmax, nseg = collections.defaultdict(int), collections.Counter()
    for x in segs:
        k = (x["s"], x["v"]); wmax[k] = max(wmax[k], x["w"]); nseg[k] += 1
    rootfreq = collections.Counter(x["root"] for x in segs if x["root"])
    names = set()
    for raw in open(M.NAMES, encoding="utf-8"):
        l = " ".join(raw.strip().split())
        if l and not l.startswith("#") and len(l.split()) == 1: names.add(M.strip_al(l))

    rows = []
    for x in segs:
        if x["pos"] not in ("N", "ADJ") or not x["lem"]: continue
        wz, _ = M.machine_wazn(x["lem"], x["root"]) if x["root"] else (None, 0)
        k = (x["s"], x["v"]); ar = M.bw2ar(M.norm_lemma(x["lem"]))
        keys = {M.bare(ar, d) for d in ("ا", "")}; keys |= {M.strip_al(z) for z in keys}
        rows.append(dict(s=x["s"], v=x["v"], w=x["w"],
                         wazn=wz or "UNLABELLED",
                         mub=int(bool(wz) and wz in M.MUBALAGHA6),
                         final=int(x["w"] == wmax[k]), nwords=wmax[k], nsegs=nseg[k],
                         divine=int(bool(keys & names)), rcv=rime_v(x["lem"]),
                         rare=int(rootfreq.get(x["root"], 0) <= M.RARE_ROOT_MAX),
                         root=x["root"]))
    nn = collections.Counter((r["s"], r["v"]) for r in rows)
    for r in rows: r["nnom"] = nn[(r["s"], r["v"])]
    print(f"FULL nominal frame: {len(rows)} (vs {sum(1 for r in rows if r['wazn']!='UNLABELLED')} template-labelled)")

    LONGSET = {"ii", "uu", "aa"}
    for r in rows: r["longrime"] = int(r["rcv"][0] in LONGSET)
    t = collections.Counter((r["longrime"], r["mub"]) for r in rows)
    lr = [r for r in rows if r["longrime"]]
    print(f"long-rime nominal stems: {len(lr)}  mub {sum(r['mub'] for r in lr)}  "
          f"non-mub {sum(1-r['mub'] for r in lr)}")
    print(f"  verse-final rate  mub {sum(r['final'] for r in lr if r['mub'])/max(sum(r['mub'] for r in lr),1):.1%}"
          f"   non-mub {sum(r['final'] for r in lr if not r['mub'])/max(sum(1-r['mub'] for r in lr),1):.1%}")

    def qbin(vals, k):
        s = sorted(vals); cuts = [s[int(len(s)*i/k)] for i in range(1, k)]
        return [bisect.bisect_left(cuts, v) for v in vals]
    dv = {(r["s"], r["v"]) for r in rows if r["divine"]}
    sub = [r for r in rows if (r["s"], r["v"]) not in dv]
    res = {}
    for tag, pool, use_div in (("P", rows, True), ("PDF", sub, False)):
        for ch, key in (("CH-W", "nwords"), ("CH-S", "nsegs"), ("CH-N", "nnom")):
            b = qbin([r[key] for r in pool], M.N_BINS)
            keys = [((bi, r["rare"], r["divine"], r["rcv"]) if use_div
                     else (bi, r["rare"], r["rcv"])) for r, bi in zip(pool, b)]
            res[f"{tag}|{ch}"] = M.run_arm(pool, keys, "mub", M.SEED, M.N_PERM)

    lines = [f"H-NEW-3150 POST-HOC  {stamp}  seed={M.SEED} n_perm={M.N_PERM}",
             "phonological rime, FULL nominal frame (template-unlabelled tokens retained "
             "in the comparison arm)", "",
             f"{'arm':<10}{'strata':>7}{'tokens':>8}{'obs':>7}{'exp':>9}{'excess':>8}"
             f"{'rel':>8}{'z':>8}{'p_perm':>10}{'S_max':>7}"]
    for k in sorted(res):
        r = res[k]
        if r["obs"] is None: lines.append(f"{k:<10} NO-INFORMATIVE-STRATA"); continue
        lines.append(f"{k:<10}{r['n_inf']:>7}{r['n_tok']:>8}{r['obs']:>7.0f}{r['exp']:>9.1f}"
                     f"{r['excess']:>8.1f}{r['rel_excess']:>8.1%}{r['z_param']:>8.2f}"
                     f"{r['p_perm']:>10.5f}{r['smax']:>7}")
    txt = "\n".join(lines)
    with open(out / "results.json", "x") as fh:
        json.dump(dict(utc=stamp, posthoc=True, arms=res,
                       long_rime_2x2={str(k): v for k, v in t.items()},
                       n_frame=len(rows)), fh, indent=2, default=str)
    with open(out / "report.txt", "x") as fh: fh.write(txt + "\n")
    print(txt)

if __name__ == "__main__":
    main()
