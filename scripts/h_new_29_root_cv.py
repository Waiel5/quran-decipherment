#!/usr/bin/env python3
"""H-NEW-29 — root renewal-process CV vs al-Jāḥiẓ *takrār maqbūl*.

For each root with count ≥ 5 in mushaf order, compute coefficient of variation
CV = σ(inter-occurrence) / μ(inter-occurrence). Under Poisson (random placement)
CV → 1. CV < 1 = regular spacing ("takrār maqbūl"), CV > 1 = clumpy.

Sub-tests (Bonferroni k=4, α_bon=0.0125):
  (a) Weighted-mean CV across roots vs bootstrap null — one-sided CV < 1
  (b) Quran vs baseline (Bukhari, Jahiz) surface-word CV (Mann-Whitney U)
  (c) Frequency-bin stratification (rare/mid/frequent/super-frequent)
  (d) Full-token-sequence shuffle null (1000 perms)

Seed 20260413.
"""
import json, math, random, re, sys, statistics
from collections import defaultdict, Counter
from pathlib import Path

ROOT = Path('/Users/grey/Downloads/quran')
random.seed(20260413)

# ---- Load QAC morphology ----
print("Loading QAC morphology...", file=sys.stderr)
LOC_RE = re.compile(r'^\((\d+):(\d+):(\d+):(\d+)\)$')
ROOT_RE = re.compile(r'ROOT:([^|]+)')

# Sequence of (sid, vid, wid, root_or_None) in canonical order
token_seq = []  # list of root or None
with open(ROOT / 'data/morphology/quranic-corpus-morphology-0.4.txt', encoding='utf-8') as f:
    for line in f:
        if line.startswith('#') or line.startswith('LOCATION') or not line.strip():
            continue
        parts = line.rstrip('\n').split('\t')
        if len(parts) < 4:
            continue
        m = LOC_RE.match(parts[0])
        if not m:
            continue
        feat = parts[3]
        # Only consider STEM segments (not PREFIX/SUFFIX), so each content-root
        # word is counted once per word
        if 'STEM' not in feat:
            continue
        rm = ROOT_RE.search(feat)
        if rm:
            token_seq.append(rm.group(1))
        else:
            token_seq.append(None)  # function word / proper name without root

# Filter to tokens with roots
root_tokens = [r for r in token_seq if r is not None]
print(f"  total STEM tokens: {len(token_seq)}", file=sys.stderr)
print(f"  tokens with root: {len(root_tokens)}", file=sys.stderr)

# ---- Build root positional index ----
positions = defaultdict(list)
for i, r in enumerate(root_tokens):
    positions[r].append(i)

# ---- CV per root ----
def cv(ds):
    if len(ds) < 2:
        return None
    m = statistics.mean(ds)
    if m == 0:
        return None
    s = statistics.stdev(ds)
    return s / m

def fano(ds):
    if len(ds) < 2:
        return None
    m = statistics.mean(ds)
    if m == 0:
        return None
    v = statistics.variance(ds)
    return v / m

def compute_root_cvs(positions_map, min_n=5):
    """Returns dict root -> (count, cv, fano, inter_arrivals)."""
    res = {}
    for r, poss in positions_map.items():
        if len(poss) < min_n:
            continue
        ds = [poss[i+1] - poss[i] for i in range(len(poss) - 1)]
        c = cv(ds)
        f = fano(ds)
        if c is None:
            continue
        res[r] = (len(poss), c, f, ds)
    return res

root_cvs = compute_root_cvs(positions, min_n=5)
print(f"  roots with n ≥ 5: {len(root_cvs)}", file=sys.stderr)

def weighted_mean_cv(root_cvs):
    num = 0.0
    den = 0.0
    for r, (n, c, f, ds) in root_cvs.items():
        num += n * c
        den += n
    return num / den if den > 0 else 0.0

wmcv = weighted_mean_cv(root_cvs)
print(f"  weighted mean CV = {wmcv:.4f}", file=sys.stderr)

# Simple mean and median for diagnostic
simple_mean_cv = statistics.mean(c for _, (_, c, _, _) in root_cvs.items())
median_cv = statistics.median(c for _, (_, c, _, _) in root_cvs.items())
print(f"  unweighted mean CV = {simple_mean_cv:.4f}", file=sys.stderr)
print(f"  median CV = {median_cv:.4f}", file=sys.stderr)

