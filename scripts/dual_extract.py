#!/usr/bin/env python3
"""Extract every dual-form token from Leeds QAC morphology and build indices."""
import re, json, collections, os, csv

MORPH = "/Users/grey/Downloads/quran/data/morphology/quranic-corpus-morphology-0.4.txt"
QURAN = "/Users/grey/Downloads/quran/quran-text/quran-no-tashkeel.json"
OUT_DIR = "/Users/grey/Downloads/quran/findings/phase-b-hypotheses"
CSV_DIR = os.path.join(OUT_DIR, "csv")
os.makedirs(CSV_DIR, exist_ok=True)

# Buckwalter -> Arabic unicode
BW2AR = {
    "'": "\u0621", "|": "\u0622", ">": "\u0623", "&": "\u0624", "<": "\u0625",
    "}": "\u0626", "A": "\u0627", "b": "\u0628", "p": "\u0629", "t": "\u062A",
    "v": "\u062B", "j": "\u062C", "H": "\u062D", "x": "\u062E", "d": "\u062F",
    "*": "\u0630", "r": "\u0631", "z": "\u0632", "s": "\u0633", "$": "\u0634",
    "S": "\u0635", "D": "\u0636", "T": "\u0637", "Z": "\u0638", "E": "\u0639",
    "g": "\u063A", "_": "\u0640", "f": "\u0641", "q": "\u0642", "k": "\u0643",
    "l": "\u0644", "m": "\u0645", "n": "\u0646", "h": "\u0647", "w": "\u0648",
    "Y": "\u0649", "y": "\u064A",
    "F": "\u064B", "N": "\u064C", "K": "\u064D", "a": "\u064E", "u": "\u064F",
    "i": "\u0650", "~": "\u0651", "o": "\u0652", "`": "\u0670", "{": "\u0671",
    "^": "\u0653",
}
def bw2ar(s):
    return "".join(BW2AR.get(c, c) for c in s)

LOC_RE = re.compile(r"\((\d+):(\d+):(\d+):(\d+)\)")
STEM_DUAL = re.compile(r"\|(?:2D|3D|2MD|2FD|3MD|3FD|MD|FD)(?:\||$)")
PRON_DUAL = re.compile(r"PRON:(?:2D|3D|2MD|2FD|3MD|3FD)")

# Load morphology segments
segments = []  # list of dicts
tokens = collections.defaultdict(list)  # (s,v,w) -> list of seg dicts
with open(MORPH, encoding="utf-8") as f:
    for line in f:
        if not line.startswith("("): continue
        parts = line.rstrip("\n").split("\t")
        if len(parts) < 4: continue
        loc, form, tag, feat = parts
        m = LOC_RE.match(loc)
        if not m: continue
        s, v, w, seg = map(int, m.groups())
        d = {"s": s, "v": v, "w": w, "seg": seg, "form": form, "tag": tag, "feat": feat}
        segments.append(d)
        tokens[(s, v, w)].append(d)

# Dual token records (one per distinct word)
records = []
for (s, v, w), segs in sorted(tokens.items()):
    stem_seg = None
    pron_dual = False
    stem_dual = False
    for seg in segs:
        if "STEM" in seg["feat"] and STEM_DUAL.search(seg["feat"]):
            stem_seg = seg
            stem_dual = True
        if PRON_DUAL.search(seg["feat"]):
            pron_dual = True
    if not (stem_dual or pron_dual): continue
    ref_seg = stem_seg or segs[0]
    lem = re.search(r"LEM:([^|]+)", ref_seg["feat"])
    root = re.search(r"ROOT:([^|]+)", ref_seg["feat"])
    pos = re.search(r"POS:([^|]+)", ref_seg["feat"])
    marker = ""
    if stem_seg:
        mm = STEM_DUAL.search(stem_seg["feat"])
        marker = mm.group(0).strip("|") if mm else ""
    full = "".join(seg["form"] for seg in segs)
    records.append({
        "s": s, "v": v, "w": w,
        "form_bw": full, "form_ar": bw2ar(full),
        "pos": pos.group(1) if pos else ref_seg["tag"],
        "lem": lem.group(1) if lem else "",
        "root": root.group(1) if root else "",
        "marker": marker,
        "stem_dual": stem_dual,
        "pron_suffix_dual": pron_dual,
        "is_verb": ref_seg["tag"] == "V",
        "is_impf": "IMPF" in ref_seg["feat"],
        "mood": (re.search(r"MOOD:(\w+)", ref_seg["feat"]) or [None,None])[1] if stem_seg else None,
    })

