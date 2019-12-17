a, b, x, y = (int(input()) for _ in range(4))
p, q = (x - 1) * a + x, (x + 1) * a + x
e, r = (y - 1) * b + y, (y + 1) * b + y
print(-1 if q < e or r < p else str(max(p, e)) + ' ' + str(min(q, r)))
