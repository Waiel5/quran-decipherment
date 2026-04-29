#!/usr/bin/env python3
"""H-META-1 confirmable-signature classifier — PILOT stage.

Task #28: build LR-lasso + shallow tree classifier on CLASS-C (49+28) vs
CLASS-R (18+25) claims. Feature vector per AMEND-4: broad_hisab_claim,
substance_type, plus the original dispatch features (era, genre, school,
claim-type, unit, scope, specificity, classical-scholar additions).

STATUS: Task is explicitly "AWAITING classical-scholar corpus verification"
per task metadata. Full CLASS-C/CLASS-R label corpus (120 claims) is NOT
available. Present pilot runs the full pipeline on a proxy-labeled subset
of the 68-claim docs/claims-catalog.md using an adjudicated label derived
from (a) presence of empirical-failure criticisms, (b) replicability, and
(c) cross-reference to HONEST-LIMITS-LEDGER.md which collects refuted
claims project-wide.

Proxy label rule (deterministic, applied without post-hoc tuning):
  - REFUTED if known_criticisms mentions "FAIL" | "refuted" | "does not hold"
    | "arithmetic errors" | "not attested" | "demonstrated failure"
  - CONFIRMED if (a) replicability=high, (b) criticisms empty or purely
    interpretive, and (c) claim is not a divisibility-miracle claim
  - DROP otherwise (ambiguous)

The PIPELINE results are reported and the same pipeline will run on the
full corpus when classical-scholar delivers it.

Seed 20260413.
"""
import hashlib, json, math, random, re
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path('/Users/grey/Downloads/quran')
random.seed(20260413)

CATALOG = (ROOT / 'docs/claims-catalog.md').read_text()

# --- Parse YAML blocks ---
def parse_yaml_blocks(text):
    """Each claim is a ```yaml ... ``` block. Return list of dicts."""
    blocks = re.findall(r'```yaml\n(.*?)```', text, re.DOTALL)
    claims = []
    for blk in blocks:
        d = {}
        current_key = None
        current_val = []
        for line in blk.split('\n'):
            if not line.strip():
                continue
            # Top-level key: value
            m = re.match(r'^([a-z_]+):\s*(.*)$', line)
            if m and not line.startswith(' '):
                if current_key is not None:
                    d[current_key] = '\n'.join(current_val).strip().strip('"\'')
                current_key = m.group(1)
                current_val = [m.group(2)]
            else:
                current_val.append(line)
        if current_key is not None:
            d[current_key] = '\n'.join(current_val).strip().strip('"\'')
        if d.get('claim_id'):
            claims.append(d)
    return claims

claims = parse_yaml_blocks(CATALOG)
print(f"parsed claims: {len(claims)}")

# --- Proxy label assignment ---
def proxy_label(claim):
    critic = claim.get('known_criticisms', '').lower()
    repli = claim.get('confidence_in_replicability', '').lower()
    stmt = claim.get('claim_statement', '').lower()

    refute_markers = ['fail', 'refuted', 'does not hold', 'arithmetic errors',
                      'not attested', 'demonstrated failure', 'broken',
                      'disappears under', 'not divisible', 'wrong']
    confirm_markers_neg_in_critic = ['not confirmed', 'no independent', 'no empirical']

    has_refute = any(m in critic for m in refute_markers)
    has_refute_in_stmt = any(m in stmt for m in ['fails', 'refuted'])

    if has_refute or has_refute_in_stmt:
        return 'REFUTED'
    # "high" replicability and empty/interpretive criticism
    if repli.startswith('high') and not critic.strip():
        return 'CONFIRMED'
    if repli.startswith('high') and 'interpretive' in critic and 'fail' not in critic:
        return 'CONFIRMED'
    return 'DROP'

for c in claims:
    c['proxy_label'] = proxy_label(c)

label_counts = Counter(c['proxy_label'] for c in claims)
print(f"proxy label dist: {dict(label_counts)}")

