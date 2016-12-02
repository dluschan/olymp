n, subtask = input().split()
n = int(n)

corp = [int(s) for s in input().split()]
tax = sum([a**2 for a in corp])
print(tax)

events = int(input())
for i in range(events):
    evtype, corpnum = input().split()
    evtype = int(evtype)
    corpnum = int(corpnum)
    tax -= corp[corpnum-1]**2
    if evtype == 1:
        free = corp.pop(corpnum-1)
        if corpnum == 1:
            tax -= corp[0]**2
            corp[0] += free
            tax += corp[0]**2
        elif corpnum == len(corp) + 1:
            tax -= corp[len(corp)-1]**2
            corp[len(corp)-1] += free
            tax += corp[len(corp)-1]**2
        else:
            tax -= corp[corpnum-2]**2 + corp[corpnum-1]**2
            corp[corpnum-2] += free // 2
            corp[corpnum-1] += (free + 1) // 2
            tax += (free // 2)**2 + ((free + 1) // 2)**2
    if evtype == 2:
        free = corp.pop(corpnum-1)
        tax -= corp[corpnum-1]**2
        corp[corpnum-1] = free // 2
        corp.insert(corpnum, (free + 1) // 2)
        tax += corp[corpnum-1]**2 + corp[corpnum]**2
    print(tax)
