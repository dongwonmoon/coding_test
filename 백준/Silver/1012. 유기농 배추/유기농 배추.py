import sys

sys.setrecursionlimit(10**6)

input = sys.stdin.readline

T = int(input())
maps = []
for _ in range(T):
    M, N, K = map(int, input().split())
    _map = [[0] * M for _ in range(N)]
    for _ in range(K):
        X, Y = map(int, input().split())
        _map[Y][X] = 1
    maps.append(_map)

dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def dfs(coordinate, map):
    x, y = coordinate
    for dx, dy in dirs:
        nx = x + dx
        ny = y + dy

        if 0 <= nx < len(map) and 0 <= ny < len(map[0]) and map[nx][ny]:
            map[nx][ny] = 0
            dfs((nx, ny), map)


for map_ in maps:
    rows = len(map_)
    cols = len(map_[0])
    count = 0

    for i in range(rows):
        for j in range(cols):
            if map_[i][j]:
                map_[i][j] = 0
                dfs((i, j), map_)
                count += 1

    print(count)
