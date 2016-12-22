n = int(input())
m = int(input())
a = int(input())
b = int(input())

lack = m - n

if lack <= 0:
    print(0)
else:
    if a <= b/4:
        print(lack*a)
    else:
        multi = lack // 4
        lack %= 4
        print(multi*b + min(a*lack, b))
