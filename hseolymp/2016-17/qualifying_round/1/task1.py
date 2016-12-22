n, m = [int(x) for x in input().split()]
stops = n // m
if n % m == 0:
    stops -= 1
time = n + (1 + stops) * stops // 2
print(time)
