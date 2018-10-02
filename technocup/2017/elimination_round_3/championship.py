city = []

def calc(num, exclude):
    res = []
    if num in city:
        res.append(num)
    for c in road[num]:
        if c != exclude:
            for r in calc(c, num):
                res.append(r)
    return res

def check(w, pair):
    if any(len(d) > pair for d in w):
        return (False, [])
    
        return (True)

n, k = map(int, input().split())

road = [[] for x in range(n)]
for i in range(n-1):
    x, y = map(int, input().split())
    road[x-1].append(y-1)
    road[y-1].append(x-1)

for c in input().split():
    city.append(int(c)-1)

print(road)
print(city)

for y in range(n):
    s = []
    if y in city:
        s.append([y])
    for x in road[y]:
        s.append(calc(x, y))
    res, pairs = check(s, k):
    if res:
        for i in range(k):
            print(pairs[0][i], pairs[1][i], y)
        break
