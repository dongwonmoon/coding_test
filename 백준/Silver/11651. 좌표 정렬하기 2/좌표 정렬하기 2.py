import sys

input = sys.stdin.readline
N = int(input())

points = []
for _ in range(N):
    x, y = map(int, input().split())
    points.append([x, y])

sorted_points = sorted(points, key=lambda point: (point[1], point[0]))

for point in sorted_points:
    print(point[0], point[1])
