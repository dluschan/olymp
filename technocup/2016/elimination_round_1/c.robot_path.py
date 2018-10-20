def neighbors(s, c, k, n, m):
    return [d for d in direction if 0 <= k % m + direction[d][0] < m and 0 <= k // m + direction[d][1] < n and s[k % m + direction[d][0] + (k // m + direction[d][1]) * m] == c]


direction = {'R': (1, 0), 'L': (-1, 0), 'D': (0, 1), 'U': (0, -1)}
n, m = map(int, input().split())
s = []
for _ in range(n):
    s += list(input())
k = s.index('S')
path = ''
while s.count('*'):
    d = neighbors(s, '*', k, n, m)[0]
    path += d
    k = k % m + direction[d][0] + (k // m + direction[d][1]) * m
    s[k] = '+'
path += neighbors(s, 'S', k, n, m)[0]
print(path)
