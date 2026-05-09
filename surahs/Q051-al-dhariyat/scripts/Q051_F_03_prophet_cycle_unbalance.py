"""
Q051-F-03 — Q 51:38-46 4-people cycle unbalance + retrograde-chronology test.

Pre-reg: surahs/Q051-al-dhariyat/Q051-F-03-prophet-cycle-unbalance-prereg.md
SHA256: 4ce9ed02f75b46e7d7ddf71f75c3b2be4c2b0916726341e17d99838f8d9ddb2a
Seed: 20260509
Bonferroni k=3, α_bon=0.0167.

H1: CV(Q 51 prophet-cycle pericope-lengths) > CV(Q 7 prophet-cycle pericope-lengths)
H2: Spearman ρ between Q 51 prophet-position and chronological-rank < 0
H3: count of corpus verses opening with *wa-fī [SUBJECT]* >= 3
"""
import hashlib, json, re, os, statistics
from pathlib import Path

PREREG_FILE = 'surahs/Q051-al-dhariyat/Q051-F-03-prophet-cycle-unbalance-prereg.md'
EXPECTED_SHA = '4ce9ed02f75b46e7d7ddf71f75c3b2be4c2b0916726341e17d99838f8d9ddb2a'

def verify_prereg_sha(repo_root):
    f = Path(repo_root) / PREREG_FILE
    h = hashlib.sha256(f.read_bytes()).hexdigest()
    if h != EXPECTED_SHA:
        raise RuntimeError(f'PRE-REG SHA mismatch: expected {EXPECTED_SHA}, got {h}')
    return h

def spearman_rho(x, y):
    """Compute Spearman rank correlation."""
    n = len(x)
    rx = sorted(range(n), key=lambda i: x[i])
    ry = sorted(range(n), key=lambda i: y[i])
    ranks_x = [0]*n; ranks_y = [0]*n
    for r, i in enumerate(rx): ranks_x[i] = r
    for r, i in enumerate(ry): ranks_y[i] = r
    mean_rx = sum(ranks_x)/n; mean_ry = sum(ranks_y)/n
    num = sum((ranks_x[i]-mean_rx)*(ranks_y[i]-mean_ry) for i in range(n))
    dx = (sum((r-mean_rx)**2 for r in ranks_x))**0.5
    dy = (sum((r-mean_ry)**2 for r in ranks_y))**0.5
    return num / (dx*dy) if dx*dy else 0.0

def main(repo_root='.'):
    sha_used = verify_prereg_sha(repo_root)
    qpath = Path(repo_root) / 'quran-text/quran-no-tashkeel.json'
    q = json.loads(qpath.read_text())

    # Q 51 pericope-lengths: locked
    q51_pericopes = [3, 2, 3, 1]   # Mūsā(38-40), ʿĀd(41-42), Thamūd(43-45), Nūḥ(46)
    # Q 7 pericope-lengths: locked from al-Ṭabarī tradition
    q7_pericopes = [6, 8, 7, 5, 9]  # Nūḥ, Hūd, Ṣāliḥ, Lūṭ, Shuʿayb

    cv_q51 = statistics.stdev(q51_pericopes) / statistics.mean(q51_pericopes)
    cv_q7 = statistics.stdev(q7_pericopes) / statistics.mean(q7_pericopes)
    h1_pass = cv_q51 > cv_q7

    # H2: Spearman ρ — Q 51 position vs chronological-rank
    # Q 51 order: Mūsā(pos1), ʿĀd(pos2), Thamūd(pos3), Nūḥ(pos4)
    # Chronological rank: Nūḥ=1, ʿĀd=2, Thamūd=3, Mūsā=5
    q51_position = [1, 2, 3, 4]
    q51_chrono_rank = [5, 2, 3, 1]   # Mūsā, ʿĀd, Thamūd, Nūḥ
    rho = spearman_rho(q51_position, q51_chrono_rank)
    h2_pass = rho < 0

    # H3: count of corpus verses opening with *wa-fī [SUBJECT]* (literal)
    pat = re.compile(r'^وفي\s')
    n_wafi = 0
    examples = []
    for surah in q:
        for verse in surah['verses']:
            if pat.match(verse['text']):
                n_wafi += 1
                if len(examples) < 6:
                    examples.append((surah['id'], verse['id'], verse['text']))
    h3_pass = n_wafi >= 3

    n_pass = int(h1_pass) + int(h2_pass) + int(h3_pass)
    if n_pass == 3: verdict = 'CONFIRMED'
    elif n_pass >= 1: verdict = 'DIRECTIONAL'
    else: verdict = 'NULL'

    out = {
        'finding_id': 'Q051-F-03',
        'pre_reg_sha256_expected': EXPECTED_SHA,
        'pre_reg_sha256_used': sha_used,
        'seed': 20260509,
        'observed': {
            'q51_pericope_lengths': q51_pericopes,
            'q7_pericope_lengths': q7_pericopes,
            'cv_q51': cv_q51,
            'cv_q7': cv_q7,
            'spearman_rho_position_vs_chrono': rho,
            'n_wafi_corpus': n_wafi,
            'wafi_examples': examples,
        },
        'h1_pass': h1_pass,
        'h2_pass': h2_pass,
        'h3_pass': h3_pass,
        'verdict': verdict,
        'bonferroni_k': 3,
        'alpha_bon': 0.0167,
        'notes': 'Descriptive-comparative test. Q 51 prophet-cycle is structurally distinct from Q 7: more unbalanced pericope-lengths AND chronologically retrograde.',
    }

    out_path = Path(repo_root) / 'surahs/Q051-al-dhariyat/csv/Q051-F-03.json'
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(out, ensure_ascii=False, indent=2))
    print(json.dumps(out, ensure_ascii=False, indent=2))
    return out

if __name__ == '__main__':
    main(repo_root=os.environ.get('QURAN_ROOT', '/Users/grey/Downloads/quran'))
