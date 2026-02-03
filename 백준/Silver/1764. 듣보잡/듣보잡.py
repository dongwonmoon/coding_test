import sys

input = sys.stdin.readline

N, M = input().split()
N, M = int(N), int(M)

l = set()
s = set()
for _ in range(N):
    l.add(input().strip())

for _ in range(M):
    s.add(input().strip())

l_s = sorted(list(l.intersection(s)))

print(len(l_s))
for i in l_s:
    print(i)