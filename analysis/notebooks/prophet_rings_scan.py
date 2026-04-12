#!/usr/bin/env python3
"""
Finer-grained scan: for each prophet pericope declared in prophet_rings.py,
slide every contiguous sub-window (sizes 5..15) inside the declared range,
compute ring-score, and test against the intra-window shuffle null.

Purpose: discover whether a smaller ring lives INSIDE a pericope we declared
larger. This is the same sub-surah sliding-window logic as chiastic-audit.

Family size for Bonferroni: sum over pericopes of their windows.
"""
from __future__ import annotations
import json, re, random, statistics, sys
from pathlib import Path
from collections import defaultdict

ROOT = Path('/Users/grey/Downloads/quran')
QURAN_JSON = ROOT / 'quran-text/quran-no-tashkeel.json'
MORPH = ROOT / 'data/morphology/quranic-corpus-morphology-0.4.txt'
SAHIH = ROOT / 'data/translations/en.sahih.txt'
OUT_JSON = ROOT / 'analysis/notebooks/prophet_rings_scan_results.json'

LOC_RE = re.compile(r'^\((\d+):(\d+):(\d+):(\d+)\)$')
ROOT_RE = re.compile(r'ROOT:([^|]+)')

def load_roots_per_verse():
    rv = defaultdict(set)
    with open(MORPH, encoding='utf-8') as f:
        header_seen = False
        for line in f:
            line = line.rstrip('\n')
            if not line or line.startswith('#'): continue
            if line.startswith('LOCATION'):
                header_seen = True; continue
            if not header_seen: continue
            parts = line.split('\t')
            if len(parts) < 4: continue
            loc = parts[0]; feats = parts[3]
            m = LOC_RE.match(loc)
            if not m: continue
            s, v = int(m.group(1)), int(m.group(2))
            rm = ROOT_RE.search(feats)
            if rm: rv[(s, v)].add(rm.group(1))
    return rv

def jaccard(a, b):
    u = a | b
    if not u: return 0.0
    return len(a & b) / len(u)

def ring_score(vr):
    n = len(vr); half = n // 2
    if half == 0: return 0.0
    return sum(jaccard(vr[i], vr[n-1-i]) for i in range(half)) / half

# same pericope list as prophet_rings.py
PERICOPES = [
    ('Noah', 'Surah Nuh', 71, 1, 28),
    ('Noah', 'Hud Noah', 11, 25, 49),
    ('Noah', 'A`raf Noah', 7, 59, 64),
    ('Noah', 'Shu`ara Noah', 26, 105, 122),
    ('Moses', 'Qasas birth', 28, 7, 42),
    ('Moses', 'Ta-Ha long', 20, 9, 98),
    ('Moses', 'A`raf Moses', 7, 103, 162),
    ('Moses', 'Shu`ara Moses', 26, 10, 68),
    ('Abraham', 'Baqara 124-141', 2, 124, 141),
    ('Abraham', 'An`am Afl', 6, 74, 83),
    ('Abraham', 'Hud angelic', 11, 69, 76),
    ('Abraham', 'Ibrahim prayer', 14, 35, 41),
    ('Abraham', 'Maryam', 19, 41, 50),
    ('Abraham', 'Anbiya idols', 21, 51, 73),
    ('Abraham', 'Shu`ara Ibrahim', 26, 69, 104),
    ('Abraham', 'Saffat sacrifice', 37, 83, 113),
    ('Joseph', 'Yusuf whole', 12, 1, 111),
    ('Joseph', 'Yusuf brothers', 12, 7, 18),
    ('Joseph', 'Yusuf prison', 12, 36, 42),
    ('Joseph', 'Yusuf recognition', 12, 58, 93),
    ('Joseph', 'Yusuf reunion', 12, 94, 101),
    ('David/Solomon', 'Naml hoopoe', 27, 15, 44),
    ('David/Solomon', 'Sad David/Sol', 38, 17, 40),
    ('David/Solomon', 'Saba jinn', 34, 10, 14),
    ('Jonah', '37 whale', 37, 139, 148),
    ('Jonah', 'Yunus whole', 10, 1, 109),
    ('Jesus', 'AL-Imran', 3, 35, 63),
    ('Jesus', 'Ma\'ida table', 5, 109, 120),
    ('Jesus', 'Maryam', 19, 16, 40),
    ('Adam', 'Baqara', 2, 30, 39),
    ('Adam', 'A`raf', 7, 11, 25),
    ('Adam', 'Hijr', 15, 26, 42),
    ('Adam', 'Ta-Ha', 20, 115, 127),
]

