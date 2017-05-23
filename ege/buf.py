buf = []
n = int(input())

for i in range(6):
    buf.append(int(input()))

l = None
res = None
for i in range(6, n):
    if buf[i % 6] % 2 != 0 and (l == None or buf[i % 6] < l):
        l = buf[i % 6]
    
    buf[i % 6] = int(input())
    
    if l != None and buf[i % 6] % 2 != 0 and (res == None or l * buf[i % 6] < res):
        res = l * buf[i % 6]

print(res if res != None else -1)