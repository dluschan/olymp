c = int(input())
p = int(input())
n = int(input())

cookie = 0
prod = 1
time = 0

without_fact = (n - cookie + prod - 1) // prod
with_fact = (c - cookie + prod - 1) // prod + (n - cookie - ((c - cookie + prod - 1) // prod * prod - c) + prod + p - 1) // (prod + p)
while with_fact < without_fact:
    time += (c - cookie + prod - 1) // prod
    cookie += (c - cookie + prod - 1) // prod * prod - c
    prod += p
    without_fact = (n - cookie + prod - 1) // prod
    with_fact = (c - cookie + prod - 1) // prod + (n - cookie - ((c - cookie + prod - 1) // prod * prod - c) + prod + p - 1) // (prod + p)

time += (n - cookie + prod - 1) // prod
print(time)
