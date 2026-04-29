#!/usr/bin/env python3
"""H-NEW-156 — First-content-root inclusio; muq vs non-muq.

Pre-registered single-test (Bonferroni k=1, α=0.05):
  H_1: inclusio rate HIGHER in muq than non-muq.
  Fisher 1-sided + 10K permutation.

Seed 20260417.
"""
import hashlib, json, random, re, sys
from collections import defaultdict
from pathlib import Path
from scipy.stats import fisher_exact

ROOT = Path('/Users/grey/Downloads/quran')
SEED = 20260417
N_PERMS = 10000

QAC_FILE = ROOT / 'data/morphology/quranic-corpus-morphology-0.4.txt'
PREREG_FILE = ROOT / 'findings/phase-b-hypotheses/h-new-156-first-root-inclusio-prereg.md'
OUT_JSON = ROOT / 'findings/phase-b-hypotheses/csv/h-new-156.json'

prereg_sha = hashlib.sha256(PREREG_FILE.read_bytes()).hexdigest()
print(f"prereg SHA-256: {prereg_sha}", file=sys.stderr)

LOC_RE = re.compile(r'^\((\d+):(\d+):(\d+):(\d+)\)$')
ROOT_RE = re.compile(r'ROOT:([^|]+)')

# Per-verse ORDERED list of STEM roots
verse_root_list = defaultdict(lambda: defaultdict(list))
with open(QAC_FILE, encoding='utf-8') as f:
    for line in f:
        if line.startswith('#') or line.startswith('LOCATION') or not line.strip(): continue
        p = line.rstrip().split('\t')
        if len(p) < 4: continue
        m = LOC_RE.match(p[0])
        if not m: continue
        sid, vid = int(m.group(1)), int(m.group(2))
        if 'STEM' not in p[3]: continue
        rm = ROOT_RE.search(p[3])
        if not rm: continue
        verse_root_list[sid][vid].append(rm.group(1))

MUQ_SURAHS = {2, 3, 7, 10, 11, 12, 13, 14, 15, 19, 20, 26, 27, 28, 29, 30,
              31, 32, 36, 38, 40, 41, 42, 43, 44, 45, 46, 50, 68}

def first_root(sid):
    """First STEM root in v1, or v2 if v1 empty (muq-only)."""
    if sid not in verse_root_list:
        return None
    v1 = verse_root_list[sid].get(1, [])
    if v1:
        return v1[0]
    v2 = verse_root_list[sid].get(2, [])
    if v2:
        return v2[0]
    v3 = verse_root_list[sid].get(3, [])
    return v3[0] if v3 else None

def last_verse_roots(sid):
    if sid not in verse_root_list:
        return set()
    last_v = max(verse_root_list[sid].keys())
    return set(verse_root_list[sid][last_v])

results_per_surah = {}
inclusio_muq = 0
inclusio_nonmuq = 0
for s in range(1, 115):
    fr = first_root(s)
    lvr = last_verse_roots(s)
    inclusio = 1 if (fr is not None and fr in lvr) else 0
    is_muq = s in MUQ_SURAHS
    results_per_surah[s] = {
        'first_root': fr,
        'last_verse_roots': sorted(lvr),
        'inclusio': inclusio,
        'is_muq': is_muq,
    }
    if is_muq:
        inclusio_muq += inclusio
    else:
        inclusio_nonmuq += inclusio

n_muq = 29
n_nonmuq = 85
rate_muq = inclusio_muq / n_muq
rate_nonmuq = inclusio_nonmuq / n_nonmuq

print(f"\nInclusio rate in muq surahs: {inclusio_muq}/{n_muq} = {rate_muq:.4f}", file=sys.stderr)
print(f"Inclusio rate in non-muq surahs: {inclusio_nonmuq}/{n_nonmuq} = {rate_nonmuq:.4f}", file=sys.stderr)
print(f"Difference: {rate_muq - rate_nonmuq:+.4f}", file=sys.stderr)

