#!/usr/bin/env python3
"""
Compression-based surah structure + kalām Allāh self-reference density test.

Task A: gzip_ratio, zlib_ratio, LZ-complexity (Kaspar-Schuster), entropy per surah.
Task B: count self-reference lemmas per verse; Meccan vs Medinan density test.
"""
import json
import gzip
import zlib
import math
import random
import re
import csv
import sys
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path("/Users/grey/Downloads/quran")
CORPUS = ROOT / "quran-text" / "quran-no-tashkeel.json"
REV_ORDER = ROOT / "data" / "revelation-order.csv"
OUT_DIR = ROOT / "findings" / "phase-b-hypotheses"

random.seed(42)

# ---------- Load corpus ----------
with open(CORPUS) as f:
    quran = json.load(f)

# Build (surah_idx, verse_idx, text) tuples
all_verses = []  # list of (s, v, text)
surah_meta = {}  # s -> {name, type, n_verses, text}
for surah in quran:
    sid = surah["id"]
    surah_meta[sid] = {
        "name": surah["transliteration"],
        "type": surah["type"],
        "n_verses": surah["total_verses"],
        "verses": [v["text"] for v in surah["verses"]],
        "text": " ".join(v["text"] for v in surah["verses"]),
    }
    for v in surah["verses"]:
        all_verses.append((sid, v["id"], v["text"]))

# Revelation order → per-surah mushaf type (already have type, but reinforce)
rev_type = {}
with open(REV_ORDER) as f:
    reader = csv.DictReader(f)
    for row in reader:
        rev_type[int(row["mushaf_order"])] = row["period"]  # 'Meccan' / 'Medinan'

# ---------- TASK A: Compression metrics ----------

def gzip_ratio(text):
    b = text.encode("utf-8")
    c = gzip.compress(b, compresslevel=9)
    return len(c) / len(b)

def zlib_ratio(text):
    b = text.encode("utf-8")
    c = zlib.compress(b, level=9)
    return len(c) / len(b)

def lempel_ziv_complexity(s):
    """Kaspar-Schuster LZ complexity: count distinct phrases while parsing left-to-right."""
    i = 0
    c = 1
    n = len(s)
    if n == 0:
        return 0
    k = 1
    l = 1
    while True:
        if i + k > n:
            break
        # find longest match starting at pos l up to l+k-1 within prefix s[:i+k-1]?
        # Classical: try to match s[l..l+k-1] within s[0..i+k-2].
        # Use standard algorithm per Kaspar-Schuster 1987.
        if i + k - 1 >= n:
            break
        sub = s[i:i+k]
        prefix = s[:i+k-1] if i+k-1 > 0 else ""
        if sub in prefix:
            k += 1
            if i + k > n:
                c += 1
                break
        else:
            c += 1
            i = i + k
            k = 1
            if i >= n:
                break
    return c

def lz76(s):
    """Standard LZ76 complexity (Lempel-Ziv 1976). Cleaner implementation."""
    n = len(s)
    if n == 0:
        return 0
    i, k, l = 0, 1, 1
    c = 1
    k_max = 1
    stop = False
    while not stop:
        if s[i + k - 1] != s[l + k - 1]:
            if k > k_max:
                k_max = k
            i += 1
            if i == l:
                c += 1
                l += k_max
                if l + 1 > n:
                    stop = True
                else:
                    i = 0
                    k = 1
                    k_max = 1
            else:
                k = 1
        else:
            k += 1
            if l + k > n:
                c += 1
                stop = True
    return c

def entropy_bits_per_char(text):
    if not text:
        return 0.0
    counts = Counter(text)
    total = sum(counts.values())
    h = 0.0
    for v in counts.values():
        p = v / total
        h -= p * math.log2(p)
    return h

