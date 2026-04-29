#!/usr/bin/env python3
"""H-NEW-152 — Book-reference inclusio test.

Pre-registered tests (Bonferroni k=2, α_bon=0.025):
  Cell A — count surahs with book-ref (qrA ∪ ktb) in BOTH v1 and v_last;
           compare to expected under independence. 2-sided exact binomial.
  Cell B — same test restricted to qrA (qurʾān-specific) roots.

Seed 20260417. Deterministic.
"""
import hashlib
import json
import math
import random
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path
from scipy.stats import binom

ROOT = Path('/Users/grey/Downloads/quran')
SEED = 20260417
N_PERMS = 10000

QAC_FILE = ROOT / 'data/morphology/quranic-corpus-morphology-0.4.txt'
PREREG_FILE = ROOT / 'findings/phase-b-hypotheses/h-new-152-book-ref-inclusio-prereg.md'
OUT_JSON = ROOT / 'findings/phase-b-hypotheses/csv/h-new-152.json'

prereg_sha = hashlib.sha256(PREREG_FILE.read_bytes()).hexdigest()
print(f"prereg SHA-256: {prereg_sha}", file=sys.stderr)

# ---------------------------------------------------------------------------
# 1. Parse QAC — per-verse STEM roots
# ---------------------------------------------------------------------------
LOC_RE = re.compile(r'^\((\d+):(\d+):(\d+):(\d+)\)$')
ROOT_RE = re.compile(r'ROOT:([^|]+)')
verse_roots = defaultdict(lambda: defaultdict(set))
with open(QAC_FILE, encoding='utf-8') as f:
    for line in f:
        if line.startswith('#') or line.startswith('LOCATION') or not line.strip():
            continue
        p = line.rstrip('\n').split('\t')
        if len(p) < 4:
            continue
        m = LOC_RE.match(p[0])
        if not m:
            continue
        sid, vid = int(m.group(1)), int(m.group(2))
        if 'STEM' not in p[3]:
            continue
        rm = ROOT_RE.search(p[3])
        if not rm:
            continue
        verse_roots[sid][vid].add(rm.group(1))

assert len(verse_roots) == 114

def run_cell(book_roots, cell_name):
    """Run Cell A or B with given book-ref root set."""
    v1_has = [False] * 115
    vlast_has = [False] * 115
    both = []
    for sid in range(1, 115):
        last_v = max(verse_roots[sid].keys())
        v1_roots = verse_roots[sid].get(1, set())
        vlast_roots = verse_roots[sid].get(last_v, set())
        v1_has[sid] = bool(v1_roots & book_roots)
        vlast_has[sid] = bool(vlast_roots & book_roots)
        if v1_has[sid] and vlast_has[sid]:
            both.append(sid)
    n_v1 = sum(v1_has[1:])
    n_vlast = sum(vlast_has[1:])
    n_both = len(both)
    # Expected under independence:
    p_v1 = n_v1 / 114
    p_vlast = n_vlast / 114
    p_joint = p_v1 * p_vlast
    expected = p_joint * 114

    # Exact 2-sided binomial p-value for N_both vs binomial(114, p_joint)
    if p_joint == 0:
        p_binom_two_sided = 1.0
    else:
        # 2-sided via cdf/sf
        p_low = binom.cdf(n_both, 114, p_joint)
        p_high = 1 - binom.cdf(n_both - 1, 114, p_joint)
        p_binom_two_sided = min(1.0, 2 * min(p_low, p_high))

    # Permutation null
    rng = random.Random(SEED + hash(cell_name) % 1000)
    null_counts = []
    v1_arr = v1_has[1:].copy()
    vlast_arr = vlast_has[1:].copy()
    for _ in range(N_PERMS):
        s1 = v1_arr[:]
        s2 = vlast_arr[:]
        rng.shuffle(s1)
        rng.shuffle(s2)
        cnt = sum(1 for i in range(114) if s1[i] and s2[i])
        null_counts.append(cnt)
    # 2-sided: min of upper/lower tail × 2
    p_perm_lower = sum(1 for c in null_counts if c <= n_both) / N_PERMS
    p_perm_upper = sum(1 for c in null_counts if c >= n_both) / N_PERMS
    p_perm_two_sided = min(1.0, 2 * min(p_perm_lower, p_perm_upper))

    # Pass: p_binom_two_sided < 0.025
    passed = p_binom_two_sided < 0.025

    return {
        'cell_name': cell_name,
        'book_roots': sorted(book_roots),
        'n_v1_has': n_v1,
        'n_vlast_has': n_vlast,
        'n_both_v1_and_vlast': n_both,
        'surahs_with_inclusio': both,
        'p_v1': p_v1,
        'p_vlast': p_vlast,
        'p_joint_independent': p_joint,
        'expected_both_under_independence': expected,
        'p_binom_two_sided': p_binom_two_sided,
        'p_perm_lower': p_perm_lower,
        'p_perm_upper': p_perm_upper,
        'p_perm_two_sided': p_perm_two_sided,
        'threshold_alpha_bon': 0.025,
        'pass': passed,
    }

