n, m = [int(x) for x in input().split()]
n += 1
car = [x for x in range(n)]
for i in range(m):
    x, y = [int(s) for s in input().split()]
    car[x], car[y] = car[y], car[x]
pos = [0 for x in range(n)]
for i in range(n):
    pos[car[i]] = i
print(pos[1:])
