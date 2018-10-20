n = int(input())
s = sorted(int(t) for t in input().split())
for a, b in zip(s[:n], s[n:][::-1]):
    print(a, b)
