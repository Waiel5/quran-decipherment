#!/usr/bin/env python3
"""H-META-1 retrained with MW-6 verbatim-confidence tier as added feature.

Implements Option A from team-lead's MW-6 moderator acceptance message
(2026-04-13). Tests two pre-registered predictions locked in
findings/cross-finding/h-meta-1-mw6-prereg.md:

  P1: Adding MW-6 tier improves LR L1 5-fold CV accuracy by >= 1 pp
      over baseline 0.7820.
  P2: The full-data L1 coefficient on mw6_tier=VERIFIED is negative.

Protocol: identical to scripts/h_meta_1_classifier.py except for the added
mw6_tier one-hot feature. Same seed (20260413), same B=500 perms, same
Bonferroni (k=2, alpha_per_test=0.025), same lambda (0.05).
"""

import json
import math
import random
import re
import time
from collections import Counter
from pathlib import Path

ROOT = Path('/Users/grey/Downloads/quran')
SEED = 20260413
rng = random.Random(SEED)

TSV = ROOT / 'findings/phase-c-structures/h-meta-1-corpus-120.tsv'
PREREG = ROOT / 'findings/cross-finding/h-meta-1-mw6-prereg.md'
BASELINE_LR_ACC = 0.7819855072463768  # from h-meta-1-classifier.json
P1_THRESHOLD = BASELINE_LR_ACC + 0.01

# ---- Parse corpus ----
TIER_RE = re.compile(r'\[([^]]+)\]')

def normalize_tier(raw):
    parts = raw.strip().split()
    if not parts:
        return 'UNTAGGED'
    head = parts[0]
    if head == 'SECONDARY-TRIANGULATED':
        return 'SECONDARY-TRIANGULATED'
    return head

rows = []
with TSV.open() as f:
    header = None
    for line in f:
        line = line.rstrip('\n')
        if not line or line.startswith('#'):
            continue
        if line.startswith('claim_id\t'):
            header = line.split('\t')
            continue
        if header is None:
            continue
        parts = line.split('\t')
        if len(parts) != len(header):
            continue
        row = dict(zip(header, parts))
        m = TIER_RE.search(row['claim_source'])
        row['mw6_tier'] = normalize_tier(m.group(1)) if m else 'UNTAGGED'
        rows.append(row)

print(f"parsed {len(rows)} claims")
print(f"verdict distribution: {Counter(r['empirical_verdict'] for r in rows)}")
print(f"mw6_tier distribution: {Counter(r['mw6_tier'] for r in rows)}")

rows = [r for r in rows if r['empirical_verdict'] in {'CONFIRMED', 'REFUTED'}]
print(f"after filter: {len(rows)} binary-label claims")
print(f"class balance: {Counter(r['empirical_verdict'] for r in rows)}")
print(f"mw6_tier × verdict cross-tab:")
ct = Counter((r['mw6_tier'], r['empirical_verdict']) for r in rows)
for k, v in sorted(ct.items()):
    print(f"  {k}: {v}")

# ---- Feature encoding (mirrors baseline + mw6_tier) ----
CAT_FEATURES = ['era', 'genre', 'school', 'claim_type', 'unit', 'scope', 'substance_type', 'mw6_tier']
BOOL_FEATURES = ['broad_hisab_claim']
NUM_FEATURES = ['specificity']

def build_levels(rows):
    return {f: sorted({r[f] for r in rows}) for f in CAT_FEATURES}

levels = build_levels(rows)
print("\nCategorical levels:")
for f, vv in levels.items():
    print(f"  {f}: {len(vv)} — {vv}")

def featurize(r, levels):
    x = []
    names = []
    for f in CAT_FEATURES:
        for v in levels[f]:
            x.append(1.0 if r[f] == v else 0.0)
            names.append(f'{f}={v}')
    for f in BOOL_FEATURES:
        x.append(1.0 if r[f].strip().upper() == 'TRUE' else 0.0)
        names.append(f)
    for f in NUM_FEATURES:
        try:
            x.append(float(r[f]))
        except ValueError:
            x.append(0.0)
        names.append(f)
    return x, names

X = []
y = []
feature_names = None
for r in rows:
    x, nm = featurize(r, levels)
    X.append(x)
    y.append(1 if r['empirical_verdict'] == 'CONFIRMED' else 0)
    if feature_names is None:
        feature_names = nm

N = len(X)
P = len(feature_names)
print(f"\nfeature matrix: N={N}, P={P} (baseline P was 38; delta = {P-38})")

# ---- Manual L1 logistic regression (proximal gradient) ----
def sigmoid(z):
    if z >= 0:
        ez = math.exp(-z)
        return 1.0 / (1.0 + ez)
    ez = math.exp(z)
    return ez / (1.0 + ez)

