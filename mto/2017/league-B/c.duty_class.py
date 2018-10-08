n = int(input())
s = []
for x in range(max(1, n - 9*9), n):
    w = x
    y = x
    while x:
        w += x % 10
        x //= 10
    if w == n:
        s.append(y)
print(len(s))
print(*s)