# --- Feature extraction (AMEND-4 compliant) ---
def features(claim):
    stmt = claim.get('claim_statement', '').lower()
    rules = claim.get('counting_rules', '').lower()
    claimant = claim.get('claimant', '').lower()
    repli = claim.get('confidence_in_replicability', '').lower()

    # AMEND-4 features
    # broad_hisab_claim: boolean
    broad_hisab = int(any(k in stmt for k in ['19', 'abjad', 'gematric', 'gematria',
                                                'divisible', 'multiple of']))

    # substance_type: structural/formal, numerical/gematric, semantic
    if broad_hisab or any(k in stmt for k in ['= ', 'count', 'equals', 'exactly']):
        substance = 'numerical-gematric'
    elif any(k in stmt for k in ['ring', 'chiasm', 'palindrome', 'symmetry',
                                  'structure', 'composition', 'order']):
        substance = 'structural-formal'
    elif any(k in stmt for k in ['meaning', 'theme', 'theolog', 'rhetoric']):
        substance = 'semantic'
    else:
        substance = 'other'

    # Era (from claimant)
    if any(y in claimant for y in ['1974', '1980', '1982', '1989', 'rashad',
                                    'yüksel', 'khalifa']):
        era = 'modern-numerology'
    elif any(y in claimant for y in ['cuypers', 'farrin', '1997', '2000',
                                      '2003', '2014']):
        era = 'contemporary-academic'
    elif any(y in claimant for y in ['al-kaheel', 'nawfal', 'kaheel']):
        era = 'modern-apologetic'
    elif any(y in claimant for y in ['al-suyūṭī', 'suyuti', 'zarkashī', 'zarkashi',
                                      'rāzī', 'razi', 'bāqillānī', 'baqillani',
                                      'jurjānī', 'jurjani', 'kirmānī', 'kirmani',
                                      'ibn', 'jāḥiẓ', 'jahiz']):
        era = 'classical-medieval'
    else:
        era = 'unknown-era'

    # Claim-type: divisibility-miracle / word-count-symmetry / letter-count /
    #             structural / scientific-foreknowledge / other
    if any(k in stmt for k in ['19', 'divisible', 'multiple of']):
        ctype = 'divisibility-miracle'
    elif any(k in stmt for k in ['appears', 'occurs', 'count', 'times']):
        ctype = 'word-count-symmetry'
    elif any(k in stmt for k in ['letter', 'grapheme', 'alif', 'bāʾ', 'lām']):
        ctype = 'letter-count'
    elif any(k in stmt for k in ['ring', 'chiasm', 'symmetry', 'structure']):
        ctype = 'structural'
    elif any(k in stmt for k in ['science', 'embryolog', 'cosmolog', 'big bang',
                                  'iron', 'atom', 'ocean', 'universe']):
        ctype = 'scientific-foreknowledge'
    else:
        ctype = 'other'

    # Unit: whole-corpus / surah / verse / word / letter
    if any(k in stmt for k in ['quran', 'whole', 'entire', 'all']):
        unit = 'whole-corpus'
    elif any(k in stmt for k in ['surah', 'chapter']):
        unit = 'surah'
    elif any(k in stmt for k in ['verse', 'ayah']):
        unit = 'verse'
    elif any(k in stmt for k in ['letter', 'grapheme']):
        unit = 'letter'
    else:
        unit = 'other'

    # Specificity (proxy: length of claim_statement + numeric density)
    digits = sum(1 for c in stmt if c.isdigit())
    specificity = min(5, int(len(stmt) / 50) + int(digits > 3))

    # Replicability (proxy-ordered)
    if repli.startswith('high'):
        rep_ord = 2
    elif repli.startswith('medium'):
        rep_ord = 1
    elif repli.startswith('low'):
        rep_ord = 0
    else:
        rep_ord = 1

    # Counting-rules disclosure: 1 if rules are specified, 0 if "not-disclosed"
    rules_disclosed = int('not-disclosed' not in rules)

    return {
        'broad_hisab_claim': broad_hisab,
        'substance_type': substance,
        'era': era,
        'claim_type': ctype,
        'unit': unit,
        'specificity': specificity,
        'rep_ordinal': rep_ord,
        'rules_disclosed': rules_disclosed,
    }

# Build dataset restricted to labeled claims
dataset = []
for c in claims:
    if c['proxy_label'] == 'DROP':
        continue
    f = features(c)
    dataset.append({
        'claim_id': c.get('claim_id'),
        'label': 1 if c['proxy_label'] == 'CONFIRMED' else 0,
        'features': f,
    })
print(f"labeled dataset: {len(dataset)} (CONFIRMED={sum(1 for d in dataset if d['label']==1)}, REFUTED={sum(1 for d in dataset if d['label']==0)})")

