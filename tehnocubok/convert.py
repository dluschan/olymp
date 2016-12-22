a, b = [int(x) for x in input().split()]

res = [b]

while b > a:
    if b % 10 == 1:
        b //= 10
        res.append(b)
        continue
    if b % 2 == 0:
        b //= 2
        res.append(b)
        continue
    if b % 10 in [3, 5, 7, 9]:
        break;

res.reverse()
if b == a:
    print('YES')
    print(len(res))
    for x in res:
        print(x, end=' ')
    print()
else:
    print('NO')
