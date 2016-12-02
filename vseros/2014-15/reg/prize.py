n, k = [int(s) for s in input().split()]
a = [int(s) for s in input().split()]

b = []
sum = 0
for p in a:
    sum += p
    b.append(sum)

l = []
for i in range(n):
    l.append(0 if i - k - 1 < -1 or i - k - 1 + k + k > n - 1 else b[i - k - 1 + k] if i - k - 1 == -1 else max(l[i - 1], b[i - k - 1 + k] - b[i - k - 1]))

r = []
for i in range(n):
    r.append(0 if k + k - 1 - i > 0 else max(r[i-1], b[n - 1 - i + k - 1 + k] - b[n - 1 - i + k - 1]))
r.reverse()

print(min([max(l[i], r[i]) for i in range(n-k+1)]))
