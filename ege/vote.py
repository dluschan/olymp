vote = [[0, i] for i in range(12)]

for i in range(int(input())):
    vote[int(input())][0] += 1

for votes, task in sorted(filter(lambda x: x[0] != 0, vote), reverse = True):
    print(task, votes)