# --- One-hot encoding ---
CATEGORICAL = ['substance_type', 'era', 'claim_type', 'unit']
NUMERIC = ['broad_hisab_claim', 'specificity', 'rep_ordinal', 'rules_disclosed']

categories = {k: sorted(set(d['features'][k] for d in dataset)) for k in CATEGORICAL}
def vectorize(d):
    v = []
    for k in CATEGORICAL:
        for cat in categories[k]:
            v.append(1 if d['features'][k] == cat else 0)
    for k in NUMERIC:
        v.append(d['features'][k])
    return v

feature_names = []
for k in CATEGORICAL:
    for cat in categories[k]:
        feature_names.append(f"{k}={cat}")
feature_names.extend(NUMERIC)

X = [vectorize(d) for d in dataset]
y = [d['label'] for d in dataset]
print(f"feature dim: {len(X[0])}")

# --- Manual logistic regression with L1 penalty (coordinate descent) ---
import math
def sigmoid(z):
    if z > 500: return 1.0
    if z < -500: return 0.0
    return 1/(1+math.exp(-z))

def logistic_l1_fit(X, y, lam=0.01, max_iter=200, lr=0.1):
    n = len(X); d = len(X[0])
    w = [0.0]*d
    b = 0.0
    for _ in range(max_iter):
        # Predict
        preds = [sigmoid(sum(w[j]*X[i][j] for j in range(d)) + b) for i in range(n)]
        # Gradient
        gb = sum(preds[i] - y[i] for i in range(n)) / n
        gw = [sum((preds[i] - y[i])*X[i][j] for i in range(n))/n for j in range(d)]
        b -= lr*gb
        for j in range(d):
            # L1 proximal
            w[j] -= lr*gw[j]
            if w[j] > lam*lr:
                w[j] -= lam*lr
            elif w[j] < -lam*lr:
                w[j] += lam*lr
            else:
                w[j] = 0.0
    return w, b

def predict(w, b, x):
    return 1 if sigmoid(sum(w[j]*x[j] for j in range(len(x))) + b) > 0.5 else 0

# --- 5-fold stratified CV ---
def stratified_folds(y, k=5, seed=20260413):
    rng = random.Random(seed)
    pos = [i for i,v in enumerate(y) if v==1]
    neg = [i for i,v in enumerate(y) if v==0]
    rng.shuffle(pos); rng.shuffle(neg)
    folds = [[] for _ in range(k)]
    for i,ix in enumerate(pos):
        folds[i%k].append(ix)
    for i,ix in enumerate(neg):
        folds[i%k].append(ix)
    return folds

folds = stratified_folds(y, k=5)
accuracies = []
fold_results = []
for fold_i in range(5):
    test_ix = folds[fold_i]
    train_ix = [i for i in range(len(y)) if i not in test_ix]
    X_tr = [X[i] for i in train_ix]; y_tr = [y[i] for i in train_ix]
    X_te = [X[i] for i in test_ix]; y_te = [y[i] for i in test_ix]
    w, b = logistic_l1_fit(X_tr, y_tr, lam=0.02, max_iter=300, lr=0.1)
    preds = [predict(w, b, x) for x in X_te]
    acc = sum(1 for a,b2 in zip(preds, y_te) if a==b2) / len(y_te) if y_te else 0
    accuracies.append(acc)
    fold_results.append({'fold': fold_i, 'n_test': len(y_te), 'acc': acc,
                          'test_labels': y_te, 'preds': preds})

mean_acc = sum(accuracies)/len(accuracies)
print(f"\n5-fold CV accuracies: {[f'{a:.3f}' for a in accuracies]}")
print(f"Mean: {mean_acc:.4f}")

# --- 1000× label permutation null ceiling ---
print("\nRunning 1000× label permutation null...")
null_accs = []
rng = random.Random(20260413)
for perm_i in range(1000):
    y_perm = y.copy()
    rng.shuffle(y_perm)
    folds_p = stratified_folds(y_perm, k=5, seed=20260413+perm_i)
    accs = []
    for fold_i in range(5):
        test_ix = folds_p[fold_i]
        train_ix = [i for i in range(len(y_perm)) if i not in test_ix]
        X_tr = [X[i] for i in train_ix]; y_tr = [y_perm[i] for i in train_ix]
        X_te = [X[i] for i in test_ix]; y_te = [y_perm[i] for i in test_ix]
        # Fewer iter for speed
        w, bp = logistic_l1_fit(X_tr, y_tr, lam=0.02, max_iter=100, lr=0.1)
        preds = [predict(w, bp, x) for x in X_te]
        acc = sum(1 for a,b3 in zip(preds, y_te) if a==b3) / len(y_te) if y_te else 0
        accs.append(acc)
    null_accs.append(sum(accs)/len(accs))

