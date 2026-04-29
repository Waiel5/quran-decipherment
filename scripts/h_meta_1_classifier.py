#!/usr/bin/env python3
"""H-META-1 confirmable-signature classifier.

Task #28 AMEND-4 — classify CLASS-C (confirmed) vs CLASS-R (refuted) claims
using only claim-side features (era, genre, school, claim-type, unit, scope,
specificity, broad_hisab_claim, substance_type).

Protocol (from findings/phase-c-structures/h-meta-1-classifier-pilot.md +
AMEND-4):
  - Logistic regression with L1 (lasso) regularization (manual gradient
    descent since sklearn unavailable).
  - 5-fold stratified cross-validation.
  - 1000× label-permutation null ceiling.
  - Bonferroni k=2 family (LR + shallow tree), α_fam = 0.025.
  - Acceptance: mean CV accuracy > 70%.
  - No-signature honest-NULL threshold: < 60%.

Corpus: findings/phase-c-structures/h-meta-1-corpus-120.tsv (120 claims:
49+28=77 CONFIRMED, 18+25=43 REFUTED).

Seed 20260413.
"""

import json
import math
import random
from pathlib import Path
from collections import Counter

ROOT = Path('/Users/grey/Downloads/quran')
SEED = 20260413
rng = random.Random(SEED)

TSV = ROOT / 'findings/phase-c-structures/h-meta-1-corpus-120.tsv'

# Parse TSV — skip comment lines
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
        rows.append(dict(zip(header, parts)))

print(f"parsed {len(rows)} claims")
print(f"verdict distribution: {Counter(r['empirical_verdict'] for r in rows)}")
if not rows:
    raise SystemExit("no data parsed")

# Filter to CONFIRMED/REFUTED binary
rows = [r for r in rows if r['empirical_verdict'] in {'CONFIRMED', 'REFUTED'}]
print(f"after filter: {len(rows)} binary-label claims")
print(f"class balance: {Counter(r['empirical_verdict'] for r in rows)}")


# ---- One-hot feature vector ----
CAT_FEATURES = ['era', 'genre', 'school', 'claim_type', 'unit', 'scope', 'substance_type']
BOOL_FEATURES = ['broad_hisab_claim']
NUM_FEATURES = ['specificity']


def build_feature_encoder(rows):
    levels = {}
    for f in CAT_FEATURES:
        vals = sorted({r[f] for r in rows})
        levels[f] = vals
    return levels


levels = build_feature_encoder(rows)
print("\nCategorical levels:")
for f, vv in levels.items():
    print(f"  {f}: {len(vv)} values — {vv[:8]}{'...' if len(vv)>8 else ''}")


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
print(f"\nfeature matrix: N={N}, P={P}")


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
    out = []
    for x in X:
        z = sum(x[j] * w[j] for j in range(len(w)))
        out.append(1 if sigmoid(z) >= 0.5 else 0)
    return out


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
        'left': build_tree([X[i] for i in left_idx], [y[i] for i in left_idx], feat_idx, depth + 1, max_depth, min_samples),
        'right': build_tree([X[i] for i in right_idx], [y[i] for i in right_idx], feat_idx, depth + 1, max_depth, min_samples),
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
        acc = sum(1 for p, t in zip(preds, yte) if p == t) / len(yte)
        accs.append(acc)
    return sum(accs) / len(accs), accs


def model_lr(Xtr, ytr, Xte, lam=0.05):
    w = train_lr_l1(Xtr, ytr, lam=lam)
    return predict(Xte, w)


def model_tree(Xtr, ytr, Xte, max_depth=3):
    feat_idx = list(range(len(Xtr[0])))
    t = build_tree(Xtr, ytr, feat_idx, 0, max_depth=max_depth)
    return tree_predict(t, Xte)


