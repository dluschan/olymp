max = 0
name = "аномалий нет"
for step in range(int(input())):
    ano = 0
    sen = input().split()
    name_cur = sen[0]
    del sen[0]
    sen = [int(x) for x in sen]
    avg = sum(sen) / len(sen)
    for i in sen:
        if abs(i - avg) > 10:
            ano += 1
    if max < ano:
        max = ano
        name = name_cur
print(name)
