#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
H-NEW-2690 — POST-HOC DIAGNOSTICS. NOT PRE-REGISTERED.

Descriptive only, MW-7-capped at single-test alpha = 0.05, no Bonferroni standing, no
verdict authority. Written to be reported whatever it returned.

Two fair objections to the registered result are answered here:

  D1. THE ṬAWĪL ATTRACTOR. H3(b) locked "the modal best-meter of the mufaṣṣal is rajaz or
      sarīʿ" and observed ṭawīl. But if ṭawīl is also the modal best-match for RANDOM
      syllable strings, then the argmin-meter statistic is reporting a property of the
      instrument, not of the text, and H3(b) was never a real test. Measured directly.

  D2. H2 MEASURES REGULARITY, NOT METRE-SPECIFICITY. The registered H2 flags a baḥr as
      "matching" when Qurʾānic conformity beats matched noise. If a text is more
      rhythmically regular than random in general, that criterion flags essentially every
      baḥr at once — which is not what "matches a metre" means. The meter-specificity
      spread (best baḥr vs median baḥr, within each corpus) separates the two readings.

Reuses the locked scanner and meter table by importing the primary script's definitions,
so every SHA is re-verified and nothing is re-implemented. Writes to its OWN immutable run
directory; the primary run directories are never touched.

