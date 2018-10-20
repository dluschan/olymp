n, x, y = map(int, input().split())
pages = sorted(int(x) for x in input().split())
res = 0
for p in pages:
    if 2*x + y >= p:
        a = min(p // 2, x)
        b = p - 2*a
        x -= a
        y -= b
        res += 1
    else:
        break
print(res)
