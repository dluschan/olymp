c = int(input())
p = int(input())
n = int(input())

cookie = 0
prod = 1
time = 0

without_fact = (n - cookie) // prod
with_fact = (c - cookie) // prod + (n - cookie - ((c - cookie) // prod * prod - c)) // (prod + p)
while with_fact < without_fact:
    time += (c - cookie) // prod
    cookie += (c - cookie) // prod * prod - c
    prod += p
    without_fact = (n - cookie) // prod
    with_fact = (c - cookie) // prod + (n - cookie - ((c - cookie) // prod * prod - c)) // (prod + p)

time += (n - cookie) // prod
print(time)
