import sys

input = sys.stdin.readline

N = int(input())
scores = [int(input()) for _ in range(N)]

if N <= 2:
    print(sum(scores))
    sys.exit()


def relax(d, key, val):
    if key not in d or d[key] < val:
        d[key] = val


frontier = {(0, 1): scores[0], (1, 1): scores[1]}
max_score = 0

while frontier:
    next_frontier = {}

    for (idx, state), score in frontier.items():
        if idx == N - 1:
            if score > max_score:
                max_score = score
            continue

        if state < 2:
            n1 = idx + 1
            if n1 <= N - 1:
                relax(next_frontier, (n1, state + 1), score + scores[n1])

        n2 = idx + 2
        if n2 <= N - 1:
            relax(next_frontier, (n2, 1), score + scores[n2])

    frontier = next_frontier

print(max_score)