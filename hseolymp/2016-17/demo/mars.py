import math
n = int(input())

factory = 1
days = 0

without_fact = int(round(0.5 + (factory + math.sqrt(factory**2 + 8*n*factory)) / (2*factory)))
with_fact = int(round(0.5 + (2*factory + math.sqrt((2*factory)**2 + 8*n*2*factory)) / (2*2*factory))) + 1

while with_fact < without_fact:
    factory *= 2
    days += 1
    without_fact = int(round(0.5 + (factory + math.sqrt(factory**2 + 8*n*factory)) / (2*factory)))
    with_fact = int(round(0.5 + (2*factory + math.sqrt((2*factory)**2 + 8*n*2*factory)) / (2*2*factory))) + 1

days += int(round(0.5 + (factory + math.sqrt(factory**2 + 8*n*factory)) / (2*factory)))
print(days)
