n, p = [int(x) for x in input().split()]
map = [[] for i in range(n)]

for i in range(n):
    #map.append([])
    for j in range(n):
        sign = input()
        if i != j:
            if sign == '+':
                map[i].append(j)
print(map)
