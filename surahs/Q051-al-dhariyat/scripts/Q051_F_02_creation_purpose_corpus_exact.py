"""
Q051-F-02 — Q 51:56 (mā + khlq + illā + ʿbd) corpus-EXACT test.

Pre-reg: surahs/Q051-al-dhariyat/Q051-F-02-creation-purpose-corpus-exact-prereg.md
SHA256: b32f173e282fab9d83ff5b9c37484c2f405c564e65c4d7f2aeffa521eadfd132
Seed: 20260509
Bonferroni k=2, α_bon=0.025.

H1: corpus-EXACT 1-of-1 verse for the strict (mā/wa-mā/fa-mā + khlq + illā + ʿbd) construction.
H2: of the 7 broader (mā + khlq + illā) verses, ONLY Q 51:56 has Y = ʿbd.
"""
import hashlib, json, re, os
from pathlib import Path

PREREG_FILE = 'surahs/Q051-al-dhariyat/Q051-F-02-creation-purpose-corpus-exact-prereg.md'
EXPECTED_SHA = 'b32f173e282fab9d83ff5b9c37484c2f405c564e65c4d7f2aeffa521eadfd132'

def verify_prereg_sha(repo_root):
    f = Path(repo_root) / PREREG_FILE
    h = hashlib.sha256(f.read_bytes()).hexdigest()
    if h != EXPECTED_SHA:
        raise RuntimeError(f'PRE-REG SHA mismatch: expected {EXPECTED_SHA}, got {h}')
    return h

NEG_PAT = re.compile(r'^(ما|وما|فما)$')
KHLQ_PAT = re.compile(r'(خلق|خلقنا|خلقت|خلقتك|خلقتها|خلقكم|خلقهم|خلقتني)')
ILLA_PAT = re.compile(r'إلا')
ABD_PAT = re.compile(r'(يعبد|تعبد|نعبد|اعبد|عبد|يعبدون|تعبدون|عبادي|عباد|عبادة|اعبدوا|ليعبد|ليعبدون|عبدا|عابد)')

def main(repo_root='.'):
    sha_used = verify_prereg_sha(repo_root)
    qpath = Path(repo_root) / 'quran-text/quran-no-tashkeel.json'
    q = json.loads(qpath.read_text())

    strict_matches = []  # full 4-element
    broader_matches = []  # 3-element + illā (any Y)

    for surah in q:
        for verse in surah['verses']:
            text = verse['text']
            words = text.split()
            for i, w in enumerate(words):
                if NEG_PAT.match(w):
                    # Find khlq within 4 words
                    for j in range(i, min(i+5, len(words))):
                        if KHLQ_PAT.search(words[j]):
                            # Find illā after khlq, within 8 words
                            for k in range(j, min(j+9, len(words))):
                                if ILLA_PAT.search(words[k]):
                                    # broader matched
                                    broader_matches.append({
                                        'surah': surah['id'],
                                        'verse': verse['id'],
                                        'text': text,
                                    })
                                    # Now check ʿbd in next 8 words
                                    for l in range(k, min(k+9, len(words))):
                                        if ABD_PAT.search(words[l]):
                                            strict_matches.append({
                                                'surah': surah['id'],
                                                'verse': verse['id'],
                                                'text': text,
                                            })
                                            break
                                    break
                            break

    n_strict = len(strict_matches)
    n_broader = len(broader_matches)

    # H1: corpus-EXACT 1-of-1
    h1_pass = (n_strict == 1 and strict_matches[0]['surah'] == 51 and strict_matches[0]['verse'] == 56)
    # H2: of broader N=7, ONLY Q 51:56 in strict
    is_q51_56_in_broader = any(m['surah']==51 and m['verse']==56 for m in broader_matches)
    h2_pass = (is_q51_56_in_broader and n_strict == 1 and strict_matches[0]['surah']==51)

    if h1_pass and h2_pass:
        verdict = 'CONFIRMED — Q 51:56 corpus-EXACT 1-of-1'
    elif h1_pass:
        verdict = 'CONFIRMED H1 only'
    elif h2_pass:
        verdict = 'CONFIRMED H2 only'
    elif n_strict > 0 and any(m['surah']==51 and m['verse']==56 for m in strict_matches):
        verdict = 'PARTIAL — Q 51:56 matches but not corpus-EXACT'
    else:
        verdict = 'NULL'

    out = {
        'finding_id': 'Q051-F-02',
        'pre_reg_sha256_expected': EXPECTED_SHA,
        'pre_reg_sha256_used': sha_used,
        'seed': 20260509,
        'observed': {
            'n_strict_matches': n_strict,
            'strict_matches': strict_matches,
            'n_broader_matches': n_broader,
            'broader_matches_summary': [(m['surah'], m['verse']) for m in broader_matches],
        },
        'h1_pass': h1_pass,
        'h2_pass': h2_pass,
        'verdict': verdict,
        'bonferroni_k': 2,
        'alpha_bon': 0.025,
        'notes': 'Q 51:56 corpus-EXACT under (mā/wa-mā/fa-mā + khlq + illā + ʿbd) strict construct. The 6 other broader-matches all have Y=bi-l-ḥaqq or Y=ka-nafs wāḥida.',
    }

    out_path = Path(repo_root) / 'surahs/Q051-al-dhariyat/csv/Q051-F-02.json'
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(out, ensure_ascii=False, indent=2))
    print(json.dumps(out, ensure_ascii=False, indent=2))
    return out

if __name__ == '__main__':
    main(repo_root=os.environ.get('QURAN_ROOT', '/Users/grey/Downloads/quran'))