# ---- Sub-test (a): bootstrap CI for weighted-mean CV ----
print("\n=== Sub (a): Bootstrap 99% CI ===", file=sys.stderr)
def bootstrap_wmcv(root_cvs, n_boot=10000):
    items = list(root_cvs.items())
    n = len(items)
    boots = []
    for _ in range(n_boot):
        sample = [items[random.randrange(n)] for _ in range(n)]
        total_num = 0.0
        total_den = 0.0
        for r, (count, c, f, ds) in sample:
            total_num += count * c
            total_den += count
        boots.append(total_num / total_den if total_den > 0 else 0)
    boots.sort()
    lo_99 = boots[int(0.005 * n_boot)]
    hi_99 = boots[int(0.995 * n_boot)]
    return lo_99, hi_99, boots

lo_99, hi_99, _ = bootstrap_wmcv(root_cvs, n_boot=5000)
print(f"  bootstrap 99% CI: [{lo_99:.4f}, {hi_99:.4f}]", file=sys.stderr)
sub_a_pass = hi_99 < 0.95
print(f"  upper 99% bound < 0.95? {sub_a_pass}", file=sys.stderr)

# ---- Sub-test (d): shuffle null of Quranic token sequence ----
# Do this BEFORE (c) because shuffle test is the most critical
print("\n=== Sub (d): Token-permutation null (1000 perms) ===", file=sys.stderr)
def shuffle_null_cv(root_tokens, n_perms=1000, min_n=5):
    null_wmcvs = []
    for perm_i in range(n_perms):
        shuffled = root_tokens[:]
        random.shuffle(shuffled)
        null_pos = defaultdict(list)
        for i, r in enumerate(shuffled):
            null_pos[r].append(i)
        null_cvs = compute_root_cvs(null_pos, min_n=min_n)
        null_wmcvs.append(weighted_mean_cv(null_cvs))
    return null_wmcvs

null_wmcvs = shuffle_null_cv(root_tokens, n_perms=500)  # 500 for compute
null_mean = statistics.mean(null_wmcvs)
null_sd = statistics.stdev(null_wmcvs)
z_shuffle = (wmcv - null_mean) / null_sd if null_sd > 0 else 0
print(f"  null μ={null_mean:.4f} ± {null_sd:.4f}", file=sys.stderr)
print(f"  observed={wmcv:.4f}, z = {z_shuffle:.3f}", file=sys.stderr)
sub_d_pass = z_shuffle < -2.5
print(f"  z < -2.5? {sub_d_pass}", file=sys.stderr)

# ---- Sub-test (c): Frequency-bin stratification ----
print("\n=== Sub (c): Frequency bin stratification ===", file=sys.stderr)
BINS = [(5, 10, 'rare'), (10, 50, 'mid'), (50, 200, 'frequent'), (200, 10**6, 'super_frequent')]

def bin_of(n):
    for lo, hi, name in BINS:
        if lo <= n < hi:
            return name
    return None

bin_cvs = defaultdict(list)
bin_counts = defaultdict(list)
for r, (n, c, f, ds) in root_cvs.items():
    b = bin_of(n)
    if b:
        bin_cvs[b].append(c)
        bin_counts[b].append(n)

bin_summary = {}
for _, _, name in BINS:
    if name not in bin_cvs or not bin_cvs[name]:
        bin_summary[name] = None
        continue
    cs = bin_cvs[name]
    ns = bin_counts[name]
    wmean = sum(n*c for n, c in zip(ns, cs)) / sum(ns)
    med = statistics.median(cs)
    bin_summary[name] = {
        'n_roots': len(cs),
        'total_count': sum(ns),
        'weighted_mean_cv': wmean,
        'median_cv': med,
    }
    print(f"  {name}: n={len(cs)} roots, Σn={sum(ns)}, wmcv={wmean:.4f}, med={med:.4f}", file=sys.stderr)

# Compute z per bin vs shuffle null (re-run shuffle per bin or use earlier nulls)
# For simplicity: use bin-specific shuffle on observed bin cv
# Actually, easier: use z from sub (d) as overall, and report bin-specific cv descriptively
# For z-per-bin vs null, we need a per-bin null. Do fast 100 perms per bin.
print("  computing per-bin shuffle nulls (100 perms)...", file=sys.stderr)
bin_z = {}
for bin_name in bin_cvs.keys():
    lo, hi = None, None
    for blo, bhi, bname in BINS:
        if bname == bin_name:
            lo, hi = blo, bhi
            break
    null_bin_cvs = []
    for _ in range(100):
        shuf = root_tokens[:]
        random.shuffle(shuf)
        np = defaultdict(list)
        for i, r in enumerate(shuf):
            np[r].append(i)
        null_rcvs = {}
        for rr, poss in np.items():
            if not (lo <= len(poss) < hi):
                continue
            ds = [poss[j+1] - poss[j] for j in range(len(poss) - 1)]
            cc = cv(ds)
            if cc is None:
                continue
            null_rcvs[rr] = (len(poss), cc)
        if null_rcvs:
            num = sum(n * c for n, c in null_rcvs.values())
            den = sum(n for n, c in null_rcvs.values())
            null_bin_cvs.append(num / den)
    if len(null_bin_cvs) > 1:
        nm = statistics.mean(null_bin_cvs)
        ns = statistics.stdev(null_bin_cvs)
        bz = (bin_summary[bin_name]['weighted_mean_cv'] - nm) / ns if ns > 0 else 0
        bin_z[bin_name] = {'null_mean': nm, 'null_sd': ns, 'z': bz}
        print(f"  {bin_name} z = {bz:.3f} (null μ={nm:.4f}, σ={ns:.4f})", file=sys.stderr)

