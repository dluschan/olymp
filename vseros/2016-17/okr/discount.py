new = []
old = {}
n = int(input())
for i in range(n):
    price = int(input())
    if price in old:
        old[price] -= 1
        if old[price] == 0:
            del old[price]
    else:
        new.append(price)
        old[price * 4 // 3] = old.get(price * 4 // 3, 0) + 1
for price in new:
    print(price)
