import sys

input = sys.stdin.readline

N, C = map(int, input().split())

x = [int(input()) for _ in range(N)]
x.sort()


def can_place(d):
    cnt = 1
    last = x[0]  # 맨 왼쪽에 한 개는 두고
    for i in range(1, N):
        if x[i] - last >= d:
            cnt += 1
            last = x[i]
            if cnt >= C:
                return True
    return False


lo, hi = 1, x[-1] - x[0]
ans = 0

while lo <= hi:
    mid = (lo + hi) // 2
    if can_place(mid):
        ans = mid
        lo = mid + 1
    else:
        hi = mid - 1

print(ans)