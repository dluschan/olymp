n = int(input())
min_odd_index = None
min_odd = None
zero_index = None
odd_count = 0

for i in range(1, n+1):
    x = int(input())
    if x == 0:
        zero_index = i
    if x % 2 != 0 and (min_odd == None or x < min_odd):
        min_odd, min_odd_index = x, i
    if x % 2 != 0:
        odd_count += 1

breaks_row = [n+1]
if odd_count % 2 != 0:
    breaks_row.append(min_odd_index)
if zero_index != None:
    breaks_row.append(zero_index)

breaks = []
b = 1
for br in sorted(breaks_row):
    breaks.append([b, br])
    b = br + 1

for i in range(len(breaks)):
    for index in range(breaks[i][0], breaks[i][1]):
        print(index, end = ' ')
print()