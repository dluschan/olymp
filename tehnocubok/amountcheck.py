s = input()
s += 'a'
sum = 0
price = 0
digitafterdot = -1

for c in s:
    if c.isdigit():
        price = price * 10 + int(c)
        if digitafterdot >= 0:
            digitafterdot += 1
    if c == '.':
        digitafterdot = 0
    if c.isalpha():
        sum += price * (100 if digitafterdot != 2 else 1)
        price = 0
        digitafterdot = -1

rub = sum // 100
cent = sum % 100
res = []
while rub:
    res.append(str(rub % 1000))
    rub //= 1000

if len(res) == 0:
    res.append('0')
else:
    res.reverse()
    
if cent:
    res.append(str(cent).zfill(2))

print('.'.join(res))
