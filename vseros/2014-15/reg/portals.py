import copy

def destroy(num, portals, visited):
    while len(portals[num]) > 0:
        x = portals[num].pop(0)
        if x not in visited:
            visited.append(x)
        destroy(x, portals, visited)

def perfect(portals):
    perfect_portals = 0
    for city_num in range(n):
        copy_portals = copy.deepcopy(portals)
        visited = [city_num]
        destroy(city_num, copy_portals, visited)
        if len(visited) == n:
            perfect_portals += 1
    return perfect_portals


n, p = [int(x) for x in input().split()]

portals = [[] for c in range(n)]
for i in range(n):
    s = input()
    for j in range(n):
        if s[j] == '+':
            portals[i].append(j);

k = perfect(portals)
print(k)

v = {}.fromkeys([i for i in range(1, n + 1)], 0)

for step in range(n * (n-1) // 2):
    index = step + 1
    reversed_portals = copy.deepcopy(portals)
    for city in range(n):
        if index > len(reversed_portals[city]):
            index -= len(reversed_portals[city])
        else:
            reversed_portals[reversed_portals[city][index - 1]].append(city)
            reversed_portals[city].remove(reversed_portals[city][index - 1])
            break
    v[perfect(reversed_portals)] += 1

res = ''
for i in range(1 if p == 1 else k + 1, n + 1):
    res += str(v[i]) + ' '
print(res[:len(res)-1])
