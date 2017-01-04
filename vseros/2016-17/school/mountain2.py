n = int(input())

up = 0
prev = 0
minfinish = 1
minstart = 1

top = int(input())

for i in range(2, n+1):
    prev = top
    top = int(input())

    if up == 1:
        if top > prev:
            start = i - 1

        if top < prev:
            finish = i
            up = 0
            if minfinish - minstart == 0 or finish - start < minfinish - minstart:
                minfinish = finish
                minstart = start

    if up == 0:
        if top > prev:
            start = i - 1
            up = 1

if minfinish - minstart == 0:
    print(0)
else:
    print(minstart, minfinish)
