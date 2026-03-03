import sys

sys.setrecursionlimit(10**7)

N = int(sys.stdin.readline())

cols = [False] * N
diag1 = [False] * (2 * N - 1)
diag2 = [False] * (2 * N - 1)


def dfs(r: int) -> int:
    if r == N:
        return 1

    cnt = 0
    for c in range(N):
        d1 = r + c
        d2 = r - c + (N - 1)
        if cols[c] or diag1[d1] or diag2[d2]:
            continue

        cols[c] = diag1[d1] = diag2[d2] = True
        cnt += dfs(r + 1)
        cols[c] = diag1[d1] = diag2[d2] = False

    return cnt


print(dfs(0))