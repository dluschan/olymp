a =[0 for i in range(10)]
for c in input():
    a[int(c)] += 1 
number = 0
for i in range(1, 10):
    number += a[i] * i
if number % 3 != 0:
    for i in range(1, 10):
        if i % 3 == number % 3 and a[i] > 0:
            number -= i
            a[i] -= 1
            break
if number % 3 != 0:
    for i in range(1, 10):
        if i % 3 != 0 and a[i] > 0:
            number -= i
            a[i] -= 1
            break
if number % 3 != 0:
    for i in range(1, 10):
        if i % 3 != 0 and a[i] > 0:
            number -= i
            a[i] -= 1
            break
if number % 3 == 0:
    for i in range (9, -1, -1):
        print(str(i) * a[i], end = '')
print()
