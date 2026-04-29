#!/usr/bin/env python3
"""Task #55 — H-NEW-2 × classical iltifāt catalog Spearman ρ.

Pre-registered directions (committed BEFORE join):
  z_H      (chain entropy)  → ρ < 0  (more iltifāt → lower entropy → more negative z_H)
  z_MI     (mutual info)    → ρ > 0  (more iltifāt → higher MI → more positive z_MI)
  z_shift  (shift density)  → ρ < 0  (more iltifāt → more shifts → more negative z_shift)

Primary tuple: Z+S-only subset (high-rigor catalog entries, drop syn-only).
Full-catalog (n=45): secondary sensitivity.
Bonferroni k=5 (Tomorrow Tests family per pre-registration).
"""
import json, math, re
from pathlib import Path

ROOT = Path('/Users/grey/Downloads/quran')
OUT = ROOT / 'findings/phase-b-hypotheses/csv/h-new-2-iltifat-rho.json'

# --- Load H-NEW-2 per-surah z-scores ---
hnew2 = json.loads((ROOT / 'scratch/team-discovery/result-pronoun-entropy.json').read_text())
per_surah_z = {row['surah']: row for row in hnew2['per_surah']}

# --- Parse classical catalog ---
md = (ROOT / 'findings/phase-b-hypotheses/classical-iltifat-catalog.md').read_text()
# Grab the TSV block
m = re.search(r'surah\tcount\texemplars\tsource_tag\n(.*?)```', md, re.DOTALL)
assert m, "catalog TSV block not found"
catalog = []
for line in m.group(1).strip().split('\n'):
    parts = line.split('\t')
    if len(parts) < 4: continue
    try:
        s = int(parts[0]); c = int(parts[1]); tag = parts[3].strip()
        catalog.append({'surah': s, 'count': c, 'tag': tag})
    except ValueError:
        continue
print(f"catalog entries: {len(catalog)}")

# --- Load verse counts ---
Q = json.loads((ROOT / 'quran-text/quran-no-tashkeel.json').read_text())
N_verses = {}
for i, sur in enumerate(Q):
    sid = sur.get('id', i+1)
    N_verses[sid] = len(sur.get('verses', []))

# --- Join ---
# NaN for missing surahs (do NOT impute zero per task spec)
joined = []
for entry in catalog:
    s = entry['surah']
    if s not in per_surah_z:
        continue  # H-NEW-2 didn't test this surah → NaN → exclude
    nv = N_verses.get(s)
    if not nv:
        continue
    density = entry['count'] / nv
    row = {
        'surah': s, 'count': entry['count'], 'N_verses': nv,
        'density': density, 'tag': entry['tag'],
        'z_H': per_surah_z[s]['z_H'],
        'z_MI': per_surah_z[s]['z_MI'],
        'z_shift': per_surah_z[s]['z_shift'],
    }
    joined.append(row)
print(f"joined (catalog ∩ H-NEW-2 tested): {len(joined)}")

# --- Spearman rho + p-value (two-sided, t-approx) ---
def rank(xs):
    # average ranks for ties
    order = sorted(range(len(xs)), key=lambda i: xs[i])
    ranks = [0.0]*len(xs)
    i = 0
    while i < len(xs):
        j = i
        while j+1 < len(xs) and xs[order[j+1]] == xs[order[i]]:
            j += 1
        avg = (i+j)/2.0 + 1
        for k in range(i, j+1):
            ranks[order[k]] = avg
        i = j+1
    return ranks

def spearman(xs, ys):
    n = len(xs)
    rx = rank(xs); ry = rank(ys)
    mx = sum(rx)/n; my = sum(ry)/n
    num = sum((rx[i]-mx)*(ry[i]-my) for i in range(n))
    dx = math.sqrt(sum((r-mx)**2 for r in rx))
    dy = math.sqrt(sum((r-my)**2 for r in ry))
    rho = num/(dx*dy) if dx*dy > 0 else 0.0
    # t-approximation
    if abs(rho) >= 1.0:
        t = float('inf')
    else:
        t = rho*math.sqrt((n-2)/(1-rho*rho))
    # two-sided p via normal approx (n>=20 reasonable)
    # use Student-t CDF via simple erf approximation
    def norm_cdf(z):
        return 0.5*(1+math.erf(z/math.sqrt(2)))
    p_two = 2*(1 - norm_cdf(abs(t)))
    return rho, p_two, n

