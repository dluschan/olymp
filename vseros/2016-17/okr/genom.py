s = input()
g1 = {}
for i in range(1, len(s)):
    g1[s[i-1: i+1]] = g1.get(s[i-1: i+1], 0) + 1
s = input()
g2 = {}
for i in range(1, len(s)):
    g2[s[i-1: i+1]] = g2.get(s[i-1: i+1], 0) + 1
print(sum([g1[g]*g2[g] for g in frozenset(g1.keys()) & frozenset(g2.keys())]))
