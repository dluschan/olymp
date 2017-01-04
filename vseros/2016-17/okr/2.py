def gcd(x, y):
    return y if x % y == 0 else gcd(y, x % y)

a = int(input())
b = int(input())
c = int(input())
d = int(input())
k = 0
while a / b < c / d:
    a += 1
    b += 1
    n = gcd(b, a)
    a /= n
    b /= n
    k += 1
if a / b == c / d:
    print(k)
else:
    print(0)