def main():
    roots = load_roots_per_verse()
    with open(QURAN_JSON) as f: quran = json.load(f)
    surah_roots = {}
    for s in quran:
        sid = s['id']; n = s['total_verses']
        surah_roots[sid] = [roots.get((sid, v+1), set()) for v in range(n)]

    sahih_lines = SAHIH.read_text(encoding='utf-8').splitlines()
    verse_index = []
    for s in quran:
        for v in range(1, s['total_verses']+1):
            verse_index.append((s['id'], v))
    vmap = {sv:i for i,sv in enumerate(verse_index)}
    def sahih(s, v): return sahih_lines[vmap[(s,v)]]

    all_windows = []
    N_TRIALS = 500
    for prophet, label, sid, start, end in PERICOPES:
        full_peri = surah_roots[sid][start-1:end]
        P = len(full_peri)
        for w in range(5, 16):
            if w > P: break
            for off in range(0, P - w + 1):
                sub = full_peri[off:off+w]
                obs = ring_score(sub)
                # intra-window shuffle null
                null_scores = []
                for t in range(N_TRIALS):
                    rng = random.Random(sid*1000000 + start*1000 + off*100 + w*10 + t)
                    perm = list(sub); rng.shuffle(perm)
                    null_scores.append(ring_score(perm))
                mu = statistics.fmean(null_scores)
                sd = statistics.pstdev(null_scores) or 1e-12
                z = (obs - mu) / sd
                if z > 2.0 or obs > 0.18:
                    all_windows.append({
                        'prophet': prophet, 'label': label,
                        'surah': sid, 'start': start+off, 'end': start+off+w-1,
                        'w': w, 'obs': obs, 'z': z, 'mu': mu, 'sd': sd,
                    })

    all_windows.sort(key=lambda r: -r['z'])
    # For each pericope, keep the best window
    best = {}
    for w in all_windows:
        k = (w['prophet'], w['label'])
        if k not in best or w['z'] > best[k]['z']:
            best[k] = w

    # Bonferroni family size = total windows scanned
    total = 0
    for prophet, label, sid, start, end in PERICOPES:
        P = end - start + 1
        for ww in range(5, 16):
            if ww > P: break
            total += (P - ww + 1)
    from statistics import NormalDist
    nd = NormalDist()
    z_crit = nd.inv_cdf(1 - 0.05/total)

    out = {
        'family_size': total,
        'bonferroni_z': z_crit,
        'top_windows': all_windows[:50],
        'best_per_pericope': list(best.values()),
    }
    with open(OUT_JSON, 'w') as f: json.dump(out, f, indent=2, default=str)
    print(f'Scanned {total} windows, Bonferroni z_crit={z_crit:.2f}', file=sys.stderr)
    print('\nTop 25 windows by z:', file=sys.stderr)
    for w in all_windows[:25]:
        survive = '***' if w['z'] > z_crit else '   '
        print(f"  {survive} {w['prophet']:14s} {w['label']:20s} {w['surah']:3d}:{w['start']:3d}-{w['end']:3d} w={w['w']:2d} obs={w['obs']:.3f} z={w['z']:+.2f}", file=sys.stderr)

if __name__ == '__main__':
    main()
