n = 1
max = 0
t = 0
while n!=0:
    n = abs(int(input()));
    if n > 9 and n < 100:
        t += 1
    else:
        if t > max :
            max = t
        t = 0
print(max)
         