print(f"Total dual tokens: {len(records)}")
print(f"Stem-dual: {sum(1 for r in records if r['stem_dual'])}")
print(f"Pron-suffix-dual: {sum(1 for r in records if r['pron_suffix_dual'])}")

# Surah totals
total_tokens_per_surah = collections.Counter()
verse_set = collections.defaultdict(set)
for (s, v, w) in tokens.keys():
    total_tokens_per_surah[s] += 1
    verse_set[s].add(v)
verse_counts = {s: len(vs) for s, vs in verse_set.items()}

surah_counts = collections.Counter(r["s"] for r in records)
surah_stem = collections.Counter(r["s"] for r in records if r["stem_dual"])
surah_pron = collections.Counter(r["s"] for r in records if r["pron_suffix_dual"])

# Per-surah density CSV
with open(os.path.join(CSV_DIR, "dual-density-per-surah.csv"), "w", newline="", encoding="utf-8") as f:
    w = csv.writer(f)
    w.writerow(["surah","verses","words","dual_tokens","stem_dual","pron_suffix_dual","duals_per_100_words","duals_per_verse"])
    for s in sorted(total_tokens_per_surah):
        tw, vc = total_tokens_per_surah[s], verse_counts[s]
        dt = surah_counts[s]
        w.writerow([s, vc, tw, dt, surah_stem[s], surah_pron[s],
                    round(100.0*dt/tw, 3) if tw else 0,
                    round(dt/vc, 3) if vc else 0])

# Dual tokens CSV
with open(os.path.join(CSV_DIR, "dual-tokens.csv"), "w", newline="", encoding="utf-8") as f:
    w = csv.writer(f)
    w.writerow(["surah","verse","word","form_bw","form_ar","pos","root","lemma","marker","stem_dual","pron_suffix_dual","is_verb","is_impf","mood"])
    for r in records:
        w.writerow([r["s"], r["v"], r["w"], r["form_bw"], r["form_ar"], r["pos"],
                    r["root"], r["lem"], r["marker"], int(r["stem_dual"]),
                    int(r["pron_suffix_dual"]), int(r["is_verb"]), int(r["is_impf"]), r["mood"] or ""])

# Verse index
verse_index = collections.defaultdict(lambda: collections.defaultdict(list))
for r in records:
    verse_index[r["s"]][r["v"]].append(r)
with open(os.path.join(CSV_DIR, "dual-verse-index.json"), "w", encoding="utf-8") as f:
    json.dump({f"{s}:{v}":[{k:x[k] for k in ("form_ar","pos","root","lem","marker","pron_suffix_dual")} for x in rlist]
               for s, vs in verse_index.items() for v, rlist in vs.items()}, f, ensure_ascii=False)

# Root frequencies
root_counts = collections.Counter()
for r in records:
    if r["stem_dual"] and r["root"]:
        root_counts[r["root"]] += 1
with open(os.path.join(CSV_DIR, "dual-root-frequencies.csv"), "w", newline="", encoding="utf-8") as f:
    w = csv.writer(f)
    w.writerow(["root","count"])
    for root, c in root_counts.most_common():
        w.writerow([root, c])

# ============== CLASSIC DUAL INVENTORY ==============
# Stem-dual records, grouped by (root, lemma)
lemma_counts = collections.Counter()
lemma_locs = collections.defaultdict(list)
for r in records:
    if r["stem_dual"]:
        lemma_counts[(r["root"], r["lem"])] += 1
        lemma_locs[(r["root"], r["lem"])].append((r["s"], r["v"]))

# Named classic duals (by lemma or form)
def lemma_like(pattern):
    out = []
    for (root, lem), c in lemma_counts.items():
        if re.search(pattern, lem):
            out.append(((root, lem), c, lemma_locs[(root, lem)]))
    return out

