#!/usr/bin/env python3
"""H-CLASSIC-48 — al-Sakkākī Miftāḥ īqāʿ verse-length distributional test.

Pre-reg: findings/phase-b-hypotheses/h-classic-48-prereg.md
Spec:    findings/phase-b-hypotheses/h-classic-44-to-49-spec.md §H-CLASSIC-48

Extends H-NEW-35 (corpus-level Fisher-z) with:
  - Per-surah ρ_k for k ∈ {1, 2, 3} on 95 surahs (n_verses ≥ 10).
  - Per-surah |ρ_1| distribution comparison via two-sample KS test
    against n_verses-matched non-overlapping baseline spans
    (Bukhari hadith-reports + Jāḥiẓ sentences).
  - Per-surah within-surah permutation null at lag 1 (10,000 shuffles)
    counting surahs exceeding 99th percentile.

Bonferroni k=6 (within H-CLASSIC-44..49 family), α_bon = 0.0083.
Worst-baseline-wins primary verdict (LOCKED in pre-reg).

Seed 20260414. Two-sided KS test (LOCKED).
"""

import json
import math
import random
import re
import statistics
import sys
from pathlib import Path

import scipy.stats

ROOT = Path('/Users/grey/Downloads/quran')
SEED = 20260414

AR_LETTER = re.compile(r'[\u0621-\u064A]')


def len_letters(text):
    return sum(1 for ch in text if AR_LETTER.match(ch))


def pearson_r(x, y):
    n = len(x)
    if n < 2:
        return 0.0
    mx = sum(x) / n
    my = sum(y) / n
    num = sum((xi - mx) * (yi - my) for xi, yi in zip(x, y))
    vx = sum((xi - mx) ** 2 for xi in x)
    vy = sum((yi - my) ** 2 for yi in y)
    if vx == 0 or vy == 0:
        return 0.0
    return num / math.sqrt(vx * vy)


def autocorr(seq, lag):
    if len(seq) <= lag:
        return None
    return pearson_r(seq[:-lag], seq[lag:])


# ---- Load Quran verse-length sequences ----
Q = json.loads((ROOT / 'quran-text/quran-no-tashkeel.json').read_text())
all_surahs = {}
for s in sorted(Q, key=lambda x: x['id']):
    all_surahs[s['id']] = [len_letters(v['text']) for v in s['verses']]

# Per-reg LOCKED filter: n_verses >= 10
qualifying = [(sid, lens) for sid, lens in all_surahs.items() if len(lens) >= 10]
print(f"[load] total surahs: {len(all_surahs)}", file=sys.stderr)
print(f"[load] qualifying (n_verses >= 10): {len(qualifying)}", file=sys.stderr)
print(f"[load] excluded (n_verses < 10): "
      f"{[sid for sid, l in all_surahs.items() if len(l) < 10]}", file=sys.stderr)

# ---- Per-surah Quran ρ_k for k in {1, 2, 3} ----
LAGS = [1, 2, 3]
quran_per_surah = {}
for sid, lens in qualifying:
    quran_per_surah[sid] = {k: autocorr(lens, k) for k in LAGS}

quran_abs_rho1 = sorted(abs(quran_per_surah[sid][1]) for sid, _ in qualifying
                        if quran_per_surah[sid][1] is not None)
print(f"[quran] |ρ_1| n={len(quran_abs_rho1)}, "
      f"mean={statistics.mean(quran_abs_rho1):.4f}, "
      f"median={statistics.median(quran_abs_rho1):.4f}", file=sys.stderr)


# ---- Load baseline corpora ----
def sentence_lens_from_text(text, hadith_split=False):
    if hadith_split:
        parts = re.split(r'حدثنا|أخبرنا|وحدثنا|وأخبرنا', text)
    else:
        parts = re.split(r'[.!?؟۔\n]+|\s{2,}', text)
    return [len_letters(s) for s in parts if len_letters(s) > 0]


bukhari_text = (ROOT / 'data/baseline-corpora/raw/bukhari-noquran.txt').read_text(
    encoding='utf-8', errors='replace')
jahiz_text = (ROOT / 'data/baseline-corpora/raw/jahiz-hayawan.txt').read_text(
    encoding='utf-8', errors='replace')

bukhari_seq = sentence_lens_from_text(bukhari_text, hadith_split=True)
jahiz_seq = sentence_lens_from_text(jahiz_text, hadith_split=False)
print(f"[baseline] bukhari: {len(bukhari_seq)} reports, "
      f"mean len={statistics.mean(bukhari_seq):.1f}", file=sys.stderr)
print(f"[baseline] jahiz: {len(jahiz_seq)} sentences, "
      f"mean len={statistics.mean(jahiz_seq):.1f}", file=sys.stderr)


