travel = {15: int(input()), 10: int(input()), 5: int(input())}
N = int(input())
print(min([(interval - N % interval) % interval + travel[interval] for interval in travel.keys()]))
