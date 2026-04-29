#!/usr/bin/env python3
"""
H-NEW-41 — Root Combinatorial Saturation (post-audit-032 amendment)

Pre-registered test. Spec locked 2026-04-15 in
  findings/phase-b-hypotheses/h-new-41-root-combinatorial-saturation-prereg.md
  (with AMENDMENTS 41-A and 41-B, 2026-04-15, tightening-only).

AMENDMENT 41-A: MW-5 positive-control is LEAVE-ONE-CORPUS-OUT.
  z_Mutanabbī is computed against null subsets of C with Mutanabbī's roots
  held out. PASS iff all 12 |z_M|<2.0. FAIL any cell -> NULL-BROKEN.
  Intermediate 1-11 -> PARTIAL-POSITIVE-CONTROL, Quran downgraded to EXPLORATORY.

AMENDMENT 41-B: SHA-256 lock of classical reference.
  Lane/Wehr not available on disk. Fallback C = QAC ∪ Mutanabbī-roots-only.
  SHA-256 of source files pinned below.

Source files (SHA-256):
  QAC morphology v0.4:
    /Users/grey/Downloads/quran/data/morphology/quranic-corpus-morphology-0.4.txt
    a1d12923815341face765083805d2148ed2d9f5cc3f7d6665219d887675d8c46
  Mutanabbī Dīwān (classical prose fallback):
    /Users/grey/Downloads/quran/data/baseline-corpora/raw/mutanabbi-diwan.txt
    d1bbed14b25111436af4149bacb5ff7cf3f400979a16e13cc45bf0d9a7ca89b9

Transparency (garden-of-forking-paths, 2026-04-15):
  An initial run (using a broader C = QAC ∪ multiple classical prose corpora,
  not restricted by amendment 41-B) was executed and its results viewed by
  the agent BEFORE amendments 41-A and 41-B were filed by audit-032. The
  amendments were filed as tightening-only (narrower C, held-out z_M). This
  re-run applies the amendments exactly as written. The prior-C results are
  preserved in the journal as h-new-41-run-1-prior-to-amendments.log; they
  are NOT used to adjudicate the verdict — only the amendment-compliant run
  is authoritative.

Seed fixed to 20260415. Numpy default_rng.
"""
import hashlib
import json
import re
import sys
import time
from collections import Counter
from pathlib import Path

import numpy as np

ROOT = Path('/Users/grey/Downloads/quran')
SEED = 20260415
N_NULL = 10000
ALPHA_BON_OUTER = 0.05 / 3  # = 0.01667 (family 2026-04-15-Fresh-Wave-3, k=3)
INNER_CELLS = 12
ALPHA_PER_CELL = ALPHA_BON_OUTER / INNER_CELLS  # = 1.389e-3

QAC_PATH = ROOT / 'data/morphology/quranic-corpus-morphology-0.4.txt'
MUT_PATH = ROOT / 'data/baseline-corpora/raw/mutanabbi-diwan.txt'
QAC_SHA = 'a1d12923815341face765083805d2148ed2d9f5cc3f7d6665219d887675d8c46'
MUT_SHA = 'd1bbed14b25111436af4149bacb5ff7cf3f400979a16e13cc45bf0d9a7ca89b9'

# ---------- Buckwalter letter set ----------
BW_LETTERS = [
    '>', 'b', 't', 'v', 'j', 'H', 'x', 'd', '*', 'r',
    'z', 's', '$', 'S', 'D', 'T', 'Z', 'E', 'g', 'f',
    'q', 'k', 'l', 'm', 'n', 'h', 'w', 'y',
]
BW_TO_CANON = {
    '>': '>', '<': '>', '&': '>', '}': '>', "'": '>',
    'A': '>', 'Y': 'y', 'p': 'h', "`": '>',
}
LETTER_SET = set(BW_LETTERS)

# Phonotactic features
POA = {
    'b': 'labial', 'f': 'labial', 'm': 'labial', 'w': 'labial',
    't': 'coronal', 'T': 'coronal', 'd': 'coronal', 'D': 'coronal',
    's': 'coronal', 'S': 'coronal', 'z': 'coronal', 'Z': 'coronal',
    'v': 'coronal', '*': 'coronal', '$': 'coronal',
    'n': 'coronal', 'l': 'coronal', 'r': 'coronal',
    'j': 'palatal', 'y': 'palatal',
    'k': 'dorsal', 'g': 'dorsal', 'x': 'dorsal', 'q': 'dorsal',
    'H': 'guttural', 'E': 'guttural',
    'h': 'guttural', '>': 'guttural',
}
EMPHATIC = set(['S', 'D', 'T', 'Z', 'q'])

