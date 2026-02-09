import sys

input = sys.stdin.readline

N, M = map(int, input().split())

board = [input().strip() for _ in range(N)]
board = [[1 if piece == "W" else 0 for piece in row] for row in board]
W = [1, 0, 1, 0, 1, 0, 1, 0]
B = [0, 1, 0, 1, 0, 1, 0, 1]
WB = [W, B] * 4
BW = [B, W] * 4

m = float("inf")
for i in range(N - 7):
    for j in range(M - 7):
        small_board = [row[j : j + 8] for row in board[i : i + 8]]
        pieces_W = 0
        pieces_B = 0

        # 1. WB로 비교
        for k, rule in enumerate(WB):
            pieces_W += sum([abs(s - r) for s, r in zip(small_board[k], rule)])

        # 2. BW로 비교
        for k, rule in enumerate(BW):
            pieces_B += sum([abs(s - r) for s, r in zip(small_board[k], rule)])

        pieces = pieces_W if pieces_W < pieces_B else pieces_B
        m = m if m < pieces else pieces

print(m)