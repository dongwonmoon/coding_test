import sys
from collections import deque

input = sys.stdin.readline

N = int(input())

grid = [list(input().strip()) for _ in range(N)]
grid_green_into_red = [r[:] for r in grid]

for i in range(N):
    for j in range(N):
        if grid_green_into_red[i][j] == "G":
            grid_green_into_red[i][j] = "R"

dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
visited = [[False] * N for _ in range(N)]
visited_green_into_red = [r[:] for r in visited]


def bfs(grid, visited):
    count = 0
    for i in range(N):
        for j in range(N):
            c = grid[i][j]
            if visited[i][j]:
                continue

            q = deque()
            q.append((i, j))
            visited[i][j] = True

            while q:
                y, x = q.popleft()
                for dx, dy in dirs:
                    nx, ny = x + dx, y + dy
                    if (
                        0 <= nx < N
                        and 0 <= ny < N
                        and c == grid[ny][nx]
                        and not visited[ny][nx]
                    ):
                        q.append((ny, nx))
                        visited[ny][nx] = True

            count += 1

    return count


ans1 = bfs(grid, visited)
ans2 = bfs(grid_green_into_red, visited_green_into_red)

print(ans1, ans2)