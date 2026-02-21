import sys
import heapq

input = sys.stdin.readline

N, E = map(int, input().split())
INF = 10**18

graph = [[] for _ in range(N + 1)]
for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
    graph[v].append((u, w))

v1, v2 = map(int, input().split())

dist_1 = [INF] * (N + 1)
dist_v1 = [INF] * (N + 1)
dist_v2 = [INF] * (N + 1)

for start, dist in ((1, dist_1), (v1, dist_v1), (v2, dist_v2)):
    pq = [(0, start)]
    dist[start] = 0

    while pq:
        d, u = heapq.heappop(pq)

        if d != dist[u]:
            continue

        for v, w in graph[u]:
            nd = d + w
            if nd < dist[v]:
                dist[v] = nd
                heapq.heappush(pq, (nd, v))

v1_v2 = dist_1[v1] + dist_v1[v2] + dist_v2[N]
v2_v1 = dist_1[v2] + dist_v2[v1] + dist_v1[N]
ans = min(v1_v2, v2_v1)
print(ans if ans < INF else -1)