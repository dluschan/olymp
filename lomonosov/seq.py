n = 200
a = [0 for i in range(n)]
a[0] = 0
a[1] = 1
a[2] = 1
for i in range(n-3):
    a[i+3] = 2*a[i] - a[i+1] + a[i+2]

s = ""
for x in a:
    s += str(x)

print(s[123:178])
