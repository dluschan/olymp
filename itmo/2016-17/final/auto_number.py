normal_num = set()
source_num = []

for i in range(int(input())):
    number = input()
    source_num.append(number)
    if number.find('??') == -1:
        if number in normal_num:
            print("NO")
            exit(0)
        else:
            normal_num.add(number)

for k in range(len(source_num)):
    if source_num[k].find('??') != -1:
        inserted = False
        for i in range(10):
            for j in range(10):
                if not inserted:
                    fixed = source_num[k][0:4] + str(i) + str(j) + source_num[k][6:7]
                    if fixed not in normal_num:
                        normal_num.add(fixed)
                        inserted = True
                        source_num[k] = fixed
        if not inserted:
            print("NO")
            exit(0)

print("Yes")
for num in source_num:
    print(num)