# ---- n_verses-matched non-overlapping baseline span sampling ----
def sample_matched_spans(baseline_seq, surah_lens_list, rng):
    """For each surah length n in surah_lens_list, sample a non-overlapping
    contiguous span of length n from baseline_seq. Returns list of
    |ρ_1| values (one per span) and a status string.

    Sampling: build interval set of "available" [start, end) intervals,
    initially [(0, len(seq))]. For each surah_n in (RNG-shuffled order
    to avoid order-bias), pick uniformly from available intervals long
    enough to fit, choose start uniformly within the interval, slice
    out [start, start+n), split the interval into the residuals.
    """
    available = [(0, len(baseline_seq))]
    spans = []

    # Process surah lengths in shuffled order so largest-first doesn't
    # pre-empt smaller ones unfairly. Keep mapping back to surah id by
    # carrying tuples (surah_idx_in_input, n).
    indexed = list(enumerate(surah_lens_list))
    rng.shuffle(indexed)

    out = [None] * len(surah_lens_list)
    degenerate = False
    for orig_idx, n in indexed:
        # Filter intervals long enough to fit n
        candidates = [iv for iv in available if iv[1] - iv[0] >= n]
        if not candidates:
            degenerate = True
            break
        # Choose uniformly weighted by interval-length-minus-(n-1)
        # (uniform start positions across all available starts).
        weights = [iv[1] - iv[0] - (n - 1) for iv in candidates]
        chosen_iv = rng.choices(candidates, weights=weights, k=1)[0]
        start_min = chosen_iv[0]
        start_max = chosen_iv[1] - n
        start = rng.randint(start_min, start_max)
        end = start + n
        # Compute span autocorr lag-1
        span = baseline_seq[start:end]
        r1 = autocorr(span, 1)
        out[orig_idx] = abs(r1) if r1 is not None else 0.0
        # Split chosen_iv into residuals
        available.remove(chosen_iv)
        if start > chosen_iv[0]:
            available.append((chosen_iv[0], start))
        if end < chosen_iv[1]:
            available.append((end, chosen_iv[1]))

    return out, degenerate


surah_lens_list = [len(lens) for _, lens in qualifying]

rng_bukhari = random.Random(SEED)
rng_jahiz = random.Random(SEED + 1)

bukhari_abs_rho1, bukhari_deg = sample_matched_spans(
    bukhari_seq, surah_lens_list, rng_bukhari)
jahiz_abs_rho1, jahiz_deg = sample_matched_spans(
    jahiz_seq, surah_lens_list, rng_jahiz)

if bukhari_deg:
    print(f"[baseline] bukhari DEGENERATE — insufficient non-overlapping "
          f"capacity for {len(qualifying)} matched spans (need "
          f"{sum(surah_lens_list)} total reports, have {len(bukhari_seq)})",
          file=sys.stderr)
    bukhari_abs_rho1_clean = []
else:
    bukhari_abs_rho1_clean = sorted(bukhari_abs_rho1)
    print(f"[baseline] bukhari sampled OK: "
          f"|ρ_1| mean={statistics.mean(bukhari_abs_rho1_clean):.4f}, "
          f"median={statistics.median(bukhari_abs_rho1_clean):.4f}",
          file=sys.stderr)

if jahiz_deg:
    print(f"[baseline] jahiz DEGENERATE — insufficient non-overlapping "
          f"capacity for {len(qualifying)} matched spans", file=sys.stderr)
    jahiz_abs_rho1_clean = []
else:
    jahiz_abs_rho1_clean = sorted(jahiz_abs_rho1)
    print(f"[baseline] jahiz sampled OK: "
          f"|ρ_1| mean={statistics.mean(jahiz_abs_rho1_clean):.4f}, "
          f"median={statistics.median(jahiz_abs_rho1_clean):.4f}",
          file=sys.stderr)


# ---- Two-sample KS tests ----
ks_results = {}

if not bukhari_deg:
    ks_b = scipy.stats.ks_2samp(quran_abs_rho1, bukhari_abs_rho1_clean,
                                  alternative='two-sided')
    ks_results['bukhari'] = {
        'status': 'COMPUTED',
        'ks_stat': float(ks_b.statistic),
        'ks_pvalue': float(ks_b.pvalue),
        'n_quran': len(quran_abs_rho1),
        'n_baseline': len(bukhari_abs_rho1_clean),
        'quran_mean_abs_rho1': statistics.mean(quran_abs_rho1),
        'baseline_mean_abs_rho1': statistics.mean(bukhari_abs_rho1_clean),
    }
    print(f"[KS] Quran vs Bukhari: D={ks_b.statistic:.4f}, "
          f"p={ks_b.pvalue:.4g}", file=sys.stderr)
