import copy
n = int(input())
enter = []
exit = []
uniqenter = set()
for i in range (n):
    a , b = map(int,input().split())
    if b - a >= 5:
        enter.append(a)
        exit.append(b)
        uniqenter.add(a)
maxsum = 0
arrivetimebest1 = 0
arrivetiemostbest2 = 5
for arrivetime in uniqenter:
    watched = set()
    for j in range(len(enter)):
        if enter[j] <= arrivetime and exit[j] >= arrivetime + 5:
                watched.add(j)
    arrivetimebest2 = arrivetime + 5
    max2 = 0
    uniqenter2 = copy.deepcopy(uniqenter)
    uniqenter2.add(arrivetime + 5)
    for arrivetime2 in uniqenter2:
        watched2 = set()
        for j in range(len(enter)):
            if enter[j] <= arrivetime2 and exit[j] >= arrivetime2 + 5 and j not in watched and abs(arrivetime2 - arrivetime) >= 5:
                watched2.add(j)
        if max2 < len(watched2):
            max2 = len(watched2)
            arrivetimebest2 = arrivetime2
    if maxsum < len(watched) + max2:
        maxsum = len(watched) + max2
        arrivetimebest1 = arrivetime
        arrivetimemostbest2 = arrivetimebest2
print(maxsum, arrivetimebest1, arrivetimemostbest2)
