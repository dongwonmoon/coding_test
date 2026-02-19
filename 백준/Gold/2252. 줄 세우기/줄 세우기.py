import sys

input = sys.stdin.readline

N, M = map(int, input().split())

graph = [[] for _ in range(N + 1)]
rank = {i: 0 for i in range(1, N + 1)}

for _ in range(M):
    l, r = map(int, input().split())
    graph[l].append(r)
    rank[r] += 1

answer = []
stack = [l for l, v in rank.items() if v == 0]
while stack:
    l = stack.pop()
    answer.append(l)

    for r in graph[l]:
        rank[r] -= 1
        if rank[r] == 0:
            stack.append(r)

print(*answer)
