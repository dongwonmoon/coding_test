import sys

input = sys.stdin.readline

N, K = map(int, input().split())

items = []
for _ in range(N):
    items.append(tuple(map(int, input().split())))

dp = [0] * (K + 1)

for weight, value in items:
    for i in range(K, weight - 1, -1):
        if i >= weight:
            dp[i] = max(dp[i], dp[i - weight] + value)

print(dp[-1])