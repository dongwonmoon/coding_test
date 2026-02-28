import sys
from collections import deque

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N, K = map(int, input().split())
    weight = [0]
    weight += list(map(int, input().split()))
    graph = [[] for _ in range(N + 1)]
    indegree = [0] * (N + 1)

    for _ in range(K):
        u, v = map(int, input().split())
        graph[u].append(v)
        indegree[v] += 1

    target = int(input())

    que = deque()
    start = []
    for i, v in enumerate(indegree):
        if v == 0:
            start.append(i)
    que.extend(start)
    dist = weight.copy()

    while que:
        u = que.popleft()
        for v in graph[u]:
            indegree[v] -= 1
            dist[v] = max(dist[v], dist[u] + weight[v])
            if indegree[v] == 0:
                que.append(v)

    print(dist[target])