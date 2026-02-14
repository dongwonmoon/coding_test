import sys
from collections import defaultdict

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N, M = map(int, input().split())
networks = defaultdict(list)
visited = [False] * (N + 1)

for _ in range(M):
    u, v = map(int, input().split())
    networks[u].append(v)
    networks[v].append(u)


def dfs(c):
    visited[c] = True
    for nc in networks[c]:
        if not visited[nc]:
            dfs(nc)


count = 0
for c in range(1, N + 1):
    if not visited[c]:
        dfs(c)
        count += 1

print(count)