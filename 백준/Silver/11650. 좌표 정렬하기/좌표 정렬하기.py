import sys

N = int(input())

coordinates = []
for _ in range(N):
    coordinates.append(list(map(int, sys.stdin.readline().split())))

c = sorted(coordinates, key=lambda x: (x[0], x[1]))
c = [f"{x} {y}" for x, y in c]

print("\n".join(c))
