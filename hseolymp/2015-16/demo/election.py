n, m = map(int, input().split())
voices = [0 for i in range(n)]
for i in range(m):
    b = input()
    if b.count('+') == 1:
        voices[b.index('+')] += 1
sum_voices = sum(voices)
for i in range(n):
    if 100 * voices[i] >= 7 * sum_voices:
        print(i+1, end=' ')
print()
