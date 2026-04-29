#!/usr/bin/env python3
"""Length-controlled compression test: compare each surah's gzip ratio to
length-matched null from same-length shuffled text block.

The original test confounds: longer texts compress better, so z-scores
track length. Proper test: draw a random contiguous verse-block of the
same CHAR length from the whole Quran, compute its gzip_ratio, repeat.
"""
import json, gzip, re, random, math
from pathlib import Path

random.seed(42)

ROOT = Path("/Users/grey/Downloads/quran")
CORPUS = ROOT / "quran-text" / "quran-no-tashkeel.json"

with open(CORPUS) as f:
    quran = json.load(f)

all_verses = []
surah_text = {}
surah_name = {}
surah_type = {}
for surah in quran:
    sid = surah["id"]
    surah_name[sid] = surah["transliteration"]
    surah_type[sid] = surah["type"]
    surah_text[sid] = re.sub(r"\s+", " ", " ".join(v["text"] for v in surah["verses"])).strip()
    for v in surah["verses"]:
        all_verses.append(v["text"])

def gzr(t):
    b = t.encode("utf-8")
    return len(gzip.compress(b, compresslevel=9)) / len(b)

# LENGTH-CONTROLLED NULL:
# For each surah of length L, draw 1000 random verse-subsets whose concatenated
# char-length is within ±2% of L. Compute gzip_ratio distribution.

def sample_length_matched(target_len, tolerance=0.02, max_tries=5000):
    lo = target_len * (1 - tolerance)
    hi = target_len * (1 + tolerance)
    pool = all_verses[:]
    for _ in range(max_tries):
        random.shuffle(pool)
        acc = []
        cur = 0
        for v in pool:
            vl = len(v) + 1
            if cur + vl > hi:
                continue
            acc.append(v)
            cur += vl
            if lo <= cur <= hi:
                return re.sub(r"\s+", " ", " ".join(acc)).strip()
        # if loop ends without yielding, try again
    return None

# Run for target surahs
targets = [2, 3, 4, 5, 6, 7, 9, 20, 26, 36, 37, 54, 55, 56, 67, 77, 78, 81, 112]
print(f"{'surah':<5} {'name':<18} {'L':>6} {'gz':>7} {'null_mean':>10} {'null_sd':>8} {'z':>7} {'pct':>6}")

NDRAWS = 500  # reduced; length-matched sampling is expensive

for sid in targets:
    text = surah_text[sid]
    L = len(text)
    obs = gzr(text)
    null_vals = []
    for _ in range(NDRAWS):
        s = sample_length_matched(L, tolerance=0.03)
        if s:
            null_vals.append(gzr(s))
    if not null_vals:
        print(f"Q{sid}: failed to sample")
        continue
    mu = sum(null_vals) / len(null_vals)
    sd = math.sqrt(sum((x-mu)**2 for x in null_vals)/len(null_vals))
    z = (obs - mu) / sd if sd else 0
    pct = sum(1 for x in null_vals if x <= obs) / len(null_vals) * 100
    print(f"Q{sid:<4} {surah_name[sid]:<18} {L:>6} {obs:.4f}  {mu:>10.4f} {sd:>8.4f} {z:>+7.2f} {pct:>5.1f}%")
