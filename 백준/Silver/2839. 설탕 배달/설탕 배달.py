import sys

input = sys.stdin.readline

N = int(input())
FLAG = False
for i in range(N // 5, 0, -1):
    if (N - (5 * i)) % 3 == 0:
        FLAG = True
        print(i + (N - (5 * i)) // 3)
        break

if FLAG:
    pass
else:
    if N % 3 == 0:
        print(N // 3)
    else:
        print(-1)
