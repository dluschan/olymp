n, a, b, c = int(input()), int(input()), int(input()), int(input())
print(0 if n == 1 else min(a, b) + (n-2) * min(a, b, c))