n = int(input())
old_price = {}
for i in range(n):
    price = int(input())
    if price in old_price:
        if old_price[price] == 1:
            del old_price[price]
        else:
            old_price[price] -= 1
    else:
        if (price * 4 // 3) in old_price:
            old_price[price * 4 // 3] += 1
        else:
            old_price[price * 4 // 3] = 1
        print(price)
