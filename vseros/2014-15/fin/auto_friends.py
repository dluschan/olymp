def artful():
    a = [[0 for x in range(100)], 1]
    b = [[0 for x in range(100)], 1]
    c = [[0 for x in range(100)], 1]
    ab = [[0 for x in range(10000)], -2]
    bc = [[0 for x in range(10000)], -2]
    ac = [[0 for x in range(10000)], -2]
    abc = [[0 for x in range(1000000)], 3]
    for i in range(int(input())):
        q, w, e = map(int, input().split())
        a[0][q - 1] += 1
        b[0][w - 1] += 1
        c[0][e - 1] += 1
        ab[0][100 * (q - 1) + (w - 1)] += 1
        bc[0][100 * (w - 1) + (e - 1)] += 1
        ac[0][100 * (q - 1) + (e - 1)] += 1
        abc[0][10000 * (q - 1) + 100 * (w - 1) + (e - 1)] += 1
    couples = 0
    for records, k in [a, b, c, ab, bc, ac, abc]:
        for value in records:
            if value > 1:
                couples += k * value * (value - 1) // 2
    return couples

def clumsy():
    n = int(input())
    x = []
    couples = 0
    for i in range(n):
        x.append([int(r) for r in input().split()])
    for i in range(n):
        for j in range(i + 1, n):
            t = 0
            for k in range(3):
                if x[i][k] == x[j][k]:
                    t += 1
            if t == 1:
                couples += 1
    return couples

print(artful())