Author: Waiel Al-Shujaa.
"""
import json, os, sys, random, statistics, datetime, re

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
CSV = os.path.join(ROOT, "csv")

src = open(os.path.join(HERE, "h-new-2690.py"), encoding="utf-8").read()
G = {"__name__": "posthoc", "__file__": os.path.join(HERE, "h-new-2690.py")}
exec(src.split("_a = sha256_file(PREREG)")[0], G)                       # constants + SHA fns
exec("# 1. Syllabifier" + src.split("# 1. Syllabifier")[1].split("# 3. POSITIVE CONTROL")[0], G)

# re-verify every frozen input (the primary script's own gate, applied here too)
for p, want in G["FROZEN"].items():
    if G["sha256_file"](p) != want:
        raise SystemExit(f"[FATAL] frozen input changed: {p}")
print("[posthoc] frozen inputs re-verified")
print("[posthoc] NOT PRE-REGISTERED — descriptive, MW-7 cap alpha=0.05, no Bonferroni standing\n")

scan, metricality, METERS = G["scan"], G["metricality"], G["METERS"]
MNAMES = [m[0] for m in METERS]
SEED = G["SEED"]
MODE = "P_forceheavy"
SAMPLE = 900                      # seed-locked; a descriptive diagnostic, not an inference

AR = re.compile("[ء-ي]")
DIAC = re.compile("[ً-ْٰٓ-ٕۡ]")

quran = json.load(open(G["QURAN"], encoding="utf-8"))
QV = [(si, v["text"]) for si, su in enumerate(quran["chapters"] if isinstance(quran, dict) else quran, 1)
      for v in su["verses"]]
poetry = []
for stem in G["GROUND"]:
    for l in open(os.path.join(G["MUAL"], stem + ".txt"), encoding="utf-8", errors="replace"):
        a = len(AR.findall(l))
        if a >= 12 and len(DIAC.findall(l)) / a >= 0.55:
            poetry.append(l.strip())
dar = json.load(open(G["DARIMI"], encoding="utf-8"))
prose = []
for h in dar["hadiths"]:
    for s in re.split(r"[.؟!]", h.get("arabic") or ""):
        if len(AR.findall(s)) >= 10:
            prose.append(s.strip())

rng = random.Random(SEED)
q_s = [t for _, t in rng.sample(QV, SAMPLE)]
p_s = poetry if len(poetry) <= SAMPLE else rng.sample(poetry, SAMPLE)
r_s = prose if len(prose) <= SAMPLE else rng.sample(prose, SAMPLE)

def strs(texts):
    return [s for s in (scan(t, MODE) for t in texts) if len(s) >= 4]

def noise(ss, seed):
    r = random.Random(seed)
    return ["".join("-" if r.random() < (o.count("-") / len(o)) else "v" for _ in o) for o in ss]

ARMS = {}
for nm, ss in (("quran", strs(q_s)), ("poetry", strs(p_s)), ("prose", strs(r_s))):
    ARMS[nm] = ss
    ARMS[nm + "_noise"] = noise(ss, SEED)

PROF = {}
for nm, ss in ARMS.items():
    PROF[nm] = [metricality(o) for o in ss]
    print(f"  profiled {nm}: n={len(ss)}")

# --- D1: the ṭawīl attractor -------------------------------------------------
print("\nD1 — modal best-meter by arm (is the argmin a property of the text or the instrument?)")
d1 = {}
for nm, pr in PROF.items():
    votes = {}
    for _, k, _ in pr:
        if k:
            votes[k] = votes.get(k, 0) + 1
    tot = sum(votes.values()) or 1
    top = sorted(votes.items(), key=lambda kv: (-kv[1], MNAMES.index(kv[0])))[:4]
    d1[nm] = {"n": tot, "modal": top[0][0], "modal_share": round(top[0][1] / tot, 4),
              "top4": {k: round(v / tot, 4) for k, v in top}}
    print(f"   {nm:<14} modal={top[0][0]:<11} {top[0][1] / tot:5.1%}   "
          + "  ".join(f"{k}={v / tot:.0%}" for k, v in top))
same = d1["quran"]["modal"] == d1["quran_noise"]["modal"]
print(f"   -> Qurʾān and its matched noise share a modal meter: {same}"
      f"  ({d1['quran']['modal']} vs {d1['quran_noise']['modal']})")
print("   -> if True, the argmin-meter statistic is an instrument attractor and H3(b) "
      "was not a real test of the text.")

# --- D2: metre-specificity ---------------------------------------------------
print("\nD2 — metre-SPECIFICITY: how far the best baḥr beats the median baḥr, per unit")
d2 = {}
for nm, pr in PROF.items():
    spread = []
    for _, _, per in pr:
        if not per:
            continue
        vals = sorted(per.values())
        spread.append(vals[len(vals) // 2] - vals[0])
    if not spread:
        continue
    d2[nm] = {"median_spread": round(statistics.median(spread), 5),
              "mean_spread": round(statistics.mean(spread), 5), "n": len(spread)}
    print(f"   {nm:<14} median(median_baḥr - best_baḥr) = {d2[nm]['median_spread']:.5f}")
print("   -> a text that genuinely sits IN a metre has a large spread (one baḥr clearly "
      "wins).\n   -> a text that is merely regular has a small spread (all buḥūr improve "
      "together).")
sp_q, sp_p = d2["quran"]["median_spread"], d2["poetry"]["median_spread"]
sp_qn = d2["quran_noise"]["median_spread"]
print(f"   poetry={sp_p:.5f}  Qurʾān={sp_q:.5f}  Qurʾān-noise={sp_qn:.5f}   "
      f"Qurʾān/poetry = {sp_q / sp_p:.2f}x")

stamp = datetime.datetime.now(datetime.timezone.utc).strftime("%Y%m%dT%H%M%SZ")
RUN = os.path.join(ROOT, "runs", "h-new-2690", f"{stamp}-posthoc")
if os.path.exists(RUN):
    raise SystemExit("[FATAL] run dir exists (immutability)")
os.makedirs(RUN)
out = {"id": "H-NEW-2690-POSTHOC",
       "status": "NOT PRE-REGISTERED — descriptive, MW-7 capped, no verdict authority",
       "mode": MODE, "sample_per_arm": SAMPLE, "seed": SEED,
       "D1_modal_meter_by_arm": d1,
       "D1_quran_and_noise_share_modal": same,
       "D2_metre_specificity_spread": d2}
json.dump(out, open(os.path.join(RUN, "result.json"), "w", encoding="utf-8"),
          ensure_ascii=False, indent=2)
json.dump({"id": "H-NEW-2690-POSTHOC", "utc": stamp,
           "script_sha256": G["sha256_file"](os.path.abspath(__file__)),
           "prereg_sha256_of_primary": G["PREREG_SHA256"],
           "status": "post-hoc supplement, no verdict authority",
           "immutability": "Immutable. Never delete or overwrite, per prereg §8."},
          open(os.path.join(RUN, "manifest.json"), "w", encoding="utf-8"),
          ensure_ascii=False, indent=2)
json.dump(out, open(os.path.join(CSV, "h-new-2690-posthoc.json"), "w", encoding="utf-8"),
          ensure_ascii=False, indent=2)
print(f"\n[run] {RUN}")