# Compute per-surah metrics
print("Computing Task A: compression metrics per surah...", file=sys.stderr)
surah_metrics = []
for sid in range(1, 115):
    text = surah_meta[sid]["text"]
    # Normalize whitespace
    text_n = re.sub(r"\s+", " ", text).strip()
    n_chars = len(text_n)
    n_verses = surah_meta[sid]["n_verses"]
    # LZ76 operates on char sequence
    lzc = lz76(text_n)
    # normalized LZ: c * log2(n) / n  (Lempel-Ziv 1976 normalization)
    lz_norm = (lzc * math.log2(max(n_chars, 2))) / max(n_chars, 1)
    surah_metrics.append({
        "surah": sid,
        "name": surah_meta[sid]["name"],
        "type": surah_meta[sid]["type"],
        "n_verses": n_verses,
        "n_chars": n_chars,
        "gzip_ratio": gzip_ratio(text_n),
        "zlib_ratio": zlib_ratio(text_n),
        "lz_complexity": lzc,
        "lz_normalized": lz_norm,
        "entropy_bpc": entropy_bits_per_char(text_n),
    })

# ---------- Null model: length-matched verse-shuffle ----------
# Permutation: for each surah, draw verses randomly (without replacement from the pool)
# matching the same n_verses count. Recompute gzip_ratio and entropy.

print("Running null: 1000 length-matched verse-shuffle permutations...", file=sys.stderr)
verse_pool = [v[2] for v in all_verses]  # all verse texts
surah_verse_counts = {sid: surah_meta[sid]["n_verses"] for sid in range(1, 115)}

# Observed gzip ratios
obs_gzip = {m["surah"]: m["gzip_ratio"] for m in surah_metrics}

# For each permutation, produce a random assignment of verses to surahs preserving sizes
NPERM = 1000
null_gzip_for_surah = defaultdict(list)  # surah -> list of gzip ratios under null

for perm in range(NPERM):
    shuffled = verse_pool[:]
    random.shuffle(shuffled)
    idx = 0
    for sid in range(1, 115):
        k = surah_verse_counts[sid]
        block = shuffled[idx:idx+k]
        idx += k
        block_text = re.sub(r"\s+", " ", " ".join(block)).strip()
        null_gzip_for_surah[sid].append(gzip_ratio(block_text))

# Compute z-scores: (obs - mean_null) / std_null
for m in surah_metrics:
    sid = m["surah"]
    arr = null_gzip_for_surah[sid]
    mu = sum(arr) / len(arr)
    var = sum((x - mu) ** 2 for x in arr) / len(arr)
    sd = math.sqrt(var) if var > 0 else 1e-9
    m["gzip_null_mean"] = mu
    m["gzip_null_std"] = sd
    m["gzip_z"] = (m["gzip_ratio"] - mu) / sd
    # empirical two-tailed p
    rank_low = sum(1 for x in arr if x <= m["gzip_ratio"])
    rank_high = sum(1 for x in arr if x >= m["gzip_ratio"])
    m["gzip_emp_p_twotail"] = 2 * min(rank_low, rank_high) / len(arr)

# Save full table
import json as _json
out_csv = OUT_DIR / "csv" / "compression_per_surah.csv"
out_csv.parent.mkdir(parents=True, exist_ok=True)
with open(out_csv, "w", newline="") as f:
    fieldnames = ["surah", "name", "type", "n_verses", "n_chars",
                  "gzip_ratio", "zlib_ratio", "lz_complexity", "lz_normalized",
                  "entropy_bpc", "gzip_null_mean", "gzip_null_std", "gzip_z",
                  "gzip_emp_p_twotail"]
    w = csv.DictWriter(f, fieldnames=fieldnames)
    w.writeheader()
    for m in surah_metrics:
        w.writerow({k: m[k] for k in fieldnames})

# ---------- TASK B: Self-reference density ----------
# Use Arabic surface-form matching on no-tashkeel text, multi-pattern per lemma
# (since no-tashkeel text drops diacritics we can use stripped forms).

# Self-reference target patterns. Each entry: lemma_name -> list of (regex, description)
# Patterns operate on no-tashkeel text. They must anchor whole-word.

# Build Arabic word-boundary regex: \b doesn't work well in Arabic; use (?:^|[^\u0600-\u06FF])
# and ?=(?:$|[^\u0600-\u06FF]) — but simpler: tokenize by whitespace and check membership.

# Strategy: tokenize each verse into whitespace-words; strip punctuation; match exact forms.