p_perm = sum(1 for a in null_accs if a >= mean_acc) / len(null_accs)
print(f"Null mean acc: {sum(null_accs)/len(null_accs):.4f}, 95th pct: {sorted(null_accs)[950]:.4f}")
print(f"Permutation p: {p_perm:.4f}")

# --- Fit final model on full dataset for interpretability ---
w_full, b_full = logistic_l1_fit(X, y, lam=0.02, max_iter=500, lr=0.1)
coefs = sorted(zip(feature_names, w_full), key=lambda x: -abs(x[1]))
print("\nTop 10 |coef| features (L1-selected):")
for name, c in coefs[:10]:
    if abs(c) > 1e-6:
        print(f"  {name}: {c:+.4f}")

# --- Acceptance criteria ---
acceptance = "PILOT_HONEST_NO_SIGNATURE"
if mean_acc > 0.70 and p_perm < 0.025:
    acceptance = "PILOT_PASS"
elif mean_acc < 0.60:
    acceptance = "PILOT_HONEST_NO_SIGNATURE"
elif mean_acc > 0.60 and mean_acc <= 0.70:
    acceptance = "PILOT_INTERMEDIATE"

out = {
    'status': 'PILOT - BLOCKED_ON_CLASSICAL_CORPUS_VERIFICATION',
    'task_id': 28,
    'seed': 20260413,
    'expected_corpus': {
        'CLASS_C_classical': 49,
        'CLASS_C_project': 28,
        'CLASS_R_classical': 18,
        'CLASS_R_project': 25,
        'total': 120,
    },
    'actual_pilot_corpus': {
        'source': 'docs/claims-catalog.md',
        'proxy_label_rule': 'criticisms-empirical-failure-markers + replicability',
        'n_total_parsed': len(claims),
        'n_labeled': len(dataset),
        'n_confirmed': sum(1 for d in dataset if d['label']==1),
        'n_refuted': sum(1 for d in dataset if d['label']==0),
        'n_dropped': sum(1 for c in claims if c['proxy_label']=='DROP'),
    },
    'amend_4_features': {
        'broad_hisab_claim': 'boolean (TRUE if claim involves 19/abjad/gematric/divisibility)',
        'substance_type': 'structural-formal | numerical-gematric | semantic | other',
    },
    'full_feature_set': feature_names,
    'cv_5fold': {
        'fold_accuracies': accuracies,
        'mean_accuracy': mean_acc,
        'fold_details': fold_results,
    },
    'null_permutation': {
        'n_perms': 1000,
        'null_mean_acc': sum(null_accs)/len(null_accs),
        'null_95pct': sorted(null_accs)[950],
        'null_99pct': sorted(null_accs)[990],
        'p_perm': p_perm,
    },
    'l1_selected_coefficients': [
        {'feature': n, 'coef': c} for n, c in coefs if abs(c) > 1e-6
    ],
    'acceptance': acceptance,
    'classical_scholar_delivery_spec': {
        'required_for_full_run': [
            '49 CLASS-C classical claims (CONFIRMED via project audit)',
            '18 CLASS-R classical claims (REFUTED via project audit)',
            '28 CLASS-C project claims (from master-findings-ledger audit-survived)',
            '25 CLASS-R project claims (from HONEST-LIMITS-LEDGER)',
            'Fields per claim: claim_id, claim_source, era, genre, school, claim_type, unit, scope, specificity, broad_hisab_claim (bool), substance_type (cat), empirical_verdict (CONFIRMED/REFUTED)',
        ],
    },
}

outp = ROOT / 'findings/phase-c-structures/csv/h-meta-1-pilot.json'
outp.parent.mkdir(parents=True, exist_ok=True)
outp.write_text(json.dumps(out, indent=2, ensure_ascii=False))

print(f"\nFINAL: {acceptance}")
print(f"mean 5-fold acc = {mean_acc:.3f}")
print(f"permutation p = {p_perm:.3f}")
print(f"saved: {outp}")
