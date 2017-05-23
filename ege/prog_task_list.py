task = [[i + 1, 0] for i in range(12)]

for i in range(int(input())):
    task[int(input()) - 1][1] += 1

for i, t in sorted(filter(lambda t: t[1] != 0, task), key = lambda x: x[1], reverse = True):
    print(i, t)
