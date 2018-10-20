n, m, k = map(int, input().split())
a, b = map(int, input().split())
a -= 1
b -= 1
entrance_time, floor_time, lift_delay, lift_time = 15, 5, 10, 1
entrance_a = a // (m * k)
entrance_b = b // (m * k)
floor_a = a % (m * k) // k
floor_b = b % (m * k) // k
time = entrance_time * min(n - abs(entrance_a - entrance_b), abs(entrance_a - entrance_b))
if entrance_a == entrance_b:
    time += min(floor_time * abs(floor_a - floor_b), lift_time * abs(floor_a - floor_b) + lift_delay)
else:
    time += min(floor_time * floor_a, lift_time * floor_a + lift_delay)
    time += min(floor_time * floor_b, lift_time * floor_b + lift_delay)
print(time)
