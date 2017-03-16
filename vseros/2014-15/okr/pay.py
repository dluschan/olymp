a = int(input())
b = int(input())
c = int(input())
n = int(input())

d = max((a+1)//2, b, c)
m = 4*d-a-b-c

if n < m:
    print(0)
    exit(0)

w = (n-m)//4

print(2*d - a + 2*w)
print(d - b + w)
print(d - c + w)
