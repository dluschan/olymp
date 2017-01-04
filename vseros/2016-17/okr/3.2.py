s1 = input()
s2 = input()
sum = 0
for i in range(len(s1) - 1):
    if s1[i: i+2] in s2:
        sum += 1
print(sum)