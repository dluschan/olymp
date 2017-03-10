a, b = map(int, input().split())
x, y, z = map(int, input().split())
h1, m1, s1 = map(int, input().split())
h2, m2, s2 = map(int, input().split())
c = input()

day = x*a*b + y*b + z
start_time = h1*a*b + m1*b + s1
finish_time = h2*a*b + m2*b + s2
need_next_day = True if start_time > finish_time else False
good_moments = 0

t = start_time
while need_next_day or not need_next_day and t != finish_time + 1:
    h = t // (a*b)
    if x > 9 and h < 10:
        h *= 10
        
    m = t % (a*b) // b
    if a > 9 and m < 10:
        m *= 10
        
    s = t % b
    if b > 9 and s < 10:
        s *= 10
    
    if (str(h) + str(m) + str(s)).find(c) != -1:
        good_moments += 1
    
    t += 1
    if t == day:
        need_next_day = False
    t %= day
print(good_moments)
