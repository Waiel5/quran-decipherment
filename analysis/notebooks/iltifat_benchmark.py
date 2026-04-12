#!/usr/bin/env python3
"""
Benchmark the iltifāt detector against Abdel Haleem's (1992) canonical
list of iltifāt verses, derived from al-Zarkashī's al-Burhān and
al-Suyūṭī's al-Itqān.

Recall = of the gold-truth verses, how many does our detector flag as
having intra-verse iltifāt or as inter-verse transitioning into the
expected direction?

Precision is not directly computable because Abdel Haleem himself says
the canonical list is incomplete and the actual occurrence is much
higher. We report precision against the gold set as an upper bound.
"""
import csv
import os

ROOT = "/Users/grey/Downloads/quran"
PER_VERSE = os.path.join(ROOT, "findings/phase-b-hypotheses/iltifat-per-verse.csv")

# Abdel Haleem's gold-truth lists (from islamic-awareness.org rendition)
GOLD = {
    "3to1": "2:23,47,73,83,118,160,172;3:25,58,168;4:30,33,37,41,64,74,114,174;5:14,15,19,32,70,86;6:22,92,97,98,99,107,110,114,126;7:37,57;8:9,41;10:7,11,21,22,23,28;11:8;13:4;14:13;16:2,40,66,75,84;17:1,21,33,97;18:7;19:9,21,58;20:53,113;21:29,37;22:57,67;24:55;25:17,32,45,48,56;26:198;27:60,81;28:57,61,75;29:4,7,23;30:16,28,34,47,51,58;31:7,10,23;32:12,16,27;33:9,31;34:5,9;35:9,27;36:8,37;37:6;39:2,3,16,27,49;40:5,70,84;41:12,28,39;42:7,13,20,23,35,38,48;45:31;46:7,15;47:13;48:25;49:13;52:21,48;53:29;54:11;55:31;58:5;59:21;61:14;65:8;66:10;67:5,17;68:15,35;69:11;70:7;72:16;76:9;80:25;86:15;87:6;88:25;89:29;92:7;96:15",
    "1to3": "2:5,23,37,161,172;3:57,151;4:30,33,69,122;6:90,95,111,112,127;7:12,58,101,142;8:4;10:22,25;14:46;15:28,96;16:52;17:1;20:4;21:19;22:6;23:14,57,78,91,116;24:35,46;25:31,47,58;26:5,9,213;27:6;28:13,59,62;29:3,40,67,69;30:54,59;31:11,23;32:25;33:9,46,50;34:21;35:31,32,38;36:36,74;37:33;38:26;40:61,85;41:19,28,40,45,53;44:6;45:22,30;48:2;51:58;53:30;54:55;57:27;60:3;65:10;66:12;67:19;68:48;76:6,24,29;87:6;94:8;95:8;97:4;108:2",
    "3to2": "1:5;2:21,25,28,60,83,214,229,233;3:180;4:11;6:6;8:7,14;9:19,69;10:3,68;11:14;16:55,68,74;19:89;21:37;23:15,65;27:90;30:34;31:33;33:55;34:37;35:3;36:59;37:25;38:59;43:16;47:22,30;50:24;52:14,19,39;55:13;56:51,91;57:17,20;67:13;75:34;76:22,30;77:38,43;78:30,36;80:3;87:16",
    "2to3": "2:54,57,85,88,187,200,216,226,229,286;4:9;10:22;16:69,72;24:63;28:16;30:38;31:32;32:10;45:35;47:23;67:18;75:31",
    "1to2": "36:22",
    "number": "2:34,38,40,106,123,217;7:24,127;14:31,37;15:49;16:65;17:36;20:37,40,41,81,124;22:45;23:51,66;27:84;29:8,57;31:15;32:13;34:12,45;35:40;43:32,69;46:5;50:30;54:17,22,32,40;55:31;65:11;68:44;69:44;70:40;73:12;74:16,31;75:3;77:39;90:4;98:8;100:11",
    "addressee": "2:144,148,150;4:109;5:48;6:133;7:3;10:87;12:29;16:2;17:63;27:93;28:35;29:46;31:31;33:4,19,51;39:31;42:13;48:9;58:2;65:1;69:18;73:20",
    "tense": "2:25,125;7:29;11:54;16:11;18:47;22:25,31,63,65;27:87;33:10;35:9;36:33;39:68;40:67",
}


