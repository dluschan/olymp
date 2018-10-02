n = int(input())
s = input()

prev_x = ''
prev_y = ''
k = 1
for c in s:
    if c in ['R', 'L']:
        if c == 'R' and prev_x == 'L' or c == 'L' and prev_x == 'R':
            k += 1
            prev_x = c
            prev_y = ''
        else:
            prev_x = c
    if c in ['U', 'D']:
        if c == 'U' and prev_y == 'D' or c == 'D' and prev_y == 'U':
            k += 1
            prev_x = ''
            prev_y = c
        else:
            prev_y = c
print(k)
