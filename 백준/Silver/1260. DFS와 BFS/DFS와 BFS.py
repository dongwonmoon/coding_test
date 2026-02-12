import sys
from collections import deque, defaultdict

sys.setrecursionlimit(10**6)

input = sys.stdin.readline

N, M, V = map(int, input().split())
networks = defaultdict(list)

for _ in range(M):
    l, r = map(int, input().split())
    networks[l].append(r)
    networks[r].append(l)

for key in networks:
    networks[key].sort()

dfs_answers = []


def dfs(start, state):
    state[start] = True
    dfs_answers.append(start)

    for i in networks[start]:
        if not state[i]:
            dfs(i, state)


dfs(V, [False] * (N + 1))
print(*dfs_answers)

deq = deque()
deq.append(V)
visited = set()
visited.add(V)
bfs_answer = []

while deq:
    s = deq.popleft()
    bfs_answer.append(s)

    for a in networks[s]:
        if a not in visited:
            visited.add(a)
            deq.append(a)

print(*bfs_answer)
