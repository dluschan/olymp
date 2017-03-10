weight = []
diff = 0
n = int(input())
for i in range(n):
    q, c = map(int, input().split())
    if c == 2:
        q *= -1
    weight.append(q)
    diff += q
min_diff = abs(diff)
for i in range(n):
    if abs(diff - 2*weight[i]) < min_diff:
        min_diff = abs(diff - 2*weight[i])
    for j in range(i+1, n):
        if abs(diff - 2*(weight[i] + weight[j])) < min_diff:
            min_diff = abs(diff - 2*(weight[i] + weight[j]))
print(min_diff)
