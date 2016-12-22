l = int(input())
n = int(input())
q = 0
c = 0
for i in range(n):
    r = int(input())
    if r == 1 and q == 0:
        c += 1
        q = l
    if q > 0:
        q -= 1
print(c)
