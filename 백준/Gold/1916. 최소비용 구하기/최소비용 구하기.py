import sys
from collections import defaultdict
import heapq

input = sys.stdin.readline

N = int(input())
M = int(input())
INF = 10**18

network = defaultdict(list)
weight = {}
for _ in range(M):
    u, v, w = map(int, input().split())
    network[u].append(v)
    weight[(u, v)] = w if w < weight.get((u, v), INF) else weight.get((u, v))

dist = [INF] * (N + 1)
start, end = map(int, input().split())

pq = [(0, start)]
dist[start] = 0

while pq:
    d, u = heapq.heappop(pq)
    vs = network.get(u, [])

    if d != dist[u]:
        continue

    for v in vs:
        if weight.get((u, v)) is None:
            continue
        nd = d + weight[(u, v)]
        if nd < dist[v]:
            dist[v] = nd
            heapq.heappush(pq, (nd, v))

print(dist[end])