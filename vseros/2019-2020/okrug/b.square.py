def enough(k):
    return (2*x + 2*y - 4*k) * k <= t

x, y, t = (int(input()) for _ in range(3))
a, b = 0, min(x, y)
while a + 1 != b:
    m = (a + b) // 2
    if enough(m):
        a = m
    else:
        b = m
print(a)
