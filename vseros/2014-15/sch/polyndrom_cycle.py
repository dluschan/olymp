n = 10000982
digits = 0
while n > 0:
    n -= 9 * 10**(digits // 2)
    digits += 1
    
base = 10**(digits//2) + n + 9 * 10**((digits-1) // 2) - 1
copy = base // 10**(digits % 2)
while copy:
    base = 10*base + copy % 10
    copy /= 10
    
print(base)