# yadā (two hands) — root ydy, lem yad + FD/MD dual
yadan = [r for r in records if r["root"] == "ydy" and r["stem_dual"]]
# jannatān — root jnn, lem: jan~ap (garden) with FD
jannatan = [r for r in records if r["root"] == "jnn" and r["stem_dual"]]
# walidān — root wld
walidan = [r for r in records if r["root"] == "wld" and r["stem_dual"]]
# ʿaynān — root Eyn
aynan = [r for r in records if r["root"] == "Eyn" and r["stem_dual"]]
# bahrān — root bHr
bahran = [r for r in records if r["root"] == "bHr" and r["stem_dual"]]
# mashriqān/maghribān — roots $rq, grb
mashriqan = [r for r in records if r["root"] == "$rq" and r["stem_dual"]]
maghriban = [r for r in records if r["root"] == "grb" and r["stem_dual"]]
# rabbukumā enclitic is pron-suffix-dual, not stem. Handled below separately.
# ithnān/ithnayn — root vny
ithnan = [r for r in records if r["root"] == "vny" and r["stem_dual"]]
# zawjān — root zwj
zawjan = [r for r in records if r["root"] == "zwj" and r["stem_dual"]]
# 'azabān — al-thaqalān
thaqalan = [r for r in records if r["root"] == "vql" and r["stem_dual"]]
# rajulān — root rjl
rajulan = [r for r in records if r["root"] == "rjl" and r["stem_dual"]]
# anthayān  (two females), dhakarān (two males) — root AnV, *kr
anthayan = [r for r in records if r["root"] == "Anv" and r["stem_dual"]]
dhakaran = [r for r in records if r["root"] == "*kr" and r["stem_dual"]]
# malakān — root mlk
malakan = [r for r in records if r["root"] == "mlk" and r["stem_dual"]]
# ʿabdān/rabbān — root rbb dual
rabban = [r for r in records if r["root"] == "rbb" and r["stem_dual"]]

classic = {
    "yadā / kaffā (two hands)": yadan,
    "jannatān (two gardens)": jannatan,
    "wālidān (two parents)": walidan,
    "ʿaynān (two springs/eyes)": aynan,
    "baḥrān (two seas)": bahran,
    "mashriqān (two easts)": mashriqan,
    "maghribān (two wests)": maghriban,
    "ithnān (two)": ithnan,
    "zawjān (two pairs)": zawjan,
    "thaqalān (two weights)": thaqalan,
    "rajulān (two men)": rajulan,
    "untha-dual (two females)": anthayan,
    "dhakarān (two males)": dhakaran,
    "malakān (two angels)": malakan,
    "rabbān (two lords)": rabban,
}

# Print classic dual counts with locations
print("\n== Classic dual catalogue ==")
classic_out = {}
for name, lst in classic.items():
    if not lst: continue
    locs = [(x["s"], x["v"], x["form_ar"], x["lem"]) for x in lst]
    print(f"  {name}: {len(lst)} — e.g. { locs[:3] }")
    classic_out[name] = {"count": len(lst), "locations": [{"s":s,"v":v,"form":f,"lem":l} for s,v,f,l in locs]}

# ============== PROPHET PAIRS ==============
# Find verses containing both names (by lemma)
pn_lem_by_verse = collections.defaultdict(set)
for seg in segments:
    if seg["tag"] == "PN":
        m = re.search(r"LEM:([^|]+)", seg["feat"])
        if m:
            pn_lem_by_verse[(seg["s"], seg["v"])].add(m.group(1))

pairs_defs = {
    "Moses/Aaron": ("muwsaY`", "ha`ruwn"),
    "Zachariah/John": ("zakariy~aA", "yaHoyaY`"),
    "Abraham/Ishmael": ("<iboraAhiym", "<isomaAEiyl"),
    "Adam/Eve": ("A^dam", None),   # Eve unnamed in Quran — only dual references
    "Yajuj/Majuj": ("ya>ojuwj", "ma>ojuwj"),
}
pair_results = {}
for name, (a, b) in pairs_defs.items():
    matches = []
    if b:
        for (s,v), lems in pn_lem_by_verse.items():
            if a in lems and b in lems:
                matches.append((s,v))
    else:
        # Adam: find verses mentioning Adam + "zawj" (wife) with dual address
        for (s,v), lems in pn_lem_by_verse.items():
            if a in lems:
                matches.append((s,v))
    # For each matching verse, check dual token presence & type
    detail = []
    for (s,v) in sorted(matches):
        drecs = verse_index[s][v]
        verb_dual = [x for x in drecs if x["is_verb"] and x["stem_dual"]]
        pron_dual = [x for x in drecs if x["pron_suffix_dual"]]
        noun_dual = [x for x in drecs if x["stem_dual"] and not x["is_verb"]]
        detail.append({
            "s": s, "v": v,
            "n_dual_tokens": len(drecs),
            "n_verb_dual": len(verb_dual),
            "n_noun_dual": len(noun_dual),
            "n_pron_dual": len(pron_dual),
            "verb_lems": [x["lem"] for x in verb_dual],
        })
    pair_results[name] = detail
    print(f"\n  {name}: {len(matches)} co-occurrence verses")
    for d in detail[:10]:
        print(f"    {d['s']}:{d['v']}  verbs_dual={d['n_verb_dual']} nouns_dual={d['n_noun_dual']} pron_dual={d['n_pron_dual']}  lems={d['verb_lems']}")

