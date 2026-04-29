#!/usr/bin/env python3
"""H-NEW-90 — Q 18 al-Kahf 4-narrative structural parallelism vs other multi-narrative surahs.

Pre-registration: findings/phase-b-hypotheses/h-new-90-kahf-narrative-structure-prereg.md

Tests:
  T1  Boundary verification (descriptive)
  T2  Inter-narrative root Jaccard (z vs random 4-block partition)
  T3  v50 narrative-boundary check
  T4  Thematic root sharing (≥3 of 4 narratives, z vs null)
  T5  Opener-triple Jaccard parallelism (z vs null)

Bonferroni k=5 → α_bon = 0.01 → z_threshold = 2.326

Comparator surahs: Q 7, Q 11, Q 26 with FIRST-4-narrative truncation.

Seed: 20260415.
"""
import json
import random
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path('/Users/grey/Downloads/quran')
SEED = 20260415
random.seed(SEED)

# ============================================================
# LOCKED narrative boundaries
# ============================================================
NARRATIVES = {
    18: [
        ('Cave',          9,  26),
        ('Gardens',       32, 44),
        ('Moses-Khidr',   60, 82),
        ('Dhul-Qarnayn',  83, 98),
    ],
    # Q 7 al-Aʿrāf — first 4 prophetic narratives (modal Mawdūdī/Rāzī)
    7: [
        ('Adam',     11, 25),
        ('Nuh',      59, 64),
        ('Hud',      65, 72),
        ('Salih',    73, 79),
    ],
    # Q 11 Hūd — first 4 prophet pericopes
    11: [
        ('Nuh',      25, 49),
        ('Hud',      50, 60),
        ('Salih',    61, 68),
        ('Ibrahim-Lut', 69, 83),
    ],
    # Q 26 al-Shuʿarāʾ — first 4 messenger units
    26: [
        ('Musa',     10, 68),
        ('Ibrahim',  69, 104),
        ('Nuh',      105, 122),
        ('Hud',      123, 140),
    ],
}

# Pre-locked verse-count tuple for null model
KAHF_VCOUNT = tuple(end - start + 1 for _, start, end in NARRATIVES[18])  # (18, 13, 23, 16)
TOTAL_KAHF_NARRATIVE_VERSES = sum(KAHF_VCOUNT)  # 70

# ============================================================
# Tashkeel / orthographic normalization
# ============================================================
TASHKEEL_RE = re.compile(r'[\u064B-\u065F\u0670\u0640\u06D6-\u06ED]')
PUNCT_RE = re.compile(r'[\u06D4\u06DD\u06DE\u06DF\u060C\u061B\u061F\u200C\u200D\u200E\u200F\u00B7]+')

def normalize_token(w):
    w = TASHKEEL_RE.sub('', w)
    w = PUNCT_RE.sub('', w)
    for src, dst in [('أ','ا'),('إ','ا'),('آ','ا'),('ٱ','ا'),
                     ('ؤ','و'),('ئ','ي'),('ى','ي'),('ة','ه')]:
        w = w.replace(src, dst)
    return w.strip()

# ============================================================
# Load Quran (no tashkeel)
# ============================================================
Qdata = json.loads((ROOT / 'quran-text/quran-no-tashkeel.json').read_text(encoding='utf-8'))
surahs = {s['id']: s for s in Qdata}
print(f"loaded Quran: {len(surahs)} surahs", file=sys.stderr)

# Extract verse text
def get_verse_text(sid, vid):
    s = surahs[sid]
    for v in s['verses']:
        if v['id'] == vid:
            return v['text'].strip()
    return ''

def get_verse_tokens(sid, vid):
    """Whitespace-split tokens of verse, normalized."""
    text = get_verse_text(sid, vid)
    if not text:
        return []
    return [normalize_token(t) for t in text.split() if normalize_token(t)]

# ============================================================
# Load QAC roots per (sid:vid:wid:sid)
# ============================================================
QAC_PATH = ROOT / 'data/morphology/quranic-corpus-morphology-0.4.txt'
ROOT_LOC = re.compile(r'\((\d+):(\d+):(\d+):(\d+)\)')
ROOT_FEAT = re.compile(r'ROOT:([A-Za-z~]+)')

verse_roots = defaultdict(set)  # (sid, vid) -> set of roots
with open(QAC_PATH, encoding='utf-8') as f:
    for line in f:
        if line.startswith('#') or line.startswith('LOCATION'):
            continue
        line = line.rstrip('\n')
        if not line.strip():
            continue
        parts = line.split('\t')
        if len(parts) < 4:
            continue
        loc, form, tag, feat = parts[:4]
        m = ROOT_LOC.match(loc)
        if not m:
            continue
        sid, vid, wid, segid = (int(x) for x in m.groups())
        rm = ROOT_FEAT.search(feat)
        if rm:
            root = rm.group(1)
            verse_roots[(sid, vid)].add(root)

