import sys
import heapq

input = sys.stdin.readline
INF = 10**18

N, M, X = map(int, input().split())

graph_1 = [[] for _ in range(N + 1)]  # 뒤집은 거. i -> X
graph_2 = [[] for _ in range(N + 1)]  # 안 뒤집은거. X -> i
for _ in range(M):
    u, v, w = map(int, input().split())
    graph_1[v].append((u, w))
    graph_2[u].append((v, w))

dist_1 = [INF] * (N + 1)
dist_2 = [INF] * (N + 1)

pq_1 = [(0, X)]
dist_1[X] = 0
while pq_1:
    d, u = heapq.heappop(pq_1)

    if d != dist_1[u]:
        continue

    for v, w in graph_1[u]:
        nd = d + w
        if nd < dist_1[v]:
            dist_1[v] = nd
            heapq.heappush(pq_1, (nd, v))

pq_2 = [(0, X)]
dist_2[X] = 0
while pq_2:
    d, u = heapq.heappop(pq_2)

    if d != dist_2[u]:
        continue

    for v, w in graph_2[u]:
        nd = d + w
        if nd < dist_2[v]:
            dist_2[v] = nd
            heapq.heappush(pq_2, (nd, v))

print(max([a + b for a, b in zip(dist_1[1:], dist_2[1:])]))