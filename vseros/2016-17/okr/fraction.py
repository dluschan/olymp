def gcd(x, y):
    return y if x % y == 0 else gcd(y, x % y)
    
a = int(input())
b = int(input())
c = int(input())
d = int(input())
step = 0
while a/b < c/d:
    a, b = a + 1, b + 1
    delimeter = gcd(b, a)
    a, b = a // delimeter, b // delimeter
    step += 1
print(step if a == c and b == d else 0)
