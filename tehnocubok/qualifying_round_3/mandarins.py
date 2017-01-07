n, k = map(int, input().split())
parts = []
for mandarin in input().split():
    parts.append(int(mandarin))

while len(parts) > k:
    parts.remove(min(parts))

while len(parts) < k and parts[0] >= 2:
    parts.append(parts[0] // 2)
    parts.append((parts[0] + 1) // 2)
    parts.remove(max(parts))

while len(parts) == k and max(parts) // 2 > min(parts):
    parts.remove(min(parts))
    parts.append(parts[0] // 2)
    parts.append((parts[0] + 1) // 2)
    parts.remove(max(parts))

if len(parts) == k:
    print(min(parts))
else:
    print(-1)
