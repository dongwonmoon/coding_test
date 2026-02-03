import sys
from collections import deque

input = sys.stdin.readline

N = int(input())

deq = deque([i for i in range(1, N + 1)])
i = 1
while len(deq) > 1:
    if i % 2 == 0:
        deq.append(deq.popleft())
    else:
        deq.popleft()
    i += 1

print(deq[0])