else:
    ks_results['bukhari'] = {'status': 'DEGENERATE'}

if not jahiz_deg:
    ks_j = scipy.stats.ks_2samp(quran_abs_rho1, jahiz_abs_rho1_clean,
                                  alternative='two-sided')
    ks_results['jahiz'] = {
        'status': 'COMPUTED',
        'ks_stat': float(ks_j.statistic),
        'ks_pvalue': float(ks_j.pvalue),
        'n_quran': len(quran_abs_rho1),
        'n_baseline': len(jahiz_abs_rho1_clean),
        'quran_mean_abs_rho1': statistics.mean(quran_abs_rho1),
        'baseline_mean_abs_rho1': statistics.mean(jahiz_abs_rho1_clean),
    }
    print(f"[KS] Quran vs Jahiz: D={ks_j.statistic:.4f}, "
          f"p={ks_j.pvalue:.4g}", file=sys.stderr)
else:
    ks_results['jahiz'] = {'status': 'DEGENERATE'}

# Worst-baseline-wins (highest p-value among COMPUTED baselines)
computed_ps = [(name, r['ks_pvalue']) for name, r in ks_results.items()
                if r.get('status') == 'COMPUTED']
if not computed_ps:
    primary_verdict = 'NULL — both baselines DEGENERATE'
    worst_baseline_name = None
    worst_p = float('nan')
elif len(computed_ps) == 1:
    worst_baseline_name, worst_p = computed_ps[0]
    print(f"[primary] only one baseline computed → "
          f"worst = {worst_baseline_name} p={worst_p:.4g}", file=sys.stderr)
else:
    # Take MAX p-value (worst, highest p = hardest to reject)
    worst_baseline_name, worst_p = max(computed_ps, key=lambda x: x[1])
    print(f"[primary] worst-baseline-wins: {worst_baseline_name} "
          f"p={worst_p:.4g}", file=sys.stderr)

primary_pass = (worst_p is not None and not math.isnan(worst_p)
                and worst_p < 0.0083)
print(f"[primary] PASS: {primary_pass} (p < 0.0083 required)", file=sys.stderr)


# ---- SECONDARY: per-surah within-surah permutation null at lag 1 ----
# 10,000 shuffles per surah, count surahs exceeding their per-surah 99th pctile
N_PERM = 10_000
print(f"\n[secondary] running per-surah permutation null "
      f"({N_PERM} perms × {len(qualifying)} surahs)...", file=sys.stderr)

rng_perm = random.Random(SEED + 2)
secondary_per_surah = {}
n_exceed_lag1 = 0
for sid, lens in qualifying:
    obs_abs = abs(quran_per_surah[sid][1] or 0.0)
    null_abs_rhos = []
    sh = list(lens)
    for _ in range(N_PERM):
        rng_perm.shuffle(sh)
        r = autocorr(sh, 1)
        if r is not None:
            null_abs_rhos.append(abs(r))
    null_abs_rhos.sort()
    pct99 = null_abs_rhos[int(0.99 * len(null_abs_rhos))]
    exceeds = obs_abs > pct99
    secondary_per_surah[sid] = {
        'obs_abs_rho1': obs_abs,
        'null_99pct': pct99,
        'exceeds': exceeds,
    }
    if exceeds:
        n_exceed_lag1 += 1

print(f"[secondary] surahs exceeding per-surah 99th pctile @ lag 1: "
      f"{n_exceed_lag1}/{len(qualifying)}", file=sys.stderr)
print(f"[secondary] PASS (k_excess >= 5): {n_exceed_lag1 >= 5}", file=sys.stderr)
secondary_pass = n_exceed_lag1 >= 5

# ---- TERTIARY: descriptive multi-lag exceedance counts ----
print(f"\n[tertiary] descriptive multi-lag exceedance counts...", file=sys.stderr)
tertiary_counts = {}
for k in LAGS:
    if k == 1:
        # Already computed in secondary
        tertiary_counts[k] = n_exceed_lag1
        continue
    rng_t = random.Random(SEED + 10 + k)
    n_exc = 0
    for sid, lens in qualifying:
        obs_abs = abs(quran_per_surah[sid][k] or 0.0)
        if quran_per_surah[sid][k] is None:
            continue
        null_abs = []
        sh = list(lens)
        for _ in range(1000):  # cheaper for tertiary: 1k perms
            rng_t.shuffle(sh)
            r = autocorr(sh, k)
            if r is not None:
                null_abs.append(abs(r))
        null_abs.sort()
        pct99 = null_abs[int(0.99 * len(null_abs))]
        if obs_abs > pct99:
            n_exc += 1
    tertiary_counts[k] = n_exc
    print(f"  lag {k}: {n_exc}/{len(qualifying)} surahs exceed "
          f"per-surah 99th pctile", file=sys.stderr)


