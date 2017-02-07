n, k = map(int, input().split())
n = min(n, k-1)
if n <= k // 2:
    m = 0
else:
    m = n - k // 2
print(m)
