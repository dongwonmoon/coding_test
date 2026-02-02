import sys

input = sys.stdin.readline
N = input()

P = sorted(list(map(int, input().split(" "))))

answer = []
for i in range(len(P)):
    answer.append(sum(P[: i + 1]))

print(sum(answer))
