import sys

input = sys.stdin.readline

N = int(input())
nums = [int(input()) for _ in range(N)]

answer = []
stack = []
cur = 1
idx = 0

while idx < N:
    while cur <= N and (not stack or stack[-1] < nums[idx]):
        stack.append(cur)
        answer.append("+")
        cur += 1

    if stack and stack[-1] == nums[idx]:
        stack.pop()
        answer.append("-")
        idx += 1
    else:
        print("NO")
        exit()

print("\n".join(answer))