def logistic_loss_grad(X, y, w, lam):
    n = len(X)
    p = len(w)
    g = [0.0] * p
    loss = 0.0
    for i in range(n):
        z = sum(X[i][j] * w[j] for j in range(p))
        p_i = sigmoid(z)
        err = p_i - y[i]
        for j in range(p):
            g[j] += err * X[i][j]
        if y[i] == 1:
            loss -= math.log(p_i + 1e-12)
        else:
            loss -= math.log(1.0 - p_i + 1e-12)
    return loss / n, [gj / n for gj in g]

def prox_l1(w, lam_step):
    out = []
    for wi in w:
        if wi > lam_step:
            out.append(wi - lam_step)
        elif wi < -lam_step:
            out.append(wi + lam_step)
        else:
            out.append(0.0)
    return out

def train_lr_l1(X, y, lam=0.05, lr=0.3, n_iter=200):
    p = len(X[0])
    w = [0.0] * p
    for _ in range(n_iter):
        _, g = logistic_loss_grad(X, y, w, lam)
        w = [w[j] - lr * g[j] for j in range(p)]
        w = prox_l1(w, lr * lam)
    return w

def predict(X, w):
    return [1 if sigmoid(sum(x[j] * w[j] for j in range(len(w)))) >= 0.5 else 0 for x in X]

# ---- Shallow tree (depth-3, Gini) ----
def gini(labels):
    n = len(labels)
    if n == 0:
        return 0
    p1 = sum(labels) / n
    p0 = 1 - p1
    return 1 - p1 * p1 - p0 * p0

def best_split(X, y, feat_idx):
    n = len(X)
    best = None
    for j in feat_idx:
        vals = sorted({X[i][j] for i in range(n)})
        for t_i in range(len(vals) - 1):
            threshold = (vals[t_i] + vals[t_i + 1]) / 2
            left_y = [y[i] for i in range(n) if X[i][j] <= threshold]
            right_y = [y[i] for i in range(n) if X[i][j] > threshold]
            if not left_y or not right_y:
                continue
            gain = gini(y) - (len(left_y) / n) * gini(left_y) - (len(right_y) / n) * gini(right_y)
            if best is None or gain > best[0]:
                best = (gain, j, threshold)
    return best

def build_tree(X, y, feat_idx, depth, max_depth=3, min_samples=4):
    n = len(X)
    if n < min_samples or depth >= max_depth or len(set(y)) == 1:
        return {'leaf': True, 'pred': 1 if sum(y) > n / 2 else 0, 'n': n}
    sp = best_split(X, y, feat_idx)
    if sp is None or sp[0] <= 0:
        return {'leaf': True, 'pred': 1 if sum(y) > n / 2 else 0, 'n': n}
    gain, j, t = sp
    left_idx = [i for i in range(n) if X[i][j] <= t]
    right_idx = [i for i in range(n) if X[i][j] > t]
    return {
        'leaf': False, 'feat': j, 'threshold': t, 'gain': gain,
        'left': build_tree([X[i] for i in left_idx], [y[i] for i in left_idx],
                           feat_idx, depth + 1, max_depth, min_samples),
        'right': build_tree([X[i] for i in right_idx], [y[i] for i in right_idx],
                            feat_idx, depth + 1, max_depth, min_samples),
    }

def tree_predict_one(tree, x):
    if tree['leaf']:
        return tree['pred']
    if x[tree['feat']] <= tree['threshold']:
        return tree_predict_one(tree['left'], x)
    return tree_predict_one(tree['right'], x)

def tree_predict(tree, X):
    return [tree_predict_one(tree, x) for x in X]

# ---- Stratified 5-fold CV ----
def stratified_folds(y, n_folds=5, seed=SEED):
    r = random.Random(seed)
    idx_by_cls = {c: [i for i, yi in enumerate(y) if yi == c] for c in set(y)}
    for c in idx_by_cls:
        r.shuffle(idx_by_cls[c])
    folds = [[] for _ in range(n_folds)]
    for c, idxs in idx_by_cls.items():
        for k, i in enumerate(idxs):
            folds[k % n_folds].append(i)
    return folds

def cv_accuracy(X, y, model_fn, n_folds=5, **kw):
    folds = stratified_folds(y, n_folds)
    accs = []
    for k in range(n_folds):
        test_idx = set(folds[k])
        Xtr = [X[i] for i in range(len(X)) if i not in test_idx]
        ytr = [y[i] for i in range(len(y)) if i not in test_idx]
        Xte = [X[i] for i in sorted(test_idx)]
        yte = [y[i] for i in sorted(test_idx)]
        preds = model_fn(Xtr, ytr, Xte, **kw)
        accs.append(sum(1 for p, t in zip(preds, yte) if p == t) / len(yte))
    return sum(accs) / len(accs), accs

