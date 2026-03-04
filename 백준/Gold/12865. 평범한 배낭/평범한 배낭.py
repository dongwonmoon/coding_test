import sys

input = sys.stdin.readline

N, K = map(int, input().split())

items = []
for _ in range(N):
    items.append(tuple(map(int, input().split())))

dp = [[0] * N for _ in range(K + 1)]

for i in range(1, K + 1):
    if i >= items[0][0]:
        dp[i][0] = items[0][1]

for i in range(1, K + 1):
    for j in range(1, N):
        dp[i][j] = dp[i][j - 1]
        if i >= items[j][0]:
            dp[i][j] = max(dp[i][j], dp[i - items[j][0]][j - 1] + items[j][1])

print(max(dp[-1]))