# ============== AR-RAHMAN DUAL ADDRESS MAP ==============
rahman = [r for r in records if r["s"] == 55]
rahman_by_verse = collections.defaultdict(list)
for r in rahman:
    rahman_by_verse[r["v"]].append(r)
print(f"\n== Ar-Rahman ==")
print(f"Total dual tokens: {len(rahman)}")
print(f"Verses containing dual: {len(rahman_by_verse)}")
# Kinds
rahman_kinds = collections.Counter(r["marker"] for r in rahman if r["stem_dual"])
print(f"Stem dual markers: {rahman_kinds}")
rahman_2nd = sum(1 for r in rahman if "2" in r["marker"] or (r["pron_suffix_dual"] and "kumaA" in r["form_bw"]))
print(f"Tokens with 2nd-person-dual shape: {rahman_2nd}")
# Refrain (root k*b 2D): count
refrain_count = sum(1 for r in rahman if r["root"] == "k*b" and "2D" in r["marker"])
print(f"tukadhdhibān count (refrain root k*b 2D): {refrain_count}")

# ============== -bAn / indicative dual impf per surah ==============
impf_dual_ind = []
for r in records:
    if r["is_verb"] and r["is_impf"] and r["stem_dual"] and r["mood"] in (None, ""):
        impf_dual_ind.append(r)
ind_per_surah = collections.Counter(r["s"] for r in impf_dual_ind)
print(f"\n== Indicative (non-SUBJ/JUS) dual imperfect verbs: {len(impf_dual_ind)} ==")
for s, c in ind_per_surah.most_common():
    print(f"  Surah {s}: {c}")

# ============== CONJOINED VS DUAL: heavens-and-earth etc. ==============
# Count pairings of roots (smw + ArD) in same verse (as plural+singular conjunctions)
# smw = samawat (plural fem), ArD = earth (sg fem)
# Token-root presence per verse
root_by_verse = collections.defaultdict(set)
for seg in segments:
    m = re.search(r"ROOT:([^|]+)", seg["feat"])
    if m:
        root_by_verse[(seg["s"], seg["v"])].add(m.group(1))

def count_pair(r1, r2):
    return sum(1 for (s,v), roots in root_by_verse.items() if r1 in roots and r2 in roots)

# Classic pairings
pair_counts = {
    "smw+ArD (heavens+earth)": count_pair("smw", "ArD"),
    "$ms+qmr (sun+moon)": count_pair("$ms", "qmr"),
    "Ans+jnn (humans+jinn)": count_pair("Ans", "jnn"),
    "*kr+Anv (male+female)": count_pair("*kr", "Anv"),
    "Hyy+mwt (life+death)": count_pair("Hyy", "mwt"),
    "lyl+nhr (night+day)": count_pair("lyl", "nhr"),
    "$rq+grb (east+west)": count_pair("$rq", "grb"),
}
print(f"\n== Paired-opposites co-occurrences ==")
for k, v in pair_counts.items():
    print(f"  {k}: {v} verses")

# Now: for each pair, count whether a DUAL token appears in the same verse
def dual_in_same_verse(r1, r2):
    matches = 0
    duals = 0
    for (s,v), roots in root_by_verse.items():
        if r1 in roots and r2 in roots:
            matches += 1
            if any(x["stem_dual"] or x["pron_suffix_dual"] for x in verse_index[s][v]):
                duals += 1
    return matches, duals
paired_opposites_dual = {}
for name, (r1, r2) in [
    ("heavens+earth", ("smw","ArD")),
    ("sun+moon", ("$ms","qmr")),
    ("humans+jinn", ("Ans","jnn")),
    ("male+female", ("*kr","Anv")),
    ("life+death", ("Hyy","mwt")),
    ("night+day", ("lyl","nhr")),
    ("east+west", ("$rq","grb")),
]:
    m, d = dual_in_same_verse(r1, r2)
    paired_opposites_dual[name] = {"verses": m, "with_dual_token": d, "share": round(d/m,3) if m else 0}
    print(f"  {name}: {m} verses, {d} have dual token ({round(100*d/m,1) if m else 0}%)")

