import sys

input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
M = max(A)

dp = [0] * (M + 1)

for i in range(N):
    A_i = A[i]
    dp[A_i] = max(dp[A_i], 1 + max(dp[:A_i]))

print(max(dp))