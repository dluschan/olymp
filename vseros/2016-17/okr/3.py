#решение задачи с помощью интерпретирования пар как 26-ричных чисел

s1 = input()
g1 = [0 for i in range(26**2)]
s2 = input()
g2 = set()
for i in range(len(s1) - 1):
    g1[26 * (int(s1[i], 36) - int('A', 36)) + (int(s1[i+1], 36) - int('A', 36))] += 1
for i in range(len(s2) - 1):
    g2.add(26 * (int(s2[i], 36) - int('A', 36)) + (int(s2[i+1], 36) - int('A', 36)))
sum = 0
for i in range(26**2):
    if i in g2:
        sum += g1[i]
print(sum)
