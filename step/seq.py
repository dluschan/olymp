n = 1
summ = 0
summmax = 0
length = 0
lengthmax = 0
while n!= 0:
    n = int(input())
    if n % 2 == 0 and n % 10 != 0:
        summ += n
        length +=1
    else:
        if lengthmax < length:
            lengthmax = length
            summmax = summ
        summ = 0
        length = 0
print(summmax)