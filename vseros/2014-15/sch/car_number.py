masklist = {'xyyyxx': 1, 'xxyyy': 2, 'xxyyyy': 3, 'yyyyxx': 4}
for i in range(3):
    mask = ''
    for c in input():
        if 'A' <= c and c <= 'Z':
            mask += 'x'
        elif c.isdigit():
            mask += 'y'
        else:
            mask += 'z'
    print(masklist[mask] if mask in masklist else 0)
