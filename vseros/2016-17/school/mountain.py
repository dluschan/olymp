n = int(input())

start = 0
finish = 0
minstart = 0
minfinish = 0

prev = int(input())
for i in range(2, n + 1):
    top = int(input())
    if prev < top:
        start = i - 1
    if prev > top:
        finish = i
    if start * finish != 0 and finish > start and (minfinish - minstart == 0 or finish - start < minfinish - minstart)
        minstart = start
        minfinish = finish
    prev = top

if min == 0:
    print(0)
else:
    print(minstart, minfinish)