FAMILIES = [
    ('same_poa',          lambda a, b: POA[a] == POA[b]),
    ('guttural_coronal',  lambda a, b: {POA[a], POA[b]} == {'guttural', 'coronal'}),
    ('labial_dorsal',     lambda a, b: {POA[a], POA[b]} == {'labial', 'dorsal'}),
    ('emphatic_emphatic', lambda a, b: (a in EMPHATIC) and (b in EMPHATIC)),
]
POSITIONS = [(0, 1), (1, 2), (0, 2)]
CELL_LABELS = [f'{fam}_{i}-{j}' for fam, _ in FAMILIES for (i, j) in POSITIONS]


def canon_letter(c):
    c = BW_TO_CANON.get(c, c)
    return c if c in LETTER_SET else None


def canon_root(s):
    if s is None:
        return None
    letters = [canon_letter(c) for c in s]
    letters = [x for x in letters if x is not None]
    return tuple(letters) if len(letters) == 3 else None


def load_qac_roots(path):
    freq = Counter()
    with open(path, encoding='utf-8') as fh:
        for line in fh:
            if line.startswith('#') or line.startswith('LOCATION') or not line.strip():
                continue
            parts = line.rstrip('\n').split('\t')
            if len(parts) < 4:
                continue
            m = re.search(r'ROOT:([^|]+)', parts[3])
            if not m:
                continue
            ct = canon_root(m.group(1).strip())
            if ct is not None:
                freq[ct] += 1
    return freq


# ---------- Heuristic root extractor (for Mutanabbī) ----------
AR_TO_BW = {
    'ا': '>', 'أ': '>', 'إ': '>', 'آ': '>', 'ء': '>', 'ؤ': '>', 'ئ': '>',
    'ب': 'b', 'ت': 't', 'ث': 'v', 'ج': 'j', 'ح': 'H',
    'خ': 'x', 'د': 'd', 'ذ': '*', 'ر': 'r', 'ز': 'z',
    'س': 's', 'ش': '$', 'ص': 'S', 'ض': 'D', 'ط': 'T',
    'ظ': 'Z', 'ع': 'E', 'غ': 'g', 'ف': 'f', 'ق': 'q',
    'ك': 'k', 'ل': 'l', 'م': 'm', 'ن': 'n', 'ه': 'h',
    'و': 'w', 'ي': 'y', 'ى': 'y', 'ة': 'h',
}
AR_DIACRITIC_RE = re.compile(r'[\u064B-\u065F\u0670\u0640\u06D6-\u06ED]')

PREFIXES = [
    'وبال', 'فبال', 'بال', 'وال', 'فال', 'كال', 'لل', 'وس', 'فس',
    'ال', 'ول', 'فل', 'ل', 'و', 'ف', 'ب', 'ك', 'س', 'ي', 'ت', 'ن', 'ا'
]
SUFFIXES = [
    'وهما', 'كموني', 'كموها', 'تموها', 'تموهم', 'تموهن',
    'كموه', 'تموه', 'هما', 'كما', 'كن', 'كم', 'هم', 'هن', 'ها',
    'ون', 'ين', 'ان', 'ات', 'نا', 'وا', 'تم', 'تن', 'تا',
    'ت', 'ه', 'ي', 'ك', 'ا', 'ن', 'ة', 'و'
]
STOPWORDS = set([
    'من', 'في', 'على', 'إلى', 'عن', 'مع', 'هذا', 'هذه', 'ذلك', 'تلك',
    'الذي', 'التي', 'الذين', 'ما', 'لا', 'إن', 'أن', 'كان', 'كانت',
    'هو', 'هي', 'هم', 'هن', 'أنت', 'أنا', 'نحن', 'قد', 'لقد', 'لم',
    'لن', 'لو', 'إذا', 'كل', 'بعض', 'غير', 'لكن', 'و', 'ف', 'ثم',
    'أو', 'أم', 'إذ', 'حتى', 'يا', 'أيها', 'بعد', 'قبل', 'عند',
    'لدى', 'بين', 'حين', 'حيث', 'كذا', 'كذلك', 'هنا', 'هناك',
])
WORD_RE = re.compile(r'[\u0600-\u06FF]+')
WEAK_BW = set(['>', 'w', 'y'])


