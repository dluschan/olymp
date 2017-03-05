import math
for i in range(1, 100):
    print(i, math.ceil(math.log(i*10000000+2563218)/math.log(2)) - math.ceil(math.log(i*256*32*18)/math.log(2)))
