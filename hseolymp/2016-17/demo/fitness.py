n = int(input())
for i in range(n):
    a, b, c, d = [int(x) for x in input().split()]
    if d - a >= b*c:
        print('YES')
    else:
        print('NO')
