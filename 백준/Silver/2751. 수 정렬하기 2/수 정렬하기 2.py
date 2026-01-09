import sys

N = int(sys.stdin.readline().rstrip())

l = list()
for _ in range(N):
    l.append(int(sys.stdin.readline().rstrip()))

l.sort()
print("\n".join(map(str, l)))