PUNCT = re.compile(r"[^\u0600-\u06FF\s]")

def tokenize(text):
    t = PUNCT.sub(" ", text)
    t = re.sub(r"\s+", " ", t).strip()
    return t.split()

# Self-reference surface-form catalog (no-tashkeel normalized)
# All forms are no-tashkeel (no ّ ً ٌ ٍ َ ُ ِ ْ ٰ).
# The source text `quran-no-tashkeel.json` preserves alif variants (ا أ إ آ)
# and ta marbuta ة; we build variants that cover definite/indefinite/case.
SELF_REF_FORMS = {
    # qur'an + al-qur'an + qur'ana (no-tashkeel: قرآن, القرآن)
    "qur'an": [
        "قرآن", "القرآن", "قرآنا", "قرآنٌ", "قرآنًا",  # accusative indef bare appears in text as قرآن
        "قرءان", "القرءان", "قرءانا",  # alternative orthography present in Uthmani rasm; rare
    ],
    # kitāb (the Book) — huge raw count but not all refer to Quran. We count occurrences
    # of the surface form and disambiguate separately.
    "kitab": [
        "كتاب", "الكتاب", "كتابا", "كتابٌ", "كتابًا", "الكتب", "كتب",
        "كتابه", "كتابك", "كتابكم", "كتابهم", "كتابي", "كتابنا", "بكتاب", "بالكتاب",
        "للكتاب", "وكتاب", "والكتاب", "فالكتاب",
    ],
    # furqān
    "furqan": [
        "فرقان", "الفرقان", "بالفرقان", "والفرقان",
    ],
    # dhikr / al-dhikr (reminder) — disambiguate male-progeny sense separately
    "dhikr": [
        "ذكر", "الذكر", "ذكرى", "الذكرى", "ذكرا", "بالذكر", "للذكر", "والذكر",
        "بذكر", "وذكر", "وذكرى", "وذكرا", "فذكر",
    ],
    # tanzīl (the Sent-down) — Form II masdar
    "tanzil": [
        "تنزيل", "التنزيل", "تنزيلا", "بتنزيل", "وتنزيل",
    ],
    # waḥy (inspiration / revelation) — noun forms only
    "wahy": [
        "وحي", "الوحي", "وحيا", "بالوحي", "ووحي",
    ],
    # āyāt / āyah (signs/verses)
    "ayat": [
        "آية", "آيات", "الآية", "الآيات", "آياتنا", "آياته", "آياتي", "آياتك",
        "آياتهم", "آيتنا", "ءاية", "ءايات", "الءاية", "الءايات", "ءاياته", "ءاياتنا",
        "بآياتنا", "بآياته", "وآياته", "وآياتنا", "فآياتنا", "فآياته",
        "بآيات", "وآيات", "لآيات", "لآية",
    ],
    # kalām (speech) — as noun only
    "kalam": [
        "كلام", "الكلام", "كلاما", "كلامي", "كلامه", "كلمات", "الكلمات",
        "بكلام", "وكلام", "كلمة", "الكلمة", "بكلمة",
    ],
    # mathānī (paired repetitions) — only 2 occurrences in Quran (15:87, 39:23)
    "mathani": [
        "مثاني", "المثاني",
    ],
    # nūr (light) — disambiguate later
    "nur": [
        "نور", "النور", "نورا", "نوره", "نوركم", "بنور", "بنوره", "ونور", "ونوره",
        "لنور", "الأنوار",
    ],
}

# Flatten to set for fast lookup, remembering which lemma
form_to_lemma = {}
for lemma, forms in SELF_REF_FORMS.items():
    for f in forms:
        form_to_lemma.setdefault(f, []).append(lemma)

# Disambiguation rules (al-Rāghib–informed).
# For this computational pass, we implement pragmatic whole-verse disambiguation:
#   - kitab: when in same verse as Torah/Gospel/Musa/Isa/banu isra'il → "prior-scripture" sense
#   - dhikr: when in a verse containing dhukur (male/masculine, root ذكر with plural ذكور)
#            or context of gender (anthā) → male sense; when "ahl al-dhikr" → prior scripture
#   - nur: count only when appears in a "revelation" frame (paired with anzalnā / kitāb /
#          rasul) within the same verse — otherwise cosmic light (sun/moon).
#   - kalam: count only when attributed to Allāh (kalām allāh, kalimāt rabb/ allāh)
#   - wahy/tanzil/ayat/furqan/mathani/qur'an: whole-verse overwhelmingly about revelation;
#          accept all.

