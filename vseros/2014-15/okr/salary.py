a = int(input())
b = int(input())
c = int(input())
n = int(input())

q = max((a+1)//2*2, 2*b, 2*c) # новая зарплата Алексая после "минимального уравнивания"
m = q - a + q // 2 - b + q // 2 - c # минимальный премиальный фонд, которого хватит уравнять
if m > n:
    print(0)
else:
    print(q - a + (n - m) // 4 * 2)
    print(q // 2 - b + (n - m) // 4)
    print(q // 2 - c + (n - m) // 4)
