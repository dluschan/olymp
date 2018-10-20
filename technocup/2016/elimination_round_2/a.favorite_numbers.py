input()
r, k = 0, 0
for s in input().split():
    x = int(s)
    degree = 0
    while x and x % 2 == 0:
        degree += 1
        x //= 2
    if degree > r:
        r, k = degree, 1
    elif degree == r:
        k += 1
print(2**r, k)
