#!/usr/bin/env python3
"""T1 rule-based classifier — can structural features distinguish Quranic 10-word passages from matched classical Arabic?"""
import json, random, re, sys
from collections import Counter
from pathlib import Path

ROOT = Path('/Users/grey/Downloads/quran')
random.seed(20260413)

# Load Quran
Q = json.loads((ROOT / 'quran-text/quran-no-tashkeel.json').read_text())

# Collect all Quranic words and 10-word consecutive windows
quran_windows = []
for surah in Q:
    verses = surah.get('verses', [])
    all_words = []
    for v in verses:
        t = v.get('text', '')
        all_words.extend(t.split())
    for i in range(len(all_words) - 9):
        quran_windows.append(' '.join(all_words[i:i+10]))

# Sample 200 Quranic 10-word windows
sampled_quran = random.sample(quran_windows, 200)

# Load Bukhari (non-Quran), Jahiz, and Muallaqat as baseline
baseline_texts = []
for fn in ['bukhari-noquran.txt', 'jahiz-hayawan.txt']:
    p = ROOT / 'data/baseline-corpora/raw' / fn
    if p.exists():
        baseline_texts.append(p.read_text()[:500_000])  # cap

# Split baseline into 10-word windows
baseline_windows = []
for txt in baseline_texts:
    # Clean diacritics roughly
    txt = re.sub(r'[\u064B-\u065F\u0670]', '', txt)
    words = txt.split()
    for i in range(0, len(words) - 9, 5):  # stride 5
        baseline_windows.append(' '.join(words[i:i+10]))

# Sample 200 baseline windows
sampled_base = random.sample(baseline_windows, 200)

# Divine-name list (Arabic rasm)
DIVINE_NAMES = set("""
الله الرحمن الرحيم الملك القدوس السلام المؤمن المهيمن العزيز الجبار
المتكبر الخالق البارئ المصور الغفار القهار الوهاب الرزاق الفتاح العليم
العالم الحكيم الحكم اللطيف الخبير الحليم العظيم الغفور الشكور الحي
القيوم الواحد الاحد الصمد القادر القدير المقتدر الاول الاخر الظاهر
الباطن الوالي المتعالي الكريم المنتقم العفو الرؤوف الصبور النور الهادي
البديع الباقي الوارث السميع البصير
""".split())

CLICHE_TOKENS = set("""
لا اله الا هو قل يايها ياايها ان ان الله ان ربكم
والله بالله ولله لله بسم بسم الله الرحمن الرحيم
""".split())

# Feature extractor
def features(passage):
    words = passage.split()
    f = {}
    f['divine_names'] = sum(1 for w in words if w in DIVINE_NAMES)
    f['cliches'] = sum(1 for w in words if w in CLICHE_TOKENS)
    f['mean_word_len'] = sum(len(w) for w in words) / max(len(words), 1)
    f['has_allah'] = 1 if 'الله' in passage else 0
    f['has_huwa'] = 1 if 'هو' in passage.split() else 0
    # Rhyme: do first or last two words share last 1-2 letters?
    if len(words) >= 2:
        f['end_assonance'] = 1 if words[-1][-1:] == words[-2][-1:] else 0
    else:
        f['end_assonance'] = 0
    # Character entropy
    chars = [c for c in passage if c.isalpha()]
    counts = Counter(chars)
    total = sum(counts.values())
    import math
    f['char_entropy'] = -sum((c/total)*math.log2(c/total) for c in counts.values() if c > 0) if total > 0 else 0
    # Short-word ratio (particles)
    f['short_word_ratio'] = sum(1 for w in words if len(w) <= 3) / max(len(words), 1)
    return f

# Build feature vectors
def featurize(corpus, label):
    rows = []
    for p in corpus:
        f = features(p)
        f['label'] = label
        rows.append(f)
    return rows

data = featurize(sampled_quran, 1) + featurize(sampled_base, 0)
random.shuffle(data)

# Train simple logistic regression via scikit if available
FEATURE_NAMES = ['divine_names', 'cliches', 'mean_word_len', 'has_allah', 'has_huwa', 'end_assonance', 'char_entropy', 'short_word_ratio']

X = [[r[k] for k in FEATURE_NAMES] for r in data]
y = [r['label'] for r in data]

train_cut = int(len(X) * 0.8)
X_train, X_test = X[:train_cut], X[train_cut:]
y_train, y_test = y[:train_cut], y[train_cut:]

try:
    from sklearn.linear_model import LogisticRegression
    from sklearn.metrics import accuracy_score, confusion_matrix
    clf = LogisticRegression(max_iter=1000, random_state=20260413)
    clf.fit(X_train, y_train)
    y_pred = clf.predict(X_test)
    acc = accuracy_score(y_test, y_pred)
    cm = confusion_matrix(y_test, y_pred)
    coefs = dict(zip(FEATURE_NAMES, clf.coef_[0].tolist()))
    method = "sklearn_logistic"
except ImportError:
    # Manual: use divine_names + cliches + has_allah as heuristic
    correct = 0
    tp = fp = tn = fn = 0
    for xi, yi in zip(X_test, y_test):
        score = xi[0] * 2 + xi[1] * 1.5 + xi[3] * 1
        pred = 1 if score >= 0.5 else 0
        if pred == yi:
            correct += 1
        if pred == 1 and yi == 1: tp += 1
        elif pred == 1 and yi == 0: fp += 1
        elif pred == 0 and yi == 0: tn += 1
        elif pred == 0 and yi == 1: fn += 1
    acc = correct / len(y_test)
    cm = [[tn, fp], [fn, tp]]
    coefs = {'divine_names': 2.0, 'cliches': 1.5, 'has_allah': 1.0}
    method = "manual_heuristic"

print(f"method: {method}")
print(f"train_n: {len(X_train)}, test_n: {len(X_test)}")
print(f"accuracy: {acc:.4f}")
print(f"confusion_matrix: {cm}")
print(f"feature_importance: {coefs}")
print(f"quran_sample_n: {len(sampled_quran)}")
print(f"baseline_sample_n: {len(sampled_base)}")

# Save JSON
out = {
    'method': method,
    'train_n': len(X_train),
    'test_n': len(X_test),
    'accuracy': acc,
    'confusion_matrix': cm if isinstance(cm, list) else cm.tolist(),
    'feature_importance': coefs,
    'seed': 20260413,
    'quran_sample_n': len(sampled_quran),
    'baseline_sample_n': len(sampled_base),
}
outp = ROOT / 'findings/phase-b-hypotheses/csv/t1-rule-based-classifier.json'
outp.parent.mkdir(parents=True, exist_ok=True)
outp.write_text(json.dumps(out, indent=2))
print(f"saved: {outp}")