# ---------------------------------------------------------------------------
# 2. Cell A — qrA + ktb
# ---------------------------------------------------------------------------
print("\n[Cell A] qrA + ktb (Qurʾān or kitāb)...", file=sys.stderr)
A = run_cell({'qrA', 'ktb'}, 'A_qrA_ktb')
for k, v in A.items():
    print(f"  {k}: {v}", file=sys.stderr)

# ---------------------------------------------------------------------------
# 3. Cell B — qrA only
# ---------------------------------------------------------------------------
print("\n[Cell B] qrA only (qurʾān-specific)...", file=sys.stderr)
B = run_cell({'qrA'}, 'B_qrA_only')
for k, v in B.items():
    print(f"  {k}: {v}", file=sys.stderr)

# ---------------------------------------------------------------------------
# 4. Final verdict
# ---------------------------------------------------------------------------
if A['pass'] and B['pass']:
    final = "STRUCTURAL — book-ref inclusio is a genuine rare structural pattern; qrA-specific is sharper"
elif A['pass'] and not B['pass']:
    final = "PARTIAL — broader qrA+ktb book-ref rare, qrA-specific common"
elif not A['pass'] and B['pass']:
    final = "NARROW — qrA-inclusio rare but broader ktb weakens pattern"
else:
    final = "NULL — no rare-inclusio pattern at α_bon=0.025"

print("\n" + "=" * 70, file=sys.stderr)
print(f"Cell A (qrA+ktb): n_both={A['n_both_v1_and_vlast']} "
      f"expected={A['expected_both_under_independence']:.2f} "
      f"p={A['p_binom_two_sided']:.4f} {'PASS' if A['pass'] else 'FAIL'}", file=sys.stderr)
print(f"Cell B (qrA):     n_both={B['n_both_v1_and_vlast']} "
      f"expected={B['expected_both_under_independence']:.2f} "
      f"p={B['p_binom_two_sided']:.4f} {'PASS' if B['pass'] else 'FAIL'}", file=sys.stderr)
print(f"FINAL: {final}", file=sys.stderr)
print("=" * 70, file=sys.stderr)

# ---------------------------------------------------------------------------
# 5. Write JSON
# ---------------------------------------------------------------------------
summary = {
    'finding_id': 'h-new-152',
    'title': 'Book-reference inclusio — Q 50 v1↔v_last uniqueness',
    'pre_reg_sha256': prereg_sha,
    'seed': SEED,
    'date': '2026-04-17',
    'bonferroni': {'k': 2, 'alpha_bon': 0.025, 'family': 'h-new-152-book-ref-inclusio'},
    'cell_A': A,
    'cell_B': B,
    'final_verdict': final,
}
OUT_JSON.write_text(json.dumps(summary, indent=2, ensure_ascii=False, default=str))
print(f"\nWrote: {OUT_JSON}", file=sys.stderr)
