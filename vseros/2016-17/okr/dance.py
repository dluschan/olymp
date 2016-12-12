n = int(input())
p = int(input())
k = int(input()) % n

a = ((((p - 1) - ((p - 1) % 2 * 2 - 1) * k) % n - 1) % n - (p % 2 * 2 - 1) * k) % n + 1
b = ((((p - 1) - ((p - 1) % 2 * 2 - 1) * k) % n + 1) % n - (p % 2 * 2 - 1) * k) % n + 1
print(min(a, b), max(a, b))
