n, m = map(int, input().split())
mountain = [None] * m
for h in range(n, 0, -1):
    for i, c in enumerate(input()):
        if c == '*' and mountain[i] is None:
            mountain[i] = h
print(max((b - a for a, b in zip(mountain[:-1], mountain[1:]) if b >= a), default=0), max((a - b for a, b in zip(mountain[:-1], mountain[1:]) if a >= b), default=0))
