n, m, k = map(int, input().split())
if 2*n*m % k:
    print('NO')
else:
    print('YES')
    print(0, 0)
    print(n, 1)
    print(n * ((2*m + k - 1) // k) - 2*n*m // k, (2*m + k - 1) // k)