# Are same-verse pairs grammatically dual, or conjoined?
# The pair is "conjoined" if both roots appear as stems but are NOT themselves marked as dual.
# Count verses where the specific root appears in DUAL form
def root_as_dual(root_name):
    return sum(1 for r in records if r["root"] == root_name and r["stem_dual"])
root_dual_counts = {
    "smw (heaven/sky)": root_as_dual("smw"),
    "ArD (earth)": root_as_dual("ArD"),
    "$ms (sun)": root_as_dual("$ms"),
    "qmr (moon)": root_as_dual("qmr"),
    "Ans (humankind)": root_as_dual("Ans"),
    "jnn (jinn)": root_as_dual("jnn"),
    "*kr (male)": root_as_dual("*kr"),
    "Anv (female)": root_as_dual("Anv"),
    "Hyy (life)": root_as_dual("Hyy"),
    "mwt (death)": root_as_dual("mwt"),
    "lyl (night)": root_as_dual("lyl"),
    "nhr (day)": root_as_dual("nhr"),
    "$rq (east)": root_as_dual("$rq"),
    "grb (west)": root_as_dual("grb"),
    "bHr (sea)": root_as_dual("bHr"),
    "jnn (garden)": sum(1 for r in records if r["root"]=="jnn" and r["stem_dual"] and r["lem"].startswith("jan")),
}
print(f"\n== Root in dual form ==")
for k, v in root_dual_counts.items():
    print(f"  {k}: {v} dual tokens")

# ============== SINGLETON LEMMAS — dual forms appearing in only one surah ==============
lem_surah = collections.defaultdict(set)
for r in records:
    if r["stem_dual"] and r["lem"]:
        lem_surah[r["lem"]].add(r["s"])
singletons = [(lem, list(surs)[0]) for lem, surs in lem_surah.items() if len(surs) == 1]
print(f"\n== Lemmas with dual form in only ONE surah: {len(singletons)} ==")
# Break them down by surah
singleton_per_surah = collections.Counter(s for lem, s in singletons)
for s, c in singleton_per_surah.most_common(10):
    lem_list = [lem for lem, ss in singletons if ss == s]
    print(f"  Surah {s}: {c} unique-dual lemmas: {lem_list[:6]}")

# ============== Dual lemmas by semantic class ==============
# POS breakdown
pos_counts = collections.Counter(r["pos"] for r in records if r["stem_dual"])
print(f"\n== POS of stem duals ==")
for p, c in pos_counts.most_common():
    print(f"  {p}: {c}")

# ============== Save aggregate JSON ==============
agg = {
    "total_dual_tokens": len(records),
    "total_stem_dual": sum(1 for r in records if r["stem_dual"]),
    "total_pron_suffix_dual": sum(1 for r in records if r["pron_suffix_dual"]),
    "surah_count_table": [
        {"surah": s, "verses": verse_counts[s], "words": total_tokens_per_surah[s],
         "dual": surah_counts[s], "stem": surah_stem[s], "pron": surah_pron[s],
         "per_100_words": round(100*surah_counts[s]/total_tokens_per_surah[s],3) if total_tokens_per_surah[s] else 0}
        for s in sorted(surah_counts, key=lambda x: -surah_counts[x])
    ],
    "classic_duals": classic_out,
    "prophet_pairs": pair_results,
    "paired_opposites_dual_overlap": paired_opposites_dual,
    "root_as_dual": root_dual_counts,
    "singleton_lemma_count": len(singletons),
    "singleton_by_surah": dict(singleton_per_surah.most_common()),
    "ind_impf_dual_per_surah": dict(ind_per_surah.most_common()),
    "pos_of_stem_duals": dict(pos_counts),
    "rahman_summary": {
        "total_duals": len(rahman),
        "verses_with_dual": len(rahman_by_verse),
        "refrain_tukadhdhiban_count": refrain_count,
        "kinds": dict(rahman_kinds),
    },
}
with open(os.path.join(CSV_DIR, "dual-aggregates.json"), "w", encoding="utf-8") as f:
    json.dump(agg, f, ensure_ascii=False, indent=2)
print("\nWrote /Users/grey/Downloads/quran/findings/phase-b-hypotheses/csv/dual-aggregates.json")
