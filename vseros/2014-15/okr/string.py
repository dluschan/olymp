def erase(s, i):
    return s.replace(s[0:i+1], s[0:i], 1)
    
def middle(a, b, c):
    return a + b + c - min(a, b, c) - max(a, b, c)

s = [[input(), []] for i in range(3)]
for pair in s:
    i = 1
    pair[1].append(1)
    while i < len(pair[0]):
        if pair[0][i-1] == pair[0][i]:
            pair[0] = erase(pair[0], i)
            pair[1][i-1] += 1
        else:
            i += 1
            pair[1].append(1)
if s[0][0] == s[1][0] and s[1][0] == s[2][0]:
    for i in range(len(s[0][0])):
        print(s[0][0][i] * middle(s[0][1][i], s[1][1][i], s[2][1][i]), end='')
    print()
else:
    print('IMPOSSIBLE')