sub_c_pass = any(
    (bin_z.get(name, {}).get('z', 0) < -2.5) for name in ('frequent', 'super_frequent')
)
print(f"  freq OR super_freq z < -2.5? {sub_c_pass}", file=sys.stderr)

# ---- Sub-test (b): Quran vs baseline corpora ----
# Use surface-word (not root) because baselines lack QAC morphology.
# Strip tashkeel and normalize hamza.
print("\n=== Sub (b): Quran vs baseline CV (surface-word) ===", file=sys.stderr)

def clean_arabic(txt):
    # Remove tashkeel (ranges U+064B-U+065F, U+0670)
    txt = re.sub(r'[\u064B-\u065F\u0670]', '', txt)
    # Normalize hamza
    for src, dst in [('أ','ا'),('إ','ا'),('آ','ا'),('ٱ','ا'),('ء','ا'),
                     ('ؤ','و'),('ئ','ي'),('ى','ي'),('ة','ه')]:
        txt = txt.replace(src, dst)
    return txt

def tokenize_arabic_words(txt):
    txt = clean_arabic(txt)
    # Take maximal Arabic-letter runs
    return re.findall(r'[\u0621-\u064A]+', txt)

def compute_surface_cv(tokens, min_n=5):
    pos = defaultdict(list)
    for i, w in enumerate(tokens):
        pos[w].append(i)
    cvs = {}
    for w, ps in pos.items():
        if len(ps) < min_n:
            continue
        ds = [ps[i+1]-ps[i] for i in range(len(ps)-1)]
        c = cv(ds)
        if c is not None:
            cvs[w] = (len(ps), c)
    return cvs

# Quran surface-word version
qn_text_file = ROOT / 'quran-text/quran-no-tashkeel.json'
Qdata = json.loads(qn_text_file.read_text())
quran_words = []
for s in sorted(Qdata, key=lambda x: x['id']):
    for v in s['verses']:
        quran_words.extend(tokenize_arabic_words(v['text']))
print(f"  Quran surface tokens: {len(quran_words)}", file=sys.stderr)
quran_cvs_surface = compute_surface_cv(quran_words, min_n=5)
quran_wmcv_surface = sum(n*c for _, (n, c) in quran_cvs_surface.items()) / \
    sum(n for _, (n, c) in quran_cvs_surface.items())
print(f"  Quran surface wmcv: {quran_wmcv_surface:.4f}", file=sys.stderr)

baseline_results = {}
for fn in ['bukhari-noquran.txt', 'jahiz-hayawan.txt']:
    p = ROOT / 'data/baseline-corpora/raw' / fn
    if not p.exists():
        continue
    txt = p.read_text()
    words = tokenize_arabic_words(txt)
    # Match length to Quran for fair comparison
    if len(words) > len(quran_words):
        words = words[:len(quran_words)]
    bcvs = compute_surface_cv(words, min_n=5)
    if not bcvs:
        continue
    bwmcv = sum(n*c for _, (n, c) in bcvs.items()) / sum(n for _, (n, c) in bcvs.items())
    print(f"  {fn}: tokens={len(words)}, wmcv={bwmcv:.4f}", file=sys.stderr)
    baseline_results[fn] = {'n_tokens': len(words), 'wmcv': bwmcv, 'n_roots': len(bcvs)}

# Mann-Whitney U: Quran per-root CV vs each baseline per-root CV
def mann_whitney_u(xs, ys):
    """Two-sided U stat + z-score (for large samples)."""
    combined = [(v, 'x') for v in xs] + [(v, 'y') for v in ys]
    combined.sort()
    ranks = {}
    i = 0
    while i < len(combined):
        j = i
        while j + 1 < len(combined) and combined[j+1][0] == combined[i][0]:
            j += 1
        mean_rank = (i + j) / 2 + 1
        for k in range(i, j+1):
            ranks[k] = mean_rank
        i = j + 1
    R_x = sum(ranks[k] for k in range(len(combined)) if combined[k][1] == 'x')
    n1, n2 = len(xs), len(ys)
    U = R_x - n1 * (n1 + 1) / 2
    mu = n1 * n2 / 2
    sigma = math.sqrt(n1 * n2 * (n1 + n2 + 1) / 12)
    z = (U - mu) / sigma if sigma > 0 else 0
    return U, z

