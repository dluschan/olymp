def process(x):
    dx = 0
    dy = 0
    for i in range(1, 6):
        for j in range(1, 6):
            if x % 2 == 1 and i != j:
                dx -= (i - j)/abs(i - j)*i
                dy += (i - j)/abs(i - j)*j
            x //= 2
    return [dx, dy]

n = 0
pattern = [-1, -1]
for k in range(2**25):
    if process(k) == pattern:
        n += 1
print(n)