CONTEXT = {
    "prior_scripture_markers": {
        "التوراة", "الإنجيل", "الانجيل", "موسى", "عيسى",
        "داود", "داوود", "زكريا", "يحيى", "إبراهيم", "ابراهيم",
        "هارون", "يعقوب", "إسحاق", "اسحاق", "إسرائيل", "اسرائيل",
        "بني", "صحف", "الزبور", "اليهود", "النصارى", "الذين", "هودا",
    },
    "male_progeny_markers": {
        "ذكرا", "ذكور", "الذكر", "والأنثى", "أنثى", "الأنثى", "وأنثى", "الأنثيين",
    },
    "revelation_frame_markers": {
        "أنزل", "أنزلنا", "نزل", "نزلنا", "أوحى", "أوحينا", "الكتاب",
        "كتاب", "رسول", "الرسول", "النبي", "نبي", "القرآن", "قرآن",
        "المبين", "مبين", "التنزيل", "تنزيل",
    },
    "allah_kalam_markers": {
        "الله", "اللّه", "ربك", "ربه", "ربهم", "الرحمن", "رب",
    },
}

def classify_kitab(verse_text, tokens):
    tset = set(tokens)
    if tset & CONTEXT["prior_scripture_markers"]:
        return "prior-scripture-or-mixed"
    return "quran"

def classify_dhikr(verse_text, tokens, lemma_form):
    tset = set(tokens)
    if "أهل" in tset and "الذكر" in tset:
        return "prior-scripture"
    if tset & CONTEXT["male_progeny_markers"]:
        return "male-vs-female"
    return "quran"

def classify_nur(verse_text, tokens):
    tset = set(tokens)
    if tset & CONTEXT["revelation_frame_markers"]:
        return "quran"
    return "cosmic-light"

def classify_kalam(verse_text, tokens):
    tset = set(tokens)
    if tset & CONTEXT["allah_kalam_markers"]:
        return "quran"
    return "general-speech"

# Count per-verse occurrences
lemma_counts_per_verse = defaultdict(lambda: defaultdict(int))  # (s,v) -> lemma -> count
lemma_verses = defaultdict(set)   # lemma -> set of (s,v)
per_verse_any = set()  # (s,v) with >=1 self-ref

for (s, v, text) in all_verses:
    tokens = tokenize(text)
    for tok in tokens:
        if tok in form_to_lemma:
            for lemma in form_to_lemma[tok]:
                # Apply disambiguation
                if lemma == "kitab":
                    cls = classify_kitab(text, tokens)
                    if cls != "quran":
                        continue
                elif lemma == "dhikr":
                    cls = classify_dhikr(text, tokens, tok)
                    if cls != "quran":
                        continue
                elif lemma == "nur":
                    cls = classify_nur(text, tokens)
                    if cls != "quran":
                        continue
                elif lemma == "kalam":
                    cls = classify_kalam(text, tokens)
                    if cls != "quran":
                        continue
                lemma_counts_per_verse[(s, v)][lemma] += 1
                lemma_verses[lemma].add((s, v))
                per_verse_any.add((s, v))

# Phase density (Meccan vs Medinan at surah level)
meccan_surahs = [sid for sid in range(1, 115) if surah_meta[sid]["type"] == "meccan"]
medinan_surahs = [sid for sid in range(1, 115) if surah_meta[sid]["type"] == "medinan"]

