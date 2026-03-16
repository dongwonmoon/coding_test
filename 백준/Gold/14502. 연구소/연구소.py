import sys
from itertools import combinations
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())

board = []
empty = []
virus = []

for y in range(N):
    row = list(map(int, input().split()))
    board.append(row)

    for x, value in enumerate(row):
        if value == 0:
            empty.append((y, x))
        elif value == 2:
            virus.append((y, x))

empty_count = len(empty)
answer = 0
dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

for walls in combinations(empty, 3):
    for y, x in walls:
        board[y][x] = 1

    q = deque(virus)
    infected = []
    infected_count = 0

    while q:
        y, x = q.popleft()

        for dy, dx in dirs:
            ny, nx = y + dy, x + dx
            if 0 <= ny < N and 0 <= nx < M and board[ny][nx] == 0:
                board[ny][nx] = 2
                infected.append((ny, nx))
                infected_count += 1
                q.append((ny, nx))

    safe_area = empty_count - 3 - infected_count
    answer = max(answer, safe_area)

    for y, x in infected:
        board[y][x] = 0
    for y, x in walls:
        board[y][x] = 0

print(answer)
