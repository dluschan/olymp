n, k = [int(q) for q in input().split()]
hole = []
for i in range(k):
    x, y = [int(q) for q in input().split()]
    hole.append(2*(x-1) + 1 + y%2)

n *= 2
a = [0 for i in range(n+1)]
b = [0 for i in range(n+1)]
c = [0 for i in range(n+1)]
d = [0 for i in range(n+1)]
a[1] = 0
a[2] = 2
b[1] = 1
b[2] = 0
c[1] = 1
c[2] = 0
d[1] = 0
d[2] = 2
for i in range(1, 3):
    if i in hole:
        #исправить!
        a[i] = 0
        b[i] = 0
        c[i] = 0
        d[i] = 0
        
for i in range(3, n+1):
    if not (i in hole):
        a[i] = (d[i-2] if (i-2) not in hole else 0) + (a[i-2] if (i-1) not in hole else 0) + b[i-1]
        b[i] = a[i-1] + (c[i-2] if (i-2) not in hole else 0)
    
    if (i+1 not in hole):
        c[i] = (b[i-2] if (i-1) not in hole else 0) + a[i-1]
        d[i] = (a[i-2] if (i-1) not in hole else 0) + b[i-1]
print(a, b, c, d)
