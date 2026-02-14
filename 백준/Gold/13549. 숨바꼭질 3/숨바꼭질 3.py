import heapq

N, K = map(int, input().split())
if N == K:
    print(0)
    exit()
if K < N:
    print(N - K)
    exit()

INF = 10**18

limit = 2 * K + 1
dist = [INF] * limit
dist[N] = 0

pq = [(0, N)]

while pq:
    d, u = heapq.heappop(pq)

    if d != dist[u]:  # 최소 보장
        continue
    if u == K:
        print(d)
        break

    for nd, v in ((d + 1, u - 1), (d + 1, u + 1), (d, 2 * u)):
        if 0 <= v < limit and nd < dist[v]:
            dist[v] = nd
            heapq.heappush(pq, (nd, v))