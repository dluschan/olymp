input()
orders = [int(x) for x in input().split()]
orders.sort()
res = 1
for i in range(len(orders)):
    res *= orders[i] - i
print(res)