def model_lr(Xtr, ytr, Xte, lam=0.05):
    w = train_lr_l1(Xtr, ytr, lam=lam)
    return predict(Xte, w)

def model_tree(Xtr, ytr, Xte, max_depth=3):
    feat_idx = list(range(len(Xtr[0])))
    t = build_tree(Xtr, ytr, feat_idx, 0, max_depth=max_depth)
    return tree_predict(t, Xte)

# ---- Main runs ----
print("\n=== Main CV runs (with mw6_tier feature) ===")
acc_lr, accs_lr_folds = cv_accuracy(X, y, model_lr, n_folds=5, lam=0.05)
print(f"LR L1 5-fold accuracy: {acc_lr:.4f} (folds: {[f'{a:.3f}' for a in accs_lr_folds]})")

acc_tree, accs_tree_folds = cv_accuracy(X, y, model_tree, n_folds=5, max_depth=3)
print(f"Shallow tree (d=3) 5-fold accuracy: {acc_tree:.4f} (folds: {[f'{a:.3f}' for a in accs_tree_folds]})")

# ---- Pre-registered prediction P1 evaluation ----
delta_lr = acc_lr - BASELINE_LR_ACC
p1_hit = acc_lr >= P1_THRESHOLD
print(f"\n=== Pre-registered P1 evaluation ===")
print(f"  Baseline LR L1 accuracy:    {BASELINE_LR_ACC:.4f}")
print(f"  Retrained LR L1 accuracy:   {acc_lr:.4f}")
print(f"  Delta:                      {delta_lr:+.4f}")
print(f"  P1 threshold (>= +0.01):    {P1_THRESHOLD:.4f}")
print(f"  P1 result:                  {'HIT' if p1_hit else 'MISS'}")

# ---- Label-permutation null ceiling ----
print("\n=== Label-permutation null (B=500) ===")
null_lr = []
null_tree = []
B = 500
t0 = time.time()
for b in range(B):
    y_perm = list(y)
    rng.shuffle(y_perm)
    a1, _ = cv_accuracy(X, y_perm, model_lr, n_folds=5, lam=0.05)
    null_lr.append(a1)
    a2, _ = cv_accuracy(X, y_perm, model_tree, n_folds=5, max_depth=3)
    null_tree.append(a2)
    if (b + 1) % 25 == 0:
        elapsed = time.time() - t0
        rate = (b + 1) / elapsed
        eta = (B - b - 1) / rate
        print(f"  perm {b+1}/{B}: LR={a1:.3f}, tree={a2:.3f}  ({rate:.2f} perm/s, ETA {eta:.0f}s)", flush=True)

null_lr.sort()
null_tree.sort()

def empirical_p(observed, null_list):
    n = len(null_list)
    return sum(1 for x in null_list if x >= observed) / n

p_lr = empirical_p(acc_lr, null_lr)
p_tree = empirical_p(acc_tree, null_tree)
alpha_bon = 0.025
sig_lr = p_lr < alpha_bon
sig_tree = p_tree < alpha_bon

print(f"\nLR L1: observed {acc_lr:.4f}, null mean {sum(null_lr)/B:.4f}, "
      f"null 97.5%ile {null_lr[int(0.975*B)]:.4f}, p_emp={p_lr:.4f}, sig@0.025={sig_lr}")
print(f"Tree:   observed {acc_tree:.4f}, null mean {sum(null_tree)/B:.4f}, "
      f"null 97.5%ile {null_tree[int(0.975*B)]:.4f}, p_emp={p_tree:.4f}, sig@0.025={sig_tree}")

# ---- Full-data LR coefficients for P2 evaluation ----
w_full = train_lr_l1(X, y, lam=0.05)
print(f"\n=== Pre-registered P2 evaluation ===")
mw6_indices = {feature_names[i]: (i, w_full[i]) for i in range(len(feature_names))
               if feature_names[i].startswith('mw6_tier=')}
for name, (idx, w) in sorted(mw6_indices.items()):
    print(f"  {name:35s} weight = {w:+.4f}")

verified_w = mw6_indices.get('mw6_tier=VERIFIED', (None, 0.0))[1]
print(f"\n  mw6_tier=VERIFIED coefficient: {verified_w:+.4f}")
if abs(verified_w) < 1e-6:
    p2_result = 'MISS-zero (L1 absorbed; collinear with substance_type or specificity)'
elif verified_w < 0:
    p2_result = 'HIT (negative, consistent with moderator finding)'
