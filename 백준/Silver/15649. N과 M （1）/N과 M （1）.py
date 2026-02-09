from itertools import permutations

N, M = map(int, input().split())
for t in sorted(list(permutations(range(1, N + 1), M))):
    print(*t)