# Muq surahs with inclusio
muq_with = [s for s in sorted(MUQ_SURAHS) if results_per_surah[s]['inclusio']]
print(f"\nMuq surahs WITH inclusio ({len(muq_with)}): {muq_with}", file=sys.stderr)
for s in muq_with[:10]:
    r = results_per_surah[s]
    print(f"  Q {s}: first_root={r['first_root']!r}", file=sys.stderr)

# Fisher exact
table = [[inclusio_muq, n_muq - inclusio_muq],
         [inclusio_nonmuq, n_nonmuq - inclusio_nonmuq]]
odds, p_fisher = fisher_exact(table, alternative='greater')
print(f"\nFisher exact 1-sided p (muq > non-muq): {p_fisher:.4f}", file=sys.stderr)

# Permutation null: shuffle muq labels
rng = random.Random(SEED)
null_diffs = []
all_inclusio = [results_per_surah[s]['inclusio'] for s in range(1, 115)]
for _ in range(N_PERMS):
    surah_ids = list(range(1, 115))
    rng.shuffle(surah_ids)
    shuffled_muq = set(surah_ids[:29])
    r_m = sum(results_per_surah[s]['inclusio'] for s in shuffled_muq) / 29
    r_n = sum(results_per_surah[s]['inclusio'] for s in range(1, 115) if s not in shuffled_muq) / 85
    null_diffs.append(r_m - r_n)

observed_diff = rate_muq - rate_nonmuq
p_perm = sum(1 for d in null_diffs if d >= observed_diff) / N_PERMS
print(f"Permutation 1-sided p: {p_perm:.4f}", file=sys.stderr)

pass_fisher = p_fisher < 0.05
pass_perm = p_perm < 0.05
overall_pass = pass_fisher and pass_perm

verdict = "PASS" if overall_pass else "FAIL"

# Descriptive: Q 50's specific case
print(f"\nQ 50: first_root={results_per_surah[50]['first_root']!r}, "
      f"inclusio={results_per_surah[50]['inclusio']}, "
      f"last_v_roots={results_per_surah[50]['last_verse_roots'][:10]}", file=sys.stderr)

print(f"\n" + "=" * 70, file=sys.stderr)
print(f"Muq: {inclusio_muq}/29 ({rate_muq:.3f}); Non-muq: {inclusio_nonmuq}/85 ({rate_nonmuq:.3f})", file=sys.stderr)
print(f"Fisher p = {p_fisher:.4f}; Permutation p = {p_perm:.4f}", file=sys.stderr)
print(f"VERDICT: {verdict}", file=sys.stderr)
print("=" * 70, file=sys.stderr)

summary = {
    'finding_id': 'h-new-156',
    'title': 'First-content-root inclusio muq vs non-muq',
    'pre_reg_sha256': prereg_sha,
    'seed': SEED,
    'date': '2026-04-17',
    'bonferroni': {'k': 1, 'alpha_bon': 0.05, 'family': 'h-new-156-first-root-inclusio'},
    'muq_count_with_inclusio': inclusio_muq,
    'muq_total': n_muq,
    'muq_rate': rate_muq,
    'nonmuq_count_with_inclusio': inclusio_nonmuq,
    'nonmuq_total': n_nonmuq,
    'nonmuq_rate': rate_nonmuq,
    'rate_difference': observed_diff,
    'fisher_odds_ratio': odds,
    'p_fisher_one_sided_greater': p_fisher,
    'p_permutation_one_sided': p_perm,
    'pass_fisher': pass_fisher,
    'pass_permutation': pass_perm,
    'overall_pass': overall_pass,
    'verdict': verdict,
    'muq_surahs_with_inclusio': muq_with,
    'nonmuq_surahs_with_inclusio': [s for s in range(1,115) if s not in MUQ_SURAHS and results_per_surah[s]['inclusio']],
    'per_surah_results': results_per_surah,
}
OUT_JSON.write_text(json.dumps(summary, indent=2, ensure_ascii=False, default=str))
print(f"\nWrote: {OUT_JSON}", file=sys.stderr)
