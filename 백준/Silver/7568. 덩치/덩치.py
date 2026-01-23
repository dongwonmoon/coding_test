import sys

input = sys.stdin.readline

N = int(input())

people = []
for i in range(N):
    weight, height = map(int, input().split())
    people.append((weight, height, i))

people.sort(key=lambda x: (-x[0], -x[1]))

answer = [1] * len(people)
for idx, (weight, height, order) in enumerate(people):
    for weight_, height_, _ in people[:idx]:
        if weight_ > weight and height_ > height:
            answer[order] += 1

print(*answer)
