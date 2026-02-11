N, M = map(int, input().split())

nums = list(range(1, N + 1))
visited = [0] * N
s = set()


def build(path, state):
    p = tuple(sorted(path))
    if len(path) == M and p not in s:
        s.add(p)
        print(*path)
        return

    for i in range(N):
        if state[i] == 0:
            state[i] = 1
            path.append(nums[i])
            build(path, state)
            path.pop()
            state[i] = 0


build([], visited)