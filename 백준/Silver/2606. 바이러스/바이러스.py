import sys
from collections import deque, defaultdict

input = sys.stdin.readline

C = int(input())
N = int(input())

network = defaultdict(list)
for _ in range(N):
    l, r = map(int, input().split())
    network[l].append(r)
    network[r].append(l)

visited = [0] * (C + 1)
q = deque([1])
visited[1] = 1

while q:
    v = q.popleft()
    for nxt in network[v]:
        if not visited[nxt]:
            visited[nxt] = 1
            q.append(nxt)

print(sum(visited) - 1)