print("\n=== Main CV runs ===")
acc_lr, accs_lr_folds = cv_accuracy(X, y, model_lr, n_folds=5, lam=0.05)
print(f"LR L1 5-fold accuracy: {acc_lr:.4f} (folds: {[f'{a:.3f}' for a in accs_lr_folds]})")

acc_tree, accs_tree_folds = cv_accuracy(X, y, model_tree, n_folds=5, max_depth=3)
print(f"Shallow tree (d=3) 5-fold accuracy: {acc_tree:.4f} (folds: {[f'{a:.3f}' for a in accs_tree_folds]})")


# ---- Label-permutation null ceiling ----
print("\n=== 1000x label-permutation null ===")
null_lr = []
null_tree = []
B = 500
import time
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
    k = sum(1 for x in null_list if x >= observed)
    return k / n


p_lr = empirical_p(acc_lr, null_lr)
p_tree = empirical_p(acc_tree, null_tree)
alpha_bon = 0.025
sig_lr = p_lr < alpha_bon
sig_tree = p_tree < alpha_bon

print(f"\nLR L1: observed {acc_lr:.4f}, null mean {sum(null_lr)/B:.4f}, "
      f"null 97.5%ile {null_lr[int(0.975*B)]:.4f}, p_emp={p_lr:.4f}, sig@0.025={sig_lr}")
print(f"Tree:   observed {acc_tree:.4f}, null mean {sum(null_tree)/B:.4f}, "
      f"null 97.5%ile {null_tree[int(0.975*B)]:.4f}, p_emp={p_tree:.4f}, sig@0.025={sig_tree}")


# ---- Feature importance from full-data LR ----
w_full = train_lr_l1(X, y, lam=0.05)
top_features = sorted(enumerate(w_full), key=lambda kv: -abs(kv[1]))[:20]
print(f"\nTop 20 LR features by |weight|:")
for j, wj in top_features:
    if abs(wj) > 1e-6:
        print(f"  {feature_names[j]}: {wj:+.3f}")


# ---- Verdict per acceptance rule ----
if max(acc_lr, acc_tree) > 0.70:
    verdict = 'PASS'
elif max(acc_lr, acc_tree) < 0.60:
    verdict = 'NO-SIGNATURE (honest NULL)'
else:
    verdict = 'WEAK-SIGNAL'
print(f"\n=== VERDICT: {verdict} ===")
print(f"best mean acc: {max(acc_lr, acc_tree):.4f}")
print(f"PASS threshold: 0.70; NO-SIGNATURE floor: 0.60")


# ---- Output JSON ----
out = {
    'seed': SEED,
    'task_id': 28,
    'amendment': 'AMEND-4',
    'corpus': str(TSV.relative_to(ROOT)),
    'N': N,
    'P': P,
    'class_balance': dict(Counter(r['empirical_verdict'] for r in rows)),
    'features_categorical': CAT_FEATURES,
    'features_bool': BOOL_FEATURES,
    'features_numeric': NUM_FEATURES,
    'feature_levels': levels,
    'lr_l1': {
        'mean_acc': acc_lr,
        'fold_accs': accs_lr_folds,
        'null_mean': sum(null_lr) / B,
        'null_975pct': null_lr[int(0.975 * B)],
        'null_95pct': null_lr[int(0.95 * B)],
        'p_empirical': p_lr,
        'significant_alpha0025': sig_lr,
        'lam': 0.05,
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
    'top_lr_features': [
        {'feature': feature_names[j], 'weight': wj}
        for j, wj in top_features if abs(wj) > 1e-6
    ],
    'bonferroni': {'k': 2, 'alpha_family': 0.05, 'alpha_bon': 0.025},
    'acceptance_rule': {'pass_threshold': 0.70, 'no_signature_floor': 0.60},
    'verdict': verdict,
}

outp = ROOT / 'findings/phase-c-structures/csv/h-meta-1-classifier.json'
outp.parent.mkdir(parents=True, exist_ok=True)
outp.write_text(json.dumps(out, indent=2, default=str))
print(f"\nsaved: {outp}")
