n = int(input())
m = int(input())
k = 0
while m != 7:
    k += 1
    m += 2
    if m > 7:
        m -= 7
print(0 if k > n else 1 + (n - k) // 7)
