import sys

N, M = map(int, input().split())

nums = list(range(1, N + 1))
visited = [0] * N


def build(path, state):
    if len(path) == M:
        sys.stdout.write(" ".join(map(str, path)) + "\n")
        return

    for i in range(N):
        if state[i] == 0:
            state[i] = 1
            path.append(nums[i])
            build(path, state)
            path.pop()
            state[i] = 0


build([], visited)