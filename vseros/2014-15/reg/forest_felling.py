from fractions import gcd
a, k, b, m, x = [int(s) for s in input().split()]

p = k * m // gcd(k, m)
c = a * (p - p // k) + b * (p - p // m)
n = x // c
x %= c

if x:
    left = 0
    right = p
    while right - left > 1:
        mid = (left + right) // 2
        if a * (mid - mid // k) + b * (mid - mid // m) >= x:
            right = mid
        else:
            left = mid
    print(n * p + right)
else:
    print(n * p - 1)
