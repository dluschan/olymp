n, k = map(int, input().split())
single_poly = {}
pair_poly = {}

for i in range(n):
    s, beaty = input().split()
    beaty = int(beaty)
    if s != s[::-1]:
        key = min(s, s[::-1]) + max(s, s[::-1])
        if key in pair_poly:
            if s in pair_poly[key]:
                pair_poly[key][s].append(beaty)
            else:
                pair_poly[key][s] = [beaty]
        else:
            pair_poly[key] = {s : [beaty]}
    else:
        if s in single_poly:
            single_poly[s].append(beaty)
        else:
            single_poly[s] = [beaty]
for pair in pair_poly:
    while 
    
print(single_poly)
print(pair_poly)

#pair_poly : {'abbbba': {'abb' : [2, 5], 'bba' : [-1]}}
