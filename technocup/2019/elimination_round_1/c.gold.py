def check(s, k):
    if len(s) == 0:
        return True
    for i in range(len(s)):
        if sum(s[:i+1]) == k:
            return check(s[i+1:], k)
        elif sum(s[:i+1]) > k:
            return False
    return False

def fit(s):
    p = sum(s)
    for i in range(len(s) - 1):
        b = sum(s[:i+1])
        if p % b == 0 and check(s[i+1:], b):
            return True
    return False

input()
s = [int(t) for t in input() if t != '0']
print('YES' if len(s) == 0 or fit(s) else 'NO')
