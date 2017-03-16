letters = {}

for c in input():
    if c in letters:
        letters[c] += 1
    else:
        letters[c] = 1

max_double = max(letters.values())
if max_double == 1:
    print(len(letters))
    for l in letters:
        print(l)
    exit(0)

if list(letters.values()).count(max_double) == 1:
    print(1)
    for l, k in letters.items():
        print(l*k, end='')
    print()
    exit(0)

ans1 = ""
found_first = False
ans2 = ""
found_second = False
for l, k in letters.items():
    if k == max_double and not found_first:
        ans1 += l*k
        found_first = True
        continue
    if k == max_double and found_first and not found_second:
        ans2 += l*k
        found_second = True
        continue
    if k == max_double and found_first and found_second:
        ans1 += l
        ans2 += l*(k-1)
        continue
    if k != max_double:
        ans1 += l*k
print(2)
print(ans1)
print(ans2)