print(f"loaded roots for {len(verse_roots)} verses", file=sys.stderr)

# ============================================================
# Narrative-block extraction
# ============================================================
def narrative_roots(sid, start, end):
    """Union of all triliteral roots in [start, end] verses of surah sid."""
    rs = set()
    for v in range(start, end + 1):
        rs |= verse_roots.get((sid, v), set())
    return rs

def narrative_tokens(sid, start, end):
    """All normalized tokens in narrative range."""
    out = []
    for v in range(start, end + 1):
        out.extend(get_verse_tokens(sid, v))
    return out

def opener_triple(sid, start, end):
    """First 3 normalized tokens of the opening verse of the narrative."""
    toks = get_verse_tokens(sid, start)
    return tuple(toks[:3])

# ============================================================
# Jaccard
# ============================================================
def jaccard(a, b):
    if not a and not b:
        return 0.0
    return len(a & b) / len(a | b) if (a | b) else 0.0

def mean_offdiag(matrix):
    n = len(matrix)
    s = 0.0
    c = 0
    for i in range(n):
        for j in range(i + 1, n):
            s += matrix[i][j]
            c += 1
    return s / c if c else 0.0

# ============================================================
# Compute observed inter-narrative Jaccard matrix per surah
# ============================================================
def surah_narrative_matrix(sid):
    nrs = []
    for name, start, end in NARRATIVES[sid]:
        nrs.append(narrative_roots(sid, start, end))
    n = len(nrs)
    M = [[0.0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i == j:
                M[i][j] = 1.0
            else:
                M[i][j] = jaccard(nrs[i], nrs[j])
    return M, nrs

# ============================================================
# Null model: random 4-block partition of contiguous verse range
# preserving Kahf verse-count tuple (18, 13, 23, 16) on the narrative
# verses of the SAME surah.
# ============================================================
def random_partition_jaccard(sid, vcount=KAHF_VCOUNT, n_iter=1000):
    """For surah sid, take contiguous narrative-range verses and randomly
    partition them into 4 contiguous blocks of sizes from vcount (in random order)."""
    # Use the NARRATIVE verses (all verses inside any locked narrative in this surah)
    all_vs = []
    for name, start, end in NARRATIVES[sid]:
        all_vs.extend(range(start, end + 1))
    # Block-size pool = vcount (Kahf's 18, 13, 23, 16)
    pool = list(vcount)
    n_total = sum(pool)
    if n_total > len(all_vs):
        # Truncate vcount to fit
        # (shouldn't happen for our four surahs but guard)
        pool = pool[:len(all_vs)]
    means = []
    n_3of4_list = []
    for it in range(n_iter):
        # Shuffle the verse pool
        vshuffled = all_vs.copy()
        random.shuffle(vshuffled)
        shuffled_pool = pool.copy()
        random.shuffle(shuffled_pool)
        idx = 0
        blocks = []
        for sz in shuffled_pool:
            block = vshuffled[idx:idx + sz]
            idx += sz
            blocks.append(block)
        # Compute root sets
        block_roots = [set().union(*[verse_roots.get((sid, v), set()) for v in b]) for b in blocks]
        # Off-diag jaccard mean
        n = len(block_roots)
        s = 0.0
        c = 0
        for i in range(n):
            for j in range(i + 1, n):
                s += jaccard(block_roots[i], block_roots[j])
                c += 1
        means.append(s / c if c else 0.0)
        # 3-of-4 root count
        if n == 4:
            allr = set().union(*block_roots)
            n_3of4 = sum(1 for r in allr if sum(r in br for br in block_roots) >= 3)
            n_3of4_list.append(n_3of4)
        else:
            n_3of4_list.append(0)
    return means, n_3of4_list

# ============================================================
# Stats
# ============================================================
def mean_std(xs):
    if not xs:
        return 0.0, 0.0
    m = sum(xs) / len(xs)
    v = sum((x - m) ** 2 for x in xs) / len(xs)
    return m, v ** 0.5

def zscore(obs, null):
    m, sd = mean_std(null)
    return (obs - m) / sd if sd > 0 else 0.0

# ============================================================
# Cell T1 — Boundary verification (descriptive)
# ============================================================
print("\n" + "=" * 60, file=sys.stderr)
print("Cell T1 — Boundary verification", file=sys.stderr)
print("=" * 60, file=sys.stderr)
T1_results = {}
for sid in (18, 7, 11, 26):
    s = surahs[sid]
    nv = len(s['verses'])
    print(f"S{sid} ({s['transliteration']}, {nv} verses):", file=sys.stderr)
    block_info = []
    for name, start, end in NARRATIVES[sid]:
        # Check first and last verse exist
        v1 = get_verse_text(sid, start)
        vN = get_verse_text(sid, end)
        ok = bool(v1 and vN)
        nverses = end - start + 1
        block_info.append({
            'name': name,
            'start': start,
            'end': end,
            'n_verses': nverses,
            'opener_triple': opener_triple(sid, start, end),
            'opener_v_text_head': v1[:60] + ('…' if len(v1) > 60 else ''),
            'verses_ok': ok,
        })
        print(f"  {name:14s} v{start:3d}-{end:3d} ({nverses:2d} verses) opener: {' '.join(opener_triple(sid, start, end))}", file=sys.stderr)
    T1_results[sid] = block_info

# ============================================================
# Cell T2 — Inter-narrative root Jaccard + null
# ============================================================
print("\n" + "=" * 60, file=sys.stderr)
print("Cell T2 — Inter-narrative root Jaccard", file=sys.stderr)
print("=" * 60, file=sys.stderr)
T2_results = {}
for sid in (18, 7, 11, 26):
    M, nrs = surah_narrative_matrix(sid)
    obs = mean_offdiag(M)
    null_means, null_3of4 = random_partition_jaccard(sid, n_iter=1000)
    z = zscore(obs, null_means)
    null_m, null_sd = mean_std(null_means)
    T2_results[sid] = {
        'matrix': M,
        'mean_offdiag': obs,
        'null_mean': null_m,
        'null_std': null_sd,
        'z_score': z,
        'null_3of4': null_3of4,
        'narrative_root_sizes': [len(r) for r in nrs],
    }
    print(f"S{sid}: mean_offdiag = {obs:.4f}, null_mean = {null_m:.4f} ± {null_sd:.4f}, z = {z:+.3f}", file=sys.stderr)
    print("  4x4 Jaccard matrix:", file=sys.stderr)
    names = [n for n, _, _ in NARRATIVES[sid]]
    header = "    " + "  ".join(f"{n[:9]:>9s}" for n in names)
    print(header, file=sys.stderr)
    for i, n in enumerate(names):
        row = f"  {n[:9]:>9s} " + "  ".join(f"{M[i][j]:9.4f}" for j in range(len(names)))
        print(row, file=sys.stderr)

# ============================================================
# Cell T3 — v50 narrative-boundary check
# ============================================================
print("\n" + "=" * 60, file=sys.stderr)
print("Cell T3 — v50 boundary check", file=sys.stderr)
print("=" * 60, file=sys.stderr)
v50_in_narrative = None
v50_in_interlude = False
for name, start, end in NARRATIVES[18]:
    if start <= 50 <= end:
        v50_in_narrative = name
        break
if v50_in_narrative is None:
    # Check interludes
    interludes = [
        ('Opening',     1,  8),
        ('InterludeA',  27, 31),
        ('InterludeB',  45, 59),
        ('Closing',     99, 110),
    ]
    for name, start, end in interludes:
        if start <= 50 <= end:
            v50_in_interlude = True
            v50_location = name
            break
T3_results = {
    'verse': 50,
    'in_narrative': v50_in_narrative,
    'in_interlude': v50_in_interlude,
    'location': v50_location if v50_in_interlude else v50_in_narrative,
    'is_narrative_interior_or_boundary': not v50_in_interlude,
}
print(f"v50 location: {T3_results['location']}", file=sys.stderr)
print(f"v50 in narrative: {v50_in_narrative}, in interlude: {v50_in_interlude}", file=sys.stderr)
# Also report what v50 says
v50_text = get_verse_text(18, 50)
print(f"v50 text head: {v50_text[:100]}", file=sys.stderr)

# ============================================================
# Cell T4 — Thematic root sharing (≥3 of 4 narratives)
# ============================================================
print("\n" + "=" * 60, file=sys.stderr)
print("Cell T4 — ≥3-of-4 narrative root count", file=sys.stderr)
print("=" * 60, file=sys.stderr)
T4_results = {}
for sid in (18, 7, 11, 26):
    nrs = []
    for name, start, end in NARRATIVES[sid]:
        nrs.append(narrative_roots(sid, start, end))
    allr = set().union(*nrs)
    counts = {r: sum(r in nr for nr in nrs) for r in allr}
    n_3of4 = sum(1 for r, c in counts.items() if c >= 3)
    n_4of4 = sum(1 for r, c in counts.items() if c == 4)
    null_3of4 = T2_results[sid]['null_3of4']
    null_m, null_sd = mean_std(null_3of4)
    z = zscore(n_3of4, null_3of4)
    # Print top shared roots (4-of-4)
    top4 = sorted([r for r, c in counts.items() if c == 4])
    T4_results[sid] = {
        'n_3of4': n_3of4,
        'n_4of4': n_4of4,
        'null_mean': null_m,
        'null_std': null_sd,
        'z_score': z,
        'roots_4of4': top4,
        'union_size': len(allr),
    }
    print(f"S{sid}: n_3of4 = {n_3of4}, n_4of4 = {n_4of4}, null = {null_m:.2f} ± {null_sd:.2f}, z = {z:+.3f}", file=sys.stderr)
    print(f"  union root count = {len(allr)}, 4-of-4 roots = {top4[:20]}", file=sys.stderr)

# ============================================================
# Cell T5 — Opener-triple Jaccard
# ============================================================
print("\n" + "=" * 60, file=sys.stderr)
print("Cell T5 — Opener-triple parallelism", file=sys.stderr)
print("=" * 60, file=sys.stderr)
T5_results = {}
for sid in (18, 7, 11, 26):
    triples = [opener_triple(sid, s, e) for _, s, e in NARRATIVES[sid]]
    sets = [set(t) for t in triples]
    n = len(sets)
    M = [[0.0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            M[i][j] = 1.0 if i == j else jaccard(sets[i], sets[j])
    obs = mean_offdiag(M)
    # Null: random 4 verses from the surah (any verses)
    s = surahs[sid]
    all_v_ids = [v['id'] for v in s['verses']]
    null_obs = []
    for it in range(1000):
        vs = random.sample(all_v_ids, 4)
        null_triples = [tuple(get_verse_tokens(sid, v)[:3]) for v in vs]
        null_sets = [set(t) for t in null_triples]
        nm = mean_offdiag([
            [1.0 if i == j else jaccard(null_sets[i], null_sets[j]) for j in range(4)]
            for i in range(4)
        ])
        null_obs.append(nm)
    null_m, null_sd = mean_std(null_obs)
    z = zscore(obs, null_obs)
    T5_results[sid] = {
        'triples': triples,
        'mean_offdiag': obs,
        'null_mean': null_m,
        'null_std': null_sd,
        'z_score': z,
    }
    print(f"S{sid}: opener-Jaccard mean = {obs:.4f}, null = {null_m:.4f} ± {null_sd:.4f}, z = {z:+.3f}", file=sys.stderr)
    for i, (name, _, _) in enumerate(NARRATIVES[sid]):
        print(f"  {name:14s} triple: {' '.join(triples[i])}", file=sys.stderr)

# ============================================================
# MW-5 positive control
# ============================================================
print("\n" + "=" * 60, file=sys.stderr)
print("MW-5 — N3↔N4 (Moses-Khidr ↔ Dhul-Qarnayn) above mean check", file=sys.stderr)
print("=" * 60, file=sys.stderr)
M_kahf, _ = surah_narrative_matrix(18)
n3_n4 = M_kahf[2][3]
mean_off = T2_results[18]['mean_offdiag']
mw5_pass = n3_n4 > mean_off
print(f"  Kahf N3↔N4 jaccard = {n3_n4:.4f}", file=sys.stderr)
print(f"  Kahf mean off-diag = {mean_off:.4f}", file=sys.stderr)
print(f"  MW-5 verdict: {'PASS' if mw5_pass else 'FAIL — metric broken'}", file=sys.stderr)

# ============================================================
# Verdict aggregation
# ============================================================
print("\n" + "=" * 60, file=sys.stderr)
print("VERDICT TABLE", file=sys.stderr)
print("=" * 60, file=sys.stderr)
Z_THRESHOLD = 2.326  # one-tailed Bonferroni alpha=0.01

cells = {}
# T1: boundaries verified (descriptive — always PASS if data extracted)
t1_pass = all(b['verses_ok'] for sid in T1_results for b in T1_results[sid])
cells['T1'] = {
    'pass': t1_pass,
    'metric': '4-of-4 boundaries extracted',
    'value': sum(1 for b in T1_results[18] if b['verses_ok']),
}
# T2: Kahf z > 2.326 AND z(Kahf) > z(comparators)
kahf_z2 = T2_results[18]['z_score']
comp_z2 = [T2_results[sid]['z_score'] for sid in (7, 11, 26)]
t2_pass = (kahf_z2 > Z_THRESHOLD) and all(kahf_z2 > z for z in comp_z2)
cells['T2'] = {
    'pass': t2_pass,
    'metric': 'inter-narrative Jaccard z',
    'value': kahf_z2,
    'comparator_z': dict(zip([7, 11, 26], comp_z2)),
}
# T3: v50 in interlude
cells['T3'] = {
    'pass': T3_results['in_interlude'],
    'metric': 'v50 in interlude (NOT narrative)',
    'value': T3_results['location'],
}
# T4: Kahf z > 2.326 AND > comparators
kahf_z4 = T4_results[18]['z_score']
comp_z4 = [T4_results[sid]['z_score'] for sid in (7, 11, 26)]
t4_pass = (kahf_z4 > Z_THRESHOLD) and all(kahf_z4 > z for z in comp_z4)
cells['T4'] = {
    'pass': t4_pass,
    'metric': '≥3-of-4 thematic roots z',
    'value': kahf_z4,
    'comparator_z': dict(zip([7, 11, 26], comp_z4)),
}
# T5: Kahf opener z > 2.326
kahf_z5 = T5_results[18]['z_score']
comp_z5 = [T5_results[sid]['z_score'] for sid in (7, 11, 26)]
t5_pass = kahf_z5 > Z_THRESHOLD
cells['T5'] = {
    'pass': t5_pass,
    'metric': 'opener-triple Jaccard z',
    'value': kahf_z5,
    'comparator_z': dict(zip([7, 11, 26], comp_z5)),
}

n_pass = sum(1 for c in cells.values() if c['pass'])
print(f"\nCells PASS: {n_pass}/5", file=sys.stderr)
for k, v in cells.items():
    status = 'PASS' if v['pass'] else 'FAIL'
    val = v['value']
    if isinstance(val, float):
        val = f"{val:+.3f}"
    print(f"  {k}: {status:4s} ({v['metric']} = {val})", file=sys.stderr)
print(f"  MW-5: {'PASS' if mw5_pass else 'FAIL'}", file=sys.stderr)

# Final verdict
if not mw5_pass:
    verdict = 'NULL-BROKEN'
elif n_pass == 5:
    verdict = 'UNIQUE-4-NARRATIVE'
elif n_pass >= 3:
    verdict = 'PARTIAL-UNIQUE'
elif n_pass >= 1:
    verdict = 'WEAK'
else:
    verdict = 'NULL'
print(f"\n*** OVERALL VERDICT: {verdict} ***", file=sys.stderr)

# ============================================================
# Save JSON results
# ============================================================
out = {
    'id': 'H-NEW-90',
    'verdict': verdict,
    'mw5_pass': mw5_pass,
    'n_pass': n_pass,
    'z_threshold_bonferroni': Z_THRESHOLD,
    'cells': {k: {kk: vv for kk, vv in v.items() if kk != 'matrix'} for k, v in cells.items()},
    'T1_boundaries': T1_results,
    'T2_jaccard': {sid: {k: v for k, v in T2_results[sid].items() if k not in ('matrix', 'null_3of4')} for sid in T2_results},
    'T2_matrices': {sid: T2_results[sid]['matrix'] for sid in T2_results},
    'T3_v50': T3_results,
    'T4_thematic': {sid: {k: v for k, v in T4_results[sid].items() if k != 'roots_4of4'} for sid in T4_results},
    'T4_roots_4of4': {sid: T4_results[sid]['roots_4of4'] for sid in T4_results},
    'T5_openers': {sid: {k: (list(map(list, v)) if k == 'triples' else v) for k, v in T5_results[sid].items()} for sid in T5_results},
    'mw5_n3n4_jaccard': n3_n4,
    'mw5_mean_offdiag': mean_off,
}

# Convert tuples to lists in T1 for JSON
for sid in out['T1_boundaries']:
    for b in out['T1_boundaries'][sid]:
        b['opener_triple'] = list(b['opener_triple'])

# Write
out_path = ROOT / 'findings/phase-c-structures/csv/h-new-90-results.json'
out_path.parent.mkdir(parents=True, exist_ok=True)
out_path.write_text(json.dumps(out, indent=2, ensure_ascii=False), encoding='utf-8')
print(f"\nResults written to {out_path}", file=sys.stderr)

# stdout final summary
print(json.dumps({'verdict': verdict, 'n_pass': n_pass, 'cells': {k: v['pass'] for k, v in cells.items()}, 'mw5': mw5_pass}, ensure_ascii=False))
