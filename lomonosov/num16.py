n = int(input())
s = input()
letterlist = ['x', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
letter = {}

for l in letterlist:
    letter[l] = 0

for i in range(n):
    if s[i:i+1] in letterlist:
        letter[s[i:i+1]] += 1

if letter['x'] > 0 and letter['0'] > 0:
    letter['0'] -= 1
    del letter['x']
    del letterlist[0]
    res = '0x'
    if any(c > 0 for c in letter.values()):
        letterlist.reverse()
        for l in letterlist:
            res += l*letter[l]
    print(res)
else:
    print('No')
