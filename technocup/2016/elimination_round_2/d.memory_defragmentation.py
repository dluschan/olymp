zero, prev, res, _ = 0, 0, 0, input()
for s in (input() + ' 0').split():
    cur = int(s)
    if cur == 0:
        if prev != cur:
            res += min(zero, mem)
        zero += 1
    else:
        if prev != cur:
            if prev:
                res += min(zero, mem)
            mem = 1
        else:
            mem += 1
    prev = cur
print(res)
