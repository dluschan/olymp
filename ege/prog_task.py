task = {i + 1: 0 for i in range(12)}

for i in range(int(input())):
    task[int(input())] += 1

for i in sorted(filter(lambda key: task[key] != 0, task)):
    print(i, task[i])
