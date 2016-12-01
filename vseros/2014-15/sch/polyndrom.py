import math

#n = int(input())
n = 100
pair = int(math.log((n + 1) / 2, 10)) + 1
numdigits = pair*2 - 1

leftnumbers = 2 * (10**(pair - 1) - 1)
if leftnumbers + 9 * (10**(numdigits//2)) < n:
    leftnumbers += 9 * (10**(numdigits//2))
    numdigits += 1

base = 10**((numdigits - 1) // 2) + n - leftnumbers - 1
copy = base // 10**(numdigits % 2)
while copy:
    base = 10*base + copy % 10
    copy /= 10
    
print(base)
