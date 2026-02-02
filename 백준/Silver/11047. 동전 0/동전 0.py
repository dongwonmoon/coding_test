import sys

input = sys.stdin.readline

N, K = map(int, input().split(" "))

coins = sorted([int(input()) for _ in range(N)], reverse=True)

answer = 0
for coin in coins:
    answer += K // coin
    K %= coin

print(answer)