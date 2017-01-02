k, n = [int(x) for x in input().split()]
single_polyndroms = {}
pair_polyndroms = {}
for i in range(k):
    s, cost = input().split()
    cost = int(cost)
    if s == s[::-1]:
        if s in single_polyndroms:
            if cost < 0:
                if len(single_polyndroms[s][0]) > 0:
                    single_polyndroms[s][0] = max(single_polyndroms[s][0][0], cost)
                else:
                    single_polyndroms[s][0] = cost
            else:
                single_polyndroms[s][1].append(cost)
        else:
            if cost < 0:
                single_polyndroms[s] = [[cost], []]
            else:
                single_polyndroms[s] = [[], [cost]]
    else:
        idpoly = min(s, s[::-1]) + max(s, s[::-1])
        if idpoly in pair_polyndroms:
            if s in pair_polyndroms[idpoly]:
                pair_polyndroms[idpoly][s].append(cost)
            else:
                pair_polyndroms[idpoly][s] = [cost]
        else:
            pair_polyndroms[idpoly] = {s: [cost]}
res = 0
for pair in pair_polyndroms.values():
    if len(pair) == 2:
        key, beauty1 = pair.popitem()
        key, beauty2 = pair.popitem()
        while len(beauty1) * len(beauty2) > 0 and max(beauty1) + max(beauty2) > 0:
            res += max(beauty1) + max(beauty2)
            beauty1.remove(max(beauty1))
            beauty2.remove(max(beauty2))
max_min_pos = 0
min_max_neg = 0
for key, beauty in single_polyndroms.items():
    if len(beauty[0]) > 0 and len(beauty[1]) > 0:
        if beauty[0][0] + min(beauty[1]) > 0:
            if beauty[0][0] < min_max_neg:
                min_max_neg = beauty[0][0]
            res += sum(beauty[1]) + beauty[0][0]
        else:
            res += sum(beauty[1]) - min(beauty[1])
    else:
        res += sum(beauty[1])
        if len(beauty[1]) % 2 == 1:
            res -= min(beauty[1])
            if min(beauty[1]) > max_min_pos:
                max_min_pos = min(beauty[1])
if max_min_pos >= 0 and min_max_neg < 0 and max_min_pos + min_max_neg < 0:
    res -= max_min_pos + min_max_neg
else:
    res += max_min_pos
print(res)
