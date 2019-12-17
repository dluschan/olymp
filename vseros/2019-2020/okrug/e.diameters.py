from heapq import heapify, heappop, heappush

t = int(input())
depart = []
for _ in range(int(input())):
	depart.append([int(input()), int(input()), 0])
for _ in range(int(input())):
	depart.append([int(input()), int(input()), 1])
heapify(depart)
train = [[], []]
while depart:
	dep, arr, k = heappop(depart)
	if not train[k] or train[k][0] > dep:
		heappush(train[1-k], arr + t)
	else:
		heappop(train[k])
		heappush(train[1-k], arr + t)
print(len(train[0]) + len(train[1]))
