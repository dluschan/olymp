n, k = map(int, input().split())
m = [int(x) for x in input().split()]

while k < len(m):
    m.remove(min(m))

while len(m) < k and max(m) > 1:
    m.append((max(m) + 1)// 2)
    m.append(max(m) // 2)
    m.remove(max(m))

while k == len(m) and min(m) < max(m) // 2:
    m.remove(min(m))
    m.append((max(m) + 1)// 2)
    m.append(max(m) // 2)
    m.remove(max(m))

if len(m) < k:
    print(-1)
else:
    print(min(m))
