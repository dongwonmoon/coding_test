import sys
from collections import defaultdict
import heapq

input = sys.stdin.readline

V, E = map(int, input().split())

start = int(input())
dist = [float("inf")] * (V + 1)
dist[start] = 0

network = defaultdict(list)
weights = {}

for _ in range(E):
    u, v, w = map(int, input().split())
    network[u].append(v)
    w_ = weights.get((u, v), float("inf"))
    weights[(u, v)] = w if w < w_ else w_

pq = [(0, start)]

while pq:
    d, u = heapq.heappop(pq)

    if d != dist[u]:
        continue

    for v in network[u]:
        nd = weights.get((u, v), None) + d
        if nd and nd < dist[v]:
            dist[v] = nd
            heapq.heappush(pq, (nd, v))

for d in dist[1:]:
    if d == float("inf"):
        print("INF")
    else:
        print(d)