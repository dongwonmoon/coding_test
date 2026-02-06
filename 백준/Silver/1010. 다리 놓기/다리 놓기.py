import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    table = {(1, j): 1 for j in range(1, M + 1)}

    for i in range(2, N + 1):
        for j in range(i, M - N + i + 1):
            table[i, j] = table.get((i - 1, j - 1), 0) + table.get((i, j - 1), 0)

    print(sum([table[N, j] for j in range(N, M + 1)]))