# --- Primary: full catalog n=45 ∩ tested ---
densities = [r['density'] for r in joined]
primary = {}
for sig in ('z_H', 'z_MI', 'z_shift'):
    vals = [r[sig] for r in joined]
    rho, p, n = spearman(densities, vals)
    primary[sig] = {'rho': rho, 'p_two_sided': p, 'n': n}

# --- Sensitivity: Z+S-only (drop syn + S-only + Z-only? task says "drop syn-only") ---
zs_only = [r for r in joined if r['tag'] != 'syn']
sens_zs = {}
if zs_only:
    d2 = [r['density'] for r in zs_only]
    for sig in ('z_H', 'z_MI', 'z_shift'):
        vals = [r[sig] for r in zs_only]
        rho, p, n = spearman(d2, vals)
        sens_zs[sig] = {'rho': rho, 'p_two_sided': p, 'n': n}

# --- Sensitivity: Z+S-strict (both sources) ---
zs_strict = [r for r in joined if r['tag'] == 'Z+S']
sens_strict = {}
if zs_strict:
    d3 = [r['density'] for r in zs_strict]
    for sig in ('z_H', 'z_MI', 'z_shift'):
        vals = [r[sig] for r in zs_strict]
        rho, p, n = spearman(d3, vals)
        sens_strict[sig] = {'rho': rho, 'p_two_sided': p, 'n': n}

# --- Pre-registered sign verdict ---
pre_reg = {'z_H': '<0', 'z_MI': '>0', 'z_shift': '<0'}
def verdict(rho, p, want):
    signed_p = p/2  # one-sided in pre-registered direction if sign matches
    if (want == '>0' and rho > 0) or (want == '<0' and rho < 0):
        return {'sign_match': True, 'one_sided_p': signed_p, 'bonf_p_k5': min(1.0, signed_p*5)}
    return {'sign_match': False, 'one_sided_p': 1-signed_p, 'bonf_p_k5': 1.0}

# Apply to primary
primary_verdicts = {sig: verdict(primary[sig]['rho'], primary[sig]['p_two_sided'], pre_reg[sig]) for sig in primary}

out = {
    'seed_for_hnew2': 20260413,
    'pre_registered_directions': pre_reg,
    'bonferroni_k': 5,
    'alpha_per_test': 0.01,
    'primary_n45_intersect': {
        'n': len(joined),
        'surahs_joined': [r['surah'] for r in joined],
        'catalog_surahs_not_in_hnew2': [e['surah'] for e in catalog if e['surah'] not in per_surah_z],
        'results': primary,
        'verdicts': primary_verdicts,
    },
    'sensitivity_drop_syn_only': {
        'n': len(zs_only),
        'tag_breakdown': {t: sum(1 for r in zs_only if r['tag']==t) for t in set(r['tag'] for r in zs_only)},
        'results': sens_zs,
    },
    'sensitivity_Z_plus_S_strict': {
        'n': len(zs_strict),
        'results': sens_strict,
    },
    'joined_data': joined,
}

OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text(json.dumps(out, indent=2, ensure_ascii=False))

print(f"\nPRE-REG: z_H<0, z_MI>0, z_shift<0")
print(f"\nPRIMARY (n={len(joined)}):")
for sig in primary:
    r = primary[sig]; v = primary_verdicts[sig]
    print(f"  {sig}: ρ={r['rho']:+.4f}  p2={r['p_two_sided']:.4g}  sign_match={v['sign_match']}  bonf_p_k5={v['bonf_p_k5']:.4g}")
print(f"\nSENSITIVITY drop-syn-only (n={len(zs_only)}):")
for sig in sens_zs:
    r = sens_zs[sig]
    print(f"  {sig}: ρ={r['rho']:+.4f}  p2={r['p_two_sided']:.4g}")
print(f"\nSENSITIVITY Z+S strict (n={len(zs_strict)}):")
for sig in sens_strict:
    r = sens_strict[sig]
    print(f"  {sig}: ρ={r['rho']:+.4f}  p2={r['p_two_sided']:.4g}")
print(f"\nsaved: {OUT}")
