def f(s, depth, ambiguity, a, b):
    if ambiguity == 0:
        s[a] = '('
        s[b] = ')'
        while depth > 0:
            depth -= 1
            a -= 1
            b += 1
            s[a] = '('
            s[b] = ')'
        return s
    print('?', a, b)
    if input().lower() in ['n', 'no']:
        return f(s, depth + 1, ambiguity - 1, a + 1, b + 1)
    else:
        s[a] = '('
        s[b] = ')'
        if depth == 0:
            a = b + 1
            b = a + 1
            return f(s, depth, ambiguity - 1, a, b)
        else:
            a = a - 1
            b = b + 1
            return f(s, depth - 1, ambiguity - 1, a, b)

n = int(input())
print('!', ''.join(f([' '] * n, 0, n // 2 - 1, 0, 1)))