# ---- Acceptance-matrix routing ----
if primary_pass and secondary_pass:
    final_verdict = 'PASS — al-Sakkākī īqāʿ confirmed at distributional level'
elif primary_pass and not secondary_pass:
    final_verdict = 'PARTIAL — distributional difference present but per-surah signals are weak'
elif (not primary_pass) and secondary_pass:
    final_verdict = 'PARTIAL — per-surah signals exist but distribution matches baseline'
else:
    final_verdict = 'NULL — al-Sakkākī īqāʿ falsified at verse-length distributional scale'

print(f"\n=== FINAL VERDICT: {final_verdict} ===", file=sys.stderr)

# ---- Write JSON output ----
out = {
    'finding_id': 'h-classic-48',
    'pre_reg': 'findings/phase-b-hypotheses/h-classic-48-prereg.md',
    'pre_reg_compliance': 'PRE-REG-STANDARD-04',
    'rules_tuple': '(no-tashkeel, hafs-kufan, character-length-cleaned-verse, orthographic-token, mashriqi)',
    'seed': SEED,
    'lags': LAGS,
    'bonferroni_k': 6,
    'alpha_bon': 0.0083,
    'sided_test': 'two-sided (KS test)',
    'qualifying_surahs': {
        'n_total': len(all_surahs),
        'n_qualifying': len(qualifying),
        'qualifying_ids': [sid for sid, _ in qualifying],
        'excluded_ids': [sid for sid, l in all_surahs.items() if len(l) < 10],
    },
    'quran_per_surah_rho': {
        str(sid): {str(k): quran_per_surah[sid][k] for k in LAGS}
        for sid, _ in qualifying
    },
    'quran_abs_rho1_distribution': quran_abs_rho1,
    'baselines': {
        'bukhari': {
            'n_seq': len(bukhari_seq),
            'mean_seq_len': statistics.mean(bukhari_seq),
            'spans_status': 'DEGENERATE' if bukhari_deg else 'COMPUTED',
            'abs_rho1_distribution': bukhari_abs_rho1_clean,
        },
        'jahiz': {
            'n_seq': len(jahiz_seq),
            'mean_seq_len': statistics.mean(jahiz_seq),
            'spans_status': 'DEGENERATE' if jahiz_deg else 'COMPUTED',
            'abs_rho1_distribution': jahiz_abs_rho1_clean,
        },
    },
    'primary': {
        'description': 'two-sample KS test on |ρ_1| distributions, worst-baseline-wins',
        'ks_results': ks_results,
        'worst_baseline': worst_baseline_name,
        'worst_p': worst_p,
        'pass': primary_pass,
    },
    'secondary': {
        'description': 'per-surah within-surah permutation null at lag 1, count surahs > 99th pctile',
        'n_perm': N_PERM,
        'n_surahs': len(qualifying),
        'n_exceed_lag1': n_exceed_lag1,
        'k_excess_threshold': 5,
        'pass': secondary_pass,
        'per_surah': {str(sid): secondary_per_surah[sid] for sid in secondary_per_surah},
    },
    'tertiary_descriptive': {
        'description': 'multi-lag (1,2,3) per-surah permutation exceedance counts',
        'lag_exceedance_counts': {str(k): tertiary_counts[k] for k in LAGS},
        'n_perm_tertiary': 1000,
        'note': 'Not Bonferroni-counted; descriptive only.',
    },
    'final_verdict': final_verdict,
    'no_fork_protections_honored': [
        'per-surah filter LOCKED at n_verses >= 10',
        'lag set LOCKED to {1, 2, 3}',
        'worst-baseline-wins primary (highest p among COMPUTED baselines)',
        'n_verses-matched non-overlapping span sampling LOCKED',
        'two-sided KS LOCKED (no one-sided substitution)',
        f'permutation null seed {SEED}, 10000 shuffles per surah',
        'baselines LOCKED to bukhari-noquran + jahiz-hayawan',
    ],
    'data_reuse_disclosed': (
        'Reuses len_letters, pearson_r, autocorr, sentence_lens_from_text from '
        'scripts/h_new_35_length_autocorr.py. Reuses quran-no-tashkeel.json + '
        'baseline-corpora/raw/{bukhari-noquran,jahiz-hayawan}.txt. '
        'KS test fresh via scipy.stats.ks_2samp.'
    ),
}

out_path = ROOT / 'findings/phase-b-hypotheses/csv/h-classic-48.json'
out_path.write_text(json.dumps(out, indent=2, default=str))
print(f"\n[output] saved: {out_path}", file=sys.stderr)
