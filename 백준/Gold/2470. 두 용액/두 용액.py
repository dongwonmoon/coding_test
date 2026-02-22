N = int(input())
A = list(map(int, input().split()))
A.sort()

if A[0] > 0:
    print(A[0], A[1])
    exit()
if A[-1] < 0:
    print(A[-2], A[-1])
    exit()

m = float("inf")
s, e = 0, N - 1
ans = [0, 0]

while s < e:
    ss = A[s] + A[e]

    if abs(ss) < m:
        m = abs(ss)
        ans[0] = A[s]
        ans[1] = A[e]

        if m == 0:
            print(A[s], A[e])
            exit()

    if ss > 0:
        e -= 1
    else:
        s += 1

print(*ans)
