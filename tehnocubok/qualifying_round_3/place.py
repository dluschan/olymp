n, m, k = map(int, input().split())
print((k + 2*m - 1) // (2*m), ((k % (2*m) if k % (2*m) != 0 else 2*m) + 1) // 2, 'R' if k % 2 == 0 else 'L')
