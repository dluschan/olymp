n = int(input())
prev = input()
days = 1
for i in range(n-1):
    cur = input()
    if prev >= cur:
        days += 1
print(days)
