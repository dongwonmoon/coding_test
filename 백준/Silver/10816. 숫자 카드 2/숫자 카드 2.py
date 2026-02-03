import sys

input = sys.stdin.readline

input()

cards = input().split()
card_count = dict()
for i in cards:
    card_count[i] = card_count.get(i, 0) + 1

input()

answer = []
for i in input().split():
    answer.append(card_count.get(i, 0))

print(*answer)