# каждая буква хранит количество вариатов раскладок из n элементов, раскладка перебирается с буквы X
# | a: 0 X | b: 0   | c: 0 X | d: 0     |
# |    0 0 |    0 X |    0   |    0 0 X |

n, k = [int(q) for q in input().split()]
hole = []
for i in range(k):
    x, y = [int(q) for q in input().split()]
    hole.append(2*(x-1) + 1 + y%2)

n *= 2
a = [0 for i in range(n+1)]
b = [0 for i in range(n+1)]
c = [0 for i in range(n+1)]
d = [0 for i in range(n+1)]
b[1] = 1
c[1] = 1
a[2] = 1 if any(index in hole for index in [1, 2]) else 2
d[2] = 1 if any(index in hole for index in [1, 3]) else 2

for i in range(3, n+1):
    a[i] = b[i-1] + (0 if any(index in hole for index in [i-2, i]) else d[i-2]) + (0 if any(index in hole for index in [i-1, i]) else a[i-2])
    b[i] = a[i-1] + (0 if any(index in hole for index in [i-2, i]) else c[i-2])
    c[i] = a[i-1] + (0 if any(index in hole for index in [i-1, i+1]) else b[i-2])
    d[i] = b[i-1] + (0 if any(index in hole for index in [i-1, i+1]) else a[i-2])
print(a[n])
