n, k, m = map(int, input().split())
s = [[] for _ in range(m)]
q = 0
p = None
for t in input().split():
    x = int(t)
    s[x % m].append(x)
    if len(s[x % m]) > q:
        q = len(s[x % m])
        p = x % m
if q >= k:
    print('Yes')
    print(*s[p][:k])
else:
    print('No')
