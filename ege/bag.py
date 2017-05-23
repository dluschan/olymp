n = int(input())
m = int(input())
cells = ['00:00'] * m
for i in range(n):
    name, start, finish = input().split()
    for k, c in enumerate(cells):
        if c <= start:
            cells[k] = finish
            print(name, k+1)
            break