def phase_stats(surah_list):
    total_verses = sum(surah_meta[s]["n_verses"] for s in surah_list)
    total_tokens = sum(
        lemma_counts_per_verse[(s, v)][l]
        for s in surah_list
        for v in range(1, surah_meta[s]["n_verses"] + 1)
        for l in SELF_REF_FORMS
    )
    verses_with_any = sum(
        1 for s in surah_list
        for v in range(1, surah_meta[s]["n_verses"] + 1)
        if (s, v) in per_verse_any
    )
    return {
        "n_surahs": len(surah_list),
        "n_verses": total_verses,
        "total_self_ref_tokens": total_tokens,
        "verses_with_any": verses_with_any,
        "tokens_per_verse": total_tokens / total_verses,
        "frac_verses_with_any": verses_with_any / total_verses,
    }

meccan_stats = phase_stats(meccan_surahs)
medinan_stats = phase_stats(medinan_surahs)
print("Meccan:", meccan_stats, file=sys.stderr)
print("Medinan:", medinan_stats, file=sys.stderr)

# Null: randomize surah labels (Meccan/Medinan) 1000 times
# Keep the same number of surahs in each class.
obs_diff = meccan_stats["tokens_per_verse"] - medinan_stats["tokens_per_verse"]

labels = ["meccan"] * len(meccan_surahs) + ["medinan"] * len(medinan_surahs)
# Precompute per-surah (n_verses, n_tokens)
surah_stats = {}
for sid in range(1, 115):
    ntok = sum(
        lemma_counts_per_verse[(sid, v)][l]
        for v in range(1, surah_meta[sid]["n_verses"] + 1)
        for l in SELF_REF_FORMS
    )
    surah_stats[sid] = (surah_meta[sid]["n_verses"], ntok)

all_surahs = list(range(1, 115))
null_diffs = []
for _ in range(1000):
    shuffled = all_surahs[:]
    random.shuffle(shuffled)
    mec_ids = shuffled[:len(meccan_surahs)]
    med_ids = shuffled[len(meccan_surahs):]
    mec_v = sum(surah_stats[s][0] for s in mec_ids)
    mec_t = sum(surah_stats[s][1] for s in mec_ids)
    med_v = sum(surah_stats[s][0] for s in med_ids)
    med_t = sum(surah_stats[s][1] for s in med_ids)
    null_diffs.append((mec_t / mec_v) - (med_t / med_v))

rank_ge = sum(1 for d in null_diffs if d >= obs_diff)
rank_le = sum(1 for d in null_diffs if d <= obs_diff)
emp_p_twotail = 2 * min(rank_ge, rank_le) / len(null_diffs)
null_mean = sum(null_diffs) / len(null_diffs)
null_sd = math.sqrt(sum((x-null_mean)**2 for x in null_diffs)/len(null_diffs))
z_obs = (obs_diff - null_mean) / null_sd if null_sd > 0 else 0

# Lemma-by-lemma totals
lemma_totals = {}
for lemma in SELF_REF_FORMS:
    total = sum(lemma_counts_per_verse[(s, v)][lemma]
                for (s, v, _) in all_verses)
    meccan_n = sum(lemma_counts_per_verse[(s, v)][lemma]
                   for s in meccan_surahs
                   for v in range(1, surah_meta[s]["n_verses"] + 1))
    medinan_n = sum(lemma_counts_per_verse[(s, v)][lemma]
                    for s in medinan_surahs
                    for v in range(1, surah_meta[s]["n_verses"] + 1))
    lemma_totals[lemma] = {
        "total_tokens": total,
        "total_verses": len(lemma_verses[lemma]),
        "meccan_tokens": meccan_n,
        "medinan_tokens": medinan_n,
        "meccan_per_verse": meccan_n / meccan_stats["n_verses"],
        "medinan_per_verse": medinan_n / medinan_stats["n_verses"],
    }

