#!/usr/bin/env python3
"""Extract fire/light vocabulary inventories from Leeds QAC morphology."""
import re, json, collections, os, sys

MORPH = "/Users/grey/Downloads/quran/data/morphology/quranic-corpus-morphology-0.4.txt"
QURAN = "/Users/grey/Downloads/quran/quran-text/quran-no-tashkeel.json"

# Targets: (label, root, optional lemma filter, description)
# Roots in Buckwalter transliteration used by QAC
# nAr/nUr root = nwr (ن و ر)
# Dy' root = DwA (ض و ء) probably "Dw'"
# sirAj root = srj
# miSbAH root = SbH
# qabas root = qbs
# $ihAb root = $hb
# nafakha root = nfx
# waqUd root = wqd
# ramAd root = rmd
# Sur (horn) root = Swr

# QAC uses these root codes (per published documentation):
# nwr, Dw', srj, SbH, qbs, $hb, nfx, wqd, rmd, Swr

ROOTS = {
    "nwr": "nār/nūr (ن و ر)",
    "DwA": "ḍiyāʾ / aḍāʾa (ض و ء)",
    "srj": "sirāj (س ر ج)",
    "SbH": "miṣbāḥ / ṣubḥ (ص ب ح)",
    "qbs": "qabas (ق ب س)",
    "$hb": "shihāb (ش ه ب)",
    "nfx": "nafakha (ن ف خ)",
    "wqd": "waqūd / istawqada (و ق د)",
    "rmd": "ramād (ر م د)",
    "Swr": "ṣūr (horn) / Sūrah (ص و ر)",
}

LOC_RE = re.compile(r"\((\d+):(\d+):(\d+):(\d+)\)")
ROOT_RE = re.compile(r"ROOT:([^|]+)")
LEM_RE = re.compile(r"LEM:([^|]+)")
POS_RE = re.compile(r"POS:([^|]+)")

# Collect
by_root = collections.defaultdict(list)
with open(MORPH, encoding="utf-8") as f:
    for line in f:
        if not line.startswith("("):
            continue
        parts = line.rstrip("\n").split("\t")
        if len(parts) < 4:
            continue
        loc, form, tag, feat = parts
        m = ROOT_RE.search(feat)
        if not m:
            continue
        root = m.group(1)
        if root not in ROOTS:
            continue
        lem = LEM_RE.search(feat)
        lem = lem.group(1) if lem else ""
        pos = POS_RE.search(feat)
        pos = pos.group(1) if pos else ""
        mloc = LOC_RE.match(loc)
        s, v, w, seg = mloc.groups()
        by_root[root].append({
            "loc": loc,
            "s": int(s), "v": int(v), "w": int(w), "seg": int(seg),
            "form": form, "tag": tag, "pos": pos, "lem": lem, "feat": feat
        })

# Load Quran text for context
with open(QURAN, encoding="utf-8") as f:
    quran = json.load(f)

def verse_text(s, v):
    try:
        return quran[s-1]["verses"][v-1]["text"]
    except Exception:
        return ""

# Output inventories
out_dir = "/Users/grey/Downloads/quran/findings/phase-b-hypotheses"
os.makedirs(out_dir, exist_ok=True)

summary = {}
for root, label in ROOTS.items():
    items = by_root[root]
    # count unique tokens (by s,v,w) vs segments
    unique_tokens = set((x["s"], x["v"], x["w"]) for x in items)
    lem_counts = collections.Counter(x["lem"] for x in items)
    pos_counts = collections.Counter(x["pos"] for x in items)
    surah_dist = collections.Counter(x["s"] for x in items)
    summary[root] = {
        "label": label,
        "segments": len(items),
        "unique_tokens": len(unique_tokens),
        "lemmas": dict(lem_counts),
        "pos": dict(pos_counts),
        "top_surahs": surah_dist.most_common(10),
    }

print(json.dumps(summary, indent=2, ensure_ascii=False))

# Write full inventory CSVs
import csv
csv_dir = os.path.join(out_dir, "csv")
os.makedirs(csv_dir, exist_ok=True)
for root, items in by_root.items():
    safe = root.replace("$","sh").replace("'","q")
    path = os.path.join(csv_dir, f"fire-light-{safe}.csv")
    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["loc","surah","verse","word","seg","form","pos","lemma","tag"])
        for x in items:
            w.writerow([x["loc"],x["s"],x["v"],x["w"],x["seg"],x["form"],x["pos"],x["lem"],x["tag"]])
    print(f"Wrote {path} ({len(items)} segs)", file=sys.stderr)

# Examine specific verses
probes = [
    (2, 17), (2, 24), (20, 10), (27, 7), (28, 29),
    (24, 35), (33, 46), (71, 16),
    (37, 10), (72, 9),
    (14, 18), (66, 6),
    (39, 68), (69, 13), (18, 99), (74, 8), (6, 73), (50, 20), (36, 51), (23, 101), (79, 13), (27, 87), (78, 18),
]
print("\n=== VERSE PROBES ===", file=sys.stderr)
for s, v in probes:
    print(f"\nQ {s}:{v} — {verse_text(s,v)}", file=sys.stderr)

# All verses that contain each root
print("\n=== nAr/nur verse list (unique s:v) ===", file=sys.stderr)
for root in ["nwr"]:
    verses = sorted(set((x["s"], x["v"]) for x in by_root[root]))
    print(f"{root}: {len(verses)} unique verses", file=sys.stderr)

# Split nwr by lemma (which lemmas are nar vs nur?)
print("\n=== nwr lemma breakdown ===", file=sys.stderr)
for lem, n in collections.Counter(x["lem"] for x in by_root["nwr"]).most_common():
    print(f"  {lem}: {n}", file=sys.stderr)
