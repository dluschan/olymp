from heapq import heapify, heappop, heappush

n = int(input())
k, y, s = 0, 0, 0
a = [int(input()) for _ in range(n)]
heapify(a)
while a:
    if a[0] * len(a) > s:
        k, y, s = len(a), a[0], a[0] * len(a)
    x = heappop(a)
print(k, y)
