x = []
x.append(int(input()))
x.append(int(input()))
x.append(int(input()))
m = int(input())

intervals = [15, 10, 5]
a = [x[i] + (intervals[i] - m % intervals[i] if m % intervals[i] > 0 else 0) for i in range(3)]

print(min(a))
