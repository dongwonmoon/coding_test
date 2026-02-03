import sys

input = sys.stdin.readline

N = int(input())

q = []
for _ in range(N):
    inp = input().split()
    if len(inp) == 2:
        command, num = inp
        num = int(num)
    else:
        command = inp[0]

    if command == "push":
        q.append(num)
    elif command == "pop":
        print(q.pop(0) if q else -1)
    elif command == "size":
        print(len(q))
    elif command == "empty":
        print(0 if q else 1)
    elif command == "front":
        print(q[0] if q else -1)
    elif command == "back":
        print(q[-1] if q else -1)