# Meta-verses (explicit self-description) — canonical set
META_VERSES = [
    (2, 2), (2, 23), (2, 185), (3, 3), (4, 82), (5, 15), (6, 19), (6, 92),
    (10, 1), (10, 37), (10, 38), (11, 13), (12, 1), (12, 2), (12, 3),
    (13, 1), (15, 1), (15, 9), (15, 87), (17, 9), (17, 41), (17, 82),
    (17, 88), (17, 89), (17, 106), (18, 1), (18, 54), (20, 4), (21, 50),
    (25, 1), (25, 32), (26, 192), (26, 193), (27, 1), (27, 6), (27, 76),
    (27, 92), (28, 2), (29, 51), (30, 58), (31, 2), (32, 2), (36, 2),
    (36, 69), (38, 1), (38, 29), (39, 1), (39, 23), (39, 27), (40, 2),
    (41, 2), (41, 3), (41, 41), (41, 42), (41, 44), (42, 7), (42, 52),
    (43, 3), (43, 4), (43, 31), (44, 58), (45, 2), (46, 2), (46, 12),
    (47, 24), (52, 34), (54, 17), (54, 22), (54, 32), (54, 40),
    (55, 1), (55, 2), (56, 77), (56, 78), (56, 79), (56, 80),
    (59, 21), (69, 40), (69, 41), (69, 42), (69, 43), (69, 44), (69, 45),
    (69, 46), (69, 47), (69, 51), (72, 1), (73, 20), (75, 16), (75, 17),
    (75, 18), (75, 19), (76, 23), (80, 11), (80, 12), (80, 13), (80, 14),
    (80, 15), (80, 16), (81, 19), (81, 20), (81, 21), (81, 22), (81, 23),
    (81, 24), (81, 25), (85, 21), (85, 22), (87, 6), (87, 7), (87, 18),
    (87, 19),
]

# Save JSON of all results
results = {
    "task_A": {
        "surah_metrics": surah_metrics,
        "null_permutations": NPERM,
    },
    "task_B": {
        "self_ref_lemmas": list(SELF_REF_FORMS.keys()),
        "lemma_totals": lemma_totals,
        "meccan": meccan_stats,
        "medinan": medinan_stats,
        "obs_diff_meccan_minus_medinan": obs_diff,
        "null_mean": null_mean,
        "null_std": null_sd,
        "z_score": z_obs,
        "emp_p_twotail": emp_p_twotail,
        "n_permutations": 1000,
        "meta_verses_count": len(META_VERSES),
    },
}

with open(OUT_DIR / "csv" / "compression_self_ref_results.json", "w") as f:
    json.dump(results, f, indent=2, ensure_ascii=False)

# ---------- Print tables ----------
print("\n=== Task A: Top 10 MOST-compressible surahs (lowest gzip_ratio) ===")
sorted_by_gz = sorted(surah_metrics, key=lambda x: x["gzip_ratio"])
for m in sorted_by_gz[:10]:
    print(f"  Q{m['surah']:>3} {m['name']:<20} gz={m['gzip_ratio']:.4f} "
          f"z={m['gzip_z']:+.2f}  verses={m['n_verses']:>3} chars={m['n_chars']}")

print("\n=== Task A: Top 10 LEAST-compressible surahs (highest gzip_ratio) ===")
for m in sorted_by_gz[-10:]:
    print(f"  Q{m['surah']:>3} {m['name']:<20} gz={m['gzip_ratio']:.4f} "
          f"z={m['gzip_z']:+.2f}  verses={m['n_verses']:>3} chars={m['n_chars']}")

print("\n=== Task A: surahs with |z| > 2 vs length-matched verse-shuffle null ===")
anom = [m for m in surah_metrics if abs(m["gzip_z"]) > 2]
for m in sorted(anom, key=lambda x: x["gzip_z"]):
    print(f"  Q{m['surah']:>3} {m['name']:<20} gz={m['gzip_ratio']:.4f} "
          f"z={m['gzip_z']:+.2f}  emp_p={m['gzip_emp_p_twotail']:.4f}")

print("\n=== Prediction check ===")
for sid in [55, 77, 54, 2]:
    m = next(x for x in surah_metrics if x["surah"] == sid)
    rank = sorted_by_gz.index(m) + 1
    print(f"  Q{sid} {m['name']:<15} gz={m['gzip_ratio']:.4f} z={m['gzip_z']:+.2f} "
          f"rank {rank}/114 (1=most compressible)")