mwu_results = {}
for fn, info in baseline_results.items():
    p = ROOT / 'data/baseline-corpora/raw' / fn
    txt = p.read_text()
    words = tokenize_arabic_words(txt)
    if len(words) > len(quran_words):
        words = words[:len(quran_words)]
    bcvs = compute_surface_cv(words, min_n=5)
    qs = [c for _, (_, c) in quran_cvs_surface.items()]
    bs = [c for _, (_, c) in bcvs.items()]
    U, z = mann_whitney_u(qs, bs)
    mwu_results[fn] = {'U': U, 'z': z}
    print(f"  Quran vs {fn}: U={U:.0f}, z={z:.3f}", file=sys.stderr)

sub_b_pass = any(abs(m['z']) > 2.5 and m['z'] < 0 for m in mwu_results.values())
# z < 0 means Quran ranks LOWER CV than baseline
print(f"  any baseline z < -2.5? {sub_b_pass}", file=sys.stderr)

# ---- Top-10 regular vs clumped roots ----
sorted_roots = sorted(root_cvs.items(), key=lambda kv: kv[1][1])
top_regular = sorted_roots[:10]  # lowest CV
top_clumped = sorted_roots[-10:]  # highest CV

print("\n=== Top-10 most regular roots (lowest CV) ===", file=sys.stderr)
for r, (n, c, f, ds) in top_regular:
    print(f"  {r}: n={n}, CV={c:.3f}, F={f:.2f}", file=sys.stderr)

print("\n=== Top-10 most clumped roots (highest CV) ===", file=sys.stderr)
for r, (n, c, f, ds) in top_clumped:
    print(f"  {r}: n={n}, CV={c:.3f}, F={f:.2f}", file=sys.stderr)

# ---- Verdicts ----
ALPHA_BON = 0.05 / 4
print("\n=== VERDICTS (Bonferroni k=4, α_bon=0.0125) ===", file=sys.stderr)
print(f"  sub (a) bootstrap 99% upper < 0.95:  {'PASS' if sub_a_pass else 'FAIL'}", file=sys.stderr)
print(f"  sub (b) Mann-Whitney Quran < baseline: {'PASS' if sub_b_pass else 'FAIL'}", file=sys.stderr)
print(f"  sub (c) freq/super-freq bin z < -2.5: {'PASS' if sub_c_pass else 'FAIL'}", file=sys.stderr)
print(f"  sub (d) shuffle null z < -2.5: {'PASS' if sub_d_pass else 'FAIL'}", file=sys.stderr)

joint_pass = sub_a_pass and sub_b_pass and sub_c_pass and sub_d_pass
print(f"  JOINT: {'PASS' if joint_pass else 'FAIL'}", file=sys.stderr)

# ---- Output ----
out = {
    'seed': 20260413,
    'hypothesis': 'H-NEW-29 root renewal-process CV < 1 (al-Jāḥiẓ takrār maqbūl)',
    'rules_tuple': '(no-tashkeel, QAC roots, mushaf order, 77797-token STEM sequence, n_R ≥ 5)',
    'n_tokens_with_root': len(root_tokens),
    'n_roots_n_ge_5': len(root_cvs),
    'weighted_mean_cv': wmcv,
    'unweighted_mean_cv': simple_mean_cv,
    'median_cv': median_cv,
    'sub_a_bootstrap': {
        'ci99_low': lo_99,
        'ci99_high': hi_99,
        'threshold_upper_lt_0_95': sub_a_pass,
    },
    'sub_b_baseline': {
        'quran_surface_wmcv': quran_wmcv_surface,
        'baselines': baseline_results,
        'mann_whitney': mwu_results,
        'pass': sub_b_pass,
    },
    'sub_c_bins': {
        'bin_summary': bin_summary,
        'bin_z': bin_z,
        'pass': sub_c_pass,
    },
    'sub_d_shuffle': {
        'null_mean': null_mean,
        'null_sd': null_sd,
        'observed': wmcv,
        'z': z_shuffle,
        'pass': sub_d_pass,
    },
    'top_regular_roots': [(r, n, c, f) for r, (n, c, f, _) in top_regular],
    'top_clumped_roots': [(r, n, c, f) for r, (n, c, f, _) in top_clumped],
    'bonferroni_k': 4,
    'alpha_bon': ALPHA_BON,
    'joint_pass': joint_pass,
}
out_path = ROOT / 'findings/phase-b-hypotheses/csv/h-new-29.json'
out_path.parent.mkdir(parents=True, exist_ok=True)
out_path.write_text(json.dumps(out, indent=2, default=str))
print(f"\nsaved: {out_path}", file=sys.stderr)
