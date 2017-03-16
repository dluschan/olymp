n, m, k = map(int, input().split())
print((k + 2*m - 1) // (2*m), (k % 2*m + 1) // 2, 'L' if k % 2 else 'R')
