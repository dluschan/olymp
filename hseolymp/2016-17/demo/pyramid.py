n = int(input())
s = {}
for i in range(n):
    w, h = [int(x) for x in input().split()]
    if not w in s or h > s[w]:
        s[w] = h
print(sum(s.values()))
