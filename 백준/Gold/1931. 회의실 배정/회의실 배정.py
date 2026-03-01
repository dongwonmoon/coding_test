import sys

input = sys.stdin.readline

N = int(input())

meetings = []

for _ in range(N):
    s, e = map(int, input().split())
    meetings.append((s, e))

meetings.sort()

stack = [meetings[0]]

for s, e in meetings[1:]:
    ps, pe = stack[-1]
    if s < pe and e > pe:
        continue

    if e < pe:
        stack[-1] = (s, e)
        continue

    if s >= pe:
        stack.append((s, e))

print(len(stack))