n, m = map(int, input().split())
rates = []
money = n
p = n
for i in range(m):
    a, b = map(int, input().split())
    if a > b:
        if a < n:
            rates.append([a, b])
            p = min(p, a)
        else:
            money = min(money, b)

path = [0 for i in range(n)]
for i in range(n):
    if n - p == i:
        rates.append([1, 1])
    if path[i] > 0 or i == 0:
        for r in rates:
            x = i + r[0]
            cost = path[i] + r[1]
            if x >= n and cost < money:
                    money = cost
            if x < n:
                path[x] = cost if path[x] == 0 else min(path[x], cost)
print(money)
