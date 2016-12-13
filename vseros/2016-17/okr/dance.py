n = int(input())
p = int(input())
k = int(input()) % n
a = (p - 2 + (p % 2 * 2 - 1) * 2 * k) % n + 1
b = (p     + (p % 2 * 2 - 1) * 2 * k) % n + 1
print(min(a, b), max(a, b))
