import sys

input = sys.stdin.readline

K = int(input())

q = []
for _ in range(K):
    inp = int(input())
    if inp == 0:
        q.pop()
    else:
        q.append(inp)

print(sum(q))