
import sys
import heapq

input = sys.stdin.readline
INF = 10**18

N, M, K, X = map(int, input().split())
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)

dist = [INF] * (N + 1)
dist[X] = 0

pq = [(0, X)]

while pq:
    d, u = heapq.heappop(pq)

    if d != dist[u]:
        continue
    if d > K:
        break

    for v in graph[u]:
        nd = d + 1
        if nd < dist[v] and nd <= K:
            dist[v] = nd
            heapq.heappush(pq, (nd, v))

ans = [i for i in range(1, N + 1) if dist[i] == K]
if not ans:
    print(-1)
else:
    ans.sort()
    print("\n".join(map(str, ans)))