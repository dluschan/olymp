n, m = map(int, input().split())
dogs = sorted((int(x) for x in input().split()))
done = 0
for _ in range(m):
    x, t = map(int, input().split())
    for i, d in enumerate(dogs):
        if x - t <= d <= x + t:
            done += 1
            dogs.pop(i)
            break
print(done)
