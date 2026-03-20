import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
board = [list(map(int, input().strip())) for _ in range(N)]

dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
visited = [[[False] * 2 for _ in range(M)] for _ in range(N)]

q = deque([(0, 0, 1, 0)])
visited[0][0][0] = True

while q:
    y, x, dist, broke = q.popleft()

    if y == N - 1 and x == M - 1:
        print(dist)
        break

    for dx, dy in dirs:
        nx, ny = x + dx, y + dy

        if not (0 <= nx < M and 0 <= ny < N):
            continue

        if board[ny][nx] == 1 and broke == 1:
            continue

        next_broke = broke + board[ny][nx]

        if visited[ny][nx][next_broke]:
            continue

        visited[ny][nx][next_broke] = True
        q.append((ny, nx, dist + 1, next_broke))
else:
    print(-1)