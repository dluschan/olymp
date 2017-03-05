n = int(input())
flow = input().split()

rose_wrong = []
fial_wrong = []

for i in range(len(flow)):
    if flow[i] == '1' and i % 2 == 1:
        fial_wrong.append(i)
    if flow[i] == '0' and i % 2 == 0:
        rose_wrong.append(i)

if len(rose_wrong) == len(fial_wrong):
    print(len(rose_wrong))
    for i in range(len(rose_wrong)):
        print(rose_wrong[i] + 1, fial_wrong[i] + 1)
else:
    print(-1)
