import sys

N = int(input())

d = dict()

for _ in range(N):
    w = sys.stdin.readline().strip()
    d[w] = len(w)

print("\n".join(sorted(list(d.keys()), key=lambda x: (d[x], x))))
