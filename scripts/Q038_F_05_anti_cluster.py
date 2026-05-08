#!/usr/bin/env python3
"""Q038-F-05 — Singleton anti-cluster test on FR-roots metric.

Pre-reg: surahs/Q038-sad/Q038-F-05-anti-cluster-prereg.md
Pre-reg SHA256: 376d3229c121dd0677d359e15672a0da821dc3e429044f3c7bf664d994f12b76
Rules-tuple: (no-tashkeel, QAC-STEM root tokens, FR-angular distance per H-NEW-111, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)
"""
import json, hashlib, sys, os

PREREG = '/Users/grey/Downloads/quran/surahs/Q038-sad/Q038-F-05-anti-cluster-prereg.md'
EXPECTED_SHA = '376d3229c121dd0677d359e15672a0da821dc3e429044f3c7bf664d994f12b76'

# muqaṭṭaʿāt clusters per al-Suyūṭī al-Itqān nawʿ 40
CLUSTERS = {
    'ALM-6': [2, 3, 29, 30, 31, 32],
    'ALR-5': [10, 11, 12, 14, 15],
    'HM-7':  [40, 41, 42, 43, 44, 45, 46],
    'TSM-3': [26, 27, 28],
}
# All 29 muqaṭṭaʿāt surahs
MUQ_ALL = [2,3,7,10,11,12,13,14,15,19,20,26,27,28,29,30,31,32,36,38,40,41,42,43,44,45,46,50,68]
TARGET = 38


def verify_sha():
    with open(PREREG, 'rb') as f:
        actual = hashlib.sha256(f.read()).hexdigest()
    if actual != EXPECTED_SHA:
        print(f"FAIL: SHA mismatch.\n  expected={EXPECTED_SHA}\n  actual  ={actual}", file=sys.stderr)
        sys.exit(1)


def main():
    verify_sha()
    d = json.load(open('/Users/grey/Downloads/quran/findings/phase-b-hypotheses/csv/h-new-111.json'))
    triples = d['D_matrix_upper_triangular']
    N = 114
    M = [[0.0]*N for _ in range(N)]
    for entry in triples:
        i,j,dist = entry
        i = int(i); j = int(j)
        M[i-1][j-1] = dist
        M[j-1][i-1] = dist

    # Q38 row
    row = M[TARGET-1]

    # Distance from Q38 to each cluster centroid (= mean distance to cluster members)
    cluster_centroids = {}
    for name, members in CLUSTERS.items():
        dists = [row[m-1] for m in members]
        cluster_centroids[name] = {
            'members': members,
            'mean_distance_to_Q38': sum(dists)/len(dists),
            'min_distance_to_Q38': min(dists),
            'min_distance_member': members[dists.index(min(dists))],
        }
    min_centroid_dist = min(c['mean_distance_to_Q38'] for c in cluster_centroids.values())
    nearest_cluster = min(cluster_centroids.items(), key=lambda kv: kv[1]['mean_distance_to_Q38'])[0]

    # Non-cluster non-muqaṭṭaʿāt surahs (excluding Q38)
    non_cluster_surahs = [s for s in range(1, 115) if s not in MUQ_ALL]
    non_cluster_dists = [(s, row[s-1]) for s in non_cluster_surahs]
    non_cluster_dists.sort(key=lambda x: x[1])
    nearest_noncluster_surah, min_noncluster_dist = non_cluster_dists[0]

    # Δ = min_centroid_dist - min_noncluster_dist; H1: Δ > 0
    delta = min_centroid_dist - min_noncluster_dist

    # Ranks of cluster centroids among Q38's 113 distances
    all_dists = sorted([(s, row[s-1]) for s in range(1,115) if s != TARGET], key=lambda x: x[1])

    # For each cluster, find rank of its CLOSEST member among Q38's neighbors
    cluster_member_ranks = {}
    for name, members in CLUSTERS.items():
        ranks = []
        for m in members:
            for rk, (sid, dist) in enumerate(all_dists, 1):
                if sid == m:
                    ranks.append((m, rk, dist))
                    break
        cluster_member_ranks[name] = ranks

    # Top-5 nearest of any kind
    top5 = all_dists[:5]
    # Singletons
    other_singletons = {50: row[49], 68: row[67]}

    # Verdict
    direction_locked_satisfied = delta > 0
    # Strict success: Δ > 0 AND no cluster centroid in top-5 nearest
    # cluster centroids are pseudo, but we reframe: no INDIVIDUAL cluster member in Q38's top-5 nearest
    cluster_members_all = set()
    for ms in CLUSTERS.values():
        cluster_members_all.update(ms)
    top5_surahs = [s for s,_ in top5]
    cluster_in_top5 = any(s in cluster_members_all for s in top5_surahs)

    if direction_locked_satisfied and not cluster_in_top5:
        verdict = 'CONFIRMED'
    elif direction_locked_satisfied and cluster_in_top5:
        verdict = 'DIRECTIONAL'
    elif not direction_locked_satisfied:
        verdict = 'NULL_PRE_COMMIT_VIOLATION'
    else:
        verdict = 'NULL'

    out = {
        'finding_id': 'Q038-F-05',
        'prereg_sha': EXPECTED_SHA,
        'rules_tuple': '(no-tashkeel, QAC-STEM root tokens, FR-angular distance per H-NEW-111, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)',
        'method': 'compare Q38 mean-FR-distance to muq cluster centroids vs Q38 min-FR-distance to non-cluster non-muq surahs',
        'cluster_centroids': cluster_centroids,
        'nearest_cluster_by_centroid': nearest_cluster,
        'min_centroid_distance': min_centroid_dist,
        'nearest_noncluster_surah': nearest_noncluster_surah,
        'min_noncluster_distance': min_noncluster_dist,
        'delta_centroid_minus_noncluster': delta,
        'direction_locked_satisfied': direction_locked_satisfied,
        'top5_nearest_to_Q38': [{'surah': s, 'distance': d} for s,d in top5],
        'cluster_in_top5_nearest': cluster_in_top5,
        'cluster_member_ranks': cluster_member_ranks,
        'other_singletons_distance': {'Q50': other_singletons[50], 'Q68': other_singletons[68]},
        'verdict': verdict,
    }
    os.makedirs('/Users/grey/Downloads/quran/surahs/Q038-sad/csv', exist_ok=True)
    with open('/Users/grey/Downloads/quran/surahs/Q038-sad/csv/Q038-F-05.json', 'w') as f:
        json.dump(out, f, indent=2, ensure_ascii=False)

    print(f"Q38 distance to cluster centroids:")
    for name, c in cluster_centroids.items():
        print(f"  {name}: mean={c['mean_distance_to_Q38']:.4f}, min={c['min_distance_to_Q38']:.4f} (member Q{c['min_distance_member']})")
    print(f"Nearest non-cluster non-muq: Q{nearest_noncluster_surah} @ {min_noncluster_dist:.4f}")
    print(f"Δ = {delta:+.4f} (positive = ANTI-CLUSTERED, direction-locked satisfied)")
    print(f"Top-5 nearest to Q38: {top5}")
    print(f"Cluster member in top-5? {cluster_in_top5}")
    print(f"Other singletons: Q50={other_singletons[50]:.4f}, Q68={other_singletons[68]:.4f}")
    print(f"\nVerdict: {verdict}")


if __name__ == '__main__':
    main()