else:
    p2_result = 'MISS-positive (sign reversal vs moderator finding)'
print(f"  P2 result: {p2_result}")

# ---- Top features ----
top_features = sorted(enumerate(w_full), key=lambda kv: -abs(kv[1]))[:25]
print(f"\nTop 25 LR features by |weight|:")
for j, wj in top_features:
    if abs(wj) > 1e-6:
        print(f"  {feature_names[j]:45s} {wj:+.4f}")

# ---- Verdict per acceptance rule ----
if max(acc_lr, acc_tree) > 0.70:
    verdict = 'PASS'
elif max(acc_lr, acc_tree) < 0.60:
    verdict = 'NO-SIGNATURE (honest NULL)'
else:
    verdict = 'WEAK-SIGNAL'
print(f"\n=== VERDICT (within-Option-A): {verdict} ===")

# ---- Decision matrix routing ----
if p1_hit and verified_w < 0 and abs(verified_w) > 1e-6:
    matrix_cell = 'P1=HIT, P2=HIT(negative) → STRONG CONFIRMATION'
elif p1_hit and verified_w > 0 and abs(verified_w) > 1e-6:
    matrix_cell = 'P1=HIT, P2=MISS(positive) → INVESTIGATION TRIGGERED (sign reversal)'
elif p1_hit and abs(verified_w) < 1e-6:
    matrix_cell = 'P1=HIT, P2=MISS(zero) → PARTIAL CONFIRMATION (L1 absorbed VERIFIED via collinearity)'
elif (not p1_hit) and verified_w < 0 and abs(verified_w) > 1e-6:
    matrix_cell = 'P1=MISS, P2=HIT(negative) → PROCEDURAL-ONLY (moderator-real but classifier-irrelevant)'
elif (not p1_hit) and verified_w > 0 and abs(verified_w) > 1e-6:
    matrix_cell = 'P1=MISS, P2=MISS(positive) → STRONG REFUTATION of classifier propagation'
else:
    matrix_cell = 'P1=MISS, P2=MISS(zero) → BOOKKEEPING-ONLY'

print(f"\nDECISION MATRIX CELL: {matrix_cell}")

# ---- Output JSON ----
out = {
    'seed': SEED,
    'task_id': 132,
    'option': 'A',
    'parent_finding': 'mw6-reliability-moderator',
    'pre_registration': str(PREREG.relative_to(ROOT)),
    'corpus': str(TSV.relative_to(ROOT)),
    'N': N,
    'P_baseline': 38,
    'P_with_mw6': P,
    'P_delta': P - 38,
    'mw6_tier_levels': levels['mw6_tier'],
    'mw6_tier_counts': dict(Counter(r['mw6_tier'] for r in rows)),
    'class_balance': dict(Counter(r['empirical_verdict'] for r in rows)),
    'baseline_lr_l1_accuracy': BASELINE_LR_ACC,
    'p1_threshold': P1_THRESHOLD,
    'lr_l1': {
        'mean_acc': acc_lr,
        'fold_accs': accs_lr_folds,
        'null_mean': sum(null_lr) / B,
        'null_975pct': null_lr[int(0.975 * B)],
        'null_95pct': null_lr[int(0.95 * B)],
        'p_empirical': p_lr,
        'significant_alpha0025': sig_lr,
        'lam': 0.05,
        'delta_vs_baseline': delta_lr,
        'p1_hit': p1_hit,
    },
    'tree_d3': {
        'mean_acc': acc_tree,
        'fold_accs': accs_tree_folds,
        'null_mean': sum(null_tree) / B,
        'null_975pct': null_tree[int(0.975 * B)],
        'null_95pct': null_tree[int(0.95 * B)],
        'p_empirical': p_tree,
        'significant_alpha0025': sig_tree,
    },
    'mw6_tier_coefficients': {name: w for name, (_, w) in mw6_indices.items()},
    'p2_evaluation': {
        'verified_coefficient': verified_w,
        'result': p2_result,
    },
    'decision_matrix_cell': matrix_cell,
    'top_lr_features': [
        {'feature': feature_names[j], 'weight': wj}
        for j, wj in top_features if abs(wj) > 1e-6
    ],
    'bonferroni': {'k': 2, 'alpha_family': 0.05, 'alpha_bon': 0.025},
    'acceptance_rule': {'pass_threshold': 0.70, 'no_signature_floor': 0.60},
    'verdict_within_option_a': verdict,
}

outp = ROOT / 'findings/cross-finding/csv/h-meta-1-mw6-retrained.json'
outp.parent.mkdir(parents=True, exist_ok=True)
outp.write_text(json.dumps(out, indent=2, default=str))
print(f"\nsaved: {outp}")
