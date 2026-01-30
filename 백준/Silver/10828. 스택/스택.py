import sys

input = sys.stdin.readline

N = int(input())
stack = []

for _ in range(N):
    s = input().strip()
    if "push" in s:
        stack.append(int(s[5:]))
    elif "top" in s:
        if stack:
            print(stack[-1])
        else:
            print(-1)
    elif "size" in s:
        print(len(stack))
    elif "empty" in s:
        if stack:
            print(0)
        else:
            print(1)
    elif "pop" in s:
        if stack:
            print(stack.pop())
        else:
            print(-1)
