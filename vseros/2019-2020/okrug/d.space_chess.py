import itertools

def dist(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def step(q):
    x, y = q
    return {(x + dx, y + sy * (3 - abs(dx))) for dx, sy in itertools.product([-2, -1, +1, +2], [+1, -1])}

t = (int(input()), int(input()))
c = (0, 0)
while dist(t, c) > 1:
    c = min(step(c), key = lambda q: dist(q, t))
    print(*c)
if c != t:
    c = (c[0] + 1, c[1] - 2)
    print(*c)
    c = (c[0] + 2, c[1] + 1)
    print(*c)
    c = (c[0] - 2, c[1] + 1)
    print(*c)
    c = (step(c) & step(t)).pop()
    print(*c)
    c = t
    print(*c)
