n = int(input())
p = int(input())
k = int(input()) % n

a = (p - 2 + 2 * k * (p % 2 * 2 - 1)) % n + 1
b = (p     + 2 * k * (p % 2 * 2 - 1)) % n + 1 
print(min(a, b), max(a, b))
