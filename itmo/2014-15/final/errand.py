def subordinate(n, personal):
    res = 1
    for i in range(len(personal)):
        if personal[i] == n:
            res += subordinate(i + 2, personal)
    return res

input()
worker = [int(x) for x in input().split()]
x = int(input())
print(subordinate(x, worker))
