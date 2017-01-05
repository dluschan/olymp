s = input()
t = input()

change = {}
res = 0
out = ''
for i in range(len(s)):
    if s[i] != t[i]:
        if s[i] in change or t[i] in change:
            if s[i] not in change or t[i] not in change or s[i] != change[t[i]] or t[i] != change[s[i]]:
                res = -1
                out = ''
                break
        else:
            change[s[i]] = t[i]
            change[t[i]] = s[i]
            res += 1
            out += s[i] + ' ' + t[i] + '\n'

print(res)
print(out, end='')
