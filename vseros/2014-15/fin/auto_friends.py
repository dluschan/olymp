a = [0 for x in range(100)]
b = [0 for x in range(100)]
c = [0 for x in range(100)]
ab = [0 for x in range(10000)]
bc = [0 for x in range(10000)]
ac = [0 for x in range(10000)]
abc = [0 for x in range(1000000)]

for i in range(int(input())):
    q, w, e = map(int, input().split())
    a[q-1] += 1
    b[w-1] += 1
    c[e-1] += 1
    ab[100*(q-1) + w-1] += 1
    bc[100*(w-1) + e-1] += 1
    ac[100*(q-1) + e-1] += 1
    abc[10000*(q-1) + 100*(w-1) + e-1] += 1

couples = 0
for records in [a, b, c]:
    for value in records:
        if value > 1:
            couples += value * (value - 1) // 2

for records in [ab, bc, ac]:
    for value in records:
        if value > 1:
            couples -= value * (value - 1)

for value in abc:
    if value > 1:
        couples += 3 * (value * (value - 1) // 2)

print(couples)