def normalize_ar(text):
    text = AR_DIACRITIC_RE.sub('', text)
    return text.replace('\u0640', '')


def ar_word_to_bw(word):
    return ''.join(AR_TO_BW[c] for c in word if c in AR_TO_BW)


def strip_affixes(stem):
    for p in PREFIXES:
        if stem.startswith(p) and len(stem) - len(p) >= 3:
            stem = stem[len(p):]; break
    for s in SUFFIXES:
        if stem.endswith(s) and len(stem) - len(s) >= 3:
            stem = stem[:-len(s)]; break
    return stem


def stem_to_root_trigram(stem_bw):
    if len(stem_bw) < 3:
        return None
    strong = [c for c in stem_bw if c not in WEAK_BW]
    if len(strong) == 3:
        cand = tuple(strong)
    elif len(strong) > 3:
        cand = (strong[0], strong[len(strong) // 2], strong[-1])
    else:
        if len(stem_bw) == 3:
            cand = tuple(stem_bw)
        elif len(stem_bw) > 3:
            cand = (stem_bw[0], stem_bw[len(stem_bw) // 2], stem_bw[-1])
        else:
            return None
    return cand if all(x in LETTER_SET for x in cand) else None


def extract_roots_from_text(text):
    text = normalize_ar(text)
    counts = Counter()
    total = 0
    for w in WORD_RE.findall(text):
        if w in STOPWORDS or len(w) < 3:
            continue
        bw = ar_word_to_bw(strip_affixes(w))
        root = stem_to_root_trigram(bw)
        if root is None:
            continue
        counts[root] += 1
        total += 1
    return counts, total


# ---------- Feature vectors ----------
def root_feature_row(r):
    v = np.zeros(12, dtype=np.int8)
    idx = 0
    for fam_name, pred in FAMILIES:
        for i, j in POSITIONS:
            v[idx] = 1 if pred(r[i], r[j]) else 0
            idx += 1
    return v


def root_feature_matrix(roots_iter):
    arr = np.stack([root_feature_row(r) for r in roots_iter]).astype(np.int8)
    return arr


def sha256_of(path):
    h = hashlib.sha256()
    with open(path, 'rb') as f:
        for chunk in iter(lambda: f.read(1 << 20), b''):
            h.update(chunk)
    return h.hexdigest()


# ---------- Main ----------
def main():
    log_lines = []

    def log(m):
        print(m, file=sys.stderr); log_lines.append(m)

    t0 = time.time()
    log(f'[h-new-41] seed={SEED}  N_NULL={N_NULL}  alpha_per_cell={ALPHA_PER_CELL:.3e}')

    # SHA-256 verification (41-B)
    qac_sha = sha256_of(QAC_PATH)
    mut_sha = sha256_of(MUT_PATH)
    log(f'[SHA] QAC: {qac_sha} (expected {QAC_SHA}) -> {qac_sha == QAC_SHA}')
    log(f'[SHA] Mut: {mut_sha} (expected {MUT_SHA}) -> {mut_sha == MUT_SHA}')
    if qac_sha != QAC_SHA or mut_sha != MUT_SHA:
        log('[SHA] MISMATCH — aborting per amendment 41-B lock')
        sys.exit(1)

    # Step 1: QAC roots
    qac_freq = load_qac_roots(QAC_PATH)
    Q_roots = set(qac_freq.keys())
    log(f'[step1] QAC Q roots (canonicalized triliterals): {len(Q_roots)}')

    # Step 2: Mutanabbī roots
    mut_text = MUT_PATH.read_text(encoding='utf-8', errors='ignore')
    mut_counts, mut_total = extract_roots_from_text(mut_text)
    # minfreq filter (same as prior pipeline, documented pre-data)
    MIN_FREQ = 2
    M_candidate = {r for r, ct in mut_counts.items() if ct >= MIN_FREQ}
    # Roots that are in Mutanabbī but NOT in Q (to avoid double-counting Q)
    M_only = M_candidate - Q_roots
    # The Mutanabbī set for positive-control testing (all M_candidate in C)
    M_roots = M_candidate & (Q_roots | M_only)  # = M_candidate (by construction)
    log(f'[step2] Mutanabbī candidate roots minfreq>=2: {len(M_candidate)}')
    log(f'[step2] Mutanabbī-only roots (not in Q): {len(M_only)}')

    # Classical superset C = QAC ∪ Mutanabbī-roots-only (amendment 41-B fallback)
    C_roots = Q_roots | M_only
    log(f'[step2] |Q|={len(Q_roots)}, |M_only|={len(M_only)}, |C|={len(C_roots)}')

    # Sub-question A coverage
    coverage = len(Q_roots) / len(C_roots)
    log(f'[subA] Q / C coverage = {coverage:.4f}')

    # Precompute feature matrices
    C_list = list(C_roots)
    C_idx = {r: i for i, r in enumerate(C_list)}
    C_feats = root_feature_matrix(C_list)  # (|C|, 12)
    log(f'[feat] C_feats shape={C_feats.shape}')

    # Mutanabbī-held-out C for amendment 41-A
    C_minus_M = [r for r in C_list if r not in M_candidate]
    C_minus_M_feats = root_feature_matrix(C_minus_M) if C_minus_M else np.zeros((0, 12))
    log(f'[feat] C\\M shape={C_minus_M_feats.shape}')

    # Observed feature vectors
    obs_Q = C_feats[[C_idx[r] for r in Q_roots]].mean(axis=0)
    obs_M = np.mean([root_feature_row(r) for r in M_candidate], axis=0)

    # --- Null for Q: uniform size-|Q| subsets of C ---
    rng = np.random.default_rng(SEED)
    n_C = len(C_list)
    n_Q = len(Q_roots)
    log(f'[null Q] drawing {N_NULL} size-{n_Q} uniform subsets from |C|={n_C} ...')
    null_Q = np.zeros((N_NULL, 12), dtype=np.float32)
    idx_C = np.arange(n_C)
    for b in range(N_NULL):
        sel = rng.choice(idx_C, size=n_Q, replace=False)
        null_Q[b] = C_feats[sel].mean(axis=0)

    # --- Null for M (amendment 41-A: LOO — draw from C\M) ---
    rng2 = np.random.default_rng(SEED + 1)
    n_C_minus_M = len(C_minus_M)
    n_M = len(M_candidate)
    log(f'[null M-LOO] drawing {N_NULL} size-{n_M} uniform subsets from |C\\M|={n_C_minus_M} ...')
    null_M = np.zeros((N_NULL, 12), dtype=np.float32)
    if n_C_minus_M >= n_M:
        idx_CmM = np.arange(n_C_minus_M)
        for b in range(N_NULL):
            sel = rng2.choice(idx_CmM, size=n_M, replace=False)
            null_M[b] = C_minus_M_feats[sel].mean(axis=0)
    else:
        log(f'[null M-LOO] WARNING: |C\\M|={n_C_minus_M} < |M|={n_M}; '
            'cannot draw without replacement. Drawing with replacement as fallback.')
        idx_CmM = np.arange(n_C_minus_M)
        for b in range(N_NULL):
            sel = rng2.choice(idx_CmM, size=n_M, replace=True)
            null_M[b] = C_minus_M_feats[sel].mean(axis=0)

    # --- Stats ---
    def two_sided_p(obs, null_col):
        m = null_col.mean()
        dev_obs = abs(obs - m)
        return (np.sum(np.abs(null_col - m) >= dev_obs) + 1) / (len(null_col) + 1)

    def zscore(obs, null_col):
        mu = null_col.mean(); sd = null_col.std(ddof=1)
        return (obs - mu) / sd if sd > 0 else 0.0

    cells = []
    for k in range(12):
        cells.append({
            'cell': CELL_LABELS[k],
            'obs_Q': float(obs_Q[k]),
            'obs_M': float(obs_M[k]),
            'null_Q_mean': float(null_Q[:, k].mean()),
            'null_Q_sd':   float(null_Q[:, k].std(ddof=1)),
            'null_M_mean_LOO': float(null_M[:, k].mean()),
            'null_M_sd_LOO':   float(null_M[:, k].std(ddof=1)),
            'z_Q': float(zscore(obs_Q[k], null_Q[:, k])),
            'p_Q': float(two_sided_p(obs_Q[k], null_Q[:, k])),
            'z_M_LOO': float(zscore(obs_M[k], null_M[:, k])),
            'p_M_LOO': float(two_sided_p(obs_M[k], null_M[:, k])),
        })
    for c in cells:
        c['significant_Q_at_alpha'] = bool(c['p_Q'] < ALPHA_PER_CELL)
        c['posctrl_cell_fail'] = bool(abs(c['z_M_LOO']) >= 2.0)

    # --- MW-5 gate per amendment 41-A ---
    fail_cells = [c for c in cells if c['posctrl_cell_fail']]
    n_posctrl_fail = len(fail_cells)
    worst_abs_z_M = max(abs(c['z_M_LOO']) for c in cells)
    log(f'[MW-5 41-A] posctrl cells failing (|z|>=2): {n_posctrl_fail}/12, '
        f'worst |z_M|={worst_abs_z_M:.3f}')

    n_sig = sum(1 for c in cells if c['significant_Q_at_alpha'])
    log(f'[verdict raw] Q significant cells = {n_sig}/12 at alpha={ALPHA_PER_CELL:.3e}')

    # Amendment 41-A verdict logic:
    # FAIL any -> NULL-BROKEN (full 12) -- ambiguous; the amendment text:
    #   "PASS criterion: for all 12 cells, |z_M| < 2.0.
    #    FAIL criterion (NULL-BROKEN): any cell with |z_M| >= 2.0. Any
    #    intermediate cell count (1-11) is reported as PARTIAL-POSITIVE-CONTROL
    #    and the Quran claim is downgraded to EXPLORATORY."
    # Interpretation: "FAIL criterion: any cell >=2.0" literally catches all
    # n_posctrl_fail>=1 cases. But then "intermediate 1-11" is also "any cell".
    # The coherent reading: PASS iff n=0; intermediate iff 1<=n<=11 (downgrade);
    # NULL-BROKEN iff n=12. We adopt this reading and document it in the garden.
    if n_posctrl_fail == 0:
        # Clean positive control — apply original verdict table to Q
        if n_sig == 0:
            verdict = 'NULL'
        elif n_sig == 1:
            verdict = 'EXPLORATORY-hit'
        elif 2 <= n_sig <= 5:
            verdict = 'PARTIAL-PASS'
        else:
            verdict = 'STRONG-PASS'
    elif n_posctrl_fail == 12:
        verdict = 'NULL-BROKEN'
    else:
        # 1-11: PARTIAL-POSITIVE-CONTROL — Quran downgraded to EXPLORATORY
        # (only promote to EXPLORATORY if Q has any signal, else NULL)
        if n_sig == 0:
            verdict = 'NULL (partial-posctrl)'
        else:
            verdict = 'EXPLORATORY (partial-posctrl downgrade)'

    log(f'[verdict] >>> {verdict} <<<')

    # Token-weighted (MW-1)
    weighted_Q = np.zeros(12, dtype=np.float64)
    for r, w in qac_freq.items():
        if r in C_idx:
            weighted_Q += w * C_feats[C_idx[r]].astype(np.float64)
    weighted_Q /= sum(qac_freq.values())
    for k in range(12):
        cells[k]['obs_Q_token_weighted'] = float(weighted_Q[k])
        cells[k]['z_Q_token_weighted'] = float(zscore(weighted_Q[k], null_Q[:, k]))

    # Sub-question C (descriptive)
    letters_list = sorted(LETTER_SET)
    uniform_feat = np.zeros(12)
    idx_ = 0
    for fam_name, pred in FAMILIES:
        for i, j in POSITIONS:
            ct = sum(1 for a in letters_list for b in letters_list if pred(a, b))
            uniform_feat[idx_] = ct / (len(letters_list) ** 2)
            idx_ += 1

    subC = []
    for k in range(12):
        subC.append({
            'cell': CELL_LABELS[k],
            'uniform_28cubed': float(uniform_feat[k]),
            'C_mean': float(null_Q[:, k].mean()),  # null-subset mean ~ C mean
            'Q_obs': float(obs_Q[k]),
            'M_obs': float(obs_M[k]),
            'delta_Q_vs_uniform': float(obs_Q[k] - uniform_feat[k]),
            'delta_C_vs_uniform': float(null_Q[:, k].mean() - uniform_feat[k]),
        })

    # --- Write output ---
    out = {
        'id': 'H-NEW-41',
        'seed': SEED,
        'n_null': N_NULL,
        'alpha_per_cell': ALPHA_PER_CELL,
        'alpha_bon_outer': ALPHA_BON_OUTER,
        'bonferroni_family': '2026-04-15-Fresh-Wave-3',
        'bonferroni_k': 3,
        'amendments_applied': ['41-A (LOO posctrl)', '41-B (SHA-256 lock, fallback C)'],
        'source_files_sha256': {
            'qac': {'path': str(QAC_PATH), 'sha256': qac_sha, 'match': qac_sha == QAC_SHA},
            'mutanabbi': {'path': str(MUT_PATH), 'sha256': mut_sha, 'match': mut_sha == MUT_SHA},
            'lane': None,
            'wehr': None,
        },
        'rules_tuple': [
            'no-tashkeel', 'orthographic-token & lemma where noted',
            'graphemes', 'basmala-counted-only-in-surah-1',
            'hafs-kufan', 'mashriqi',
        ],
        'data_inventory': {
            'qac_Q_roots': len(Q_roots),
            'mutanabbi_candidate_roots_minfreq2': len(M_candidate),
            'mutanabbi_only_roots_not_in_Q': len(M_only),
            'classical_C_roots': len(C_roots),
            'classical_C_minus_M': len(C_minus_M),
            'coverage_Q_over_C': coverage,
            'mutanabbi_total_tokens': mut_total,
            'U_never_attested_estimate': 28**3 - len(C_roots),
        },
        'cells': cells,
        'subQ_C_zero_attest': subC,
        'posctrl_LOO_worst_abs_z_M': worst_abs_z_M,
        'posctrl_LOO_n_cells_failing': n_posctrl_fail,
        'n_significant_cells_Q': n_sig,
        'verdict': verdict,
        'wall_seconds': time.time() - t0,
        'gardens_of_forking_paths': [
            'Amendment 41-A (LOO posctrl) and 41-B (SHA-256 lock + fallback C='
            'QAC ∪ Mutanabbī-only) were filed by audit-032 AFTER an initial, '
            'broader-C run had been executed by this agent. That prior run '
            'result was viewed. The amendments are tightening-only and are '
            'applied exactly as written here; the prior-run result is '
            'preserved in journal/h-new-41-run-1-prior-to-amendments.log but '
            'is NOT used to adjudicate this verdict.',
            'Amendment 41-A verdict-text interpretation: "FAIL criterion: any '
            'cell >=2.0 -> NULL-BROKEN" and "intermediate 1-11 -> '
            'PARTIAL-POSITIVE-CONTROL" are literally inconsistent (the set '
            '{1..11} is a subset of "any cell >=2.0"). Coherent reading '
            'adopted: PASS iff n=0; intermediate iff 1<=n<=11 (downgrade Q to '
            'EXPLORATORY); NULL-BROKEN iff n=12. This reading preserves the '
            'existence of the PARTIAL-POSITIVE-CONTROL tier. Recorded here '
            'pre-data-viewing of this run.',
            '28-letter canonicalization: alif variants, hamza seats, and '
            "alif-maqsura fold into a single 28-set per QAC conventions. "
            'Applied identically to Q, M, and C.',
            'Stemmer minfreq=2 (non-Q extracted roots only) carried over from '
            'prior run. This is conservative (reduces stemmer noise).',
            '12-cell feature family locked per pre-reg: 4 POA predicates × 3 '
            'position pairs. No expansions.',
        ],
    }
    csv_dir = ROOT / 'findings/phase-b-hypotheses/csv'
    csv_dir.mkdir(parents=True, exist_ok=True)
    outp = csv_dir / 'h-new-41.json'
    outp.write_text(json.dumps(out, indent=2))
    log(f'[out] wrote {outp}')

    (csv_dir / 'h-new-41-rootlists.json').write_text(json.dumps({
        'qac_roots_sorted': sorted(''.join(r) for r in Q_roots),
        'mutanabbi_only_roots_sorted': sorted(''.join(r) for r in M_only),
    }, indent=2))

    (ROOT / 'journal/h-new-41-run-1.log').write_text('\n'.join(log_lines))
    return out


if __name__ == '__main__':
    main()
