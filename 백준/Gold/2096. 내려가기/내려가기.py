import sys

input = sys.stdin.readline

N = int(input())

max_dp = list(map(int, input().split()))
min_dp = max_dp.copy()

for i in range(1, N):
    p_max = max_dp.copy()
    p_min = min_dp.copy()
    n = list(map(int, input().split()))
    for p_s, j in ((p_max[:2], 0), (p_max, 1), (p_max[1:], 2)):
        max_dp[j] = max(p_s) + n[j]
    for p_s, j in ((p_min[:2], 0), (p_min, 1), (p_min[1:], 2)):
        min_dp[j] = min(p_s) + n[j]

print(max(max_dp), min(min_dp))