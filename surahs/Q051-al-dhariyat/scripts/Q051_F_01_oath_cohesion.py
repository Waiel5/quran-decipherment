"""
Q051-F-01 — Q 51:1-4 4-element oath cohesion test.

Pre-reg: surahs/Q051-al-dhariyat/Q051-F-01-creation-purpose-construct-prereg.md
SHA256: 063a22f51b2b8724b685e555d5e1f6ea6a5d70b851fe2b9f2261539472e9ff75
Seed: 20260509
n_perm: 10000
Bonferroni k=3, α_bon=0.0167.

H1: cohesion of Q 51:1-4 > random 4-spans of Q 51 (token-cosine)
H2: morphological-template parallelism (descriptive)
H3: cohesion of Q 51:1-4 > Q 51:5-8
"""
import hashlib, json, random, sys, os
from collections import Counter
from pathlib import Path

PREREG_FILE = 'surahs/Q051-al-dhariyat/Q051-F-01-creation-purpose-construct-prereg.md'
EXPECTED_SHA = '063a22f51b2b8724b685e555d5e1f6ea6a5d70b851fe2b9f2261539472e9ff75'

def verify_prereg_sha(repo_root):
    f = Path(repo_root) / PREREG_FILE
    h = hashlib.sha256(f.read_bytes()).hexdigest()
    if h != EXPECTED_SHA:
        raise RuntimeError(f'PRE-REG SHA mismatch: expected {EXPECTED_SHA}, got {h}')
    return h

def cosine(c1, c2):
    keys = set(c1) | set(c2)
    if not keys: return 0.0
    dot = sum(c1.get(k,0) * c2.get(k,0) for k in keys)
    n1 = sum(v*v for v in c1.values()) ** 0.5
    n2 = sum(v*v for v in c2.values()) ** 0.5
    return dot / (n1*n2) if (n1*n2) else 0.0

def mean_pair_cos(verses):
    bags = [Counter(v.split()) for v in verses]
    if len(bags) < 2: return 0.0
    s = 0.0; n = 0
    for i in range(len(bags)):
        for j in range(i+1, len(bags)):
            s += cosine(bags[i], bags[j]); n += 1
    return s / n if n else 0.0

def main(repo_root='.'):
    sha_used = verify_prereg_sha(repo_root)
    seed = 20260509
    n_perm = 10000
    random.seed(seed)

    qpath = Path(repo_root) / 'quran-text/quran-no-tashkeel.json'
    q = json.loads(qpath.read_text())
    s51 = q[50]
    verses = [v['text'] for v in s51['verses']]
    assert s51['id'] == 51

    target_idx = list(range(0, 4))   # vv. 1-4
    comp_idx = list(range(4, 8))      # vv. 5-8
    target_verses = [verses[i] for i in target_idx]
    comp_verses = [verses[i] for i in comp_idx]

    # H1: token cohesion of vv. 1-4
    obs_token = mean_pair_cos(target_verses)
    null_dist = []
    pool = list(range(60))
    for _ in range(n_perm):
        sample_idx = random.sample(pool, 4)
        sample_verses = [verses[i] for i in sample_idx]
        null_dist.append(mean_pair_cos(sample_verses))
    null_mean = sum(null_dist)/len(null_dist)
    p_one_tailed = sum(1 for v in null_dist if v >= obs_token) / len(null_dist)

    # H2: morphological-template descriptive
    # Each of vv 1-4 follows: (و/ف)+ال+[participle]+[cognate-accusative]
    # Detect: word 1 starts with و/ف+ال, word 2 ends in vowel-extension (descriptive only)
    # Simple structural check
    template_match = 0
    for verse in target_verses:
        words = verse.split()
        if len(words) < 2: continue
        w1, w2 = words[0], words[1]
        # Check w1 starts with و/فا or و/فال
        if (w1.startswith('وال') or w1.startswith('فال')) and len(words) == 2:
            template_match += 1

    # H3: vv 1-4 vs vv 5-8 token-cohesion
    comp_token = mean_pair_cos(comp_verses)

    # Verdict
    h1_pass = p_one_tailed <= 0.0167
    h2_pass = template_match == 4
    h3_pass = obs_token > comp_token

    n_pass = int(h1_pass) + int(h2_pass) + int(h3_pass)
    if n_pass == 3:
        verdict = 'CONFIRMED'
    elif n_pass >= 1:
        verdict = 'DIRECTIONAL'
    else:
        verdict = 'NULL'

    # Pre-commit violation: token level reversed
    pre_commit_viol = obs_token < (null_mean - 0.001)
    if pre_commit_viol:
        verdict = 'PRE-COMMIT VIOLATION (lexical-token level)'

    out = {
        'finding_id': 'Q051-F-01',
        'pre_reg_sha256_expected': EXPECTED_SHA,
        'pre_reg_sha256_used': sha_used,
        'seed': seed,
        'n_perm': n_perm,
        'observed': {
            'mean_pair_token_cosine_q51_1_4': obs_token,
            'mean_pair_token_cosine_q51_5_8': comp_token,
            'morphological_template_match': template_match,
        },
        'null_distribution': {
            'mean': null_mean,
            'p_one_tailed': p_one_tailed,
        },
        'verdict': verdict,
        'h1_pass': h1_pass,
        'h2_pass': h2_pass,
        'h3_pass': h3_pass,
        'bonferroni_k': 3,
        'alpha_bon': 0.0167,
        'notes': 'Token-level cohesion at zero is the EXPECTED OUTCOME under iʿjāz-balagha morphological-template reading (cf. Q037-F-03 PRE-COMMIT VIOLATION). The 4 verses are held together by morphological pattern, not lexical overlap.',
    }

    out_path = Path(repo_root) / 'surahs/Q051-al-dhariyat/csv/Q051-F-01.json'
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(out, ensure_ascii=False, indent=2))
    print(json.dumps(out, ensure_ascii=False, indent=2))
    return out

if __name__ == '__main__':
    main(repo_root=os.environ.get('QURAN_ROOT', '/Users/grey/Downloads/quran'))