def parse_list(s):
    out = set()
    for chunk in s.split(";"):
        chunk = chunk.strip()
        if not chunk:
            continue
        sn, vs = chunk.split(":")
        sn = int(sn)
        for v in vs.split(","):
            out.add((sn, int(v.strip())))
    return out


gold_sets = {k: parse_list(v) for k, v in GOLD.items()}
gold_person_union = set()
for k in ("3to1", "1to3", "3to2", "2to3", "1to2"):
    gold_person_union |= gold_sets[k]
gold_full_union = set()
for k in gold_sets:
    gold_full_union |= gold_sets[k]

print(f"Gold person-union: {len(gold_person_union)} verses")
print(f"Gold full-union (incl. number/addressee/tense): {len(gold_full_union)} verses")

# Load detector output
detector = {}
with open(PER_VERSE, "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        s = int(row["surah"])
        a = int(row["ayah"])
        detector[(s, a)] = dict(
            primary=row["primary_person"],
            effective=row["effective_primary"],
            person_set=row["person_set"],
            intra_level=int(row["intra_level"]),
            intra_strict=int(row["intra_strict"]),
            inter_shift=int(row["inter_shift"]),
            inter_shift_strict=int(row["inter_shift_strict"]),
            transition=row["inter_transition"],
        )

# Count flagged-as-iltifat verses
detector_any = set(k for k, r in detector.items()
                   if r["intra_level"] >= 1 or r["inter_shift"] == 1)
detector_strict = set(k for k, r in detector.items()
                      if r["intra_strict"] == 1 or r["inter_shift_strict"] == 1)
print(f"\nDetector permissive flagged: {len(detector_any)} verses ({len(detector_any)/6236*100:.1f}%)")
print(f"Detector strict flagged: {len(detector_strict)} verses ({len(detector_strict)/6236*100:.1f}%)")

# Per-category recall
print("\n=== Recall by gold category ===")
for cat, gset in gold_sets.items():
    rec_perm = len(gset & detector_any) / len(gset)
    rec_strict = len(gset & detector_strict) / len(gset)
    print(f"  {cat:10s}  n={len(gset):4d}  recall_perm={rec_perm:.3f}  recall_strict={rec_strict:.3f}")

# Person union recall (the main number)
inter = gold_person_union & detector_any
inter_strict = gold_person_union & detector_strict
print(f"\n=== Person-iltifat (canonical) ===")
print(f"  recall_perm   = {len(inter)/len(gold_person_union):.3f} ({len(inter)}/{len(gold_person_union)})")
print(f"  recall_strict = {len(inter_strict)/len(gold_person_union):.3f} ({len(inter_strict)}/{len(gold_person_union)})")

# Direction-aware check: for the 3→2 gold verses, does our detector report
# either intra has-2&has-3 OR an inter transition involving 2 or 3?
print("\n=== Direction-aware match for 3to2 gold verses ===")
matches = 0
misses_examples = []
for k in gold_sets["3to2"]:
    r = detector.get(k)
    if not r:
        continue
    person_set = r["person_set"]
    has_2_3 = "2" in person_set and "3" in person_set
    inter_2 = r["transition"] and "2" in r["transition"]
    if has_2_3 or inter_2:
        matches += 1
    else:
        misses_examples.append((k, person_set, r["transition"]))
print(f"  matched: {matches}/{len(gold_sets['3to2'])} = {matches/len(gold_sets['3to2']):.3f}")
print(f"  example misses (first 5): {misses_examples[:5]}")

# Direction-aware check for 3to1
print("\n=== Direction-aware match for 3to1 gold verses ===")
matches = 0
misses_examples = []
for k in gold_sets["3to1"]:
    r = detector.get(k)
    if not r:
        continue
    person_set = r["person_set"]
    has_1_3 = "1" in person_set and "3" in person_set
    inter_match = r["transition"] in ("3->1",)
    if has_1_3 or inter_match:
        matches += 1
    else:
        misses_examples.append((k, person_set, r["transition"]))
print(f"  matched: {matches}/{len(gold_sets['3to1'])} = {matches/len(gold_sets['3to1']):.3f}")
print(f"  example misses (first 5): {misses_examples[:5]}")

# Special case: Q 36:22 disputed 1to2
r = detector[(36, 22)]
print(f"\nQ 36:22 disputed 1->2: detector reports {r}")
