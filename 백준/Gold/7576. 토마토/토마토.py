import sys
from collections import deque

input = sys.stdin.readline

M, N = map(int, input().split())
box = [list(map(int, input().split())) for _ in range(N)]

q = deque()
for y in range(N):
    for x in range(M):
        if box[y][x] == 1:
            q.append((y, x))

dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

while q:
    y, x = q.popleft()
    for dx, dy in dirs:
        ny, nx = y + dy, x + dx
        if 0 <= ny < N and 0 <= nx < M and box[ny][nx] == 0:
            box[ny][nx] = box[y][x] + 1
            q.append((ny, nx))

max_day = 1
for row in box:
    if 0 in row:
        print(-1)
        sys.exit()
    max_day = max(max_day, max(row))

print(max_day - 1)