# muqatta'at surahs: 2, 3, 7, 10, 11, 12, 13, 14, 15, 19, 20, 26, 27, 28, 29, 30, 31, 32, 36, 38, 40, 41, 42, 43, 44, 45, 46, 50, 68
muq = [2,3,7,10,11,12,13,14,15,19,20,26,27,28,29,30,31,32,36,38,40,41,42,43,44,45,46,50,68]
mean_muq = sum(next(x["gzip_ratio"] for x in surah_metrics if x["surah"]==s) for s in muq)/len(muq)
mean_nonmuq = sum(m["gzip_ratio"] for m in surah_metrics if m["surah"] not in muq)/(114-len(muq))
print(f"\n  Muqatta'at-opening mean gzip_ratio: {mean_muq:.4f} (n={len(muq)})")
print(f"  Non-muqatta'at mean gzip_ratio    : {mean_nonmuq:.4f} (n={114-len(muq)})")
print(f"  Difference (muq − nonmuq)         : {mean_muq - mean_nonmuq:+.4f}")

print("\n=== Task B: Self-reference density ===")
print(f"  Meccan: {meccan_stats['total_self_ref_tokens']} tokens over "
      f"{meccan_stats['n_verses']} verses = "
      f"{meccan_stats['tokens_per_verse']:.4f} per verse "
      f"({meccan_stats['frac_verses_with_any']*100:.2f}% of verses have ≥1)")
print(f"  Medinan: {medinan_stats['total_self_ref_tokens']} tokens over "
      f"{medinan_stats['n_verses']} verses = "
      f"{medinan_stats['tokens_per_verse']:.4f} per verse "
      f"({medinan_stats['frac_verses_with_any']*100:.2f}% of verses have ≥1)")
print(f"\n  Obs diff (M − M): {obs_diff:+.5f}")
print(f"  Null mean: {null_mean:+.5f}, null std: {null_sd:.5f}")
print(f"  z-score: {z_obs:+.3f}, empirical two-tail p: {emp_p_twotail:.4f}")
print(f"  Direction: {'Meccan > Medinan (predicted)' if obs_diff > 0 else 'Medinan > Meccan (against prediction)'}")

print("\n=== Lemma-by-lemma ===")
print(f"  {'lemma':<10} {'total':>6} {'Meccan/v':>10} {'Medinan/v':>10} {'ratio':>6}")
for lemma, s in lemma_totals.items():
    ratio = s["meccan_per_verse"] / max(s["medinan_per_verse"], 1e-9)
    print(f"  {lemma:<10} {s['total_tokens']:>6} {s['meccan_per_verse']:>10.4f} "
          f"{s['medinan_per_verse']:>10.4f} {ratio:>6.2f}")

print("\n=== Top 10 surahs by self-reference density ===")
surah_self_ref = []
for sid in range(1, 115):
    ntok = sum(lemma_counts_per_verse[(sid, v)][l]
               for v in range(1, surah_meta[sid]["n_verses"] + 1)
               for l in SELF_REF_FORMS)
    surah_self_ref.append({
        "surah": sid,
        "name": surah_meta[sid]["name"],
        "type": surah_meta[sid]["type"],
        "n_verses": surah_meta[sid]["n_verses"],
        "tokens": ntok,
        "per_verse": ntok / surah_meta[sid]["n_verses"],
    })
for m in sorted(surah_self_ref, key=lambda x: -x["per_verse"])[:10]:
    print(f"  Q{m['surah']:>3} {m['name']:<20} {m['type']:<8} {m['tokens']:>3}/{m['n_verses']:<3} = {m['per_verse']:.3f}")

# Save surah-level self-reference CSV
with open(OUT_DIR / "csv" / "self_reference_per_surah.csv", "w", newline="") as f:
    fieldnames = ["surah", "name", "type", "n_verses", "tokens", "per_verse"]
    w = csv.DictWriter(f, fieldnames=fieldnames)
    w.writeheader()
    for m in surah_self_ref:
        w.writerow(m)

print("\n=== DONE ===", file=sys.stderr)
print("Outputs:", file=sys.stderr)
print(f"  {out_csv}", file=sys.stderr)
print(f"  {OUT_DIR/'csv'/'compression_self_ref_results.json'}", file=sys.stderr)
print(f"  {OUT_DIR/'csv'/'self_reference_per_surah.csv'}", file=sys.stderr)
