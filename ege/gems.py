gems = [0] * 20
n = int(input())
k = 0.05*n
m = 0
for i in range(n):
    gems[20-int(input().split()[2])] += 1

i = 0
prev = 20
cur = 20
while m < k:
    if gems[i] > 0:
        prev = cur
        cur = i
    m += gems[i]
    i += 1
print(20-(i-1) if sum(gems[0:5]) >= k or m == k else 20-prev)
