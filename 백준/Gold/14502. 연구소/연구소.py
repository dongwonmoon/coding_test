import sys
from itertools import combinations
from copy import deepcopy
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())

board = []
safe = []

for i in range(N):
    row = list(map(int, input().split()))

    for j, item in enumerate(row):
        if item == 0:
            safe.append((i, j))

    board.append(row)

wall_poss = combinations(safe, 3)

q_og = deque()
for y in range(N):
    for x in range(M):
        if board[y][x] == 2:
            q_og.append((y, x))

safe_count = 0
dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

for coords in wall_poss:
    temp_board = deepcopy(board)
    for coord in coords:
        i, j = coord
        temp_board[i][j] = 1

    q = q_og.copy()
    while q:
        y, x = q.popleft()
        for dx, dy in dirs:
            ny, nx = y + dy, x + dx
            if 0 <= ny < N and 0 <= nx < M and temp_board[ny][nx] == 0:
                temp_board[ny][nx] = 2
                q.append((ny, nx))

    count = 0
    for row in temp_board:
        count += row.count(0)

    if safe_count < count:
        safe_count = count

print(safe_count)